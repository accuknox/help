# API security cheat sheet package

PDF: `references/cheatsheets-best-practices/output/2026-10-07-api-security-best-practices-guide-v2.pdf` (12 pages).

## 1. Web Page Metadata

| Field | Value |
|---|---|
| Eyebrow | CHEAT SHEET |
| Title (H1) | API Security Best Practices: Do's and Don'ts Guide |
| Meta title | API Security Best Practices Cheat Sheet \| AccuKnox |
| Meta description | Free API security cheat sheet with do's and don'ts for shadow API discovery, OpenAPI spec checks, sensitive data and routing each finding to an owner. |
| Slug | api-security-best-practices-guide |
| URL | https://accuknox.com/cheatsheets/api-security-best-practices-guide/ |
| Tagline (H2) | Find and fix every API you run. |
| Subtitle blurb | This free guide provides clear do's and don'ts for six API security practices, plus a gap checklist. |
| What's new | Adds API security to the cheat sheet series, with practices drawn from the AccuKnox API Security docs. |
| Form image | `output/api-security-best-practices-guide-form-image.png` |
| OG image alt text | Cover of the AccuKnox API security best practices cheat sheet, titled Find every API before an attacker does. |
| Primary keyword | api security best practices |
| Secondary keywords | shadow api detection, zombie api, openapi spec validation |

What's inside:

- Do's and don'ts for six API security practices
- How to find shadow, zombie and orphan APIs
- How to use your OpenAPI spec as a scan baseline
- How to spot sensitive data in API requests and responses
- A checklist that matches each API gap to a first step

## 2. Email

HTML: `build/api-security/email.html`, copied to `output/api-security-best-practices-guide-email.html`.

Subject: Find every API before attackers do

Preview text: Six practices to find shadow APIs, check traffic against your spec and close findings.

Body:

> Cloudflare found 30.7% more API endpoints through discovery than teams reported on their own.
>
> Our new cheat sheet gives you do's and don'ts for six API security practices.
>
> Find shadow and zombie APIs, check live traffic against your OpenAPI spec, and route each finding to an owner.
>
> [Get the cheat sheet](https://accuknox.com/cheatsheets/api-security-best-practices-guide/?utm_source=email&utm_medium=email&utm_campaign=api-security-cheat-sheet)

Source line in the footer: Cloudflare, 2024 API Security and Management Report.

## 3. LinkedIn Post

Post type: ebook promo. Image: `output/api-security-best-practices-guide-linkedin.png`. `li.py` appends the leadership roster, so it is not typed here.

```text
Daily API attacks rose 113% year over year, per Akamai's 2026 State of the Internet report.

Cloudflare found 30.7% more API endpoints through discovery than teams had reported.

Our new API security cheat sheet gives you six practices:
↳ Build the inventory from live gateway and mesh traffic
↳ Compare that traffic to your OpenAPI spec to find shadow and zombie APIs
↳ Route every finding to an owner, with a ticket and a rate limit

Each practice has 4 do's, 3 don'ts and the first step to take this week.

Grab the free guide via the link in the comments.

#APISecurity #OWASP #CloudSecurity
```

First comment:

```text
Get the API security best practices cheat sheet: https://accuknox.com/cheatsheets/api-security-best-practices-guide/?utm_source=linkedin&utm_medium=social&utm_campaign=api-security-cheat-sheet
```

## 4. Images

| Image | Path | Size |
|---|---|---|
| Form image | `output/api-security-best-practices-guide-form-image.png` | 1200 px wide, cover at 2x |
| LinkedIn image | `output/api-security-best-practices-guide-linkedin.png` | 1200 x 1200 |

Both images build from `build/api-security/social/cover.py`, `build/api-security/social/linkedin.html` and `build/api-security/social/li.py`.
