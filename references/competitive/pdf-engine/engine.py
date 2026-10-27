"""Shared AccuKnox comparison PDF engine.

Every comparison PDF is built here, so every one carries the same cover, type, colors and
layout. A comparison set (see ../pdf-sources/) supplies a SPEC dict and calls build(spec).

SPEC keys
    vendors        ["AccuKnox", "Snyk", ...]   index 0 is always AccuKnox
    sections       [{"name": "A. Area", "rows": [row, ...]}]
                   row = {"no": 1, "name": "...", "short": "AccuKnox one-liner",
                          "cells": [{"st": "Y|P|N", "text": "...", "src": url|None}, ...]}  one cell per vendor
    themes         [(title, body, (row numbers))]  AccuKnox differentiators, shown on page 1 of the body
    strengths      {vendor index: [(lead, text)]}  where the competitor is strong. Required per head-to-head
    sources        {vendor index: (name, [(label, url)])}
    ak_refs        {area letter: [(label, path under help.accuknox.com)]}
    tag            small cover label, e.g. "Application security"
    date           e.g. "October 2026"
    scope_vs       cover text for a head-to-head, with {name}
    scope_score    cover text for a scorecard
    kick_vs, kick_score        cover eyebrow lines
    score_title    list of cover title lines for a scorecard
    score_note     HTML list items for the "Where AccuKnox is partial" box on a scorecard
    jobs           [{"kind": "score", "file": "...", "title": "...", "vendors": [0, 1, 2, 3]},
                    {"kind": "vs", "file": "...", "title": "...", "vendor": 1}]
    category       free text for the index, e.g. "appsec"
    out_dir        folder that receives the PDFs, normally the set folder (Path)
    sheet_url      optional, where the data came from

Output: <out_dir>/<file>.pdf plus <file>.meta.json (read by ../build_index.py). out_dir is the set's own folder.
Needs: playwright with Chromium, pypdf, Pillow, network for Google Fonts.
"""

import base64
import html
import io
import json
import datetime
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).parent
TMP = HERE / "_tmp"
IMG = Path(r"D:\AccuKnox\help\docs\assets\images")
AK_DOCS = "https://help.accuknox.com"
E = html.escape
VAL = {"Y": 1.0, "P": 0.5, "N": 0.0}
RANK = {"Y": 2, "P": 1, "N": 0}


def _b64(path, max_w=None):
    im = Image.open(path).convert("RGBA")
    if max_w and im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG")
    return base64.b64encode(buf.getvalue()).decode()


LOGO_WHITE = _b64(IMG / "logo-white.png")
LOGO_DARK = _b64(IMG / "logo-black.png", 700)

S = {}
ROWS = []
SECTIONS = []
VENDORS = []
TOTAL = 0
NSEC = 0


def configure(spec):
    global S, ROWS, SECTIONS, VENDORS, TOTAL, NSEC
    S = spec
    SECTIONS = spec["sections"]
    ROWS = [r for s in SECTIONS for r in s["rows"]]
    VENDORS = spec["vendors"]
    TOTAL = len(ROWS)
    NSEC = len(SECTIONS)
    for r in ROWS:
        assert len(r["cells"]) == len(VENDORS), f"row {r['no']} has {len(r['cells'])} cells for {len(VENDORS)} vendors"


