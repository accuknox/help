---
title: AccuKnox AI Security Data Points
updated: 2026-09-25
use: Facts for any AI security writing in this repo, such as docs, blogs, comparisons, RFPs, decks and battlecards
---

# AccuKnox AI Security Data Points

This file collects the AI security facts that surfaced while the Netskope battlecard was rebuilt on
2026-09-25. Each fact carries its source tier, so you know whether it can ship on a public page.
Check this file before you write about shadow AI, the Prompt Firewall, managed agents, model
security or AI for Security features.

The accuracy rule in `.claude/core/runtime-contract.md` still governs. Open the named source
before a fact from this file goes into a page.

## Source Tiers Decide Where a Fact Can Ship

| Tier | Meaning | Where it can ship |
| --- | --- | --- |
| **D** | A `help.accuknox.com` page or a release note in `docs/` states it | Anywhere |
| **I** | An internal AccuKnox asset in `references/` states it | Sales PDFs, decks, RFP answers. Confirm with product before a public web page |
| **A** | An AccuKnox team member asserted it, and no doc or asset shows it yet | Only when the requester confirms it for that piece. Flag it in the reply |

When you promote a fact from tier I or A to tier D, update its row here.

## Shadow AI Covers Four Surfaces

Source: `references/source-of-truth/shadow-ai-coverage.pdf`, coverage status as of September 2026.
Tier I. The shadow AI discovery page is `docs/use-cases/shadow-ai-discovery.md`, tier D for host
and cluster scanning.

| Surface | Status | Mechanism | Controls and coverage |
| --- | --- | --- | --- |
| Browser plugin | Full coverage | A browser extension inspects prompts and file uploads before they reach the AI app | Blocks sensitive uploads. Masks PII, PHI and PCI. Stops secrets and confidential code. Allows approved tools only, such as ChatGPT Enterprise. Keeps a prompt and response audit trail. Covers ChatGPT, Claude.ai, Gemini, Microsoft Copilot and GitHub Copilot |
| Host scanning | Linux and macOS full, Windows in progress | Scans VMs and containers and fingerprints AI software in 7 categories, with a severity per finding | Covers managed and unmanaged AI assets |
| Desktop telemetry app | Beta | Collects the OpenTelemetry that desktop AI tools emit, plus their HTTPS traffic | Identifies the agents, tools and skills in use. Covers Claude Code. Built on the open-source KubeArmor OTel adapter at `github.com/kubearmor/otel-adapter` |
| CLI agent security | Full coverage | A gateway proxy configuration routes CLI agent traffic through the Prompt Firewall | Blocks prompt injection and jailbreaks. Prevents secret, credential and confidential code leaks. Keeps prompt and response forensics. Covers OpenAI Codex, Kiro and Claude Code |

All four surfaces report to one AccuKnox control plane with one AI asset inventory, one set of
guardrails and one audit trail. The inventory exports as an AI-BOM in CycloneDX format.

### The Seven Host-Scan Categories Carry Example Counts

These counts come from one monitored environment over 60 days, from 26 July to 23 September 2026. The
tenant is anonymized, so never name it or imply it is a named customer. Use them in a blog post or a
case study with that context. Leave them off a battlecard.

| Category | Assets found | Critical findings |
| --- | --- | --- |
| AI/ML frameworks | 2,308 | 72 |
| AI SDKs | 1,180 | 9 |
| AI automation | 296 | 6 |
| AI agents | 124 | 12 |
| MCP servers | 53 | 1 |
| AI inference engines | 40 | 2 |
| AI gateways | 25 | 28 |
| **Total** | **4,026** | **130** |

## The Prompt Firewall Handles Thirteen Browser Use Cases

Source: the "Prompt Firewall Use Cases" tab of the AI Security Checklist Google Sheet, Drive ID
`1IajfllcBXQXcaqruI-kXEXlwiFRnRIZeivJs3t9AIS8`. The repo copy is
`references/source-of-truth/ai-security-checklist.md`, with the `.xlsx` export beside it. Tier I. The sheet is a POC checklist, so each row is a
capability AccuKnox scopes into a proof of concept. Confirm a row against
`docs/use-cases/prompt-firewall-overview.md` before a public page uses it.

