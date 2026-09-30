# Raw Research — Harvey AI "Building an Agentic SOC" Teardown

Source: https://www.harvey.ai/blog/building-an-agentic-security-operations-center
Status: Fully extracted. Accessible.
Purpose: Harvey is not a competitor. It is a reference architecture. They built an internal agentic SOC and published the design. This is the single best public blueprint for the agentic layer AccuKnox needs to build. Read this as engineering input for the PRD, not as competitive intel.

---

## 1. The core thesis

Harvey reframes the SOC away from "humans writing queries against a SIEM" and toward a "persistent, agent-native SOC" that runs on a "security world model" — a machine-readable representation of the threat surface, live telemetry, and accumulated interpretation.

The line that matters most for AccuKnox:

> "The agentic SOC is fundamentally an exercise in spending compute to ask the data better questions, faster."

And the corollary that should shape our whole data-layer argument:

> "Invest in your log warehouse before you invest in your agents."

This is the same thesis Latio reaches independently. Both say the same thing: the agent is downstream of the data. If the data layer is slow or unstructured, the agent hallucinates and burns money. AccuKnox's eBPF runtime telemetry is a data-layer advantage, not just a detection feature. Frame it that way.

## 2. The Security World Model (four layers)

This is the substrate every agent reads from and writes back to.

1. **Security Analytics Corpus** — a continuous, append-only telemetry stream, terabytes per day, from product + infra + SaaS tooling, served through optimized ClickHouse tables as "ground truth."
2. **MCP Server Infrastructure** — built with RunReveal, giving agents "legible tools to access and understand the corpus." The agents reach data through MCP tools, not raw SQL.
3. **Threat Model System Prompt** — structured as "paths to crown jewels — concrete chains of access an attacker would traverse to reach customer data." Severity is anchored to which path a finding sits on.
4. **Self-Improving Intelligence Layer** — a fleet of hunting agents that persist memories and iterate detection work over time.

Scale signals they published:
- "petabytes of historic data"
- "5,300 persistent memories"
- "2,500+ investigations from the last 30 days"
- "400+ production detections"

## 3. The data-layer obsession (most transferable lesson)

- **Query latency is context budget.** "The difference between 200ms and 2s per query is the difference between an agent that explores three hypotheses and one that explores 30." Slow queries literally make the agent dumber because it runs out of context budget before it finishes reasoning.
- **Semantic enrichment beats raw access.** They compress raw `JSONExtract` queries into simple computed columns (example given: `isProdCluster`). This reduces the cognitive load and token spend per agent loop.
- **Optimization philosophy:** semantic richness and speed multiply every downstream agent loop. Spend on the warehouse first.

AccuKnox takeaway: our pitch should explicitly say "we built the data layer for agents, not just for humans." Normalize to a common taxonomy, pre-enrich, index on ingest, keep hot queries sub-second.

## 4. Multi-agent topology — three persistent background workflows

These run on a schedule, read the world model, and write findings back, compounding intelligence across runs.

1. **Daily Reports** — scores alert volume, detection performance, ingest anomalies; surfaces investigation leads. Inherits baselines (noisy detections, benign IP patterns, pending rotations).
2. **Hourly Alert Triage** — semantic grouping of alerts; auto-escalates critical clusters into deep-dive investigations.
3. **Threat-Watch** — morning ingestion of CISA KEV and public threat intel, cross-referenced against deployment coverage. Remembers TTPs already covered.

## 5. The detection-engineering pipeline (four phases)

A staged agent workflow that turns a threat into a tested detection into an alert:

| Phase | Function |
|---|---|
| Research | External intelligence cross-referenced with internal context |
| Consolidate | Documentation and deduplication |
| Validate | Data-tested detection proposals (run against historic false positives) |
| Finalize | Pull request generation for human review |

The design philosophy behind it, quoted directly:

