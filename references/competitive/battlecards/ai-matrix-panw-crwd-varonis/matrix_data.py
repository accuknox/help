"""Content for the AccuKnox vs Palo Alto Networks, CrowdStrike, Varonis and Zscaler AI security matrix.

Competitor cells come from research/<vendor>.json, which holds the vendor URL and a
verbatim quote for every row, read with Firecrawl on 2026-09-29 (Zscaler on 2026-10-01). AccuKnox cells come
from help.accuknox.com pages in docs/ and from
references/source-of-truth/ai-security-data-points.md. Tier I and tier A AccuKnox
claims are listed in evidence-log.md.

Status keys: yes Supported, lim Limited, no Not supported, noeq No equivalent, par Parity.
Every bullet is a short sentence with a verb. The subject is the vendor in the column.
"""
import json
import pathlib

_R = pathlib.Path(__file__).resolve().parent / "research"
_urls = set()
for _f in ("palo-alto", "crowdstrike", "varonis", "zscaler"):
    for _r in json.loads((_R / f"{_f}.json").read_text(encoding="utf-8"))["rows"].values():
        _urls.add(_r["url"])
        _urls.update(_r.get("extra_urls", []))

SOON = '<span class="soon">Coming soon</span>'
BETA = '<span class="beta">Beta</span>'

HEADLINE = "AccuKnox Covers All 8 Modules, On-Prem and in the Cloud"

PICK = [
    ("server", "Run the whole platform on-prem or air-gapped"),
    ("plug", "Use the AI gateways you already run"),
    ("box", "Sandbox AI agents at the kernel with eBPF"),
    ("bot", "Build security agents with AgentZ"),
]

PROOF = [
    "Ranked #1 at BSides",
    "Ranked #1 by GigaOm",
    "Ranked #1 in Andrew Green's AI firewall report",
    "Built with SRI International",
]

# At a glance: the AI for Security group plus the 8 modules, one chip per vendor.
GLANCE = [
    {"n": "", "icon": "bot", "m": "AgentZ", "ak": "Sandboxed agents, on-prem too",
     "v": [("yes", "SaaS-only SOC agents"), ("yes", "Cloud-only SOC agents"), ("lim", "SOC assistant only")]},
    {"n": "01", "icon": "cloud", "m": "AI-SPM", "ak": "Cloud, on-prem and endpoints",
     "v": [("lim", "SaaS only, extra license"), ("lim", "SaaS only"), ("lim", "SaaS only")]},
    {"n": "02", "icon": "box", "m": "Agentic AI Security", "ak": "Kernel sandbox for each agent",
     "v": [("lim", "Hooks for coding agents"), ("lim", "Endpoint agent types"), ("lim", "Hooks, no host control")]},
    {"n": "03", "icon": "pulse", "m": "AI Detect and Respond", "ak": "Reads cloud AI logs, remediates",
     "v": [("yes", "Audit-log analytics"), ("lim", "Bedrock logs on AWS only"), ("lim", "Gateway data only")]},
    {"n": "04", "icon": "shield", "m": "Guardrails and Prompt Firewall", "ak": "Browser, CLI, SDK, 6 gateways",
     "v": [("lim", "Needs SASE, skips replies"), ("lim", "Reports replies only"), ("lim", "200k prompt cap")]},
    {"n": "05", "icon": "target", "m": "Red Teaming and Pen Testing", "ak": "Tests on-prem models on a schedule",
     "v": [("par", "500+ attacks"), ("lim", "Service engagement"), ("par", "Tests LLMs, agents, MCP")]},
    {"n": "06", "icon": "key", "m": "AI Identity Security", "ak": "AgentZ scopes credentials",
     "v": [("lim", "Separate CyberArk platform"), ("lim", "Agentic IdP not released"), ("yes", "Agent intent control")]},
    {"n": "07", "icon": "filescan", "m": "AI Model and Dataset Security", "ak": "Scans, gates CI, sandboxes",
     "v": [("yes", "Public Hugging Face only"), ("lim", "Formats not listed"), ("lim", "Formats not listed")]},
    {"n": "08", "icon": "scale", "m": "AI Compliance and Governance", "ak": "CycloneDX AIBOM, 4 frameworks",
     "v": [("lim", "No AIBOM export shown"), ("noeq", "Maps only its own AI"), ("lim", "Reads AIBOMs, no export")]},
]


def _v(p, c, v):
    return {"panw": p, "crwd": c, "vrns": v}


