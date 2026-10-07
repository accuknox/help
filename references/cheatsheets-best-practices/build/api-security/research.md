# API security cheat sheet research

Module: `api-security`. Slug: `api-security-best-practices-guide`. Campaign: `api-security-cheat-sheet`.
Research date: 2026-10-07. Every number below was read on the opened page.

## Problem Data Points

| # | Number | Exact wording on the page | Publisher, year | URL opened |
|---|---|---|---|---|
| 1 | 113% | "The average number of daily API attacks rose 113% year over year." | Akamai, 2026 Apps, APIs, and DDoS SOTI press release, 17 March 2026 | https://www.akamai.com/newsroom/press-release/ai-transformation-at-risk-apis-emerge-as-the-primary-attack-surface-akamai-research-finds |
| 2 | 87% | "87% of surveyed organizations reported experiencing an API-related security incident in 2025." | Akamai, same release, 2026 | same URL as row 1 |
| 3 | 258 vs 121 | "The average number of API attacks per enterprise per day reached 258 in 2025, compared with 121 in 2024." | Help Net Security on the Akamai SOTI report, 19 March 2026 | https://www.helpnetsecurity.com/2026/03/19/akamai-api-attack-trends-report/ |
| 4 | 30.7% | "we found 30.7% more API endpoints through machine learning-based discovery than the self-reported approach" | Cloudflare, 2024 API Security and Management Report, 9 January 2024 | https://blog.cloudflare.com/2024-api-security-report/ |
| 5 | "well over half" | "well over half of the dynamic traffic on our network consists not of web pages, but of Application Programming Interface (API) traffic" | Cloudflare, 2024 | same URL as row 4 |
| 6 | 19% | "Only 19% are 'very confident' in the accuracy of their API inventory" | Salt Security, H2 2025 State of API Security Report, 8 October 2025 | https://salt.security/press-releases/salt-security-report-shows-api-security-blind-spots-could-put-ai-agent-deployments-at-risk |
| 7 | 54% | "more than half (54%) rely on error-prone developer documentation to identify sensitive data exposure" | Salt Security, 2025 | same URL as row 6 |
| 8 | 80% | "80% of organizations lack continuous, real-time API monitoring" | Salt Security, 2025 | same URL as row 6 |
| 9 | OWASP API Top 10 2023 | API9:2023 Improper Inventory Management, API4:2023 Unrestricted Resource Consumption, API1:2023 Broken Object Level Authorization, API3:2023 Broken Object Property Level Authorization | OWASP, 2023 | https://api-security.owasp.org/editions/2023/en/0x11-t10 |

Used in the PDF: rows 1, 4, 6 on page 2. Rows 2, 7, 8, 9 on page 3.

Dropped:

- "57% of dynamic traffic is API". A search snippet gave it, but the opened Cloudflare page says only "well over half".
- The 74%, 92% and 40% figures on accuknox.com/platform/api-security. The page names no survey source.
- "68% of organizations lack visibility into their shadow APIs" in `docs/faqs/api-sec.md`. No source cited.

## Product Truth

| Claim used in the PDF | Source |
|---|---|
| Inventory fills from gateway logs. It shows method, path, request and response bodies, sensitive data classification, internal and external labels | `docs/use-cases/api-security.md` section 2 |
| A collection is created from the host endpoint. Custom collections filter on Host, Name, Regex, Method | `docs/use-cases/api-security.md` section 3 |
| Upload OpenAPI or Swagger in JSON or YAML, up to 3 MB. Same name upload overwrites | `docs/how-to/api-security-onboarding.md` |
| Spec scan classifies Shadow, Zombie, Orphan and Active APIs. Each finding has request, response and occurrence detail | `docs/use-cases/api-security.md` sections 4 to 6 |
| Spec scans run On-demand or Scheduled, on All Endpoints or Specific Collections | `docs/how-to/api-security-onboarding.md` |
| API Scan collector runs active tests on a target URL. Spec scan reports drift, collector reports live weaknesses | `docs/how-to/api-security-onboarding.md` |
| Generate an OpenAPI spec from observed traffic | `docs/getting-started/3.4-release.md`, `docs/faqs/api-sec.md` Q5 |
| Endpoint detail lists sensitive params for request and response | `docs/how-to/api-security-onboarding.md`, PRODUCT UI 4.png |
| Integrations: AWS API Gateway, K8s API proxy, Istio, NGINX Ingress, F5, Kong, NGINX Server, Azure API Management | `docs/integrations/api-overview.md` |
| Rate limiting via `RateLimitPolicy`, per user or IP per endpoint, per user or IP global, global service, Block or Alert | `docs/use-cases/api-security.md`, `docs/getting-started/3.4-release.md`, 3.5 release notes (YAML policy) |
| Finding detail has Create Ticket and Ask AI. Rules Engine creates tickets for matching findings | v3.3 release image-6, `docs/use-cases/rules-engine-ticket-creation.md` |
| Shadow, zombie and orphan detection addresses the OWASP inventory category | `docs/faqs/api-sec.md` Q12 |
| Platform covers OWASP API Top 10, shadow, zombie and orphan APIs, SaaS or on-prem control plane | https://accuknox.com/platform/api-security (scraped 2026-10-07) |

## Proof Row

| Fact | Source |
|---|---|
| Featured in KuppingerCole's 2026 CNAPP Leadership Compass | https://accuknox.com/analyst-recognition |
| Two 2026 Best Practices recognitions, one global and one Asia-Pacific | https://accuknox.com/analyst-recognition |
| 8 API traffic integrations | https://help.accuknox.com/integrations/api-overview/ |

## Screenshots

| File in the PDF | Source | Width px | Page |
|---|---|---|---|
| img/arch.png | docs/integrations/image-17.png | 1777 | 4 |
| img/inventory-crop.png | references/PRODUCT UI/API security/3.png, cropped, cursor removed | 2737 | 5 |
| img/spec-crop.png | docs/getting-started/images/release-notes/v3.3/image-5.png, cropped | 2305 | 6 |
| img/findings-crop.png | docs/how-to/images/api-sec-onboarding/08-api-security-findings.png, cropped | 1839 | 7 |
| img/sensitive-crop.png | references/PRODUCT UI/API security/4.png, detail panel only, half width frame | 1218 | 8 |
| img/scan-crop.png | references/PRODUCT UI/API security/2.png, cropped | 2767 | 9 |
| img/ticket-crop.png | docs/getting-started/images/release-notes/v3.3/image-6.png, cropped | 2849 | 10 |

Skipped: PRODUCT UI 5.png (a third party vendor hostname in the request), 6.png (internal staging hostname), v3.3 image-4 (customer hostnames).
