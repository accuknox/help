---
title: AI-BOM, Product Notes
updated: 2026-09-26
tier: A unless a row says otherwise
---

# AI-BOM

AI-BOM, the AI Bill of Materials, is a structured inventory of AI and ML assets. It lists models,
frameworks, dependencies and the risks attached to each one. It extends the AccuKnox XBOM framework,
which already covers SBOM, CBOM, HBOM and QBOM. Tier A. The Shadow AI coverage sheet adds that the
AI asset inventory exports as an AI-BOM in CycloneDX format. Tier I.

Tier D today. AIBOM in the repo and model scans in CI/CD are documented in
`docs/getting-started/xbom-setup.md` and `docs/how-to/model-scan-cicd.md`. The public
`/platform` page lists AI-BOM under Supply Chain, and a Top 3 Indian public sector bank case study
shows AI-BOM in an air-gapped deployment.

## Two Ingestion Paths Keep Onboarding Simple

1. **Auto-generation from cloud onboarding.** When a cloud connector onboards an AI or ML asset,
   the AI-BOM generates automatically or on selection. This matches how a repo already produces an
   SBOM for containers and SCA.
2. **Manual upload.** The customer uploads an AI-BOM artifact that already exists. This matches the
   existing SBOM upload.

## Hosted Models Get Scanned on Their Own Host

For a model on an external endpoint, such as a Hugging Face mirror or an internal model server, the
customer installs the [confirm the binary name, heard as "Knox Kettle"] binary on that host. The
customer sets the login and the path and points the binary at the model. The scan runs locally and
pushes results to the AccuKnox SaaS console. This covers legacy and on-premises models. Tier A.

## Registry Gating Comes Later

A pre-push workflow will generate the AI-BOM and run security checks before a model enters the
model registry. Workflows will branch on the scan result. This is not in the first release.
Tier A.

## Three Lines Answer the AE Questions on AI-BOM

- Lead with "know exactly which AI models and dependencies run in your environment, before they
  become a risk."
- Two paths. Auto-generate from cloud onboarding, or upload the AI-BOM you already have.
- The hosted-model scanner answers "what about our on-premises or self-hosted models?"
