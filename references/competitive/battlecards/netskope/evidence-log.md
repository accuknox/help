# Netskope Evidence Log for the AccuKnox Comparison

Firecrawl pulled 43 Netskope pages on 24 September 2026. The scrapes sit in `.firecrawl/netskope/`, which git ignores. This log records the fact each matrix row rests on, so a reviewer can check a cell without rerunning the crawl.

## Product Names and Scope

- Netskope sells the AI line as Netskope Skylight AI Security. Its product page lists AI Command Center, GenAI App Security, Agentic Broker, AI Gateway, AI Guardrails, Agent Action Control and AI Red Teaming. Source: <https://www.netskope.com/products/ai-products>
- The docs index names six modules: Access Control, AI Gateway, AI Red Teaming, AI Guardrails, Agent Action Control and Agentic Broker. Source: <https://docs.netskope.com/en/ai-security>
- The docs index says Netskope identifies 3,300+ Gen AI apps. The product page says inline inspection covers 1,800+ AI apps. The matrix uses the docs figure.

## Facts Behind Each Row

| Row | Netskope fact | Source |
| --- | --- | --- |
| A1 | AI Platforms posture covers 5 AWS, 4 Azure and 4 GCP platforms. Netskope marks it a preview feature. | <https://docs.netskope.com/en/ai-platforms-discovery-and-security-posture-management> |
| A2 | Client AI Discovery runs on Windows and macOS with Client 138 or later. It misses VM and container assets without the Client, and it detects only assets in the signature file. | <https://docs.netskope.com/en/netskope-client-ai-discovery> |
| A3 | Access control identifies 3,300+ Gen AI apps with activity and instance policies. | <https://docs.netskope.com/en/ai-security> |
| B1 | None of the six AI Security module pages describes a model artifact scan. AI Gateway 1.8 adds TSS Fast Scan for files in transit. | <https://docs.netskope.com/en/new-features-and-enhancements-in-ai-gateway-1-8> |
| B3 | Red team targets connect by REST API, LLM or OpenAI-compatible API. The default rate is 60 requests per minute. Model Drifting charts the 10 most recent rounds. | <https://docs.netskope.com/en/creating-a-target> |
| C1 | AI Guardrails lists 20 supported Gen AI apps. AI Gateway supports OpenAI-compatible, Gemini and Claude schemas, and other schemas get no content inspection. | <https://docs.netskope.com/en/ai-guardrails> |
| C2 | The guardrails profile has 10 predefined categories, 256 keywords and 10 semantic phrases. Custom topics go up to 30 and are Beta. The docs list 29 languages. | <https://docs.netskope.com/en/ai-security-guardrails-profile> |
| C3 | AI Gateway includes guardrails, and DLP is an add-on subscription. | <https://docs.netskope.com/en/ai-gateway-licensing-terms> |
| D1 | Agent Action Control covers 79 apps and 70 agents. The page says it is a Beta feature. | <https://docs.netskope.com/en/agent-action-control> |
| D2 | MCP Gateway allows up to 100 MCP providers per tenant on Streamable HTTP spec 2025-11-25. Agentic Broker needs its own license. | <https://docs.netskope.com/en/configuring-mcp-gateway> |
| D3 | AICC defines identities as IdP users plus unknown sources by IP address. | <https://docs.netskope.com/en/ai-command-center> |
| E1 | AISecOps agents triage DLP and insider-risk alerts, including Microsoft Purview alerts. | <https://docs.netskope.com/en/ai-security-ops-release-notes-version-august-2026> |
| E2 | Guardrails and red teaming map to OWASP Top 10 LLM and MITRE ATLAS. The Claude integration maps to GDPR, HIPAA and AICPA as a preview feature. | <https://docs.netskope.com/en/anthropic-claude-support-for-ai-discovery> |
| F1 | The AI Gateway appliance runs on AWS, GCP, Azure or VMware ESXi with 16 vCPU, 32 GB RAM and 200 GB disk. AI Guardrails runs in FedRAMP and PBMM tenants. | <https://docs.netskope.com/en/ai-gateway-overview> |
| F2 | AICC bills per AI asset over a rolling 90 days. AI Gateway bills per gateway plus monthly transactions and suspends past the limit. | <https://docs.netskope.com/en/ai-command-center-licensing-terms> |

## Two Facts Still Need a Human Answer

- [confirm the AccuKnox AI Security licensing unit and tiers with AccuKnox sales] Row F2 stays unscored until then.
- The help docs label AI GRC and AI Identity Security "Coming soon". The macro deck, slide 160, says "Beta / Coming Soon". The matrix marks both Beta on the product owner's instruction.
