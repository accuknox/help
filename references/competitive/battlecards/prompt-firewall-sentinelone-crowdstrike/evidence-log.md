# Evidence Log, AI Prompt Firewall Stack Ranking

Draft: `references/drafts/comparison/ai-prompt-firewall-stack-ranking-accuknox-sentinelone-crowdstrike.md`.
Firecrawl read every rival page on 2026-10-13. The raw scrapes sit in `research/crwd/` (31 pages) and `research/s1/` (20 pages). Each row names the vendor page and a verbatim quote from it.

## AccuKnox Sources Are All Tier D

| Rows | Fact | Source |
| --- | --- | --- |
| 1, 2, 18, 19 | Plugin intercepts prompts and responses on 5 AI apps. Request log holds direction, verdict and latency, with JSON export | `docs/integrations/chrome-browser-integration.md`, `docs/getting-started/3.6-release.md` |
| 2, 5 | `scanPrompts`, `scanResponses`, Response Mode `overlay`, Timeout `2000`. Force install on Chrome and Edge for Windows, Chrome for macOS | `docs/integrations/intune-browser-plugin-deployment.md` |
| 3 | Attachment Type scanner. Only the extension is sent. Generated files are not monitored | `docs/getting-started/3.6-release.md` |
| 4, 9, 14, 19 | AI tool allow-list, AI Gateway, custom policies in plain language, latency trend | `docs/getting-started/3.7-release.md` |
| 5 | Firefox and Safari load as temporary add-ons and unload on restart | `docs/getting-started/3.5-release.md` |
| 6 | `pip install accuknox-llm-defense`, `scan_prompt`, `scan_response`, `session_id` | `docs/how-to/llm-defense-app-onboard.md` |
| 7 | LiteLLM callback. Bifrost "only logs and categorizes" and "does not actively block" | `docs/integrations/litellm.md`, `docs/integrations/bifrost-integration.md` |
| 8 | Azure APIM through Bicep, AWS API Gateway through Terraform, Apigee proxy with `continueOnError="true"` | `docs/getting-started/azure-ai-foundry.md`, `docs/how-to/aws-apim.md`, `docs/integrations/apigee-integration.md` |
| 10 | Developer CLI tool maps to a gateway proxy configuration. The plugin sees browser traffic only | `docs/integrations/ai-overview.md` |
| 11 | Power Apps flow, prompt scan and response scan endpoints, shared session ID | `docs/integrations/powerapps-integration.md` |
| 12, 13, 15, 16 | 14 policy types, stateful conversation tracking, Anonymize, global and local policies, the probabilistic guardrail warning | `docs/use-cases/prompt-firewall-overview.md` |
| 17, Faster | On-prem parity, air-gapped support, "Within minutes" and "30 min - 4 hours" | `docs/how-to/aiml-saas-vs-onprem.md` |

## Product Screens Viewed and Linked

Each image was opened from `docs/` on 2026-10-13, and its live URL passed `verify_links.py`.

| Screen | Live URL | What it shows |
| --- | --- | --- |
| Architecture | https://help.accuknox.com/use-cases/image-1.png | Traffic controller, policy governance, audit log, input and output stops |
| Policy types | https://help.accuknox.com/use-cases/image.png | Console catalog of prompt policy types |
| Query details | https://help.accuknox.com/use-cases/images/image2.png | Blocked prompt with BanCode and PromptInjection results |
| Browser banners | https://help.accuknox.com/getting-started/images/release-notes/v3.6/prompt-firewall-browser-plugin-platforms.png | "Prompt blocked: Policy violation" on Microsoft Copilot, Gemini, GitHub Copilot |
| Attachment Type | https://help.accuknox.com/getting-started/images/release-notes/v3.6/prompt-firewall-attachment-type.png | Allowed extensions and a PDF denied with `query_status` BLOCK |
| Custom policy | https://help.accuknox.com/getting-started/images/release-notes/v3.7/prompt-firewall-custom-policy.png | Policy description, violating examples, safe examples |
| AI Gateway | https://help.accuknox.com/getting-started/images/release-notes/v3.7/ai-gateway-applications.png | Prompt Firewall toggle with queries, violations, blocked |
| Azure APIM flow | https://help.accuknox.com/getting-started/image-57.png | Prompt scan and response scan around Azure AI Foundry |

