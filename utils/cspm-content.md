# CSPM — Cloud Security Posture Management

---

## Definition

Cloud Security Posture Management (CSPM) is a security solution that continuously monitors and manages cloud infrastructure security risks. It identifies misconfigurations, enforces compliance with frameworks like SOC 2, PCI-DSS, and HIPAA, and provides visibility into potential risks across cloud accounts. AccuKnox CSPM is 100% agentless for public cloud environments, using cloud APIs to discover assets and configurations without installing agents in cloud accounts.

---

## Pain Points

- Cloud environments are dynamic — services spin up and down, permissions change, and configurations drift without security team awareness
- Accidental public exposure of data — S3 buckets, RDS instances, and EC2 machines left accessible to `0.0.0.0/0`
- Over-permissioned IAM roles — wildcard permissions (`*`), admin roles, or broad service permissions assigned to non-privileged workloads
- Root accounts with MFA disabled — flagged as Critical, often overlooked
- Stale access keys not rotated in more than 90 days — includes unused keys still active
- Shadow admins — IAM users or roles that can escalate to admin via policy chaining, invisible in standard IAM review
- Hardcoded secrets in Lambda environment variables, ECS task definitions, and SSM Parameter Store
- Unencrypted storage — S3 buckets without SSE-S3 or SSE-KMS, EBS volumes without encryption, RDS without encryption at rest or in transit (TLS disabled)
- Cross-account trust policies with overly permissive external IDs — allow lateral movement across accounts
- Unused IAM identities — service accounts with zero API calls in 30+ days still active and credentialed
- Configuration drift — infrastructure diverges from approved Terraform or CloudFormation templates without detection
- Isolated security findings obscure actual risk — a single misconfiguration looks low-risk but chains with others to create exploitable attack paths
- No visibility into AI/ML cloud assets — Amazon Bedrock models, inference endpoints, and agent configurations left unmonitored
- Bedrock APIs accessible without VPC endpoint or PrivateLink — externally exposed
- Cross-region AI inference calls outside approved data residency zones
- No unified view across AWS, Azure, and GCP — each cloud siloed in its own tool
- Compliance reporting is manual and periodic — no continuous compliance monitoring
- Ghost resources accumulating — orphaned EBS volumes, unattached EIPs, stale IAM users consuming cost and expanding attack surface

---

## Use Cases

### Asset Inventory & Visibility
- Auto-discover and categorize 50+ AWS asset types across all regions and accounts
- Ghost resource detection: orphaned EBS volumes, unattached Elastic IPs, stale IAM users
- Egress/Ingress mapping: flag ports open to `0.0.0.0/0` — SSH (22), RDP (3389), HTTP (80), HTTPS (443)
- Asset grouping by tag, account, region, and compliance scope for granular reporting
- Maintain automated asset inventory that reflects additions and removals after each scan
- Discover: Compute (EC2, VMs), Storage (S3, EBS, RDS), Network (VPCs, SGs, NACLs), IAM, Databases, AI/ML, Serverless (Lambda, Cloud Functions)

### Misconfiguration Detection
- Continuously scan cloud assets against 1500+ built-in policies
- Identify insecure configurations and deviations from security best practices
- Risk-rank findings by exploitability and blast radius — not just severity
- Detect: public S3 buckets, over-permissioned IAM roles, unencrypted databases, exposed services

### Toxic Combination Analysis
- Correlate isolated findings into exploitable attack chains — not raw alert counts
- Example chain 1: Public EC2 + Missing IMDSv2 + Overprivileged Instance Role = High-priority attack path
- Example chain 2: Unencrypted RDS + Public Subnet + Permissive Security Group = Data exfiltration risk
- Risk score based on exploitability AND blast radius — prioritizes what matters most

### IAM Hardening
- Detect root accounts with MFA disabled — flag as Critical immediately
- Flag access keys not rotated in more than 90 days, including unused keys
- Identify roles with `*`, Admin, or wildcard service permissions (Over-Privileged Roles)
- Detect shadow admins — IAM users/roles that can escalate to admin via policy chaining
- Flag unused identities — service accounts and IAM users with zero API calls in 30+ days
- Flag overly permissive cross-account trust policies and suspicious external IDs

### Public Exposure Detection
- S3 encryption: buckets missing SSE-S3/SSE-KMS — flag unencrypted or public objects
- RDS publicly accessible: instances with `publicly_accessible=true` or SGs open to `0.0.0.0/0`
- EBS volumes unencrypted and attached to running EC2 instances
- EC2 with public IPs assigned without business justification
- Endpoint exposure: services accessible from the internet without VPC endpoint