| Use case | What AccuKnox does | POC priority |
| --- | --- | --- |
| Identity and tenant enforcement | Detects the login identity, SSO, email domain and tenant ID, and blocks personal accounts such as Gmail | Must |
| Shadow AI app discovery | Finds sanctioned and unsanctioned GenAI apps, extensions and sessions in the browser | Must |
| Prompt sensitive data inspection | Inspects prompts for PII, PHI, PCI, secrets, credentials, source code and custom patterns | Must |
| AI security taxonomy | Classifies prompt injection, prompt extraction, jailbreak, system-prompt override, RAG poisoning, data exfiltration, malicious code and harmful content | Must |
| Policy actions | Allow, warn, redact, block, or require a business justification, per data class, risk category, user, group and app | Must |
| Attachment upload control | Intercepts upload, drag-and-drop and attachment events, with a global block, a file-type allowlist or a per-app policy | Must |
| Microsoft Purview label enforcement | Reads Purview sensitivity labels, allows labels such as General and blocks Confidential, Highly Confidential and custom labels | Must |
| Attachment content scanning | Scans document content for PII, PHI, PCI and secrets even when the label looks permissible | Must |
| Response sensitive data filtering | Redacts, warns or blocks sensitive data in model responses | Must |
| Clipboard and paste protection | Inspects paste and form-submit events | Good to have |
| Source code and IP protection | Detects proprietary code, architecture and credentials and enforces enterprise-AI-only policies | Good to have |
| Response threat filtering | Inspects responses for malicious links, exploit help and unsafe content | Good to have |
| Interaction telemetry and risk scoring | Captures user, app, tenant, risk category, data class, attachment metadata, action and outcome, and scores session and user risk | Must |

Tier D facts for the same product: 14 policy classes, a stateful engine that scores a whole session
by `session_id`, and the v3.6 Attachment Type scanner. Sources are
`docs/use-cases/prompt-firewall-overview.md` and `docs/getting-started/3.6-release.md`. The browser
plugin runs on Chrome, Edge and Firefox, v3.5 adds Safari and Brave, and Intune can force-install it.
Sources are `docs/integrations/chrome-browser-integration.md`,
`docs/integrations/intune-browser-plugin-deployment.md` and `docs/getting-started/3.5-release.md`.

## Integration Coverage Spans Cloud, On-Prem and Managed Agents

Source: the "AI Security Checklist" tab of the same sheet and the same repo copy, tier I, unless a row names a doc.

| Area | Coverage | Tier and source |
| --- | --- | --- |
| Cloud model and agent platforms | Azure AI Foundry, Amazon Bedrock, Google Model Garden, Vertex AI | D, `docs/support-matrix/aiml-support-matrix.md`. The matrix is a set of images, so read them rather than grep |
| On-prem model platforms | vLLM, Hugging Face, Run:ai | D for vLLM and Triton, `docs/how-to/aiml-vllm-collector.md` and `docs/how-to/aiml-triton-collector.md`. I for Run:ai |
| Managed-agent platforms | Amazon Bedrock AgentCore, Microsoft Copilot Studio, Microsoft Power Apps, Microsoft 365, Google Agent Engine | D for AgentCore, Copilot Studio, M365 Agents, Azure AI Foundry and Bedrock Agent, `docs/getting-started/3.5-release.md`. D for Power Apps, `docs/integrations/powerapps-integration.md`. I for Agent Engine |
| Agent-first view | Managed agents are discovered and listed per agent across platforms | D, `docs/getting-started/3.5-release.md` shows a managed agent list filtered by cloud provider. "Agent-first" as a phrase is positioning |
| AI gateways | Bifrost, LiteLLM, Kong AI | D for Bifrost and LiteLLM, `docs/integrations/ai-overview.md`. I for Kong AI |
| API gateways | Azure APIM, AWS API Gateway, Apigee | D, `docs/integrations/ai-overview.md` |
| Agent sandboxing | DaemonSet on Kubernetes, systemd on VMs | I. The sandbox itself is D, `docs/use-cases/modelarmor.md`, which does not name the install modes |
| Dataset and compute | Dataset exposure, PII and PHI scans, compute exposure and vulnerabilities | I |
| DevSecOps | AIBOM in the repo, build blocking on AI risk, model scans in the build, scheduled scans | D for AIBOM and CI/CD model scans, `docs/getting-started/xbom-setup.md` and `docs/how-to/model-scan-cicd.md` |