# ----------------------------------------------------------------------------- tokens
CSS = """
:root{
  --ink:#141b3a; --ink2:#363f63; --mute:#68708f; --line:#dde2f0; --hair:#e9ecf6;
  --navy:#11206D; --night:#0a1240; --blue:#0046FF; --wash:#eef2ff; --wash2:#f6f8ff;
  --yes:#117a47; --yesbg:#dff4e8; --part:#8a5800; --partbg:#fdf0cf; --no:#b3122a; --nobg:#fbe4e8;
  --d:'Inter','Segoe UI',Arial,sans-serif; --b:'Hanken Grotesk','Segoe UI',Arial,sans-serif;
}
*{box-sizing:border-box} html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:var(--b);color:var(--ink);font-size:9.6pt;line-height:1.42}
h1,h2,h3,h4{font-family:var(--d);margin:0;letter-spacing:-.012em}
a{color:var(--blue);text-decoration:none}
.chip{display:inline-flex;align-items:center;gap:5px;font:700 7.4pt/1 var(--b);padding:4px 8px 4px 7px;border-radius:99px;white-space:nowrap}
.chip::before{content:'';width:6px;height:6px;border-radius:50%;background:currentColor}
.chip.Y{background:var(--yesbg);color:var(--yes)} .chip.P{background:var(--partbg);color:var(--part)} .chip.N{background:var(--nobg);color:var(--no)}
.eyebrow{font:700 7.8pt/1 var(--b);letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
h2.big{font-size:21pt;line-height:1.08;color:var(--navy);margin:6px 0 4px}
.lede{color:var(--ink2);font-size:10.4pt;margin:0;max-width:150mm}
.board{margin:14px 0 8px;display:grid;gap:7px}
.bar-row{display:grid;grid-template-columns:24mm 1fr 52mm;gap:12px;align-items:center}
.bar-row .nm{font:700 11pt var(--d);color:var(--ink)} .bar-row.ak .nm{color:var(--navy)}
.bar{height:13px;border-radius:99px;background:#e6e9f5;display:flex;overflow:hidden} .bar-row.ak .bar{height:18px}
.bar i{display:block;height:100%} .bar .y{background:#1fa463} .bar .p{background:#f0b533}
.bar-row .ct{font-size:8.4pt;color:var(--mute);text-align:right} .bar-row .ct b{color:var(--ink)}
.legend{display:flex;gap:16px;align-items:center;font-size:8.4pt;color:var(--mute);margin:2px 0 0}
.legend span.t{margin-left:-8px}
h3.band{font-size:13pt;color:var(--navy);margin:20px 0 8px;padding-bottom:6px;border-bottom:1.5px solid var(--navy)}
.diff{display:grid;grid-template-columns:9mm 1fr 58mm;gap:4px 12px;padding:10px 0;border-bottom:1px solid var(--hair);break-inside:avoid;align-items:start}
.diff .no{font:700 11pt var(--d);color:var(--blue)}
.diff h4{font-size:11.2pt;color:var(--ink);margin:0 0 2px} .diff p{margin:0;color:var(--ink2);font-size:9pt;max-width:104mm}
.mini{display:grid;gap:4px;padding-top:3px}
.mini .r{display:flex;align-items:center;gap:6px;font-size:7.4pt;color:var(--mute)}
.mini .r b{width:17mm;font-weight:600;color:var(--ink2)}
.mini .cells{display:flex;gap:2px}
.cell{width:8px;height:12px;border-radius:2px;display:inline-block}
.cell.Y{background:#1fa463} .cell.P{background:#f0b533} .cell.N{background:#e3e6f1}
.strong{margin:16px 0 0;border:1px solid #f0d9a0;background:#fffaf0;border-radius:10px;padding:12px 16px;break-inside:avoid}
.strong h4{font-size:10.6pt;color:var(--part);margin-bottom:5px}
.strong ul{margin:0;padding-left:16px} .strong li{margin:3px 0;font-size:9pt;color:var(--ink2)} .strong li b{color:var(--ink)}
.sec-h{display:flex;align-items:center;gap:10px;margin:22px 0 7px;break-after:avoid}
.sec-h .L{width:8mm;height:8mm;border-radius:6px;background:var(--navy);color:#fff;font:700 11pt/8mm var(--d);text-align:center}
.sec-h h3{font-size:13.5pt;color:var(--navy);flex:1} .sec-h .n{font-size:8pt;color:var(--mute)}
table{width:100%;border-collapse:collapse;table-layout:fixed}
th{font:700 7.2pt/1 var(--b);letter-spacing:.1em;text-transform:uppercase;color:var(--mute);text-align:left;padding:7px 9px;border-bottom:1.5px solid var(--ink)}
th.ak{color:var(--navy);background:var(--wash)} th.v{text-align:center}
tr{break-inside:avoid}
td{padding:8px 9px;border-bottom:1px solid var(--hair);vertical-align:top}
td.cap{font-weight:700;color:var(--ink)} td.cap .n{display:block;font:600 7.4pt var(--b);color:#98a0bd;margin-bottom:1px;letter-spacing:.04em}
td.ak{background:var(--wash2)}
td .t{display:block;margin-top:5px;font-size:8.7pt;line-height:1.4;color:var(--ink2)} td .t a{color:inherit;text-decoration:underline;text-decoration-color:#b3bbdc;text-underline-offset:2px}
.sc td.ak{font-size:8.6pt;color:var(--ink2);vertical-align:middle} .sc td.v{text-align:center;vertical-align:middle}
.sc th.v{text-align:center}
.refs{font-size:7.8pt;color:var(--mute);margin:7px 0 0} .refs a{margin-right:11px}
.method{font-size:8.9pt;color:var(--ink2);margin:0;padding-left:16px} .method li{margin:4px 0} .method b{color:var(--ink)}
.src{columns:2;column-gap:26px;font-size:8.5pt;margin:0;padding:0;list-style:none} .src li{margin:0 0 5px;break-inside:avoid;word-break:break-word}
.src-h{font:700 9.4pt var(--d);color:var(--ink);margin:10px 0 5px}
.cta{margin-top:20px;border-radius:14px;background:linear-gradient(120deg,var(--night),var(--navy) 60%,#1e3fd6);color:#fff;padding:20px 24px;display:flex;align-items:center;justify-content:space-between;gap:24px;break-inside:avoid}
.cta h3{font-size:15pt;margin:0 0 4px} .cta p{margin:0;color:#d5dcff;font-size:9.4pt} .cta img{height:24px}
.cta b{color:#fff}
.cover{width:210mm;height:297mm;position:relative;overflow:hidden;color:#fff;
  background:radial-gradient(120mm 120mm at 92% 78%,rgba(0,70,255,.55),transparent 70%),radial-gradient(90mm 90mm at 0% 0%,rgba(66,110,255,.22),transparent 70%),linear-gradient(165deg,#0a1240 0%,#0d1a5c 55%,#11206D 100%)}
.cover .in{position:absolute;inset:0;padding:17mm 16mm 15mm;display:flex;flex-direction:column}
.cover .top{display:flex;justify-content:space-between;align-items:center}
.cover .top img{height:9mm}
.cover .tag{font:600 8pt var(--b);letter-spacing:.2em;text-transform:uppercase;color:#aebcff}
.cover .mid{margin-top:34mm}
.cover .kick{font:600 9pt var(--b);letter-spacing:.2em;text-transform:uppercase;color:#7fa2ff;margin-bottom:6mm}
.cover h1{font:700 66pt/0.98 var(--d);letter-spacing:-.035em;margin:0}
.cover h1 .vs{color:#7fa2ff;font-weight:500}
.cover h1.sc{font-size:56pt}
.cover .scope{margin-top:9mm;font-size:12.2pt;line-height:1.5;color:#d3dbff;max-width:128mm}
.cover .low{margin-top:auto}
.cover .say{font:500 14pt/1.4 var(--d);color:#fff;max-width:175mm;margin:0 0 9mm}
.cover .say b{color:#7fe3ac;font-weight:700}
.code{display:grid;gap:3mm}
.code .row{display:grid;grid-template-columns:24mm 1fr;align-items:center;gap:3mm}
.code .nm{font:600 8.6pt var(--b);color:#c7d1ff} .code .row.ak .nm{color:#fff;font-weight:700}
.code .strip{display:flex;gap:2.2mm}
.code .grp{display:flex;gap:.7mm;flex:1}
.code .k{flex:1;height:7mm;border-radius:1px}
.code .row.ak .k{height:11mm}
.code .k.Y{background:#3fdc95} .code .k.P{background:#f4bd4a} .code .k.N{background:transparent;box-shadow:inset 0 0 0 .5pt rgba(255,255,255,.28)}
.code .letters{display:grid;grid-template-columns:24mm 1fr;gap:3mm;margin-bottom:-.6mm}
.code .letters .strip{display:flex;gap:2.2mm} .code .letters span{font:600 6.4pt var(--b);color:#8fa0e8;letter-spacing:.08em}
.cleg{display:flex;white-space:nowrap;gap:5mm;margin:5mm 0 0 27mm;font:500 7.6pt var(--b);color:#aebcff;align-items:center}
.cleg i{display:inline-block;width:3mm;height:3mm;border-radius:1px;margin-right:1.6mm;vertical-align:-0.5mm}
.cover .foot{display:flex;justify-content:space-between;margin-top:9mm;padding-top:4.5mm;border-top:.5pt solid rgba(255,255,255,.22);font:500 8.2pt var(--b);color:#aebcff}
"""


