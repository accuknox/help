# Pass 2: Independent Verification of the Stack Ranking

Read FRAMEWORK.md in this folder first. Pass 1 wrote vendors/<slug>.json. You re-check them with fresh eyes. You did not write them.

Accuracy works in both directions. A false `no` against a competitor is a legal risk. A false `yes` inflates a competitor and makes the ranking useless. Score what the vendor ships and documents today.

## Apply These Strict Sub-Feature Tests

| Sub | Counts as `yes` only when |
|---|---|
| 1.1 | The product discovers AI assets in cloud accounts (Bedrock, SageMaker, Azure OpenAI, Vertex, and similar) or on hosts and clusters. Network or browser usage discovery alone is `partial` for 1.1. |
| 1.2 | It detects unsanctioned AI use: SaaS AI apps, local models, unapproved agents, MCP servers. |
| 1.3 | It checks posture or misconfiguration of AI resources, pipelines or supply chain. |
| 2.1 | It names at least one integration with a managed agent platform (Copilot Studio, Agentforce, Bedrock AgentCore, Azure AI Foundry, ServiceNow, Vertex Agent Builder). |
| 2.2 | It discovers, scans or proxies MCP servers. |
| 2.3 | It enforces runtime policy on agent tool calls, sandboxes agents, or controls agent egress. |
| 3.1 | It detects attacks or anomalies on AI apps or agents at runtime or from logs. |
| 3.2 | It names a SIEM, SOAR or ITSM integration (Splunk, Sentinel, ServiceNow, Jira, etc.) or documents automated remediation. |
| 3.3 | It blocks at runtime, not only alerts. |
| 4.1 | It has an inline enforcement point: gateway, proxy, SDK, API or browser extension. |
| 4.2 | It blocks prompt injection, jailbreak, or PII leakage. |
| 4.3 | It filters unsafe output: toxicity, hallucination, off-topic, harmful code. |
| 5.1 | It produces an AIBOM or an equivalent exportable AI inventory record. |
| 5.2 | The product maps findings or controls to named frameworks (NIST AI RMF, ISO 42001, OWASP LLM Top 10, EU AI Act, MITRE ATLAS). A blog or whitepaper alone is `partial`. |
| 5.3 | It keeps audit trails, evidence or compliance reports. |
| 6.1 | It ships an automated adversarial attack library. |
| 6.2 | It runs multi-turn or agentic attacks against live AI apps or endpoints. |
| 6.3 | It runs red teaming continuously or in CI/CD. A service-only engagement is `partial`. |
| 7.1 | It gives agents or AI workloads a distinct identity. |
| 7.2 | It enforces least-privilege authorization per agent, tool or user. |
| 7.3 | It discovers and governs non-human identities: service accounts, API keys, tokens, OAuth grants. |
| 8.1 | It scans model files (pickle, safetensors, GGUF, ONNX) for malware or backdoors. |
| 8.2 | It scans training or RAG datasets for PII, sensitive data or poisoning. |
| 8.3 | It scans source code for AI or LLM risks, or offers AI-assisted SAST. |

These do not count as evidence for `yes`: SEO glossary pages, "what is X" academy articles, whitepapers, and a single vague homepage line. Beta, preview, early access and "coming soon" all score `partial`.

The module status follows mechanically from the subs: `yes` when 2 or more subs are `yes`. `partial` when at least one sub is `yes` or `partial`. `no` when all three subs are `no`.

## Check Each Vendor in Four Steps

1. Scrape the cited `url` for every module. Confirm the page exists and supports the claim. If the page is dead or does not support it, find a page that does, or downgrade.
2. Re-score all 24 subs with the strict tests above.
3. For every sub that is `partial` or `no`, run at least one targeted search to look for evidence pass 1 missed, e.g. `"<vendor>" splunk integration` or `"<vendor>" model scanning`. Upgrade when you find real evidence.
4. Rewrite `reason` when the status changes. Keep it at 18 words or fewer, plain and factual, with no em dashes and no semicolons.

Budget: about 8 to 14 Firecrawl calls per vendor. Use `python fc.py` from this folder. The helper now strips cookie banners.

## Write the Verified File Beside the Original

Write `vendors_v2/<slug>.json` in the same shape as pass 1. Add these two fields to each module:

    "verify": "confirmed|upgraded|downgraded|url-fixed",
    "verify_note": "One line on what you checked and what changed."

Do not edit `vendors/`. Reply with a table of every status change (vendor, module, old, new, why) and a count of confirmed modules.
