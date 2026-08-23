# Platform Page, Full Copy

Paste-ready copy for the rebuilt AccuKnox platform page. Section numbers match `platform-page-update-plan.md`. Every image reference is a live accuknox.com asset, verified to load.

Conventions: `[IMG]` an existing image, `[CTA]` a button, `[LINK]` an inline link. Image base path is `https://accuknox.com/wp-content/uploads/`.

**SEO targeting.** Primary keyword is *Zero Trust CNAPP platform*. Secondary keywords carried in H2s and H3s: cloud security posture management, cloud workload protection platform, Kubernetes security posture management, application security posture management, API security, AI security posture management, data security posture management, cloud detection and response, SBOM, continuous compliance, runtime security, eBPF. Every section heading leads with the term a buyer searches for rather than a rhetorical phrase.

---

## Section 1. Hero

**Eyebrow:** The AccuKnox Platform

**H1:** Zero Trust CNAPP Platform for Cloud, Application and AI Security

**Sub:** Cloud posture, workloads, Kubernetes, code, APIs, data and AI on one policy engine and one console. Enforcement runs inline at the kernel with eBPF and LSMs, so an unauthorized process, file access or network call is denied before it completes.

**Hero visual:** `[IMG] AccuKnox-Security-Modules.webp`

**Stat strip:**

| Number | Label |
|---|---|
| 12 | CNAPP modules, one policy engine |
| 45+ | Compliance frameworks out of the box |
| 4 | Deployment models, SaaS to air-gapped |
| 50+ | Security and DevOps integrations |

[CTA primary] Book a technical deep dive
[CTA secondary] See the platform

---

## Section 1b. Press band

Kept from the current page, moved directly under the hero. Label: **AccuKnox is the top CNAPP security pick.** Auto-scrolling logo marquee.

`[IMG]` `sjultra-press-slider.webp`, `nationalgrid-partners-press-slider.webp`, `cloud-security-list-press-slider.webp`, `the-new-stack-press-slider.webp`, `intellyx-press-slider.webp`, `medium-press-slider.webp`, `nutanix-press-slider.webp`, `aws-press-slider.webp`, `lf-edge-press-slider.webp`, `ai-techpark-press-slider.webp`, `redhat-press-slider.webp`

---

## Section 2. Six security domains

Same component as the homepage hero tabs, same six labels and icons. On the platform page each card links to the module page rather than a generic solutions page.

### Tab 1. AI Security

| Card | One line | Link |
|---|---|---|
| AI Security Posture (AI-SPM) | Live, agentless inventory of every model, dataset, pipeline and agent | `/platform/ai-security` |
| Agentic AI Security | Sandboxes every agent with eBPF and LSM | `/solutions/agentic-ai-security` |
| AI Detect and Respond (AI-DR) | Reconstructs attack chains across prompts and tool calls | `/solutions/ai-dr` |
| AI Guardrails, Stateful Prompt Firewall | Blocks leaked API keys, credentials and injected prompts | `/solutions/prompt-firewall` |
| AI Red Teaming and Pen Testing | Scheduled tests mapped to the OWASP LLM Top 10 | `/solutions/ai-red-teaming` |
| AI Identity Security | Scopes permissions per agent, removes standing credentials | *needs a page* |
| AI Model and Dataset Security | Scans five model formats for backdoors and poisoned weights | *needs a page* |
| AI Compliance and Governance (AI-GRC) | Assigns an EU AI Act risk tier on discovery | *needs a page* |

### Tab 2. Agentic AI Harness (AgentZ)

Agent Builder, every egress recorded at the kernel. MCP Server Connections, authorize once and any MCP server works. Signed Runtime Traces, every model and tool call cryptographically signed. Zero Trust Default Deny, every agent action denied until explicitly allowed. Zero Credential Exposure, agents never hold or store secrets. Scheduling and Skills, schedule agents and generate reusable skills. All six link to `/platform/agentz`.

### Tab 3. Cloud Security

Cloud Security (CSPM), finds misconfigurations across AWS, Azure, GCP and Oracle. Workload Protection (CWPP), blocks runtime attacks using eBPF and LSMs. Cloud Detection and Response (CDR), turns cloud events into ranked, auto-remediated incidents. Kubernetes Security (KSPM), hardens clusters and enforces admission policy. Kubernetes Identities (KIEM), maps every service account to its actual reach. Cloud Identity Management (CIEM), cuts standing permissions down to real usage.

### Tab 4. Application Security

Application Security (SAST, DAST, SCA, IAST), scans code, dependencies, running apps and Terraform. Supply Chain (SBOM, CBOM, HBOM, QBOM, AI-BOM), scores every bill of materials against CERT-In and NTIA. Repo, Pipeline and Container Scanning, catches secrets, poisoned pipelines and vulnerable images. API Security, finds shadow APIs and tests OWASP API risks.

