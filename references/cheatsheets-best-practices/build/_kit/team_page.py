#!/usr/bin/env python3
"""Build the self-contained team launch playbook page.

Usage:
    python team_page.py <out.html>

Embeds every LinkedIn image and form image as a compressed WebP data URI, and
the web, email and social copy from each build/<module>/package.md.
"""

from __future__ import annotations

import base64
import io
import json
import sys
from pathlib import Path

import fitz  # PyMuPDF
import markdown
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import MODULES, OUT, BUILD, latest_pdf  # noqa: E402
from handoff import split  # noqa: E402

DRIVE = "https://drive.google.com/drive/folders/"
LINKS = {
    "root": DRIVE + "1-iSsaEvks8bNAaHOGp8i6PwDI9wzrduu",
    "start": DRIVE + "1PzZ_TGfUZxEzN5INSvGEWcxP0--dwMFX",
    "design": DRIVE + "1W4XfIBtHYtNz_V63s52ups9rnxRFYAFw",
    "website": DRIVE + "1zwrSML8NR8ZF5SH3XFZXBXplphbT1JdR",
    "email": DRIVE + "1Xsv_NVm_VxNrqUXWfDF59b2JksBjB_hr",
    "social": DRIVE + "10kcU2gw3b4GUPoNhkESaVynUZVtuMGuo",
    "doc_start": "https://docs.google.com/document/d/1p6Khba6crJi6WjN4BYJRxYhlXJAUmPeRJbCKexOSANU/edit",
    "doc_web": "https://docs.google.com/document/d/1u3_f3PQfZLO6qhpAP7XydROeX_7RVcob6JtMwxsNoEc/edit",
    "doc_email": "https://docs.google.com/document/d/1GlNiiOhr0hck6iEN1CYXz5jW-bbEhBJkBaZrF9_KGus/edit",
    "doc_social": "https://docs.google.com/document/d/14ulDSc_ecLSTkAEc5nQca0aE9fuysG-jzHmjFIbhGWM/edit",
}


def webp(path: Path, width: int) -> str:
    im = Image.open(path).convert("RGB")
    im.thumbnail((width, width * 4))
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=82, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def md(text: str) -> str:
    return markdown.markdown(text, extensions=["tables", "fenced_code"])


def main() -> int:
    target = Path(sys.argv[1]).resolve()
    mods = []
    for folder, name, slug in MODULES:
        s = split(BUILD / folder / "package.md")
        pdf = latest_pdf(slug)
        mods.append({
            "id": folder, "name": name, "slug": slug,
            "pdf": pdf.name, "pages": len(fitz.open(pdf)),
            "url": f"https://accuknox.com/cheatsheets/{slug}/",
            "cover": webp(OUT / f"{slug}-form-image.png", 560),
            "li": webp(OUT / f"{slug}-linkedin.png", 720),
            "web": md(s.get("web", "")), "email": md(s.get("email", "")), "social": md(s.get("social", "")),
            "emailFile": f"{slug}-email.html", "liFile": f"{slug}-linkedin.png", "formFile": f"{slug}-form-image.png",
        })
    tpl = (Path(__file__).resolve().parent / "team_page_template.html").read_text(encoding="utf-8")
    page = tpl.replace("/*__DATA__*/null", json.dumps({"mods": mods, "links": LINKS}).replace("</", "<\/"))
    target.write_text(page, encoding="utf-8")
    print(target, round(target.stat().st_size / 1e6, 2), "MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
