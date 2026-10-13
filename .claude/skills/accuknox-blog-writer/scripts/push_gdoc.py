#!/usr/bin/env python3
"""Publish a blog draft to Google Docs through the `gws` CLI.

What it does, in order:

1. Converts the draft with `to_gdoc_html.py` (images embedded, line height 1).
2. Creates a Google Doc from the HTML, or replaces the body of the Doc it made
   last time. The id lives in `<draft>.gdoc.json` beside the draft, so a re-run
   keeps the same URL. Pass `--new` to force a fresh Doc.
3. Sets every paragraph to line spacing 100 (single, the tightest Docs offers)
   with one `documents.batchUpdate`, then reads the Doc back and reports any
   paragraph that is not at 100.

`gws` must be signed in (`gws auth status` shows `token_valid`). A failed login
needs `gws auth login` from a person at a browser, which this script cannot do.

Usage:
    python push_gdoc.py draft.md
    python push_gdoc.py draft.md --new
    python push_gdoc.py draft.md --update <doc url or id>
    python push_gdoc.py draft.md --folder <drive folder id>
    python push_gdoc.py draft.md --dry-run      # convert and stop

Exit codes: 0 published and verified, 1 published with a spacing warning,
2 could not publish.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import to_gdoc_html  # noqa: E402

DOC_MIME = "application/vnd.google-apps.document"
LINE_SPACING = 100  # percent. 100 is single spacing.


def gws(*args: str, cwd: Path | None = None) -> dict:
    """Run one gws command and return its JSON. Drops the keyring banner.

    gws refuses an `--upload` path outside its working directory, so an upload
    passes `cwd` and a bare file name.
    """
    exe = shutil.which("gws")
    if not exe:
        raise SystemExit("gws is not on PATH. Run "
                         "~/.claude/skills/_config/toolbelt.ps1 or install "
                         "@googleworkspace/cli.")
    p = subprocess.run([exe, *args], capture_output=True, text=True,
                       encoding="utf-8", cwd=cwd)
    out = "\n".join(l for l in p.stdout.splitlines()
                    if not l.startswith("Using keyring backend"))
    if p.returncode != 0:
        raise RuntimeError((out or p.stderr).strip()[:600])
    try:
        return json.loads(out) if out.strip() else {}
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"gws returned non-JSON: {out[:300]}") from exc


def doc_id_from(value: str) -> str:
    m = re.search(r"/document/d/([A-Za-z0-9_-]+)", value)
    return m.group(1) if m else value.strip()


def paragraphs(content: list[dict]):
    """Every paragraph in the body, table cells included."""
    for el in content:
        if "paragraph" in el:
            yield el
        elif "table" in el:
            for row in el["table"]["tableRows"]:
                for cell in row["tableCells"]:
                    yield from paragraphs(cell["content"])


def set_line_spacing(doc_id: str) -> tuple[int, int]:
    """Set lineSpacing on the whole body. Return (paragraphs, off spec)."""
    doc = gws("docs", "documents", "get", "--params",
              json.dumps({"documentId": doc_id}))
    end = doc["body"]["content"][-1]["endIndex"]
    gws("docs", "documents", "batchUpdate",
        "--params", json.dumps({"documentId": doc_id}),
        "--json", json.dumps({"requests": [{
            "updateParagraphStyle": {
                "range": {"startIndex": 1, "endIndex": end - 1},
                "paragraphStyle": {"lineSpacing": LINE_SPACING},
                "fields": "lineSpacing"}}]}))
    doc = gws("docs", "documents", "get", "--params",
              json.dumps({"documentId": doc_id}))
    paras = list(paragraphs(doc["body"]["content"]))
    off = sum(1 for p in paras
              if p["paragraph"]["paragraphStyle"].get("lineSpacing")
              != LINE_SPACING)
    images = len(doc.get("inlineObjects", {}))
    print(f"line spacing {LINE_SPACING} on {len(paras) - off} of "
          f"{len(paras)} paragraphs, {images} inline image(s)")
    return len(paras), off


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("draft", type=Path)
    ap.add_argument("--new", action="store_true",
                    help="ignore the saved Doc id and create a new Doc")
    ap.add_argument("--update", metavar="URL_OR_ID",
                    help="replace the body of this Doc instead")
    ap.add_argument("--folder", metavar="FOLDER_ID",
                    help="Drive folder for a new Doc")
    ap.add_argument("--dry-run", action="store_true",
                    help="convert and stop before any upload")
    args = ap.parse_args()

    if not args.draft.exists():
        print(f"no such file: {args.draft}", file=sys.stderr)
        return 2
    draft = args.draft.resolve()

    title, page = to_gdoc_html.convert(draft.read_text("utf-8"), draft.stem,
                                       draft.parent)
    html_path = draft.with_suffix(".gdoc.html")
    html_path.write_text(page, encoding="utf-8", newline="\n")
    print(f"converted {draft.name}: {len(page) // 1024} KB, title: {title}")
    if args.dry_run:
        return 0

    sidecar = draft.with_suffix(".gdoc.json")
    doc_id = None
    if args.update:
        doc_id = doc_id_from(args.update)
    elif sidecar.exists() and not args.new:
        doc_id = json.loads(sidecar.read_text("utf-8")).get("id")

    try:
        if doc_id:
            res = gws("drive", "files", "update",
                      "--params", json.dumps({"fileId": doc_id,
                                              "fields": "id,name,webViewLink"}),
                      "--json", json.dumps({"name": title}),
                      "--upload", html_path.name,
                      "--upload-content-type", "text/html",
                      cwd=html_path.parent)
            verb = "updated in place"
        else:
            meta = {"name": title, "mimeType": DOC_MIME}
            if args.folder:
                meta["parents"] = [args.folder]
            res = gws("drive", "files", "create",
                      "--params", json.dumps({"fields": "id,name,webViewLink"}),
                      "--json", json.dumps(meta),
                      "--upload", html_path.name,
                      "--upload-content-type", "text/html",
                      cwd=html_path.parent)
            verb = "created"
        doc_id = res["id"]
        _, off = set_line_spacing(doc_id)
    except (RuntimeError, KeyError) as exc:
        print(f"publish failed: {exc}", file=sys.stderr)
        return 2

    url = f"https://docs.google.com/document/d/{doc_id}/edit"
    sidecar.write_text(json.dumps({"id": doc_id, "url": url, "title": title},
                                  indent=2) + "\n", encoding="utf-8")
    print(f"{verb}: {url}")
    if off:
        print(f"warning: {off} paragraph(s) are not at line spacing "
              f"{LINE_SPACING}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
