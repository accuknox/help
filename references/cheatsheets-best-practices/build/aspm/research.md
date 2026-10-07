# ASPM cheat sheet research

Module: ASPM. Slug: `aspm-best-practices-guide`. Campaign: `aspm-cheat-sheet`. Compiled 2026-10-07.

## Problem data points, every source opened

| # | Number | Exact wording on the page | Publisher, report, year | URL opened | Used on |
|---|---|---|---|---|---|
| 1 | 48,244 CVE records in 2025, 40,077 in 2024 | Table "Published CVE Records", row TOTAL: 2025 = 48,244, 2024 = 40,077 | CVE Program, Metrics page, 2026 snapshot | https://www.cve.org/about/Metrics | p2 |
| 2 | 28,649,024 new secrets, up 34% | "28,649,024" new secrets detected in public GitHub commits in 2025, "34%" increase | GitGuardian, The State of Secrets Sprawl 2026 | https://www.gitguardian.com/state-of-secrets-sprawl-report-2026 | p2 |
| 3 | 64% still active | Of secrets leaked in 2022, "64% are still active and exploitable, sitting in public repositories" | GitGuardian, The State of Secrets Sprawl 2026 | https://www.gitguardian.com/state-of-secrets-sprawl-report-2026 | p3 |
| 4 | 43 days median, up from 32. 26% fully fixed | "The median time for full resolution went up to 43 days, almost two weeks more than the previous year's 32 days." Only 26% of CISA KEV vulnerabilities fully remediated in 2025, down from 38% | Verizon, 2026 Data Breach Investigations Report | https://www.verizon.com/business/resources/Td15/reports/2026-dbir-data-breach-investigations-report.pdf | p2 |
| 5 | 31%, up from 20% | Vulnerability exploitation is the top initial access vector, "reaching the height of 31%, up from 20% last year" | Verizon, 2026 DBIR | same PDF as #4 | p3 |
| 6 | 18% | "only 18% of critical dependency vulnerabilities stay critical after adjusting the severity score". Adjustment uses runtime context, exploit availability and EPSS | Datadog, State of DevSecOps, updated February 2026 | https://www.datadoghq.com/state-of-devsecops/ | p3 |

Dropped on purpose:

- Cycode State of ASPM (50 tools average) and OX Security benchmark (2 to 5% of alerts critical). Both are ASPM vendors that compete with AccuKnox.
- Black Duck OSSRA 2026 (581 vulnerabilities per codebase) and Veracode SoSS 2026 (82% hold security debt). Both are AppSec vendors that compete with AccuKnox.
- OX "569,354 alerts per organization". It appears only in third party coverage, never on the OX page.

## Proof row, accuknox.com

| Fact | URL opened |
|---|---|
| Featured in KuppingerCole 2026 CNAPP Leadership Compass. The report names DevSecOps and unified risk correlation | https://accuknox.com/analyst-recognition/ |
| Gartner Emerging Tech techscape profile, among startups driving the convergence of cloud and application security | https://accuknox.com/analyst-recognition/ |
| One CLI, six scan types (IaC, SAST, SonarQube SAST, secrets, container, DAST) | https://help.accuknox.com/use-cases/aspm-scanner-cli/ |

## Product truth, help docs read

