# Writing rules

The style layer for every page in this repo. A help page, a how-to, a use case, an integration
guide, a release note, a FAQ answer and a blog post all load this file.

The ban list is not here. The ten banned words and constructions live in `CLAUDE.md` and `AGENTS.md`
at the repo root, which load into every session already. This file holds the rules a word list
cannot express, and it never repeats one of them.

## 0. Who reads this

Three readers, and each one arrives under pressure.

A platform or DevOps engineer who has to make something work today. A security engineer or analyst
who is mid-investigation and needs one exact answer. A security lead evaluating whether the
platform does what a vendor said it does.

None of them is browsing. Every one of them will leave for a competing page the moment yours makes
them work for the answer. That single fact decides most of the rules below.

## 1. Substance decides the page

Say what the thing does. Then say what it does not do.

A page that describes a capability in the abstract has told the reader nothing they can act on. Name
the exact resource, the exact policy type, the exact CLI command, the exact console path. `Cluster
Misconfiguration Scanning` is a feature name. "It flags a pod running as root and shows you the
line in the manifest" is what the reader came for.

A named limitation is the most credible sentence on a technical page. "This does not cover
Windows nodes" earns more trust than three paragraphs of coverage claims, and it is the first thing
a polish pass deletes.

## 2. Kill the filler transition

This is the failure that reads as generated text more than any word choice, and no linter catches it.

A filler transition is a sentence that announces the next point instead of making it. The shapes are
`That is where X comes in`, `Here is the honest limit`, `This is the part that matters`, `Let us
look at why` and `Watch this closely`. Each one takes a line and delivers no fact.

The repair is deletion. Read the sentence before it and the sentence after it. If they connect
without the announcement, the announcement was filler.

**Never write a sentence whose subject is the page, the table or the section.** No "the table below
shows", no "this section covers", no "as mentioned earlier". Inform the reader, never narrate the
document at them.

## 3. Kill the clever declarative

A short quotable line that carries no fact you can point at is decoration. `Security is a process,
not a product` is a bumper sticker. Cut the line and keep the number, the command or the
consequence.

The test is one question. Could a reader do anything differently after reading that sentence? When
the answer is no, it goes.

## 4. Name every referent

No dangling `it`, `this`, `they`, `all four` or `the above`. Name the thing in the sentence that
uses it.

This matters more in security writing than anywhere else, because a page often holds four nouns
that could all be `it`. A policy, a pod, a scanner and a finding. A reader who has to reread a
sentence to work out which noun you meant has already lost confidence in the page.

## 5. Paragraph depth over paragraph count

Three to four sentences per paragraph. A run of two-sentence paragraphs passes every mechanical
check and never builds an argument, because each one restarts before it arrives anywhere.

A paragraph makes one point and finishes it. State the claim, give the mechanism, give the
consequence for the reader. If a paragraph is two sentences long, it is usually missing the
mechanism.

## 6. A heading says what the section delivers

A heading is the unit a reader scans and the unit an answer engine lifts, so it carries the
conclusion rather than the topic.

Weak: `Understanding policy enforcement`. Strong: `Enforcement blocks the process before it runs`.
Weak: `Prerequisites`. Strong: `Prerequisites` is fine, because a reader scanning for it expects
that exact word. Use a conventional label where the reader hunts for the label, and a conclusion
everywhere else.

Sentence case, always. No colon in a heading. No skipped heading level.

## 7. Active voice, second person, real commands

Write to the reader as `you`. Give an instruction as a command.

- Weak: "The agent should then be deployed to the cluster."
- Strong: "Deploy the agent to the cluster."

Passive voice hides who acts, and in a security procedure the actor is the whole point. Use passive
only where the actor is genuinely unknown or irrelevant.

One action per step. A numbered step that contains `and then` twice is two steps.

## 8. Define the term once, then reuse it exactly

Expand an acronym on first use in a page, then use the acronym and nothing else. `Cloud Native
Application Protection Platform (CNAPP)`, then `CNAPP` every time after.

Never rename a subject for variety. A model reaches for `the solution`, `the platform` and `the
tool` to avoid repeating a product name. That reads smoother and costs precision, because a reader
cannot tell whether the new phrase means the same component. Repeat the real name.

Use the product's canonical name every time. Check an existing page rather than trusting a memory
of it.

## 9. Cite the source and link the reader to it

Every version number, CVE identifier, CVSS score, benchmark control, pricing claim and third-party
behaviour comes from an opened source, and the page links to it.

Never invent a CVE, a CVSS score, a compliance control number, a CLI flag, an API field, a default
value or a supported version. These are the facts a reader will act on and the facts a model will
produce confidently and wrongly. When you need one and do not have it, write the gap in visible
brackets, such as `[confirm the minimum agent version]`, and leave it for a human. A bracket cannot
ship by accident. An invented flag can, and it will burn a reader who runs it.

`experts recommend`, `studies show` and `industry best practice suggests` are not sources. Name the
benchmark, link the advisory, or drop the claim.

## 10. No fear, uncertainty and doubt

A security page carries a real risk, so it never needs inflation.

State the attack, the condition that makes it possible, and the mitigation. Skip the adjectives.
`Devastating`, `catastrophic`, `crippling` and `unprecedented` add no information and cost
credibility with the exact reader you want, who has seen the incident and does not need it dramatised.

Never attack a competitor. Compare on a named, sourced capability or not at all.

Never publish a working exploit chain, a live payload or a customer's tenant data. A screenshot gets
redacted before it reaches the repo.

## 11. Blog post specifics

A blog post in this repo answers a question a practitioner typed into a search box.

Front-load the answer. The first 150 words resolve the query, because an answer engine lifts the
first passage that does and a human who arrived from a search result decides in that span whether to
stay. No preamble, no definition of the industry, no history of the problem.

Then earn the length. A real scenario with real components, the mechanism behind the failure, the
detection, the fix, and what the fix does not cover. A post that could be published unchanged by any
vendor in the category is a post nobody needed.

## 12. The mechanical bar

- A code fence carries its language tag.
- A command is complete and copy-pasteable, with no placeholder the reader cannot resolve.
- A number carries its unit and its source.
- A link carries descriptive text, never `click here` and never a bare URL in prose.
- An image carries alt text that says what the picture proves, never "a screenshot of the dashboard".
- A screenshot matches the current console. A stale screenshot is a support ticket.
- A table has a header row and no empty cells.

## 13. The test that outranks every rule above

Read the page as the reader who arrived mid-incident.

Can they find the one answer they came for, act on it, and know what it does not cover? If yes, the
page works, even where it breaks a rule here. If no, the page fails, even with every rule followed.

## Related

- `.claude/core/runtime-contract.md`, the load order and the gate order
- `.claude/core/restraint-rules.md`, what an anti-slop edit must not touch
- `CLAUDE.md` and `AGENTS.md`, the ten banned words and constructions
