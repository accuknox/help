# Answer rules

How to turn an evidence pack into a response a buyer scores well and legal can stand behind. Read
this before drafting the first row.

## 1. Pick the verdict from the evidence, then map it

Decide in AccuKnox terms first. `fill.py` maps the verdict onto the customer's own dropdown.

| The docs show | Verdict | Flag |
| --- | --- | --- |
| The capability, as asked, with a page and a screenshot | `MEETS` | GREEN |
| The capability plus clearly more than asked, and you can name the extra | `EXCEEDS` | GREEN |
| The capability, but narrower than the requirement reads | `MEETS` with the limit stated in a bullet | AMBER |
| The capability through a named integration, webhook or partner | `PARTNER` | AMBER |
| Part of it today, the rest nowhere | `PARTIAL` if offered, else a roadmap tier | AMBER |
| Nothing today, and the roadmap FAQ or product lists it | `ROADMAP_30` to `ROADMAP_90PLUS` | AMBER, RED until a date is confirmed |
| Nothing anywhere | `ROADMAP_90PLUS` | RED. Ask before sending |

`NEGATIVE` does not exist here. `fill.py` stops the run if it sees one.

When the customer's scale lacks the verdict you picked, `fill.py` degrades it and writes why into the
review note:

- A missing roadmap tier falls to the next available tier.
- A scale with no roadmap option falls to Partial, then Need More Info.
- A Yes/No scale leaves only Yes. The row goes RED and needs a human, because Yes plus a roadmap
  sentence is still a claim.

Roadmap tiers are promises. Propose them, mark them, and get the date confirmed before sending.

## 2. Answer the literal question

Read the requirement twice. The most common way to lose a row is a correct answer to a different
question.

- "Delta analysis between scans" asks for scan-to-scan comparison, not reporting.
- "Integrate with Eclipse, IntelliJ, Visual Studio" names IDEs. A VS Code extension does not answer
  it on its own.
- "Mobile application code analysis" can mean source SAST or APK and IPA testing. Say which one you
  answer.

If the requirement is ambiguous and the verdict depends on the reading, ask the user.

## 3. The comment

Match the house shape the team already uses in these sheets.

```text
- One fact per bullet, with the exact feature, console path, CLI flag or integration name.
- Two to four bullets. The first one answers the question.
- A scope limit, when there is one, gets its own plain bullet.

https://help.accuknox.com/<page>/
```

- Name things. `Settings > Collectors > Trigger Scan` beats "the platform supports rescans".
- Numbers come from the page you opened, today. A past RFP said "more than 33 compliance frameworks"
  where the validated AI Security sheet counted about 41. Re-count every time.
- No absolutes you cannot prove. A past RFP said runtime security "can prevent all types of attacks",
  which no page supports.
- No em dashes and none of the ten banned words. `fill.py` stops on them.
- The link goes last, on its own line. Add a second link when a second page carries a different part
  of the answer.

## 4. Existing answers

The customer, or an earlier AccuKnox draft, may have filled rows already.

- **Never change an existing response** unless the user asks in this conversation. Record their
  words in `override_reason`. The change is logged in the review copy.
- **Never rewrite an existing comment.** Append links. Append bullets only with `mode: supplement`.
- **Replace a comment only with `mode: override` and `replace_comment: true`**, and only when the
  old text contradicts the new response. A Meets answer sitting on "this is not currently
  available" is the typical case.
- **Report what you find.** An existing Meets over a comment that says roadmap is a contradiction.
  `validate.py` lists these. Raise them with the user rather than fixing them quietly.

## 5. Evidence images

Try the sources in this order and stop at the first one that proves the claim.

1. **An image embedded in the page you cite.** `ground.py` lists them per page. This is the right
   image by construction.
2. **The module's image folders** in `assets/modules.json`.
3. **`references/brian-demo-screenshots/`**, curated AI Security screenshots with captions in
   `DEMO-SUMMARY.md`.
4. **accuknox.com**, as `web:<url>`. `rfp_lib.py` accepts only accuknox.com hosts.
5. **A generated diagram** with `diagram.py`, built only from values on the cited page, with that page
   in its footer.

Open every image before you use it. Check that it shows the claimed capability, that it carries no
customer or tenant data, and that it is not under `release-notes/v3.7/` or any other unpublished draft.

## 6. Links

- `help.accuknox.com` is the primary source. `rfp_lib.doc_url()` maps a docs path to its live URL.
- A feature page beats a release note. Cite a release note when it is the only page with the fact.
- `accuknox.com` is secondary. Use it for positioning and for modules the help docs cover thinly.
  Read any page as markdown by adding `.md`, or with
  `.claude/skills/accuknox-blog-writer/scripts/fetch_md.py`.
- Never cite `getting-started/3.7-release.md` or anything under `release-notes/v3.7/`. They are drafts.

## 7. When the docs disagree

`assets/modules.json` keeps a `_conflicts` list. Known cases include MFA for DAST, M365 SSPM and
DSPM. The rule:

1. Prefer the newer page, by `git log -1 --format=%ad -- <file>`.
2. Flag the row AMBER and name both pages in the review note.
3. Add the stale page to the review summary so someone fixes the docs.
4. Ask the user when the older page is the one a buyer is likely to read.

## 8. Flags

| Flag | Meaning | Who acts |
| --- | --- | --- |
| GREEN | Grounded, linked, evidenced, and answers the question as asked | Nobody |
| AMBER | Grounded, but narrower than asked, degraded, or resting on a conflict | Reviewer reads the note |
| RED | Not grounded, a roadmap date nobody confirmed, or a Yes/No row with a gap | A human decides before sending |

A wrong GREEN is worse than an honest RED.

## 9. Failure modes seen in past AccuKnox RFPs

| What went wrong | Where | The rule that now catches it |
| --- | --- | --- |
| Response "Compliant" over a comment that says "In Roadmap" | SABIC row 16 | `validate.py` answer and comment agree |
| A requirement left blank, another answered with no comment | SABIC rows 20 and 25 | `validate.py` no blank rows, `fill.py` needs a link |
| "More than 33 frameworks" where the validated count is about 41 | SABIC row 27 | Section 3, re-count |
| ArcSight No, Elastic Roadmap, both on the same transport | AI Security sheet | `validate.py` similar requirements answered alike |
| Internal notes in the file sent to the customer | TDM, first pass | Two output files, `validate.py` leak check |
| Researched reporting for a delta-analysis row | TDM SAST row 35 | Section 2 |
| Saving without Pillow deleted every image | TDM, first pass | `rfp_lib.require_pillow()` |
| A dropdown value with a double space looked illegal | TDM | Compare raw cell values |