### Tab 5. Data Security

Data Discovery and Classification, finds and labels sensitive data agentlessly. Sensitive Data Risk Dashboard, ranks every data store by risk. Identity-Aware Exposure Graph, shows who can actually reach sensitive data. Explainable Risk Prioritization, states why each finding ranks critical. Lineage and Drift Monitoring, tracks who touched data and when. CNAPP and DSPM Correlated Risk, ranks data risk by surrounding cloud context.

### Tab 6. Infrastructure Security

SIEM, correlates cloud, cluster and endpoint telemetry. Securing Secrets, finds exposed keys in repos and images and hardens the vault. AI SOC, triages alerts and drafts the investigation. Continuous Threat Exposure (CTEM), ranks exposures by real attacker reach.

---

## Section 3. Platform architecture

**H2:** Code to cloud to AI security on a single control plane

**Body:** A finding that starts as a line of Terraform stays traceable when it becomes a running container, and again when that container serves a model. One policy engine, one schema, one console, so a runtime signal can deprioritize a CVE a static scanner marked critical.

`[IMG] AccuKnox-Security-Modules.webp` with caption "AccuKnox Zero Trust CNAPP module map"

**Three problem cards:**

1. **Advanced attacks are runtime attacks.** Posture management alone leaves you exposed to zero days, because the exploit executes long before any scanner runs again.
2. **Split tooling creates the blind spots.** Separate products for application, cloud and AI security cannot correlate a code finding to a running workload.
3. **On-premise and cloud duplication.** Two stacks for one estate roughly doubles both tooling cost and the headcount needed to operate it.

---

## Section 4. Platform modules

**H2:** Twelve CNAPP modules on one policy engine

**Sub:** All public clouds, all private clouds. Enable what you need now and add the rest without a new contract. Most enterprises start with CSPM, CWPP and KSPM.

| # | Module | What it solves | Page |
|---|---|---|---|
| 01 | Cloud Security (CSPM) | Automates cloud misconfiguration detection and posture hygiene | `/platform/cspm` |
| 02 | Workload Security (CWPP) | Blocks zero-day attacks and malware with eBPF inline prevention | `/platform/cwpp` |
| 03 | Kubernetes Security (KSPM) | Hardens clusters against CIS benchmarks and visualizes RBAC risk | `/platform/kubernetes-security` |
| 04 | Application Security (ASPM) | Correlates code to cloud to rank vulnerabilities that are reachable | `/platform/aspm` |
| 05 | API Security | Discovers shadow APIs and enforces schema validation at the kernel | `/platform/api-security` |
| 06 | AI Security (AI-SPM) | Detects prompt injection and model drift, prevents LLM data leakage | `/platform/ai-security` |
| 07 | Cloud Detection and Response | Real-time detection of process anomalies and lateral movement | `/platform/cdr` |
| 08 | Secrets Manager | Automates rotation and replaces hardcoded keys in source code | `/solutions/secrets-management` |
| 09 | Events Management (SIEM) | Centralized logging with AI noise reduction to reduce alert fatigue | `/platform/siem` |
| 10 | Cloud Identity Security (CIEM) **Beta** | Identifies over-privileged accounts and enforces least privilege | *Beta* |
| 11 | Supply Chain (SBOM) | Tracks third-party library risk and proves software integrity | `/solutions/sbom` |
| 12 | Threat Exposure (CTEM) **Beta** | Ranks attack paths by asset criticality instead of raw CVSS | `/platform/ctem` |

**Copilot block.** H3: AI Copilot writes the fix, not the summary. Body: Ask AI about a failing control and it returns a remediation script referencing the actual resource ARNs in your account, rather than generic documentation. It works across cloud findings, compliance failures and vulnerability triage.
`[IMG] ask-ai-platfrom-card.webp`

---

## Section 5. Product showcase (the tabbed centerpiece)

**H2:** Every AccuKnox platform module, in the product

**Sub:** Thirteen modules, real console screenshots, no mockups.

Component: icon tab bar, one panel per module, kicker plus SEO headline plus support stat plus four capability bullets plus a screenshot stage with a thumbnail strip, plus an Explore button and a help-doc link.

---

### Tab 1. Cloud Security (CSPM)
**H3:** Cloud Security Posture Management for AWS, Azure, GCP and Oracle
**Support:** 5+ public clouds supported `[IMG] public-cloud-support-home.webp`

- Agentless asset inventory across 50+ AWS resource types, plus Azure, GCP and Oracle
- 1,500+ built-in policies mapped to CIS, NIST, SOC 2, HIPAA and PCI-DSS
- Toxic combination analysis chains isolated findings into an exploitable attack path
- Drift detection correlates console changes against Terraform and CloudTrail

