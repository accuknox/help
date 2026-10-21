#!/usr/bin/env python3
"""Turn a blog draft into the HTML that Google Drive imports as a Google Doc.

Google Drive converts an uploaded `text/html` file into a native Google Doc and
keeps headings, tables, bold, italics, hyperlinks and inline images. Uploading
raw markdown loses all of it, so always convert first.

Three things this converter does on purpose:

- Line height is 1 everywhere. Google Docs reads `line-height: 1` as single
  spacing (lineSpacing 100), the tightest the format offers. `push_gdoc.py`
  checks it again after the import.
- A local image (`![alt](images/x.png)`) becomes a base64 data URI sized to at
  most 620 px wide, so the Doc carries the picture and nothing needs a public
  URL. A remote image keeps its URL.
- The front matter renders as an `SEO metadata` table at the top, because that
  block is what marketing copies into WordPress.

Usage:
    python to_gdoc_html.py draft.md                 # writes draft.gdoc.html
    python to_gdoc_html.py draft.md -o out.html
    python to_gdoc_html.py draft.md --print-title   # the Google Doc title only

To upload, run `push_gdoc.py`. It calls this module, then `gws`.
"""

from __future__ import annotations

import argparse
import base64
import html
import io
import mimetypes
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover
    print("pip install markdown  (python 3.10 on this machine has it)",
          file=sys.stderr)
    raise

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    Image = None  # images still embed, at their stored size

# No `nl2br`. A hard-wrapped markdown paragraph would otherwise arrive in the
# Google Doc with a line break after every source line.
EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list"]

MAX_IMG_WIDTH = 620   # CSS px. Google Docs shows 620 px as 465 pt, the page width.
MAX_STORED_WIDTH = 1600  # downscale anything wider before embedding

CSS = """
* { line-height: 1; }
body { font-family: Arial, sans-serif; font-size: 11pt; color: #0D1B4B; }
p { margin: 0 0 8pt 0; }
li { margin: 0 0 3pt 0; }
h1 { font-size: 22pt; color: #11206D; margin: 0 0 10pt 0; }
h2 { font-size: 16pt; color: #11206D; margin: 18pt 0 6pt 0; }
h3 { font-size: 13pt; color: #003BF6; margin: 12pt 0 4pt 0; }
table { border-collapse: collapse; width: 100%; }
th, td { border: 1px solid #B9C0DE; padding: 6pt 8pt; text-align: left;
         vertical-align: top; font-size: 10pt; }
th { background: #EEF1FB; color: #11206D; font-weight: bold; }
code { font-family: 'Courier New', monospace; font-size: 9.5pt;
       background: #F4F6FC; }
table.code { border-collapse: collapse; width: 100%; margin: 10pt 0; }
table.code td { background: #F4F6FC; border: 1px solid #B9C0DE;
                padding: 8pt 10pt; font-family: 'Courier New', monospace;
                font-size: 9.5pt; white-space: pre-wrap; }
blockquote { border-left: 3px solid #4D4DD9; margin: 0 0 8pt 0;
             padding-left: 12pt; color: #595959; }
em { color: #595959; }
img { display: block; }
.meta th { width: 26%; }
"""


