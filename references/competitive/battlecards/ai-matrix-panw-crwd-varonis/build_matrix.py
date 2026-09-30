"""Build the AccuKnox vs Palo Alto Networks, CrowdStrike and Varonis AI security matrix PDF.

The PDF is a 16:9 document. The cover and the closing page are the fixed
layouts 0 and 1 from doc-ppt-template/PPT Template.pptx, exported through
PowerPoint. The body pages render from HTML with Playwright. Content lives in
matrix_data.py, so a fact change never touches this file.

Run from anywhere:
    python build_matrix.py [out.pdf]

Needs playwright (chromium), pypdf, pypdfium2, python-pptx and PowerPoint.
"""
import base64
import pathlib
import subprocess
import sys

from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter, Transformation

import matrix_data as D

HERE = pathlib.Path(__file__).resolve().parent
A = HERE / "assets"
BUILD = HERE / "build"
TPL = pathlib.Path(r"D:\AccuKnox\doc-ppt-template")
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(
    r"D:\AccuKnox\AccuKnox_vs_PaloAlto_CrowdStrike_Varonis_AI_Security.pdf")


def b64(name):
    return "data:image/png;base64," + base64.b64encode((A / name).read_bytes()).decode()


def si(name, color):
    svg = (A / f"si_{name}.svg").read_text(encoding="utf-8")
    return svg.replace("<svg ", f'<svg class="brand" fill="#{color}" ', 1)


BR = {k: si(f, c) for k, (f, c) in {
    "openai": ("openai", "000000"), "claude": ("claude", "D97757"), "gemini": ("googlegemini", "8E75B2"),
    "copilot": ("githubcopilot", "000000"), "nvidia": ("nvidia", "76B900"), "k8s": ("kubernetes", "326CE5"),
    "hf": ("huggingface", "FFB000"), "ollama": ("ollama", "000000"), "langchain": ("langchain", "1C3C3C"),
    "n8n": ("n8n", "EA4B71"), "gcp": ("googlecloud", "4285F4"), "kong": ("kong", "003459"),
    "gha": ("githubactions", "2088FF"), "jenkins": ("jenkins", "D24939"), "jira": ("jira", "0052CC"),
    "slack": ("slack", "4A154B"), "ms": ("microsoft", "5E5E5E"),
}.items()}

I = {
    "code": '<polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "bot": '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
    "cross": '<circle cx="12" cy="12" r="10"/><line x1="22" x2="18" y1="12" y2="12"/><line x1="6" x2="2" y1="12" y2="12"/><line x1="12" x2="12" y1="6" y2="2"/><line x1="12" x2="12" y1="22" y2="18"/>',
    "eyeoff": '<path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/><path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/><path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"/><line x1="2" x2="22" y1="2" y2="22"/>',
    "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9Z"/>',
    "server": '<rect width="20" height="8" x="2" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7Z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "browser": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 8h20"/><path d="M6 4v4"/><path d="M10 4v4"/>',
    "gateway": '<rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6.01 18H6"/><path d="M10.01 18H10"/><path d="M15 10v4"/><path d="M17.84 7.17a4 4 0 0 0-5.66 0"/><path d="M20.66 4.34a8 8 0 0 0-11.31 0"/>',
    "box": '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "filescan": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><circle cx="11.5" cy="14.5" r="2.5"/><path d="M13.3 16.3 15 18"/>',
    "list": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
    "pulse": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "monitor": '<rect width="20" height="14" x="2" y="3" rx="2"/><line x1="8" x2="16" y1="21" y2="21"/><line x1="12" x2="12" y1="17" y2="21"/>',
    "term": '<polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "half": '<circle cx="12" cy="12" r="9"/><path d="M12 3v18"/>',
    "equal": '<line x1="5" x2="19" y1="9" y2="9"/><line x1="5" x2="19" y1="15" y2="15"/>',
    "key": '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
    "plug": '<path d="M12 22v-5"/><path d="M9 8V2"/><path d="M15 8V2"/><path d="M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z"/>',
    "db": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>',
    "scale": '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    "zap": '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "award": '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
}


