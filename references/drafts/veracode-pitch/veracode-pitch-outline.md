# AccuKnox for Veracode, Pitch Deck Outline

The built deck is `AccuKnox_Veracode_Pitch.pptx` in this folder. It has 17 slides: the template cover, 15 content slides and the template closing slide. Each slide's speaker notes hold the full source list. The screenshots come from the `references/PRODUCT UI` folder and show demo tenant data.

## Slide 1. Cover

- Title: AccuKnox for Veracode. Container, IaC, CSPM, DSPM and API Security.
- Subtitle: Partner briefing, October 2026.
- Layout: the template Intro Title, with its badges and screenshot collage left unchanged.

## Slide 2. Agenda

- 01 The Problem: risk after the commit. Slide 3.
- 02 Our Solution: four products, one platform. Slides 4 to 7.
- 03 Architecture: technical, deployment and modes. Slides 8 to 10.
- 04 Use Cases and POC: scenarios with pass checks. Slides 11 and 12.
- 05 User Journey: the console, step by step. Slide 13.
- 06 Why AccuKnox: differentiators, ranking and pricing. Slides 14 to 16.

## Slide 3. The Problem We Solve

- Kicker: Code findings stop at the commit. Risk keeps moving to production.
- Diagram: eight stages, each with its risk.
  - Source code has flaws in your code.
  - IaC has public buckets and hardcoded secrets.
  - CI/CD ships vulnerable base images.
  - The registry holds images nobody rescans.
  - Runtime sees execution from /tmp and crypto-mining.
  - Cloud accounts carry misconfiguration and drift.
  - Data stores hold PII and PCI data in open buckets.
  - APIs include shadow APIs with no auth.
- Callout: AccuKnox tracks each finding from the first commit to live production, in one console.
- Source: accuknox.com/differentiators, plus the use-case pages named in the notes.

## Slide 4. Container Security and IaC

- KubeArmor blocks the attack inline, before the process runs.
- The Runtime Verified flag marks CVEs that execute in production and cuts CVE noise by up to 100x.
- AccuKnox scans 8 registries and runs in 10 CI/CD platforms.
- IaC scanning covers 13 formats, including Terraform, Helm and CloudFormation.
- KSPM is agentless and covers the CIS Kubernetes benchmark, KIEM and Pod Security.
- [INSERT SCREENSHOT: references/PRODUCT UI/1_dashboard/ASPM_Container Image_Dash 1.png]
- [INSERT SCREENSHOT: references/PRODUCT UI/1_dashboard/ASPM_IaC Findings_Dash.png]
- Sources: `docs/faqs/runtime-security.md`, `docs/getting-started/3.4-release.md`, `docs/support-matrix/registry.md`, `docs/support-matrix/cicd-support-matrix.md`, `docs/support-matrix/iac.md` and `docs/use-cases/kspm.md`.

## Slide 5. Cloud Security Posture (CSPM)

- Stats: 40+ compliance frameworks, 1,500+ policies and controls, 50+ cloud asset types.
- Onboarding is agentless through read-only cloud APIs. On AWS, AccuKnox uses ReadOnlyAccess and SecurityAudit.
- One asset inventory shows list and hierarchy views.
- AccuKnox checks for misconfiguration and drift against baselines, and Monitors watch critical assets.
- The compliance view shows a pass rate per control and drills down per framework.
- Findings become Jira, Freshservice or ConnectWise tickets, and GitOps pull requests fix IaC-managed resources.
- Logos: AWS, Azure, GCP and Oracle.
- [INSERT SCREENSHOT: references/PRODUCT UI/1_dashboard/CSPM Dash 1.png]
- Sources: accuknox.com/differentiators for the 40+ figure, the CSPM POC guide for 1,500+ and 50+, and `docs/faqs/cspm.md`.

## Slide 6. Data Security Posture (DSPM)

