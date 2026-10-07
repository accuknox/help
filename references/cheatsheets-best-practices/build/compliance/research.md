# Research: cloud compliance (GRC) best practices cheat sheet

Module: `compliance`. Slug: `cloud-compliance-best-practices-guide`. Campaign: `compliance-cheat-sheet`.
Researched 2026-10-07. Every number below was read on the page named in its URL.

## Problem data points (used in the PDF)

| # | Number | Exact wording | Publisher, year | URL opened |
|---|---|---|---|---|
| 1 | EUR 1.2 billion | "European supervisory authorities issued fines totalling approximately EUR1.2 billion (USD1.42 billion/GBP1.06 billion) in 2025" | DLA Piper, GDPR Fines and Data Breach Survey, January 2026 | https://www.dlapiper.com/en/insights/publications/2026/01/dla-piper-gdpr-fines-and-data-breach-survey-january-2026 |
| 2 | 443 per day | "Between 28 January 2025 and 27 January 2026, the average number of breach notifications per day increased by 22% – from 363 to 443." | DLA Piper, January 2026 | same URL |
| 3 | EUR 7.1 billion | "The aggregate total fines reported since the application of GDPR on 25 May 2018 to 10 January 2026 across all the jurisdictions surveyed now stands at EUR7.1 billion" | DLA Piper, January 2026 | same URL |
| 4 | 74% | "nearly all organizations (97%) now conduct at least two audits annually, with 74% of large enterprises managing four or more" | A-LIGN, 2026 Compliance Benchmark Report, published 2026-01-28, 1,043 respondents | https://www.a-lign.com/articles/a-lign-releases-2026-compliance-benchmark-report |
| 5 | 97% | same sentence as row 4 | A-LIGN, 2026 | same URL |
| 6 | 11 working weeks | "11 working weeks a year are spent on compliance tasks—increasing by 1 week since last year" | Vanta, State of Trust Report 2024 (Sapio Research, 2,500 business and IT leaders, US, UK, Australia), published 2024-10-23 | https://www.vanta.com/resources/state-of-trust-report-2024-vantacon-agenda |
| 7 | 3 to 5 hours a week | "Respondents say they could save between 3-5 hours each week—up to 5 working weeks a year—if security and compliance tasks were automated" | Vanta, 2024 | same URL |
| 8 | 72% | "72% of organizations recognize that compliance programs must evolve to keep pace with increasingly complex requirements" | A-LIGN, 2026 | same URL as row 4 |

## Dropped, could not confirm on a primary page

- IBM Cost of a Data Breach 2025, "32 percent paid a regulatory fine". Read only on a law firm summary (bakerdonelson.com). The IBM report page and the IBM newsroom release did not show it. Dropped.
- "Noncompliance costs 2.71 times more than compliance". Ponemon and Globalscape, 2017. Only seen in a search snippet. Too old and not opened. Dropped.
- "4,300 hours a year on audit preparation" and "67% of evidence is similar across frameworks". Search snippets with no primary source. Dropped.
- Scrut 2026, "92% manage two or more frameworks". Survey of Scrut customers only, so it does not describe a typical firm. Dropped.
- AccuKnox FAQ claim "60 hours to under 5 hours per quarter" for an unnamed financial services client. No named customer or public case study. Not used.

## Product truth (help docs)

| Claim used in the PDF | Source |
|---|---|
| More than 1,000 out of the box checks, each mapped to one or more compliance programs and sub controls | https://help.accuknox.com/use-cases/compliance/ |
| Score per sub control = passed checks / (passed + failed + warning + not available) | same page |
| Detailed View filters by cloud account, region, severity and checks | same page |
| Framework lists per cloud (AWS 28, Azure 25, GCP 25 in the support matrix table) | same page and https://help.accuknox.com/support-matrix/compliance-matrix/ |
| Kubernetes CIS Benchmarking job, onboarded from Settings > Manage Clusters, with a scan schedule. GKE based benchmarking for managed GKE clusters today | https://help.accuknox.com/how-to/cis-benchmarking/ |
| VM Scanner ships CIS and DISA STIG profiles for Ubuntu 22.04 and 24.04. 1020 controls, 479 automated, 541 manual review. Manual controls report as skipped, never as a pass | https://help.accuknox.com/use-cases/vm-compliance-benchmarking/ |
| Custom reports: on demand or scheduled daily, weekly or monthly, emailed to recipients. Support configures a custom template from the backend | https://help.accuknox.com/how-to/custom-reports/ |
| Summary report widgets: new critical findings, findings fixed, critical findings unticketed, weekly trends | https://help.accuknox.com/how-to/summarized-custom-reports/ |
| Scheduled CSPM and ASPM reports, versioned, for SOC 2, ISO 27001 and other frameworks (v3.2) | docs/getting-started/3.2-release.md |
| Cloud Compliance report: one account against many frameworks, or one framework across many accounts (v3.5) | docs/getting-started/3.5-release.md |
| Findings lifecycle: Active on first scan, Waiting for Verification when absent on the second, Fixed after the third. Manual statuses include Accepted Risk and Exception Requested. Create Ticket to Jira, ServiceNow and others | https://help.accuknox.com/how-to/findings-lifecycle/ |
| Rules Engine creates tickets for findings that match conditions, with an expiration date | https://help.accuknox.com/use-cases/rules-engine-ticket-creation/ |
| Drift: group assets, apply a baseline conformance on a schedule, and Monitors alert on configuration change in critical assets such as an S3 bucket or a bastion | https://help.accuknox.com/use-cases/cloud-misconfigurations/ |

## accuknox.com (fetched through Firecrawl, cited with site_assets.py)

| Fact | URL (final, after redirect) |
|---|---|
| `platform/grc` redirects to `platform/compliance`, title "Governance, Risk & Compliance With AccuKnox Security" | https://accuknox.com/platform/compliance |
| "Continuously map controls to NIST/CIS/PCI/SOC2, collect evidence, monitor drift, and auto-remediate via IaC workflows." Workload, Cloud and AI compliance. Customizable frameworks | same |
| "33+ global compliances". The list page shows 51 entries | https://accuknox.com/compliance |
| Featured in KuppingerCole's 2026 CNAPP Leadership Compass | https://accuknox.com/analyst-recognition |
| AI Copilot cited for drift remediation, "continuously comparing cloud assets to IaC templates" | same |

## Screenshots

| File in `img/` | Source | Width px | Check |
|---|---|---|---|
| frameworks-list.png | PRODUCT UI/5_compliance/Compliance 1.png, cropped | 3250 | Design mock, Contoso placeholder accounts |
| framework-catalog.png | Compliance 3.png, dialog crop | 2126 | Clean |
| benchmark-insights.png | Compliance 2.png, cropped | 3250 | Clean |
| k8s-cis-finding.png | docs/how-to/images/cis-benchmarking/8.png, drawer crop | 1344 | Shows DO-demo-cluster only, list with names cropped out. Shown at 130 mm |
| scheduled-reports.png | PRODUCT UI/10_reports/Reports 1.png, cropped | 3250 | Clean. Reports 3 and 4 skipped, they show a personal email |
| finding-ticket.png | Compliance 4.png, drawer crop, account value blurred | 1780 | Account ID blurred |
| compliance-summary.png | docs/use-cases/images/compliance-summary.png, cropped | 1860 | Account already pixelated in source |

Skipped: every file under `10_reports/customer reports`. VM STIG screens in the docs show a hostname named after a person. The cluster onboarding screen shows a join token.
