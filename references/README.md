# references

Support assets for agentic tasks and content generation. MkDocs does not publish this folder.

Start with `source-of-truth/` for any AccuKnox fact. Use the other folders for drafts, competitor work and raw material.

## Naming Rules Keep Every Path Predictable

1. Use lowercase kebab-case for every new file and folder, for example `accuknox-vs-netskope-ai-security.xlsx`.
2. Put a date in `YYYY-MM` or `YYYY-MM-DD` form, never as a month name.
3. Put a new file in the folder for its job. Do not add loose files at the root of `references/`.
4. When you move or rename a file, update every path to it. Search `.claude/`, `references/` and `seo/` for the old path.

## `source-of-truth/` Holds the Facts Every Writer Loads

| File | Contents |
|---|---|
| `accuknox-summary-and-narrative.md` | Approved company positioning from Nat Natraj (2026-09-24): a five-point summary, the eight AI Security modules, analyst and customer proof, the three differentiators, and five technical blog links. Use it for intros in blogs, decks, RFPs and sales emails. |
| `ai-security-data-points.md` | AccuKnox AI security facts, each with a source tier: the four shadow AI surfaces, the 13 Prompt Firewall browser use cases, integration coverage, the AI for Security features, asserted facts that still need a doc, and the Netskope gaps. The runtime contract and the writing hook load it for any AI security writing. |
| `ai-security-checklist.xlsx` | The export of Gaurav Mishra's Google Sheet "AI Security Checklist" (last modified 2026-09-22). One tab holds the staged AI Security Checklist (discovery, POC must-haves, PCI column). The other tab holds the Prompt Firewall Use Cases. |
| `ai-security-checklist.md` | A Markdown copy of both checklist tabs, with the sheet URL. Search this copy, and refresh both files when the sheet changes. |
| `shadow-ai-coverage.pdf` | The AccuKnox Shadow AI coverage document. |

## `drafts/` Holds Unpublished Writing by Channel

The writing hook and `.claude/core/runtime-contract.md` send each channel's output to one subfolder.

| Folder | Channel |
|---|---|
| `drafts/blog/` | Blog posts |
| `drafts/case-study/` | Customer case studies |
| `drafts/comparison/` | Comparison and versus pages |
| `drafts/press-release/` | Press releases |

## `competitive/` Holds Competitor Comparisons and Battlecards

`competitive/battlecards/` holds the comparison spreadsheets: AccuKnox vs Checkpoint, Promptfoo, RHACS/NeuVector, Straiker, Invicti, Netskope, and a container comparison. It also holds the build scripts.

1. `netskope/` builds the Netskope spreadsheet and the Markdown draft, and pushes the Google Sheet. `netskope/battlecard/` is the reference PDF battlecard build, with its logos and back page in `assets/`.
2. `ai-stack-ranking-v3/` builds `ai-security-stack-ranking-v3-beta.xlsx` from one JSON file per vendor in `vendors_v2/`. `ai-stack-ranking-sources.pdf` lists the sources.
3. `build_promptfoo_battlecard.py` builds the Promptfoo spreadsheet.

`competitive/aspm-comparisons/` holds the ASPM versus pages: Black Duck, HCL AppScan, Invicti and OpenText Fortify.

## `product-research/` Holds PRD and Market Research

| Folder | Contents |
|---|---|
| `ai-soc/` | The AI SOC go-to-market package: `ai-soc-data-package.xlsx`, `ai-soc-pitch-deck.pptx` and `ai-soc-wireframes.pptx`, plus `competitor-screens/` (13 competitor UI captures) and `raw-research/` (market and vendor teardown notes). |
| `dspm/` | The DSPM competitive analysis site: a 10-page HTML report in `dspm-analysis/` (executive summary, competitor cards, feature matrix, next steps), plus a standalone `dspm-competitive-analysis.html`. |
| `security-graph/` | The Security Graph UI work: `design-brief.md`, `competitive-analysis.docx`, and 15 competitor graph screenshots in `competitor-screens/`. |

## `technical-reference/` Holds Internal Product Documents

These files are read-only. Do not edit them.

| Folder | Contents |
|---|---|
| `architecture/` | The control plane architecture document (v3.4 PDF) and the v3.5 technical review. |
| `compliance/` | The SOC2 report (2024), the ISO 27001-2022 internal audit report, the VAPT report, the SLA escalation matrix, the CTR Kubernetes hardening guidance, and the RBI draft guidance on model risk management. |
| `decks/` | The AI Security macro deck (2026-06), the AI Security onboarding, architecture and support matrix deck, the DAST deck (2026-06), and the VM security journey use cases. |
| `playbooks-and-poc/` | The CWPP and ASPM playbooks, the container security POC guides, the CSPM POC prerequisites, and the Air India AI security SOP. |

## Other Folders Hold Assets, Campaigns and Generated Output

| Folder | Contents |
|---|---|
| `assets/demo-screenshots/` | 22 curated, captioned product screenshots for AI security assets: dashboard, findings, AI red teaming, prompt firewall, runtime protection and zero-trust discovery. `DEMO-SUMMARY.md` indexes the captions. Use these first for blog and deck images. |
| `campaigns/prompt-guardrails-blog-series/` | The 3-part prompt guardrails blog series (voice agents, multi-turn jailbreaks, indirect prompt injection): `series-brief.docx`, the three blog Markdown files, chart images in `images/`, and the research PDFs and documents in `reference-files/`. |
| `onboarding/openshift-private-cloud/` | The OpenShift private cloud onboarding walkthrough: `onboarding-steps.md`, `part-1-walkthrough.md`, two screen recordings (`part-1.mp4`, `part-2.mp4`), the `part-1.srt` transcript, and open questions for Murtaza. |
| `reports/` | Generated reports: `cwpp-management-report.pdf` with its build script and proposal email, the DAST appendix build script, and the OSS tool name audit. |
| `rfp-generation/` | RFP response scripts in `scripts/` and output in `responses/`. `responses/client-rfps/` holds inbound client RFPs. The scripts cover RFP responses and SLA documents. |
| `content-planning/` | The platform pages content plan and the prompt files for content runs. `seo/README.md` marks this folder as outdated, so do not use it as the SEO source of truth. |
