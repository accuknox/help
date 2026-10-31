"""Build the AccuKnox vs Wiz, Palo Alto Networks and SentinelOne CNAPP comparison PDF.

Four landscape A4 pages: cover, comparison, what to buy first plus POC, sources.
Every claim carries a numbered source listed on page 4. Content lives in cnapp_content.py.
Run validate_evidence.py first: it checks each quote against the saved source page.

Run from this folder:
    python build_battlecard.py [out.pdf]

Needs playwright (with chromium) and pypdf.
"""
import base64
import html
import pathlib
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader

import cnapp_content as D

HERE = pathlib.Path(__file__).resolve().parent
A = HERE / "assets"
BUILD = HERE / "build"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "AccuKnox-vs-Wiz-Palo-Alto-SentinelOne-CNAPP-Comparison.pdf"


def b64(name):
    return "data:image/png;base64," + base64.b64encode((A / name).read_bytes()).decode()


ICONS = {
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    "list": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
    "graph": '<circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><path d="M11 7.3 6 16.7M13 7.3l5 9.4M7.5 19h9"/>',
    "db": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/>',
    "brain": '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
    "code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "pipe": '<line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "pulse": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "server": '<rect width="20" height="8" x="2" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>',
    "sliders": '<line x1="21" x2="14" y1="4" y2="4"/><line x1="10" x2="3" y1="4" y2="4"/><line x1="21" x2="12" y1="12" y2="12"/><line x1="8" x2="3" y1="12" y2="12"/><line x1="21" x2="16" y1="20" y2="20"/><line x1="12" x2="3" y1="20" y2="20"/><line x1="14" x2="14" y1="2" y2="6"/><line x1="8" x2="8" y1="10" y2="14"/><line x1="16" x2="16" y1="18" y2="22"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "equal": '<line x1="5" x2="19" y1="9" y2="9"/><line x1="5" x2="19" y1="15" y2="15"/>',
    "up": '<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>',
    "minus": '<line x1="5" x2="19" y1="12" y2="12"/>',
}


