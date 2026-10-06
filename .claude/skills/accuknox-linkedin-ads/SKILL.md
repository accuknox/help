---
name: accuknox-linkedin-ads
description: Plan, check and present AccuKnox paid ad campaigns on LinkedIn, with X and Reddit for AgentZ. Use this skill whenever the user asks to plan a LinkedIn ad, run a paid campaign, set a LinkedIn budget, write ad copy or a Lead Gen Form, pick an ICP or audience, choose a CTA, set up retargeting, review campaign results, judge cost per lead, make ad image mockups, or build or update the paid ads playbook deck in Google Slides. Triggers include "LinkedIn ads", "paid ads", "lead gen campaign", "Campaign Manager", "ad budget", "$1,000 campaign", "lead gen form", "ad mockup", "ads playbook", "campaign deck" and "how did the ads do". Carries the $1,000 budget rules, the pre-launch checklist, the kill rules, the copy checker, the mockup renderer and the Google Slides publisher. It plans and checks campaigns. For a single generated ad image with an image model, use the cloud skill anthropic-skills:accuknox-linkedin-ads instead.
---

# AccuKnox Paid Ads

This skill turns a campaign idea into a launch-ready plan, and keeps every plan in one Google
Slides deck that leadership reviews. Every campaign runs on a fixed $1,000 a month, so the skill
spends its effort on narrowing the audience, sharpening the offer and killing weak ads fast.

The Q4 2026 deck is the reference build:
[`references/campaigns/paid-ads-q4-2026/`](../../../references/campaigns/paid-ads-q4-2026/).
Read its `campaigns.json` and `build_deck.py` before you start a new quarter.

## Five Rules Hold for Every Campaign

1. **The budget is $1,000 per campaign per month.** Never recommend more. Plan inside the cap.
2. **The goal is a demo-ready lead.** The objective is Lead generation with a native LinkedIn Lead
   Gen Form, the offer is a demo or a bottom-of-funnel asset, and success is counted in demos held.
   Brand awareness, engagement and cheap ebook downloads are out of scope.
3. **Never name a competitor.** Not in an ad, the copy, the deck or a speaker note. Group old
   campaigns that carried a competitor name as "replacement campaigns".
4. **Every number has a source.** A benchmark carries its publisher and date. A fact nobody has
   gets an amber `[bracket]` and an owner.
5. **Account data stays private.** The repo is public. Account IDs, spend, the analytics sheet link
   and the deck link live in `config.local.json` and `private/` folders, both gitignored.

## The Workflow Runs in Six Steps

1. **Load the playbook.** Read [`references/playbook.md`](references/playbook.md). It holds the
   budget split, the settings, the form standard, the checklist and the kill rules, each with its
   source.
2. **Fill the brief.** Copy the campaign block in `campaigns.json` and fill every field in
   [`references/campaign-brief.md`](references/campaign-brief.md). Leave a `[bracket]` for any
   fact the requester has not given.
3. **Write three ads.** Two photo parables or one parable and one second screenshot, plus one
   product proof. A plain gradient with text does not ship, because it stops nobody in the feed. The copy
   rules are in the playbook. Run the checker:

    ```bash
    python .claude/skills/accuknox-linkedin-ads/scripts/check_copy.py references/campaigns/<folder>/campaigns.json
    ```

4. **Render the mockups.** Photos come from Pexels and go in the campaign's `photos/` folder with a
   `LICENSES.md` line each. Product screenshots come from `references/PRODUCT UI/`.

    ```bash
    python .claude/skills/accuknox-linkedin-ads/scripts/render_ads.py references/campaigns/<folder>/campaigns.json references/campaigns/<folder>/mockups
    ```

5. **Build the deck.** Copy `build_deck.py` from the reference build, change the `PLAN` and `ADS`
   blocks, and run it. The deck stays at 20 slides or fewer. It opens on the cover from the
   AccuKnox master template (`assets/ppt-template.pptx`, layout 0), then a contents slide with
   clickable rows, eight playbook slides, a campaigns-at-a-glance slide, and two slides per
   campaign on one template: a plan slide and an ads slide with large mockups. It closes on
   layout 1. Content slides use layout 4. It imports the primitives from `scripts/deck_kit.py`. The past-results slide
   needs a CSV export of the analytics sheet's LinkedIn Paid Ads tab in the campaign's `private/`
   folder, named in `past_ads_csv`, with `past_ads_snapshot` set to the latest Report Date. The
   columns run Report Date, Campaign, Ad Account, Currency, Status, Start Date, End Date,
   Impressions, Clicks, CTR %, Spend, Cost per Lead, Leads, Conversion Rate %, Demo Bookings. Without
   the file, the deck builds without that slide.

6. **Publish to Google Slides.** The first run creates the deck and saves its link in
   `config.local.json`. Later runs replace the content behind the same link.

    ```bash
    python .claude/skills/accuknox-linkedin-ads/scripts/publish.py references/campaigns/<folder>/out/<deck>.pptx --thumbs references/campaigns/<folder>/out/thumbs
    ```

    Read every thumbnail before you hand the link over. The contents links survive the import as
    slide links, and `gws slides presentations get` shows them as `link.pageObjectId`. Also open the
    file in PowerPoint once, because PowerPoint rejects animation XML that Google Slides accepts. Add `--share` once to give everyone at
    accuknox.com edit access.

## Results Review Uses the Analytics Sheet

The LinkedIn Marketing API needs a developer app with Advertising API approval, and AccuKnox has
none. So results come from the analytics sheet in `config.local.json`, which the team updates every
Monday. Read it with the `gws-sheets` skill. The sheet repeats every campaign in each monthly
snapshot, so use only the latest snapshot. Judge each campaign on the kill rules in the playbook,
then on demos held.

## Setup on a New Machine Takes Four Commands

```bash
pip install python-pptx lxml playwright pillow
```

```bash
python -m playwright install chromium
```

```bash
cp .claude/skills/accuknox-linkedin-ads/config.example.json .claude/skills/accuknox-linkedin-ads/config.local.json
```

```bash
python .claude/skills/accuknox-linkedin-ads/scripts/setup_vendor.py
```

Fill every value in `config.local.json`. `publish.py` also needs the `gws` CLI, signed in with
Drive and Slides scopes. Check it with `gws auth status`.

The second command clones the open LinkedIn Ads Manager plugin into `vendor/` for reference. The
plugin has no license, so it stays gitignored, its text never enters this skill, and nothing here
depends on it. Every script in the plugin needs the Marketing API, which AccuKnox does not have.

## Nine Files Make up the Skill

| Path | Holds |
|---|---|
| `references/playbook.md` | The rules, the numbers and their sources |
| `references/campaign-brief.md` | The fields every campaign fills before it gets a slide |
| `scripts/check_copy.py` | Length, opener and competitor-name checks on ad copy |
| `scripts/render_ads.py` | 1200 x 1200 mockups from a campaigns file, through Playwright |
| `scripts/deck_kit.py` | Brand slide primitives with entrance animations that survive the Google Slides import |
| `scripts/publish.py` | Upload to Google Slides, keep one link, pull thumbnails, share with the domain |
| `scripts/setup_vendor.py` | Clone the reference plugin into the ignored `vendor/` folder |
| `assets/` | The AccuKnox master PPT template and logos for dark and light backgrounds |
| `config.example.json` | The config shape. Copy it to `config.local.json` |

## What This Skill Does Not Do

It does not create, launch or pause anything in Campaign Manager, because there is no API access. A
person launches each campaign by hand from the deck and the checklist. It does not produce final
ad images either. The mockups show the idea, and a designer finishes them.