# ---------------------------------------------------------------------------- helpers
def chip(st):
    return f'<span class="chip {st}">{ {"Y": "Yes", "P": "Partial", "N": "No"}[st] }</span>'


def counts(v):
    ys = sum(1 for r in ROWS if r["cells"][v]["st"] == "Y")
    ps = sum(1 for r in ROWS if r["cells"][v]["st"] == "P")
    return ys, ps, TOTAL - ys - ps


def tally(a, b):
    lead = par = trail = 0
    for r in ROWS:
        x, y = RANK[r["cells"][a]["st"]], RANK[r["cells"][b]["st"]]
        lead += x > y
        par += x == y
        trail += x < y
    return lead, par, trail


def letter_of(sec):
    return sec["name"].split(".")[0].strip()


def title_of(sec):
    return sec["name"].split(".", 1)[1].strip()


def html_doc(body, title, is_cover=False):
    return (
        f"<!doctype html><html><head><meta charset='utf-8'><title>{E(title)}</title>"
        "<link rel='preconnect' href='https://fonts.googleapis.com'>"
        "<link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap' rel='stylesheet'>"
        f"<style>{CSS}{'@page{size:A4;margin:0}' if is_cover else ''}</style></head><body>{body}</body></html>"
    )


# ------------------------------------------------------------------------------ cover
def barcode(vendors):
    out = ['<div class="code">']
    spans = "".join(f'<div class="grp" style="flex:{len(s["rows"])}"><span>{letter_of(s)}</span></div>' for s in SECTIONS)
    out.append(f'<div class="letters"><div></div><div class="strip">{spans}</div></div>')
    for v in vendors:
        groups = ""
        for s in SECTIONS:
            ks = "".join(f'<i class="k {r["cells"][v]["st"]}"></i>' for r in s["rows"])
            groups += f'<div class="grp" style="flex:{len(s["rows"])}">{ks}</div>'
        cls = "row ak" if v == 0 else "row"
        out.append(f'<div class="{cls}"><div class="nm">{E(VENDORS[v])}</div><div class="strip">{groups}</div></div>')
    out.append("</div>")
    out.append(
        '<div class="cleg"><span><i style="background:#3fdc95"></i>Documented in full</span>'
        '<span><i style="background:#f4bd4a"></i>Limited form</span>'
        '<span><i style="box-shadow:inset 0 0 0 .5pt rgba(255,255,255,.4)"></i>Not found in public docs</span>'
        '<span style="margin-left:auto">One mark per capability, areas A to ' + letter_of(SECTIONS[-1]) + "</span></div>"
    )
    return "".join(out)


