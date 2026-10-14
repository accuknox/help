---
title: NTT Data reply on matrix criteria and maturity
status: DRAFT, needs product sign-off on the bracketed items
thread: Re: AccuKnox <> NTT Data Group (Xue-san, 14 Oct 2026)
asset: AccuKnox AI-Security-Stack-Comparative Matrix-v3 10.13.2026.pdf
---

# NTT Data Reply on Matrix Criteria and Maturity

## Six Items Need Sign-Off Before You Send

Resolve F1 first. It changes what the matrix claims. Every other item only fills a bracket in the email.

- **F1. The AI-GRC cell says Supported with no BETA tag, but our own docs say AI-GRC is coming soon.** The `ai-security-arch.md` page says "Neither is in the console today". The `aiml-overview.md` page and the glossary also say coming soon. The AI Security FAQ lists "AI Compliance" as live, so our docs disagree with each other. Xue-san can find the coming-soon page on help.accuknox.com. Decision for Nat and product: relabel the cell BETA or Partial in v3.1. The email below says AI-GRC is coming soon.
- **F2. The Model cell names GGUF and safetensors.** The live ML Static Scan page lists Pickle, HDF5/H5, TensorFlow SavedModel, checkpoints and ONNX. Dataset poisoning detection appears only in AI Security FAQ 24, with no how-to page.
- **F3. No source calls AgentZ "GA".** John told NTT on 13 Oct that AgentZ launched in August 2026. The AgentZ FAQ marks the Coding workspace type as Preview.
- **F4. The AI Gateway has no confirmed label.** The v3.7 draft notes document it and still list open items. The product ruling of 2026-09-26 allows a "Coming soon" tag on web pages.
- **F5. The Shadow AI Beta items come from the 2026-09-26 product ruling.** These are macOS host scanning and the desktop telemetry app. Confirm the ruling still holds on 14 Oct.
- **F6. Low priority. The Noma Red Team cell says multi-turn attacks in CI/CD, mapped to OWASP.** The Noma page cited in the matrix shows multi-turn attacks and no CI/CD or OWASP text. The error favors Noma, not AccuKnox. Re-check it before anyone defends that cell.

## Email for John to Forward Once F1 to F5 Are Closed

**Subject:** Re: AccuKnox AI Security Comparative Matrix, Criteria and Maturity

Xue-san,

Thank you for the questions. The answers are current as of 14 October 2026.

**1. How we rate Supported and Partial**

We score every vendor with the same rules. AccuKnox is included.

- Each of the 8 modules has a benchmark of 3 parts.
- **Supported** means the vendor's public pages show all 3 parts.
- **Partial** means the pages show 1 or 2 parts.
- **No evidence** means we found nothing after two or more searches.
- The score is Supported = 1, Partial = 0.5, No evidence = 0.
- AccuKnox scores 7.5 of 8. That is 7 Supported and 1 Partial.

| Module | The 3 parts tested |
| --- | --- |
| AI-SPM | AI inventory, shadow AI, pipeline posture |
| Agentic AI Security | Managed agents, MCP, agent sandbox |
| AI-DR | Detect, respond, block at runtime |
| Prompt Guardrails & AI Gateway | Inline firewall, injection and PII, unsafe output |
| Compliance and AI-GRC | AIBOM, framework mapping, audit trail |
| Red Team + AI DAST | Attack library, live multi-turn attacks, CI/CD |
| AI & Agent Identity Security | Agent identity, least privilege, non-human identity (NHI) |
| Model, Dataset + AI-SAST | Model files, datasets, AI code scanning |

One example: Cranium rates Partial on AI-SPM. Its public pages show no Kubernetes or on-prem AI inventory.

Three limits apply to the ratings.

- The ratings measure public evidence against the AccuKnox benchmark. They do not measure product depth. A vendor may have features it does not publish.
- Every competitor cell links to that vendor's own page. Page 7 of the PDF lists the links. The Has and Lacks lines in each cell give the reason for the rating.
- If you know that a cell is wrong, tell us. We will re-check it against the vendor's page.

**2. Which Supported features are GA**

