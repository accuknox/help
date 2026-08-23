---
name: accuknox-comparison-writer
description: >
  Write an AccuKnox comparison page. Use this skill whenever the user asks for a
  comparison, a versus page, a competitor comparison, an alternatives listicle,
  a stack ranking, a battlecard page, or a migration page for AccuKnox.
  Triggers include "AccuKnox vs X", "compare us with X", "write a 3-way against
  X and Y", "top 5 X alternatives", "stack ranking for AI security", "we need a
  comparison page for X". Carries the four live archetypes, the parameter sets
  per product category, the sourcing rule for every competitor claim, and the
  structural validator.
trigger: /ak-compare
---

# AccuKnox comparison writer

A comparison page is read by a buyer with a shortlist and by the competitor's
sales team. Both are looking for the sentence you cannot back up.

Repo root: `D:\Atharva\AccuKnox\HelpDocs`.
Shared harness: `.claude/skills/accuknox-blog-writer/`, written below as
`<harness>/`.

## Load the writing chain first

1. `.claude/core/runtime-contract.md`
2. `.claude/core/writing-rules.md`, and section 10 owns this channel
3. `.claude/core/restraint-rules.md`
4. `<harness>/references/house-style.md`
5. `references/comparison-layout.md` and `references/parameter-sets.md` in this
   skill

Print the `Loaded` block above the draft.

**Two rules decide whether this page can ship.** Never attack a competitor.
Compare on a named capability with a source, or drop the row. And **every
competitor claim links to something the competitor published**, their docs,
their pricing page, their release notes. A claim sourced from a competitor's own
documentation is the only version that survives their legal team reading it. The
validator fails a draft that names a competitor repeatedly with no link to them.

## Ask five things before you write a word

1. **Archetype.** Which of the four:

   | Archetype | Shape | Example |
   | --- | --- | --- |
   | `head-to-head` | AccuKnox against one competitor, parameter matrix | `accuknox-vs-quilr` |
   | `three-way` | Two competitors and AccuKnox, same matrix, three columns | `checkpoint-vs-prisma-cloud-vs-accuknox` |
   | `alternatives` | Numbered listicle of five vendors, AccuKnox first | `prisma-cloud-alternatives` |
   | `stack-ranking` | Four or five vendors, feature grid, thin prose | `ai-security-stack-ranking` |

2. **Category.** Which slice of the suite the page compares. This decides the
   parameter rows, and `references/parameter-sets.md` holds the real set for
   each one: `cnapp`, `appsec`, `kubernetes`, `ai-security`, `cloud-posture`,
   `siem`, `mixed`.

3. **Competitors**, by exact legal or product name. `OpenText Fortify`, not
   `Fortify`. `Palo Alto Cortex Cloud`, not `Prisma`.

4. **Sources for the competitor side.** Their docs URL, their pricing page,
   their release notes. Where the user has none, say Firecrawl will pull them
   and name what you found.

5. **Depth.** Standard is 10 to 15 parameter rows. The OpenText AppSec page runs
   25 because AppSec has that many distinct capabilities. A page under 6 rows is
   not a comparison.

Ask once, in one message. Skip the ask when the user says to go with your
recommendation, and state the four choices you made instead.

## Write it

**1. Check what already exists.** Fifty-five comparison pages are live.

```bash
grep -i "<competitor>" <harness>/sources/comparisons.md
python <harness>/scripts/fetch_md.py comparisons          # the hub, 15 KB
```

A near-duplicate means the job is an update. Say so before writing 1,800 words.

**2. Read the nearest live page of the same archetype and category.**

```bash
python <harness>/scripts/fetch_md.py comparisons/accuknox-vs-quilr        # ai-security
python <harness>/scripts/fetch_md.py comparisons/accuknox-vs-red-hat-rhacs # kubernetes
python <harness>/scripts/fetch_md.py comparisons/accuknox-vs-opentext-fortify # appsec
python <harness>/scripts/fetch_md.py comparisons/checkpoint-vs-prisma-cloud-vs-accuknox # cnapp
python <harness>/scripts/fetch_md.py comparisons/prisma-cloud-alternatives # alternatives
```

**3. Build the AccuKnox column from this repo, not from memory.** Every AccuKnox
capability claim reaches a `help.accuknox.com` page that proves it. That is what
the live pages do, and the validator requires at least two.

```bash
grep -n "aiml-support-matrix\|runtime-sec-arch\|llm-static-scan" mkdocs.yml
cat docs/support-matrix/README.md
```

**4. Build the competitor column from their own documentation.**

```bash
firecrawl scrape "https://docs.<competitor>.com/<page>"
firecrawl search "<competitor> <capability> documentation" --limit 5
```

On `Insufficient credits`, run
`python "D:\Atharva\NOTES\SCRIPTS\keys\keys.py" activate` and retry.

Where a capability is genuinely unclear from their docs, write
`[confirm from <competitor> docs]` and leave it. A bracket cannot ship by
accident. An invented gap becomes a legal letter.

**5. Copy the template and fill it.**

```bash
cp .claude/skills/accuknox-comparison-writer/assets/comparison-template.md \
   references/comparison-drafts/<slug>.md
```

`references/comparisons-builder/` in this repo holds the existing competitor
research. Read it before writing a versus paragraph.

**6. Write pass 1, read it cold, fix, then gate.**

## The gates

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/check_asset.py <draft.md> --channel comparison  # CRITICAL 0
python scripts/verify_links.py <draft.md> --fix-suggestions    # 0 broken
python scripts/slop.py <draft.md>                              # adjusted CRIT 0
```

Then section 5 of `.claude/core/restraint-rules.md` by reading.

`check_asset.py` fails on attack language, on fewer than six parameter rows, on
a competitor named three or more times with no link to their own documentation,
and on fewer than two help-docs links. It cannot judge whether a claim is fair.
Read every competitor cell once more and ask whether their product manager would
call it accurate.

## Output

Google Doc by default:

```bash
cd .claude/skills/accuknox-blog-writer
python scripts/to_gdoc_html.py <draft.md>
python scripts/to_gdoc_html.py <draft.md> --print-title
```

Then `create_file` with `contentMimeType: "text/html"`. The parameter matrix
survives the conversion as a real Google Docs table, which is the point.

Reply with the Doc URL, the markdown path, the gate results, and a list of every
competitor claim whose source you could not find.

## What the template already adds

WordPress injects the testimonial carousel, the `See How Customers Accelerate
Business And Reduce Risks With AccuKnox` block, and the `Looking to Migrate from
<competitor>?` CTA. Write none of them.

The `DOWNLOAD PDF` link points at
`https://accuknox.com/wp-content/uploads/AccuKnox-vs-<Competitor>.pdf`. Include
it only when marketing produced the PDF.

## Files in this skill

| Path | What it holds |
| --- | --- |
| `references/comparison-layout.md` | The four archetypes and the section order for each |
| `references/parameter-sets.md` | The real parameter rows per category, lifted from the live pages |
| `assets/comparison-template.md` | The file you copy to start a draft |

Everything else comes from `<harness>/`.

## Related

- `references/comparisons-builder/` in this repo, the existing research
- `.claude/skills/accuknox-blog-writer/`, the shared harness
- `.claude/core/writing-rules.md` section 10, no fear, uncertainty and doubt
