# How to use the AccuKnox RFP filler

Print this page, as written, when someone asks how to use the skill, what it does, or what to do next.

---

**The AccuKnox RFP filler answers a customer RFP from the AccuKnox help docs.** Every answer comes
with a help.accuknox.com link and an evidence image, and uses the customer's own answer scale. You
get two files back: one to send, and one for internal review.

## What to give it

1. **The RFP file.** Excel works best. Word works too. A PDF gets read page by page and turned into
   an AccuKnox response sheet.
2. **The customer name**, and the submission deadline if there is one.
3. **Anything already agreed with the customer**, such as deployment model (SaaS, on-prem or
   air-gapped), modules in scope, or answers product has already confirmed.

Keep the RFP outside the help-docs repo, for example in Downloads. The repo is public on GitHub, so
the skill refuses to write customer files inside it.

## What happens, in order

| Step | What the skill does | What you do |
| --- | --- | --- |
| 1. Intake | Reads every sheet, finds the answer column and its dropdown, counts blank and mandatory rows | Answer a few questions if the file is unusual |
| 2. Fit check | Routes each requirement to one of 12 AccuKnox modules and flags topics outside them | Decide GO, CONDITIONAL or NO-GO |
| 3. Grounding | Finds the help pages, the matching lines and the screenshots for every row | Nothing |
| 4. Drafting | Writes each answer from the pages it opened, picks the image, and flags the row GREEN, AMBER or RED | Approve roadmap dates and RED rows |
| 5. Fill | Writes the customer copy and the review copy, keeping every existing answer and image | Nothing |
| 6. Validation | Checks dropdown values, links, images, banned words and contradictions | Fix anything it fails |
| 7. Review | Three independent reviewers check accuracy, mechanics and how a buyer will score it | Make the final calls |

## The rules it will not break

- **It never answers No.** A gap becomes a roadmap tier, a third-party integration, or a partial
  answer, whichever the customer's scale offers. If the scale only has Yes and No, the row goes RED
  for a human.
- **It never overwrites your answers.** Existing responses, comments and images stay. It adds
  links and evidence. To change an answer, say so in plain words, and the change gets logged.
- **Every claim traces to a help page.** Nothing comes from memory. When no page supports a claim,
  the row is flagged, not guessed.
- **The customer copy carries nothing internal.** Flags and notes live only in the review copy.

## Ask it things like

- `/accuknox-rfp-filler` then attach the file
- "Is this RFP a fit for us?"
- "Fill the blank rows only"
- "Change SAST row 24 to Meets"
- "Why is DAST row 18 red?"
- "Which answers need product sign-off?"
- "How do I use this?" prints this page

## What you get back

- `<RFP name> - AccuKnox Response.xlsx`, ready to send after the RED rows are resolved
- `<RFP name> - AccuKnox Review.xlsx`, internal only, with flags, notes and a review sheet
- `<RFP name>.rfp-work/`, the working folder with the profile, evidence, diagrams and the validation report
