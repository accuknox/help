"""Build the AccuKnox vs DAXA (AI Security) battlecard PDF, for a customer-facing audience.

Copied from the Netskope reference build. Sources for
every cell sit in ../evidence-log.md. Layout rules live in
.claude/skills/accuknox-comparison-writer/references/battlecard-pdf.md.

Run from the repo root:
    python references/competitive/battlecards/daxa-hpe/battlecard/build_battlecard.py [out.pdf]

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
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else BUILD / "accuknox-vs-daxa-ai-security.pdf"


def b64(name):
    data = (A / name).read_bytes()
    mime = "jpeg" if name.endswith(".jpg") else "png"
    return f"data:image/{mime};base64," + base64.b64encode(data).decode()


def si(name, color):
    svg = (A / f"si_{name}.svg").read_text(encoding="utf-8")
    return svg.replace("<svg ", f'<svg class="brand" fill="#{color}" ', 1)


BRANDS = {
    "openai": si("openai", "000000"),
    "claude": si("claude", "D97757"),
    "gemini": si("googlegemini", "8E75B2"),
    "copilot": si("githubcopilot", "000000"),
    "ms": si("microsoft", "5E5E5E"),
    "nvidia": si("nvidia", "76B900"),
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
    "clip": '<path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"/>',
    "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
    "reply": '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    "up": '<path d="m5 12 7-7 7 7"/><path d="M12 19V5"/>',
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
    "np": ("c-np", "help", "Not shown"),
    "lead": ("c-win", "up", "Leads"),
}


def chip(k):
    cls, icon, label = CHIP[k]
    return f'<span class="chip {cls}">{ic(icon, "ci")}{label}</span>'


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def row(icon, cap, ak, dx_k, dx, tk, ak_k="yes"):
    return f"""<tr>
