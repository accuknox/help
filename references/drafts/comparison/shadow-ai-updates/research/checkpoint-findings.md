# Check Point Shadow AI Findings

Read 2026-10-27. `WAI/` means `https://sc1.checkpoint.com/documents/Workforce_AI_Security/`, stamped 25 October 2026. The old Infinity_Portal guide URLs return 404.

## A. The Live AccuKnox Page

**Groups:** DISCOVERY & GOVERNANCE, MODEL & SUPPLY CHAIN, RUNTIME PROTECTION, AGENTIC AI SECURITY, DATA & PIPELINE, AI FACTORY & INFRA, GATEWAY & INTEGRATIONS, DEPLOYMENT.

**Terminology:** "Checkpoint" in headings, "Check Point" in cells, "Check Point AI Security", "Check Point Factory Firewall". No cell names GenAI Protect, Workforce AI Security or Lakera.

**Tone:** terse, 5 to 20 words per cell. AccuKnox cells end in "Reference".

**Verbatim rows** (icon, then cell text):

| Row | AccuKnox | Check Point |
|---|---|---|
| Shadow AI Detection (self- hosted + SaaS) | Yes. "Finds self-hosted inference engines (Ollama, vLLM, on-prem LLMs) in addition to SaaS GenAI. Reference" | Yes. "Check Point is browser/SaaS-centric." |
| GenAI App Governance (ChatGPT, Copilot, Gemini) | Yes. "AccuKnox adds CLI, SDK, and AI gateway modes for the same enforcement. Reference" | Yes. (empty) |
| AI Asset Inventory & AI-SPM | Yes. "Security Graph maps agents to models, tools, datasets, and cloud accounts across AWS, Azure, GCP, and on-prem in one console. Reference" | Dash. "No published AI-SPM module" |
| AIBOM / xBOM | Yes. "Generate, sign, compare, and verify SBOM, CBOM, HBOM, AIBOM. Aligned to CERT-In guidance. Reference" | No. (empty) |
| Agent Runtime Monitoring | Dash. "AccuKnox Agentic Runtime Security is in beta with deeper eBPF visibility via KubeArmor. Reference" | Yes. "Check Point is GA on tool-call interception." |
| MCP Server Security & Sandboxing | Dash. "eBPF sandboxing of MCP tool execution and untrusted models. Reference" | Dash. "Check Point inspects MCP-flowing content but does not isolate execution." |
| Agent Identity, SPM & Red Teaming | Dash. "Agent inventory, SPIFFE-based agent identity, agent red teaming. Reference" | Dash. "Check Point markets agent security but has no published SPM or identity module." |

**Workbook** (`accuknox-vs-checkpoint-ai-security.xlsx`): the Shadow AI row reads "Supported (SaaS-side via browser extension)". It holds no Check Point source URLs.

**Stale claims:** "browser/SaaS-centric" and "No published AI-SPM module" conflict with section B.

## B. What Check Point Documents

**1. Browser and SaaS discovery.** "Deploy instantly with our lightweight browser extension" (checkpoint.com/ai-security/ai-workforce-security/). Harmony Browse GenAI Protect runs in the "secure browser extension" (sc1 Harmony-Browse-Admin-Guide, Data-Loss-Prevention_DLP_.htm). The SASE path covers "more than 300 services" (blog.checkpoint.com, protect-your-organization-from-genai-risks-with-harmony-sase). The gateway path lists 7 apps, needs "HTTPS Inspection" (sc1 R82.20 SecurityManagement GenAI.htm). Workforce app count: Not found in public docs (searched: WAI/discovery/discovery.html, WAI/applications/applications.html).

**2. Endpoint and desktop.** Windows and macOS only. "ChromeOS supports extension deployment only" (WAI/downloads/downloading_deployment_packages_for_your_platform.html). The Agentic Endpoint Discovery scan "does not require the installation of the Workforce AI Security desktop client" (WAI/downloads/understanding_agentic_endpoint_discovery_capabilities.html). The Fleet Scan Script runs through MDM: "Select the operating system (Windows or macOS)" (WAI/downloads/deploying_fleet_scan_discovery_script.html). Linux: Not found in public docs (searched: the pages above, site:sc1.checkpoint.com).

