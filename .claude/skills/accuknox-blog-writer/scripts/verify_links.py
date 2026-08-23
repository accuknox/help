#!/usr/bin/env python3
"""Check every link in a draft resolves, before the draft ships.

The accuknox.com sitemap is not exhaustive and slugs move. `platform/aispm`
returns 200 and is absent from the sitemap. `platform/prompt-firewall` is
linked from a live post and returns 404. Neither problem is visible without a
request, so run this on every draft.

Usage:
    python verify_links.py draft.md
    python verify_links.py draft.md --fix-suggestions
    python verify_links.py draft.md --timeout 20 --workers 12

Exit codes: 0 every link resolves, 1 at least one link is broken.
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; accuknox-blog-writer/1.0)"}
LINK = re.compile(r"\[(?P<text>[^\]]*)\]\((?P<url>https?://[^)\s]+)\)")
BARE = re.compile(r"(?<![(\[<])\bhttps?://[^\s)>\]]+")

SOURCES = Path(__file__).resolve().parent.parent / "sources"

# A bot block is not a dead link. These statuses get reported and do not fail
# the run, because the host refused the checker rather than the URL.
BLOCKED = {401, 403, 405, 429, 503}


def clean(url: str) -> str:
    """Trim the punctuation and quote characters markdown drags along."""
    return url.rstrip(".,;:)\"'>")


def check(url: str, timeout: int) -> tuple[str, int, str]:
    """Return (url, status, note). Status 0 means the request never completed."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, headers=HEADERS, method=method)
        for verify in (True, False):
            try:
                ctx = None
                if not verify:
                    ctx = ssl.create_default_context()
                    ctx.check_hostname = False
                    ctx.verify_mode = ssl.CERT_NONE
                with urllib.request.urlopen(req, timeout=timeout,
                                            context=ctx) as r:
                    return url, r.status, ""
            except HTTPError as exc:
                if exc.code in (403, 405) and method == "HEAD":
                    break  # some hosts refuse HEAD, retry with GET
                return url, exc.code, exc.reason or ""
            except (URLError, ssl.SSLError, TimeoutError) as exc:
                if verify:
                    continue
                return url, 0, str(getattr(exc, "reason", exc))[:60]
    return url, 0, "no response"


def known_slugs() -> set[str]:
    slugs: set[str] = set()
    for f in SOURCES.glob("*.md"):
        slugs.update(re.findall(r"\| `([^`]+)` \|", f.read_text("utf-8")))
    return slugs


def suggest(url: str, slugs: set[str]) -> str:
    """Offer the closest known slug for a broken accuknox.com URL."""
    if "accuknox.com" not in url:
        return ""
    path = re.sub(r"^https?://[^/]+/", "", url).rstrip("/")
    tail = path.rsplit("/", 1)[-1]
    words = {w for w in re.split(r"[-/]", tail) if len(w) > 2}
    scored = []
    for s in slugs:
        other = {w for w in re.split(r"[-/]", s) if len(w) > 2}
        overlap = len(words & other)
        if overlap:
            scored.append((overlap / max(len(words | other), 1), s))
    scored.sort(reverse=True)
    return ", ".join(s for _, s in scored[:3])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", type=Path)
    ap.add_argument("--timeout", type=int, default=25)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--fix-suggestions", action="store_true",
                    help="for a broken accuknox.com link, name the closest "
                         "slugs from sources/")
    args = ap.parse_args()

    text = args.draft.read_text("utf-8")
    # Front matter holds `url` and `markdown_url`. They are metadata, not links
    # in the prose, and scanning them produces quote-suffixed false positives.
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            text = text[end + 4:]

    # A URL inside a fence is an argument to a command. Checking a helm repo
    # root or a chart OCI reference tells you nothing about the prose.
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]+`", "", text)

    urls, anchors = [], {}
    for m in LINK.finditer(text):
        u = clean(m.group("url"))
        urls.append(u)
        anchors.setdefault(u, m.group("text").strip())
    bare = [clean(b) for b in BARE.findall(text)]
    urls = list(dict.fromkeys(urls + bare))

    if not urls:
        print("no links found")
        return 0

    print(f"checking {len(urls)} links from {args.draft.name}\n")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda u: check(u, args.timeout), urls))

    blocked = [(u, s, n) for u, s, n in results if s in BLOCKED]
    broken = [(u, s, n) for u, s, n in results
              if (s == 0 or s >= 400) and s not in BLOCKED]
    ok = len(results) - len(broken) - len(blocked)
    slugs = known_slugs() if args.fix_suggestions and broken else set()

    for url, status, note in sorted(results, key=lambda r: -abs(r[1] - 200)):
        if status == 200:
            continue
        if status in BLOCKED:
            mark = "BLOCKD"
        elif status == 0 or status >= 400:
            mark = "BROKEN"
        else:
            mark = "note  "
        print(f"{mark} {status or '---'}  {url}  {note}")
        if slugs and mark == "BROKEN":
            s = suggest(url, slugs)
            if s:
                print(f"       closest known slugs: {s}")

    empty = [u for u, a in anchors.items() if not a or a.lower() in
             ("click here", "here", "read more", "link", u)]
    for u in empty:
        print(f"ANCHOR      weak or missing anchor text: {u}")

    print(f"\n{ok} ok, {len(broken)} broken, {len(blocked)} blocked by the "
          f"host, {len(empty)} weak anchors")
    if blocked:
        print("A blocked status means the host refused the checker, not that "
              "the URL is dead. Open each one in a browser before you ship.")
    if bare:
        print(f"{len(bare)} bare URL(s) in prose. Wrap each in descriptive "
              "link text (writing-rules section 12).")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
