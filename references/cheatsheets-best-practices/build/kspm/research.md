# KSPM cheat sheet research

Module: kspm. Slug: `kubernetes-security-best-practices-guide`. Campaign: `kspm-cheat-sheet`.
Opened on 2026-10-07.

## Problem data points (each read on the page)

| # | Number | Exact wording | Publisher, report, year | URL opened |
|---|---|---|---|---|
| 1 | 89% | "Nearly 9 in 10 organizations had at least 1 container or Kubernetes security incident in the last 12 months." | Red Hat, The State of Kubernetes Security Report, 2024 (n=600) | https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-2024-1210287-202406-en.pdf |
| 2 | 67% | "67% of respondents have delayed or slowed down deployment" due to security concerns | Red Hat, same report, 2024 | same PDF, and https://www.redhat.com/en/resources/kubernetes-adoption-security-market-trends-overview |
| 3 | 40% | "40% said their organization detected misconfigurations in their container or Kubernetes environments" | Red Hat, same report, 2024 | same PDF |
| 4 | 46% | "46% of respondents also revealed that their organization experienced revenue or customer loss as a result of a security incident." | Red Hat, same report, 2024 | same PDF |
| 5 | 39% / 34% / 54% | "Two in five (39%) EKS clusters and one in three (34%) AKS clusters are exposed to the internet." GKE "over one in two (54%)" | Datadog, State of Cloud Security, October 2025 | https://www.datadoghq.com/state-of-cloud-security/ |
| 6 | 13% | "13% of clusters have a dangerous node role that has full administrator access" (EKS) | Datadog, State of Cloud Security, 2025 | https://www.datadoghq.com/state-of-cloud-security/ |
| 7 | 2% | "Only 2% of granted permissions are being used" | Sysdig, 2024 Cloud-Native Security and Usage Report, press release 2024-01-31 | https://sysdig.com/press-releases/sysdig-2024-usage-report/ |
| 8 | 82% | "82% of organizations have a Kubernetes API server that is publicly accessible" | Orca Security, 2024 State of Cloud Security Report | https://orca.security/lp/2024-state-of-cloud-security-report/ |

Used in the PDF: 89% and 67% and 40% (page 2), 2% and 54% (page 3).

Dropped: Sysdig 2025 root and privileged container shares (no figure on the page), Red Hat RBAC chart
percentages (text unreadable), Shadowserver exposed API servers (2022, snippet only). The Red Hat report
gives no share of incidents caused by misconfiguration, so the sheet uses the 40% "detected
misconfigurations" figure and says exactly that.

## Product truth (help docs read)

- `docs/use-cases/kspm.md`. KSPM is agentless, with compliance monitoring and alerting.
- `docs/use-cases/cis-benchmarking.md`, `docs/how-to/cis-benchmarking.md`. CIS K8s Benchmarking runs as a
  scheduled cron job. Findings under Issues > Findings, filter CIS k8s Benchmarking, Risk Factor, Tool
  Output Failed. Managed CIS benchmarking is supported for GKE ("Currently we support GKE based CIS
  Benchmarking for managed GKE clusters"). Platform selection matters for accuracy.
- `docs/use-cases/cluster-misconfiguration-scanning.md`, `docs/how-to/cluster-misconfig-scan-onboarding.md`,
  `docs/how-to/k8s-security-onboarding.md`. Cron job. Checks root containers, privilege escalation and
  100+ other rules. Example finding: hard coded MYSQL_ROOT_PASSWORD in a Deployment env, with source
  code tab and Solution tab ("Use Kubernetes secrets or Key Management Systems to store credentials").
  Jira ticket from the finding.
- `docs/use-cases/admission-controller-knoxguard.md`, `knoxguard-supply-chain.md`. KnoxGuard uses Kyverno.
  Registry restrictions at cluster and namespace level. Deny privileged containers today. Vulnerability
  scan thresholds are "in the pipeline", so the sheet does not claim them. Policies uploaded as YAML
  via Create Policy. Violations under Monitors > Alerts, type Admission Controller. Logs can go to SIEM.
- `docs/use-cases/pod-security-admission-controller.md`. Levels Privileged, Baseline, Restricted. Modes
  Enforce and Audit. Set per namespace from Inventory > Clusters > View Workloads > cog icon. Dry Run
  before Enforce.
- `docs/use-cases/kiem.md`. Install KIEM job from Manage Cluster, cron scans. Identity > KIEM. 15
  built-in queries, examples: service accounts with no workloads, principals with excessive privileges,
  roles that modify workloads, roles that read secrets, unused roles. Graph view and full-text search.
- `docs/use-cases/network-segmentation.md`. Auto discovered network policies per workload, applied
  policy goes Pending, then needs approval, then Active.
- `docs/how-to/cluster-onboarding.md`. One Helm command from Settings > Manage Clusters, toggles for
  KIEM, Cluster Misconfiguration, CIS Benchmarking, in cluster image scan.
- `docs/how-to/k8s-security-onboarding.md`. Managed (EKS, AKS, OCI) and on prem, Kubernetes >= 1.18,
  only egress connectivity from cluster to control plane.

## Screenshots

| File | Source | Width px | Frame |
|---|---|---|---|
| img/cluster-overview.png | PRODUCT UI/2_inventory/Clusters 2.png, cropped | 1856 | full |
| img/cis-findings.png | docs/use-cases/images/cis-benchmarking/1.png | 1692 | full |
| img/misconfig-source.png | docs/use-cases/images/cluster-misconfig-scan/4.png | 1919 | full |
| img/admission-policies.png | PRODUCT UI/6_runtime/Runtime 1.png, cropped | 3270 | full |
| img/psa-mode_up.png | docs PSA image1.png, upscaled 2x (screen model) | 1370 | half |
| img/psa-dryrun_up.png | docs PSA image4.png, upscaled 2x (screen model) | 1390 | half |
| img/kiem-query.png | docs/use-cases/images/kiem/kiem-query.png | 1301 | half |
| img/kiem-filter.png | docs/use-cases/images/kiem/kiem-filter.png | 1303 | half |
| img/netpol_up.png | docs/use-cases/images/network-1.png, upscaled 2x | 3140 | full |
