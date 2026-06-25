# AccuKnox AI Governance: Point of View

*Confidential — Internal Draft, June 2026*

**Core position:** You cannot govern what you cannot see, and you cannot trust what you haven't tested. AccuKnox AI governance spans four pillars: discover every asset, test every model, guard every prompt, surface every shadow.

---

## Pillar I: AI Asset Discovery

Agentless, continuous inventory across cloud and on-prem. Discovery begins within minutes of account onboarding. No agents installed on AI infrastructure.

| | Managed | Unmanaged | Datasets & Compute |
|---|---|---|---|
| **Cloud** | AWS Bedrock, SageMaker, Bedrock AgentCore; Azure AI Foundry, OpenAI, Copilot Studio; GCP Vertex AI, Gemini | Unapproved notebooks, EC2-hosted models, anything outside the MLOps pipeline | Training datasets, vector stores, GPU clusters, misconfigured S3/Blob buckets with model weights |
| **On-Prem** | Ollama, vLLM, NVIDIA Triton, Run.ai; K8s-deployed endpoints; on-prem MLOps pipelines | Undeclared inference containers, dev-workstation LLMs, unauthorized inference servers | NFS shares, local storage mounts, bare-metal GPU nodes, containerized training jobs |

**What the inventory produces:**
- **AIBOM** per model and agent: lineage, dependencies, provenance
- EU AI Act risk-tier classification (minimal / limited / high-risk)
- Ownership attribution, exposure scoring, and continuous drift detection

---

## Pillar II: Continuous Compliance via Red Teaming

Annual pen tests are obsolete for AI. AccuKnox runs **150+ adversarial probes** on every model update, cron-scheduled continuously.

| Category | What It Tests | Key Probes |
|---|---|---|
| **Prompt Injection** | Instruction override, jailbreaks, data exfil | Grandma Exploit, Do Not Answer (150+ prompts), encoding attacks (Base64/Hex/ASCII85), TAP multi-turn, XSS via markdown |
| **Sentiment Analysis** | Toxic, abusive, offensive outputs | RoBERTa + Google Perspective API; threats, insults, bullying, sexual content (50 prompts each) |
| **Code Safety** | Malware generation, AV evasion | 200+ malware probes (48 subfunctions, 88 payloads, 56 evasion); EICAR/GTUBE signatures |
| **Hallucination** | False assertions, fabricated packages | DistilBERT NLI; snowball errors; package hallucination across PyPI, npm, RubyGems, Crates |

Every finding auto-tagged to: **OWASP LLM Top 10 · MITRE ATLAS · NIST AI RMF · EU AI Act · ISO 42001 · AVID**

Custom JSON probe uploads for domain-specific scenarios (finance, healthcare, sector-specific risks).

---

## Pillar III: Prompt Firewall Guardrails

Multi-turn attacks succeed 78.5% of the time against per-prompt firewalls (vs. 4.3% single-turn). AccuKnox runs a **stateful, bidirectional firewall** with full conversation context, under 50ms p95 latency.

**Inspection pipeline (every request):**

| Stage | What Happens |
|---|---|
| **1. Normalize** | Decode Unicode, homoglyphs, character-injection obfuscation |
| **2. Classify** | Fast stateless screens: injection, jailbreak, PII, toxicity |
| **3. Contextualize** | Join session state: identity, history embeddings, tool-call ledger, prior scores |
| **4. Score** | Cumulative risk across full trajectory; detects semantic drift and slow-burn escalation |
| **5. Enforce** | Allow / Sanitize / Block / Step-up auth — encrypted, tenant-isolated audit trail |

**14 policy classes (applied to both input and output):**
Anonymize (PII/PHI) · Ban Code · Gibberish · Prompt Injection · Sentiment · Toxicity · Ban Competitors · Ban Topics · Code Language · Language · Regex · Secrets Detection · Token Limit · Relevance

**Integration points:**

| Hook | Platforms |
|---|---|
| API Gateway | AWS API GW, Azure APIM, GCP Apigee, LiteLLM, Bifrost |
| SDK | `accuknox-llm-defense` (Python): `scan_prompt()` / `scan_response()` |
| Browser | Chrome (ChatGPT, Claude), Firefox — intercepts before prompt leaves session |
| Platform | Power Apps, Copilot Studio, Bedrock AgentCore |

---

## Pillar IV: Shadow AI Risk Mitigation

Shadow AI costs an average of $670K extra per breach (IBM 2025). Three attack surfaces covered:

**Browser Plugin — Stealth Mode**
Silent Chrome/Firefox extension scans prompts against org policies before the LLM receives them. Blocks PII, credentials, and source code exfiltration at the source. No changes to the AI service. No user awareness needed.

**Managed AI Asset Scanning (VMs + K8s)**
- KubeArmor eBPF policies sandbox inference servers: no sub-shells, read-only model weights, restricted outbound
- ML artifact scans for supply chain risks: pickle deserialization, HDF5 injection, poisoned weights
- AI-DR ingests CloudTrail, Azure Logs, GCP Logs to flag misconfiguration drift, unauthorized fine-tune jobs, over-permissive IAM

**Unmanaged AI Asset Scanning (VMs + K8s)**
Same pipeline applied to undeclared assets discovered via Kubernetes admission signals and network telemetry. Auto-remediation removes public access on misconfiguration. Findings route to Jira, ServiceNow, Slack, or PagerDuty with full incident context.

---

## Full Coverage Matrix

| | Cloud Managed | Cloud Unmanaged | On-Prem Managed | On-Prem Unmanaged |
|---|:---:|:---:|:---:|:---:|
| Asset Inventory + AIBOM | Yes | Yes | Yes | Yes |
| Dataset / Compute Discovery | Yes | Yes | Yes | Yes |
| Red Teaming (150+ probes) | Yes | Yes | Yes | Yes |
| Prompt Firewall (stateful) | Yes | Yes | Yes | Yes |
| Browser Plugin Enforcement | Yes | Yes | Yes | Yes |
| Runtime Sandboxing (eBPF) | Yes | Yes | Yes | Yes |
| Compliance Evidence | Yes | Yes | Yes | Yes |

**Frameworks:** OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF, EU AI Act, ISO 42001, ISO 27001, SOC 2, PCI DSS, HIPAA, GDPR, HITRUST CSF, RBI CSF

---

*AccuKnox AI Governance — Internal Draft · Not for external distribution*
