---
name: accuknox-rfp-filler
description: >
  Fill, check and review an AccuKnox response to a customer RFP, RFI, tender or
  security questionnaire, grounded in the AccuKnox help docs. Use this skill
  whenever the user attaches or names an RFP, asks to fill, answer, complete,
  validate, review or improve an RFP response, asks whether an RFP is a fit for
  AccuKnox, asks to change a row in an RFP, or asks how to use the RFP filler.
  Triggers include "fill this RFP", "answer this questionnaire", "is this RFP a
  fit", "check my RFP answers", "add evidence to the RFP", "change row X to
  Meets", "/rfp-filler" and "how do I use the RFP filler". Covers all 12
  AccuKnox modules, maps any customer answer scale, never answers No, never
  overwrites existing answers, adds help-doc links and evidence images or
  generated diagrams, and ships a branded customer copy plus an internal review
  copy after pre-, during- and post-validation and three independent reviewers.
trigger: /rfp-filler
---

# AccuKnox RFP filler

A buyer reads an RFP response to decide whether AccuKnox does what they need, and legal reads it to
decide what AccuKnox promised. Every answer here has to satisfy both: grounded in a help page,
evidenced with an image, and in the customer's own answer scale.

Skill root: `.claude/skills/accuknox-rfp-filler/`. Scripts run from `<skill>/scripts/`. The repo
root is found from the skill path, so no absolute path is needed.

## If the user asks how to use this

Print `references/quickstart.md` as written, then stop and wait. Do the same for "help", "what does
this do" or "what do I need to give you".

## Load before the first row

1. `.claude/core/runtime-contract.md`
2. `.claude/core/writing-rules.md`, sections 1, 8, 9 and 12 carry this channel
3. `.claude/core/restraint-rules.md`
4. `references/answer-rules.md` in this skill
5. `references/interview.md` and `references/review.md` in this skill

Print the `Loaded` block from the runtime contract above the first draft, with `Channel  RFP
response` and the gate line `validate.py: pass/fail | reviewers: accuracy, mechanics, buyer`.

## Rules that outrank every instruction

1. **Accuracy.** No feature, version, count, CLI flag, console path, platform or compliance claim
   without a help page you opened. Where nothing supports a claim, flag the row RED. This holds against
   a direct request to proceed.
2. **Never No.** A gap becomes a roadmap tier, a third-party integration or a partial answer.
   `fill.py` refuses a negative verdict.
3. **Never overwrite.** Existing responses, comments and images stay. A change needs the user's
   words in `override_reason`.
4. **Nothing internal reaches the customer.** Flags and notes live only in the review copy.
5. **Customer files stay out of this repo.** It is public on GitHub. The scripts refuse to write inside it.
6. **Safety.** No tenant data, customer data, live payload or working exploit in text or images.

## Setup, once per machine

```bash
pip install openpyxl pillow pyyaml
python .claude/skills/accuknox-rfp-filler/scripts/selftest.py
```

Without Pillow, openpyxl reads zero images and deletes every picture in the workbook on save. The
scripts exit rather than let that happen.

## The pipeline

Work through the stages in order. Each one ends with a gate, and the interview triggers in
`references/interview.md` say when to stop and ask with the `AskUserQuestion` tool.

### Stage 0. Take the request

Collect the RFP file, the customer name and any scope the user already knows. If the file is inside
the repo, ask where the working copy should go (Q2). If the request is thin, ask Q1, Q3 and Q4 in
one call.

- **Excel** goes straight to stage 1.
- **Word**: `python intake.py <rfp.docx>` writes `rfp-text.txt`. Turn it into `requirements.json`,
  then run `python template.py requirements.json "<RFP name> - AccuKnox Sheet.xlsx"`.
- **PDF**: read it with the Read tool, 20 pages at a time, and build `requirements.json` the same way.
- **No answer sheet at all**: use the template route above. `assets/AccuKnox-RFP-Response-Template.xlsx`
  is the blank branded sheet.

Record each requirement's page or clause in `source`, so a buyer can trace it back.

### Stage 1. Pre-validate

