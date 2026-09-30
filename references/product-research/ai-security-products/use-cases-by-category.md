---
title: AI Gateway and Shadow AI Use Cases by Category
updated: 2026-09-26
use: Source list for product pages, solution pages, FAQs and sales enablement
---

# AI Gateway and Shadow AI Use Cases by Category

This file sorts every use case from the product walkthrough, the Shadow AI coverage sheet and the
live accuknox.com pages into three groups. Each row names a buyer, the job and the source tier. The
live pages were read on 2026-09-26.

1. **AI gateway, the category.** What any AI gateway does, and how AccuKnox secures the gateways a
   customer already runs.
2. **The AccuKnox AI Gateway.** What the AccuKnox product adds.
3. **Shadow AI.** Discovery and control of AI that nobody approved.

## Group 1, AI Gateways as a Category Need Inventory and Policy

| Use case | Buyer and job | Tier and source |
| --- | --- | --- |
| Integrate the gateway the customer already runs | A platform team on Bifrost or LiteLLM wants AccuKnox policy on that traffic | D, `docs/integrations/ai-overview.md` |
| Integrate Kong AI Gateway | A team on Kong wants the same | I, AI Security Checklist |
| Read AI traffic at the API gateway | An enterprise that fronts models with Azure APIM, AWS API Gateway or Apigee | D, `docs/integrations/ai-overview.md` |
| Find unmanaged AI gateways on hosts | A security team learns which teams run their own gateway. In one environment, 25 AI gateways carried 28 critical findings | I, coverage sheet |
| Merge API management and AI gateway design | An enterprise architect plans one layer for API and model traffic | A, walkthrough |
| Enforce one prompt policy at the gateway | A security lead wants the same policy at the API gateway, the SDK, the browser plugin and Copilot Studio | Live page, `/platform/ai-security`, Prompt Firewall module |

## Group 2, the AccuKnox AI Gateway Adds Visibility, Governance and a Native Firewall

| Use case | Buyer and job | Tier and source |
| --- | --- | --- |
| Inventory every model call | A CISO wants to know which models the company uses and who calls them | A, walkthrough |
| Govern model access by policy | A platform team allows a model per team, app or data class | A, walkthrough |
| Rate-limit model usage | A platform team caps usage per team or app | A, walkthrough |
| Run the prompt firewall inline | A security team inspects every prompt and response on the gateway path, with the existing Prompt Firewall policy types | A for the native firewall. D for the policy types, `docs/use-cases/prompt-firewall-overview.md` |
| Govern local models for BYOM | A regulated buyer runs on-premises LLMs and needs one control plane for them | A, walkthrough |
| Run in an air-gapped network | A bank or government buyer cannot use a cloud-hosted gateway | A, walkthrough |
| Route CLI coding agents through the firewall | An engineering lead puts Codex, Kiro and Claude Code traffic under policy | I, coverage sheet, CLI agent security surface |
| Serve as the model layer for AI SAST | AI SAST calls its models through the AccuKnox AI Gateway | A, walkthrough |

The live site names the gateway only once, as "AI Gateway Enforcement" in the Prompt Firewall
Dashboard tab on `/platform/ai-security`. No page describes the AccuKnox AI Gateway yet.

## Group 3, Shadow AI Covers Five Surfaces and Three Compliance Jobs

| Use case | Buyer and job | Tier and source |
| --- | --- | --- |
| Stop data leaks into public chat apps | A CISO stops staff pasting contracts and customer records into ChatGPT or Gemini | I, coverage sheet, browser plugin |
| Allow approved AI tools only | IT allows ChatGPT Enterprise and blocks the rest | I, coverage sheet. A for the list of about 400 tools |
| Inventory AI software on servers | A security team finds agents, SDKs, MCP servers and inference engines on VMs and containers | I, coverage sheet. D for host and cluster scanning, `docs/use-cases/shadow-ai-discovery.md` |
| Find MCP servers | A security team finds MCP servers that no register lists. 53 found in one environment | I, coverage sheet |
| See what desktop agents do | A security team sees the tools and skills that Claude Code and similar apps use | I, coverage sheet, beta |
| Put guardrails on CLI coding agents | An engineering lead stops secrets and code leaving through terminal agents | I, coverage sheet |
| Find unapproved cloud AI deployments | A cloud team finds Bedrock, Azure AI Foundry or Vertex AI deployments outside the approved list | A, walkthrough. The live `/platform/ai-security` AI DR module describes the same detection from cloud logs |
| Keep a live model inventory for a regulator | A bank shows the RBI a complete inventory that includes unregistered models | Live blog, `accuknox.com/blog/rbi-model-risk-management-ai-security` |
| Export the inventory as an AI-BOM | A compliance team hands an auditor a CycloneDX AI-BOM | I, coverage sheet |
| Classify EU AI Act risk at discovery | A GRC team tiers each model as it is found | Live page, `/platform/ai-security`, AI-SPM module |

## Shadow AI Appears on Four Live Pages, Always as a Single Line

| Page | What it says today | The gap |
| --- | --- | --- |
| `/platform/ai-security` | One AI-SPM bullet, one tour tab titled "Shadow AI Discovery", and FAQs 26 and 27 | No section on the surfaces, the browser plugin, desktop telemetry or CLI agents |
| `/platform` | Nothing under the AI Security tab | No mention |
| Solutions menu, Use Cases | "Shadow AI Discovery" links to the help docs page | No solution page on accuknox.com |
| `/platform/dspm` | "Shadow IT and unmanaged data store identification" in the Discovery step | No link between shadow AI and sensitive data |

## Related

- `shadow-ai-discovery.md`, `ai-gateway.md`, the product notes behind these rows
- `references/source-of-truth/ai-security-data-points.md`, the fact file with source tiers
