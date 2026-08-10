# Platform Page, Full Copy

Paste-ready copy for the rebuilt AccuKnox platform page. Section numbers match `platform-page-update-plan.md`. Every image reference points at either a live accuknox.com asset or a file in this repo.

Conventions used below:
`[IMG]` a picture that already exists. `[NEW]` a diagram that has to be designed. `[CTA]` a button. `[LINK]` an inline link.

---

## Section 1. Hero

**Eyebrow:** The AccuKnox Platform

**H1:** One platform. Twelve modules. Zero Trust from kernel to prompt.

**Sub:** AccuKnox secures code, cloud, clusters, APIs, data, and AI on a single policy engine and a single console. Most platforms detect an attack and send you an alert. AccuKnox denies the syscall in the kernel before the action finishes.

**Stat strip (4 tiles):**

| Number | Label |
|---|---|
| 12 | Modules, one policy engine |
| 45+ | Compliance frameworks out of the box |
| 4 | Deployment models, SaaS to air-gapped |
| 50+ | Integrations live on day one |

[CTA primary] Book a technical deep dive
[CTA secondary] Take the product tour

---

## Section 2. Six domain tabs

Same component as the homepage hero tabs, same six labels, same icons. On the platform page each card carries the module page link rather than a generic solutions link.

**Section H2:** Pick where you hurt. The platform covers all six.

### Tab 1. AI Security
Eight modules that treat a model like any other production workload.

| Card | One line | Link |
|---|---|---|
| AI Security Posture (AI-SPM) | Live, agentless inventory of every model, dataset, pipeline, and agent | `/platform/ai-security` |
| Agentic AI Security | Sandboxes every agent with eBPF and LSM | `/solutions/agentic-ai-security` |
| AI Detect and Respond (AI-DR) | Reconstructs attack chains across prompts and tool calls | `/solutions/ai-dr` |
| AI Guardrails, Stateful Prompt Firewall | Blocks leaked keys, credentials, and injected prompts in both directions | `/solutions/prompt-firewall` |
| AI Red Teaming and Pen Testing | Scheduled jailbreak, injection, and extraction tests mapped to OWASP LLM Top 10 | `/solutions/ai-red-teaming` |
| AI Identity Security | Scopes permissions per agent, kills standing credentials | *needs a page* |
| AI Model and Dataset Security | Scans five model formats for backdoors and poisoned weights | *needs a page* |
| AI Compliance and Governance (AI-GRC) | Assigns an EU AI Act risk tier on discovery | *needs a page* |

### Tab 2. Agentic AI Harness (AgentZ)
Six controls for agents you build and agents you run.

Agent Builder, every egress recorded at the kernel. MCP Server Connections, authorize once and any MCP server works. Signed Runtime Traces, every model and tool call signed. Zero Trust Default Deny, every agent action denied until allowed. Zero Credential Exposure, agents never hold or store secrets. Scheduling and Skills, cron your agents and generate reusable skills.
All six link to `/platform/agentz`.

### Tab 3. Cloud Security
Cloud Security (CSPM), finds misconfigurations across AWS, Azure, GCP, and Oracle. Workload Protection (CWPP), blocks runtime attacks using eBPF. Cloud Detection and Response (CDR), turns cloud events into ranked incidents. Kubernetes Security (KSPM), hardens clusters and enforces admission policy. Kubernetes Identities (KIEM), maps every service account to its actual reach. Cloud Identity Management (CIEM), cuts standing permissions down to real usage.

### Tab 4. Application Security
App Sec (SAST, DAST, SCA, IAST), scans code, dependencies, running apps, and Terraform. Supply Chain (SBOM, CBOM, HBOM, QBOM, AI-BOM), scores every BOM against CERT-In and NTIA. Repo, Pipeline and Container Scanning, catches secrets, poisoned pipelines, and vulnerable images. API Security, finds shadow APIs and tests OWASP risks.