<td class="cap"><div class="capw">{ic(icon, 'capi')}<span>{cap}</span></div></td>
<td class="ak">{chip(ak_k)}{ul(ak)}</td>
<td class="ns {dx_k}">{chip(dx_k)}{ul(dx)}</td>
<td class="tk">{tk}</td></tr>"""


B = BRANDS
APPS = f'<span class="inl">{B["openai"]}{B["claude"]}{B["gemini"]}{B["copilot"]}{B["ms"]}</span>'
NV = f'<span class="inl">{B["nvidia"]}</span>'

PAIN = [
    row("shield", "Prompt &amp; response data",
        ["<b>Stateful</b> Prompt Firewall scores the session", "14 policy types: PII, PHI, secrets, code", "Custom policies in plain language", "Scans responses for leaked data"],
        "par", ["Safe Prompt strips sensitive data", "Multi-turn scoring not stated"],
        "Catches jailbreaks split across turns", ak_k="par"),
    row("browser", "SaaS AI on R&amp;D endpoints",
        [f"Browser plugin on 5 AI apps {APPS}", "<b>No SSL interception</b>, no proxy", "AI tool allow-list, upload file types", "Intune force-install"],
        "lim", ["Network gateway through SASE", "Needs <b>SSL termination, TLS inspection</b>"],
        "IP stays in, TLS stays intact"),
    row("eyeoff", "Shadow AI &amp; external LLMs",
        ["Host and cluster scans, 7 AI categories", "AI Gateway routes approved providers", "AI-BOM in CycloneDX"],
        "par", ["Discovers LLMs, agents, datastores", "Routes to sanctioned LLMs"],
        "Find it, then route it", ak_k="par"),
    row("box", "Over-permissioned agents",
        ["eBPF + LSM sandbox: process, file, network", "AgentZ: default-deny, zero secrets"],
        "par", ["MCP permission checks per tool", "Human confirm on destructive actions"],
        "Kernel control under the MCP layer", ak_k="par"),
    row("gateway", "AI gateway",
        ["Onboard by provider, model, key", "Prompt Firewall toggle per app", "Plugs into LiteLLM, Azure APIM, Apigee"],
        "par", ["OpenAI-compatible Safe Infer", "Model routing, token budgets"],
        "Reuse the gateway you run", ak_k="par"),
]

STACK = [
    row("filescan", "Model scan before deploy",
        ["Pickle, HDF5, SavedModel, ONNX", "Hugging Face, GitHub, on-prem model store", "Flags an unsafe pickle before load"],
        "np", ["No model file scanning shown"],
        "Unsafe models never reach production"),
    row("target", "AI red teaming",
        [f"Collectors: vLLM, {NV}Triton, Ollama, Bedrock", "Hundreds of probes, custom prompts", "Maps to OWASP LLM, MITRE ATLAS"],
        "np", ["No red teaming product shown"],
        "Test every hosted model on a schedule"),
    row("cloud", "AI-SPM",
        ["Agentless on AWS, Azure, GCP", "Managed agents and pipeline graph", "On-prem assets shown as Unmanaged"],
        "par", ["Risk graph of LLMs, frameworks, datastores"],
        "One inventory, cloud and private", ak_k="par"),
    row("pulse", "AI detection &amp; response",
        ["Watches AI cloud control-plane logs", "Tickets and auto-remediation"],
        "np", ["Agent audit trail only", "No control-plane detection shown"],
        "Risky AI changes get reverted"),
    row("server", "Air-gapped &amp; on-prem",
        ["<b>Full SaaS parity</b>, air-gapped", "Live in 30 min to 4 h", "Helm on Kubernetes or 3-node VMs"],
        "lim", ["Private cloud deployment shown", "Air-gapped mode not stated"],
        "Fits air-gapped private AI"),
    row("list", "MSSP &amp; multi-tenant",
        ["Isolated tenant per end customer", "MSSP viewer and editor access", "Partner branding, one dashboard"],
        "np", ["No MSSP or tenant model shown"],
        "Built to resell as a service"),
    row("pen", "Compliance &amp; AI GRC",
        ["MITRE ATLAS, OWASP LLM Top 10", "NIST AI RMF, AVID"],
        "par", ["EU AI Act checks", "GDPR, HIPAA, PCI, ISO 42001 named"],
        "Findings map to AI frameworks", ak_k="par"),
    row("term", "API &amp; MCP integration",
        ["MCP server: read-only, tenant-scoped", "Self-hostable, open source", "REST API and Python SDK"],
        "par", ["Pebblo MCP and SDK", "Pebblo is open source"],
        "Plugs into your own console", ak_k="par"),
    row("code", "AppSec for AI apps",
        ["AI SAST flags false positives", "DAST scans behind MFA logins", "AgentZ builds security agents"],
        "np", ["No SAST or DAST shown"],
        "One vendor for app and AI"),
]

THEAD = f"""<colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"></colgroup>
<thead><tr><th class="h-cap">Capability</th><th class="h-ak"><img src="{b64('accuknox-logo.png')}"></th>
<th class="h-ns"><span class="vn">DAXA</span><span class="vp">Pebblo, Safe Infer, Safe Agent</span></th><th class="h-tk">Takeaway</th></tr></thead>"""

G1_CHIPS = [("shield", "Prompt &amp; response data"), ("browser", "SaaS AI on endpoints"), ("eyeoff", "Shadow AI"),
            ("box", "Agent permissions"), ("gateway", "AI gateway")]
G2_CHIPS = [("filescan", "Model scanning"), ("target", "Red teaming"), ("cloud", "AI-SPM"), ("pulse", "AI-DR"), ("server", "Air-gapped"),
            ("list", "MSSP"), ("pen", "AI GRC"), ("term", "API &amp; MCP"), ("code", "AppSec")]


def tiles(items):
    return "".join(f'<div class="tile">{ic(i, "ti")}<span>{t}</span></div>' for i, t in items)


PICK = [("filescan", "Scan models before they deploy"), ("target", "Red team every hosted model"),
        ("browser", "Guard SaaS AI, no SSL interception"), ("server", "Run air-gapped, resell as MSSP")]


H = "https://help.accuknox.com/"
JOURNEY = [
    ("Scan the model", "Check each model file before it reaches the registry.",
     "Pickle, HDF5, SavedModel and ONNX.", "screen-model-scan.jpg", H + "how-to/ml-static-scan/"),
    ("Red team it", "Run probes against the served model on a schedule.",
     "Collectors reach vLLM, NVIDIA Triton and Ollama.", "screen-red-team.jpg", H + "use-cases/red-teaming/"),
    ("Guard the endpoint", "Route each application through the AI Gateway.",
     "Switch on the Prompt Firewall per application.", "screen-gateway.jpg", H + "getting-started/3.7-release/"),
    ("Guard the users", "Block a risky prompt inside the SaaS AI page.",
     "No SSL interception on the R&amp;D endpoint.", "screen-browser-block.jpg", H + "integrations/chrome-browser-integration/"),
]


def journey():
    out = ""
    for n, (title, l1, l2, img, url) in enumerate(JOURNEY, 1):
        out += f"""<a class="step" href="{url}"><div class="stxt"><span class="snum">{n}</span>