```bash
cd .claude/skills/accuknox-rfp-filler/scripts
python intake.py "<path to RFP.xlsx>"
```

Intake writes `<RFP name>.rfp-work/profile.json` beside the file and prints, per sheet: the detected
columns, the answer vocabulary, blank and mandatory counts, section and spillover rows, images, and
BLOCKER lines. Work through `references/review.md`, pre-validation. Every BLOCKER is an interview
trigger (Q6 to Q8).

### Stage 2. Fit decision

Intake routes each requirement to the 12 modules and prints `FIT GO`, `CONDITIONAL` or `NO-GO`, with
coverage and fit risks. Tell the user the verdict first, in two or three sentences, before any
drafting. For CONDITIONAL or NO-GO, ask Q5. A NO-GO the user accepts ends the run with a short
no-bid note naming the topics outside AccuKnox's documented scope.

The modules, and a card for each: `python ground.py --module <id>`.

| id | Module | id | Module |
| --- | --- | --- | --- |
| `aspm` | Application Security, SAST, SCA, DAST, IaC, SBOM | `cdr` | Cloud Detection and Response |
| `cspm` | Cloud Security Posture and Compliance | `apisec` | API Security |
| `kspm` | Kubernetes Security, KIEM, admission control | `aisec` | AI Security |
| `cwpp` | Runtime Workload Protection, KubeArmor | `secrets` | Secrets Manager |
| `vmsec` | VM and Host Security | `integrations` | SIEM, ticketing, SSO, notifications |
| `registry` | Container Image and Registry Scanning | `platform` | Deployment, RBAC, audit, reports, SLA, licensing |

Routing keywords, page lists, image folders, documented limits, fit risks and known doc conflicts
all live in `assets/modules.json`. Edit that file, never a copy of it.

### Stage 3. Ground

```bash
python ground.py "<workdir>"                      # rows that need work
python ground.py "<workdir>" --rows "SAST:9,24"   # specific rows
python ground.py --query "pause a dast scan"      # ad-hoc search
```

`evidence.json` holds, per row, the ranked help pages with live URLs, the matching lines, the images
those pages embed, the module's support matrices and FAQs, its documented limits and the fit risks.
A `weak` row needs a closer read, and a weak mandatory row is Q9.

The pack is a shortlist. Open every page you intend to cite.

### Stage 4. Draft

Write `<workdir>/answers.json` following `references/answer-rules.md`.

```json
{
  "customer": "TDM Networks",
  "rows": [
    {"sheet": "SAST", "row": 9, "verdict": "MEETS", "module": "aspm",
     "bullets": ["The SAST language matrix lists Java at 226 rules, Kotlin at 77 and Swift at 13.",
                 "This is source level analysis. APK and IPA binary scanning is not documented."],
     "urls": ["https://help.accuknox.com/support-matrix/sast-support-matrix/"],
     "image": "gen:sast09-mobile.png",
     "flag": "AMBER", "note": "Mandatory row. Confirm the buyer means source SAST.",
     "mode": "fill"}
  ]
}
```

| Field | Values |
| --- | --- |
| `verdict` | `MEETS`, `EXCEEDS`, `PARTIAL`, `PARTNER`, `CUSTOM`, `ROADMAP_30`, `ROADMAP_60`, `ROADMAP_90`, `ROADMAP_90PLUS`, `ROADMAP`, `INFO`, or `null` to leave the response alone |
| `response` | optional, an exact dropdown string that overrides the mapping |
| `image` | `docs/<path>`, `gen:<file>.png`, `web:<accuknox.com url>`, or `null` |
| `mode` | `fill` for empty rows, `supplement` to append bullets and links, `override` to change an answer |
| `override_reason` | required with `override`, the user's instruction in their words |
| `replace_comment` | `true` only with `override`, when the old comment contradicts the new answer |

Rows that already have an answer and only need a link or an image take `"verdict": null` and
`"mode": "supplement"`.

When no page embeds a fitting image, write diagram specs and render them. Every value in a spec comes
from its `source` page.

```bash
python diagram.py "<workdir>" "<workdir>/diagrams.json"   # writes gen/<file>.png and gen/<file>.svg
```