### Secrets & Data Discovery
- Scan Lambda environment variables for plaintext keys
- Scan ECS task definitions for embedded secrets
- Scan SSM Parameter Store for unencrypted sensitive values
- S3 access logging disabled — missing audit trail
- RDS audit logs, Lambda execution logs disabled

### Compliance & Drift Detection
- Map findings to 30+ compliance frameworks continuously
- Detect "console drift" — when infrastructure diverges from approved Terraform/CloudFormation
- Track who made the change, when, and from which IP (via CloudTrail correlation)
- Flag IaC templates with hardcoded credentials, open SGs, or missing encryption
- Export findings as annotated IaC diff for engineering team remediation

### AI / Bedrock Governance
- Discover active Amazon Bedrock models, inference endpoints, and agent configurations
- Validate CloudTrail logging for Bedrock API calls is enabled
- Detect over-permissive roles with `bedrock:*` or full `InvokeModel` access
- Confirm model input/output and artifact encryption via CMK / BYOK
- Flag cross-region inference calls outside approved data residency zones
- Detect Bedrock APIs accessible without VPC endpoint or PrivateLink

### CDR — Cloud Detection & Response
- S3 Auto-Remediation: exposed S3 bucket reverted to private within 60 seconds of event
- EC2 Public IP Removal: public IP detached within 90 seconds of policy violation
- Geo-Fencing Alert: critical alert fired within 30 seconds of access from denied region
- IAM rollback in under 2 minutes via CLI/Webhook → Lambda/serverless
- Auto-formatted Jira tickets created per critical finding (asset ID + severity pre-populated)
- Real-time Slack alerts on CDR event with full asset context
- PagerDuty on-call escalation for Critical CDR events with severity-filtered routing

### AskADA GenAI Copilot
- On-demand asset-specific Terraform fix snippets generated by AI
- Query: "Why is this finding critical?" → AskADA explains risk in plain language
- Query: "How do I fix this S3 misconfiguration?" → returns ready-to-apply Terraform snippet
- Query: "What are my top 5 IAM risks?" → returns prioritized IAM risk list with remediation

### CI/CD Integration
- Scan assets from SaaS, on-prem, and CI/CD model
- Prevent risky deployments before they happen using policy-as-code
- Block pipelines on critical cloud misconfigurations detected in IaC templates

---

## Features

### Agentless Cloud Scanning
| Feature | Detail |
|---|---|
| Deployment model | 100% API-based read — no data stored outside tenant boundary |
| Intrusion level | No kernel modules, no intrusive agents required |
| Coverage | AWS, Azure, GCP, Hybrid cloud |
| Event-driven scanning | Dynamic, continuous — not just scheduled batch scans |

### Asset Inventory
| Feature | Detail |
|---|---|
| Asset types | 50+ types: Compute, Storage, Network, IAM, Databases, AI/ML, Serverless |
| Discovery | Auto-discover across all regions and accounts |
| Tagging | Group by tag, account, region, compliance scope |
| Ghost detection | Orphaned EBS volumes, unattached EIPs, stale IAM users |

### Policy Engine
| Feature | Detail |
|---|---|
| Built-in policies | 1500+ controls mapped to CIS, NIST, SOC2, HIPAA, PCI-DSS |
| Custom policies | Define organization-specific guardrails |
| Policy-as-Code | YAML/JSON policies — prevent risky deployments before they happen |
| Auto-fix | Auto-remediation playbooks for common issues |

### Compliance Engine
| Framework | Control Count |
|---|---|
| CIS Benchmarks v2.0 | 200+ (EC2, S3, IAM, RDS, VPC, EKS) |
| NIST 800-53 Rev 5 | 110+ (federal controls, audit-ready export) |
| SOC 2 Type II | 64+ (continuous evidence collection) |
| HIPAA | 54+ (PHI encryption, access, audit trail) |
| PCI-DSS v4.0 | 80+ (cardholder data environment scoping) |
| ISO 27001 | 114+ (ISMS control validation) |
| AWS Well-Architected | 50+ (security pillar alignment) |
| GDPR | Included |
| FedRAMP | Included |
| Total frameworks | 30+ |

### Toxic Combination Analysis
| Feature | Detail |
|---|---|
| Attack path correlation | Chains isolated findings into exploitable attack paths |
| Risk scoring | Based on exploitability AND blast radius |
| Example chain | Public EC2 + Missing IMDSv2 + Overprivileged IAM Role |
| Prioritization | Filters noise — surfaces the paths that matter most |

