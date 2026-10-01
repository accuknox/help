# The $1,000 LinkedIn Playbook

Every rule here assumes one campaign, $1,000, 28 days and one goal: a demo-ready lead. The deck
shows the same rules to leadership. When a rule changes, change it here first, then rebuild the deck.

## $1,000 Buys About Five Leads Under Good Conditions

| Metric | Range | Source |
|---|---|---|
| Cost per click | $6 to $12, cybersecurity $8 to $15 | Google AI Overview, 2026-10-01, citing TripleDart and Stackmatix |
| Clicks per $1,000 | 83 to 166 | Same |
| Cost per lead, Lead Gen Form | $150 to $300+ | Same |
| Leads per $1,000 | 3 to 7 | Same |
| Spend-weighted CPL | $202 | Metadata.io, 138 advertisers, $57.6M of 2025 spend |
| CPC, CPM, CTR | $9.39, $63.19, 0.67% | Same |
| CPL, Lead Gen Form against landing page | $193 against $346 | Same |
| Win rate on traced opportunities | 19.5% | Same |
| First impression to revenue | 281 days | Dreamdata, LinkedIn Ads Benchmarks Report 2026 |
| Lead Gen Form completion rate | 13% average | LinkedIn Marketing Blog, Lead Gen Forms guide |

At these rates one flight yields about 15,800 impressions, 106 clicks and 5 leads. Plan on 3 leads
and 1 to 2 demos per campaign, because AccuKnox's own narrow-audience campaigns cost several hundred
dollars per lead. Best case is 7. Treat every number as a range. At 5 leads a month, one lead more
or less moves CPL by 20%.

AccuKnox's own history shows the trap. The 2026-10 audit of the analytics sheet found cheap leads
from broad, low-cost placements, and no lead traced to a demo. The narrow campaigns cost several
hundred dollars per lead, which is what a real buyer costs. The figures stay in the gitignored
`private/` folder of each campaign, because this repo is public.

## Six Account Problems Get Fixed Before Any Campaign

A 2026-10-01 audit of Campaign Manager found six problems. Recheck all six at the start of every
quarter, because each one wastes spend no matter how good the ads are.

| Problem | Fix |
|---|---|
| The 404 page gets about 50,000 visits a month, which points to bots or broken links | Find the source in GA4, block bots in Cloudflare, and build audiences from real page URLs |
| Factors.ai conversions show "No activity" but sit on live ad sets | Repair the Factors.ai sync, or archive those conversions |
| The one active conversion is attached to 0 ad sets | Attach the four shared conversions below to every ad set |
| A demo-button click counts as a Qualified lead, across 4 button names | Track the booking page as Book appointment, and keep clicks as Contact |
| No conversion uses the Lead type | Add a Lead conversion on the form thank-you page |
| Tracking sends only the source, spelled "LinkedIn" | Use the account tracking string below |

## One Tracking String and Four Conversions Make Results Measurable

Paste this into Account settings, Account-level parameters, as one line. The macros are the October
2025 names from LinkedIn Help a5968064. Name campaigns, ad sets and ads with no spaces.

```text
utm_source=linkedin&utm_medium=paid-social&utm_campaign={{CAMPAIGN_NAME}}&utm_term={{AD_SET_NAME}}&utm_content={{AD_NAME}}&li_ad_id={{AD_ID}}
```

Add the same values by hand to each form's thank-you link.

| Conversion | LinkedIn type | Counts when | Use |
|---|---|---|---|
| Demo booked | Book appointment | The page after a Cal.com booking loads | Optimize for it |
| Website lead | Lead | The contact or demo form thank-you page loads | Report |
| Demo button click | Contact | A demo button is clicked | Report only |
| Qualified lead | Qualified lead | Salesforce marks the lead as qualified | Judge campaigns on it |

