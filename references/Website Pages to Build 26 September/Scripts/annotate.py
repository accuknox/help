"""Draw numbered change boxes on live accuknox.com pages and save one crop per change.

Each annotation finds the smallest element whose text starts with `text`, climbs `up` ancestors,
outlines it and tags it with a code and an action. Output goes to shots/<code>.png.
"""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

OUT = pathlib.Path(__file__).parent / "shots"
OUT.mkdir(exist_ok=True)
B = "https://accuknox.com"

COLORS = {"UPDATE": "#d97706", "REPLACE": "#dc2626", "NEW ABOVE": "#16a34a", "NEW BELOW": "#16a34a",
          "FIX": "#7c3aed", "ADD": "#16a34a", "MOVE": "#2563eb"}

PAGES = {
    "/platform/ai-security": [
        ("A1", "UPDATE", "Discover every model, agent, and pipeline", 0),
        ("A2", "UPDATE", "AI Security Posture Management (AI SPM)", 1),
        ("A3", "UPDATE", "AI Guardrails, Stateful Prompt Firewall", 1),
        ("A4", "NEW ABOVE", "AI Security Platform Tour", 0),
        ("A5", "UPDATE", "AI Security Key Differentiators", 1),
        ("A6", "REPLACE", "How does AccuKnox discover unsanctioned AI tools", 1),
    ],
    "/platform": [
        ("P1", "ADD", "AI Security Posture (AI-SPM)", 2),
        ("P2", "UPDATE", "12 CNAPP, AppSec, CloudSec, AI-Sec Modules In A Unified Platform", 1),
    ],
    "/platform/dspm": [
        ("D1", "UPDATE", "AI-powered DSPM to discover, classify", 0),
        ("D2", "REPLACE", "Recent Data Security Incidents", 1),
        ("D3", "REPLACE", "The Data Security Challenge", 1),
        ("D4", "UPDATE", "Why Choose AccuKnox for", 1),
        ("D5", "NEW BELOW", "DSPM Capabilities & Use Cases", 1),
        ("D6", "UPDATE", "Automated Sensitive", 1),
        ("D7", "REPLACE", "Multi-Cloud Data Security Asset Coverage", 1),
        ("D8", "REPLACE", "AccuKnox DSPM Differentiators", 1),
        ("D9", "REPLACE", "Flexible DSPM Deployment Models", 1),
    ],
    "/solutions/sast": [
        ("S1", "NEW BELOW", "Want to Shift Left and Secure Right?", 1),
        ("S2", "UPDATE", "How can organizations address the potential for false positives", 1),
    ],
    "/solutions/dast": [
        ("T1", "NEW BELOW", "Want to See How Your Application Behaves Under Attack?", 1),
        ("T2", "UPDATE", "Aggregate Your DAST tools in One Dashboard", 1),
    ],
    "/platform/aspm": [
        ("M1", "UPDATE", "Prioritize & Automate Security in", 1),
        ("M2", "NEW BELOW", "Is Application Security an Afterthought in the AI Era?", 1),
    ],
}

JS_FIND = """([text, up]) => {
  const all = [...document.querySelectorAll('h1,h2,h3,h4,h5,p,a,span,li,div,button,summary')];
  const norm = s => (s || '').replace(/\\s+/g, ' ').trim();
  const t = norm(text).toLowerCase();
  let best = null;
  for (const el of all) {
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) continue;
    const s = norm(el.innerText).toLowerCase();
    if (!s.startsWith(t)) continue;
    if (!best || el.innerText.length < best.innerText.length) best = el;
  }
  if (!best) return null;
  let el = best;
  for (let i = 0; i < up && el.parentElement; i++) el = el.parentElement;
  for (let i = 0; i < 6 && el.parentElement; i++) {
    const h = el.getBoundingClientRect().height, ph = el.parentElement.getBoundingClientRect().height;
    if (h >= 220 || ph > 1500) break;
    el = el.parentElement;
  }
  const r = el.getBoundingClientRect();
  return {x: r.left + scrollX, y: r.top + scrollY, w: r.width, h: r.height};
}"""

