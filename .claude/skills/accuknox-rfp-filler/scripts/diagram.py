"""Evidence diagrams for rows that have no matching screenshot.

    python diagram.py <workdir> <specs.json>     render every spec to <workdir>/gen/
    python diagram.py --demo <outdir>            render one of each kind

Each diagram is drawn once as a list of shapes, then written twice: an SVG you
can reuse anywhere, and a PNG for the workbook, since Excel does not render SVG
in a cell anchor. Both carry the AccuKnox header band and a source footer.

Spec, one object per diagram. Every value must come from the page in `source`.

    {"file": "sast09-mobile", "kind": "bars", "title": "...", "subtitle": "...",
     "source": "docs/support-matrix/sast-support-matrix.md",
     "rows": [["Java (Android)", 226], ["Kotlin (Android)", 77]], "unit": "rules",
     "note": "optional amber line stating a scope limit"}

kinds: bars (rows), flow (steps: [[head, body]]), items (entries: [[head, body]]),
       code (lines: [str]), matrix (columns: [str], cells: [[str]])
"""
import argparse
import base64
import os
import sys
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rfp_lib as L  # noqa: E402

W = 820
PAD = 32
BAND = 58


def rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


NAVY, ACCENT, ALERT, BODY, MUTED = (rgb(x) for x in (L.NAVY, L.ACCENT, L.ALERT, L.BODY, L.MUTED))
WHITE, CARD, LINE, CODEBG, AMBER = (255, 255, 255), (244, 245, 251), (221, 224, 238), (17, 22, 45), (156, 87, 0)
FONT_STACK = "Inter, 'Segoe UI', Arial, sans-serif"
MONO_STACK = "Consolas, 'Courier New', monospace"


def _font(size, bold=False, mono=False):
    names = (["consolab.ttf"] if bold else ["consola.ttf"]) if mono else \
            (["Inter-Bold.ttf", "segoeuib.ttf", "arialbd.ttf"] if bold else ["Inter-Regular.ttf", "segoeui.ttf", "arial.ttf"])
    for n in names:
        p = os.path.join(r"C:\Windows\Fonts", n)
        if os.path.isfile(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


class Canvas:
    """Collects shapes, then renders them to PNG and SVG."""

    def __init__(self):
        self.ops = []
        self._measure = ImageDraw.Draw(Image.new("RGB", (1, 1)))

    def rect(self, x, y, w, h, fill, stroke=None, r=0):
        self.ops.append(("rect", x, y, w, h, fill, stroke, r))

    def line(self, x1, y1, x2, y2, color, width=1):
        self.ops.append(("line", x1, y1, x2, y2, color, width))

    def circle(self, cx, cy, r, fill):
        self.ops.append(("circle", cx, cy, r, fill))

    def text(self, x, y, s, size, color, bold=False, mono=False, anchor="start"):
        self.ops.append(("text", x, y, s, size, color, bold, mono, anchor))

    def image(self, x, y, w, h, path):
        self.ops.append(("image", x, y, w, h, path))

    def width_of(self, s, size, bold=False, mono=False):
        return self._measure.textlength(s, font=_font(size, bold, mono))

    def wrap(self, s, size, maxw, bold=False):
        words, lines, cur = str(s).split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if self.width_of(t, size, bold) <= maxw:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines or [""]

    def png(self, path, h):
        im = Image.new("RGB", (W, h), WHITE)
        d = ImageDraw.Draw(im)
        for op in self.ops:
            k = op[0]
            if k == "rect":
                _, x, y, w, hh, fill, stroke, r = op
                d.rounded_rectangle([x, y, x + w, y + hh], radius=r, fill=fill, outline=stroke, width=1 if stroke else 0)
            elif k == "line":
                _, x1, y1, x2, y2, c, wd = op
                d.line([x1, y1, x2, y2], fill=c, width=wd)
            elif k == "circle":
                _, cx, cy, r, fill = op
                d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill)
            elif k == "text":
                _, x, y, s, size, c, bold, mono, anchor = op
                f = _font(size, bold, mono)
                if anchor == "middle":
                    x -= d.textlength(s, font=f) / 2
                elif anchor == "end":
                    x -= d.textlength(s, font=f)
                d.text((x, y - size), s, font=f, fill=c)
            elif k == "image":
                _, x, y, w, hh, p = op
                logo = Image.open(p).convert("RGBA").resize((int(w), int(hh)), Image.LANCZOS)
                im.paste(logo, (int(x), int(y)), logo)
        im.save(path)

    def svg(self, path, h):
        hexc = lambda c: "#%02x%02x%02x" % c  # noqa: E731
        out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">',
               f'<rect width="{W}" height="{h}" fill="#ffffff"/>']
        for op in self.ops:
            k = op[0]
            if k == "rect":
                _, x, y, w, hh, fill, stroke, r = op
                s = f' stroke="{hexc(stroke)}"' if stroke else ""
                out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{hh}" rx="{r}" fill="{hexc(fill)}"{s}/>')
            elif k == "line":
                _, x1, y1, x2, y2, c, wd = op
                out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{hexc(c)}" stroke-width="{wd}"/>')
            elif k == "circle":
                _, cx, cy, r, fill = op
                out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{hexc(fill)}"/>')
            elif k == "text":
                _, x, y, s, size, c, bold, mono, anchor = op
                fam = MONO_STACK if mono else FONT_STACK
                wt = ' font-weight="700"' if bold else ""
                out.append(f'<text x="{x}" y="{y - size * 0.18:.1f}" font-family="{fam}" font-size="{size}"{wt} '
                           f'fill="{hexc(c)}" text-anchor="{anchor}" xml:space="preserve">{escape(s)}</text>')
            elif k == "image":
                _, x, y, w, hh, p = op
                with open(p, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode()
                out.append(f'<image x="{x}" y="{y}" width="{w}" height="{hh}" href="data:image/png;base64,{b64}"/>')
        out.append("</svg>")
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(out))