def cover(job):
    if job["kind"] == "score":
        vs = job["vendors"]
        h1 = '<h1 class="sc">' + "<br>".join(E(x) for x in S["score_title"]) + "</h1>"
        scope, kick = S["scope_score"], S["kick_score"]
        rest = ", ".join(f"{VENDORS[i]} {counts(i)[0]}" for i in vs[1:])
        say = f"AccuKnox documents <b>{counts(0)[0]} of {TOTAL}</b> capabilities in full. {rest}."
        code = barcode(vs)
    else:
        v = job["vendor"]
        name = VENDORS[v]
        h1 = f'<h1>AccuKnox<br><span class="vs">vs</span> {E(name)}</h1>'
        scope, kick = S["scope_vs"].format(name=name), S["kick_vs"]
        say = f"AccuKnox documents <b>{counts(0)[0]} of {TOTAL}</b> capabilities in full. {E(name)} documents {counts(v)[0]}."
        code = barcode([0, v])
    return (
        f'<div class="cover"><div class="in">'
        f'<div class="top"><img src="data:image/png;base64,{LOGO_WHITE}" alt="AccuKnox"><div class="tag">{E(S["tag"])}</div></div>'
        f'<div class="mid"><div class="kick">{E(kick)}</div>{h1}<p class="scope">{E(scope)}</p></div>'
        f'<div class="low"><p class="say">{say}</p>{code}'
        f'<div class="foot"><span>{TOTAL} capabilities · {NSEC} areas</span><span>{E(S["date"])}</span><span>accuknox.com</span></div></div>'
        "</div></div>"
    )


