"""Build the AccuKnox vs Orca Security (CNAPP, Jubilee Insurance) battlecard PDF.

Reference implementation for the PDF output mode of the accuknox-comparison-writer
skill. Copy this folder for a new competitor, then edit the row lists and the
PICK strip. Layout rules live in
.claude/skills/accuknox-comparison-writer/references/battlecard-pdf.md.

Run from the repo root:
    python references/competitive/battlecards/orca-jubilee/battlecard/build_battlecard.py [out.pdf]

Needs playwright (with chromium) and pypdf. The cover and the table pages render
from HTML. The AccuKnox back page is appended from assets/back-page.pdf.
"""
import base64
import pathlib
import sys
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = pathlib.Path(__file__).resolve().parent
A = HERE / "assets"
BUILD = HERE / "build"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else BUILD / "accuknox-vs-orca-security-jubilee.pdf"


def b64(name):
    data = (A / name).read_bytes()
    return "data:image/png;base64," + base64.b64encode(data).decode()


def si(name, color):
    svg = (A / f"si_{name}.svg").read_text(encoding="utf-8")
    return svg.replace("<svg ", f'<svg class="brand" fill="#{color}" ', 1)


BRANDS = {
    "openai": si("openai", "000000"),
    "claude": si("claude", "D97757"),
    "gemini": si("googlegemini", "8E75B2"),
    "copilot": si("githubcopilot", "000000"),
    "nvidia": si("nvidia", "76B900"),
    "k8s": si("kubernetes", "326CE5"),
}

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
}


