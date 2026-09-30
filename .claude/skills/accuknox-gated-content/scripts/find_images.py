#!/usr/bin/env python3
"""Find images for a gated PDF in the help docs and in references/PRODUCT UI.

Ranks by relevance to the query only. File dates never count, so an older
screenshot that matches the topic beats a newer one that does not.

Two local sources:

  docs     every image under docs/, with the alt text, the page that embeds it,
           the page title, the live help.accuknox.com URL, and whether the page
           sits in the mkdocs.yml nav
  ui       every image under references/PRODUCT UI, scored on folder and file name

Usage:
    python find_images.py "prompt firewall"
    python find_images.py "cspm dashboard" --source ui --top 10
    python find_images.py "kubearmor policy" --source docs --copy build/img
    python find_images.py "ai-spm" --json

Exit codes: 0 at least one match, 1 no match.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DOCS = REPO / "docs"
UI = REPO / "references" / "PRODUCT UI"
MKDOCS = REPO / "mkdocs.yml"
SITE = "https://help.accuknox.com/"
IMG_EXT = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif"}

MD_IMG = re.compile(r"!\[([^\]]*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_IMG = re.compile(r"<img\b[^>]*>", re.I)
ATTR = re.compile(r'(\w+)\s*=\s*["\']([^"\']*)["\']')
H1 = re.compile(r"^#\s+(.+)$", re.M)
TITLE_FM = re.compile(r"^title:\s*[\"']?(.+?)[\"']?\s*$", re.M)


def tokens(text: str) -> list[str]:
    return [t for t in re.split(r"[^a-z0-9]+", text.lower()) if len(t) > 1]


def hit(q: str, have: set[str]) -> bool:
    """Exact token, or a shared stem of 4+ letters, so "dash" meets "dashboard"."""
    if q in have:
        return True
    return any(len(h) >= 4 and len(q) >= 4 and (h.startswith(q) or q.startswith(h)) for h in have)


def score(query: list[str], fields: dict[str, str]) -> float:
    """Weighted token overlap. Alt text and file name count most."""
    weights = {"alt": 3.0, "name": 2.5, "title": 2.0, "folder": 1.5, "page": 1.0}
    total = 0.0
    for key, text in fields.items():
        have = set(tokens(text))
        total += weights.get(key, 1.0) * sum(1 for q in query if hit(q, have))
    # A phrase match on the joined query beats scattered tokens.
    phrase = " ".join(query)
    if any(phrase in " ".join(tokens(t)) for t in fields.values()):
        total += 4.0
    return total


def nav_pages() -> set[str]:
    if not MKDOCS.exists():
        return set()
    text = MKDOCS.read_text(encoding="utf-8", errors="replace")
    nav = text.split("\nnav:", 1)[-1]
    return set(re.findall(r"([\w./ -]+\.md)", nav))


def page_url(md: Path) -> str:
    rel = md.relative_to(DOCS).as_posix()
    rel = rel[:-3]
    if rel.endswith("index"):
        rel = rel[: -len("index")]
    else:
        rel += "/"
    return SITE + rel


def index_docs() -> list[dict]:
    nav = nav_pages()
    seen: dict[Path, dict] = {}
    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        m = TITLE_FM.search(text[:800]) or H1.search(text)
        title = m.group(1).strip() if m else md.stem
        refs = [(a, s) for a, s in MD_IMG.findall(text)]
        for tag in HTML_IMG.findall(text):
            attrs = dict((k.lower(), v) for k, v in ATTR.findall(tag))
            if "src" in attrs:
                refs.append((attrs.get("alt", ""), attrs["src"]))
        rel_md = md.relative_to(DOCS).as_posix()
        for alt, src in refs:
            if src.startswith(("http:", "https:", "data:")):
                continue
            img = (md.parent / src.split("#")[0].split("?")[0]).resolve()
            if not img.exists() or img.suffix.lower() not in IMG_EXT:
                continue
            entry = seen.setdefault(img, {
                "source": "docs", "path": str(img), "alt": alt.strip(),
                "title": title, "page": rel_md, "url": page_url(md),
                "in_nav": rel_md in nav,
            })
            if not entry["alt"] and alt.strip():
                entry["alt"] = alt.strip()
    # Images on disk that no page embeds still count, with less context.
    for img in DOCS.rglob("*"):
        if img.suffix.lower() in IMG_EXT and img.resolve() not in seen:
            seen[img.resolve()] = {
                "source": "docs", "path": str(img.resolve()), "alt": "",
                "title": "", "page": "", "url": "", "in_nav": False,
            }
    return list(seen.values())


def index_ui() -> list[dict]:
    if not UI.exists():
        return []
    out = []
    for img in UI.rglob("*"):
        if img.suffix.lower() in IMG_EXT:
            out.append({
                "source": "ui", "path": str(img.resolve()), "alt": "",
                "title": "", "page": img.parent.relative_to(UI).as_posix(),
                "url": "", "in_nav": False,
            })
    return out


def rank(query: str, items: list[dict], top: int) -> list[dict]:
    q = tokens(query)
    ranked = []
    for it in items:
        p = Path(it["path"])
        s = score(q, {
            "alt": it["alt"], "name": p.stem, "title": it["title"],
            "folder": p.parent.name if it["source"] == "docs" else it["page"],
            "page": it["page"],
        })
        if s > 0:
            if it["in_nav"]:
                s += 0.5
            ranked.append({**it, "score": round(s, 1)})
    ranked.sort(key=lambda r: (-r["score"], r["path"]))
    return ranked[:top]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("query")
    ap.add_argument("--source", choices=["docs", "ui", "all"], default="all")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--copy", metavar="DIR", help="copy the ranked images into DIR")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    items: list[dict] = []
    if a.source in ("docs", "all"):
        items += index_docs()
    if a.source in ("ui", "all"):
        items += index_ui()
    hits = rank(a.query, items, a.top)

    if a.copy:
        dest = Path(a.copy)
        dest.mkdir(parents=True, exist_ok=True)
        for h in hits:
            src = Path(h["path"])
            name = re.sub(r"[^a-z0-9.]+", "-", f"{h['source']}-{src.parent.name}-{src.name}".lower())
            shutil.copy2(src, dest / name)
            h["copied_to"] = str(dest / name)

    if a.json:
        print(json.dumps(hits, indent=2))
    else:
        for h in hits:
            where = h["url"] or h["page"]
            nav = " nav" if h["in_nav"] else ""
            print(f"{h['score']:>5}  [{h['source']}{nav}]  {h['path']}")
            if h["alt"] or where:
                print(f"       alt: {h['alt'] or '-'}  |  {where}")
    return 0 if hits else 1


if __name__ == "__main__":
    sys.exit(main())
