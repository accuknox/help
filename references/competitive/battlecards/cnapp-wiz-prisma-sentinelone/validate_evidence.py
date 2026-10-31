"""Check that every evidence phrase in cnapp_content.py appears in the saved source page.

Run from this folder:  python validate_evidence.py
Exit code 1 when any phrase is missing or any source file is absent.
"""
import pathlib
import re
import sys

import cnapp_content as D

HERE = pathlib.Path(__file__).resolve().parent
RAW = HERE / "research" / "raw"


def norm(t):
    t = t.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    t = t.replace("–", "-").replace("—", "-").replace(" ", " ")
    t = re.sub(r"\(https?://[^)]*\)", "", t)
    t = re.sub(r"[\\*_`\[\]#>|]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.lower()


def pairs():
    for r in D.ROWS:
        for k in ("ak", "wz", "pa", "s1"):
            for sid, ph in r[k]["ev"]:
                yield f"{r['cap']}.{k}", sid, ph
    for mod, _, _, _, ev in D.FIT:
        for sid, ph in ev:
            yield f"FIT:{mod}", sid, ph
    for bl in D.LICENSE_NOTES + D.WHERE_ACCUKNOX_LEADS:
        for sid, ph in bl["ev"]:
            yield "NOTE", sid, ph
    for _, _, bl in D.POC:
        for sid, ph in bl["ev"]:
            yield "POC", sid, ph
    for sid, ph in D.POC_TIMELINE["ev"]:
        yield "POC", sid, ph
    for _, _, ev in D.PICK:
        for sid, ph in ev:
            yield "PICK", sid, ph
    for _, ev in D.NOTES.values():
        for sid, ph in ev:
            yield "NOTES", sid, ph


def main():
    cache, bad, n = {}, 0, 0
    for where, sid, ph in pairs():
        n += 1
        if sid not in D.SOURCES:
            print(f"UNKNOWN SOURCE {sid} at {where}")
            bad += 1
            continue
        stem = D.SOURCES[sid][1]
        if stem not in cache:
            f = RAW / f"{stem}.md"
            cache[stem] = norm(f.read_text(encoding="utf-8", errors="ignore")) if f.exists() else None
        if cache[stem] is None:
            print(f"MISSING FILE {stem}.md for {sid}")
            bad += 1
        elif norm(ph) not in cache[stem]:
            print(f"NOT FOUND  {where:34s} {sid:10s} {ph!r}")
            bad += 1
    print(f"{n} evidence quotes checked, {bad} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
