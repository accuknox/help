# Quilr Findings for the Shadow AI Discovery Section

All pages read 2026-10-27.

## A. Current Live Page

- **Overview heading:** "AccuKnox vs. Quilr. AI Security Platform Comparison"
- **Intro:** "Compare AccuKnox and Quilr across AI pipeline security, model and dataset security, prompt firewalling, runtime protection, red teaming, AI gateways, agentic AI, MCP security, and deployment options."
- **Groups (14), one row each:** On-Prem Support, AI Pipeline Security, Model Security, Dataset Security, Runtime Security, Prompt Firewalling, two Safety Guardrails rows, Red Teaming, Incident Response, AI Gateway Integrations, SDK and Platform Integrations, Agentic AI and MCP Security, Deployment Flexibility. No discovery or shadow AI group exists.
- **Quilr terms:** endpoint agent, browser extension, Guardian Agent, Red Team Agent, MCP Gateway, LLM gateway.
- **Tone:** AccuKnox cells run 3 sentences plus a "References:" block. Quilr cells run 1 to 2 sentences, no references, often "X. No Y."
- **Stale text:** the closing calls AccuKnox "a potential Tenable alternative".

Rows that touch discovery, endpoint, browser, MCP or agents, verbatim (AccuKnox references omitted). Three more rows mention the endpoint: AI Pipeline Security (Quilr No, "Secures the IDE and endpoint, not the build."), Incident Response (Quilr Dash, "Endpoint actions: block an app, quarantine a file, prompt for justification, kill the network.") and SDK and Platform Integrations (Quilr Yes, "plus endpoint agents").

| Row | AccuKnox cell | Quilr cell |
|---|---|---|
| Model Security | Yes. "Static scans of LLM and ML model files: Pickle, TensorFlow SavedModel, GGUF, DDUF. Runtime model execution visibility via KubeArmor (eBPF). Supply-chain poisoning detection for models pulled from public repos." | No. "Discovers models on endpoints only. No static scanning of model artifacts." |
| Runtime Security | Yes. "Zero Trust enforcement on process, file, network, and capabilities via eBPF (KubeArmor). Behaviour baselining and anomaly detection across K8s, VMs, bare metal, and serverless. No iptables or kernel modules needed." | Dash. "Endpoint agent on macOS and Windows monitors network and processes. No workload runtime enforcement for K8s, VMs, or serverless." |
| Agentic AI and MCP Security | Yes. "SPIFFE workload identity for AI agents across multi-cloud. OpenFGA fine-grained authorization with upstream caller-sequence tracking. MCP tool sandboxing on least-permissive access, with auto-discovery of agents and MCP servers." | Dash. "MCP Gateway authenticates agents, tiers tools by risk (read, write, destructive), and scans tool traffic for PII. No SPIFFE identity or OpenFGA policy model." |
| Deployment Flexibility | Yes. "SaaS, on-prem, air-gapped, public cloud, private cloud, and edge/IoT. Listed on AWS, Azure, Red Hat, and Oracle Cloud marketplaces. Hardware prerequisites and architecture documented for both models." | Dash. "Hosted gateway, embedded SDK, endpoint agent, browser extension, or on-prem/VPC. No air-gapped, edge/IoT, or marketplace listings." |

## B. What Quilr Documents

Quilr calls discovery "AI-SPM". Sensors: Endpoint Agent, Browser Extension, LLM Gateway, MCP Gateway.

1. **Browser and SaaS GenAI apps.** A browser extension plus a native Browser Agent, "in managed Chrome and Edge browsers" (docs.quilrai.dev/browser-extension/get-started/overview). No count of discoverable GenAI apps found.
2. **Endpoint and desktop apps.** "macOS 13.0 (Ventura)" and "Windows 10 (1903+) or Server 2019", "64-bit only" (docs.quilrai.dev/endpoint-agent/get-started/requirements). It "Finds installed and running AI apps" and detects "Ollama and LM Studio, and downloaded models" (docs.quilrai.dev/endpoint-agent/get-started/overview). Linux: Not found in public docs (searched: the requirements page, endpoint overview, quilr.ai/platform/endpoint-agent).
3. **Server, VM, container and Kubernetes.** Endpoint discovery reads "npm, pip, go, gem, Homebrew, and Chocolatey" (docs.quilrai.dev/endpoint-agent/how-it-works/process-mapping). quilr.ai/solutions/open-source-ai lists "Ollama on port 11434 across the network" and "Running vLLM / TGI endpoints". UNCLEAR: no page says how that network scan runs or what it installs on servers. Kubernetes or container discovery: Not found in public docs (searched: quilr.ai/platform, quilr.ai/faq, process-mapping page).
4. **CLI coding agents.** The endpoint agent "Discovers tools such as Cursor and Claude Code, plus their hooks, plugins" (endpoint overview). Codex CLI and Gemini CLI: Not found in public docs (searched: quilr.ai/solutions/agentic-coding, quilr.ai/solutions/claude-code, endpoint docs).
5. **MCP servers.** The endpoint agent "Inventories MCP server configurations and agent skills on the device" (endpoint overview). The Inventory flags MCP servers "Outside gateway" (docs.quilrai.dev/console/observe/inventory).
6. **Cloud AI assets.** The Azure AI Foundry connector "discovers agents, projects, models, access" and is "read-only" (docs.quilrai.dev/integrations/pull-ai-usage-and-inventory/azure-ai-foundry). Library cards cover "Amazon Bedrock Agents" and "Google Vertex AI Agent Builder" (docs.quilrai.dev/integrations/pull-ai-usage-and-inventory/agent-platforms-and-frameworks).
7. **Enforcement.** Endpoint app policy: "Allow", "Block", "Quarantine", "Justify" (process-mapping page). Network DLP can "block or ask for justification" (endpoint overview). The browser can "ask the user to justify, redact sensitive data, or block" (browser overview).
8. **AI-BOM and export.** Inventory covers "applications, browser extensions, AI clients, models, MCP servers, agents" with an **Export** button (inventory page). The Export Center offers "JSONL" or "Excel workbook" from source "Inventory" (docs.quilrai.dev/console/settings-data/export-center). CycloneDX or SPDX format: Not found in public docs (searched: the export center and inventory pages).
9. **Gap signals in Quilr's own words.**
   - The endpoint agent "is a separate package from the Browser Extension" (endpoint overview).
   - The endpoint agent needs a trusted root CA and "WinDivert driver" on Windows (requirements page).
   - Bedrock and Vertex cards list 3 regions each (agent-platforms page).
   - Preview or Beta labels and a separate license: Not found in public docs (searched: all pages above).

## Five Documented Contrasts Favor AccuKnox on Coverage

- Endpoint discovery documents macOS 13+ and 64-bit Windows. Linux is not documented. https://docs.quilrai.dev/endpoint-agent/get-started/requirements
- Kubernetes and container discovery is not documented. Server coverage is an Ollama and vLLM network scan of UNCLEAR method. https://quilr.ai/solutions/open-source-ai
- Browser coverage needs managed Chrome or Edge plus a native agent. The desktop agent is a second package. https://docs.quilrai.dev/browser-extension/get-started/overview
- Cloud AI discovery uses per-platform connectors. Bedrock and Vertex cards list 3 regions each. https://docs.quilrai.dev/integrations/pull-ai-usage-and-inventory/agent-platforms-and-frameworks
- Named coding agents are Claude Code, Cursor, Copilot, Windsurf and Devin. Codex CLI and Gemini CLI are not named. https://quilr.ai/solutions/agentic-coding
