# Research, secrets management best practices cheat sheet

Module: `secrets-manager`. Slug: `secrets-management-best-practices-guide`. Campaign: `secrets-manager-cheat-sheet`. Opened 2026-10-07.

## Data points used in the PDF

| # | Number | Exact wording on the page | Publisher, year | URL opened | Used on |
|---|---|---|---|---|---|
| 1 | 28.65 million, +34% | "28.65 million new hardcoded secrets were added to public GitHub commits in 2025 alone, a 34% increase year over year and the largest single-year jump we've recorded." | GitGuardian, State of Secrets Sprawl 2026 (March 2026) | https://blog.gitguardian.com/the-state-of-secrets-sprawl-2026/ | p2 |
| 2 | above 64% | "In the 2025 report, we found that nearly 70% of credentials confirmed as valid in 2022 were still valid in January 2025 ... When we retested that same dataset in January 2026, the validity rate was still above 64%" | GitGuardian, 2026 | same | p2 |
| 3 | 94 days | "our research found the median time to remediate leaked secrets discovered in a GitHub repository was 94 days." (page 7) | Verizon, 2025 DBIR Executive Summary | https://www.verizon.com/business/resources/reports/2025-dbir-executive-summary.pdf | p2 |
| 4 | roughly 6x | "Internal repos are roughly 6× more likely than public ones to contain hardcoded secrets." | GitGuardian, 2026 | same blog | p3 |
| 5 | about 28% | "About 28% of incidents originate entirely outside repositories, in places like Slack, Jira, and Confluence." | GitGuardian, 2026 | same blog | p3 |
| 6 | 59% | "The report also notes that 59% of the compromised machines were CI/CD runners rather than personal workstations" (Shai-Hulud 2 dataset, 6,943 compromised machines) | GitGuardian, 2026 | same blog | p3 |

## Checked and not used

- Verizon 2025 DBIR, credential abuse at 22% of initial access. The executive summary text only says credential abuse "is still the most common vector". The 22% sits in Figure 1, which the text extract does not carry, so it was dropped.
- Verizon 2026 DBIR. Its press release (https://www.verizon.com/about/news/breach-industry-wide-dbir-finds) says vulnerability exploitation (31%) passed stolen credentials as the top entry point. The 13% credential abuse figure appears only in secondary coverage, and the full PDF exceeded the fetch limit, so it was dropped.
- GitGuardian 2026, AI service secrets up 81% and Claude Code assisted commits at a 3.2% leak rate. True on the page, but off topic for this guide.

## Proof facts on page 12

| Fact | Source opened |
|---|---|
| Featured in KuppingerCole's 2026 CNAPP Leadership Compass | https://accuknox.com/analyst-recognition/ (Firecrawl scrape, 200) |
| Ranked first AI security startup of 2025 at Security BSides Bangalore | https://accuknox.com/press-release/accuknox-wins-1-ai-security-startup-of-2025-security-bsides-bangalore-annual-cybersecurity-2025 (linked from the analyst recognition page) |
| KubeArmor is an AccuKnox CNCF sandbox open source project, and AccuKnox CWPP hardens every Secrets Manager pod with it | docs/use-cases/hashicorp.md, docs/secrets-manager/architecture.md |
| Vault compatible APIs, existing Vault apps move with minimal changes | docs/faqs/secrets-manager.md |

## Product truth, per practice

| Practice | Doc support |
|---|---|
| 01 Find leaked secrets | use-cases/secret-scan-cicd-aws.md: full history checkout, fail the build, Issues > Findings filter Secret Scan, type, file path, commit SHA, Jira or ServiceNow ticket, revoke then rotate, BFG Repo Cleaner. CI integrations in mkdocs nav: GitHub Actions, GitLab, Jenkins, Bitbucket, CircleCI and more |
| 02 Centralize | overview.md, architecture.md (engines KV, Database, PKI, Transit, SSH, TOTP), kv-secrets.md (versions, path per component, delete vs destroy), sharing-secrets.md (Transit one off sharing), deployment.md (retire the root token) |
| 03 Runtime delivery | connect-applications.md, sdk-integration.md (memory only, K8s auth, AppRole secret ID through the pipeline, never log), external-secrets.md (namespace copy) |
| 04 Rotate and expire | kv-secrets.md, use-case-wordpress-mysql.md (10s refresh, restart), architecture.md (Database engine short lived credentials, token keeps old policies), faqs (leases and renewal), sharing-secrets.md (revoke under Access > Tokens) |
| 05 Least privilege | sharing-secrets.md (narrowest path, verify deny), external-secrets.md (one role per store, ReadWrite label grants nothing), architecture.md (auth methods, audit log), high-availability.md (SIEM) |
| 06 HA and air gapped | high-availability.md (3 nodes, 15 minute snapshots, 14 day expiry, anti affinity, no throughput gain), air-gapped.md (internal registry, 3 of 5 Shamir keys offline), architecture.md (KubeArmor hardening) |

## Gaps the docs flag that the PDF avoids

- Auto unseal through an on premises HSM is unconfirmed in air-gapped.md, so the PDF does not claim it.
- SIEM forwarding method is unconfirmed in high-availability.md, so the PDF says "forward the audit log to your SIEM" with no method.
- The External Secrets Operator version tested with v2.5.4 is unconfirmed, so the PDF names no version.

## Screenshots

| File in img/ | Source | Pixel size | Page |
|---|---|---|---|
| arch.png | docs/secrets-manager/images/sm-architecture-diagram.png | 2560 x 1180 | 4 |
| scan.png | references/PRODUCT UI/1_dashboard/ASPM_Secret Scan Findings_Dash.png, cropped to the top two widgets to drop the contributor emails and repo names | 1615 x 525 | 5 |
| engines.png | sm-select-secret-engine.png, browser bar cropped | 2904 x 920 | 6 |
| flow.png | sm-request-flow.png | 2560 x 720 | 7 |
| versions.png | sm-kv-version-history.png, browser bar cropped | 2904 x 796 | 8 |
| policy.png | sm-share-create-acl-policy.png, browser bar cropped | 2908 x 855 | 9 |
| airgap.png | sm-airgap-flow.png | 2560 x 600 | 10 |