**Screenshots (8):** `CSPM-Single-Pane-Cloud-Asset-View-platform.webp`, `CSPM-Cloud-Misconfiguration-platform.webp`, `CSPM-Asset-Vulnerabilities-platform.webp`, `CSPM-Drift-Detection-platform.webp`, `CSPM1-` through `CSPM4-dashboard-home.webp`
[CTA] Explore CSPM → `/platform/cspm` · [LINK] `https://help.accuknox.com/how-to/aws-onboarding/`

---

### Tab 2. Workload Security (CWPP)
**H3:** Cloud Workload Protection with eBPF runtime enforcement
**Support:** 10+ Kubernetes engines supported `[IMG] k8-engines-support-home.webp`

- eBPF and LSM enforcement denies unauthorized fork, execve, file and network calls in kernel space
- Auto policy discovery builds least-privilege policies from observed behavior
- Hardening policies ship mapped to MITRE, CIS, NIST 800-53 and STIGs
- One agent covers Kubernetes, VMs, bare metal and edge

**Screenshots (8):** `CWPP-MonitorAppBehaviour.webp`, `CWPP-HardenYourVMs.webp`, `CWPP-Host-Scan-Easily-platform.webp`, `CWPP-Secure-Your-Secrets-Vault-platform.webp`, `CWPP1-` through `CWPP4-dashboard-home.webp`
[CTA] Explore CWPP → `/platform/cwpp` · [LINK] `https://help.accuknox.com/use-cases/zero-trust/`

---

### Tab 3. Kubernetes Security (KSPM)
**H3:** Kubernetes Security Posture Management and CIS benchmark hardening
**Support:** 10+ Kubernetes engines supported

- Cluster misconfiguration detection for privileged containers, writable hostPath and missing resource limits
- CIS and STIG benchmark scans with per-control evidence
- KIEM maps every service account, role binding and dangling identity to its actual reach
- Admission control with Pod Security Admission levels and a dry-run mode

**Screenshots (8):** `KSPM-Scan-Cluster-Misconfigurations-platform.webp`, `KSPM-CIS-Benchmark-Findings-platform.webp`, `KSPM-Identity-Entitlements-Management-platform.webp`, `KSPM-Pod-Security-Admission-platform.webp`, `KSPM1-` through `KSPM4-dashboard-home.webp`
[CTA] Explore KSPM → `/platform/kubernetes-security` · [LINK] `https://help.accuknox.com/use-cases/kiem/`

---

### Tab 4. Application Security (ASPM)
**H3:** Application Security Posture Management across the CI/CD pipeline
**Support:** 9+ CI/CD platforms supported `[IMG] cicd-platform-support-home.webp`

- SAST, DAST, SCA, IAST, IaC, container and secret scanning in one module
- Runtime context deprioritizes CVEs present on disk but never loaded in memory
- EPSS scoring plus a rules engine that opens the Jira ticket automatically
- GitHub Actions, Jenkins, GitLab, Azure DevOps, Bamboo and Harness

**Screenshots (7):** `ASPM_StaticApplicationSecurity.webp`, `ASPM_ContainerScanning.webp`, `ASPM_IaC_Scanning.webp`, `ASPM_Vulnerability_Management.webp`, `ASPM1-`, `ASPM2-`, `ASPM4-dashboard-home.webp`
[CTA] Explore ASPM → `/platform/aspm` · [LINK] `https://help.accuknox.com/how-to/aspm-overview/`

---

### Tab 5. API Security
**H3:** API security: discovery, inventory and runtime protection
**Support:** 5+ integrations `[IMG] api-sec-logos-home.webp`

- Discovers shadow, zombie and orphan APIs across north-south and east-west traffic
- Flags PII and PHI in headers and bodies, mapped to DORA, GDPR, HIPAA and PCI-DSS
- Rate limiting, auth checks and schema drift enforced at the kernel, not in application code
- Static and runtime API testing against the OWASP API Top 10

**Screenshots (8):** `api-discovery.webp`, `sankey-diagram.webp`, `owasp-ui-1-api.webp`, `owasp-ui-2-api.webp`, `True-Behavioral-Analytics-dashboard.webp`, `Targeted-OWASP-Protection-dashboard.webp`, `api1-`, `api2-dashboard-home.webp`
[CTA] Explore API Security → `/platform/api-security`

---

### Tab 6. AI Security (AI-SPM)
**H3:** AI Security Posture Management for models, datasets and pipelines
**Support:** 10+ model and provider types `[IMG] ai-llm-logos-home.webp`

- Agentless inventory of models, datasets, pipelines, compute, agents, MCP servers and shadow AI
- Stateful prompt firewall evaluates the whole conversation, not one prompt at a time
- Scheduled red teaming for jailbreaks, injection, extraction, code generation and hallucination
- Model and dataset scanning across five formats, including pickle deserialization attacks

