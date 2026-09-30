---
title: Shadow AI Discovery, Product Notes
updated: 2026-09-26
tier: I for rows from the coverage sheet, A for rows from the product walkthrough
---

# Shadow AI Discovery

AccuKnox finds AI that nobody approved across five surfaces. The coverage sheet names four. The
product walkthrough names four. Three overlap, so the full set is five. All surfaces report to one
AccuKnox control plane, with one AI asset inventory, one set of guardrails and one audit trail.

## Five Surfaces, Each at a Different Maturity

| Surface | Status | Mechanism | Tier and source |
| --- | --- | --- | --- |
| Cloud AI services | The most mature | Agentless API queries. AWS Bedrock and Bedrock AgentCore through Boto3. Azure AI Foundry and ML Workspace through the Azure SDK. GCP Vertex AI through the Google SDK | A, walkthrough. D for the platform list in `docs/support-matrix/aiml-support-matrix.md` |
| Browser plugin | Full coverage | An extension inspects prompts and uploads before they reach the AI app, then blocks, masks or logs them. A tool policy blocks or allowlists about 400 AI tools, for example "allow only ChatGPT and Gemini" | I for the controls, coverage sheet. A for the 400-tool list |
| Host scanning | Linux and macOS full, Windows in progress | Scans VMs and containers and fingerprints AI software in 7 categories. Runs vulnerability and malware checks on the binaries it finds. Runs on an interval, such as every 10 minutes, so it is not real time | I, coverage sheet. A for the interval and the malware check |
| Desktop telemetry app | Beta | Collects the OpenTelemetry that desktop AI tools emit, plus their HTTPS traffic, to find the agents, tools and skills in use. Runs as a local process. Built on the open-source KubeArmor OTel adapter | I, coverage sheet |
| CLI agent security | Full coverage | A gateway proxy configuration sends coding agent traffic through the Prompt Firewall | I, coverage sheet |

### Product Set the Public Status Labels on 2026-09-26

The coverage sheet and the walkthrough disagreed on three points. Product settled them as follows.

- **macOS host scanning** shows "Beta" on public pages. Linux stays "Full coverage".
- **The desktop telemetry app** shows "Beta".
- **The fourth surface.** Present all five surfaces.

Every page that shows a "Beta" label also shows a legend. "Full coverage" means generally available,
"Beta" means available now with coverage still growing, and "In progress" means not yet available.

## Each Surface Answers One Risk

| Surface | The risk | Covers |
| --- | --- | --- |
| Browser plugin | Staff paste contracts, source code and customer records into public chat apps | ChatGPT, Claude.ai, Gemini, Microsoft Copilot, GitHub Copilot |
| Host scanning | Developers install agents, SDKs, MCP servers and inference engines that never appear in cloud accounts or IAM logs | AI/ML frameworks, AI SDKs, AI automation, AI agents, MCP servers, AI inference engines, AI gateways |
| Desktop telemetry app | Desktop agents call tools, load skills and reach external services that no inventory records | Claude Code and other desktop AI tools. [confirm the app heard as "HubMace"]. Kiro |
| CLI agent security | CLI agents run with the developer's shell access and can send code, secrets and credentials to external models | OpenAI Codex, Kiro, Claude Code |
| Cloud AI services | Teams deploy models and agents in cloud accounts outside the approved list | Bedrock, AgentCore, Azure AI Foundry, Azure ML, Vertex AI |

Browser plugin controls, tier I. Block sensitive uploads. Mask PII, PHI and PCI data. Stop secrets
and confidential code. Allow approved tools only, such as ChatGPT Enterprise. Keep a prompt and
response audit trail.

CLI agent controls, tier I. Block prompt injection and jailbreaks. Prevent secret and credential
leaks. Prevent confidential code uploads. Keep prompt and response forensics.

## One Environment Found 4,026 Unmanaged AI Assets in 60 Days

Host scanning ran in one monitored environment from 26 July to 23 September 2026. The tenant is
anonymized, so never name it. Tier I. The per-category table lives in
`references/source-of-truth/ai-security-data-points.md`.

Product ruled on 2026-09-26 that the exact counts never appear on a public page. Write "4K+" for
assets, "100+" for critical findings and "50+" for MCP servers. The exact figures below are for
internal use only.

| Measure | Value |
| --- | --- |
| Unmanaged AI assets found on hosts | 4,026 |
| Critical findings on those assets | 130 |
| AI asset categories fingerprinted | 7 |
| Largest category | AI/ML frameworks, 2,308 assets |
| Most critical findings per asset | AI gateways, 28 critical findings on 25 assets |

## The Browser Plugin Misses Tools Outside Its List

The plugin only detects the tools on its list of about 400. A tool outside that list needs its own
integration. Tier A.

The best interception point for shadow AI is the secure web gateway or CASB layer, such as Zscaler
or Netskope, because all HTTPS traffic passes there. AccuKnox has no product at that layer. Do not
position AccuKnox as a CASB replacement. Position it as endpoint and cloud coverage that works beside
the CASB. Tier A.

## macOS Notarization Would Close the Desktop Gap

AccuKnox is working on macOS notarization. With it, an EDR-level agent could intercept all desktop
and network traffic on a Mac, and Mac discovery would no longer depend on the host scanner. This is
a future capability. Do not sell it today. Tier A.

## The Market Leader Started in the Browser

The product team named [confirm the vendor, heard as "Quiller"] as the market leader in shadow AI
discovery. That vendor started with a browser plugin and now covers desktop telemetry and host
scanning. Tier A. Confirm the vendor name and its coverage from its own site before a comparison
page uses it.

AccuKnox differs in three ways. It links discovery to the wider CNAPP. It enforces with the Prompt
Firewall. It adds red teaming on top of discovery. On the desktop, AccuKnox uses the OpenTelemetry
connector and does not deploy a binary agent.

## Four Lines Answer the AE Questions on Shadow AI

- Lead with "you can't govern what you can't see. We give you an inventory across cloud, browser,
  host and desktop."
- State the gaps. Windows host scanning is in progress. macOS host scanning and desktop telemetry
  are in beta.
- Against the market leader. "We cover the same surfaces, and we enforce. The prompt firewall, red
  teaming and CNAPP integration are native."
- Against Zscaler or Netskope. Do not compete on network interception. Position AccuKnox as the
  endpoint and cloud layer beside them.

## Related

- `docs/use-cases/shadow-ai-discovery.md`, the public page, tier D for host and cluster scanning
- `references/source-of-truth/shadow-ai-coverage.pdf`, the coverage sheet
- `ai-gateway.md`, the enforcement layer that pairs with discovery
