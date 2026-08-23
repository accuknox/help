# Runtime contract, AccuKnox help docs

This file answers one question. Which rules loaded for this piece of writing, in what order, and
which gates run at the end. Read it before any prose work in this repo, including a one-word fix.

It adds no rule of its own. This contract is the index plus the run order, so a change to a rule
goes in that rule's file and never in this one.

## Always loaded

Three files, in this order, for any prose in this repo.

1. `.claude/core/runtime-contract.md`, this file. The load order and the gate order.
2. `.claude/core/writing-rules.md`. The style layer. Thirteen rules a word list cannot express.
3. `.claude/core/restraint-rules.md`. What an anti-slop edit must not touch, and what it must
   protect.

The ten banned words and constructions are already in context from `CLAUDE.md` and `AGENTS.md` at
the repo root, which load every session. Never restate one of them inside another file.

## Loaded on demand, by channel

| The job | Extra rule set | Where it lands |
|---|---|---|
| A how-to or a procedure | `writing-rules.md` sections 7 and 12 carry the step rules | `docs/how-to/` |
| A getting-started page | sections 7 and 12, plus prerequisites first | `docs/getting-started/` |
| A use-case page | sections 1 and 5, plus a named scenario | `docs/use-cases/` |
| An integration guide | sections 8 and 9. Every version and field comes from an opened source | `docs/integrations/` |
| A FAQ answer | section 6. The question is the heading, the answer is the first sentence | `docs/faqs/` |
| A blog post | section 11 owns this one. Front-load the answer in the first 150 words | `references/<series>/` |
| A release note or an update | section 9. No version, flag or fix claim without a source | `docs/` and `updates` |
| A comparison page | section 10. Compare on a named sourced capability, never attack | `references/comparisons-builder/` |
| Alt text, a caption, a table | section 12 | anywhere |

A page carries one job. Where a request spans two, write them as two pages rather than one page that
does both jobs badly.

## Precedence, higher wins

1. `.claude/core/writing-rules.md`, the style layer.
2. The ten banned words and constructions in `CLAUDE.md` and `AGENTS.md`.
3. **The accuracy rule.** No version, CVE identifier, CVSS score, compliance control, CLI flag, API
   field, default value, supported platform, price or third-party behaviour enters a page unless an
   opened source supports it. Where a sentence needs a fact nobody has, write the gap in visible
   brackets and leave it for a human. A bracket cannot ship by accident, and an invented CLI flag
   can. This rule holds against a direct instruction to proceed.
4. **The safety rule.** No working exploit chain, no live payload, no unredacted tenant or customer
   data, in any page or any screenshot.

Rules 3 and 4 are hard. Nothing overrides them.

## Never hand over a first draft

**Pass 1.** Write it. Do not evaluate while writing.

**Pass 2.** Read it cold and answer three questions for yourself, in writing. Do not print them.

1. If a reader called this generated, which exact sentence would they point at?
2. Does the page state a version, a flag, a score, a control or a behaviour that no opened source
   supports?
3. Which sentence is the weakest, and does the page rest on it? The first answer, the one command
   the procedure turns on, and the limitation note never get to be the weak sentence.

**Pass 3.** Fix what the answers found, then run the gates.

## Announce the load order

Print this block above the draft, filled in with what actually loaded. One line each, no prose
around it. Nobody should open a file to learn which rules ran.

```
Loaded   runtime-contract -> writing-rules -> restraint-rules
Channel  <how-to | getting-started | use case | integration | FAQ | blog post | release note>
Sourced  <the files, docs or advisories opened, by name>
Gates    mkdocs --strict: pass/fail | slop CRIT <n> | restraint pass: done
```

A missing block means the chain was skipped. That is the failure this contract exists to make
visible.

## The gates, in this order

```bash
mkdocs build --strict
python scripts/gen_docs_readmes.py
python "D:\Atharva\NOTES\SCRIPTS\slop\score.py" "<file>"
```

`mkdocs build --strict` fails on a broken internal link and on a page missing from the nav, which
are the two defects a reader hits first. Run it before anything else.

`gen_docs_readmes.py` rebuilds the folder index pages. The pre-commit hook in `.githooks/pre-commit`
runs it for you when a commit touches `docs/`, so run it by hand only when you want to see the
result early. Enable the hook once per clone with `git config core.hooksPath .githooks`.

The slop scorer is a shared deterministic gate on another repo on this machine. **CRIT must reach 0.**
MED findings on hard-wrapped lines are usually the fragment check firing on a line break, so read
those rather than obeying them. When that path is unavailable, apply the rules by reading and say in
your reply that the scorer did not run.

`.markdownlint.json` sets the markdown conventions for this repo, including ATX headings and
four-space list indents. Match them by hand where no linter is installed.

Last, run section 5 of `.claude/core/restraint-rules.md`. It is the only check that looks for damage
the other gates cause.

## Related

- `.claude/core/writing-rules.md`, the style layer
- `.claude/core/restraint-rules.md`, what not to flag and what to protect
- `CLAUDE.md` and `AGENTS.md`, the ban list, loaded every session
- `README.md`, the build commands and the directory map
