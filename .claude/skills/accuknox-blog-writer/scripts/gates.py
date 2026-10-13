#!/usr/bin/env python3
"""Run the three blog gates in order and print one summary.

    grade.py         SEO and structure, CRITICAL must reach 0
    verify_links.py  every link resolves, 0 broken
    slop.py          the shared slop scorer, adjusted CRIT must reach 0

Pass the length the user asked for. `--max-words` counts every word in the
body, tables and headings included, so a "under 1200 words" brief means
`--max-words 1199`.

Usage:
    python gates.py draft.md
    python gates.py draft.md --min-words 800 --max-words 1199
    python gates.py draft.md --full        # print each gate's full output

The restraint pass in `.claude/core/restraint-rules.md` section 5 is a reading
task, so no script runs it. Do it after this one is green.

Exit codes: 0 all three passed, 1 at least one failed.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def run(script: str, *args: str) -> tuple[int, str]:
    p = subprocess.run([sys.executable, str(HERE / script), *args],
                       capture_output=True, text=True, encoding="utf-8")
    return p.returncode, (p.stdout + p.stderr).strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", type=Path)
    ap.add_argument("--min-words", type=int, default=1200)
    ap.add_argument("--max-words", type=int)
    ap.add_argument("--full", action="store_true")
    args = ap.parse_args()

    grade_args = [str(args.draft), "--min-words", str(args.min_words)]
    if args.max_words:
        grade_args += ["--max-words", str(args.max_words)]

    results = []
    rc, out = run("grade.py", *grade_args)
    overall = re.search(r"Overall\s+(\d+)/100", out)
    crit = re.search(r"CRITICAL \((\d+)\)", out)
    high = re.search(r"HIGH \((\d+)\)", out)
    words = re.search(r"(\d+) words in all", out)
    results.append(("grade", rc == 0 and not high,
                    f"score {overall.group(1) if overall else '?'}, "
                    f"CRITICAL {crit.group(1) if crit else 0}, "
                    f"HIGH {high.group(1) if high else 0}, "
                    f"{words.group(1) + ' words' if words else 'words ?'}", out))

    rc, out = run("verify_links.py", str(args.draft), "--fix-suggestions")
    tail = out.splitlines()[-1] if out else "no output"
    broken = re.search(r"(\d+) broken", out)
    results.append(("links", rc == 0 and (not broken or broken.group(1) == "0"),
                    tail, out))

    rc, out = run("slop.py", str(args.draft))
    adj = re.search(r"adjusted CRIT:\s*(\d+)", out)
    results.append(("slop", rc == 0 and bool(adj) and adj.group(1) == "0",
                    f"adjusted CRIT {adj.group(1) if adj else 'scorer did not run'}",
                    out))

    ok = True
    for name, passed, line, full in results:
        ok &= passed
        print(f"{'pass' if passed else 'FAIL'}  {name:6s} {line}")
        if args.full or not passed:
            print("\n".join("      " + l for l in full.splitlines()))
    print("\nnext: restraint pass, .claude/core/restraint-rules.md section 5"
          if ok else "\nfix the failures above, then rerun")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
