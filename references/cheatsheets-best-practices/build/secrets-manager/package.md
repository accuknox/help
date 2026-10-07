# Package, secrets management best practices cheat sheet

PDF: `output/2026-10-07-secrets-management-best-practices-guide-v2.pdf`, 12 pages. Campaign: `secrets-manager-cheat-sheet`.

## 1. Web page metadata

| Field | Value |
|---|---|
| Eyebrow | CHEAT SHEET |
| Title (H1) | Secrets Management Best Practices: Do's and Don'ts Guide |
| Meta title | Secrets Management Best Practices Cheat Sheet \| AccuKnox |
| Meta description | Get do's and don'ts for six secrets management practices, from finding leaked keys to runtime delivery, rotation and least privilege, plus a gap check. |
| Slug | `secrets-management-best-practices-guide` |
| URL | `https://accuknox.com/cheatsheets/secrets-management-best-practices-guide/` |
| Tagline (H2) | Find, store and serve every secret safely. |
| Subtitle blurb | This free guide gives clear do's and don'ts for six secrets management practices, plus a gap checklist that maps each gap to AccuKnox Secrets Manager. |
| Form image | `output/secrets-management-best-practices-guide-form-image.png` |
| OG image alt text | Cover of the AccuKnox secrets management best practices cheat sheet, titled Keep every secret out of your code. |
| Primary keyword | secrets management best practices |
| Secondary keywords | hardcoded secrets in code, secret rotation best practices, Kubernetes secrets management |

**What's inside**

- Find leaked keys in code, commit history and CI/CD pipelines
- Move every secret into one versioned, encrypted store
- Serve secrets at runtime through the SDK or External Secrets
- Rotate, expire and scope each app to its own paths
- Run the store highly available, backed up and air gapped

**What's new.** The guide pairs each practice with the Secrets Manager setup page that closes the gap, including the air gapped install.

## 2. Email

| Field | Value |
|---|---|
| Subject | Leaked secrets stay valid for years |
| Preview text | 64% of secrets valid in 2022 still worked in 2026. Six practices close the gap. |
| Button | Get the cheat sheet, to `https://accuknox.com/cheatsheets/secrets-management-best-practices-guide/?utm_source=email&utm_medium=email&utm_campaign=secrets-manager-cheat-sheet` |

Body:

> Developers added 28.65 million new hardcoded secrets to public GitHub commits in 2025, according to GitGuardian.
>
> Over 64% of the secrets found valid in 2022 still worked in January 2026.
>
> Our free cheat sheet gives you the do's and don'ts for six practices: find leaked keys, centralize storage, serve secrets at runtime, rotate, scope access and run the store highly available.
>
> Each practice ends with the AccuKnox Secrets Manager setup page, and a gap check shows where to start.

HTML: `build/secrets-manager/email.html`, copied to `output/secrets-management-best-practices-guide-email.html`.

## 3. LinkedIn post

Image: `output/secrets-management-best-practices-guide-linkedin.png`. `li.py` appends the leadership roster, so it is not typed here.

```text
28.65 million new hardcoded secrets hit public GitHub commits in 2025, up 34% year over year (GitGuardian).

Over 64% of the secrets found valid in 2022 still worked in January 2026.

Our new cheat sheet gives you the do's and don'ts for six practices:

↳ Find keys already leaked in code and pipelines
↳ Serve secrets at runtime, not from env files
↳ Rotate, scope and run the store highly available

Each practice maps to AccuKnox Secrets Manager, with a gap check at the end.

Grab the free guide via the link in the comments.

#SecretsManagement #DevSecOps #Kubernetes
```

First comment:

```text
Get the secrets management best practices cheat sheet: https://accuknox.com/cheatsheets/secrets-management-best-practices-guide/?utm_source=linkedin&utm_medium=social&utm_campaign=secrets-manager-cheat-sheet
```

## 4. Images

| Image | Path | Size |
|---|---|---|
| Form image, PDF cover | `output/secrets-management-best-practices-guide-form-image.png` | 1200 x 1699 |
| LinkedIn image | `output/secrets-management-best-practices-guide-linkedin.png` | 1200 x 1200, source `build/secrets-manager/social/linkedin.html` |

## Open items for a human

- The landing page URL does not exist yet. The email button and the LinkedIn comment point at it.
- Several Secrets Manager help pages are new and uncommitted. The PDF links them at their nav paths, so they go live only after the docs merge.