### Tab 5. Data Security
Data Discovery and Classification, finds and labels sensitive data agentlessly. Sensitive Data Risk Dashboard, ranks every data store by risk. Identity-Aware Exposure Graph, shows who can actually reach sensitive data. Explainable Risk Prioritization, says why a finding ranks critical. Lineage and Drift Monitoring, tracks who touched data and when. CNAPP x DSPM Correlated Risk, ranks data risk by cloud context.

### Tab 6. Infrastructure Security
SIEM, correlates cloud, cluster, and endpoint telemetry. Securing Secrets, finds exposed keys in repos and images and hardens the vault itself. AI SOC, triages alerts and drafts the investigation. Continuous Threat Exposure (CTEM), ranks exposures by real attacker reach.

---

## Section 3. Code to Cognition

**H2:** Code to Cognition, on one control plane

**Body:** A finding that starts as a line of Terraform should still be traceable when it becomes a running container, and again when that container serves a model. AccuKnox keeps one identity for that asset the whole way through. AppSec, CloudSec, and AISec share a policy engine, a data schema, and a console, which is why a runtime signal can deprioritize a CVE that a scanner marked critical.

`[NEW asset 1]` Code to Cognition architecture. Three vertical bands, AppSec / CloudSec CNAPP / AISec, sitting on three deployment columns, Public Cloud / Private Cloud / Edge and IoT. Four horizontal bars run across all three bands: SIEM for threat intelligence, Ask AI for the conversational interface, Compliance for 45+ standards, CTEM for exposure management.

**Three supporting statements:**

1. Every advanced attack is a runtime attack, so posture alone leaves you exposed to zero days.
2. Separate tools for AppSec, CloudSec, and AISec create the blind spots where breaches start.
3. Separate tools for on-prem and cloud double the cost of both tooling and headcount.

---

## Section 4. Twelve modules, by what they solve

**H2:** Twelve modules. Turn on what you need, add the rest without a new contract.

**Sub:** All public clouds, all private clouds. Customers commonly start with three and grow into the rest.

| # | Module | What it solves | Page |
|---|---|---|---|
| 1 | AI Security (AI-SPM) | Detects prompt injection and model drift, prevents LLM data leakage | `/platform/ai-security` |
| 2 | API Security | Discovers shadow APIs and enforces schema validation at the kernel level | `/platform/api-security` |
| 3 | Cloud Security (CSPM) | Automates misconfiguration detection and cloud hygiene | `/platform/cspm` |
| 4 | Workload Security (CWPP) | Blocks zero-day attacks and malware using eBPF inline prevention | `/platform/cwpp` |
| 5 | Kubernetes Security (KSPM) | Hardens clusters against CIS benchmarks and visualizes RBAC risk | `/platform/kubernetes-security` |
| 6 | Application Security (ASPM) | Correlates signals from code to cloud to rank the vulnerabilities that matter | `/platform/aspm` |
| 7 | Cloud Detection and Response (CDR) | Real-time detection of process anomalies and lateral movement | `/platform/cdr` |
| 8 | Secrets Manager | Automates rotation and replaces hardcoded keys in source code | `/solutions/secrets-management` |
| 9 | Events Management (SIEM) | Centralized logging with AI noise reduction to end alert fatigue | `/platform/siem` |
| 10 | Cloud Identity Security (CIEM) | Identifies over-privileged accounts and enforces least privilege | *Beta* |
| 11 | Supply Chain (SBOM) | Tracks third-party library risk and proves software integrity | `/solutions/sbom` |
| 12 | Threat Exposure (CTEM) | Ranks attack paths by asset criticality instead of raw CVSS | `/platform/ctem` |

**Callout inside this section:** Ask AI, the AccuKnox copilot, writes the fix, not the summary. Ask it about a failing control and it returns a Terraform snippet referencing the actual resource ARNs in your account.
`[IMG]` `utils/brian-demo-screenshots/10-ask-ai-copilot-remediation.png`

---

## Section 5. Platform showcase (the tabbed centerpiece)

**H2:** See every module in the product

**Sub:** Twelve tabs, real consoles, no mockups.

Component behaves exactly like the homepage showcase: icon tab bar across the top, one panel per module, headline plus support stat plus capability bullets plus a screenshot carousel plus an Explore button. Two additions on this page, a four-item capability list and a help-doc link under each Explore button.

