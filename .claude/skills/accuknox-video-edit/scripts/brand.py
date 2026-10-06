"""Brand layer for an AccuKnox edit: the 5 s hook, the logo watermark, the end card and the
sound design. Pure OpenCV, PIL and numpy, so it renders the same on every machine.

The hook is built from the recording's own frames. Each shot floats the product screen in
3D over a dark brand field, pushes the camera toward one fact, and punches that fact in as
kinetic type. The last beat slams the AccuKnox logo in. Nothing here invents a screen.

vedit.py calls three things per frame:
    hook_frame(ctx, lt)      the hook at local time lt
    outro_frame(ctx, lt)     the end card at local time lt
    watermark(frame)         the corner logo on every product frame
and one thing per render:
    sfx_track(events, total, path)   a WAV of whooshes, hits and the pad, mixed under the voice
"""
import math
import os
import wave

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(HERE, "..", "assets"))
LOGO_PATH = os.path.join(ASSETS, "logo-white-hd.png")

# Brand colours from the logo mark, RGB.
RED = (214, 16, 48)
BLUE = (0, 76, 255)
VIOLET = (112, 112, 255)
NAVY = (7, 9, 22)


def _font_path(*names):
    for n in names:
        for d in (r"C:\Windows\Fonts", os.path.expanduser(r"~\AppData\Local\Microsoft\Windows\Fonts"),
                  "/usr/share/fonts/truetype/dejavu", "/Library/Fonts"):
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    return None


F_DISPLAY = _font_path("Montserrat-Bold.ttf", "segoeuib.ttf", "DejaVuSans-Bold.ttf")
F_MEDIUM = _font_path("Montserrat-Medium.ttf", "seguisb.ttf", "DejaVuSans.ttf")
F_REGULAR = _font_path("Montserrat-Regular.ttf", "segoeui.ttf", "DejaVuSans.ttf")
_fonts = {}


def font(path, size):
    k = (path, int(size))
    if k not in _fonts:
        _fonts[k] = ImageFont.truetype(path, int(size)) if path else ImageFont.load_default()
    return _fonts[k]


def ease(x):
    x = min(max(x, 0.0), 1.0)
    return 1 - (1 - x) ** 3


def ease_io(x):
    x = min(max(x, 0.0), 1.0)
    return 4 * x ** 3 if x < 0.5 else 1 - (-2 * x + 2) ** 3 / 2


def back_out(x, s=1.4):
    x = min(max(x, 0.0), 1.0) - 1
    return 1 + (s + 1) * x ** 3 + s * x ** 2