The BETA tag in the matrix marks a module with a part that is not yet General Availability (GA). The Supported rating counts only the GA parts of that module. This table lists the GA parts and the other parts for each AccuKnox module.

| Module | GA today | Beta, Preview or not yet available |
| --- | --- | --- |
| AI-SPM (Supported) | Cloud onboarding on AWS, Azure and GCP. Managed agent inventory for Copilot Studio, Microsoft 365 Agents, Azure AI Foundry, Bedrock AgentCore and Bedrock Agent. Browser plugin. Linux host scanning. | macOS host scanning: Beta. Desktop telemetry app: Beta. Windows host scanning: in progress. |
| Agentic AI Security (Supported) | ModelArmor runtime sandbox, built on KubeArmor. Managed agent visibility. | AgentZ: available since August 2026 [confirm label: GA or other]. AgentZ Coding workspace type: Preview. |
| AI-DR (Supported) | Detection from AWS CloudTrail, Azure Event Hub and GCP logging. Alerts, tickets and auto-remediation. | None. AI-DR reads control-plane events and does not block in the request path. Prompt Firewall and ModelArmor block. |
| Prompt Guardrails & AI Gateway (Supported, BETA) | Prompt Firewall on the browser extension, the gateway, LiteLLM and Bifrost. | AI Gateway [confirm label: Beta or Coming soon]. |
| Compliance and AI-GRC (Supported) | AIBOM in CycloneDX 1.6, from knoxctl, GitHub Actions and Azure DevOps. Compliance mapping for [confirm the AI frameworks live in the console]. | The dedicated AI-GRC module: coming soon. [Nat to confirm: this cell becomes BETA in the next matrix.] |
| Red Team + AI DAST (Supported, BETA) | LLM red teaming with scheduled scans and multi-turn attacks, mapped to OWASP LLM Top 10 and MITRE ATLAS. DAST with 4 scan types and recorded-login scans behind MFA. | AI DAST: coming soon. |
| Model, Dataset + AI-SAST (Supported, BETA) | Model file scans for Pickle, HDF5/H5, TensorFlow SavedModel, checkpoints and ONNX. A CI/CD gate for model scans. Opt-in AI analysis of SAST findings. | IDE-based AI SAST: coming soon. [Confirm GGUF, safetensors and dataset poisoning detection.] |
| AI & Agent Identity Security (Partial, BETA) | None as a module. | The dedicated AI Identity Security module: coming soon. AgentZ gives each agent a SPIFFE identity today. |

We can send a per-feature breakdown for the modules that matter most to your Guardian Agent review. Tell us which ones.

Best regards,
John

## Sources Opened for Every Claim in the Email

- The matrix PDF v3, pages 2, 3, 4, 6 and 7, from John's 13 Oct 2026 email. It holds the legend, the module benchmark, the scoring rule and the verification note.
- `docs/getting-started/ai-security-arch.md`. Six modules are GA. AI Identity Security and AI-GRC are on the roadmap.
- `docs/how-to/aiml-overview.md`, `docs/resources/glossary.md` and `docs/index.md`. Coming-soon labels.
- `docs/faqs/ai-security.md` and `docs/faqs/general.md`. The GA module list and FAQ 24 on datasets.
- `docs/getting-started/3.5-release.md`, `3.6-release.md` and `3.7-release.md`. Managed agents, xBOM, DAST scan types and the AI Gateway draft.
- `docs/support-matrix/compliance-matrix.md`. EU AI Act and ISO/IEC 42001 rows.
- `references/source-of-truth/ai-security-data-points.md`. Tier I status for host scanning, the desktop app, the AI Gateway and AI DAST.
- Firecrawl, 14 Oct 2026: the ML Static Scan, Red Teaming, AI-DR, Prompt Firewall, Shadow AI and xBOM pages on help.accuknox.com, the AgentZ product page and FAQ, the Agentic AI Security solution page, and the 2026 AI Security roadmap blog.
- Firecrawl, 14 Oct 2026: the Akto and Noma pages cited in the matrix. The Akto page matched its cell. The Noma page did not show CI/CD, see F6.