## AI for Security Covers Four Features

AI for Security means AccuKnox uses AI to improve its own security workflows. Pair it with Security
for AI, the protection of the customer's AI, in any two-group comparison.

| Feature | Fact | Tier and source |
| --- | --- | --- |
| AI SAST | Opt-in AI analysis of SAST findings, powered by Anthropic, marks false positives and assesses severity | D, `docs/getting-started/3.4-release.md` |
| AI SAST | An "AI Enabled SAST" option in the scan-type selector adds AI analysis on top of the static scan | D, `docs/getting-started/3.7-release.md` |
| DAST | 4 scan types, from a passive baseline to Advanced Active Penetration Testing rules | D, `docs/how-to/dast-scan-types.md` |
| DAST | A recorded browser login scans behind MFA, TOTP codes included | D, `docs/getting-started/3.6-release.md` |
| AI DAST | AI inside the DAST engine | A. No doc names an AI step in DAST yet. Describe the documented DAST facts instead |
| AgentZ | A job described in one sentence becomes a skill with wired steps. Each agent runs in a default-deny sandbox, holds no secret and writes a replayable trace. It runs from chat, API, CLI or cron | D, `docs/agentz/index.md` |
| AI-powered pentesting | Automated attacks on the app and the model, run on demand or on a schedule | A for the "AI-powered pentesting" name. D for the parts, `docs/use-cases/red-teaming.md` and `docs/how-to/dast-scan-types.md` |

## Asserted Facts That Need a Source

Tier A. The requester supplied each one for the Netskope battlecard. Each needs a doc before a web
page can use it.

- Cloud AI security covers OCI as a fourth public cloud. The AI/ML support matrix names AWS, Azure
  and GCP only.
- AccuKnox covers NVIDIA environments and AI factories. Docs show NVIDIA Triton support, tier D, but
  not the "AI factory" framing.
- Power Apps agents appear in the same managed-agent view as Bedrock AgentCore and Copilot Studio.
  The v3.5 view lists the other two, tier D. Power Apps has its own integration page, tier D, but no
  doc shows it in that view.

## Competitor Gaps Found, Netskope

Read from docs.netskope.com on 2026-09-24. The full log with URLs is
`references/competitive/battlecards/netskope/evidence-log.md`, and the cells sit in
`references/drafts/comparison/accuknox-vs-netskope-ai-security.md`.

- The Secure Web Gateway identifies 3,300+ GenAI apps. AI Guardrails run inline for 20 listed apps.
- The Netskope Client misses AI in VMs and containers that do not run the Client, by Netskope's own
  statement. It runs on Windows and macOS with Client 138 or later.
- AI Platforms discovery and posture is a Preview feature. Agent Action Control is Beta.
- The management console runs only in the Netskope cloud tenant.
- The AI Gateway is a 16 vCPU appliance billed per gateway plus monthly transactions.
- DLP and Agentic Broker are separate licenses.
- The AI Security docs show no model file scanning, no AIBOM and no detection on AI cloud
  control-plane logs.

## Related

- `references/source-of-truth/accuknox-summary-and-narrative.md`, the positioning narrative from Nat Natraj
- `.claude/skills/accuknox-comparison-writer/references/positioning-playbook.md`, how to use these facts in a comparison
- `references/competitive/battlecards/netskope/battlecard/`, the battlecard build that uses them