<h3>{title}</h3><p>{l1}</p><p class="s2">{l2}</p></div>
<div class="simg"><img src="{b64(img)}"></div></a>"""
    return out

html = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
@page {{ size:A4; margin:12mm 11mm }}
@page cover {{ margin:0 }}
:root{{--navy:#11206D;--blue:#0046FF;--ink:#1B223B;--mute:#5A637D;--line:#DDE2EE;
--win:#0B7A42;--win-bg:#E4F5EC;--no:#C80019;--no-bg:#FCE9EC;--lim:#A15C00;--lim-bg:#FFF1DC;--par:#4D4DD9;--par-bg:#ECECFB}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:'Space Grotesk',Arial,sans-serif;color:var(--ink);font-size:9pt;line-height:1.3}}
a{{color:var(--blue);text-decoration:none}}
.ic,.ci,.capi,.ti{{display:inline-block;vertical-align:middle}}
.brand{{width:11px;height:11px;vertical-align:-1.5px}}
.inl .brand{{margin-right:3px}}

/* cover */
.cover{{page:cover;width:210mm;height:297mm;position:relative;overflow:hidden;page-break-after:always;padding:20mm 17mm}}
.blob{{position:absolute;width:190mm;opacity:.9}}
.b1{{right:-70mm;top:-80mm}} .b2{{left:-80mm;bottom:-90mm}}
.cover .logo{{width:52mm;position:relative}}
.cover .title{{position:relative;margin-top:42mm;border-left:5px solid;border-image:linear-gradient(#F0505A,#1136D8) 1;padding-left:9mm}}
.cover .t1{{font-size:54pt;font-weight:700;color:#1136D8;line-height:1}}
.cover .vs{{font-size:30pt;color:#44505F;margin:4mm 0}}
.cover .t2{{font-size:54pt;font-weight:700;color:#1136D8;line-height:1}}
.cover .t3{{font-size:20pt;font-weight:500;color:var(--navy);margin-top:6mm}}
.groups{{position:absolute;left:17mm;right:17mm;bottom:22mm;display:grid;grid-template-columns:1fr 2.3fr;gap:5mm}}
.grp{{background:rgba(255,255,255,.82);border:1px solid #C9D2E6;border-radius:10px;padding:5mm}}
.grp h3{{margin:0 0 4mm;font-size:12pt;color:var(--navy)}}
.grp .n{{display:inline-block;background:var(--navy);color:#fff;border-radius:4px;font-size:8pt;padding:1px 6px;margin-right:6px;vertical-align:2px}}
.tiles{{display:grid;gap:2.5mm}}
.grp.a .tiles{{grid-template-columns:1fr}} .grp.b .tiles{{grid-template-columns:1fr 1fr 1fr}}
.tile{{display:flex;align-items:center;gap:6px;font-size:8.6pt;font-weight:600;color:var(--ink)}}
.ti{{width:17px;height:17px;color:var(--blue);flex:none;background:#EAF0FF;border-radius:5px;padding:3px;box-sizing:content-box}}

/* body */
.page{{padding:0}}
.topbar{{height:4px;background:linear-gradient(90deg,#1136D8,#6B3FD1 55%,#F0505A);border-radius:2px;margin-bottom:9px}}
h1{{font-size:20pt;line-height:1.1;margin:0 0 8px;color:var(--navy)}}
h1 em{{font-style:normal;color:var(--blue)}}
.verdict{{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:stretch;border:1.5px solid var(--blue);border-radius:10px;padding:8px 10px;background:#F4F7FF;margin-bottom:6px}}
.verdict .lbl{{font-weight:700;font-size:10pt;color:var(--blue);display:flex;align-items:center;max-width:26mm;line-height:1.15}}
.picks{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}}
.pick{{display:flex;gap:6px;align-items:center;font-weight:600;font-size:8.8pt;line-height:1.2}}
.pick .ti{{background:#fff}}
.tally{{display:flex;gap:14px;font-size:8.2pt;color:var(--mute);margin:0 2px 8px;align-items:center}}
.tally b{{color:var(--ink)}}
.dot{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px;vertical-align:0}}

.sec{{display:flex;align-items:center;gap:8px;margin:10px 0 5px;break-after:avoid}}
.sec .num{{font-size:8.5pt;font-weight:700;color:#fff;background:var(--navy);border-radius:4px;padding:2px 7px}}
.sec h2{{font-size:14pt;margin:0;color:var(--navy)}}

table{{width:100%;border-collapse:separate;border-spacing:0;table-layout:fixed}}
col.c1{{width:22%}}col.c2{{width:38%}}col.c3{{width:24%}}col.c4{{width:16%}}
thead th{{padding:5px 8px 6px;text-align:left;border-bottom:2px solid var(--navy);font-size:7.6pt;text-transform:uppercase;letter-spacing:.5px;color:var(--mute);vertical-align:bottom}}
th.h-ak{{background:#EEF3FF;border-radius:8px 8px 0 0;border-bottom-color:var(--blue)}}
th.h-ak img{{height:17px}} th.h-ns img{{height:22px}}
tbody tr{{break-inside:avoid}}
td{{vertical-align:top;padding:5px 8px;border-bottom:1px solid var(--line)}}
td.cap .capw{{display:flex;gap:7px;align-items:flex-start;font-weight:700;font-size:11.5pt;line-height:1.15;color:var(--navy)}}
.capi{{width:18px;height:18px;flex:none;color:var(--blue);margin-top:1px}}
td.cap .refs{{display:block;font-size:6.8pt;margin:4px 0 0 25px}}
td.ak{{background:#F3F7FF;border-left:3px solid var(--win)}}
td.ns{{border-left:3px solid var(--line)}}
td.ns.no,td.ns.noeq{{border-left-color:var(--no)}} td.ns.lim{{border-left-color:#E0A340}} td.ns.par{{border-left-color:var(--par)}}
td.tk{{font-weight:700;font-size:8.2pt;color:var(--blue);line-height:1.25}}
td ul{{margin:4px 0 0;padding-left:12px}} td li{{margin:0 0 2px}} td li::marker{{color:#9AA3BD}}
td.ns li{{color:#4A5270}}
.chip{{display:inline-flex;align-items:center;gap:3px;font-weight:700;font-size:6.9pt;letter-spacing:.3px;padding:1.5px 7px 1.5px 5px;border-radius:9px;text-transform:uppercase}}
.ci{{width:9px;height:9px;stroke-width:3}}
.c-win{{background:var(--win-bg);color:var(--win)}} .c-no{{background:var(--no-bg);color:var(--no)}}
.c-lim{{background:var(--lim-bg);color:var(--lim)}} .c-par{{background:var(--par-bg);color:var(--par)}}
.tags i{{font-style:normal;display:inline-block;background:#fff;border:1px solid #C9D6F5;border-radius:4px;padding:0 4px;margin:1px 2px 1px 0;font-size:7.8pt;font-weight:600;color:var(--navy)}}

/* shadow AI */
.panel{{border:1.5px solid var(--navy);border-radius:10px;padding:9px 10px;margin:2px 0 10px;break-inside:avoid;background:linear-gradient(180deg,#F4F7FF,#fff 55%)}}
.panel .hd{{display:flex;align-items:center;gap:8px;margin-bottom:7px}}
.panel .hd .capi{{width:22px;height:22px}}
.panel h3{{margin:0;font-size:14pt;color:var(--navy)}}
.panel h3 .neq{{color:var(--no)}}
.vs2{{display:grid;grid-template-columns:62fr 38fr;gap:8px}}
.col{{border-radius:8px;padding:7px 9px;background:#fff}}
.col.ak{{border:1px solid #BFD0FF}} .col.ns{{border:1px solid #F4C3CB}}
.col .top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}
.col .top img{{height:14px}} .col.ns .top img{{height:19px}}
.surfs{{display:grid;grid-template-columns:1fr 1fr;gap:7px}}
.surf{{display:flex;gap:7px;align-items:flex-start}}
.surf .ti{{width:16px;height:16px}}
.surf b{{display:block;font-size:9.2pt;color:var(--navy)}}
.surf span{{font-size:8pt;color:#3A4262}}
.surf .logos{{display:block;margin-top:2px}} .surf .logos .brand{{width:12px;height:12px;margin-right:4px}}
.col.ns ul{{margin:0;padding-left:12px;font-size:8.6pt}} .col.ns li{{margin:0 0 4px;color:#4A5270}}
.col.ns li b{{color:var(--ink)}}
.ptk{{margin-top:7px;font-weight:700;color:var(--blue);font-size:9pt}}

/* journey page */
.jpage{{break-before:page}}
.jpage h1{{font-size:19pt;margin:6px 0 16px}}
.journey{{display:grid;gap:8mm}}
.step{{display:grid;grid-template-columns:50mm 1fr;gap:8mm;align-items:center;color:var(--ink);break-inside:avoid}}
.snum{{display:inline-flex;width:9mm;height:9mm;border-radius:50%;background:var(--blue);color:#fff;font-weight:700;font-size:12pt;align-items:center;justify-content:center}}
.stxt h3{{font-size:15pt;color:var(--navy);margin:3mm 0 2mm}}
.stxt p{{font-size:9.6pt;line-height:1.45;margin:0 0 1.5mm;color:#2A3352}}
.stxt p.s2{{color:var(--mute)}}
.simg{{height:55mm;border:1px solid #C9D2E6;border-radius:10px;background:#F6F8FD;display:flex;align-items:center;justify-content:center;padding:2.5mm;overflow:hidden}}
.simg img{{max-width:100%;max-height:100%;border-radius:5px}}
/* two-rival overrides */
h1{{font-size:16.5pt;margin-bottom:6px}}
.sec{{margin:12px 0 7px}} .sec h2{{font-size:13pt}}
.verdict{{padding:6px 10px}} .tally{{margin:4px 2px 10px}}
body{{font-size:8.3pt}}
col.c1{{width:16.5%}}col.c2{{width:30%}}col.c3{{width:19.5%}}col.c4{{width:20.5%}}col.c5{{width:13.5%}}
td{{padding:7px 8px}}
td.cap .capw{{font-size:10pt;gap:6px}} .capi{{width:16px;height:16px}}
td.tk{{font-size:7.8pt}}
td ul{{margin:3px 0 0;padding-left:11px}} td li{{margin:0 0 1.5px}}
th.h-ns{{line-height:1.1}}
.vn{{display:block;font-size:10.5pt;font-weight:700;color:var(--navy);text-transform:none;letter-spacing:0}}
.vp{{display:block;font-size:6.8pt;color:var(--mute);text-transform:none;letter-spacing:0}}
.c-np{{background:#EEF0F5;color:#5A637D}} td.ns.np{{border-left-color:#B4BACB}} td.ns.lead{{border-left-color:var(--win)}}
.inl .brand{{margin-right:2px}}
.cover .t2{{font-size:38pt;line-height:1.08}}
.cover .title{{margin-top:30mm}}
.groups{{grid-template-columns:1fr 1fr}}
.grp.a .tiles,.grp.b .tiles{{grid-template-columns:1fr 1fr}}
.modes{{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}}
.mode{{background:#fff;border:1px solid #BFD0FF;border-radius:8px;padding:6px 7px;color:var(--ink);display:block}}
.mode .mh{{display:flex;align-items:center;gap:5px;font-weight:700;font-size:9pt;color:var(--navy);margin-bottom:3px}}
.mode .ti{{width:13px;height:13px}}
.mode .ms{{display:block;font-size:7.6pt;color:#3A4262;line-height:1.25}}
.mode .mb{{display:block;font-size:7.6pt;font-weight:700;color:var(--blue);margin-top:3px;line-height:1.25}}
.panel{{padding:8px 9px;margin:2px 0 8px}} .panel h3{{font-size:12.5pt}}
.screens{{display:grid;grid-template-columns:1.18fr 1.4fr 1.42fr;gap:8px;margin-top:9px;align-items:start}}
.shot{{display:block;border:1px solid #C9D2E6;border-radius:8px;overflow:hidden;background:#fff}}
.shot img{{display:block;width:100%}}
.shot span{{display:block;padding:4px 7px;font-size:7.8pt;font-weight:700;color:var(--navy);border-top:1px solid var(--line)}}

/* single-rival build */
col.c1{{width:20%}}col.c2{{width:37%}}col.c3{{width:27%}}col.c4{{width:16%}}
body{{font-size:8.8pt}}
td{{padding:7px 9px}}
td.cap .capw{{font-size:10.5pt}}
.cover .t2{{font-size:54pt}}
.cover .t3{{font-size:17pt}}
.cover .t4{{font-size:11pt;color:var(--mute);margin-top:3mm;font-weight:500}}
.verdict{{grid-template-columns:1fr;margin-bottom:12px}}
.asks{{display:grid;grid-template-columns:repeat(4,1fr);gap:7px}}
.ask{{background:#fff;border:1px solid #BFD0FF;border-radius:8px;padding:7px 8px}}
.ask .ah{{display:flex;align-items:center;gap:5px;font-weight:700;font-size:8.8pt;color:var(--navy);margin-bottom:3px;line-height:1.2}}
.ask .ti{{width:13px;height:13px}}
.ask .ab{{display:block;font-size:7.9pt;color:#3A4262;line-height:1.3}}
.know{{margin-top:7px;font-size:8.2pt;color:#3A4262}} .know b{{color:var(--no)}}
</style></head><body>

<section class="cover">
  <img class="blob b1" src="{b64('cover-blob-red.png')}"><img class="blob b2" src="{b64('cover-blob-blue.png')}">
  <img class="logo" src="{b64('accuknox-logo-cover.png')}">
  <div class="title"><div class="t1">AccuKnox</div><div class="vs">vs</div><div class="t2">DAXA</div><div class="t3">(AI Security)</div></div>
  <div class="groups">
    <div class="grp a"><h3><span class="n">01</span>Data, Prompts and Agents</h3><div class="tiles">{tiles(G1_CHIPS)}</div></div>
    <div class="grp b"><h3><span class="n">02</span>Models, Posture and Operations</h3><div class="tiles">{tiles(G2_CHIPS)}</div></div>
  </div>
</section>

<section class="page">
<div class="topbar"></div>
<h1>DAXA controls data access. AccuKnox secures the <em>whole AI stack</em>.</h1>
<div class="verdict"><div class="picks">{"".join(f'<div class="pick">{ic(i, "ti")}<span>{t}</span></div>' for i, t in PICK)}</div></div>


<div class="sec"><span class="num">01</span><h2>Data, Prompts and Agents</h2></div>
<table>{THEAD}<tbody>{"".join(PAIN)}</tbody></table>

<div class="sec" style="break-before:page"><span class="num">02</span><h2>Models, Posture and Operations</h2></div>
<table>{THEAD}<tbody>{"".join(STACK)}</tbody></table>
</section>

<section class="page jpage">
<div class="topbar"></div>
<h1>Where AccuKnox sits in your <em>AI stack</em>.</h1>
<div class="journey">{journey()}</div>
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