def _frame(c, spec):
    c.rect(0, 0, W, BAND, NAVY)
    lw = 150
    c.image(W - PAD - lw, (BAND - lw * 118 / 500) / 2, lw, lw * 118 / 500, L.LOGO)
    c.text(PAD, 37, "Evidence diagram", 13, (190, 196, 240), bold=True)
    y = BAND + 40
    for ln in c.wrap(spec["title"], 24, W - 2 * PAD, bold=True):
        c.text(PAD, y, ln, 24, BODY, bold=True)
        y += 30
    if spec.get("subtitle"):
        for ln in c.wrap(spec["subtitle"], 15, W - 2 * PAD):
            c.text(PAD, y, ln, 15, MUTED)
            y += 21
    c.line(PAD, y + 4, W - PAD, y + 4, LINE)
    return y + 26


def _footer(c, y, spec):
    if spec.get("note"):
        for ln in c.wrap(spec["note"], 14, W - 2 * PAD):
            c.text(PAD, y + 14, ln, 14, AMBER, bold=True)
            y += 20
        y += 8
    y += 14
    c.line(PAD, y, W - PAD, y, LINE)
    src = spec["source"]
    if src.startswith("docs/"):
        src = L.doc_url(src)
    c.text(PAD, y + 26, f"Source: {src}", 13, MUTED)
    c.rect(0, y + 42, W, 6, ACCENT)
    return y + 48


def draw(spec):
    c = Canvas()
    y = _frame(c, spec)
    kind = spec["kind"]
    if kind == "bars":
        rows = spec["rows"]
        mx = max(v for _, v in rows) or 1
        labw = max(c.width_of(k, 15, True) for k, _ in rows) + 24
        for k, v in rows:
            c.text(PAD, y + 20, k, 15, BODY, bold=True)
            bw = max(6, (W - PAD * 2 - labw - 120) * v / mx)
            c.rect(PAD + labw, y + 4, bw, 24, ACCENT, r=4)
            c.text(PAD + labw + bw + 12, y + 21, f"{v} {spec.get('unit', '')}".strip(), 15, MUTED)
            y += 42
    elif kind in ("flow", "items"):
        key = "steps" if kind == "flow" else "entries"
        items = spec[key]
        for i, (head, body) in enumerate(items):
            left = PAD + (56 if kind == "flow" else 22)
            body_lines = c.wrap(body, 13, W - left - PAD - 16)
            hh = 34 + 18 * len(body_lines)
            c.rect(PAD, y, W - 2 * PAD, hh, CARD, LINE, r=8)
            if kind == "flow":
                c.circle(PAD + 28, y + hh / 2, 14, ACCENT)
                c.text(PAD + 28, y + hh / 2 + 6, str(i + 1), 15, WHITE, bold=True, anchor="middle")
            else:
                c.rect(PAD, y, 6, hh, ACCENT, r=0)
            c.text(left, y + 24, head, 15, BODY, bold=True)
            for j, ln in enumerate(body_lines):
                c.text(left, y + 44 + j * 18, ln, 13, MUTED)
            y += hh + 10
            if kind == "flow" and i < len(items) - 1:
                c.line(PAD + 28, y - 10, PAD + 28, y, LINE, 2)
    elif kind == "code":
        lines = spec["lines"]
        hh = 22 * len(lines) + 24
        c.rect(PAD, y, W - 2 * PAD, hh, CODEBG, r=8)
        for i, ln in enumerate(lines):
            col = (140, 214, 160) if ln.strip().startswith("#") else (232, 235, 248)
            c.text(PAD + 18, y + 30 + i * 22, ln, 14, col, mono=True)
        y += hh + 8
    elif kind == "matrix":
        cols = spec["columns"]
        cw = (W - 2 * PAD) / len(cols)
        c.rect(PAD, y, W - 2 * PAD, 32, NAVY, r=4)
        for i, h in enumerate(cols):
            c.text(PAD + 12 + i * cw, y + 22, h, 14, WHITE, bold=True)
        y += 32
        for r_i, row in enumerate(spec["cells"]):
            wrapped = [c.wrap(v, 13, cw - 20) for v in row]
            hh = 14 + 18 * max(len(w) for w in wrapped)
            c.rect(PAD, y, W - 2 * PAD, hh, CARD if r_i % 2 == 0 else WHITE, LINE)
            for i, lines in enumerate(wrapped):
                for j, ln in enumerate(lines):
                    c.text(PAD + 12 + i * cw, y + 20 + j * 18, ln, 13, BODY, bold=(i == 0))
            y += hh
        y += 8
    else:
        raise ValueError(f"unknown kind {kind}")
    h = _footer(c, y, spec)
    return c, int(h)


