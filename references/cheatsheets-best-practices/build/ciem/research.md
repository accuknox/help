# CIEM cheat sheet research

Module: `ciem`. Slug: `ciem-best-practices-guide`. Campaign: `ciem-cheat-sheet`. Researched 2026-10-07.

## Data points used in the PDF

Every number below was read on the page at the URL listed.

| # | Number | Exact wording | Publisher, year | URL |
|---|---|---|---|---|
| 1 | 2% | "Of the 51,000 permissions granted to those identities (a 22% increase from 2022), only 2% were used and 50% were considered high-risk." | Microsoft, 2024 State of Multicloud Security Risk Report | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/2024-State-of-Multicloud-Security-Risk-Report.pdf |
| 2 | 10 to 1 | "Today, there is one human identity for every 10 workload identities. This problem is even more acute among small- and medium-sized businesses, which have one human identity for every 50 workload identities." | Microsoft, 2024 State of Multicloud Security Risk Report | same PDF as row 1 |
| 3 | 83% | "Identity compromise underpinned 83% of compromises." | Google Cloud, Cloud Threat Horizons Report H1 2026 | https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026 |
| 4 | 59% | "In AWS, 59% of IAM users have an active access key older than one year. Over half of these users have credentials that have been unused for over 90 days" | Datadog, State of Cloud Security, updated October 2025 | https://www.datadoghq.com/state-of-cloud-security/ |
| 5 | 2.4% and 19.4% | "almost one in five (19.4%) is overprivileged" and "2.4% allow an attacker to gain full administrative access to the account by privilege escalation" (EC2 instances) | Datadog, State of Cloud Security, October 2025 | https://www.datadoghq.com/state-of-cloud-security/ |
| 6 | 13% | "For EKS, we determined that 13% of clusters have a dangerous node role that has full administrator access, allows for privilege escalation, has overly permissive data access" | Datadog, State of Cloud Security, October 2025 | https://www.datadoghq.com/state-of-cloud-security/ |
| 7 | 80% | "the average percentage of inactive workload identities, at 80%, has doubled since 2021" | Microsoft Entra blog, 2023 State of Cloud Permissions Risks report | https://techcommunity.microsoft.com/blog/microsoft-entra-blog/2023-state-of-cloud-permissions-risks-report-now-published/1061397 |

## Data points checked and dropped

- Verizon DBIR as "identity is the top breach vector". The 2026 DBIR page says "31% of breaches now start with software vulnerabilities, beating stolen passwords as the top way attackers get in" (https://www.verizon.com/business/resources/reports/dbir/). The claim no longer holds, so the PDF does not make it. The 2025 DBIR figure of 22% credential abuse is superseded.
- Google Threat Horizons H1 2026 also reports weak or absent credentials fell from 47.1% to 27.2% of initial access in H2 2025. The PDF uses the 83% identity compromise figure from the same report instead, because it describes the whole compromise, not only the entry point.
- Microsoft 2023 "1% of permissions used". Read only on secondary sites (Infosecurity Magazine, Scribd). The Microsoft blog says "less than 5% of permissions granted are used by workload identities". Superseded by the 2024 report's 2%.
- The KIEM help page claim that "65% of Kubernetes administrators struggle with policy configuration" carries no source. Not used.

## Product truth, from the docs

Sources: `docs/getting-started/ciem-overview.md`, `docs/getting-started/ciem-onboarding.md`, `docs/use-cases/kiem.md`, `docs/getting-started/3.5-release.md`, `docs/faqs/general.md`, `references/competitive/ciem-page-study-2026-09.md`.

- CIEM is marked "Coming soon" in the docs and "Beta" in the FAQ. The PDF states this on the map page and in the closing page.
- CIEM supports standalone accounts only. Organization accounts are not supported yet. Stated on the map page.
- Clouds: AWS, GCP, Azure and OCI. Identity types: users, groups and roles. Classification: human or machine.
- Risk classes from attached policies: Privilege Escalation, Data Exfiltration, Credentials Exposure, Infrastructure Modification.
- Lifecycle columns: Age In Days, Identity Created At, Created By, Last Used, Days Since Last Used.
- Identity panel tabs: Overview (policy JSON, Total Findings by severity), Access Graph, Related Identities, Raw Information.
- Policy types: cloud managed, inline policy, user managed.
- Onboarding: CIEM toggle on by default in Step 2 of 3.
- KIEM: 15 built in queries, including service accounts not connected to any workload, principals with excessive privileges, roles that modify workloads, roles that read secrets, unused roles. v3.5 KIEM findings show the raw rule and the affected ServiceAccount or role binding.

Practices dropped because the docs do not support them:

- Toxic combinations such as admin plus no MFA. CIEM docs show no MFA signal.
- Automated right sizing or generated least privilege policies. The page study lists this as a competitor claim AccuKnox does not make.
- Unused permission analysis at the action level. CIEM shows identity last use, not per permission use. The PDF frames the practice as dormant identities and reading the policy document.
- Just in time access and IdP ingestion.

## accuknox.com

- `https://accuknox.com/platform/ciem` returns 404 (site_assets.py cite, 2026-10-07). No CIEM page is live yet.
- `https://accuknox.com/blog/kubernetes-identity-entitlement-management` 200, KIEM guide.
- `https://accuknox.com/analyst-recognition` 200. Read: "Featured in KuppingerCole's 2026 CNAPP Leadership Compass" and "Two 2026 Best Practices recognitions, one global, one regional".
- `https://accuknox.com/demo` 200.

## Screenshots

All from the live help docs, already redacted by the docs team. Cropped with PIL, no upscale.

| File | Source | Pixels |
|---|---|---|
| `img/org-graph.png` | `docs/getting-started/images/ciem/ciem-org-graph.png` | 2560 x 1074 |
| `img/p1-inventory.png` | `ciem-identity-list-all.png` | 2560 x 883 |
| `img/p2-dormant.png` | `ciem-identity-list-columns.png` | 2560 x 730 |
| `img/p3-risk.png` | `ciem-identity-list.png` | 2086 x 730 |
| `img/p4-policy.png` | `ciem-identity-overview.png` | 1792 x 538 |
| `img/p5-graph.png` | `ciem-identity-graph.png` | 1792 x 628 |
| `img/p6-kiem.png` | `docs/getting-started/images/release-notes/v3.5/kiem-finding-create-roles-rolebindings.png`, cluster location redacted | 1919 x 620 |

Skipped: `references/PRODUCT UI/CIEM/List View/misconfiguration.png` shows a person's username and a Misconfiguration tab the docs do not document. The KIEM use case images are under 1400 px wide.
