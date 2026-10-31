"""Build the AccuKnox-centric AI Security Stack Ranking for the KuppingerCole vendor set.

Reads vendors_kc/*.json (v3 schema, see ../ai-stack-ranking-v3/FRAMEWORK.md and BENCHMARK.md)
and renders a landscape PDF with Playwright: cover, ranking table, module evidence, sources.

Usage: python build.py [output.pdf]
"""
import base64
import glob
import html
import json
import os
import sys
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "ai-security-stack-ranking-kuppingercole-oct-2026.pdf")
LOGO = os.path.join(HERE, "..", "ai-matrix-panw-crwd-varonis", "assets", "accuknox-logo-light-bg.png")
AS_OF = "October 2026"

MODULES = [
    ("1", "AI-SPM", "AI inventory, shadow AI, pipeline posture"),
    ("2", "Agentic AI Security", "Managed agents, MCP, agent sandbox"),
    ("3", "AI-DR", "Detect, respond, block at runtime"),
    ("4", "Prompt Guardrails &amp; AI Gateway", "Inline firewall, injection and PII, unsafe output"),
    ("5", "Compliance and AI-GRC", "AIBOM, framework mapping, audit trail"),
    ("6", "Red Team + AI DAST", "Attack library, live multi-turn attacks, CI/CD"),
    ("7", "AI &amp; Agent Identity Security", "Agent identity, least privilege, NHI"),
    ("8", "Model, Dataset + AI-SAST", "Model files, datasets, AI code scanning"),
]
WORD = {"yes": "Supported", "partial": "Partial", "no": "No evidence"}
VAL = {"yes": 1.0, "partial": 0.5, "no": 0.0}
DOMAIN = {
    "accuknox": "accuknox.com", "cisco": "cisco.com", "microsoft": "microsoft.com", "f5": "f5.com",
    "cequence": "cequence.ai", "radware": "radware.com", "a10-networks": "a10networks.com",
    "nsfocus": "nsfocusglobal.com", "skyhigh-security": "skyhighsecurity.com", "forcepoint": "forcepoint.com",
    "plainid": "plainid.com", "unosecur": "unosecur.com", "adversa-ai": "adversa.ai",
    "midships": "midships.io", "check-point": "checkpoint.com", "palo-alto-networks": "paloaltonetworks.com",
    "crowdstrike": "crowdstrike.com", "varonis": "varonis.com", "neuraltrust": "neuraltrust.ai",
    "straiker": "straiker.ai", "zenity": "zenity.io",
}


def favurl(d):
    dom = DOMAIN.get(d["slug"]) or urlparse(d.get("website", "")).netloc.replace("www.", "")
    if d["slug"] == "palo-alto-networks":
        return "https://icons.duckduckgo.com/ip3/paloaltonetworks.com.ico"
    return f"https://www.google.com/s2/favicons?domain={dom}&sz=128"


def esc(s):
    return html.escape(s or "", quote=False)


def load():
    rows = [json.load(open(p, encoding="utf-8")) for p in glob.glob(os.path.join(HERE, "vendors_kc", "*.json"))]
    for d in rows:
        d["score"] = sum(VAL[d["modules"][m[0]]["status"]] for m in MODULES)
    ak = [d for d in rows if d["slug"] == "accuknox"][0]
    rest = sorted([d for d in rows if d["slug"] != "accuknox"], key=lambda d: (-d["score"], d["vendor"].lower()))
    ordered = [ak] + rest
    rank, prev, pos = {}, None, 0
    for i, d in enumerate(ordered, 1):
        if d["score"] != prev:
            pos, prev = i, d["score"]
        rank[d["slug"]] = pos
    return ordered, rank


def icon(d, size=26):
    if d["slug"] == "accuknox":
        b64 = base64.b64encode(open(LOGO, "rb").read()).decode()
        return f'<img class="aklogo" src="data:image/png;base64,{b64}">'
    return (f'<img class="fav" width="{size}" height="{size}" '
            f'src="{favurl(d)}" alt="">'
            f'<span class="vname">{esc(d["vendor"])}</span>')


