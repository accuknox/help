---
title: AccuKnox AI Security Products, Product Notes
updated: 2026-09-26
use: Positioning, onboarding and objection handling for AI DAST, AI SAST, the AccuKnox AI Gateway, Shadow AI Discovery and AI-BOM
---

# AccuKnox AI Security Products

These notes hold what the product team explained about five AI security products. Each file gives
the product definition, the onboarding flow, the limits of the first release and a short AE
cheat sheet. Use them for sales enablement, product pages, FAQs and onboarding guides.

## Product Must Confirm Every Asserted Fact Before It Ships

The tiers come from `references/source-of-truth/ai-security-data-points.md`.

| Source | Tier | Where a fact can ship |
| --- | --- | --- |
| A product walkthrough by the AccuKnox product and engineering team | A | Sales enablement and internal drafts. Confirm with product before a public page |
| `references/source-of-truth/shadow-ai-coverage.pdf` | I | Sales PDFs, decks and RFP answers |
| A page under `docs/` | D | Anywhere |

On 2026-09-26 the requester confirmed that web pages may market the AccuKnox AI Gateway, AI DAST
and IDE-based AI SAST ahead of release. Tag each one "Coming soon" on the page. The other tier A
facts still need product confirmation.

Every row in these files names its tier. A value in square brackets is a gap or a probable
transcription error. A human must confirm it before the value ships.

## Six Files Cover Five Products and One Use-Case Map

| File | Product | What it answers |
| --- | --- | --- |
| `ai-dast.md` | AI DAST | What AI does in the pentest, the five onboarding areas, BYOM, what is not in the first release |
| `ai-sast.md` | AI SAST | The IDE and pipeline surfaces, the Black Duck comparison, the false positive caveat |
| `ai-gateway.md` | AccuKnox AI Gateway | Visibility, then governance, then the prompt firewall. Deployment modes and the competitor set |
| `shadow-ai-discovery.md` | Shadow AI Discovery | The four surfaces, their maturity, the CASB gap, the competitor comparison |
| `ai-bom.md` | AI-BOM | The two ingestion paths and hosted-model scanning |
| `use-cases-by-category.md` | All of the above | Use cases sorted into three groups. AI gateways as a category, the AccuKnox AI Gateway, and Shadow AI |

## How the Five Products Fit Together

Shadow AI Discovery finds the AI in use. The AccuKnox AI Gateway routes and governs the model
traffic that discovery finds, and it runs the prompt firewall inline. AI-BOM records the models,
frameworks and dependencies as an inventory. AI SAST and AI DAST cover the application lifecycle,
from the developer's IDE to a black-box pentest of the running app. The AccuKnox AI Gateway is also
the model routing layer that AI SAST uses.

## Related

- `references/source-of-truth/ai-security-data-points.md`, the fact file with source tiers
- `references/source-of-truth/shadow-ai-coverage.pdf`, the Shadow AI coverage sheet
- `docs/use-cases/shadow-ai-discovery.md`, the public Shadow AI page
- `docs/use-cases/prompt-firewall-overview.md`, the public Prompt Firewall page