**Screenshots (8):** `Ai-sec-Inventory-View.webp`, `Ai-sec-AI-Model-View.webp`, `Ai-sec-Unmanaged-Assets-Discovery.webp`, `Ai-sec-Prompt-Firewall.webp`, `Ai-sec-Runtime-Defense.webp`, `Ai-sec-AI-Compliance.webp`, `AI-SPM1-`, `AI-SPM3-dashboard-home.webp`
[CTA] Explore AI Security → `/platform/ai-security` · [LINK] `https://help.accuknox.com/use-cases/prompt-firewall-overview/`

---

### Tab 7. Agentic AI Security
**H3:** Agentic AI security: agent discovery, gateway and runtime sandboxing
**Support:** MCP servers, tool calls and generated code

- Agent discovery and inventory across clouds, including agents nobody registered
- Prompt firewalling at the agent gateway, applied to both request and response
- Sandboxes unsafe tool use and untrusted auto-generated code with eBPF and LSM
- Signed runtime traces for every model and tool call, with zero standing credentials

**Screenshots (7):** `Multi-Cloud-Agent-Visibility-Auditing-agentic.webp`, `Sandbox-Unsafe-Tool-Usage-agentic.webp`, `Sandbox-Auto-Generated-Code-agentic.webp`, `Multi-Platform-Support-agentic.webp`, `Ai-sec-Managed-Agents-View.webp`, `Ai-sec-Runtime-Agent-Sandboxing.webp`, `agentz-tab-home-1.webp`
[CTA] Explore AgentZ → `/platform/agentz`

---

### Tab 8. Data Security (DSPM)
**H3:** Data Security Posture Management for multi-cloud data stores
**Support:** Cloud storage, databases and VMs `[IMG] dspm-support-home.webp`

- Agentless discovery and classification of sensitive data at rest
- Identity-aware exposure graph answers who can actually reach a given data store
- Explainable prioritization states why a finding ranks critical instead of showing only a score
- Lineage and drift monitoring tracks who touched the data and when

**Screenshots (7):** `Discovery-dashboard-dspm.webp`, `Classification-dashboard-dspm.webp`, `Access-Review-dashboard-dspm.webp`, `Monitoring-dashboard-dspm.webp`, `Remediation-dashboard-dspm.webp`, `Onboarding-Data-Source-Connection-dashboard-dspm.webp`, `DSPM1-dashboard-home.webp`
[CTA] Explore DSPM → `/platform/dspm`

---

### Tab 9. Supply Chain (SBOM)
**H3:** Software supply chain security and SBOM generation
**Support:** 8 bill-of-materials standards `[IMG] sbom-support-home.webp`

- Generates SBOM, SaaSBOM, CBOM, HBOM, AIBOM, OBOM, MBOM and QBOM in CycloneDX and SPDX
- Live generation from the pipeline, plus ingestion of bills of materials a vendor supplies
- Dependency drift detection and license mapping at scale
- Audit-ready reporting for CERT-In, NTIA and executive-order mandates

**Screenshots (4):** `SBOM1-` through `SBOM4-dashboard-home.webp`
[CTA] Explore SBOM → `/solutions/sbom`

---

### Tab 10. Secrets Manager
**H3:** Secrets management and secrets scanning across multi-cloud
**Support:** HashiCorp Vault compatible `[IMG] hashicorp-logo-home.webp`

- Shift-left scanning catches hardcoded credentials in repos, pipelines, images, S3 and ConfigMaps
- Dynamic secret generation with automatic rotation
- Runtime hardening of the secrets store itself, including Vault on-premise
- Multi-tenant isolation, with air-gapped and hybrid deployment supported

**Screenshots (3):** `secrets-manager-dashboard-home.webp`, `secrets-manager-1-dashboard-home.webp`, `CWPP-Secure-Your-Secrets-Vault-platform.webp`
[CTA] Explore Secrets Management → `/solutions/secrets-management` · [LINK] `https://help.accuknox.com/use-cases/hashicorp/`

---

### Tab 11. Cloud Detection and Response (CDR)
**H3:** Cloud Detection and Response with automated remediation
**Support:** AWS, Azure, GCP and Oracle

- Exposed S3 bucket returned to private in under 60 seconds
- Public IP detached from a non-compliant EC2 instance within 90 seconds
- Geo-fencing alerts fire within 30 seconds of access from a denied region
- Rules engine automates ticketing, alerting and false-positive suppression

**Screenshots (5):** `cdr-solution-dashboard.webp`, `Enforcing-private-access-policy-on-S3-buckets.webp`, `Ensure-public-IP-is-not-enabled-for-VMs.webp`, `Notify-if-AWS-access-from-unknown-regions.webp`, `AccuKnox-cdr-Architecture.webp`
[CTA] Explore CDR → `/platform/cdr` · [LINK] `https://help.accuknox.com/use-cases/cdr/`

