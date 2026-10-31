---
slug: "ai-gateway-stock-exchange-poc"
title: "AI Security Gateway PoC at a Top 5 Global Stock Exchange"
description: "A top 5 global stock exchange tested an AI security gateway on premises with 92 test cases. See what worked across the API, browser, IDE and endpoint paths."
author: "Atharva Shah"
date: "2026-10-28"
category: "AI-SPM"
primary_keyword: "ai security gateway"
secondary_keywords: ["ai gateway proof of concept", "prompt firewall", "shadow ai discovery", "financial services ai security", "llm data leak prevention"]
---

# What a Top 5 Global Stock Exchange Learned From an AI Security Gateway PoC

## TL;DR

- A top 5 global stock exchange ran the AccuKnox AI security gateway on premises against a plan of 92 test cases in 13 suites.
- Prompt injection and jailbreaks were blocked, including attacks written in regional and mixed-language prompts.
- National ID numbers, bank details and API keys were stopped before the prompt left for the LLM provider.
- One policy engine governed 4 surfaces: applications, browsers, IDEs and endpoints.
- Alerts reached the exchange's SIEM, and every policy change carried an audit trail.

## An Exchange Has to Control the AI Use It Cannot See

Staff paste text into chat apps, and developers run coding agents in their IDEs. Scripts and containers also call model APIs, often with no human watching. Any of these paths can carry a customer record or an API key to a third-party model.

