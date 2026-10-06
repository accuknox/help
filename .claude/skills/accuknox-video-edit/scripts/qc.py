"""Quality checks that read the output instead of trusting the plan.

    python qc.py <project> voice    transcribe every voiced line locally and diff it against the script
    python qc.py <project> hook     pass or fail the first 5 s, the logo and the watermark (exit 1 on fail)
                                    add --preview to test the output of render --until
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

import cv2
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


def _match(gray, tmpl, scales):
    """Best normalised match of `tmpl` in `gray` over a few scales."""
    best = -1.0
    for s in scales:
        t = cv2.resize(tmpl, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
        if t.shape[0] >= gray.shape[0] or t.shape[1] >= gray.shape[1] or min(t.shape[:2]) < 8:
            continue
        best = max(best, float(cv2.matchTemplate(gray, t, cv2.TM_CCOEFF_NORMED).max()))
    return best


def hook(P):
    """Pass or fail the opening and the branding of the rendered MP4. Exit 1 on any fail.

    H1 opens bright         the first frame is not black (mean luma > 40)
    H2 product by 0.5 s     a hook shot or a product frame is on screen by 0.5 s
    H3 motion               the first 5 s change on every step (median frame diff > 3) with 2+ cuts
    H4 voice by 0.8 s       narration starts within 0.8 s
    H5 body by 6.5 s        the hook hands over to the walkthrough by 6.5 s
    H6 logo in the hook     the AccuKnox logo is found in the hook's last second
    H7 watermark            the corner logo is on 90%+ of product frames
    H8 logo on the end card the logo is on the end card, when the output reaches it
    """
    import brand
    v = os.path.join(P.out_dir, P.out_name)
    if "--preview" in sys.argv:
        v = v[:-4] + "_preview.mp4"
    tl = __import__("json").load(open(os.path.join(P.out_dir, "timeline.json"), encoding="utf-8"))
    beats = {b["id"]: b for b in tl["beats"]}
    cap = cv2.VideoCapture(v)
    fps = cap.get(cv2.CAP_PROP_FPS)
    n = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    dur = n / fps

    def frame(t):
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(round(t * fps)))
        ok, fr = cap.read()
        return fr if ok else None
    rows = []
    hk = beats.get("HOOK")
    f0 = frame(0.03)
    luma = float(cv2.cvtColor(f0, cv2.COLOR_BGR2GRAY).mean())
    rows.append(("H1 opens bright", luma > 40, f"luma {luma:.0f} at 0.03 s"))
    first_body = next((b["start"] for b in tl["beats"] if b["id"] not in ("HOOK", "B00")), 0)
    rows.append(("H2 product by 0.5 s", bool(hk) or first_body <= 0.5,
                 "hook shot 1 starts at 0.0 s" if hk else f"first product frame at {first_body:.2f} s"))
    diffs, prev = [], None
    for k in range(int(min(5.0, dur) * 10)):
        fr = frame(k / 10)
        g = cv2.cvtColor(cv2.resize(fr, (320, 180)), cv2.COLOR_BGR2GRAY).astype(np.float32)
        if prev is not None:
            diffs.append(float(np.abs(g - prev).mean()))
        prev = g
    med = float(np.median(diffs)) if diffs else 0.0
    cuts = sum(d > 25 for d in diffs)
    rows.append(("H3 motion", med > 3 and cuts >= 2, f"median diff {med:.1f}, {cuts} cuts in 5 s"))
    pcm = subprocess.run([vedit.FF, "-v", "error", "-i", v, "-t", "3", "-ac", "1", "-ar", "16000", "-f", "s16le",
                          "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    # Voice, not the sound design: the first 50 ms window where 300 Hz to 3 kHz energy dominates.
    t_voice = None
    for i in range(0, len(a) - 800, 800):
        w = a[i:i + 800]
        sp = np.abs(np.fft.rfft(w))
        fq = np.fft.rfftfreq(len(w), 1 / 16000)
        band = sp[(fq > 300) & (fq < 3000)].sum()
        if np.sqrt((w ** 2).mean()) > 0.02 and band / (sp.sum() + 1e-9) > 0.6:
            t_voice = i / 16000
            break
    rows.append(("H4 voice by 0.8 s", t_voice is not None and t_voice <= 0.8,
                 f"voice at {t_voice:.2f} s" if t_voice is not None else "no voice in 3 s"))
    rows.append(("H5 body by 6.5 s", first_body <= 6.5, f"walkthrough starts at {first_body:.2f} s"))
    logo = cv2.imread(brand.LOGO_PATH, cv2.IMREAD_UNCHANGED)
    lg = cv2.cvtColor(logo[..., :3], cv2.COLOR_BGR2GRAY)
    lg = (lg.astype(np.float32) * (logo[..., 3] / 255.0)).astype(np.uint8)
    if hk:
        t = hk["start"] + hk["dur"] - 0.6
        g = cv2.cvtColor(frame(t), cv2.COLOR_BGR2GRAY)
        base = P.W * 0.40 / lg.shape[1]
        sc = _match(g, lg, [base * s for s in (0.92, 1.0, 1.08)])
        rows.append(("H6 logo in the hook", sc > 0.5, f"match {sc:.2f} at {t:.1f} s"))
    else:
        rows.append(("H6 logo in the hook", False, "no HOOK in edit.py"))
    if P.watermark:
        patch = brand._badge(P.W, P.H)
        x, y, w, h = brand.watermark_box(P.W, P.H, P.watermark)
        # Compare the logo inside the pill only. The pill's soft edge takes the page colour.
        ix, iy = int(w * 0.09), int(h * 0.28)
        x, y, w, h, off = x + ix, y + iy, w - 2 * ix, h - 2 * iy, (ix, iy)
        body = [b for b in tl["beats"] if b["id"] not in ("HOOK", "B00", "END")]
        ts = [t for b in body for t in np.arange(b["start"] + 0.5, b["start"] + b["dur"] - 0.3, 2.0) if t < dur - 1.3]
        ref = None
        hits = 0
        for t in ts:
            fr = frame(t)
            crop = cv2.cvtColor(fr[y:y + h, x:x + w], cv2.COLOR_BGR2GRAY).astype(np.float32)
            if ref is None:
                pz = patch[0]
                sh = patch[1]
                ox, oy = sh + off[0], sh + off[1]
                ref = cv2.cvtColor(pz[oy:oy + h, ox:ox + w, 2::-1].astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
            c = np.corrcoef(crop.ravel(), ref.ravel())[0, 1]
            hits += c > 0.85
        ok = bool(ts) and hits / len(ts) >= 0.9
        rows.append(("H7 watermark", ok, f"{hits} of {len(ts)} product frames"))
    else:
        rows.append(("H7 watermark", False, "BRAND watermark is off"))
    end = beats.get("END")
    if end and end["start"] + 1.5 < dur:
        t = end["start"] + 1.5
        g = cv2.cvtColor(frame(t), cv2.COLOR_BGR2GRAY)
        base = P.W * 0.36 / lg.shape[1]
        sc = _match(g, lg, [base * s for s in (0.95, 1.0, 1.05)])
        rows.append(("H8 logo on the end card", sc > 0.5, f"match {sc:.2f} at {t:.1f} s"))
    else:
        rows.append(("H8 logo on the end card", None, "not in this output (preview or no OUTRO)"))
    lines = [f"Hook and brand test: {v} ({dur:.1f} s)", ""]
    for name, ok, ev in rows:
        lines.append(f"{'PASS' if ok else ('N/A ' if ok is None else 'FAIL')}  {name:<26} {ev}")
    out = "\n".join(lines)
    print(out)
    open(os.path.join(P.out_dir, "_qc_hook.txt"), "w", encoding="utf-8").write(out + "\n")
    if any(ok is False for _, ok, _ in rows):
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    vedit.P = P = vedit.Project(sys.argv[1])
    {"voice": voice, "full": full, "hook": hook}[sys.argv[2]](P)
