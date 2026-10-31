"""Screenshots of the live HiveTrace GuardRate Leaderboard, 2x, for proof images."""
from playwright.sync_api import sync_playwright
from pathlib import Path
OUT = Path(__file__).parent / "assets"
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1400, "height": 1000}, device_scale_factor=2)
    pg.goto("https://hivetrace-guardrateleaderboard.hf.space/", wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(2500)
    pg.screenshot(path=str(OUT / "shot-leaderboard-ranking.png"), clip={"x": 0, "y": 0, "width": 1400, "height": 1000})
    pg.goto("https://hivetrace-guardrateleaderboard.hf.space/tools", wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(3500)
    pg.screenshot(path=str(OUT / "_tools-full.png"), full_page=True)
    b.close()
print("done")
