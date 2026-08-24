# The AccuKnox comparison layout

Read on 2026-08-23 from the live pages, through their `.md` twins. Fifty-five
comparison pages exist and they fall into four archetypes.

| Archetype | Live example | Body words |
| --- | --- | --- |
| `head-to-head` | `comparisons/accuknox-vs-quilr` | 1,513 |
| `head-to-head`, long | `comparisons/accuknox-vs-opentext-fortify` | 1,859 |
| `three-way` | `comparisons/checkpoint-vs-prisma-cloud-vs-accuknox` | 1,284 |
| `alternatives` | `comparisons/prisma-cloud-alternatives` | 2,508 |
| `stack-ranking` | `comparisons/ai-security-stack-ranking` | 1,239 |

Refresh with
`python <harness>/scripts/fetch_md.py comparisons/<slug> --headings`.

## What you write and what WordPress adds

Every comparison page ends with the same injected blocks: the `See How Customers
Accelerate Business And Reduce Risks With AccuKnox` carousel, seven repeated
`DevSecOps & Security Teams Love our AppSec/CloudSec/AISec Platform` cards, five
customer testimonials, and a `Looking to Migrate from <competitor>?` CTA.

Write none of it. `scripts/fetch_md.py` strips the tail so you study only what a
human wrote.

## Archetype 1, head-to-head

```
H1     AccuKnox (vs) <Competitor>
H2     <Category> Platform Comparison
       one-sentence scope line naming every capability the page covers
       [DOWNLOAD PDF] where marketing produced one
H2     Parameters                     <- the matrix column header
H2     <Competitor>                   <- the matrix column header
H3     <Parameter 1>                  <- one per row, 10 to 25 of them
         AccuKnox cell: mechanism, technology, reference links
         Competitor cell: what they do, then what they do not
H3     <Parameter 2>
       ...
H2     Why Customers Choose AccuKnox Over <Competitor>
H3       Better
H3       Faster
H3       Cheaper
```

The two H2s named `Parameters` and `<Competitor>` are table column headers that
the markdown twin flattens into headings. In a draft, write the matrix as a real
three-column markdown table and let the Google Docs converter carry it. That is
what a reviewer wants to read and what WordPress needs anyway.

The scope line under the H2 subtitle earns its place. It lists every capability
the page covers in one sentence, so a buyer knows in five seconds whether this
page answers their question. `Compare AccuKnox and Quilr across AI pipeline
security, model and dataset security, prompt firewalling, runtime protection,
red teaming, AI gateways, agentic AI, MCP security, and deployment options.`

## Archetype 2, three-way

Same spine, one more column, fewer rows.

```
H1     AccuKnox vs <A> vs <B> Cloud Native Security Overview
H2     Overview                       <- three or four sentences of framing
H2     Parameters
H2     <Competitor A>
H2     <Competitor B>
H3     <Parameter 1>                  <- 6 to 8 rows only
       ...
H2     Researching about <category> Alternatives?
```

Seven rows is the live norm. A three-way matrix with twenty rows does not fit on
a screen and nobody reads column three.

## Archetype 3, alternatives listicle

The only archetype that reads like a blog post, and the longest.

```
H1     Top 5 <Competitor> Alternatives for <year>
H2     Find Out the Best <Category>: Top <Competitor> Alternatives
H3       Table of content
H2     TL;DR: Best <Competitor> Alternatives at a Glance
H2     Why Look for a <Competitor> Alternative?
H2     Top 5 <Competitor> Alternatives Comparison    <- the summary table
H2     Top 5 Alternatives to <Competitor>
H3       AccuKnox, Best <Competitor> Alternative for <capabilities>
H3         Overview
H3         Key Features
H3         Why choose AccuKnox over <Competitor>?
H2     2. <Vendor Two>
H3       Overview / Key Features / Why choose <Vendor Two> over <Competitor>?
       ... vendors 3, 4, 5
H2     What to Look for in a <Competitor> Alternative in <year>
H2     Final Thoughts
```

AccuKnox is entry one and is not numbered on the live page, while vendors two
through five are. Every other vendor gets a genuine, fair `Why choose X`
paragraph. A listicle where four of the five entries are strawmen is worthless
to a buyer and obvious to everyone.

## Archetype 4, stack ranking

The thinnest prose and the widest table.

```
H1     <Category> Stack Ranking (<year>)
       three-sentence positioning paragraph
       [DOWNLOAD PDF]
H2     Features
H2     <Vendor A> / <Vendor B> / <Vendor C> / <Vendor D>   <- column headers
H3     <Capability 1>
         one short phrase per vendor, no sentences
       ...
```

Cells are phrases, not sentences. `Full stack CNAPP (CSPM, CWPP, CIEM, ASPM,
KSPM, KIEM)` against `Focused on CWPP, limited CSPM`. Four or five vendors, ten
to fifteen capability rows.

## Better, Faster, Cheaper

The closing section on every head-to-head and three-way page. Three H3s, two or
three sentences each.

- **Better.** The capability the competitor does not have, named and sourced.
- **Faster.** Time to value. Deployment hours, coverage in week one, an
  onboarding step count.
- **Cheaper.** The consolidation argument, or the licensing model. Never a
  competitor's price unless it is published on their own pricing page and you
  link it.

Each one carries a fact. `Better` filled with adjectives is the section a
reviewer deletes.

## The sourcing rule

Every competitor claim links to something the competitor published. Their docs,
their pricing page, their release notes, their support matrix. Not a review
site, not an analyst summary, not a memory.

Every AccuKnox claim links to `help.accuknox.com`. The Quilr page does this
inside the cells, as a `References:` list of two or three doc links under the
AccuKnox paragraph. Copy that pattern.

`check_asset.py --channel comparison` fails a draft where a competitor is named
three or more times with no link to their own site, and where fewer than two
help-docs links appear.

## Tone

Section 10 of `.claude/core/writing-rules.md` is hard on this and the validator
enforces the obvious half.

- State what the competitor does before you state what it does not.
- No adjective doing a fact's job. Not `weak`, `limited`, `poor`, `basic`.
  `No static scanning of model artifacts` is stronger and cannot be argued with.
- Never imply a competitor is insecure or negligent.
- Where their product genuinely wins a row, say so. One honest row where the
  competitor is better buys credibility for the other fourteen.
- Where you cannot confirm a capability, write `[confirm from <competitor>
  docs]`. An invented gap becomes a legal letter.

## Length

| Archetype | Prose words |
| --- | --- |
| `head-to-head` | 1,200 to 1,900 |
| `three-way` | 1,000 to 1,400 |
| `alternatives` | 2,000 to 2,600 |
| `stack-ranking` | 900 to 1,300 |

## Related

- `references/parameter-sets.md`, the real rows per category
- `assets/comparison-template.md`, the file you copy
- `<harness>/references/house-style.md`, tables, bullets, callouts, watermarks
- `<harness>/scripts/check_asset.py`, the validator for this channel