---

### Tab 1. Cloud Security (CSPM)
**Headline:** Secure, monitor, and stay compliant across every cloud you run
**Support stat:** 5+ public clouds supported `[IMG] public-cloud-support-home.webp`

- Agentless asset inventory across 50+ AWS resource types, plus Azure, GCP, and Oracle
- 1,500+ built-in policies mapped to CIS, NIST, SOC 2, HIPAA, and PCI-DSS
- Toxic combination analysis chains isolated findings into a real attack path
- Drift detection correlates console changes against Terraform and CloudTrail

**Carousel:** `CSPM1` `CSPM2` `CSPM3` `CSPM4-dashboard-home.webp`
[CTA] Explore CSPM → `/platform/cspm`
[LINK] AWS onboarding guide → `https://help.accuknox.com/how-to/aws-onboarding/`

---

### Tab 2. Workload Security (CWPP)
**Headline:** Block the attack, do not write it up afterwards
**Support stat:** 10+ Kubernetes engines supported `[IMG] k8-engines-support-home.webp`

- eBPF plus LSM enforcement denies unauthorized fork, execve, file, and network calls in kernel space
- Auto policy discovery builds least-privilege policies from observed behavior, so nobody hand-writes YAML
- Hardening policies ship mapped to MITRE, CIS, NIST 800-53, and STIGs
- One agent covers Kubernetes, VMs, bare metal, and edge

**Carousel:** `CWPP1` `CWPP2` `CWPP3` `CWPP4-dashboard-home.webp`, plus `22-application-behavior-monitoring.png`
[CTA] Explore CWPP → `/platform/cwpp`
[LINK] Zero Trust use case → `https://help.accuknox.com/use-cases/zero-trust/`

---

### Tab 3. Kubernetes Security (KSPM)
**Headline:** Lock down clusters and prove it against CIS
**Support stat:** 10+ Kubernetes engines supported

- Cluster misconfiguration detection for privileged containers, writable hostPath, and missing resource limits
- CIS and STIG benchmark scans with per-control evidence
- KIEM maps every service account, role binding, and dangling identity to its actual reach
- Admission control with Pod Security Admission levels and a dry-run mode before enforcement

**Carousel:** `KSPM1` `KSPM2` `KSPM3` `KSPM4-dashboard-home.webp`
[CTA] Explore KSPM → `/platform/kubernetes-security`
[LINK] KIEM use case → `https://help.accuknox.com/use-cases/kiem/`

---

### Tab 4. Application Security (ASPM)
**Headline:** Write secure code and fix the findings that are actually reachable
**Support stat:** 9+ CI/CD platforms supported `[IMG] cicd-platform-support-home.webp`

- SAST, DAST, SCA, IAST, IaC, container, and secret scanning in one module
- Runtime context deprioritizes CVEs that are present on disk but never loaded in memory
- EPSS scoring plus a rules engine that opens the Jira ticket for you
- GitHub Actions, Jenkins, GitLab, Azure DevOps, Bamboo, and Harness

**Carousel:** `ASPM1` `ASPM2` `ASPM4-dashboard-home.webp`
[CTA] Explore ASPM → `/platform/aspm`
[LINK] ASPM overview → `https://help.accuknox.com/how-to/aspm-overview/`

---

### Tab 5. API Security
**Headline:** Find the APIs nobody owns, then enforce a schema on them
**Support stat:** 5+ integrations `[IMG] api-sec-logos-home.webp`

- Discovers shadow, zombie, and orphan APIs across north-south and east-west traffic
- Flags PII and PHI in headers and bodies, mapped to DORA, GDPR, HIPAA, and PCI-DSS
- Rate limiting, auth checks, and schema drift enforced at the kernel, not in application code
- Static and runtime API testing against the OWASP API Top 10

**Carousel:** `api1` `api2` `api3-dashboard-home.webp`
[CTA] Explore API Security → `/platform/api-security`

---