# ------------------------------------------------------------------------------- body
def board(vendors):
    out = ['<div class="board">']
    for v in vendors:
        ys, ps, ns = counts(v)
        cls = "bar-row ak" if v == 0 else "bar-row"
        out.append(
            f'<div class="{cls}"><div class="nm">{E(VENDORS[v])}</div>'
            f'<div class="bar"><i class="y" style="width:{ys / TOTAL * 100:.1f}%"></i><i class="p" style="width:{ps / TOTAL * 100:.1f}%"></i></div>'
            f'<div class="ct"><b>{ys} full</b> · {ps} partial · {ns} none</div></div>'
        )
    out.append("</div>")
    return "".join(out)


def legend():
    return f'<div class="legend">{chip("Y")}<span class="t">Confirmed capability</span>{chip("P")}<span class="t">Available in a limited form</span>{chip("N")}<span class="t">Not found in public documentation</span></div>'


def minirows(nos, vendors):
    rs = [r for r in ROWS if r["no"] in nos]
    out = ['<div class="mini">']
    for v in vendors:
        cells = "".join(f'<i class="cell {r["cells"][v]["st"]}"></i>' for r in rs)
        out.append(f'<div class="r"><b>{E(VENDORS[v])}</b><span class="cells">{cells}</span></div>')
    out.append("</div>")
    return "".join(out)


def diff_rows(vendors):
    out = []
    for i, (title, body, nos) in enumerate(S["themes"], 1):
        out.append(
            f'<div class="diff"><div class="no">0{i}</div><div><h4>{E(title)}</h4><p>{E(body)}</p></div>'
            f"{minirows(nos, vendors)}</div>"
        )
    return "".join(out)


def ak_refs(letter):
    refs = S.get("ak_refs", {}).get(letter, [])
    links = "".join(f'<a href="{AK_DOCS}{p}">{E(n)}</a>' for n, p in refs)
    return f'<div class="refs">AccuKnox docs: {links}</div>' if refs else ""


def sec_head(sec):
    return (
        f'<div class="sec-h"><div class="L">{letter_of(sec)}</div><h3>{E(title_of(sec))}</h3>'
        f'<span class="n">{len(sec["rows"])} capabilities</span></div>'
    )


