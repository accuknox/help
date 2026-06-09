# Raw Research — AI-SOC Pricing and Market Benchmarks

Compiled June 2026. All figures sourced inline. Aggregator numbers (CostBench, G2, UnderDefense, Spendflo) are list/estimate figures, not vendor-confirmed contracts. Treat vendor-page numbers as authoritative and aggregator numbers as directional.

---

## Section 1 — Pricing model teardown

### Endpoint / EDR-XDR platforms

**SentinelOne Singularity** — per-endpoint/year, tiered. The agentic AI SOC analyst is gated to the top Enterprise tier; Purple AI drops in much earlier (Control).

| Package | List (per endpoint/yr) | Bundled | AI gating |
|---|---|---|---|
| Core | $69.99 | Cloud-native NGAV, basic EPP | No Purple AI |
| Control | $79.99 | + firewall/device control | Purple AI included from here up |
| Complete | $179.99 | + EDR/XDR, 14-day retention, Identity Threat Detection | Purple AI; agentic analyst as add-on |
| Commercial | $229.99 | + 90-day retention, Managed Threat Hunting | Purple AI; agentic analyst as add-on |
| Enterprise | Contact sales | + full managed services / MDR | Agentic AI SOC Analyst is the headline feature |

- Monthly equivalents (aggregators): Core ~$5.83, Control ~$6.67, Complete ~$8.25, Commercial ~$17.50 per endpoint/mo.
- AI-SIEM ingest: consumption per-GB, 10 GB/day free, overage quote-only.
- Purple AI: no standalone price, bundled from Control up.
- Takeaway: endpoint is the billing primitive. Purple AI is a mid-tier upsell hook. The autonomous SOC analyst is the enterprise anchor (top tier + custom quote).
- Sources: sentinelone.com/platform-packages, sentinelone.com/platform/purple, CostBench, TrustRadius, CheckThat.ai.

### Legacy SIEM (the cost-pain anchor)

**Microsoft Sentinel** — per-GB ingested with commitment tiers.

| Model | Rate |
|---|---|
| Pay-as-you-go | ~$4.30 to $5.22 per GB/day |
| Commitment 100 GB/day | ~$2.96/GB/day |
| Commitment 1,000+ GB/day | ~$2.46/GB/day |

Commitment tiers save up to ~52% vs PAYG. Sources: microsoft.com/security/pricing, learn.microsoft.com, UnderDefense.

**Splunk** — dual model: ingest (per GB/day) or workload (per SVC compute unit).
- Cloud ingest list ~$0.60 to $1.20 per GB/day; real spend $1,800 to $18,000/yr per 1 to 10 GB/day depending on tier. Overages run 1.5 to 2x base.
- Workload Pricing decouples from data volume, bills compute. Sources: splunk.com/products/pricing, UnderDefense.

This is the legacy SIEM cost pain anchor. Ingestion is a tax that scales with telemetry growth, not with security value delivered.

### AI-SOC / agentic-SOC startups

The market is splitting into two camps: consumption (per-investigation/alert) vs flat use-case/seat. The flat-pricing camp attacks consumption pricing as a defect.

| Vendor | Model | Anchors | Bundled | Funding |
|---|---|---|---|---|
| Dropzone AI | Consumption, per AI analyst | ~$36,000/yr per AI analyst = up to 4,000 investigations/yr (~$9/investigation), "one human Tier-1 analyst." Unlimited users | All alert categories, integrations, TI feeds, chatbot, 8-hr SLA | $37M Series B |
| Radiant Security | Flat, priced on use cases + end users, all features included | Entry ~$1,188/yr (directional). "100% predictable, no per-alert add-ons." Markets against per-alert | Full platform, no add-ons | $15M Series A (Next47) |
| Prophet Security | Not disclosed (quote-only) | >1M autonomous investigations; claims 10x faster response, 96% fewer false positives | Full agentic SOC suite | $41M total (BCV seed + Accel Series A) |
| Exaforce | Not disclosed; platform + bundled MDR | Claims 10x reduction in human SOC work; Exabots at 98% accuracy | Agentic platform + MDR | $200M total ($75M A + $125M B at ~$725M valuation, May 2026) |
| Torq HyperSOC | Platform subscription, scales by workflows/integrations/actions, quote-only | No public list | Multi-agent (Socrates orchestrator), native MCP, case management | $1.2B valuation, ~$332M total |
| Mate Security | Not disclosed (early design-partner) | Pilot-only; "10x more effective" analyst claim | Context graph + investigation agents | $15.5M seed (Team8, Insight) |

