# Help docs striking-distance audit, October 2026

Twenty-one deleted help pages still serve stale copies and still collect Google impressions. This
PR redirects each one to its current page, fixes the page title template, and tunes three titles
and descriptions. It changes no instruction step, heading or body paragraph in the docs.

Source: the Google Search Console Pages and Queries exports for `accuknox.com` and
`help.accuknox.com`, last 3 months, pulled on 2026-10-15. Treg supplied search volume, keyword
difficulty and a live Google SERP check for the top 40 queries.

## Method Follows the GSC Striking-Distance Workflow

A striking-distance page ranks at an average position of 4 to 30 with at least 100 impressions. Each
page gets a review score. Position counts for 50%, impressions for 35% and the gap between expected
and actual clicks for 15%. The fix depends on the position band.

| Band | What the page needs |
|---|---|
| 4 to 10 | A better title and description, and the answer in the first lines |
| 11 to 20 | Missing content and internal links |
| 21 to 30 | A check that the right URL ranks, before any rewrite |

The method comes from three guides: [KairoxBuild](https://kairoxbuild.com/blog/gsc-striking-distance-opportunities),
[SEOTesting](https://seotesting.com/blog/striking-distance-keywords/) and
[Vazoola](https://www.vazoola.com/resources/striking-distance-link-building-targets).

## Help Docs Hold 117 Striking-Distance Pages

The help site has 223 pages in the export, with 126,766 impressions and 1,553 clicks. Of those, 117
pages sit in striking distance with 109,810 impressions.

| Band | Pages | Impressions |
|---|---|---|
| 4 to 10 | 41 | 57,441 |
| 11 to 20 | 60 | 40,418 |
| 21 to 30 | 16 | 11,951 |

## Stale Pages on S3 Take the Rankings From Current Pages

The deploy job runs `aws s3 sync ./site s3://help.accuknox.com` without `--delete`. A page removed
from `docs/` stays on S3 and keeps serving its last build. Forty URLs in the export have no source
file in this repo.

The worst case is DVWA. Two URLs compete for the query `dvwa` (24,965 impressions, position 7.4).

| URL | Impressions | Clicks | Position | State |
|---|---|---|---|---|
| `/use-cases/dvwa/` | 31,665 | 583 | 8.5 | Stale. Canonical points to `accuknox.com/use-cases/dvwa/`, which returns 403 |
| `/getting-started/dvwa/` | 18,226 | 267 | 11.1 | Current page, not in the Google top 30 for `dvwa` |

Google ranks the stale page at position 9 for `dvwa`, and its canonical tag points at a URL that
returns 403. The redirect sends that ranking signal to the current page.

### This PR redirects 21 stale URLs

Each redirect uses the `mkdocs-redirects` plugin that is already in `mkdocs.yml`. The plugin writes
an HTML redirect at the old path, and the next S3 sync overwrites the stale copy with it.

| Old URL | Impressions | New page |
|---|---|---|
| `/use-cases/dvwa/` | 31,665 | `/getting-started/dvwa/` |
| `/integrations/semgrep-sast/` | 2,073 | `/integrations/opengrep-sast/` |
| `/use-cases/host-sec/` | 1,863 | `/use-cases/vm-host-scan/` |
| `/integrations/checkmarx-sca/` | 911 | `/integrations/checkmarx/` |
| `/overview/what-is-cspm/` | 444 | `/use-cases/cspm/` |
| `/overview/defining-runtime-security-and-static-security/` | 376 | `/getting-started/runtime-sec-arch/` |
| `/getting-started/cloud-onboarding/` | 376 | `/how-to/high-level-onboarding/` |
| `/overview/what-is-cwpp/` | 351 | `/use-cases/cwpp/` |
| `/introduction/accuknox-architecture/` | 277 | `/getting-started/accuknox-arch/` |
| `/use-cases/malware-scan/` | 198 | `/use-cases/vm-malware-scan/` |
| `/getting-started/sbom/` | 164 | `/getting-started/xbom-setup/` |
| `/use-cases/use-cases-home/` | 132 | `/use-cases/` |
| `/getting-started/cluster-onboarding/` | 106 | `/how-to/cluster-onboarding/` |
| `/how-to/dast-baseline-vs-full/` | 142 | `/how-to/dast-scan-types/` |
| `/how-to/vm-onboarding-getting-started/` | 86 | `/how-to/vm-onboard-deboard-systemd/` |
| `/getting-started/on-prem-prereq/` | 68 | `/getting-started/on-prem-overview/` |
| `/use-cases/bifrost-integration/` | 61 | `/integrations/bifrost-integration/` |
| `/getting-started/kubearmor-support-matrix/` | 46 | `/support-matrix/kubearmor-support-matrix/` |
| `/knoxctl/knoxctl-install/` | 41 | `/knoxctl/` |
| `/integrations/jira-cloud-cwpp/` | 41 | `/integrations/jira-cloud/` |
| `/getting-started/gar/` | 1 | `/how-to/gar/` |

### Nineteen stale URLs stay out of this PR

These URLs have no clear current page, or the plugin cannot redirect them.

- `/overview/cnapp-definition/` (1,624 impressions, position 26.3). No current page defines CNAPP.
  The docs team decides whether to restore a definition page or point it at `accuknox.com/platform/cnapp`.
- The `/saas/*` pages (9 URLs, 499 impressions in total). They describe the old SaaS console and
  have no one-to-one page today.
- `/getting-started/gcp-asset-count/` (121 impressions). `resources/count-assets.md` covers AWS only.
- Eight PDF files under `/how-to/` and `/getting-started/images/`. The plugin redirects pages, not
  files. An S3 or CloudFront rule handles these.

## The Title Template Added a Stray Hyphen to Every Page

`site_name` in `mkdocs.yml` is empty, so the Material theme rendered every title as
`Page title - `. The homepage title was `AccuKnox Help Center - `. A new `htmltitle` block in
`overrides/main.html` renders `Page title | AccuKnox Docs` and keeps the homepage as
`AccuKnox Help Center`. The visible page, the header and the navigation stay the same.

## Three Pages Get a New Title or Description

| Page | Field | Change | Evidence |
|---|---|---|---|
| `getting-started/dvwa.md` | Title | `DVWA (Damn Vulnerable Web Application) on Kubernetes` | `dvwa` 24,965 impressions. `damn vulnerable web application` has 2,400 US searches at KD 13 |
| `getting-started/dvwa.md` | Description | Names the deploy, the SQL injection and command injection tests, and the CWPP block | Matches `what is dvwa`, `dvwa sql injection` and `dvwa walkthrough` |
| `use-cases/epss-scoring.md` | Title | `EPSS vs CVSS: Vulnerability Prioritization with CWE` | Page at position 22.3 on 3,629 impressions. `cvss vs epss` at position 14.2 |
| `integrations/checkmarx.md` | Description | Lists SAST, SCA, KICS and container scan, as the H1 does | `checkmarx sca` at position 19.0. The old description named SAST only |

## Five Follow-Ups Need an Owner

1. Add `--delete` to the S3 sync, or add an S3 lifecycle check for orphaned files. Stale pages come
   back each time a page is deleted without a redirect. A wrong `--delete` removes live assets, so
   test it against a copy of the bucket first.
2. Redirect the eight PDF URLs with an S3 website rule or a CloudFront function.
3. `integrations/aws-kubearmor/` ranks at 6.8 on 3,137 impressions with 1 click. The query that
   triggers it is not in the export. Pull the query-by-page report for that URL in Search Console
   before you change the title.
4. `use-cases/crypto-mining/` ranks at 21.5 on 2,711 impressions. The query `cryptojacking` has
   1,604 impressions at 20.3, and `accuknox.com/blog/cryptojacking-threat-prevention` competes for
   it. Decide which site owns the term, then link the other page to it.
5. Request a re-crawl in Search Console for `/getting-started/dvwa/` and `/use-cases/dvwa/` after
   this deploys. Compare impressions and position for `dvwa` 28 days later.
