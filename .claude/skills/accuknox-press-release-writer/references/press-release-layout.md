# The AccuKnox press release layout

Read on 2026-08-23 from the live pages on accuknox.com, through their `.md`
twins:

| Page | Type |
| --- | --- |
| `press-release/fairfirst-insurance-accuknox-partnership` | Customer win with two channel partners |
| `press-release/accuknox-launches-ai-security-2-0-at-rsac-2026` | Product launch at an event |
| `press-release/sabpaisa-selects-accuknox` | Customer win |
| `press-release/accuknox-wins-ai-startup-award-bsides-bangalore-2026` | Award |

Refresh with
`python <harness>/scripts/fetch_md.py press-release/<slug>`.

## The spine, every type

1. **YAML front matter.** Fields in `assets/press-release-template.md`.
2. **H1.** The headline. Who did what, in one line, active voice.
3. **The metadata block.** Date, release time with timezone, contact name and
   email. WordPress injects these above the body from the front matter, so do
   not write them into the draft.
4. **The dateline paragraph.** Bold city and country, the date, then an italic
   one-sentence summary of the news.
5. **The lede.** Two to four paragraphs. Who, what, why, and the scope.
6. **H2 body sections.** Two to four, each with a heading that states something.
7. **H2 Leadership Perspectives.** The quotes, one per organisation.
8. **H2 `About <Organisation>`.** One per named organisation, AccuKnox last but
   always present.
9. **H2 Media Contacts.** One block per organisation.

Nothing after Media Contacts.

## The headline

Active voice, present or past tense, names both parties. It reads as news, not
as marketing.

| Weak | Strong |
| --- | --- |
| `AccuKnox Announces Exciting New Partnership` | `FairFirst Insurance Selects AccuKnox ASPM in Collaboration with VS ONE Pvt Ltd and APTS` |
| `New AI Security Capabilities Available` | `AccuKnox Launches AI-Security 2.0 at RSAC 2026, San Francisco, USA` |
| `AccuKnox Recognised at Event` | `AccuKnox Wins AI Startup Award at BSides Bangalore 2026` |

Title Case. The customer or partner goes first in a win, AccuKnox goes first in
a launch or an award.

## The dateline

The live pages use an en dash after the date. The house ban list forbids it, so
write two sentences instead. Same information, same italics, and the slop
scorer passes.

```markdown
**Colombo, Sri Lanka**, 20 AUG 2026. *The collaboration brings together
AccuKnox's application security technology, VS ONE's distribution capabilities,
and APTS's local implementation and support expertise.*
```

City and country bold. Date in `DD MON YYYY`. The italic sentence summarises
the news in one line and never repeats the headline word for word.

For an event launch the dateline carries the event:
`**March 23, Monday, San Francisco, RSAC 2026**.`

## The lede

Two to four paragraphs, and the first one carries the whole story. A journalist
who reads only that paragraph has the news.

Name the customer with a descriptor and a credential in the same sentence.
`FairFirst Insurance, one of Sri Lanka's leading and largest general insurance
providers and the recipient of the "Best Insurance Company in Sri Lanka" title
at the People's Excellency Awards 2025, has selected AccuKnox Application
Security Posture Management (ASPM)`.

Expand the acronym on first use, then use the acronym alone.

State the channel structure explicitly where there is one. Distributor,
reseller, in-country support. Partners read this section to check their role is
described correctly.

## Body sections by release type

| Type | H2 sections |
| --- | --- |
| `customer-win` | `Strengthening <capability>`, then `Leadership Perspectives` |
| `partnership` | `What the partnership covers`, `Why <region> now`, then `Leadership Perspectives` |
| `product-launch` | `What's new in <product>` with a module table, then one H3 per module, then `Leadership Perspectives` |
| `award` | `The award and the category`, `What the judges evaluated`, then `Leadership Perspectives` |
| `executive-hire` | `The role`, `Background`, then `Leadership Perspectives` |

The live pages put the body sections at H3 directly under the H1, skipping H2
entirely. That is a WordPress theme habit, not a decision. Write H2 instead. The
outline is correct, Google Docs renders it properly, and the validator stops
flagging a skipped level. Nothing about the published page changes.

A product launch is the longest shape. The AI-Security 2.0 release opens its
`What's new` section with a two-column table of module and status, GA or Beta,
then gives each module its own H3 with three or four sentences. That table is
the most-quoted block in the release, so it carries exact status values and no
adjectives.

## Quotes

Two to five, one per organisation named in the headline. Italic body, then a
bold attribution line.

```markdown
*"At FairFirst Insurance, we believe that protecting our customers begins with
protecting the digital services and infrastructure that support them."*

**— Srimal Silva, AGM - IT, FairFirst Insurance**
```

Three rules, and all three get checked by the other organisation's comms team:

- Full name, exact job title, exact organisation name. No abbreviation nobody
  uses.
- The customer quote leads. The AccuKnox quote never goes first.
- Each quote makes a different point. Four quotes that all say the partnership
  is exciting is one quote repeated four times.

Where the wording is not approved yet, write the quote you propose and mark it
`[DRAFT, pending approval from <name>]` on the attribution line.

## About blocks

One H2 per organisation, AccuKnox included, AccuKnox last. Two or three
sentences plus a website line.

```markdown
## About AccuKnox

AccuKnox provides a Zero Trust Cloud-Native Application Protection Platform
that delivers security visibility and risk management across applications,
cloud environments, containers, Kubernetes, and AI workloads.

**Website:** [accuknox.com](https://accuknox.com/)
```

The customer's own About text comes from the customer. Never write it for them
from a website scrape, because the wording is theirs to approve. Where you do
not have it, bracket it.

## Media contacts

One block per organisation, in the same order as the About blocks.

```markdown
## Media Contacts

**AccuKnox**
Syed Hadi
Product Marketing & Partnerships Lead
media@accuknox.com

**FairFirst Insurance**
Srimal Silva
Assistant General Manager - IT
[email]
```

Email addresses on the live pages are Cloudflare-obfuscated, which is a
WordPress plugin doing its job. Write the plain address in the draft.

## Length and tone

350 to 950 prose words. The FairFirst release runs about 700 with four quotes
and four About blocks.

No adjectives doing work a fact should do. `Comprehensive`, `industry-leading`
and `cutting-edge` are on the ban list, and a journalist deletes them anyway.
Say what the platform does and let the customer's quote carry the enthusiasm.

Never claim a competitor lost the deal, and never name a displaced vendor
without written clearance from the customer. A case study can say
`replacing Wazuh`. A press release says it only if the customer approved that
sentence.

## Related

- `assets/press-release-template.md`, the file you copy
- `<harness>/references/house-style.md`, watermarks and layout
- `<harness>/scripts/check_asset.py`, the validator for this channel
