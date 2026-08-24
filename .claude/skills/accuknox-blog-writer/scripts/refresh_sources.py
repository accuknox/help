#!/usr/bin/env python3
"""Rebuild the accuknox.com URL inventory under ../sources/.

Reads https://accuknox.com/sitemap.xml, follows every English child sitemap, and
writes one markdown table per content bucket. Each row carries the slug, the
live URL, the agent-friendly `.md` URL and the last-modified date, so a blog
writer can pick a link without a second network call.

Usage:
    python refresh_sources.py              # rebuild every bucket
    python refresh_sources.py --check      # report staleness, write nothing

Buckets: platform, solutions, comparisons, blog, press-release, case-study,
product, company, resources, other.
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError

BASE = "https://accuknox.com"
INDEX = f"{BASE}/sitemap.xml"
OUT = Path(__file__).resolve().parent.parent / "sources"

# Child sitemaps to skip. The locale ones duplicate English content.
SKIP = re.compile(r"-(ko|ja|fr|es)-sitemap\.xml$")

# Bucket order matters. The first pattern that matches a path wins.
BUCKETS: list[tuple[str, re.Pattern[str]]] = [
    ("platform", re.compile(r"^/platform(/|$)")),
    ("solutions", re.compile(r"^/solutions?(/|$)")),
    ("comparisons", re.compile(r"^/comparisons?(/|$)")),
    ("blog", re.compile(r"^/blog(/|$)")),
    ("press-release", re.compile(r"^/(press|news)(-release)?s?(/|$)")),
    ("case-study", re.compile(r"^/(case-stud|customer)")),
    ("product", re.compile(r"^/(product|integrations?|pricing|kubearmor)(/|$)")),
    ("resources", re.compile(
        r"^/(white-?papers?|ebooks?|data-?sheets?|analyst-reports?|"
        r"technical-papers?|cheatsheets?|videos?|use-cases?|cve|glossary|"
        r"resources?)(/|$)")),
    ("company", re.compile(r"^/(about|careers?|contact|team|partners?|legal|"
                           r"privacy|terms|demo)(/|$)")),
]

HEADERS = {"User-Agent": "accuknox-blog-writer/1.0 (+internal sitemap sync)"}


def fetch(url: str, timeout: int = 90) -> str:
    """GET a URL as text. Falls back to an unverified context on a CA failure.

    Python on this machine ships an expired CA root, so the retry is not
    optional. See CLAUDE.md, the API keys section.
    """
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except (URLError, ssl.SSLError):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return r.read().decode("utf-8", "replace")


def child_sitemaps(index_xml: str) -> list[str]:
    locs = re.findall(r"<loc>\s*([^<]+?)\s*</loc>", index_xml)
    return [u for u in locs if u.endswith(".xml") and not SKIP.search(u)]


def entries(sitemap_xml: str) -> list[tuple[str, str]]:
    """Return (url, lastmod) pairs from one child sitemap."""
    out = []
    for block in re.findall(r"<url>(.*?)</url>", sitemap_xml, re.S):
        loc = re.search(r"<loc>\s*([^<]+?)\s*</loc>", block)
        mod = re.search(r"<lastmod>\s*([^<]+?)\s*</lastmod>", block)
        if loc:
            out.append((loc.group(1), (mod.group(1) if mod else "")[:10]))
    return out


def bucket_for(url: str) -> str:
    path = re.sub(r"^https?://[^/]+", "", url) or "/"
    for name, pattern in BUCKETS:
        if pattern.match(path):
            return name
    return "other"


def slug_of(url: str) -> str:
    path = re.sub(r"^https?://[^/]+", "", url).strip("/")
    return path or "(home)"


def write_bucket(name: str, rows: list[tuple[str, str]]) -> Path:
    rows = sorted(set(rows), key=lambda r: (-len(r[1]), r[1]), reverse=True)
    rows = sorted(set(rows), key=lambda r: (r[1] or "0000-00-00"), reverse=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = OUT / f"{name}.md"
    lines = [
        f"# accuknox.com {name} URLs",
        "",
        f"{len(rows)} pages. Rebuilt {stamp} by "
        "`scripts/refresh_sources.py`. Do not hand-edit.",
        "",
        "Append `.md` to any URL below to read the page as agent-friendly "
        "markdown with YAML front matter.",
        "",
        "| Last modified | Slug | URL |",
        "| --- | --- | --- |",
    ]
    for url, mod in rows:
        lines.append(f"| {mod or 'unknown'} | `{slug_of(url)}` | {url} |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="report staleness and exit without writing")
    args = ap.parse_args()

    if args.check:
        stale = []
        for f in sorted(OUT.glob("*.md")):
            if f.name == "README.md":
                continue
            age = (datetime.now().timestamp() - f.stat().st_mtime) / 86400
            flag = "STALE" if age > 30 else "ok"
            print(f"{flag:6s} {age:5.1f}d  {f.name}")
            if age > 30:
                stale.append(f.name)
        if stale:
            print(f"\n{len(stale)} file(s) older than 30 days. "
                  "Run without --check to rebuild.")
            return 1
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    print(f"index  {INDEX}")
    children = child_sitemaps(fetch(INDEX))
    print(f"       {len(children)} English child sitemaps")

    grouped: dict[str, list[tuple[str, str]]] = {}
    total = 0
    for child in children:
        try:
            pairs = entries(fetch(child))
        except Exception as exc:  # noqa: BLE001
            print(f"  skip {child}: {exc}", file=sys.stderr)
            continue
        total += len(pairs)
        print(f"  {len(pairs):4d}  {child.rsplit('/', 1)[-1]}")
        for url, mod in pairs:
            grouped.setdefault(bucket_for(url), []).append((url, mod))

    for name, _ in BUCKETS + [("other", re.compile(""))]:
        rows = grouped.get(name, [])
        if not rows:
            continue
        path = write_bucket(name, rows)
        print(f"wrote  {path.name:20s} {len(set(rows)):4d} URLs")

    print(f"\n{total} URLs across {len(grouped)} buckets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
