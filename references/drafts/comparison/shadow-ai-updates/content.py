"""Shadow AI Discovery blocks for six AI security comparison pages, short form.

AccuKnox claims: Shadow AI coverage one-pager, Oct 2026
(references/drafts/shadow-ai-one-pager/shadow-ai-coverage-one-pager.pdf).
Competitor claims: the vendor's own pages, read 2026-10-27. Full notes with every
URL sit in research/<vendor>-findings.md.

Icons map to the WordPress "Image Select" field: Yes, Dash, No.
The third value in a competitor cell is True when a person must approve it.
"""

H = "https://help.accuknox.com"
SHADOW = f"{H}/use-cases/shadow-ai-discovery/"
BROWSER = f"{H}/integrations/chrome-browser-integration/"
CLI = f"{H}/faqs/ai-security/"
AIBOM = f"{H}/integrations/azure-xbom/"

AK_BROWSER = ("Yes", "Plugin on Chrome, Edge, Firefox and Safari. Blocks uploads and masks PII, PHI and PCI.", BROWSER)
AK_HOST = ("Yes", "Scans Linux, Windows and macOS hosts, VMs and containers. Finds 100+ AI tools in 7 categories.", SHADOW)
AK_CLI = ("Yes", "Cursor, Claude Code, Codex and Gemini CLI route through the Prompt Firewall.", CLI)
AK_MCP = ("Yes", "Host scan lists MCP servers as their own category.", SHADOW)
AK_AIBOM = ("Yes", "Exports managed and unmanaged AI assets as a CycloneDX AI-BOM.", AIBOM)

