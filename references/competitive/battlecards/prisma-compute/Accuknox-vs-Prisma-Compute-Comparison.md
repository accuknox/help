---
title: "AccuKnox vs Prisma Cloud Compute Edition"
subtitle: "Workloads On-Prem With Prisma. Everything On-Prem With AccuKnox."
slug: accuknox-vs-prisma-compute
url: https://accuknox.com/comparisons/accuknox-vs-prisma-compute
archetype: head-to-head
category: cnapp
competitors:
  - "Palo Alto Networks Prisma Cloud Compute Edition"
excerpt: "Prisma Cloud Compute Edition is the self-hosted edition of Prisma Cloud. It includes the Cloud Workload Protection Platform (CWPP) module only. Cloud posture sits in Prisma Cloud Enterprise Edition, which Palo Alto Networks runs as SaaS. AccuKnox installs its control plane on your servers or in an air-gapped network. It runs every feature there except AI CoPilot (AskADA)."
checked: 2026-10-06
---

# AccuKnox vs Prisma Cloud Compute Edition

**Workloads On-Prem With Prisma. Everything On-Prem With AccuKnox.**

Prisma Cloud Compute Edition is the self-hosted edition of Prisma Cloud. It includes the Cloud Workload Protection Platform (CWPP) module only. Cloud posture sits in Prisma Cloud Enterprise Edition, which Palo Alto Networks runs as SaaS. AccuKnox installs its control plane on your servers or in an air-gapped network. It runs every feature there except AI CoPilot (AskADA) [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) [[3]](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce) [[1]](https://help.accuknox.com/resources/deployment/).

*Compared with Prisma Cloud Compute Edition (self-hosted), per its administrator guide read on 2026-10-06 [[57]](https://docs.prismacloud.io/admin-guide/welcome/getting-started).*

## AccuKnox Runs Every Module On-Prem, Compute Edition Runs One

### Deployment and Data Residency

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| Modules Available On-Prem | Supported. All features run on-prem except AI CoPilot (AskADA) [[1]](https://help.accuknox.com/resources/deployment/) | Limited. CWPP module only. CSPM is in Enterprise Edition (SaaS) [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| On-Prem Control Plane | Supported. Native install on your servers, VMs or bare metal [[1]](https://help.accuknox.com/resources/deployment/) | Supported. Self-hosted Console on any container host, Kubernetes or OpenShift [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| Air-Gapped Operation | Supported. Isolated network with no call-home, images staged in own registry [[1]](https://help.accuknox.com/resources/deployment/) | Supported. Listed for air-gapped sites, with manual threat feed loading [[3]](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce) |
| Data Residency and Telemetry | Supported. No data egress on-prem. Control plane pulls image and chart updates [[1]](https://help.accuknox.com/resources/deployment/) | Supported. Data stays on your Console. Anonymous telemetry on by default, can be off [[4]](https://docs.prismacloud.io/admin-guide/technology-overviews/telemetry) |
| Multi-Tenancy | Supported. Each tenant runs in its own K8s namespace [[5]](https://help.accuknox.com/resources/multitenancy/) | Supported. Projects: one Console per tenant behind a central Console [[6]](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects) |

### Application Security

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| Secrets (Repo / IaC) | Supported. Repos, pipelines, IaC, correlated in ASPM [[7]](https://help.accuknox.com/faqs/aspm/) | Limited. Secrets in images, containers, hosts. Not in repos or IaC files [[8]](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets) |
| Code Quality (Best Practices) | Supported. 2-engine SAST, 14 languages, SonarQube gates [[9]](https://help.accuknox.com/support-matrix/sast-support-matrix/) | Not supported. Repo scans check package dependencies only. No source code analysis [[10]](https://docs.prismacloud.io/admin-guide/continuous-integration/code-repo-scanning) |
| SAST | Supported. Pipeline and IDE SAST [[11]](https://help.accuknox.com/getting-started/3.4-release/) | Not supported. No SAST scanner. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| DAST | Supported. 4 scan types, incl. authenticated behind MFA [[12]](https://help.accuknox.com/how-to/dast-scan-types/) | Not supported. No DAST scanner. WAAS protects running web apps and APIs [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| SARIF Ingestion | Supported. Any tool: Checkmarx, JFrog, Gitleaks, Sonatype [[13]](https://help.accuknox.com/getting-started/sarif-findings/) | Not supported. No SARIF import. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| Repo / CI/CD Integration | Supported. GitHub, GitLab, Bitbucket + 9 CI/CD platforms [[14]](https://help.accuknox.com/support-matrix/cicd-support-matrix/) | Limited. Jenkins plugin plus twistcli for other CI. No repo-host apps [[15]](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin) |
| Container Scanning | Supported. CI/CD, registry, in-cluster, deploy blocking [[16]](https://help.accuknox.com/use-cases/container-scan/) | Supported. Image CVE scans in CI, 13 registry types, deployed images [[17]](https://docs.prismacloud.io/admin-guide/vulnerability-management/vuln-management-rules) |
| Generate & Ingest SBOMs | Supported. CycloneDX out, CycloneDX or SPDX in [[18]](https://help.accuknox.com/faqs/sbom/) | Limited. Exports CycloneDX 1.4. No SBOM import [[19]](https://docs.prismacloud.io/admin-guide/vulnerability-management/exporting-sboms) |

### Cloud Security Posture

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| CSPM (AWS, Azure, GCP) | Supported. CSPM on all 3 clouds with CDR auto-remediation [[20]](https://help.accuknox.com/use-cases/cloud/aws/) [[21]](https://help.accuknox.com/how-to/azure-org-onboard/) [[22]](https://help.accuknox.com/use-cases/cloud/gcp/) | Limited. No CSPM. CWPP module only [[23]](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning) |
| Multi-Cloud Asset Inventory | Supported. One inventory of accounts, assets, workloads [[24]](https://help.accuknox.com/use-cases/asset-inventory/) | Limited. Discovers VMs, K8s, registries, serverless on 3 clouds [[25]](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-accounts-discovery-pcce) |
| Private Cloud (OpenShift / Nutanix) | Supported. OpenShift, Nutanix, VMware Tanzu enforcement [[26]](https://help.accuknox.com/support-matrix/private-cloud/) | Limited. OpenShift 4.12 to 4.22 and Tanzu. Nutanix not listed [[27]](https://docs.prismacloud.io/admin-guide/install/system-requirements) |
| Real-Time Cloud Event Automation | Supported. CDR alerts on CloudTrail events, triggers remediation [[28]](https://help.accuknox.com/use-cases/cdr/) | Not supported. No cloud audit-event alerting. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| Compliance Frameworks | Supported. 42 benchmarks incl. ISO 27001, NIST, CIS, PCI, SOC 2, HIPAA [[29]](https://help.accuknox.com/support-matrix/compliance-matrix/) | Limited. 8 CIS benchmarks plus PCI DSS, HIPAA, NIST 800-190, GDPR, DISA STIG [[30]](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks) |

### Workload and Kubernetes Runtime

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| Container & K8s Runtime | Supported. Process, file, network enforcement + microsegmentation [[31]](https://help.accuknox.com/use-cases/app-behavior/) | Supported. Learned models and rules with Alert, Prevent, Block [[32]](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) |
| Preemptive / Inline Blocking | Supported. Kernel LSM stops a process before it runs [[33]](https://help.accuknox.com/faqs/runtime-security/) | Supported. Prevent stops the violating process. Block stops the container [[32]](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) |
| eBPF / Kernel Enforcement | Supported. eBPF plus AppArmor, SELinux, BPF-LSM [[33]](https://help.accuknox.com/faqs/runtime-security/) | Not supported. Linux Defender runs in user space, not as a kernel module. eBPF not named [[34]](https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture) |
| Process Allow / Deny | Supported. Per-pod or per-host process policies [[31]](https://help.accuknox.com/use-cases/app-behavior/) | Supported. Allowed and denied process lists per rule [[32]](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) |
| File Integrity Monitoring | Supported. Monitors and blocks critical path changes [[35]](https://help.accuknox.com/use-cases/vm-file-integrity/) | Supported. Host FIM. Container writes block by directory [[36]](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts) |
| Workload Anomaly Detection | Supported. Learns baseline, blocks deviations [[37]](https://help.accuknox.com/use-cases/zero-trust/) | Supported. Learned models, 1h learning, 24h dry run [[32]](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) |
| K8s Misconfiguration | Supported. Findings with fix steps and Jira tickets [[38]](https://help.accuknox.com/use-cases/cluster-misconfiguration-scanning/) | Supported. CIS node checks plus OPA admission rules [[39]](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent) |
| Trusted Registry Enforcement | Supported. KnoxGuard admission per cluster or namespace [[40]](https://help.accuknox.com/use-cases/admission-controller-knoxguard/) | Supported. Trusted Images rules. Alert or block [[41]](https://docs.prismacloud.io/admin-guide/compliance/trusted-images) |

### Kubernetes Identity (KIEM)

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| KIEM (K8s Entitlements) | Supported. RBAC search, graph, 15 risk queries [[42]](https://help.accuknox.com/use-cases/kiem/) | Limited. Alerts on K8s audit events only. No RBAC entitlement analysis [[43]](https://docs.prismacloud.io/admin-guide/audit/kubernetes-auditing) |
| Service Account Inventory | Supported. Service accounts, roles, bindings per cluster [[42]](https://help.accuknox.com/use-cases/kiem/) | Not supported. No K8s RBAC or service account inventory. CWPP only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| Over-Permission Detection | Supported. Flags principals with excess privileges [[42]](https://help.accuknox.com/use-cases/kiem/) | Not supported. No RBAC privilege analysis. CWPP only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| Risky Bindings & Cluster-Admin | Supported. Flags roles that modify workloads or read secrets [[42]](https://help.accuknox.com/use-cases/kiem/) | Limited. Custom audit rules alert on events. No binding risk analysis [[43]](https://docs.prismacloud.io/admin-guide/audit/kubernetes-auditing) |
| Stale K8s Entitlements | Supported. Unused roles and orphan service accounts [[42]](https://help.accuknox.com/use-cases/kiem/) | Not supported. No stale entitlement analysis. CWPP only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |

### API Security

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| North-South (NGINX Ingress) | Supported. NGINX Ingress connector feeds API inventory [[44]](https://help.accuknox.com/integrations/api-overview/) | Limited. WAAS inspects at the app container. No ingress connector documented [[45]](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro) |
| TLS Classification at Ingress | Supported. Inspects TLS, flags misconfigurations [[46]](https://help.accuknox.com/faqs/api-sec/) | Limited. Per-endpoint TLS with a supplied certificate. No TLS report [[47]](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas) |
| Shadow API Detection | Supported. Traffic vs OpenAPI spec [[48]](https://help.accuknox.com/use-cases/api-security/) | Supported. WAAS alerts or blocks paths missing from the imported spec [[49]](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection) |
| Zombie API Detection | Supported. Zombie and orphan APIs vs spec [[48]](https://help.accuknox.com/use-cases/api-security/) | Limited. Last-seen date per endpoint. No zombie API flag [[50]](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery) |

### Data Security (DSPM)

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| Data Discovery | Supported. S3, Blob, cloud and self-hosted DBs, Drive, Salesforce [[51]](https://help.accuknox.com/getting-started/dspm-overview/) | Not supported. No DSPM. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| Data Classification | Supported. 283 classes, PII, PHI, PCI, secrets, 62 country packs [[51]](https://help.accuknox.com/getting-started/dspm-overview/) | Not supported. No data classification. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |

### AI Security

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| LLM Red Teaming | Supported. Bedrock, Vertex AI, AI Foundry, Triton, vLLM [[52]](https://help.accuknox.com/use-cases/red-teaming/) | Not supported. No AI security module. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| Prompt Firewall | Supported. Inline: blocks, masks or logs prompts and responses [[53]](https://help.accuknox.com/use-cases/prompt-firewall-overview/) | Not supported. No prompt firewall. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| OWASP LLM Top 10 | Supported. v2025 mapped in AI-SPM and red teaming [[29]](https://help.accuknox.com/support-matrix/compliance-matrix/) | Not supported. No OWASP LLM Top 10 mapping. CWPP module only [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) |
| AI/ML Runtime Sandboxing | Supported. ModelArmor sandboxes models and agents [[54]](https://help.accuknox.com/use-cases/modelarmor/) | Limited. Generic runtime defense. No AI-specific sandbox [[32]](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) |

### Integrations

| Parameter | AccuKnox | Prisma Cloud Compute Edition |
| --- | --- | --- |
| Bi-Directional Ticketing | Supported. Ticket closes finding, recurrence reopens it [[55]](https://help.accuknox.com/faqs/general/) | Limited. Alerts create Jira issues and ServiceNow incidents. Push only [[56]](https://docs.prismacloud.io/admin-guide/alerts/jira) |


## Why Customers Choose AccuKnox Over Prisma Cloud Compute Edition

### Better

AccuKnox covers code, cloud, Kubernetes, data and AI from one on-prem control plane. Compute Edition covers workloads, and its docs list no SAST, DAST, DSPM or AI security module [[1]](https://help.accuknox.com/resources/deployment/) [[2]](https://docs.prismacloud.io/admin-guide/welcome/product-architecture).

### Faster

KubeArmor enforces policy inline at the kernel, so a disallowed process stops before it runs. The Compute Edition Linux Defender runs in user space. At one of India's top 3 public sector banks, AccuKnox cut remediation time by 91% and false positives by 89% [[33]](https://help.accuknox.com/faqs/runtime-security/) [[34]](https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture) [[58]](https://accuknox.com/wp-content/uploads/SBOM-Case-Study.pdf).

### Affordable

One AccuKnox platform includes SAST, DAST, DSPM and AI security on-prem. Compute Edition licenses each protected host, container host and function with credits, and covers workload protection only [[1]](https://help.accuknox.com/resources/deployment/) [[59]](https://docs.prismacloud.io/admin-guide/welcome/licensing).

## Every Cell Cites a Vendor Page

Prisma Cloud facts come from the Prisma Cloud Compute Edition administrator guide at docs.prismacloud.io, read on 2026-10-06. AccuKnox facts come from help.accuknox.com and one published AccuKnox case study. Palo Alto Networks also sells Prisma Cloud Enterprise Edition (SaaS) and Cortex Cloud, and their capabilities differ from this table.

| # | Source | # | Source | # | Source |
| --- | --- | --- | --- | --- | --- |
| 1 | [AccuKnox Help, Deployment](https://help.accuknox.com/resources/deployment/) | 2 | [Prisma Cloud Compute Edition docs, product architecture](https://docs.prismacloud.io/admin-guide/welcome/product-architecture) | 3 | [Prisma Cloud Compute Edition docs, pcee vs pcce](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce) |
| 4 | [Prisma Cloud Compute Edition docs, telemetry](https://docs.prismacloud.io/admin-guide/technology-overviews/telemetry) | 5 | [AccuKnox Help, Multitenancy](https://help.accuknox.com/resources/multitenancy/) | 6 | [Prisma Cloud Compute Edition docs, projects](https://docs.prismacloud.io/admin-guide/deployment-patterns/projects) |
| 7 | [AccuKnox Help, Aspm](https://help.accuknox.com/faqs/aspm/) | 8 | [Prisma Cloud Compute Edition docs, detect secrets](https://docs.prismacloud.io/admin-guide/compliance/detect-secrets) | 9 | [AccuKnox Help, Sast support matrix](https://help.accuknox.com/support-matrix/sast-support-matrix/) |
| 10 | [Prisma Cloud Compute Edition docs, code repo scanning](https://docs.prismacloud.io/admin-guide/continuous-integration/code-repo-scanning) | 11 | [AccuKnox Help, 3.4 release](https://help.accuknox.com/getting-started/3.4-release/) | 12 | [AccuKnox Help, Dast scan types](https://help.accuknox.com/how-to/dast-scan-types/) |
| 13 | [AccuKnox Help, Sarif findings](https://help.accuknox.com/getting-started/sarif-findings/) | 14 | [AccuKnox Help, Cicd support matrix](https://help.accuknox.com/support-matrix/cicd-support-matrix/) | 15 | [Prisma Cloud Compute Edition docs, jenkins plugin](https://docs.prismacloud.io/admin-guide/continuous-integration/jenkins-plugin) |
| 16 | [AccuKnox Help, Container scan](https://help.accuknox.com/use-cases/container-scan/) | 17 | [Prisma Cloud Compute Edition docs, vuln management rules](https://docs.prismacloud.io/admin-guide/vulnerability-management/vuln-management-rules) | 18 | [AccuKnox Help, Sbom](https://help.accuknox.com/faqs/sbom/) |
| 19 | [Prisma Cloud Compute Edition docs, exporting sboms](https://docs.prismacloud.io/admin-guide/vulnerability-management/exporting-sboms) | 20 | [AccuKnox Help, Aws](https://help.accuknox.com/use-cases/cloud/aws/) | 21 | [AccuKnox Help, Azure org onboard](https://help.accuknox.com/how-to/azure-org-onboard/) |
| 22 | [AccuKnox Help, Gcp](https://help.accuknox.com/use-cases/cloud/gcp/) | 23 | [Prisma Cloud Compute Edition docs, agentless scanning](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning) | 24 | [AccuKnox Help, Asset inventory](https://help.accuknox.com/use-cases/asset-inventory/) |
| 25 | [Prisma Cloud Compute Edition docs, cloud accounts discovery pcce](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-accounts-discovery-pcce) | 26 | [AccuKnox Help, Private cloud](https://help.accuknox.com/support-matrix/private-cloud/) | 27 | [Prisma Cloud Compute Edition docs, system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements) |
| 28 | [AccuKnox Help, Cdr](https://help.accuknox.com/use-cases/cdr/) | 29 | [AccuKnox Help, Compliance matrix](https://help.accuknox.com/support-matrix/compliance-matrix/) | 30 | [Prisma Cloud Compute Edition docs, cis benchmarks](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks) |
| 31 | [AccuKnox Help, App behavior](https://help.accuknox.com/use-cases/app-behavior/) | 32 | [Prisma Cloud Compute Edition docs, runtime defense containers](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) | 33 | [AccuKnox Help, Runtime security](https://help.accuknox.com/faqs/runtime-security/) |
| 34 | [Prisma Cloud Compute Edition docs, host defender architecture](https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture) | 35 | [AccuKnox Help, Vm file integrity](https://help.accuknox.com/use-cases/vm-file-integrity/) | 36 | [Prisma Cloud Compute Edition docs, runtime defense hosts](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-hosts) |
| 37 | [AccuKnox Help, Zero trust](https://help.accuknox.com/use-cases/zero-trust/) | 38 | [AccuKnox Help, Cluster misconfiguration scanning](https://help.accuknox.com/use-cases/cluster-misconfiguration-scanning/) | 39 | [Prisma Cloud Compute Edition docs, open policy agent](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent) |
| 40 | [AccuKnox Help, Admission controller knoxguard](https://help.accuknox.com/use-cases/admission-controller-knoxguard/) | 41 | [Prisma Cloud Compute Edition docs, trusted images](https://docs.prismacloud.io/admin-guide/compliance/trusted-images) | 42 | [AccuKnox Help, Kiem](https://help.accuknox.com/use-cases/kiem/) |
| 43 | [Prisma Cloud Compute Edition docs, kubernetes auditing](https://docs.prismacloud.io/admin-guide/audit/kubernetes-auditing) | 44 | [AccuKnox Help, Api overview](https://help.accuknox.com/integrations/api-overview/) | 45 | [Prisma Cloud Compute Edition docs, waas intro](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-intro) |
| 46 | [AccuKnox Help, Api sec](https://help.accuknox.com/faqs/api-sec/) | 47 | [Prisma Cloud Compute Edition docs, deploy waas](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas) | 48 | [AccuKnox Help, Api security](https://help.accuknox.com/use-cases/api-security/) |
| 49 | [Prisma Cloud Compute Edition docs, waas api protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection) | 50 | [Prisma Cloud Compute Edition docs, waas api discovery](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-discovery) | 51 | [AccuKnox Help, Dspm overview](https://help.accuknox.com/getting-started/dspm-overview/) |
| 52 | [AccuKnox Help, Red teaming](https://help.accuknox.com/use-cases/red-teaming/) | 53 | [AccuKnox Help, Prompt firewall overview](https://help.accuknox.com/use-cases/prompt-firewall-overview/) | 54 | [AccuKnox Help, Modelarmor](https://help.accuknox.com/use-cases/modelarmor/) |
| 55 | [AccuKnox Help, General](https://help.accuknox.com/faqs/general/) | 56 | [Prisma Cloud Compute Edition docs, jira](https://docs.prismacloud.io/admin-guide/alerts/jira) | 57 | [Prisma Cloud Compute Edition docs, getting started](https://docs.prismacloud.io/admin-guide/welcome/getting-started) |
| 58 | [AccuKnox case study, Top 3 Indian public sector bank operationalises SBOM air-gapped](https://accuknox.com/wp-content/uploads/SBOM-Case-Study.pdf) | 59 | [Prisma Cloud Compute Edition docs, licensing](https://docs.prismacloud.io/admin-guide/welcome/licensing) | - | - |