| Claim in the PDF | Doc |
|---|---|
| ASPM covers SAST, DAST, SCA, IaC, container, secrets, SBOM | `docs/use-cases/aspm.md`, `docs/faqs/aspm.md` |
| Findings land in Issues, Findings, filter by Data Type (Opengrep SAST Scan, IaC Scan, DAST Scan, Secret Scan) | `sast-sq.md`, `iac-scan.md`, `dast-xss.md`, `secret-scan-cicd-aws.md` |
| Jenkins plugin uploads are normalized, deduplicated, ticketed, tracked across builds | `docs/integrations/jenkins-sast.md` |
| SonarQube results can be ingested, keep the existing scanner | `faqs/aspm.md` Q7, `aspm-scanner-cli.md` (sq-sast) |
| ASPM reports, on demand or scheduled, SAST, DAST, SCA, IaC, Secret Scan, up to 30 days range, email | `aspm-reports.md` |
| EPSS is FIRST's 30 day exploit probability. EPSS SIG says it "is not ... a complete picture of risk" | `epss-scoring.md` |
| EPSS score and percentile shown beside CVSS in findings, container image scanning only | `getting-started/3.3-release.md` |
| Runtime Verified flag from eBPF telemetry via KubeArmor, enrichment with CISA KEV, EPSS, GitHub PoC links | `getting-started/3.4-release.md` |
| App Based integration for GitHub, GitLab, Bitbucket Cloud. Read only. SCA, Secrets, SAST, SBOM, IaC. Auto connect new repos. Default branch preselected. Bitbucket Data Center not covered | `how-to/code-source-onboarding.md` |
| CI/CD platforms: GitHub Actions, GitLab, Jenkins, Azure DevOps, AWS CodePipeline, Bitbucket, CircleCI, Google Cloud Build, Harness, Bamboo | `integrations/cicd-overview.md`, `faqs/aspm.md` Q3 |
| CLI local run with skip upload and keep results, softfail flag | `aspm-scanner-cli.md` |
| Secret scan action with fail: true fails the build. Checkout clones history. Revoke, rotate, then clean history with BFG. Only findings metadata is uploaded | `secret-scan-cicd-aws.md`, `faqs/aspm.md` Q13 |
| soft_fail starts in observe mode, then enforce | `faqs/aspm.md` Q8, `integrations/google-build.md` |
| DAST baseline scan for CI, full scan for staging | `faqs/aspm.md` Q4, `dast-authenticated.md` |
| KnoxGuard blocks deployments from untrusted registries | `knoxguard-supply-chain.md` |
| SBOM in CycloneDX and SPDX, generate in CI or upload from Syft or Trivy, compare versions, license severity levels | `faqs/sbom.md`, `aspm-scanner-cli.md` (generate SBOM) |
| Rule Engine conditions plus Create Ticket action, rule expiration | `rules-engine-ticket-creation.md` |
| Parent field groups findings into a Jira parent with sub tasks | `getting-started/3.5-release.md` |
| Lifecycle automation: Active, Waiting for Verification, Fixed once two scans agree, ticket closes | `getting-started/3.6-release.md` |

Not claimed, because the docs do not support it: SAST reachability analysis, EPSS on SAST or IaC findings, cross scanner deduplication for every data type (Group by Unique Vulnerability is cloud findings only).

## Screenshots

| File | Source | Pixels | Page |
|---|---|---|---|
| `img/platform.png` | `references/PRODUCT UI/platformization/image.png` cropped to the module columns | 5832 x 2260 | p4 |
| `img/findings-summary.png` | `references/PRODUCT UI/3_issues/Issues_1.png`, cropped | 3400 x 1250 | p5 |
| `img/container-dash.png` | `references/PRODUCT UI/1_dashboard/ASPM_Container Image_Dash 1.png`, cropped | 3400 x 1380 | p6 |
| `img/iac-dash.png` | `references/PRODUCT UI/1_dashboard/ASPM_IaC Findings_Dash.png`, cropped | 3400 x 1400 | p7 |
| `img/secret-dash.png` | `references/PRODUCT UI/1_dashboard/ASPM_Secret Scan Findings_Dash.png`, cropped above the contributor emails | 3400 x 880 | p8 |
| `img/secret-gate.png` | `docs/use-cases/images/secret-scan-cicd-aws/1.png`, cropped to the failing lines | 1920 x 575 | p9 |
| `img/sbom-compare.png` | `references/PRODUCT UI/sbom/SBOM_4.png`, cropped | 3400 x 1500 | p10 |
| `img/rule-engine.png` | `docs/getting-started/images/release-notes/v3.5/rule-engine-create-ticket-parent-field.png`, cropped to conditions and actions | 1882 x 610 | p11 |

Skipped: the EPSS column screenshot in the 3.3 release notes (578 px wide, too small), Issues_2 and Issues_4 (show an AWS account ID), the lower half of the secret dashboard (contributor email addresses).
