# Evidence Log, AccuKnox vs DAXA AI Security for HPE

PDF: `references/drafts/comparison/accuknox-vs-daxa-ai-security-hpe-battlecard.pdf`.
Builder: `battlecard/build_battlecard.py`. Firecrawl read every DAXA and HPE page on 2026-10-13. The raw scrapes sit in `research/`.

## DAXA States It Is Already Inside HPE Private Cloud AI

Read this before the next HPE call. DAXA is an existing HPE partner, by its own statement.

| Fact | Source | Quote |
| --- | --- | --- |
| DAXA is built into two HPE offerings | https://www.daxa.ai/about | Today Daxa is built into HPE AI Factory and Private Cloud AI, and we work with NVIDIA on agent governance. |
| DAXA published an HPE demo on 2026-07-22 | https://www.daxa.ai/videos/hpe-ai-token-factory-demo | discover how Daxa Safe Infer extends HPE Private Cloud AI with intelligent model routing, built-in governance, token budgeting, and real-time observability. |
| DAXA joined NVIDIA Inception on 2026-05-14 | https://www.daxa.ai/news/daxa-joins-nvidia-inception | DAXA has joined the NVIDIA Inception program |
| DAXA has an AI Factory page | https://www.daxa.ai/ai-factory | A single platform built to secure AI factories, agentic workflows, and enterprise AI. |

## DAXA Cells Cite 7 Public Pages

DAXA has no public technical docs. `docs.daxa.ai` did not resolve on 2026-10-13. "Not shown" means the 15 scraped pages do not state the capability.

| Row | Status | Source | Quote |
| --- | --- | --- | --- |
| Prompt and response data | Parity | https://www.daxa.ai/pebblo | Safe Prompt. Removes sensitive data and prevents injection attacks. |
| SaaS AI on R&D endpoints | Limited | https://www.daxa.ai/shadow-ai | DAXA Safe Infer Gateway integrates with your existing SASE infrastructure. SSL Termination, L7 Proxy, TLS Inspection, Classification, Policy Enforcement |
| Shadow AI and external LLMs | Parity | https://www.daxa.ai/product | Continuously discover Gen AI components such as LLMs, frameworks, agents, datastores and endpoints in the entire cloud estate. |
| Shadow AI and external LLMs | Parity | https://www.daxa.ai/pebblo | Pebblo Safe Infer is your AI gateway for safely connecting chatbots and agents to multiple sanctioned LLMs. |
| Over-permissioned agents | Parity | https://www.daxa.ai/shadow-ai | Safe Agent. Permission checks, role and project context validation, and payload sanitization for MCP tools |
| Over-permissioned agents | Parity | https://www.daxa.ai/news/daxa-joins-nvidia-inception | requiring human confirmation for destructive or irreversible operations before they execute. |
| AI gateway | Leads | https://www.daxa.ai/pebblo | base_url="https://api.acmecorp.com/safe_infer/llm/v1" with the OpenAI client. Route to policy approved, authorized AI Model/Adapter for inference. |
| AI gateway | Leads | https://www.daxa.ai/videos/hpe-ai-token-factory-demo | intelligent model routing, built-in governance, token budgeting, and real-time observability |
| RAG retrieval permissions | Leads | https://www.daxa.ai/ai-factory | SafeConnectors pull fine-grained permissions from your enterprise systems, and SafeRetriever applies them before any data reaches the LLM. |
| Model scan before deploy | Not shown | https://www.daxa.ai/ai-factory | Secure Models. Protection against poisoning, unsafe context, and inference-level exploitation. No page describes a scan of model files. |
| AI red teaming | Not shown | https://www.daxa.ai/product | A search of all 15 scraped pages for "red team" returned no match. |
| AI-SPM | Parity | https://www.daxa.ai/product | Continuously discover LLMs, frameworks, datastores, and endpoints. Track linkages between them on a live risk graph. |
| AI detection and response | Not shown | https://www.daxa.ai/news/daxa-joins-nvidia-inception | Runtime Visibility. A complete audit trail of what agents accessed, which models were invoked, and what actions were taken |
| Air-gapped and on-prem | Limited | https://www.daxa.ai/about | Today Daxa is built into HPE AI Factory and Private Cloud AI. A search for "air-gap" and "on-prem" returned no match. |
| MSSP and multi-tenant | Not shown | https://www.daxa.ai/product | A search for "MSSP", "multi-tenant" and "white-label" returned no match. |
| Compliance and AI GRC | Parity | https://www.daxa.ai/product | Comply with current and emerging Gen AI regulations such as the EU AI Act. |
| Compliance and AI GRC | Parity | https://www.daxa.ai/shadow-ai | Unaudited AI interactions violate GDPR, PCI-DSS, HIPAA, and ISO 42001 requirements |
| API and MCP integration | Parity | https://www.daxa.ai/pebblo | Safe MCP. Secure, unified data access for MCP agents with identity and policy control. |
| AppSec for AI apps | Not shown | https://www.daxa.ai/product | No page describes SAST or DAST. |

