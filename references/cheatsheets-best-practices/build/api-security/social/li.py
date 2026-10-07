from pathlib import Path
from playwright.sync_api import sync_playwright
d = Path(__file__).resolve().parent
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": 1200, "height": 1200})
    pg.goto((d / "linkedin.html").as_uri()); pg.wait_for_timeout(800)
    pg.screenshot(path=str(d.parents[2] / "output" / "api-security-best-practices-guide-linkedin.png"))
    br.close()