def render(spec, outdir):
    if not spec.get("source"):
        raise ValueError(f"{spec.get('file')}: every diagram needs a source page")
    if L.is_draft(spec["source"]):
        raise ValueError(f"{spec['file']}: source is an unpublished draft")
    os.makedirs(outdir, exist_ok=True)
    c, h = draw(spec)
    base = os.path.join(outdir, spec["file"])
    c.png(base + ".png", h)
    c.svg(base + ".svg", h)
    return base + ".png", base + ".svg"


DEMO = [
    {"file": "demo-bars", "kind": "bars", "title": "Mobile source coverage, Android and iOS",
     "subtitle": "Rule counts per language across both SAST engines",
     "source": "docs/support-matrix/sast-support-matrix.md", "unit": "rules",
     "rows": [["Java (Android)", 226], ["Kotlin (Android)", 77], ["Swift (iOS)", 13]],
     "note": "Source level analysis. APK and IPA binary scanning is not documented."},
    {"file": "demo-flow", "kind": "flow", "title": "Crawl and audit run as ordered phases",
     "subtitle": "Three phases, set by the scan type", "source": "docs/how-to/dast-scan-types.md",
     "steps": [["Traditional Spider and AJAX Spider", "Discovery, bounded by maxDuration, maxChildren and maxDepth"],
               ["Passive scan", "Analyses captured traffic and sends no attack payload"],
               ["Active scan", "Sends payloads using the Dev CICD, Dev Standard or Dev Full policy"]]},
    {"file": "demo-code", "kind": "code", "title": "Breaking a build on a severity threshold",
     "source": "docs/integrations/github-unified-code-analysis-tool.md",
     "lines": ["# Enforce, a non-zero exit breaks the build", "soft_fail: false", 'sast_severity: "HIGH,CRITICAL"']},
    {"file": "demo-matrix", "kind": "matrix", "title": "License classes and severity",
     "source": "docs/faqs/sbom.md", "columns": ["Severity", "License type", "Examples"],
     "cells": [["Low", "Permissive", "MIT, BSD-3-Clause, Apache-2.0"],
               ["Medium", "Weak Copyleft", "LGPL-3.0, MPL-2.0"],
               ["High", "Strong Copyleft", "GPL-3.0, AGPL-3.0"],
               ["Critical", "Banned or incompatible", "SSPL, CC-NC"]]},
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workdir", nargs="?")
    ap.add_argument("specs", nargs="?")
    ap.add_argument("--demo", metavar="OUTDIR")
    a = ap.parse_args()
    if a.demo:
        specs, outdir = DEMO, a.demo
    else:
        if not (a.workdir and a.specs):
            sys.exit("usage: diagram.py <workdir> <specs.json>   or   diagram.py --demo <outdir>")
        specs, outdir = L.read_json(a.specs), os.path.join(a.workdir, "gen")
    for s in specs:
        png, svg = render(s, outdir)
        print(f"rendered {os.path.basename(png)} + {os.path.basename(svg)}   (use image ref gen:{os.path.basename(png)})")


if __name__ == "__main__":
    main()
