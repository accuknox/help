# CSPM cheat sheet research

Module: `cspm`. Slug: `cspm-best-practices-guide`. Campaign: `cspm-cheat-sheet`. Opened 2026-10-07.

## Problem data points

Each number below was read on the opened page. The pages were opened again with WebFetch on 2026-10-07 to confirm the wording.

| # | Number | Exact wording | Publisher, report, year | URL opened | Used on |
|---|---|---|---|---|---|
| 1 | 65% | "65% of organizations experienced a cloud-related security incident in the past year" | Check Point, 2025 Cloud Security Report, press release 5 June 2025 | https://www.checkpoint.com/press-releases/dangerous-blind-spots-costing-enterprises-time-trust-and-agility-exposed-in-check-points-2025-cloud-security-report/ | Page 2 card |
| 2 | 62% and 6% | "62% took more than 24 hours to remediate breaches" and "a mere 6% managed to remediate it within that time frame" (the first hour) | Check Point, 2025 Cloud Security Report, 2025 | Same as 1 | Page 2 card |
| 3 | nearly 500 alerts | "More than half of them face nearly 500 alerts daily hindering response times" | Check Point, 2025 | Same as 1 | Page 3 |
| 4 | 71% | "71% of respondents rely on over 10 different cloud security tools" | Check Point, 2025 | Same as 1 | Not used |
| 5 | 9% and 97% | "9% of publicly accessible cloud storage contains sensitive data, 97% of which is classified as restricted or confidential." | Tenable, Cloud Security Risk Report 2025, press release 18 June 2025 | https://www.tenable.com/press-releases/tenable-research-finds-pervasive-cloud-misconfigurations-exposing-critical-data-and-secrets | Page 2 card |
| 6 | 29% | A "toxic cloud trilogy", "a workload that is publicly exposed, critically vulnerable, and highly privileged", fell "from 38% to 29%" of organizations | Tenable, 2025 | Same as 5 | Page 3 |
| 7 | 84% | "at least 84% of organizations use more than one AWS account" | Datadog, State of Cloud Security, October 2025 | https://www.datadoghq.com/state-of-cloud-security/ | Page 3 |
| 8 | 1% | "One percent of S3 buckets are effectively public, down from 1.5% in 2024" | Datadog, 2025 | Same as 7 | Not used |
| 9 | 59% | "59% of IAM users have an active access key older than one year" | Datadog, 2025 | Same as 7 | Not used |
| 10 | #1 of 11 | The #1 top threat is "Misconfiguration & Inadequate Change Control", from "insights of over 500 experts" on "the 11 top cybersecurity threats" | Cloud Security Alliance, Top Threats to Cloud Computing 2024, blog 20 Aug 2024 | https://cloudsecurityalliance.org/blog/2024/08/20/top-threat-1-misconfig-misadventures-taming-the-change-control-chaos | Page 3 |

### Dropped

- Gartner "99% of cloud security failures will be the customer's fault". The Gartner page returned 403, and the claim dates from 2019.
- Verizon DBIR 2025 misconfiguration share. The Verizon press release does not carry it, and only third party roundups do.
- "81% of cloud incidents come from customer misconfiguration". Found only in third party roundups.
- Orca 2025 "76% of organizations have at least one public-facing asset that enables lateral movement". Read by the research agent but not opened a second time, so it stays out of the PDF.
- IBM Cost of a Data Breach 2024 "40% of breaches involved data stored across multiple environments". Correct, but 2024 and less specific to posture than the cards above.

## Product truth, help docs read

