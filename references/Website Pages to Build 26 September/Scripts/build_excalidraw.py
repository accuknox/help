"""Build nav-and-pages.excalidraw and a matching SVG preview from one data model."""
import json, random, pathlib, html

HERE = pathlib.Path(__file__).parent
COL = {"new": ("#b2f2bb", "#2f9e44"), "update": ("#ffec99", "#e67700"), "fix": ("#d0bfff", "#6741d9"),
       "move": ("#a5d8ff", "#1971c2"), "keep": ("#f1f3f5", "#868e96"), "head": ("#343a40", "#343a40")}

els, svg = [], []
seed = lambda: random.randint(1, 2**31 - 1)


def box(id_, x, y, w, h, text, kind="keep", size=16, bold=False):
    bg, stroke = COL[kind]
    tcol = "#ffffff" if kind == "head" else "#1e1e1e"
    els.append({"id": id_, "type": "rectangle", "x": x, "y": y, "width": w, "height": h, "angle": 0,
                "strokeColor": stroke, "backgroundColor": bg, "fillStyle": "solid", "strokeWidth": 2,
                "strokeStyle": "solid", "roughness": 0, "opacity": 100, "groupIds": [], "frameId": None,
                "roundness": {"type": 3}, "seed": seed(), "version": 1, "versionNonce": seed(),
                "isDeleted": False, "boundElements": [{"type": "text", "id": id_ + "_t"}], "updated": 1,
                "link": None, "locked": False})
    lines = text.split("\n")
    th = len(lines) * size * 1.25
    els.append({"id": id_ + "_t", "type": "text", "x": x + 8, "y": y + (h - th) / 2, "width": w - 16,
                "height": th, "angle": 0, "strokeColor": tcol, "backgroundColor": "transparent",
                "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
                "groupIds": [], "frameId": None, "roundness": None, "seed": seed(), "version": 1,
                "versionNonce": seed(), "isDeleted": False, "boundElements": None, "updated": 1, "link": None,
                "locked": False, "text": text, "fontSize": size, "fontFamily": 2, "textAlign": "center",
                "verticalAlign": "middle", "containerId": id_, "originalText": text, "lineHeight": 1.25,
                "autoResize": True})
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{bg}" stroke="{stroke}" stroke-width="2"/>')
    for i, ln in enumerate(lines):
        ty = y + (h - th) / 2 + size * (i + 1)
        svg.append(f'<text x="{x + w / 2}" y="{ty}" font-size="{size}" font-family="Segoe UI, Arial" '
                   f'text-anchor="middle" fill="{tcol}" font-weight="{"700" if bold or kind == "head" else "400"}">'
                   f'{html.escape(ln)}</text>')
    return (x, y, w, h)


def label(x, y, text, size=22):
    els.append({"id": f"lbl{len(els)}", "type": "text", "x": x, "y": y, "width": len(text) * size * 0.55,
                "height": size * 1.25, "angle": 0, "strokeColor": "#1e1e1e", "backgroundColor": "transparent",
                "fillStyle": "solid", "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
                "groupIds": [], "frameId": None, "roundness": None, "seed": seed(), "version": 1,
                "versionNonce": seed(), "isDeleted": False, "boundElements": None, "updated": 1, "link": None,
                "locked": False, "text": text, "fontSize": size, "fontFamily": 2, "textAlign": "left",
                "verticalAlign": "top", "containerId": None, "originalText": text, "lineHeight": 1.25,
                "autoResize": True})
    svg.append(f'<text x="{x}" y="{y + size}" font-size="{size}" font-family="Segoe UI, Arial" font-weight="700" '
               f'fill="#1e1e1e">{html.escape(text)}</text>')


B = {}


def arrow(a, b, color="#495057", dashed=False, via=None):
    ax, ay, aw, ah = B[a]; bx, by, bw, bh = B[b]
    sx, sy = ax + aw, ay + ah / 2
    ex, ey = bx, by + bh / 2
    if bx + bw <= ax:  # target on the left
        sx, ex = ax, bx + bw
    if bx < ax + aw and ax < bx + bw:  # stacked, go bottom to top
        sx, sy, ex, ey = ax + aw / 2, ay + ah, bx + bw / 2, by
    pts = [(sx, sy)] + (via or []) + [(ex, ey)]
    aid = f"ar_{a}_{b}"
    els.append({"id": aid, "type": "arrow", "x": sx, "y": sy, "width": abs(ex - sx), "height": abs(ey - sy),
                "angle": 0, "strokeColor": color, "backgroundColor": "transparent", "fillStyle": "solid",
                "strokeWidth": 2, "strokeStyle": "dashed" if dashed else "solid", "roughness": 0, "opacity": 100,
                "groupIds": [], "frameId": None, "roundness": {"type": 2}, "seed": seed(), "version": 1,
                "versionNonce": seed(), "isDeleted": False, "boundElements": None, "updated": 1, "link": None,
                "locked": False, "points": [[px - sx, py - sy] for px, py in pts], "lastCommittedPoint": None,
                "startBinding": {"elementId": a, "focus": 0, "gap": 4},
                "endBinding": {"elementId": b, "focus": 0, "gap": 4}, "startArrowhead": None,
                "endArrowhead": "arrow"})
    for e in els:
        if e["id"] in (a, b) and e["type"] == "rectangle":
            e["boundElements"].append({"type": "arrow", "id": aid})
    dash = 'stroke-dasharray="8 6"' if dashed else ''
    d = " ".join(f"{px},{py}" for px, py in pts)
    svg.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="2" {dash} marker-end="url(#ah)"/>')