### Tab 6. AI Security (AI-SPM)
**Headline:** Keep models, datasets, and inferences safe from threats
**Support stat:** 10+ model and provider types `[IMG] ai-llm-logos-home.webp`

- Agentless inventory of models, datasets, pipelines, compute, agents, MCP servers, and shadow AI
- Stateful prompt firewall evaluates the conversation, not one prompt at a time
- Scheduled red teaming for jailbreaks, injection, extraction, code generation, and hallucination
- Model and dataset scanning across five formats, including pickle deserialization attacks

**Carousel:** `AI-SPM1` through `AI-SPM6-dashboard-home.webp`, plus `16-ai-pipeline-topology.png`, `17-ai-red-teaming-risks.png`, `18-prompt-firewall-policy-config.png`
[CTA] Explore AI Security → `/platform/ai-security`
[LINK] Prompt firewall docs → `https://help.accuknox.com/use-cases/prompt-firewall-overview/`

---

### Tab 7. Agentic AI Security (AgentZ)
**Headline:** An agent is a process. Sandbox it like one.
**Support stat:** MCP, tool calls, and autogenerated code covered

- Agent discovery and inventory across clouds, including agents nobody registered
- Prompt firewalling at the agent gateway, applied to both the request and the response
- Sandboxes unsafe tool use and untrusted autogenerated code with eBPF and LSM
- Signed runtime traces for every model and tool call, and zero standing credentials

**Carousel:** needs capture. Ship with the AgentZ architecture diagram until console shots exist.
[CTA] Explore AgentZ → `/platform/agentz`

---

### Tab 8. Data Security (DSPM)
**Headline:** Discover, classify, and protect sensitive data across every cloud
**Support stat:** multi-cloud data stores `[IMG] dspm-support-home.webp`

- Agentless discovery and classification of sensitive data at rest
- Identity-aware exposure graph answers who can actually reach a given store
- Explainable prioritization states why a finding ranks critical instead of showing a score
- Lineage and drift monitoring tracks who touched the data and when

**Carousel:** `DSPM1-dashboard-home.webp`, `Onboarding-Data-Source-Connection-dashboard-dspm.webp`, `Access-Review-dashboard-dspm.webp`, `Remediation-dashboard-dspm.webp`
[CTA] Explore DSPM → `/platform/dspm`

---

### Tab 9. Supply Chain (SBOM)
**Headline:** Catalogue every component, library, and dependency you ship
**Support stat:** 8 BOM standards `[IMG] sbom-support-home.webp`

- Generates SBOM, SaaSBOM, CBOM, HBOM, AIBOM, OBOM, MBOM, and QBOM in CycloneDX and SPDX
- Live generation from the pipeline, plus ingestion of BOMs a vendor hands you
- Dependency drift detection and license mapping at scale
- Audit-ready reporting for CERT-In, NTIA, and executive-order mandates

**Carousel:** `SBOM1` `SBOM2` `SBOM3` `SBOM4-dashboard-home.webp`
[CTA] Explore SBOM → `/solutions/sbom`

---

### Tab 10. Secrets Manager
**Headline:** Centralized credentials, and no secrets sprawl across clouds
**Support stat:** HashiCorp Vault compatible `[IMG] hashicorp-logo-home.webp`

- Shift-left scanning catches hardcoded credentials in repos, pipelines, images, S3, and ConfigMaps
- Dynamic secret generation with automatic rotation
- Runtime hardening of the secrets store itself, including Vault on-prem
- Multi-tenant isolation, air-gapped and hybrid deployment supported

**Carousel:** `secrets-manager-dashboard-home.webp`, `secrets-manager-1-dashboard-home.webp`
[CTA] Explore Secrets Management → `/solutions/secrets-management`

---

### Tab 11. Cloud Detection and Response (CDR)
**Headline:** Turn cloud events into ranked incidents, then fix them automatically
**Support stat:** sub-minute auto-remediation

- Exposed S3 bucket returned to private in under 60 seconds
- Public IP detached from a non-compliant EC2 instance within 90 seconds
- Geo-fencing alerts fire within 30 seconds of access from a denied region
- Rules engine works like IFTTT for findings, with auto-ticketing and auto-suppression

