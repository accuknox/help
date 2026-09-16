"""Stage 6, post-validation. Gate the two output files before anyone sends them.

    python validate.py <workdir>              every check, live URL test included
    python validate.py <workdir> --offline    skip the live URL test

Exit code 1 when any check FAILs. Writes validation-report.md in the workdir.
"""
import argparse
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rfp_lib as L  # noqa: E402

POSITIVE = {"MEETS", "EXCEEDS"}
ROADMAP_WORDS = re.compile(r"roadmap|planned|upcoming|future|will be|next release", re.I)


class Report:
    def __init__(self):
        self.rows = []

    def add(self, name, status, detail):
        self.rows.append((name, status, detail))

    @property
    def failed(self):
        return any(s == "FAIL" for _, s, _ in self.rows)

    def text(self):
        w = max(len(n) for n, _, _ in self.rows)
        return "\n".join(f"{s:5} {n:<{w}}  {d}" for n, s, d in self.rows)

    def markdown(self):
        out = ["| Status | Check | Detail |", "| --- | --- | --- |"]
        out += [f"| {s} | {n} | {str(d).replace('|', '/')} |" for n, s, d in self.rows]
        return "\n".join(out)


def urls_in(text):
    return re.findall(r"https?://[^\s)\]>\"']+", text or "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workdir")
    ap.add_argument("--offline", action="store_true")
    a = ap.parse_args()

    prof = L.read_json(os.path.join(a.workdir, "profile.json"))
    man = L.read_json(os.path.join(a.workdir, "fill-manifest.json"))
    rep = Report()
    sheets = {s["sheet"]: s for s in prof["sheets"] if "rows" in s}
    filled = {(e["sheet"], e["row"]): e for e in man["rows"]}

    # 1 original untouched
    same = L.sha256(prof["rfp"]) == prof["sha256"]
    rep.add("original file unchanged", "PASS" if same else "FAIL", prof["sha256"][:16])

    resp_path, rev_path = man["outputs"]["Response"], man["outputs"]["Review"]
    orig = L.load_workbook(prof["rfp"])
    cust = L.load_workbook(resp_path)
    rev = L.load_workbook(rev_path)

    illegal, negative_new, negative_old, blank, altered = [], [], [], [], []
    no_url, banned, contra, clipped, orphan = [], [], [], [], []
    verdicts = {}
    for name, s in sheets.items():
        ws, wo = cust[name], orig[name]
        cols = s["columns"]
        rc, cc = cols["response"], cols.get("comment")
        opts = set(s["options"])
        for x in s["rows"]:
            if x["kind"] != "requirement":
                continue
            r = x["row"]
            v = L.cell_text(ws.cell(r, rc).value)
            ov = L.cell_text(wo.cell(r, rc).value)
            key = (name, r)
            if not v:
                blank.append(f"{name}!{r}")
                continue
            raw = str(ws.cell(r, rc).value).strip()
            if opts and raw not in opts:
                illegal.append(f"{name}!{r}={raw!r}")
            verdict = L.classify_option(v)
            verdicts[key] = verdict
            if verdict == "NEGATIVE":
                (negative_new if v != ov else negative_old).append(f"{name}!{r}")
            e = filled.get(key)
            if ov and v != ov and not (e and e["mode"] == "override"):
                altered.append(f"{name}!{r} {ov!r}->{v!r}")
            if not e or not cc:
                continue
            new_c = str(ws.cell(r, cc).value or "")
            old_c = str(wo.cell(r, cc).value or "")
            if e["flag"] != "RED" and not urls_in(new_c):
                no_url.append(f"{name}!{r}")
            added = new_c[len(old_c):] if new_c.startswith(old_c.rstrip()[:200]) else new_c
            hit = L.banned_hit(added)
            if hit:
                banned.append(f"{name}!{r}:{hit}")
            if verdict in POSITIVE and L.GAP_PHRASES.search(new_c):
                contra.append(f"{name}!{r} says {v!r} but the comment reads as a gap: "
                              f"'{L.GAP_PHRASES.search(new_c).group(0)}'")
            if verdict and verdict.startswith("ROADMAP") and not ROADMAP_WORDS.search(new_c):
                contra.append(f"{name}!{r} says {v!r} but the comment never mentions the roadmap")
            if "image" in e["changed"]:
                imgs = [im for im in ws._images if im.anchor._from.row + 1 == r]
                for im in imgs:
                    h_px = im.anchor.ext.height / 9525 if hasattr(im.anchor, "ext") and im.anchor.ext else im.height
                    if (ws.row_dimensions[r].height or 15) < h_px * 0.75 * 0.9:
                        clipped.append(f"{name}!{r}")
                if not imgs:
                    orphan.append(f"{name}!{r} image missing after save")

    rep.add("responses are dropdown options", "FAIL" if illegal else "PASS", illegal[:10] or "all legal")
    rep.add("no negative answer written", "FAIL" if negative_new else "PASS", negative_new or "none")
    rep.add("pre-existing negative answers", "WARN" if negative_old else "PASS",
            (negative_old[:10], "left as the customer or an earlier draft wrote them. Review.") if negative_old else "none")
    rep.add("no blank requirement rows", "FAIL" if blank else "PASS", blank[:20] or "none")
    rep.add("existing answers untouched", "FAIL" if altered else "PASS", altered[:10] or "no silent changes")
    rep.add("every filled comment has a link", "FAIL" if no_url else "PASS", no_url or "yes")
    rep.add("no banned words in added text", "FAIL" if banned else "PASS", banned or "clean")
    rep.add("answer and comment agree", "WARN" if contra else "PASS", contra[:10] or "consistent")
    rep.add("new images fit their rows", "WARN" if clipped else "PASS", clipped or "ok")
    rep.add("new images anchored", "FAIL" if orphan else "PASS", orphan or "ok")

    # dropdowns survived the save
    lost = []
    for name in sheets:
        before = len([d for d in orig[name].data_validations.dataValidation if d.type == "list"])
        after = len([d for d in cust[name].data_validations.dataValidation if d.type == "list"])
        if after < before:
            lost.append(f"{name}: {before}->{after}")
    rep.add("answer dropdowns preserved", "FAIL" if lost else "PASS", lost or "all present")

    # image integrity
    from PIL import Image
    base = sum(prof["images_baseline"].values())
    got = sum(L.image_count(cust).values())
    expect = base + man["images_added"] + (1 if man["summary"] != "none" else 0)
    corrupt = []
    for ws in cust.worksheets:
        for im in ws._images:
            try:
                Image.open(io.BytesIO(im._data())).verify()
            except Exception:  # noqa: BLE001
                corrupt.append(f"{ws.title} r{im.anchor._from.row + 1}")
    rep.add("images preserved and valid", "FAIL" if got < expect or corrupt else "PASS",
            f"{got} images, expected >= {expect}" + (f", corrupt {corrupt}" if corrupt else ""))

    # customer copy carries nothing internal
    leaks = []
    if "AccuKnox Review" in cust.sheetnames:
        leaks.append("Review sheet present")
    for name, s in sheets.items():
        nc = s["columns"]["review_note"]
        if any(L.cell_text(cust[name].cell(x["row"], nc).value).startswith(("GREEN", "AMBER", "RED"))
               for x in s["rows"]):
            leaks.append(f"{name}: review notes in column {nc}")
    rep.add("customer copy has no internal notes", "FAIL" if leaks else "PASS", leaks or "clean")
    rep.add("review copy carries notes", "PASS" if "AccuKnox Review" in rev.sheetnames else "FAIL", rev_path)

    # links
    all_urls = set()
    for name, s in sheets.items():
        cc = s["columns"].get("comment")
        if not cc:
            continue
        for x in s["rows"]:
            if (name, x["row"]) in filled:
                all_urls.update(urls_in(str(cust[name].cell(x["row"], cc).value or "")))
    drafts = [u for u in all_urls if L.is_draft(u)]
    rep.add("no links to unpublished drafts", "FAIL" if drafts else "PASS", drafts or "none")
    if a.offline:
        rep.add("links resolve", "SKIP", f"{len(all_urls)} links not tested (--offline)")
    else:
        broken = [(u, st) for u in sorted(all_urls) if (st := L.url_status(u.rstrip(".,;"))) != 200]
        rep.add("links resolve", "FAIL" if broken else "PASS", broken or f"{len(all_urls)} links, all 200")

    # cross-row consistency, near-duplicate requirements with different answer classes
    def cls(v):
        return "positive" if v in POSITIVE else "roadmap" if v and v.startswith("ROADMAP") else v

    reqs = [(n, x) for n, s in sheets.items() for x in s["rows"] if x["kind"] == "requirement"]
    toks = {(n, x["row"]): set(L.tokens(x["requirement"])) for n, x in reqs}
    mixed = []
    keys = list(toks)
    for i, k1 in enumerate(keys):
        for k2 in keys[i + 1:]:
            a1, a2 = toks[k1], toks[k2]
            if len(a1) < 3 or len(a2) < 3:
                continue
            j = len(a1 & a2) / len(a1 | a2)
            if j >= 0.6 and cls(verdicts.get(k1)) != cls(verdicts.get(k2)) and (k1 in filled or k2 in filled):
                mixed.append(f"{k1[0]}!{k1[1]} {verdicts.get(k1)} vs {k2[0]}!{k2[1]} {verdicts.get(k2)}")
    rep.add("similar requirements answered alike", "WARN" if mixed else "PASS", mixed[:10] or "consistent")

    # items for a human
    red = [f"{e['sheet']}!{e['row']}" for e in man["rows"] if e["flag"] == "RED"]
    mand = [f"{e['sheet']}!{e['row']}" for e in man["rows"] if e["mandatory"] and e["flag"] != "GREEN"]
    rep.add("RED rows needing a decision", "WARN" if red else "PASS", red or "none")
    rep.add("mandatory rows not GREEN", "WARN" if mand else "PASS", mand or "none")

    print(rep.text())
    out = os.path.join(a.workdir, "validation-report.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Validation report\n\nCustomer copy: `{resp_path}`\n\nReview copy: `{rev_path}`\n\n{rep.markdown()}\n")
    print(f"\n{'FAILED' if rep.failed else 'PASSED'}. Report: {out}")
    sys.exit(1 if rep.failed else 0)


if __name__ == "__main__":
    main()