def split_front_matter(text: str) -> tuple[list[tuple[str, str]], str]:
    if not text.startswith("---"):
        return [], text
    end = text.find("\n---", 3)
    if end < 0:
        return [], text
    raw, body = text[3:end], text[end + 4:].lstrip("\n")
    pairs: list[list[str]] = []
    key = None
    for line in raw.splitlines():
        m = re.match(r"^([a-z_][a-z0-9_]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            pairs.append([key, m.group(2).strip()])
        elif key and line.strip() and pairs:
            pairs[-1][1] = (pairs[-1][1] + " " + line.strip()).strip()
    cleaned = []
    for k, v in pairs:
        v = v.strip()
        if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        cleaned.append((k, v.lstrip(">|").strip()))
    return cleaned, body


def doc_title(pairs: list[tuple[str, str]], body: str, fallback: str) -> str:
    for key in ("title", "seo_title"):
        for k, v in pairs:
            if k == key and v:
                return v
    m = re.search(r"^#\s+(.*)$", body, re.M)
    return m.group(1).strip() if m else fallback


def meta_table(pairs: list[tuple[str, str]]) -> str:
    if not pairs:
        return ""
    rows = "\n".join(
        f"<tr><th>{html.escape(k)}</th><td>{html.escape(v)}</td></tr>"
        for k, v in pairs)
    return ("<h2>SEO metadata</h2>\n"
            f'<table class="meta">{rows}</table>\n<hr/>\n')


PRE_BLOCK = re.compile(r"<pre><code[^>]*>(.*?)</code></pre>", re.S)


def code_as_tables(html_body: str) -> str:
    """Rewrite every `<pre>` block as a single-cell table.

    Google Docs imports `<pre>` as ordinary body text. The monospace font, the
    shading and the block boundary are all lost, which turns a kubectl command
    into a paragraph. A one-cell table survives the import intact, so the
    reader still sees a code block.
    """
    def repl(m: re.Match[str]) -> str:
        code = m.group(1).rstrip("\n")
        lines = code.split("\n")
        cell = "<br/>".join(
            line.replace(" ", "&nbsp;") if line.startswith(" ") else line
            for line in lines)
        return f'<table class="code"><tr><td>{cell}</td></tr></table>'
    return PRE_BLOCK.sub(repl, html_body)


IMG_TAG = re.compile(r"<img\b([^>]*?)\s*/?>", re.I)


def embed_image(path: Path) -> tuple[str, int, int]:
    """Return (data URI, width px, height px) for a local image."""
    raw = path.read_bytes()
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    w = h = 0
    if Image is not None:
        im = Image.open(io.BytesIO(raw))
        w, h = im.size
        if w > MAX_STORED_WIDTH:
            h = round(h * MAX_STORED_WIDTH / w)
            w = MAX_STORED_WIDTH
            im = im.resize((w, h), Image.LANCZOS)
            buf = io.BytesIO()
            fmt = "PNG" if mime == "image/png" else "JPEG"
            im.convert("RGB" if fmt == "JPEG" else im.mode).save(
                buf, fmt, optimize=True)
            raw = buf.getvalue()
    uri = f"data:{mime};base64,{base64.b64encode(raw).decode('ascii')}"
    if w > MAX_IMG_WIDTH:
        h = round(h * MAX_IMG_WIDTH / w)
        w = MAX_IMG_WIDTH
    return uri, w, h


def embed_images(inner: str, base_dir: Path | None) -> str:
    """Swap each local `<img src>` for a sized data URI."""
    def repl(m: re.Match[str]) -> str:
        attrs = m.group(1)
        src = re.search(r'src="([^"]*)"', attrs)
        if not src or base_dir is None:
            return m.group(0)
        s = html.unescape(src.group(1))
        if s.startswith(("http://", "https://", "data:")):
            return m.group(0)
        file = (base_dir / s).resolve()
        if not file.exists():
            raise FileNotFoundError(f"image not found: {file}")
        uri, w, h = embed_image(file)
        alt = re.search(r'alt="([^"]*)"', attrs)
        alt_attr = f' alt="{alt.group(1)}"' if alt else ""
        size = f' width="{w}" height="{h}"' if w and h else ""
        return f'<img{size}{alt_attr} src="{uri}">'
    return IMG_TAG.sub(repl, inner)


def convert(md_text: str, fallback_title: str,
            base_dir: Path | None = None) -> tuple[str, str]:
    pairs, body = split_front_matter(md_text)
    title = doc_title(pairs, body, fallback_title)
    # Drop a duplicate H1 so the Google Doc does not repeat the title.
    body = re.sub(r"^#\s+.*$", "", body, count=1, flags=re.M).lstrip("\n")
    inner = markdown.markdown(body, extensions=EXTENSIONS, output_format="html5")
    inner = code_as_tables(inner)
    inner = embed_images(inner, base_dir)
    page = (
        "<!DOCTYPE html><html><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(title)}</title><style>{CSS}</style></head><body>"
        f"<h1>{html.escape(title)}</h1>\n{meta_table(pairs)}{inner}"
        "</body></html>")
    return title, page


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", type=Path)
    ap.add_argument("-o", "--out", type=Path)
    ap.add_argument("--print-title", action="store_true")
    args = ap.parse_args()

    title, page = convert(args.draft.read_text("utf-8"), args.draft.stem,
                          args.draft.resolve().parent)
    if args.print_title:
        print(title)
        return 0
    out = args.out or args.draft.with_suffix(".gdoc.html")
    out.write_text(page, encoding="utf-8", newline="\n")
    print(f"{out}  {len(page)} bytes")
    print(f"title: {title}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