**Carousel:** needs capture. `12-rules-engine-custom-rules.png` and `01-main-dashboard-overview.png` work as interim shots.
[CTA] Explore CDR → `/platform/cdr`

---

### Tab 12. Compliance and GRC
**Headline:** 45+ frameworks out of the box, with the evidence attached
**Support stat:** 45+ frameworks `[IMG] integrated-compliance-frameworks-home.webp`

- SOC 2, HIPAA, PCI-DSS, NIST 800-53, ISO 27001, GDPR, FedRAMP, CIS, MITRE, STIGs
- CIS and STIG scans run on VMs and on Kubernetes clusters, not only cloud accounts
- Custom compliance maps internal policy into the same engine and scores it the same way
- Reports on demand or on a schedule, with separate views for executives, auditors, and engineers

**Carousel:** `COMPLIANCE1` `COMPLIANCE2` `COMPLIANCE3-dashboard-home.webp`, plus `13-compliance-frameworks-list.png`, `14-hipaa-compliance-detail-view.png`
[CTA] Explore Compliance → `/platform/compliance`

---

**Below the tab bar, a one-line row:** Also on the platform: SIEM, CIEM, CTEM, ASM, SSPM, AI-SOC, and AI-GRC.

---

## Section 6. Runtime as a lens vs runtime as a shield

**H2:** "Runtime security" means two different things. Ask which one you are buying.

**Body:** Almost every CNAPP vendor now claims runtime security, and almost all of them mean telemetry. eBPF enriches their posture data and ranks CVEs by what is loaded in memory. That is useful. It is also not prevention, because the alert fires after the action already ran.

`[NEW asset 2]` Two columns.

| Runtime as a lens (typical vendors) | Runtime as a shield (AccuKnox) |
|---|---|
| eBPF → telemetry → alert → manual response | eBPF + LSM → policy → deny or kill, automatically |
| Enriches posture data | Enforces policy in kernel space |
| Prioritizes CVEs by memory presence | Blocks unauthorized fork, execve, file, and network calls |
| Alert fires after execution | Syscall denied before it completes |

**Pull quote:** A blocked syscall leaves nothing to investigate. A detection tool alerts you after the file was already written.

**Closing line:** Test it during the POC. Run the exploit and watch which console shows an alert and which one shows a denial.

---

## Section 7. Runtime at every layer

**H2:** From kernel to prompt

**Sub:** Visibility, enforcement, and auto policy discovery applied at all four layers.

`[NEW asset 3]` Four stacked rows.

| Layer | Scope | Controls |
|---|---|---|
| L4 Application | Prompts, responses, HTTPS data discovery | LLM prompts, responses, HTTPS discovery |
| L3 API | Runtime API security and schema enforcement | Auth and authz, rate limits, schema drift |
| L2 Data | Access to sensitive data stores | Secrets, PII access, egress control |
| L1 Kernel and system | Files, processes, network | eBPF telemetry, LSM enforcement |

Three capability chips run beside the stack: **Visibility**, eBPF telemetry across processes, syscalls, and traffic. **Enforcement**, inline kernel-level deny through LSMs. **Auto Policy Discovery**, least-privilege policies generated from observed behavior.

---

## Section 8. Security maturity phases

**H2:** You do not deploy twelve modules on a Tuesday

**Sub:** Every track starts with agentless visibility, moves to enforcement, then to automation. Pick a track, pick a phase, and the platform grows with you.

Tabbed matrix. Five tracks across the top, three phase columns inside each.

### Track 1. Cloud Security (CSPM)

| Phase I | Phase II | Phase III |
|---|---|---|
| Detect misconfiguration and security risk across clouds. Detect compliance posture across 30+ regulations and frameworks. | Automate the findings lifecycle: auto-ticket critical issues, auto-alert, auto-suppress known false positives. Quick insights on the most common and most critical issues. CIEM. | Threat analytics on time-series cloud data. AI-assisted remediation. |

### Track 2. CI/CD and Application Security (ASPM)