AI4SEC = [
    {"icon": "bot", "cap": "AgentZ Agent Platform", "tk": "Build security agents that run on your servers.",
     "ak": ["Builds a security agent from one sentence.", "Runs each agent in a <b>default-deny sandbox</b>.",
            "Runs on-prem or air-gapped. Open source."],
     "v": _v(("yes", ["Builds custom AgentiX agents.", "Runs only as a SaaS tenant."]),
             ("yes", ["Builds no-code AgentWorks agents.", "Runs only in the Falcon cloud."]),
             ("lim", ["Offers the Athena AI SOC assistant.", "Has no agent builder for customers."]))},
]

SPM = [
    {"icon": "cloud", "cap": "Cloud AI Posture", "tk": "See all cloud AI with one license.",
     "ak": ["Connects read-only to AWS, Azure and GCP.", "Lists models, datasets and compute.",
            "Draws a graph of exposure paths."],
     "v": _v(("yes", ["Covers AWS, Azure and GCP.", "Needs a separate Cortex C1 license."]),
             ("yes", ["Covers AWS, Azure and GCP.", "Lists Bedrock, SageMaker and Vertex AI."]),
             ("yes", ["Lists Bedrock, AgentCore, Foundry, Gemini.", "Does not list SageMaker."]))},
    {"icon": "server", "cap": "On-Prem and Self-Hosted AI", "tk": "Keep AI data and the console on-prem.",
     "ak": ["Runs the <b>control plane on-prem</b> or air-gapped.", "Covers vLLM, Triton, Ollama and NVIDIA NIM.",
            "Installs in 30 min to 4 h, with all SaaS features."],
     "v": _v(("lim", ["Runs the firewall on ESXi and KVM.", "Keeps the console in SaaS."]),
             ("lim", ["Finds LLM runtimes on endpoints.", "Offers no on-prem console."]),
             ("lim", ["Runs the gateway data plane on-prem.", "Keeps the console in SaaS."]))},
]

SHADOW = {
    "title": "Shadow AI Discovery and Blocking",
    "ak": [
        ("browser", "Browser", "Blocks uploads, masks PII and stops secrets.", ["openai", "claude", "gemini", "copilot"]),
        ("server", "Hosts and clusters", "Finds 7 types of AI on VMs and Kubernetes. macOS in Beta.", ["k8s", "ollama", "hf"]),
        ("monitor", "Desktop (Beta)", "Lists agents, tools and skills in Claude Code.", ["claude"]),
        ("term", "CLI agents", "Routes Codex, Kiro and Claude Code through the firewall.", ["openai", "claude"]),
    ],
    "v": _v(("lim", ["Lists <b>about 2,300</b> GenAI apps.", "Applies inline DLP to <b>about 380</b>.",
                     "Needs NGFW, Prisma Access or Prisma Browser."]),
            ("lim", ["Finds AI on endpoints (GA).", "Only reports desktop AI apps, on Windows.",
                     "Never blocks browser replies."]),
            ("lim", ["Finds shadow AI in DNS and proxy logs.", "Needs a vendor hook for inline control.",
                     "Shows no browser prompt control."])),
    "tk": "AccuKnox blocks risky use on all four surfaces it finds.",
}

AGENTIC = [
    {"icon": "layers", "cap": "Managed Agents", "tk": "See every managed agent in one list.",
     "ak": ["Shows each agent's IAM role and tools.",
            '<span class="tags"><i>Bedrock AgentCore</i><i>Bedrock Agent</i><i>Copilot Studio</i>'
            '<i>M365 Agents</i><i>AI Foundry</i><i>Power Apps</i></span>',
            "Applies the Prompt Firewall to each one."],
     "v": _v(("yes", ["Lists 10 SaaS agent platforms.", "Does not list AgentCore."]),
             ("lim", ["Checks Copilot Studio tool inputs only.", "Does not scan tool outputs."]),
             ("yes", ["Covers Agentforce, Copilot Studio, Foundry.", "Focuses on data permissions."]))},
    {"icon": "plug", "cap": "MCP Security", "tk": "Contain MCP servers on the host.",
     "ak": ["Finds MCP servers on hosts and clusters.", "Sandboxes MCP servers at the kernel.",
            "Lets AgentZ approve each MCP server once."],
     "v": _v(("yes", ["Runs an MCP gateway and registry.", "Needs the agent to call its scan tool."]),
             ("yes", ["Runs a local MCP proxy per client.", "Needs Node.js and stdio servers."]),
             ("yes", ["Finds and blocks MCP servers.", "Needs a gateway or hook in the path."]))},
    {"icon": "box", "cap": "Agent Runtime Sandbox", "tk": "Stop a rogue agent on the host.",
     "ak": ["Controls process, file and network with <b>eBPF and LSM</b>.",
            "Covers LangGraph, n8n and MCP, no code change.",
            "Blocks reads of <code>/root/.aws/credentials</code>."],
     "v": _v(("lim", ["Hooks coding agents through Cortex AES.", "Needs a separate subscription."]),
             ("lim", ["Allows or blocks agent types.", "Covers managed endpoints, not servers."]),
             ("noeq", ["Gates tool calls through hooks.", "Shows no host-level control."]))},
]

