#!/usr/bin/env python3
"""Render a gated PDF with Playwright Chromium, then run the QA checks.

Checks after render:
  1. Every section is exactly one A4 page (595 x 842 pt), and the page count
     equals the section count.
  2. Inter is the only font embedded in the PDF.
  3. No element spills past its page, and no content runs into the footer band.
  4. Every page rasterizes into <build>/qa/ as a contact sheet, six pages per sheet, for
     the visual pass. Read each sheet before you deliver.

Never overwrites a PDF. If the target name exists, the script stops and asks for
the next version number.

Usage:
    python render.py <build>/report.html <out>/2026-10-01-runtime-security-report-v1.pdf

Exit codes: 0 clean, 1 a QA check failed, 2 render failed or target exists.
"""

from __future__ import annotations

import sys
from pathlib import Path

import fitz  # PyMuPDF
from PIL import Image
from playwright.sync_api import Error as PWError
from playwright.sync_api import sync_playwright

# Collects overflow and footer collisions per page, in CSS px (96 per inch).
PROBE = r"""
() => {
  const mm = 96 / 25.4, out = [];
  document.querySelectorAll('section.page').forEach((pg, i) => {
    const r = pg.getBoundingClientRect();
    const foot = pg.querySelector('.foot');
    const footTop = foot ? foot.getBoundingClientRect().top : r.bottom - 11 * mm;
    pg.querySelectorAll('*').forEach(el => {
      if (el.closest('.art') || el.closest('.foot') || el.classList.contains('art')) return;
      const cs = getComputedStyle(el);
      if (cs.position === 'absolute' && el.classList.contains('bottom')) return;
      const b = el.getBoundingClientRect();
      if (!b.width || !b.height || !el.childElementCount && !el.textContent.trim() && el.tagName !== 'IMG') return;
      const tag = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : '');
      if (b.bottom > r.bottom + 1 || b.right > r.right + 1) out.push(`p${i + 1} spills off the page: ${tag}`);
      else if (foot && b.bottom > footTop - 2 && b.top < footTop) out.push(`p${i + 1} runs into the footer: ${tag}`);
    });
    const fam = getComputedStyle(pg).fontFamily;
    if (!/Inter/.test(fam)) out.push(`p${i + 1} font-family is ${fam}`);
  });
  return {pages: document.querySelectorAll('section.page').length, issues: [...new Set(out)]};
}
"""


def render(src: Path, out: Path) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 794, "height": 1123})
        page.goto(src.as_uri(), wait_until="load", timeout=60000)
        page.evaluate("document.fonts.ready")
        loaded = page.evaluate("[...document.fonts].filter(f => f.status === 'loaded').map(f => f.family)")
        page.emulate_media(media="print")
        probe = page.evaluate(PROBE)
        page.pdf(path=str(out), format="A4", print_background=True, prefer_css_page_size=True,
                 margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        browser.close()
    probe["loaded"] = loaded
    return probe


def qa(out: Path, probe: dict, qa_dir: Path) -> list[str]:
    fails = list(probe["issues"])
    if not any("Inter" in f for f in probe["loaded"]):
        fails.append("Inter did not load in the browser. Check fonts/InterVariable.ttf sits next to report.html")
    doc = fitz.open(out)
    if doc.page_count != probe["pages"]:
        fails.append(f"PDF has {doc.page_count} pages for {probe['pages']} sections. A section overflowed")
    fonts = set()
    for i, pg in enumerate(doc):
        w, h = round(pg.rect.width), round(pg.rect.height)
        if (w, h) != (595, 842):
            fails.append(f"p{i + 1} is {w} x {h} pt, not A4")
        fonts |= {f[3] for f in pg.get_fonts()}
    stray = [f for f in fonts if "Inter" not in f]
    if stray:
        fails.append(f"fonts other than Inter embedded: {', '.join(sorted(stray))}")

    qa_dir.mkdir(exist_ok=True)
    thumbs = [Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
              for pix in (pg.get_pixmap(dpi=60) for pg in doc)]
    for s in range(0, len(thumbs), 6):
        batch = thumbs[s:s + 6]
        tw, th = batch[0].size
        sheet = Image.new("RGB", (tw * 3 + 40, th * 2 + 30), "#9aa5ad")
        for j, t in enumerate(batch):
            sheet.paste(t, (10 + (j % 3) * (tw + 10), 10 + (j // 3) * (th + 10)))
        sheet.save(qa_dir / f"sheet-{s // 6 + 1:02d}.png")
    for i, pg in enumerate(doc):
        pg.get_pixmap(dpi=110).save(qa_dir / f"page-{i + 1:02d}.png")
    doc.close()
    return fails


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if out.exists():
        print(f"{out.name} exists. Never overwrite a version. Raise the -vN suffix and rerun.")
        return 2
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        probe = render(src, out)
    except PWError as e:
        print(f"Render failed: {e}")
        return 2
    fails = qa(out, probe, src.parent / "qa")
    for f in fails:
        print("FAIL", f)
    print(f"{'Wrote' if not fails else 'Wrote with QA failures'} {out}  ({probe['pages']} pages)")
    print(f"Contact sheets and page images in {src.parent / 'qa'}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
