# CWPP best practices cheat sheet, launch package

PDF: `references/cheatsheets-best-practices/output/2026-10-07-cwpp-best-practices-guide-v3.pdf` (12 pages).
Campaign: `cwpp-cheat-sheet`. Sources for every number: `build/cwpp/research.md`.

## 1. Web page metadata

| Field | Value |
|---|---|
| Eyebrow | CHEAT SHEET |
| Title (H1) | CWPP Best Practices: Do's and Don'ts Guide |
| Meta title | CWPP Best Practices Cheat Sheet \| AccuKnox |
| Meta description | Get do's and don'ts for six CWPP runtime controls, from app baselines and hardening to inline blocking, plus a gap check with a first step for each. |
| Slug | cwpp-best-practices-guide |
| URL | https://accuknox.com/cheatsheets/cwpp-best-practices-guide/ |
| Tagline (H2) | Block runtime attacks inside every workload. |
| Subtitle blurb | This free guide provides clear do's and don'ts for six runtime security practices, plus a gap checklist. |
| Form image | `output/cwpp-best-practices-guide-form-image.png` |
| OG image alt text | Cover of the AccuKnox CWPP best practices cheat sheet, titled Stop the attack inside the workload. |
| Primary keyword | cwpp best practices |
| Secondary keywords | runtime security best practices, container runtime security, kubernetes runtime protection |

### What's inside

- Six CWPP practices, from app behavior baselines to BLOCK mode
- How to harden containers with CIS, MITRE and NIST policies
- How to stop cryptominers and lock system files at runtime
- How to segment pod traffic and keep forensics past the pod
- A checklist that matches each runtime gap to a first step

### What's new

The first AccuKnox cheat sheet for runtime security, built on the eight step Runtime Security Journey from audit to BLOCK.

## 2. Email

| Field | Copy |
|---|---|
| Subject | Block runtime attacks, not only alerts |
| Preview text | Six do and don't lists for container runtime security, plus a gap check. |
| Button | Get the cheat sheet |
| Button URL | https://accuknox.com/cheatsheets/cwpp-best-practices-guide/?utm_source=email&utm_medium=email&utm_campaign=cwpp-cheat-sheet |

Body:

> Attackers need about 10 minutes to go from recon to a finished cloud attack (Sysdig, 2023).
>
> A runtime tool that kills the process after the alert is too late. The miner or the shell already ran.
>
> Our new CWPP cheat sheet gives you do's and don'ts for six runtime practices: baseline app behavior, harden workloads, block in the kernel, segment pods, stop miners and keep forensics.
>
> It ends with a gap check that maps each gap to a first step you can take this week.

HTML version: `build/cwpp/email.html`, copied to `output/cwpp-best-practices-guide-email.html`.

## 3. LinkedIn post

Draft only. Not scheduled. `li.py` appends the leadership roster on send, so the roster is not typed here.

```text
Attackers need about 10 minutes to go from recon to a finished cloud attack (Sysdig, 2023).

Most runtime tools kill the process after the alert. By then the miner already ran.

Our new CWPP cheat sheet gives you do's and don'ts for six runtime controls:
↳ Baseline app behavior before you write a rule
↳ Move STABLE policies from AUDIT to BLOCK, enforced in the kernel by KubeArmor
↳ Stop cryptominers and lock system files

It ends with a gap check that maps each gap to a first step.

Grab the free guide via the link in the comments.

#CWPP #RuntimeSecurity #KubeArmor
```

First comment:

```text
Download the CWPP best practices cheat sheet: https://accuknox.com/cheatsheets/cwpp-best-practices-guide/?utm_source=linkedin&utm_medium=social&utm_campaign=cwpp-cheat-sheet
```

Image: `output/cwpp-best-practices-guide-linkedin.png`. Post type: ebook or guide promo. Audience: platform and security engineers who run Kubernetes. CTA: link in the first comment. Source: the PDF and `research.md`. The hook stat is the Sysdig 2023 Global Cloud Threat Report, https://www.sysdig.com/press-releases/2023-cloud-threat-report.

## 4. Images

| Image | Path | Size |
|---|---|---|
| Form image | `output/cwpp-best-practices-guide-form-image.png` | 1200 px wide, PDF cover |
| LinkedIn image | `output/cwpp-best-practices-guide-linkedin.png` | 1200 x 1200 |
