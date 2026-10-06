"""Build the Q4 2026 paid ads playbook deck on the AccuKnox master template.

    python build_deck.py            # writes out/paid-ads-playbook-q4-2026.pptx

Twenty slides. Part 1 is the reusable playbook, executive slides first. Part 2 gives
each campaign the same two-slide template: a plan slide and an ads slide.

Private input, never committed: ../../../.claude/skills/accuknox-linkedin-ads/config.local.json
Publish with the skill's publish.py, which converts the file to Google Slides.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parents[2] / ".claude" / "skills" / "accuknox-linkedin-ads"
sys.path.insert(0, str(SKILL / "scripts"))
from deck_kit import *  # noqa: E402,F403

CFG = json.loads((SKILL / "config.local.json").read_text(encoding="utf-8"))
DATA = json.loads((HERE / "campaigns.json").read_text(encoding="utf-8"))
CAMPS = {c["id"]: c for c in DATA["campaigns"]}
MOCK = HERE / "mockups"
OUT = HERE / "out"
X0, XW = 0.4, 9.2          # body left edge and width on the template
Y0 = 0.98                  # first body line under the title band

prs = from_template()


def checkbox_rows(s, x, y, w, items, size=11.5, row=0.44):
    objs = []
    for i, it in enumerate(items):
        yy = y + i * row
        b = shape(s, "round", x, yy, w, row - 0.06, fill=OFF if i % 2 == 0 else WHITE, line="D5DBEE", radius=0.12)
        shape(s, "rect", x + 0.14, yy + (row - 0.06) / 2 - 0.1, 0.2, 0.2, fill=WHITE, line=BLUE, lw=1.5)
        text(s, x + 0.48, yy, w - 0.6, row - 0.06, it, size=size, color=INK, anchor="m")
        objs.append(b)
    return objs


# ================================================================== 1. cover
cover(prs, "The Paid Ads Playbook",
      scope=[("$1,000", "per campaign, per month"), ("3 to 7", "leads at best"), ("4", "campaigns")])

# ================================================================== 2. contents (rows and links filled in at the end)
s_toc = content(prs, "Contents")
TOC = []

# ================================================================== 3. what $1,000 buys
s = content(prs, "$1,000 Buys 83 to 166 Clicks and 3 to 7 Leads at Best")
cards = [("$6-12", "COST PER CLICK", "Security often runs $8 to $15"),
         ("83-166", "CLICKS A MONTH", "Ad clicks or form opens"),
         ("$150-300+", "COST PER LEAD", "With LinkedIn's own form"),
         ("3-7", "LEADS A MONTH", "Best case, fully optimized")]
objs = [stat(s, X0 + i * 2.33, Y0, 2.2, 1.55, a, b, c, fill=TNAVY) for i, (a, b, c) in enumerate(cards)]
flow = [("$1,000", "budget"), ("~15.8K", "ad views"), ("~106", "clicks"), ("~3", "leads"), ("1 to 2", "demos"), ("0 to 1", "deal")]
cols = [TNAVY, "1A2C8F", NAVY, BLUE, PURPLE, RED]
for i, (n_, l_) in enumerate(flow):
    c = shape(s, "chevron" if i else "pent", X0 + i * 1.53, 2.7, 1.6, 0.85, fill=cols[i])
    label(c, [f"**{n_}**", l_], size=11.5, pad=0.02)
    objs.append(c)
box = shape(s, "round", X0, 3.75, XW, 0.72, fill=LIGHT_RED, line=RED, radius=0.08)
label(box, ["**We plan on 3 leads and 1 to 2 demos per campaign.** LinkedIn's ideal budget is $3,000 to $5,000 a month. "
            "Ours stays at $1,000, so the audience, the offer and the form do the work."], size=12, color=INK, align="l", pad=0.2)
terms = text(s, X0, 4.55, XW, 0.6, ["**Terms.** A lead is one completed form. A demo is a held sales meeting. Cost per lead is spend divided by leads.",
                                      "Source: Google AI Overview, 2026-10-01, citing TripleDart and Stackmatix. Funnel rates from Metadata.io 2025."],
             size=10, color=MID, after=2)
anim(s, *objs, box, terms, effect="fly_up", step=140)
notes(s, "The four cards are the best case for a fully optimized $1,000 campaign. The arrow row shows how $1,000 thins out. "
         "Metadata.io puts views at $63 per 1,000 and clicks at 0.67% of views. We plan on 3 leads, not 7, because our own "
         "narrow-audience campaigns cost several hundred dollars per lead.")
SLIDE_BUYS = s

# ================================================================== 4. disclaimer
s = content(prs, "Read Every Number in This Deck as a Range")
cards = [("Third-party estimates", "The $1,000 math comes from public benchmarks and an AI search summary. LinkedIn guarantees no result.", RED),
         ("Best case only", "3 to 7 leads needs a tight audience, strong ads and a clean setup. A weak month gives zero.", RED),
         ("Small numbers swing", "At 5 leads a month, one lead more or less moves cost per lead by 20%. Judge after 4 weeks.", AMBER),
         ("Leads are not revenue", "A lead is a form fill. Dreamdata measured 281 days from first ad view to revenue.", AMBER),
         ("Mockups are drafts", "The ad images show the idea. The designer finishes them before launch.", BLUE),
         ("Brackets need an answer", "An [amber bracket] marks a fact we do not have yet. Nothing launches with one open.", BLUE)]
objs = []
for i, (t, b_, col) in enumerate(cards):
    bx, _ = card(s, X0 + (i % 3) * 3.08, Y0 + (i // 3) * 2.08, 2.96, 1.95, t, b_, accent=col, tsize=14, bsize=12)
    objs.append(bx)
anim(s, *objs, effect="fade", step=150)

# ================================================================== 5. six setup problems
s = content(prs, "Six Setup Problems Waste Money Before Any Ad Runs")
rows = [["#", "What we found in Campaign Manager", "Why it hurts", "Fix"],
        ["1", "The 404 page gets about 50,000 visits a month, 8x our best blog post", "Bots and broken links fill every website audience",
         "Find the source in GA4. Block bots in Cloudflare. Build audiences from real page URLs"],
        ["2", "Three Factors.ai conversions show \"No activity\" but sit on 6, 6 and 12 ad sets", "Those ad sets report and optimize against nothing",
         "Repair the Factors.ai sync, or archive the three"],
        ["3", "The one active conversion is attached to 0 ad sets", "No campaign counts what it tracks", "Attach the shared conversions to every ad set"],
        ["4", "A demo-button click counts as a Qualified lead, across 4 button names", "It inflates leads and breaks when button text changes",
         "Track the booking page as Book appointment. Keep clicks as Contact"],
        ["5", "No conversion uses the Lead type", "Website form fills stay invisible to LinkedIn", "Add a Lead conversion on the form thank-you page"],
        ["6", "Tracking sends only the source, spelled \"LinkedIn\"", "GA4 cannot file the visit as paid social or name the ad",
         "Use the full tracking string on the next slide"]]
tb = table(s, X0, Y0, XW, rows, [0.35, 3.2, 2.6, 3.05], size=10.5, row_h=0.57, head_fill=TNAVY)
anim(s, tb, effect="fade")
notes(s, "Found in Campaign Manager screenshots on 2026-10-01: account tracking parameters, conversion tracking and website actions. "
         "Problem 1 matches the analytics sheet, where sessions jumped from 26,472 to 178,089 with 94.58% direct traffic.")

# ================================================================== 6. account configuration
s = content(prs, "One Tracking String and Four Conversions Make Results Measurable")
acct = [["Account item", "Value"],
        ["Ad account", f"{CFG['linkedin_ad_account_id']} [confirm, it bills in INR]"],
        ["USD account", f"{CFG['usd_ad_account_id']}, ran 24 campaigns"],
        ["Insight Tag", f"{CFG['insight_tag_partner_id']}, live on accuknox.com"],
        ["Lead destination", "Salesforce, through the Lead Gen Form sync"],
        ["CRM conversions", "Connect CRM, then pick Salesforce"]]
t1 = table(s, X0, Y0, 4.45, acct, [1.45, 3.0], size=10.5, row_h=0.36, head_fill=TNAVY, bold_first_col=True)
text(s, 5.05, Y0 - 0.02, 4.55, 0.3, "Account tracking parameters, paste as one line", size=11.5, color=INK, font=HEAD, bold=True)
code = shape(s, "round", 5.05, Y0 + 0.3, 4.55, 1.2, fill="0A144A", radius=0.06)
code.name = "code"
label(code, "utm_source=linkedin&utm_medium=paid-social&utm_campaign={{CAMPAIGN_NAME}}&utm_term={{AD_SET_NAME}}&utm_content={{AD_NAME}}&li_ad_id={{AD_ID}}",
      size=10, color="D7DDFF", font="Consolas", align="l", pad=0.15)
nm = text(s, 5.05, Y0 + 1.55, 4.55, 0.6, "**Names use no spaces,** so the values stay readable. Example: campaign ai-security_q4-2026, ad set prospecting, ad a-wolf.",
          size=10.5, color=INK)
conv = [["Conversion", "Type", "Counts when", "Use"],
        ["Demo booked", "Book appointment", "The page after a Cal.com booking loads [confirm redirect]", "Optimize for it"],
        ["Website lead", "Lead", "The contact or demo form thank-you page loads [confirm paths]", "Report"],
        ["Demo button click", "Contact", "Any of the 4 demo buttons is clicked", "Report only"],
        ["Qualified lead", "Qualified lead", "Salesforce marks the lead as qualified", "Judge campaigns on it"]]
t2 = table(s, X0, 3.25, XW, conv, [1.6, 1.6, 4.3, 1.7], size=10.5, row_h=0.36, head_fill=TNAVY, bold_first_col=True)
l1 = text(s, X0, 5.1, 2.5, 0.25, "Open Campaign Manager", size=10, color=BLUE, bold=True)
l2 = text(s, 3.0, 5.1, 2.5, 0.25, "Open the analytics sheet", size=10, color=BLUE, bold=True)
l1.text_frame.paragraphs[0].runs[0].hyperlink.address = CFG["campaign_manager_url"]
l2.text_frame.paragraphs[0].runs[0].hyperlink.address = CFG["analytics_sheet_url"]
anim(s, t1, code, nm, t2, effect="fade", step=220)
notes(s, "Attach all four conversions to every ad set. Archive the old per-campaign Factors.ai conversions once Salesforce sends the "
         "Qualified lead signal. LinkedIn Help a5968064 lists CAMPAIGN_NAME, AD_SET_NAME, AD_NAME and AD_ID under the October 2025 "
         "naming. Add the same parameters by hand to each form's thank-you link.")

# ================================================================== 7. how we run every campaign
s = content(prs, "Every Campaign Runs Eight Steps and Five Weekly Rules")
steps = ["Brief", "Audience", "3 ads", "Form", "Checklist", "Launch", "Review", "Report"]
objs = []
for i, st_ in enumerate(steps):
    c = shape(s, "round", X0 + i * 1.165, Y0, 0.98, 0.75, fill=TNAVY if i < 4 else BLUE, radius=0.15)
    label(c, [f"**{i + 1}**", st_], size=11, pad=0.02)
    objs.append(c)
    if i < 7:
        objs.append(shape(s, "arrow", X0 + i * 1.165 + 1.0, Y0 + 0.28, 0.15, 0.2, fill=MID))
rules = [["Weekly signal", "When it trips", "What we do"],
         ["One ad's click rate", "Under 0.4% after 1,000 views", "Pause that ad, add a fresh one"],
         ["Leads", "Zero after $500 spent", "Switch to the fallback assessment offer"],
         ["Cost per lead", "Over $400 after $800 spent", "Narrow the audience"],
         ["Spend pace", "Under 80% of plan for 3 days", "Raise the bid 10-15%, never above $15"],
         ["Every Monday", "Always", "Log leads and demos held in the analytics sheet"]]
tb = table(s, X0, 2.0, XW, rules, [2.3, 3.0, 3.9], size=11.5, row_h=0.47, head_fill=TNAVY, bold_first_col=True)
anim(s, *objs, tb, effect="fly_left", step=110)
notes(s, "Only the ads and the bid change mid-flight. The audience changes only by the cost-per-lead rule, and the offer only by the "
         "zero-lead rule. Adjust thresholds after two campaigns of our own data.")

# ================================================================== 8. eight settings
s = content(prs, "Eight Settings Decide Whether $1,000 Reaches a Buyer")
cards = [("Lead generation", "LinkedIn's own form. Benchmark cost per lead $193, against $346 for a landing page."),
         ("$1,000 cap", "One campaign per product. Most goes to new buyers, a small slice to retargeting."),
         ("Manual bid, max $15", "Start at the low end of LinkedIn's range. Raise 10-15% if spend lags."),
         ("50,000 to 150,000 people", "Job titles only. A seniority filter drops architects and governance leads."),
         ("Expansion and Network off", "Both are on by default and spend on people outside the plan."),
         ("Four regions", "US, Canada, UK, Western Europe. UK and EU wait for the cookie fix."),
         ("Exclusions", "Customers, our staff, competitor staff, students and entry-level titles."),
         ("Retarget by page", "Product, blog and demo pages. Never the 404 page.")]
objs = []
for i, (t, b_) in enumerate(cards):
    bx, _ = card(s, X0 + (i % 4) * 2.32, Y0 + (i // 4) * 2.08, 2.2, 1.95, t, b_, accent=BLUE if i < 4 else PURPLE, tsize=13, bsize=11.5)
    objs.append(bx)
anim(s, *objs, effect="fade", step=120)
notes(s, "Sources: LinkedIn Help on bidding (a421112), audience size (a423690), Audience Expansion (a418929) and Audience Network "
         "(a423409), plus Metadata.io 2025 benchmarks. Practitioners split on bidding. With a hard cap, a manual bid keeps the first "
         "week from buying expensive views.")

# ================================================================== 9. lead form
s = content(prs, "The Form Asks Seven Things, Then Hands the Lead to Salesforce")
phone = shape(s, "round", X0, Y0, 2.75, 4.15, fill=WHITE, line=INK, lw=1.5, radius=0.07)
text(s, X0 + 0.2, Y0 + 0.12, 2.35, 0.5, "Where is your AI stack exposed?", size=12, color=INK, font=HEAD, bold=True)
fields = ["First name", "Last name", "Work email, checked", "Company", "Job title", "Top priority?", "When will you act?"]
fobjs = []
for i, f in enumerate(fields):
    fb = shape(s, "rect", X0 + 0.2, Y0 + 0.68 + i * 0.4, 2.35, 0.33, fill=OFF if i < 5 else SOFT, line="C9D0E8")
    label(fb, f, size=10, color=INK, align="l", pad=0.08)
    fobjs.append(fb)
sub = shape(s, "round", X0 + 0.2, Y0 + 3.55, 2.35, 0.42, fill=BLUE, radius=0.3)
label(sub, "Submit", size=11, bold=True)
flow = [("Ad", "Request Demo button"), ("Form", "Mostly prefilled"), ("Thank-you", "Opens the booking page"),
        ("Salesforce", "Lead syncs on its own"), ("Sales", "Hot leads called in 1 hour")]
fl = []
for i, (t, sb) in enumerate(flow):
    y = Y0 + i * 0.84
    b = shape(s, "round", 3.45, y, 2.4, 0.66, fill=TNAVY if i < 3 else PURPLE, radius=0.15)
    label(b, [f"**{t}**", sb], size=11)
    fl.append(b)
    if i < 4:
        fl.append(shape(s, "down", 4.53, y + 0.67, 0.24, 0.16, fill=MID))
rules_ = text(s, 6.1, Y0, 3.5, 4.2, [
    "**Validate work email.** It blocks Gmail and other free addresses.",
    "**Neutral answer first.** LinkedIn pre-selects the first option, so \"Just researching\" leads.",
    "**No free-text and no phone field.** Each one cuts form fills.",
    "**Hidden fields** carry campaign, source and offer into Salesforce.",
    "**Privacy link and consent box,** because the UK and EU are in scope.",
], size=11, color=INK, after=7)
anim(s, phone, *fobjs, sub, *fl, rules_, effect="fade", step=80)
notes(s, "Sources: LinkedIn Help on Lead Gen Form fields (a425337) and the CRM integration with Salesforce Sales Cloud (a425316). "
         "Four fields prefill. Work email prefills only when the profile holds a work address. Salesforce drops the LinkedIn profile URL field.")

# ================================================================== 10. launch checklist
s = content(prs, "Tick Every Box Before the First Dollar Goes Out")
text(s, X0, Y0 - 0.05, 4.5, 0.32, "Once, for the account", size=13, color=TNAVY, font=HEAD, bold=True)
text(s, 5.15, Y0 - 0.05, 4.5, 0.32, "Every campaign", size=13, color=TNAVY, font=HEAD, bold=True)
once = ["Pick one ad account [confirm]", "Fix the six problems on slide 5", "CookieYes blocks the tag until consent",
        "Lead Gen Forms sync to Salesforce", "Connect CRM conversions to Salesforce", "Booking link on every form",
        "Upload exclusion lists", "Sales calls hot leads within 1 hour"]
every = ["Objective is Lead generation", "$1,000 cap and an end date", "Forecast 50,000 to 150,000",
         "Expansion and Network off", "Validate work email ticked", "Neutral answer first on both questions",
         "Privacy link, consent box, hidden fields", "3 finished ads, copy checked"]
o1 = checkbox_rows(s, X0, Y0 + 0.35, 4.45, once, size=11.5, row=0.47)
o2 = checkbox_rows(s, 5.15, Y0 + 0.35, 4.45, every, size=11.5, row=0.47)
anim(s, *o1, *o2, effect="fly_left", step=60)

# ================================================================== 11. campaigns at a glance
s = content(prs, "Four Campaigns, $1,000 Each, Judged on Demos Held")
SLIDE_GLANCE = s
GLANCE = [("agentz", "X and Reddit", "Free-tier signups", "Sign Up", "Cost per signup"),
          ("ai-security", "LinkedIn", "Demo requests", "Request Demo", "1+ demo held"),
          ("agent-security", "LinkedIn", "Demo requests", "Request Demo", "1+ demo held"),
          ("ctem", "LinkedIn", "Demo plus free scan", "Request Demo", "1+ demo held")]
objs = []
for i, (cid, ch, goal, cta, win) in enumerate(GLANCE):
    x = X0 + i * 2.32
    bx = shape(s, "round", x, Y0, 2.2, 2.75, fill=WHITE, line="C4CCDE", radius=0.06)
    shape(s, "rect", x, Y0, 2.2, 0.08, fill=[PURPLE, TNAVY, BLUE, RED][i])
    text(s, x + 0.15, Y0 + 0.18, 1.9, 0.4, CAMPS[cid]["name"], size=15, color=INK, font=HEAD, bold=True)
    p_ = shape(s, "round", x + 0.15, Y0 + 0.65, 1.4, 0.3, fill=SOFT, radius=0.5)
    label(p_, ch, size=9.5, color=BLUE, bold=True)
    text(s, x + 0.15, Y0 + 1.05, 1.95, 1.3, [f"**Goal** {goal}", f"**Button** {cta}", f"**Win** {win}"], size=11.5, color=INK, after=6)
    lk = text(s, x + 0.15, Y0 + 2.35, 1.9, 0.3, "Open the plan", size=10.5, color=BLUE, bold=True)
    TOC.append((lk, cid))
    objs.append(bx)
box = shape(s, "round", X0, 3.9, XW, 1.2, fill=OFF, line="D5DBEE", radius=0.06)
label(box, ["**Expected:** about 9 leads and 3 to 6 demos from the three LinkedIn campaigns, plus one AgentZ signup test.",
            "**Every ad follows four rules:** never name a competitor, open on the buyer's world, keep the post under 150 "
            "characters, and give one button that matches the form."], size=11.5, color=INK, align="l", pad=0.2)
anim(s, *objs, box, effect="fly_up", step=150)
notes(s, "Each campaign gets the same two slides: a plan slide and an ads slide. Copy both for a new campaign. AgentZ is the one "
         "exception to the demo goal, because it sells a self-serve free tier to developers.")

# ================================================================== campaign template
PLAN = {
    "agentz": dict(
        title="AgentZ Buys Free-Tier Signups on X and Reddit",
        cols=[("Who we target", ["**I2 on Reddit.** Zero Trust and security-first engineers in r/cybersecurity, r/netsec, r/devsecops",
                                 "**I1 on X.** Developers who search for AI agents and MCP servers",
                                 "**I3 and I4 wait for month 2.** Four groups on $1,000 is too thin to learn from"]),
              ("What we offer", ["**Offer** Free tier at agentzharness.ai, no card",
                                 "**Button** Sign Up",
                                 "**AgentZ** is the AccuKnox agentic AI harness, sold self-serve",
                                 "**Measure** cost per signup [set the target]"]),
              ("Fix before launch", ["Add the X and Reddit pixels and a signup event", "Add tracking to every link",
                                     "Fix Ad 3 labels and its open-source claim", "Use \"A leaked prompt leaks nothing.\" on Ad 2",
                                     "Remove third-party model logos, or get legal OK"])]),
    "ai-security": dict(
        title="AI Security Asks Security Leaders for a 30-Minute Session",
        cols=[("Who we target", ["**Titles** CISO, Head of Security, Security Architect, Head of AI Platform, AI Governance Lead",
                                 "**Companies** 1,000+ staff in finance, insurance, healthcare, telecom, software",
                                 "**Regions** US, Canada, UK, Western Europe"]),
              ("What we offer", ["**Offer** A 30-minute session that maps your models, agents and prompts to Zero Trust controls",
                                 "**Form** Where is your AI stack exposed?",
                                 "**Fallback** A free AI red-team test of one model endpoint [confirm delivery]"]),
              ("How we judge it", ["**3+ leads** and **1+ demo held** by week 4", "**Cost per lead** under $400",
                                   "**Click rate** 0.6% or higher", "**Runs first**, because AI Security is the widest story"])]),
    "agent-security": dict(
        title="Agent Security Targets Teams With Agents in Production",
        cols=[("Who we target", ["**Titles** CISO, Head of AppSec, Head of Platform Engineering, Head of AI, CTO",
                                 "**Companies** 500+ staff in software, finance, IT services, telecom",
                                 "**Retarget** readers of the AI kill-switch blog, about 6,000 a month"]),
              ("What we offer", ["**Offer** A 30-minute agent review: every agent, its tools and its data [confirm controls with product]",
                                 "**Form** Can you list every AI agent and what it can reach?",
                                 "**Fallback** A free agent permission audit of one environment [confirm delivery]"]),
              ("How we judge it", ["**3+ leads** and **1+ demo held** by week 4", "**Cost per lead** under $400",
                                   "**Click rate** 0.6% or higher", "**Runs after AI Security**, because both target CISOs"])]),
    "ctem": dict(
        title="CTEM Offers a Free Attack-Surface Scan With the Demo",
        cols=[("Who we target", ["**Titles** Head of Vulnerability Management, Security Engineering Director, SecOps Manager, Head of Cloud Security",
                                 "**Companies** 500+ staff in finance, healthcare, retail, manufacturing, software",
                                 "**No CISOs** while AI Security runs, so we never bid against ourselves"]),
              ("What we offer", ["**Offer** A demo plus a free attack-surface scan of the lead's domain [confirm sales can deliver]",
                                 "**Form** Want a free scan of your attack surface?",
                                 "**Fallback** A 30-minute review of their last pentest report"]),
              ("How we judge it", ["**3+ leads** and **1+ demo held** by week 4", "**Cost per lead** under $400",
                                   "**Click rate** 0.6% or higher", "**CTEM** means continuous threat exposure management"])]),
}
ADS = {
    "agentz": dict(title="AgentZ Bets on One Ad per Platform", show=["agentz-2", "agentz-1"],
                   pick="**Our bet:** I2 on Reddit, because no framework can copy the no-credential proxy. I1 on X is the volume bet."),
    "ai-security": dict(title="AI Security Bets on the Prompt Firewall Proof", show=["ai-sec-c", "ai-sec-a", "ai-sec-b"],
                        pick="**Our bet:** C, because it shows the product and a #1 analyst ranking [get OK to cite the report]."),
    "agent-security": dict(title="Agent Security Bets on the Audit Questions", show=["agent-sec-c", "agent-sec-a", "agent-sec-b"],
                           pick="**Our bet:** C, because auditors ask exactly these questions and the screenshot answers two."),
    "ctem": dict(title="CTEM Bets on the Free Scan", show=["ctem-c", "ctem-a", "ctem-b"],
                 pick="**Our bet:** C, because it names the free scan. A runs once product confirms daily testing [confirm]."),
}
ADLOOK = {a["id"]: a for c in DATA["campaigns"] for a in c["ads"]}
CAMP_SLIDE = {}

for cid in ("agentz", "ai-security", "agent-security", "ctem"):
    c, P, A = CAMPS[cid], PLAN[cid], ADS[cid]
    # plan slide
    s = content(prs, P["title"])
    CAMP_SLIDE[cid] = s
    tag = (f"{c['name'].upper()}  |  LINKEDIN  |  $1,000  |  4 WEEKS" if cid != "agentz"
           else "AGENTZ  |  X AND REDDIT  |  $1,000  |  14-DAY TEST")
    pill_ = shape(s, "round", X0, Y0 - 0.02, 4.2, 0.34, fill=SOFT, radius=0.5)
    label(pill_, tag, size=10, color=BLUE, bold=True)
    objs = []
    for i, (hd, items) in enumerate(P["cols"]):
        x = X0 + i * 3.08
        bx = shape(s, "round", x, Y0 + 0.5, 2.96, 3.65, fill=WHITE, line="C4CCDE", radius=0.05)
        hb = shape(s, "rect", x, Y0 + 0.5, 2.96, 0.48, fill=[TNAVY, BLUE, PURPLE][i])
        label(hb, hd, size=13, bold=True, font=HEAD)
        text(s, x + 0.16, Y0 + 1.1, 2.66, 2.95, items, size=11.5, color=INK, after=8)
        objs += [bx, hb]
    anim(s, pill_, *objs, effect="fly_up", step=150)
    notes(s, "Why this campaign: " + c["why"])
    # ads slide
    s = content(prs, A["title"])
    show = [ADLOOK[a] for a in A["show"]]
    pk = shape(s, "round", X0, Y0 - 0.06, XW, 0.4, fill=SOFT, line=BLUE, radius=0.3)
    label(pk, A["pick"], size=10.5, color=INK, align="l", pad=0.15)
    if cid == "agentz":
        w, h, gap = 4.45, 4.45 * 628 / 1200, 0.3
    else:
        w = h = 2.72
        gap = (XW - 3 * w) / 2
    top = Y0 + 0.44
    objs = [pk]
    for i, ad in enumerate(show):
        x = X0 + i * (w + gap)
        img = HERE / ad["image_only"] if "image_only" in ad else MOCK / f"{ad['id']}.png"
        pic = picture(s, img, x, top, w=w, h=h)
        pic.line.color.rgb = rgb("C4CCDE")
        objs.append(pic)
        if i == 0:
            bet = shape(s, "round", x + w - 1.05, top + 0.08, 0.97, 0.3, fill=RED, radius=0.5)
            label(bet, "OUR BET", size=10, bold=True, font=HEAD, pad=0.02)
            objs.append(bet)
        cap = text(s, x, top + h + 0.04, w, 5.5 - (top + h + 0.04),
                   [f"**{ad['label'].split(',')[0].split('.')[0]}.  {ad['li_headline']}**", ad["intro"]],
                   size=10.5 if cid != "agentz" else 11.5, color=INK, after=3)
        objs.append(cap)
    anim(s, *objs, effect="fade", step=150)
    notes(s, "Mockups are low fidelity. The designer replaces them before launch. Photos come from Pexels under the Pexels License. "
             "Request Demo is the button on every LinkedIn ad, because the goal is a meeting.")

# ================================================================== 20. closing
closing(prs, "APPROVE FOUR $1,000 TESTS", "Fix the six setup problems first. Report demos held every Monday.")

# ================================================================== contents rows with links
SL = list(prs.slides)
num = {id(sl): i + 1 for i, sl in enumerate(SL)}
p1 = [("$1,000 buys 3 to 7 leads at best", SLIDE_BUYS), ("Read every number as a range", SL[3]),
      ("Six setup problems to fix", SL[4]), ("Account, tracking and conversions", SL[5]),
      ("How we run every campaign", SL[6]), ("Eight settings that decide results", SL[7]),
      ("The lead form and Salesforce", SL[8]), ("Launch checklist", SL[9])]
p2 = [("Four campaigns at a glance", SLIDE_GLANCE), ("AgentZ on X and Reddit", CAMP_SLIDE["agentz"]),
      ("AI Security on LinkedIn", CAMP_SLIDE["ai-security"]), ("Agent Security on LinkedIn", CAMP_SLIDE["agent-security"]),
      ("CTEM on LinkedIn", CAMP_SLIDE["ctem"])]
objs = []
for col, (hd, items) in enumerate((("Part 1  |  The playbook", p1), ("Part 2  |  The campaigns", p2))):
    x = X0 + col * 4.7
    text(s_toc, x, Y0 - 0.05, 4.5, 0.35, hd, size=14, color=TNAVY, font=HEAD, bold=True)
    for i, (t, target) in enumerate(items):
        y = Y0 + 0.38 + i * 0.47
        nb = shape(s_toc, "rect", x, y, 0.55, 0.4, fill=TNAVY if col == 0 else BLUE)
        label(nb, str(num[id(target)]), size=12, bold=True, font=HEAD)
        rb = shape(s_toc, "rect", x + 0.58, y, 3.9, 0.4, fill=LIGHT if i % 2 == 0 else OFF)
        label(rb, t, size=12, color=INK, align="l", pad=0.14)
        link(nb, target)
        link(rb, target)
        objs += [nb, rb]
hint = text(s_toc, X0 + 4.7, Y0 + 0.38 + 5 * 0.47 + 0.15, 4.5, 0.6,
            "Click any row to jump to that slide. Each campaign has a plan slide and an ads slide on the same template.",
            size=10.5, color=MID)
anim(s_toc, *objs, hint, effect="fly_left", step=60)
for lk, cid in TOC:
    link(lk, CAMP_SLIDE[cid])

finalize(prs)
OUT.mkdir(exist_ok=True)
target = OUT / "paid-ads-playbook-q4-2026.pptx"
prs.save(target)
print("wrote", target, "slides:", len(prs.slides))
