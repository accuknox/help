#!/usr/bin/env python3
"""Turn a blog draft into the HTML that Google Drive imports as a Google Doc.

Google Drive converts an uploaded `text/html` file into a native Google Doc and
keeps headings, tables, bold, italics and hyperlinks. Uploading raw markdown
loses all of it, so always convert first.

The front matter is rendered as a table at the top of the document rather than
dropped, because the SEO fields are the part the marketing team copies into
WordPress.

Usage:
    python to_gdoc_html.py draft.md                 # writes draft.gdoc.html
    python to_gdoc_html.py draft.md -o out.html
    python to_gdoc_html.py draft.md --print-title   # the Google Doc title only

Then upload with the Google Drive connector:
    create_file(title=<--print-title output>,
                textContent=<the HTML>,
                contentMimeType="text/html")
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:  # pragma: no cover
    print("pip install markdown  (python 3.10 on this machine has it)",
          file=sys.stderr)
    raise

# No `nl2br`. A hard-wrapped markdown paragraph would otherwise arrive in the
# Google Doc with a line break after every source line.
EXTENSIONS = ["tables", "fenced_code", "sane_lists", "attr_list"]

CSS = """
body { font-family: Arial, sans-serif; font-size: 11pt; line-height: 1.5;
       color: #0D1B4B; }
h1 { font-size: 22pt; color: #11206D; }
h2 { font-size: 16pt; color: #11206D; margin-top: 22pt; }
h3 { font-size: 13pt; color: #003BF6; margin-top: 16pt; }
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
blockquote { border-left: 3px solid #4D4DD9; margin-left: 0; padding-left: 12pt;
             color: #595959; }
em { color: #595959; }
.meta th { width: 26%; }
"""


def split_front_matter(text: str) -> tuple[list[tuple[str, str]], str]:
    if not text.startswith("---"):
        return [], text
    end = text.find("\n---", 3)
    if end < 0:
        return [], text
    raw, body = text[3:end], text[end + 4:].lstrip("\n")
    pairs: list[tuple[str, str]] = []
    key = None
    for line in raw.splitlines():
        m = re.match(r"^([a-z_][a-z0-9_]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            pairs.append([key, m.group(2).strip()])  # type: ignore[arg-type]
        elif key and line.strip() and pairs:
            pairs[-1][1] = (pairs[-1][1] + " " + line.strip()).strip()  # type: ignore[index]
    cleaned = []
    for k, v in pairs:  # type: ignore[misc]
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


def convert(md_text: str, fallback_title: str) -> tuple[str, str]:
    pairs, body = split_front_matter(md_text)
    title = doc_title(pairs, body, fallback_title)
    # Drop a duplicate H1 so the Google Doc does not repeat the title.
    body = re.sub(r"^#\s+.*$", "", body, count=1, flags=re.M).lstrip("\n")
    inner = markdown.markdown(body, extensions=EXTENSIONS, output_format="html5")
    inner = code_as_tables(inner)
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

    title, page = convert(args.draft.read_text("utf-8"), args.draft.stem)
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
