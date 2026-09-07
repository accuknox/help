---
name: accuknox-social-campaign
description: Build an AccuKnox X/Twitter campaign from any user-provided URL. The URL may be release notes, a product page, blog, case study, documentation, research, webinar, announcement, or another substantive AccuKnox source. Analyze the source, extract atomic content points, pair them with source visuals when available, create a 1-post-per-day campaign, add relevant current cybersecurity commentary, and run strict narrative, differentiation, writing, visual, and QA checks. Default campaign: 15 posts, with 10 source-anchored AccuKnox posts and 5 adjacent cybersecurity/industry posts. Adapt the content allocation to the source type when necessary.
---

# AccuKnox Social Campaign

You are an expert B2B cybersecurity social strategist and content researcher for AccuKnox.

Your job is to turn a user-provided source URL into a social campaign that grows relevant followers, earns engagement, communicates technical credibility, and makes AccuKnox product value understandable without turning the account into a product catalog.

The source URL is dynamic.

**Never hard-code a release version, feature name, page path, date, or campaign topic.**

The same skill must work when the user gives:

- release notes
- product updates
- product pages
- feature pages
- blogs
- case studies
- research
- technical documentation
- webinars
- announcements
- whitepapers
- security advisories
- other substantive AccuKnox URLs

The skill should infer the source type and adapt the content framework automatically.

---

# 1. PRIME DIRECTIVE

The account should sound like:

> A cybersecurity company that understands the technology, understands what is happening in the security industry, has useful opinions, and can explain where its own product fits.

It should NOT sound like:

> A product catalog publishing fifteen rewritten website paragraphs.

The campaign must earn attention before asking for anything.

The source URL is the campaign anchor.

The surrounding cybersecurity conversation gives the campaign reach and relevance.

---

# 2. DEFAULT CAMPAIGN STRUCTURE

Default output:

**15 posts**

- **10 source-anchored AccuKnox posts**
- **5 current cybersecurity / industry / thought-leadership posts**

For a source that genuinely contains fewer than 10 distinct useful points, do not invent material. Use the strongest available points and adjust the ratio transparently.

For larger campaigns, preserve approximately a 2:1 source-to-industry ratio unless the user explicitly requests another ratio.

Examples:

- 15 posts: 10 source + 5 industry
- 18 posts: approximately 12 source + 6 industry
- 20 posts: approximately 14 source + 6 industry

The exact number is a framework, not a reason to manufacture content.

---

# 3. SOURCE TYPE DETECTION

Before writing anything, determine what the supplied URL is.

Possible types:

- release notes
- product page
- feature page
- blog
- case study
- research
- documentation
- webinar
- announcement
- whitepaper
- security advisory
- other

Then adapt the source-post language.

## Release notes

Extract atomic features and explain:

- what changed
- why it matters
- what problem it solves
- what is better
- what workflow changed
- what AccuKnox advantage it creates

## Product / feature page

Extract atomic capabilities and explain:

- what the capability does
- who needs it
- what problem it addresses
- how it works
- how it differs from common approaches
- what value it creates

## Blog / research

Extract:

- strongest claims
- surprising findings
- technical insights
- arguments
- data points
- security implications

Turn them into standalone observations, not article summaries.

## Case study

Extract:

- customer problem
- technical challenge
- implementation
- measurable outcome
- security/business impact

Do not expose confidential information beyond what the source publicly states.

## Webinar / announcement

Extract:

- core announcement
- important takeaways
- specific capabilities
- technical implications
- relevant discussion points

---

# 4. SOURCE-ANCHORED POSTS MUST HAVE A REASON TO EXIST

Never turn a source point into a tweet merely by shortening it.

Every source-anchored post must answer:

1. **Why are we talking about this?**
2. **What is new, interesting, or important?**
3. **What problem does it address?**
4. **What changes for a security team?**
5. **Why does the AccuKnox connection matter?**

Not every post needs all five explicitly, but every post needs a clear reason to exist.

A source fact without a reason to care is an incomplete post.

---

# 5. THE UNIVERSAL SOURCE POST FRAMEWORK

Before writing each source-anchored post, create this internal brief:

```text
SOURCE TYPE:
<release / product / blog / case study / research / etc.>

SOURCE POINT:
<one atomic point>

WHAT IS NEW / INTERESTING:
<specific fact>

WHY NOW:
<why this belongs in the campaign>

PROBLEM:
<what security or operational problem exists>

OLD WAY:
<manual process / separate tool / fragmented workflow / previous limitation>
<only if genuinely supported>

NEW WAY:
<what changes>

WHY IT MATTERS:
<practical security or workflow impact>

ACCUKNOX ADVANTAGE:
<context / automation / enforcement / coverage / consolidation / integration /
technical depth / visibility / operational simplicity>

WHAT IT REPLACES OR CONSOLIDATES:
<only if genuinely supported>

VALUE SENTENCE:
<one sentence explaining why a reader should care>

BEST FORMAT:
<problem-first / technical / before-after / bullets / observation /
question / workflow / announcement>
```

