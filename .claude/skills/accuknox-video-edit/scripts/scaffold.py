"""Create an edit project for one recording.

    python scaffold.py <slug> <source.mp4> [--vtt <captions.vtt>] [--title "..."] [--root <dir>]

Creates <root>/<slug>/ (default root: references/video-edits) with edit.py from the
template and a .gitignore that keeps the whole folder out of git. A recording of a
customer call holds customer data, so nothing in the folder is ever committed.
The source stays where it is. edit.py points at it by absolute path.
"""
import argparse
import datetime
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from vedit import FP, fit_16_9  # noqa: E402

REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("source")
    ap.add_argument("--vtt")
    ap.add_argument("--title", default="AccuKnox recording")
    ap.add_argument("--root", default=os.path.join(REPO, "references", "video-edits"))
    a = ap.parse_args()

    src = os.path.abspath(a.source)
    if not os.path.exists(src):
        sys.exit(f"source not found: {src}")
    r = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                        "-of", "csv=p=0", src], capture_output=True, text=True)
    w, h = (int(x) for x in r.stdout.strip().split(","))
    outw, outh = fit_16_9(w, h)

    proj = os.path.join(a.root, a.slug)
    if os.path.exists(os.path.join(proj, "edit.py")):
        sys.exit(f"{proj}/edit.py exists. Edit it, do not scaffold over it.")
    os.makedirs(proj, exist_ok=True)
    with open(os.path.join(proj, ".gitignore"), "w") as f:
        f.write("# Customer recording workspace. Never commit any of it.\n*\n")
    t = open(os.path.join(HERE, "..", "references", "edit_template.py"), encoding="utf-8").read()
    vtt = repr(os.path.abspath(a.vtt).replace("\\", "/")) if a.vtt else "None"
    for k, v in {"__TITLE__": a.title, "__SOURCE__": src.replace("\\", "/"), "__VTT__": vtt,
                 "__W__": str(w), "__H__": str(h), "__OUTW__": str(outw), "__OUTH__": str(outh),
                 "__SLUG__": a.slug, "__DATE__": datetime.date.today().strftime("%B %-d, %Y")
                 if os.name != "nt" else datetime.date.today().strftime("%B %#d, %Y")}.items():
        t = t.replace(k, v)
    with open(os.path.join(proj, "edit.py"), "w", encoding="utf-8") as f:
        f.write(t)
    print(proj)
    print(f"source {w}x{h}. Next: python {os.path.join(HERE, 'survey.py')} \"{proj}\"")


if __name__ == "__main__":
    main()