**3. Server, VM, container, Kubernetes.** Not found in public docs (searched: WAI/ downloads pages, docs.lakera.ai/docs/agent-security/discovery, checkpoint.com/ai-security/ai-agent-security/). UNCLEAR: AI Factory Firewall protects "GPU clusters, and AI workloads" (checkpoint.com/ai-security/), with no stated software inventory.

**4. CLI coding agents.** The Discovery screen lists "Cursor and VS Code", "Claude Code", "GitHub Copilot" (WAI/discovery/discovery.html). Claude Inference Hooks enforcement "covers claude.ai, Claude Code, and Claude Cowork" (WAI/integration_claude_inference_hooks/claude_inference_hooks_integration.html). Codex and Gemini CLI: Not found in public docs (searched: the same pages).

**5. MCP discovery.** Endpoint view: "shows active and inactive MCP servers used by users" (WAI/agents_mcp_servers/agents.html). The inventory has a "Toolsets & MCP" view (WAI/inventory/toolsets-and-mcp-servers.html).

**6. Cloud AI assets.** Agent Discovery connects to 7 platforms: Bedrock, Bedrock AgentCore, Google Cloud, Copilot Studio, Agentforce, n8n and Relevance AI (docs.lakera.ai/docs/agent-security/discovery). The Google Cloud integration "will be available in late June 2026" (checkpoint.com Google Cloud press release). Model or GPU asset discovery in cloud accounts: Not found in public docs.

**7. Enforcement.** Access policy: Allow, Ask, Block. Chats DLP: "Allow, Ask, Block, Prevent, Detect". Agent policy: "Control MCP servers and tools" (WAI/architecture/architecture_and_key_concepts.html). Harmony Browse adds "Force redact" with asterisks (Harmony Browse DLP page). Inference Hooks: "does not support prompt redaction or rewriting".

**8. AI-BOM and export.** AI-BOM appears only as an explainer (checkpoint.com/cyber-hub/cyber-security/what-is-ai-security/ai-bom/). An AI-BOM export: Not found in public docs. Reports cover "Last Day / Last Week / Last Month" (WAI/reports/generate-report.html). UNCLEAR: the docs do not state the report file format.

**9. Gap signals in their own words.**
- Tiers: Essentials covers "Web Applications only". Enterprise covers "Web, Desktop, MCP, IDEs" (WAI/introduction_to_workforce_ai_security/introduction_to.html).
- MDM sync "does not automatically deploy the agent" (WAI/settings/agentic_endpoint_discovery.html).
- Inference Hooks need "A Claude Enterprise plan". Hooks run on prompts only: "Anthropic currently sends only prompt-side events."
- Regions: Harmony Browse DLP lists "EU, US, India, Australia, and UAE regions".
- Gateway: "Spark Firewall Appliances do not support Workforce AI Security" (R82.20 GenAI.htm).
- License: GenAI Protect is "part of Browse Security Advanced license" (Harmony Browse DLP page).
- Lakera: the acquisition is official (checkpoint.com press release). docs.lakera.ai carries Check Point branding.

## Five Documented Limits Favor AccuKnox

- Check Point endpoint discovery runs on Windows and macOS only. Linux servers, VMs and Kubernetes appear in no doc (WAI/downloads/downloading_deployment_packages_for_your_platform.html).
- Desktop, IDE and MCP discovery needs the Enterprise tier. Essentials is web only (WAI/introduction_to_workforce_ai_security/introduction_to.html).
- Claude Code enforcement depends on Claude Enterprise hooks. The hooks only allow or deny prompts and cannot redact (WAI/integration_claude_inference_hooks/claude_inference_hooks_integration.html).
- Agent inventory comes from API connectors to 7 SaaS and cloud platforms, and depth varies by platform (docs.lakera.ai/docs/agent-security/discovery).
- Check Point publishes no AI-BOM export. AI-BOM appears only as an explainer page (checkpoint.com/cyber-hub/cyber-security/what-is-ai-security/ai-bom/).