def method_and_sources(vs, extra=""):
    srcs = ""
    for v in vs:
        if v not in S["sources"]:
            continue
        name, links = S["sources"][v]
        li = "".join(f'<li><a href="{E(u)}">{E(n)}</a></li>' for n, u in links)
        srcs += f'<div class="src-h">{E(name)}</div><ul class="src">{li}</ul>'
    return (
        '<h3 class="band">How we scored</h3><ul class="method">'
        "<li><b>Yes</b> means the vendor documents the capability. <b>Partial</b> means it exists in a limited form. <b>No</b> means we found no native capability in public documentation.</li>"
        f"<li>AccuKnox ratings come from help.accuknox.com. Competitor ratings come from the vendors' own documentation and product pages, listed below. Reviewed {E(S['date'])}.</li>"
        "<li>Vendors ship changes often. If a rating no longer matches your version of a product, tell us and we will update it.</li>"
        f"{extra}</ul>"
        f'<h3 class="band">Competitor sources</h3>{srcs}'
    )


def cta(competitor=None):
    line = (
        f"Run AccuKnox next to {competitor} on your own code, clusters and registries."
        if competitor
        else "Run AccuKnox on your own code, clusters and registries."
    )
    return (
        f'<div class="cta"><div><h3>See it on your stack</h3><p>{line} Book a demo at <b>accuknox.com</b>. '
        f"Product documentation lives at <b>help.accuknox.com</b>.</p></div>"
        f'<img src="data:image/png;base64,{LOGO_WHITE}" alt="AccuKnox"></div>'
    )


def body_score(job):
    vs = job["vendors"]
    b = [
        '<div class="eyebrow">Summary</div><h2 class="big">Capability coverage at a glance</h2>'
        f'<p class="lede">Full, partial and missing capabilities out of {TOTAL}, by vendor.</p>'
        f"{board(vs)}{legend()}"
        '<h3 class="band">Where the gap is widest</h3>' + diff_rows(vs)
        + f'<div class="strong"><h4>Where AccuKnox is partial</h4><ul>{S["score_note"]}</ul></div>'
    ]
    n = len(vs)
    vw = {4: 12, 3: 15, 2: 18}.get(n, 12)
    capw = 24 if n == 4 else 28
    detw = 100 - capw - vw * n
    for sec in SECTIONS:
        rows = []
        for r in sec["rows"]:
            c = r["cells"]
            rows.append(
                f'<tr><td class="cap"><span class="n">{r["no"]:02d}</span>{E(r["name"])}</td><td class="ak">{E(r["short"])}</td>'
                + "".join(f'<td class="v">{chip(c[i]["st"])}</td>' for i in vs)
                + "</tr>"
            )
        cols = f'<col style="width:{capw}%"><col style="width:{detw}%">' + f'<col style="width:{vw}%">' * n
        heads = '<th class="v ak">AccuKnox</th>' + "".join(f'<th class="v">{E(VENDORS[i])}</th>' for i in vs[1:])
        b.append(
            sec_head(sec)
            + f'<table class="sc"><colgroup>{cols}</colgroup><thead><tr><th>Capability</th><th class="ak">AccuKnox detail</th>{heads}</tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>{ak_refs(letter_of(sec))}'
        )
    b.append(method_and_sources(vs[1:], S.get("score_method_extra", "")) + cta())
    return "".join(b)


def body_versus(job):
    v = job["vendor"]
    name = VENDORS[v]
    lead, par, trail = tally(0, v)
    strengths = "".join(f"<li><b>{E(a)}</b> {E(b)}</li>" for a, b in S["strengths"][v])
    b = [
        f'<div class="eyebrow">Summary</div><h2 class="big">{TOTAL} capabilities compared</h2>'
        f'<p class="lede">AccuKnox leads on {lead} rows, matches {E(name)} on {par} and trails on {trail}.</p>'
        f"{board([0, v])}{legend()}"
        f'<h3 class="band">Where AccuKnox is different</h3>{diff_rows([0, v])}'
        f'<div class="strong"><h4>Where {E(name)} is strong</h4><ul>{strengths}</ul></div>'
    ]
    for sec in SECTIONS:
        rows = []
        for r in sec["rows"]:
            a, c = r["cells"][0], r["cells"][v]
            ctxt = E(c["text"])
            if c.get("src"):
                ctxt = f'<a href="{E(c["src"])}">{ctxt}</a>'
            rows.append(
                f'<tr><td class="cap"><span class="n">{r["no"]:02d}</span>{E(r["name"])}</td>'
                f'<td class="ak">{chip(a["st"])}<span class="t">{E(a["text"])}</span></td>'
                f'<td>{chip(c["st"])}<span class="t">{ctxt}</span></td></tr>'
            )
        b.append(
            sec_head(sec)
            + '<table><colgroup><col style="width:22%"><col style="width:41%"><col style="width:37%"></colgroup>'
            f'<thead><tr><th>Capability</th><th class="ak">AccuKnox</th><th>{E(name)}</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>{ak_refs(letter_of(sec))}'
        )
    b.append(method_and_sources((v,)) + cta(name))
    return "".join(b)