| Phase I | Phase II | Phase III |
|---|---|---|
| Get started with 10+ CI/CD tools through a workflow file, a plugin, or native IaC integration. | Turn on the full scan set: SAST, DAST, IaC, container, and secrets. Work the insights through the ASPM dashboard and findings. | One unified view across pipeline security. Scans trigger on events. Focus shifts to prioritization and automation. |

### Track 3. Runtime Security, post deployment

| Phase I | Phase II | Phase III |
|---|---|---|
| Agentless VM and Kubernetes risk assessment. KSPM on CronJobs, KIEM identity misconfiguration, cluster misconfigurations, Kubernetes CIS benchmark, in-cluster image scan, rules engine for bulk automation, SOC 2 / STIG / CIS compliance. | Zero Trust least permissive posture with the eBPF and LSM agent, covering Kubernetes, Docker, VMs, and bare metal. Admission controller. Policy-driven continuous diagnostics against MITRE, NIST, CIS, and PCI file integrity. Cryptojacking defense and secrets manager hardening. | Adversarial attack simulation, agentless. MITRE Caldera against a Vault deployment, ransomware and secret-theft scenarios, cryptominer attack, tested consistently across vendors. |

### Track 4. AI Security

| Phase I | Phase II | Phase III |
|---|---|---|
| AI asset inventory. Agentless detection of LLMs, ML models, datasets, and compute across multi-cloud. | Pre-assessment of models before an AI application is built. Detect issues in models. Prompt security, code, hallucination, and sentiment analysis. Compute, dataset, and application issue overview. | Full LLM pipeline security across the AI application lifecycle in cloud or on-prem. Pipeline visibility into training iterations. PII checks on models and datasets. Static and dynamic prompt visibility. |

### Track 5. VM Security

| Phase I | Phase II | Phase III |
|---|---|---|
| VM vulnerability scanning: missing patches, known CVEs, misconfigurations, weak services and exposed ports, outdated packages, compliance gaps. | VM malware scanning: ransomware, trojans, spyware, cryptominers, persistence mechanisms, malicious binaries and scripts. | VM runtime hardening and behavior detection. Monitors behavior, detects attacks, blocks malicious actions, enforces zero trust policy. VM compliance against STIGs, CIS, and SOC 2. |

**Footer line for the section:** Easier, then faster, then better. Most customers reach Phase II on their first track inside a quarter.

---

## Section 9. The runtime security journey

**H2:** Eight steps from onboarding to block mode

`[NEW asset 5]` Horizontal stepper.

1. **Onboard cluster.** Connect your Kubernetes cluster to AccuKnox.
2. **Discover default posture.** Baseline every container in every namespace. Golden baseline on day one, day two onward catches cron jobs and periodic activity.
3. **Recommended hardening policies.** Cluster-wide, mapped to CIS, MITRE, NIST, and STIGs.
4. **Activate hardening policies.** Continuous diagnostics and mitigation on violations, still in audit.
5. **Keep learning behavior.** Review per-container changes and accept or discard each one. Audit mode runs two to three weeks.
6. **Behavior marked stable.** No significant change over a sustained period, so policies move to stable.
7. **Enforce in block mode.** Allow known and approved behavior. Deny everything else.
8. **True Zero Trust.** Unknown malware and unseen signatures are auto-denied, because only the least permissive behavior is allowed to run.

`[IMG]` `utils/brian-demo-screenshots/21-zero-trust-policy-discovery.png` beside step 5.

---

## Section 10. Deploy anywhere

**H2:** Four deployment models. One control plane. Identical policy.

`[NEW asset 6]`

| Model | What it means | Who picks it |
|---|---|---|
| AccuKnox SaaS | We host it. First findings the same day you onboard. | Fast-moving teams, first POCs |
| Your public or private cloud | You host the control plane in your own account. | Data residency requirements |
| On-premise | VMs or bare metal, native install rather than a modified SaaS agent. | Banking, healthcare, telecom |
| Fully air-gapped | No telemetry, no call-home, no outbound connection. | Federal, defense, GDPR, DPDP, ITAR |

