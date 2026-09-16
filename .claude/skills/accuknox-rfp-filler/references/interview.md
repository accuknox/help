# Interview bank

The skill asks with the `AskUserQuestion` tool, never with a question buried in prose. One call
holds up to four questions, each with two to four options, and the user can always pick Other. Put
the recommended option first and label it `(Recommended)`.

Ask when a trigger below fires. Do not ask for anything the file, the docs or a sensible default
already answers, and do not ask the same thing twice in one run.

## When to ask

| Trigger | Stage | Ask |
| --- | --- | --- |
| No file attached, or a path that does not exist | Start | Q1 |
| The RFP sits inside the help-docs repo | Start | Q2 |
| Customer name unknown | Start | Q3, bundled with Q4 |
| Fit verdict is CONDITIONAL or NO-GO | Fit check | Q5 |
| `intake.py` prints a BLOCKER | Intake | Q6, Q7 or Q8, whichever matches |
| A mandatory row has weak evidence | Grounding | Q9 |
| A requirement reads two ways and the verdict depends on it | Drafting | Q10 |
| A roadmap tier is proposed | Drafting | Q11, all roadmap rows in one call |
| The docs contradict each other on a row | Drafting | Q12 |
| The user supplies draft answers that are vague, unlinked or overclaimed | Drafting | Q13 |
| The user asks to mark everything Meets, or to skip validation | Any | Q14 |
| `validate.py` fails, or the reviewers disagree | Review | Q15 |

## The questions

**Q1. The file.** "Which RFP should I work on?" Options: attach the file, give a path, paste the
requirements as text.

**Q2. Location.** "This RFP is inside the public help-docs repo. Where should the working copy go?"
Options: Downloads (Recommended), another folder, stop.

**Q3. Customer.** "What name goes on the response?" Options: the name found in the file, if any,
then Other.

**Q4. Scope.** "Which deployment will this customer run?" Options: SaaS, on-prem, air-gapped,
not decided.

**Q5. Go or no-go.** State the verdict, the coverage figure and the top fit risks first, in one
short paragraph. Then ask: "How should I proceed?" Options: answer every row with honest roadmap and
partner answers (Recommended when CONDITIONAL), answer only the in-scope sections, stop and draft a
no-bid note.

**Q6. Answer column.** "I could not find the answer dropdown on sheet X. Which column holds the
response?" Options: the two most likely columns, plus "there is no answer column, build an AccuKnox
sheet".

**Q7. Unmapped scale.** "Sheet X offers these answers: ... Which one means a planned capability?"
Options: each unmapped value.

**Q8. Extra table.** "Sheet X has N rows below the answer range, rows A to B. Do they need answers?"
Options: skip them (Recommended), answer them in a new AccuKnox sheet, show me first.

**Q9. Weak evidence on a mandatory row.** "Row X asks for Y. The closest documented capability is
Z. How should I answer?" Options: Meets with the limit stated, roadmap tier, ask product first.

**Q10. Ambiguous requirement.** "Row X can mean A or B. Which did the buyer mean?" Options: A, B,
answer both in the comment.

**Q11. Roadmap dates.** One question per row, up to four per call. "Row X, capability Y. Which
tier?" Options: the customer's roadmap values that exist in the sheet, with the one you propose
first.

**Q12. Conflicting docs.** "Page A says X, page B, which is newer, says Y. Which is current?"
Options: trust the newer page (Recommended), trust the older page, ask product.

**Q13. Weak draft answers.** Show two examples of what is missing, such as no link, no feature
name, or a claim no page supports. Then ask: "How should I treat your drafts?" Options: keep them
and add links and evidence (Recommended), rewrite them from the docs, keep them as they are and flag
them.

**Q14. Unsafe request.** Explain in one sentence what the request would put in front of the
customer. Then ask: "How should I proceed?" Options: keep the honest answers (Recommended), mark
only the rows you name, stop.

**Q15. Failed gate.** List the failing checks. Then ask: "How should I fix these?" Options: fix
them all (Recommended), show me each one, ship with the failures listed in the review copy.

## Negligent or thin input

A request like "just fill it" with no file, no customer and no scope gets Q1, Q3 and Q4 in one call.
Anything the user will not decide takes the safe default: honest verdicts, existing answers kept,
review copy produced. The review summary records every default the skill chose.