- The scanner runs in your region as a VM, a Kubernetes CronJob or a Lambda. It is read-only and opens no inbound ports.
- AccuKnox finds PII, PHI, PCI data and secrets, and gives each finding a confidence tier.
- Values stay masked to the last 4 characters, and rows are discarded after classification.
- Findings map to GDPR, PCI DSS, HIPAA, CCPA and DPDP, with CWE and MITRE.
- Stats: 283 data classes, 62 country packs, 282 classes mapped to regulations.
- [INSERT SCREENSHOT: references/PRODUCT UI/DSPM (Data Security)/dashboard/DSPM Dashboard.png, top section]
- Source: `docs/getting-started/dspm-overview.md`.

## Slide 7. API Security

- AccuKnox discovers every endpoint, with its method, path, bodies and sensitive data labels.
- It sorts APIs into Shadow, Zombie, Orphan and Active against your OpenAPI spec.
- It generates an OpenAPI spec from live traffic.
- Active tests run against a live target URL.
- Each API gets a risk score from its auth, sensitive data, exposure and category.
- Traffic sources: AWS API Gateway, the Kubernetes proxy, Istio, NGINX, Kong and F5 BIG-IP.
- Callout: API Security is priced on unique endpoints, not traffic, and 1 unit is 50 endpoints.
- [INSERT SCREENSHOT: references/PRODUCT UI/API security/3.png]
- Sources: `docs/use-cases/api-security.md`, `docs/how-to/api-security-onboarding.md` and `docs/faqs/api-sec.md`.

## Slide 8. Technical Architecture

- Kicker: Partner findings enter by SARIF or API and get the same correlation as native findings.
- Diagram:
  - Sources: code scanners, CI/CD, registries, Kubernetes, clouds, data stores and APIs.
  - Collect: SARIF and API import, CI plugins and CLI, the KubeArmor agent, agentless scans, the DSPM scanner and API connectors.
  - Control plane: it normalizes, correlates, prioritizes with Runtime Verified, KEV and EPSS, maps findings to 40+ frameworks and runs the rules engine.
  - Act: Jira and ServiceNow, SIEM, Slack, reports and Ask AI.
- Sources: `docs/getting-started/sarif-findings.md` and `docs/getting-started/accuknox-arch.md`. A CLI integration takes 1 sprint. An API integration takes 2 to 3 weeks.

## Slide 9. Deployment Architecture

- Kicker: Posture scans need no agent. Only runtime enforcement runs one.
- Diagram:
  - Kubernetes runs the KubeArmor DaemonSet and the KSPM job.
  - CI/CD pipelines run scans and upload SARIF.
  - Cloud accounts use a read-only role.
  - The data region runs the DSPM scanner.
  - API gateways connect through connectors.
  - All five send findings to the control plane.
- Runtime enforcement keeps working if the control plane is down.
- Sources: `docs/faqs/cspm.md`, `docs/getting-started/dspm-overview.md` and `docs/faqs/deployment.md`.

## Slide 10. Deployment Modes

- SaaS puts the control plane in the AccuKnox cloud. Setup takes the same day with no install, and it suits a fast proof of concept.
- Your Cloud puts the control plane in your cloud account. No data leaves, and it suits data residency.
- On-Premises puts the control plane on your servers. The install is native, with no SaaS agent, and it suits banking, healthcare and telecom.
- Air-Gapped puts the control plane in an isolated network. It sends no outbound traffic and suits federal, defense and ITAR work.
- Callout: The platform, the policies and the price stay the same in all four modes.
- Sources: accuknox.com/differentiators ("Your Cloud. Your data. Your AI.") and the Pricing and Sizing sheet.

## Slide 11. Use Cases

- Block a vulnerable image: a GitHub Actions scan stops node:18-alpine. Tag: Container.
- Catch a public bucket in IaC: a Terraform bucket set to public-read gets flagged. Tag: IaC.
- Close a public S3 bucket: CSPM finds the bucket and remediation closes public access. Tag: CSPM.
- Find PCI data before an audit: scan a database replica, then filter by framework. Tag: DSPM.
- Expose shadow APIs: upload a spec, scan, and list the Shadow and Orphan APIs. Tag: API Security.
- One view for partner findings: import SARIF from any tool next to native findings. Tag: Platform.