**Line under the table:** Control plane sizing for on-prem is one VM at 16 vCPU, 64 GB RAM, and 512 GB disk. Full requirements are in the [LINK] deployment models doc → `https://help.accuknox.com/getting-started/deployment-models/`

**Specialized environments strip:** Nutanix, Red Hat OpenShift, VMware Tanzu, OpenStack, IBM Cloud, 5G networks, IoT and edge on ARM and x86.

---

## Section 11. Secure across every infrastructure

Reuse the homepage table verbatim. It is accurate and it already exists.

| Category | Coverage |
|---|---|
| All public clouds | AWS, Azure, GCP, Oracle |
| All private clouds | OpenStack, OpenShift, VMware, Nutanix |
| Modern assets | Kubernetes, API, Infrastructure as Code, AI and LLM, edge and IoT |
| Traditional assets | Virtual machines, bare metal |
| AI and LLM assets | Hugging Face, OpenAI, TensorFlow, Ollama, managed models, private models |

---

## Section 12. Compliance

**H2:** 45+ frameworks, and the evidence an auditor asks for

- SOC 2, HIPAA, PCI-DSS v4.0, NIST 800-53, ISO 27001, GDPR, FedRAMP, CIS, MITRE ATT&CK, STIGs, DORA, NSA Kubernetes Hardening
- Auto-conformance mapping to MITRE and NIST
- CIS, SOC 2, and STIG discovery on VMs and Kubernetes clusters, not only cloud accounts
- Custom compliance for internal policy and sector mandates
- AI-assisted remediation attached to each failing control

**Four metrics the module reports:** compliance posture score, time to remediation, risk exposure reduction, automated control failure rate.

[CTA] View all compliances → `/compliance`

---

## Section 13. Consolidation

**H2:** One platform replaces three to five tools

**Body:** The average enterprise we onboard runs more than 45 security tools. Each one is a renewal, an integration, and an alert queue. Because every AccuKnox module runs on the same engine rather than being a separate acquired product, consolidation cuts tooling spend by more than half.

`[NEW asset 7]` Grid of replaced categories against replaced vendors.

Replaced categories: AI-SPM and CNAPP, container and Kubernetes security, CIS compliance, CIEM, CWPP, cloud detection and response, data security, secret and malware scanning, vulnerability management, IaC and CI/CD scanning, shadow AI defense, AI identity controls.

**Stat row:** 12+ security domains. 3 to 5 tools replaced per deployment. 80% fewer alerts. Over 50% cost reduction.

**Analyst quote:** By 2026, 80% of enterprises will consolidate security tooling to three or fewer vendors. *Gartner, CNAPP Market Guide*

---

## Section 14. Stack ranking

**H2:** Where we win, and where we do not

**Sub:** The rows that decide most evaluations are kernel enforcement, on-prem coverage, and air-gapped support.

| Capability | AccuKnox | Sysdig | Palo Alto | CrowdStrike | Tigera | Wiz | Upwind |
|---|---|---|---|---|---|---|---|
| Private cloud and air-gapped deployment | Full | No | Partial | No | No | No | No |
| CNCF open source led | Full | Full | No | No | Full | No | No |
| Application Security (ASPM) | Full | Partial | Partial | Partial | No | Full | Partial |
| Vulnerability prioritization | Full | Full | Full | Full | No | Full | No |
| Cloud Security (CSPM) | Full | Full | Full | Full | No | Full | Partial |
| Workload Security (CWPP) | Full | Full | Partial | Partial | Partial | No | Full |
| Runtime inline enforcement | Full | No | No | No | No | No | Partial |
| AI Security | Full | No | Full | No | No | Partial | No |

*See the open questions in the plan file. The deck version is marked confidential, so decide whether the public page names vendors.*

---

## Section 15. Integrations

**H2:** 50+ integrations, live on day one

| Category | Tools |
|---|---|
| Ticketing | Jira, ServiceNow, Freshservice, ConnectWise |
| SIEM | Splunk, QRadar, Elastic, Azure Sentinel, Rsyslog |
| Logging | Telemetry logs, AWS CloudWatch, Elastic |
| Messaging | Slack, Microsoft Teams, PagerDuty, email |
| DevSecOps pipelines | GitHub, GitLab, Jenkins, Bamboo, Harness, Azure DevOps, Bitbucket |
| API connectors | Auth0 SSO (OIDC), Checkmarx, GitHub API |
| Automation | Webhooks and workflows |

