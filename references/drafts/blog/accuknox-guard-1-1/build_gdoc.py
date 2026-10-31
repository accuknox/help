"""Build one Google Doc with two tabs, the business post and the technical post, through the Docs API.

Blocks are inserted in reverse order at index 1 of each tab, so every style range is known at insert time.
Images come from the Drive asset folder through drive_ids.txt.
Run: python build_gdoc.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
GWS = r"D:\Atharva\Software\nodejs\npm\node_modules\@googleworkspace\cli\bin\gws.exe"
IDS = dict(l.split()[:2] for l in (HERE / "drive_ids.txt").read_text().splitlines() if l.strip())
TITLE = "AccuKnox Guard 1.1 #1 on GuardRate - Business and Technical blogs (rewrite 2026-10-21)"
NAVY = {"red": 0x11 / 255, "green": 0x20 / 255, "blue": 0x6D / 255}
BLUE = {"red": 0, "green": 0x3B / 255, "blue": 0xF6 / 255}
GREY = {"red": 0x59 / 255, "green": 0x59 / 255, "blue": 0x59 / 255}
CALLOUT_BG = {"red": 0xEE / 255, "green": 0xF2 / 255, "blue": 1.0}
CODE_BG = {"red": 0.96, "green": 0.96, "blue": 0.97}


def gws(*args, body=None, _retry=0):
    cmd = [GWS, *args]
    if body is not None:
        cmd += ["--json", json.dumps(body)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf8")
    out = r.stdout[r.stdout.find("{"):] if "{" in r.stdout else r.stdout
    try:
        d = json.loads(out)
    except Exception:
        sys.exit(f"gws failed: {r.stdout[:800]} {r.stderr[:800]}")
    if "error" in d:
        if d["error"].get("code") == 429 and _retry < 4:
            import time
            time.sleep(65)
            return gws(*args, body=body, _retry=_retry + 1)
        sys.exit(f"API error: {json.dumps(d)[:1500]}")
    return d


def batch(doc, reqs):
    chunk, size = [], 0
    for rq in reqs:
        s = len(json.dumps(rq))
        if chunk and size + s > 24000:
            gws("docs", "documents", "batchUpdate", "--params", json.dumps({"documentId": doc}), body={"requests": chunk})
            chunk, size = [], 0
        chunk.append(rq)
        size += s
    if chunk:
        gws("docs", "documents", "batchUpdate", "--params", json.dumps({"documentId": doc}), body={"requests": chunk})


# ---------- markdown parsing ----------
INLINE = re.compile(r"\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`|(?<![\w*])\*([^*]+?)\*(?![\w*])")


def inline(text):
    """Return plain text and a list of (start, end, style) spans."""
    out, spans, pos = "", [], 0
    for m in INLINE.finditer(text):
        out += text[pos:m.start()]
        s = len(out)
        if m.group(1) is not None:
            inner, sub = inline(m.group(1))
            out += inner
            spans += [(s + a, s + b, st) for a, b, st in sub]
            spans.append((s, len(out), {"bold": True}))
        elif m.group(2) is not None:
            inner, sub = inline(m.group(2))
            out += inner
            spans += [(s + a, s + b, st) for a, b, st in sub]
            spans.append((s, len(out), {"link": m.group(3)}))
        elif m.group(4) is not None:
            out += m.group(4)
            spans.append((s, len(out), {"code": True}))
        else:
            inner, sub = inline(m.group(5))
            out += inner
            spans += [(s + a, s + b, st) for a, b, st in sub]
            spans.append((s, len(out), {"italic": True}))
        pos = m.end()
    out += text[pos:]
    return out, spans


def parse(md):
    fm, body = {}, md
    if md.startswith("---"):
        _, raw, body = md.split("---", 2)
        key = None
        for line in raw.strip().splitlines():
            if re.match(r"^[a-z_]+:", line):
                key, val = line.split(":", 1)
                fm[key] = val.strip().strip('"').rstrip(">").strip()
            elif key:
                fm[key] = (fm[key] + " " + line.strip()).strip()
    blocks, lines, i = [], body.strip().splitlines(), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("```"):
            j = i + 1
            while not lines[j].startswith("```"):
                j += 1
            blocks.append(("code", "\n".join(lines[i + 1:j])))
            i = j + 1
        elif m := re.match(r"^(#{1,3}) (.*)", ln):
            blocks.append((f"h{len(m.group(1))}", m.group(2)))
            i += 1
        elif m := re.match(r"^\[?!\[([^\]]*)\]\(([^)]+)\)(?:\]\(([^)]+)\))?$", ln.strip()):
            blocks.append(("img", m.group(2), m.group(1), m.group(3)))
            i += 1
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r"-+", c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows))
        elif ln.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i][1:].strip())
                i += 1
            paras = [p.strip() for p in "\n".join(buf).split("\n\n") if p.strip()]
            for p in paras:
                blocks.append(("callout", " ".join(p.split("\n"))))
        elif re.match(r"^(- |\d+\. )", ln):
            numbered = bool(re.match(r"^\d+\. ", ln))
            items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i]))
                i += 1
            blocks.append(("list", items, numbered))
        else:
            buf = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|>|\||- |\d+\. |```|!\[|\[!)", lines[i]):
                buf.append(lines[i].strip())
                i += 1
            blocks.append(("p", " ".join(buf)))
    return fm, blocks


# ---------- request builders, every block inserted at index 1 ----------
def loc(tab, idx=1):
    return {"index": idx, "tabId": tab}


def rng(tab, a, b):
    return {"startIndex": a, "endIndex": b, "tabId": tab}


RESET = "bold,italic,underline,link,foregroundColor,backgroundColor,weightedFontFamily,fontSize"


def text_block(tab, text, spans, style="NORMAL_TEXT", extra_para=None, base_text=None):
    n = len(text) + 1
    reqs = [{"insertText": {"location": loc(tab), "text": text + "\n"}},
            {"updateParagraphStyle": {"range": rng(tab, 1, 1 + n),
                                      "paragraphStyle": {"namedStyleType": style, **(extra_para or {})},
                                      "fields": "namedStyleType,shading,borderLeft,indentStart,indentEnd,alignment"}},
            {"deleteParagraphBullets": {"range": rng(tab, 1, 1 + n)}},
            {"updateTextStyle": {"range": rng(tab, 1, 1 + n), "textStyle": base_text or {}, "fields": RESET}}]
    reqs += span_reqs(tab, spans, 1)
    return reqs


def span_reqs(tab, spans, off):
    out = []
    for a, b, st in spans:
        if b <= a:
            continue
        if "link" in st:
            ts, f = {"link": {"url": st["link"]}, "foregroundColor": {"color": {"rgbColor": BLUE}}, "underline": True}, "link,foregroundColor,underline"
        elif "code" in st:
            ts, f = {"weightedFontFamily": {"fontFamily": "Roboto Mono"}}, "weightedFontFamily"
        else:
            k = next(iter(st))
            ts, f = {k: True}, k
        out.append({"updateTextStyle": {"range": rng(tab, off + a, off + b), "textStyle": ts, "fields": f}})
    return out


def block_reqs(tab, blk):
    kind = blk[0]
    if kind in ("h1", "h2", "h3"):
        t, sp = inline(blk[1])
        return text_block(tab, t, sp, {"h1": "TITLE", "h2": "HEADING_2", "h3": "HEADING_3"}[kind])
    if kind == "p":
        t, sp = inline(blk[1])
        if t.startswith("Caption") or (blk[1].startswith("*") and blk[1].endswith("*") and not blk[1].startswith("**")):
            return text_block(tab, t, sp, base_text={"italic": True, "foregroundColor": {"color": {"rgbColor": GREY}}})
        return text_block(tab, t, sp)
    if kind == "callout":
        t, sp = inline(blk[1])
        border = {"color": {"color": {"rgbColor": BLUE}}, "width": {"magnitude": 3, "unit": "PT"},
                  "padding": {"magnitude": 8, "unit": "PT"}, "dashStyle": "SOLID"}
        para = {"shading": {"backgroundColor": {"color": {"rgbColor": CALLOUT_BG}}}, "borderLeft": border,
                "indentStart": {"magnitude": 12, "unit": "PT"}, "indentEnd": {"magnitude": 12, "unit": "PT"}}
        return text_block(tab, t, sp, extra_para=para)
    if kind == "code":
        para = {"shading": {"backgroundColor": {"color": {"rgbColor": CODE_BG}}}}
        return text_block(tab, blk[1].replace("\n", "\u000b"), [], extra_para=para,
                          base_text={"weightedFontFamily": {"fontFamily": "Roboto Mono"}, "fontSize": {"magnitude": 9, "unit": "PT"}})
    if kind == "list":
        texts, spans, off = [], [], 0
        for it in blk[1]:
            t, sp = inline(it)
            spans += [(off + a, off + b, s) for a, b, s in sp]
            texts.append(t)
            off += len(t) + 1
        full = "\n".join(texts)
        reqs = text_block(tab, full, spans)
        reqs.append({"createParagraphBullets": {"range": rng(tab, 1, 1 + len(full)),
                                                "bulletPreset": "NUMBERED_DECIMAL_ALPHA_ROMAN" if blk[2] else "BULLET_DISC_CIRCLE_SQUARE"}})
        return reqs
    if kind == "img":
        src = blk[1]
        if src.startswith("assets/"):
            uri = f"https://lh3.googleusercontent.com/d/{IDS[src.split('/', 1)[1]]}"
        else:
            uri = src
        reqs = [{"insertText": {"location": loc(tab), "text": "\n"}},
                {"updateParagraphStyle": {"range": rng(tab, 1, 2), "paragraphStyle": {"namedStyleType": "NORMAL_TEXT", "alignment": "CENTER"},
                                          "fields": "namedStyleType,alignment"}},
                {"deleteParagraphBullets": {"range": rng(tab, 1, 2)}},
                {"insertInlineImage": {"location": loc(tab), "uri": uri,
                                       "objectSize": {"width": {"magnitude": 468, "unit": "PT"}}}}]
        if blk[3]:
            reqs.append({"updateTextStyle": {"range": rng(tab, 1, 2), "textStyle": {"link": {"url": blk[3]}}, "fields": "link"}})
        return reqs
    raise ValueError(kind)


def table_reqs(doc, tab, rows, header=True):
    """Insert a table at index 1, then fill its cells in reverse order."""
    R, C = len(rows), len(rows[0])
    batch(doc, [{"insertTable": {"rows": R, "columns": C, "location": loc(tab)}}])
    T = 2
    reqs = []
    for r in range(R - 1, -1, -1):
        for c in range(C - 1, -1, -1):
            idx = T + 3 + r * (1 + 2 * C) + 2 * c
            t, sp = inline(rows[r][c])
            if not t:
                continue
            reqs.append({"insertText": {"location": loc(tab, idx), "text": t}})
            reqs.append({"updateParagraphStyle": {"range": rng(tab, idx, idx + len(t) + 1),
                                                  "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"},
                                                  "fields": "namedStyleType,shading,borderLeft,indentStart,indentEnd,alignment"}})
            reqs.append({"updateTextStyle": {"range": rng(tab, idx, idx + len(t)), "textStyle": {"fontSize": {"magnitude": 10, "unit": "PT"}},
                                             "fields": RESET}})
            reqs += span_reqs(tab, sp, idx)
            if header and r == 0:
                reqs.append({"updateTextStyle": {"range": rng(tab, idx, idx + len(t)), "textStyle": {"bold": True}, "fields": "bold"}})
    return reqs


def build_tab(doc, tab, md_path):
    fm, blocks = parse(Path(md_path).read_text(encoding="utf8"))
    meta = [["Field", "Value"]] + [[k, v] for k, v in fm.items() if k in (
        "title", "seo_title", "meta_description", "slug", "url", "primary_keyword", "secondary_keywords", "excerpt",
        "category", "author", "reading_time", "audience", "cover_image_prompt_claude", "cover_image_prompt_midjourney")]
    seq = [("h3", "SEO metadata")] + [("table", meta)] + blocks
    pending = []
    for blk in reversed(seq):
        if blk[0] == "table":
            batch(doc, pending)
            pending = []
            batch(doc, table_reqs(doc, tab, blk[1]))
        else:
            pending += block_reqs(tab, blk)
    batch(doc, pending)
    print("filled tab", tab, len(seq), "blocks")


def main():
    doc = gws("docs", "documents", "create", body={"title": TITLE})["documentId"]
    d = gws("docs", "documents", "get", "--params", json.dumps({"documentId": doc, "includeTabsContent": True}))
    tab1 = d["tabs"][0]["tabProperties"]["tabId"]
    batch(doc, [{"updateDocumentTabProperties": {"tabProperties": {"tabId": tab1, "title": "Business blog"}, "fields": "title"}},
                {"addDocumentTab": {"tabProperties": {"title": "Technical blog", "index": 1}}}])
    d = gws("docs", "documents", "get", "--params", json.dumps({"documentId": doc, "includeTabsContent": True}))
    tab2 = [t for t in d["tabs"] if t["tabProperties"]["title"] == "Technical blog"][0]["tabProperties"]["tabId"]
    build_tab(doc, tab1, HERE / "business-blog.md")
    build_tab(doc, tab2, HERE / "technical-blog.md")
    (HERE / "gdoc_id.txt").write_text(doc)
    print("https://docs.google.com/document/d/" + doc + "/edit")


if __name__ == "__main__":
    main()