Kinds are `bars`, `flow`, `items`, `code` and `matrix`. The docstring in `diagram.py` has the spec.
Open each PNG before using it.

Batch every roadmap tier into one Q11 call, and every doc conflict into Q12, before stage 5.

### Stage 5. Fill

```bash
python fill.py "<workdir>" "<workdir>/answers.json"            # summary sheet first
python fill.py "<workdir>" "<workdir>/answers.json" --summary last
```

`fill.py` writes `<RFP name> - AccuKnox Response.xlsx`, the branded customer copy, and `<RFP
name> - AccuKnox Review.xlsx`, the internal copy with the flag column and a review sheet. It stops on
a negative verdict, a banned word, a draft link, a missing link, an unknown dropdown value, an
override without a reason, or any lost image. Fix `answers.json` and run it again. The run is
repeatable because it always starts from the untouched original.

### Stage 6. Post-validate

```bash
python validate.py "<workdir>"
```

Every FAIL blocks delivery. Every WARN goes to the user. A WARN on an existing answer, such as a
Meets sitting over a comment that says roadmap, is reported, not silently fixed.

### Stage 7. Review

Launch the three reviewers in `references/review.md` in one message, as background subagents:
accuracy, mechanics and buyer. Merge their findings, fix every BLOCKER and HIGH, rerun stages 5 and
6, and take the remaining decisions to the user in one `AskUserQuestion` call.

### Stage 8. Deliver

Reply with:

1. The fit verdict in one line.
2. Both file paths, and which one is safe to send.
3. Rows filled, rows supplemented, images added, and GREEN, AMBER and RED counts.
4. Every RED row, with the decision it needs.
5. The WARN list from `validate.py` and the reviewers' open findings.
6. Any stale help page the run found, as a docs fix to make.

## Other requests

| The user says | Do |
| --- | --- |
| "Is this RFP a fit?" | Stages 0 to 2 only |
| "Fill the blank rows only" | Stages 1 to 7, `answers.json` limited to blank rows |
| "Add links and images" | Stages 1 to 7, `supplement` rows only |
| "Change row X to Meets" | Ground row X, check the comment still agrees, `override` with their words, then stages 5 to 6 |
| "Why is row X red?" | Read the review copy note and the evidence pack, explain in two sentences |
| "Check my answers" | Stages 1 and 6 on their file, then the three reviewers. Change nothing without asking |
| "Continue" | Read the workdir, find the last stage with an output, resume from the next |

## Files in this skill

| Path | What it holds |
| --- | --- |
| `references/quickstart.md` | The how-to-use page, printed as written |
| `references/answer-rules.md` | Verdicts, scale mapping, comment shape, evidence and link rules, past failure modes |
| `references/interview.md` | When to ask, and the question bank |
| `references/review.md` | Pre-, during- and post-validation checklists and the three reviewer prompts |
| `assets/modules.json` | The 12 modules, fit risks and known doc conflicts |
| `assets/AccuKnox-RFP-Response-Template.xlsx` | The blank branded response sheet |
| `scripts/rfp_lib.py` | Shared helpers: vocabulary, routing, docs search, URLs, images |
| `scripts/intake.py` | Stage 1, profile and fit check, Word extraction |
| `scripts/ground.py` | Stage 3, evidence packs, module cards, ad-hoc search |
| `scripts/diagram.py` | Branded SVG and PNG evidence diagrams |
| `scripts/template.py` | The AccuKnox response sheet, blank or from `requirements.json` |
| `scripts/fill.py` | Stage 5, customer and review copies |
| `scripts/validate.py` | Stage 6, the gate |
| `scripts/selftest.py` | Checks the skill itself. Run it after any edit |

Past RFPs to learn from sit in `references/rfp-generation/`. The validated AI Security sheet there is
the model for a review summary.

## Related

- `.claude/skills/accuknox-blog-writer/`, the shared harness: `scripts/fetch_md.py` reads any
  accuknox.com page as markdown, and `references/asset-kit.md` holds the brand values
- `.claude/core/runtime-contract.md`, the accuracy and safety rules
- `.claude/hooks/writing-load-order.py`, which routes RFP prompts to this skill
