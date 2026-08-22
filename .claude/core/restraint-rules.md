# Restraint rules

The ban list in `CLAUDE.md` and the rules in `writing-rules.md` say what to cut. This file says what
to leave alone, and it carries the same weight.

Applied without judgement, a remove-list produces the second failure. Prose stripped so hard that
nobody is home. That output is not human writing, it is a different machine's writing, and it is
where the complaint that edited documentation reads flat and generic comes from. A page can pass
every check and still tell a reader nothing.

## 1. What is not evidence of AI

None of the following, on its own, means a machine wrote the sentence. Do not cut one unless it sits
in a cluster with real tells.

- **Clean grammar and consistent style.** Documentation is edited. Polish proves nothing.
- **Technical or formal vocabulary.** The ban list names specific overused words. It does not ban
  precision. Leave `idempotent`, `ephemeral` and `immutable` where they are the right word.
- **Dry, plain prose.** For a prerequisite list, a limitation note or a runbook step, dry is correct
  and anything livelier is worse.
- **A repeated product or component name.** Rule 8 in `writing-rules.md` requires it. Never rename a
  subject for variety.
- **One transition word.** A single `however` is English. The pile-up is the tell.
- **One short emphatic sentence.** People land a point with a clipped sentence. Flag the staccato
  drumbeat only when several stack in a row.
- **A numbered procedure that reads mechanically.** A procedure is meant to read mechanically. Do
  not add colour to a sequence of commands.
- **An unsourced claim.** Most sentences carry no citation. That may be a sourcing problem under
  rule 9. It is not an AI problem, and a rewrite does not fix it.
- **A watched word inside a quotation, a heading, a product name, a log line or an example.** When
  the page discusses the phrase rather than uses it, leave it exactly as written.

## 2. What to protect

- **A command, a path, a flag, a version, a field name or an output block.** Reformat one never. A
  shortened path or a tidied log line is a factual error wearing the clothes of an edit. Copy these
  through untouched, byte for byte.
- **A named limitation, an unsupported platform, a known issue.** The most credible sentences on the
  page, and the first casualties of a smoothing pass.
- **Odd, specific, hard-to-invent detail.** An exact error string. A real timeout value. The precise
  console path with its three clicks. Models round specifics off and engineers collect them.
- **A warning, a caution, or an irreversible-step note.** Never soften one into a hedge, and never
  merge one into the paragraph above it. It is set apart because a reader must not miss it.
- **Uneven rhythm.** A nine-word sentence beside a forty-word one. Model output drifts to one
  uniform cadence. The variance is the human signal, so do not regularise it.
- **An opinion an engineer can defend.** When the person who built the thing can say why a word was
  chosen, that reasoning outranks every rule in this repo.

## 3. Clusters, not instances

One em dash means nothing on its own. An em dash, plus a tricolon, plus `robust and comprehensive`,
plus a `Challenges and future directions` heading, is a confession.

Count the cluster before you edit. Where you cannot tell whether a pattern belongs to the writer or
to a model, assume it belongs to the writer and leave it.

## 4. Which failure does this draft have

**It carries AI patterns.** Cut them in clusters, using the ban list and `writing-rules.md`.

**Nobody is home.** No command, no version, no named limitation, no real output, no position.
Deleting another banned word will not fix that page. It needs a fact and a boundary, and both come
from an opened source or from an engineer. Never from invention.

The second failure is the more common one after a heavy edit, and nothing in this repo detects it
automatically.

## 5. The pass that runs after every gate

Run this last, on the finished page.

- [ ] Is every command, path, flag, version and output block identical to the source?
- [ ] Did the edit delete a named limitation, or soften it into a hedge?
- [ ] Is every warning and caution still set apart and still blunt?
- [ ] Did any specific get generalised to make a sentence flow?
- [ ] Does the page still vary sentence length, or did it flatten to one cadence?
- [ ] Was anything cut on the evidence of a single section 1 item?
- [ ] Could a reader mid-incident still find the one answer they came for?

A page that fails one of these goes back, even with the build green.

## Related

- `.claude/core/runtime-contract.md`, the load order and the gate order
- `.claude/core/writing-rules.md`, the style layer