### Drift Detection
| Feature | Detail |
|---|---|
| IaC alignment | Compares running infra to Terraform/CloudFormation baseline |
| CloudTrail correlation | Who changed it, when, from which IP |
| IaC diff export | Annotated IaC diff for engineering teams |
| Console drift | Flag manual changes that bypass approved IaC workflows |

### CDR (Cloud Detection & Response)
| Feature | Detail |
|---|---|
| S3 auto-remediation | Reverted to private in < 60 seconds |
| EC2 public IP removal | Detached in < 90 seconds |
| Geo-fencing | Alert within 30 seconds of access from denied region |
| IAM rollback | Via CLI/Webhook → Lambda in < 2 minutes |
| Remediation method | CLI / Webhook → Lambda / serverless functions |

### Reporting
| Feature | Detail |
|---|---|
| Scheduled reports | Automated PDF CSPM reports on a schedule |
| On-demand reports | Trigger report generation at any time |
| Executive summary | High-level posture report for stakeholders |
| Compliance export | Audit-ready exports per framework |

### AI Copilot (AskADA)
| Feature | Detail |
|---|---|
| Terraform fix generation | Asset-specific remediation code on demand |
| Risk explanation | Plain-language risk explanations per finding |
| Query interface | Natural language queries against your cloud posture |

---

## Dashboard & UI Flows

### POC Onboarding Workflow — 6 Steps
1. **Account Selection:** Choose AWS Organization Unit (OU) or standalone account; select deployment model (SaaS or On-Prem)
2. **IAM Provisioning:** Grant read-only role for discovery; contributor/write role for CDR auto-remediation
3. **Asset Tagging & Scope Setup:** Tag assets by team and type; select compliance frameworks
4. **Integration Setup:** Connect Slack, Jira, ServiceNow, or PagerDuty
5. **Automated Security Scan:** First scan runs; full asset inventory populated
6. **Ongoing Monitoring:** Continuous scanning, drift detection, CDR alerts, compliance scores

### Standard Navigation Paths
- Asset Inventory: Inventory → Cloud Assets → filter by type/region/account
- Misconfigurations: Issues → Cloud Misconfigurations → filter by severity/framework
- Compliance Dashboard: Compliance → select framework → view pass/fail breakdown
- Attack Path Analysis: Security Graph → view toxic combination chains
- CDR Events: Monitors/Alerts → CDR Events → view auto-remediation actions taken
- Reports: Reports → schedule or generate on-demand
- Integrations: Settings → Integrations → configure Jira/Slack/ServiceNow

### 2-Week POC Execution Plan
| Day | Activity |
|---|---|
| D1–D2 | Prerequisites finalization and scoping |
| D1–D2 | AccuKnox Control Plane connectivity |
| D3–D4 | Cloud account onboarding |
| D3–D4 | Jira and Slack integration setup |
| D5–D6 | Full asset inventory scan |
| D5–D7 | Baseline compliance scores (CIS, NIST, SOC2, HIPAA) |
| D7–D8 | Toxic combination analysis walkthrough |
| D8 | IAM and data security findings review |
| D8–D9 | Enable CDR write permissions for testing |
| D9–D10 | CDR simulation: S3 public exposure |
| D10–D11 | CDR simulation: EC2 public IP + Geo-Fencing |
| D11–D12 | Bedrock/AI asset audit |
| D12–D14 | Executive report generation |

### POC Success Criteria Matrix
| Category | Use Case | Success Criteria |
|---|---|---|
| Visibility | Asset Discovery | 100% of AWS assets discovered across all regions and accounts |
| CSPM | Misconfiguration Scan | Top-20 critical misconfigs identified and risk-ranked on Day 3 |
| CSPM | Toxic Combinations | At least 1 chained attack path identified per account |
| Compliance | CIS + NIST 800-53 | Accurate pass/fail posture report generated for both frameworks |
| Compliance | SOC2 / HIPAA | Compliance scores generated with control mapping |
| CDR | S3 Auto-Remediation | Exposed S3 bucket reverted to private within 60 seconds |
| CDR | EC2 Public IP Removal | Public IP detached within 90 seconds of policy violation |
| CDR | Geo-Fencing Alert | Critical alert fired within 30 seconds of access from denied region |
| IAM | Identity Hardening | MFA-disabled root accounts, stale keys, over-privileged roles found |
| AI | Bedrock Audit | Bedrock models discovered, logging validated, IAM scope reviewed |
| Integration | Jira Ticketing | Auto-formatted Jira ticket created per critical finding |
| Integration | Slack Alerts | Real-time Slack alert fires on CDR event with asset context |