### MDR (per-endpoint/month benchmark)
- Typical $10 to $30 per endpoint/month. Basic $10 to 15, elite with dedicated advisors $20 to 30+.
- Provider ranges: Huntress $3 to 9, Sophos $7 to 17, SentinelOne $7 to 23, Arctic Wolf $8 to 25, CrowdStrike $25 to 45 per endpoint/mo.
- Hidden costs: onboarding $5K to $25K, log overages $1 to 5/GB/day, IR retainers $250 to $400/hr. A 200-endpoint org lands at roughly $24K to $72K/yr.
- Sources: UnderDefense, mdrcost.com, Expel.

---

## Section 2 — Recommended pricing primitives for AccuKnox AI-SOC

The data points to one conclusion. Do not price the AI-SOC on raw alert or GB volume. That re-imports the exact SIEM cost pain customers are escaping, and the flat-pricing challengers (Radiant) are already winning the messaging war by calling per-alert pricing "not scalable."

1. **Avoid pure per-GB / per-alert as the primary meter.** Telemetry grows 20 to 30%/yr. If the bill scales with alert volume, AccuKnox is economically aligned against noise reduction, the thing the product sells. Dropzone draws review criticism precisely because per-alert ingestion gets cost-prohibitive at large or unpredictable volume.
2. **Price on the AI analyst as the unit of value, the headcount it replaces.** The buyer already budgets in analyst FTEs. Dropzone's "$36K/yr = one Tier-1 analyst = 4,000 investigations" works because it maps to a loaded human Tier-1 SOC analyst (roughly $90K to $130K loaded in the US). "An AI analyst at ~30% of a human's cost" is an instantly legible ROI story.
3. **Flat platform fee + capacity tiers, not a la carte usage.** Radiant's "all features included, no surprise bills" is the predictability story buyers want after a decade of SIEM overage trauma. Combine: flat platform access fee + a few AI-analyst capacity tiers (e.g. 2k / 4k / 8k investigations) with soft overage.
4. **Gate the autonomous tier as the premium anchor.** Copy SentinelOne's structure, not its primitive. Entry tiers land on AI-assisted triage; reserve full autonomous response for the top tier (sales-assisted). Protects margin, creates an expansion ladder.
5. **Recommended primitive stack:**
   - Primary meter: AI SOC analyst unit (capacity = investigations/yr), benchmarked at ~25 to 35% of a loaded human analyst cost.
   - Floor: flat platform fee (all integrations + detection content bundled).
   - Premium gate: autonomous response / agentic remediation on the top tier.
   - Avoid as primary: per-GB ingest and per-alert. If ingesting customer logs, pass through at cost with a generous free allowance (mirror SentinelOne's 10 GB/day free).
   - Optional asset/identity overlay where coverage genuinely scales with assets (cloud identities monitored), which aligns with AccuKnox's CNAPP/AI-SPM footprint.

One-line positioning: **price the outcome (analyst capacity replaced), bundle the platform, never bill the noise.**

---

## Section 3 — Market sizing and growth

- Cybersecurity Agentic AI market: $1.83B (2025) to $7.84B (2030), 33.83% CAGR. Mordor Intelligence.
- Agentic AI Security market (broader): $1.65B (2026) to $13.52B (2032), 42.0% CAGR. MarketsandMarkets.
- AI in Cybersecurity (whole category): $25.35B (2024) to $93.75B (2030), 24.4% CAGR (Grand View). A second house pegs $25.53B (2026) to $50.83B (2031), 14.8% CAGR (MarketsandMarkets). Cite the agentic-specific numbers for AI-SOC TAM.
- Spending split (Gartner 2025): AI-amplified security (using AI to defend) hit $49B in 2025; securing AI itself was $2.8B. Enterprises spend ~17x more on AI-powered security than on securing AI. Total security forecast $244.2B.

## Section 4 — Pain-point statistics (FUD ammunition)

### Burnout / turnover / alert fatigue
- 71% of SOC analysts experience burnout. (NetEnrich, UnderDefense)
- 64% considering leaving within a year. 70% of analysts with 5 years or less leave within three years. Average tenure 18 to 24 months. (UnderDefense)
- 76% cite alert fatigue as a top challenge; 73% cite analyst burnout. (Gurucul/CSI Pulse of the AI SOC 2025)

### Alert volume / false positives / uninvestigated
- ~960 alerts/day average; enterprises 3,000+/day from ~30 tools. (Pulse of the AI SOC 2025)
- 40% of alerts go completely uninvestigated (one ref cites 63% unaddressed).
- 61% admit ignoring alerts that later proved critical; 60% experienced breaches tied to ignored alerts.
- False-positive rates frequently exceed 50%, up to 80%. False positives consume ~52% of analyst time. ~70 minutes to fully investigate one alert.
- 88% report alert volume increased; 46% saw a >25% spike in 12 to 24 months.

### Cost of a data breach (IBM 2025)
- Global average $4.44M (down 9% from $4.88M in 2024).
- US average $10.22M, record high, up 9% YoY. Healthcare highest at $7.42M.
- Mean time to identify + contain: 241 days (158 + 83), lowest in 9 years.
- AI/automation in security operations saved ~$1.9M per breach and cut the lifecycle by ~80 days.
- Shadow-AI angle: high shadow-AI use added $670K to average breach cost. 13% of orgs reported breaches of AI models/apps; 97% of those lacked AI access controls.

### SIEM total cost of ownership
- TCO runs 2 to 3x the headline license once staffing + integration are added.
- Telemetry grows 20 to 30%/yr. At 5 TB/day and $2 to 4/GB, ingestion alone is $3.6M to $7.3M/yr before storage/compute/staff.
- A mid-size enterprise at 2 to 5 TB/day runs $1.5M to $4M/yr all-in.

### Gartner / Forrester on AI in the SOC
- By 2028, 70% of large SOCs expected to pilot AI agents for Tier-1/2 ops; only 15% will see measurable improvement without structured evaluation. Multi-agent AI in threat detection rises from 5% to 70% by 2028, mostly to augment not replace.
- By 2028, 50% of enterprise cybersecurity IR effort will focus on incidents involving custom-built AI-driven applications (AI as attack surface).
- By 2028, 25% of enterprise GenAI applications will experience at least 5 minor security incidents/year.
- Caution flag: Gartner predicts >40% of agentic AI projects canceled by end of 2027 (cost/value/risk). Use for honest positioning.
- Forrester 2026: predicts an agentic-AI deployment will cause a publicly disclosed breach this year, leading to dismissals.

---

## How AccuKnox uses this

- The pricing model writes itself around the "AI analyst FTE" primitive with a flat platform floor and an autonomous top tier. See the polished pricing deliverable.
- The pain stats anchor the FUD in the PRD, blog, deck, and video. Lead with 71% burnout, 40% uninvestigated, $10.22M US breach, 241-day dwell.
- The $670K shadow-AI breach premium plus the 17x AI-defense-vs-securing-AI spend gap is the bridge from "AI-SOC" to AccuKnox's AI-security moat. The market overspends on AI-powered defense and underspends on securing the AI itself. AccuKnox does both.
- The Gartner ">40% of agentic projects canceled" stat is the honesty hook. AccuKnox's answer is runtime enforcement and explainability, the two things that make an agentic project survivable.