## HPE Facts Come From Two HPE Pages

| Fact | Source |
| --- | --- |
| Private Cloud AI is co-developed with NVIDIA, for inferencing, RAG and fine-tuning | https://www.hpe.com/us/en/collaterals/collateral.a50009216enw.html |
| HPE documents a Private Cloud AI Air-Gapped solution | https://support.hpe.com/hpesc/public/docDisplay?docId=sd00007758en_us |

The four pain points and the MSSP interest come from the call notes of 2026-10-13. No HPE blueprint was read for this PDF.

## Every AccuKnox Cell Is Tier D

| Rows | Tier | Source |
| --- | --- | --- |
| Prompt Firewall, 14 policy types, stateful sessions | D | `docs/use-cases/prompt-firewall-overview.md` |
| Custom policies, AI Gateway, AI tool allow-list | D | `docs/getting-started/3.7-release.md` |
| Browser plugin, 5 AI apps, attachment types, Intune | D | `docs/integrations/chrome-browser-integration.md`, `docs/getting-started/3.6-release.md`, `docs/integrations/intune-browser-plugin-deployment.md` |
| Host and cluster scans, 7 categories, Unmanaged assets | D | `docs/use-cases/shadow-ai-discovery.md` |
| eBPF and LSM sandbox | D | `docs/use-cases/modelarmor.md` |
| AgentZ default-deny sandbox, no secrets | D | `docs/agentz/index.md` |
| Model formats, model sources, unsafe pickle check | D | `docs/how-to/ml-static-scan.md` |
| Red teaming collectors, probes, OWASP and ATLAS mapping | D | `docs/use-cases/red-teaming.md`, `docs/how-to/aiml-vllm-collector.md`, `docs/how-to/aiml-triton-collector.md` |
| AI-DR control-plane detection, tickets, auto-remediation | D | `docs/use-cases/aidr.md` |
| On-prem parity, air gap, 30 min to 4 h, Helm, frameworks | D | `docs/how-to/aiml-saas-vs-onprem.md` |
| MSSP tenant isolation, MSSP access, branding | D | `docs/faqs/partnerships.md` |
| MCP server, read-only, tenant-scoped, self-hostable | D | `docs/integrations/mcp-server.md` |
| AI SAST, DAST behind MFA | D | `docs/getting-started/3.4-release.md`, `docs/getting-started/3.6-release.md` |
| AI-BOM in CycloneDX | D | `docs/getting-started/xbom-setup.md` |

## Checks a Reviewer Should Run

- The call notes say the AccuKnox gateway is OpenAI-compatible and that the intent policy uses an LLM as judge. No help doc states either, so the PDF leaves both out. DAXA's page shows an OpenAI-compatible `base_url`, so the gateway row goes to DAXA.
- The call notes mention a white-label API. The docs say MSSPs can brand the service. The PDF says "Partner branding".
- The PDF names no MSSP reference customer. The call notes list them, and no doc in this repo does.
- The email thread says DAXA has fewer than 4 employees. No DAXA page states a headcount, and the careers section lists 4 open roles. The PDF does not mention company size.
- Tally: 7 AccuKnox leads, 6 parity, 2 DAXA leads (AI gateway and RAG retrieval permissions).