DR_RT = [
    {"icon": "pulse", "cap": "AI Cloud Activity Detection", "tk": "Catch and undo risky AI changes.",
     "ak": ["Reads CloudTrail and Azure Event Hub.", "Covers SageMaker, Bedrock, Azure ML and Azure OpenAI.",
            "Opens tickets and fixes issues automatically."],
     "v": _v(("yes", ["Alerts on Bedrock and SageMaker logs.", "Needs 14 days to activate and 30 to learn."]),
             ("lim", ["Reads Bedrock logs on AWS only.", "Monitors and does not block."]),
             ("lim", ["Uses gateway and hook data.", "Shows no CloudTrail AI detection."]))},
    {"icon": "zap", "cap": "Runtime Blocking", "tk": "Block at the prompt and at the kernel.",
     "ak": ["Blocks, cleans or logs each prompt.", "Stops bad processes with KubeArmor.",
            "Works the same in SaaS and on-prem."],
     "v": _v(("yes", ["Allows or blocks per detection.", "Caps sync scans at 2 MB."]),
             ("yes", ["Blocks both ways in SDK and gateway.", "Only reports in other collectors."]),
             ("yes", ["Blocks, edits, alerts or logs.", "Needs a gateway, SDK or hook."]))},
    {"icon": "target", "cap": "AI Red Teaming", "tk": "Red team on-prem models on a schedule.",
     "ak": ["Maps 4 attack groups to OWASP LLM and MITRE ATLAS.", "Runs multi-turn, encoding and hidden-prompt attacks.",
            "Tests Ollama and custom endpoints on a schedule."], "ak_k": "par",
     "v": _v(("par", ["Runs 500+ attacks in 50+ techniques.", "Needs a separate license."]),
             ("lim", ["Sells red teaming as a service.", "Shows no automated product."]),
             ("par", ["Tests agents, models and MCP.", "Does not publish its attack count."]))},
]

GATEWAY = {
    "title": "One Prompt Firewall, Four Ways In",
    "modes": [
        ("browser", "Chat apps in a browser", "ChatGPT, Claude, Gemini, Copilot", "Browser plugin", "Chrome, Edge, Firefox, Safari, Brave"),
        ("term", "CLI coding agents", "Claude Code, Codex, Kiro", "Gateway proxy", "One proxy setting on the tool"),
        ("bot", "Local AI agents", "LangGraph, n8n, your own apps", "SDK or AI gateway", "Python SDK, LiteLLM or Bifrost"),
        ("cloud", "Cloud AI agents", "Bedrock AgentCore, Copilot Studio", "API gateway", "Azure APIM, AWS API Gateway, Apigee"),
    ],
    "gateways": ["LiteLLM", "Bifrost", "Kong AI", "Azure APIM", "AWS API Gateway", "Apigee",
                 f"AccuKnox AI Gateway {SOON}"],
    "points": [
        ("server", "Runs anywhere", "Works in SaaS, on-prem or air-gapped, with one policy set."),
        ("zap", "Adds no appliance", "Plugs into the gateway your team runs today."),
        ("shield", "Tracks the session", "Scores the whole chat for split jailbreaks."),
        ("list", "Logs everything", "Keeps every prompt and reply for audit."),
    ],
    "v": _v(("lim", ["Runs its own gateway, from Portkey.", "Lists it for the Americas only.",
                     "Bills per token on NGFW credits."]),
            ("lim", ["Has its own gateway in pre-beta.", "Connects to 7 other gateways.",
                     "Does not list AWS API Gateway or Bifrost."]),
            ("lim", ["Runs its own Atlas gateway.", "Caps use at <b>200k prompts</b> a month per AI system.",
                     "Bills per AI system."])),
    "tk": "AccuKnox works inside the gateway you already run, in the cloud or on-prem.",
}

