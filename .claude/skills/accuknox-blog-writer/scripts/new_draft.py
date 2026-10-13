#!/usr/bin/env python3
"""Start a blog draft: copy the template, fill the fixed fields, make the image folder.

Fills `slug`, `date` (today), `author` and the keyword fields. You write the
rest. Drafts land in `references/drafts/blog/`, never in `docs/`.

Usage:
    python new_draft.py auditable-ai-agents --keyword "auditable ai agents"
    python new_draft.py my-slug --category CNAPP --author "Atharva Shah"

Prints the draft path and the image folder. Refuses to overwrite a draft.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
TEMPLATE = ROOT / "assets" / "blog-template.md"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--keyword", help="primary keyword")
    ap.add_argument("--category", default="AI-SPM")
    ap.add_argument("--author", default="Atharva Shah")
    args = ap.parse_args()

    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", args.slug):
        print("slug must be lowercase words joined by hyphens", file=sys.stderr)
        return 2
    out = REPO / "references" / "drafts" / "blog" / f"{args.slug}.md"
    if out.exists():
        print(f"{out} already exists", file=sys.stderr)
        return 2

    text = TEMPLATE.read_text("utf-8")
    text = text.replace('slug: "lowercase-hyphenated-slug"',
                        f'slug: "{args.slug}"')
    text = text.replace('date: "YYYY-MM-DD"',
                        f'date: "{dt.date.today().isoformat()}"')
    text = text.replace('author: "Atharva Shah"', f'author: "{args.author}"')
    text = text.replace('category: "AI-SPM"', f'category: "{args.category}"')
    if args.keyword:
        text = text.replace('primary_keyword: "the one phrase this post targets"',
                            f'primary_keyword: "{args.keyword.lower()}"')
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")
    imgs = out.parent / "images" / args.slug
    imgs.mkdir(parents=True, exist_ok=True)
    print(f"draft   {out}")
    print(f"images  {imgs}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