def chip(m):
    s = m["status"]
    beta = '<span class="beta">BETA</span>' if m.get("beta") else ""
    return f'<span class="chip {s}"><i></i>{WORD[s]}</span>{beta}'


def short(d):
    return d["vendor"]


CSS = """
@page { size: 1434pt 842pt; margin: 0 }
* { box-sizing: border-box; margin: 0; padding: 0 }
body { font-family: 'Inter', Arial, sans-serif; color: #1f2937; -webkit-print-color-adjust: exact; print-color-adjust: exact }
.page { width: 1912px; height: 1123px; position: relative; overflow: hidden; page-break-after: always; background: #fff }
.bar { background: #11206D; color: #fff; text-align: center; font-size: 30px; font-weight: 700; height: 66px; line-height: 66px }
.foot { position: absolute; left: 40px; right: 40px; bottom: 18px; display: flex; justify-content: space-between; align-items: center; font-size: 12px; color: #6b7280 }
.foot img { height: 18px }
.cover { background: radial-gradient(900px 500px at 100% 0, #fde4e4 0, transparent 60%), radial-gradient(900px 600px at 0 100%, #e6edff 0, transparent 60%), #fbfcff }
.cover .brand { position: absolute; left: 74px; top: 52px } .cover .brand img { height: 46px }
.cover .tag { position: absolute; right: 74px; top: 70px; font-size: 13px; letter-spacing: .18em; color: #4b5563; font-weight: 600 }
.cover .head { position: absolute; left: 74px; top: 160px; width: 860px; border-left: 5px solid #5b2fd0; padding-left: 34px; border-image: linear-gradient(#e11d48, #5b2fd0) 1 }
.cover h1 { font-size: 80px; line-height: 1.02; color: #1b2fbf; font-weight: 800; letter-spacing: -.02em }
.cover p.lede { margin-top: 28px; font-size: 20px; line-height: 1.55; color: #374151; width: 720px }
.stats { display: flex; gap: 56px; margin-top: 34px } .stats b { display: block; font-size: 34px; color: #11206D } .stats span { font-size: 12px; letter-spacing: .08em; color: #4b5563; font-weight: 600 }
.vbox { position: absolute; right: 74px; top: 130px; width: 880px; background: #fff; border: 1px solid #e5e7eb; border-radius: 18px; padding: 24px 24px 20px; box-shadow: 0 8px 30px rgba(17,32,109,.08) }
.vbox h3 { font-size: 19px; color: #11206D; display: flex; justify-content: space-between; align-items: baseline } .vbox h3 small { font-size: 13px; color: #6b7280; font-weight: 500 }
.vgrid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-top: 16px }
.vcell { border: 1px solid #e5e7eb; border-radius: 10px; height: 66px; display: flex; align-items: center; justify-content: center; gap: 8px; padding: 0 8px; font-weight: 700; font-size: 17px; color: #111827; text-align: center; line-height: 1.1 }
.vcell .fav { border-radius: 5px; flex: none } .vcell.ak { border-color: #1b2fbf; background: #eef2ff }
.offer { position: absolute; left: 74px; right: 74px; bottom: 74px }
.offer h4 { font-size: 22px; color: #11206D; margin-bottom: 14px } .offer h4 small { font-size: 13px; color: #6b7280; font-weight: 400; margin-left: 12px }
.ocols { display: grid; grid-template-columns: 1fr 2.5fr; gap: 24px }
.ocard { background: #fff; border: 1px solid #e5e7eb; border-radius: 16px; padding: 22px 26px }
.ocard h5 { font-size: 18px; color: #11206D; margin-bottom: 14px; display: flex; align-items: center; gap: 10px } .ocard h5 b { background: #11206D; color: #fff; font-size: 11px; padding: 3px 7px; border-radius: 5px }
.ocard ul { list-style: none; display: grid; gap: 11px 40px; font-size: 14px } .ocard.two ul { grid-template-columns: repeat(3, 1fr) } .ocard li::before { content: ''; display: inline-block; width: 8px; height: 8px; border-radius: 3px; background: #4f6bff; margin-right: 12px }
.body { padding: 22px 28px 0 }
table { border-collapse: separate; border-spacing: 4px; width: 100% }
th { background: #dbe8ff; padding: 7px 10px; font-size: 12px; text-align: left; vertical-align: middle; border-radius: 6px; color: #11206D }
th small { display: block; font-weight: 400; color: #475569; font-size: 10px; margin-top: 2px } th .n { display: inline-block; background: #11206D; color: #fff; width: 18px; text-align: center; border-radius: 4px; margin-right: 6px; font-size: 11px }
td { background: #eef1f6; padding: 0 10px; border-radius: 6px; font-size: 13px; vertical-align: middle }
tr.ak td { background: #fff; border: 2px solid #1b2fbf }
.rank { text-align: center; font-weight: 700; width: 56px } .vend { width: 250px } .vend .fav { vertical-align: middle; border-radius: 5px; margin-right: 8px } .vend .vname { font-weight: 700; font-size: 17px; vertical-align: middle; color: #111827 } .aklogo { height: 26px; vertical-align: middle }
.score { width: 130px; font-weight: 700 } .score i { display: inline-block; width: 52px; height: 6px; background: #d1d5db; border-radius: 4px; vertical-align: middle; margin-left: 8px; position: relative } .score i b { position: absolute; left: 0; top: 0; bottom: 0; background: #11206D; border-radius: 4px }
.chip { font-weight: 600; font-size: 12.5px; display: inline-flex; align-items: center; gap: 6px } .chip i { width: 14px; height: 14px; border-radius: 50%; display: inline-block }
.chip.yes { color: #137333 } .chip.yes i { background: #16a34a } .chip.partial { color: #9a6700 } .chip.partial i { background: #f59e0b } .chip.no { color: #b3261e } .chip.no i { background: #dc2626 }
.beta { font-size: 9px; font-weight: 700; color: #1b2fbf; background: #dbe4ff; border-radius: 4px; padding: 1px 5px; margin-left: 6px; letter-spacing: .05em }
.legend { margin: 10px 4px 0; border: 1px solid #e5e7eb; border-radius: 8px; padding: 10px 16px; font-size: 12px; color: #475569; display: flex; gap: 28px; align-items: center } .legend .chip { font-size: 12px; white-space: nowrap } .legend { flex-wrap: nowrap; white-space: nowrap }
.evt td { vertical-align: top; padding: 9px 10px; font-size: 12px; line-height: 1.35 } .evt .chip { margin-bottom: 4px } .evt b { color: #111827 } .evt .lk { color: #6b7280 }
.evt .vend { padding-top: 12px } .evt .vend .meta { font-size: 11.5px; color: #4b5563; margin-top: 6px; line-height: 1.35 } .evt .vend .pill { display: inline-block; background: #11206D; color: #fff; font-size: 10.5px; padding: 2px 7px; border-radius: 5px; margin-top: 6px; font-weight: 700 }
h2.sec { font-size: 24px; color: #11206D; margin: 8px 6px 10px } h2.sec small { font-size: 13px; color: #6b7280; font-weight: 400; margin-left: 12px }
.src td { font-size: 10.5px; padding: 6px 8px; word-break: break-all; line-height: 1.25 } .src a { color: #1b2fbf; text-decoration: none }
.method { margin: 6px 8px 0; font-size: 12.5px; color: #374151; line-height: 1.5 }
"""


