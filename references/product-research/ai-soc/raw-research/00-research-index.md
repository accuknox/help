# AI-SOC Raw Research Index

Unpolished research dumps that ground every polished deliverable in the parent folder. Compiled June 2026.

## URL access log (per the brief, confirmed up front)

| Source | Status | Notes |
|---|---|---|
| Harvey AI agentic SOC blog | Accessible, fully extracted | Reference architecture, not a competitor |
| Latio Pulse "Emerging Categories" | Accessible, fully extracted | First-wave vs second-wave framing |
| Latio Security Operations Report 2026 (PDF, 305pp) | Accessible via pdftotext | The centerpiece. Survey data, category map, 11 vendor spotlights |
| mate.security + blog | Accessible, fully extracted | Homepage + 6 blog posts crawled |
| exaforce.com (full site) | Accessible, 13 pages crawled | Product tours are interactive embeds, could not fetch click-paths via WebFetch; screen inventory recovered from demo-room listing |
| SentinelOne Purple AI + pricing | Accessible | Product page + pricing aggregators |
| Emerging vendors (Prophet, Dropzone, Radiant, Intezer, Torq, 7AI, AiStrike, Conifers, Simbian) | Accessible | Homepage + product pages |

Nothing in the brief was inaccessible. One gap flagged: Exaforce's interactive product-tour click-paths (exact button labels per frame) need a real browser to capture. The screen inventory is captured.

## Files

- [00-research-index.md](00-research-index.md) — this file
- [01-harvey-agentic-soc-architecture-teardown.md](01-harvey-agentic-soc-architecture-teardown.md) — the agentic architecture blueprint (world model, memory, multi-agent topology, agent isolation)
- [02-latio-security-operations-report-2026-synthesis.md](02-latio-security-operations-report-2026-synthesis.md) — full report synthesis, survey data, category taxonomy, vendor spotlights
- [03-pricing-and-market-benchmarks.md](03-pricing-and-market-benchmarks.md) — pricing teardown, recommended primitives, TAM, pain stats with sources
- [04-emerging-vendors-and-ui-ux-pattern-catalog.md](04-emerging-vendors-and-ui-ux-pattern-catalog.md) — 9 emerging vendors plus the cross-vendor screen vocabulary (foundation for the 30-40 screens)
- [05-market-research-synthesis.md](05-market-research-synthesis.md) — the strategic read, category definition, the four claims only AccuKnox can make
- [vendor-teardown-mate-security.md](vendor-teardown-mate-security.md)
- [vendor-teardown-exaforce.md](vendor-teardown-exaforce.md)
- [vendor-teardown-sentinelone.md](vendor-teardown-sentinelone.md)
- latio-report-full.txt — raw extracted text of the PDF

## The one-paragraph takeaway

The whole category agrees on one thing: the AI analyst is only as good as the data under it, and the move that matters is from AI-assisted to agentic. Every serious vendor (Exaforce, Mate, SentinelOne, the autonomous-analyst tools) detects, triages, investigates, and responds through API integrations. Not one of them enforces at the kernel, grounds its data in runtime truth from eBPF, or secures its own AI agents as untrusted workloads. That is the exact whitespace AccuKnox already occupies as a Zero Trust CNAPP. The AI-SOC is the intelligence layer on top of enforcement AccuKnox already does.
