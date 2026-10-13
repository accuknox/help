#!/usr/bin/env python3
"""Rebuild the cheat sheet cover and every asset made from it.

Cover layout: logo at the top, the title under it, the deck under the title,
and the module art at the bottom right. The cover carries no other text.

Each module keeps its art in build/<module>/cover-art.pdf, a vector page of
446 x 432 pt. A module with build/<module>/cover-art.html renders that file
into cover-art.pdf first.

Per module the script writes:
  output/<drive name>.pdf             the cheat sheet, new cover on page 1
  output/<slug>-form-image.png        page 1 at 1200 px wide
  build/<module>/social/<thumb>.png   page 1 for the LinkedIn card
  output/<slug>-linkedin.png          the LinkedIn card

Usage:
    python cover.py              every module
    python cover.py aspm cspm    named modules
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import fitz  # PyMuPDF
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import MODULES, OUT, BUILD  # noqa: E402

# The PDF names in the shared Drive folder. Keep them exactly, because the
# landing pages point at these files.
DRIVE_NAMES = {
    "ai-security": "2026-10-07-ai-security-best-practices-guide-v7.pdf",
    "api-security": "2026-10-07-api-security-best-practices-guide-v5.pdf",
    "aspm": "2026-10-07-aspm-best-practices-guide-v7.pdf",
    "ciem": "2026-10-07-ciem-best-practices-guide-v7.pdf",
    "compliance": "2026-10-07-cloud-compliance-best-practices-guide-v6.pdf",
    "cspm": "2026-10-07-cspm-best-practices-guide-v8.pdf",
    "cwpp": "2026-10-07-cwpp-best-practices-guide-v6.pdf",
    "dspm": "2026-10-07-dspm-best-practices-guide-v6.pdf",
    "kspm": "2026-10-07-kubernetes-security-best-practices-guide-v7.pdf",
    "secrets-manager": "2026-10-07-secrets-management-best-practices-guide-v5.pdf",
}

COVER = """<section class="page bg-navy">
  <img src="../_kit/logo-cover.png" alt="AccuKnox" style="position:absolute;left:17mm;top:20mm;height:9mm">
  <div style="position:absolute;left:17mm;right:17mm;top:44mm">
    <h1 class="h-display">{title}</h1>
    <p class="deck" style="color:rgba(255,255,255,.7);font-size:18pt;max-width:150mm">{deck}</p>
  </div>
</section>"""

ART_SCALE = 0.95  # art box width on the page = 446 pt x scale
ART_BLEED = 12    # pt the art box runs past the bottom edge
GAP = 18          # pt of clear space required between the deck and the art


def new_cover(html: str) -> str:
    """Swap the first navy section for the new cover, keeping title and deck."""
    m = re.search(r'<section class="page bg-navy">.*?</section>', html, re.S)
    sec = m.group(0)
    title = re.search(r'<h1 class="h-display">(.*?)</h1>', sec, re.S).group(1)
    deck = re.search(r'<p class="deck"[^>]*>(.*?)</p>', sec, re.S).group(1)
    return html[:m.start()] + COVER.format(title=title, deck=deck) + html[m.end():]


def art_pdf(folder: Path, browser) -> Path:
    art = folder / "cover-art.pdf"
    src = folder / "cover-art.html"
    if src.exists():
        pg = browser.new_page()
        pg.goto(src.as_uri())
        pg.wait_for_timeout(300)
        pg.pdf(path=str(art), width="157.34mm", height="152.4mm", print_background=True)
        pg.close()
    return art


def build(folder_name: str, slug: str, browser) -> None:
    folder = BUILD / folder_name
    report = folder / "report.html"
    report.write_text(new_cover(report.read_text(encoding="utf-8")), encoding="utf-8")

    tmp = folder / "qa" / "_render.pdf"
    tmp.parent.mkdir(exist_ok=True)
    pg = browser.new_page(viewport={"width": 794, "height": 1123})
    pg.goto(report.as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    pg.emulate_media(media="print")
    pg.pdf(path=str(tmp), format="A4", print_background=True, prefer_css_page_size=True,
           margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
    pg.close()

    doc = fitz.open(tmp)
    page = doc[0]
    art = fitz.open(art_pdf(folder, browser))
    w, h = art[0].rect.width * ART_SCALE, art[0].rect.height * ART_SCALE
    box = fitz.Rect(page.rect.x1 - w, page.rect.y1 - h + ART_BLEED, page.rect.x1, page.rect.y1 + ART_BLEED)
    text_bottom = max(b[3] for b in page.get_text("blocks"))
    if text_bottom + GAP > box.y0:
        raise SystemExit(f"{folder_name}: deck ends at {text_bottom:.0f} pt, art starts at {box.y0:.0f} pt")
    page.show_pdf_page(box, art, 0)

    target = OUT / DRIVE_NAMES[folder_name]
    doc.save(target, garbage=4, deflate=True)
    doc.close()
    tmp.unlink()

    cover = fitz.open(target)[0]
    cover.get_pixmap(matrix=fitz.Matrix(1200 / cover.rect.width, 1200 / cover.rect.width)).save(OUT / f"{slug}-form-image.png")
    cover.get_pixmap(matrix=fitz.Matrix(2 * 794 / cover.rect.width, 2 * 794 / cover.rect.width)).save(folder / "qa" / "page-01.png")

    social = folder / "social"
    li = social / "linkedin.html"
    thumb = re.search(r'<img class="(?:thumb|cover)" src="([^"]+)"', li.read_text(encoding="utf-8")).group(1)
    cover.get_pixmap(matrix=fitz.Matrix(2 * 794 / cover.rect.width, 2 * 794 / cover.rect.width)).save(social / thumb)
    pg = browser.new_page(viewport={"width": 1200, "height": 1200})
    pg.goto(li.as_uri())
    pg.wait_for_timeout(600)
    pg.screenshot(path=str(OUT / f"{slug}-linkedin.png"))
    pg.close()
    print(f"{folder_name}: {target.name}, deck ends {text_bottom:.0f} pt, art from {box.y0:.0f} pt")


def main() -> int:
    want = set(sys.argv[1:])
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for folder, _name, slug in MODULES:
            if not want or folder in want:
                build(folder, slug, browser)
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
