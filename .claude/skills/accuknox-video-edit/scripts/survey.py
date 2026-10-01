"""Inspect a source recording before writing the edit map.

    python survey.py <project>                    probe, 1 fps frames, contact sheets, change events, transcript
    python survey.py <project> events A B [min]   change events between source seconds A and B
    python survey.py <project> grab T1 T2 ...     full-resolution frames of the shared screen (work/fr_T.png)
    python survey.py <project> grid T1 T2 T3 T4   the same four frames side by side in one image (work/grid.png)

Everything lands in <project>/work/. Read the sheets in order, then grab the exact frames
around every cut. A change event is the fraction of pixels that moved between two frames
0.2 s apart. Above 0.3 is a page change, 0.01 to 0.1 is a click, a dropdown or a scroll.
"""
import os
import re
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vedit  # noqa: E402


def mmss(t):
    return f"{int(t // 60)}:{t % 60:05.2f}"


def probe(P):
    r = subprocess.run([vedit.FP, "-v", "error", "-show_entries",
                        "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate",
                        "-of", "compact", P.src], capture_output=True, text=True)
    print(r.stdout.strip())


def frames_and_sheets(P, work):
    f1 = os.path.join(work, "f1")
    os.makedirs(f1, exist_ok=True)
    if not os.listdir(f1):
        subprocess.run([vedit.FF, "-hide_banner", "-loglevel", "error", "-i", P.src, "-vf", "fps=1",
                        "-q:v", "3", os.path.join(f1, "%05d.jpg")], check=True)
    files = sorted(os.listdir(f1))
    sheets = os.path.join(work, "sheets")
    os.makedirs(sheets, exist_ok=True)
    try:
        fnt = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        fnt = ImageFont.load_default()
    tw, th = 384, 240
    for s in range(0, len(files), 40):          # 20 tiles per sheet, one every 2 s
        chunk = list(range(s, min(s + 40, len(files)), 2))
        sheet = Image.new("RGB", (5 * tw, ((len(chunk) + 4) // 5) * th), "white")
        for k, i in enumerate(chunk):
            im = Image.open(os.path.join(f1, files[i])).resize((tw, th))
            d = ImageDraw.Draw(im)
            d.rectangle((0, 0, 92, 28), fill="black")
            d.text((4, 2), f"{i // 60}:{i % 60:02d}", fill="yellow", font=fnt)
            sheet.paste(im, ((k % 5) * tw, (k // 5) * th))
        sheet.save(os.path.join(sheets, f"s_{s:05d}.jpg"), quality=85)
    print(f"{len(files)} frames, sheets in {sheets}")


def change_events(P, work):
    import cv2
    cap = cv2.VideoCapture(P.src)
    fps = cap.get(cv2.CAP_PROP_FPS)
    step = max(1, int(round(fps / 5)))
    x, y, w, h = P.share
    prev, out, i = None, [], 0
    while True:
        ok, f = cap.read()
        if not ok:
            break
        if i % step == 0:
            g = cv2.cvtColor(cv2.resize(f[y:y + h, x:x + w], (w // 4, h // 4)), cv2.COLOR_BGR2GRAY).astype(np.int16)
            if prev is not None:
                out.append((i / fps, float((np.abs(g - prev) > 20).mean())))
            prev = g
        i += 1
    np.save(os.path.join(work, "diff.npy"), np.array(out))
    with open(os.path.join(work, "events.txt"), "w") as fh:
        for t, v in out:
            if v > 0.003:
                fh.write(f"{mmss(t)}  {t:8.2f}  {v:.3f}\n")
    print(f"change events in {os.path.join(work, 'events.txt')}")


def transcript(P, work):
    vtt = getattr(P.m, "VTT", None)
    if not vtt:
        return
    text = open(P.path(vtt), encoding="utf-8", errors="replace").read()
    rows = re.findall(r"(\d+:\d+:\d+\.\d+) --> [\d:.]+\s*\n(.+?)(?:\n\n|\Z)", text, re.S)
    with open(os.path.join(work, "transcript.txt"), "w", encoding="utf-8") as fh:
        for ts, line in rows:
            fh.write(f"{ts[3:8]}  {' '.join(line.split())}\n")
    print(f"{len(rows)} cues in {os.path.join(work, 'transcript.txt')}")
    if P.jev != "all":
        return
    import jev  # only with JEV = "all": the caption text of the call goes to TypeSafe
    kinds = jev.cues([(ts[3:8], " ".join(line.split())) for ts, line in rows])
    if kinds is None:
        return
    with open(os.path.join(work, "cues.txt"), "w", encoding="utf-8") as fh:
        for (ts, line), (k, conf) in zip(rows, kinds):
            mark = "  <-- check for a cut" if k in ("setup", "off_track", "wrap_up") else ""
            fh.write(f"{ts[3:8]}  {k:<10} {conf:.2f}  {' '.join(line.split())}{mark}
")
    print(f"cue triage by Jev in {os.path.join(work, 'cues.txt')}. A label is a lead, the frame decides.")


def grab(P, work, ts):
    x, y, w, h = P.share
    paths = []
    for t in ts:
        p = os.path.join(work, f"fr_{t}.png")
        subprocess.run([vedit.FF, "-v", "error", "-y", "-ss", str(t), "-i", P.src, "-frames:v", "1",
                        "-vf", f"crop={w}:{h}:{x}:{y}", p], check=True)
        paths.append(p)
    return paths


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    vedit.P = P = vedit.Project(sys.argv[1])
    work = os.path.join(P.root, "work")
    os.makedirs(work, exist_ok=True)
    cmd = sys.argv[2] if len(sys.argv) > 2 else "all"
    if cmd == "all":
        probe(P)
        transcript(P, work)
        frames_and_sheets(P, work)
        change_events(P, work)
    elif cmd == "events":
        a, b = float(sys.argv[3]), float(sys.argv[4])
        lo = float(sys.argv[5]) if len(sys.argv) > 5 else 0.004
        d = np.load(os.path.join(work, "diff.npy"))
        print("  ".join(f"{mmss(t)}({t:.1f}) {v:.3f}" for t, v in d if a <= t <= b and v >= lo))
    elif cmd == "grab":
        for p in grab(P, work, sys.argv[3:]):
            print(p)
    elif cmd == "grid":
        ps = grab(P, work, sys.argv[3:7])
        tw, th = P.share[2] // 2, P.share[3] // 2
        g = Image.new("RGB", (tw * 2, th * ((len(ps) + 1) // 2)))
        for i, p in enumerate(ps):
            g.paste(Image.open(p).resize((tw, th)), ((i % 2) * tw, (i // 2) * th))
        out = os.path.join(work, "grid.png")
        g.save(out)
        print(out)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
