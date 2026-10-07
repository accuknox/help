# CIEM cheat sheet package

PDF: `references/cheatsheets-best-practices/output/2026-10-07-ciem-best-practices-guide-v4.pdf`, 12 pages.

## 1. Web page metadata

| Field | Value |
|---|---|
| Eyebrow | CHEAT SHEET |
| Title (H1) | CIEM Best Practices: Do's and Don'ts Guide |
| Meta title | CIEM Best Practices Cheat Sheet \| AccuKnox |
| Meta description | Get six CIEM best practices for cloud and Kubernetes identities, with do's, don'ts, AccuKnox screens and a gap check that cuts unused access. |
| Slug | ciem-best-practices-guide |
| URL | https://accuknox.com/cheatsheets/ciem-best-practices-guide/ |
| Tagline (H2) | Cut the cloud access nobody uses. |
| Subtitle blurb | This free guide gives clear do's and don'ts for six cloud and Kubernetes identity practices, plus a gap checklist. |
| What's new | The first AccuKnox guide to cover CIEM and KIEM together, with the beta CIEM screens. |
| Form image | `output/ciem-best-practices-guide-form-image.png` |
| OG image alt text | Cover of the AccuKnox CIEM best practices cheat sheet, titled Cut the access your identities never use. |
| Primary keyword | ciem best practices |
| Secondary keywords | cloud infrastructure entitlement management, least privilege cloud iam, kubernetes rbac best practices |

What's inside:

- Inventory every human and machine identity in four clouds
- Retire dormant identities with lifecycle data
- Rank identities by risk class, privilege escalation first
- Read policy documents and trace access through groups
- Review Kubernetes RBAC with KIEM, plus a six row gap check

Note for the web team: CIEM is beta in the docs. `https://accuknox.com/platform/ciem` returns 404 on 2026-10-07, so the page links to the help docs instead.

## 2. Email

Subject: Cut the cloud access nobody uses

Preview text: Six CIEM practices, with do's, don'ts and a gap check you can run this week.

Body:

> Microsoft found only 2% of 51,000 granted cloud permissions were used. The rest stay live on users, roles and service accounts.
>
> Our CIEM cheat sheet gives you do's and don'ts for six practices, from the identity inventory to Kubernetes RBAC.
>
> It ends with a six row gap check you can run this week.
>
> [Get the cheat sheet](https://accuknox.com/cheatsheets/ciem-best-practices-guide/?utm_source=email&utm_medium=email&utm_campaign=ciem-cheat-sheet)

HTML: `build/ciem/email.html`, copied to `output/ciem-best-practices-guide-email.html`.

Source for the 2%: Microsoft, 2024 State of Multicloud Security Risk Report.

## 3. LinkedIn post

Body:

```text
Microsoft found only 2% of 51,000 granted cloud permissions were used.

The rest stay live on users, roles and service accounts. An attacker who takes one identity gets all of it.

Our new CIEM cheat sheet covers six practices, each with do's and don'ts:
↳ Inventory every human and machine identity across AWS, GCP, Azure and OCI
↳ Retire identities nobody has used
↳ Read the policy document, not the policy name
↳ Give Kubernetes RBAC the same review

Each page shows the AccuKnox CIEM or KIEM screen that checks it.

Grab the free guide via the link in the comments.

#CIEM #CloudSecurity #IdentitySecurity
```

First comment:

```text
Get the CIEM best practices cheat sheet: https://accuknox.com/cheatsheets/ciem-best-practices-guide/?utm_source=linkedin&utm_medium=social&utm_campaign=ciem-cheat-sheet
```

Image: `output/ciem-best-practices-guide-linkedin.png`. `li.py` appends the leadership roster above the hashtags when the post is scheduled. Nothing is scheduled.

## 4. Images

| Image | File | Size |
|---|---|---|
| Form image | `output/ciem-best-practices-guide-form-image.png` | 1200 x 1697 |
| LinkedIn image | `output/ciem-best-practices-guide-linkedin.png` | 1200 x 1200 |

Rebuild both with `python build/ciem/social/shots.py`.