# ---- title and legend
label(40, 20, "accuknox.com, AI Security, AppSec and DSPM update map (2026-09-26)", 28)
lx = 40
for k, t in [("new", "NEW page or item"), ("update", "UPDATE copy"), ("fix", "FIX dead link"),
             ("move", "MOVE in nav"), ("keep", "No change")]:
    box(f"leg_{k}", lx, 70, 190, 40, t, k, 15); lx += 205

# ---- column 1, nav
label(40, 140, "1. Nav mega menu", 22)
y = 180
nav = [
    ("n_plat", "Platform", "head"),
    ("n_ai", "Secure AI (NEW)", "head"),
    ("n_aispm", "AI SPM - Security Posture Mgmt", "keep"),
    ("n_shadow", "+ Shadow AI Discovery   N1", "new"),
    ("n_gw", "+ AccuKnox AI Gateway (coming soon)   N1", "new"),
    ("n_id", "AI Identity Security -> /#   N2", "fix"),
    ("n_rest", "Guardrails, Red Teaming, AI DR, Agentic,\nModel, GRC, Copilot, MCP, AI Factories", "keep"),
    ("n_code", "Secure Code", "head"),
    ("n_sast", "AI SAST (was AI-Accelerated SAST -> /#)   N3", "fix"),
    ("n_dast", "+ AI DAST (coming soon)   N3", "new"),
    ("n_data", "Secure Data (DSPM), no beta tag\nmoved out of Coming Soon   N4", "move"),
    ("n_sol", "Solutions", "head"),
    ("n_uc_shadow", "Use Cases: Shadow AI Discovery\nrepoint to new page   N5", "update"),
    ("n_uc_dspm", "+ Use Cases / Industries:\nDSPM for Indian Banks   N5", "new"),
]
for id_, t, k in nav:
    h = 62 if "\n" in t else 40
    indent = 0 if k == "head" and id_ in ("n_plat", "n_sol") else 24
    B[id_] = box(id_, 40 + indent, y, 400 - indent, h, t, k, 15)
    y += h + 10
    if id_ == "n_data":
        y += 20

# ---- column 2, existing pages
label(560, 140, "2. Existing pages to update", 22)
pages = [
    ("p_ais", "/platform/ai-security\nA1 hero, A2 module grid, A3 guardrails bullet\nA4 NEW: Shadow AI, AI Gateway, AI AppSec\nA5 differentiators, A6 FAQs 26-27", "update", 130),
    ("p_plat", "/platform\nP1 +2 AI cards, fix 2 captions\nP1b AppSec card, P1c data card, P2 grid", "update", 100),
    ("p_dspm", "/platform/dspm\nD1 hero, D2-D3 replace unsourced stats\nD4 numbers, D5 NEW DSPM for AI\nD6-D9 doc facts, D8b NEW India band", "update", 130),
    ("p_sast", "/solutions/sast\nS1 NEW AI SAST section, S2 FAQ", "update", 70),
    ("p_dast", "/solutions/dast\nT1 NEW AI DAST section, T2 copy", "update", 70),
    ("p_aspm", "/platform/aspm\nM1 tab labels, M2 NEW AI SAST + DAST band", "update", 70),
]
y = 180
for id_, t, k, h in pages:
    B[id_] = box(id_, 560, y, 420, h, t, k, 15)
    y += h + 26

# ---- column 3, new pages
label(1100, 140, "3. New solution pages", 22)
B["w_shadow"] = box("w_shadow", 1100, 180, 420, 250,
                    "NEW /solutions/shadow-ai-discovery\n\nHero, stats row (4K+)\nFive surface cards, beta legend\nUse cases by buyer\nCoverage matrix\nDiscover -> govern -> firewall\nIntegrations, honest limits, FAQs",
                    "new", 15)
B["w_dspm"] = box("w_dspm", 1100, 480, 420, 270,
                  "NEW /solutions/dspm-indian-banks\n\nHero on RBI Advisory 3/2026 + DPDP deadline\nMandate strip, advisory vs regulation\nValue tiles, solutions by job\nRegulation to control matrix\nIndian data classes, air-gapped first\nAI data risk, case study, FAQs",
                  "new", 15)
B["help"] = box("help", 1100, 800, 420, 90,
                "help.accuknox.com\nDSPM overview + onboarding (merged today)\nShadow AI Discovery use case", "keep", 15)

# ---- arrows, nav to pages
for a, b in [("n_aispm", "p_ais"), ("n_gw", "p_ais"), ("n_shadow", "w_shadow"), ("n_sast", "p_sast"),
             ("n_dast", "p_dast"), ("n_data", "p_dspm")]:
    arrow(a, b)
ys = B["n_uc_shadow"][1] + B["n_uc_shadow"][3] / 2
yd = B["n_uc_dspm"][1] + B["n_uc_dspm"][3] / 2
arrow("n_uc_shadow", "w_shadow", via=[(500, ys), (500, 990), (1060, 990), (1060, 305)])
arrow("n_uc_dspm", "w_dspm", via=[(520, yd), (520, 1005), (1075, 1005), (1075, 615)])
# cross-links between pages
for a, b in [("p_ais", "w_shadow"), ("p_dspm", "w_dspm"), ("p_dspm", "help")]:
    arrow(a, b, "#2f9e44", dashed=True)

W, H = 1560, 1030
doc = {"type": "excalidraw", "version": 2, "source": "https://excalidraw.com", "elements": els,
       "appState": {"gridSize": None, "viewBackgroundColor": "#ffffff"}, "files": {}}
(HERE / "nav-and-pages.excalidraw").write_text(json.dumps(doc, indent=1), encoding="utf-8")
(HERE / "nav-and-pages.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
    '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#495057"/></marker></defs>'
    f'<rect width="{W}" height="{H}" fill="#ffffff"/>' + "".join(svg) + "</svg>", encoding="utf-8")
print(len(els), "elements")