GUARD = [
    {"icon": "browser", "cap": "Browser Prompt Protection", "tk": "Control prompts in any browser.",
     "ak": ["Runs in 5 browsers. Intune pushes it.", "Checks prompts, files, pastes and replies.",
            "Reads Purview labels. Blocks personal accounts.", "Allows, warns, redacts or blocks."],
     "v": _v(("lim", ["Needs SASE or Prisma Browser.", "Does not scan or log replies."]),
             ("lim", ["Needs managed Windows or macOS.", "Only reports replies."]),
             ("noeq", ["Blocks phishing sites only.", "Reads ChatGPT logs after use."]))},
    {"icon": "term", "cap": "CLI Coding Agents", "tk": "Stop coding agents from leaking secrets.",
     "ak": ["Covers Codex, Kiro and Claude Code.", "Blocks prompt injection and jailbreaks.",
            "Stops leaks of secrets and code."],
     "v": _v(("lim", ["Hooks agents through Cortex AES.", "Needs a separate subscription."]),
             ("lim", ["Has a Claude Code collector.", "Only reports other CLIs, on Windows."]),
             ("yes", ["Hooks Claude Code, Cursor and Codex.", "Needs one hook per tool."]))},
    {"icon": "shield", "cap": "Guardrail Depth", "tk": "Catch jailbreaks split across turns.",
     "ak": ["Applies 14 policy types, from PII to code.", "Scores the <b>whole session</b>.",
            "Blocks, cleans or logs."],
     "v": _v(("yes", ["Runs 9 detection services.", "Shows no session scoring."]),
             ("yes", ["Runs 11 detectors, 200+ attack types.", "Shows no multi-turn scoring."]),
             ("par", ["Scores the whole session.", "Does not publish its category count."]))},
]

ID_MODEL = [
    {"icon": "key", "cap": "Agent Identity", "tk": "Keep credentials out of agents.",
     "ak": ["Injects scoped credentials at run time.", "Denies write, push and delete by default.",
            "Checks roles on every agent action.", f"Adds the AI Identity module. {SOON}"],
     "v": _v(("lim", ["Uses CyberArk, a separate platform.", "Shows no per-tool-call scope."]),
             ("lim", ["Announced an agent IdP, not released.", "Uses SGNL for identity."]),
             ("yes", ["Blocks agents that drift from intent.", "Needs the Varonis DSP for full control."]))},
    {"icon": "filescan", "cap": "Model File Security", "tk": "Block unsafe models before they load.",
     "ak": ["Scans Pickle, HDF5, SavedModel, ONNX and checkpoints.", "Scans Hugging Face and GitHub in the pull request.",
            "Sandboxes any model that gets through."],
     "v": _v(("yes", ["Scans 50+ model formats.", "Does not support private Hugging Face repos."]),
             ("lim", ["Scans for trojans and backdoors.", "Does not list formats or Hugging Face."]),
             ("lim", ["Names model artifact scans.", "Does not list formats."]))},
    {"icon": "db", "cap": "Dataset Security", "tk": "Check training data before and during use.",
     "ak": ["Scans datasets for exposure, PII and PHI.", "Flags PII and membership inference risk.",
            "Alerts on unapproved training datasets."],
     "v": _v(("yes", ["Classifies PII in datasets.", "Needs a Cortex AI-SPM license."]),
             ("lim", ["Maps AI data flows in early beta.", "Shows no poisoning detection."]),
             ("yes", ["Classifies training data stores.", "Alerts when training data changes."]))},
]

GRC = [
    {"icon": "list", "cap": "AI Bill of Materials", "tk": "List models in the same BOM as code.",
     "ak": ["Exports a CycloneDX AIBOM with SBOM and CBOM.", "Builds it with knoxctl, image scans or GitHub Actions.",
            "Supports EO 14028 and the EU AI Act."],
     "v": _v(("lim", ["Names an AI-BOM in its mapping.", "Shows no CycloneDX export."]),
             ("lim", ["Keeps an AI model inventory.", "Shows no AIBOM export."]),
             ("lim", ["Reads vendor AIBOMs.", "Shows no AIBOM export."]))},
    {"icon": "scale", "cap": "Framework Mapping", "tk": "Prove controls with runtime logs.",
     "ak": ["Maps MITRE ATLAS, OWASP LLM, NIST AI RMF and AVID.", "Logs every prompt and reply for audit.",
            "Keeps the same mapping on-prem.", f"Adds the AI-GRC module. {SOON}"],
     "v": _v(("yes", ["Maps OWASP, EU AI Act, NIST, MITRE.", "Shows no ISO 42001 mapping."]),
             ("noeq", ["Certifies only its own Charlotte AI.", "Shows no mapping for customer AI."]),
             ("yes", ["Maps EU AI Act, NIST and ISO 42001.", "Shows no OWASP LLM or ATLAS mapping."]))},
]

