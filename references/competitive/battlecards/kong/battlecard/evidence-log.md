# AccuKnox vs Kong AI Gateway, Evidence Log

Kong pages were read with Firecrawl on 30 October 2026. The full prose comparison, with every
cell sourced, is `references/drafts/comparison/accuknox-vs-kong-ai-gateway-uidai-rfp.md`.

## Kong Claims Map to Kong's Own Pages

| Claim on the PDF | Kong source |
| --- | --- |
| On-prem is parity. Self-hosted Kong Gateway runs AI plugins, and the control plane can be self-hosted for air-gap | https://developer.konghq.com/ai-gateway/configure-on-prem/, https://konghq.com/blog/enterprise/building-the-kong-context-mesh-stack |
| The 2.x entity model needs Konnect | https://developer.konghq.com/ai-gateway/architecture/ |
| Shadow AI is limited to AI traffic seen by the gateway | https://konghq.com/blog/enterprise/shadow-ai-detection-enterprise-governance |
| Routes Claude Code, Codex and Gemini CLI | https://developer.konghq.com/ai-gateway/ai-clis/, https://developer.konghq.com/ai-gateway/use-gemini-cli-with-ai-gateway/ |
| Partner options are not scored: Lakera, NeMo, AWS, Azure, GCP, CrowdStrike, Noma Security | https://developer.konghq.com/ai-gateway/policies/, https://konghq.com/resources/videos/ai-runtime-protection |
| Full doc map checked: 2,964 URLs, no page on red teaming, eBPF, kernel, host inventory or posture | `firecrawl map https://developer.konghq.com`, 30 October 2026 |
| LLM, MCP and A2A traffic only | https://developer.konghq.com/ai-gateway/architecture/ |
| 19 AI policies, none for browser, host discovery, sandbox, BOM, model scan, posture or red teaming | https://developer.konghq.com/ai-gateway/policies/ |
| Regex allow and deny lists | https://developer.konghq.com/plugins/ai-prompt-guard/ |
| Similarity matching needs an AI license and a vector database | https://developer.konghq.com/plugins/ai-semantic-prompt-guard/ |
| Lakera Guard option uses the Lakera SaaS service | https://developer.konghq.com/plugins/ai-lakera-guard/ |
| PII categories include Aadhaar, separate PII container, no Hindi model listed | https://developer.konghq.com/plugins/ai-sanitizer/ |
| Proxies Claude Code, Codex CLI and Qwen Code CLI | https://developer.konghq.com/ai-gateway/ai-clis/ |
| MCP tool ACLs at the gateway | https://developer.konghq.com/plugins/ai-mcp-proxy/ |
| LLM as Judge scores accuracy from 1 to 100 | https://developer.konghq.com/plugins/ai-llm-as-judge/ |
| Advanced AI plugins carry "AI License Required" | https://developer.konghq.com/plugins/ai-proxy-advanced/ |

## AccuKnox Claims Map to Help Docs

| Claim on the PDF | Source | Tier |
| --- | --- | --- |
| Control plane on-prem, air-gapped, Helm on Kubernetes or 3 VMs, offline image updates | `docs/faqs/ai-security.md`, `docs/how-to/aiml-saas-vs-onprem.md` | D |
| One control plane, one AI inventory across all surfaces | `references/source-of-truth/shadow-ai-coverage.pdf` | I |
| ML injection detection, stateful multi-turn scoring, 14 policy types | `docs/use-cases/prompt-firewall-overview.md` | D |
| CLI traffic through the gateway proxy | `docs/integrations/ai-overview.md` | D |
| Browser plugin, Intune force-install, five browsers | `docs/integrations/chrome-browser-integration.md`, `docs/integrations/intune-browser-plugin-deployment.md`, `docs/getting-started/3.5-release.md` | D |
| 7 AI categories, Linux, Windows and macOS endpoints | `docs/use-cases/shadow-ai-discovery.md` | D |
| eBPF and LSM sandbox, no code change, air-gapped | `docs/use-cases/modelarmor.md`, `docs/agentz/index.md` | D |
| SBOM, CBOM, AIBOM in CycloneDX, model file checks | `docs/getting-started/xbom-setup.md`, `docs/getting-started/3.7-release.md`, `docs/how-to/ml-static-scan.md` | D |
| Red teaming probes, OWASP and MITRE mapping, schedules | `docs/use-cases/red-teaming.md` | D |
| AI posture frameworks and risk classification | `docs/how-to/aiml-saas-vs-onprem.md`, `docs/use-cases/aiml-usecases.md` | D |
| KubeArmor is a CNCF Sandbox project | `docs/getting-started/open-source.md` | D |

## RFP Numbers Come From the UIDAI Sheets

- 157 Must requirements and per-section counts: Summary & Statistics tab of the RFP sheet.
- 34 of 100 PoC marks: TE-21, TE-22, TE-23, TE-25, TE-26, TE-27, TE-29, TE-30, TE-31, TE-33 and TE-34 on the Technical Evaluation tab.
- Criterion 3 deduction of 3 marks per surface: Evaluation Criteria tab.
- Seven POC modules in 10 working days: UIDAI POC Project Plan and Timeline.
