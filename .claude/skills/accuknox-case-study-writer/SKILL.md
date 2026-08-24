---
name: accuknox-case-study-writer
description: >
  Write an AccuKnox customer case study. Use this skill whenever the user asks
  for a case study, a customer story, a customer win writeup, a POC writeup, a
  success story, or a reference story for AccuKnox. Triggers include "write a
  case study on X", "customer story for X", "turn this POC into a case study",
  "we won X, write it up", or pasting POC results and asking for a customer
  page. Carries the exact section order of the live accuknox.com case studies,
  the intake list of what the writer must supply, the anonymisation rules and
  the structural validator.
trigger: /ak-case-study
---

# AccuKnox case study writer

A case study answers one question for a buyer who is midway through an
evaluation. Did somebody like me get a result out of this, and how fast.

Repo root: `D:\Atharva\AccuKnox\HelpDocs`.
Shared harness: `.claude/skills/accuknox-blog-writer/`. Paths below written as
`<harness>/` mean that folder.

## Load the writing chain first

1. `.claude/core/runtime-contract.md`
2. `.claude/core/writing-rules.md`, sections 1, 9 and 10 carry this channel
3. `.claude/core/restraint-rules.md`
4. `<harness>/references/house-style.md`, the watermarks and the layout
5. `references/case-study-layout.md` in this skill

Print the `Loaded` block above the draft.

Two rules outrank everything here. **No figure, module name, timeframe, cloud,
compliance framework or customer claim without a source the user supplied or a
document you opened**, and a visible bracket where the fact is missing. **No
unredacted customer data**, in text or in a screenshot. A case study is the one
channel where the second rule gets tested every time.

## Ask for the intake before you write a word

A case study is 90% supplied facts. Without them there is nothing to write, so
ask for all of it in one message and wait. Mark anything the user leaves blank
as a visible bracket in the draft rather than inventing it.

**Identity and permission**

1. **Customer name**, and whether it can be published. If not, give the
   descriptor to use: `Top #3 Indian Public Sector Bank`, `UAE Islamic Bank`,
   `AI Healthcare Innovator`. Sector plus region plus a size marker.
2. **Sector and region.** Banking, insurance, healthcare, fleet and logistics,
   telecom, SaaS. India, UAE, Sri Lanka, Singapore, US.
3. **Quote clearance.** A named person with a title, or `Security Leadership`
   where the name cannot be published. Both appear on live pages.

**The environment**

4. **Clouds and platforms.** AWS, Azure, GCP, on-prem, air-gapped. Name the
   services: AKS, EKS, ACR, CloudTrail, VPC Flow Logs, Azure Event Hub.
5. **Deployment model.** SaaS, on-prem, air-gapped, hybrid. Air-gapped is a
   headline in itself.
6. **Scale.** Subscriptions, clusters, projects, workloads, users. A number here
   is worth three adjectives.

**The story**

7. **Four to six challenges**, each with the business consequence, not only the
   technical gap. `No unified visibility across 6 Azure subscriptions` is the
   gap. `to continuously validate posture against Azure CIS, PCI, and SOC 2
   Type II` is why it mattered.
8. **Four to six solutions.** Which AccuKnox modules, deployed where, doing
   what. Use the canonical module names: CSPM, KSPM, CWPP, ASPM, CIEM, KIEM,
   CDR, SIEM, CTEM, DSPM, AI-SPM, AI-DR, Prompt Firewall, AI Red Teaming,
   KubeArmor, KnoxGuard.
9. **Four to six outcomes, at least three carrying a number and a unit.**
   `7-day end-to-end deployment`, `300+ unique vulnerabilities`, `10 projects
   scanned`, `$1B+ in secured operations`. The validator fails a draft with
   fewer than three.
10. **Compliance frameworks touched.** CERT-In, RBI IT Framework, ISO 27001,
    PCI DSS, SOC 2 Type II, HIPAA, SSDF, EO 14028.
11. **What it replaced**, if anything. Wazuh, Snyk, a manual process. A
    displacement is the strongest line in a case study.
12. **The PDF.** If marketing already produced one, give the filename so the
    draft links `https://accuknox.com/wp-content/uploads/<name>.pdf`.

Ask once. Do not re-ask mid-draft, and skip the ask entirely when the user says
to go with your recommendation.

## Write it

**1. Check the customer is not already published.**

```bash
grep -i "<customer or sector>" <harness>/sources/case-study.md
```

**2. Read the layout.** `references/case-study-layout.md` in this skill carries
the section order, the stat-tile rule, the bullet shape and the quote format,
all derived from the four most recent live pages.

**3. Pull the supporting facts.** Module behaviour comes from this repo, not
from memory:

```bash
grep -n "CSPM\|KSPM\|SBOM" mkdocs.yml
python <harness>/scripts/fetch_md.py case-studies/sbom-india-bank --headings
```

**4. Pick one or two images.** `<harness>/references/asset-kit.md`. A case study
carries at most two, and a console screenshot showing the customer's own data is
never one of them.

```bash
cd <harness>
python scripts/drive_sync.py check
python scripts/drive_sync.py search "compliance report"
```

**5. Copy the template and fill it.**

```bash
cp .claude/skills/accuknox-case-study-writer/assets/case-study-template.md \
   references/case-study-drafts/<slug>.md
```

**6. Write pass 1, then read it cold**, then fix, then gate. The three questions
are in the runtime contract.

## The gates

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/check_asset.py <draft.md> --channel case-study   # CRITICAL 0
python scripts/verify_links.py <draft.md> --fix-suggestions     # 0 broken
python scripts/slop.py <draft.md>                               # adjusted CRIT 0
```

Then section 5 of `.claude/core/restraint-rules.md` by reading.

The anonymisation check is the one that matters most here. `check_asset.py`
fails the draft when `anonymized: true` and the body still names the customer,
but it cannot see a customer name burned into a screenshot. Look at every image
yourself.

## Output

Google Doc by default, same path as the blog writer:

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/to_gdoc_html.py <draft.md>
python scripts/to_gdoc_html.py <draft.md> --print-title
```

Then `create_file` with `contentMimeType: "text/html"`. A revision means
`create_file` again plus `trash_file` on the old id, because the Drive connector
cannot replace a Doc body.

Reply with the Doc URL, the local markdown path, the gate results, and a plain
list of every bracket left for a human.

## What the template already adds

WordPress injects the three stat tiles (**37+ Native Integrations**, **89%
Fewer False Positives**, **91% Reduced Remediation Time**) and the **More Case
Studies** block. Those are site constants, not per-customer numbers. Write
neither, and never restate one of those three figures as if the customer
measured it.

## Files in this skill

| Path | What it holds |
| --- | --- |
| `references/case-study-layout.md` | The section order and every rule, from the four newest live pages |
| `assets/case-study-template.md` | The file you copy to start a draft |

Everything else comes from `<harness>/`: `references/house-style.md`,
`references/source-of-truth.md`, `references/asset-kit.md`, `sources/`,
`media/`, and the scripts.

## Related

- `.claude/skills/accuknox-press-release-writer/`, the announcement that pairs
  with a customer win
- `.claude/skills/accuknox-blog-writer/`, the shared harness
- `.claude/core/runtime-contract.md`, the accuracy and safety rules