JS_DRAW = """([box, code, action, color]) => {
  const d = document.createElement('div');
  d.className = 'ak-annot';
  Object.assign(d.style, {position:'absolute', left:(box.x-6)+'px', top:(box.y-6)+'px', width:(box.w+12)+'px',
    height:(box.h+12)+'px', border:'4px solid '+color, borderRadius:'6px', zIndex:2147483646, pointerEvents:'none',
    boxSizing:'border-box'});
  const tag = document.createElement('div');
  tag.textContent = code + '  ' + action;
  Object.assign(tag.style, {position:'absolute', left:'-4px', top:'-34px', background:color, color:'#fff',
    font:'700 18px/1 system-ui, sans-serif', padding:'7px 12px', borderRadius:'4px', whiteSpace:'nowrap'});
  d.appendChild(tag);
  document.body.appendChild(d);
}"""


def prep(page, url):
    page.goto(url, wait_until="domcontentloaded", timeout=90000)
    page.wait_for_timeout(3000)
    if "unable to access" in page.evaluate("document.body.innerText.slice(0,300)"):
        print("BLOCKED", url)
    for label in ["Reject All", "Reject all"]:
        try:
            page.get_by_role("button", name=label).first.click(timeout=2000)
            break
        except Exception:
            pass
    h = page.evaluate("document.body.scrollHeight")
    for y in range(0, h, 700):
        page.evaluate(f"window.scrollTo(0,{y})")
        page.wait_for_timeout(120)
    page.evaluate("window.scrollTo(0,0)")
    page.wait_for_timeout(800)
    # sticky header would cover crops
    page.add_style_tag(content="header, .header, #header, [class*='sticky'], [class*='navbar'] {position: static !important;}"
                               " .cky-consent-container, .cky-overlay, .cky-btn-revisit-wrapper, .cky-modal {display:none !important;}")


def main(only=None):
    log = {}
    with sync_playwright() as p:
        try:
            br = p.chromium.launch(channel="chrome", args=["--disable-blink-features=AutomationControlled"])
        except Exception:
            br = p.chromium.launch(args=["--disable-blink-features=AutomationControlled"])
        ctx = br.new_context(viewport={"width": 1440, "height": 900}, locale="en-US", user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
        ctx.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        pg = ctx.new_page()
        for path, anns in PAGES.items():
            if only and path not in only:
                continue
            prep(pg, B + path)
            pg.wait_for_timeout(4000)
            for code, action, text, up in anns:
                box = pg.evaluate(JS_FIND, [text, up])
                if not box:
                    log[code] = "NOT FOUND"
                    continue
                if box["h"] > 1600:  # climbed too far, fall back to the element itself
                    box = pg.evaluate(JS_FIND, [text, 0])
                pg.evaluate(JS_DRAW, [box, code, action, COLORS[action]])
                top = max(0, box["y"] - 110)
                height = min(box["h"] + 190, 1300)
                if action == "NEW ABOVE":
                    top = max(0, box["y"] - 420); height = 620
                if action == "NEW BELOW":
                    height = min(box["h"] + 420, 1300)
                pg.set_viewport_size({"width": 1440, "height": 900})
                pg.screenshot(path=str(OUT / f"{code}.png"), full_page=True,
                              clip={"x": 0, "y": top, "width": 1440, "height": height})
                log[code] = {"box": box}
        # the mega menu, opened by hover on Platform
        if not only or "nav" in only:
            prep(pg, B + "/")
            pg.add_style_tag(content="header, .header, #header {position: absolute !important;}")
            try:
                pg.get_by_text("Platform", exact=True).first.hover(timeout=5000)
                pg.wait_for_timeout(1500)
                navs = [("N1", "ADD", "Secure AI", 2), ("N2", "FIX", "AI Identity Security", 0),
                        ("N3", "FIX", "AI-Accelerated SAST Scanning", 0), ("N4", "MOVE", "Data Security (DSPM)", 0)]
                for code, action, text, up in navs:
                    box = pg.evaluate(JS_FIND, [text, up])
                    if box:
                        pg.evaluate(JS_DRAW, [box, code, action, COLORS[action]])
                    log[code] = box or "NOT FOUND"
                pg.screenshot(path=str(OUT / "N-platform-menu.png"), clip={"x": 0, "y": 0, "width": 1440, "height": 900})
            except Exception as e:
                log["nav"] = str(e)
        br.close()
    print(json.dumps(log, indent=1)[:4000])


if __name__ == "__main__":
    main(sys.argv[1:] or None)
