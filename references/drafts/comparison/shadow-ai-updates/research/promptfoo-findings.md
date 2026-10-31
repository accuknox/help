# Promptfoo Findings for the Shadow AI Discovery Section

Date read: 2026-10-27. promptfoo.dev pages scraped with Firecrawl.

## A. The Live Page Already Has a Shadow AI Discovery Group

**Intro (verbatim).** Heading: "AccuKnox vs Promptfoo: AI Security Comparison". Description: "See how AccuKnox and Promptfoo compare across AI security capabilities, from asset discovery and AI-SPM to model security, red teaming, guardrails, agent protection, and runtime enforcement. (edited)".

**Shadow AI Discovery rows (verbatim).** AccuKnox is Yes on all 8. Promptfoo is No on all 8, with no Third Column description.

| Sub Heading | AccuKnox description | Promptfoo |
|---|---|---|
| Agentless AI asset discovery across AWS, Azure, GCP | Shadow AI Discovery / AWS AI/ML Cloud Onboarding | No |
| On-prem VM discovery: package-level scan of the host filesystem | Agent-Based VM Scanning for Linux | No |
| In-cluster Kubernetes discovery across nodes, namespaces, images | Kubernetes Security Onboarding | No |
| Classify assets into 7 types: Agent, Automation, Gateway, Inference Engine, AI-ML, SDK, MCP | (none) | No |
| Find unapproved agentic runtimes installed on workstations and build VMs | (none) | No |
| Browser plugin that records GenAI service usage (ChatGPT, Claude, Gemini, Copilot) | Prompt Firewall Gen AI Browser Integration (Chrome) | No |
| Cloud AI pipeline graph: connectivity, exposure, service relationships | (none) | No |
| Vulnerability and malware findings attached to each discovered AI asset | (none) | No |

**Other groups.** AI Posture Management (AI-SPM), AI Model & Dataset Security, AI Red Teaming & Pen Testing, AI Guardrails (Prompt Firewall), Agentic AI & MCP Security, Agentic Harness Platform (AgentZ), AI Detection & Response (AI-DR), Compliance & Governance, Developer Workflow, Deployment & Platform.

**Promptfoo terms used on the page.** Model Security, red teaming plugins (157 across 6 categories), Enterprise adaptive guardrails, the OSS `guardrails` assert, MCP proxy, Code Scanning, VS Code extension. The last row, "Independent vendor", is AccuKnox Yes and Promptfoo No.

**Tone.** Third Column cells are short and factual. Each is one clause plus a promptfoo.dev URL.

**Workbook** (`references/competitive/battlecards/accuknox-vs-promptfoo-ai-security.xlsx`, sheet "Stack Ranking"). Same 8 rows. The Promptfoo source for the group is "Not offered. Their six products are Red Teaming, Evaluations, Code Scanning, Model Security, Guardrails, MCP: promptfoo.dev". The Independent vendor row cites "Promptfoo states it is part of OpenAI, on every page banner". UNCLEAR: the 2026-10-27 homepage scrape showed no such banner.

**Ownership.** https://www.promptfoo.dev/blog/promptfoo-joining-openai says "Promptfoo has agreed to be acquired by OpenAI." It also says "closing of the acquisition is subject to customary closing conditions." Closing status: UNCLEAR.

## B. What Promptfoo Publishes per Surface

The homepage lists 6 products: "Red TeamingEvaluationsCode ScanningModel SecurityGuardrailsMCP" (https://www.promptfoo.dev/).

1. **Browser and SaaS GenAI app discovery.** Not found in public docs. Searched: site map of promptfoo.dev (606 URLs), https://www.promptfoo.dev/, https://www.promptfoo.dev/guardrails/, plus Firecrawl searches "promptfoo shadow AI discovery" and "site:promptfoo.dev shadow AI inventory endpoint browser".
2. **Endpoint and desktop AI app discovery.** Not found in public docs. Searched: the same sources.
3. **Server, VM, container or Kubernetes discovery of installed AI software.** Not found in public docs. Searched: the same sources. The only "discovery" feature is the Target Discovery Agent. It probes one chat target for "Purpose", "Limitations", tools and users before a red team run (https://www.promptfoo.dev/docs/red-team/discovery/). It does not inventory hosts.
4. **CLI coding agents.** Promptfoo tests coding agents as targets. It does not discover or enforce on them. Its guide covers "OpenAI Codex SDK", "Claude Agent SDK" and "OpenCode SDK" (https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/). The red team collection tests "Untrusted repository text steers the agent" (https://www.promptfoo.dev/docs/red-team/coding-agents/). Discovery or enforcement on Claude Code, Codex, Gemini CLI or Cursor installs: not found in public docs (searched both URLs above and the site map).
5. **MCP server discovery or scanning.** The MCP proxy can "Whitelist approved MCP servers" and shows an "Unapproved MCP" path (https://www.promptfoo.dev/mcp/). It tracks "all MCP requests with detailed logging and real-time alerts". UNCLEAR: the page does not say the proxy finds MCP servers that do not route through it.
6. **Cloud AI asset discovery.** Not found in public docs. Searched: the same sources plus https://www.promptfoo.dev/pricing/.
7. **Code scanning for LLM usage.** Yes. Code Scanning "uses AI agents to find LLM-related vulnerabilities in your codebase" (https://www.promptfoo.dev/docs/code-scanning/). It flags prompt injection, PII exposure and excessive agency. Surfaces are the GitHub Action, the CLI and a VS Code extension. UNCLEAR: it scans code changes for risk. It does not claim to produce an inventory of AI usage across repos.
8. **Enforcement after discovery.** Adaptive guardrails return "`allow`, `log`, `warn`, `block`, or `error`" through an API call (https://www.promptfoo.dev/docs/enterprise/guardrails/). A transforming policy "can return `sanitizedContent`". Tool call guardrails apply "a PII filter to `TOOL_CALL_INPUT`". The surface is the customer's app code, which calls `POST /api/v1/guardrails/{id}/evaluate`. The MCP proxy enforces at the MCP layer. Browser or endpoint enforcement: not found in public docs.
9. **Gap signals in their own words.**
   - Guardrails: "This feature requires Promptfoo Enterprise" (https://www.promptfoo.dev/docs/enterprise/guardrails/).
   - Guardrails limit: "Guardrails can only block patterns similar to known vulnerabilities" (same URL).
   - VS Code extension: "Available for enterprise customers" (https://www.promptfoo.dev/docs/code-scanning/).
   - MCP proxy: sold as "enterprise MCP proxy", with "Request a Demo" as the only call to action (https://www.promptfoo.dev/mcp/).
   - No Beta labels found on these pages.

## Five Documented Contrasts Favor AccuKnox

- Promptfoo lists 6 products and none is asset discovery: https://www.promptfoo.dev/
- Its only "discovery" feature profiles one chat target for red teaming: https://www.promptfoo.dev/docs/red-team/discovery/
- Promptfoo tests coding agents as eval targets and documents no install discovery: https://www.promptfoo.dev/docs/guides/evaluate-coding-agents/
- Guardrails require Enterprise, run in app code, and "can only block patterns similar to known vulnerabilities": https://www.promptfoo.dev/docs/enterprise/guardrails/
- Promptfoo "agreed to be acquired by OpenAI", and the post says closing is pending: https://www.promptfoo.dev/blog/promptfoo-joining-openai