def _render(browser, html_str, out_pdf, *, margins, header=None, footer=None):
    f = TMP / (out_pdf.stem + ".html")
    f.write_text(html_str, encoding="utf-8")
    pg = browser.new_page()
    pg.goto(f.as_uri(), wait_until="networkidle")
    pg.evaluate("document.fonts.ready")
    kw = dict(path=str(out_pdf), format="A4", print_background=True, margin=margins)
    if header or footer:
        kw.update(display_header_footer=True, header_template=header or "<div></div>", footer_template=footer or "<div></div>")
    else:
        kw.update(prefer_css_page_size=True)
    pg.pdf(**kw)
    pg.close()


def build(spec, only=None):
    """Build every job in spec['jobs'] (or just the ones whose file name is in `only`)."""
    configure(spec)
    PDF_DIR = Path(spec["out_dir"])
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    TMP.mkdir(exist_ok=True)
    built = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for job in spec["jobs"]:
            if only and job["file"] not in only:
                continue
            title, fname = job["title"], job["file"]
            cpdf, bpdf = TMP / f"{fname}-cover.pdf", TMP / f"{fname}-body.pdf"
            _render(browser, html_doc(cover(job), title, True), cpdf, margins=dict(top="0", right="0", bottom="0", left="0"))
            header = (
                "<div style=\"width:100%;padding:0 10mm;display:flex;justify-content:space-between;align-items:center;"
                "font-family:'Hanken Grotesk','Segoe UI',Arial,sans-serif;font-size:7.4pt;color:#68708f\">"
                f'<img style="height:3.6mm" src="data:image/png;base64,{LOGO_DARK}"><span>{E(title)}</span></div>'
            )
            footer = (
                "<div style=\"width:100%;padding:0 10mm;text-align:right;font-family:'Hanken Grotesk','Segoe UI',Arial,sans-serif;"
                "font-size:7.4pt;color:#68708f\"><span class='pageNumber'></span> / <span class='totalPages'></span></div>"
            )
            body = body_score(job) if job["kind"] == "score" else body_versus(job)
            _render(browser, html_doc(body, title), bpdf, margins=dict(top="19mm", right="10mm", bottom="14mm", left="10mm"), header=header, footer=footer)
            w = PdfWriter()
            for part in (cpdf, bpdf):
                for page in PdfReader(str(part)).pages:
                    w.add_page(page)
            w.add_metadata({"/Title": title, "/Author": "AccuKnox"})
            out = PDF_DIR / f"{fname}.pdf"
            with open(out, "wb") as fh:
                w.write(fh)
            vend = job["vendors"] if job["kind"] == "score" else [0, job["vendor"]]
            meta = {
                "title": title,
                "file": f"{fname}.pdf",
                "kind": job["kind"],
                "vendors": [VENDORS[i] for i in vend],
                "category": spec.get("category", ""),
                "capabilities": TOTAL,
                "pages": len(w.pages),
                "built": datetime.date.today().isoformat(),
                "sheet_url": spec.get("sheet_url", ""),
            }
            (PDF_DIR / f"{fname}.meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
            built.append(meta)
            print("built", fname, len(w.pages), "pages")
        browser.close()
    for f in TMP.glob("*"):
        f.unlink()
    TMP.rmdir()
    return built
