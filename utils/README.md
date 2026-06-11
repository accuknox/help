# utils

Support assets for agentic tasks and content generation. Not published as documentation.

## Root files

| File | What it is |
|---|---|
| `PPT TEMPLATE - ALWAYS WHEN ASKED TO MAKE PPTS USE THIS.pptx` | Master AccuKnox brand template — copy this as the base for every new deck |

## Folders

### `ppt-output/`
Build workspace for python-pptx slide decks. Contains the blank template, build scripts (`build.py`, `render.ps1`, `final_check.py`, `verify.py`), and template inspection tools (`.tmp_tpl/`). Generated `.pptx` files land here. See [`ppt-output/README.md`](ppt-output/README.md) for the full workflow.

### `ai-soc/`
AI SOC go-to-market assets: Excel data package, pitch deck, wireframes, and competitor UI screenshots (`competitor-screens/`, `raw-research/`).

### `comparisons-builder/`
Competitive comparison spreadsheets (AccuKnox vs Checkpoint, vs RHACS/NeuVector, vs Straiker, vs Invicti). Used for battlecards and sales collateral.

### `content-planning/`
Platform pages content plan and prompt files for content generation runs.

### `reports/`
Generated reports and design documents: CWPP report PDF and build script, Security Graph UI design brief, competitive analysis doc, and supporting images.

### `rfp-generation/`
RFP response generation scripts (`scripts/`) and output files (`responses/`). Includes both standard RFP responses and SLA documents.

### `technical-reference/`
Internal reference PDFs: playbooks (CWPP, ASPM, VM security), architecture docs, POC prerequisites, Kubernetes hardening guidance, and SLA escalation matrix. Read-only — do not edit.
