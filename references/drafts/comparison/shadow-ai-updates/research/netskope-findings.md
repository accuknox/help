# Netskope Shadow AI Discovery Findings

Read 2026-10-27 with Firecrawl. All 2026-09-24 evidence-log facts below were re-checked live.

## A. Current Live Page

Source: `accuknox-vs-netskope.md`, exported 2026-10-27.

**Groups.** Discovery and AI Posture (AI-SPM), Model Security and Red Teaming, Runtime Guardrails, Agentic AI and MCP, Detection, Response and Governance.

**Netskope terms used.** AI Command Center, Netskope Client, Next Gen Secure Web Gateway, AI Guardrails, AI Gateway, Agent Action Control, Agentic Broker, MCP Gateway, Skope IT. The page never says "SkopeAI".

**Tone.** Neutral. Cells cite counts and Netskope's own limits.

**Rows.** Netskope cells are verbatim. AccuKnox cells are summarized, with full text in the export.

1. Cloud AI service inventory. AccuKnox: Yes (agentless AWS, Azure, GCP roles). Netskope: Dash. "AI Command Center discovers 13 AI platforms: 5 on AWS, 4 on Azure and 4 on GCP. It runs static configuration checks on custom agents, enterprise chatbots and model serving. Findings trace IAM, network, storage and encryption controls. Netskope marks this capability as a preview feature."
2. Self-hosted and shadow AI discovery. AccuKnox: Yes (VM snapshot, VM agent and Kubernetes scanners, 7 package types). Netskope: Yes. "The Netskope Client scans managed endpoints for AI agents, local LLMs (Ollama, LM Studio, Jan AI, GPT4All), MCP servers and IDE or browser AI extensions. It runs on Windows and macOS with Client 138 or later. Netskope states it misses AI assets in VMs or containers that do not run the Client. It detects only assets in the Netskope signature file."
3. Workforce GenAI app visibility and control. AccuKnox: Yes (browser plugin on 5 browsers). Netskope: Yes. "The Next Gen Secure Web Gateway identifies 3,300+ Gen AI apps. Admins apply activity-based and instance-based policies, app tags and real-time user coaching. The traffic must be steered through Netskope."
4. AI supply chain in CI/CD and AIBOM. AccuKnox: Yes (xBOM, CycloneDX 1.6 AIBOM). Netskope: No. "The Netskope AI Security docs and product pages describe no AIBOM output and no model scan step for a CI/CD pipeline."
5. Agent runtime sandbox. AccuKnox: Yes (ModelArmor and AgentZ). Netskope: Dash. "Agent Action Control applies intent, risk and access policies to agent traffic. It covers 79 SaaS and cloud apps and 70 named agents, including Claude Code, Cursor and ChatGPT Desktop. Netskope marks it Beta, and support must enable it per tenant."
6. MCP visibility and control. AccuKnox: Dash (MCP packages found, protocol policies on roadmap). Netskope: Yes. "Agentic Broker logs MCP messages such as CallToolRequest and ReadResourceRequest in Skope IT. Real-time Protection blocks by server, tool or activity, and a catalog risk-scores public MCP servers. MCP Gateway applies access control, DLP, guardrails and rate limits for up to 100 MCP providers per tenant. Agentic Broker needs its own license."

**Two live cells are now stale.** Row 4 says Netskope has no AIBOM, but AI-BOM Analysis exists (B8). The guardrail row says 20 apps, and the docs now list 27 (B7).

## B. Netskope Docs Findings

1. **Browser and SaaS GenAI apps.** The Next-Gen SWG discovers apps in steered traffic. "Netskope can identify 3,300+ Gen AI apps to control usage." https://docs.netskope.com/en/ai-security.
2. **Endpoint discovery.** The Client runs "periodic signature-based scanning". Windows (64-bit) and macOS, Client 138 minimum, Codex needs 142, network telemetry needs 140.0.0. Browser extensions cover Chrome, Edge and Safari only. On shared machines it scans only the active user's profile. https://docs.netskope.com/en/netskope-client-ai-discovery. Codex and telemetry are new.
3. **Servers, VMs, containers, Kubernetes.** Stated blind spot: VM or Docker AI assets "are not detected" unless the Client runs inside them. https://docs.netskope.com/en/netskope-client-ai-discovery. A Linux or Kubernetes scanner: Not found in public docs (searched: site search "AI discovery Linux server Kubernetes", https://docs.netskope.com/en/ai-command-center).
4. **CLI coding agents.** UNCLEAR. The Client lists Claude Code and Codex as AI Agents without saying CLI or desktop. Agent Action Control lists Claude Code and Cursor among 70 agents, "a Beta feature". https://docs.netskope.com/en/agent-action-control. Gemini CLI: Not found in public docs (searched: both pages above, site search "Claude Code CLI").
5. **MCP servers.** Agentic Broker sees steered traffic, and the Client finds "local MCP servers". https://docs.netskope.com/en/ai-command-center. Skope IT MCP logs need the "Agentic Broker license". https://docs.netskope.com/en/visibility-into-mcp-usage. MCP Gateway: "up to 100 MCP providers per tenant". Stdio transport is "not validated". https://docs.netskope.com/en/configuring-mcp-gateway.
6. **Cloud AI platforms.** Still 13 platforms (5 AWS, 4 Azure, 4 GCP), and "currently available as a preview feature". https://docs.netskope.com/en/ai-platforms-discovery-and-security-posture-management.
7. **Enforcement after discovery.** AI Guardrails now lists 27 apps, up from 20, including Microsoft Foundry and Copilot Studio. https://docs.netskope.com/en/ai-guardrails. Agent Action Control still covers 79 apps and 70 agents. A block on a local asset the Client finds is UNCLEAR, because the docs describe none.
8. **AI-BOM and inventory export.** New: AI-BOM Analysis emits "a cryptographically signed CycloneDX JSON manifest" for agent skill .zip files via API. It is "in Limited Availability". https://docs.netskope.com/en/ai-bom-analysis. An AICC Inventory export to CSV: Not found in public docs (searched: https://docs.netskope.com/en/ai-inventory, https://docs.netskope.com/en/ai-agents-aicc, site search "AI inventory export CSV").
9. **Gap signals.** AI Platforms is Preview, Agent Action Control is Beta, and AI-BOM is Limited Availability. Agentic Broker and DLP are separate licenses. AICC bills per AI Asset over "a rolling 90-day period". https://docs.netskope.com/en/ai-command-center-licensing-terms.

## Five Netskope Limits the Docs State Outright

- Endpoint discovery misses AI in VMs and containers without the Client. https://docs.netskope.com/en/netskope-client-ai-discovery
- Discovery covers Windows and macOS only. https://docs.netskope.com/en/configuring-discovery-of-ai-assets-on-managed-endpoints
- Cloud AI platform posture is still Preview. https://docs.netskope.com/en/ai-platforms-discovery-and-security-posture-management
- App and MCP discovery need steered traffic, and Agentic Broker is a separate license. https://docs.netskope.com/en/ai-command-center
- AICC "stops displaying new AI Assets" past the quota. https://docs.netskope.com/en/ai-command-center-licensing-terms
