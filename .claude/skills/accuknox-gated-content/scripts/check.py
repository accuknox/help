#!/usr/bin/env python3
"""Check a gated PDF's HTML against the content rules before it renders.

Fails on:
  - placeholder text: {{ }}, TBD, [INSERT], lorem
  - em dash, en dash, semicolon, emoji or hashtag in visible text
  - a hyphenated compound in visible text (URLs and code excluded)
  - a banned filler word
  - a colon in a heading
  - a link to accuknox.com without utm_source=gated-pdf, utm_medium=pdf and utm_campaign
  - an image src that does not exist on disk, or a remote image
  - a page with a stat numeral and no source line on the same page
  - a font-family other than Inter

Usage:
    python check.py references/drafts/gated-content/<slug>/build/report.html

Exit codes: 0 clean, 1 at least one failure.
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

BANNED = ["cutting-edge", "cutting edge", "streamline", "game-changer", "game changer", "powerful",
          "delve", "leverage", "robust", "seamless", "ensure", "comprehensive", "state-of-the-art",
          "revolutionize", "furthermore", "moreover", "additionally"]
PLACEHOLDER = re.compile(r"\{\{|\}\}|\bTBD\b|\[INSERT|lorem ipsum", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
COMPOUND = re.compile(r"\b[A-Za-z]+-[A-Za-z]+\b")
# Product and standard names that carry a hyphen by definition.
COMPOUND_OK = {"ai-spm", "ai-dr", "nist-800", "iso-27001", "e-mail", "k8s-native", "x-ray", "pci-dss", "cis-benchmark"}
STAT_CLASSES = {"stat", "stat-m", "stat-s", "v"}


class Page:
    def __init__(self, n: int):
        self.n = n
        self.text: list[str] = []
        self.has_stat = False
        self.has_src = False


class Walker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pages: list[Page] = []
        self.stack: list[tuple[str, set]] = []
        self.skip = 0
        self.heading = 0
        self.headings: list[tuple[int, str]] = []
        self.links: list[tuple[int, str]] = []
        self.imgs: list[tuple[int, str]] = []
        self.buf = ""

    @property
    def page(self) -> Page | None:
        return self.pages[-1] if self.pages else None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = set((a.get("class") or "").split())
        if tag == "section" and "page" in cls:
            self.pages.append(Page(len(self.pages) + 1))
        if tag in ("style", "script"):
            self.skip += 1
        n = self.page.n if self.page else 0
        if self.page and cls & STAT_CLASSES:
            self.page.has_stat = True
        if self.page and cls & {"src", "shot-cap"}:
            self.page.has_src = True
        if tag in ("h1", "h2", "h3"):
            self.heading += 1
            self.buf = ""
        if tag == "a" and a.get("href"):
            self.links.append((n, a["href"]))
        if tag == "img" and a.get("src"):
            self.imgs.append((n, a["src"]))
        if tag not in ("img", "br", "hr", "meta", "link", "path", "circle", "polygon", "stop"):
            self.stack.append((tag, cls))

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self.skip -= 1
        if tag in ("h1", "h2", "h3") and self.heading:
            self.heading -= 1
            self.headings.append((self.page.n if self.page else 0, self.buf.strip()))
        while self.stack:
            t, _ = self.stack.pop()
            if t == tag:
                break

    def handle_data(self, data):
        if self.skip or not self.page:
            return
        self.page.text.append(data)
        if self.heading:
            self.buf += data


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    path = Path(sys.argv[1]).resolve()
    raw = path.read_text(encoding="utf-8")
    w = Walker()
    w.feed(raw)
    fails: list[str] = []

    for m in re.finditer(r"font-family\s*:\s*([^;}\"]+)", raw):
        fam = [f.strip(" '\"") for f in m.group(1).split(",")]
        if any(f.lower() != "inter" for f in fam):
            fails.append(f"font-family other than Inter: {m.group(0)}")

    for p in w.pages:
        text = re.sub(r"\s+", " ", " ".join(p.text))
        text_no_urls = re.sub(r"\S+\.(com|io|org|net|ai)\S*", "", text)
        for rx, why in [(PLACEHOLDER, "placeholder"), (re.compile("[—–]"), "em or en dash"),
                        (re.compile(";"), "semicolon"), (EMOJI, "emoji"), (re.compile(r"(^|\s)#\w"), "hashtag")]:
            for m in rx.finditer(text):
                fails.append(f"p{p.n} {why}: ...{text[max(0, m.start() - 30):m.end() + 30]}...")
        for m in COMPOUND.finditer(text_no_urls):
            if m.group(0).lower() not in COMPOUND_OK:
                fails.append(f"p{p.n} hyphenated compound: {m.group(0)}")
        low = text.lower()
        for b in BANNED:
            if re.search(rf"\b{re.escape(b)}", low):
                fails.append(f"p{p.n} banned word: {b}")
        if p.has_stat and not p.has_src:
            fails.append(f"p{p.n} has a stat numeral but no .src source line on the page")

    for n, h in w.headings:
        if ":" in h:
            fails.append(f"p{n} colon in heading: {h}")

    for n, href in w.links:
        u = urlparse(href)
        if "accuknox.com" in u.netloc and "help.accuknox.com" not in u.netloc:
            q = parse_qs(u.query)
            if q.get("utm_source") != ["gated-pdf"] or q.get("utm_medium") != ["pdf"] or not q.get("utm_campaign"):
                fails.append(f"p{n} CTA link missing UTM parameters: {href}")

    for n, src in w.imgs:
        if src.startswith(("http:", "https:")):
            fails.append(f"p{n} remote image, download it into img/ first: {src}")
        elif not (path.parent / src).exists():
            fails.append(f"p{n} image not found: {src}")

    if not w.pages:
        fails.append("no <section class=\"page\"> found")

    for f in fails:
        print("FAIL", f)
    print(f"{len(w.pages)} pages, {len(fails)} failures")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