| Practice | What the docs show | Page |
|---|---|---|
| Inventory every account | Agentless read only scans of AWS, Azure and GCP. Organization onboarding through a CloudFormation StackSet with "Automatically connect to new accounts". Azure management group scope with auto fetch of new subscriptions. STS Assume Role with External ID for standalone AWS accounts, with no long lived keys. List and hierarchy views of Cloud Assets. Labels on cloud accounts | `docs/use-cases/asset-inventory.md`, `docs/how-to/aws-org-onboard.md`, `docs/how-to/azure-org-onboard.md`, `docs/getting-started/3.6-release.md`, `docs/faqs/cspm.md`, `docs/how-to/how-to-create-labels.md` |
| Fix by risk | Findings filters by Status, Asset Name, Risk Factor and Framework. Checks Management switches checks off per account and changes severity, and the change follows into findings, compliance and reports. Dashboard widgets for insights, open tickets for critical and high findings, and SLA status | `docs/how-to/findings-lifecycle.md`, `docs/getting-started/3.6-release.md`, `references/PRODUCT UI/1_dashboard/CSPM Dash 3.png` |
| Read findings in context | Security Graph on an asset (Inventory, Cloud Assets, Security Graph tab) and on a finding (Issues, Findings, Security Graph tab). Shows blast radius, the Internet node, IAM identities. Badges flag major issues only. On by default for AWS, Azure and GCP. Needs a completed scan | `docs/getting-started/3.6-release.md` |
| Map to compliance | 1,000+ checks, 30+ compliance programs, per sub control percentage, Detailed View filters, each finding lists every framework and control it maps to | `docs/use-cases/compliance.md`, `docs/getting-started/3.6-release.md` |
| Automate tickets and remediation | Rule Engine with conditions, expiration and the Create Ticket action. Parent field groups findings under one parent ticket. Jira, ServiceNow, Freshservice and ConnectWise. Finding moves Active, Waiting for Verification, Fixed, and the linked ticket closes. Solution tab with remediation steps and code snippets. Batch Ask AI | `docs/use-cases/rules-engine-ticket-creation.md`, `docs/getting-started/3.6-release.md`, `docs/how-to/findings-lifecycle.md`, `docs/faqs/cspm.md`, `docs/getting-started/3.3-release.md` |
| Drift detection | Scheduled scans, asset groups with baseline conformance, Monitors on critical assets such as S3 buckets and bastions, Status Logs on cloud findings | `docs/use-cases/cloud-misconfigurations.md`, `docs/faqs/cspm.md`, `docs/getting-started/3.6-release.md` |

Toxic combinations. The docs describe the Security Graph showing an internet exposed instance with its IAM identities and attack path. They do not describe an automated toxic combination detector, so the PDF says "read the finding with what it can reach" and cites Tenable for the toxic combination share.

## Proof row on page 12

Read on https://accuknox.com/analyst-recognition (cited with `site_assets.py cite`, status 200).

- "Featured in KuppingerCole's 2026 CNAPP Leadership Compass". The text names attack path analysis and unified risk correlation.
- "Two 2026 Best Practices recognitions, one global, one regional". The page badge is the Frost & Sullivan badge.

## Screenshots

| File | Source | Width px |
|---|---|---|
| `img/map.png` | `PRODUCT UI/1_dashboard/Cloud Finding Dash 1.png`, crop | 3235 |
| `img/inventory.png` | `PRODUCT UI/1_dashboard/CSPM Dash 1.png`, crop | 3245 |
| `img/risk.png` | `PRODUCT UI/1_dashboard/CSPM Dash 3.png`, crop | 3245 |
| `img/graph.png` | `PRODUCT UI/security graph/Security Graph 2.png`, crop below the asset header, so the account ID is out of frame | 2480 |
| `img/compliance.png` | `PRODUCT UI/5_compliance/Compliance 2.png`, crop | 3270 |
| `img/tickets.png` | `PRODUCT UI/integrations/Integrations 3.png`, crop below the tenant name | 4660 |
| `img/drift.png` | `PRODUCT UI/1_dashboard/Cloud Finding Dash 2.png`, crop | 3235 |

Skipped: `3_issues/Issues_2.png` and `Issues_4.png`, `5_compliance/Compliance 4.png` and `CSPM Dash 2.png`, because each shows an AWS account ID.