# ---------------------------------------------------------------- cached layers
class Kit:
    """Per-size caches: background field, dot grid, vignette, rounded mask, logos."""

    def __init__(self, W, H):
        self.W, self.H = W, H
        sw, sh = W // 4, H // 4
        yy, xx = np.mgrid[0:sh, 0:sw].astype(np.float32)
        self.sx, self.sy = xx / sw, yy / sh
        self.aspect = sw / sh
        # Dot grid, faint, full size.
        g = np.zeros((H, W), np.float32)
        step = max(24, W // 48)
        g[step // 2::step, step // 2::step] = 1.0
        self.grid = cv2.GaussianBlur(g, (0, 0), 1.1) * 3.2
        # Vignette.
        vy, vx = np.mgrid[0:H, 0:W].astype(np.float32)
        d = np.sqrt(((vx / W - 0.5) * 1.15) ** 2 + ((vy / H - 0.5) * 1.0) ** 2)
        self.vig = np.clip(1.15 - d * 1.05, 0.35, 1.0)[..., None]
        # Rounded screen mask.
        m = np.zeros((H, W), np.uint8)
        r = int(W * 0.014)
        cv2.rectangle(m, (r, 0), (W - r, H), 255, -1)
        cv2.rectangle(m, (0, r), (W, H - r), 255, -1)
        for cx, cy in ((r, r), (W - r, r), (r, H - r), (W - r, H - r)):
            cv2.circle(m, (cx, cy), r, 255, -1, cv2.LINE_AA)
        self.mask = m
        # Diagonal coordinate for the light sweep.
        self.diag = (vx + 0.55 * vy) / (W + 0.55 * H)
        self.logo = Image.open(LOGO_PATH).convert("RGBA") if os.path.exists(LOGO_PATH) else None
        self._logo_cache = {}

    def logo_at(self, width):
        width = max(8, int(width))
        if width not in self._logo_cache:
            lg = self.logo.copy()
            lg = lg.resize((width, round(lg.size[1] * width / lg.size[0])), Image.LANCZOS)
            self._logo_cache[width] = lg
        return self._logo_cache[width]


_kits = {}


def kit(W, H):
    if (W, H) not in _kits:
        _kits[(W, H)] = Kit(W, H)
    return _kits[(W, H)]


# ---------------------------------------------------------------- background
def field(K, lt, energy=1.0):
    """The dark brand field: navy base, a red and a blue glow drifting, dot grid, vignette."""
    sx, sy = K.sx, K.sy
    img = np.empty(sx.shape + (3,), np.float32)
    img[:] = NAVY[::-1]
    for (cx, cy, r, col, amp) in (
        (0.18 + 0.05 * math.sin(lt * 0.9), 0.22 + 0.04 * math.cos(lt * 0.7), 0.42, RED, 0.55),
        (0.86 + 0.04 * math.cos(lt * 0.8), 0.80 + 0.05 * math.sin(lt * 0.6), 0.55, BLUE, 0.75),
        (0.55, 0.50, 0.30, VIOLET, 0.18),
    ):
        d2 = ((sx - cx) * K.aspect) ** 2 + (sy - cy) ** 2
        g = np.exp(-d2 / (r * r)) * amp * energy
        img += g[..., None] * np.array(col[::-1], np.float32)
    img = cv2.resize(img, (K.W, K.H), interpolation=cv2.INTER_LINEAR)
    img += K.grid[..., None] * 9.0
    img *= K.vig
    return img


# ---------------------------------------------------------------- floating screen
def project(K, yaw, pitch, scale, cx, cy):
    """Corners of a W x H screen rotated in 3D and projected back to the canvas."""
    W, H = K.W, K.H
    f = 2.4 * W
    out = []
    cyw, syw = math.cos(math.radians(yaw)), math.sin(math.radians(yaw))
    cp, sp = math.cos(math.radians(pitch)), math.sin(math.radians(pitch))
    for x, y in ((-W / 2, -H / 2), (W / 2, -H / 2), (W / 2, H / 2), (-W / 2, H / 2)):
        x, y = x * scale, y * scale
        x1, z1 = x * cyw, x * syw
        y2, z2 = y * cp - z1 * sp, y * sp + z1 * cp
        k = f / (f + z2)
        out.append((cx * W + x1 * k, cy * H + y2 * k))
    return np.float32(out)


def float_screen(K, canvas, screen, yaw, pitch, scale, cx, cy, sweep=None, glow=1.0, alpha=1.0):
    """Composite `screen` (BGR, W x H) into `canvas` (float BGR) as a tilted floating panel."""
    W, H = K.W, K.H
    scr = screen.astype(np.float32)
    if sweep is not None:   # a soft diagonal band of light moving across the glass
        band = np.exp(-((K.diag - sweep) ** 2) / (2 * 0.045 ** 2))
        scr += band[..., None] * 70.0
    dst = project(K, yaw, pitch, scale, cx, cy)
    src = np.float32([(0, 0), (W, 0), (W, H), (0, H)])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(scr, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    m = cv2.warpPerspective(K.mask, M, (W, H), flags=cv2.INTER_LINEAR).astype(np.float32) / 255.0
    # Shadow and coloured glow, computed small for speed.
    small = cv2.resize(m, (W // 4, H // 4), interpolation=cv2.INTER_AREA)
    sh = cv2.GaussianBlur(small, (0, 0), 10)
    sh = cv2.resize(np.roll(sh, 6, axis=0), (W, H))
    canvas *= (1 - 0.65 * alpha * sh)[..., None]
    gl = cv2.resize(cv2.GaussianBlur(small, (0, 0), 7), (W, H))
    tint = np.array(BLUE[::-1], np.float32) * 0.55 + np.array(VIOLET[::-1], np.float32) * 0.45
    canvas += (gl * 0.55 * glow * alpha)[..., None] * tint
    ma = (m * alpha)[..., None]
    canvas[:] = canvas * (1 - ma) + warped * ma
    # Thin bright rim on the glass edge.
    rim = np.clip(m - cv2.erode(m, np.ones((3, 3), np.uint8)), 0, 1)
    canvas += (rim * 90 * alpha)[..., None]
    return canvas


# ---------------------------------------------------------------- type
def text_layer(K, items):
    """items: list of (text, font, size, (x, y), fill RGBA, anchor). Returns RGBA PIL layer with a soft shadow."""
    W, H = K.W, K.H
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow = Image.new("L", (W, H), 0)
    d, ds = ImageDraw.Draw(lay), ImageDraw.Draw(shadow)
    for text, fp, size, (x, y), fill, anchor in items:
        if fill[3] <= 0:
            continue
        f = font(fp, size)
        ds.text((x, y + size * 0.06), text, font=f, fill=int(fill[3] * 0.85), anchor=anchor)
        d.text((x, y), text, font=f, fill=fill, anchor=anchor)
    sh = np.array(shadow, np.float32)
    sh = cv2.GaussianBlur(sh, (0, 0), max(4, W / 260))
    return lay, sh


def comp_layer(canvas, lay, sh=None):
    if sh is not None:
        canvas *= (1 - (sh / 255.0) * 0.75)[..., None]
    a = np.array(lay, np.float32)
    al = a[..., 3:4] / 255.0
    canvas[:] = canvas * (1 - al) + a[..., 2::-1] * al
    return canvas


def gradient_bar(canvas, x0, y0, w, h, alpha=1.0):
    if w < 2 or alpha <= 0:
        return canvas
    x0, y0, w, h = int(x0), int(y0), int(w), int(h)
    H, W = canvas.shape[:2]
    x1, y1 = min(W, x0 + w), min(H, y0 + h)
    if x1 <= x0 or y1 <= y0:
        return canvas
    t = np.linspace(0, 1, x1 - x0, dtype=np.float32)[None, :, None]
    col = np.array(RED[::-1], np.float32) * (1 - t) + np.array(BLUE[::-1], np.float32) * t
    canvas[y0:y1, x0:x1] = canvas[y0:y1, x0:x1] * (1 - alpha) + col * alpha
    return canvas


def kinetic(K, canvas, kicker, headline, lt, dur):
    """Kicker plus a punch-in headline in the lower left, with a dark scrim behind it."""
    W, H = K.W, K.H
    # Scrim: a soft dark pool behind the type.
    x = W * 0.065
    base_y = H * 0.83
    yy, xx = np.mgrid[0:H // 4, 0:W // 4].astype(np.float32)
    d2 = ((xx / (W / 4) - 0.18) / 0.42) ** 2 + ((yy / (H / 4) - 0.86) / 0.32) ** 2
    pool = cv2.resize(np.exp(-d2 * 1.6), (W, H))
    k_in = ease(lt / 0.35)
    canvas *= (1 - 0.84 * pool * k_in)[..., None]
    size = H * 0.118
    words = headline.split()
    items = []
    if kicker:
        ka = ease((lt - 0.05) / 0.3)
        items.append((kicker.upper(), F_MEDIUM, H * 0.026, (x + 4, base_y - size * 1.12 + (1 - ka) * 10),
                      (200, 206, 255, int(255 * ka)), "ls"))
    # Headline: per-word stagger, rise and scale settle.
    f = font(F_DISPLAY, size)
    cursor = x
    for i, wd in enumerate(words):
        p = (lt - 0.08 - 0.07 * i) / 0.32
        a = ease(p)
        rise = (1 - back_out(p)) * size * 0.55
        items.append((wd, F_DISPLAY, size, (cursor, base_y + rise), (255, 255, 255, int(255 * a)), "ls"))
        cursor += f.getlength(wd + " ")
    # Fade out in the last 0.12 s of the shot.
    out_k = 1.0 - ease((lt - (dur - 0.12)) / 0.12)
    items = [(t, fp, s, pos, fill[:3] + (int(fill[3] * out_k),), an) for t, fp, s, pos, fill, an in items]
    lay, sh = text_layer(K, items)
    comp_layer(canvas, lay, sh)
    bw = (cursor - x - f.getlength(" ")) * ease((lt - 0.25) / 0.35)
    gradient_bar(canvas, x + 2, base_y + size * 0.22, bw, max(4, H * 0.007), alpha=out_k)
    return canvas


# ---------------------------------------------------------------- transitions
def whip(img, amount, direction=1):
    """Horizontal motion blur plus a white flash. amount 0..1."""
    if amount <= 0.01:
        return img
    n = int(1 + amount * img.shape[1] * 0.045) | 1
    kern = np.zeros((1, n), np.float32)
    kern[0, :] = 1.0 / n
    out = cv2.filter2D(img, -1, kern, borderType=cv2.BORDER_REPLICATE)
    shift = int(direction * amount * img.shape[1] * 0.02)
    out = np.roll(out, shift, axis=1)
    return out + 255.0 * 0.55 * amount ** 1.5


# ---------------------------------------------------------------- logo
def logo_layer(K, canvas, cx, cy, width, alpha=1.0, shine=None, bloom=0.0):
    if K.logo is None or alpha <= 0:
        return canvas
    lg = K.logo_at(width)
    a = np.array(lg, np.float32)
    h, w = a.shape[:2]
    x0, y0 = int(cx - w / 2), int(cy - h / 2)
    H, W = canvas.shape[:2]
    xs0, ys0, xs1, ys1 = max(0, x0), max(0, y0), min(W, x0 + w), min(H, y0 + h)
    if xs1 <= xs0 or ys1 <= ys0:
        return canvas
    a = a[ys0 - y0:ys1 - y0, xs0 - x0:xs1 - x0]
    al = a[..., 3:4] / 255.0 * alpha
    rgb = a[..., 2::-1].copy()
    if shine is not None:   # a bright band sweeping across the letters
        xx = np.linspace(0, 1, rgb.shape[1], dtype=np.float32)[None, :, None]
        yy = np.linspace(0, 1, rgb.shape[0], dtype=np.float32)[:, None, None]
        band = np.exp(-(((xx + 0.25 * yy) - shine) ** 2) / (2 * 0.04 ** 2))
        rgb = np.minimum(255, rgb + band * 120)
    if bloom > 0:
        glow = np.zeros((H, W), np.float32)
        glow[ys0:ys1, xs0:xs1] = al[..., 0]
        g = cv2.resize(cv2.GaussianBlur(cv2.resize(glow, (W // 4, H // 4)), (0, 0), 9), (W, H))
        tint = np.array(BLUE[::-1], np.float32) * 0.6 + np.array(VIOLET[::-1], np.float32) * 0.4
        canvas += (g * bloom * 1.6)[..., None] * tint
    reg = canvas[ys0:ys1, xs0:xs1]
    canvas[ys0:ys1, xs0:xs1] = reg * (1 - al) + rgb * al
    return canvas


def ring(K, canvas, cx, cy, radius, width, alpha):
    if alpha <= 0:
        return canvas
    W, H = K.W, K.H
    m = np.zeros((H // 2, W // 2), np.float32)
    cv2.circle(m, (int(cx / 2), int(cy / 2)), int(radius / 2), 1.0, max(1, int(width / 2)), cv2.LINE_AA)
    m = cv2.resize(cv2.GaussianBlur(m, (0, 0), 3), (W, H))
    tint = np.array(VIOLET[::-1], np.float32)
    canvas += (m * alpha * 1.2)[..., None] * tint
    return canvas


# ---------------------------------------------------------------- hook
def hook_layout(cfg, dur):
    """Split the hook into shot windows plus the logo slam. Returns ([(t0, t1)], logo_t0)."""
    n = max(1, len(cfg["shots"]))
    slam = float(cfg.get("slam", 1.6))
    shot_total = max(1.8, dur - slam)
    step = shot_total / n
    return [(i * step, (i + 1) * step) for i in range(n)], shot_total


def hook_frame(ctx, lt):
    """ctx: dict(K, cfg, dur, screen(i, p) -> BGR W x H). Returns uint8 BGR."""
    K, cfg, dur = ctx["K"], ctx["cfg"], ctx["dur"]
    W, H = K.W, K.H
    wins, t_logo = hook_layout(cfg, dur)
    canvas = field(K, lt)
    if lt < t_logo:
        i = next(k for k, (a, b) in enumerate(wins) if lt < b or k == len(wins) - 1)
        a, b = wins[i]
        sl = lt - a
        sd = b - a
        p = ease_io(sl / sd)
        side = -1 if i % 2 == 0 else 1
        shot = cfg["shots"][i]
        yaw = side * (17 - 10 * p)
        pitch = 9 - 4 * p
        scale = 0.70 + 0.12 * p
        cx = 0.60 + side * 0.02 * (1 - p)
        cy = 0.44
        scr = ctx["screen"](i, p)
        float_screen(K, canvas, scr, yaw, pitch, scale, cx, cy, sweep=-0.2 + 1.5 * p, glow=1.0)
        kinetic(K, canvas, shot.get("kicker", ""), shot.get("text", ""), sl, sd)
        # Whip in at the start of every shot after the first, and into the logo slam.
        if i > 0 and sl < 0.14:
            canvas = whip(canvas, 1 - sl / 0.14, side)
        if b - lt < 0.08:
            canvas = whip(canvas, 1 - (b - lt) / 0.08, -side)
        if i == 0 and lt < 0.10:   # open on a flash, never on black
            canvas = canvas + 255.0 * 0.6 * (1 - lt / 0.10)
    else:
        q = lt - t_logo
        L = dur - t_logo
        cx, cy = W / 2, H * 0.44
        k = back_out(q / 0.45, 1.2)
        width = W * 0.40 * (1.22 - 0.22 * k)
        ring(K, canvas, cx, cy, W * (0.12 + 0.55 * ease(q / 0.9)), W * 0.006, 0.9 * (1 - ease(q / 0.9)))
        logo_layer(K, canvas, cx, cy, width, alpha=ease(q / 0.22), shine=-0.3 + 1.6 * ease((q - 0.25) / 0.7),
                   bloom=0.9 * (1 - 0.5 * ease(q / 1.2)))
        items = []
        ta = ease((q - 0.35) / 0.4)
        if cfg.get("product"):
            items.append((cfg["product"].upper(), F_MEDIUM, H * 0.03, (cx, cy + H * 0.115 + (1 - ta) * 14),
                          (200, 206, 255, int(255 * ta)), "mm"))
        if cfg.get("tagline"):
            tb = ease((q - 0.5) / 0.4)
            items.append((cfg["tagline"], F_DISPLAY, H * 0.058, (cx, cy + H * 0.19 + (1 - tb) * 18),
                          (255, 255, 255, int(255 * tb)), "mm"))
        if cfg.get("footer"):
            tc = ease((q - 0.7) / 0.4)
            items.append((cfg["footer"], F_REGULAR, H * 0.019, (cx, H * 0.93), (165, 172, 195, int(255 * tc)), "mm"))
        lay, sh = text_layer(K, items)
        comp_layer(canvas, lay, sh)
        if q < 0.12:
            canvas = whip(canvas, 1 - q / 0.12, 1)
        if L - q < 0.1:   # flash out into the body
            canvas = canvas + 255.0 * 0.5 * (1 - (L - q) / 0.1)
    return np.clip(canvas, 0, 255).astype(np.uint8)


# ---------------------------------------------------------------- end card
def outro_frame(ctx, lt):
    """ctx: dict(K, cfg, dur, backdrop BGR or None)."""
    K, cfg, dur = ctx["K"], ctx["cfg"], ctx["dur"]
    W, H = K.W, K.H
    canvas = field(K, lt, energy=0.9)
    if ctx.get("backdrop") is not None:
        p = ease(lt / dur)
        float_screen(K, canvas, ctx["backdrop"], -8 + 4 * p, 6, 0.46 + 0.04 * p, 0.5, 0.80, glow=0.6, alpha=0.35)
    cx, cy = W / 2, H * 0.34
    k = back_out(lt / 0.5, 1.1)
    logo_layer(K, canvas, cx, cy, W * 0.36 * (1.12 - 0.12 * k), alpha=ease(lt / 0.3),
               shine=-0.3 + 1.6 * ease((lt - 0.3) / 0.8), bloom=0.6)
    items = []
    ta = ease((lt - 0.35) / 0.4)
    if cfg.get("title"):
        items.append((cfg["title"], F_DISPLAY, H * 0.05, (cx, cy + H * 0.15 + (1 - ta) * 16),
                      (255, 255, 255, int(255 * ta)), "mm"))
    lay, sh = text_layer(K, items)
    comp_layer(canvas, lay, sh)
    # Call to action pill.
    if cfg.get("cta"):
        tb = ease((lt - 0.6) / 0.4)
        f = font(F_MEDIUM, H * 0.032)
        tw = f.getlength(cfg["cta"])
        pw, ph = tw + H * 0.09, H * 0.075
        x0, y0 = cx - pw / 2, cy + H * 0.25 + (1 - tb) * 14
        pill = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        d = ImageDraw.Draw(pill)
        d.rounded_rectangle((x0, y0, x0 + pw, y0 + ph), ph / 2, fill=(255, 255, 255, int(24 * tb)),
                            outline=(150, 150, 255, int(220 * tb)), width=max(2, int(H * 0.003)))
        d.text((cx, y0 + ph / 2), cfg["cta"], font=f, fill=(255, 255, 255, int(255 * tb)), anchor="mm")
        comp_layer(canvas, pill)
    if cfg.get("sub"):
        tc = ease((lt - 0.8) / 0.4)
        lay, _ = text_layer(K, [(cfg["sub"], F_REGULAR, H * 0.022, (cx, H * 0.93), (165, 172, 195, int(255 * tc)), "mm")])
        comp_layer(canvas, lay)
    return np.clip(canvas, 0, 255).astype(np.uint8)


# ---------------------------------------------------------------- watermark
_badges = {}


def _badge(W, H):
    """The colour logo on a frosted white pill with a soft shadow, as one RGBA patch.
    It reads on the white product UI and on a dark terminal alike."""
    if (W, H) in _badges:
        return _badges[(W, H)]
    p = os.path.join(ASSETS, "logo-color-hd.png")
    lg = Image.open(p).convert("RGBA")
    lw = int(W * 0.082)
    lg = lg.resize((lw, round(lg.size[1] * lw / lg.size[0])), Image.LANCZOS)
    px, py = int(lw * 0.11), int(lg.size[1] * 0.42)
    pw, ph = lw + 2 * px, lg.size[1] + 2 * py
    sh = int(ph * 0.35)                       # room for the shadow
    patch = Image.new("RGBA", (pw + 2 * sh, ph + 2 * sh), (0, 0, 0, 0))
    shadow = Image.new("L", patch.size, 0)
    ImageDraw.Draw(shadow).rounded_rectangle((sh, sh + 2, sh + pw, sh + ph + 2), ph / 2, fill=90)
    shadow = Image.fromarray(cv2.GaussianBlur(np.array(shadow), (0, 0), sh / 2.5))
    patch.paste(Image.new("RGBA", patch.size, (8, 12, 30, 255)), (0, 0), shadow)
    pill = Image.new("RGBA", patch.size, (0, 0, 0, 0))
    ImageDraw.Draw(pill).rounded_rectangle((sh, sh, sh + pw, sh + ph), ph / 2, fill=(255, 255, 255, 236),
                                           outline=(210, 214, 235, 255), width=1)
    patch.alpha_composite(pill)
    patch.alpha_composite(lg, (sh + px, sh + py))
    _badges[(W, H)] = (np.array(patch, np.float32), sh, pw, ph)
    return _badges[(W, H)]


def watermark_box(W, H, corner="br"):
    """(x, y, w, h) of the visible pill, so the speed badge can sit beside it."""
    _, sh, pw, ph = _badge(W, H)
    m = int(W * 0.012)
    x0 = W - pw - m if corner and corner[1] == "r" else m
    y0 = H - ph - m if corner and corner[0] == "b" else m
    return x0, y0, pw, ph


def watermark(frame, corner="br", opacity=0.94):
    """The AccuKnox logo, small, in one corner of every product frame."""
    if not corner:
        return frame
    H, W = frame.shape[:2]
    patch, sh, pw, ph = _badge(W, H)
    x0, y0, _, _ = watermark_box(W, H, corner)
    x0, y0 = x0 - sh, y0 - sh
    h, w = patch.shape[:2]
    xs0, ys0, xs1, ys1 = max(0, x0), max(0, y0), min(W, x0 + w), min(H, y0 + h)
    p = patch[ys0 - y0:ys1 - y0, xs0 - x0:xs1 - x0]
    out = frame.astype(np.float32)
    al = p[..., 3:4] / 255.0 * opacity
    out[ys0:ys1, xs0:xs1] = out[ys0:ys1, xs0:xs1] * (1 - al) + p[..., 2::-1] * al
    return np.clip(out, 0, 255).astype(np.uint8)


# ---------------------------------------------------------------- sound design
SR = 48000


def _lp_sweep(x, f0, f1):
    """One-pole low-pass whose cutoff moves from f0 to f1 (Hz) across the signal."""
    n = len(x)
    fc = np.geomspace(max(f0, 20), max(f1, 20), n)
    a = 1 - np.exp(-2 * np.pi * fc / SR)
    y = np.empty(n, np.float32)
    acc = 0.0
    for i in range(n):
        acc += a[i] * (x[i] - acc)
        y[i] = acc
    return y


def whoosh(dur=0.45, rng=None):
    rng = rng or np.random.default_rng(7)
    n = int(dur * SR)
    t = np.linspace(0, 1, n, dtype=np.float32)
    noise = rng.standard_normal(n).astype(np.float32)
    rise = _lp_sweep(noise, 400, 7000)
    fall = _lp_sweep(noise[::-1], 500, 5000)[::-1]
    y = np.where(t < 0.6, rise, fall)
    env = np.abs(np.sin(np.pi * np.clip(t, 0, 1))) ** 2.2
    return y * env * 0.9


def impact(dur=1.4):
    n = int(dur * SR)
    t = np.arange(n, dtype=np.float32) / SR
    f = 38 + 42 * np.exp(-t * 9)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 3.2)
    rng = np.random.default_rng(3)
    click = _lp_sweep(rng.standard_normal(n).astype(np.float32), 3000, 300) * np.exp(-t * 40)
    return (sub * 0.95 + click * 0.6).astype(np.float32)


def shimmer(dur=1.2):
    n = int(dur * SR)
    t = np.arange(n, dtype=np.float32) / SR
    y = sum(np.sin(2 * np.pi * f * t) * a for f, a in ((1318.5, 0.5), (1975.5, 0.35), (2637, 0.25)))
    return (y * np.exp(-t * 3.5) * np.clip(t / 0.01, 0, 1) * 0.18).astype(np.float32)


def riser(dur=0.7):
    n = int(dur * SR)
    t = np.linspace(0, 1, n, dtype=np.float32)
    rng = np.random.default_rng(11)
    y = _lp_sweep(rng.standard_normal(n).astype(np.float32), 300, 9000)
    tone = np.sin(2 * np.pi * np.cumsum(220 + 660 * t ** 2) / SR) * 0.25
    return ((y * 0.8 + tone) * t ** 2.2).astype(np.float32)


def pad(dur):
    """A low, wide drone: A minor colour with slow beating. Sits under the hook and the end card."""
    n = int(dur * SR)
    t = np.arange(n, dtype=np.float32) / SR
    y = np.zeros(n, np.float32)
    for f, a in ((55.0, 0.55), (82.41, 0.35), (110.0, 0.30), (130.81, 0.18), (164.81, 0.12)):
        for det in (-0.25, 0.25):
            y += np.sin(2 * np.pi * (f + det) * t + det * 3) * a
    lfo = 0.75 + 0.25 * np.sin(2 * np.pi * 0.35 * t)
    fade = np.clip(t / 0.25, 0, 1) * np.clip((dur - t) / 1.0, 0, 1)
    return (y / 3.2 * lfo * fade).astype(np.float32)


SOUNDS = {"whoosh": whoosh, "impact": impact, "shimmer": shimmer, "riser": riser}


def sfx_track(events, total, path, gain_db=-14.0):
    """events: [(t, kind, arg)]. kind is whoosh, impact, shimmer, riser, or pad (arg = duration)."""
    n = int(total * SR) + SR
    mix = np.zeros(n, np.float32)
    for t, kind, arg in events:
        s = pad(arg) if kind == "pad" else SOUNDS[kind]()
        if kind == "riser":
            t = t - len(s) / SR       # a riser ends on its time
        i = max(0, int(t * SR))
        j = min(n, i + len(s))
        mix[i:j] += s[: j - i]
    mix = np.nan_to_num(mix)
    peak = np.abs(mix).max() or 1.0
    mix = mix / peak * (10 ** (gain_db / 20))
    pcm = (np.clip(mix[: int(total * SR)], -1, 1) * 32767).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    return path


def hook_sfx(t0, cfg, dur):
    """Sound events for a hook that starts at t0 seconds."""
    wins, t_logo = hook_layout(cfg, dur)
    ev = [(t0, "pad", dur + 0.8), (t0, "impact", None)]
    for a, _ in wins[1:]:
        ev.append((t0 + a - 0.2, "whoosh", None))
    ev += [(t0 + t_logo, "riser", None), (t0 + t_logo, "impact", None), (t0 + t_logo + 0.2, "shimmer", None),
           (t0 + dur - 0.25, "whoosh", None)]
    return ev


def outro_sfx(t0, dur):
    return [(t0, "pad", dur), (t0 - 0.15, "whoosh", None), (t0 + 0.1, "impact", None), (t0 + 0.35, "shimmer", None)]
