# AccuKnox Platform Pages — Content Plan & Gap Analysis

**Sources used:**
- Live scrape of `accuknox.com/platform/aspm`, `/cspm`, `/kubernetes-security`, `/cwpp`
- PDFs: `ASPM PlayBook - April 2026.pdf`, `CSPM_POC_Pre-Req.pdf`, `AccuKnox Container Security POC (CWPP +KSPM).pdf`, `CWPP Playbook.pdf`, `AccuKnox Container Security POC.pdf`
- Help docs: `faqs/aspm.md`, `faqs/cspm.md`, `faqs/kspm.md`, `faqs/runtime-security.md`, `how-to/aspm-overview.md`

---

## Table of Contents
1. [ASPM — Application Security Posture Management](#1-aspm)
2. [CSPM — Cloud Security Posture Management](#2-cspm)
3. [Kubernetes Security / KSPM](#3-kubernetes-security--kspm)
4. [CWPP — Cloud Workload Protection Platform](#4-cwpp)
5. [Cross-Cutting Gaps & Recommendations](#5-cross-cutting-gaps--recommendations)

---

## 1. ASPM

### What the Current Page Has
- Hero statement: "Shift Left" application security testing
- Problem framing: alert noise, false positives, silos between AppSec and CloudSec
- Solution overview: integrates SCA, SAST, DAST, IaC scanning
- IaC Scanner section and GitHub Actions integration
- Pipeline stages: Dev/QA → Application → Production (ASPM)
- Tools supported logos (image only — no list)
- Scheduled & on-demand reports callout
- Pricing CTA
- Guide section: What is ASPM, Core Components, Components Table, Use Cases
- FAQs (7 questions)
- Latest Resources links

---

### Pain Points (Current + From Playbook/Docs)

| Pain Point | Source |
|---|---|
| Security teams drowning in 10,000+ findings with no prioritization | Playbook headline |
| False positives and unexploitable findings create alert fatigue | Platform page |
| AppSec and CloudSec tools work in silos — no shared context | Platform page |
| No runtime context for static findings (can't tell what's running) | Platform page |
| Manual pen testing every few months creates long exposure windows | FAQ docs |
| No single source of truth across code, pipeline, and runtime | Guide section |
| Supply chain vulnerabilities in third-party dependencies undetected | Playbook Use Cases |
| Sensitive data (private keys, credentials) embedded in container images | Playbook Use Cases |
| IaC misconfigurations reaching production (S3 public access, privilege escalation) | Playbook Use Cases |
| Teams lack CI/CD pipeline security gates — builds deploy with known issues | Playbook |

**Gaps: Missing from current page**
- No quantified pain point stats (e.g., "X% of CVEs are unexploitable at runtime")
- No buyer persona framing (who suffers: Dev, AppSec, CISO?)
- No "day in the life" scenario showing the before/after

---

### Use Cases (Current + From Playbook/Docs)

**From Playbook (April 2026)**
- Container Scan: Dependency analysis / supply chain vulnerabilities
- Container Scan: Sensitive data exposure (RSA keys in images)
- Container Scan: Authentication vulnerabilities (curl/libcurl bypass)
- IaC Scan: Public cloud exposure (S3 without `restrict_public_buckets`)
- IaC Scan: Privilege escalation enabled (`allowPrivilegeEscalation`)
- IaC Scan: Credential exposure in manifests
- SAST Scan: Static code vulnerability detection
- DAST Scan: Authenticated and unauthenticated endpoint scanning
- Secret Scanning: Secrets in CI/CD pipelines, code repos, S3 buckets, container images, Kubernetes ConfigMaps

**From Guide/FAQ**
- Secure CI/CD pipelines from build to deploy
- Identify and prioritize exploitable vulnerabilities (vs. unexploitable noise)
- Monitor for software drift and zero-day threats
- Achieve compliance with DevSecOps maturity frameworks
- Reduce MTTR by unifying context from code to cloud
- EPSS scoring for prioritization
- Rules engine and automated ticket creation
- SCA for software composition analysis
- SBOM analysis (on roadmap)

**From Help Docs (aspm-overview.md)**
- IaC Scanning
- Container Scanning
- SAST
- Vulnerability Management
- DAST (MFA-enabled)
- DAST XSS Mitigation
- Secret Scan in CI/CD
- Secrets in Code Repositories
- Secrets in S3 Buckets & File Systems
- Rules Engine & Automated Ticket Creation
- EPSS Scoring for Prioritization
- SCA
- Secrets in Container Images
- Secrets in Kubernetes ConfigMaps
- IaC Security (Azure)

**Gaps: Missing use cases from current page**
- Secret scanning is barely mentioned (only in help docs)
- DAST use cases not demonstrated on page
- EPSS scoring for prioritization not showcased
- SBOM analysis not mentioned
- Rules engine / automated ticket creation not surfaced
- Software drift detection not explained

---

### Features

| Feature | Description |
|---|---|
| SAST | Static code analysis integrated via CI/CD |
| SCA | Software Composition Analysis for OSS dependencies |
| DAST | Dynamic testing — authenticated and non-authenticated |
| IaC Scanning | Terraform, Helm, CloudFormation misconfiguration detection |
| Container Scanning | Registry and CI/CD-based image vulnerability scanning |
| Secret Scanning | Detect secrets in repos, images, S3, ConfigMaps, pipelines |
| EPSS Scoring | Exploit Prediction Scoring System for prioritization |
| Rules Engine | Automated ticket creation on policy violations |
| CI/CD Pipeline Gates | Block builds on policy violation |
| GitHub Actions Integration | Container scan + IaC scan actions in GitHub Marketplace |
| Jenkins Integration | Plugin-based container scan + IaC integration |
| GitLab CI/CD | Supported (mentioned in overview) |
| Azure DevOps | Supported (mentioned in overview) |
| Findings Dashboard | Registry scan page + Findings page with filters |
| SBOM Analysis | On roadmap per FAQ |
| Auto-PR / Auto-patch | In progress (planned Oct 2025, now in 2026) |

---

### Dashboard / Feature Showcase

**What exists on the page:**
- ASPM workflow diagram (static image)
- IaC scan devops image
- Production ASPM image
- Application image (Dev/QA)
- ASPM Reports image

**What the Playbook demonstrates (not on page):**
- Label and token creation flow (Settings → Labels/Tokens)
- GitHub Actions workflow YAML configuration
- Jenkins plugin installation and job configuration
- Registry scan page with findings
- Findings page with Container Image Findings dropdown
- IaC Findings page with arrow-to-detail UI
- Step-by-step use case screenshots per scan type

**Gaps: Missing from page**
- No embedded product tour / interactive walkthrough for ASPM
- No screenshot walkthrough of the Findings page
- No live example of a finding with CVE detail + recommended fix
- No dashboard aggregate view showing "X findings, Y critical, Z fixed"
- No demo of EPSS-based prioritization UI

---

### AccuKnox Differentiators (ASPM)

| Differentiator | Basis |
|---|---|
| Multi-tool parser flexibility (open source + commercial) | Integrates many scanning tools via built-in parsers — not locked to one |
| Composite posture — not a single-tool result | Normalizes and correlates findings from multiple tools |
| Runtime context layered over static findings | Understands what's actually running to deprioritize unexploitable CVEs |
| CI/CD native with GitHub Actions in GitHub Marketplace | AccuKnox Container Scan + IaC actions published and usable directly |
| Zero Trust integration — runtime enforcement via KubeArmor | ASPM signals feed into runtime policy enforcement |
| No IDE lock-in — pipeline-first strategy | Works with existing IDEs, enforces security at pipeline level |
| Code-to-cloud continuity | Single platform from SAST/SCA → IaC → Container → Runtime |

---

### Integrations (ASPM)

**CI/CD Platforms:**
- GitHub Actions (Marketplace: AccuKnox Container Scan, AccuKnox IaC)
- Jenkins (Plugin-based)
- GitLab CI/CD
- Azure DevOps
- Others (see CI/CD support matrix)

**Scanning Tools Supported (from page):**
- Trivy (container scanning)
- Checkov, tfsec (IaC)
- Semgrep (SAST)
- OWASP ZAP (DAST)
- TruffleHog / Gitleaks (secret scanning)
- *(exact list shown as logos — needs text version)*

**Ticketing / ITSM:**
- Jira (auto-ticket on finding)
- Freshservice
- ConnectWise

**SIEM:**
- Splunk, ELK (log forwarding)

---

### Onboarding (ASPM)

**Steps from Playbook:**
1. Generate AccuKnox Label: Settings → Labels → Create → copy label
2. Generate AccuKnox API Token: Settings → Tokens → Create → copy token
3. Configure label + token as secrets in CI/CD pipeline
4. Add AccuKnox GitHub Action (container scan or IaC) to `.github/workflows/*.yml`
5. Push to trigger workflow, or run manually from Actions tab
6. Review findings: AccuKnox dashboard → Issues → Findings → Select scan type

**For Jenkins:**
1. Manage Jenkins → Plugins → Advanced → Upload & install AccuKnox plugin
2. Open Jenkins job → Add build step → Select AccuKnox scan → Fill details → Trigger

---

### Important Links & Resources (ASPM)

| Resource | URL |
|---|---|
| ASPM Overview (Help) | https://help.accuknox.com/how-to/aspm-overview/ |
| CI/CD Support Matrix | https://help.accuknox.com/support-matrix/cicd-support-matrix/ |
| CI/CD Integrations | https://help.accuknox.com/integrations/cicd-overview/ |
| DevSecOps Page | https://help.accuknox.com/getting-started/devsecops/ |
| IaC Scan Use Case | https://help.accuknox.com/use-cases/iac-scan/ |
| Container Scan Use Case | https://help.accuknox.com/use-cases/container-scan/ |
| SAST Use Case | https://help.accuknox.com/use-cases/sast-sq/ |
| DAST (MFA) | https://help.accuknox.com/use-cases/mfa-dast/ |
| Secret Scan CI/CD | https://help.accuknox.com/use-cases/secret-scan-cicd-aws/ |
| ASPM Secrets in Repos | https://help.accuknox.com/use-cases/aspm/ |
| EPSS Scoring | https://help.accuknox.com/use-cases/epss-scoring/ |
| Rules Engine & Ticketing | https://help.accuknox.com/use-cases/rules-engine-ticket-creation/ |
| GitHub Action: Container Scan | https://github.com/marketplace/actions/accuknox-container-scan |
| GitHub Action: IaC | https://github.com/marketplace/actions/accuknox-iac |
| ASPM Definitive Guide (eBook) | https://accuknox.com/ebooks/application-security-posture-management-definitive-guide |
| Azure IaC Integration | https://help.accuknox.com/integrations/azure-iac/ |

---

### Diagrams to Include (ASPM)

1. **SDLC Pipeline Security Flow** — Show Dev → Build (SAST/SCA) → IaC Scan → Container Scan → Deploy → Runtime (KubeArmor). Highlight where each tool plugs in.
2. **Findings Funnel** — 10,000 raw findings → filtered by exploitability/runtime context → 5 actionable critical issues. Illustrates noise reduction.
3. **Tool Integration Architecture** — AccuKnox as aggregator receiving results from Trivy, Semgrep, Checkov, ZAP, TruffleHog via parsers.
4. **GitHub Actions Workflow Diagram** — PR/push → Trigger scan → Results in AccuKnox dashboard.
5. **ASPM Use Case Map** — Grid or table: Container Scan / IaC Scan / SAST / DAST / Secret Scan × Use Case.

---

## 2. CSPM

### What the Current Page Has
- Hero: "AI-Powered CSPM That Never Sleeps"
- Overview: Agentless, multi-cloud (AWS/Azure/GCP), 360° posture
- Bullet list: asset inventory, misconfiguration detection, prioritization, ticketing, CI/CD scan, K8s protection, runtime enforcement, KIEM
- CSPM workflow and compliance images
- Sections: Compliance/Drift/Monitoring, Scheduled Reports
- Contextual CSPM section: cloud attack path analysis, prioritization, risk profiling
- Competitor comparisons (Wiz, AquaSec, Calico, Palo Alto, Orca, Checkpoint, PingSafe, CrowdStrike)
- Pricing CTA
- Guide section: What is CSPM, Why Critical, Key Capabilities, Differentiators, Get Started
- FAQs (34 questions — extensive)
- Latest Resources

---

### Pain Points (Current + From CSPM POC Pre-Req)

| Pain Point | Source |
|---|---|
| Accidental public exposure of data (S3 buckets open to internet) | Platform page + POC doc |
| Over-permissioned IAM roles — blast radius too large | Platform page + POC doc |
| Unused or vulnerable cloud services accumulating | Platform page |
| Missed compliance controls in dynamic environments | Platform page |
| Configuration drift — infra diverges from Terraform/CloudFormation | POC doc |
| Root accounts with MFA disabled | POC doc |
| Stale access keys not rotated in >90 days | POC doc |
| Shadow admins via IAM policy chaining | POC doc |
| Hardcoded secrets in Lambda env vars, ECS task defs | POC doc |
| Unencrypted RDS + public subnet + permissive SG = data exfiltration | POC doc Toxic Combo |
| Cross-account trust policies allowing lateral movement | POC doc |
| AI/LLM assets (Bedrock) unmonitored — no audit logging | POC doc |
| Cloud resources spin up and down without security team awareness | Platform page |
| No unified view across AWS + Azure + GCP | Platform page |

**Gaps: Missing from current page**
- Toxic Combination analysis is mentioned conceptually but not showcased with examples
- AI/LLM governance angle (Bedrock, OpenAI) is not present on the page
- Drift detection from CloudTrail correlation not detailed
- Specific IAM hardening use cases not shown
- Public exposure scenarios (RDS, EC2 public IP) not concretely illustrated

---

### Use Cases (Current + From POC Pre-Req Doc)

**From POC Pre-Req (CSPM):**
- Global Asset Inventory: Auto-discover 50+ AWS asset types, ghost resource detection (orphaned EBS, stale IAM)
- Egress/Ingress mapping: Flag ports open to 0.0.0.0/0 (SSH/RDP/HTTP/HTTPS)
- Toxic Combination Analysis: Chains of misconfigs → exploitable attack paths
  - Public EC2 + Missing IMDSv2 + Overprivileged Instance Role = High-priority path
  - Unencrypted RDS + Public Subnet + Permissive SG = Data exfiltration risk
- Compliance: CIS v2.0 (200+), NIST 800-53 (110+), SOC2 (64+), HIPAA (54+), PCI-DSS v4.0 (80+), ISO 27001 (114+), AWS Well-Architected (50+)
- Drift Detection: Console drift from Terraform/CloudFormation + CloudTrail correlation
- IAM Hardening: Root MFA, stale keys, over-privileged roles, shadow admins, unused identities, cross-account trust
- Public Exposure: S3 encryption, RDS publicly accessible, EBS unencrypted, endpoint exposure
- Secrets & Data Discovery: Lambda env vars, ECS task definitions, SSM Parameter Store
- AI/Bedrock Governance: Discover active Bedrock models, validate audit logging, IAM scope, encryption, data residency, endpoint exposure

**CDR (Cloud Detection & Response) Use Cases:**
- S3 Auto-Remediation: Exposed S3 bucket → private in <60 seconds
- EC2 Public IP Removal: Detached within 90 seconds of policy violation
- Geo-Fencing Alert: Critical alert within 30 seconds of access from denied region
- Auto-formatted Jira tickets per critical finding
- Real-time Slack alerts on CDR event with asset context

**From Platform Page:**
- Detect and fix misconfigured S3 buckets, IAM roles, and exposed services
- Monitor compliance across cloud accounts
- Reduce noise by correlating risks across services and regions
- Empower DevSecOps with security insights in the pipeline
- Agentless inventory of cloud assets

---

### Features

| Feature | Description |
|---|---|
| Agentless Cloud Scanning | 100% API-based read, no data stored outside tenant boundary |
| Asset Inventory (50+ types) | Compute, Storage, Network, IAM, Databases, AI/ML, Serverless |
| 1500+ Built-in Policies | Mapped to CIS, NIST, SOC2, HIPAA, PCI-DSS |
| Toxic Combination Analysis | Correlates isolated findings into exploitable attack chains |
| Compliance Mapping | 30+ frameworks: CIS, NIST, SOC2, HIPAA, PCI-DSS, ISO 27001, GDPR, FedRAMP |
| Drift Detection | Detects console drift vs IaC templates; CloudTrail correlation |
| IAM Hardening | Root MFA, stale keys, over-privileged roles, shadow admins, unused identities |
| AI/Bedrock Governance | Discover AI assets, validate logging, scope IAM, check data residency |
| Attack Path Analysis | Visualize exploitable paths across resources |
| Scheduled + On-Demand Reports | CSPM PDF report generation |
| CDR (Cloud Detection & Response) | Auto-remediation: S3, EC2, IAM rollback in <2 minutes |
| AI Copilot (AskADA) | Asset-specific Terraform fix snippets on demand |
| Agentless VM Scanning | For cloud accounts (AWS, Azure) |
| KIEM | Kubernetes Identity & Entitlement Management |

---

### Dashboard / Feature Showcase

**What exists on page:**
- CSPM report image
- GCP Security Cheatsheet image
- Storage/compute/network CSPM images
- CSPM Reports image

**What POC doc demonstrates (not on page):**
- 2-week POC execution timeline with specific daily deliverables
- POC Success Criteria Matrix (12 use cases with pass/fail)
- Onboarding workflow: 6-step diagram (Account Selection → IAM Provisioning → Asset Tagging → Integration → Automated Scan)
- CSPM PoC Steps: AWS Accounts → Cloud Telemetry → AccuKnox Control Plane → Response & Reporting
- Weekly triaging sessions with AccuKnox team
- Executive Summary Report template

**Gaps: Missing from page**
- No interactive product tour for CSPM (unlike CWPP which has "Self Guided Tour")
- Toxic Combination visual — showing how two separate findings chain into attack path
- AI Copilot / AskADA not surfaced on main page
- CDR auto-remediation not shown with timeline metrics (<60s, <90s)
- No compliance coverage table showing frameworks + control counts

---

### AccuKnox Differentiators (CSPM)

| Differentiator | Basis |
|---|---|
| Zero Trust Architecture with CSPM | Combines posture management with runtime enforcement |
| Deep Kubernetes visibility | KSPM integrated alongside cloud CSPM |
| Toxic Combination analysis | Chains isolated findings into exploitable paths (vs. raw alert counts) |
| CDR with sub-minute auto-remediation | S3 →private in <60s, EC2 public IP removal in <90s |
| AI/LLM Governance built-in | Bedrock model discovery, audit log validation — unique to AccuKnox |
| Agentless + agent-based flexibility | No forced trade-off |
| Open-source integration | OpenSCAP, KubeArmor |
| 1500+ built-in policies | Broadest policy library in class |
| AskADA GenAI Copilot | On-demand asset-specific Terraform fix snippets |

**Competitor differentiation links already on page:**
- vs Wiz, AquaSec, Calico, Palo Alto/Prisma, Orca, Checkpoint, PingSafe, CrowdStrike

---

### Integrations (CSPM)

**Cloud Providers:**
- AWS (standalone account or AWS Organization Unit)
- Azure
- GCP
- Hybrid cloud

**Data Sources:**
- AWS: CloudTrail, AWS Config, VPC Flow Logs, GuardDuty, Bedrock audit logs
- Agentless VM scanning (cloud VMs)

**Ticketing / ITSM:**
- Jira (auto-formatted tickets with asset ID + severity)
- ServiceNow (SNOW table API, dynamic incident template)
- Freshservice
- ConnectWise

**Alerting / Notification:**
- Slack (real-time, severity-filtered routing)
- Microsoft Teams (webhook URL)
- PagerDuty (on-call escalation for Critical CDR events)
- Email (SMTP daily digest + individual finding alerts)

**SIEM:**
- Splunk
- ELK

**Automation / Response:**
- Webhooks (generic)
- AWS Lambda / serverless for auto-remediation

---

### Onboarding (CSPM)

**From POC Pre-Req Doc — 6 Steps:**
1. **Account Selection:** Choose AWS Org Unit or standalone account, select deployment model (SaaS vs. On-Prem)
2. **IAM Provisioning:** Grant read-only role for discovery phase; contributor/write role for CDR auto-remediation
3. **Asset Tagging & Scope Setup:** Tag assets by team & type; set compliance frameworks
4. **Integration:** Link Slack, Jira, or ServiceNow
5. **Automated Security Scan:** First scan runs; assets discovered
6. **Ongoing Monitoring:** Continuous scanning, drift detection, CDR alerts

**Prerequisites (AWS):**
- AWS IAM with `ReadOnlyAccess` + `SecurityAudit` (or equivalent)
- For CDR write permissions: `s3:PutBucketPublicAccessBlock`, `ec2:TerminateInstances`, `cloudtrail:StartLogging`
- For AI/Bedrock: additional permissions for Bedrock model discovery
- Jira project URL (optional), Slack workspace + channel (optional)

**Reference Links:**
- Standalone account onboarding: help.accuknox.com (standalone)
- Organization onboarding: help.accuknox.com (org)
- Agentless VM scanning: help.accuknox.com/how-to/agentless-vm-scan

---

### Important Links & Resources (CSPM)

| Resource | URL |
|---|---|
| AWS Onboarding | https://help.accuknox.com/how-to/aws-onboarding/ |
| Azure Onboarding | https://help.accuknox.com/how-to/azure-onboarding/ |
| CSPM Prerequisites AWS | https://help.accuknox.com/getting-started/cspm-prereq-aws/ |
| CSPM Use Cases Overview | https://help.accuknox.com/use-cases/cnapp-security-overview/ |
| Jira Integration | https://help.accuknox.com/integrations/ (CSPM section) |
| Cloud Offboarding | https://help.accuknox.com/how-to/cloud-offboarding/ |
| CSPM Report PDF | https://help.accuknox.com/resources/assets/CSPM_Report.pdf |
| GCP Security Cheatsheet | https://accuknox.com/cheatsheets/gcp-security |
| CSPM eBook | https://www.accuknox.com/wp-content/uploads/CSPM_eBook.pdf |
| Asset Inventory Video | https://www.youtube.com/watch?v=7K09AW4aH4c |
| AI-Powered Cloud Security Video | https://www.youtube.com/watch?v=hKNTGE85ATI |

---

### Diagrams to Include (CSPM)

1. **Cloud Account Onboarding Workflow** — 6-step visual: Select Accounts → IAM Provisioning → Tag Resources → Connect Apps → Automated Scan (from POC doc — can be adapted).
2. **Toxic Combination Analysis Visual** — 3-node chain: Public EC2 + Missing IMDSv2 + Overprivileged Role → Attack Path (risk score and blast radius).
3. **Compliance Coverage Matrix** — Table showing CIS/NIST/SOC2/HIPAA/PCI-DSS/ISO with control counts and pass/fail rates.
4. **CDR Auto-Remediation Timeline** — S3 event detected → auto-remediation triggered → private in <60 seconds. EC2 IP removal in <90 seconds.
5. **AI/Bedrock Governance Architecture** — AccuKnox scanning Bedrock models, checking VPC endpoints, validating logging, IAM scope.
6. **Multi-Cloud Unified Dashboard Concept** — Single pane of glass: AWS + Azure + GCP assets, risk score per cloud.

---

## 3. Kubernetes Security / KSPM

### What the Current Page Has
- Hero: "Tired of Complex Kubernetes Architecture?" / "Simple Kubernetes Security That Prevents Unknown Attacks"
- Stats: 78% orgs use K8s; 62% severely misconfigured
- CNAPP for enterprise Kubernetes
- KSPM Section: Misconfiguration detection, CIS/STIGs benchmarks, Admission Controller, Security Risk Assessment, KIEM, K8TLS (TLS Posture)
- Runtime Security Section: K8s/Containers/VM/Baremetal, Workload Hardening, Network Microsegmentation, App Behavior Monitoring, Zero Trust Policy, Auto Remediation
- Key Challenges: Network Security, Identity & Access, Securing Containers, Monitoring & Detection
- Zero Trust Platform section: Runtime Guardrails, Incident Response, Compliance Reporting
- Key Capabilities table: Runtime Guardrails, Threat Detection, Compliance & Forensics
- Differentiators: Purpose-built, Simple DevSecOps Flow, Proactive, Compliance Checks, Trusted
- KSPM Guide section + FAQs (15 questions)
- Download: Zero Trust Kubernetes Security Definitive Guide

---

### Pain Points (Current + From Container Security POC)

| Pain Point | Source |
|---|---|
| 62% Kubernetes deployments are severely misconfigured/unsecured | Platform page stat |
| Flat network topology — any compromised pod can laterally access others | Platform page |
| Cryptojacking malware spreading between pods | Platform page |
| Misconfigured cluster roles and namespaces | Platform page + POC |
| Excessive RBAC permissions — over-permissioned service accounts | Platform page + POC |
| Unsecured workloads and network paths | Platform page |
| Limited visibility into dynamic, short-lived pods | Platform page |
| Unauthorized process execution from /tmp folders | Container POC |
| Crypto-mining binaries executing in containers | Container POC |
| Containers with `allowPrivilegeEscalation` enabled | Container POC + ASPM Playbook |
| Container management tools used from within containers | Container POC |
| Penetration testing / recon tools (nmap, masscan) running inside containers | Container POC |
| Workloads missing CPU/memory limits | Container POC |
| Secrets and credentials embedded in K8s manifests | Container POC |
| Service accounts with anonymous access | Container POC |
| Privileged containers running in the cluster | Container POC |
| Writable hostPath volumes | Container POC |
| Users/namespaces with ClusterAdmin privileges | Container POC |

---

### Use Cases (Current + From Container Security POC)

**From Container Security POC (KSPM section):**

*Container Runtime Security:*
- File Integrity Monitoring/Protection — block updates to system bin/boot folders
- Protecting Trusted Root Certificates — block tampering of cert stores
- Flag Process executions from /tmp
- Detect Anomalous Process Executions (auto-discovered behavioral baseline)
- Prevent Crypto Mining executions
- Prevent unauthorized access to environment variables
- Audit package management tool use at runtime (apt, dnf)
- Prevent container management tools from being used within containers (docker, crictl, kubectl)
- Prevent use of masscan/nmap from within containers
- Prevent/Audit filesystem-related operations (mount, nsenter, fsck, lsblk)
- Prevent Recon/Pen Testing tools from within containers
- Apply policies via CLI, Control Plane, or GitOps
- Classify process executions (interactive terminal vs background)
- Process Whitelisting — Zero Trust execution model
- Nano Segmentation — only trusted processes handle network communication
- Protect HashiCorp Vault Secrets Manager on-prem (advanced)

*Compliance:*
- CIS scan of Kubernetes cluster
- MITRE ATT&CK framework mapping for policies and violations
- NIST 800-53 mapping

*Cluster Misconfiguration Detection:*
- Identify service accounts with anonymous access
- Identify secrets/credentials in manifests and config files
- Ensure CPU/Memory limits across all workloads
- Identify external-facing workloads
- Detect workloads with Host PID/IPC privileges
- Detect use of privileged containers
- Detect use of writable hostPath volumes

*K8s Identity & Entitlements (KIEM):*
- Identify users/services/namespaces with ClusterAdmin privileges
- Identify K8s service accounts with elevated permissions
- Identify unused roles not mapped to workloads
- Identify subjects with permission to create roles and role bindings

*Vulnerability Scanning:*
- Scan container images in K8s environment
- Alert on new critical vulnerabilities
- Show vulnerabilities in context of clusters/namespaces/workloads
- Triage and handle findings lifecycle

**From Platform Page (additional):**
- K8TLS (TLS Posture) enforcement
- Admission Controller / Pod Security Admission (PSA)
- K8s Security Risk Assessment
- Network Microsegmentation (L3/L4/L7)
- Zero Trust Policy enforcement

---

### Features

| Feature | Category | Description |
|---|---|---|
| K8s Misconfiguration Detection | KSPM | Identify security misconfigs in K8s setup |
| CIS/STIGs Benchmarks | KSPM | Scan and report against CIS and STIG standards |
| Admission Controller (KnoxGuard) | KSPM | PSA support, controls container image deployment |
| K8s Security Risk Assessment | KSPM | Evaluate and prioritize risks across K8s resources |
| KIEM | KSPM | Manage unused service accounts, revoke excess permissions |
| K8TLS | KSPM | Enforce TLS and certificate best practices |
| Runtime Protection (KubeArmor) | Runtime | eBPF + LSM enforcement: process, file, network |
| Workload Hardening | Runtime | FIM, malware protection, root cert protection |
| Network Microsegmentation | Runtime | Auto-discover and suggest network policies |
| App Behavior Monitoring | Runtime | File, process, network activity + workload network graph |
| Zero Trust Policy | Runtime | ZTNA + process whitelisting |
| Auto Remediation | Runtime | Kill process, quarantine pod on threat detection |
| Pod Security Admission (PSA) | Runtime | Privileged/Baseline/Restricted levels + enforce/audit modes |
| Policy Discovery Engine | Runtime | Auto-discover behavioral policies per workload |
| GitOps Policy Management | Policy | Apply policies via CLI, UI, or GitOps |
| MITRE ATT&CK Mapping | Compliance | Map violations to MITRE techniques |
| NIST 800-53 Mapping | Compliance | Map findings to NIST controls |
| CIS Benchmark Scan | Compliance | Automated cluster hardening scan |
| Vulnerability Scanning (Container) | Vuln Mgmt | Scan images in K8s for CVEs |
| Nano Segmentation | Advanced | Process-level network trust enforcement |

---

### Dashboard / Feature Showcase

**On page currently:**
- KSPM dashboard image
- KSPM architecture SVG
- Kubernetes security KSPM image (gated download CTA)

**From CWPP Playbook (applicable to K8s too):**
- Cluster Onboarding: Settings → Manage Cluster → Onboard Now
- Cluster View: Inventory → Clusters → View Workloads
- App Behavior: Runtime Protection → App Behavior → Network Graph + List View
- Policies → Discovered tab (behavioral whitelisting)
- Zero Trust Journey: audit mode → stable → block mode progression
- Policies → Hardening tab (MITRE/CIS/NIST hardening policies)
- Pod Security Admission: Inventory → Clusters → cog → PSA level + mode + Dry Run
- Alerts: Monitors/Alerts → Alerts (custom filters)
- CWPP Dashboard: Runtime Protection → CWPP Dashboard (per cluster)

**From Container Security POC:**
- Control Plane visibility for all audit/block events
- GitOps policy management workflow

**Gaps: Missing from page**
- No product tour / self-guided tour (unlike CWPP page which has one)
- Zero Trust Journey progression not visualized (audit → stable → block)
- KIEM dashboard not shown
- No network graph visualization shown
- K8TLS tool not linked to a demo or screenshot
- Nano segmentation concept not shown with visual

---

### AccuKnox Differentiators (Kubernetes/KSPM)

| Differentiator | Basis |
|---|---|
| Inline mitigation (pre-execution) vs post-attack detection | KubeArmor stops attacks at syscall level before execution |
| eBPF + LSM (AppArmor/BPF-LSM/SELinux) — kernel-level | Not just application-layer hooks — true system-level enforcement |
| Open-source KubeArmor (CNCF sandbox project) | Transparent, extensible, community-backed |
| Patented micro-segmentation technology | Pod-level isolation using Linux primitives |
| Zero True Positive rate for false positives | Policy-based allows only; everything else blocked |
| Multi-LSM abstraction — AppArmor, BPF-LSM, SELinux | Works across node types with different LSMs seamlessly |
| Auto-policy discovery — behavioral learning | No manual policy writing required |
| 50 microservices protected under 1 hour | Fast time-to-value for enterprise deployments |
| Multi-environment: K8s, VM, BareMetal, IoT/Edge | One agent, any workload type |
| Supports: EKS, AKS, GKE, RKE/Robin, on-prem, edge | Broadest Kubernetes distribution support |
| K8TLS in-house TLS posture tool | Open-source, native to AccuKnox |

---

### Integrations (Kubernetes Security)

**Deployment:**
- Kubernetes clusters: EKS, AKS, GKE, RKE/Robin, on-prem
- Containers: Docker, Containerd, CRIO, Podman
- VM/Bare-Metal: Virtual Machines, Bare Metal
- IoT/Edge: ARM, x86

**Integration modes:**
- Agent-based (eBPF sensors via KubeArmor daemonset)
- Agentless (CronJob mode for KSPM posture checks)

**Policy / GitOps:**
- CLI (`knoxctl`)
- AccuKnox Control Plane UI
- GitOps workflows (policy-as-code)

**Notification / Alerting:**
- Slack
- Email
- Webhooks
- PagerDuty

**Ticketing:**
- Jira, ServiceNow, Freshservice

**SIEM:**
- Splunk, ELK

---

### Onboarding (Kubernetes)

**Agent-Based (from CWPP Playbook):**
1. Navigate to Settings → Manage Cluster → click "Onboard Now"
2. Provide a cluster name
3. Install agents via commands shown on screen (DaemonSet deployment)
4. Navigate to Inventory → Clusters to verify onboarded cluster
5. Click "View Workloads" to see containers/pods
6. Runtime Protection → App Behavior — review network graph

**On-Prem (from Container Security POC):**
- AccuKnox Control Plane: 1 VM, ≥16 vCPUs, ≥64 GB RAM, ≥512 GB disk (256 GB for /var)
- AccuKnox provides licensed installation tgz (~20 GB)
- No external network connectivity needed during installation
- Reference: https://help.accuknox.com/getting-started/on-prem-single-node-installation/

**Agentless KSPM:**
- CronJob-based scanning — no persistent agent required
- Works on any managed K8s (EKS, AKS, GKE)

---

### Important Links & Resources (Kubernetes)

| Resource | URL |
|---|---|
| Cluster Onboarding Help | https://help.accuknox.com/how-to/cluster-onboarding/ |
| CNAPP Security Overview | https://help.accuknox.com/use-cases/cnapp-security-overview/ |
| Admission Controller (KnoxGuard) | https://help.accuknox.com/use-cases/admission-controller-knoxguard/ |
| KIEM Use Case | https://help.accuknox.com/use-cases/kiem/ |
| Network Segmentation | https://help.accuknox.com/use-cases/cards/Network-Segmentation/ |
| Zero Trust Use Case | https://help.accuknox.com/use-cases/zero-trust/ |
| App Behavior | https://help.accuknox.com/saas/app-behavior/ |
| On-Prem Installation (Single Node) | https://help.accuknox.com/getting-started/on-prem-single-node-installation/ |
| KSPM Playbook | https://help.accuknox.com/how-to/playbook-kspm/ |
| KubeArmor Differentiation | https://docs.kubearmor.io/kubearmor/quick-links/differentiation |
| K8TLS GitHub | https://github.com/kubearmor/k8tls |
| KubeArmor GitHub | https://github.com/kubearmor/KubeArmor |
| Zero Trust K8s Guide (Download) | https://accuknox.com/ebooks/zero-trust-kubernetes-security-definitive-guide |

---

### Diagrams to Include (Kubernetes)

1. **eBPF / LSM Architecture Diagram** — Show how KubeArmor hooks into the kernel: syscall → eBPF probe → BPF-LSM / AppArmor / SELinux decision → allow/block. Differentiates inline vs post-attack.
2. **Kubernetes Attack Surface Map** — Cluster → Namespace → Pod → Container with labeled attack vectors: network lateral movement, cryptojacking, container escape, privileged container, /tmp execution.
3. **Zero Trust Journey Timeline** — Learning Mode → Audit Mode → Policy Stable → Enforce/Block Mode. Shows how behavioral policies evolve.
4. **KIEM Visual** — Service account → Role Binding → ClusterRole → overexposed permissions → KIEM identifies and remediates.
5. **Multi-Environment Deployment** — Single KubeArmor agent across K8s / VM / BareMetal / IoT-Edge.
6. **Network Microsegmentation Visual** — Pod-to-pod traffic with allowed (green) and blocked (red) paths, L3/L4/L7 labels.

---

## 4. CWPP

### What the Current Page Has
- Hero: Monitor runtime protection in multi-cloud with real-time alerts, compliance, asset coverage
- eBPF section: Multi-cloud vulnerabilities, application pod vulnerabilities, Detect & Respond challenges, Modern workload protection
- CNAPP Platform consolidation image (integrations)
- Agent-based CWPP section: Zero Trust fundamentals, NIST/Gartner alignment, proactive remediation, zero false positives, hardening policies
- Unique Offerings: App Behavior + Application Microsegmentation
- Scheduled & On-Demand Reports
- App Hardening section: CIS/MITRE/NIST-800-53/STIGs policies, block-based recommendations
- Network Micro Segmentation section
- Zero Trust Use Cases: Auto Discovered ZT Policy, Custom ZT Policy, Inline Remediation, Network Micro Segmentation
- Self Guided Tour (video)
- CWPP Product Tour
- Guide section: What is CWPP, Why it Matters, Key Capabilities, Components Table, Use Cases
- FAQs (6 questions)
- Latest Resources

---

### Pain Points (Current + From POC/Playbook)

| Pain Point | Source |
|---|---|
| Traditional security tools miss ephemeral, short-lived workloads | Platform page |
| Process injection and privilege escalation at runtime | Platform page |
| Vulnerability exploitation in container images or serverless | Platform page |
| Difficulty tracking workload activity across multi-cloud | Platform page |
| Remote code execution from compromised application pods | Platform page |
| False sense of security from post-attack mitigation engines | Platform page |
| Zero-day attacks not stopped until after execution (post-exploit) | Platform page |
| Unauthorized access to environment variables | Container POC |
| File system tampering (mount, nsenter, fsck operations) | Container POC |
| Crypto-mining binaries executing in workloads | Container POC |
| Package management tools (apt, dnf) abused at runtime | Container POC |
| Container management tools (docker, kubectl) used inside containers | Container POC |
| Recon/pen testing tools (nmap, masscan) run from within containers | Container POC |
| Trusted root certificates tampered | Container POC |
| HashiCorp Vault accessed without authorization (on-prem) | Container POC |
| Lateral movement via network between pods/workloads | CWPP Playbook + Platform page |
| Multi-tenant deployment risks (shared environments) | Container POC architecture |

---

### Use Cases (Current + From Playbook/POC)

**From CWPP Playbook:**
- Cluster Onboarding (agent-based)
- Application Behavior Monitoring (graph + list view)
- Policy Discovery (behavioral whitelist generation)
- Zero Trust Journey: audit → stable → enforce block mode
- Hardening Policies (MITRE/CIS/NIST framework policies → activate)
- Pod Security Admission (PSA) configuration (Privileged/Baseline/Restricted × enforce/audit)
- Log & Alert monitoring for policy violations (custom filter + save)
- Container Registry Scanning (onboard registries, scan by regex/date/schedule)
- Container Image Inventory (Inventory → Cloud Assets → Container filter)
- Viewing all Container Image Findings

**From Container Security POC (same as K8s runtime section above):**
- Full list of 15+ runtime use cases

**From Platform Page:**
- Auto discovered Zero Trust policy (behavioral baseline)
- Custom Zero Trust policy (Policy Editor)
- Inline Remediation against APT and log4j-style attacks
- Network Micro Segmentation (lateral movement prevention)
- Workload security across public cloud, private cloud, on-prem VMs/BareMetal
- Protect Jupyter Notebook from malicious code execution (demo video)

---

### Features

| Feature | Description |
|---|---|
| eBPF-based Runtime Protection | Kernel-level visibility and enforcement (BPF-LSM) |
| App Behavior Monitoring | File, process, network observability per workload; network graph |
| Auto Policy Discovery | Behavioral policies auto-generated from workload observation |
| Policy Enforcement (block/audit) | Fine-grained control — syscall, file I/O, network |
| Hardening Policies | Based on MITRE, CIS, NIST-800-53, STIGs |
| Network Microsegmentation | Pod-level isolation; L3/L4/L7; CNI-agnostic |
| Zero Trust Policy (custom) | Policy Editor for personalized rule creation |
| Inline Remediation | Stops attacks pre-execution using LSM enforcement |
| Pod Security Admission | Privileged/Baseline/Restricted + enforce/audit modes |
| Container Registry Scanning | Onboard registries; scan by regex, update date, pull date |
| Container Image Vulnerability | Scan images for CVEs; view in context of workloads |
| Vulnerability Triage | Lifecycle management: review, suppress, accept risk, remediate |
| CWPP Dashboard | Per-cluster comprehensive view after policies applied |
| Scheduled + On-Demand Reports | CWPP PDF reports |
| GitOps Policy Management | CLI + UI + GitOps workflow support |
| Alerts & Forensics | Monitors/Alerts → Alerts with custom filtering; detailed audit logs |

---

### Dashboard / Feature Showcase

**From CWPP Playbook (step-by-step UI flows):**
- Cluster Onboarding screen
- Inventory → Clusters → View Workloads
- Runtime Protection → App Behavior → Network Graph (visual graph of pod-to-pod traffic + processes)
- Runtime Protection → App Behavior → List View (filter by cluster/namespace/workload; network/file/process tabs)
- Runtime Protection → Policies → Discovered tab (whitelist policies per workload)
- Zero Trust Journey progression (audit → changes available → stable → block)
- Runtime Protection → Policies → Hardening tab (framework-based policies, activate button)
- PSA configuration (Dry Run mode before enforcing)
- Monitors/Alerts → Alerts (policy violation logs with filter)
- CWPP Dashboard (after policies applied — comprehensive cluster view)
- Registry Scan → Onboard → Configure → View Results
- Container Image Inventory (Cloud Assets filter)
- Findings page → Container Image Findings dropdown

**On current page:**
- CWPP hero GIF (animated dashboard)
- Integrations CWPP image
- Agent-based CWPP image
- App Hardening image
- Network Microsegmentation image
- CWPP Reports image
- Self Guided Tour video (Jupyter Notebook protection demo)
- CWPP Product Tour video

**Gaps: Missing from page**
- No deep-dive screenshot walkthrough of App Behavior Graph view
- Zero Trust Journey progression not illustrated
- Registry scanning workflow not shown
- Container Image Findings triage workflow not shown

---

### AccuKnox Differentiators (CWPP)

| Differentiator | Basis |
|---|---|
| Inline mitigation — stops attacks pre-execution | KubeArmor uses BPF-LSM to prevent at syscall level |
| Zero false positives | Policy-based allow list — anything not in policy is blocked |
| eBPF without kernel modifications | Modern protection without kernel source changes |
| Reduced alert fatigue | No noise from post-exploit detection — inline stops it |
| Open-source KubeArmor (CNCF) | Transparent, community-validated security |
| CNI-agnostic microsegmentation | Works with any Container Network Interface |
| App Behavior auto-discovery | No manual policy writing — behavioral learning generates policies |
| Multi-environment support | K8s + VM + BareMetal + IoT/Edge in one platform |
| NIST/Gartner-aligned Zero Trust | Documented alignment with NIST ZT guidelines and Gartner recommendations |
| Self-Guided Tour available | Immediate value demonstration without sales call |

---

### Integrations (CWPP)

**Container Runtimes:**
- Docker, Containerd, CRIO, Podman

**Container Registries:**
- ECR (AWS), ACR (Azure), GCR/Artifact Registry (GCP)
- Harbor, generic registries
- Filter by: Regex, Update Date, Pull Date

**Orchestration:**
- Kubernetes (all major distributions)
- ECS (containers on VM)

**Notification / Alerting:**
- Slack
- Email
- Webhooks (generic)
- PagerDuty

**Ticketing:**
- Jira, ServiceNow, Freshservice, ConnectWise

**SIEM:**
- Splunk, ELK

**Policy / GitOps:**
- CLI (knoxctl)
- AccuKnox Control Plane UI
- GitOps workflows

---

### Onboarding (CWPP)

**Agent-Based Onboarding (from Playbook):**
1. Settings → Manage Cluster → "Onboard Now"
2. Name the cluster
3. Install agents via on-screen commands (KubeArmor DaemonSet)
4. Inventory → Clusters → verify cluster appears
5. Click "View Workloads" to see pods/containers
6. Runtime Protection → App Behavior → review network graph and list view
7. Runtime Protection → Policies → Discovered tab — review auto-discovered behavioral policies
8. Start Zero Trust Journey: audit mode → wait for stable → enforce block mode

**Registry Scanning Onboarding:**
1. Settings → Integrations → Registry tab
2. Click "Add Registry"
3. Input Name, Description, Registry Type
4. Provide Auth Credentials
5. Optionally configure: images to scan (regex/update date/pull date), scan schedule
6. Test Connection → Save
7. Issues → Registry Scan to view results

---

### Important Links & Resources (CWPP)

| Resource | URL |
|---|---|
| CWPP Overview | https://help.accuknox.com/overview/what-is-cwpp/ |
| CWPP Use Cases | https://help.accuknox.com/use-cases/ |
| CWPP Security Use Cases | https://help.accuknox.com/use-cases/ |
| Network Segmentation | https://help.accuknox.com/use-cases/cards/Network-Segmentation/ |
| App Behavior | https://help.accuknox.com/saas/app-behavior/ |
| Zero Trust Use Case | https://help.accuknox.com/use-cases/zero-trust/ |
| CNAPP Security Overview | https://help.accuknox.com/use-cases/cnapp-security-overview/ |
| KubeArmor Differentiation | https://docs.kubearmor.io/kubearmor/quick-links/differentiation |
| CWPP eBook | https://accuknox.com/ebooks/accuknox-cloud-workload-protection-platform-cwpp-an-inside-look |
| CrushFTP CVE Demo Video | https://www.youtube.com/watch?v=3uhBXc71-U0 |
| Enterprise ZT Automation Video | https://www.youtube.com/watch?v=lxq5sLNFj9w |
| CWPP Blog | https://accuknox.com/blog/role-of-cwpp-in-modern-cloud-security |
| CWPP Playbook | https://help.accuknox.com (internal reference) |

---

## 5. Cross-Cutting Gaps & Recommendations

### Gaps Across All Four Pages

| Gap Category | ASPM | CSPM | K8s/KSPM | CWPP |
|---|---|---|---|---|
| Quantified pain point statistics | ❌ | Partial | Has 2 stats | ❌ |
| Interactive product tour / self-guided demo | ❌ | ❌ | ❌ | ✅ (video) |
| Onboarding walkthrough on page | Partial | ❌ | ❌ | Partial |
| Competitor comparison table | ❌ | ✅ (links only) | ❌ | ❌ |
| Compliance framework coverage table | ❌ | Partial | ❌ | ❌ |
| Architecture/flow diagrams | 1 image | 2 images | 2 images | 1 GIF |
| Pricing model explanation | CTA only | CTA only | CTA only | CTA only |
| Integration list (named tools) | Logos only | Partial | Not on page | Not on page |
| Onboarding prerequisites checklist | ❌ | ❌ | ❌ | ❌ |
| Case study / customer quote specific to module | ❌ | 1 quote | ❌ | 1 quote |
| AI/ML Security angle | ❌ | Not on page | ❌ | ❌ |

### Recommendations Per Page

#### ASPM
- Add a **"Before/After" noise reduction visual** — 10,000 findings → 5 actionable with EPSS + runtime context
- Surface **secret scanning** prominently — it's in the help docs but invisible on the page
- Add **named integration list** for SAST/DAST/SCA/IaC tools (not just logos)
- Add an **interactive Storylane demo** (already built: secrets in container images, secrets in ConfigMaps)
- Include a **CI/CD pipeline architecture diagram** showing where each scan type plugs in
- Add a **"Getting Started in 4 Steps"** section with Label/Token → Pipeline integration → Findings → Triage

#### CSPM
- Add **Toxic Combination Analysis** as a standalone feature section with a visual
- Surface **AI/Bedrock Governance** — this is a differentiator no competitor has prominently
- Add a **CDR section** with sub-minute remediation metrics (<60s, <90s)
- Add a **compliance coverage table** (framework + control count)
- Replace the generic competitor comparison links with a **feature comparison matrix**
- Add **AskADA GenAI Copilot** section with example (ask → get Terraform fix)
- Include the **onboarding workflow 6-step visual** from the POC doc

#### Kubernetes / KSPM
- Add a **KSPM vs CWPP explainer** — many buyers don't know the difference
- Surface **KIEM** as a standalone capability section with a visual
- Add **Zero Trust Journey visual** (audit → stable → block)
- Include an **attack surface map** specific to Kubernetes
- Add a **"Supported Distributions" section** (EKS, AKS, GKE, RKE, on-prem, edge)
- Add **K8TLS** as a highlight (currently just a link, no explanation)
- Add **nano segmentation** explanation — it's in the POC but not on the page
- Add **GitOps policy management** angle for DevOps/platform teams

#### CWPP
- Add **Registry Scanning** as a prominent feature section — currently buried in playbook
- Surface **container image vulnerability** findings with triage workflow
- Add a **Zero Trust Journey animation or step-by-step** section
- Add **IoT/Edge workload support** — ARM/x86 mentioned in POC but not on page
- Add **"Supported Environments" table** (K8s, VMs, BareMetal, IoT/Edge, Docker/Containerd/CRIO/Podman)
- Create a **standalone inline mitigation vs post-attack comparison** diagram (already in FAQ with image)

### Common Diagrams Needed Across All Four Pages
1. **AccuKnox CNAPP Architecture** showing how ASPM + CSPM + KSPM + CWPP fit together
2. **Zero Trust Code-to-Cloud Flow** — each module's role in the overall security lifecycle
3. **Deployment Options Comparison** — SaaS vs. On-Prem vs. Air-Gapped (relevant to all four)
4. **Compliance Coverage Master Table** — one table showing all frameworks across all modules

---

*Document compiled: May 2026*
*Sources: Live web scrape + PDF extraction + Help docs review*
