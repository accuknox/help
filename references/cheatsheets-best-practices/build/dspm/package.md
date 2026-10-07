# DSPM cheat sheet package

PDF: `references/cheatsheets-best-practices/output/2026-10-07-dspm-best-practices-guide-v3.pdf`, 12 pages.

## 1. Web page metadata

| Field | Value |
|---|---|
| Eyebrow | CHEAT SHEET |
| Title (H1) | DSPM Best Practices: Do's and Don'ts Guide |
| Meta title | DSPM Best Practices Cheat Sheet \| AccuKnox |
| Meta description | Get six DSPM best practices to find, classify and protect sensitive data, with do's, don'ts, AccuKnox screens and a gap check for cloud data stores. |
| Slug | dspm-best-practices-guide |
| URL | https://accuknox.com/cheatsheets/dspm-best-practices-guide/ |
| Tagline (H2) | Find sensitive data before attackers do. |
| Subtitle blurb | This free guide gives clear do's and don'ts for six data security practices, plus a gap checklist. |
| What's new | The first AccuKnox guide to DSPM, with the scanner's read only, in region design and the new Data Security screens. |
| Form image | `output/dspm-best-practices-guide-form-image.png` |
| OG image alt text | Cover of the AccuKnox DSPM best practices cheat sheet, titled Find sensitive data before attackers do. |
| Primary keyword | dspm best practices |
| Secondary keywords | data security posture management, sensitive data discovery, data classification cloud |

What's inside:

- Scan every data store, including public buckets, by tag and name
- Classify by content with country packs and confidence tiers
- Close public and unencrypted stores that hold sensitive records
- Triage findings by severity, sensitivity and SLA
- Mask PII at the AI prompt and map regulated data to frameworks

Note for the web team: the accuknox.com nav lists Data Security (DSPM) as BETA. Keep the landing page wording in line with that label.

## 2. Email

Subject: Find sensitive data before attackers do

Preview text: Six DSPM practices, with do's, don'ts and a gap check you can run this week.

Body:

> Only 37% of breached organizations encrypt sensitive data both at rest and in transit, says IBM's 2026 Cost of a Data Breach study.
>
> Our DSPM cheat sheet gives you do's and don'ts for six practices, from scanning every data store to showing auditors where regulated data sits.
>
> It ends with a six row gap check you can run this week.
>
> [Get the cheat sheet](https://accuknox.com/cheatsheets/dspm-best-practices-guide/?utm_source=email&utm_medium=email&utm_campaign=dspm-cheat-sheet)

HTML: `build/dspm/email.html`, copied to `output/dspm-best-practices-guide-email.html`.

Source for the 37%: IBM newsroom, 29 July 2026, https://newsroom.ibm.com/2026-07-29-ibm-study-one-in-four-malicious-breaches-are-ai-enabled,-costing-companies-6-million-on-average

## 3. LinkedIn post

Body:

```text
Only 37% of breached organizations encrypt sensitive data both at rest and in transit. (IBM, Cost of a Data Breach 2026)

Encryption only helps once you know which store holds the card numbers and the PII.

Our new DSPM cheat sheet covers six practices, each with do's and don'ts:
↳ Scan every data store, including public buckets nobody listed
↳ Classify by content, not by bucket name
↳ Close public and unencrypted stores first
↳ Keep PII and secrets out of AI prompts

Each page shows the AccuKnox screen that checks it.

Grab the free guide via the link in the comments.

#DSPM #DataSecurity #CloudSecurity
```

First comment:

```text
Get the DSPM best practices cheat sheet: https://accuknox.com/cheatsheets/dspm-best-practices-guide/?utm_source=linkedin&utm_medium=social&utm_campaign=dspm-cheat-sheet
```

Image: `output/dspm-best-practices-guide-linkedin.png`. `li.py` appends the leadership roster above the hashtags when the post is scheduled. Nothing is scheduled.

## 4. Images

| Image | File | Size |
|---|---|---|
| Form image | `output/dspm-best-practices-guide-form-image.png` | 1200 x 1697 |
| LinkedIn image | `output/dspm-best-practices-guide-linkedin.png` | 1200 x 1200 |

Rebuild both with `python build/dspm/social/shots.py`.
