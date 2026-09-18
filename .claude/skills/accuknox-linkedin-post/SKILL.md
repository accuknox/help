---
name: accuknox-linkedin-post
description: Draft, review and schedule AccuKnox company-page LinkedIn posts through the local Zernio account. Use for any request to write, draft, plan, review or schedule LinkedIn copy for AccuKnox, including single posts, webinar and event promos, blog and ebook promos, partner posts, customer wins, and a whole multi-week calendar. Carries the AccuKnox voice model built from 68 real posts, the link-in-comments rule, the @mention resolver, and the scheduler that pins every write to the AccuKnox profile.
---

# AccuKnox LinkedIn

One skill covers the whole job: decide whether the post is worth making, write
it in the AccuKnox voice, resolve the tags, and schedule it onto the AccuKnox
company page through Zernio.

Merged on 2026-09-18 from `linkedin_post_digital_twin` (voice and strategy) and
`accuknox_linkedin_post` (the Zernio recipe). Both of those came from a
different agent harness whose `zernio_call_tool` and `pd_linkedin_*` tools do
not exist here, so the mechanics were rewritten against the Zernio REST API and
verified live. Delete any older copy of either skill rather than keeping two.

## Six Pieces Ship With Every Post, or It Does Not Go

Never ship a bare post. Every AccuKnox LinkedIn post carries all six:

1. **Copy** written in the voice below, drafted and shown before anything is scheduled.
2. **No link in the body.** A link in the caption suppresses reach. `li.py` refuses to schedule a post whose body contains one.
3. **A first comment** holding the link, which posts from the page automatically on publish.
4. **A CTA line** pointing at the comment, such as "Read the full blog via the link in the comments."
5. **The leadership roster**, appended to the end of every post. `li.py` adds it automatically, so never type it by hand. Any partner or speaker tags go on their own line above it. See the roster section below.
6. **An image.** 70 of the 77 posts in the 2026-08-11 performance pull were image posts, so images are the house default. That sample is too one-sided to prove images win, only that nothing else has been tried.

If the requester leaves a piece out, fill it with a sensible default or ask one
question. Do not silently drop it.

## Six Steps Run Before Any Draft Is Shown

1. **Diagnose.** What is it about, which post type (announcement, recap, webinar, event, blog, ebook, video, partnership, customer win, analyst, press release, milestone, award), which audience (CISO vs security engineer vs developer, which changes depth and hook), what CTA, what source material.
2. **Read the real source.** Never draft from a title. Open the blog, the ebook landing page, the event listing. Pull the argument, the numbers, the CVEs, the frameworks. Never invent a metric, a quote, a customer name, or a "first / only / best / leader" claim the source does not support.
3. **Mirror the sample.** Grep `references/style_examples.json` for 3 to 5 posts of the same type and match their rhythm before writing a line.
4. **Draft, then cut.** See the editing discipline below.
5. **Self-check** against the QC list in `references/full_prompt_spec.txt` section 20.
6. **Show the draft** and wait. Only then resolve tags and schedule.

If something critical is missing and cannot be inferred from the attached
content, ask one smallest question. Do not interrogate.

## Five Files Hold the Voice and the Numbers

| File | Holds |
|---|---|
| `references/style_examples.json` | 68 real AccuKnox posts with text, hashtags, likes and date. Read before drafting. |
| `references/full_prompt_spec.txt` | The full brief: process, post-type taxonomy, audience detection, CTA logic, QC checklist. Read once per new post type. |
| `references/natural_writing_rules.txt` | The banned-pattern list with before and after examples. |
| `references/content_strategy_engine.txt` | The strategy framework behind the decision rules below. |
| `scripts/li_performance_baseline.py` | Pulls day-of-week and format performance live from the LinkedIn API. |

## The Hook Has 210 Characters Before LinkedIn Cuts It

