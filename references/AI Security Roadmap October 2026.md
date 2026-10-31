# AI Security Roadmap, October 2026

AccuKnox plans 6 dated AI security items in the next 7 weeks: 2 in the last week of November and 4 in the second week of December. The live tracker is the [GitHub project board](https://github.com/orgs/accuknox/projects/34/views/1). This file is a groomed snapshot of the roadmap page as of 2026-10-28.

**How to read the refs.** Each item keeps its number from the source page, with a prefix for its list.

| Prefix | Source list |
|---|---|
| `C` | Core AI security list (the untitled first list: AI Gateway, Prompt Firewall, browser plugin) |
| `M` | ModelKnox |
| `L` | LLM Defense |
| `A` | Ask Ada |

**Status words.** Delivered, In progress, Planned, Partial, Parked, Blocked and Unscheduled. "Planned" means the source names a target and no completion. Priority (P0, P1, P2) appears only where the source gives it.

## Six Dated Items Land Before the End of December

| Ref | Item | Target |
|---|---|---|
| C18 | Redact and restore. The model sees placeholders, the user sees the originals. | Last week of November 2026 |
| C22 | SSO, with group-wise and user-wise policy | Last week of November 2026 |
| C17 | Browser plugin: block indirect injection via tools, such as hidden instructions in a web page or email that an agent fetches | Second week of December 2026 |
| C20 | Tool allow-list for AI agents | Second week of December 2026 |
| C21 | Argument inspection on agent tool calls | Second week of December 2026 |
| C23 | Policy as code: export and re-import via API, Git or Terraform | Second week of December 2026 |

C19, malicious output in AI answers, sits in the same block of the source but has no date.

## The Roadmap by Quarter

| Window | Refs |
|---|---|
| Delivered in Q3 2026 | C6, C9, C12, C13, M14, M28, M45a, M45b, M50 |
| Q3 2026 target, not marked delivered | C3 (ChatGPT), C4, C15, M6, M17, M18, M21, M22, M23, M25, M26, M27, M29 (Korean), M33, M43, M44 |
| Q4 2026 | C1, C2, C3 (Claude, Copilot, others), C4 (spillover), C5, C7, C10, C14, C16, C17, C18, C20, C21, C22, C23, M7, M8, M12, M24, M38, M45c |
| Q1 2027 | C11, M1, M2, M3, M5, M9, M11, M13, M16, M19, M20, M32, M34, M39, M46 |
| Q2 2027 | M35 |
| Q4 2027 | M49 |
| Partial | M47, M48 |
| TBD or on customer demand | M4, M10, M29 (Japanese, Arabic), M37, M47 (SharePoint) |
| Parked or blocked | C8, M30, M31, M36, M41 |
| Unscheduled | C19, M15, M40, M42, L1 to L13, A1 to A6 |

## Nine Questions for the Item Owners

Each question comes from a gap or a conflict in the source page.

1. **Q3 targets.** Q4 started on October 1. Sixteen entries still carry a Q3 target with no "delivered" mark (see the table above). Confirm each one as delivered or give it a new date.
2. **M6 and C7, document scanning.** M6 reads "WIP - Q3 Delivered". C7 lists document scanning as WIP with Yash Sanjay Kulkarni for Q4. Confirm which one is current.
3. **M49, SaaS AI control through the browser plugin.** The target reads Q4 2027. Every neighbor sits in 2026 or Q1 2027, so confirm the year.
4. **C4, GCP Agent Discovery.** The source says "Q3 Delivery/A4 SpillOver". This file reads "A4" as Q4.
5. **C19, malicious output.** The item has no date, and every item around it has one.
6. **M23, LLM-as-a-judge.** It is P0 with a Q3 target, but the evaluation metrics and the implementation are both open questions.
7. **L13.** The source reads "To scanner latency with GPUs on AWS and DO". The verb is missing. "Reduce scanner latency" is the likely meaning.
8. **Ask Ada.** The source ends with the heading "New product requirements/Operational changes" and no items under it.
9. **C5, Air India responses.** The source screenshot sits behind an expired Confluence media link, so this file drops the image. Open the Confluence page to see it.

## Runtime Protection Holds 22 Items, 6 Already Delivered

### Prompt Firewall and Runtime Guardrails

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C3 | Stateful Prompt Firewall: context remembrance across a conversation | ChatGPT Q3 2026. Claude, Copilot and others Q4 2026 | Planned | |
| C5 | Contextual, user-friendly block responses | Q4 2026 | Planned | Air India ask. Screenshot in the Confluence source |
| C9 | Streaming applications | Q3 2026 | Delivered | |
| C19 | Malicious output: links, scripts and markup in AI answers | None | Unscheduled | |
| M3 | Responses tailored for ChatGPT and Claude | Q1 2027 | Planned | |
| M38 | Contextual coaching and awareness notifications when users interact with GenAI tools | Q4 2026 | Planned | Part of Stateful Prompt Firewall. AI-DR handles it, not yet tested |
| L1 | Multimodal queries | None | Unscheduled | P0 |

### Browser Plugin and SaaS AI Control

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C6 | SaaS AI applications: visibility and blocking | Q3 2026 | Delivered | |
| C8 | Dynamic plugin update | None | Blocked | Source: "To be picked up. Cannot be done." |
| C11 | Clipboard access control in the browser | Q1 2027 | Planned | |
| C17 | Indirect injection via tools: hidden instructions in a web page or email that an agent fetches | Second week of December 2026 | Planned | |
| M48 | AI governance through a ChatGPT proxy | None | Partial | |
| M49 | Control usage of SaaS AI apps through the browser plugin | Q4 2027 | Planned | Confirm the year (question 3) |
| L5 | Tell Enterprise Claude from personal Claude, and block prompts accordingly | None | Unscheduled | |

### Data Protection and Content Scanning

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C7 | Document scanning | Q4 2026 | In progress | Owner: Yash Sanjay Kulkarni |
| C12 | Redact prompts and responses to anonymize them | Q3 2026 | Delivered | |
| C18 | Redact and restore: placeholders go to the model, originals show to the user | Last week of November 2026 | Planned | |
| M6 | Document scanning | Q3 2026 | Conflicting | Source reads "WIP - Q3 Delivered" (question 2) |
| M14 | Prompt masking | Q3 2026 | Delivered | |
| M45a | Scan uploaded files for sensitive content before they reach the model | Q3 2026 | Delivered | Listed under multimodal support for LLM Red Teaming |
| M45b | File coverage: PDF, DOCX, XLSX, PPTX, images through OCR, code files and compressed archives | Q3 2026 | Delivered | |
| M45c | Evasion detection: invisible Unicode (zero-width spaces, directional overrides), homoglyphs, GCG-style adversarial suffixes, Base64, hex and ROT13 payloads, image steganography, whitespace-encoded instructions | Q4 2026 | Planned | |

## Agent Security Carries 12 Items, Most With a Q3 Target Still Open

### Agents, MCP and Coding Assistants

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C4 | GCP agent discovery | Q3 2026, spillover to Q4 | In progress | Doc AI work in progress |
| C15 | Power Platform support and visibility | Q3 2026 | In progress | Backend done, frontend in progress |
| C16 | Pipeline view support beyond 10 agents | Q4 2026 | In progress | The current view breaks past 10 agents. Design in progress |
| C20 | Tool allow-list for AI agents | Second week of December 2026 | Planned | |
| C21 | Argument inspection on agent tool calls | Second week of December 2026 | Planned | |
| M17 | Power Apps onboarding for Azure | Q3 2026 | In progress | Collector built |
| M25 | Secure Claude Code, Codex and other coding agents | Q3 2026 | Planned | |
| M26 | Auto behavior discovery of MCP servers and ML tooling such as Jupyter Notebook and PyTorch | Q3 2026 | Planned | |
| M36 | Skills scanner | None | Parked | |
| M43 | System-level observability for AI agents with eBPF | Q3 2026 | Planned | Handled through the Omni scanner |
| M44 | MCP server security | Q3 2026 | Planned | P0. Unmanaged assets already give visibility |
| M47 | Copilot and SharePoint AI security | Copilot done. SharePoint on demand | Partial | |

## Red Teaming Has 9 Items, With Knox RT Due in Q4 2026

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C10 | Test language models on smaller commands | Q4 2026 | Planned | |
| C14 | Knox RT implementation | Q4 2026 | In progress | Owner: Eshrath |
| M2 | Model red teaming in languages other than English | Q1 2027 | Planned | |
| M15 | Collector for adaptive red teaming | None | Unscheduled | |
| M19 | Unified Red Teaming, phase 2: file upload in the Prompts Library, self-hosted model support | Q1 2027 | Planned | |
| M23 | LLM-as-a-judge | Q3 2026 | In progress | P0. Evaluation metrics and implementation still open |
| M28 | Probe quality for red teaming | Q3 2026 | Delivered | P0 |
| M50 | Standalone red teaming of agents on-prem | Q3 2026 | Delivered | |
| L6 | Use [Shannon](https://github.com/KeygraphHQ/shannon) | None | Unscheduled | |

## Gateway and Model Integrity Hold 15 Items, 7 Without a Date

### AI Gateway, Cost and Performance

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C1 | AI Gateway v2.0: load balancing, token utilization, failover | Q4 2026 | Planned | |
| M11 | Model routing in the AI Gateway | Q1 2027 | Planned | |
| M22 | Cost visibility in dollars on a central dashboard, with throttling or blocking past set thresholds | Q3 2026 | Planned | AI Gateway |
| L8 | Prompt Firewall performance metrics: time to first token, time to output token, token rate | None | Unscheduled | |
| L13 | Scanner latency with GPUs on AWS and DigitalOcean | None | Unscheduled | Wording incomplete (question 7) |

### Model Inventory, Integrity and Posture

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| M10 | SBOM widget on the AI dashboard | TBD | Unscheduled | |
| M12 | BYOM, bring your own model | Q4 2026 | In progress | Frontend pending |
| M24 | Model drift detection: identification and visibility | Q4 2026 | Planned | |
| M27 | AI infrastructure issue detection and automated remediation | Q3 2026 | Planned | |
| M31 | Secure RAG pipelines: knowledge base integrity, vector store access control, poisoned embedding detection, cross-tenant leak prevention, retrieval quality | None | Parked | |
| M32 | Model and data integrity check with Open Model Signing (OMS). Includes pre-red-teaming of models on Azure AI Foundry and AWS Bedrock | Q1 2027 | Planned | P1 |
| M35 | Audit trail for models ([MK-491](https://accu-knox.atlassian.net/browse/MK-491)) | Q2 2027 | Planned | P2 |
| M37 | Model versioning and updates | TBD per customer | Unscheduled | P2 |
| M42 | Risks from multi-model architectures | None | Unscheduled | |
| L11 | LLM risk database for AI-BOM ([MK-483](https://accu-knox.atlassian.net/browse/MK-483)) | None | Unscheduled | |

## Platform Work Spans Policy, APIs, Alerts, Compliance, Integrations and Languages

### Policy Management and Platform APIs

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C22 | SSO, with group-wise and user-wise policy | Last week of November 2026 | Planned | |
| C23 | Policy as code: export and re-import via API, Git or Terraform | Second week of December 2026 | Planned | |
| L4 | Pre-defined policy buckets | None | Unscheduled | P2 |
| L7 | Test a policy with sample queries while you create it | None | Unscheduled | P1 |
| L9 | API to bulk delete applications ([MK-1185](https://accu-knox.atlassian.net/browse/MK-1185)) | None | Unscheduled | |
| L10 | API to bulk delete policies ([MK-1186](https://accu-knox.atlassian.net/browse/MK-1186)) | None | Unscheduled | |
| L12 | API to enable or disable many policies at once ([MK-1187](https://accu-knox.atlassian.net/browse/MK-1187)) | None | Unscheduled | |

### Alerts, Reporting and Platform UX

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| M7 | Email alerts through Mustache templates and a webhook | Q4 2026 | In progress | |
| M8 | Tie alerts to the Air India email ID and asset ID | Q4 2026 | Planned | Air India BL |
| M9 | Automate alerts and reports. Manual report creation does not scale | Q1 2027 | Planned | Air India BL |
| M18 | UX revamp: Red Teaming view (adaptive, intelligent, generic), Prompt Firewall view, managed and unmanaged asset view | Q3 2026 | Planned | Red Teaming view deployed on Dev on 4 July 2026 |
| M33 | Historical tracking for each scan | Q3 2026 | Planned | |
| M34 | Developer mode: deeper insights for developers, normal mode for the CISO, CIO and other personas | Q1 2027 | Planned | |
| M39 | Custom reporting for AI and ML assets | Q1 2027 | Planned | |
| M41 | Global Advanced Search ([MK-567](https://accu-knox.atlassian.net/browse/MK-567)) | None | Parked | P1 |
| L2 | Alerts for violated queries | None | In progress | P0 |

### Compliance and Governance

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| M20 | ISO/IEC 27090 compliance | Q1 2027 | Planned | |
| M21 | AI compliance frameworks: ISO 42001, EU AI Act, MITRE | Q3 2026 | Planned | |
| M40 | Assess and monitor AI service provider posture: SOC 2, data handling, training data policy, breach history, API security, encryption, SLAs | None | Unscheduled | |

### Third-Party Integrations

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C2 | Microsoft Purview: visibility into Copilot agent prompts and responses | Q4 2026 | Planned | National Grid ask. [Reference video](https://youtu.be/IxcOZ5_o1N0) |
| M1 | Purview integration | Q1 2027 | Planned | P0 |
| M4 | Claude Cowork | TBD | Unscheduled | [Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry) |
| M5 | Perplexity support | Q1 2027 | Planned | CP Vietnam ask |
| M13 | Microsoft Defender integration | Q1 2027 | Planned | |
| M16 | [Straiker](http://straiker.ai/) integration | Q1 2027 | Planned | Source email: "Claude Code + no guardrails + curl = your credentials, gone." |
| M30 | Claude Mythos integration and security check | None | Parked | |
| M46 | SIEM and CDR visibility into AI usage | Q1 2027 | Planned | |

### Language Support

| Ref | Item | Target | Status | Notes |
|---|---|---|---|---|
| C13 | Korean, Vietnamese, French and Japanese | Q3 2026 | Delivered | French, Korean and Japanese by arush |
| M29 | Korean, Japanese and Arabic | Korean Q3 2026. The rest on customer demand | Planned | |
| L3 | Multilingual Prompt Firewall | None | In progress | P0 |

## Ask Ada Has 6 Items With No Date

None of the 6 Ask Ada items has a date or a status in the source.

| Ref | Item | Notes |
|---|---|---|
| A1 | Integrate tools such as KIEM, ModelKnox and API Security | |
| A2 | Multimodality | |
| A3 | AI remediation for on-prem environments | |
| A4 | Refresh platform data from the updated help docs | [AI-1226](https://accu-knox.atlassian.net/browse/AI-1226) |
| A5 | Ticketing automation through a rules engine | |
| A6 | AI-based reporting engine | |
