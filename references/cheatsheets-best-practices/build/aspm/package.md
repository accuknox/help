# ASPM cheat sheet package

PDF: `output/2026-10-07-aspm-best-practices-guide-v3.pdf` (13 pages). Campaign: `aspm-cheat-sheet`.

## 1. Web page metadata

| Field | Value |
|---|---|
| Eyebrow | CHEAT SHEET |
| Title (H1) | ASPM Best Practices: Do's and Don'ts Guide |
| Meta title | ASPM Best Practices Cheat Sheet \| AccuKnox |
| Meta description | Get seven ASPM do's and don'ts for SAST, DAST, SCA, IaC, secrets, SBOM and ticketing, plus a gap check that maps each gap to its first step. Free PDF. |
| Slug | aspm-best-practices-guide |
| URL | https://accuknox.com/cheatsheets/aspm-best-practices-guide/ |
| Tagline (H2) | Fix the flaws attackers can really reach. |
| Subtitle blurb | This free guide gives clear do's and don'ts for seven ASPM practices, plus a gap checklist. |
| Form image | `output/aspm-best-practices-guide-form-image.png` |
| OG image alt text | Cover of the AccuKnox ASPM best practices cheat sheet, titled Fix the flaws attackers can really reach. |
| Primary keyword | ASPM best practices |
| Secondary keywords | application security posture management, EPSS vulnerability prioritization, secret scanning in CI/CD |

What's inside:

- One findings queue for SAST, DAST, SCA, IaC, secrets and containers
- Fix order set by EPSS and runtime evidence, not CVSS alone
- Secret scanning and pipeline gates that observe first, then enforce
- SBOM per build, with version comparison and license findings
- A seven row gap check with the first step for each gap

What's new: The first AccuKnox guide that takes ASPM from the first commit to the closed ticket, with 2026 data from Verizon, GitGuardian and Datadog.

Meta description length: 150 characters. Meta title: 42 characters. H1: 42 characters.

## 2. Email

- Subject: 7 ASPM practices in one cheat sheet
- Preview text: 48,244 CVEs landed in 2025. Here is how to choose which ones to fix first.

Body:

> The CVE Program published 48,244 CVE records in 2025. Most teams see their share of them split across separate scanner consoles.
>
> Our new cheat sheet gives seven practices for application security posture management. It covers one findings queue, EPSS based priority, secret scanning, pipeline gates, SBOMs and owned tickets.
>
> It ends with a seven row gap check you can run with your team this week.
>
> [Get the cheat sheet]

Button link: `https://accuknox.com/cheatsheets/aspm-best-practices-guide/?utm_source=email&utm_medium=email&utm_campaign=aspm-cheat-sheet`

HTML: `build/aspm/email.html`, copied to `output/aspm-best-practices-guide-email.html`.

## 3. LinkedIn post

Post type: ebook promo. Audience: AppSec and DevSecOps leads. CTA: link in comments. The `accuknox-linkedin-post` skill appends the leadership roster when it schedules the post through `li.py`, so the roster is not typed here. Image: `output/aspm-best-practices-guide-linkedin.png`.

```
28.6 million new secrets landed in public GitHub commits in 2025, up 34% in one year (GitGuardian, 2026). 🔐

Most teams find them in one console, their CVEs in another and IaC issues in a third. Nobody owns the total.

The AccuKnox ASPM Best Practices Cheat Sheet is live:

↳ One findings queue for SAST, DAST, SCA, IaC, secrets and containers
↳ Fix order set by EPSS and runtime evidence, not CVSS alone
↳ Pipeline gates that observe first, then enforce

It ends with a seven row gap check you can run this week.

Grab the guide via the link in the comments.

#ASPM #DevSecOps #AppSec #SecretsManagement
```

First comment:

```
Get the ASPM Best Practices Cheat Sheet: https://accuknox.com/cheatsheets/aspm-best-practices-guide/?utm_source=linkedin&utm_medium=social&utm_campaign=aspm-cheat-sheet
```

## 4. Images

| Image | File | Size |
|---|---|---|
| Form image, PDF cover | `output/aspm-best-practices-guide-form-image.png` | 1200 x 1699 |
| LinkedIn image | `output/aspm-best-practices-guide-linkedin.png` | 1200 x 1200 |

The LinkedIn card source is `build/aspm/social/linkedin.html`, rendered with Playwright.
