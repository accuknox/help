# Straiker Shadow AI Findings

Date read: 2026-10-27. Sources: Straiker's own pages only.

## A. Current Live Page

- **Overview heading:** "AccuKnox vs Straiker | Full-Stack AI Security vs Agentic Runtime Security"
- **Framing:** full-stack AI security versus "agentic runtime alone". The tone is factual, with "No documented ..." used for gaps.
- **Product terms:** Discover AI, Ascend AI, Defend AI, "Agent-SPM", "AI Sensor", "MCP Threat Database", "Chain of Threat".
- **Groups (16):** OnPrem Support, AI-SPM, AI Pipeline, Model, Dataset, Runtime, Prompt Firewalling, Session Abuse, Unsafe Content, Red Teaming, AI-DR, Incident Response, AI Gateway, SDK and Platform, Agentic AI and MCP, Deployment Flexibility.

Verbatim rows below. Line breaks are joined and source typos are kept.

**AI Platform Security (AI-SPM)**
- AccuKnox (Yes): "Multi-cloud AI inventory across AWS, Azure, GCP, and on-prem from one console / Auto-mapping of deployed AI apps with security graph view and AI-aware policy evaluation with automated remediation / 33+ compliance frameworks including ISO 27001, OWASP, and AVID mapped natively"
- Straiker (No): "Discover AI delivers AI-SPM and self-coined “Agent-SPM" — agent inventory, posture, misconfig & risky-permission detection / Focused on the agent/MCP layer (Bedrock AgentCore, Azure Foundry, Copilot Studio) rather than full multi-cloud AI asset inventory / Maps findings to OWASP Agentic Top 10, MITRE ATLAS, NIST AI RMF, EU AI Act"

**Attack Detection (AI-DR)**
- AccuKnox (Yes): "... Shadow AI detection discovers unapproved notebooks, models, and AI services across AWS, Azure, GCP"
- Straiker (Dash): "... Shadow-AGENT discovery (Discover AI) but no CloudTrail/ Azure-log AI-DR across cloud planes"

**SDK and Platform Integrations**
- AccuKnox (Yes): "... Pre-built integrations for Azure Copilot Studio, Bedrock AgentCore, and Microsoft Power Apps ..."
- Straiker (Dash): "Integrations Cursor, Claude Code, GitHub Copilot, Windsurf, MS Copilot, ChatGP Enterprise, Agentforce, Bedrock AgentCore, Azure AI Foundry, Copilot Studio, Slack AI, Box, Google Drive, LangChain / Open elemetry-based SDK + AI Sensor for Kubernetes"

**Agentic AI and MCP Security**
- AccuKnox (Yes): "... MCP tool sandboxing with least- permissive access enforcement and auto-discovery of AI agents and MCP servers"
- Straiker (Dash): "Deep agentic/MCP specialist MCP discovery, proprietary MCP hreat Database, tool-poisoning/ rug-pull/ output-in ection prevention, A2A coverage ..."

The page has no row for browser or endpoint discovery.

## B. Straiker Documented Capabilities

1. **Browser / SaaS GenAI apps:** UNCLEAR. Discover AI uses "agentic traces to map every productivity agent" ([productivity-agents](https://www.straiker.ai/solution/productivity-agents)). The same page names a "browser extension" as one deploy option. Covered apps include "MS Copilot (browser, standalone, Office suite)". No general SaaS GenAI app catalog was found.
2. **Endpoint / desktop:** Yes, described in a blog. Discover AI is "inventorying the AI applications, agents, extensions, and MCP servers" ([EDR blog, Sept 10 2026](https://www.straiker.ai/blog/why-firewalls-and-edr-miss-shadow-ai)). The blog names macOS bundle identifiers and Windows Authenticode signer data. Linux: not found in public docs (searched: the EDR blog, discover-ai, coding-agents).
3. **Server / VM / K8s installed AI software:** UNCLEAR. The same blog lists "A Docker image" and Ollama or LM Studio as endpoint evidence. The page's "AI Sensor for Kubernetes" is a Defend AI deploy option. A server or cluster inventory scan was not found in public docs (searched: discover-ai, defend-ai, the EDR blog).
4. **CLI coding agents:** Partial. Covered: "Cursor Agent, GitHub Copilot, Claude Code, and Windsurf" ([coding-agents](https://www.straiker.ai/solution/coding-agents)). Defend AI enforces through a "thin-client integration". Codex and Gemini CLI appear only as examples in blogs. They are not listed as supported.
5. **MCP discovery:** Yes. Discover AI "inventories every internal and external MCP server" ([mcp-agent-skills-security](https://www.straiker.ai/solution/mcp-agent-skills-security)). It also discovers Claude Skills ([discover-ai](https://www.straiker.ai/products/discover-ai)).
6. **Cloud agents:** "Bedrock Agentcore, Azure Foundry, and MS Copilot Studio" ([discover-ai](https://www.straiker.ai/products/discover-ai)). Agentforce and ChatGPT Enterprise are covered through productivity-agents. Vertex AI was not found in public docs.
7. **Enforcement after discovery:** Discover AI "can enforce controls to block malicious or compromised integrations" ([launch release, Mar 23 2026](https://www.straiker.ai/blog/straiker-secures-agents-building-agents)). The Agentic Kill Switch can "contain the affected agent" ([kill-switch](https://www.straiker.ai/solution/agentic-kill-switch)). For endpoint tools, the blog asks which controls "can be applied through the EDR, editor policy, or MDM". UNCLEAR whether Straiker blocks unapproved desktop apps itself.
8. **AI-BOM / export:** Not found in public docs (searched: discover-ai, ai-compliance-governance, the site map, a site search for "AI-BOM"). Discover AI keeps a "continuous agent inventory and audit trail".
9. **Gap signals in their words:**
   - Their own guide says: "Not for shadow AI or employee usage controls" ([top-7 blog, May 28 2026](https://www.straiker.ai/blog/top-7-ai-agent-visibility-and-governance-platforms)).
   - The same guide says: "Straiker governs sanctioned, deployed agents."
   - Usage-control buyers "will want a usage controls solution alongside Straiker".
   - The EDR blog promises the scanning design in "the next post" (quick and deep scan modes). That design is not yet published.
   - No Preview or Beta label was found.

## Strongest Documented Contrasts

- Straiker's own May 2026 guide says Discover AI is "Not for shadow AI or employee usage controls". The September 2026 endpoint blog moves toward shadow AI but sends enforcement to EDR and MDM. [top-7](https://www.straiker.ai/blog/top-7-ai-agent-visibility-and-governance-platforms), [EDR blog](https://www.straiker.ai/blog/why-firewalls-and-edr-miss-shadow-ai)
- The endpoint discovery evidence names macOS and Windows only. No Linux, server or Kubernetes inventory of installed AI software was found. [EDR blog](https://www.straiker.ai/blog/why-firewalls-and-edr-miss-shadow-ai)
- No AI-BOM or inventory export appears in Straiker's public pages. [discover-ai](https://www.straiker.ai/products/discover-ai)
- Cloud discovery is limited to agent-builder platforms: Bedrock AgentCore, Azure Foundry and Copilot Studio. Straiker documents no discovery of cloud notebooks, models or AI services from cloud logs. [discover-ai](https://www.straiker.ai/products/discover-ai)
- Coding-agent coverage names four tools (Cursor, Copilot, Claude Code, Windsurf). Codex CLI and Gemini CLI are not in the supported list. [coding-agents](https://www.straiker.ai/solution/coding-agents)
