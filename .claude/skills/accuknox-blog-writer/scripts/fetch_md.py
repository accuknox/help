#!/usr/bin/env python3
"""Read any accuknox.com page as agent-friendly markdown.

accuknox.com serves a markdown twin of every page. Append `.md` to the path and
you get YAML front matter (title, slug, published_at, excerpt, taxonomy) plus
the body as clean markdown. That is far cheaper than scraping HTML, so try this
before you reach for Firecrawl.

Usage:
    python fetch_md.py platform/aispm
    python fetch_md.py https://accuknox.com/blog/ai-spm-tools
    python fetch_md.py comparisons --headings      # H1-H3 skeleton only
    python fetch_md.py blog/ai-spm-tools --out draft-research/
    python fetch_md.py blog/a blog/b blog/c        # several at once

Exit codes: 0 all fetched, 1 at least one failed.
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import urllib.request
from pathlib import Path
from urllib.error import HTTPError, URLError

BASE = "https://accuknox.com"
HEADERS = {"User-Agent": "accuknox-blog-writer/1.0 (+internal content sync)"}


def to_md_url(target: str) -> str:
    """Normalise a slug, a path or a full URL into its `.md` twin."""
    t = target.strip()
    if not t.startswith("http"):
        t = f"{BASE}/{t.lstrip('/')}"
    t = t.rstrip("/")
    if not t.endswith(".md"):
        t += ".md"
    return t


def fetch(url: str, timeout: int = 90) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except (URLError, ssl.SSLError) as exc:
        if isinstance(exc, HTTPError):
            raise
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.read().decode("utf-8", "replace")


# Everything the WordPress template injects into the markdown twin. None of it
# was written by the author, so strip it before you study a page for layout.
#
# The flag says whether the heading owns the block beneath it. The CTA and the
# related-posts block do, so their subheadings go with them. `Table of Contents`
# does not: it renders as a widget, and the next heading is authored content.
# Treating it as an owner swallowed a post whose TL;DR was an H3, because the H3
# sat deeper than the H2 that opened the skip.
BOILERPLATE_HEADINGS = {
    "ready for a personalized security assessment": True,
    "continue reading": True,
    "table of contents": False,
}


def strip_boilerplate(md: str) -> str:
    """Drop the template-injected share links, CTA block and related posts."""
    lines = md.splitlines()
    out: list[str] = []
    skip_depth = 0  # 0 means keeping; otherwise the level that opened the skip
    for line in lines:
        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            level = len(heading.group(1))
            label = re.sub(r"[*_`\[\]]", "", heading.group(2)).strip().lower()
            match = next((b for b in BOILERPLATE_HEADINGS
                          if label.startswith(b)), None)
            if skip_depth and level <= skip_depth:
                skip_depth = 0  # a sibling or shallower heading ends the block
            if match and BOILERPLATE_HEADINGS[match]:
                skip_depth = level
            elif match:
                continue  # drop the widget heading, keep what follows it
        if skip_depth:
            continue
        # Bare share, feed and AI-handoff links sit on their own lines.
        if re.match(r"^\[https?://(twitter|x|www\.linkedin|reddit|chat\.openai|"
                    r"claude\.ai|www\.perplexity|www\.google)\.", line):
            continue
        if line.strip() in (f"[{BASE}/feed]({BASE}/feed)", "Get a LIVE Tour"):
            continue
        out.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


def headings(md: str) -> str:
    rows = []
    for i, line in enumerate(md.splitlines(), 1):
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            text = re.sub(r"\*\*|__", "", m.group(2)).strip()
            rows.append(f"{i:5d}  {'  ' * (len(m.group(1)) - 1)}{text}")
    return "\n".join(rows)


def body_word_count(md: str) -> int:
    body = re.split(r"^#{1,3}\s+\**TL;DR", md, maxsplit=1, flags=re.M | re.I)
    text = body[-1] if len(body) > 1 else md
    return len(text.split())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("targets", nargs="+",
                    help="slug, path or full accuknox.com URL")
    ap.add_argument("--headings", action="store_true",
                    help="print the H1-H3 skeleton instead of the body")
    ap.add_argument("--raw", action="store_true",
                    help="keep the template share links and CTA blocks")
    ap.add_argument("--out", metavar="DIR",
                    help="write each page to DIR/<slug>.md instead of stdout")
    args = ap.parse_args()

    failed = 0
    for target in args.targets:
        url = to_md_url(target)
        try:
            md = fetch(url)
        except Exception as exc:  # noqa: BLE001
            print(f"FAIL  {url}: {exc}", file=sys.stderr)
            failed += 1
            continue
        if not args.raw:
            md = strip_boilerplate(md)

        if args.out:
            outdir = Path(args.out)
            outdir.mkdir(parents=True, exist_ok=True)
            name = url.rsplit("/", 1)[-1]
            path = outdir / name
            path.write_text(md, encoding="utf-8", newline="\n")
            print(f"{path}  {body_word_count(md)} body words")
        elif args.headings:
            print(f"# {url}  ({body_word_count(md)} body words)")
            print(headings(md))
            print()
        else:
            print(md)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