def ic(name, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{I[name]}</svg>'


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


CHIP["lead"] = ("c-win", "check", "AccuKnox leads")
CHIP["orca"] = ("c-neu", "check", "Supported")
CHIP["lim2"] = ("c-next", "check", "Next release")
CHIP["par"] = ("c-par", "equal", "Parity")


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def row(icon, cap, ak_k, ak, ns_k, ns, tk):
    return f"""<tr>
<td class="cap"><div class="capw">{ic(icon, 'capi')}<span>{cap}</span></div></td>
<td class="ak {ak_k}">{chip(ak_k)}{ul(ak)}</td>
<td class="ns {ns_k}">{chip(ns_k)}{ul(ns)}</td>
<td class="tk">{tk}</td></tr>"""


G1 = [
    row("shield", "Runtime workload protection", "lead",
        ["eBPF + LSM kernel enforcement", "<b>Blocks the action</b> before it completes", "Keeps enforcing if the control plane drops"],
        "lim", ["Sensor detects with eBPF", "Can terminate processes"],
        "Blocks before the action completes"),
    row("bot", "AI security", "lead",
        ["<b>Prompt Firewall</b> blocks injection inline", "ModelArmor sandboxes agents", "Model file scans, CycloneDX AI BOM"],
        "lim", ["AI-SPM inventory, 50+ AI packages", "Detects injection, inline block not shown"],
        "Enforces policy beyond AI inventory"),
    row("code", "Application security", "lead",
        ["SAST, <b>DAST</b>, secrets, IaC, SBOM", "CI/CD pipeline scanning"],
        "lim", ["SCA, SAST, secrets, IaC, images", "No DAST on its AppSec page"],
        "Tests the running app too"),
    row("globe", "Hosting regions and residency", "lead",
        ["<b>US, Europe, Middle East, India</b>", "Hard isolation option", "On-prem and air-gapped available"],
        "lim", ["Docs portal lists 7 regions", "No Middle East or Africa region listed"],
        "Host in the region you choose"),
    row("box", "Kubernetes and containers", "par",
        ["KSPM, in-cluster image scans", "RBAC analysis, KnoxGuard admission"],
        "par", ["Agentless image and registry checks", "Guardrails block insecure deploys"],
        "Admission control plus runtime enforcement"),
    row("list", "Policy setup effort", "par",
        ["Learns each workload baseline", "Drafts least-permissive policy", "Audit mode 2 to 3 weeks first"],
        "par", ["Thousands of alert templates", "Query builder, natural language"],
        "Policies drafted from observed behavior"),
]

G2 = [
    row("layers", "Unified platform", "par",
        ["CSPM, CWPP, KSPM, ASPM, AI, CDR", "One policy engine, one schema"],
        "par", ["CSPM, CWPP, CIEM, DSPM together"],
        "No stack of point tools"),
    row("cloud", "Cloud coverage", "par",
        ["AWS, Azure, GCP, OCI", "One console"],
        "par", ["AWS, Azure, GCP, OCI, Alibaba"],
        "Jubilee's three clouds covered"),
    row("pulse", "Cloud posture onboarding", "par",
        ["Agentless, read-only roles", "1 account, 1 role, about 2 hours"],
        "par", ["SideScanning, no agents", "Deploys in minutes, per Orca"],
        "Both start without agents"),
    row("monitor", "Compliance reporting", "par",
        ["40+ frameworks, control-level mapping", "CIS, NIST 800-53, ISO 27001, PCI DSS", "Scheduled, versioned reports"],
        "par", ["150+ frameworks, custom frameworks", "CSV, JSON, PDF reports"],
        "All four named frameworks covered"),
    row("target", "Identity and entitlements (CIEM)", "lim2",
        ["Identities on AWS, Azure, GCP, OCI", "Human and machine identity tags", "Policies, risk classes, access graph"],
        "orca", ["Policy optimizer, 90-day usage", "Just-in-time access for AWS"],
        "Closes in the next release"),
    row("filescan", "Data security (DSPM)", "lim2",
        ["<b>Scanner runs in your region</b>", "Only a findings file leaves", "OCR on images"],
        "orca", ["Cloud-wide data discovery", "Shadow data, OCR"],
        "Data stays in the region you pick"),
]

THEAD = f"""<colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"></colgroup>
<thead><tr><th class="h-cap">Capability</th><th class="h-ak"><img src="{b64('accuknox-logo.png')}"></th>
<th class="h-ns"><img src="{b64('orca-logo.png')}"></th><th class="h-tk">Takeaway</th></tr></thead>"""

COVER_A = [("shield", "Runtime protection"), ("bot", "AI security"), ("code", "Application security"),
           ("globe", "Regions and residency"), ("box", "Kubernetes"), ("list", "Policy setup")]
COVER_B = [("layers", "Unified platform"), ("cloud", "Cloud coverage"), ("pulse", "Fast onboarding"),
           ("monitor", "Compliance"), ("target", "Identity (CIEM)"), ("filescan", "Data (DSPM)")]


def tiles(items):
    return "".join(f'<div class="tile">{ic(i, "ti")}<span>{t}</span></div>' for i, t in items)


PICK = [("shield", "Block threats before they finish"), ("bot", "Enforce policy on prompts and agents"),
        ("globe", "Host in Europe or Middle East"), ("layers", "Run code to AI on one platform")]

PROOF = [("SOC 2 Type II", "report, Infoguard"), ("ISO 27001", "2022 audit completed"), ("2M+", "KubeArmor downloads"),
         ("200+", "cloud accounts secured"), ("24x7", "Platinum support")]

html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
@page {{ size:A4; margin:12mm 11mm 15mm }}
@page cover {{ margin:0 }}
:root{{--navy:#11206D;--blue:#0046FF;--ink:#1B223B;--mute:#5A637D;--line:#DDE2EE;
--win:#0B7A42;--win-bg:#E4F5EC;--no:#C80019;--no-bg:#FCE9EC;--lim:#A15C00;--lim-bg:#FFF1DC;--par:#4D4DD9;--par-bg:#ECECFB;--ora:#B45309;--ora-bg:#FDF0DC}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Space Grotesk',Arial,sans-serif;color:var(--ink);font-size:9pt;line-height:1.3}}
a{{color:var(--blue);text-decoration:none}}
.ic,.ci,.capi,.ti{{display:inline-block;vertical-align:middle}}
.fill{{background:#FFF3BF;color:#7A5B00;padding:0 3px;border-radius:3px;font-weight:700}}

/* cover */
.cover{{page:cover;width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;padding:20mm 17mm}}
.blob{{position:absolute;width:190mm;opacity:.9}}
.b1{{right:-70mm;top:-80mm}} .b2{{left:-80mm;bottom:-90mm}}
.cover .logo{{width:52mm;position:relative}}
.cover .title{{position:relative;margin-top:36mm;border-left:5px solid;border-image:linear-gradient(#F0505A,#1136D8) 1;padding-left:9mm}}
.cover .t1{{font-size:54pt;font-weight:700;color:#1136D8;line-height:1}}
.cover .vs{{font-size:30pt;color:#44505F;margin:4mm 0}}
.cover .t2{{font-size:54pt;font-weight:700;color:#1136D8;line-height:1}}
.cover .t3{{font-size:19pt;font-weight:500;color:var(--navy);margin-top:6mm}}
.cover .for{{position:relative;margin-top:10mm;font-size:11pt;color:var(--mute);padding-left:14mm}}
.cover .for b{{color:var(--ink)}}
.groups{{position:absolute;left:17mm;right:17mm;bottom:22mm;display:grid;grid-template-columns:1fr 1fr;gap:5mm}}
.grp{{background:rgba(255,255,255,.86);border:1px solid #C9D2E6;border-radius:10px;padding:5mm}}
.grp h3{{margin:0 0 4mm;font-size:12pt;color:var(--navy)}}
.grp .n{{display:inline-block;background:var(--navy);color:#fff;border-radius:4px;font-size:8pt;padding:1px 6px;margin-right:6px;vertical-align:2px}}
.tiles{{display:grid;gap:3mm;grid-template-columns:1fr 1fr}}
.tile{{display:flex;align-items:center;gap:6px;font-size:8.6pt;font-weight:600;color:var(--ink)}}
.ti{{width:17px;height:17px;color:var(--blue);flex:none;background:#EAF0FF;border-radius:5px;padding:3px;box-sizing:content-box}}

/* body */
.page{{padding:0}}
.topbar{{height:4px;background:linear-gradient(90deg,#1136D8,#6B3FD1 55%,#F0505A);border-radius:2px;margin-bottom:9px}}
.brandrow{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}
.brandrow img{{height:17px}} .brandrow span{{font-size:7.6pt;color:var(--mute);letter-spacing:.4px;text-transform:uppercase}}
h1{{font-size:21pt;line-height:1.1;margin:0 0 8px;color:var(--navy)}}
h1 em{{font-style:normal;color:var(--blue)}}
.verdict{{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:stretch;border:1.5px solid var(--blue);border-radius:10px;padding:8px 10px;background:#F4F7FF;margin-bottom:6px}}
.verdict .lbl{{font-weight:700;font-size:10pt;color:var(--blue);display:flex;align-items:center;max-width:26mm;line-height:1.15}}
.picks{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}}
.pick{{display:flex;gap:6px;align-items:center;font-weight:600;font-size:8.6pt;line-height:1.2}}
.pick .ti{{background:#fff}}
.tally{{display:flex;gap:14px;font-size:8.2pt;color:var(--mute);margin:0 2px 8px;align-items:center}}
.tally b{{color:var(--ink)}}
.dot{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px}}
.sec{{display:flex;align-items:center;gap:8px;margin:10px 0 5px;break-after:avoid}}
.sec .num{{font-size:8.5pt;font-weight:700;color:#fff;background:var(--navy);border-radius:4px;padding:2px 7px}}
.sec h2{{font-size:14pt;margin:0;color:var(--navy)}}
.sec .sub{{font-size:8pt;color:var(--mute)}}

table{{width:100%;border-collapse:separate;border-spacing:0;table-layout:fixed}}
col.c1{{width:21%}}col.c2{{width:38%}}col.c3{{width:25%}}col.c4{{width:16%}}
thead th{{padding:5px 8px 6px;text-align:left;border-bottom:2px solid var(--navy);font-size:7.6pt;text-transform:uppercase;letter-spacing:.5px;color:var(--mute);vertical-align:bottom}}
th.h-ak{{background:#EEF3FF;border-radius:8px 8px 0 0;border-bottom-color:var(--blue)}}
th.h-ak img{{height:17px}} th.h-ns img{{height:22px}}
tbody tr{{break-inside:avoid}}
td{{vertical-align:top;padding:6px 8px;border-bottom:1px solid var(--line)}}
td.cap .capw{{display:flex;gap:7px;align-items:flex-start;font-weight:700;font-size:11pt;line-height:1.15;color:var(--navy)}}
.capi{{width:18px;height:18px;flex:none;color:var(--blue);margin-top:1px}}
td.ak{{background:#F3F7FF;border-left:3px solid var(--win)}}
td.ak.par{{border-left-color:var(--par)}} td.ak.lim2{{border-left-color:var(--blue)}}
td.ns{{border-left:3px solid var(--line)}}
td.ns.lim{{border-left-color:#E0A340}} td.ns.par{{border-left-color:var(--par)}} td.ns.orca{{border-left-color:var(--line)}}
td.tk{{font-weight:700;font-size:8.2pt;color:var(--blue);line-height:1.25}}
td ul{{margin:4px 0 0;padding-left:12px}} td li{{margin:0 0 2px}} td li::marker{{color:#9AA3BD}}
td.ns li{{color:#4A5270}}
.chip{{display:inline-flex;align-items:center;gap:3px;font-weight:700;font-size:6.9pt;letter-spacing:.3px;padding:1.5px 7px 1.5px 5px;border-radius:9px;text-transform:uppercase}}
.ci{{width:9px;height:9px;stroke-width:3}}
.c-win{{background:var(--win-bg);color:var(--win)}} .c-no{{background:var(--no-bg);color:var(--no)}}
.c-lim{{background:var(--lim-bg);color:var(--lim)}} .c-par{{background:var(--par-bg);color:var(--par)}} .c-ora{{background:var(--ora-bg);color:var(--ora)}} .c-next{{background:#EAF0FF;color:var(--blue)}} .c-neu{{background:#EEF0F5;color:#4A5270}}

/* roadmap + proof, flat and spacious */
.road{{margin-top:16px;break-inside:avoid}}
.road h3{{margin:0 0 3px;font-size:14pt;color:var(--navy)}}
.road .lead{{font-size:8.6pt;color:var(--mute);margin-bottom:10px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.col{{border:1px solid var(--line);border-radius:10px;padding:12px 14px;background:#fff}}
.col h4{{margin:0 0 9px;font-size:10.5pt;color:var(--navy);display:flex;align-items:center;gap:8px}}
.col .lab{{display:block;font-size:6.9pt;font-weight:700;letter-spacing:.7px;text-transform:uppercase;color:var(--mute);margin:8px 0 3px}}
.col .lab.nx{{color:var(--blue)}}
.col p{{margin:0;font-size:8.6pt;line-height:1.4}}
.col ul{{margin:0;padding-left:13px;font-size:8.6pt}} .col li{{margin:0 0 3px;line-height:1.4}}
.proof{{display:grid;grid-template-columns:repeat(5,1fr);margin-top:20px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);break-inside:avoid}}
.pf{{padding:12px 6px 12px 12px;border-left:1px solid var(--line)}} .pf:first-child{{border-left:0;padding-left:0}}
.pf b{{display:block;font-size:13pt;line-height:1.1;color:var(--navy)}} .pf span{{display:block;font-size:7.4pt;color:var(--mute);margin-top:3px}}
.cta{{margin-top:16px;border-radius:10px;padding:13px 16px;background:var(--blue);color:#fff;font-weight:700;font-size:10.5pt;break-inside:avoid}}
.cta span{{display:block;font-weight:500;font-size:8.4pt;margin-top:3px}}
.src{{margin-top:12px;font-size:6.8pt;color:var(--mute);line-height:1.4}}
</style></head><body>

<section class="cover">
  <img class="blob b1" src="{b64('cover-blob-red.png')}"><img class="blob b2" src="{b64('cover-blob-blue.png')}">
  <img class="logo" src="{b64('accuknox-logo-cover.png')}">
  <div class="title"><div class="t1">AccuKnox</div><div class="vs">vs</div><div class="t2">Orca Security</div><div class="t3">(Zero Trust CNAPP)</div></div>
  <div class="for">Prepared for <b>Jubilee Insurance</b> &nbsp;·&nbsp; October 2026</div>
  <div class="groups">
    <div class="grp"><h3><span class="n">01</span>Protect and enforce</h3><div class="tiles">{tiles(COVER_A)}</div></div>
    <div class="grp"><h3><span class="n">02</span>Posture, identity and data</h3><div class="tiles">{tiles(COVER_B)}</div></div>
  </div>
</section>

<section class="page">
<div class="topbar"></div>
<div class="brandrow"><img src="{b64('accuknox-logo.png')}"><span>Prepared for Jubilee Insurance</span></div>
<h1>Orca finds risk. AccuKnox finds it and <em>stops</em> it.</h1>
<div class="verdict"><div class="lbl">Pick AccuKnox to</div><div class="picks">{"".join(f'<div class="pick">{ic(i, "ti")}<span>{t}</span></div>' for i, t in PICK)}</div></div>
<div class="tally"><span><span class="dot" style="background:var(--win)"></span><b>4</b> AccuKnox leads</span>
<span><span class="dot" style="background:var(--par)"></span><b>6</b> parity</span>
<span><span class="dot" style="background:var(--blue)"></span><b>2</b> closing in the next release</span></div>

<div class="sec"><span class="num">01</span><h2>Protect and enforce</h2><span class="sub">Where AccuKnox leads or matches</span></div>
<table>{THEAD}<tbody>{"".join(G1)}</tbody></table>
</section>

<section class="page" style="break-before:page">
<div class="topbar"></div>
<div class="sec" style="margin-top:0"><span class="num">02</span><h2>Posture, identity and data</h2><span class="sub">Parity on posture, a plan for identity and data</span></div>
<table>{THEAD}<tbody>{"".join(G2)}</tbody></table>

<div class="road">
  <h3>Identity and data security land in the next release</h3>
  <div class="lead">Posture matches Orca today. These two rows close in the next release.</div>
  <div class="two">
    <div class="col"><h4>{ic("target", "ti")}Identity (CIEM)</h4>
      <span class="lab">Today</span><p>Identities, risk classes and access graph on AWS, Azure, GCP and OCI.</p>
      <span class="lab nx">Next release</span><ul><li>Organization accounts</li><li>Privileged account activity monitoring</li></ul></div>
    <div class="col"><h4>{ic("filescan", "ti")}Data security (DSPM)</h4>
      <span class="lab">Today</span><p>Scanner in your region for S3, Blob, RDS, Azure SQL, Cosmos DB, MongoDB, Drive and Salesforce.</p>
      <span class="lab nx">Next release</span><ul><li>OCI data stores</li></ul></div>
  </div>
</div>

<div class="proof">{"".join(f'<div class="pf"><b>{a}</b><span>{b}</span></div>' for a, b in PROOF)}</div>
<div class="cta">Verify AccuKnox on your own accounts by Week 1<span>Agree success criteria in Week 0, onboard one account, and run runtime policies in audit mode.</span></div>
<div class="src">Orca facts come from public Orca pages read 13 October 2026. AccuKnox facts come from help.accuknox.com and the proposal dated 10 August 2026.</div>
</section>
</body></html>"""

BUILD.mkdir(exist_ok=True)
(BUILD / "battlecard.html").write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto((BUILD / "battlecard.html").as_uri())
    pg.wait_for_load_state("networkidle")
    pg.pdf(path=str(BUILD / "body.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
    b.close()

n = PdfReader(str(BUILD / "body.pdf"))
w = PdfWriter()
for pg in n.pages:
    w.add_page(pg)
w.add_page(PdfReader(str(A / "back-page.pdf")).pages[0])
w.write(OUT)
print(f"{OUT}: {len(n.pages) + 1} pages")