---

## AccuKnox Differentiators

| Differentiator | Detail |
|---|---|
| Toxic Combination analysis | Chains isolated findings into exploitable attack paths — not just raw alert counts |
| CDR with sub-minute auto-remediation | S3 reverted in <60s, EC2 IP removed in <90s, IAM rollback in <2min |
| AI/LLM governance built in | Bedrock model discovery, audit log validation, IAM scope, data residency checks |
| AskADA GenAI Copilot | On-demand Terraform fix snippets and natural-language risk explanations |
| 1500+ built-in policies | Broadest policy library in class |
| Zero Trust architecture support | Least-privilege enforcement and IAM behavioral insights |
| Deep Kubernetes visibility | KSPM integrated alongside cloud CSPM in same platform |
| Agentless + agent-based flexibility | No forced trade-off between deployment model and capabilities |
| Open-source integration | OpenSCAP, KubeArmor — transparent and extensible |
| CloudTrail-correlated drift detection | Who changed infra, when, from which IP — not just what changed |
| 100% API-based — no data stored outside tenant | Full data residency compliance |

---

## Comparisons

| Competitor | AccuKnox vs |
|---|---|
| Wiz | https://accuknox.com/comparisons/accuknox-vs-wiz |
| AquaSec | https://accuknox.com/comparisons/accuknox-vs-aquasec |
| Calico Cloud | https://accuknox.com/comparisons/accuknox-vs-calicocloud |
| Palo Alto / Prisma | https://accuknox.com/comparisons/accuknox-vs-prisma |
| Orca Security | https://accuknox.com/comparisons/accuknox-vs-orca-security |
| Checkpoint | https://accuknox.com/comparisons/accuknox-vs-checkpoint |
| PingSafe | https://accuknox.com/comparisons/accuknox-vs-pingsafe |
| CrowdStrike | https://accuknox.com/comparisons/accuknox-vs-crowdstrike |

---

## Integrations

### Cloud Providers
- AWS (standalone account or AWS Organization Unit)
- Azure
- GCP
- Hybrid cloud environments

### Data Sources (AWS)
- CloudTrail
- AWS Config
- VPC Flow Logs
- Amazon GuardDuty findings
- Amazon Bedrock audit logs

### Ticketing / ITSM
- Jira (auto-formatted tickets — asset ID + severity pre-populated)
- ServiceNow (SNOW table API, dynamic incident template)
- Freshservice
- ConnectWise

### Alerting / Notification
- Slack (real-time, severity-filtered routing)
- Microsoft Teams (webhook URL)
- PagerDuty (on-call escalation for Critical CDR events)
- Email (SMTP daily digest + individual finding alerts)

### Automation / Response
- AWS Lambda / serverless (auto-remediation)
- Webhooks (generic endpoint — for CI/CD pipeline or internal tooling)

### SIEM
- Splunk (log forwarding endpoint)
- ELK / Elasticsearch (log forwarding endpoint)

---

## Onboarding

### Prerequisites — AWS
- Deployment model: SaaS (simplest, fastest) or On-Prem (air-gapped/self-managed)
- Account type: AWS Organization Unit (OU) or standalone AWS account — both supported
- Cloud resources: account must contain EC2, RDS/databases, EKS cluster (optional), AI assets (Bedrock — optional)
- IAM permissions: read-only role for discovery phase (`ReadOnlyAccess` + `SecurityAudit`)
- For CDR write permissions: `s3:PutBucketPublicAccessBlock`, `ec2:TerminateInstances`, `cloudtrail:StartLogging`
- For AI/Bedrock: additional permissions for Bedrock model discovery and audit log access

### Prerequisites — Azure
- Service principal with read delegated permissions for cloud asset discovery and posture checks

### Prerequisites — GCP
- Service account with JSON private key; read-only permissions for cloud asset discovery

### Optional Integrations Setup
- Jira: project URL + API credentials
- Slack: workspace + channel name
- Teams: webhook URL
- ServiceNow: instance URL + credentials
- SIEM: Splunk or ELK endpoint for log forwarding