## Slide 12. POC Scenarios

- Five-day timeline: Day 1 onboarding, Days 2 to 3 scan results, Days 3 to 4 asset inventory, Days 4 to 5 findings by category.
- A SaaS POC takes 1 to 2 weeks. An on-prem POC takes 2 to 3 weeks.
- Container test: run /tmp execution and a crypto-miner under a block policy. Pass: both processes are blocked.
- CSPM test: make one S3 bucket public. Pass: the top 20 findings are ranked by Day 3 and the bucket is reverted in 60 seconds.
- DSPM test: scope S3 by tag and include public buckets. Pass: PII and PCI findings show per bucket.
- API test: upload a spec and connect a gateway. Pass: Shadow and Orphan APIs are listed.
- The help docs define no formal success criteria, so agree them with Veracode before Day 1.

## Slide 13. User Journey in the Console

1. Add a source. [INSERT SCREENSHOT: collectors/Collectors 1.png]
2. See the posture. [INSERT SCREENSHOT: 1_dashboard/CNAPP_Dashboard_1.png]
3. Walk the assets. [INSERT SCREENSHOT: security graph/Security Graph 1.png]
4. Rank the findings. [INSERT SCREENSHOT: 3_issues/Issues_2.png]
5. Score compliance. [INSERT SCREENSHOT: 5_compliance/Compliance 1.png]
6. Report and ticket. [INSERT SCREENSHOT: 10_reports/Reports 1.png]

## Slide 14. Key Differentiators

- Stats: 3 to 5x tools replaced, 80% alert reduction, 40+ frameworks.
- Inline prevention blocks threats before they run, at the kernel.
- Code to cloud: AccuKnox tracks each finding from commit to production.
- One data layer lets you add a module with no re-integration.
- AccuKnox runs anywhere: public, private, on-prem and air-gapped.
- Open formats connect your tools: SARIF, syslog, CEF and webhooks.
- The open source core is KubeArmor, with 2M+ downloads.
- Source: accuknox.com/differentiators and `docs/faqs/general.md`.

## Slide 15. Stack Ranking for Veracode

| Rank | Module | Why in this order | Footprint | 1 unit |
|---|---|---|---|---|
| 1 | Container + IaC | Runs in the same pipelines as code scans | CI plugin, Helm agent | 1 node, 40 images, 30 repos |
| 2 | API Security | Tests the live endpoints the code becomes | Gateway connector | 50 endpoints |
| 3 | CSPM | Checks the cloud the code deploys into | Agentless, read-only | 10 assets |
| 4 | DSPM | Finds the sensitive data behind the app | Scanner in your region | [Sales to confirm] |

- Callout: Start with one module. Add the next one on the same data layer, with no re-integration.

## Slide 16. Pricing

- Price per unit per month, in USD:
  - Tier 1, 10 to 50 units: $40.
  - Tier 2, 51 to 250 units: $34.
  - Tier 3, 251 to 750 units: $29.
  - Tier 4, 751 to 2,500 units: $25.
  - Tier 5, 2,501 to 5,000 units: $21.
  - Tier 6, 5,001 units and up: negotiated.
- One unit covers 10 CSPM assets, 1 CWPP or KSPM node, 40 container images, 30 repos for IaC, SAST and secrets, or 50 API endpoints.
- [FILL: DSPM unit. The sheet has no DSPM divisor. Sales to confirm.]
- Support: Silver is included. Gold adds 10%. Platinum adds 25% and covers 24x7.
- Deployment: on-premises costs $0 and shared SaaS costs $0. A dedicated tenant costs $3,000 a month plus 10%.
- Source: AccuKnox - Pricing & Sizing - SEP 2026.xlsx.

## Slide 17. Closing

- SEE US IN ACTION. support@accuknox.com.
