#!/usr/bin/env python3
"""Find a real image for a blog post, then crop it clean.

`find` searches every place a usable picture lives, by keyword, and prints the
path, the pixel size and the alt text or description that goes with it:

1. the help-doc pages, which carry alt text on every image (`docs/`)
2. the curated demo screenshots (`references/assets/demo-screenshots/`)
3. the PRODUCT UI Drive index (`media/INDEX.md`, binaries mirror locally)

`prep` converts and crops one file into the draft's image folder. It reads
webp, writes png, cuts a box you give it and downscales anything wider than
1600 px. It never touches the original.

Usage:
    python images.py find agentz trace
    python images.py find "prompt firewall" --limit 10
    python images.py prep SRC.webp OUT.png --crop 38,424,1068,1032

Look at the crop afterward. A screenshot can carry a tenant name or a token,
and `.claude/core/runtime-contract.md` bans both.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg")

MD_IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)")
HTML_IMG = re.compile(r"<img\b[^>]*>", re.I)


def size(path: Path) -> str:
    if Image is None or path.suffix.lower() == ".svg":
        return "-"
    try:
        with Image.open(path) as im:
            return f"{im.size[0]}x{im.size[1]}"
    except Exception:  # noqa: BLE001
        return "?"


def doc_hits(words: list[str]):
    """Every image a docs page uses, with its alt text, filtered by keyword."""
    seen: set[Path] = set()
    for md in (REPO / "docs").rglob("*.md"):
        text = md.read_text("utf-8", errors="ignore")
        found = [(a, s) for a, s in MD_IMG.findall(text)]
        for tag in HTML_IMG.findall(text):
            s = re.search(r'src="([^"]+)"', tag)
            a = re.search(r'alt="([^"]*)"', tag)
            if s:
                found.append((a.group(1) if a else "", s.group(1)))
        for alt, src in found:
            if src.startswith(("http", "data:")):
                continue
            target = (md.parent / src.split("#")[0]).resolve()
            if target in seen or target.suffix.lower() not in EXT:
                continue
            hay = f"{alt} {target.parent.name} {target.name} {md.stem}".lower()
            if all(w in hay for w in words) and target.exists():
                seen.add(target)
                yield target, alt or md.stem


def listing_hits(file: Path, words: list[str]):
    if not file.exists():
        return
    for line in file.read_text("utf-8", errors="ignore").splitlines():
        if all(w in line.lower() for w in words):
            yield line.strip()


def cmd_find(args: argparse.Namespace) -> int:
    words = [w.lower() for w in " ".join(args.keywords).split()]
    n = 0
    print("help-doc images (real console shots with alt text)")
    for path, alt in doc_hits(words):
        rel = path.relative_to(REPO).as_posix()
        print(f"  {size(path):>10}  {rel}\n              {alt[:110]}")
        n += 1
        if n >= args.limit:
            break
    print("\ncurated demo screenshots")
    shown = 0
    for line in listing_hits(
            REPO / "references/assets/demo-screenshots/DEMO-SUMMARY.md", words):
        print("  " + line[:140])
        shown += 1
        if shown >= args.limit:
            break
    print("\nPRODUCT UI Drive index (run drive_sync.py pull to fetch)")
    shown = 0
    for line in listing_hits(ROOT / "media/INDEX.md", words):
        print("  " + line[:140])
        shown += 1
        if shown >= args.limit:
            break
    return 0


def cmd_prep(args: argparse.Namespace) -> int:
    if Image is None:
        print("pip install pillow", file=sys.stderr)
        return 2
    src, out = Path(args.src), Path(args.out)
    im = Image.open(src).convert("RGB")
    if args.crop:
        x0, y0, x1, y1 = (int(v) for v in args.crop.split(","))
        im = im.crop((x0, y0, x1, y1))
    if im.size[0] > args.max_width:
        h = round(im.size[1] * args.max_width / im.size[0])
        im = im.resize((args.max_width, h), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, optimize=True)
    print(f"{out}  {im.size[0]}x{im.size[1]}  {out.stat().st_size // 1024} KB")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("find", help="search every image source by keyword")
    f.add_argument("keywords", nargs="+")
    f.add_argument("--limit", type=int, default=15)
    f.set_defaults(fn=cmd_find)
    p = sub.add_parser("prep", help="convert, crop and downscale one image")
    p.add_argument("src")
    p.add_argument("out")
    p.add_argument("--crop", help="x0,y0,x1,y1 in source pixels")
    p.add_argument("--max-width", type=int, default=1600)
    p.set_defaults(fn=cmd_prep)
    args = ap.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    raise SystemExit(main())