### Onboarding Steps
1. Select deployment model (SaaS or On-Prem)
2. Connect cloud accounts (AWS standalone or OU; Azure; GCP)
3. Validate IAM permissions for discovery
4. AccuKnox provisions read-only access — no data stored outside tenant boundary
5. Initial asset discovery scan runs automatically
6. Asset inventory and compliance dashboards populate
7. Configure ticketing, alerting, and SIEM integrations (optional)
8. Enable CDR write permissions for auto-remediation testing (optional)
9. Schedule weekly triaging sessions with AccuKnox team (POC/onboarding)
10. Review weekly: which findings to prioritize, what threat vectors exist, top cloud misconfigurations

---

## Pricing

Pricing is based on value delivered. Key factors:
- Number of cloud assets
- Number of cloud accounts/regions
- Number of workloads and nodes
- Modules selected: CSPM-only, or full CNAPP bundle (CSPM + KSPM + CWPP + ASPM)

Custom quote: https://accuknox.com/pricing

---

## Diagrams

### 1. Cloud Account Onboarding Workflow (6-Step)
- Step 1: Select Accounts → Step 2: Grant IAM Permissions → Step 3: Tag Resources → Step 4: Connect Apps (Slack/Jira) → Step 5: Automated Cloud Security Scan → Step 6: Continuous Monitoring

### 2. CSPM Data Flow
- AWS Accounts (Org Unit or Standalone) → CloudTrail + Config + VPC Flow Logs + GuardDuty → AccuKnox Control Plane (1500+ Policies + CSPM + CDR + AI Copilot) → Jira + Slack + ServiceNow + Auto-Remediation + Reports

### 3. Toxic Combination Analysis Visual
- Node 1: Public EC2 instance → Node 2: Missing IMDSv2 → Node 3: Overprivileged Instance Role → Combined Risk Score: CRITICAL — Attack Path visualized as linked chain with blast radius

### 4. Compliance Coverage Matrix
- Y-axis: Compliance frameworks (CIS, NIST, SOC2, HIPAA, PCI-DSS, ISO 27001, FedRAMP)
- X-axis: Cloud services (EC2, S3, IAM, RDS, VPC, EKS, Lambda, Bedrock)
- Cell: Pass/Fail control count per service per framework

### 5. CDR Auto-Remediation Timeline
- T=0: S3 bucket made public → T+5s: CloudTrail event detected → T+15s: CDR rule triggered → T+60s: S3 bucket reverted to private → T+65s: Slack alert sent + Jira ticket created

### 6. AI/Bedrock Governance Architecture
- AccuKnox scanning Bedrock models → checks VPC endpoint status → validates CloudTrail logging → reviews IAM role permissions (`bedrock:*` detection) → checks data residency for cross-region calls → reports to CSPM dashboard

### 7. Multi-Cloud Unified Dashboard
- Single pane: AWS + Azure + GCP asset counts, risk scores per cloud, compliance posture per framework, CDR event log

---

## Important Links & Resources

| Resource | URL |
|---|---|
| AWS Onboarding | https://help.accuknox.com/how-to/aws-onboarding/ |
| AWS Org Onboarding | https://help.accuknox.com/how-to/aws-org-onboard/ |
| Azure Onboarding | https://help.accuknox.com/how-to/azure-onboarding/ |
| Azure Org Onboarding | https://help.accuknox.com/how-to/azure-org-onboard/ |
| CSPM Prerequisites (AWS) | https://help.accuknox.com/getting-started/cspm-prereq-aws/ |
| CNAPP Security Overview Use Cases | https://help.accuknox.com/use-cases/cnapp-security-overview/ |
| CIS Benchmarking | https://help.accuknox.com/how-to/cis-benchmarking/ |
| Cloud Offboarding | https://help.accuknox.com/how-to/cloud-offboarding/ |
| CSPM Report PDF (Sample) | https://help.accuknox.com/resources/assets/CSPM_Report.pdf |
| GCP Security Cheatsheet | https://accuknox.com/cheatsheets/gcp-security |
| CSPM eBook | https://www.accuknox.com/wp-content/uploads/CSPM_eBook.pdf |
| Asset Inventory Video | https://www.youtube.com/watch?v=7K09AW4aH4c |
| AI-Powered Cloud Security Video | https://www.youtube.com/watch?v=hKNTGE85ATI |
| AIML AWS Onboarding | https://help.accuknox.com/how-to/aiml-aws-onboard/ |
| AIML Azure Onboarding | https://help.accuknox.com/how-to/aiml-azure-onboard/ |
| AIML GCP Onboarding | https://help.accuknox.com/how-to/aiml-gcp-onboard/ |
| AIML Overview | https://help.accuknox.com/how-to/aiml-overview/ |
| Pricing | https://accuknox.com/pricing |
