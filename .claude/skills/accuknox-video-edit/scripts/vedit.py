"""Render engine for an AccuKnox screen-recording edit.

    python vedit.py <project> check          judge every narration line for customer identifiers and hard words
    python vedit.py <project> tts            check, then voice every new narration line with ElevenLabs (cached)
    python vedit.py <project> plan           print the timeline, write output/timeline.json + narration.srt
    python vedit.py <project> qc B12:3 ...   render chosen frames (beat id : seconds into beat) + a grid
    python vedit.py <project> map            write EDIT_MAP_beats.md from edit.py
    python vedit.py <project> render         render, mix narration, mux the MP4 with chapters
    python vedit.py <project> render --until 20   render only the first 20 s, a preview
    python vedit.py <project> tts --until 20      voice only the lines a 20 s preview needs

<project> is a folder holding edit.py. edit.py is the only file you edit. Every source
time in it is a source-video second, and every rect and view is in source pixels.
"""
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from collections import OrderedDict

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import brand  # noqa: E402
import eleven  # noqa: E402


# ---------------------------------------------------------------- tools
def find_tool(name):
    """Prefer a modern build. ImageMagick ships an old ffmpeg 4.2 that shadows it on PATH."""
    env = os.environ.get(name.upper())
    cands = [env, rf"C:\ProgramData\chocolatey\bin\{name}.exe", shutil.which(name)]
    for p in cands:
        if p and os.path.exists(p):
            return p
    sys.exit(f"{name} not found. Install it: choco install ffmpeg  (or winget install Gyan.FFmpeg)")


FF = find_tool("ffmpeg")
FP = find_tool("ffprobe")


def first_font(*names):
    for n in names:
        for d in (r"C:\Windows\Fonts", "/usr/share/fonts/truetype/dejavu", "/Library/Fonts"):
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    return None


FONT_B = first_font("segoeuib.ttf", "DejaVuSans-Bold.ttf", "Arial Bold.ttf")
FONT_SB = first_font("seguisb.ttf", "DejaVuSans-Bold.ttf", "Arial Bold.ttf")
FONT_R = first_font("segoeui.ttf", "DejaVuSans.ttf", "Arial.ttf")
ACCENT = (255, 176, 32)   # amber highlight
INK = (17, 24, 39)        # label background


