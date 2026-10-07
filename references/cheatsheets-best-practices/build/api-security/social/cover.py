from pathlib import Path
from playwright.sync_api import sync_playwright
b = Path(__file__).resolve().parent.parent
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=2)
    pg.goto((b / "report.html").as_uri()); pg.wait_for_timeout(800)
    pg.locator("section.page").first.screenshot(path=str(b / "social" / "cover.png"))
    br.close()
