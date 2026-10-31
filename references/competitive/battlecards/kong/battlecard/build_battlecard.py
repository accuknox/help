"""Build the AccuKnox vs Kong AI Gateway comparison PDF for the UIDAI RFP.

Copied from the Netskope reference build and reworked for an RFP-led layout:
cover, at-a-glance page, capability matrix, RFP levers page, stock back page.
Layout rules live in
.claude/skills/accuknox-comparison-writer/references/battlecard-pdf.md, and the
cover follows the repo CLAUDE.md rule "Marketing files must not look machine made".
Every claim and its source sits in evidence-log.md beside this file.

Run from the repo root:
    python references/competitive/battlecards/kong/battlecard/build_battlecard.py [out.pdf]

Needs playwright (with chromium) and pypdf.
"""
import base64
import pathlib
import sys
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

HERE = pathlib.Path(__file__).resolve().parent
A = HERE / "assets"
BUILD = HERE / "build"
TITLE = "AccuKnox Comparison Kong AI Gateway UIDAI"
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else BUILD / "AccuKnox_Comparison_Kong_AI_Gateway_UIDAI.pdf"


def b64(name):
    return "data:image/png;base64," + base64.b64encode((A / name).read_bytes()).decode()


def si(name, color, cls="brand"):
    svg = (A / f"si_{name}.svg").read_text(encoding="utf-8")
    return svg.replace("<svg ", f'<svg class="{cls}" fill="#{color}" ', 1)


BR = {
    "openai": si("openai", "000000"),
    "claude": si("claude", "D97757"),
    "gemini": si("googlegemini", "8E75B2"),
    "copilot": si("githubcopilot", "000000"),
    "ms": si("microsoft", "5E5E5E"),
    "k8s": si("kubernetes", "326CE5"),
    "ollama": si("ollama", "000000"),
    "nvidia": si("nvidia", "76B900"),
}
KONG_MARK = si("kong", "000000", "kmark")
AK_LOGO = f'<img class="aklogo" src="{b64("accuknox-logo.png")}">'
KONG_LOGO = f'<span class="konglogo">{KONG_MARK}<b>Kong</b></span>'

