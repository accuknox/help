# Review pipeline and checklists

Three checklists and three reviewers. The checklists run in the main session. The reviewers are
separate subagents, so none of them grades its own work.

## Pre-validation, before drafting

Run `intake.py`, then confirm each line.

- [ ] Pillow, openpyxl and PyYAML import. `rfp_lib.require_pillow()` exits if Pillow is missing.
- [ ] The RFP and its work folder are outside the help-docs repo.
- [ ] Every sheet shows the right requirement, response, comment and evidence columns.
- [ ] The dropdown vocabulary is mapped, and no option is left unmapped.
- [ ] The scale's negative option is known, so nobody picks it by accident.
- [ ] Section rows, spillover rows and extra tables are identified and agreed with the user.
- [ ] The fit verdict is shared with the user, and a CONDITIONAL or NO-GO is decided.
- [ ] Existing answers are counted. The plan says which rows get filled and which get supplemented.

## During-validation, while drafting

For every row, before it goes into `answers.json`:

- [ ] The pages in the evidence pack were opened, not only the snippets.
- [ ] The verdict answers the literal requirement.
- [ ] Every number, version, flag and console path is on a page you opened.
- [ ] The image was opened and shows the claim. No tenant data. No v3.7 draft.
- [ ] The link is a published page, and a feature page where one exists.
- [ ] The flag and the note say exactly what a reviewer needs to check.
- [ ] Rows that answer similar requirements get the same verdict class.

`fill.py` enforces the mechanical half and stops on a negative verdict, a banned word, a draft link,
a missing link, an unknown dropdown value, or an override without a reason.

## Post-validation, after filling

`validate.py <workdir>` runs these checks and writes `validation-report.md`.

| Check | Fails the run |
| --- | --- |
| Original file unchanged | yes |
| Responses are dropdown options | yes |
| No negative answer written | yes |
| No blank requirement rows | yes |
| Existing answers untouched unless overridden | yes |
| Every filled comment has a link | yes |
| No banned words in added text | yes |
| Answer dropdowns preserved | yes |
| Images preserved and valid | yes |
| Customer copy has no internal notes | yes |
| No links to drafts, and every link resolves | yes |
| Answer and comment agree | warns |
| Similar requirements answered alike | warns |
| New images fit their rows | warns |
| RED rows and mandatory rows that are not GREEN | warns |

A WARN goes to the user in the final reply. It does not block the files.

## The three reviewers

Launch all three in one message, in the background, after `validate.py` passes. Pass each one the
workdir path. If a reviewer dies on an API error, relaunch it once. A reviewer that fails twice is
reported as not run, never as passed.

### Reviewer 1, accuracy

```text
You are an adversarial accuracy reviewer for an AccuKnox RFP response. A wrong claim is a
contractual exposure, so default to doubt.

Workdir: <WORKDIR>. Read fill-manifest.json for the filled rows and the customer copy it names.
Docs root: <REPO>/docs. Live URL rule: docs/<path>.md is https://help.accuknox.com/<path>/.

For every filled row, open the linked pages and check each claim in the comment: feature names,
console paths, CLI flags, config keys, versions, counts, supported platforms. Grep the wider docs
too. Check that the response value is defensible and that the requirement is answered as written.

Report only problems, as: sheet, row, the exact claim, BLOCKER / WARN / NIT, what the docs say with
the file path, and the corrected sentence. End with the counts.
```

### Reviewer 2, mechanics

```text
You are a mechanical reviewer for an AccuKnox RFP response. Pillow must import before openpyxl.

Workdir: <WORKDIR>. Run: python <SKILL>/scripts/validate.py <WORKDIR>
Then open both output files named in fill-manifest.json and check what the script cannot:
every new image shows what its row claims, no image carries tenant or customer data, no text is
clipped, the summary sheet renders cleanly, and the review sheet lists every RED row.

Report a table of check, PASS or FAIL, detail with sheet and row. Fix nothing.
```

### Reviewer 3, buyer

```text
You are a skeptical procurement evaluator scoring a vendor's RFP response. You are not the vendor.

Workdir: <WORKDIR>. Read profile.json for every requirement, and the customer copy named in
fill-manifest.json. Treat the review copy's notes as the vendor's private admissions.

Find: answers to a different question than the one asked; Meets or Exceeds answers whose own note
admits a material gap; roadmap answers that look like a No; mandatory rows at risk of
disqualification; contradictions between rows and sheets; hedging or apologetic bullets.

Rank each finding HIGH, MEDIUM or LOW, with the rewrite you would want. End with how many rows you
would score full, partial and zero.
```

## After review

1. Merge the three reports. Fix every BLOCKER and HIGH by editing `answers.json` and running
   `fill.py` and `validate.py` again.
2. Take every open decision to the user with one `AskUserQuestion` call. See Q11, Q12 and Q15.
3. Reply with both file paths, the flag counts, the fit verdict, the open RED rows, the WARN list,
   and any stale docs page the run found.
