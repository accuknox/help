"""Write evidence-log.md: every claim, its source URL and the exact quote that backs it.

Run from this folder after validate_evidence.py passes:  python write_evidence_log.py
"""
import cnapp_content as D

NAMES = (("ak", "AccuKnox"), ("wz", "Wiz"), ("pa", "Palo Alto Networks"), ("s1", "SentinelOne"))
REL = {"": "", "ak": "AccuKnox leads", "par": "Matches", "comp": "Competitor leads", "nc": "Not compared"}


def q(s):
    return s.replace("|", "/")


lines = [
    "# Evidence log, AccuKnox vs Wiz, Palo Alto Networks and SentinelOne (CNAPP)",
    "",
    f"Pages read on {D.READ_DATE} with Firecrawl. AccuKnox pages were read live on help.accuknox.com. "
    "Saved copies sit in `research/raw/`. `validate_evidence.py` checks that every quote below appears in its saved page.",
    "Wiz and SentinelOne technical docs need a login, so those columns use public product pages, blogs and the Wiz AWS Marketplace listing.",
    "A cell marked Not compared with no text makes no claim. The PDF contains no claim about what a vendor lacks, except the Palo Alto statement quoted for SAST.",
    "",
    "| Row | Cell | Relation to AccuKnox | PDF text | Source | Quote |",
    "|---|---|---|---|---|---|",
]
for r in D.ROWS:
    for k, name in NAMES:
        cl = r[k]
        for sid, ph in cl["ev"]:
            lines.append(f"| {r['cap']} | {name} | {REL[cl['win']]} | {q(cl['t'])} | {D.SOURCES[sid][3]} | {q(ph)} |")
lines += ["", "## Module fit", "", "| Module | PDF text | Source | Quote |", "|---|---|---|---|"]
for mod, pr, why, unit, ev in D.FIT:
    for sid, ph in ev:
        lines.append(f"| {mod} | Licensed by: {unit} | {D.SOURCES[sid][3]} | {q(ph)} |")
lines += ["", "## Other claims", "", "| Section | PDF text | Source | Quote |", "|---|---|---|---|"]
for sec, bls in (("How the others license", D.LICENSE_NOTES), ("Where AccuKnox leads", D.WHERE_ACCUKNOX_LEADS)):
    for bl in bls:
        for sid, ph in bl["ev"]:
            lines.append(f"| {sec} | {q(bl['t'])} | {D.SOURCES[sid][3]} | {q(ph)} |")
for n, t, bl in D.POC:
    for sid, ph in bl["ev"]:
        lines.append(f"| POC, {n} | {q(t)} | {D.SOURCES[sid][3]} | {q(ph)} |")
for sid, ph in D.POC_TIMELINE["ev"]:
    lines.append(f"| POC timeline | {q(D.POC_TIMELINE['t'])} | {D.SOURCES[sid][3]} | {q(ph)} |")
for i, t, ev in D.PICK:
    for sid, ph in ev:
        lines.append(f"| Pick AccuKnox for | {q(t)} | {D.SOURCES[sid][3]} | {q(ph)} |")
for key, (t, ev) in D.NOTES.items():
    for sid, ph in ev:
        lines.append(f"| Note, {key} | {q(t)} | {D.SOURCES[sid][3]} | {q(ph)} |")
open("evidence-log.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"evidence-log.md: {len(lines)} lines")
