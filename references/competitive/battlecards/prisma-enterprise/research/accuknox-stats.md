---
title: AccuKnox Stats Check for the Prisma Cloud Enterprise Page
checked: 2026-09-30
scope: The three "Why Customers Choose" stats on the live AccuKnox vs Prisma Cloud Enterprise page
---

# AccuKnox Stats Check for the Prisma Cloud Enterprise Page

The help docs support none of the three stats as written. Two stats need a new number, and one stat needs a source outside the help docs.

| Live stat | Verdict | Replace with | Source | Tier |
|---|---|---|---|---|
| Over 45 compliance frameworks | Unsourced, and higher than every help doc | 33+ compliance frameworks, or 40+ benchmarks if you count each version | `docs/faqs/compliance.md`, `docs/support-matrix/compliance-matrix.md` | D |
| KubeArmor has over 1 million downloads | Understated. The help docs say 2 million+ | 2 million+ downloads | `docs/faqs/general.md` | D |
| 91% less remediation time, 89% fewer false positives | Unsourced in the help docs. The numbers come from one accuknox.com case study | Keep the numbers, and name the case study | accuknox.com SBOM case study, Indian public sector bank | I |

## The Help Docs Support 33+ Frameworks, Never 45

No help doc says 45. The FAQ says "33+ compliance frameworks" twice, on [Compliance FAQs](https://help.accuknox.com/faqs/compliance/). The [CSPM use case](https://help.accuknox.com/use-cases/cspm/) and the [GRC page](https://help.accuknox.com/use-cases/compliance/) say "30+". The resources page links to a "List of 33+ Compliance Frameworks" on accuknox.com.

The [Compliance Matrix](https://help.accuknox.com/support-matrix/compliance-matrix/) holds 42 rows. Several rows are versions of one benchmark. AWS CIS has 4 versions, Azure CIS has 3, GCP CIS has 3 and ISO 27001 has 2. Collapse the versions and 34 distinct frameworks remain.

So the matrix row label "Cloud Compliance Frameworks (35+)" is also one higher than the docs. Change it to "33+". Use "40+ benchmarks" only when the page says that it counts each version.

## The Help Docs Say KubeArmor Passed 2 Million Downloads

[General FAQs](https://help.accuknox.com/faqs/general/), question 2, says KubeArmor is "a CNCF Sandbox project with 2 million+ downloads and 1,000+ GitHub stars". So "over 1 million" is true but undersells the documented figure. Neither fact file in `references/source-of-truth/` gives a download count.

The same FAQ answer also lists "Cloud Native Computing Foundation Incubating Project" under awards. Every other help page calls KubeArmor a CNCF Sandbox project. Use "CNCF Sandbox" until product confirms a change.

## The 91% and 89% Figures Come From One Bank Case Study

No help doc and no fact file holds 91% or 89%. The figures appear on the accuknox.com case study "Top #3 Indian Public Sector Bank Operationalises SBOM in an Air-Gapped Environment". The repo copy is `references/Website Pages to Build 26 September/Scripts/scrape/accuknox_com_case_studies_sbom_india_bank.md`. It shows "89% Fewer False Positives" and "91% Reduced Remediation Time". The PDF is at `https://accuknox.com/wp-content/uploads/SBOM-Case-Study.pdf`.

These are single-customer results, so the live page must not present them as platform averages. Write "one public sector bank cut remediation time by 91%" and link the case study. The page cannot link a help doc for these numbers.

Do not confuse these figures with the "89% uptime" stat for IDT Telecom in the accuknox.com nav, or with the "up to 95%" false-positive reduction in [AI Security FAQs](https://help.accuknox.com/faqs/ai-security/).
