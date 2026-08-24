# House style

The four AccuKnox writing skills share this file. It sits under
`.claude/core/writing-rules.md`, adds nothing that contradicts it, and covers the
two things that file leaves open: the AI watermarks a word list cannot catch,
and how Atharva wants a page laid out.

Read `.claude/core/restraint-rules.md` beside it. That file names what an
anti-slop pass must not destroy, and the failure it prevents is the one this file
can cause.

## Part 1, the watermarks

A ban list catches vocabulary. These are shapes, and a draft can carry every one
of them without using a single banned word.

### The parallel-clause reflex

A model reaches for balanced pairs and triples because they sound finished.

- `not only X but also Y`
- `it isn't X, it's Y` and `not X, but rather Y`
- Three items where two carry the meaning. `visibility, control, and governance`
- The mirrored sentence. `Admission asks whether it should exist. Runtime asks what it is doing.`

The mirrored sentence is the hardest one, because it is genuinely useful. Keep at
most one per page and only where the two halves carry different facts. Cut the
rest.

### The announcement sentence

A sentence whose whole job is to introduce the next sentence. `That is where X
comes in`. `Here is the honest limit`. `Let us look at why`. `The table below
shows`. `This section covers`.

Delete it and read the two neighbours together. They almost always connect.

### The verbless punch

`Same prompt. Same model.` `The problem.` A two-to-five word fragment that exists
for rhythm rather than for meaning is the single loudest tell in short-form
security writing. Every sentence needs a finite verb. `That is the problem` is
fine. `The problem.` is not.

Rebuild rhythm through sentence length, never through truncation.

### The uniform cadence

Model output drifts toward one sentence length and one paragraph shape. A run of
two-sentence paragraphs passes every mechanical check and builds no argument,
because each one restarts before it arrives.

Three to four sentences per paragraph. Claim, mechanism, consequence. Then vary
it: put a nine-word sentence next to a thirty-word one on purpose.

### The clever declarative

A quotable line carrying no fact. `Security is a process, not a product.` Ask
whether a reader could do anything differently after reading it. If not, cut the
line and keep the number.

### The hollow paragraph

The worst failure, and no linter finds it. A paragraph that would read
identically under a competitor's logo. No command, no version, no console path,
no named limitation, no position.

The repair is a fact, and the fact comes from an opened source. Never from
invention. Where nobody has it, write `[confirm the minimum agent version]` in
visible brackets and leave it.

### The dangling referent

`It`, `this`, `they`, `all four`, `the above`. Security writing holds four nouns
that could all be `it` in one paragraph: a policy, a pod, a scanner, a finding.
Name the thing in the sentence that uses it.

### What is not a watermark

Do not cut a sentence for any of these alone. `.claude/core/restraint-rules.md`
section 1 has the full list, and it carries the same weight as this one.

Clean grammar. Precise vocabulary such as `idempotent` or `ephemeral`. Dry prose
in a prerequisite list. A repeated product name, which rule 8 of the writing
rules requires. One `however`. One short emphatic sentence. A procedure that
reads mechanically, because a procedure should.

Count the cluster before you edit. Where you cannot tell whether a pattern
belongs to the writer or to a model, it belongs to the writer.

## Part 2, the layout

Atharva reads by scanning. The formatting below is not decoration, it is how the
page gets read at all.

### Tables

Use one wherever three or more items share the same attributes. A comparison, a
control map, a status matrix, a criteria list. A table is also the block an
answer engine extracts most reliably, so a page with none is leaving citations
behind.

| Rule | Why |
| --- | --- |
| Header row always | A table without one is a grid of orphans |
| No empty cells | Write `-`, `Not supported`, or `In the pipeline` |
| Three to five columns | Six wraps badly on a phone and in a Google Doc |
| Facts, not adjectives | `v0.2.0` and `Blocked` beat `Excellent` and `Strong` |
| Left-align text, and keep numbers in their own column | Scanning a mixed column costs the reader a beat |

### Bullets

Bullet a paragraph only when it enumerates three or more genuinely parallel
items. Keep it as prose when the sentences build an argument where order and
causality matter, when there are only two items, or when the flow is the point.

Every bullet is a complete sentence with a finite verb. A noun fragment is not a
bullet, it is a table cell in the wrong place.

Two shapes both work, so pick one per section and hold it:

- **Bold lead-in, then the sentence.** The lead-in names the thing, the sentence
  carries the fact. Case studies use this shape.
- A plain complete sentence with no lead-in, used where the bullets are already
  short.

### Callouts

Four kinds, and each has one job. In markdown that renders on accuknox.com or in
a Google Doc, use a blockquote with a bold label. In `docs/`, use the MkDocs
admonition syntax the repo already uses.

```markdown
> **Note.** Context a reader can skip without breaking anything.

> **Prerequisite.** What must be true before the next step works.

> **Warning.** An irreversible step, a data-loss risk, or a production impact.

> **Limitation.** What this does not cover. The most credible box on the page.
```

Cap them at three per page. A page of callouts is a page with no hierarchy, and
a warning surrounded by four notes stops reading as a warning.

Never soften a warning into a hedge and never merge one into the paragraph above
it. It is set apart because a reader must not miss it.

### Headings

Sentence case. No colon. No skipped level. The heading carries the conclusion,
not the topic.

- Weak: `Understanding policy enforcement`
- Strong: `Enforcement blocks the process before it runs`

Use a conventional label where the reader hunts for the exact word.
`Prerequisites`, `Challenges`, `Outcomes` and `FAQs` all stay as they are.

A reader who reads only the headings should have read the argument.

### Numbers and code

- A number carries its unit and its source. `2,428 critical findings` beats `many`.
- A code fence carries its language tag.
- A command is complete and copy-pasteable, with no placeholder the reader cannot
  resolve.
- Copy a command, path, flag, version, field name or output block through
  untouched, byte for byte. A tidied log line is a factual error wearing the
  clothes of an edit.

### Links

Inline, on the words that earn them. Never `click here`, never a bare URL in
prose, never a `further reading` dump at the bottom. An inline link is what makes
the page rank and what lets a reader verify a claim without leaving the sentence.

## The test that outranks all of it

Read the page as the reader who arrived mid-incident. Can they find the one
answer they came for, act on it, and know what it does not cover?

If yes, the page works, even where it breaks a rule above. If no, the page fails,
even with every rule followed.

## Related

- `.claude/core/writing-rules.md`, the style layer this sits under
- `.claude/core/restraint-rules.md`, what an anti-slop pass must not touch
- `CLAUDE.md` and `AGENTS.md`, the banned words, loaded every session
