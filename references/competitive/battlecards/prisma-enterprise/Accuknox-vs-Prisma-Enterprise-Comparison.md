---
title: "AccuKnox vs Prisma Cloud Enterprise Edition"
subtitle: "AccuKnox vs Prisma Cloud Enterprise Edition: CNAPP & Cloud Security Platform Comparison"
slug: accuknox-vs-prisma
url: https://accuknox.com/comparisons/accuknox-vs-prisma
archetype: head-to-head
category: cnapp
competitors:
  - "Palo Alto Networks Prisma Cloud Enterprise Edition"
excerpt: "Compare AccuKnox and Prisma Cloud Enterprise Edition across ASPM, CSPM, KSPM, CWPP, DSPM and AI security. AccuKnox runs the full platform in your cloud, on-prem or air-gapped. It also ships native SAST, DAST and LLM security, which Prisma Cloud Enterprise Edition does not include."
checked: 2026-09-30
---

# AccuKnox vs Prisma Cloud Enterprise Edition

**AccuKnox vs Prisma Cloud Enterprise Edition: CNAPP & Cloud Security Platform Comparison**

Compare AccuKnox and Prisma Cloud Enterprise Edition across ASPM, CSPM, KSPM, CWPP, DSPM and AI security. AccuKnox runs the full platform in your cloud, on-prem or air-gapped. It also ships native SAST, DAST and LLM security, which Prisma Cloud Enterprise Edition does not include [[3]](https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce) [[24]](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion) [[14]](https://docs.prismacloud.io/content-collections/application-security/application-security) [[82]](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview).

*Compared with Prisma Cloud Enterprise Edition (SaaS), release 26.8.1. Compute Edition excluded [[94]](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2026/features-introduced-in-august-2026).*

## AccuKnox Leads on Deployment, Native AppSec and AI Security

### Deployment Models

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| SaaS (Regional / Sovereign) | Supported. SaaS in US, EU, India, Middle East [[1]](https://help.accuknox.com/faqs/general/) | Limited. 17 SaaS tenants incl. GovCloud, China [[2]](https://docs.prismacloud.io/content-collections/get-started/console-prerequisites) |
| Customer Cloud (BYOC) | Supported. Control plane in your AWS, Azure or GCP [[1]](https://help.accuknox.com/faqs/general/) | Not supported. SaaS only. PAN runs the console [[3]](https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce) |
| On-Prem / Private Cloud | Supported. Full control plane on-prem, all features but AskADA [[4]](https://help.accuknox.com/getting-started/deployment-models/) | Limited. Defenders on-prem. Control plane SaaS only [[5]](https://docs.prismacloud.io/content-collections/get-started/welcome-to-prisma-cloud) |
| Air-Gapped Deployment | Supported. ASPM, CSPM, CWPP, KSPM, GRC fully offline [[1]](https://help.accuknox.com/faqs/general/) | Not supported. Not in Enterprise Edition. Compute Edition only [[3]](https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce) |

### Application Security

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| SAST | Supported. Pipeline and IDE SAST, AI false-positive triage [[23]](https://help.accuknox.com/getting-started/3.4-release/) | Limited. No native scanner. Imports Veracode, SonarQube, SARIF [[24]](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion) |
| DAST | Supported. 4 scan types, incl. authenticated behind MFA [[25]](https://help.accuknox.com/how-to/dast-scan-types/) | Not supported. No DAST. WAAS is runtime protection [[14]](https://docs.prismacloud.io/content-collections/application-security/application-security) |
| Code Quality (Best Practices) | Supported. 2-engine SAST, 14 languages, SonarQube gates [[13]](https://help.accuknox.com/support-matrix/sast-support-matrix/) | Limited. No code quality scanning documented [[14]](https://docs.prismacloud.io/content-collections/application-security/application-security) |
| IaC Scanning | Supported. Terraform, CFN, ARM, Bicep, Helm, Ansible, CDK + 6 [[15]](https://help.accuknox.com/support-matrix/iac/) | Supported. Terraform, OpenTofu, CFN, ARM, Bicep, Helm, Ansible + 7 [[16]](https://docs.prismacloud.io/content-collections/application-security/supported-technologies) |
| Container Scanning | Supported. CI/CD, registry, in-cluster, deploy blocking [[17]](https://help.accuknox.com/use-cases/container-scan/) | Supported. Registry, CI, agentless and twistcli scans [[18]](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/registry-scanning) |
| Secrets (Repo / IaC) | Supported. Repos, pipelines, IaC, correlated in ASPM [[6]](https://help.accuknox.com/faqs/aspm/) | Supported. VCS and CI/CD scans, Git history, validation [[7]](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/secrets-scanning) |
| Secrets in K8s ConfigMaps | Supported. ConfigMaps and deployment manifests [[10]](https://help.accuknox.com/how-to/aspm-overview/) | Limited. Repo files only. No in-cluster ConfigMap scan [[7]](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/secrets-scanning) |
| SARIF Ingestion | Supported. Any tool: Checkmarx, JFrog, Gitleaks, Sonatype [[19]](https://help.accuknox.com/getting-started/sarif-findings/) | Supported. SARIF 2.0 and 2.1 via console or API [[20]](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sarif-ingestion) |
| Repo / CI/CD Integration | Supported. GitHub, GitLab, Bitbucket + 9 CI/CD platforms [[21]](https://help.accuknox.com/support-matrix/cicd-support-matrix/) | Supported. 5 VCS + Jenkins, Actions, CircleCI, Azure [[22]](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs) |

### Software Supply Chain

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| SCA | Supported. Dependency SCA with CVE and license checks [[11]](https://help.accuknox.com/getting-started/xbom-setup/) | Supported. SCA, license compliance, PR package fixes [[12]](https://docs.prismacloud.io/content-collections/application-security/visibility/sbom) |
| Generate & Ingest SBOMs | Supported. CycloneDX out, CycloneDX or SPDX in [[69]](https://help.accuknox.com/faqs/sbom/) | Limited. CycloneDX 1.4 export. Ingestion not documented [[70]](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/exporting-sboms) |
| Track Vulnerable Components | Supported. CVEs, licenses, outdated versions per component [[11]](https://help.accuknox.com/getting-started/xbom-setup/) | Supported. Packages with CVEs and top severity [[12]](https://docs.prismacloud.io/content-collections/application-security/visibility/sbom) |
| Continuous CVE Monitoring | Supported. Live NVD feed, daily EPSS and CISA KEV [[71]](https://help.accuknox.com/resources/vulnerability-database/) | Supported. Intelligence Stream, several updates daily [[45]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-security-components/intelligence-stream) |

### Cloud Security Posture

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| AWS | Supported. CSPM, CDR auto-fix, inventory, GovCloud [[26]](https://help.accuknox.com/use-cases/cloud/aws/) | Supported. CSPM, runtime security, DSPM [[27]](https://docs.prismacloud.io/content-collections/compliance/compliance-standards) |
| Azure | Supported. CSPM, org-level onboarding, CDR auto-fix [[28]](https://help.accuknox.com/how-to/azure-org-onboard/) | Supported. CSPM, runtime security, DSPM [[27]](https://docs.prismacloud.io/content-collections/compliance/compliance-standards) |
| GCP | Supported. CSPM, CDR auto-fix, CIS GCP benchmarks [[29]](https://help.accuknox.com/use-cases/cloud/gcp/) | Supported. CSPM, runtime security, DSPM [[27]](https://docs.prismacloud.io/content-collections/compliance/compliance-standards) |
| Multi-Cloud Asset Inventory | Supported. One inventory of accounts, assets, workloads [[30]](https://help.accuknox.com/use-cases/asset-inventory/) | Supported. AWS, Azure, GCP, OCI, Alibaba. 24h refresh SLA [[31]](https://docs.prismacloud.io/content-collections/cloud-and-software-inventory/asset-inventory) |
| Private Cloud (OpenShift / Nutanix) | Supported. OpenShift, Nutanix, VMware Tanzu enforcement [[32]](https://help.accuknox.com/support-matrix/private-cloud/) | Limited. OpenShift v4. Nutanix not listed [[33]](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/kubernetes/openshift) |
| Secrets in S3 / Filesystems | Supported. S3, filesystems, Hugging Face datasets [[8]](https://help.accuknox.com/integrations/github-actions-secret-scan/) | Limited. Host and image filesystems. S3 undocumented [[9]](https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/detect-secrets) |
| Public S3 Detection + Auto-Fix | Supported. CloudTrail detection, reverts bucket to private [[34]](https://help.accuknox.com/use-cases/cdr/) | Supported. Config policy plus CLI auto-remediation [[35]](https://docs.prismacloud.io/content-collections/governance/create-a-policy) |
| Real-Time Cloud Event Automation | Supported. Real-time CloudTrail alerts trigger remediation [[34]](https://help.accuknox.com/use-cases/cdr/) | Limited. Audit events alert only, can lag hours. No CLI auto-fix [[35]](https://docs.prismacloud.io/content-collections/governance/create-a-policy) |

### Workload & Kubernetes Runtime

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| Host Protection (VM, Bare Metal) | Supported. KubeArmor systemd mode on VMs, bare metal [[39]](https://help.accuknox.com/support-matrix/kubearmor-support-matrix/) | Supported. Host Defenders, Linux and Windows [[40]](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/defender-types) |
| Container & K8s Runtime | Supported. Process, file, network enforcement + microsegmentation [[41]](https://help.accuknox.com/use-cases/app-behavior/) | Supported. Learned models, Alert, Prevent, Block rules [[42]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers) |
| Preemptive / Inline Blocking | Supported. Kernel LSM stops a process before it runs [[43]](https://help.accuknox.com/faqs/runtime-security/) | Supported. Prevent effect stops a disallowed process [[42]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers) |
| eBPF / Kernel Enforcement | Supported. eBPF plus AppArmor, SELinux, BPF-LSM [[43]](https://help.accuknox.com/faqs/runtime-security/) | Not supported. User-space Defender. No eBPF in docs [[61]](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/host/host-defender-architecture) |
| Process Allow / Deny | Supported. Per-pod or per-host process policies [[41]](https://help.accuknox.com/use-cases/app-behavior/) | Supported. Allow and deny lists, Prevent or Block [[42]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers) |
| File Integrity Monitoring | Supported. Monitors and blocks critical path changes [[46]](https://help.accuknox.com/use-cases/vm-file-integrity/) | Supported. Host FIM. Container write Prevent by directory [[47]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-hosts) |
| Workload Anomaly Detection | Supported. Learns baseline, blocks deviations [[48]](https://help.accuknox.com/use-cases/zero-trust/) | Supported. 1h learning, 24h dry run, rule enforcement [[42]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers) |
| Fileless Malware Protection | Supported. Allow-list blocks unknown processes [[48]](https://help.accuknox.com/use-cases/zero-trust/) | Limited. [confirm from Prisma Cloud docs] |
| Continuous Image Scanning | Supported. Scheduled scans of running images [[44]](https://help.accuknox.com/how-to/in-cluster-image-scan-helm/) | Supported. Registry, CI, deployed images, several times daily [[45]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-security-components/intelligence-stream) |
| Trusted Registry Enforcement | Supported. KnoxGuard admission per cluster or namespace [[55]](https://help.accuknox.com/use-cases/admission-controller-knoxguard/) | Supported. Trusted Images, alert or block [[56]](https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/trusted-images) |
| K8s Misconfiguration | Supported. Findings with fix steps and Jira tickets [[49]](https://help.accuknox.com/use-cases/cluster-misconfiguration-scanning/) | Supported. CIS checks plus OPA admission rules [[50]](https://docs.prismacloud.io/content-collections/runtime-security/access-control/open-policy-agent) |
| K8s CIS Benchmarks | Supported. Scheduled Helm-installed CIS scanner [[51]](https://help.accuknox.com/how-to/cis-benchmarking/) | Supported. CIS K8s, EKS, AKS, GKE, OpenShift [[52]](https://docs.prismacloud.io/content-collections/runtime-security/compliance/visibility/cis-benchmarks) |

### Kubernetes Identity (KIEM)

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| KIEM (K8s Entitlements) | Supported. RBAC search, graph, 15 risk queries [[53]](https://help.accuknox.com/use-cases/kiem/) | Limited. CIEM is cloud IAM only. No K8s RBAC [[54]](https://docs.prismacloud.io/content-collections/administration/configure-iam-security/what-is-prisma-cloud-iam-security) |
| Service Account Inventory | Supported. Service accounts, roles, bindings per cluster [[53]](https://help.accuknox.com/use-cases/kiem/) | Not supported. No K8s identity inventory documented [[54]](https://docs.prismacloud.io/content-collections/administration/configure-iam-security/what-is-prisma-cloud-iam-security) |
| Over-Permission Detection | Supported. Flags principals with excess privileges [[53]](https://help.accuknox.com/use-cases/kiem/) | Not supported. Cloud IAM only. K8s RBAC not documented [[57]](https://docs.prismacloud.io/content-collections/administration/configure-iam-security) |
| Risky Bindings & Cluster-Admin | Supported. Flags roles that modify workloads or read secrets [[53]](https://help.accuknox.com/use-cases/kiem/) | Limited. Audit-event alerts. No binding analysis [[58]](https://docs.prismacloud.io/content-collections/runtime-security/audit/kubernetes-auditing) |
| Stale K8s Entitlements | Supported. Unused roles and orphan service accounts [[53]](https://help.accuknox.com/use-cases/kiem/) | Not supported. Cloud IAM only. K8s not documented [[54]](https://docs.prismacloud.io/content-collections/administration/configure-iam-security/what-is-prisma-cloud-iam-security) |

### API Security

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| North-South (NGINX Ingress) | Supported. NGINX Ingress connector feeds API inventory [[62]](https://help.accuknox.com/integrations/api-overview/) | Limited. WAAS per app. No NGINX ingress integration [[63]](https://docs.prismacloud.io/content-collections/runtime-security/waas/deploy-waas) |
| TLS Classification at Ingress | Supported. Inspects TLS, flags misconfigurations [[64]](https://help.accuknox.com/faqs/api-sec/) | Limited. Decrypts per endpoint. No TLS report [[65]](https://docs.prismacloud.io/content-collections/runtime-security/waas/deploy-waas/oob-containers) |
| Sensitive Data in APIs | Supported. Request and response data classification [[66]](https://help.accuknox.com/use-cases/api-security/) | Supported. Flags card, PII and session data [[67]](https://docs.prismacloud.io/content-collections/runtime-security/waas/waas-api-discovery) |
| Shadow API Detection | Supported. Traffic vs OpenAPI spec [[66]](https://help.accuknox.com/use-cases/api-security/) | Supported. Detects shadow APIs. OpenAPI import [[68]](https://docs.prismacloud.io/content-collections/cloud-and-software-inventory/api-endpoints-inventory) |
| Zombie API Detection | Supported. Zombie and orphan APIs vs spec [[66]](https://help.accuknox.com/use-cases/api-security/) | Limited. Last-seen dates only. No zombie detection [[67]](https://docs.prismacloud.io/content-collections/runtime-security/waas/waas-api-discovery) |

### Data Security (DSPM)

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| Data Discovery | Supported. S3, Blob, cloud and self-hosted DBs, Drive, Salesforce [[72]](https://help.accuknox.com/getting-started/dspm-overview/) | Supported. AWS, Azure, GCP, Snowflake, M365, file shares [[73]](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/supported-assets) |
| Data Classification | Supported. 283 classes, PII, PHI, PCI, secrets, 62 country packs [[72]](https://help.accuknox.com/getting-started/dspm-overview/) | Supported. Predefined and custom classifiers [[74]](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/use-cases) |
| Data Access Verification | Coming soon | Supported. Read, Write, List, Manage and public access map [[75]](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information) |
| Publicly Exposed Data | Supported. Flags public buckets, CDR makes them private [[34]](https://help.accuknox.com/use-cases/cdr/) | Supported. Public access flagged by risk rules [[75]](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information) |
| Data Policy Controls | Coming soon | Supported. Built-in and custom risk rules, DDR alerts [[76]](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/create-and-edit-custom-risks) |

### Compliance & Reporting

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| Compliance Frameworks | Supported. 33+ frameworks, 42 versions, ISO, NIST, PCI, SOC 2 [[77]](https://help.accuknox.com/support-matrix/compliance-matrix/) [[78]](https://help.accuknox.com/faqs/compliance/) [[36]](https://help.accuknox.com/use-cases/compliance/) | Supported. 60+ standards for AWS, plus 4 clouds, custom [[27]](https://docs.prismacloud.io/content-collections/compliance/compliance-standards) [[37]](https://docs.prismacloud.io/content-collections/compliance/custom-compliance-standard) |
| Compliance Reports | Supported. Audit-ready PDF, CSV, JSON [[78]](https://help.accuknox.com/faqs/compliance/) | Supported. One-time or recurring, emailed [[79]](https://docs.prismacloud.io/content-collections/compliance/new-compliance-report) |
| Findings Reporting | Supported. Deduplicated across CSPM, KSPM, ASPM, runtime [[1]](https://help.accuknox.com/faqs/general/) | Supported. Alert, compliance and Command Center reports [[38]](https://docs.prismacloud.io/content-collections/reports/prisma-cloud-reports) |
| Audit Trail | Supported. EventTrail logs who, when, result [[59]](https://help.accuknox.com/getting-started/audit-trail-logs/) | Supported. 120-day platform audit log [[60]](https://docs.prismacloud.io/content-collections/administration/view-audit-logs) |
| Findings Collaboration | Supported. Jira, ServiceNow, Zendesk + 2, PDF/CSV/JSON [[1]](https://help.accuknox.com/faqs/general/) | Supported. Jira, email, Slack, CSV, snooze [[80]](https://docs.prismacloud.io/content-collections/alerts/view-respond-to-prisma-cloud-alerts) |

### AI Security

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| LLM Red Teaming | Supported. Bedrock, Vertex AI, AI Foundry, Triton, vLLM [[81]](https://help.accuknox.com/use-cases/red-teaming/) | Not supported. Not in Enterprise Edition. Sold as Prisma AIRS [[82]](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview) |
| Prompt Firewall | Supported. Inline: blocks, masks or logs prompts and responses [[83]](https://help.accuknox.com/use-cases/prompt-firewall-overview/) | Not supported. Not in Enterprise Edition. Sold as Prisma AIRS [[82]](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview) |
| ML Model Scanning | Supported. Pickle, Keras H5, SavedModel, ONNX [[84]](https://help.accuknox.com/how-to/ml-static-scan/) | Not supported. Finds Hugging Face files. Scanning is AIRS [[85]](https://docs.prismacloud.io/content-collections/ai-security-posture-management/unmanaged-ai-models) |
| OWASP LLM Top 10 | Supported. v2025 mapped in AI-SPM and red teaming [[77]](https://help.accuknox.com/support-matrix/compliance-matrix/) | Limited. Posture findings mapped. No runtime control [[86]](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2024/features-introduced-in-december-2024) |
| AI/ML Runtime Sandboxing | Supported. ModelArmor sandboxes models and agents [[87]](https://help.accuknox.com/use-cases/modelarmor/) | Limited. Generic runtime defense. No AI sandbox [[42]](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers) |
| AI Model & Dataset Exposure | Supported. Detects public endpoints, makes them private [[88]](https://help.accuknox.com/faqs/ai-security/) | Limited. Detects exposure. No blocking [[89]](https://www.paloaltonetworks.com/blog/cloud-security/ai-spm/) |
| Unknown-Region Model Access | Supported. Alerts outside allowed regions [[34]](https://help.accuknox.com/use-cases/cdr/) | Limited. Generic UEBA location alerts [[90]](https://docs.prismacloud.io/content-collections/governance/anomaly-policies) |

### Integrations

| Parameter | AccuKnox | Prisma Cloud Enterprise Edition |
| --- | --- | --- |
| SIEM | Supported. Splunk, Sentinel, QRadar, Sumo Logic, rsyslog [[91]](https://help.accuknox.com/integrations/splunk/) | Supported. Splunk HEC, Security Lake, webhooks, SQS [[92]](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-splunk) |
| Bi-Directional Ticketing | Supported. Ticket closes finding, recurrence reopens it [[1]](https://help.accuknox.com/faqs/general/) | Limited. One-way push to Jira, ServiceNow [[93]](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow) |


## Why Customers Choose AccuKnox Over Prisma Cloud

### Better

AccuKnox secures code, cloud, Kubernetes, data and AI in one platform, mapped to 33+ compliance frameworks. Its runtime engine, KubeArmor, is a CNCF Sandbox project with 2 million+ downloads [[78]](https://help.accuknox.com/faqs/compliance/) [[1]](https://help.accuknox.com/faqs/general/).

### Faster

KubeArmor enforces policy inline at the kernel, so a disallowed process stops before it runs. At one of India's top 3 public sector banks, AccuKnox cut remediation time by 91% and false positives by 89% [[43]](https://help.accuknox.com/faqs/runtime-security/) [[96]](https://accuknox.com/wp-content/uploads/SBOM-Case-Study.pdf).

### Affordable

One AccuKnox platform includes SAST, DAST, DSPM and AI security. Prisma Cloud Enterprise Edition documents no native SAST or DAST, and Palo Alto Networks sells AI red teaming and prompt inspection separately as Prisma AIRS [[24]](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion) [[82]](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview).

## Every Cell Cites a Vendor Page

Prisma Cloud facts come from Prisma Cloud Enterprise Edition documentation at docs.prismacloud.io and from paloaltonetworks.com, read on 2026-09-30. AccuKnox facts come from help.accuknox.com and one published AccuKnox case study. A cell marked [confirm] had no public source when this was written. Palo Alto Networks offers Cortex Cloud as an upgrade for Prisma Cloud customers, and Cortex Cloud capabilities differ from this table.

| # | Source | # | Source | # | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | [AccuKnox Help, General](https://help.accuknox.com/faqs/general/) | 2 | [Prisma Cloud Enterprise Edition docs, console prerequisites](https://docs.prismacloud.io/content-collections/get-started/console-prerequisites) | 3 | [Prisma Cloud Enterprise Edition docs, pcee vs pcce](https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce) |
| 4 | [AccuKnox Help, Deployment models](https://help.accuknox.com/getting-started/deployment-models/) | 5 | [Prisma Cloud Enterprise Edition docs, welcome to prisma cloud](https://docs.prismacloud.io/content-collections/get-started/welcome-to-prisma-cloud) | 6 | [AccuKnox Help, Aspm](https://help.accuknox.com/faqs/aspm/) |
| 7 | [Prisma Cloud Enterprise Edition docs, secrets scanning](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/secrets-scanning) | 8 | [AccuKnox Help, Github actions secret scan](https://help.accuknox.com/integrations/github-actions-secret-scan/) | 9 | [Prisma Cloud Enterprise Edition docs, detect secrets](https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/detect-secrets) |
| 10 | [AccuKnox Help, Aspm overview](https://help.accuknox.com/how-to/aspm-overview/) | 11 | [AccuKnox Help, Xbom setup](https://help.accuknox.com/getting-started/xbom-setup/) | 12 | [Prisma Cloud Enterprise Edition docs, sbom](https://docs.prismacloud.io/content-collections/application-security/visibility/sbom) |
| 13 | [AccuKnox Help, Sast support matrix](https://help.accuknox.com/support-matrix/sast-support-matrix/) | 14 | [Prisma Cloud Enterprise Edition docs, application security](https://docs.prismacloud.io/content-collections/application-security/application-security) | 15 | [AccuKnox Help, Iac](https://help.accuknox.com/support-matrix/iac/) |
| 16 | [Prisma Cloud Enterprise Edition docs, supported technologies](https://docs.prismacloud.io/content-collections/application-security/supported-technologies) | 17 | [AccuKnox Help, Container scan](https://help.accuknox.com/use-cases/container-scan/) | 18 | [Prisma Cloud Enterprise Edition docs, registry scanning](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/registry-scanning) |
| 19 | [AccuKnox Help, Sarif findings](https://help.accuknox.com/getting-started/sarif-findings/) | 20 | [Prisma Cloud Enterprise Edition docs, sarif ingestion](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sarif-ingestion) | 21 | [AccuKnox Help, Cicd support matrix](https://help.accuknox.com/support-matrix/cicd-support-matrix/) |
| 22 | [Prisma Cloud Enterprise Edition docs, ci cd runs](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs) | 23 | [AccuKnox Help, 3.4 release](https://help.accuknox.com/getting-started/3.4-release/) | 24 | [Prisma Cloud Enterprise Edition docs, third party ingestion](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion) |
| 25 | [AccuKnox Help, Dast scan types](https://help.accuknox.com/how-to/dast-scan-types/) | 26 | [AccuKnox Help, Aws](https://help.accuknox.com/use-cases/cloud/aws/) | 27 | [Prisma Cloud Enterprise Edition docs, compliance standards](https://docs.prismacloud.io/content-collections/compliance/compliance-standards) |
| 28 | [AccuKnox Help, Azure org onboard](https://help.accuknox.com/how-to/azure-org-onboard/) | 29 | [AccuKnox Help, Gcp](https://help.accuknox.com/use-cases/cloud/gcp/) | 30 | [AccuKnox Help, Asset inventory](https://help.accuknox.com/use-cases/asset-inventory/) |
| 31 | [Prisma Cloud Enterprise Edition docs, asset inventory](https://docs.prismacloud.io/content-collections/cloud-and-software-inventory/asset-inventory) | 32 | [AccuKnox Help, Private cloud](https://help.accuknox.com/support-matrix/private-cloud/) | 33 | [Prisma Cloud Enterprise Edition docs, openshift](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/kubernetes/openshift) |
| 34 | [AccuKnox Help, Cdr](https://help.accuknox.com/use-cases/cdr/) | 35 | [Prisma Cloud Enterprise Edition docs, create a policy](https://docs.prismacloud.io/content-collections/governance/create-a-policy) | 36 | [AccuKnox Help, Compliance](https://help.accuknox.com/use-cases/compliance/) |
| 37 | [Prisma Cloud Enterprise Edition docs, custom compliance standard](https://docs.prismacloud.io/content-collections/compliance/custom-compliance-standard) | 38 | [Prisma Cloud Enterprise Edition docs, prisma cloud reports](https://docs.prismacloud.io/content-collections/reports/prisma-cloud-reports) | 39 | [AccuKnox Help, Kubearmor support matrix](https://help.accuknox.com/support-matrix/kubearmor-support-matrix/) |
| 40 | [Prisma Cloud Enterprise Edition docs, defender types](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/defender-types) | 41 | [AccuKnox Help, App behavior](https://help.accuknox.com/use-cases/app-behavior/) | 42 | [Prisma Cloud Enterprise Edition docs, runtime defense containers](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-containers) |
| 43 | [AccuKnox Help, Runtime security](https://help.accuknox.com/faqs/runtime-security/) | 44 | [AccuKnox Help, In cluster image scan helm](https://help.accuknox.com/how-to/in-cluster-image-scan-helm/) | 45 | [Prisma Cloud Enterprise Edition docs, intelligence stream](https://docs.prismacloud.io/content-collections/runtime-security/runtime-security-components/intelligence-stream) |
| 46 | [AccuKnox Help, Vm file integrity](https://help.accuknox.com/use-cases/vm-file-integrity/) | 47 | [Prisma Cloud Enterprise Edition docs, runtime defense hosts](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-hosts) | 48 | [AccuKnox Help, Zero trust](https://help.accuknox.com/use-cases/zero-trust/) |
| 49 | [AccuKnox Help, Cluster misconfiguration scanning](https://help.accuknox.com/use-cases/cluster-misconfiguration-scanning/) | 50 | [Prisma Cloud Enterprise Edition docs, open policy agent](https://docs.prismacloud.io/content-collections/runtime-security/access-control/open-policy-agent) | 51 | [AccuKnox Help, Cis benchmarking](https://help.accuknox.com/how-to/cis-benchmarking/) |
| 52 | [Prisma Cloud Enterprise Edition docs, cis benchmarks](https://docs.prismacloud.io/content-collections/runtime-security/compliance/visibility/cis-benchmarks) | 53 | [AccuKnox Help, Kiem](https://help.accuknox.com/use-cases/kiem/) | 54 | [Prisma Cloud Enterprise Edition docs, what is prisma cloud iam security](https://docs.prismacloud.io/content-collections/administration/configure-iam-security/what-is-prisma-cloud-iam-security) |
| 55 | [AccuKnox Help, Admission controller knoxguard](https://help.accuknox.com/use-cases/admission-controller-knoxguard/) | 56 | [Prisma Cloud Enterprise Edition docs, trusted images](https://docs.prismacloud.io/content-collections/runtime-security/compliance/operations/trusted-images) | 57 | [Prisma Cloud Enterprise Edition docs, configure iam security](https://docs.prismacloud.io/content-collections/administration/configure-iam-security) |
| 58 | [Prisma Cloud Enterprise Edition docs, kubernetes auditing](https://docs.prismacloud.io/content-collections/runtime-security/audit/kubernetes-auditing) | 59 | [AccuKnox Help, Audit trail logs](https://help.accuknox.com/getting-started/audit-trail-logs/) | 60 | [Prisma Cloud Enterprise Edition docs, view audit logs](https://docs.prismacloud.io/content-collections/administration/view-audit-logs) |
| 61 | [Prisma Cloud Enterprise Edition docs, host defender architecture](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/host/host-defender-architecture) | 62 | [AccuKnox Help, Api overview](https://help.accuknox.com/integrations/api-overview/) | 63 | [Prisma Cloud Enterprise Edition docs, deploy waas](https://docs.prismacloud.io/content-collections/runtime-security/waas/deploy-waas) |
| 64 | [AccuKnox Help, Api sec](https://help.accuknox.com/faqs/api-sec/) | 65 | [Prisma Cloud Enterprise Edition docs, oob containers](https://docs.prismacloud.io/content-collections/runtime-security/waas/deploy-waas/oob-containers) | 66 | [AccuKnox Help, Api security](https://help.accuknox.com/use-cases/api-security/) |
| 67 | [Prisma Cloud Enterprise Edition docs, waas api discovery](https://docs.prismacloud.io/content-collections/runtime-security/waas/waas-api-discovery) | 68 | [Prisma Cloud Enterprise Edition docs, api endpoints inventory](https://docs.prismacloud.io/content-collections/cloud-and-software-inventory/api-endpoints-inventory) | 69 | [AccuKnox Help, Sbom](https://help.accuknox.com/faqs/sbom/) |
| 70 | [Prisma Cloud Enterprise Edition docs, exporting sboms](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/exporting-sboms) | 71 | [AccuKnox Help, Vulnerability database](https://help.accuknox.com/resources/vulnerability-database/) | 72 | [AccuKnox Help, Dspm overview](https://help.accuknox.com/getting-started/dspm-overview/) |
| 73 | [Prisma Cloud Enterprise Edition docs, supported assets](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/supported-assets) | 74 | [Prisma Cloud Enterprise Edition docs, use cases](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/use-cases) | 75 | [Prisma Cloud Enterprise Edition docs, explore data asset access information](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information) |
| 76 | [Prisma Cloud Enterprise Edition docs, create and edit custom risks](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/create-and-edit-custom-risks) | 77 | [AccuKnox Help, Compliance matrix](https://help.accuknox.com/support-matrix/compliance-matrix/) | 78 | [AccuKnox Help, Compliance](https://help.accuknox.com/faqs/compliance/) |
| 79 | [Prisma Cloud Enterprise Edition docs, new compliance report](https://docs.prismacloud.io/content-collections/compliance/new-compliance-report) | 80 | [Prisma Cloud Enterprise Edition docs, view respond to prisma cloud alerts](https://docs.prismacloud.io/content-collections/alerts/view-respond-to-prisma-cloud-alerts) | 81 | [AccuKnox Help, Red teaming](https://help.accuknox.com/use-cases/red-teaming/) |
| 82 | [Prisma Cloud Enterprise Edition docs, aispmoverview](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview) | 83 | [AccuKnox Help, Prompt firewall overview](https://help.accuknox.com/use-cases/prompt-firewall-overview/) | 84 | [AccuKnox Help, Ml static scan](https://help.accuknox.com/how-to/ml-static-scan/) |
| 85 | [Prisma Cloud Enterprise Edition docs, unmanaged ai models](https://docs.prismacloud.io/content-collections/ai-security-posture-management/unmanaged-ai-models) | 86 | [Prisma Cloud Enterprise Edition docs, features introduced in december 2024](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2024/features-introduced-in-december-2024) | 87 | [AccuKnox Help, Modelarmor](https://help.accuknox.com/use-cases/modelarmor/) |
| 88 | [AccuKnox Help, Ai security](https://help.accuknox.com/faqs/ai-security/) | 89 | [Palo Alto Networks, ai spm](https://www.paloaltonetworks.com/blog/cloud-security/ai-spm/) | 90 | [Prisma Cloud Enterprise Edition docs, anomaly policies](https://docs.prismacloud.io/content-collections/governance/anomaly-policies) |
| 91 | [AccuKnox Help, Splunk](https://help.accuknox.com/integrations/splunk/) | 92 | [Prisma Cloud Enterprise Edition docs, integrate prisma cloud with splunk](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-splunk) | 93 | [Prisma Cloud Enterprise Edition docs, integrate prisma cloud with servicenow](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow) |
| 94 | [Prisma Cloud release notes, features introduced in August 2026 (26.8.1)](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2026/features-introduced-in-august-2026) | 95 | [Palo Alto Networks press release, Cortex Cloud launch (February 2025)](https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-introduces-cortex-cloud--the-future-of-real-time-cloud-security) | 96 | [AccuKnox case study, Top 3 Indian public sector bank operationalises SBOM air-gapped](https://accuknox.com/wp-content/uploads/SBOM-Case-Study.pdf) |
