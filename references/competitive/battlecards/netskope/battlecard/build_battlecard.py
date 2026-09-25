"""Build the AccuKnox vs Netskope (AI Security) battlecard PDF.

Reference implementation for the PDF output mode of the accuknox-comparison-writer
skill. Copy this folder for a new competitor, then edit the row lists and the
PICK strip. Layout rules live in
.claude/skills/accuknox-comparison-writer/references/battlecard-pdf.md.

Run from the repo root:
    python references/competitive/battlecards/netskope/battlecard/build_battlecard.py [out.pdf]

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
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else BUILD / "accuknox-vs-netskope-ai-security.pdf"


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


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def row(icon, cap, ak, ns_k, ns, tk, refs=None, ak_k="yes"):
    r = ""
    if False:
        r = '<span class="refs">' + " · ".join(f'<a href="{u}">{t}</a>' for t, u in refs) + "</span>"
    return f"""<tr>
<td class="cap"><div class="capw">{ic(icon, 'capi')}<span>{cap}</span></div>{r}</td>
<td class="ak">{chip(ak_k)}{ul(ak)}</td>
<td class="ns {ns_k}">{chip(ns_k)}{ul(ns)}</td>
<td class="tk">{tk}</td></tr>"""


H = "https://help.accuknox.com/"
N = "https://docs.netskope.com/en/"

AI4SEC = [
    row("code", "AI SAST",
        ["AI flags false positives", "AI rates severity per finding"],
        "no", ["No SAST engine"],
        "Faster SAST triage"),
    row("globe", "AI DAST",
        ["4 scan types, baseline to active pentest", "Scans behind MFA logins", "Fails the CI/CD build on risk"],
        "no", ["No DAST engine"],
        "Tests the live app, past the login"),
    row("bot", "AgentZ",
        ["One sentence builds a security agent", "Default-deny sandbox, zero secrets", "Replayable trace of every action"],
        "lim", ["AISecOps triages DLP alerts only"],
        "Agents for any security job"),
    row("cross", "AI-powered pentesting",
        ["Automated attacks on app and model", "On demand or scheduled"],
        "no", ["LLM red teaming only", "No app pentest"],
        "Continuous pentests replace manual ones"),
]

SEC4AI = [
    row("cloud", "Cloud AI security",
        ["Agentless on AWS, Azure, GCP, OCI", "Pipeline graph shows exposure"],
        "lim", ["Preview only", "AWS, Azure, GCP"],
        "GA on 4 clouds",
        [("AK", H + "support-matrix/aiml-support-matrix/"), ("NS", N + "ai-platforms-discovery-and-security-posture-management")]),
    row("server", "On-prem &amp; self-hosted AI",
        ["<b>Control plane runs on-prem</b>, air-gapped", f'vLLM, Triton, Ollama, <span class="inl">{BRANDS["nvidia"]}</span>NVIDIA AI factories', "Live in 30 min to 4 h"],
        "no", ["Cloud-only control plane"],
        "Your AI stays in your data center",
        [("AK", H + "how-to/aiml-saas-vs-onprem/"), ("NS", N + "ai-gateway-overview")]),
    row("layers", "Managed agents",
        ["Agent-first view of every managed agent", '<span class="tags"><i>Bedrock AgentCore</i><i>Copilot Studio</i><i>Power Apps</i><i>M365 Agents</i><i>AI Foundry</i></span>', "Prompt Firewall enforces on each"],
        "lim", ["Preview config checks", "No managed-agent inventory"],
        "Every managed agent in one view",
        [("AgentCore", H + "integrations/bedrock-agentcore/"), ("Power Apps", H + "integrations/powerapps-integration/")]),
    row("browser", "Prompt Firewall &amp; browser",
        ["5 browsers, pushed by Intune", "Inspects prompts, files, pastes, replies", "Blocks personal accounts", "Allow, warn, redact, block"],
        "lim", ["Needs proxy steering", "Prompt DLP is an extra license"],
        "Full prompt control, no proxy",
        [("AK", H + "use-cases/prompt-firewall-overview/")]),
    row("gateway", "AI Gateway",
        ["Plugs into Azure APIM, Apigee, AWS API Gateway, Kong, LiteLLM, Bifrost", "SDK and REST API in the app"],
        "lim", ["Own 16 vCPU appliance", "Billed per gateway + transactions"],
        "No new appliance",
        [("AK", H + "integrations/ai-overview/"), ("NS", N + "ai-gateway-licensing-terms")]),
    row("box", "Agent runtime sandbox",
        ["<b>eBPF discovery</b> at the kernel", "<b>eBPF + LSM sandbox</b>: process, file, network", "LangGraph, CrewAI, n8n, MCP, no code change"],
        "noeq", ["Beta traffic filter only"],
        "Stops a rogue agent on the host",
        [("ModelArmor", H + "use-cases/modelarmor/"), ("NS", N + "agent-action-control")]),
    row("filescan", "Model security &amp; audit",
        ["Pickle, HDF5, SavedModel, ONNX scanned pre-load", "Supply chain and provenance checks"],
        "no", ["In-transit malware scan only"],
        "Unsafe models never load",
        [("AK", H + "how-to/ml-static-scan/")]),
    row("list", "AI BOM",
        ["CycloneDX 1.6 AIBOM, SBOM, CBOM", "GitHub Actions, Azure DevOps, Jenkins"],
        "no", ["No AIBOM"],
        "Models sit in the same BOM as code",
        [("AK", H + "getting-started/xbom-setup/")]),
    row("target", "Red teaming",
        ["14 probe families", "Reaches on-prem vLLM, Triton, Ollama"],
        "par", ["GA, with drift chart"],
        "AccuKnox adds on-prem models",
        [("AK", H + "use-cases/red-teaming/"), ("NS", N + "ai-red-teaming")], ak_k="par"),
    row("shield", "Runtime guardrails",
        ["14 policy classes: secrets, code, PII, PHI", "<b>Multi-turn</b> session scoring"],
        "lim", ["10 categories", "No multi-turn scoring"],
        "Catches split jailbreaks",
        [("AK", H + "how-to/llm-defense-app-onboard/"), ("NS", N + "ai-security-guardrails-profile")]),
    row("pulse", "AI Detection &amp; Response",
        ["Watches CloudTrail, Event Hub, GCP logs", "Auto-reverts risky changes", "Jira, ServiceNow, Slack, PagerDuty"],
        "no", ["No AI cloud log detection"],
        "Detect and revert AI misuse",
        [("AI-DR", H + "use-cases/aidr/")]),
]

THEAD = f"""<colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"></colgroup>
<thead><tr><th class="h-cap">Capability</th><th class="h-ak"><img src="{b64('accuknox-logo.png')}"></th>
<th class="h-ns"><img src="{b64('netskope-logo.png')}"></th><th class="h-tk">Takeaway</th></tr></thead>"""

AI4_CHIPS = [("code", "AI SAST"), ("globe", "AI DAST"), ("bot", "AgentZ"), ("cross", "AI pentesting")]
SEC_CHIPS = [("eyeoff", "Shadow AI"), ("cloud", "Cloud AI"), ("server", "On-prem AI"), ("layers", "Managed agents"),
             ("browser", "Prompt Firewall"), ("gateway", "AI Gateway"), ("box", "Agent sandbox"), ("filescan", "Model security"),
             ("list", "AI BOM"), ("target", "Red teaming"), ("shield", "Guardrails"), ("pulse", "AIDR")]


def tiles(items):
    return "".join(f'<div class="tile">{ic(i, "ti")}<span>{t}</span></div>' for i, t in items)


PICK = [("eyeoff", "Block shadow AI, beyond discovery"), ("server", "Run the control plane on-prem"),
        ("box", "Sandbox agents with eBPF"), ("filescan", "Scan models and ship an AIBOM")]

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
</style></head><body>

<section class="cover">
  <img class="blob b1" src="{b64('cover-blob-red.png')}"><img class="blob b2" src="{b64('cover-blob-blue.png')}">
  <img class="logo" src="{b64('accuknox-logo-cover.png')}">
  <div class="title"><div class="t1">AccuKnox</div><div class="vs">vs</div><div class="t2">Netskope</div><div class="t3">(AI Security)</div></div>
  <div class="groups">
    <div class="grp a"><h3><span class="n">01</span>AI for Security</h3><div class="tiles">{tiles(AI4_CHIPS)}</div></div>
    <div class="grp b"><h3><span class="n">02</span>Security for AI</h3><div class="tiles">{tiles(SEC_CHIPS)}</div></div>
  </div>
</section>

<section class="page">
<div class="topbar"></div>
<h1>Netskope identifies AI. AccuKnox <em>protects</em> it.</h1>
<div class="verdict"><div class="lbl">Pick AccuKnox to</div><div class="picks">{"".join(f'<div class="pick">{ic(i, "ti")}<span>{t}</span></div>' for i, t in PICK)}</div></div>
<div class="tally"><span><span class="dot" style="background:var(--win)"></span><b>15 of 16</b> AccuKnox leads</span>
<span><span class="dot" style="background:var(--no)"></span><b>8</b> Netskope not supported</span>
<span><span class="dot" style="background:#E0A340"></span><b>7</b> Netskope limited</span>
<span><span class="dot" style="background:var(--par)"></span><b>1</b> parity</span></div>

<div class="sec"><span class="num">01</span><h2>AI for Security</h2></div>
<table>{THEAD}<tbody>{"".join(AI4SEC)}</tbody></table>

<div class="sec" style="margin-top:12px"><span class="num">02</span><h2>Security for AI</h2></div>
<div class="panel">
  <div class="hd">{ic("eyeoff", "capi")}<h3>Shadow AI: identify <span class="neq">&ne;</span> protect</h3></div>
  <div class="vs2">
    <div class="col ak">
      <div class="top"><img src="{b64('accuknox-logo.png')}">{chip("yes")}</div>
      <div class="surfs">
        <div class="surf">{ic("browser", "ti")}<div><b>Browser</b><span>Block uploads, mask PII, stop secrets</span><span class="logos">{BRANDS["openai"]}{BRANDS["claude"]}{BRANDS["gemini"]}{BRANDS["copilot"]}</span></div></div>
        <div class="surf">{ic("server", "ti")}<div><b>Hosts</b><span>AI on VMs and containers, 7 categories. Linux, macOS</span></div></div>
        <div class="surf">{ic("monitor", "ti")}<div><b>Desktop (Beta)</b><span>Agents, tools and skills in Claude Code</span><span class="logos">{BRANDS["claude"]}</span></div></div>
        <div class="surf">{ic("term", "ti")}<div><b>CLI agents</b><span>Codex, Kiro, Claude Code via Prompt Firewall</span><span class="logos">{BRANDS["openai"]}{BRANDS["claude"]}</span></div></div>
      </div>
    </div>
    <div class="col ns">
      <div class="top"><img src="{b64('netskope-logo.png')}">{chip("lim")}</div>
      <ul>
        <li><b>Identifies</b> 3,300+ GenAI apps</li>
        <li><b>Guards</b> 20 listed apps inline</li>
        <li>Misses VMs and containers without its Client</li>
        <li>Detects only signature-file assets</li>
      </ul>
    </div>
  </div>
  <div class="ptk">AccuKnox enforces on every surface it discovers.</div>
</div>

<table style="break-before:page">{THEAD}<tbody>{"".join(SEC4AI)}</tbody></table>
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