**Hooks.** Specific and concrete. A number ("$180,000 burned in 72 hours"), a
blunt claim ("Zero Trust for AI Agents is here"), a real question ("What is your
AI missing?"), a plain announcement ("BLACK HAT USA 2026."), a day marker
("TODAY. 4:30 PM IST"). Never "In today's rapidly evolving landscape", "We are
thrilled to announce", or "This is where AccuKnox comes in."

The first paragraph has to survive truncation. LinkedIn cuts at roughly 210
characters behind "see more", so the claim that earns the click lives above
that line. `li.py plan` counts this and warns.

**Sentences.** Short, punchy, conversational. Standalone one-liners as their own
paragraph. A mix of "we" for company news and third person for product
statements. Direct address ("Your AI. Their exposure.") appears sometimes.

**Emojis.** Zero to three, at the hook or as bullet markers, never decorative.
Roughly 30% of the sample uses none, so do not force them. Recurring set:
🚀 🎉 🚨 🔵🔴 ✨ 💙 🤝 🔐 📍 🏆 🎊 and country flags for market posts. `↳` and
`▪` `▸` are the usual list markers rather than plain dashes. Use a real
codepoint, never a lone surrogate.

**Hashtags.** Three to five, topical and specific, at the very end. About a
third of the sample uses none at all, which is a valid choice. camelCase is
fine (`#ContainerSecurity`). Never dump a generic block like
`#AI #Cybersecurity #Technology #Innovation #Cloud #Security`.

**Formatting.** Paragraphs of one to three lines, blank line between. Bullets
for feature lists. The CTA as its own short line near the end.

**Terminology.** Exact product and category names: CNAPP, KSPM, CSPM, CWPP,
ASPM, AI-SPM, AI-DR, eBPF, BPF-LSM, KubeArmor, Zero Trust, Prompt Firewall,
xBOM, SPIFFE, AgentZ, ModelKnox. Never swap a term for variety.

## Cut to Half the Words, Then Add Back Only What Is Missing

Draft, then cut. Kill lines that restate the headline. Do not enumerate every
item in the source: pick two or three and imply the rest. Merge sentences that
share one idea. Target half the words, then add back only what is missing.

Three to five short scannable lines beat a dense paragraph. A strong one-line
hook plus one proof point plus one CTA beats a comprehensive summary. Event
recaps and detailed customer wins earn more length because the audience wants
specifics. Everything else defaults to trimming.

`li.py plan` flags anything over 1300 characters. The hard cap is 3000.

## Two Tests Catch Copy That Reads Like a Machine Wrote It

The repo rules in `CLAUDE.md` and `.claude/core/writing-rules.md` are the
mechanical baseline. These are the voice layer on top.

- No manufactured punchlines or bridge sentences. "This is what X looks like when...", "Not a demo. The real thing.", "That's the difference." If a sentence carries no new fact, context, CTA or reaction, cut it.
- State facts plainly rather than sloganising them. "Covered vulnerability detection and CERT-In field mapping", not "all came through clean."
- Plain verbs. Passed, completed, tested, validated, ran. Not demonstrated, showcased, empowered.
- Do not over-explain why something matters. Match the emotional pitch to the actual news.
- Test every sentence twice. Could a competitor post this unchanged? Would a real AccuKnox marketer say it out loud to a colleague? If either answer is wrong, rewrite or cut.

**Override.** These are defaults. When the content owner explicitly asks for a
hype opener, an emoji or an exclamation mark, put it back. They have final call
on tone.

## A Customer Win Runs Five Lines and One Number Set

Roughly five lines. Emoji hook ("🚀 Big win!"), who partnered and why in one
sentence, one sentence collapsing every finding into a single number set with no
critical-versus-high breakdown, one sentence on the outcome, then the CTA. A
fuller stat breakdown only on request.

Never lift an anonymised customer's name out of a page's SEO title. If the blog
body says "a leading global airline", that is the name. Flag it rather than
treating a title-cased phrase as real.

## Event Detail Lives in Luma JSON, and Guests Are Not Speakers

`accuknox.com/events/...` pages render their real detail from an embedded Luma
widget, so a plain markdown scrape returns navigation and nothing else. Scrape
`--format rawHtml --wait-for 9000` and read the inlined JSON instead.

The fields that matter are `start_at` and `end_at` (UTC, convert yourself),
`timezone`, and `geo_address_json` for a physical venue.

**`featured_guests` is the registrant list, not a speaker list.** Never name
anyone as a speaker from that field. If no speakers are published, tag the host
and the partner company page and say that speakers are unconfirmed.

Verify that the promo date actually sits before the event date. An event page
whose Luma date is six weeks after the scheduled promo is a scheduling bug, not
a copy problem, so raise it before drafting.

## Challenge the Request Before You Write the Post

Be the strategist, not only the copywriter. Full framework in
`references/content_strategy_engine.txt`.

- **Pull performance live.** `py -3.11 scripts/li_performance_baseline.py [--since YYYY-MM-DD]` hits the LinkedIn API directly. Org URN `urn:li:organization:14651364`. Do not use the cached Marketing Analytics sheet, which has no post-format data. Re-run rather than quoting a stale number, and always label a figure with its pull date.
- **Baseline, pulled 2026-08-11, n=77 posts, impressions ≥100.** Monday leads engagement at 5.41%, Friday leads reach at 3,483 impressions. The spread is mild, all days inside 4.55% to 5.41%. 70 of 77 were image posts, so there is no evidence on which format wins. Images are simply all that has been tried.
- **Be upfront about the gaps.** LinkedIn's API exposes no time-of-day field and no topic or CTA tag. "Best time to post" and "best topic" cannot be answered with AccuKnox data. Say so rather than inventing a pattern.
- **Challenge a weak request.** Evaluate value, timing, repetition and recency before agreeing. When you push back, name the evidence and propose a specific alternative day or angle.
- **Track fatigue.** Check recent posts for the same topic, product or CTA back to back. Two promos for one webinar need two different entry points, not two rewordings.
- **Think in campaigns.** A launch runs awareness, then consideration, then launch, then post-launch, ramping toward the date. It is not one announcement repeated for a month.
- **Match confidence to evidence.** "Early signal" for one or two data points, "pattern" for a handful, "consistently" only for many observations over time.

## One Script Writes to the Page, and Only With --live

`li.py` is the only path. Do not use the FavStash MCP, which reaches Instagram,
YouTube and TikTok only, and do not schedule through the Zernio web UI, because
only `li.py` writes the `_sent.tsv` ledger.

Full SOP in `README.md` beside this file. The short version:

```bash
py -3.11 .claude/skills/accuknox-linkedin-post/li.py plan campaigns/<file>.md
py -3.11 .claude/skills/accuknox-linkedin-post/li.py tags campaigns/<file>.md
py -3.11 .claude/skills/accuknox-linkedin-post/li.py send campaigns/<file>.md --live
```

Dry run is the default on every command. Nothing leaves the machine without
`--live`, and a live write to the company page needs Atharva's explicit
go-ahead every time.

### The two-profile trap

One `ZERNIO_API_KEY` reaches two profiles under one user. The Personal profile
holds Atharva's own X and Instagram. `li.py` pins every call to the AccuKnox
profile and re-checks the pinned account ID, platform, profile, username and
enabled flag on each run, so a wrong destination is an error rather than a
silent mis-send.

| Thing | Value |
|---|---|
| Profile | AccuKnox, `6a7ebc0ab7c6776815670114` |
| LinkedIn account | `AccuKnox`, `6a80942677555aae01131b68` |
| Org URN | `urn:li:organization:14651364` |
| Key | `ZERNIO_API_KEY` in `D:\Atharva\NOTES\.env`, never copied into this repo |

### The roster goes on every post, and the script adds it

Fourteen names close every AccuKnox post, in a fixed order, as their own
paragraph between the body and the hashtags. `ROSTER` in `li.py` holds it
pre-resolved, so it costs no API call and cannot drift. Never hand-type it, and
never reorder it.

The line runs 572 raw characters and renders as 195, so it leaves roughly
2,428 of the 3,000 cap for the body.

```
Rahul Jadhav @[Brian Laing](urn:li:person:1_hyf_Kkj2) @[Phil Porras](urn:li:person:NRO9pOGMwC)
@[Nat Natraj](urn:li:person:eMG-5lrxYG) @[Raj Panchapakesan](urn:li:person:wa6BAPBF-Z)
@[Saqib Syed](urn:li:person:BxZyI5TInj) @[Raghuram Madabushi](urn:li:person:8NzWZ_xnj9)
@[Sunil Sapra](urn:li:person:SJaMyws9at) @[Rajeev Punetha](urn:li:person:d0l9fqc1oO)
@[John Kirch](urn:li:person:Z_29xCBYO-) @[Vineel Kurumella](urn:li:person:OMl-GgumFD)
@[Parthasarathy Thulasi](urn:li:person:5DaNU4amLg) @[Syed Hadi](urn:li:person:3pITlsoPHn)
@[Atharva Shah](urn:li:person:vgNIoB5fbg)
```

**Barun Acharya is never tagged.** He appears in the two posts published on
2026-09-16. Atharva removed him on 2026-09-18. Do not add him back, and do not
copy the roster line out of those two older posts.

**Rahul Jadhav is plain text and comes first, on purpose.** He is CTO. His
profile is `in.linkedin.com/in/rahul-jadhav-a0485310`, confirmed from
AccuKnox's own post linking to it, and LinkedIn's URL-to-URN endpoint refuses
that exact profile across every variant tried.

Two other profiles do resolve, `/in/rahuljadhav` as `urn:li:person:opvtc8E0N0`
and `/in/rahul-jadhav` as `urn:li:person:5j_ai1-iOX`. **Neither is the AccuKnox
CTO.** Rahul Jadhav is a common name. Never substitute one of those to make the
tag clickable, because that tags a stranger from the company page. A plain name
reads correctly and is the safe failure.

`roster: no` on a post drops the line. Use it only when asked.

### Extra tags sit on their own line above the roster

`tag:` lines add a partner company, a host or a speaker. `li.py` resolves them
through `GET /accounts/{id}/linkedin-mentions?url=&displayName=` and places
them between the body and the roster. `li.py tags` previews what will and will
not render.

A **company page always resolves.** A **person resolves only when the AccuKnox
page can see them**, so a non-follower returns no `mentionFormat` and ships as
plain text. `send` prints which names that happened to.

| Organization | URN |
|---|---|
| AccuKnox | `urn:li:organization:14651364` |
| TD SYNNEX | `urn:li:organization:74956728` |
| TD SYNNEX Japan | `urn:li:organization:14535604` |
| Shield Core | `urn:li:organization:91317284` |

Other confirmed people outside the roster: Samir Boukharta, SecuVerse.ai
founder, `urn:li:person:9K3rQA-jR-`.

Does not resolve: **Rahul Jadhav** and **Mehlam Shakir** as people, and
**SecuVerse.ai** has no findable company page.

### Media

Zernio-hosted media auto-deletes after 7 days, silently, and a post scheduled
past that publishes with a dead image. A public `help.accuknox.com` or
`accuknox.com` URL in `media:` skips the upload and never expires, so prefer one
whenever the image already lives on a site. `li.py plan` marks every uploaded
image that fires after the TTL, and `sync-media --live` re-uploads onto posts
that are already scheduled.

## Lead With the Post, Then One Line of Internal Note

Give the finished post first, then a short internal note: post type, audience,
CTA, source used. Offer alternative angles only when asked for options.