def ic(name, cls="ic"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round">{I[name]}</svg>')


CHIP = {
    "yes": ("c-win", "check", "Supported"),
    "no": ("c-no", "x", "Not supported"),
    "noeq": ("c-no", "x", "No equivalent"),
    "lim": ("c-lim", "half", "Limited"),
    "par": ("c-par", "equal", "Parity"),
}


def chip(k):
    cls, icon, label = CHIP[k]
    return f'<span class="chip {cls}">{ic(icon, "ci")}{label}</span>'


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


VENDORS = [("panw", "Palo Alto Networks"), ("crwd", "CrowdStrike"), ("vrns", "Varonis")]


def vhead():
    return "".join(f'<th class="h-v"><span class="vn">{n}</span></th>' for _, n in VENDORS)


def thead():
    return (f'<colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c3"><col class="c3"></colgroup>'
            f'<thead><tr><th class="h-cap">Capability</th><th class="h-ak"><img src="{b64("accuknox-logo.png")}"></th>'
            f'{vhead()}</tr></thead>')


def row(r):
    ak_k = r.get("ak_k", "yes")
    cells = ""
    for key, _ in VENDORS:
        k, items = r["v"][key]
        cells += f'<td class="vd {k}">{chip(k)}{ul(items)}</td>'
    return (f'<tr><td class="cap"><div class="capw">{ic(r["icon"], "capi")}<span>{r["cap"]}</span></div>'
            f'<div class="tk">{r["tk"]}</div></td>'
            f'<td class="ak">{chip(ak_k)}{ul(r["ak"])}</td>{cells}</tr>')


def table(rows):
    return f'<table>{thead()}<tbody>{"".join(row(r) for r in rows)}</tbody></table>'


PAGE_NO = [1]


def page(mod, title, body, sub=None):
    PAGE_NO[0] += 1
    s = f'<div class="sub">{sub}</div>' if sub else ""
    return f"""<section class="pg" id="p{PAGE_NO[0]}">
<div class="topbar"></div>
<header><div class="hl"><span class="mod">{mod}</span><h1>{title}</h1>{s}</div>
<img class="hlogo" src="{b64('accuknox-logo.png')}"></header>
<div class="body">{body}</div>
<footer><span>AccuKnox vs Palo Alto Networks, CrowdStrike and Varonis &middot; AI Security</span><span>{PAGE_NO[0]}</span></footer>
</section>"""


# ---------------------------------------------------------------- page bodies

def glance():
    picks = "".join(f'<div class="pick">{ic(i, "ti")}<span>{t}</span></div>' for i, t in D.PICK)
    head = "".join(f'<th>{n}</th>' for _, n in VENDORS)
    body = ""
    for g in D.GLANCE:
        cells = "".join(f'<td class="g {k}">{chip(k)}<span class="gn">{t}</span></td>' for k, t in g["v"])
        body += (f'<tr><td class="gm"><span class="gnum">{g["n"]}</span>{ic(g["icon"], "capi")}<b>{g["m"]}</b></td>'
                 f'<td class="g ak">{chip(g.get("ak_k", "yes"))}<span class="gn">{g["ak"]}</span></td>{cells}</tr>')
    tally = "".join(f'<span><span class="dot" style="background:{c}"></span><b>{n}</b> {t}</span>' for c, n, t in D.TALLY)
    proof = "".join(f'<div class="pf">{ic("award", "pfi")}<span>{t}</span></div>' for t in D.PROOF)
    return f"""<div class="verdict"><div class="lbl">Choose AccuKnox to</div><div class="picks">{picks}</div></div>
<div class="tally">{tally}</div>
<table class="glance"><colgroup><col style="width:24.5%"><col style="width:21.5%"><col style="width:18%"><col style="width:18%"><col style="width:18%"></colgroup>
<thead><tr><th>Module</th><th class="h-ak"><img src="{b64('accuknox-logo.png')}"></th>{head}</tr></thead><tbody>{body}</tbody></table>
<div class="proof">{proof}</div>"""


def shadow_panel():
    s = D.SHADOW
    surf = "".join(
        f'<div class="surf">{ic(i, "ti")}<div><b>{n}</b><span>{t}</span>'
        f'<span class="logos">{"".join(BR[b] for b in bs)}</span></div></div>' for i, n, t, bs in s["ak"])
    comp = ""
    for key, name in VENDORS:
        k, items = s["v"][key]
        comp += f'<div class="col vcol"><div class="top"><span class="vn">{name}</span>{chip(k)}</div>{ul(items)}</div>'
    return f"""<div class="panel">
<div class="hd">{ic("eyeoff", "capi")}<h3>{s["title"]}</h3></div>
<div class="vs3">
  <div class="col akc"><div class="top"><img src="{b64('accuknox-logo.png')}">{chip("yes")}</div><div class="surfs">{surf}</div></div>
  {comp}
</div>
<div class="ptk">{s["tk"]}</div></div>"""


def gateway_page():
    g = D.GATEWAY
    modes = "".join(
        f'<div class="mode"><div class="from">{ic(i, "ti")}<div><b>{a}</b><span>{b}</span></div></div>'
        f'{ic("arrow", "arr")}<div class="to"><b>{c}</b><span>{d}</span></div></div>' for i, a, b, c, d in g["modes"])
    gws = "".join(f'<span class="gw">{x}</span>' for x in g["gateways"])
    comp = ""
    for key, name in VENDORS:
        k, items = g["v"][key]
        comp += f'<div class="gcol"><div class="top"><span class="vn">{name}</span>{chip(k)}</div>{ul(items)}</div>'
    pts = "".join(f'<div class="gp">{ic(i, "ti")}<div><b>{h}</b><span>{t}</span></div></div>' for i, h, t in g["points"])
    return f"""<div class="gwrap">
<div class="gleft">
  <div class="gtitle">{ic("plug", "capi")}<span>{g["title"]}</span></div>
  <div class="modes">{modes}</div>
  <div class="gwrow"><span class="gwl">Enforces inside</span>{gws}</div>
  <div class="gpts">{pts}</div>
</div>
<div class="gright">{comp}</div>
</div>
<div class="ptk">{g["tk"]}</div>"""


def deploy_strip():
    d = D.DEPLOY
    cells = f'<div class="dp akd"><img src="{b64("accuknox-logo.png")}"><b>{d["ak"][0]}</b><span>{d["ak"][1]}</span></div>'
    for key, name in VENDORS:
        a, b = d["v"][key]
        cells += f'<div class="dp"><span class="vn">{name}</span><b>{a}</b><span>{b}</span></div>'
    return f'<div class="deploy"><div class="dl">{ic("server", "capi")}<span>{d["title"]}</span></div><div class="dps">{cells}</div></div>'


def toc(entries):
    items = "".join(
        f'<a class="te" href="#p{n}"><span class="tn">{m.replace("Module ", "") if m.startswith("Module") else "AZ"}</span>'
        f'<span class="tm">{m} &middot; page {n}</span><span class="tt">{t}</span></a>' for n, m, t in entries)
    return f'<div class="toc">{items}</div>'


def short(u):
    return u.replace("https://", "").replace("www.", "").rstrip("/")


def sources():
    cols = [("AccuKnox", D.AK_SOURCES)] + [(n, D.SOURCES[k]) for k, n in VENDORS]
    body = ""
    for name, urls in cols:
        links = "".join(f'<a href="{u}">{short(u)}</a>' for u in urls)
        body += f'<div class="scol"><div class="sh">{name}</div>{links}</div>'
    return f'<div class="srcs">{body}</div>'


# ---------------------------------------------------------------- CSS

CSS = """
@page { size: 13.333in 7.5in; margin: 0 }
:root{--navy:#11206D;--blue:#0046FF;--ink:#1B223B;--mute:#5A637D;--line:#DDE2EE;--sec:#6464FF;
--win:#0B7A42;--win-bg:#E4F5EC;--no:#C80019;--no-bg:#FCE9EC;--lim:#A15C00;--lim-bg:#FFF1DC;--par:#4D4DD9;--par-bg:#ECECFB}
*{box-sizing:border-box}
body{margin:0;font-family:'Space Grotesk',Arial,sans-serif;color:var(--ink);font-size:9.6pt;line-height:1.28}
.ic,.ci,.capi,.ti{display:inline-block;vertical-align:middle}
.brand{width:12px;height:12px;vertical-align:-2px;margin-right:4px}
.pg{width:13.333in;height:7.5in;padding:0.30in 0.42in 0.26in;position:relative;page-break-after:always;overflow:hidden;display:flex;flex-direction:column}
.topbar{position:absolute;left:0;right:0;top:0;height:5px;background:linear-gradient(90deg,#1136D8,#6B3FD1 55%,#F0505A)}
header{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px}
.mod{display:inline-block;font-size:8pt;font-weight:700;letter-spacing:.6px;text-transform:uppercase;color:#fff;background:var(--navy);border-radius:4px;padding:2px 8px;margin-bottom:5px}
h1{font-size:21pt;line-height:1.08;margin:0;color:var(--navy);font-weight:700}
h1 em{font-style:normal;color:var(--blue)}
.sub{font-size:10pt;color:var(--mute);margin-top:4px}
.hlogo{height:20px;margin-top:4px}
.body{flex:1;min-height:0}
footer{display:flex;justify-content:space-between;font-size:7.4pt;color:#8A92AA;border-top:1px solid var(--line);padding-top:5px;margin-top:6px}

/* matrix table */
table{width:100%;border-collapse:separate;border-spacing:0;table-layout:fixed}
col.c1{width:17%}col.c2{width:29%}col.c3{width:18%}
thead th{padding:5px 9px 6px;text-align:left;border-bottom:2px solid var(--navy);font-size:7.6pt;text-transform:uppercase;letter-spacing:.5px;color:var(--mute);vertical-align:bottom}
th.h-ak{background:#EEF3FF;border-radius:8px 8px 0 0;border-bottom-color:var(--blue)}
th.h-ak img{height:19px}
.vn{font-size:11.5pt;font-weight:700;color:#3A4262;text-transform:none;letter-spacing:0}
tbody tr{break-inside:avoid}
td{vertical-align:top;padding:11px 10px 10px;border-bottom:1px solid var(--line)}
td.cap .capw{display:flex;gap:7px;align-items:flex-start;font-weight:700;font-size:13.5pt;line-height:1.12;color:var(--navy)}
.capi{width:21px;height:21px;flex:none;color:var(--blue);margin-top:1px}
td.cap .tk{margin:7px 0 0 28px;font-weight:700;font-size:9.6pt;color:var(--blue);line-height:1.22}
td.ak{background:#F3F7FF;border-left:3px solid var(--win)}
td.vd{border-left:3px solid var(--line)}
td.vd.no,td.vd.noeq{border-left-color:var(--no)} td.vd.lim{border-left-color:#E0A340} td.vd.par{border-left-color:var(--par)} td.vd.yes{border-left-color:#7CC4A0}
td ul{margin:7px 0 0;padding-left:14px} td li{margin:0 0 4px} td li::marker{color:#9AA3BD}
td.vd li{color:#4A5270;font-size:10pt}
td.ak li{font-size:10.8pt}
.chip{display:inline-flex;align-items:center;gap:3px;font-weight:700;font-size:7.4pt;letter-spacing:.3px;padding:1.5px 7px 1.5px 5px;border-radius:9px;text-transform:uppercase;white-space:nowrap}
.ci{width:9px;height:9px;stroke-width:3}
.c-win{background:var(--win-bg);color:var(--win)} .c-no{background:var(--no-bg);color:var(--no)}
.c-lim{background:var(--lim-bg);color:var(--lim)} .c-par{background:var(--par-bg);color:var(--par)}
.soon{display:inline-block;font-size:6.6pt;font-weight:700;letter-spacing:.3px;text-transform:uppercase;color:var(--par);background:var(--par-bg);border-radius:4px;padding:0 4px;margin-left:3px;vertical-align:1px}
.beta{display:inline-block;font-size:6.6pt;font-weight:700;letter-spacing:.3px;text-transform:uppercase;color:var(--lim);background:var(--lim-bg);border-radius:4px;padding:0 4px;margin-left:3px;vertical-align:1px}
.tags i{font-style:normal;display:inline-block;background:#fff;border:1px solid #C9D6F5;border-radius:4px;padding:0 4px;margin:1px 2px 1px 0;font-size:8.2pt;font-weight:600;color:var(--navy)}
b.k{color:var(--navy)}

/* at a glance */
.verdict{display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:stretch;border:1.5px solid var(--blue);border-radius:10px;padding:8px 12px;background:#F4F7FF;margin-bottom:6px}
.verdict .lbl{font-weight:700;font-size:10.5pt;color:var(--blue);display:flex;align-items:center;max-width:30mm;line-height:1.15}
.picks{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.pick{display:flex;gap:7px;align-items:center;font-weight:600;font-size:10pt;line-height:1.2}
.ti{width:18px;height:18px;color:var(--blue);flex:none;background:#EAF0FF;border-radius:5px;padding:3px;box-sizing:content-box}
.pick .ti{background:#fff}
.tally{display:flex;gap:18px;font-size:9.2pt;color:var(--mute);margin:0 2px 6px;align-items:center}
.tally b{color:var(--ink)}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px}
table.glance th{font-size:8pt}
table.glance thead th:not(.h-ak){font-size:10pt;font-weight:700;color:#3A4262;text-transform:none;letter-spacing:0}
table.glance td{padding:6.5px 9px;vertical-align:middle}
td.gm{font-size:10.6pt;color:var(--navy);line-height:1.15}
td.gm .capi{width:15px;height:15px;margin:0 6px 0 0}
.gnum{display:inline-block;width:22px;font-size:7.6pt;font-weight:700;color:#8A92AA}
td.g{border-left:3px solid var(--line)} td.g.ak{background:#F3F7FF;border-left-color:var(--win)}
td.g.no,td.g.noeq{border-left-color:var(--no)} td.g.lim{border-left-color:#E0A340} td.g.yes{border-left-color:#7CC4A0} td.g.par{border-left-color:var(--par)}
.gn{display:block;font-size:9.2pt;color:#4A5270;margin-top:1px;line-height:1.15}
td.g.ak .gn{color:var(--ink);font-weight:600}
.proof{display:flex;gap:10px;margin-top:10px}
.pf{flex:1;display:flex;gap:6px;align-items:center;font-size:9.2pt;font-weight:600;color:var(--navy);background:#F4F7FF;border:1px solid #D5DEF7;border-radius:8px;padding:5px 8px}
.pfi{width:15px;height:15px;color:var(--blue);flex:none}

/* shadow AI panel */
.panel{border:1.5px solid var(--navy);border-radius:10px;padding:11px 12px;break-inside:avoid;background:linear-gradient(180deg,#F4F7FF,#fff 55%);margin-top:10px}
.panel .hd{display:flex;align-items:center;gap:8px;margin-bottom:7px}
.panel h3{margin:0;font-size:14pt;color:var(--navy)}
.panel h3 .neq{color:var(--no)}
.vs3{display:grid;grid-template-columns:40fr 20fr 20fr 20fr;gap:8px}
.col{border-radius:8px;padding:7px 9px;background:#fff}
.col.akc{border:1px solid #BFD0FF} .col.vcol{border:1px solid #F0D2B8}
.col .top{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;gap:4px}
.col .top img{height:14px}
.col .vn{font-size:9.4pt}
.surfs{display:grid;grid-template-columns:1fr 1fr;gap:7px 10px}
.surf{display:flex;gap:7px;align-items:flex-start}
.surf .ti{width:15px;height:15px}
.surf b{display:block;font-size:10.4pt;color:var(--navy)}
.surf span{font-size:9.2pt;color:#3A4262}
.surf .logos{display:block;margin-top:2px}
.col.vcol ul{margin:0;padding-left:13px;font-size:9.4pt} .col.vcol li{margin:0 0 3px;color:#4A5270}
.col.vcol li b{color:var(--ink)}
.ptk{margin-top:9px;font-weight:700;color:var(--blue);font-size:10.6pt}

/* gateway */
.gwrap{display:grid;grid-template-columns:58fr 42fr;gap:12px}
.gleft{border:1.5px solid var(--blue);border-radius:10px;padding:10px 12px;background:linear-gradient(180deg,#F4F7FF,#fff 60%)}
.gtitle{display:flex;gap:8px;align-items:center;font-size:14.5pt;font-weight:700;color:var(--navy);margin-bottom:11px}
.modes{display:grid;gap:9px}
.mode{display:grid;grid-template-columns:1fr 18px 1fr;gap:8px;align-items:center}
.from,.to{border-radius:7px;padding:8px 10px;min-height:52px}
.from{display:flex;gap:7px;align-items:center;background:#fff;border:1px solid var(--line)}
.from .ti{width:15px;height:15px}
.to{background:#EAF0FF;border:1px solid #BFD0FF}
.from b,.to b{display:block;font-size:10.8pt;color:var(--navy)} .from span,.to span{font-size:9.4pt;color:#4A5270}
.arr{width:16px;height:16px;color:var(--blue)}
.gwrow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:14px 0 12px}
.gwl{font-size:8pt;font-weight:700;color:var(--mute);text-transform:uppercase;letter-spacing:.4px;margin-right:3px}
.gw{background:var(--navy);color:#fff;border-radius:5px;padding:3px 9px;font-size:9.6pt;font-weight:600}
.gpts{display:grid;grid-template-columns:1fr 1fr;gap:10px 14px}
.gp{display:flex;gap:7px;align-items:flex-start}
.gp .ti{width:15px;height:15px}
.gp b{display:block;font-size:10.6pt;color:var(--navy)} .gp span{font-size:9.4pt;color:#3A4262}
.gright{display:grid;gap:12px;align-content:stretch}
.gcol{border:1px solid var(--line);border-left:3px solid #E0A340;border-radius:8px;padding:10px 12px}
.gcol .top{display:flex;justify-content:space-between;align-items:center}
.gcol ul{margin:7px 0 0;padding-left:14px;font-size:10.2pt} .gcol li{margin:0 0 4px;color:#4A5270}
.toc{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(5,auto);grid-auto-flow:column;gap:10px 22px;margin-top:10px}
.te{display:grid;grid-template-columns:44px 1fr;grid-template-rows:auto auto;column-gap:10px;align-items:center;text-decoration:none;border:1px solid var(--line);border-left:4px solid var(--blue);border-radius:9px;padding:11px 14px;background:#fff}
.tn{grid-row:1/3;font-size:20pt;font-weight:700;color:var(--blue)}
.tm{font-size:8pt;font-weight:700;letter-spacing:.5px;text-transform:uppercase;color:var(--mute)}
.tt{font-size:11.5pt;font-weight:700;color:var(--navy);line-height:1.2}
.srcs{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;margin-top:4px}
.scol{min-width:0}
.sh{font-size:11pt;font-weight:700;color:var(--navy);border-bottom:2px solid var(--navy);padding-bottom:4px;margin-bottom:5px}
.scol a{display:block;font-size:7.6pt;line-height:1.55;color:var(--blue);text-decoration:none;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
code{font-family:Consolas,monospace;font-size:8.4pt;background:#fff;border:1px solid #D5DEF7;border-radius:3px;padding:0 3px}
.deploy{margin-top:18px;border:1.5px solid var(--navy);border-radius:10px;padding:9px 11px;background:linear-gradient(180deg,#F4F7FF,#fff 60%)}
.dl{display:flex;gap:8px;align-items:center;font-size:13pt;font-weight:700;color:var(--navy);margin-bottom:7px}
.dps{display:grid;grid-template-columns:29fr 23.6fr 23.6fr 23.6fr;gap:8px}
.dp{border:1px solid var(--line);border-left:3px solid var(--no);border-radius:8px;padding:7px 10px;background:#fff}
.dp.akd{border-left-color:var(--win);background:#F3F7FF}
.dp img{height:15px;display:block;margin-bottom:4px}
.dp .vn{display:block;margin-bottom:3px}
.dp b{display:block;font-size:12.5pt;color:var(--navy)} .dp span{font-size:9.6pt;color:#4A5270}
"""


def build_html():
    entries = [(4 + i, label, name) for label, name, i in D.MODULES]
    PAGE_NO[0] = 1
    pages = [page("AI Security Comparison", "Contents", toc(entries))]
    pages.append(page("At a glance", D.HEADLINE, glance()))
    for p in D.PAGES:
        if p["kind"] == "table":
            body = table(p["rows"])
            if p.get("shadow"):
                body += shadow_panel()
            if p.get("deploy"):
                body += deploy_strip()
        elif p["kind"] == "gateway":
            body = gateway_page()
        pages.append(page(p["mod"], p["title"], body, p.get("sub")))
    pages.append(page("Sources", "Vendor Pages and AccuKnox Help Docs", sources()))
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>{"".join(pages)}</body></html>"""


def covers():
    pptx = BUILD / "covers.pptx"
    pdf = BUILD / "covers.pdf"
    subprocess.run(["py", "-3.11", str(TPL / "scripts" / "build_ai_matrix_covers.py"), str(pptx)],
                   check=True, capture_output=True)
    ps = BUILD / "topdf.ps1"
    ps.write_text("param([string]$Pptx,[string]$Pdf)\n$pp = New-Object -ComObject PowerPoint.Application\n"
                  "try { $p = $pp.Presentations.Open($Pptx, $true, $false, $false); $p.SaveAs($Pdf, 32); $p.Close() }\n"
                  "finally { $pp.Quit(); [System.Runtime.InteropServices.Marshal]::ReleaseComObject($pp) | Out-Null }\n")
    subprocess.run(["powershell", "-NoProfile", "-File", str(ps), "-Pptx", str(pptx), "-Pdf", str(pdf)], check=True)
    return pdf


def main():
    BUILD.mkdir(exist_ok=True)
    html = build_html()
    (BUILD / "matrix.html").write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto((BUILD / "matrix.html").as_uri())
        pg.wait_for_load_state("networkidle")
        pg.pdf(path=str(BUILD / "body.pdf"), print_background=True, prefer_css_page_size=True)
        b.close()
    body = PdfReader(str(BUILD / "body.pdf"))
    W, H = float(body.pages[0].mediabox.width), float(body.pages[0].mediabox.height)
    cov = PdfReader(str(covers()))
    w = PdfWriter()

    def scaled(pg):
        s = W / float(pg.mediabox.width)
        pg.add_transformation(Transformation().scale(s, s))
        pg.mediabox.upper_right = (W, H)
        pg.cropbox.upper_right = (W, H)
        return pg

    w.add_page(scaled(cov.pages[0]))
    for pg in body.pages:
        w.add_page(pg)
    w.add_page(scaled(cov.pages[1]))
    w.add_metadata({"/Title": "AccuKnox vs Palo Alto Networks, CrowdStrike and Varonis: AI Security",
                    "/Author": "AccuKnox"})
    w.write(OUT)
    print(f"{OUT}: {len(body.pages) + 2} pages")


if __name__ == "__main__":
    main()
