# DSPM cheat sheet research

Module: DSPM. Slug: `dspm-best-practices-guide`. Campaign: `dspm-cheat-sheet`. Opened 2026-10-07.

## Problem data points

Every number below was read on the page named. Primary sources are marked.

| # | Number | Exact wording | Publisher, year | URL opened | Used on |
|---|---|---|---|---|---|
| 1 | 54% | "This year, 54% of cloud data was classified as sensitive, up from 47% in 2024." | Thales, 2025 Cloud Security Study blog (Todd Moore, 8 July 2025). Primary | https://cpl.thalesgroup.com/blog/data-security/cloud-security-study-2025-key-insights | Page 2 |
| 2 | 37% | "Only 37% of breached organizations stated that they encrypt sensitive data both at rest and in transit" | IBM newsroom, Cost of a Data Breach 2026 press release, 29 July 2026. Primary | https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average | Page 2 |
| 3 | 43% | "Workers using unapproved AI tools figured in 43% of security incidents, more than double last year's share" | Help Net Security, reporting IBM Cost of a Data Breach 2026, 30 July 2026. Secondary | https://www.helpnetsecurity.com/2026/07/30/ibm-cost-of-a-data-breach-2026/ | Page 2 |
| 4 | 8% | "Only 8% of organizations encrypting 80% or more of their cloud data" and "nearly half of all sensitive data stored in the cloud remains unencrypted." | Thales, 2025 Cloud Security Study blog. Primary | https://cpl.thalesgroup.com/blog/data-security/cloud-security-study-2025-key-insights | Page 3 |
| 5 | 85 | "Enterprises now use an average of 85 SaaS applications, contributing to security tool sprawl." | Thales newsroom, 2025 Cloud Security Study press release. Primary | https://cpl.thalesgroup.com/about-us/newsroom/thales-2025-cloud-security-study-reveals-ai-tool-sprawl-security-gap | Page 3 |
| 6 | 52% | "Customer personally identifiable information (PII) was the most frequently compromised data type, accounting for 52% of stolen or exposed data, averaging $192 per record." | Network World (Michael Cooney, 29 July 2026), reporting IBM Cost of a Data Breach 2026. Secondary | https://www.networkworld.com/article/4202554/ibm-ai-driven-attacks-increased-56-last-year-and-data-breach-costs-are-up-12.html | Page 3 |
| 7 | 247 days | Mean time to identify and contain: "247 days, reversing five straight years of decline" | Help Net Security, reporting IBM Cost of a Data Breach 2026. Secondary | https://www.helpnetsecurity.com/2026/07/30/ibm-cost-of-a-data-breach-2026/ | Page 3 |
| 8 | $4.99M | Global average cost of a data breach, "a 12% increase over last year and a record high" | IBM, Cost of a Data Breach Report 2026 landing page. Primary | https://www.ibm.com/reports/data-breach | Not used, kept as backup |

Dropped:

- IBM 2026 "53% did not encrypt sensitive data at rest and in motion, 10% unsure". Network World and search snippets carry it, but the IBM press release states the same fact as "only 37% encrypt both". The PDF uses the primary IBM wording.
- IBM 2025 "62% of shadow AI incidents involved data across multiple environments and public cloud". Only secondary pages carried it, and the 2026 report replaced it.
- No 2026 IBM figure on "shadow data" as a separate category was found on any opened page, so the PDF makes no shadow data stat claim.

## Product truth

Help docs opened:

- `docs/getting-started/dspm-overview.md` (help.accuknox.com/getting-started/dspm-overview/). Scanner runs in your region on a VM or Kubernetes CronJob, read only, nightly, up to 10,000 rows per table and files up to 100 MB. 283 data classes, confidence tiers Very likely, Likely, Possible, default floor Likely. 62 country packs. 282 of 283 classes carry regulation clauses. Filter findings by framework. Limitation: shows where regulated data sits, does not assess controls. Not supported: Google Cloud Storage, SMB or NFS shares, Oracle Database, Snowflake. Values masked to last four characters. Console can run on premises or air gapped.
- `docs/getting-started/dspm-onboarding.md` (help.accuknox.com/getting-started/dspm-onboarding/). Five steps, read only grants per store, one VM per region. Review in Issues > Findings > Data Security Findings filter. Finding detail: severity, SLA, sensitivity, Create Ticket, Ask AI, Status, Ignored, Location, Solution tab. Triage order: Critical and Restricted, then largest match counts, then oldest against SLA. Last detected stops advancing once data is masked, moved or deleted. Add ignored values to the allow list.
- `docs/use-cases/prompt-firewall-overview.md`. Anonymize masks PII and PHI, Secrets blocks API keys and tokens, input and output inspection, block, sanitize or monitor. Warning: guardrails are probabilistic.
- `docs/use-cases/cloud/aws-storage.md`. CSPM finds publicly exposed S3 buckets, create a ticket, follow remediation, verify.
- `docs/faqs/ai-security.md` Q12. Prompt Firewall detects PII, PHI, API keys and credentials in prompts and responses.
- Other grep hits (secret scanning, container image sensitive data tab, API security sensitive data, CSPM permission tables, VM use cases) mention sensitive data in passing and add no DSPM fact.

Product UI opened (`references/PRODUCT UI/DSPM (Data Security)`):

- `onboarding/3.png`. Configure Data Security for S3: include buckets by tag and by name pattern, Scan Publicly Exposed buckets, Allow AccuKnox AI to scan results to reduce false positives. Data sources listed: AWS S3, AWS RDS, AWS Knowledge Base. The left half shows an access key ID, so only the right panel is used.
- `onboarding/1.png`. Shows a real AWS account ID and Azure subscription IDs. Skipped.
- `asset/1.png`, `asset/2.png`, `asset/3.png`. Asset overview with sensitive records by type, tags, security configuration (encryption, public accessibility), evidence per file, risks such as "A data asset is public" and "An unencrypted data asset can be accessed by identities". Demo data.
- `finding/1.png`, `finding/3.png`. Findings grouped by name, sensitive records by PCI, PII, PHI, Compliance filter, compliance frameworks on a finding (PCI DSS, SOC 2, HIPAA).
- `dashboard/DSPM Dashboard.png`. Shows bucket names with account numbers. Skipped.
- `arch-diagram.png`. Shows GCP, Snowflake, NFS and SMB sources that the docs list as not supported. Skipped to avoid a false coverage claim.

accuknox.com opened through `site_assets.py` (Firecrawl): https://accuknox.com/platform/dspm returns 200, title "AccuKnox DSPM - Data Security Posture Management Platform". Facts: 283 data classes, 159 detectors, 62 country packs, 16 compliance framework groups, read only, stays in region, findings only leave. Page also lists Access and Permissions (user to asset mapping, over permission detection) and "Sensitive data reaches AI through datasets, prompts and shadow tools". The site nav marks Data Security (DSPM) as BETA under Security Roadmap.

https://accuknox.com/analyst-recognition returns 200. Fact used: "Featured in KuppingerCole's 2026 CNAPP Leadership Compass".