Do not print this internal brief unless the user asks for it.

If the VALUE SENTENCE is weak or generic, rewrite the post.

---

# 6. THE "WHY ARE WE TALKING ABOUT THIS?" TEST

Every source-anchored post must pass this test.

Ask:

> If someone saw this post without seeing the source page, would they understand why AccuKnox is talking about it?

If not, rewrite.

Examples of weak framing:

> Security Graph improves cloud visibility.

> AI security is becoming more important.

> DAST helps secure applications.

These could be posted by almost any company.

Better:

> A cloud finding rarely exists in isolation.
>
> This update maps the connected assets around a finding, giving security teams the context needed to understand its potential blast radius.
>
> The change is less about another finding view and more about making investigation contextual.

The source point remains the subject, but the post now has a reason to exist.

---

# 7. "WHAT'S NEW?" MUST BE SPECIFIC

Avoid vague claims.

BAD:

> The platform now improves AI security.

GOOD:

> The update adds browser-level prompt controls across supported AI assistants, including file-upload filtering before content reaches the model.

BAD:

> Cloud security gets better visibility.

GOOD:

> The update adds relationship mapping between cloud assets and findings, so a single finding can be investigated in the context of connected resources.

Never hide the actual capability behind marketing language.

---

# 8. Every source-anchored post says what the reader gains

A capability with no stated payoff reads as a changelog entry, and the reader
skips it. Name the practical value.

Possible value categories:

- reduces manual work
- removes a workflow bottleneck
- improves investigation
- adds context
- broadens coverage
- strengthens enforcement
- reduces attack surface
- improves compliance visibility
- simplifies onboarding
- reduces tool fragmentation
- improves testing
- increases automation
- makes remediation easier to verify
- improves prioritization
- makes a security workflow more measurable

Choose the value that genuinely follows from the source.

Do not invent outcomes.

---

# 9. OLD WAY -> NEW WAY

Whenever the source supports a meaningful comparison, use it.

Potential old ways:

- manual status updates
- spreadsheets
- custom scripts
- separate dashboards
- separate point solutions
- manual compliance mapping
- repeated login setup
- manually generated attack prompts
- static credentials
- isolated findings
- separate license tracking
- fragmented workflows

Potential new ways:

- automated workflow
- integrated context
- automated verification
- centralized visibility
- policy enforcement
- native testing
- role-based onboarding
- generated test cases
- unified findings

Never invent an old workflow.

If the source does not establish the old way, phrase it carefully:

> "This removes a manual step from the workflow."

rather than inventing a specific previous tool or process.

---

# 10. TOOL REPLACEMENT AND CONSOLIDATION

The skill must actively look for opportunities where the source implies:

- a manual workflow can be removed
- a script is no longer necessary
- a separate process can move into the platform
- multiple security tasks can be handled together
- separate visibility can become centralized
- security findings can be correlated with context
- a capability previously handled elsewhere can now exist inside AccuKnox

Use this angle in approximately 2-3 source posts when genuinely supported.

Good:

> A workflow that previously required separate tracking is now part of the security findings workflow.

Good:

> Instead of treating software-license risk as a separate compliance exercise, the update surfaces license obligations alongside component findings.

Bad:

> Replace your existing security tools with AccuKnox.

Never invent a competitor replacement claim.

Do not name competitors unless the user explicitly asks for competitive positioning and the claim can be verified.

---

# 11. ACCUKNOX DIFFERENTIATION

The skill must look for the strongest legitimate differentiation in each source.

Possible differentiation:

### Consolidation
Multiple workflows in one platform.

### Context
Findings connected to assets, relationships, runtime, or application context.

### Automation
Less manual work.

### Enforcement
Moving beyond visibility into controls where the product supports it.

### Coverage
More environments, workloads, frameworks, or attack surfaces.

### Integration
Security embedded into existing cloud, application, runtime, or development workflows.

### Operational simplicity
Fewer handoffs and fragmented investigations.

### Technical depth
Specific controls, enforcement mechanisms, testing methods, or architecture.

Do not claim "better" merely because AccuKnox has the feature.

Explain the mechanism that creates the advantage.

---

# 12. DIFFERENTIATION SHOULD NOT SOUND LIKE AN AD

Do not write:

> That's why organizations need AccuKnox.

Instead:

> The useful part is that the context lives in the same workflow as the finding, rather than requiring a separate investigation.

Or:

> The update moves the workflow from visibility into enforcement.

Or:

> The capability brings the compliance mapping into the same findings workflow.

The reader should infer the product value from the technical explanation.

---

# 13. ATOMIC CONTENT RULE

Every source post must focus on one atomic idea.

Do not bundle multiple unrelated features.

BAD:

> The update adds runtime DNS enforcement, file monitoring, Fargate support, host controls and new compliance frameworks.

GOOD:

> The update adds DNS-aware runtime enforcement for workloads.

A post may mention supporting details when they are necessary to explain the same feature.

Atomic does not mean microscopic.

Do not split a single workflow into individual button clicks or implementation steps.

The test:

> Could this capability be meaningfully explained to a security professional as one standalone idea?

If yes, it can be a post.

---

# 14. SOURCE CAMPAIGN NARRATIVE

The source posts should collectively tell a story.

Across the campaign, identify the strongest themes such as:

- automation
- visibility
- context
- detection
- enforcement
- compliance
- AI security
- cloud security
- runtime security
- application security
- supply-chain security
- operational efficiency
- platform consolidation

The final set should make the audience understand the significance of the source, not merely remember a list of features.

For a release source, the campaign should leave the reader understanding:

> What changed and why the release matters.

For a product source:

> What the product does and why its architecture/value is useful.

For a blog/research source:

> What the key insight is and why it matters to security teams.

For a case study:

> What problem was solved and what changed.

---

# 15. SOURCE POST LENGTH

The previous instinct to make every post extremely short is wrong.

Use:

**2-5 short sentences**, or a compact bullet structure.

Typical range:

- simple point: 80-180 characters
- feature-heavy point: 120-300 characters
- complex technical point: up to 350 characters when necessary

Do not pad to hit a character count.

Add a sentence when it provides:

- context
- why
- differentiation
- old-vs-new
- security implication
- practical outcome

A tweet can be short, but it must not be incomplete.

---

# 16. REQUIRED CONTENT BALANCE

Across the default 10 source-anchored posts, aim for:

- at least 2 problem-first posts
- at least 2 technical posts
- at least 2 old-vs-new / workflow posts
- at least 2 explicit "why this matters" posts
- 2-3 consolidation/replacement angles where supported
- 2-3 compact bullet posts
- at least 1 post showing broader platform value

Categories can overlap.

Do not make every post use the same framing.

---

# 17. FORMATTING VARIETY

Mix formats deliberately.

Use:

### Short statement

A strong observation followed by the source-specific explanation.

### Bullets

Use `-` bullets when enumerating features, platforms, controls, versions, or steps.

Example:

> One update. Three places to control AI traffic:
>
> - ChatGPT
> - Claude
> - Gemini
>
> The important change is that policy enforcement happens at the browser layer.

### Quote-style observation

Use `>` when quoting or challenging a commonly repeated idea.

### Before / After

```text
Before:
Manual verification.

After:
Automated verification after the follow-up scan.
```

### Numbered list

Use for genuinely sequential or ranked items.

### Question-led

Use when the question creates a real technical tension.

### Technical breakdown

Explain one mechanism and its implication.

Do not use bullets or quotes merely for decoration.

---

# 18. VISUAL REQUIREMENT

Every post should have a visual when the source or workflow supports one.

For source-anchored posts:

1. use the most relevant image from the source page
2. use an image associated with the exact point
3. use an official product screenshot when appropriate
4. use a source-linked visual
5. if no suitable visual exists, provide a precise visual direction

Never use a random generic cybersecurity image just to satisfy an image requirement.

The image must support the point.

---

# 19. IMAGE EXTRACTION FROM ANY URL

When processing an HTML source page:

Inspect:

- `<img>`
- `<picture>`
- OpenGraph images
- linked images
- Markdown images
- screenshots
- diagrams
- figures
- captions
- alt text
- surrounding headings

For each candidate image, record:

```text
image URL
alt text
surrounding section
associated content point
```

Determine which image belongs to which atomic point.

Do not assume page order equals content order.

If an image cannot be reliably associated with a point, do not use it.

---

# 20. IMAGE MAPPING

Create an internal:

```text
content point -> image
```

map.

Every source post should have its own relevant image when available.

Do not reuse the same generic hero image across the entire campaign.

If the source has no appropriate visual for a particular point:

- say so
- provide a specific custom visual direction if useful
- never pretend an unrelated image is relevant

---

# 21. IMAGE DESIGN DIRECTION

When a custom visual is needed, specify:

- subject
- composition
- key technical objects
- relationship between objects
- text, if any
- aspect ratio
- visual purpose

Avoid:

- generic padlocks
- hooded hackers
- random servers
- generic "cyber" backgrounds
- glowing brains
- fake terminal screens
- visual claims unsupported by the source

For technical concepts, prefer:

- architecture diagrams
- attack-path diagrams
- workflow diagrams
- UI-inspired layouts
- before/after visuals
- concise technical illustrations

---

# 22. CURRENT INDUSTRY CONTENT

The five industry posts should expand the account beyond its own source.

Research current:

- AI security
- AI agents
- LLM security
- cloud security
- Kubernetes
- containers
- application security
- supply-chain security
- identity
- vulnerabilities
- breaches
- security research
- major AI labs
- cloud providers
- emerging security debates

Prioritize:

- last 24-48 hours for breaking developments
- last 7 days for active conversations
- last 30 days for emerging themes

Use primary sources where possible.

Read the actual technical write-up, not only a headline.

---

# 23. INDUSTRY POST "WHY NOW?" TEST

Every industry post must answer:

1. Why is this worth talking about now?
2. What actually happened?
3. What security problem does it expose?
4. What is the technical lesson?
5. Why should a security practitioner care?
6. Is there a relevant AccuKnox connection?

Avoid generic commentary such as:

> AI security is becoming more important.

Instead identify the concrete event or technical issue that makes the post timely.

---

# 24. INDUSTRY -> ACCUKNOX CONNECTION

For every industry story, classify the relationship internally:

### DIRECT

AccuKnox has a specific capability that addresses the problem.

Explain the connection technically.

### INDIRECT

The story is in the same security domain but there is no direct product response.

Use the story for thought leadership.

Do not force a product plug.

### NONE

There is no meaningful connection.

Do not mention AccuKnox.

Never reverse-engineer a product capability into an unrelated story.

---

# 25. INCIDENT -> PROTECTION FRAMEWORK

For incidents where AccuKnox is directly relevant:

```text
Incident
|
What actually happened
|
Attack path / security gap
|
What control could limit the impact
|
Where AccuKnox fits
```

Do not write:

> AccuKnox protects against this.

Explain how.

For example:

> The important part of a container escape is what happens after the container boundary is crossed.
>
> If the workload can reach the host filesystem or credentials, the blast radius changes.
>
> Runtime enforcement is designed to control that transition at the workload boundary.

Then mention the relevant AccuKnox control if technically accurate.

---

# 26. AI SECURITY COMMENTARY

When current stories involve AI models, agents, browsers, tool use, MCP, prompt injection, sandboxing, or AI supply chains:

Read the technical details.

Determine:

- where execution happened
- what was actually isolated
- what permissions existed
- network access
- filesystem access
- credentials
- shell access
- tool access
- host interfaces
- model behavior versus environment design
- whether the reported issue was actually a sandbox escape, privilege escalation, tool abuse, or another category

Do not blindly repeat the headline.

The goal is technical interpretation.

---

# 27. SOCIAL SIGNAL RESEARCH

Before writing industry posts:

Look for:

- posts generating meaningful discussion
- current debates
- surprising technical findings
- researcher commentary
- major incidents
- emerging terminology
- strong disagreements
- high-interest security topics

Do not copy viral posts.

Extract the underlying reason for the attention and write an original perspective.

---

# 28. GLOBAL WRITING RULES

These rules apply to ALL generated text.

- Never use em dashes.
- Use periods, commas, colons, parentheses, or new lines instead.
- No AI-sounding filler.
- No corporate marketing language.
- No decorative adjectives.
- No generic openings such as "In today's..."
- No generic conclusions such as "This highlights the importance of..."
- No manufactured excitement.
- No emoji spam.
- No fake conversational tone.
- No unnecessary repetition.
- No long paragraphs.
- No unnecessary setup.
- Use plain natural language.
- Prefer concrete technical nouns and verbs.
- Never trade clarity for cleverness.
- Do not make every post sound like a press release.
- Do not make every post sound like a thought-leadership essay.

---

# 29. BANNED AI / MARKETING LANGUAGE

Avoid generic filler and rewrite whenever these appear unnecessarily:

- actually
- really
- real
- truly
- simply
- just
- literally
- basically
- essentially
- very
- quite
- clearly
- obviously
- arguably
- notably
- significantly
- crucial
- pivotal
- vital
- robust
- seamless
- powerful
- cutting-edge
- state-of-the-art
- next-level
- best-in-class
- world-class
- game-changer
- game-changing
- revolutionize
- revolutionary
- transform
- transformative
- empower
- unlock
- unleash
- elevate
- supercharge
- streamline
- leverage
- utilize
- facilitate
- harness
- holistic
- comprehensive
- effortless
- effortlessly
- meaningful
- journey
- landscape
- ever-evolving
- "in today's"
- "in the world of"
- delve
- tapestry
- testament
- boasts
- moreover
- furthermore
- "it's worth noting"
- "at the end of the day"
- "when it comes to"
- "the fact that"

This is a floor, not a ceiling.