Attach all four to every ad set. The CRM is Salesforce. Lead Gen Forms sync to Salesforce Sales
Cloud through LinkedIn's native integration (Help a425316), and Salesforce drops the LinkedIn
profile URL field. Connect CRM in the conversion settings, then pick Salesforce, so the Qualified
lead signal comes from real sales stages.

## The Budget Splits $850 to Prospecting and $150 to Retargeting

- One campaign group capped at $1,000, holding two campaigns. LinkedIn sets the budget per
  campaign, so the split needs two of them.
- Prospecting campaign: $850 lifetime over 28 days, about $30 a day.
- Retargeting campaign: $150 lifetime over days 15 to 28, about $10.70 a day. LinkedIn's daily
  minimum is $10 [unverified, LinkedIn Help does not state it].
- One campaign per product. Never run parallel copies of one campaign, because they split the
  budget and bid against each other.
- Two campaigns aimed at the same titles run one after the other, never at the same time. When two
  must overlap, take the shared titles out of one of them.

## Eight Settings Decide Whether the Money Reaches a Buyer

1. **Objective is Lead generation** with a native Lead Gen Form. Never Website visits, Engagement or
   Video views. One past "video views" boost spent $140 for 39 clicks and 0 leads.
2. **Bid manual CPC** at the low end of LinkedIn's suggested range, never above $15, and raise it
   10 to 15% if spend runs under 80% of pace for 3 days. If the suggested floor sits above $15,
   widen company size one band and keep the bid. Practitioners disagree here. Some start on Maximum delivery,
   but with a hard cap manual CPC keeps week 1 from buying expensive impressions (ZenABM, 2026-02).
   LinkedIn's three strategies are on LinkedIn Help a421112.
3. **Audience of 50,000 to 150,000**, built from job titles only, with no seniority facet. A
   seniority filter drops architects and governance leads whose seniority reads Senior or Manager.
   LinkedIn suggests 50,000 or more (Help a423690). Under 50,000 delivery stalls and CPM climbs.
   Over 150,000 most buyers never see the ad once. Paste the forecast onto the campaign slide.
4. **Audience Expansion off.** LinkedIn turns it on by default (Help a418929).
5. **LinkedIn Audience Network off.** It serves ads off LinkedIn (Help a423409). The past campaigns
   with a CPM of $1 to $5 point to broad or off-LinkedIn delivery.
6. **Geography** US, Canada, UK and Western Europe only. LinkedIn has no Western Europe region,
   so add DE, FR, NL, BE, LU, AT and CH and IE as countries.
7. **Exclusions** current customers, AccuKnox employees, competitor companies, students and
   entry-level titles.
8. **Rotation** set to optimize for performance, with 3 ads live.

## The Lead Gen Form Has Seven Fields and Ends on a Calendar

- Five profile fields: first name, last name, work email, company, job title. Four always prefill.
- Two multiple-choice questions: one priority question and one timeline question. No free-text
  question, because each one cuts submissions by 3 to 4% (LinkedIn Marketing Blog).
- Put the neutral answer first, such as "Just researching". LinkedIn pre-selects the first option,
  so a careless submit must land on the cold answer.
- Work email prefills only when LinkedIn validates the profile email as a work address.
- No phone field. Most profiles lack one, so it blocks the prefill.
- Tick **Validate work email**. It blocks Gmail, Hotmail and Yahoo (Help a1381647).
- Add hidden fields for campaign, lead source and offer before launch. LinkedIn does not allow
  adding them once the form runs on a live campaign. Hidden values are fixed per form, so ad-level
  results come from the leads report.
- Add the privacy policy link and a marketing-consent checkbox, because the UK and EU are in the
  geography.
- Write the form headline as a question, under 120 characters.
- The thank-you button opens the booking page, so a ready buyer books on the spot.
- Download or sync leads daily. Campaign Manager keeps them for 90 days.
- Call a "This quarter" lead within 1 business hour and every other lead the same business day.
  Log the demo status in the analytics sheet within 48 hours.
