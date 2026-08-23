#!/usr/bin/env python3
r"""Index and mirror the AccuKnox PRODUCT UI Drive folder for use in content.

The folder holds product screenshots, architecture diagrams, event photography
and booth artwork that never made it into the help docs. It is the eye-candy
source. `docs/` and accuknox.com are the other two, and this script does not
touch either.

Two artifacts, two homes:

  * The **manifest and index** live in the repo, under `media/`. They are text,
    they are small, and they are what a writer reads to pick an image.
  * The **binaries** live outside the repo, under `MIRROR` below, so a 2 GB
    screenshot library never enters git history.

Google authentication comes from the `gws` CLI, already signed in as
atharva@accuknox.com. This script shells out to it rather than holding its own
credentials.

Usage:
    python drive_sync.py index                 # walk Drive, rewrite the manifest
    python drive_sync.py index --max-depth 3
    python drive_sync.py pull                  # download what the manifest lists
    python drive_sync.py pull --folder CIEM --limit 20
    python drive_sync.py check                 # drift against the last index
    python drive_sync.py search "prompt firewall"

Exit codes: 0 in sync, 1 drift found or a download failed, 2 gws unavailable.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT_FOLDER_ID = "1wrvtlSCSB7hZfWKd_7V7BUtf3R7FbZk2"
ROOT_FOLDER_URL = f"https://drive.google.com/drive/folders/{ROOT_FOLDER_ID}"

SKILL = Path(__file__).resolve().parent.parent
MEDIA = SKILL / "media"
MANIFEST = MEDIA / "MANIFEST.json"
INDEX = MEDIA / "INDEX.md"

# Binaries land outside the repo. Override with ACCUKNOX_MEDIA_MIRROR.
MIRROR = Path(os.environ.get("ACCUKNOX_MEDIA_MIRROR",
                             r"D:\Atharva\AccuKnox\product-ui-assets"))

FOLDER_MIME = "application/vnd.google-apps.folder"
IMAGE_MIMES = {"image/png", "image/jpeg", "image/jpg", "image/webp",
               "image/gif", "image/svg+xml", "image/avif"}
VIDEO_MIMES = {"video/mp4", "video/quicktime", "video/webm"}

# Re-index when the manifest passes this age. Quarterly, as agreed.
STALE_DAYS = 90


def gws(args: list[str]) -> dict:
    """Run a gws command and return its parsed JSON body."""
    exe = shutil.which("gws")
    if not exe:
        print("gws CLI not found on PATH. Install it or sign in, then retry.",
              file=sys.stderr)
        raise SystemExit(2)
    proc = subprocess.run([exe, *args], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip()[:400] or "gws failed")
    # The CLI prints a keyring banner on the first line of stdout.
    body = proc.stdout
    start = body.find("{")
    if start < 0:
        raise RuntimeError(f"no JSON in gws output: {body[:200]}")
    return json.loads(body[start:])


def list_children(folder_id: str) -> list[dict]:
    out: list[dict] = []
    token = None
    while True:
        params = {
            "q": f"'{folder_id}' in parents and trashed=false",
            "pageSize": 200,
            "fields": "files(id,name,mimeType,size,modifiedTime,"
                      "imageMediaMetadata/width,imageMediaMetadata/height),"
                      "nextPageToken",
            "supportsAllDrives": True,
            "includeItemsFromAllDrives": True,
            "orderBy": "folder,name",
        }
        if token:
            params["pageToken"] = token
        data = gws(["drive", "files", "list", "--params", json.dumps(params)])
        out.extend(data.get("files", []))
        token = data.get("nextPageToken")
        if not token:
            break
    return out


def walk(folder_id: str, path: str, depth: int, max_depth: int) -> list[dict]:
    rows: list[dict] = []
    try:
        children = list_children(folder_id)
    except Exception as exc:  # noqa: BLE001
        print(f"  skip {path}: {exc}", file=sys.stderr)
        return rows
    for f in children:
        name = f["name"]
        here = f"{path}/{name}" if path else name
        if f["mimeType"] == FOLDER_MIME:
            print(f"  {'  ' * depth}{here}/")
            if depth < max_depth:
                rows.extend(walk(f["id"], here, depth + 1, max_depth))
            continue
        meta = f.get("imageMediaMetadata") or {}
        rows.append({
            "id": f["id"],
            "name": name,
            "path": here,
            "folder": path or "(root)",
            "mime": f["mimeType"],
            "bytes": int(f.get("size") or 0),
            "modified": (f.get("modifiedTime") or "")[:10],
            "width": meta.get("width"),
            "height": meta.get("height"),
        })
    return rows


def kind(mime: str) -> str:
    if mime in IMAGE_MIMES:
        return "image"
    if mime in VIDEO_MIMES:
        return "video"
    if mime.startswith("application/vnd.google-apps"):
        return "gdoc"
    return "other"


def human(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024 or unit == "GB":
            return f"{n:.0f}{unit}" if unit == "B" else f"{n/1:.0f}{unit}"
        n /= 1024  # type: ignore[assignment]
    return f"{n}B"


def size_label(n: int) -> str:
    if n <= 0:
        return "-"
    if n < 1024:
        return f"{n}B"
    if n < 1024 ** 2:
        return f"{n/1024:.0f}KB"
    return f"{n/1024**2:.1f}MB"


def write_manifest(rows: list[dict], max_depth: int) -> None:
    MEDIA.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": ROOT_FOLDER_URL,
        "folder_id": ROOT_FOLDER_ID,
        "indexed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "max_depth": max_depth,
        "mirror": str(MIRROR),
        "file_count": len(rows),
        "byte_count": sum(r["bytes"] for r in rows),
        "files": sorted(rows, key=lambda r: r["path"].lower()),
    }
    MANIFEST.write_text(json.dumps(payload, indent=2) + "\n",
                        encoding="utf-8", newline="\n")


def write_index(rows: list[dict]) -> None:
    by_folder: dict[str, list[dict]] = {}
    for r in rows:
        by_folder.setdefault(r["folder"], []).append(r)

    total = sum(r["bytes"] for r in rows)
    images = [r for r in rows if kind(r["mime"]) == "image"]
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    out = [
        "# PRODUCT UI media index",
        "",
        f"{len(rows)} files across {len(by_folder)} folders, "
        f"{size_label(total)} total, {len(images)} images. "
        f"Indexed {stamp} by `scripts/drive_sync.py`. Do not hand-edit.",
        "",
        f"Source: [PRODUCT UI on Drive]({ROOT_FOLDER_URL})",
        "",
        f"Binaries mirror to `{MIRROR}`, outside this repo. Pull one folder "
        "at a time with `python scripts/drive_sync.py pull --folder <name>`.",
        "",
        "## Folders",
        "",
        "| Folder | Files | Images | Size |",
        "| --- | --- | --- | --- |",
    ]
    for folder in sorted(by_folder, key=str.lower):
        fs = by_folder[folder]
        out.append(f"| `{folder}` | {len(fs)} | "
                   f"{sum(1 for f in fs if kind(f['mime']) == 'image')} | "
                   f"{size_label(sum(f['bytes'] for f in fs))} |")
    out += ["", "## Files", ""]
    for folder in sorted(by_folder, key=str.lower):
        out += [f"### {folder}", "",
                "| File | Kind | Size | Pixels | Modified |",
                "| --- | --- | --- | --- | --- |"]
        for f in sorted(by_folder[folder], key=lambda r: r["name"].lower()):
            px = (f"{f['width']}x{f['height']}"
                  if f.get("width") and f.get("height") else "-")
            out.append(f"| `{f['name']}` | {kind(f['mime'])} | "
                       f"{size_label(f['bytes'])} | {px} | {f['modified']} |")
        out.append("")
    INDEX.write_text("\n".join(out), encoding="utf-8", newline="\n")


def load_manifest() -> dict:
    if not MANIFEST.exists():
        print("no manifest yet. Run: python drive_sync.py index",
              file=sys.stderr)
        raise SystemExit(1)
    return json.loads(MANIFEST.read_text("utf-8"))


def cmd_index(args: argparse.Namespace) -> int:
    print(f"walking {ROOT_FOLDER_URL}")
    rows = walk(ROOT_FOLDER_ID, "", 0, args.max_depth)
    write_manifest(rows, args.max_depth)
    write_index(rows)
    total = sum(r["bytes"] for r in rows)
    print(f"\n{len(rows)} files, {size_label(total)}")
    print(f"wrote {MANIFEST.relative_to(SKILL)}")
    print(f"wrote {INDEX.relative_to(SKILL)}")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    old = load_manifest()
    indexed = datetime.fromisoformat(old["indexed_at"])
    age = datetime.now(timezone.utc) - indexed
    print(f"last indexed {indexed.date()} ({age.days} days ago), "
          f"{old['file_count']} files")

    if age > timedelta(days=STALE_DAYS) and not args.deep:
        print(f"\nSTALE. The manifest is older than {STALE_DAYS} days.")
        print("Run: python drive_sync.py index")
        return 1

    if not args.deep:
        print("fresh. Add --deep to compare against Drive right now.")
        return 0

    print("comparing against Drive")
    now = walk(ROOT_FOLDER_ID, "", 0, old.get("max_depth", 4))
    before = {f["id"]: f for f in old["files"]}
    after = {f["id"]: f for f in now}
    added = [after[i] for i in after.keys() - before.keys()]
    removed = [before[i] for i in before.keys() - after.keys()]
    changed = [after[i] for i in after.keys() & before.keys()
               if after[i]["modified"] != before[i]["modified"]]

    for label, rows in (("added", added), ("removed", removed),
                        ("changed", changed)):
        for r in rows[:20]:
            print(f"  {label:8s} {r['path']}")
        if len(rows) > 20:
            print(f"  {label:8s} ... and {len(rows) - 20} more")

    drift = len(added) + len(removed) + len(changed)
    print(f"\n{len(added)} added, {len(removed)} removed, "
          f"{len(changed)} changed")
    if drift:
        print("Out of sync. Run: python drive_sync.py index")
    return 1 if drift else 0


def cmd_pull(args: argparse.Namespace) -> int:
    data = load_manifest()
    rows = [f for f in data["files"] if kind(f["mime"]) in ("image", "video")]
    if args.folder:
        needle = args.folder.lower()
        rows = [f for f in rows if needle in f["folder"].lower()]
    if args.match:
        pat = re.compile(args.match, re.I)
        rows = [f for f in rows if pat.search(f["path"])]
    rows = rows[:args.limit]
    if not rows:
        print("nothing matched")
        return 0

    exe = shutil.which("gws")
    failed = 0
    for f in rows:
        dest = MIRROR / f["path"]
        if dest.exists() and dest.stat().st_size == f["bytes"] and not args.force:
            print(f"have  {f['path']}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        # gws rejects an --output path outside its working directory, so run it
        # from the destination folder and pass a bare filename.
        proc = subprocess.run(
            [exe, "drive", "files", "get", "--params",
             json.dumps({"fileId": f["id"], "alt": "media",
                         "supportsAllDrives": True}),
             "--output", dest.name],
            capture_output=True, text=True, cwd=str(dest.parent))
        if proc.returncode != 0 or not dest.exists():
            print(f"FAIL  {f['path']}: {proc.stderr.strip()[:120]}",
                  file=sys.stderr)
            failed += 1
            continue
        print(f"got   {f['path']}  {size_label(dest.stat().st_size)}")
    print(f"\nmirror: {MIRROR}")
    return 1 if failed else 0


def cmd_search(args: argparse.Namespace) -> int:
    data = load_manifest()
    terms = [t.lower() for t in args.query.split() if t]
    hits = []
    for f in data["files"]:
        hay = f["path"].lower()
        score = sum(1 for t in terms if t in hay)
        if score:
            hits.append((score, f))
    hits.sort(key=lambda x: (-x[0], x[1]["path"]))
    if not hits:
        print(f"no match for {args.query!r} in {data['file_count']} files")
        return 0
    for _, f in hits[:args.limit]:
        px = (f"{f['width']}x{f['height']}"
              if f.get("width") and f.get("height") else "-")
        print(f"{kind(f['mime']):6s} {size_label(f['bytes']):>8s} {px:>10s}  "
              f"{f['path']}")
    print(f"\n{len(hits)} match(es). Pull one folder with "
          f"--folder '<folder name>'.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("index", help="walk Drive and rewrite the manifest")
    p.add_argument("--max-depth", type=int, default=4)
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("check", help="report staleness or drift")
    p.add_argument("--deep", action="store_true",
                   help="walk Drive and diff against the manifest")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("pull", help="download binaries to the mirror")
    p.add_argument("--folder", help="substring of the folder path")
    p.add_argument("--match", help="regex against the full path")
    p.add_argument("--limit", type=int, default=40)
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_pull)

    p = sub.add_parser("search", help="find files by name in the manifest")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=25)
    p.set_defaults(func=cmd_search)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
