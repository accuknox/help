"""Stage 3, grounding. Build an evidence pack for every requirement.

    python ground.py <workdir>                    evidence for rows that need work
    python ground.py <workdir> --all              evidence for every requirement row
    python ground.py <workdir> --rows SAST:9,24   only these rows
    python ground.py --module aspm                print one module card
    python ground.py --query "pause a dast scan"  ad-hoc search over the docs

For each row the pack holds the ranked help pages with their live URL, the lines
that matched, and the images those same pages embed. An image taken from the
page you cite is the right image. The pack is a shortlist, not an answer: open
the pages before you write a word.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rfp_lib as L  # noqa: E402

IMG_MD = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)")
IMG_HTML = re.compile(r"<img[^>]+src=[\"']([^\"']+)[\"'][^>]*?(?:alt=[\"']([^\"']*)[\"'])?", re.I)


def page_images(rel):
    """Images embedded in a docs page, resolved to docs-relative paths."""
    path = os.path.join(L.DOCS, rel)
    with open(path, encoding="utf-8", errors="ignore") as f:
        text = f.read()
    found = []
    for m in IMG_MD.finditer(text):
        found.append((m.group(2), m.group(1)))
    for m in IMG_HTML.finditer(text):
        found.append((m.group(1), m.group(2) or ""))
    out, seen = [], set()
    base = os.path.dirname(rel)
    for src, alt in found:
        if src.startswith(("http://", "https://", "data:")) or src.endswith(".svg"):
            continue
        src = src.split("#")[0].split("?")[0]
        cand = os.path.normpath(os.path.join(base, src)).replace(os.sep, "/")
        if src.startswith("/"):
            cand = src.lstrip("/")
        if cand in seen or L.is_draft(cand) or not os.path.isfile(os.path.join(L.DOCS, cand)):
            continue
        seen.add(cand)
        out.append({"image": "docs/" + cand, "alt": alt.strip()[:120]})
    return out


def snippets(rel, query, n=3):
    q = set(L.tokens(query))
    with open(os.path.join(L.DOCS, rel), encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()
    scored = []
    in_style = False
    for i, line in enumerate(lines):
        if "<style" in line or "<script" in line:
            in_style = True
        if in_style:
            if "</style>" in line or "</script>" in line:
                in_style = False
            continue
        t = line.strip()
        if len(t) < 25 or t.startswith(("![", "<", "|--", "---")):
            continue
        hits = len(q & set(L.tokens(t)))
        if hits:
            scored.append((hits, i + 1, t[:220]))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [{"line": ln, "text": t} for _, ln, t in scored[:n]]


def evidence_for(req, section, sheet, mods, top=5):
    m_objs = [L.module_by_id(m) for m in mods]
    prefer = set()
    for m in m_objs:
        prefer.update(m["pages"] + m["matrices"] + m["faqs"])
    query = f"{req} {section or ''}"
    pages = []
    for rel, score, title in L.search_docs(query, top=top, prefer=prefer):
        pages.append({
            "page": "docs/" + rel, "url": L.doc_url(rel), "title": title, "score": score,
            "in_nav": L.in_nav(rel), "module_page": rel in prefer,
            "lines": snippets(rel, req),
            "images": page_images(rel)[:6],
        })
    strength = "strong" if pages and pages[0]["score"] >= 12 and pages[0]["lines"] else \
               "weak" if not pages or pages[0]["score"] < 7 else "moderate"
    return {
        "modules": mods,
        "strength": strength,
        "pages": pages,
        "matrices": [{"page": "docs/" + p, "url": L.doc_url(p)} for m in m_objs for p in m["matrices"]],
        "faqs": [{"page": "docs/" + p, "url": L.doc_url(p)} for m in m_objs for p in m["faqs"]],
        "limits": [lim for m in m_objs for lim in m["limits"]],
        "web": [u for m in m_objs for u in m["web"]],
        "fit_risks": L.fit_risks(req),
    }


def needs_work(x):
    return (not x["existing_response"]) or (x["comment_len"] and not x["comment_has_url"]) \
        or not x["has_image"] or x["existing_verdict"] == "NEGATIVE"


def module_card(mid):
    m = L.module_by_id(mid)
    print(f"{m['id']}  {m['name']}")
    print(f"covers   {m['covers']}")
    for k in ("pages", "matrices", "faqs"):
        for p in m[k]:
            print(f"  {k[:-1]:8} {L.doc_url(p)}   (docs/{p})")
    for u in m["web"]:
        print(f"  web      {u}")
    for d in m["image_dirs"]:
        print(f"  images   docs/{d}/")
    for lim in m["limits"]:
        print(f"  limit    {lim['gap']}   [source: docs/{lim['source']}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workdir", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--rows", help="SHEET:row,row;SHEET:row")
    ap.add_argument("--module")
    ap.add_argument("--query")
    a = ap.parse_args()

    if a.module:
        return module_card(a.module)
    if a.query:
        for rel, score, title in L.search_docs(a.query, top=8):
            print(f"{score:6}  {L.doc_url(rel):70}  {title}")
            for s in snippets(rel, a.query, 2):
                print(f"          L{s['line']}: {s['text'][:140]}")
            for im in page_images(rel)[:3]:
                print(f"          img {im['image']}")
        return
    if not a.workdir:
        sys.exit("give a workdir, --module or --query")

    prof = L.read_json(os.path.join(a.workdir, "profile.json"))
    want = None
    if a.rows:
        want = set()
        for part in a.rows.split(";"):
            sh, rows = part.split(":")
            want |= {(sh, int(r)) for r in rows.split(",")}

    packs = []
    for s in prof["sheets"]:
        for x in s.get("rows", []):
            if x["kind"] != "requirement":
                continue
            key = (s["sheet"], x["row"])
            if want is not None and key not in want:
                continue
            if want is None and not a.all and not needs_work(x):
                continue
            mods = x["modules"] or ["platform"]
            ev = evidence_for(x["requirement"], x["section"], s["sheet"], mods)
            packs.append({"sheet": s["sheet"], "row": x["row"], "id": x["id"],
                          "mandatory": x["mandatory"], "requirement": x["requirement"],
                          "existing_response": x["existing_response"], "has_image": x["has_image"],
                          "comment_has_url": x["comment_has_url"], **ev})

    out = os.path.join(a.workdir, "evidence.json")
    L.write_json(out, packs)
    weak = [p for p in packs if p["strength"] == "weak"]
    no_img = [p for p in packs if not p["has_image"] and not any(pg["images"] for pg in p["pages"])]
    print(f"evidence packs {len(packs)} | strong {sum(p['strength'] == 'strong' for p in packs)} | "
          f"moderate {sum(p['strength'] == 'moderate' for p in packs)} | weak {len(weak)} | "
          f"rows with no candidate image {len(no_img)}")
    for p in packs:
        top = p["pages"][0] if p["pages"] else {}
        flag = "!" if p["strength"] == "weak" else " "
        mand = "M" if p["mandatory"] else " "
        print(f" {flag}{mand} {p['sheet'][:14]:14} r{p['row']:<4} {'/'.join(p['modules']):18} "
              f"{top.get('url', '-')[len(L.HELP_BASE) - 1:]:52} imgs {sum(len(pg['images']) for pg in p['pages'])}")
    print(f"wrote {out}")
    if weak:
        print("Weak evidence rows need a closer read or an interview question before you answer them.")


if __name__ == "__main__":
    main()