Three screens were viewed and left out. `docs/integrations/image-65.png` shows request latency from 412 ms to 1253 ms. `docs/how-to/images/prompt-firewall/ai-security-dashboard.png` shows test application names. `docs/integrations/image-48.png` names the database, the hosting region and a 90-day retention period.

## CrowdStrike Falcon AIDR Cells Cite 9 Public Docs Pages

| Row | Status | Source | Quote |
| --- | --- | --- | --- |
| 1 | Parity | https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies | You can use browser collectors to enforce input rules that block or redact sensitive data before it reaches the AI provider. |
| 2 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/policies | You can use browser collectors to detect threats in AI responses, but they can't modify what users see. Output rules automatically run in Report Only Mode |
| 3 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint/network-inspection | No file attachments - AIDR doesn't process file attachments from network events. |
| 4 | Parity | https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access | Use site access rules to block, redirect, report, or ignore visits to sites monitored by the browser collector. |
| 5 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/chrome | The CrowdStrike-hosted browser extension version 1.x.x requires an enterprise-managed machine: Enrolled in MDM, such as Intune or Jamf. Joined to an Active Directory domain. Registered with Microsoft Entra ID |
| 5 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors | Windows, Mac (Chrome, Edge). Web-based AI tools. AIDR for Workforce + Falcon Insight XDR. Falcon Endpoint |
| 6 | Leads | https://aidr-docs.crowdstrike.com/docs/aidr/collectors | Any (Python, JS, Go, cURL). Any LLM provider. AIDR for Agents. Application. SDK / API |
| 7, 8 | Parity, Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors | Gateway - Apply AIDR policies to data flowing through supported API gateways. Apigee, Azure API Management, Kong Gateway and Kong AI Gateway, LiteLLM AI Gateway, Portkey AI Gateway, TrueFoundry AI Gateway, JetStream AI Hub |
| 7 | Parity | https://aidr-docs.crowdstrike.com/docs/aidr/collectors | Kong Gateway. This collector doesn't support streaming responses. |
| 9 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors | Same gateway list as rows 7 and 8. No CrowdStrike-built gateway appears in it. |
| 10 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors/falcon-endpoint | Network Inspection. Platform: Windows. Input enforcement: Report. Output enforcement: Not captured. |
| 10 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors | This collector doesn't monitor LLM responses, model configuration, token usage, extended thinking, system prompts, or subagent context. |
| 11 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/collectors | During enforcement, the collector analyzes only the tool name and parameters - not the user prompt or conversation history. |
| 12 | Parity | https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules | Detector headings: Malicious Prompt, Malicious Entity, MCP Validation, Confidential and PII Entity, Secret and Key Entity, Language, Code, Competitors, Custom Entity, Topic, Emoji, Malicious Skills and Tools. Topics: Financial, Legal, Religion, Politics, Health, Toxicity, Negative sentiment, Self-harm and violence, Roleplay, Weapons, Criminal conduct |
| 13 | Not shown | https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules | Prompt rules inspect and act on the content of requests and responses that your collector intercepts from AI systems. A search of all 31 scraped pages for "multi-turn" and "conversation history" matched the Copilot Studio line only. |
| 14 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules | Custom Entity - Lets you create and apply custom rules based on text patterns. Custom Malicious Prompt Detection - Provide examples of malicious prompts for better accuracy. |
| 15 | Leads | https://aidr-docs.crowdstrike.com/docs/aidr/policies/prompt-rules | Redact action headings: Replacement, Mask, Partial Mask, Hash, Format Preserving Encryption (FPE) |
| 16 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr/policies | Each policy type corresponds to a collector category. You can reuse policies across multiple collectors of the same type. |
| 17 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr | CrowdStrike clouds: Available in US-1, US-2, and EU-1 |
| 18 | Parity | https://aidr-docs.crowdstrike.com/docs/aidr | Original prompts and AI responses. Request metadata (timestamp, user ID, device ID, application ID, collector ID, etc.). Detection results |
| 19 | Not shown | https://aidr-docs.crowdstrike.com/docs/aidr | Same metadata list as row 18. The list ends in "etc.", so a latency field may exist without being named. |
| 20 | Limited | https://aidr-docs.crowdstrike.com/docs/aidr | AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in Falcon Guardian with expanded AI security. |
| Cheaper | - | https://aidr-docs.crowdstrike.com/docs/aidr | Requires one or more of these subscriptions: AIDR for Workforce, AIDR for Agents |

## SentinelOne Prompt Security Cells Cite 7 Public Pages