Findings flow both ways, so a SIEM receives enriched context instead of another raw event feed.

[CTA] See all integrations → `/integrations`

---

## Section 16. Open source

**H2:** The runtime engine is open source, and you can read it

| Project | What it does | Link |
|---|---|---|
| KubeArmor | eBPF and LSM runtime enforcement. CNCF project. | `kubearmor.io` |
| ModelArmor | Secures AI models and sandboxes untrusted model execution | `/platform/modelarmor` |
| ClawArmor | Agentic endpoint security and malicious agent detection | `/platform/clawarmor` |
| K8TLS | TLS and certificate posture for Kubernetes | `github.com/kubearmor/k8tls` |

---

## Section 17. Proof

**H2:** Who backs this, and who runs it

**Company facts:** Founded 2020 with SRI International. 120+ people. 10+ US patents on Zero Trust security. $15M seed from SRI International and National Grid Partners. Five books published.

**Analyst and award recognition:** Three Gartner research mentions, including Emerging Tech Techscape 2025, Hardened Container Images 2026, and State of AI for I&O. An Omdia vendor profile on the AccuKnox CNAPP by Rik Turner, November 2025. Two Frost and Sullivan awards in 2026, Technology Innovation for global AI stack security and Transformational Innovation for APAC cloud security. Agentic AI Security Startup of the Year 2025.

**Partner validation:** AWS 2024 AI Partner Program. Red Hat verified and validated on RHEL. IBM and mimik Open Horizon project partner.

**Customer results:**

> The 45% reduction in engineering overhead alone justified our investment. Their platform eliminated the alert fatigue that was burning out our security team.
> **Tyler Pinckard**, Head of Security and DPO, SupportLogic

> We conducted an extensive evaluation of best-in-class vendors and selected AccuKnox based on their features, ease of deployment, third party integrations, and real-time security to prevent advanced zero-day attacks.
> **David Billeter**, Cybersecurity Leader, Sonesta International Hotels

> Choosing AccuKnox was driven by KubeArmor's novel use of eBPF and LSM technologies, delivering automatic, scalable, and highly effective runtime Zero Trust security.
> **Golan Ben-Oni**, CIO, IDT Telecom

> AccuKnox AI-Security 2.0 takes a principled approach: applying Zero Trust at the AI layer to provide runtime protection, visibility, and identity governance where the exposure actually exists.
> **Dr. Ed Amoroso**, former CISO, AT&T, and founder of TAG Cyber

**Lighthouse contracts:** $1.5M from NSF, SRI, and the US Army Under Secretary of Defense for 5G security research. $500,000 for Zero Trust satellite security.

---

## Section 18. Start, POC, FAQs

**H2:** From first call to enforcement in three weeks

| Week | What happens |
|---|---|
| Week 1 | Onboarding and discovery. One cluster or one cloud account and roughly two hours from your team. |
| Week 2 | Policy and findings. Hardening policies activate in audit mode, findings get triaged together. |
| Week 3 | Enforcement and readout against the success criteria agreed in writing before the POC started. |

Most CNAPP vendors need six to eight weeks for the same setup.

[CTA primary] Book a technical deep dive
[CTA secondary] Talk to a security expert

### Platform FAQs

1. What is the difference between KSPM and CWPP, and do I need both?
2. Does AccuKnox block attacks or only detect them?
3. Can AccuKnox run fully air-gapped, with no telemetry leaving my network?
4. Does it work on VMs and bare metal, or only Kubernetes?
5. Which AI security controls are in production today, and which are Beta?
6. How does AccuKnox reduce false positives on vulnerability findings?
7. Which compliance frameworks ship out of the box, and can I add my own?
8. What does agentless onboarding cover, and when do I need the agent?
9. How do findings reach my existing SIEM and ticketing system?
10. What does a POC need from my team?
