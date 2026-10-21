#!/usr/bin/env python3
"""Pull the text out of a source file a blog is built from.

Reads `.pdf`, `.docx`, `.pptx` and plain text. It needs no poppler, no
python-docx and no python-pptx, so it runs on this machine as is. PDF uses
PyMuPDF (`fitz`). A docx or pptx is a zip of XML, and this reads the XML.

The Read tool cannot open a PDF here because `pdftoppm` is missing, and the
console codepage breaks on arrows and smart quotes. This script always writes
UTF-8, to a file, so neither problem reaches you.

Usage:
    python extract_text.py "D:/Downloads/paper.pdf"
    python extract_text.py deck.pptx --out notes.txt
    python extract_text.py paper.pdf --pages 1-5

Default output is `<name>.txt` in the system temp folder. The path prints on the
last line, and you open it with the Read tool.

A PRD, a roadmap deck or a summary memo is an internal source. Use it to learn
the product direction, and publish only what a public doc, a release note or the
accuknox.com site also states. Write the rest as a visible bracket.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
import tempfile
import zipfile
from pathlib import Path


def ooxml(path: Path, pattern: str) -> str:
    z = zipfile.ZipFile(path)

    def order(name: str) -> int:
        nums = re.findall(r"\d+", name)
        return int(nums[-1]) if nums else 0

    parts = sorted((n for n in z.namelist() if re.match(pattern, n)), key=order)
    out = []
    for n in parts:
        xml = z.read(n).decode("utf-8")
        xml = re.sub(r"</a:p>|</w:p>", "\n", xml)
        text = html.unescape(re.sub(r"<[^>]+>", "", xml)).strip()
        out.append(f"--- {n}\n{text}")
    return "\n\n".join(out)


def pdf_text(path: Path, pages: str | None) -> str:
    try:
        import fitz  # PyMuPDF
    except ImportError:
        raise SystemExit("PyMuPDF is missing. Run this with `py -3.11` or "
                         "`python`, both have it on this machine.")
    doc = fitz.open(path)
    lo, hi = 1, len(doc)
    if pages:
        m = re.fullmatch(r"(\d+)(?:-(\d+))?", pages)
        if not m:
            raise SystemExit("--pages takes N or N-M")
        lo = int(m.group(1))
        hi = int(m.group(2) or lo)
    out = [f"pages {len(doc)}"]
    for i in range(lo, min(hi, len(doc)) + 1):
        out.append(f"--- page {i}\n{doc[i - 1].get_text()}")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--pages", help="PDF only, such as 1-5")
    args = ap.parse_args()

    if not args.source.exists():
        print(f"no such file: {args.source}", file=sys.stderr)
        return 2
    ext = args.source.suffix.lower()
    if ext == ".pdf":
        text = pdf_text(args.source, args.pages)
    elif ext == ".docx":
        text = ooxml(args.source, r"word/document\.xml")
    elif ext == ".pptx":
        text = ooxml(args.source, r"ppt/slides/slide\d+\.xml")
    elif ext in (".txt", ".md"):
        text = args.source.read_text("utf-8", errors="replace")
    else:
        print(f"unsupported type: {ext}", file=sys.stderr)
        return 2

    out = args.out or Path(tempfile.gettempdir()) / f"{args.source.stem}.txt"
    out.write_text(text, encoding="utf-8", newline="\n")
    print(f"{len(text.split())} words")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
