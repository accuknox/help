"""Publish a .pptx to Google Slides and pull slide thumbnails for review.

    python publish.py <deck.pptx> [--title "Paid Ads Playbook"] [--thumbs <dir>] [--new]

First run: creates a Google Slides file from the .pptx (Drive converts it, and
the entrance animations and fade transitions survive) and stores the URL in
deck_url. --share gives everyone in share_domain edit access.

Later runs: replace the content of the same file, so the link never changes.
Pass --new to create a separate file instead.

--thumbs <dir> downloads a PNG of every slide through the Slides API, which is
the cheapest way to see what Google actually renders.

Needs the gws CLI, authenticated with Drive and Slides scopes.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
CFG_PATH = SKILL / "config.local.json"
PPTX_MIME = "application/vnd.openxmlformats-officedocument.presentationml.presentation"


def gws(*args):
    r = subprocess.run([shutil.which("gws") or "gws", *args], capture_output=True, text=True, encoding="utf-8")
    out = r.stdout
    start = out.find("{")
    if r.returncode != 0 or start < 0:
        sys.exit(f"gws {' '.join(args[:3])} failed:\n{r.stderr}\n{out}")
    return json.loads(out[start:])


def file_id(url):
    m = re.search(r"/d/([\w-]+)", url or "")
    return m.group(1) if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("--title", default="AccuKnox Paid Ads Playbook")
    ap.add_argument("--thumbs")
    ap.add_argument("--new", action="store_true")
    ap.add_argument("--share", action="store_true", help="share with share_domain as writer")
    a = ap.parse_args()
    cfg = json.loads(CFG_PATH.read_text(encoding="utf-8"))
    fid = None if a.new else file_id(cfg.get("deck_url"))

    if fid:
        gws("drive", "files", "update", "--params", json.dumps({"fileId": fid}),
            "--json", json.dumps({"name": a.title}), "--upload", a.pptx, "--upload-content-type", PPTX_MIME)
        print("updated", fid)
    else:
        res = gws("drive", "files", "create",
                  "--json", json.dumps({"name": a.title, "mimeType": "application/vnd.google-apps.presentation"}),
                  "--upload", a.pptx, "--upload-content-type", PPTX_MIME)
        fid = res["id"]
        cfg["deck_url"] = f"https://docs.google.com/presentation/d/{fid}/edit"
        CFG_PATH.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")
        print("created", fid)

    domain = cfg.get("share_domain")
    if a.share and domain:
        gws("drive", "permissions", "create", "--params", json.dumps({"fileId": fid}),
            "--json", json.dumps({"type": "domain", "domain": domain, "role": "writer"}))
        print("shared with everyone at", domain, "as writer")

    print(f"https://docs.google.com/presentation/d/{fid}/edit")

    if a.thumbs:
        out = Path(a.thumbs)
        out.mkdir(parents=True, exist_ok=True)
        pres = gws("slides", "presentations", "get", "--params", json.dumps({"presentationId": fid, "fields": "slides.objectId"}))
        for i, sl in enumerate(pres["slides"], 1):
            th = gws("slides", "presentations", "pages", "getThumbnail", "--params",
                     json.dumps({"presentationId": fid, "pageObjectId": sl["objectId"],
                                 "thumbnailProperties.thumbnailSize": "LARGE"}))
            # curl, because this machine's Python CA bundle is stale.
            subprocess.run(["curl", "-s", "-L", "--max-time", "60", "-o", str(out / f"slide-{i:02d}.png"),
                            th["contentUrl"]], check=True)
        print("thumbnails:", len(pres["slides"]), "in", out)


if __name__ == "__main__":
    main()
