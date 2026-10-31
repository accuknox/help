"""Business blog cover, 1200x628 at 2x. The bars are the real GuardRate group scores, snapshot 2026-10-16.
Run: python cover.py
"""
import json
from pathlib import Path

from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
LOGO = Path(r"D:\AccuKnox\help\.claude\skills\accuknox-video-edit\assets\logo-color-hd.png").as_uri()
tools = json.load(open(HERE / "data" / "tools.json"))
by = {}
for r in tools["rows"]:
    by.setdefault(r["model"], {})[r["group"]] = r["score"]
AK, RU = "Accuknoxtechnologies/accuknox-guard-1.1", "Alibaba-AAIG/YuFeng-XGuard-Reason-8B"
groups = tools["groups"]


def bars(model, cls):
    vals = [by[model][g] for g in groups]
    low = min(vals)
    out = []
    for g, v in zip(groups, vals):
        k = "low" if v == low else ""
        out.append(f'<div class="bar {cls} {k}" style="height:{v*100:.1f}%" title="{g} {v:.3f}"></div>')
    return "".join(out), low


ak_bars, ak_low = bars(AK, "ak")
ru_bars, ru_low = bars(RU, "ru")

HTML = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root {{ --navy: oklch(0.28 0.13 268); --blue: oklch(0.50 0.27 264); --ink: oklch(0.24 0.06 268);
  --muted: oklch(0.52 0.02 268); --paper: oklch(0.985 0.004 268); --track: oklch(0.94 0.008 268);
  --grey: oklch(0.80 0.015 268); --red: oklch(0.53 0.21 25); }}
* {{ box-sizing: border-box; margin: 0; }}
body {{ width: 1200px; height: 628px; background: var(--paper); font-family: Inter, sans-serif; color: var(--ink);
  display: grid; grid-template-columns: 470px 1fr; padding: 56px 60px 44px; gap: 52px; overflow: hidden; }}
.left {{ display: flex; flex-direction: column; }}
.kicker {{ font: 600 14px/1.4 Inter; letter-spacing: .08em; text-transform: uppercase; color: var(--blue); }}
h1 {{ font: 700 54px/1.04 'Inter'; letter-spacing: -0.03em; margin-top: 22px; color: var(--navy); }}
h1 span {{ color: var(--blue); }}
.sub {{ font: 400 19px/1.45 Inter; color: var(--muted); margin-top: 20px; max-width: 30ch; }}
.logo {{ margin-top: auto; height: 34px; width: auto; align-self: flex-start; }}
.right {{ display: flex; flex-direction: column; justify-content: center; gap: 26px; }}
.row .name {{ display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px; }}
.row .name b {{ font: 600 17px 'Inter'; }}
.row .name em {{ font: 500 14px Inter; font-style: normal; color: var(--muted); }}
.chart {{ position: relative; height: 150px; display: grid; grid-template-columns: repeat(19, 1fr); gap: 5px;
  align-items: end; background: linear-gradient(to top, var(--track) 0 100%); border-radius: 6px; padding: 0 6px; }}
.bar {{ border-radius: 3px 3px 0 0; }}
.bar.ak {{ background: var(--blue); }}
.bar.ru {{ background: var(--grey); }}
.bar.low.ru {{ background: var(--red); }}
.bar.low.ak {{ background: var(--navy); }}
.floor {{ position: absolute; left: 0; right: 0; border-top: 2px dashed currentColor; }}
.floor span {{ position: absolute; left: -2px; top: -30px; box-shadow: 0 1px 2px oklch(0.5 0.02 268 / .25); font: 700 14px 'Inter'; background: var(--paper);
  padding: 2px 8px; border-radius: 4px; }}
.src {{ font: 400 12px Inter; color: var(--muted); }}
</style></head><body>
<div class="left">
  <div class="kicker">GuardRate leaderboard by HiveTrace</div>
  <h1>#1 of 41 guardrail models. <span>No weak spot.</span></h1>
  <p class="sub">It ranks first across 19 benchmark groups because its lowest group score is the highest on the board.</p>
  <img class="logo" src="{LOGO}">
</div>
<div class="right">
  <div class="row"><div class="name"><b>AccuKnox Guard 1.1</b><em>#1 · weakest group {ak_low:.3f}</em></div>
    <div class="chart">{ak_bars}<div class="floor" style="bottom:{ak_low*150:.0f}px;color:var(--navy)"><span>floor {ak_low:.3f}</span></div></div></div>
  <div class="row"><div class="name"><b>Runner-up, YuFeng-XGuard-Reason-8B</b><em>#2 · weakest group {ru_low:.3f}</em></div>
    <div class="chart">{ru_bars}<div class="floor" style="bottom:{ru_low*150:.0f}px;color:var(--red)"><span>floor {ru_low:.3f}</span></div></div></div>
  <div class="src">Each bar is one of 19 benchmark groups. Snapshot October 16, 2026.</div>
</div>
</body></html>"""

(HERE / "cover.html").write_text(HTML, encoding="utf8")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 628}, device_scale_factor=2)
    pg.goto((HERE / "cover.html").as_uri(), wait_until="networkidle")
    pg.wait_for_timeout(800)
    pg.screenshot(path=str(HERE / "assets" / "cover-business-blog.png"))
    b.close()
print("wrote cover-business-blog.png")