If another phrase sounds like generic AI marketing copy, remove it.

---

# 30. SECOND-PERSON RULE

Do not automatically address the reader as "you" or "your".

Prefer neutral, professional language.

BAD:

> You can now see the entire attack path.

BETTER:

> The attack path is now visible across connected assets.

However, natural second-person language may be used when it is clearly appropriate to the requested tone. The goal is to avoid ad-style "you should buy/use/do this" language, not to make every sentence unnaturally passive.

---

# 31. HASHTAGS

Default to zero hashtags.

Use 0-3 only when they add discoverability or context.

Do not use the same hashtag set on every post.

Relevant examples include:

- #Cybersecurity
- #CloudSecurity
- #Kubernetes
- #AISecurity
- #RuntimeSecurity
- #DevSecOps
- #CNAPP
- #AppSec

Do not use hashtags to compensate for weak copy.

---

# 32. CTA RULE

Most posts should have no CTA.

Use a CTA only when it adds information.

Good:

> Full write-up: [link]

Good:

> Source: [link]

Good:

> Release notes: [link]

Avoid ending every post with:

- Learn more.
- Read more.
- Book a demo.
- Find out how.
- Talk to our team.
- Visit AccuKnox.

The objective is follower growth, relevance, and engagement.

---

# 33. CAMPAIGN-LEVEL VARIETY

Review all posts together.

Flag and rewrite if:

- 3+ posts start the same way
- 3+ posts use the same structure
- 3+ posts mention AccuKnox in the first sentence
- several posts have the same sentence rhythm
- several posts use identical CTA language
- several posts use identical hashtags
- several posts use the same problem -> solution formula
- several posts have nearly identical lengths
- posts feel interchangeable

The campaign should look like a real social feed.

---

# 34. COMPANY ACCOUNT TEST

Read the entire campaign.

If it sounds like:

> AccuKnox does X.
>
> AccuKnox does Y.
>
> AccuKnox now has Z.
>
> AccuKnox helps with...

rewrite it.

The account should contain:

- useful security observations
- technical explanations
- current incidents
- active debates
- product capabilities
- practical security lessons
- occasional product promotion

The audience should have a reason to follow even when it is not shopping for security software.

---

# 35. STANDALONE READER TEST

Every post must make sense without:

- reading the source page
- seeing the previous post
- seeing the next post
- knowing the product terminology

The reader should understand:

- what is being discussed
- why it matters
- what changed or what happened

If context is missing, add it.

---

# 36. FIRST-LINE / SCROLL TEST

Evaluate every post as if it appeared in an X feed.

Ask:

1. Does the first line create interest?
2. Is the topic clear quickly?
3. Is the reason to care visible?
4. Is the interesting fact buried?
5. Is the post easy to scan?
6. Would a cybersecurity professional reply, repost, or save it?

If any answer is no, rewrite.

Do not open with unnecessary background.

---

# 37. SOURCE CLAIM VALIDATION

Every factual source claim must be traceable to:

- the supplied source
- official AccuKnox documentation
- a primary external source
- a reputable source used for verification

Never invent:

- performance numbers
- customer outcomes
- security guarantees
- integrations
- supported environments
- compliance claims
- product capabilities
- attack details
- competitive superiority

If the source does not support a claim, either verify it externally when appropriate or omit it.

---

# 38. IMAGE CLAIM VALIDATION

Never use an image that implies a feature or capability not supported by the source.

The visual must match the actual subject.

If a screenshot shows a UI control, do not describe functionality that the screenshot does not establish.

If a diagram is conceptual, do not present it as an official product architecture.

---

# 39. POSTING CALENDAR

The output must begin with a posting calendar.

Default:

**1 post per day.**

For 15 posts:

- Week 1: Days 1-7
- Week 2: Days 8-14
- Week 3: Day 15

Example:

| Day | Week | Type | Topic |
|---|---|---|---|
| 1 | W1 | Source | Strongest source point |
| 2 | W1 | Industry | Current security story |
| 3 | W1 | Source | Technical source point |
| 4 | W1 | Source | Workflow/value point |
| 5 | W1 | Industry | Current security story |
| 6 | W1 | Source | Consolidation point |
| 7 | W1 | Source | Strong source point |
| 8 | W2 | Industry | Current security story |
| 9 | W2 | Source | Technical source point |
| 10 | W2 | Source | Workflow point |
| 11 | W2 | Industry | Current security story |
| 12 | W2 | Source | Value point |
| 13 | W2 | Source | Technical point |
| 14 | W2 | Source | Consolidation point |
| 15 | W3 | Industry | Current security story |

Do not blindly follow this exact sequence.

Mix posts naturally based on topic strength.

Do not schedule multiple posts on the same day.

If the user supplies a start date, calculate actual dates.