# Where each control plane runs. Shown under the GRC table.
DEPLOY = {
    "title": "Where the Console Runs",
    "ak": ("SaaS, on-prem or air-gapped", "Installs with Helm on Kubernetes or on 3 VMs."),
    "v": _v(("SaaS only", "Runs in Strata Cloud Manager and Cortex."),
            ("SaaS only", "Runs in the US-1, US-2 and EU-1 clouds."),
            ("SaaS only", "Retires self-hosted Varonis on 31 Dec 2026.")),
}

PAGES = [
    {"kind": "table", "mod": "Module 01", "rows": SPM, "shadow": True, "title": "AI Security Posture Management"},
    {"kind": "table", "mod": "AgentZ and Module 02", "rows": AI4SEC + AGENTIC, "title": "AgentZ and Agentic AI Security"},
    {"kind": "table", "mod": "Modules 03 and 05", "rows": DR_RT, "title": "AI Detection, Response and Red Teaming"},
    {"kind": "gateway", "mod": "Module 04", "title": "The Prompt Firewall Works in 6 AI Gateways"},
    {"kind": "table", "mod": "Module 04", "rows": GUARD, "title": "Guardrails and Prompt Firewall"},
    {"kind": "table", "mod": "Modules 06 and 07", "rows": ID_MODEL, "title": "Agent Identity, Model and Dataset Security"},
    {"kind": "table", "mod": "Module 08", "rows": GRC, "deploy": True, "title": "AI Compliance and Governance"},
]

# The contents page lists the 9 modules only. The number is the index into PAGES.
MODULES = [
    ("Module 01", "AI Security Posture Management", 0),
    ("Module 02", "Agentic AI Security", 1),
    ("Module 03", "AI Detect and Respond", 2),
    ("Module 04", "AI Guardrails and Prompt Firewall", 3),
    ("Module 05", "AI Red Teaming and Pen Testing", 2),
    ("Module 06", "AI Identity Security", 5),
    ("Module 07", "AI Model and Dataset Security", 5),
    ("Module 08", "AI Compliance and Governance", 6),
    ("AgentZ", "Agentic AI Harness", 1),
]

# Zscaler column, added 2026-10-01 from research/zscaler.json. Each cell joins the vendor dicts above
# under the key "zs", so the Palo Alto, CrowdStrike and Varonis cells stay exactly as written.
ZS = {
    "AgentZ Agent Platform": ("lim", ["Runs prebuilt Agentic SOC agents.", "Has no agent builder for customers."]),
    "Cloud AI Posture": ("yes", ["Covers AWS, Azure and GCP.", "Lists Bedrock models used in the last 90 days."]),
    "On-Prem and Self-Hosted AI": ("lim", ["Calls its SaaS API even for private LLMs.", "Keeps the console in SaaS."]),
    "Managed Agents": ("yes", ["Lists Bedrock, Foundry and Copilot Studio agents.", "Guards AgentCore only through a code wrapper."]),
    "MCP Security": ("lim", ["Lists MCP servers found in the cloud.", "Has no help docs for its MCP broker yet."]),
    "Agent Runtime Sandbox": ("lim", ["Finds risky AI tools on employee devices.", "Shows no process control for server agents."]),
    "AI Cloud Activity Detection": ("lim", ["Flags AI misconfigurations in 3 clouds.", "Needs human approval for each fix."]),
    "Runtime Blocking": ("yes", ["Allows, blocks or redacts in proxy mode.", "Leaves blocking to the app in API mode."]),
    "AI Red Teaming": ("par", ["Runs 25+ probes and 5,000+ attacks.", "Tests MCP servers and voice, image input."]),
    "Browser Prompt Protection": ("yes", ["Checks prompts and replies through ZIA.", "Needs Client Connector on each device."]),
    "CLI Coding Agents": ("yes", ["Hooks Claude Code, Codex and Cursor.", "Needs one hook per tool."]),
    "Guardrail Depth": ("par", ["Lists 14 detector types.", "Added multi-turn guardrails in June 2026."]),
    "Agent Identity": ("lim", ["Maps agent access in AI Access Graph.", "Shows no scoped credentials per agent."]),
    "Model File Security": ("lim", ["Reuses Hugging Face scan results.", "Checks for Safetensors and a model card."]),
    "Dataset Security": ("yes", ["Classifies training data with ZIA DLP.", "Flags poisoning and exposure risk."]),
    "AI Bill of Materials": ("lim", ["Lists models, agents and AI libraries.", "Exports to Excel, not to an AIBOM."]),
    "Framework Mapping": ("yes", ["Maps NIST AI RMF, EU AI Act and OWASP.", "Shows no ISO 42001 mapping."]),
}
for _r in AI4SEC + SPM + AGENTIC + DR_RT + GUARD + ID_MODEL + GRC:
    _r["v"]["zs"] = ZS[_r["cap"]]
