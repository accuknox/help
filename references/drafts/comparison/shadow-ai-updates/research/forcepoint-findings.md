# Forcepoint Findings for the Shadow AI Discovery Section

Read 2026-10-27. Sources: Forcepoint's site and help docs only. The live page has an en dash in one cell, shown as [en dash].

## A. Current Live Page

**Intro.** H1: "AccuKnox vs. Forcepoint. AI Prompt Firewall Comparison". Description: "See how AccuKnox compares to Forcepoint for AI prompt security across browsers, AI agents, API gateways, CLI tools, applications, and self-hosted models."

**Groups.** Deployment Model, six "Prompt Firewall on/in/for ..." rows, Prompt Firewall Policies, Enforcement, Stateful Detection, Performance, Coverage & Deployment, Testing & Compliance, Integration Coverage.

**Terms and tone.** "Prompt Firewall", "DLP / SSE solution", "Web/CASB access control". Forcepoint cells run 0 to 8 words, often blank with No.

**Verbatim rows (AccuKnox cell | Forcepoint cell)**

- Deployment Model: Yes "Browser plugin, inline proxy, SDK, API gateway" | Dash "Need to deploy complete DLP / SSE solution. No LLM proxy"
- Prompt Firewall on SaaS AI apps such as Claude, Gemini, ChatGPT, MS Copilot, GitHub Copilot: Yes "Chrome, Edge, Safari, Firefox" | Dash "Web/CASB access control only"
- Prompt Firewall on AI agents such as Copilot Studio, Bedrock AgentCore, MS Teams 365 agents: Yes "Power Apps, Copilot Studio, Bedrock AgentCore" | No
- Prompt Firewall for CLI tools such as Codex, Claude Code, Anti-Gravity: Yes "Native CLI integration" | No
- Policies / Do not allow ChatGPT public / anonymous: Yes | Yes
- Coverage / Self-hosted models (Ollama, vLLM): Yes | No
- Integration / Browser: Yes "Chrome, Edge, Safari, Firefox [en dash] intercepts prompts in -browser before they leave the session" | Dash "Access control only"
- Integration / SaaS AI apps: Yes "ChatGPT, Claude, Gemini, MS Copilot, GitHub Copilot" | Dash "Allow / block per app"
- Integration / AI agents: Yes "Power Apps, Copilot Studio, Bedrock AgentCore, MS Teams 365 agents" | No
- Integration / CLI tools: Yes "Codex, Claude Code, Anti-Gravity" | No
- Integration / Self-hosted models: Yes "Ollama, vLLM, custom inference endpoints" | No

## B. What Forcepoint Documents

Product: Forcepoint AI Security on Data Security Cloud (DSC), with AI DR, Shadow AI and AI Agent Gateway. Launched 2026-07-22.

**1. Browser and SaaS GenAI discovery.** The help docs name web traffic as the source. Unsanctioned apps arrive "Through your Forcepoint web security traffic." (help.forcepoint.com/fpdsc/aisecurity/guid-15ba7ee6-ec36-4089-8cc6-552e3bf004ff.html). The page lists only apps "present in this database" (same URL). No GenAI app count is stated.

**2. Endpoint discovery.** Cloud DLP or On-Prem DLP customers get visibility "through supported endpoint agents" (F1E 26.09+ or DSE 30.9+) on "Windows and macOS" (help.forcepoint.com/fpdsc/aisecurity/guid-7ecc5492-0787-4515-9a78-c4837ba3d126.html). Marketing names "browser extensions, vibe-coding tools and MCP clients" (forcepoint.com/use-case/shadow-ai-security).

**3. Server, VM, container or Kubernetes discovery.** Not found in public docs (searched: help pages guid-7ecc5492, guid-15ba7ee6, guid-06f6235c, plus /ai-data-security, /use-case/shadow-ai-security, /use-case/agentic-ai-security, launch release).

**4. CLI coding agents.** UNCLEAR. Marketing says "vibe-coding tools" but names no product. Claude Code, Codex, Gemini CLI and Cursor do not appear on any page read.

**5. MCP discovery.** Marketing lists "MCP clients" among detected tools (shadow-ai-security URL). The AI Agent Gateway sits "inline between AI agents and SaaS MCP servers". Its connectors are Atlassian, Salesforce and Microsoft 365, and agents need registration (What's New URL). Discovery of local or self-hosted MCP servers: Not found in public docs.

**6. Cloud AI asset discovery.** Marketing names an AWS Bedrock API connector for sanctioned usage (forcepoint.com/use-case/ai-usage-monitoring). Help docs list only "ChatGPT Enterprise, Microsoft Copilot, and Claude Enterprise" (What's New URL). Discovery of models, endpoints or AI resources in cloud accounts: Not found in public docs.

**7. Enforcement.** Shadow AI access control "Requires Cloud Web Security" for DLP customers (What's New URL). Marketing lists "Inline allow, restrict or block per AI application" plus user coaching and personal-account blocking (shadow-ai-security URL). AI DR remediation is "Audit, Copy, and Unshare", applied out of band (What's New URL). Marketing claims "automatically block, redact or allow" for prompts (forcepoint.com/ai-data-security). MCP Gateway DLP actions are "Permit and Block" (What's New URL).

**8. AI-BOM or inventory export.** An AI-BOM was Not found in public docs. Interaction logs are "exportable on demand in formats auditors recognize" (forcepoint.com/ai-data-security).

**9. Gap signals in their own words**
- Shadow AI detection needs web traffic, and tools outside the database are missed: "not yet classified as an application" (guid-15ba7ee6 URL).
- Shadow AI shows only "Which app was used, how many users used it".
- Endpoint OS: "Windows and macOS". Linux is not listed.
- The capabilities ship "on a rolling basis over the next quarter" (forcepoint.com/newsroom/2026/forcepoint-defines-how-agentic-enterprises-control-data-ai-data-security-launch).
- Customers add it to "their existing Forcepoint solution" (launch URL). UNCLEAR if a separate SKU.
- Quarantine and Delete are "Coming in future releases" (What's New URL).
- Known issue AIS-9146: Claude artifacts "are not scanned for sensitive data" (help.forcepoint.com/fpdsc/aisecurity/guid-06f6235c-056d-4854-9798-5cd2bbe40ec7.html).

**Risk to existing rows.** "No Redaction possible" conflicts with the "block, redact or allow" claim. The AI agents "No" cells conflict with AI Agent Gateway. Re-check both.

## Four Documented Gaps Favor AccuKnox on Discovery Reach

- Shadow AI discovery runs on web proxy traffic plus Windows and macOS endpoint agents. Server, container and Kubernetes discovery was not found in public docs. (guid-15ba7ee6 and What's New URLs)
- Discovery covers only apps in the X-Labs AI application database, so unlisted tools stay hidden. (guid-15ba7ee6 URL)
- Blocking shadow AI needs a Cloud Web Security entitlement. (What's New URL)
- The MCP Gateway covers 3 SaaS connectors with registered agents. Local MCP server inventory was not found. (What's New URL)