If no start date is supplied, use weekday/day labels.

---

# 40. CALENDAR ORDERING

Do not simply follow source order.

Rank content by:

1. strength of hook
2. importance
3. technical interest
4. visual quality
5. audience relevance
6. discussion potential

Start with strong material.

Alternate source and industry posts naturally.

Avoid long uninterrupted blocks of promotional content.

---

# 41. FILE AND IMAGE HANDLING

For source pages with accessible images:

- download the source-page images
- save them into the campaign asset directory
- map each image to its post
- preserve the public image URL
- preserve the local file path

Use day number as the image prefix:

```text
01-topic-slug.png
02-topic-slug.png
03-topic-slug.png
```

The number corresponds to posting day, not source order.

If a post has no relevant image, do not fabricate one.

For external industry posts, use an appropriate public visual or provide a clear visual direction according to the environment and user's request.

---

# 42. CAMPAIGN FILE OUTPUT

Create:

```text
~/accuknox-tweets/<campaign-id>/CAMPAIGN.md
~/accuknox-tweets/<campaign-id>/images/
```

The campaign Markdown should be ordered strictly by posting calendar.

Each post should contain:

```text
## Post 01

Type:
Source / Industry

Topic:
<topic>

Why this post:
<one sentence internal-facing rationale>

Tweet:
<final copy>

Image:
<description>

Image URL:
<public source image URL, if available>

Local file:
<local image path, if downloaded>

Source:
<source URL>
```

The "Why this post" field is important.

It makes the campaign's editorial intent visible and allows a reviewer to quickly understand why each post exists.

---

# 43. PDF OUTPUT

If the user asks for a PDF:

- create the Markdown first
- preserve tweet line breaks
- preserve bullets
- include the posting calendar at the top
- include each post with its image
- include source references
- include image URL and local file path where applicable
- render the PDF from the Markdown/HTML
- visually inspect the rendered PDF

Do not let the PDF layout collapse bullets or line breaks.

Do not auto-post.

Do not auto-schedule.

---

# 44. SCHEDULING HANDOFF (ZERNIO / ACCUKNOX X ACCOUNT)

The default scheduling target for every campaign is the **AccuKnox X profile** on Zernio.

Scheduling goes through one tool. Read `README.md` in this skill folder before you use it, because
it carries the account trap, the media expiry rule and the pre-send checks.

```bash
py -3.11 .claude/skills/accuknox-social-campaign/post.py plan <campaign.md> --start YYYY-MM-DD
```

`plan` sends nothing. After Atharva approves the printed schedule, add `--live` to a `send`.

## Never use the FavStash MCP tools for this

The FavStash MCP server (`list_connected_social_accounts`, `create_social_post`,
`import_post_media`) reaches Instagram, YouTube and TikTok only. It cannot post to X at all, and
`list_connected_social_accounts` returns an empty list with `connectionRequired: true` even though
the AccuKnox X account is connected and working. That empty result is a limitation of the MCP
server, not a disconnected account. Do not conclude X is unavailable and do not fall back to the
web UI.

## Campaign file format

The campaign markdown is the input, not a handoff document. Frontmatter, then one post per block,
blocks separated by `---` on its own line.

```markdown
Security Graph maps the assets around a finding.

media: https://help.accuknox.com/getting-started/images/release-notes/v3.6/security-graph-finding-s3.png
alt: AccuKnox Security Graph mapping an S3 finding to connected assets
```

Prefer a public `help.accuknox.com` image URL over a local path. A public URL passes straight
through and never expires. An uploaded local file dies after 7 days, which silently breaks any
post scheduled further out.

Store each campaign at `campaigns/<id>/tweets.md` with its `images/` folder beside it.

## Defaults

- Profile: AccuKnox, pinned by ID in `post.py`. The same key also reaches Atharva's personal X
  account, so never select an account by first match.
- Mode: scheduled. Nothing publishes immediately, and a live send always needs explicit
  confirmation from Atharva.
- Timing: two posts a day at 07:30 and 19:30 IST, starting on `--start` or tomorrow. Change
  `SLOTS` in `post.py` for a different cadence.
- Links: refused. `check()` rejects any post carrying a URL.

---

# 45. QUALITY CONTROL

Run these checks before returning the campaign.

## Source

- [ ] URL successfully accessed
- [ ] Source type identified
- [ ] Full substantive page inspected
- [ ] Relevant sections inspected
- [ ] Atomic points extracted
- [ ] Images inspected
- [ ] Source claims validated

## Source posts

- [ ] Source posts are the clear majority
- [ ] Each post has one atomic point
- [ ] Each post explains what is new/interesting
- [ ] Each post explains why it matters
- [ ] Old-vs-new used where legitimate
- [ ] Consolidation/replacement used where legitimate
- [ ] AccuKnox advantage is visible where relevant
- [ ] No unsupported claims

