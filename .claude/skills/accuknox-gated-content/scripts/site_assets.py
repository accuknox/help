#!/usr/bin/env python3
"""Pull images and citable URLs from accuknox.com through Firecrawl.

Cloudflare answers a plain request for an accuknox.com page with 403, so every
page read goes through the Firecrawl v2 scrape API. Image files under
/wp-content/uploads/ download directly and need no Firecrawl credit.

The Firecrawl key comes from FIRECRAWL_API_KEY, else from
`python "D:\\Atharva\\NOTES\\SCRIPTS\\keys\\keys.py" firecrawl`. Calls shell out to
curl because Python on this machine carries an expired CA root.

Usage:
    python site_assets.py images platform/aispm              # product images on a page
    python site_assets.py images platform/aispm --grep prompt firewall
    python site_assets.py images platform/aispm --all        # include nav icons and badges
    python site_assets.py links platform/aispm --grep blog   # accuknox.com URLs to cite
    python site_assets.py cite platform/aispm blog/ai-spm-tools
    python site_assets.py download <image-url> [...] --out build/img

Exit codes: 0 success, 1 a page or file failed, 2 no Firecrawl key.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

BASE = "https://accuknox.com"
API = "https://api.firecrawl.dev/v2/scrape"
KEYS = r"D:\Atharva\NOTES\SCRIPTS\keys\keys.py"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

# Site chrome that shows up on every page and never belongs in a report.
NOISE = re.compile(r"nav-icon|nav-image|-icon\.|/themes/|-cta\.|footer|favicon|gravatar|badge|logo|g2-|gartner-peer|flag|avatar|emoji", re.I)


def to_url(target: str) -> str:
    t = target.strip()
    if not t.startswith("http"):
        t = f"{BASE}/{t.lstrip('/')}"
    return t


def key() -> str:
    k = os.environ.get("FIRECRAWL_API_KEY", "").strip()
    if k:
        return k
    try:
        out = subprocess.run([sys.executable, KEYS, "firecrawl"], capture_output=True, text=True, timeout=120)
        lines = [ln.strip() for ln in out.stdout.splitlines() if ln.strip().startswith("fc-")]
        return lines[-1] if lines else ""
    except (OSError, subprocess.TimeoutExpired):
        return ""


def scrape(url: str, formats: list[str]) -> dict:
    k = key()
    if not k:
        sys.exit("No Firecrawl key. Set FIRECRAWL_API_KEY or fill D:\\Atharva\\NOTES\\.env")
    body = json.dumps({"url": url, "formats": formats, "onlyMainContent": False})
    out = subprocess.run(
        ["curl", "-s", "-X", "POST", API, "-H", f"Authorization: Bearer {k}",
         "-H", "Content-Type: application/json", "--data-binary", "@-"],
        input=body, capture_output=True, text=True, encoding="utf-8", timeout=180,
    )
    try:
        d = json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"success": False, "error": out.stdout[:300] or out.stderr[:300]}
    return d


def matches(text: str, terms: list[str]) -> bool:
    low = text.lower()
    return all(t.lower() in low for t in terms)


def cmd_images(a) -> int:
    d = scrape(to_url(a.page), ["images"])
    if not d.get("success"):
        print(f"FAIL {a.page}: {d.get('error')}", file=sys.stderr)
        return 1
    seen = []
    for img in d["data"].get("images") or []:
        img = img.replace("://www.accuknox.com", "://accuknox.com")
        if img in seen or (not a.all and NOISE.search(img)):
            continue
        if a.grep and not matches(img, a.grep):
            continue
        seen.append(img)
    print("\n".join(seen))
    return 0


def cmd_links(a) -> int:
    d = scrape(to_url(a.page), ["links"])
    if not d.get("success"):
        print(f"FAIL {a.page}: {d.get('error')}", file=sys.stderr)
        return 1
    out = []
    for ln in d["data"].get("links") or []:
        host = urlparse(ln).netloc.replace("www.", "")
        if host != "accuknox.com" or "wp-content" in ln or "#" in ln:
            continue
        ln = ln.replace("://www.", "://").rstrip("/") + "/"
        if ln not in out and (not a.grep or matches(ln, a.grep)):
            out.append(ln)
    print("\n".join(sorted(out)))
    return 0


def cmd_cite(a) -> int:
    bad = 0
    for p in a.pages:
        d = scrape(to_url(p), ["summary"]) if a.summary else scrape(to_url(p), ["links"])
        meta = (d.get("data") or {}).get("metadata", {})
        code = meta.get("statusCode")
        ok = d.get("success") and code == 200
        bad += not ok
        final = meta.get("url") or meta.get("sourceURL") or to_url(p)
        print(f"{'OK  ' if ok else 'FAIL'} {code}  {final}  |  {meta.get('title', '')}")
        if a.summary and ok:
            print(f"      {d['data'].get('summary', '')}")
    return 1 if bad else 0


def cmd_download(a) -> int:
    dest = Path(a.out)
    dest.mkdir(parents=True, exist_ok=True)
    bad = 0
    for u in a.urls:
        name = "site-" + re.sub(r"[^a-z0-9.]+", "-", Path(urlparse(u).path).name.lower())
        target = dest / name
        r = subprocess.run(["curl", "-sfL", "-A", UA, "-o", str(target), u], capture_output=True, timeout=120)
        if r.returncode or not target.exists() or target.stat().st_size == 0:
            print(f"FAIL {u}", file=sys.stderr)
            bad += 1
        else:
            print(f"OK   {target}  ({target.stat().st_size // 1024} KB)  <- {u}")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("images", help="list content images on a page")
    s.add_argument("page")
    s.add_argument("--grep", nargs="*", default=[])
    s.add_argument("--all", action="store_true", help="keep nav icons, logos and badges")
    s.set_defaults(fn=cmd_images)

    s = sub.add_parser("links", help="list accuknox.com URLs linked from a page")
    s.add_argument("page")
    s.add_argument("--grep", nargs="*", default=[])
    s.set_defaults(fn=cmd_links)

    s = sub.add_parser("cite", help="confirm a URL answers 200 and print its title")
    s.add_argument("pages", nargs="+")
    s.add_argument("--summary", action="store_true", help="also print a Firecrawl summary")
    s.set_defaults(fn=cmd_cite)

    s = sub.add_parser("download", help="save image files into a build folder")
    s.add_argument("urls", nargs="+")
    s.add_argument("--out", required=True)
    s.set_defaults(fn=cmd_download)

    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