---

### Tab 12. SIEM
**H3:** Cloud-native SIEM with AI-driven threat detection
**Support:** Splunk, Sentinel, Elastic and Rsyslog

- Centralized log management across cloud, cluster and endpoint telemetry
- AI noise reduction and high-fidelity alerting to cut alert fatigue
- Pre-built compliance reporting with versatile ingest pipelines
- Single pane of glass for every CNAPP event, with two-way SIEM and SOAR integration

**Screenshots (8):** `Main-Security-Overview-Dashboard.webp`, `Alert-Investigation-Correlation-Details.webp`, `Log-Search-Threat-Hunting-Interface.webp`, `Incident-Threat-Timeline-Visualization.webp`, `Compliance-Reporting-Dashboard-e.g.-PCI.webp`, `Integration-Data-Source-Management.webp`, `siem-architecture.webp`, `noise-reduction.webp`
[CTA] Explore SIEM → `/platform/siem`

---

### Tab 13. Compliance and GRC
**H3:** Continuous compliance and GRC across 45+ frameworks
**Support:** 45+ frameworks out of the box `[IMG] integrated-compliance-frameworks-home.webp`

- SOC 2, HIPAA, PCI-DSS v4.0, NIST 800-53, ISO 27001, GDPR, FedRAMP, CIS, MITRE and STIGs
- CIS and STIG scans run on VMs and Kubernetes clusters, not only cloud accounts
- Custom compliance maps internal policy into the same engine and scores it identically
- Scheduled and on-demand reports for executives, auditors and engineers

**Screenshots (5):** `COMPLIANCE1-` through `COMPLIANCE3-dashboard-home.webp`, `Achieve-Key-Compliance-dashboard.webp`, `Ai-sec-AI-Compliance.webp`
[CTA] Explore Compliance → `/platform/compliance` · [LINK] `https://help.accuknox.com/use-cases/compliance/`

---

**Row below the tab bar:** Also on the platform: CIEM, CTEM, Attack Surface Management, SaaS Security Posture Management, AI-SOC and AI-GRC.

---

## Section 6. Runtime security differentiator

**H2:** Runtime security: threat detection versus inline prevention

**Body:** Most CNAPP vendors claim runtime security and mean telemetry. eBPF enriches their posture data and ranks CVEs by memory presence. Useful, but not prevention, because the alert fires after the action ran.

| Runtime as a lens (typical CNAPP vendors) | Runtime as a shield (AccuKnox) |
|---|---|
| eBPF → telemetry → alert → manual response | eBPF + LSM → policy → deny or kill, automatically |
| eBPF telemetry enriches cloud posture data | eBPF and Linux Security Modules enforce policy in kernel space |
| Prioritizes CVEs by what is loaded in memory | Blocks unauthorized fork, execve, file and network calls |
| Alerts fire after the action executes | Denies the syscall before it completes |
| An analyst decides what happens next | No analyst in the loop for a known-bad action |

**Pull quote:** A blocked syscall leaves nothing to investigate. A detection tool alerts you after the file was already written.

**Closing line:** Validate it during the proof of concept. Run the exploit, then compare which console shows an alert and which shows a denial.

---

## Section 7. Runtime coverage

**H2:** Runtime security at every layer, from kernel to prompt

**Sub:** Visibility, inline enforcement and automated policy discovery applied across the kernel, data, API and application layers.

| Layer | Scope | Controls |
|---|---|---|
| L4 Application | Prompts, responses and HTTPS data discovery | LLM prompts, responses, HTTPS discovery |
| L3 API | Runtime API security and schema enforcement | Auth and authz, rate limits, schema drift |
| L2 Data | Access to sensitive data stores | Secrets, PII access, egress control |
| L1 Kernel and system | Files, processes and network | eBPF telemetry, LSM enforcement |

**Three capability cards:** Visibility, eBPF telemetry across processes, syscalls and traffic. Enforcement, inline kernel-level deny through LSMs. Auto policy discovery, least-privilege policies from observed behavior.

`[IMG] Ai-sec-Runtime-Defense.webp`

---

## Section 8. Adoption roadmap

**H2:** CNAPP adoption roadmap and security maturity phases

**Sub:** Each track starts with agentless visibility, moves to inline enforcement, then to automation.

Tabbed matrix, five tracks, three phase columns per track.

### Track 1. Cloud Security

| Phase I, Visibility | Phase II, Automation | Phase III, Analytics |
|---|---|---|
| Detect misconfiguration and security risk across clouds. Detect compliance posture across 30+ regulations and frameworks. | Automate the findings lifecycle. Auto-ticket critical issues, auto-alert, and auto-suppress known false positives. Quick insights on the most common and most critical issues. CIEM. | Threat analytics on time-series cloud data. AI-assisted remediation. |