- Track the booking with the "Demo booked" conversion above. The Cal.com confirmation redirects
  to an accuknox.com thank-you page, which fires it.
- Leads sync to Salesforce through the Lead Gen Form integration.

## Twelve Boxes Get Ticked Before Launch

1. Objective is Lead generation.
2. Lifetime budget $1,000 with start and end dates.
3. Audience forecast between 50,000 and 150,000.
4. Audience Expansion off and Audience Network off.
5. Exclusion lists attached.
6. Manual CPC bid at the low end of the suggested range.
7. Validate work email ticked, neutral answers first, privacy link and consent box on the form.
8. Thank-you button opens the booking page.
9. Hidden fields added.
10. Leads sync to Salesforce, and the four conversions sit on every ad set.
11. CookieYes blocks the Insight Tag until a visitor accepts advertising cookies.
12. UTMs use `utm_source=linkedin` and `utm_medium=paid-social`.

Item 11 was open on 2026-10-01. The tag fired on accuknox.com with advertising consent set to no.

## Retargeting Waits for 300 Matched Members

Retargeting runs on days 15 to 28 at $150, with a product-proof ad and the same form. LinkedIn needs
300 matched members before it serves an audience (Help a420552), and one campaign makes only about
40 form openers. So the retargeting campaign uses one combined audience: visitors to real
accuknox.com pages such as /platform, /blog, /demo and /pricing over 180 days, company page visitors
over 365 days, and openers of any AccuKnox Lead Gen Form over 365 days. Never use "all website
visitors", because the 404 page draws most of that traffic. Readers of the AI kill-switch blog,
about 6,000 a month, make the best pool for an agent security campaign. Below 300, the $150 stays in prospecting. The cookie-consent fix will shrink the EU part of
the website audience. help.accuknox.com has no Insight Tag, so docs readers cannot be retargeted yet.

## Kill Rules Run Every Monday

| Signal | Threshold | Action |
|---|---|---|
| CTR on one ad | Under 0.4% after 1,000 impressions | Pause that ad |
| Suggested bid | LinkedIn's floor sits above $15 | Keep the $15 bid, widen company size one band |
| Leads | Zero after $500 spent | Swap to the fallback assessment offer, on the same demo form |
| Cost per lead | Over $400 after $800 spent | Narrow the audience |
| Spend pace | Under 80% of the daily budget for 3 days | Raise the bid 10 to 15% |

The creative and the bid change mid-flight. The audience changes only by the cost-per-lead rule, and
the offer only by the zero-lead rule. The fallback is always an assessment on the demo form, such as
a free red-team test of one model endpoint, never a download.

Week 1: launch on a Monday and leave bids alone for 3 days. Week 2: pause the weakest ad and read
lead quality with sales. Week 3: add one fresh ad, and retargeting starts on day 15. Week 4: change nothing,
then log results and demos held in the analytics sheet.

## Each Ad Carries One Picture, One Claim and One Ask

- Square image, 1200 x 1200. Horizontal 1200 x 628 also works. JPG or PNG under 5 MB.
- Intro text under 150 characters, because LinkedIn hides the rest behind "see more". Headline
  under 70 characters. Both limits are on the LinkedIn single image ad specs page.
- Open on the buyer's world. Never start the intro with "We" or "AccuKnox".
- One CTA per ad, matched to the form. Request Demo for a demo, Download for an asset.
- AccuKnox logo top left, 60 px clear of every edge.
- Three ads per campaign. A photo parable stops the scroll. A product proof shows the console.
  The third ad is a second photo or screenshot. A plain gradient with text never ships.
- Never name a competitor.

## X and Reddit Follow the Same Budget Rule

AgentZ runs on X and Reddit because its buyers are developers. The goal there is a free-tier signup,
so the kill rule counts signups, never CTR alone. Judge each ICP across both platforms combined, on
day 7, because a smaller cell is noise. Each platform needs its pixel and a signup
conversion event before launch, and every link carries UTMs.