| Row | Status | Source | Quote |
| --- | --- | --- | --- |
| 1, 15 | Parity | https://www.sentinelone.com/platform/prompt-security-ai-usage-control/ | Redact PII, secrets, and other sensitive data at the edge, inline, before a prompt ever leaves the device |
| 2 | Not shown | https://www.sentinelone.com/blog/a-new-chapter-for-ai-and-cybersecurity-sentinelone-acquires-prompt-security/ | Every prompt and response is captured with full context, giving security teams searchable logs for audit and compliance. |
| 4 | Parity | https://www.sentinelone.com/platform/securing-ai-prompt/ | Redact sensitive data and enforce policies across 15,000+ AI services in real time |
| 5 | Not shown | https://prompt.security/blog/the-key-layer-in-ai-security-browser-and-endpoint-sensors | you need local, purpose-built sensors: a browser extension and a dedicated AI endpoint agent. |
| 6, 19 | Parity, Limited | https://www.sentinelone.com/platform/prompt-security-ai-application-security/ | Deploy instantly with a single line of code. Add zero latency and zero disruption to the user experience |
| 9 | Limited | https://www.sentinelone.com/blog/a-new-chapter-for-ai-and-cybersecurity-sentinelone-acquires-prompt-security/ | Prompt Security's MCP Gateway sits between AI applications and more than 13,000 known MCP servers, intercepting every call, prompt template, and response. |
| 10 | Parity | https://www.sentinelone.com/platform/prompt-security-ai-usage-control/ | Track every AI code assistant in the environment, including GitHub Copilot, Cursor, and Claude Code |
| 11 | Limited | https://www.sentinelone.com/press/sentinelone-announces-ai-security-integration-with-amazon-bedrock-agentcore-to-deliver-runtime-guardrails-for-ai-agents/ | The upcoming integration will be available in Amazon Bedrock AgentCore later this year. |
| 12, 13 | Parity, Not shown | https://www.sentinelone.com/platform/prompt-security-ai-application-security/ | A runtime firewall inspects every prompt and response bidirectionally. It blocks prompt injection and jailbreak attempts inbound and scrubs sensitive data, toxicity, and off-brand or hallucinated content outbound. |
| 14, 18 | Not shown, Parity | https://www.sentinelone.com/platform/prompt-security-ai-usage-control/ | Set granular, role-based AI usage rules by department and user. Review every prompt, redaction, and policy action in one place, with a full audit trail |
| 16 | Parity | https://www.sentinelone.com/platform/securing-ai-prompt/ | Turn red teaming findings into production guardrails automatically, on a shared policy fabric |
| 17 | Parity | https://www.sentinelone.com/press/sentinelone-brings-ai-security-to-on-premise-regulated-sovereign-self-hosted-and-airgapped-environments/ | SentinelOne's Prompt Security On-Premises adds these same protections to the world of AI, even in fully disconnected environments. |
| 20 | Parity | https://www.sentinelone.com/platform/securing-ai-prompt/ | Prompt Security is built into the SentinelOne Singularity Platform. |

## Checks a Reviewer Should Run

- SentinelOne has no public technical docs for Prompt Security. `docs.prompt.security` did not resolve on 2026-10-13. Ten SentinelOne cells read "Not shown" or "Limited" for that reason. A SentinelOne customer login would settle rows 2, 3, 5, 7, 8, 13 and 14.
- CrowdStrike Falcon Guardian docs need a login. Every CrowdStrike cell cites the AIDR docs, which state that Guardian continues the same capabilities. Recheck rows 2, 9 and 13 against Guardian before the page ships.
- Row 9 marks the AccuKnox AI Gateway as shipped, from `docs/getting-started/3.7-release.md`. `references/source-of-truth/ai-security-data-points.md` still carries the 2026-09-26 ruling that tags it "Coming soon". Confirm with product and update that file.
- Row 2 rests on the request log showing a RESPONSE direction with an ALLOW or BLOCK verdict, and on the `scanResponses` and `overlay` settings. No AccuKnox doc shows a screenshot of a blocked response in the browser.
- Tier I facts were left out: personal-account blocking, Microsoft Purview labels, attachment content scanning, clipboard and paste control, and the named CLI agents Codex, Kiro and Claude Code.
- The tally is 9 AccuKnox leads, 9 parity and 2 CrowdStrike leads (rows 6 and 15). A row counts as an AccuKnox lead when both rival cells read Limited or Not shown.