### Track 2. CI/CD and Application Security

| Phase I, Connect | Phase II, Scan | Phase III, Prioritize |
|---|---|---|
| Integrate with 10+ CI/CD tools through a workflow file, a plugin, or native IaC integration. | Enable the full scan set. SAST, DAST, IaC, container and secrets scanning. Work the insights through the ASPM dashboard and findings. | One unified view across pipeline security. Scans trigger on events. Focus shifts to prioritization and automation. |

### Track 3. Runtime Security

| Phase I, Assess (agentless) | Phase II, Enforce (agent) | Phase III, Simulate |
|---|---|---|
| VM and Kubernetes risk assessment. KSPM on CronJobs, KIEM identity misconfiguration, cluster misconfigurations, Kubernetes CIS benchmark, in-cluster image scan, rules engine for bulk automation, and SOC 2, STIG and CIS compliance. | Zero Trust least permissive posture with the eBPF and LSM agent across Kubernetes, Docker, VMs and bare metal. Admission controller. Policy-driven continuous diagnostics against MITRE, NIST, CIS and PCI file integrity. Cryptojacking defense and secrets manager hardening. | Agentless adversarial attack simulation. MITRE Caldera against a Vault deployment, ransomware and secret-theft scenarios, and a cryptominer attack, tested consistently across vendors. |

### Track 4. AI Security

| Phase I, Inventory | Phase II, Assess | Phase III, Pipeline security |
|---|---|---|
| AI asset inventory. Agentless detection of LLMs, ML models, datasets and compute across multi-cloud. | Pre-assessment of models before an AI application is built. Detect issues in models. Prompt security, code, hallucination and sentiment analysis, plus compute, dataset and application issue overviews. | LLM pipeline security across the AI application lifecycle in cloud or on-premise. Pipeline visibility into training iterations. PII checks on models and datasets. Static and dynamic prompt visibility. |

### Track 5. VM Security

| Phase I, Vulnerabilities | Phase II, Malware | Phase III, Runtime |
|---|---|---|
| Missing patches, known CVEs, misconfigurations, weak services and exposed ports, outdated packages and compliance gaps. | Ransomware, trojans, spyware, cryptominers, persistence mechanisms, and malicious binaries or scripts. | VM runtime hardening and behavior detection. Monitors behavior, detects attacks, blocks malicious actions and enforces zero trust policy. VM compliance against STIGs, CIS and SOC 2. |

---

## Section 9. Zero Trust rollout

**H2:** Zero Trust runtime security journey in eight steps

**Sub:** Cluster onboarding to kernel-level block mode, with an audit period so enforcement never breaks a running workload.

1. **Onboard cluster.** Connect your Kubernetes cluster to the AccuKnox control plane.
2. **Discover default posture.** Baseline every container in every namespace. Golden baseline on day one, day two onward captures cron jobs.
3. **Recommended hardening policies.** Cluster-wide policies mapped to CIS, MITRE, NIST and STIGs.
4. **Activate hardening policies.** Continuous diagnostics and mitigation on violations, still in audit mode.
5. **Keep learning behavior.** Review per-container changes and accept or discard each one. Audit runs two to three weeks.
6. **Behavior marked stable.** No significant change over a sustained period, so policies move to stable.
7. **Enforce in block mode.** Allow known and approved behavior. Deny everything else.
8. **Zero Trust enforced.** Unknown malware and unseen signatures are auto-denied, because only least permissive behavior runs.

`[IMG] CWPP-MonitorAppBehaviour.webp` caption "Application behavior monitoring feeds auto policy discovery"
`[IMG] CWPP-Secure-Your-Secrets-Vault-platform.webp` caption "Runtime policy hardening a HashiCorp Vault deployment"

---

## Section 10. Deployment models

**H2:** Flexible deployment models: SaaS, private cloud, on-premise and air-gapped

**Sub:** One control plane, four models, identical policy enforcement. A mixed estate still reports into a single console.

**Primary visual:** `[IMG] deployment-models-differentiators.webp` caption "AccuKnox deployment models and differentiators"

| Deployment model | What it means | Typical buyer |
|---|---|---|
| AccuKnox SaaS | AccuKnox hosts the control plane. First findings the same day you onboard. | Fast-moving teams, first proof of concept |
| Customer-hosted cloud | You host the control plane inside your own public or private cloud account. | Data residency requirements |
| On-premise | VMs or bare metal. A native install, not a modified SaaS agent. | Banking, healthcare, telecom |
| Fully air-gapped | No telemetry, no call-home and no outbound connection. | Federal, defense, GDPR, DPDP, ITAR |