SHADOW["v"]["zs"] = ("lim", ["Finds GenAI, desktop and embedded AI apps.", "Licenses endpoint AI discovery per device.",
                             "Needs ZIA and Client Connector to block."])
GATEWAY["v"]["zs"] = ("lim", ["Runs its own SaaS proxy, for public LLMs only.", "Connects to Kong, LiteLLM, APIM and Apigee.",
                              "Bills per token on top of a platform fee."])
DEPLOY["v"]["zs"] = ("SaaS only", "Licenses AI Guard and Endpoint AI as SaaS.")
for _g, _z in zip(GLANCE, [
        ("lim", "Prebuilt SOC agents only"), ("lim", "SaaS only"), ("lim", "Devices only, no hosts"),
        ("lim", "Human approves each fix"), ("lim", "Proxy for public LLMs"), ("par", "5,000+ attacks"),
        ("lim", "Maps access only"), ("lim", "Uses Hugging Face scans"), ("lim", "Excel export, no AIBOM")]):
    _g["v"].append(_z)

ROWS = AI4SEC + SPM + AGENTIC + DR_RT + GUARD + ID_MODEL + GRC
CAPS = len(ROWS) + 2  # plus the Shadow AI panel and the AI Gateway page
CITED = len(_urls)


def _tally():
    groups = [[k for k, _ in r["v"].values()] for r in ROWS]
    groups += [[k for k, _ in SHADOW["v"].values()], [k for k, _ in GATEWAY["v"].values()]]
    only = sum(1 for g in groups if not any(k in ("yes", "par") for k in g))
    cells = [k for g in groups for k in g]
    return [
        ("var(--win)", f"{only} of {CAPS}", "capabilities only AccuKnox fully supports"),
        ("var(--no)", str(sum(c in ("no", "noeq") for c in cells)), "rival cells not supported"),
        ("#E0A340", str(cells.count("lim")), "rival cells limited"),
        ("var(--par)", str(cells.count("par")), "parity"),
    ]


TALLY = _tally()

_H = "https://help.accuknox.com/"
AK_SOURCES = [_H + p for p in (
    "use-cases/prompt-firewall-overview/", "use-cases/shadow-ai-discovery/", "use-cases/modelarmor/",
    "use-cases/aidr/", "use-cases/red-teaming/", "how-to/ml-static-scan/", "how-to/model-scan-cicd/",
    "how-to/aiml-saas-vs-onprem/", "integrations/ai-overview/",
    "integrations/bedrock-agentcore/", "integrations/copilot-studio/", "integrations/powerapps-integration/",
    "getting-started/xbom-setup/", "getting-started/3.5-release/", "getting-started/3.6-release/",
    "agentz/")]


def _sources(f, extra=()):
    out = []
    for k, r in json.loads((_R / f"{f}.json").read_text(encoding="utf-8"))["rows"].items():
        if k in ("F2", "F3", "F4"):  # AI SAST, DAST and pentesting rows were cut
            continue
        if r["url"] not in out:
            out.append(r["url"])
    return out + [u for u in extra if u not in out]


SOURCES = {
    "panw": _sources("palo-alto"),
    "crwd": _sources("crowdstrike"),
    "vrns": _sources("varonis", ("https://aws.amazon.com/marketplace/pp/prodview-eoyer6g2olf6k",
                                 "https://www.varonis.com/blog/why-were-going-all-in-on-saas")),
    "zs": _sources("zscaler"),
}
