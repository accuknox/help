from pathlib import Path
from playwright.sync_api import sync_playwright
d = Path(__file__).resolve().parent
b = d.parent
out = d.parents[2] / "output"
slug = "cloud-compliance-best-practices-guide"
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=2)
    pg.goto((b / "report.html").as_uri()); pg.wait_for_timeout(800)
    pg.locator("section.page").first.screenshot(path=str(d / "cover.png"))
    pg2 = br.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=1200 / 794)
    pg2.goto((b / "report.html").as_uri()); pg2.wait_for_timeout(800)
    pg2.locator("section.page").first.screenshot(path=str(out / f"{slug}-form-image.png"))
    pg3 = br.new_page(viewport={"width": 1200, "height": 1200})
    pg3.goto((d / "linkedin.html").as_uri()); pg3.wait_for_timeout(800)
    pg3.screenshot(path=str(out / f"{slug}-linkedin.png"))
    br.close()
