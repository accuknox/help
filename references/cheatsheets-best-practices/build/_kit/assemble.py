#!/usr/bin/env python3
"""Merge every build/<module>/package.md into one output/LAUNCH-KIT.md.

Usage:
    python assemble.py
"""

from __future__ import annotations

import re
from pathlib import Path

import fitz  # PyMuPDF

KIT = Path(__file__).resolve().parent
BUILD = KIT.parent
OUT = BUILD.parent / "output"

# folder, display name, slug
MODULES = [
    ("ai-security", "AI Security", "ai-security-best-practices-guide"),
    ("cspm", "CSPM", "cspm-best-practices-guide"),
    ("cwpp", "CWPP", "cwpp-best-practices-guide"),
    ("kspm", "Kubernetes Security (KSPM)", "kubernetes-security-best-practices-guide"),
    ("aspm", "ASPM", "aspm-best-practices-guide"),
    ("api-security", "API Security", "api-security-best-practices-guide"),
    ("secrets-manager", "Secrets Management", "secrets-management-best-practices-guide"),
    ("ciem", "CIEM", "ciem-best-practices-guide"),
    ("dspm", "DSPM", "dspm-best-practices-guide"),
    ("compliance", "Cloud Compliance", "cloud-compliance-best-practices-guide"),
]

SECTIONS = {
    "web page metadata": "Web Page Metadata",
    "email": "Email",
    "linkedin post": "LinkedIn Post",
    "images": "Images",
}


def latest_pdf(slug: str) -> Path | None:
    def ver(p: Path) -> int:
        m = re.search(r"-v(\d+)\.pdf$", p.name)
        return int(m.group(1)) if m else 0
    hits = sorted(OUT.glob(f"*-{slug}-v*.pdf"), key=ver)
    return hits[-1] if hits else None


def normalize(body: str) -> str:
    lines = body.splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]  # drop the package's own title
    out = []
    for ln in lines:
        m = re.match(r"^(#{1,6})\s+(?:\d+\.\s*)?(.+?)\s*$", ln)
        if m:
            key = m.group(2).lower()
            level = len(m.group(1))
            if key in SECTIONS:
                out.append(f"### {SECTIONS[key]}")
                continue
            out.append("#" * max(level + 2, 4) + " " + m.group(2))
            continue
        out.append(ln)
    return "\n".join(out).strip()


def main() -> int:
    rows = ["| Module | PDF | Pages | Landing URL |", "|---|---|---|---|"]
    blocks = []
    for folder, name, slug in MODULES:
        pdf = latest_pdf(slug)
        pages = len(fitz.open(pdf)) if pdf else 0
        url = f"https://accuknox.com/cheatsheets/{slug}/"
        rows.append(f"| {name} | `{pdf.name if pdf else 'missing'}` | {pages} | {url} |")
        pkg = BUILD / folder / "package.md"
        body = normalize(pkg.read_text(encoding="utf-8")) if pkg.exists() else "Package missing."
        blocks.append(
            f"\n---\n\n## {name} Best Practices Cheat Sheet\n\n"
            f"Files in `output/`: `{pdf.name if pdf else 'missing'}`, `{slug}-email.html`, "
            f"`{slug}-form-image.png`, `{slug}-linkedin.png`\n\n{body}\n"
        )
    head = [
        "# AccuKnox Best Practices Cheat Sheets Launch Kit\n",
        "Ten gated cheat sheets, one per AccuKnox module. Each section below holds the web page "
        "metadata, the email and the LinkedIn post for one module.\n",
        "## Every Module at a Glance\n",
        "\n".join(rows),
    ]
    target = OUT / "LAUNCH-KIT.md"
    target.write_text("\n".join(head) + "\n" + "".join(blocks), encoding="utf-8")
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