The exchange asked one question. Can a single control point sit in front of all those paths, run on premises, and stop sensitive data before a prompt leaves the building? The PoC tested the [AccuKnox AI Security platform](https://accuknox.com/platform/ai-security) against that question. The results say yes.

## The PoC Ran Monitor Mode First and Enforcement Second

The exchange wrote a plan of 92 test cases in 13 suites. They covered prompt attacks, data protection, agent security, shadow AI, policy, cost, performance, operations, and the browser, IDE and endpoint surfaces.

Phase one ran in monitor mode, which detects without blocking. Phase two ran in enforce mode, which blocks live. The team used default policies first, then tuned them. Every test got a recorded result with evidence.

## Prompt Attacks in Regional and Mixed Languages Were Blocked

Direct instruction overrides, jailbreak sets and system prompt extraction were blocked. So were injections hidden in Base64, hex, leetspeak and Unicode lookalike characters.

Attacks written in regional languages, or in a mix of English and a regional language, were caught. Injections spread across several turns, or hidden in retrieved documents, were detected too.

Benign security questions and code snippets stayed within the exchange's false-positive target.

![A prompt injection blocked in a chat app, beside the policy result showing the injection policy blocked it](images/ai-gateway-stock-exchange-poc/collage-prompt-attacks.png)

*The injection attempt never reaches the model, and the policy result shows which rule fired.*

## National IDs and Secrets Were Stopped Before the LLM

The data-protection suite sent synthetic national ID numbers, tax IDs, passport numbers, bank routing codes and payment IDs in varied formats. It also sent local phone number formats, card numbers, API keys, passwords, JWTs, private keys and connection strings. The [Prompt Firewall](https://accuknox.com/solutions/prompt-firewall) caught each class before the prompt reached the model.

The exchange also defined its own data class for an internal identifier without vendor help. Evasion tricks did not help an attacker. Data split across turns, padded with spaces, or spelled out in words was still caught. A model tricked into repeating sensitive context was blocked on the way out.

![Prompt Firewall blocking prompts with PII in Copilot, Gemini and GitHub Copilot, beside the DLP policy types](images/ai-gateway-stock-exchange-poc/collage-sensitive-data.png)

*Prompts with sensitive data are blocked in the chat app, driven by Anonymize and Secrets policies.*

## One Policy Engine Covered Four Surfaces

| Surface | Control point | What the PoC showed |
| --- | --- | --- |
| Applications | Gateway inline on the API path | One request format across providers, with rate limits, budget caps and cost attributed per team |
| Browser | Managed extension | Approved and unapproved AI sites found per user, and pastes and uploads inspected |
| IDE | Plugin deployed through device management | Coding assistants visible, secrets blocked, rollout and rollback through the exchange's own tooling |
| Endpoint | Runtime sensor | AI calls from CLIs, SDKs, scripts and containers tied to a process, user, provider and model |

![Unmanaged AI coding agents found on an endpoint, beside the AI agent inventory dashboard](images/ai-gateway-stock-exchange-poc/collage-dev-runtime.png)

*Coding agents on developer machines and cloud agents show up in one inventory.*

The [AI Gateway (BETA)](https://help.accuknox.com/getting-started/3.7-release/) sits between an application and the LLM, so it sees every prompt and response. The same user was recognised across browser, IDE and API.

## Shadow AI Use Became Visible per User

The browser extension found approved and unapproved AI sites for each user, along with the destination. Prompts, pastes and file uploads were inspected before they left the browser. Synthetic PII pasted into a public chat app was blocked.

The extension added under 3% browser overhead. When a tester tried to disable or remove it, the console raised an alert.

Developers got the same coverage. IDE assistants and coding agents showed up with their provider and model. Secrets typed into IDE prompts were blocked, and agent terminal actions were visible. The plugin was rolled out and rolled back through the exchange's device management.

Outside the browser and IDE, the runtime sensor tied each AI call to a process, user, provider and model. That covered CLIs, SDK clients, scripts, containers and agent runtimes, including calls made by child processes.

![Discovered AI assets grouped by category, beside the browser extension page blocking an unapproved AI site](images/ai-gateway-stock-exchange-poc/collage-shadow-ai.png)

*Discovered AI apps feed policy, and the extension blocks the sites the exchange disallows.*

## AI Spend Was Capped and Attributed per Team

The gateway reached every in-scope model provider through one request format. Streaming, tool calls, structured output, vision and embeddings all passed through it.

Rate limits held per key and per team. Hard budget caps stopped spend at the set amount. Cost was tagged by team and application, and the totals matched the provider invoice.

A security engineer built a new policy in the console in under 15 minutes. It combined a data class, a user group and an action.

![AI gateway applications with queries, violations and blocked counts, beside the audit trail log](images/ai-gateway-stock-exchange-poc/collage-cost-soc.png)

*Gateway traffic per application and a searchable audit trail sit in the same console.*

## Operations and Audit Evidence Passed Every Test

The operations suite passed all 6 of its tests. Alerts and logs reached the exchange's SIEM. An analyst found a blocked request by user and time. OpenTelemetry traces matched application logs, and RBAC separated read-only users from policy admins.

The team also tested a new policy in monitor mode before enforcing it, and every change was recorded with who, what and when. For audit, the exchange received controls mapped to the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and to its national data protection law.

## Put One Control Point in Front of Every AI Path

Start in monitor mode on all four surfaces. Read what staff and systems send to models, then enforce on the data classes you define.

Teams that run autonomous agents can read about [agentic AI security](https://accuknox.com/solutions/agentic-ai-security). Teams that keep inspection inside their own network can start with the [on-prem and air-gapped guide](https://accuknox.com/blog/ai-security-platform-for-on-prem-air-gapped).

## See the Prompt Firewall Setup and Demo

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/l_RCQosnNJk" title="AccuKnox Prompt Firewall Setup and Demo" frameborder="0" allowfullscreen></iframe>
```

Watch [the Prompt Firewall setup and demo on the AccuKnox YouTube channel](https://www.youtube.com/watch?v=l_RCQosnNJk).

## FAQs

### Did the PoC use real customer data?

No. Every test used synthetic and anonymised data, and evidence was recorded for each test case.

### Does the inspection run on premises?

Yes. The exchange hosted the deployment in its own environment. Sensitive data is stopped before a prompt leaves for an LLM provider.

### Which AI surfaces does one policy cover?

One policy covers four surfaces. The gateway covers applications on the API path, a managed extension covers browsers, an IDE plugin covers developers, and a runtime sensor covers scripts and containers.

<!--
Nothing goes below the FAQ. WordPress injects the table of contents, the share
row, the byline, the reading time, the "Ready For A Personalized Security
Assessment" CTA, the three testimonials and the "Continue Reading" block.
Writing any of those duplicates the template.
-->