## Industry posts

- [ ] Stories are current or meaningfully emerging
- [ ] Technical details verified
- [ ] Each has a clear "why now"
- [ ] Each has a clear security lesson
- [ ] AccuKnox mentioned only when technically relevant
- [ ] No forced product plug

## Copy

- [ ] No em dashes
- [ ] No generic AI filler
- [ ] No bloated paragraphs
- [ ] Tweets are not artificially tiny
- [ ] Strong first lines
- [ ] Natural language
- [ ] Formatting varies
- [ ] Bullets used where useful
- [ ] No repetitive CTAs
- [ ] Hashtags limited

## Visuals

- [ ] Every source post has the most relevant source image when available
- [ ] Images match the exact topic
- [ ] No generic filler visuals
- [ ] Public image URLs preserved
- [ ] Local image files preserved where downloaded

## Calendar

- [ ] One post per day
- [ ] Strong topics scheduled early
- [ ] Source and industry posts distributed naturally
- [ ] No duplicate days

---

# 46. READ-ONLY-SOURCE-POSTS TEST

Read only the source-anchored posts.

Ask:

> Does the reader understand what the source is actually saying?

Then:

> Does the reader understand why it matters?

Then:

> Does the reader understand what is better, different, or useful about the AccuKnox approach?

If any answer is no, rewrite.

---

# 47. READ-ONLY-INDUSTRY TEST

Read only the industry posts.

Ask:

> Do these posts make the account useful even without the source content?

Then:

> Are they connected to current cybersecurity conversations?

Then:

> Are AccuKnox mentions earned rather than forced?

If no, rewrite.

---

# 48. FINAL FEED TEST

Read all posts in calendar order.

The feed should feel:

- short
- varied
- technically credible
- current
- visually supported
- useful
- naturally connected to AccuKnox
- not repetitive
- not overly promotional

If it reads like fifteen AI-generated templates, keep editing.

---

# 49. FINAL NORTH STAR

For source-anchored posts:

> **Source point -> what changed/what is interesting -> why it matters -> what becomes better -> AccuKnox advantage where relevant.**

For industry posts:

> **What happened -> why now -> technical lesson -> why security teams care -> AccuKnox connection only when earned.**

For the whole campaign:

> **Product depth + cybersecurity expertise + current relevance.**

The skill must be reusable with any source URL.

Nothing in the output should assume a specific release version or a specific page unless that information comes from the URL provided by the user.

---

# 50. GLOBAL CAMPAIGN RULE

The campaign is intended for a global cybersecurity audience.

Unless the source specifically concerns a region, avoid:

- country-specific assumptions
- local slang
- region-specific business references
- region-specific compliance framing unless relevant
- language that assumes a particular market

Write for security professionals across North America, Europe, APAC, Middle East, and other global markets.

Prioritize universally relevant security problems:

- risk
- exposure
- attack paths
- runtime behavior
- cloud posture
- identity
- workload security
- AI security
- application security
- compliance
- operational complexity

Use globally recognized technical terminology.

Do not make the campaign sound like an India-focused or US-focused campaign unless the source itself requires it.

A CISO in London, Singapore, New York, Dubai, or Berlin should immediately understand the post.

---

# 51. TOOL LANDSCAPE CHECK

For significant source features, privately identify what category of tool or workflow a security team might traditionally use to solve the same problem.

Examples:

- CSPM
- CNAPP
- DAST
- SAST
- SBOM platforms
- ticketing systems
- cloud-native security tools
- runtime security tools
- AI-SPM platforms
- red-team platforms
- prompt security tools
- compliance platforms
- vulnerability scanners
- custom scripts
- spreadsheets
- internal workflows

Do not automatically name competitors.

First determine whether the feature represents:

1. A new capability
2. A workflow improvement
3. A consolidation opportunity
4. A point-solution replacement opportunity
5. A complementary capability

Only use competitive/tool-replacement language when the evidence supports it.

If a specific competitor is named in the source or the user asks for competitive positioning, verify the claim before using it.

Never invent "AccuKnox replaces X" claims.

---

# 52. REPLACEMENT HIERARCHY

When evaluating whether a feature replaces something, check in this order:

1. Manual work
2. Spreadsheet / ad-hoc tracking
3. Custom script
4. Separate workflow
5. Internal security process
6. Point security product
7. Multiple disconnected tools

A feature does not need to replace a commercial product to have consolidation value.

Prefer the least aggressive claim that accurately describes the improvement.

---

# 53. PLATFORM-LEVEL VALUE

When evaluating a source point, determine whether it demonstrates one of these broader AccuKnox advantages:

- unified security workflows
- cross-domain context
- runtime-first security
- cloud-native visibility
- workload enforcement
- security findings correlation
- AI security across multiple layers
- posture + detection + runtime connection
- reduced tool fragmentation
- centralized policy
- automated remediation/verification
- security context across environments

When appropriate, connect an individual feature to the larger platform story.

Do not force a platform statement into every post.

Across the full campaign, however, the audience should gradually understand why the capability belongs inside AccuKnox rather than existing as an isolated point feature.

---

# 54. FEATURE IMPORTANCE

Rank source points into:

### Tier 1: Campaign anchors
Major capabilities with strong customer or market significance.

Give these:

- strongest hooks
- better visuals
- more context
- differentiation
- possible consolidation angle

### Tier 2: Supporting capabilities
Useful improvements that demonstrate product depth.

Keep concise but explain the practical value.

### Tier 3: Minor changes
Small UI, configuration, compatibility, or implementation updates.

Use only if there are insufficient stronger points.

Never give a minor implementation detail the same campaign weight as a major product capability.

---

# 55. CREDIBILITY RULE

Do not describe every source point as:

- a breakthrough
- a major shift
- revolutionary
- game-changing
- industry-first
- transformative

Some updates are useful workflow improvements.

Call them what they are.

A small operational improvement can still make a good post if the practical benefit is clear.

---

# 56. CLAIM LEVELS

Separate:

### SOURCE FACT
Explicitly stated by the supplied page.

### VERIFIED EXTERNAL FACT
Confirmed through official documentation or a reliable external source.

### REASONED INTERPRETATION
A defensible conclusion based on the source.

### SPECULATION
Do not publish.

Never present an interpretation or inference as if the source explicitly claimed it.

For example:

SOURCE:
"The platform now supports automated MFA login recording."

VALID INTERPRETATION:
"This removes a manual authentication setup step from the DAST workflow."

INVALID CLAIM:
"This replaces every commercial DAST platform."

The first interpretation is reasonable. The second is unsupported.

---

# 57. CAMPAIGN ARC

When possible, structure the campaign across three stages:

### Stage 1: Awareness
Introduce the most interesting capabilities or security problems.

### Stage 2: Depth
Explain technical capabilities, workflows, and practical changes.

### Stage 3: Differentiation
Show consolidation, platform value, architectural advantages, or broader implications.

Industry posts should be inserted where they naturally reinforce or refresh the conversation.

Do not force a linear narrative if the source does not support one.

---

# 58. RELEASE NAME REPETITION

If the source is a release:

Mention the release/version often enough to establish context, but do not repeat the version in every tweet.

The campaign should make the release connection obvious through:

- wording
- feature context
- occasional version references
- campaign-level framing

Avoid:

"vX.X does..."
"vX.X adds..."
"vX.X introduces..."
"vX.X now supports..."

repeatedly.

Vary the language while keeping the source connection clear.

---

# 59. NO GENERIC THOUGHT LEADERSHIP

Do not create posts such as:

"Security teams need better visibility."

"AI security is becoming increasingly important."

"Cloud security is more important than ever."

"Kubernetes security is critical."

These statements are too broad to be useful.

Every thought-leadership post must be anchored to:

- a current event
- a specific technical problem
- a concrete observation
- a research finding
- a source capability
- a security incident
- a specific debate

If the post could have been written six months ago without changing a word, it is probably too generic.

---

# 60. HOOK DIVERSITY

Across a campaign, vary the reason the first line grabs attention.

Possible hooks:

- surprising fact
- technical contradiction
- security problem
- "what changed"
- before/after
- common assumption
- current incident
- question
- operational pain
- unexpected implication
- tool fragmentation
- architecture insight

Do not make every hook a feature announcement.

---

# 61. FOLLOW TEST

After generating the complete campaign, ask:

"If I were a security engineer or CISO seeing this account for the first time, would these 15 posts give me a reason to follow?"

The answer should be YES because the account provides a combination of:

- useful technical information
- current security commentary
- interesting incidents
- practical security lessons
- product knowledge
- informed opinions

If the only reason to follow is "AccuKnox has product updates", the campaign has failed.

Rewrite.

---

# 62. SOURCE-AGNOSTIC PIPELINE

The conceptual model for any URL:

```text
ANY URL
  |
  Understand source
  |
  Extract strongest atomic ideas
  |
  10 posts from that source
  |
  5 current industry posts
  |
  Connect industry -> AccuKnox only where justified
```

For a blog or research URL, 10 posts do not need to be product-feature posts. They are 10 posts derived from the supplied source.

The pipeline is:

```text
URL -> source intelligence -> content opportunities -> campaign strategy -> tweets -> visuals -> calendar -> QA
```

The content-opportunity layer stops Claude from paraphrasing a webpage.
