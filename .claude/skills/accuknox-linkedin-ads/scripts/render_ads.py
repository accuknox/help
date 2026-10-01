"""Render low-fidelity ad mockups from a JSON spec with Playwright Chromium.

Usage:
    python render_ads.py <campaigns.json | ads.json> <out_dir> [--only ID]

The spec is either a list of ads or a campaigns file with
{"campaigns": [{"ads": [...]}]}. Each ad:
    {
      "id": "ai-sec-a",
      "layout": "photo" | "ui" | "type",
      "size": [1200, 1200],            # optional, LinkedIn square is the default
      "image": "relative/or/absolute.jpg",  # photo or product screenshot
      "focus": "50% 40%",               # optional object-position for the photo
      "kicker": "AI SECURITY",
      "headline": "The wolf won't knock.",
      "body": "One line of product truth.",
      "tagline": "Trust nothing. Verify everything.",
      "cta": "Request a demo",
      "proof": "Ranked #1 by GigaOm",   # optional small badge
      "dim": 0.7,                       # optional photo brightness
      "zoom": 1.6                       # optional zoom into a UI screenshot
    }

Paths in "image" resolve against the folder that holds ads.json.
A designer swaps these mockups out, so the renderer favours clear hierarchy
over polish: one photo, one headline, one line of truth, one CTA.
"""
import argparse
import base64
import html
import json
import mimetypes
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
LOGO_WHITE = SKILL / "assets" / "logo-white.png"

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{width:{W}px;height:{H}px;overflow:hidden;font-family:Inter,sans-serif;background:#05082a;color:#fff}
.ad{position:relative;width:{W}px;height:{H}px;overflow:hidden}
.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{FOCUS};}
.dim{position:absolute;inset:0;background:#000;opacity:{DIMO}}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(5,8,42,.15) 0%,rgba(5,8,42,.05) 35%,rgba(5,8,42,.85) 62%,#05082a 82%)}
.logo{position:absolute;top:{PAD}px;left:{PAD}px;height:{LOGOH}px}
.kicker{display:inline-block;font:600 {KS}px/1 Inter;letter-spacing:.14em;color:#9fb4ff;margin-bottom:{KG}px}
.copy{position:absolute;left:{PAD}px;right:{PAD}px;bottom:{BOT}px}
h1{font:700 {HS}px/1.04 'Space Grotesk';letter-spacing:-.02em;margin-bottom:{HG}px}
.body{font:400 {BS}px/1.35 Inter;color:#dfe5ff;max-width:92%;margin-bottom:{BG}px}
.row{display:flex;align-items:center;justify-content:space-between;gap:24px}
.tag{font:700 {TS}px/1.2 'Space Grotesk';color:#fff}
.cta{flex:none;background:#0046FF;color:#fff;font:600 {CS}px/1 Inter;padding:{CP}px {CPX}px;border-radius:999px;box-shadow:0 8px 30px rgba(0,70,255,.45)}
.proof{position:absolute;top:{PAD}px;right:{PAD}px;font:600 {PS}px/1 Inter;color:#fff;border:1.5px solid rgba(255,255,255,.55);border-radius:999px;padding:12px 20px;background:rgba(5,8,42,.35)}
.ui-bg{position:absolute;inset:0;background:radial-gradient(120% 80% at 80% 10%,#1d33ff 0%,#0000C8 35%,#05082a 80%)}
.frame{position:absolute;left:{PAD}px;right:{PAD}px;top:{FT}px;height:{FH}px;border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 30px 80px rgba(0,0,0,.55);}
.frame .bar{height:34px;background:#eef1fb;display:flex;gap:8px;align-items:center;padding-left:16px}
.frame .bar i{width:11px;height:11px;border-radius:50%;background:#c9cfe6;display:block}
.frame img{width:100%;height:calc(100% - 34px);object-fit:cover;object-position:{FOCUS};transform:scale({ZOOM});transform-origin:{FOCUS}}
.ui .copy{bottom:{BOT}px}
.type-bg{position:absolute;inset:0;background:linear-gradient(135deg,#05082a 0%,#0000C8 70%,#0046FF 100%)}
.type-bg:after{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.12) 1.5px,transparent 1.5px);background-size:28px 28px}
.type h1{font-size:{HSX}px}
"""


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/png"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def build_html(ad: dict, base: Path) -> str:
    w, h = ad.get("size", [1200, 1200])
    s = w / 1200
    tall = h / w
    vals = {
        "W": w, "H": h, "FOCUS": ad.get("focus", "50% 40%"), "DIMO": round(1 - ad.get("dim", 1.0), 2),
        "PAD": int(64 * s), "LOGOH": int(46 * s), "KS": int(22 * s), "KG": int(18 * s),
        "BOT": int(64 * s), "HS": int((84 if tall > 0.8 else 64) * s), "HSX": int((104 if tall > 0.8 else 76) * s),
        "HG": int(22 * s), "BS": int((32 if tall > 0.8 else 26) * s), "BG": int(34 * s), "TS": int(30 * s),
        "CS": int(28 * s), "CP": int(22 * s), "CPX": int(36 * s), "PS": int(20 * s),
        "FT": int(132 * s), "FH": int((h * 0.44)), "ZOOM": ad.get("zoom", 1.0),
    }
    longest = max(len(x) for x in ad.get("headline", "").split("\n"))
    if longest > 24:
        vals["HS"] = int(vals["HS"] * 24 / longest)
    css = CSS
    for k, v in vals.items():
        css = css.replace("{" + k + "}", str(v))
    esc = lambda k: html.escape(ad.get(k, "")).replace("\n", "<br>")
    layout = ad.get("layout", "photo")
    img_html = ""
    if ad.get("image"):
        p = Path(ad["image"])
        p = p if p.is_absolute() else base / p
        if not p.exists():
            sys.exit(f"missing image for {ad['id']}: {p}")
        src = data_uri(p)
        if layout == "photo":
            img_html = f'<img class="photo" src="{src}"><div class="dim"></div><div class="shade"></div>'
        elif layout == "ui":
            img_html = f'<div class="ui-bg"></div><div class="frame"><div class="bar"><i></i><i></i><i></i></div><img src="{src}"></div>'
    if layout == "type":
        img_html = '<div class="type-bg"></div>'
    if layout == "ui" and not ad.get("image"):
        img_html = '<div class="ui-bg"></div>'
    proof = f'<div class="proof">{esc("proof")}</div>' if ad.get("proof") else ""
    kicker = f'<div class="kicker">{esc("kicker")}</div>' if ad.get("kicker") else ""
    body = f'<p class="body">{esc("body")}</p>' if ad.get("body") else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head>
<body><div class="ad {layout}">{img_html}
<img class="logo" src="{data_uri(LOGO_WHITE)}">{proof}
<div class="copy">{kicker}<h1>{esc("headline")}</h1>{body}
<div class="row"><div class="tag">{esc("tagline")}</div><div class="cta">{esc("cta")} &rarr;</div></div></div>
</div></body></html>"""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("out")
    ap.add_argument("--only")
    a = ap.parse_args()
    spec = Path(a.spec).resolve()
    out = Path(a.out).resolve()
    out.mkdir(parents=True, exist_ok=True)
    data = json.loads(spec.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        ads = [ad for c in data["campaigns"] for ad in c.get("ads", [])]
    else:
        ads = data
    # Ads that ship a finished image ("image_only") need no mockup.
    ads = [ad for ad in ads if "image_only" not in ad]
    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for ad in ads:
            if a.only and ad["id"] != a.only:
                continue
            w, h = ad.get("size", [1200, 1200])
            page = browser.new_page(viewport={"width": w, "height": h})
            page.set_content(build_html(ad, spec.parent), wait_until="networkidle")
            page.wait_for_timeout(300)
            target = out / f"{ad['id']}.png"
            page.screenshot(path=str(target))
            page.close()
            print("wrote", target)
        browser.close()


if __name__ == "__main__":
    main()