def cover(vendors):
    cells = "".join(
        f'<div class="vcell"><img class="fav" width="28" height="28" src="{favurl(d)}" alt="">{esc(d["vendor"])}</div>'
        for d in sorted(vendors[1:], key=lambda d: d["vendor"].lower()))
    b64 = base64.b64encode(open(LOGO, "rb").read()).decode()
    n = len(vendors) - 1
    ak = vendors[0]
    ofs = ["AI SAST", "AI DAST", "AgentZ", "AI pentesting"]
    sfa = ["Shadow AI", "Cloud AI", "On-prem AI", "Managed agents", "Prompt Firewall", "AI Gateway",
           "Agent sandbox", "Model security", "AI BOM", "Red teaming", "Guardrails", "AIDR"]
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    return f"""<section class="page cover">
<div class="brand"><img src="data:image/png;base64,{b64}"></div>
<div class="tag">AI SECURITY &nbsp;|&nbsp; COMPETITIVE ANALYSIS &nbsp;|&nbsp; 2026</div>
<div class="head"><h1>AI Security<br>Stack Ranking</h1>
<p class="lede">AccuKnox against the {n} other vendors plotted in the KuppingerCole AI security Leadership Compass,
scored on public evidence across 8 modules. From AI-SPM and agentic AI security to runtime detection, guardrails, red teaming and identity.</p>
<div class="stats"><div><b>{n}</b><span>VENDORS COMPARED</span></div><div><b>8</b><span>SECURITY MODULES</span></div>
<div><b>{ak['score']:g} / 8</b><span>ACCUKNOX SCORE</span></div></div></div>
<div class="vbox"><h3>Vendors compared<small>{n} vendors, A to Z</small></h3><div class="vgrid">{cells}</div></div>
<div class="offer"><h4>The AccuKnox AI Security offering<small>One zero trust platform for AI for Security and Security for AI</small></h4>
<div class="ocols"><div class="ocard"><h5><b>01</b> AI for Security</h5><ul>{li(ofs)}</ul></div>
<div class="ocard two"><h5><b>02</b> Security for AI</h5><ul>{li(sfa)}</ul></div></div></div>
</section>"""