# ---------------------------------------------------------------- project
class Project:
    def __init__(self, root):
        self.root = os.path.abspath(root)
        spec = importlib.util.spec_from_file_location("edit", os.path.join(self.root, "edit.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        self.m = m
        g = lambda k, d=None: getattr(m, k, d)
        self.src = self.path(g("SOURCE"))
        if not os.path.exists(self.src):
            sys.exit(f"SOURCE not found: {self.src}")
        self.share = tuple(g("SHARE"))                      # (x, y, w, h) of the shared screen
        out = g("OUTPUT", {})
        fw, fh = fit_16_9(self.share[2], self.share[3])
        self.W = int(out.get("width", fw))
        self.H = int(out.get("height", fh))
        if self.W > self.share[2] or self.H > self.share[3]:
            print(f"warning: output {self.W}x{self.H} is larger than SHARE, which upscales the source")
        self.out_name = out.get("name", "edit.mp4")
        self.meta_title = out.get("title", "AccuKnox recording (internal)")
        self.out_dir = self.path(out.get("dir", "output"))
        pace = g("PACE", {})
        self.base = float(pace.get("base", 1.0))
        self.vo_tempo = float(pace.get("vo_tempo", 1.0))
        self.badge_from = float(pace.get("badge_from", 1.6))
        voice = g("VOICE", {})
        self.voice_id = voice.get("voice_id", eleven.DEFAULT_VOICE)     # Alice, British female
        self.model = voice.get("model", eleven.MODEL)                   # eleven_v4
        self.voice_settings = voice.get("settings", eleven.DEFAULT_SETTINGS)
        self.vo_dir = self.path(g("VO_DIR", "vo"))
        self.intro = g("INTRO")
        self.hook = g("HOOK")             # the first 5 s: floating product shots, then the logo slam
        self.outro = g("OUTRO")           # the end card: logo, title, call to action
        b = g("BRAND", {})
        self.watermark = b.get("watermark", "br")    # corner of the logo on every product frame, or None
        self.sfx = b.get("sfx", True)                # whooshes, hits and the pad under hook and end card
        self.jev = g("JEV", "narration")                   # off | narration | all (see jev.py)
        self.redact = list(g("REDACT", []))             # (t0, t1, x, y, w, h) source seconds and pixels
        self.sections = g("SECTIONS", {})
        self.beats = g("BEATS")
        self.xfade = int(g("XFADE", 6))
        self.title_dur = float(g("TITLE_DUR", 2.2))
        self.gap = float(g("GAP", 0.35))
        self.tail = float(g("TAIL", 0.6))
        self.views = {k: v for k, v in vars(m).items()
                      if k.isupper() and isinstance(v, tuple) and len(v) == 3 and all(isinstance(x, (int, float)) for x in v)}
        self.default_view = g("FULL") or (self.share[0], self.share[1], self.share[2])
        self.fps = probe_fps(self.src)

    def path(self, p):
        return p if os.path.isabs(p) else os.path.join(self.root, p)


def fit_16_9(w, h):
    """The largest even 16:9 size that fits inside w x h, so nothing is upscaled."""
    if w * 9 <= h * 16:
        W = w // 2 * 2
        return W, round(W * 9 / 16 / 2) * 2
    H = h // 2 * 2
    return round(H * 16 / 9 / 2) * 2, H


def probe_fps(path):
    r = subprocess.run([FP, "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=r_frame_rate",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    a, b = r.stdout.strip().split("/")
    return float(a) / float(b)


P = None  # the loaded Project


# ---------------------------------------------------------------- narration
def raw_path(text):
    key = f"{P.voice_id}|{P.model}|{json.dumps(P.voice_settings, sort_keys=True)}|{text}"
    return os.path.join(P.vo_dir, hashlib.sha1(key.encode()).hexdigest()[:16] + ".mp3")


def legacy_path(text):
    return os.path.join(P.vo_dir, hashlib.sha1(f"{P.voice_id}|{P.model}|{text}".encode()).hexdigest()[:16] + ".mp3")


def line_path(text):
    """The voiced line after the tempo change. atempo keeps the pitch."""
    src = raw_path(text)
    if not os.path.exists(src) and os.path.exists(legacy_path(text)):
        src = legacy_path(text)
    if P.vo_tempo == 1.0 or not os.path.exists(src):
        return src
    out = src[:-4] + f"_t{P.vo_tempo:g}.wav"
    if not os.path.exists(out):
        subprocess.run([FF, "-v", "error", "-y", "-i", src, "-af", f"atempo={P.vo_tempo}", "-ar", "44100", out],
                       check=True)
    return out


def duration(path):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    return float(r.stdout.strip())


def speech_bounds(path):
    """(lead, end) seconds of real speech inside a voiced file."""
    pcm = subprocess.run([FF, "-v", "error", "-i", path, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768
    win = 160
    n = len(a) // win
    rms = np.sqrt((a[: n * win].reshape(n, win) ** 2).mean(1))
    on = np.where(rms > 0.01)[0]
    if len(on) == 0:
        return 0.0, len(a) / 16000
    return on[0] * win / 16000, (on[-1] + 1) * win / 16000


def all_lines():
    return [t for b in beat_list() for _, t in b.get("lines", [])]


def check(lines=None, strict=True):
    """Gate narration before it leaves the machine. Jev judges meaning, code patterns are the floor."""
    import jev
    lines = all_lines() if lines is None else lines
    if not lines:
        return True
    # A v4 audio tag such as "[confident]" is direction for the voice, not text, so the gate
    # judges the words alone. The tag still goes to ElevenLabs.
    import re
    lines = [re.sub(r"\[[a-z ]+\]\s*", "", l).strip() for l in lines]
    if P.jev == "off":
        blocked = [(i, f"pattern: {h}") for i, l in enumerate(lines) for h in jev.narration_fallback(l) if h != "acronym"]
        warns = [(i, "pattern: acronym") for i, l in enumerate(lines) if "acronym" in jev.narration_fallback(l)]
        used = False
    else:
        blocked, warns, used = jev.gate(lines, getattr(P.m, "JEV_TERMS", ()))
    print(f"narration check over {len(lines)} lines, {'Jev + patterns' if used else 'patterns only'}")
    for i, why in blocked:
        print(f"  BLOCK  {why:<40} {lines[i]}")
    for i, why in warns:
        print(f"  warn   {why:<40} {lines[i]}")
    if blocked and strict:
        print("Rewrite the blocked lines in edit.py. Nothing was sent to ElevenLabs.")
        return False
    return True


def tts(until=None):
    """Voice every line not yet cached. With `until`, only lines that start before that output
    second, re-planned after each pass because a voiced line moves the ones after it."""
    os.makedirs(P.vo_dir, exist_ok=True)

    def have(t):
        return os.path.exists(raw_path(t)) or os.path.exists(legacy_path(t))
    for _ in range(4):
        want = all_lines() if until is None else [l["text"] for l in plan()[1] if l["t"] < until]
        new = [t for t in dict.fromkeys(want) if not have(t)]
        if not new:
            return
        if not check(new):
            sys.exit(1)
        for text in new:
            eleven.tts(text, P.voice_id, raw_path(text), P.model, P.voice_settings)
            print(f"  {duration(raw_path(text)):5.2f}s  {text[:72]}")
        if until is None:
            return


# ---------------------------------------------------------------- timeline
def clip_len(c):
    return c["dur"] if any(k in c for k in ("hold", "intro", "hook", "outro")) else (c["b"] - c["a"]) / c["speed"]


def card(c):
    return any(k in c for k in ("intro", "hook", "outro"))


def paced(c):
    c = dict(c)
    if card(c):
        return c
    if c.get("view") is None:
        c["view"] = P.default_view
    if "hold" in c:
        c["dur"] = c["dur"] / P.base
    else:
        c["speed"] = c["speed"] * P.base
    return c


def beat_list():
    beats = list(P.beats)
    if P.intro:
        beats.insert(0, dict(id="B00", intro=True, clips=[dict(intro=True, dur=P.intro.get("dur", 2.0))],
                             lines=[(P.intro.get("line_at", 0.3), P.intro["line"])] if P.intro.get("line") else []))
    if P.hook:
        beats.insert(0, dict(id="HOOK", intro=True, clips=[dict(hook=True, dur=P.hook.get("dur", 5.0))],
                             lines=[(P.hook.get("line_at", 0.12), P.hook["line"])] if P.hook.get("line") else []))
    if P.outro:
        beats.append(dict(id="END", intro=True, clips=[dict(outro=True, dur=P.outro.get("dur", 4.5))],
                          lines=[(P.outro.get("line_at", 0.5), P.outro["line"])] if P.outro.get("line") else []))
    return beats


def plan():
    t = 0.0
    beats, lines, chapters = [], [], []
    for b in beat_list():
        clips = [paced(x) for x in b["clips"]]
        vis = sum(clip_len(c) for c in clips)
        cursor, need = 0.0, 0.0
        placed = []
        for off, text in b.get("lines", []):
            p = line_path(text)
            lead, end = speech_bounds(p) if os.path.exists(p) else (0.0, len(text) / 15.0)
            start = max(0.0, max(off if b.get("intro") else off / P.base, cursor) - lead)
            placed.append((start, p, text, lead, end))
            cursor = start + end + P.gap
            need = start + end + P.tail
        if need > vis and b.get("intro"):
            clips[-1]["dur"] += need - vis
            vis = need
        if need > vis:  # the voice runs long: hold the last frame of the beat
            last = clips[-1]
            src_t = last["hold"] if "hold" in last else last["b"] - 1.0 / P.fps
            view = last["view"][1] if isinstance(last["view"][0], tuple) else last["view"]
            clips.append(dict(hold=src_t, dur=need - vis, view=view, ann=last["ann"]))
            vis = need
        if b.get("section"):
            chapters.append((t, b["section"], P.sections[b["section"]]))
        for start, p, text, lead, end in placed:
            lines.append(dict(t=t + start, path=p, text=text, speak_from=t + start + lead, speak_to=t + start + end))
        beats.append(dict(id=b["id"], start=t, dur=vis, section=b.get("section"), clips=clips, intro=b.get("intro")))
        t += vis
    return beats, lines, chapters, t


def fmt(s):
    return f"{int(s // 60)}:{s % 60:05.2f}"


def write_plan(beats, lines, chapters, total):
    os.makedirs(P.out_dir, exist_ok=True)
    with open(os.path.join(P.out_dir, "timeline.json"), "w", encoding="utf-8") as f:
        json.dump(dict(total=total, chapters=chapters, beats=beats, lines=lines), f, indent=1, default=str)

    def ts(s):
        return f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d},{int(s * 1000) % 1000:03d}"
    with open(os.path.join(P.out_dir, "narration.srt"), "w", encoding="utf-8") as f:
        for i, l in enumerate(lines, 1):
            f.write(f"{i}\n{ts(l['speak_from'])} --> {ts(l['speak_to'])}\n{l['text']}\n\n")


# ---------------------------------------------------------------- source reader
class Source:
    """Sequential reader with a small cache. Returns only the shared-screen area."""

    def __init__(self):
        self.cap = cv2.VideoCapture(P.src)
        self.idx = -1
        self.cache = OrderedDict()
        x, y, w, h = P.share
        self.crop = (slice(y, y + h), slice(x, x + w))

    def get(self, t):
        want = max(0, int(round(t * P.fps)))
        if want in self.cache:
            return self.cache[want]
        if want < self.idx:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, max(0, want - 50))
            self.idx = int(self.cap.get(cv2.CAP_PROP_POS_FRAMES)) - 1
        while self.idx < want:
            ok, fr = self.cap.read()
            if not ok:
                break
            self.idx += 1
            self.cache[self.idx] = fr[self.crop]
            if len(self.cache) > 80:
                self.cache.popitem(last=False)
        return self.cache[min(want, self.idx)]


# ---------------------------------------------------------------- redaction
def redact(frame, t):
    """Pixelate then blur every REDACT rect live at source time t. Runs before any zoom, so rects
    stay in source pixels. Returns a copy, so the reader cache keeps the clean frame."""
    hits = [r for r in P.redact if r[0] - 1e-3 <= t <= r[1] + 1e-3]
    if not hits:
        return frame
    out = frame.copy()
    H, W = out.shape[:2]
    for _, _, x, y, w, h in hits:
        x0, y0 = max(0, int(x - P.share[0])), max(0, int(y - P.share[1]))
        x1, y1 = min(W, int(x - P.share[0] + w)), min(H, int(y - P.share[1] + h))
        if x1 <= x0 or y1 <= y0:
            continue
        roi = out[y0:y1, x0:x1]
        small = cv2.resize(roi, (max(1, (x1 - x0) // 14), max(1, (y1 - y0) // 14)), interpolation=cv2.INTER_AREA)
        big = cv2.resize(small, (x1 - x0, y1 - y0), interpolation=cv2.INTER_NEAREST)
        out[y0:y1, x0:x1] = cv2.GaussianBlur(big, (0, 0), 4)
    return out


# ---------------------------------------------------------------- drawing
def ease(x):
    x = min(max(x, 0.0), 1.0)
    return 4 * x * x * x if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def view_at(view, local_t):
    if isinstance(view[0], tuple):
        v0, v1 = view
        k = ease(local_t / 0.8)
        return tuple(v0[i] + (v1[i] - v0[i]) * k for i in range(3))
    return view


def warp(frame, v):
    """Scale source view v=(x, y, w) to the output size. frame is already cropped to SHARE."""
    W, H = P.W, P.H
    x, y, w = v[0] - P.share[0], v[1] - P.share[1], v[2]
    s = W / w
    if abs(s - 1) < 1e-3 and float(x).is_integer() and float(y).is_integer() and x >= 0 and y >= 0:
        out = frame[int(y):int(y) + H, int(x):int(x) + W]
        if out.shape[0] < H or out.shape[1] < W:
            pad = np.zeros((H, W, 3), np.uint8)
            pad[: out.shape[0], : out.shape[1]] = out
            out = pad
        return out
    M = np.float32([[s, 0, -x * s], [0, s, -y * s]])
    out = cv2.warpAffine(frame, M, (W, H), flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
    if s > 1.15:  # light unsharp mask keeps enlarged UI text crisp
        blur = cv2.GaussianBlur(out, (0, 0), 1.0)
        out = cv2.addWeighted(out, 1.35, blur, -0.35, 0)
    return out


_fonts = {}


def font(path, size):
    k = (path, size)
    if k not in _fonts:
        _fonts[k] = ImageFont.truetype(path, size) if path else ImageFont.load_default()
    return _fonts[k]


def map_rect(r, v):
    x, y, w = v
    s = P.W / w
    return ((r[0] - x) * s, (r[1] - y) * s, r[2] * s, r[3] * s)


def draw_label(d, text, anchor, pos, alpha, at=None):
    W, H = P.W, P.H
    f = font(FONT_SB, 24)
    tw = d.textlength(text, font=f)
    pw, ph = tw + 34, 44
    ax, ay, aw, ah = anchor
    if at is not None:
        px, py = at
    elif pos == "below":
        px, py = ax, ay + ah + 10
    elif pos == "above":
        px, py = ax, ay - ph - 10
    elif pos == "right":
        px, py = ax + aw + 14, ay + ah / 2 - ph / 2
    else:
        px, py = ax - pw - 14, ay + ah / 2 - ph / 2
    px = min(max(px, 12), W - pw - 12)
    py = min(max(py, 12), H - ph - 12)
    d.rounded_rectangle((px, py, px + pw, py + ph), 10, fill=INK + (int(235 * alpha),))
    d.rounded_rectangle((px, py, px + 6, py + ph), 3, fill=ACCENT + (int(255 * alpha),))
    d.text((px + 20, py + ph / 2), text, font=f, fill=(255, 255, 255, int(255 * alpha)), anchor="lm")


def overlay(frame, anns, v, src_t, rng, title, speed, t_out):
    W, H = P.W, P.H
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    drew = False
    for an in anns:
        st0, st1 = an["st"]
        if not (st0 - 1e-3 <= src_t <= st1 + 1e-3):
            continue
        a0, a1 = max(st0, rng[0]), min(st1, rng[1])   # fade over 0.25 s of output time
        fin = (src_t - a0) / speed / 0.25 if speed else 1.0
        fout = (a1 - src_t) / speed / 0.25 if (speed and a1 < rng[1] - 1e-3) else 1.0
        alpha = max(0.0, min(1.0, fin, fout))
        if alpha <= 0:
            continue
        r = map_rect(an["rect"], v)
        x0, y0, x1, y1 = r[0] - 4, r[1] - 4, r[0] + r[2] + 4, r[1] + r[3] + 4
        d.rounded_rectangle((x0 - 3, y0 - 3, x1 + 3, y1 + 3), 12, outline=ACCENT + (int(70 * alpha),), width=4)
        d.rounded_rectangle((x0, y0, x1, y1), 10, outline=ACCENT + (int(255 * alpha),), width=3)
        if an.get("text"):
            at = None
            if an.get("at"):
                m = map_rect((an["at"][0], an["at"][1], 0, 0), v)
                at = (m[0], m[1])
            draw_label(d, an["text"], (x0, y0, x1 - x0, y1 - y0), an["pos"], alpha, at)
        drew = True
    if speed and speed >= P.badge_from:
        f = font(FONT_SB, 20)
        txt = f"{round(speed, 1):g}x speed"
        tw = d.textlength(txt, font=f)
        right = W - 16
        if P.watermark and P.watermark[0] == "b" and P.watermark[1] == "r":
            right = brand.watermark_box(W, H, P.watermark)[0] - 14
        d.rounded_rectangle((right - tw - 28, H - 52, right, H - 16), 9, fill=(17, 24, 39, 190))
        d.text((right - tw - 14, H - 34), txt, font=f, fill=(255, 255, 255, 235), anchor="lm")
        drew = True
    if title is not None:
        num, name, tt = title
        if tt < P.title_dur:
            k = 1.0 if tt < P.title_dur - 0.5 else (P.title_dur - tt) / 0.5
            if t_out > 0.5:
                k = min(k, tt / 0.3)
            k = max(0.0, min(1.0, k))
            d.rectangle((0, 0, W, H), fill=(8, 12, 24, int(150 * k)))
            d.text((W / 2, H / 2 - 52), f"SECTION {num} OF {len(P.sections)}", font=font(FONT_SB, 26),
                   fill=ACCENT + (int(255 * k),), anchor="mm")
            d.text((W / 2, H / 2 + 12), name, font=font(FONT_B, 64), fill=(255, 255, 255, int(255 * k)), anchor="mm")
            d.rounded_rectangle((W / 2 - 40, H / 2 + 62, W / 2 + 40, H / 2 + 67), 2, fill=ACCENT + (int(255 * k),))
            drew = True
    if not drew:
        return frame
    base = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).convert("RGBA")
    base.alpha_composite(ov)
    return cv2.cvtColor(np.array(base.convert("RGB")), cv2.COLOR_RGB2BGR)


# ---------------------------------------------------------------- intro card
_intro_base = {}


def intro_frame(src, lt, dur):
    """Opening card over a blurred, dimmed frame of the recording itself. No outside imagery."""
    W, H, cfg = P.W, P.H, P.intro
    if "img" not in _intro_base:
        bt = cfg.get("backdrop_t", 0.0)
        fr = warp(redact(src.get(bt), bt), cfg.get("backdrop_view", P.default_view))
        fr = cv2.GaussianBlur(fr, (0, 0), 14)
        fr = cv2.addWeighted(fr, 0.2, np.full_like(fr, (34, 20, 12)), 0.8, 0)
        _intro_base["img"] = fr
    z = 1.0 + 0.035 * (lt / dur)  # slow push-in on the backdrop
    M = cv2.getRotationMatrix2D((W / 2, H / 2), 0, z)
    bg = cv2.warpAffine(_intro_base["img"], M, (W, H), borderMode=cv2.BORDER_REFLECT)
    base = Image.fromarray(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)).convert("RGBA")
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    sx = W / 1440  # layout is designed at 1440 wide

    def a(t0):
        k = ease((lt - t0) / 0.6)
        return k, (1 - k) * 14

    k, dy = a(0.15)
    d.text((120 * sx, 222 * sx + dy), cfg.get("kicker", "").upper(), font=font(FONT_SB, int(24 * sx)),
           fill=ACCENT + (int(255 * k),))
    k, dy = a(0.35)
    d.text((114 * sx, 258 * sx + dy), cfg.get("title", ""), font=font(FONT_B, int(84 * sx)),
           fill=(255, 255, 255, int(255 * k)))
    k, dy = a(0.55)
    d.text((120 * sx, 378 * sx + dy), cfg.get("subtitle", ""), font=font(FONT_R, int(32 * sx)),
           fill=(214, 222, 235, int(255 * k)))
    k, _ = a(0.7)
    d.rounded_rectangle((120 * sx, 444 * sx, (120 + 120 * k) * sx, 449 * sx), 2, fill=ACCENT + (int(255 * k),))
    if cfg.get("chapters", True):
        x, y = 120 * sx, 540 * sx
        fs = font(FONT_SB, int(19 * sx))
        for i in sorted(P.sections):
            k, dy = a(0.9 + 0.09 * i)
            label = f"{i}   {P.sections[i]}"
            w = d.textlength(label, font=fs) + 30 * sx
            if x + w > W - 110 * sx:
                x, y = 120 * sx, y + 50 * sx
            d.rounded_rectangle((x, y + dy, x + w, y + 38 * sx + dy), 8, fill=(255, 255, 255, int(22 * k)),
                                outline=(255, 255, 255, int(60 * k)), width=1)
            d.text((x + 15 * sx, y + 19 * sx + dy), label, font=fs, fill=(230, 236, 245, int(255 * k)), anchor="lm")
            x += w + 12 * sx
    k, _ = a(1.6)
    d.text((120 * sx, H - 70 * sx), cfg.get("footer", ""), font=font(FONT_R, int(18 * sx)),
           fill=(160, 170, 185, int(255 * k)))
    base.alpha_composite(ov)
    K = brand.kit(W, H)
    if K.logo is not None:   # the logo on the title card, top left above the kicker
        lg = K.logo_at(260 * sx).copy()
        k, _ = a(0.0)
        lg.putalpha(lg.getchannel("A").point(lambda v: int(v * k)))
        base.alpha_composite(lg, (int(120 * sx), int(120 * sx)))
    return cv2.cvtColor(np.array(base.convert("RGB")), cv2.COLOR_RGB2BGR)


# ---------------------------------------------------------------- hook and end card
def hook_ctx(src, dur):
    shots = P.hook["shots"]

    def screen(i, p):
        sh = shots[i]
        st = sh["t"] if "t" in sh else sh["a"] + p * (sh["b"] - sh["a"])
        v = sh.get("view") or P.default_view
        if isinstance(v[0], tuple):
            v = tuple(v[0][j] + (v[1][j] - v[0][j]) * p for j in range(3))
        return warp(redact(src.get(st), st), v)
    return dict(K=brand.kit(P.W, P.H), cfg=P.hook, dur=dur, screen=screen)


def outro_ctx(src, dur):
    bd = None
    if P.outro.get("backdrop_t") is not None:
        bt = P.outro["backdrop_t"]
        bd = warp(redact(src.get(bt), bt), P.outro.get("backdrop_view", P.default_view))
    return dict(K=brand.kit(P.W, P.H), cfg=P.outro, dur=dur, backdrop=bd)


# ---------------------------------------------------------------- frames
def frames(beats, total, wanted=None, until=None):
    """Yield (frame_index, image). With `wanted`, only those indices are drawn (fast QC).
    With `until`, stop at that output second and fade out there."""
    src = Source()
    prev = None
    fi = 0
    flash_to = -1
    end = min(total, until) if until else total
    stop = int(round(end * P.fps))
    for b in beats:
        sec = b["section"]
        beat_t = 0.0
        for ci, c in enumerate(b["clips"]):
            n = int(round(clip_len(c) * P.fps))
            hold = "hold" in c
            if "hook" in c:
                ctx = hook_ctx(src, clip_len(c))
                flash_to = fi + n + 5
            elif "outro" in c:
                ctx = outro_ctx(src, clip_len(c))
            for k in range(n):
                if fi >= stop:
                    return
                lt = k / P.fps
                t_now = fi / P.fps
                draw = wanted is None or fi in wanted
                if draw:
                    if "hook" in c:
                        fr = brand.hook_frame(ctx, lt)
                    elif "outro" in c:
                        fr = brand.outro_frame(ctx, lt)
                    elif "intro" in c:
                        fr = intro_frame(src, lt, clip_len(c))
                    else:
                        if hold:
                            st, sp, rng = c["hold"], 0, (c["hold"], c["hold"])
                        else:
                            st, sp, rng = c["a"] + lt * c["speed"], c["speed"], (c["a"], c["b"])
                        v = view_at(c["view"], lt)
                        fr = warp(redact(src.get(st), st), v)
                        if wanted is None and k < P.xfade and prev is not None and not hold and fi >= flash_to:
                            al = (k + 1) / (P.xfade + 1)
                            fr = cv2.addWeighted(fr, al, prev, 1 - al, 0)
                        title = (sec, P.sections[sec], beat_t) if sec else None
                        fr = overlay(fr, c["ann"], v, st, rng, title, sp, t_now)
                        if fi < flash_to:   # land out of the hook on a white flash
                            kf = (flash_to - fi) / 5.0
                            fr = np.clip(fr.astype(np.float32) + 255 * 0.5 * kf, 0, 255).astype(np.uint8)
                        if P.watermark:
                            fr = brand.watermark(fr, P.watermark)
                    if not P.hook and t_now < 0.6:
                        fr = (fr * (t_now / 0.6)).astype(np.uint8)
                    if t_now > end - 1.2:
                        fr = (fr * max(0.0, (end - t_now) / 1.2)).astype(np.uint8)
                    prev = fr
                    yield fi, fr
                fi += 1
                beat_t += 1 / P.fps


def render(beats, lines, chapters, total, until=None):
    os.makedirs(P.out_dir, exist_ok=True)
    if until:
        total = min(total, until)
        lines = [l for l in lines if l["t"] < total]
        chapters = [ch for ch in chapters if ch[0] < total]
    silent = os.path.join(P.out_dir, "_video.mp4")
    p = subprocess.Popen([FF, "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "bgr24", "-s", f"{P.W}x{P.H}",
                          "-r", f"{P.fps:g}", "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "15",
                          "-pix_fmt", "yuv420p", "-movflags", "+faststart", silent], stdin=subprocess.PIPE)
    last = -1
    for fi, fr in frames(beats, total, until=until):
        p.stdin.write(fr.tobytes())
        t = fi / P.fps
        if int(t) // 30 != last:
            last = int(t) // 30
            print(f"  rendered {fmt(t)} / {fmt(total)}", flush=True)
    p.stdin.close()
    p.wait()

    audio = os.path.join(P.out_dir, "_narration.wav")
    ins = [l["path"] for l in lines]
    delays = [l["t"] for l in lines]
    events = []
    if P.sfx:
        for b in beats:
            if b["id"] == "HOOK":
                events += brand.hook_sfx(b["start"], P.hook, b["dur"])
            elif b["id"] == "END":
                events += brand.outro_sfx(b["start"], b["dur"])
    if events:
        ins.append(brand.sfx_track(events, total, os.path.join(P.out_dir, "_sfx.wav")))
        delays.append(0.0)
    if ins:
        args = [FF, "-v", "error", "-y"]
        for pth in ins:
            args += ["-i", pth]
        fc = [f"[{i}:a]aresample=48000,aformat=channel_layouts=mono,adelay={int(round(d * 1000))}:all=1[a{i}]"
              for i, d in enumerate(delays)]
        fc.append("".join(f"[a{i}]" for i in range(len(ins))) +
                  f"amix=inputs={len(ins)}:normalize=0,apad,atrim=0:{total:.3f},"
                  f"afade=t=out:st={max(0, total - 1.2):.3f}:d=1.2,"
                  "loudnorm=I=-16:TP=-1.5:LRA=11,aresample=48000[out]")
        subprocess.run(args + ["-filter_complex", ";".join(fc), "-map", "[out]", "-ac", "2", audio], check=True)
    else:
        subprocess.run([FF, "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                        "-t", f"{total:.3f}", audio], check=True)

    meta = os.path.join(P.out_dir, "_chapters.txt")
    with open(meta, "w", encoding="utf-8") as f:
        f.write(f";FFMETADATA1\ntitle={P.meta_title}\n")
        for i, (t0, num, name) in enumerate(chapters):
            t1 = chapters[i + 1][0] if i + 1 < len(chapters) else total
            f.write(f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={int(t0 * 1000)}\nEND={int(t1 * 1000)}\ntitle={num}. {name}\n")
    # A preview never overwrites the full render.
    final = os.path.join(P.out_dir, P.out_name if not until else P.out_name[:-4] + "_preview.mp4")
    subprocess.run([FF, "-v", "error", "-y", "-i", silent, "-i", audio, "-i", meta, "-map", "0:v", "-map", "1:a",
                    "-map_metadata", "2", "-map_chapters", "2", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", "-movflags", "+faststart", final], check=True)
    print("wrote", final)


def qc(beats, total, specs):
    """specs like B12:7.5 = 7.5 output seconds into beat B12. Writes qc_*.jpg and qc_grid_N.jpg."""
    start = {b["id"]: b["start"] for b in beats}
    targets = {}
    for s in specs:
        bid, off = s.split(":")
        targets[int(round((start[bid] + float(off)) * P.fps))] = s
    paths = []
    for fi, fr in frames(beats, total, set(targets)):
        p = os.path.join(P.out_dir, f"qc_{targets[fi].replace(':', '_')}.jpg")
        cv2.imwrite(p, fr, [cv2.IMWRITE_JPEG_QUALITY, 92])
        paths.append(p)
    for g in range(0, len(paths), 4):
        tw, th = P.W // 2, P.H // 2
        grid = Image.new("RGB", (tw * 2, th * 2))
        for i, p in enumerate(paths[g:g + 4]):
            grid.paste(Image.open(p).resize((tw, th)), ((i % 2) * tw, (i // 2) * th))
        gp = os.path.join(P.out_dir, f"qc_grid_{g // 4}.jpg")
        grid.save(gp, quality=90)
        print(gp)


def edit_map():
    names = {v: k for k, v in P.views.items()}

    def m(s):
        return f"{int(s // 60)}:{s % 60:04.1f}"

    def vname(x):
        if x is None:
            return "default"
        if isinstance(x[0], tuple):
            return f"{vname(x[0])} -> {vname(x[1])}"
        return f"{names.get(x, str(x))} ({P.W / x[2]:.2f}x)"
    out = ["# Edit Map, Generated From edit.py", "",
           f"Source `{os.path.basename(P.src)}`. Times are source m:ss. Base pace {P.base}x, "
           f"narration tempo {P.vo_tempo}x. Do not hand-edit, rerun `vedit.py <project> map`.", ""]
    if P.hook:
        shots = " / ".join(sh.get("text", "") for sh in P.hook["shots"])
        out += [f"Hook, {P.hook.get('dur', 5.0)} s: {shots}, then the logo and '{P.hook.get('tagline', '')}'", ""]
        if P.hook.get("line"):
            out += [f"VO: \"{P.hook['line']}\"", ""]
    if P.intro:
        out += [f"Intro card, {P.intro.get('dur', 2.0)} s: {P.intro.get('title', '')}", ""]
        if P.intro.get("line"):
            out += [f"VO: \"{P.intro['line']}\"", ""]
    for b in P.beats:
        if b.get("section"):
            out += [f"## {b['section']}. {P.sections[b['section']]}", "",
                    "| Beat | Source in-out | Speed | Framing | Callouts |", "|---|---|---|---|---|"]
        for c in b["clips"]:
            anns = "; ".join(a["text"] or "box" for a in c["ann"]) or "-"
            if "hold" in c:
                out.append(f"| {b['id']} | hold {m(c['hold'])} for {c['dur']}s | freeze | {vname(c['view'])} | {anns} |")
            else:
                out.append(f"| {b['id']} | {m(c['a'])} - {m(c['b'])} | {c['speed']}x | {vname(c['view'])} | {anns} |")
        for off, t in b.get("lines", []):
            out.append(f"| | VO at +{off}s | | | \"{t}\" |")
    p = os.path.join(P.root, "EDIT_MAP_beats.md")
    open(p, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(p)


def main():
    global P
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    P = Project(sys.argv[1])
    cmd = sys.argv[2]
    until = None
    if "--until" in sys.argv:
        until = float(sys.argv[sys.argv.index("--until") + 1])
    if cmd == "tts":
        return tts(until)
    if cmd == "check":
        return check(strict=False)
    if cmd == "map":
        return edit_map()
    beats, lines, chapters, total = plan()
    write_plan(beats, lines, chapters, total)
    if cmd == "plan":
        for b in beats:
            print(f"{b['id']:>4}  {fmt(b['start'])}  {b['dur']:5.1f}s  {('section ' + str(b['section'])) if b['section'] else ''}")
        missing = [l["text"] for l in lines if not os.path.exists(l["path"])]
        if missing:
            print(f"{len(missing)} lines not voiced yet, timings are estimates. Run: tts")
        print("total", fmt(total), f"| output {P.W}x{P.H} @ {P.fps:g} fps")
    elif cmd == "render":
        render(beats, lines, chapters, total, until)
    elif cmd == "qc":
        qc(beats, total, [a for a in sys.argv[3:] if ":" in a])
    else:
        sys.exit(f"unknown command {cmd}\n{__doc__}")


if __name__ == "__main__":
    main()
