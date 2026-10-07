#!/usr/bin/env python3
"""Mirror a staged handoff folder into Google Drive with the gws CLI.

Usage:
    python drive_upload.py <stage_dir> "<root folder name>"

The four role docs (*.html beside a same-name .md) become Google Docs.
Every other file uploads as is. Prints the root folder link.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

DOC = "application/vnd.google-apps.document"
FOLDER = "application/vnd.google-apps.folder"


def gws(*args: str, cwd: Path | None = None) -> dict:
    out = subprocess.run([shutil.which("gws"), "drive", "files", "create", *args, "--params", '{"fields":"id,name,webViewLink"}'],
                         capture_output=True, text=True, encoding="utf-8", cwd=cwd)
    txt = out.stdout[out.stdout.find("{"):]
    if out.returncode != 0 or not txt:
        raise SystemExit(f"gws failed: {out.stderr or out.stdout}")
    return json.loads(txt)


def folder(name: str, parent: str | None) -> dict:
    body = {"name": name, "mimeType": FOLDER}
    if parent:
        body["parents"] = [parent]
    return gws("--json", json.dumps(body))


def upload(path: Path, parent: str) -> dict:
    is_doc = path.suffix == ".html" and path.with_suffix(".md").exists()
    body = {"name": path.stem if is_doc else path.name, "parents": [parent]}
    args = ["--upload", path.name]
    if is_doc:
        body["mimeType"] = DOC
        args += ["--upload-content-type", "text/html"]
    return gws("--json", json.dumps(body), *args, cwd=path.parent)


def mirror(src: Path, parent: str) -> None:
    for p in sorted(src.iterdir()):
        if p.is_dir():
            mirror(p, folder(p.name, parent)["id"])
        elif p.suffix == ".md" and p.with_suffix(".html").exists():
            continue  # the Google Doc version replaces it
        else:
            print("  up", p.relative_to(src.parent).as_posix())
            upload(p, parent)


def main() -> int:
    stage, name = Path(sys.argv[1]), sys.argv[2]
    # "id:<folderId>" reuses an existing root folder.
    root = {"id": name[3:], "webViewLink": f"https://drive.google.com/drive/folders/{name[3:]}"} if name.startswith("id:") else folder(name, None)
    mirror(stage / "AccuKnox Cheat Sheets", root["id"])
    upload(stage / "accuknox-cheat-sheets-everything.zip", root["id"])
    print("ROOT", root["webViewLink"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
