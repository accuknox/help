#!/usr/bin/env python3
"""Create a build folder for one gated PDF.

Copies the HTML template, the official logo and the bundled Inter font, so the
render never depends on a system font or on Google Fonts.

Usage:
    python scaffold.py runtime-security-report

Creates references/drafts/gated-content/<slug>/build/ with report.html,
logo.png, fonts/ and an empty img/ folder. An existing report.html is never
overwritten.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
REPO = SKILL.parents[2]
OUT = REPO / "references" / "drafts" / "gated-content"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    slug = sys.argv[1].strip().lower()
    build = OUT / slug / "build"
    (build / "img").mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILL / "assets" / "fonts", build / "fonts", dirs_exist_ok=True)
    shutil.copy2(SKILL / "assets" / "logo.png", build / "logo.png")
    html = build / "report.html"
    if html.exists():
        print(f"kept   {html}")
    else:
        shutil.copy2(SKILL / "assets" / "template.html", html)
        print(f"made   {html}")
    print(f"build  {build}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
