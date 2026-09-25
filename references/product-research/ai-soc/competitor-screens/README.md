# Competitor AI-SOC UI/UX Screenshots

Real captured screenshots of the top AI-SOC vendors' product pages, June 2026. 36 PNGs across 18 pages from 13 vendors. Each page has a `-hero.png` (the top fold, the main product visual) and a `-full.png` (the entire page, every UI mockup the vendor publishes). Captured headless at 1440px width with lazy-loaded images triggered, so the product screenshots the vendors embed are all present.

How to use these. Pair them with the vendor teardowns in `../raw/`. The teardowns describe the screens, these show them. Together they are the competitive UI/UX reference for designing AccuKnox's own console, and the evidence behind the deck's "Competitor UI/UX teardown" slide.

The one thing to notice across all 36 images. Every console ends at investigate and respond. Look for a screen that shows a threat blocked at the kernel, or an attack chain halted mid-sequence, or the vendor's own agents shown sandboxed. There isn't one. That absence is the AccuKnox opening.

---

## Exaforce (the benchmark, $200M raised, Latio AI Innovator + SIEM Disruptor)

- `exaforce-01-home` — Hero "AI gave attackers machine scale. Now you have the advantage." The four Exabots framed as personas (Detect, Triage, Investigate, Respond).
- `exaforce-02-platform` — Platform overview, "10x the productivity and efficacy of your SOC," multi-model AI.
- `exaforce-03-triage` — Exabot Triage. The richest UI page: threat findings table, the attack-chain visualization, entity graph, evidence tab.
- `exaforce-04-investigate` — Exabot Investigate. NL search results, the dual-mode query builder, the visual exploration graph, events-over-time dashboard.
- `exaforce-05-data-platform` — The dual hot/cold data architecture, "60-80% cost reduction vs traditional SIEMs."
- `exaforce-06-respond` — Exabot Respond. The visual workflow editor, Task Agent nodes, the Slack human-in-the-loop approval card.

What to take. Exaforce sets the bar for the agentic data-platform UX. AccuKnox must match this screen vocabulary, then add the enforcement and agent-security screens Exaforce does not have. Note their "deterministic, explainable" framing is their answer to "isn't this just GPT."

## Mate Security (Latio AI Innovator, knowledge-graph foundation)

- `mate-01-home` — The Security Context Graph concept, the alert-coverage dashboard (6K to 23K investigated), the closed-by-Mate vs escalated chart, the 93% MTTR reduction chart (2300 to 100 min). The clearest dashboard visuals in the set.

What to take. Mate's CD/CR loop and context graph are the narrative to beat. AccuKnox's answer is CD/CR plus enforcement, grounded in runtime not tickets.

## SentinelOne Purple AI (the incumbent benchmark)

- `sentinelone-01-purple` — Purple AI "the world's most advanced AI security analyst," the explainable AI Verdict, natural-language hunting, agentic Athena workflows, the MCP server.

What to take. Closed, endpoint-rooted, the autonomous tier gated to the top package. AccuKnox wins on kernel enforcement, open source, and AI-agent security.

## Autonomous analyst tools

- `dropzone-01-home`, `dropzone-02-product` — Dropzone AI. "Glass Box, Not Black Box," the plain-English investigation reports, the attack timeline, the chatbot. Capacity-based pricing (~$36K/yr per AI analyst).
- `prophet-01-home` — Prophet Security. The agentic SOC analyst, threat hunter, and detection advisor. Shows the investigation plan, queries, and evidence.
- `radiant-01-platform` — Radiant Security. Cases dashboard, the "1 to 3 alerts a day" triage queue, the reasoning view. Flat, predictable pricing, markets against per-alert.
- `intezer-01-forensic` — Intezer. Forensic verdicts fused with agentic reasoning, the triage queue with verdicts and recommended actions, 98% verdict accuracy.
- `simbian-01-agent` — Simbian. The verdict screens with instant confidence rating, the "Context Lake," 92% automated resolution.

What to take. These replace a Tier-1 analyst and stop there. No posture, no runtime, no enforcement. AccuKnox replaces the architecture, not just the analyst.

## Agentic platforms and orchestration

- `torq-01-hypersoc` — Torq HyperSOC. Socrates the agentic quarterback, the case interface, the agent builder, the auditable reasoning record.
- `7ai-01-home` — 7AI. The Kanban cases board, the swarm of 60+ agents, the drag-and-drop workflow builder.
- `aistrike-01-home` — AiStrike. The "SOC intelligence fabric," the four-cycle composite-AI loop, explainable investigations.
- `conifers-01-home` — Conifers CognitiveSOC. "One fabric, five stages, agents inside, analysts on top." The same closed-loop idea as Mate's CD/CR.

What to take. Strong orchestration and case-management UX. All of it is API-level response. None enforce at the kernel.

---

## Cross-vendor pattern summary (what the images confirm)

Every vendor's UI converges on the same screens: an alert triage queue that shrinks to a handful, a cases or Kanban board, an investigation timeline or attack chain, a glass-box reasoning panel, a verdict card with a confidence score, a chat copilot, a coverage and MTTR dashboard, a response or workflow builder, and increasingly a detection-as-code editor and a context graph. AccuKnox's UI/UX spec (`../UIUX-Journey-and-Screens.md`) covers all of these, then adds the three screens none of these vendors can render: the eBPF enforcement policy view, the live runtime block timeline, and the agent sandbox monitor.

## Capture details

Captured with headless Chromium (Puppeteer), 1440x900 viewport, cookie banners dismissed, full-page scroll to trigger lazy-loaded images. See `_capture-log.json` for the exact URLs and capture status (18 of 18 succeeded). Regenerate any time with `../deck-build/screens.js`.

Usage note. These are competitors' published marketing screenshots, captured for internal competitive analysis. Keep them to internal enablement and the competitive teardown. Do not republish them in customer-facing AccuKnox material.