def head_cells():
    return "".join(f'<th><span class="n">{n}</span>{t}<small>{s}</small></th>' for n, t, s in MODULES)


def foot(i, total):
    b64 = base64.b64encode(open(LOGO, "rb").read()).decode()
    return f'<div class="foot"><img src="data:image/png;base64,{b64}"><span>{i} / {total}</span></div>'


def ranking(vendors, rank, total):
    rows = []
    for d in vendors:
        cls = "ak" if d["slug"] == "accuknox" else ""
        cells = "".join(f"<td>{chip(d['modules'][m[0]])}</td>" for m in MODULES)
        pct = d["score"] / 8 * 100
        rows.append(f'<tr class="{cls}" style="height:36px"><td class="rank">{rank[d["slug"]]}</td><td class="vend">{icon(d)}</td>'
                    f'<td class="score">{d["score"]:g}<i><b style="width:{pct:.0f}%"></b></i></td>{cells}</tr>')
    legend = ('<div class="legend"><span class="chip yes"><i></i>Supported</span> matches the AccuKnox benchmark on all 3 parts of the module '
              '<span class="chip partial"><i></i>Partial</span> has part of it '
              '<span class="chip no"><i></i>No evidence</span> none found after two or more searches '
              '<span class="beta">BETA</span> upcoming AccuKnox feature, the mark rests on GA features '
              '<span style="margin-left:auto">Score of 8: Supported 1, Partial 0.5, No evidence 0. Ties share a rank.</span></div>')
    return f"""<section class="page"><div class="bar">AI Security Stack Ranking: KuppingerCole Vendors</div><div class="body">
<table><tr><th style="text-align:center">Rank</th><th>Vendor</th><th style="text-align:center">Score<small>of 8</small></th>{head_cells()}</tr>
{''.join(rows)}</table>{legend}</div>{foot(2, total)}</section>"""


def cell_ev(m):
    has = esc(m.get("has", ""))
    lacks = esc(m.get("lacks", ""))
    out = f'<div>{chip(m)}</div>'
    if has:
        out += f"<div><b>Has:</b> {has}</div>"
    if lacks:
        out += f"<div><b>Lacks:</b> {lacks}</div>"
    if not has and not lacks:
        out += "<div><b>Lacks:</b> No public evidence found.</div>"
    return f"<td>{out}</td>"


