"""Quality checks that read the output instead of trusting the plan.

    python qc.py <project> voice    transcribe every voiced line locally and diff it against the script
    python qc.py <project> full     contact sheets of the rendered MP4 at 1 fps, a transcript of the
                                    final mix, and silence and black-frame detection

Speech to text runs locally with faster-whisper (pip install faster-whisper). Nothing is uploaded.
"""
import difflib
import os
import re
import shutil
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vedit  # noqa: E402


def whisper():
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sys.exit("pip install faster-whisper")
    return WhisperModel("small.en", device="cpu", compute_type="int8")


def norm(s):
    return re.sub(r"[^a-z0-9 ]", "", s.lower().replace("-", " ")).split()


def voice(P):
    m = whisper()
    flagged = 0
    for text in vedit.all_lines():
        p = vedit.line_path(text)
        if not os.path.exists(p):
            print("MISSING", text)
            flagged += 1
            continue
        segs, _ = m.transcribe(p, beam_size=5)
        heard = " ".join(s.text for s in segs).strip()
        ratio = difflib.SequenceMatcher(None, norm(text), norm(heard)).ratio()
        pcm = subprocess.run([vedit.FF, "-v", "error", "-i", p, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                             capture_output=True).stdout
        a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
        n = len(a) // 160
        on = np.where(np.sqrt((a[: n * 160].reshape(n, 160) ** 2).mean(1)) > 0.01)[0]
        pause = float(np.diff(on).max() * 0.01) if len(on) > 1 else 0.0
        ok = ratio > 0.9 and pause < 1.0
        flagged += not ok
        print(f"{'OK ' if ok else 'CHK'} {ratio:.2f} pause {pause:.2f}s | {heard}")
    print(f"flagged {flagged}. A CHK on digits ('94' for 'ninety four') is fine. A CHK on a word is not.")


def full(P):
    v = os.path.join(P.out_dir, P.out_name)
    fd = os.path.join(P.out_dir, "_qc_frames")
    sd = os.path.join(P.out_dir, "_qc_sheets")
    for d in (fd, sd):
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
    subprocess.run([vedit.FF, "-v", "error", "-y", "-i", v, "-vf", "fps=1,scale=384:216",
                    os.path.join(fd, "%05d.jpg")], check=True)
    files = sorted(os.listdir(fd))
    try:
        fnt = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        fnt = ImageFont.load_default()
    for s in range(0, len(files), 25):
        sh = Image.new("RGB", (384 * 5, 216 * 5))
        for k, fn in enumerate(files[s:s + 25]):
            im = Image.open(os.path.join(fd, fn))
            t = s + k
            d = ImageDraw.Draw(im)
            d.rectangle((0, 0, 70, 24), fill="black")
            d.text((4, 1), f"{t // 60}:{t % 60:02d}", fill="yellow", font=fnt)
            sh.paste(im, ((k % 5) * 384, (k // 5) * 216))
        sh.save(os.path.join(sd, f"sheet_{s:05d}.jpg"), quality=85)
    print(f"{len(files)} s watched as {len(os.listdir(sd))} sheets in {sd}")
    segs, _ = whisper().transcribe(v, beam_size=5)
    tp = os.path.join(P.out_dir, "_qc_transcript.txt")
    with open(tp, "w", encoding="utf-8") as fh:
        for sg in segs:
            fh.write(f"{sg.start:7.2f} {sg.end:7.2f} {sg.text.strip()}\n")
    print("transcript of the final mix:", tp)
    r = subprocess.run([vedit.FF, "-v", "info", "-i", v, "-af", "silencedetect=n=-40dB:d=4",
                        "-vf", "blackdetect=d=0.5:pix_th=0.05", "-f", "null", "-"], capture_output=True, text=True)
    hits = [l.split("] ")[-1] for l in r.stderr.splitlines() if "silence_end" in l or "black_start" in l]
    print("silences over 4 s and black frames:")
    print("\n".join(hits) or "  none")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    vedit.P = P = vedit.Project(sys.argv[1])
    {"voice": voice, "full": full}[sys.argv[2]](P)