**Line under the table:** On-premise control plane sizing is one VM at 16 vCPU, 64 GB RAM and 512 GB disk. Full requirements are in the [LINK] deployment models documentation → `https://help.accuknox.com/getting-started/deployment-models/`

---

## Section 11. Infrastructure coverage

**H3:** Multi-cloud and hybrid infrastructure coverage

| Category | Coverage |
|---|---|
| Public clouds | AWS, Azure, GCP, Oracle |
| Private clouds | OpenStack, OpenShift, VMware, Nutanix |
| Modern assets | Kubernetes, API, Infrastructure as Code, AI and LLM, edge and IoT |
| Traditional assets | Virtual machines, bare metal |
| AI and LLM assets | Hugging Face, OpenAI, TensorFlow, Ollama, managed and private models |

`[IMG] saas-onprem.webp`

---

## Section 12. Compliance

**H2:** Continuous compliance across 45+ frameworks

**Sub:** SOC 2, HIPAA, PCI-DSS v4.0, NIST 800-53, ISO 27001, GDPR, FedRAMP, CIS, MITRE ATT&CK, STIGs and DORA, with per-control evidence on every finding.

- CIS, SOC 2 and STIG scans run on VMs and Kubernetes clusters, not only cloud accounts
- Custom compliance maps internal policy into the same engine and scores it identically
- Scheduled and on-demand reports with separate executive, auditor and engineer views
- AI-assisted remediation attached to each failing control

**Four reported metrics:** compliance posture score, time to remediation, risk exposure reduction, automated control failure rate.

`[IMG] COMPLIANCE1-dashboard-home.webp`
[CTA] View all compliances → `/compliance`

---

## Section 13. Consolidation and TCO

**H2:** Security tool consolidation and TCO reduction

**Body:** The average enterprise we onboard runs more than 45 security tools, each one a renewal, an integration and a separate alert queue. Every AccuKnox module runs on the same engine, so consolidation cuts tooling spend by more than half.

**Stat row:** 12+ security domains. 3 to 5 tools replaced per deployment. 80% fewer alerts. Over 50% cost reduction.

**Replaced vendor chips:** Aqua, Snyk, Bridgecrew, Orca, Qualys, Lacework, SentinelOne, Cyera, Laminar, Prisma Cloud, Checkmarx, Veracode.

**Analyst quote:** By 2026, 80% of enterprises will consolidate security tooling to three or fewer vendors. *Gartner, CNAPP Market Guide*

---

## Section 14. Vendor comparison

**H2:** CNAPP vendor comparison

**Sub:** The rows that decide most CNAPP evaluations are kernel-level enforcement, private cloud coverage and air-gapped support.

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

*Decision needed: the deck version is marked confidential. Confirm whether the public page names vendors.*

---

## Section 15. Integrations

**H2:** 50+ security and DevOps integrations

**Sub:** Findings flow both ways, so your SIEM gets enriched context instead of another raw event feed.

**Layout:** two columns. Six compact category cards on the left, the integration logo wheel on the right.

**Primary visual:** `[IMG] logo-wheel.webp` (1000 x 1000, verified)

| Category | Tools |
|---|---|
| Ticketing and ITSM | Jira, ServiceNow, Freshservice, ConnectWise |
| SIEM and SOAR | Splunk, QRadar, Elastic, Azure Sentinel, Rsyslog |
| DevSecOps pipelines | GitHub, GitLab, Jenkins, Bamboo, Harness, Azure DevOps |
| Messaging and alerting | Slack, Microsoft Teams, PagerDuty, email |
| Logging | Telemetry logs, AWS CloudWatch, Elastic |
| API connectors | Auth0 SSO (OIDC), Checkmarx, GitHub API, webhooks |

[CTA] See all integrations → `/integrations`

---

## Section 16. Gated asset

Layout kept from the current page. `[IMG] cnapp-buyers-guide-400x250.webp`

**H3:** Zero Trust CNAPP, a definitive guide
**What is inside this guide:** eBPF runtime blocking under 1% CPU overhead. CNAPP coverage across the AI stack. How low-severity gaps chain into breaches. One Zero Trust policy across hybrid and multi-cloud.
[CTA] Grab a free copy

---

## Section 17. Proof

**H2:** Analyst recognition, patents and customer results

**Company stats:** 10+ US patents on Zero Trust security. $15M seed from SRI International and National Grid Partners. 120+ people, founded 2020 with SRI. Five books published on Zero Trust.

**Analysts and awards.** Three Gartner research mentions, including Emerging Tech Techscape 2025 and Hardened Container Images 2026. An Omdia vendor profile by Rik Turner, November 2025. Two Frost and Sullivan awards in 2026. Agentic AI Security Startup of the Year 2025.

