#!/usr/bin/env python3
"""Run the shared slop scorer and account for the one finding this channel forces.

`D:\\Atharva\\NOTES\\SCRIPTS\\slop\\score.py` bans the semicolon. The AccuKnox blog
layout requires a heading spelled `TL;DR`, which every live post carries. That
collision produces one CRIT on every correct draft, so a raw CRIT count is not a
usable gate here.

The same holds for the em dash. Every published AccuKnox press release and case
study attributes a quote with `**- Name, Title, Company**` using an em dash, and
the ban list forbids that character in prose.

This wrapper prints the scorer output unchanged, then names every finding it
suppressed and why. It suppresses exactly two shapes: a semicolon CRIT on a
heading whose text is `TL;DR`, and an em-dash CRIT on a quote attribution line.
Nothing else is filtered, and the adjusted count is what the gate reads.

Usage:
    python slop.py draft.md
    python slop.py draft.md --raw       # no suppression, no summary

Exit codes: 0 adjusted CRIT is 0, 1 adjusted CRIT is above 0, 2 the scorer did
not run.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SCORER = Path(r"D:\Atharva\NOTES\SCRIPTS\slop\score.py")
FINDING = re.compile(r"^\s*(CRIT|MED|LOW)\s+L(\d+)\s+\[([a-z0-9-]+)\]\s*(.*)$")

# A quote attribution: `**— Srimal Silva, AGM - IT, FairFirst Insurance**`.
# Every published AccuKnox press release and case study uses this exact shape.
ATTRIBUTION = re.compile(r"^\**\s*—\s*[\w\[].*,.*?\**$")


def is_tldr_semicolon(draft_lines: list[str], line_no: int, rule: str) -> bool:
    """True when a semicolon CRIT lands on the mandatory `TL;DR` heading."""
    if rule != "semicolon":
        return False
    if not 1 <= line_no <= len(draft_lines):
        return False
    text = draft_lines[line_no - 1].strip()
    return bool(re.fullmatch(r"#{1,4}\s*\**TL;DR\**\s*:?", text))


def is_attribution_dash(draft_lines: list[str], line_no: int,
                        rule: str) -> bool:
    """True when an em-dash CRIT lands on a quote attribution line.

    The dash is a typographic marker introducing a speaker, not prose
    punctuation, and it is the carve-out restraint-rules section 1 already
    makes for a watched character inside a quotation.
    """
    if rule != "em-dash":
        return False
    if not 1 <= line_no <= len(draft_lines):
        return False
    return bool(ATTRIBUTION.match(draft_lines[line_no - 1].strip()))


SUPPRESSIONS = [
    (is_tldr_semicolon, "the `TL;DR` heading the AccuKnox blog layout requires"),
    (is_attribution_dash, "the em dash opening a quote attribution line"),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", type=Path)
    ap.add_argument("--raw", action="store_true",
                    help="print the scorer output only, suppress nothing")
    args = ap.parse_args()

    if not SCORER.exists():
        print(f"scorer not found at {SCORER}", file=sys.stderr)
        print("Apply the writing rules by reading, and say in your reply that "
              "the scorer did not run.", file=sys.stderr)
        return 2

    proc = subprocess.run([sys.executable, str(SCORER), str(args.draft)],
                          capture_output=True, text=True)
    out = proc.stdout + proc.stderr
    print(out.rstrip())
    if args.raw:
        return proc.returncode

    draft_lines = args.draft.read_text("utf-8").splitlines()
    crit = suppressed = 0
    notes: list[str] = []
    for line in out.splitlines():
        m = FINDING.match(line)
        if not m or m.group(1) != "CRIT":
            continue
        line_no, rule = int(m.group(2)), m.group(3)
        hit = next((why for test, why in SUPPRESSIONS
                    if test(draft_lines, line_no, rule)), None)
        if hit:
            suppressed += 1
            notes.append(f"  L{line_no} [{rule}] {hit}")
            continue
        crit += 1

    print()
    if notes:
        print(f"suppressed {suppressed} finding(s), named in full:")
        for n in notes:
            print(n)
    print(f"adjusted CRIT: {crit}")
    if crit:
        print("Fix every remaining CRIT. The gate is 0.")
    return 1 if crit else 0


if __name__ == "__main__":
    raise SystemExit(main())
