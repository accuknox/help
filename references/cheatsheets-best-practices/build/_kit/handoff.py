#!/usr/bin/env python3
"""Stage the team handoff: one folder per owner, plus one zip of everything.

Usage:
    python handoff.py <stage_dir>

Writes <stage_dir>/AccuKnox Cheat Sheets/ with role folders and Google Doc
ready HTML files, and <stage_dir>/accuknox-cheat-sheets-everything.zip.
"""

from __future__ import annotations

import re
import shutil
import sys
import zipfile
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).resolve().parent))
from assemble import MODULES, OUT, BUILD, latest_pdf  # noqa: E402

SECTIONS = {"web page metadata": "web", "email": "email", "linkedin post": "social", "images": "images"}


def split(pkg: Path) -> dict[str, str]:
    """Return the package sections keyed web, email, social, images, other."""
    parts: dict[str, list[str]] = {"other": []}
    key = "other"
    top = None
    for ln in pkg.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(#{1,6})\s+(?:\d+\.\s*)?(.+?)\s*$", ln)
        if m and m.group(2).lower() in SECTIONS:
            key, top = SECTIONS[m.group(2).lower()], len(m.group(1))
            parts.setdefault(key, [])
            continue
        if m and top and len(m.group(1)) <= top:
            key, top = "other", None
            if ln.startswith("# "):
                continue
        parts.setdefault(key, []).append(ln)
    return {k: "\n".join(v).strip() for k, v in parts.items()}


def doc(path: Path, title: str, intro: str, blocks: list[tuple[str, str]]) -> None:
    md = [f"# {title}", "", intro, ""]
    for head, body in blocks:
        md += ["", f"## {head}", "", body, ""]
    text = "\n".join(md)
    html = markdown.markdown(text, extensions=["tables", "fenced_code"])
    path.with_suffix(".html").write_text(f"<html><head><meta charset='utf-8'></head><body>{html}</body></html>", encoding="utf-8")
    path.with_suffix(".md").write_text(text, encoding="utf-8")


def main() -> int:
    stage = Path(sys.argv[1]).resolve() / "AccuKnox Cheat Sheets"
    if stage.exists():
        shutil.rmtree(stage)
    f_start = stage / "00 Start Here"
    f_design = stage / "01 Design Review - Anish"
    f_web = stage / "02 Website - Debjani and Mrinal"
    f_email = stage / "03 Emails - Kavitha"
    f_social = stage / "04 Social - Jahana"
    for f in (f_start, f_design, f_web, f_email, f_social):
        f.mkdir(parents=True)

    web, mail, social = [], [], []
    for folder, name, slug in MODULES:
        s = split(BUILD / folder / "package.md")
        pdf = latest_pdf(slug)
        files = (f"PDF `{pdf.name}`, form image `{slug}-form-image.png`.")
        web.append((name, files + "\n\n" + s.get("web", "")))
        mail.append((name, f"HTML file `{slug}-email.html`.\n\n" + s.get("email", "")))
        social.append((name, f"Image `{slug}-linkedin.png`.\n\n" + s.get("social", "")))

        # Design gets every visual and the editable source.
        d = f_design / name
        d.mkdir()
        shutil.copy2(pdf, d)
        for suf in ("form-image.png", "linkedin.png"):
            shutil.copy2(OUT / f"{slug}-{suf}", d)
        # Website gets the PDF to gate and the form image.
        w = f_web / name
        w.mkdir()
        shutil.copy2(pdf, w)
        shutil.copy2(OUT / f"{slug}-form-image.png", w)
        shutil.copy2(OUT / f"{slug}-email.html", f_email)
        shutil.copy2(OUT / f"{slug}-linkedin.png", f_social)

    doc(f_web / "Web page metadata", "Web page metadata for 10 cheat sheet pages",
        "One block per page. Each page follows the live AI security page at "
        "https://accuknox.com/cheatsheets/ai-security-best-practices-guide/. "
        "Upload the PDF behind the form and use the form image beside the form.", web)
    doc(f_email / "Email copy", "Email copy for 10 cheat sheets",
        "Each HTML file in this folder is ready to import. Subject, preview text and body are below "
        "for review. Point each button at the live landing page once the website team confirms it.", mail)
    doc(f_social / "LinkedIn posts", "LinkedIn posts for 10 cheat sheets",
        "Post the body with the matching image. Put the link in the first comment, never in the body. "
        "Use the landing page URL once the website team confirms it is live.", social)

    # Editable source for design: HTML, images and fonts, without QA renders.
    src_zip = f_design / "editable-source-html.zip"
    with zipfile.ZipFile(src_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for p in BUILD.rglob("*"):
            if p.is_file() and "qa" not in p.relative_to(BUILD).parts:
                z.write(p, p.relative_to(BUILD))

    shutil.copy2(OUT / "LAUNCH-KIT.md", f_start / "LAUNCH-KIT.md")
    readme = Path(__file__).resolve().parent / "START-HERE.md"
    text = readme.read_text(encoding="utf-8")
    shutil.copy2(readme, f_start / "Start here.md")
    html = markdown.markdown(text, extensions=["tables"])
    (f_start / "Start here.html").write_text(
        f"<html><head><meta charset='utf-8'></head><body>{html}</body></html>", encoding="utf-8")

    everything = stage.parent / "accuknox-cheat-sheets-everything.zip"
    with zipfile.ZipFile(everything, "w", zipfile.ZIP_DEFLATED) as z:
        for p in stage.rglob("*"):
            if p.is_file():
                z.write(p, p.relative_to(stage.parent))
    print(stage)
    print(everything, everything.stat().st_size // 1_000_000, "MB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