VENDORS = [
    {
        "name": "Quilr",
        "url": "https://accuknox.com/comparisons/accuknox-vs-quilr",
        "where": "New group SHADOW AI DISCOVERY, first in the table",
        "heading": "AccuKnox Finds Shadow AI From the Browser to the Linux Server",
        "intro": "AccuKnox discovers shadow AI in the browser, on Linux, Windows and macOS hosts, and in CLI coding agents. "
                 "Quilr documents endpoint discovery on macOS and Windows, plus managed Chrome and Edge.",
        "rows": [
            ("Browser GenAI control", AK_BROWSER, ("Yes", "Extension in managed Chrome and Edge. Can redact or block.", False)),
            ("Host and VM discovery", AK_HOST, ("Dash", "Endpoint agent on macOS 13+ and 64-bit Windows.", True)),
            ("CLI coding agents", AK_CLI, ("Dash", "Discovers Cursor and Claude Code.", True)),
            ("AI inventory export", AK_AIBOM, ("Dash", "Exports JSONL or Excel.", True)),
        ],
        "sources": ["docs.quilrai.dev/endpoint-agent/get-started/requirements",
                    "docs.quilrai.dev/browser-extension/get-started/overview",
                    "docs.quilrai.dev/console/settings-data/export-center"],
    },
    {
        "name": "Promptfoo",
        "url": "https://accuknox.com/comparisons/accuknox-vs-promptfoo",
        "where": "Add to the existing Shadow AI Discovery group",
        "heading": "AccuKnox Builds the AI Inventory Before Red Teaming Starts",
        "intro": "AccuKnox finds the AI agents, SDKs, MCP servers and coding assistants running in your estate. "
                 "Promptfoo lists six products, and none of them is asset discovery.",
        "rows": [
            ("Windows and macOS host scanning", ("Yes", "Scans Windows and macOS endpoints as well as Linux. Finds 100+ AI tools.", SHADOW),
             ("No", "Not among Promptfoo's six products.", True)),
            ("CLI coding agents", AK_CLI, ("No", "Tests coding agents as red team targets.", False)),
            ("MCP server discovery", AK_MCP, ("Dash", "MCP proxy allowlists approved servers.", True)),
            ("AI-BOM export", AK_AIBOM, ("No", "Not among Promptfoo's six products.", True)),
        ],
        "sources": ["promptfoo.dev", "promptfoo.dev/mcp", "promptfoo.dev/docs/guides/evaluate-coding-agents"],
    },
    {
        "name": "Forcepoint",
        "url": "https://accuknox.com/comparisons/accuknox-vs-forcepoint",
        "where": "New group Shadow AI Discovery, after Deployment Model",
        "heading": "AccuKnox Finds Installed Shadow AI Beyond Web Traffic",
        "intro": "AccuKnox scans hosts, VMs and containers for installed AI tools, then enforces policy in the browser and terminal. "
                 "Forcepoint finds shadow AI through web traffic and endpoint agents on Windows and macOS.",
        "rows": [
            ("Discovery source", ("Yes", "Host scan on Linux, Windows and macOS, plus the browser plugin.", SHADOW),
             ("Dash", "Web security traffic, or endpoint agents on Windows and macOS.", False)),
            ("AI SDKs, frameworks and inference engines", ("Yes", "Finds 100+ AI tools in 7 categories, including SDKs and inference engines.", SHADOW),
             ("No", "Not found in Forcepoint docs.", True)),
            ("MCP server discovery", AK_MCP, ("Dash", "AI Agent Gateway covers 3 SaaS MCP connectors.", False)),
            ("AI-BOM export", AK_AIBOM, ("No", "Not found in Forcepoint docs.", True)),
        ],
        "sources": ["help.forcepoint.com/fpdsc/aisecurity/guid-15ba7ee6-ec36-4089-8cc6-552e3bf004ff.html",
                    "help.forcepoint.com/fpdsc/aisecurity/guid-7ecc5492-0787-4515-9a78-c4837ba3d126.html",
                    "forcepoint.com/use-case/shadow-ai-security"],
    },
    {
        "name": "Check Point",
        "url": "https://accuknox.com/comparisons/accuknox-vs-checkpoint",
        "where": "DISCOVERY & GOVERNANCE group, replace the Shadow AI Detection row",
        "heading": "AccuKnox Extends Shadow AI Discovery to Linux Servers and Containers",
        "intro": "Both products discover AI in the browser, the IDE and on endpoints. "
                 "AccuKnox also scans Linux hosts, VMs and containers, and exports a CycloneDX AI-BOM.",
        "rows": [
            ("Browser GenAI discovery and DLP", AK_BROWSER, ("Yes", "Browser extension with allow, ask and block policy.", False)),
            ("Linux host, VM and container discovery", AK_HOST, ("Dash", "Endpoint discovery lists Windows and macOS.", True)),
            ("CLI coding agent enforcement", AK_CLI, ("Dash", "Claude Code hooks need Claude Enterprise. Allow or deny only.", False)),
            ("AI-BOM export", AK_AIBOM, ("No", "Not found in Check Point docs.", True)),
        ],
        "sources": ["sc1.checkpoint.com/documents/Workforce_AI_Security/",
                    "checkpoint.com/ai-security/ai-workforce-security/"],
    },
    {
        "name": "Netskope",
        "url": "https://accuknox.com/comparisons/accuknox-vs-netskope",
        "where": "Discovery and AI Posture group, replace the Self-hosted and shadow AI discovery row",
        "heading": "AccuKnox Scans VMs and Containers for Installed Shadow AI",
        "intro": "AccuKnox scans Linux, Windows and macOS hosts, VMs and containers for installed AI tools. "
                 "Netskope states its Client does not detect AI in VMs or containers unless the Client runs there.",
        "rows": [
            ("Shadow AI in VMs and containers", AK_HOST, ("Dash", "Client misses AI in VMs or containers without the Client.", False)),
            ("Browser GenAI control", ("Yes", "Plugin on 4 browsers inspects prompts and uploads before they reach the AI app.", BROWSER),
             ("Yes", "Identifies 3,300+ GenAI apps in steered traffic.", False)),
            ("CLI coding agents", AK_CLI, ("Dash", "Agent Action Control covers Claude Code and Cursor. Beta.", False)),
            ("AI-BOM export", AK_AIBOM, ("Dash", "AI-BOM for agent skill packages. Limited Availability.", False)),
        ],
        "sources": ["docs.netskope.com/en/netskope-client-ai-discovery",
                    "docs.netskope.com/en/agent-action-control",
                    "docs.netskope.com/en/ai-bom-analysis"],
    },
    {
        "name": "Straiker",
        "url": "https://accuknox.com/comparisons/accuknox-vs-straiker",
        "where": "New group Shadow AI Discovery, after AI Platform Security (AI-SPM)",
        "heading": "AccuKnox Covers Employee Shadow AI Alongside Sanctioned Agents",
        "intro": "AccuKnox discovers and controls the AI tools staff install and the AI apps they open. "
                 "Straiker's May 2026 guide describes Discover AI as “Not for shadow AI or employee usage controls.”",
        "rows": [
            ("Employee GenAI use in the browser", AK_BROWSER, ("Dash", "Browser extension listed for productivity agents.", True)),
            ("Installed AI tools on hosts", AK_HOST, ("Dash", "Blog describes macOS and Windows endpoint inventory.", True)),
            ("CLI coding agents", AK_CLI, ("Dash", "Supports Cursor, Copilot, Claude Code and Windsurf.", False)),
            ("MCP server discovery", AK_MCP, ("Yes", "Inventories internal and external MCP servers.", False)),
        ],
        "sources": ["straiker.ai/blog/top-7-ai-agent-visibility-and-governance-platforms",
                    "straiker.ai/blog/why-firewalls-and-edr-miss-shadow-ai",
                    "straiker.ai/solution/coding-agents"],
    },
]

APPROVE = [
    "macOS host scanning: the one-pager says Full, a 2026-09-26 product note says Beta. Pick one.",
    "Safari plugin: no help doc yet. Chrome, Edge and Firefox have one.",
    "Cursor and Gemini CLI through the Prompt Firewall: help docs name Claude Code and Codex only.",
    "100+ AI tools: on the one-pager only.",
    "CycloneDX AI-BOM export from the shadow AI inventory: confirm with product.",
    "Every competitor cell marked REVIEW: we found nothing in their docs. Absence is not proof.",
    "Straiker quote: their September 2026 blog moves toward shadow AI. Keep or drop the quote.",
]

FIX_LIVE = [
    "Check Point: “browser/SaaS-centric” and “No published AI-SPM module” are now out of date.",
    "Netskope: the AIBOM row says No (now Limited Availability). Guardrails cover 27 apps, not 20.",
    "Forcepoint: “No Redaction possible” and the AI agents No cells conflict with Forcepoint's own pages.",
    "Quilr: the closing paragraph calls AccuKnox a Tenable alternative.",
]