I = {
    "server": '<rect width="20" height="8" x="2" y="2" rx="2"/><rect width="20" height="8" x="2" y="14" rx="2"/><line x1="6" x2="6.01" y1="6" y2="6"/><line x1="6" x2="6.01" y1="18" y2="18"/>',
    "layers": '<path d="m12 2 10 5-10 5L2 7Z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "term": '<polyline points="4 17 10 11 4 5"/><line x1="12" x2="20" y1="19" y2="19"/>',
    "browser": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 8h20"/><path d="M6 4v4"/><path d="M10 4v4"/>',
    "eyeoff": '<path d="M9.88 9.88a3 3 0 1 0 4.24 4.24"/><path d="M10.73 5.08A10.43 10.43 0 0 1 12 5c7 0 10 7 10 7a13.16 13.16 0 0 1-1.67 2.68"/><path d="M6.61 6.61A13.526 13.526 0 0 0 2 12s3 7 10 7a9.74 9.74 0 0 0 5.39-1.61"/><line x1="2" x2="22" y1="2" y2="22"/>',
    "box": '<path d="M21 8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16Z"/><path d="m3.3 7 8.7 5 8.7-5"/><path d="M12 22V12"/>',
    "list": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
    "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    "gauge": '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
    "gateway": '<rect width="20" height="8" x="2" y="14" rx="2"/><path d="M6.01 18H6"/><path d="M10.01 18H10"/><path d="M15 10v4"/><path d="M17.84 7.17a4 4 0 0 0-5.66 0"/><path d="M20.66 4.34a8 8 0 0 0-11.31 0"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    "half": '<circle cx="12" cy="12" r="9"/><path d="M12 3v18"/>',
    "equal": '<line x1="5" x2="19" y1="9" y2="9"/><line x1="5" x2="19" y1="15" y2="15"/>',
    "pulse": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "flag": '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" x2="4" y1="22" y2="15"/>',
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
MARK = {"yes": ("m-win", "check"), "no": ("m-no", "x"), "noeq": ("m-no", "x"), "lim": ("m-lim", "half"), "par": ("m-par", "equal")}


def chip(k):
    cls, icon, label = CHIP[k]
    return f'<span class="chip {cls}">{ic(icon, "ci")}{label}</span>'


def mark(k):
    cls, icon = MARK[k]
    return f'<span class="mark {cls}">{ic(icon, "mi")}</span>'


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def row(icon, cap, rfp, ak, kg_k, kg, tk, ak_k="yes"):
    return f"""<tr>
<td class="cap"><div class="capw">{ic(icon, 'capi')}<span>{cap}</span></div><div class="rfp">{rfp}</div></td>
<td class="ak">{chip(ak_k)}{ul(ak)}</td>
<td class="kg {kg_k}">{chip(kg_k)}{ul(kg)}</td>
<td class="tk">{tk}</td></tr>"""


LOGOS_PF = f'<span class="logos">{BR["openai"]}{BR["claude"]}{BR["gemini"]}{BR["copilot"]}{BR["ms"]}</span>'

G1 = [
    row("server", "On-prem control plane", "R-009 to R-013",
        ["<b>Control plane on-prem</b>", "Air-gapped, offline updates"],
        "par", ["Self-hosted Kong Gateway, AI plugins", "2.x entity model needs Konnect"],
        "Both run in your data center", ak_k="par"),
    row("layers", "One platform", "R-026 to R-028 · PQ-05",
        ["<b>Gateway, browser, CLI, host, agent</b>", "One inventory"],
        "lim", ["Gateway traffic: LLM, MCP, A2A"],
        "One vendor, every surface"),
]

G2 = [
    row("shield", "Prompt injection", "R-057 to R-063",
        ["<b>Multi-turn session scoring</b>", "14 policy types"],
        "lim", ["Regex, similarity, third-party guards"],
        "Catches split jailbreaks"),
    row("lock", "PII masking", "R-070 to R-073",
        ["PII, PHI, secrets, custom regex"],
        "par", ["PII container, no Hindi model"],
        "Masked before it leaves", ak_k="par"),
    row("term", "Coding agents", "R-133 to R-141",
        ["<b>Routes and discovers</b> CLI agents"],
        "lim", ["Routes Claude Code, Codex, Gemini CLI", "No discovery of installed agents"],
        "Seen and governed"),
    row("browser", "Browser GenAI", "R-119 to R-132",
        [f"<b>Prompt checks in browser</b> {LOGOS_PF}", "Intune push, removal blocked"],
        "no", ["No browser extension"],
        "Stops leaks at the laptop"),
    row("eyeoff", "Shadow AI on hosts", "R-105 to R-112",
        ["<b>7 AI categories</b> on VMs and K8s", "Linux, Windows, macOS"],
        "lim", ["Finds AI traffic sent to the gateway"],
        "Unapproved AI made visible"),
    row("box", "Agent sandbox", "R-090 to R-101",
        ["<b>eBPF + LSM</b> in the kernel", "No code change"],
        "noeq", ["MCP tool ACLs, no host control"],
        "Stops rogue agents"),
]

G3 = [
    row("list", "AI-BOM &amp; model scan", "R-113, R-114, R-145",
        ["<b>AIBOM in CycloneDX</b>", "Unsafe model files caught"],
        "no", ["No BOM or model scan"],
        "Bad models never load"),
    row("target", "Red teaming", "R-150 to R-156",
        ["<b>Hundreds of probes</b>", "OWASP LLM, MITRE ATLAS"],
        "no", ["No native red teaming"],
        "Attacked before attackers try"),
    row("gauge", "AI posture", "R-142 to R-149",
        ["<b>4 frameworks</b> mapped"],
        "no", ["No posture scoring"],
        "Every AI asset scored"),
]

THEAD = f"""<colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"></colgroup>
<thead><tr><th class="h-cap">Capability</th><th class="h-ak">{AK_LOGO}</th>
<th class="h-kg">{KONG_LOGO}</th><th class="h-tk">What you get</th></tr></thead>"""

# RFP sections: letter, name, Must count, leader (ak | par | kong)
SECTIONS = [
    ("B", "On-prem &amp; air-gap", 15, "par"), ("C", "One control plane", 8, "ak"),
    ("D", "AI Gateway", 15, "kong"), ("E", "Prompt Firewall", 12, "ak"),
    ("F", "Data protection", 9, "par"), ("G", "Response safety", 2, "par"),
    ("H", "Agent sandbox", 12, "ak"), ("I", "Shadow AI", 9, "ak"),
    ("J", "Browser", 8, "ak"), ("K", "Coding agents", 7, "ak"),
    ("L", "Posture &amp; models", 6, "ak"), ("M", "Red teaming", 6, "ak"),
    ("N", "Identity &amp; policy", 7, "par"), ("O", "SOC &amp; telemetry", 10, "kong"),
]
LEAD = {"ak": ("s-ak", "AccuKnox ahead"), "par": ("s-par", "Both"), "kong": ("s-kong", "Kong ahead")}


def heat():
    out = []
    for letter, name, must, lead in SECTIONS:
        cls, label = LEAD[lead]
        out.append(f'<div class="sq {cls}"><div class="sl">{letter}</div><div class="sn">{name}</div>'
                   f'<div class="sm"><b>{must}</b> Must</div><div class="sw">{label}</div></div>')
    return "".join(out)


# Surface coverage grid: icon, surface, AccuKnox status, Kong status
SURF = [
    ("gateway", "AI gateway routing", "yes", "yes"),
    ("shield", "Prompt firewall", "yes", "lim"),
    ("lock", "PII masking", "yes", "yes"),
    ("term", "Coding agents", "yes", "lim"),
    ("server", "On-prem control plane", "yes", "yes"),
    ("browser", "Browser GenAI", "yes", "no"),
    ("eyeoff", "Shadow AI discovery", "yes", "lim"),
    ("box", "Agent kernel sandbox", "yes", "no"),
    ("list", "AI-BOM, model scan", "yes", "no"),
    ("target", "Red teaming", "yes", "no"),
    ("gauge", "AI posture", "yes", "no"),
]


def grid():
    cells = []
    for icon, name, a, k in SURF:
        cells.append(f'<div class="gc">{ic(icon, "gi")}<span class="gn">{name}</span>{mark(a)}{mark(k)}</div>')
    return "".join(cells)


TLDR = [
    ("gateway", "AI gateway routing", "yes", "Built in", "yes", "Core strength"),
    ("server", "On-prem control plane", "yes", "Air-gapped", "yes", "Self-hosted gateway"),
    ("lock", "PII masking", "yes", "PII, PHI, secrets", "yes", "PII container"),
    ("shield", "Prompt firewall", "yes", "Multi-turn scoring", "lim", "Regex and partners"),
    ("term", "Coding agents", "yes", "Route and discover", "lim", "Route only"),
    ("eyeoff", "Shadow AI discovery", "yes", "Hosts, browser, CLI", "lim", "Gateway traffic only"),
    ("browser", "Browser GenAI", "yes", "5 browsers, Intune", "no", "None"),
    ("box", "Agent kernel sandbox", "yes", "eBPF and LSM", "no", "None"),
    ("list", "AI-BOM and model scan", "yes", "CycloneDX AIBOM", "no", "None"),
    ("target", "Red teaming", "yes", "Hundreds of probes", "no", "None native"),
    ("gauge", "AI posture", "yes", "4 frameworks", "no", "None"),
]


def tldr():
    out = []
    for icon, name, a, at, k, kt in TLDR:
        out.append(f'<div class="tr"><div class="tl">{mark(a)}<span>{at}</span></div>'
                   f'<div class="tm">{ic(icon, "gi")}<b>{name}</b></div>'
                   f'<div class="tk2 {k}">{mark(k)}<span>{kt}</span></div></div>')
    return "".join(out)


PICK = [("eyeoff", "Find AI on every host and browser"), ("layers", "Cover browser, host and agent"),
        ("box", "Sandbox agents in the kernel"), ("target", "Red-team models before release")]

# PoC marks: suite, marks, marks Kong lists no equivalent for
SUITES = [("Deployment", 12, 0), ("Prompt threats", 16, 0), ("Data protection", 12, 0), ("AI gateway", 11, 0),
          ("Agent &amp; runtime", 17, 14), ("Shadow AI", 10, 7), ("Browser &amp; dev", 10, 7), ("Red teaming", 6, 6),
          ("Operations", 6, 0)]


def pocbar():
    segs, labels = [], []
    for name, total, gap in SUITES:
        segs.append(f'<div class="seg" style="flex:{total}">'
                    + (f'<div class="gap" style="width:{gap / total * 100:.1f}%"></div>' if gap else "")
                    + f'<span{" class=on" if gap / total >= .5 else ""}>{total}</span></div>')
        labels.append(f'<div class="segl" style="flex:{total}">{name}</div>')
    return f'<div class="bar">{"".join(segs)}</div><div class="barl">{"".join(labels)}</div>'


# UIDAI POC plan modules: icon, module, Kong status (AccuKnox delivers all seven in the plan)
POC = [("shield", "Prompt Firewall", "lim"), ("gateway", "AI Gateway", "yes"), ("eyeoff", "Shadow AI Discovery", "lim"),
       ("browser", "Browser plugin", "no"), ("pulse", "Dashboard &amp; alerts", "yes"),
       ("target", "Red teaming &amp; model audit", "no"), ("box", "Agent sandboxing", "no")]


def poc():
    return "".join(f'<div class="pt {"gap" if k == "no" else ""}">{ic(i, "gi")}<b>{n}</b>'
                   f'<div class="pm"><span>{AK_LOGO}</span>{mark("yes")}</div>'
                   f'<div class="pm"><span>{KONG_LOGO}</span>{mark(k)}</div></div>' for i, n, k in POC)


PARTNERS = ["Lakera Guard (SaaS)", "NVIDIA NeMo Guardrails", "AWS Guardrails", "Azure Content Safety",
            "GCP Model Armor", "CrowdStrike Falcon", "Noma Security"]
SOURCES = ["developer.konghq.com/ai-gateway/architecture", "developer.konghq.com/ai-gateway/configure-on-prem",
           "developer.konghq.com/ai-gateway/policies", "developer.konghq.com/ai-gateway/ai-clis",
           "developer.konghq.com/plugins/ai-sanitizer", "developer.konghq.com/plugins/ai-mcp-proxy",
           "developer.konghq.com/catalog/agents", "konghq.com/blog/enterprise/shadow-ai-detection-enterprise-governance",
           "konghq.com/blog/enterprise/building-the-kong-context-mesh-stack", "konghq.com/resources/videos/ai-runtime-protection"]

PQ = [("AI gateway policy engine", "yes", "yes"), ("Prompt inspection engine", "yes", "lim"),
      ("Host runtime enforcement", "yes", "no"), ("AI asset discovery", "yes", "lim")]
C3 = [("Gateway", True), ("IDE / CLI", True), ("Browser", False), ("Endpoint", False), ("Runtime", False)]

MUST = [
    ("box", "R-091, R-093, R-094, R-098, R-101", "Kernel sandbox for agents", "O4 Contain agents", "noeq"),
    ("eyeoff", "R-105 to R-110, R-112", "Host AI discovery, CLI agents", "O5 See all AI", "no"),
    ("list", "R-113, R-114", "AIBOM, SBOM, CBOM in CycloneDX", "O5 See all AI", "no"),
    ("browser", "R-119 to R-126", "Managed browser extension via MDM", "O5 See all AI", "no"),
    ("gauge", "R-145, R-147", "Model file scan, framework posture", "O3 Stop attacks", "no"),
    ("target", "R-150 to R-155", "On-prem automated red teaming", "O3 Stop attacks", "noeq"),
    ("flag", "R-211", "Open-source engine under a foundation", "Avoid lock-in", "lim"),
]


def musts():
    return "".join(f'<tr><td>{ic(i, "mi2")}</td><td class="rid">{r}</td><td>{w}</td><td class="obj">{o}</td><td>{chip(k)}</td></tr>'
                   for i, r, w, o, k in MUST)


COVER_ART = """<svg class="art" viewBox="0 0 520 300" fill="none" stroke="#11206D" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
  <rect x="200" y="112" width="120" height="76" rx="10"/>
  <path d="M222 138h76M222 152h76M222 166h44"/>
  <circle cx="300" cy="166" r="5" stroke="#0046FF"/>
  <rect x="30" y="30" width="110" height="72" rx="8"/><path d="M30 46h110M44 38h0M54 38h0"/>
  <path d="M48 64h60M48 78h40"/>
  <rect x="380" y="30" width="110" height="72" rx="8"/><path d="M380 54h110M380 78h110"/><path d="M394 42h0M394 66h0M394 90h0"/>
  <rect x="30" y="198" width="110" height="72" rx="8"/><path d="M58 222l14 12-14 12M84 248h30"/>
  <path d="M435 196l40 18v30c0 22-40 34-40 34s-40-12-40-34v-30z"/><path d="M420 240l11 11 21-21" stroke="#0046FF"/>
  <path d="M140 66C180 66 170 125 200 132M380 66C340 66 350 125 320 132M140 234C180 234 170 175 200 168M395 228C360 220 350 178 320 168"/>
  <circle cx="200" cy="132" r="3" fill="#11206D"/><circle cx="320" cy="132" r="3" fill="#11206D"/>
  <circle cx="200" cy="168" r="3" fill="#11206D"/><circle cx="320" cy="168" r="3" fill="#11206D"/>
</svg>"""

CSS = """
@page { size:A4; margin:12mm 11mm 12mm }
@page cover { margin:0 }
:root{--navy:#11206D;--blue:#0046FF;--ink:#1B223B;--mute:#5A637D;--line:#DDE2EE;--tint:#F3F6FF;
--win:#0B7A42;--win-bg:#E4F5EC;--no:#C80019;--no-bg:#FCE9EC;--lim:#A15C00;--lim-bg:#FFF1DC;--par:#4D4DD9;--par-bg:#ECECFB}
*{box-sizing:border-box}
body{margin:0;font-family:'Inter',Arial,sans-serif;color:var(--ink);font-size:9pt;line-height:1.3}
.ic,.ci,.capi,.ti,.gi,.mi,.mi2{display:inline-block;vertical-align:middle}
.brand{width:10px;height:10px;vertical-align:-1.5px;margin-right:3px}
.aklogo{height:16px;vertical-align:middle}
.konglogo{display:inline-flex;align-items:center;gap:5px;font-size:13pt;color:#000;letter-spacing:-.2px;text-transform:none}
.kmark{width:17px;height:17px}

/* cover: TLDR split, AccuKnox left, Kong right, flat colors */
.cover{page:cover;width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;padding:16mm 16mm 12mm;background:#fff}
.cover .logo{width:44mm}
.cover h1{margin:9mm 0 0;font-size:36pt;line-height:1;font-weight:700;color:var(--navy);letter-spacing:-1px}
.cover .deck{margin-top:3mm;font-size:12.5pt;color:var(--mute);font-weight:500}
.vsrow{display:grid;grid-template-columns:1fr 18mm 1fr;align-items:stretch;margin-top:8mm}
.side{border-radius:12px;padding:5mm 6mm;display:flex;flex-direction:column;justify-content:center}
.side.ak{background:var(--navy);color:#fff;align-items:flex-start}
.side.ak img{height:18px;background:#fff;border-radius:5px;padding:4px 6px}
.side.kg{background:#F1F2F6;color:var(--ink);align-items:flex-end;text-align:right}
.side.kg .konglogo{font-size:16pt}.side.kg .kmark{width:20px;height:20px}
.side .score{font-size:44pt;font-weight:700;line-height:1;margin-top:3mm;letter-spacing:-1px}
.side .score small{font-size:18pt;font-weight:600;opacity:.7}
.side .cap{font-size:9pt;font-weight:600;opacity:.85;margin-top:1mm}
.vsb{display:flex;align-items:center;justify-content:center;font-size:15pt;font-weight:800;color:var(--navy)}
.tbl{margin-top:5mm;border-top:2px solid var(--navy)}
.tr{display:grid;grid-template-columns:1fr 64mm 1fr;align-items:center;border-bottom:1px solid var(--line);padding:2.1mm 0}
.tl{display:flex;align-items:center;gap:7px;font-size:9.4pt;font-weight:700;color:var(--navy);padding-left:2mm}
.tm{display:flex;align-items:center;justify-content:center;gap:6px;font-size:9.6pt;color:var(--ink);background:#F7F8FB;border-radius:6px;padding:1.6mm 0}
.tm .gi{width:15px;height:15px;color:var(--navy)}
.tk2{display:flex;align-items:center;justify-content:flex-start;gap:7px;font-size:9.4pt;font-weight:600;color:#6A7290;padding-right:2mm;flex-direction:row-reverse}
.tk2.no span{color:var(--no)} .tk2.lim span{color:var(--lim)} .tk2.yes span{color:var(--ink)}
.bars{margin-top:5mm;display:flex;flex-direction:column;gap:2.4mm}
.br{display:grid;grid-template-columns:22mm 1fr 44mm;align-items:center;gap:4mm;font-size:9pt;font-weight:700;color:var(--navy)}
.bt{display:flex;height:11px;border-radius:6px;overflow:hidden;gap:2px;background:#fff}
.bt i{display:block} .bt .f{background:var(--win)} .bt .p{background:#E0A340} .bt .n{background:var(--no)}
.bv{font-weight:600;color:var(--mute);font-size:8.4pt}
.cfoot{position:absolute;left:16mm;right:16mm;bottom:9mm;font-size:7.4pt;color:var(--mute)}

/* body */
.hdr{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid var(--navy);padding-bottom:5px;margin-bottom:10px}
.hdr .t{font-size:7.8pt;font-weight:600;color:var(--mute);letter-spacing:.4px;text-transform:uppercase}
.hdr img{height:13px}
h1.v{font-size:21pt;line-height:1.1;margin:0 0 8px;color:var(--navy);letter-spacing:-.3px}
h1.v em{font-style:normal;color:var(--win)}
.pg{break-before:page}
.picks{display:grid;grid-template-columns:repeat(4,1fr);gap:7px;margin-bottom:10px}
.pick{display:flex;gap:7px;align-items:center;font-weight:600;font-size:8.8pt;line-height:1.2;background:#fff;border:1.5px solid var(--navy);border-radius:8px;padding:7px 8px}
.ti{width:16px;height:16px;color:#fff;flex:none;background:var(--navy);border-radius:5px;padding:3px;box-sizing:content-box}

.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px}
.stat{border-radius:10px;padding:9px 11px;background:var(--navy);color:#fff}
.stat .n{font-size:27pt;font-weight:700;line-height:1;letter-spacing:-.5px}
.stat .n small{font-size:13pt;font-weight:600;opacity:.75}
.stat .d{font-size:8.4pt;margin-top:5px;line-height:1.25;opacity:.92}

.sec{display:flex;align-items:center;gap:8px;margin:10px 0 6px;break-after:avoid}
.sec .num{font-size:8.5pt;font-weight:700;color:#fff;background:var(--navy);border-radius:4px;padding:2px 7px}
.sec h2{font-size:13pt;margin:0;color:var(--navy)}
.sec .key{margin-left:auto;display:flex;gap:10px;font-size:7.6pt;color:var(--mute);align-items:center}
.sw2{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:4px;vertical-align:-1px}

.heat{display:grid;grid-template-columns:repeat(7,1fr);gap:5px}
.sq{border-radius:7px;padding:6px 6px 5px;min-height:19mm;display:flex;flex-direction:column}
.sq .sl{font-size:13pt;font-weight:700;line-height:1}
.sq .sn{font-size:7.6pt;font-weight:600;line-height:1.15;margin-top:3px;flex:1}
.sq .sm{font-size:7pt;opacity:.85}
.sq .sw{font-size:6.6pt;font-weight:700;text-transform:uppercase;letter-spacing:.4px;margin-top:2px}
.s-ak{background:var(--navy);color:#fff}
.s-par{background:#E9ECF5;color:var(--ink)}
.s-kong{background:#fff;color:var(--ink);border:1.5px solid #9AA3BD}

.gridwrap{border:1px solid var(--line);border-radius:10px;padding:8px 10px 6px}
.gh{display:grid;grid-template-columns:1fr 1fr;gap:0 18px;margin-bottom:3px}
.gh div{display:grid;grid-template-columns:1fr 78px 60px;font-size:7.4pt;font-weight:700;color:var(--mute);text-transform:uppercase;letter-spacing:.4px;align-items:center}
.gh div span{text-align:center}
.gh .aklogo{height:11px}
.gh .konglogo{font-size:9pt}.gh .kmark{width:12px;height:12px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:0 18px}
.gc{display:grid;grid-template-columns:18px 1fr 78px 60px;align-items:center;padding:4px 0;border-top:1px solid var(--line);font-size:9pt;font-weight:600}
.gi{width:15px;height:15px;color:var(--navy)}
.mark{justify-self:center;width:21px;height:21px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.mi{width:11px;height:11px;stroke-width:3}
.m-win{background:var(--win-bg);color:var(--win)} .m-no{background:var(--no-bg);color:var(--no)}
.m-lim{background:var(--lim-bg);color:var(--lim)} .m-par{background:var(--par-bg);color:var(--par)}
.tally{font-size:8.2pt;color:var(--mute);margin:6px 2px 0}
.tally b{color:var(--ink)}

table.m{width:100%;border-collapse:separate;border-spacing:0;table-layout:fixed}
col.c1{width:23%}col.c2{width:36%}col.c3{width:25%}col.c4{width:16%}
table.m thead th{padding:5px 8px 6px;text-align:left;border-bottom:2px solid var(--navy);font-size:7.4pt;text-transform:uppercase;letter-spacing:.5px;color:var(--mute);vertical-align:bottom}
th.h-ak{border-bottom:3px solid var(--win)!important}
table.m tbody tr{break-inside:avoid}
table.m td{vertical-align:top;padding:8px 8px 8px;border-bottom:1px solid var(--line)}
td.cap .capw{display:flex;gap:7px;align-items:flex-start;font-weight:700;font-size:10.8pt;line-height:1.15;color:var(--navy)}
.capi{width:18px;height:18px;flex:none;color:var(--navy);margin-top:1px}
td.cap .rfp{font-size:6.9pt;color:var(--mute);margin:4px 0 0 24px;font-weight:600;line-height:1.3}
td.ak{background:#fff;border-left:4px solid var(--win)} td.ak li{font-size:9.6pt;font-weight:500;color:var(--ink)} td.ak li b{color:var(--navy)}
td.kg{border-left:3px solid var(--line)}
td.kg.no,td.kg.noeq{border-left-color:var(--no)} td.kg.lim{border-left-color:#E0A340} td.kg.par{border-left-color:var(--par)}
td.tk{font-weight:700;font-size:9pt;color:var(--win);line-height:1.25}
table.m ul{margin:4px 0 0;padding-left:12px} table.m li{margin:0 0 2px} table.m li::marker{color:#9AA3BD}
td.kg li{color:#6A7290;font-size:8.6pt}
.logos{white-space:nowrap}
.chip{display:inline-flex;align-items:center;gap:3px;font-weight:700;font-size:7.4pt;letter-spacing:.3px;padding:1.5px 7px 1.5px 5px;border-radius:9px;text-transform:uppercase;white-space:nowrap}
.ci{width:9px;height:9px;stroke-width:3}
.c-win{background:var(--win-bg);color:var(--win)} .c-no{background:var(--no-bg);color:var(--no)}
.c-lim{background:var(--lim-bg);color:var(--lim)} .c-par{background:var(--par-bg);color:var(--par)}

/* levers */
.levers{display:grid;grid-template-columns:1fr 1fr;gap:9px;margin-bottom:9px}
.card{border:1px solid var(--line);border-radius:10px;padding:9px 11px;break-inside:avoid}
.card h3{margin:0 0 2px;font-size:10.5pt;color:var(--navy)}
.card .sub{font-size:7.8pt;color:var(--mute);margin-bottom:7px}
.pq{display:grid;grid-template-columns:1fr 78px 60px;align-items:center;font-size:8.6pt;font-weight:600}
.pq > div{padding:3.5px 0;border-top:1px solid var(--line)}
.pq .h{border-top:0;font-size:7pt;color:var(--mute);text-transform:uppercase;letter-spacing:.4px;text-align:center}
.pq .h:first-child{text-align:left}
.pq .aklogo{height:11px} .pq .konglogo{font-size:9pt} .pq .kmark{width:12px;height:12px}
.pq .mk{display:flex;justify-content:center}
.big{font-size:22pt;font-weight:700;color:var(--no);line-height:1}
.big small{font-size:10pt;color:var(--mute);font-weight:600}
.pills{display:flex;gap:5px;margin:7px 0 2px;flex-wrap:wrap}
.pill{font-size:8pt;font-weight:700;border-radius:12px;padding:3px 9px 3px 7px;display:inline-flex;gap:4px;align-items:center}
.pill.ok{background:var(--win-bg);color:var(--win)} .pill.miss{background:var(--no-bg);color:var(--no)}
.pill .mi{width:9px;height:9px}
.bar{display:flex;height:22px;border-radius:6px;overflow:hidden;gap:2px;margin-top:6px}
.seg{position:relative;background:#E3E7F1;display:flex;align-items:center;justify-content:center;font-size:7.4pt;font-weight:700;color:var(--mute)}
.seg .gap{position:absolute;left:0;top:0;bottom:0;background:var(--no)}
.seg span{position:relative;color:var(--ink)} .seg span.on{color:#fff}
.barl{display:flex;gap:2px;margin-top:3px}
.segl{font-size:6.3pt;color:var(--mute);text-align:center;line-height:1.1}
.legend{display:flex;gap:12px;font-size:7.6pt;color:var(--mute);margin-top:6px}
table.mu{width:100%;border-collapse:collapse;font-size:8.6pt}
table.mu td{padding:4px 5px;border-top:1px solid var(--line);vertical-align:middle}
table.mu tr:first-child td{border-top:0}
.mi2{width:14px;height:14px;color:var(--navy)}
td.rid{font-weight:700;color:var(--navy);white-space:nowrap}
td.obj{color:var(--mute);font-size:7.8pt;white-space:nowrap}
.poc{display:grid;grid-template-columns:repeat(7,1fr);gap:5px}
.pt{border:1px solid var(--line);border-radius:8px;padding:7px 6px;display:flex;flex-direction:column;gap:4px;font-size:8pt;line-height:1.15}
.pt.gap{border-color:#F1A7B2;background:#FFF7F8}
.pt b{color:var(--navy);min-height:2.35em}
.pt .gi{width:17px;height:17px}
.pm{display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:3px}
.pm .aklogo{height:8px} .pm .konglogo{font-size:7.5pt;gap:3px} .pm .kmark{width:9px;height:9px}
.pm .mark{width:15px;height:15px} .pm .mi{width:9px;height:9px}
.pill.neu{background:#EEF0F5;color:var(--ink);font-weight:600}
.method p{margin:0 0 6px;font-size:8.4pt;color:var(--ink);line-height:1.4}
.src{display:grid;grid-template-columns:1fr 1fr;gap:2px 14px;font-size:7pt;color:var(--mute)}
.foot{margin-top:9px;background:var(--navy);color:#fff;border-radius:10px;padding:9px 12px;font-size:10pt;font-weight:600;display:flex;gap:9px;align-items:center}
.foot .ti{background:#fff;color:var(--navy)}
"""

PICKS_HTML = "".join(f'<div class="pick">{ic(i, "ti")}<span>{t}</span></div>' for i, t in PICK)
HDR = f'<div class="hdr"><span></span><img src="{b64("accuknox-logo.png")}"></div>'
KEY = ('<div class="key"><span><span class="sw2" style="background:var(--navy)"></span>AccuKnox ahead</span>'
       '<span><span class="sw2" style="background:#E9ECF5"></span>Both</span>'
       '<span><span class="sw2" style="background:#fff;border:1.5px solid #9AA3BD"></span>Kong ahead</span></div>')

html = f"""<!doctype html><html><head><meta charset="utf-8"><title>{TITLE}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>

<section class="cover">
  <div class="ctop"><img class="logo" src="{b64('accuknox-logo-cover.png')}"></div>
  <h1>AccuKnox vs Kong</h1>
  <div class="deck">AI Security and AI Gateway comparison for UIDAI</div>
  <div class="vsrow">
    <div class="side ak"><img src="{b64('accuknox-logo.png')}"><div class="score">11<small>/11</small></div><div class="cap">AI areas covered natively</div></div>
    <div class="vsb">VS</div>
    <div class="side kg">{KONG_LOGO}<div class="score">3<small>/11</small></div><div class="cap">AI areas covered natively</div></div>
  </div>
  <div class="tbl">{tldr()}</div>
  <div class="bars">
    <div class="br"><span class="bn">AccuKnox</span><div class="bt"><i class="f" style="flex:11"></i></div><span class="bv">11 full</span></div>
    <div class="br"><span class="bn">Kong</span><div class="bt"><i class="f" style="flex:3"></i><i class="p" style="flex:3"></i><i class="n" style="flex:5"></i></div><span class="bv">3 full, 3 partial, 5 none</span></div>
  </div>
  <div class="cfoot">Kong ratings from Kong's public docs, 30 October 2026. Partner products not counted.</div>
</section>

<section>
{HDR}
<h1 class="v">Kong governs gateway traffic. AccuKnox <em>secures every AI surface.</em></h1>
<div class="picks">{PICKS_HTML}</div>
<div class="stats">
  <div class="stat"><div class="n">11<small> / 11</small></div><div class="d">AI capability areas AccuKnox covers natively</div></div>
  <div class="stat"><div class="n">3<small> / 11</small></div><div class="d">Areas Kong covers natively in full</div></div>
  <div class="stat"><div class="n">7<small> modules</small></div><div class="d">POC scope, delivered in 10 working days</div></div>
</div>

<div class="sec"><h2>Coverage by RFP section</h2>{KEY}</div>
<div class="heat">{heat()}</div>

<div class="sec" style="margin-top:12px"><h2>Coverage by AI surface</h2></div>
<div class="gridwrap">
  <div class="gh"><div><span style="text-align:left">Surface</span><span>{AK_LOGO}</span><span>{KONG_LOGO}</span></div>
  <div><span style="text-align:left">Surface</span><span>{AK_LOGO}</span><span>{KONG_LOGO}</span></div></div>
  <div class="grid">{grid()}</div>
</div>
<div class="tally"><b>11 surfaces.</b> AccuKnox covers all 11. Kong covers 3 in full, 3 in part and 5 not at all.</div>

<div class="sec" style="margin-top:12px"><h2>Deployment and platform</h2></div>
<table class="m">{THEAD}<tbody>{"".join(G1)}</tbody></table>
</section>

<section class="pg">
{HDR}
<div class="sec" style="margin-top:0"><h2>AI surfaces</h2></div>
<table class="m">{THEAD}<tbody>{"".join(G2)}</tbody></table>
<div class="sec" style="margin-top:10px"><h2>Model assurance</h2></div>
<table class="m"><colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"></colgroup><tbody>{"".join(G3)}</tbody></table>
</section>

<section class="pg">
{HDR}
<div class="sec" style="margin-top:0"><h2>Four engines on one platform</h2></div>
<div class="levers">
  <div class="card"><h3>Native engines</h3><div class="sub">The RFP asks one OEM to supply all four (PQ-05).</div>
    <div class="pq"><div class="h">Engine</div><div class="h">{AK_LOGO}</div><div class="h">{KONG_LOGO}</div>
    {"".join(f'<div>{n}</div><div class="mk">{mark(a)}</div><div class="mk">{mark(k)}</div>' for n, a, k in PQ)}</div>
  </div>
  <div class="card"><h3>Kong partner options</h3><div class="sub">Kong lists third-party products for some areas. This comparison scores native capability only.</div>
    <div class="pills">{"".join(f'<span class="pill neu">{n}</span>' for n in PARTNERS)}</div>
  </div>
</div>

<div class="sec" style="margin-top:12px"><h2>UIDAI POC plan, 7 modules in 10 working days</h2></div>
<div class="poc">{poc()}</div>
<div class="foot">{ic("box", "ti")}<span>AccuKnox delivers all 7 POC modules from one control plane.</span></div>

<div class="sec" style="margin-top:14px"><h2>How this comparison was made</h2></div>
<div class="card method"><p>Kong ratings come from Kong's public documentation and resources, read on 30 October 2026. Partner products are not counted. <b>Supported</b> means documented natively. <b>Limited</b> means a partial form. <b>Not supported</b> means not found in public docs.</p>
<div class="src">{"".join(f'<span>{u}</span>' for u in SOURCES)}</div></div>
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
for page in n.pages:
    w.add_page(page)
w.add_page(PdfReader(str(A / "back-page.pdf")).pages[0])
w.add_metadata({"/Title": TITLE, "/Author": "AccuKnox"})
w.write(OUT)
print(f"{OUT}: {len(n.pages) + 1} pages")