**Partner validation.** AWS 2024 AI Partner Program. Red Hat verified and validated on RHEL. IBM and mimik Open Horizon project partner. Listed on the AWS, Azure, GCP, Oracle and Alibaba marketplaces.

**Lighthouse contracts.** $1.5M from NSF, SRI and the US Army Under Secretary of Defense for 5G security research. $500,000 for Zero Trust satellite security.

**Customer quotes (with headshot and logo):**

> The 45% reduction in engineering overhead alone justified our investment. Their platform eliminated the alert fatigue that was burning out our security team.
> **Tyler Pinckard**, Head of Security and DPO, SupportLogic

> We conducted an extensive evaluation of vendors and selected AccuKnox based on their features, ease of deployment, third party integrations, and real-time security to prevent advanced zero-day attacks.
> **David Billeter**, Cybersecurity Leader, Sonesta International Hotels · `[IMG] David-Billeter-testi.webp` `[IMG] sonesta-home.webp`

> Choosing AccuKnox was driven by KubeArmor's novel use of eBPF and LSM technologies, delivering automatic, scalable and highly effective runtime Zero Trust security.
> **Golan Ben-Oni**, CIO, IDT Telecom · `[IMG] golan-ben-oni.webp` `[IMG] idt-1.webp`

> AccuKnox does a tremendous job at showing the complexity of different approaches to Kubernetes security in terms of the speed of response against emerging CVEs and unknown cloud attacks.
> **James Berthoty**, Founder and Security Analyst, Latio · `[IMG] jamesb.png` `[IMG] latio3.webp`

---

## Section 17b. Resources

Layout kept from the current page. Four typed resource cards.

| Type | Title | Image |
|---|---|---|
| eBook | ModelKnox AI-SPM for AI security and LLM protection | `zero-trust-llm-security-featured.webp` |
| Blog | CNAPP solution buyer's guide | `cnapp-buyers-guide-400x250.webp` |
| Help doc | AccuKnox platform user manual | `help-doc-platform.webp` |
| Video | AccuKnox CNAPP explainer | `explainer-2.0.webp` |

---

## Section 18. Proof of concept and FAQs

**H2:** CNAPP proof of concept in three weeks

**Sub:** Most CNAPP vendors need six to eight weeks. Success criteria are agreed in writing before it begins.

| Week | What happens |
|---|---|
| Week 1 | Onboarding and discovery. One cluster or one cloud account, read-only IAM credentials, and roughly two hours from your team. |
| Week 2 | Policy and findings. Hardening policies activate in audit mode. Findings are triaged jointly with the AccuKnox team. |
| Week 3 | Enforcement and readout. Block mode enforcement, then a readout against the agreed success criteria. |

[CTA primary] Book a technical deep dive · [CTA secondary] Talk to a security expert

### Platform FAQs

1. **What is the difference between KSPM and CWPP, and do I need both?** KSPM checks how a Kubernetes cluster is configured. CWPP controls what a running workload is permitted to do. Posture without runtime leaves you exposed to zero days, and runtime without posture leaves misconfigurations in place, so most enterprises run both.
2. **Does AccuKnox block attacks or only detect them?** Both. eBPF provides the telemetry and Linux Security Modules perform the enforcement, so an unauthorized process, file access or network call is denied at the syscall before it completes.
3. **Can AccuKnox run fully air-gapped with no telemetry leaving my network?** Yes. The air-gapped build has no telemetry and no outbound connection, which is what GDPR, DPDP and ITAR environments require.
4. **Does AccuKnox work on VMs and bare metal, or only Kubernetes?** One agent covers Kubernetes, Docker, virtual machines, bare metal and edge devices on ARM and x86.
5. **Which AI security controls are in production today?** AI-SPM, the stateful prompt firewall, automated red teaming, AI-DR and agentic AI security are in production. AI Identity Security and AI-GRC are on the roadmap.
6. **How does AccuKnox reduce false positives on vulnerability findings?** Runtime context. A CVE present on disk but never loaded into memory drops in priority, which is where the reported 80% alert reduction comes from.
7. **Which compliance frameworks ship out of the box, and can I add my own?** 45+ frameworks ship out of the box. Custom compliance maps internal policy into the same engine.
8. **What does agentless onboarding cover, and when is the agent needed?** Agentless covers cloud posture, compliance, asset inventory, KSPM, KIEM and risk assessment. The agent is needed for runtime enforcement, application behavior monitoring and microsegmentation.
9. **How do findings reach my existing SIEM and ticketing system?** Through 50+ integrations including Splunk, QRadar, Elastic, Azure Sentinel, Jira and ServiceNow. ServiceNow sync is bidirectional.
10. **What does a proof of concept require from my team?** One cluster or one cloud account, read-only IAM credentials and roughly two hours. Write permissions are only needed if you want CDR auto-remediation during the proof of concept.