> "Agents are extraordinary at the parts of detection work that are tedious like consolidation, deduplication, validation, documentation, and continuous tuning; they are merely competent at the parts that demand judgment."

This is the single best sentence to steal for the PRD's "agentic design principles." Put agents on tedium, humans on judgment.

## 6. Memory architecture (how it self-improves)

- **Postgres-backed knowledge base.** Categorized facts (entity, finding, baseline) each with TTLs.
- **Deduplication** via prefix match and Jaccard similarity.
- **Per-profile injection budgets** decide how much memory each workflow is allowed to pull into context.
- **Read at start, write at end.** Every agent loop reads memory first, writes findings back last.
- **Humans close the loop.** Analysts annotate artifacts with notes that can be persisted as agent memories marked `source='analyst'`.

The compounding claim:

> "Each loop's output is the next loop's input. The world model is the substrate that makes that compounding possible; the longer it runs, the more it knows."

Concrete examples of memory paying off:
- Validation agents remember false-positive patterns.
- Clustering agents inherit prior verdicts.
- Threat-watch agents remember existing coverage so they do not re-flag covered TTPs.

## 7. Explainability and human-in-the-loop

- "Gated by human review on every production change."
- Agents produce "an auditable narrative" inside a "bespoke canvas enabling branched prompts for complex investigations."
- Worked example: when Wiz reported the LiteLLM supply-chain compromise, an investigation kicked off automatically, with steps and findings documented for human review.
- Partnership model: humans on judgment, agents on tedium, producing "a paper trail that traditional SOCs can't match."

## 8. The security separation that AccuKnox must copy

Harvey runs two distinct agentic platforms with different trust postures:

- **Spectre** (product agents) — operates inside the trust boundary, optimized for customer-work speed.
- **Agentic SOC** — operates on the trust boundary, optimized for adversarial robustness.

Their rationale, quoted:

> "Forcing both onto one substrate creates exactly the privilege-escalation path the SOC exists to prevent."

This is gold for AccuKnox because it maps directly onto our differentiator. AccuKnox already ships KnoxClaw and ModelArmor for sandboxing AI agents at the kernel. Harvey is telling the market, in their own words, that an agentic SOC is itself an attack surface and must be isolated. AccuKnox is the only vendor in this set that can enforce that isolation at the syscall level. This is the security-hardening-of-the-agents story the brief asks for, validated by a third party.

## 9. Published results

- Expanded detections from 75 to 400+ (5.7x coverage).
- Reduced weekly alert average from ~300,000 to ~20,000 (~95% reduction in alert space).
- Combined claim: "5.7x increase in coverage while shrinking alert space by ~95%."
- Alert classification model: "active triage, silent tripwires, and informational signals to ensure high-fidelity attention on critical events."
- One-button vulnerability response shortens investigation "from hours or days to minutes."

## 10. What AccuKnox lifts directly into the PRD

1. **World model as the substrate.** AccuKnox's version: normalize all telemetry into a common taxonomy, enrich on ingest, expose to agents via MCP-style tools. eBPF runtime telemetry is a first-class layer.
2. **Threat-model-anchored severity.** Severity is a function of which path-to-crown-jewels a finding sits on, not how scary the alert string looks. AccuKnox already has the runtime + asset context (CNAPP) to build these paths.
3. **Agents on tedium, humans on judgment.** Four-phase detection pipeline. Reuse the Research / Consolidate / Validate / Finalize split.
4. **Persistent memory with analyst feedback.** Continuous learning requirement in the brief maps exactly to this. Mark analyst-sourced memories distinctly.
5. **Isolate the SOC agents at the trust boundary.** This is AccuKnox's KnoxClaw / ModelArmor moat. No other AI-SOC vendor enforces agent isolation in-kernel. Build the whole "secure the agents themselves" section around this.
6. **Data layer before agents.** The marketing line writes itself: "An AI analyst is only as good as the data underneath it. We rebuilt the data layer for runtime truth, then put agents on top."