def evidence(chunk, rank, page_no, total, first, last, n):
    rows = []
    for d in chunk:
        cls = "ak" if d["slug"] == "accuknox" else ""
        cells = "".join(cell_ev(d["modules"][m[0]]) for m in MODULES)
        meta = esc(d.get("what_it_is", ""))
        rows.append(f'<tr class="{cls}"><td class="vend">{icon(d, 24)}<div><span class="pill">#{rank[d["slug"]]} &nbsp; {d["score"]:g} / 8</span></div>'
                    f'<div class="meta">{meta}</div></td>{cells}</tr>')
    return f"""<section class="page"><div class="bar">AI Security Stack Ranking: KuppingerCole Vendors</div><div class="body">
<h2 class="sec">Module evidence by vendor<small>What each vendor has, and lacks, against the AccuKnox benchmark. Vendors {first} to {last} of {n}, ordered by rank.</small></h2>
<table class="evt"><tr><th class="vend">Vendor</th>{head_cells()}</tr>{''.join(rows)}</table></div>{foot(page_no, total)}</section>"""


def sources(vendors, total, page_no, last_page):
    def link(m):
        u = m.get("url", "")
        if not u:
            return "<td></td>"
        p = urlparse(u)
        label = (p.netloc.replace("www.", "") + p.path).rstrip("/")
        label = label if len(label) <= 52 else label[:51] + "…"
        return f'<td><a href="{esc(u)}">{esc(label)}</a></td>'
    rows = "".join(f'<tr><td class="vend">{icon(d, 20)}</td>' + "".join(link(d["modules"][m[0]]) for m in MODULES) + "</tr>" for d in vendors)
    note = ("""<p class="method"><b>How we scored.</b> Each module has three parts. Supported means the vendor matches the AccuKnox benchmark on all three, shown on the vendor's own site or docs.
Partial means it covers part of the module, or ships it in beta or preview. No evidence means two or more targeted searches and a look at the product pages found nothing public.
Vendor list taken from the KuppingerCole AI security Leadership Compass chart. Scores reflect public documentation only, read October 2026.</p>""" if last_page else "")
    return f"""<section class="page"><div class="bar">AI Security Stack Ranking: KuppingerCole Vendors</div><div class="body">
<h2 class="sec">Source links<small>One public page per vendor and module, same columns as the ranking. Read {AS_OF}.</small></h2>
<table class="src"><tr><th class="vend">Vendor</th>{head_cells()}</tr>{rows}</table>
{note}</div>{foot(page_no, total)}</section>"""


def main():
    from playwright.sync_api import sync_playwright
    vendors, rank = load()
    n = len(vendors)
    sizes = [4, 4, 4, 4, 5]
    chunks, at = [], 0
    for z in sizes:
        chunks.append(vendors[at:at + z])
        at += z
    src_chunks = [vendors[:11], vendors[11:]]
    total = 2 + len(chunks) + len(src_chunks)
    pages = [cover(vendors), ranking(vendors, rank, total)]
    for i, ch in enumerate(chunks):
        pages.append(evidence(ch, rank, 3 + i, total, sum(sizes[:i]) + 1, sum(sizes[:i]) + len(ch), n))
    for k, sc in enumerate(src_chunks):
        pages.append(sources(sc, total, 3 + len(chunks) + k, k == len(src_chunks) - 1))
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" '
           f'href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">'
           f'<style>{CSS}</style></head><body>{"".join(pages)}</body></html>')
    tmp = os.path.join(HERE, "_build.html")
    open(tmp, "w", encoding="utf-8").write(doc)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file:///" + tmp.replace("\\", "/"), wait_until="networkidle")
        pg.pdf(path=OUT, width="1912px", height="1123px", print_background=True)
        b.close()
    os.remove(tmp)
    print("wrote", OUT, "vendors", n)


if __name__ == "__main__":
    main()
