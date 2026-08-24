# The SEO audit

`scripts/grade.py` counts what a regex can count. This file holds the rest, the
judgement calls that decide whether a post ranks and whether an answer engine
cites it.

Run the script first, then work this file against the draft. Report both.

```bash
python scripts/grade.py draft.md
python scripts/verify_links.py draft.md --fix-suggestions
```

## What the script already checks

Front matter completeness, `seo_title` and `meta_description` lengths, slug
shape, reading time against word count, one H1, heading hierarchy, weak heading
openers, colons in headings, TL;DR and FAQ presence, FAQ question count, prose
word count, paragraph depth, passive voice ratio, keyword density and first-150
placement, concrete figures, internal and external link counts, anchor text,
bare URLs, alt text, captions and table presence.

Do not repeat any of that by hand.

## Module 1, does the post answer the query

The first 150 words resolve the search that brought the reader. Read them alone
and ask whether a practitioner who typed the primary keyword has their answer.

A post that opens by defining the category has already lost. `Cloud native
application protection platforms have become essential as organizations migrate`
is a sentence written for nobody.

Check the search intent matches the shape:

| Query shape | What the post must be |
| --- | --- |
| `what is X` | A definition in the first two sentences, then the mechanism |
| `best X tools` | A named shortlist with selection criteria stated before the list |
| `how to X` | Numbered steps with real commands, prerequisites first |
| `X vs Y` | A sourced capability table, no adjectives |
| `X CVE` or an incident | What happened, the condition, the detection, the fix |

A `best tools` post that never names a competing tool is not a `best tools`
post. Google reads it as a product page and ranks it as one.

## Module 2, E-E-A-T for a security audience

Google's quality rater guidelines weight four factors. Security content is
Your Money or Your Life adjacent, so the bar is higher than for general
marketing copy.

| Factor | Weight | The signal in an AccuKnox post |
| --- | --- | --- |
| Experience | 20% | Real POC numbers, a customer scenario, an incident the team handled |
| Expertise | 25% | Correct eBPF, LSM, RBAC, CVE and control detail. One wrong CVSS score costs the whole page |
| Authoritativeness | 25% | Links to the standard, the advisory, the vendor doc. Named author |
| Trustworthiness | 30% | Sourced claims, a named limitation, no invented flags |

**The named limitation is the highest-value sentence you can add.** `This does
not cover Windows nodes` earns more trust than three paragraphs of coverage
claims, and a polish pass deletes it first. Put one in every post and protect it.

AI-assisted drafting is fine. Generic drafting is not. Flag any paragraph that
would read identically under a competitor's logo.

## Module 3, technical metadata

The draft is markdown, so most of this is a note for whoever publishes it. State
these in the handoff rather than scoring them:

- Canonical tag self-referencing on `accuknox.com/blog/<slug>`.
- `og:title`, `og:description`, `og:image`, `og:url` present.
- `twitter:card` set to `summary_large_image`.
- `index,follow` unless the post is gated.

The cover image is the one performance risk you control from the draft. Ask for
WebP under 200 KB with explicit width and height, which removes the layout shift
before it happens.

## Module 4, schema

Recommend exactly one: `BlogPosting`, or `Article` where the post is an incident
writeup. Both need `headline`, `datePublished`, `dateModified`, `author`,
`publisher` and `image`.

Never recommend `HowTo`, which Google deprecated, and never `FAQPage`, whose
rich results are restricted to government and health sites. The FAQ section
still earns its place through answer engines, which read the H3 questions
directly.

Ship the JSON-LD as a fenced block in the handoff, not in the body.

## Module 5, AI citation readiness

Five things decide whether ChatGPT, Perplexity or an AI Overview quotes the post:

1. A standalone factual sentence that survives being lifted out of context.
2. An H2 hierarchy that reads as the argument, so a machine can pick the section.
3. A table. It is the single most extractable block on the page.
4. Specific figures with units and dates. `2,428 critical findings across five
   deployed LLMs` gets quoted. `Many critical findings` does not.
5. An unambiguous author and date.

Every AccuKnox post already carries the byline and date from the template, so
points 1 through 4 are the work.

## How to report the audit

Give the score table from `grade.py`, then the findings this file produced,
ranked CRITICAL, HIGH, MEDIUM, LOW. For each finding name the fix and the line.
No vague suggestions.

Then say plainly which findings you fixed and which you left, and why.

## Related

- `references/blog-layout.md`, the shape the audit assumes
- `.claude/core/restraint-rules.md` section 5, run it after every fix
