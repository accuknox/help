# Parameter sets by category

The rows in a comparison matrix. Each set below was lifted from a live page on
accuknox.com on 2026-08-23, so it reflects what AccuKnox actually compares on
rather than what a model would invent.

Pick the set that matches the category, then cut or add rows to fit the
competitor. A row where both products do the same thing equally well is a row
that helps nobody, so drop it. Ten to fifteen rows is standard. Under six is not
a comparison.

## `ai-security`

Two live pages, and the Promptfoo one is the current shape. Source:
`comparisons/accuknox-vs-promptfoo` and `comparisons/accuknox-vs-quilr`.

| # | Parameter | What the row decides |
| --- | --- | --- |
| 1 | Shadow AI Discovery | Whether unregistered models and agents get found at all |
| 2 | AI Posture Management (AI-SPM) | Inventory of models, notebooks, pipelines, agents, per cloud |
| 3 | AI Model and Dataset Security | Static scans of Pickle, TensorFlow SavedModel, GGUF, DDUF, plus PII and PHI in datasets |
| 4 | AI Red Teaming and Pen Testing | Automated adversarial campaigns, and whether results feed policy |
| 5 | AI Guardrails (Prompt Firewall) | Inline enforcement at the request path, audit mode, failover |
| 6 | Safety Guardrails, session abuse | Multi-turn jailbreaks and session-level state |
| 7 | Safety Guardrails, unsafe content | Toxicity, bias, unsafe code generation |
| 8 | Agentic AI and MCP Security | Tool-call abuse, agent identity, MCP server posture |
| 9 | Agentic Harness Platform (AgentZ) | Runtime boundary for agents |
| 10 | AI Detection and Response (AI-DR) | CloudTrail and Event Hub correlation, automated response |
| 11 | AI Pipeline Security | Secrets and IaC scanning inside CI jobs, model-to-endpoint graph |
| 12 | Runtime Security | eBPF and LSM enforcement on process, file, network, capabilities |
| 13 | AI Gateway Integrations | Where the firewall can sit |
| 14 | SDK and Platform Integrations | How an application wires in |
| 15 | Compliance and Governance | OWASP LLM Top 10, ISO 27001, AVID, NIST AI RMF mapping |
| 16 | Deployment Flexibility | SaaS, on-prem, air-gapped, AWS AMI, EKS/AKS/GKE managed install |

## `appsec`

Source: `comparisons/accuknox-vs-opentext-fortify`. The longest live set at 25
rows, because AppSec genuinely has that many distinct capabilities.

| # | Parameter |
| --- | --- |
| 1 | Platform positioning |
| 2 | ASPM coverage and correlation |
| 3 | Deployment flexibility |
| 4 | SAST |
| 5 | SAST language and framework breadth |
| 6 | Developer and IDE experience |
| 7 | SCA and dependency security |
| 8 | Open source intake governance |
| 9 | DAST |
| 10 | Authenticated DAST and MFA |
| 11 | API security testing |
| 12 | IaC security |
| 13 | Secrets detection |
| 14 | Container image security |
| 15 | External scanner aggregation |
| 16 | Risk prioritization |
| 17 | False positive management |
| 18 | AI remediation and direct auto-fix |
| 19 | AI security assistant scope |
| 20 | CI/CD integration |
| 21 | Ticketing and workflow automation |
| 22 | SBOM generation and export |
| 23 | Third-party SBOM ingestion |
| 24 | SBOM lifecycle and version comparison |
| 25 | SBOM format support |

Cut to 12 to 15 for a competitor with a narrower product. Keep rows 1 to 3, the
scanner rows that apply, and the SBOM block, which is where AccuKnox separates.

## `kubernetes`

Source: `comparisons/accuknox-vs-red-hat-rhacs` and
`comparisons/accuknox-vs-suse-neuvector`. The live page groups rows under four
themes rather than listing them flat.

| Theme | Rows underneath |
| --- | --- |
| Runtime Security | eBPF and LSM enforcement, process and file and network policy, behaviour baselining, admission control, drift detection |
| Risk Assessment | KSPM benchmarks, CIS Kubernetes, image scanning, RBAC and identity (KIEM), attack path graph |
| Miscellaneous | Multi-cluster, air-gapped, managed distributions (EKS, AKS, GKE, OpenShift), open source lineage |
| AI Security in containers | Model workloads on Kubernetes, GPU node posture, agent runtime |

Use the four themes as H3 groups and put the individual rows in a table under
each. That is what the live page does and it scans far better than 20 flat rows.

## `cnapp`

Source: `comparisons/checkpoint-vs-prisma-cloud-vs-accuknox` and the other
twenty three-way pages. Seven broad rows, because a three-way matrix with
twenty rows is unreadable.

| # | Parameter | What the row decides |
| --- | --- | --- |
| 1 | Application security coverage | SAST, DAST, SCA, IaC, secrets, container, API |
| 2 | Observability and remediation | Findings correlation, attack paths, auto-fix, ticketing |
| 3 | Hardening and prevention | Inline runtime enforcement versus detect-and-alert |
| 4 | Deployment models | SaaS, on-prem, air-gapped, hybrid, sovereign |
| 5 | Open versus proprietary | KubeArmor and the CNCF lineage against a closed agent |
| 6 | Integrations | SIEM, ticketing, CI/CD, cloud-native services, registry |
| 7 | Future-proof security | AI security, agentic security, the roadmap the buyer is betting on |

Row 5 is the one AccuKnox wins outright and the one a buyer with an open-source
mandate reads first. Never drop it.

## `cloud-posture`

Drawn from the CNAPP set, narrowed to posture. Use when the competitor is a
CSPM-only tool.

Multi-cloud coverage. Compliance framework count. Custom policy authoring.
Agentless assessment. Drift detection. IAM and entitlement analysis (CIEM).
Attack path graph. Remediation automation. Reporting and evidence export.
Deployment model.

## `siem`

Use when the competitor is a logging or SIEM product and the page is about
displacement. Source: the Yoma Fleet story, which replaced Wazuh.

Log source breadth. Cloud-native ingestion (CloudTrail, VPC Flow Logs,
GuardDuty, Azure Event Hub). Correlation across security tools. Retention and
cost model. Detection content and tuning. Automated response workflows.
Compliance reporting. Deployment model. Migration path from the incumbent.

## `mixed`

A full-suite page against a full-suite competitor. Do not merge two sets. Take
the seven `cnapp` rows as the spine and add three to five rows from whichever
other category the competitor actually competes in.

A page that lists forty rows to look thorough reads as a spec sheet, and a buyer
stops at row eight.

## Writing one row

Every row is three cells: the parameter, the AccuKnox answer, the competitor
answer. On the live pages each cell is two to four sentences plus reference
links.

**The AccuKnox cell** states the mechanism, names the technology, and links the
help-docs page that proves it.

> Static scans of LLM and ML model files: Pickle, TensorFlow SavedModel, GGUF,
> DDUF. Runtime model execution visibility via KubeArmor (eBPF). References:
> [LLM Static Scans](https://help.accuknox.com/how-to/llm-static-scan/),
> [AI/ML Support Matrix](https://help.accuknox.com/support-matrix/aiml-support-matrix/)

**The competitor cell** states what they do, then what they do not, in that
order. Positive first is what keeps the page credible.

> Discovers models on endpoints only. No static scanning of model artifacts.

Two sentences. No adjectives. The second sentence is the gap, stated flatly,
with a link to their documentation showing the scope.

## Related

- `references/comparison-layout.md`, the archetype and section order
- `assets/comparison-template.md`, the file you copy
- `references/comparisons-builder/` in the repo root, the existing research