def ic(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'


CHIP = {
    "ak": ("c-win", "check", "AccuKnox leads"),
    "par": ("c-par", "equal", "Matches"),
    "star": ("c-win", "check", "AccuKnox strength"),
    "nc": ("c-nl", "minus", "Not compared"),
}


def chip(k):
    cls, icon, label = CHIP[k]
    return f'<span class="chip {cls}">{ic(icon, "ci")}{label}</span>'


NUM = {}
ORDER = []


def num(sid):
    if sid not in NUM:
        ORDER.append(sid)
        NUM[sid] = len(ORDER)
    return NUM[sid]


def cites(ev):
    ids = []
    for e in ev:
        if e[0] not in ids:
            ids.append(e[0])
    ns = sorted(num(s) for s in ids)
    return f'<sup class="c">{",".join(str(n) for n in ns)}</sup>' if ns else ""


def esc(s):
    return html.escape(s, quote=False)


VENDORS = [("wz", "Wiz"), ("pa", "Palo Alto Networks"), ("s1", "SentinelOne")]
HEAD_SUB = {"wz": "Wiz Cloud, Code, Defend", "pa": "Prisma Cloud, Cortex Cloud", "s1": "Singularity Cloud Security"}
GTITLE = dict(D.GROUPS)


def tally(key):
    t = {"ak": 0, "par": 0, "comp": 0, "nc": 0}
    for r in D.ROWS:
        t[r[key]["win"]] += 1
    return t


LOGO = b64("accuknox-logo.png")

# ---- cover ----
TILES = [("cloud", "Cloud posture"), ("db", "Data and AI security"), ("code", "Code scanning and CI/CD"), ("lock", "Runtime protection")]
tiles_html = "".join(f'<div class="tile">{ic(i, "ti")}<span>{t}</span></div>' for i, t in TILES)
cover = f"""
<section class="page cover">
  <img class="blob b1" src="{b64('cover-blob-red.png')}"><img class="blob b2" src="{b64('cover-blob-blue.png')}">
  <img class="clogo" src="{b64('accuknox-logo-cover.png')}">
  <div class="ctitle"><div class="t1">AccuKnox</div><div class="vs">vs</div>
    <div class="t2">Wiz, Palo Alto Networks<br>and SentinelOne</div>
    <div class="t3">(CNAPP for AWS and Azure)</div></div>
  <div class="ctiles">{tiles_html}</div>
  <div class="cdate">16 October 2026</div>
</section>"""

# ---- page 2: comparison ----
pick_html = "".join(
    f'<div class="pick">{ic(i, "ti")}<span>{esc(t)}{cites(ev)}</span></div>' for i, t, ev in D.PICK
)
tally_html = ""
for k, n in VENDORS:
    t = tally(k)
    parts = [("w", t["ak"], "AccuKnox leads")]
    tally_html += f'<div class="tl"><b>vs {n}</b> ' + "".join(f'<span class="{c}">{v} {lbl}</span>' for c, v, lbl in parts if v) + f'<span class="n">{12} capabilities compared</span></div>'


def cell_html(cl):
    if cl["win"] == "nc" and not cl["t"]:
        return f'<td class="cm s-nc">{chip("nc")}</td>'
    line = f'<div class="ln">{esc(cl["t"])}{cites(cl["ev"])}</div>' if cl["t"] else ""
    lab = "" if cl["win"] in ("par", "comp") else chip(cl["win"])
    return f'<td class="cm s-{"par" if cl["win"] == "comp" else cl["win"]}">{lab}{line}</td>'


def table_rows():
    out, last = [], None
    for r in D.ROWS:
        if r["g"] != last:
            out.append(f'<tr class="gh"><td colspan="5"><span class="num">{r["g"]}</span>{esc(GTITLE[r["g"]])}</td></tr>')
            last = r["g"]
        star = chip("star") if r.get("ak_star") else ""
        ak = f'<td class="ak">{star}<div class="ln">{esc(r["ak"]["t"])}{cites(r["ak"]["ev"])}</div></td>'
        out.append(
            f'<tr><td class="cap"><div class="capw">{ic(r["icon"], "capi")}<span>{esc(r["cap"])}</span></div></td>{ak}'
            + "".join(cell_html(r[k]) for k, _ in VENDORS) + "</tr>"
        )
    return "".join(out)


thead = (
    '<colgroup><col class="k1"><col class="k2"><col class="k3"><col class="k3"><col class="k3"></colgroup>'
    f'<thead><tr><th class="h-cap">Capability</th><th class="h-ak"><img src="{LOGO}"></th>'
    + "".join(f'<th class="h-c"><b>{n}</b><i>{HEAD_SUB[k]}</i></th>' for k, n in VENDORS)
    + "</tr></thead>"
)

page2_top = f"""
  <div class="topbar"></div>
  <div class="hd"><img class="logo" src="{LOGO}"><h1>Native code scanners and open-source runtime, in one CNAPP</h1></div>
  <div class="verdict"><div class="lbl">Pick AccuKnox for</div><div class="picks">{pick_html}</div></div>
  """
table2 = f'<table class="cmp">{thead}<tbody>{table_rows()}</tbody></table>'
note_pa = f'{esc(D.NOTES["palo"][0])}{cites(D.NOTES["palo"][1])}'
note_wz = f'{esc(D.NOTES["wiz"][0])}{cites(D.NOTES["wiz"][1])}'
page2 = f"""
<section class="page">
  {page2_top}
  {table2}
  <div class="notes"><span>{note_pa}</span><span>{note_wz}</span></div>
  <div class="legend">A cell with no label covers the same capability. Green label: AccuKnox leads or has a documented strength. Grey label: not compared.</div>
  <div class="pf"><span>AccuKnox vs Wiz, Palo Alto Networks and SentinelOne. One short line per cell, sourced on page 4.</span><span>2 / 4</span></div>
</section>"""

# ---- page 3: what to buy first, leads, POC, licensing ----
FITCLS = {"Must": ("f-must", "Must-have"), "Good": ("f-good", "Good-to-have"), "Defer": ("f-defer", "Defer")}
fit_rows = ""
for mod, pr, why, unit, ev in D.FIT:
    cls, lbl = FITCLS[pr]
    fit_rows += f'<tr><td class="fm">{esc(mod)}</td><td><span class="fit {cls}">{lbl}</span></td><td class="fw">{esc(why)}</td><td class="fw">{esc(unit)}{cites(ev)}</td></tr>'
fit_table = (
    '<table class="fit-t"><colgroup><col style="width:22%"><col style="width:14%"><col style="width:42%"><col style="width:22%"></colgroup>'
    "<thead><tr><th>AccuKnox module</th><th>Priority</th><th>Why, for your scope</th><th>Licensed by</th></tr></thead>"
    f"<tbody>{fit_rows}</tbody></table>"
)


def ul(bls):
    return "<ul>" + "".join(f'<li>{esc(x["t"])}{cites(x["ev"])}</li>' for x in bls) + "</ul>"


poc_html = "".join(f'<div class="pocr"><b>{esc(n)}</b><span>{esc(t)}{cites(bl["ev"])}</span></div>' for n, t, bl in D.POC)
poc_time = f'{esc(D.POC_TIMELINE["t"])}{cites(D.POC_TIMELINE["ev"])}.'
page3 = f"""
<section class="page">
  <div class="topbar"></div>
  <div class="sec"><span class="num">E</span><h2>What to buy first</h2><em class="sub">Our suggestion for the scope you gave. Confirm it at kickoff.</em></div>
  {fit_table}
  <div class="p3">
    <div class="card lead"><h3>Where AccuKnox leads</h3>{ul(D.WHERE_ACCUKNOX_LEADS)}<p class="ct">Check each one in the POC.</p></div>
    <div class="card poc"><h3>Small POC, after your internal approval</h3>{poc_html}<p class="ct">{poc_time}</p></div>
    <div class="card lic"><h3>How the others license</h3>{ul(D.LICENSE_NOTES)}</div>
  </div>
  <div class="pf"><span>AccuKnox vs Wiz, Palo Alto Networks and SentinelOne.</span><span>3 / 4</span></div>
</section>"""

# ---- page 4: sources (built last so numbering follows render order) ----
VN = {"ak": "AccuKnox", "wz": "Wiz", "pa": "Palo Alto", "s1": "SentinelOne"}
src_items = "".join(
    f'<li value="{NUM[s]}"><b class="v-{D.SOURCES[s][0]}">{VN[D.SOURCES[s][0]]}</b> '
    f'{esc(D.SOURCES[s][2])}. <a href="{html.escape(D.SOURCES[s][3])}">{esc(D.SOURCES[s][3].replace("https://", "").rstrip("/"))}</a></li>'
    for s in ORDER
)
page4 = f"""
<section class="page">
  <div class="topbar"></div>
  <div class="srcs"><h3>Sources, read 16 October 2026</h3>
    <p class="meth">AccuKnox pages were read live on help.accuknox.com. Competitor pages are product pages, documentation, blogs and marketplace listings, read with Firecrawl.
    Wiz and SentinelOne technical docs need a login, so those columns use public pages only. "Not compared" means this comparison makes no claim about that cell.
    Each line is a short paraphrase of the cited page. Superscripts match the numbers below.</p>
    <ol>{src_items}</ol></div>
  <div class="pf"><span>AccuKnox vs Wiz, Palo Alto Networks and SentinelOne. Schedule a demo: accuknox.com/contact-us</span><span>4 / 4</span></div>
</section>"""

CSS = """
@page { size: A4 landscape; margin: 0 }
:root{--navy:#11206D;--blue:#0046FF;--ink:#1B223B;--mute:#5A637D;--line:#DDE2EE;
--win:#0B7A42;--win-bg:#E4F5EC;--lim:#A15C00;--lim-bg:#FFF1DC;--par:#4D4DD9;--par-bg:#ECECFB;--nl:#5A637D;--nl-bg:#EEF0F5}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',Arial,sans-serif;color:var(--ink);font-size:8.6pt;line-height:1.28}
a{color:var(--blue);text-decoration:none}
.page{width:297mm;height:210mm;padding:8mm 10mm 10mm;position:relative;overflow:hidden;page-break-after:always;break-after:page}
.page:last-child{page-break-after:auto;break-after:auto}
.topbar{height:3px;background:linear-gradient(90deg,#1136D8,#6B3FD1 55%,#F0505A);border-radius:2px;margin-bottom:7px}
.ic,.ci,.capi,.ti{display:inline-block;vertical-align:middle}
.cover{padding:0}
.blob{position:absolute;width:200mm;opacity:.9}.b1{right:-70mm;top:-80mm}.b2{left:-80mm;bottom:-95mm}
.clogo{position:absolute;left:20mm;top:16mm;width:56mm}
.ctitle{position:absolute;left:20mm;top:52mm;border-left:5px solid;border-image:linear-gradient(#F0505A,#1136D8) 1;padding-left:9mm}
.t1{font-size:50pt;font-weight:700;color:#1136D8;line-height:1}.vs{font-size:24pt;color:#44505F;margin:2mm 0}
.t2{font-size:30pt;font-weight:700;color:#1136D8;line-height:1.1}.t3{font-size:16pt;font-weight:500;color:var(--navy);margin-top:5mm}
.ctiles{position:absolute;left:20mm;right:20mm;bottom:24mm;display:grid;grid-template-columns:repeat(4,1fr);gap:6mm}
.tile{display:flex;align-items:center;gap:8px;background:rgba(255,255,255,.88);border:1px solid #C9D2E6;border-radius:12px;padding:5mm;font-size:11pt;font-weight:600;color:var(--navy)}
.tile .ti{width:20px;height:20px;padding:5px;background:#EAF0FF;color:var(--blue);border-radius:7px;box-sizing:content-box;flex:none}
.cdate{position:absolute;left:20mm;bottom:12mm;font-size:9pt;color:var(--mute)}
.hd{display:flex;gap:14px;align-items:center;margin-bottom:4px}.logo{height:20px}
h1{font-size:17pt;line-height:1.1;margin:0;color:var(--navy)}
.verdict{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:center;border:1.5px solid var(--blue);border-radius:9px;padding:3px 10px;background:#F4F7FF;margin-bottom:4px}
.verdict .lbl{font-weight:700;font-size:9.5pt;color:var(--blue);max-width:22mm;line-height:1.1}
.picks{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.pick{display:flex;gap:6px;align-items:center;font-weight:600;font-size:8.8pt;line-height:1.2}
.ti{width:15px;height:15px;color:var(--blue);flex:none;background:#fff;border-radius:5px;padding:3px;box-sizing:content-box}
.tallies{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:5px}
.tl{font-size:7.6pt;white-space:nowrap;color:var(--mute);border:1px solid var(--line);border-radius:7px;padding:2px 8px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.tl b{color:var(--ink);font-size:8.4pt}.tl .w{color:var(--win);font-weight:700}.tl .p{color:var(--par);font-weight:600}.tl .o{color:var(--lim);font-weight:600}
table{width:100%;border-collapse:separate;border-spacing:0;table-layout:fixed}
col.k1{width:17%}col.k2{width:25%}col.k3{width:19.3%}
thead th{padding:3px 7px 4px;text-align:left;border-bottom:2px solid var(--navy);font-size:7.6pt;text-transform:uppercase;letter-spacing:.4px;color:var(--mute);vertical-align:bottom}
th.h-ak{background:#EEF3FF;border-radius:7px 7px 0 0;border-bottom-color:var(--blue)}th.h-ak img{height:15px}
th.h-c b{display:block;font-size:10pt;color:var(--ink);text-transform:none;letter-spacing:0}
th.h-c i{display:block;font-style:normal;font-size:6.8pt;color:var(--mute);text-transform:none;letter-spacing:0;font-weight:500}
tr.gh td{padding:4px 0 1px;border-bottom:1.5px solid var(--navy);font-weight:700;font-size:9.4pt;color:var(--navy)}
tr.gh .num{font-size:7.6pt;color:#fff;background:var(--navy);border-radius:4px;padding:1px 6px;margin-right:7px}
td{vertical-align:middle;padding:2px 7px;border-bottom:1px solid var(--line)}
.capw{display:flex;align-items:center;gap:6px;font-weight:700;font-size:9pt;color:var(--navy);line-height:1.15}
.capi{width:15px;height:15px;flex:none;color:var(--blue)}
td.ak .chip+.ln{margin-top:2px}td.ak{background:#F3F7FF;border-left:3px solid var(--win);font-weight:600;font-size:9pt}
td.cm{border-left:3px solid var(--line)}
td.cm.s-ak{border-left-color:var(--win)}td.cm.s-par{border-left-color:var(--par)}td.cm.s-comp{border-left-color:#E0A340}td.cm.s-nc{border-left-color:#B6BCCB}
.ln{margin-top:1px;line-height:1.25}td.cm .chip+.ln{margin-top:2px}td.cm .ln{color:#3F4766}td.ak .ln{margin-top:0}
.chip{display:inline-flex;align-items:center;gap:3px;font-weight:700;font-size:6.6pt;letter-spacing:.3px;padding:1px 6px 1px 4px;border-radius:8px;text-transform:uppercase}
.ci{width:8px;height:8px;stroke-width:3}
.c-win{background:var(--win-bg);color:var(--win)}.c-lim{background:var(--lim-bg);color:var(--lim)}.c-par{background:var(--par-bg);color:var(--par)}.c-nl{background:var(--nl-bg);color:var(--nl)}
sup.c{font-size:5.8pt;color:var(--blue);font-weight:700;margin-left:1px;vertical-align:super;line-height:0}
.legend{font-size:7pt;color:var(--mute);margin-top:3px}.notes{display:grid;grid-template-columns:1fr 1fr;gap:14px;font-size:7pt;color:var(--mute);margin-top:6px}
.sec{display:flex;align-items:baseline;gap:8px;margin:0 0 5px}
.sec .num{font-size:8pt;font-weight:700;color:#fff;background:var(--navy);border-radius:4px;padding:1px 7px}
.sec h2{font-size:15pt;margin:0;color:var(--navy)}.sec .sub{font-size:8pt;color:var(--mute);font-style:normal;margin-left:6px}
.fit-t th{font-size:7.6pt;padding:4px 7px;text-align:left;border-bottom:2px solid var(--navy);text-transform:uppercase;letter-spacing:.4px;color:var(--mute)}
.fit-t td{padding:9px 8px;font-size:10.6pt}
.fm{font-weight:700;color:var(--navy)}.fw{color:#3F4766}
.fit{display:inline-block;font-weight:700;font-size:7pt;text-transform:uppercase;letter-spacing:.3px;padding:1px 7px;border-radius:8px}
.f-must{background:var(--navy);color:#fff}.f-good{background:#DDEBFF;color:#0B3FA8}.f-defer{background:var(--nl-bg);color:var(--nl)}
.p3{display:grid;grid-template-columns:1fr 1.15fr 1fr;gap:12px;margin-top:18px}
.card{border:1.5px solid var(--line);border-radius:9px;padding:8px 11px}
.card h3{margin:0 0 7px;font-size:12pt;color:var(--navy)}
.card ul{margin:0;padding-left:13px}.card li{margin:0 0 6px;font-size:10pt}
.card .ct{margin:7px 0 0;font-weight:700;color:var(--blue);font-size:9.4pt}
.card.lead{border-color:#9ED8B8;background:#F2FBF6}.card.poc{border-color:#BFD0FF;background:#F4F7FF}
.pocr{display:grid;grid-template-columns:24mm 1fr;gap:6px;margin-bottom:6px;font-size:10pt}.pocr b{color:var(--navy)}
.srcs h3{margin:0 0 3px;font-size:12pt;color:var(--navy)}
.meth{margin:0 0 7px;font-size:8pt;color:var(--mute);line-height:1.35}
.srcs ol{margin:0;padding-left:17px;columns:3;column-gap:16px}
.srcs li{font-size:7pt;line-height:1.3;break-inside:avoid;color:#4A5270;margin-bottom:2px;overflow-wrap:anywhere}
.srcs li b{font-weight:700;font-size:6.3pt;text-transform:uppercase;letter-spacing:.3px;margin-right:2px}
.srcs a{color:#2A3560;text-decoration:underline;text-decoration-color:#B8C0D8}
.v-ak{color:var(--blue)}.v-wz{color:#7A2E9E}.v-pa{color:#C0471A}.v-s1{color:#6B3FD1}
.pf{position:absolute;left:10mm;right:10mm;bottom:4mm;display:flex;justify-content:space-between;font-size:6.6pt;color:#8089A3}
"""

HTML = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>AccuKnox vs Wiz, Palo Alto Networks and SentinelOne: CNAPP comparison</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{cover}{page2}{page3}{page4}</body></html>"""

BUILD.mkdir(exist_ok=True)
(BUILD / "comparison.html").write_text(HTML, encoding="utf-8")
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page()
    pg.goto((BUILD / "comparison.html").as_uri())
    pg.wait_for_load_state("networkidle")
    over = pg.evaluate(
        """() => [...document.querySelectorAll('.page')].map((el, i) => {
            let maxB = 0;
            el.querySelectorAll('*').forEach(n => { if (n.closest('.pf')) return; const r = n.getBoundingClientRect(); maxB = Math.max(maxB, r.bottom - el.getBoundingClientRect().top); });
            return [i + 1, Math.round(maxB), Math.round(el.getBoundingClientRect().height)];
        })"""
    )
    for i, used, total in over:
        print(f"page {i}: content bottom {used}px of {total}px" + ("  <-- OVERFLOW" if used > total - 14 and i > 1 else ""))
    pg.pdf(path=str(OUT), width="297mm", height="210mm", print_background=True, prefer_css_page_size=True)
    br.close()

print(f"{OUT}: {len(PdfReader(str(OUT)).pages)} pages, {len(ORDER)} sources")
