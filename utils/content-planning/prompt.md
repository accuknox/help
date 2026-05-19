Here is the refined prompt:

---

## Objective

Create a comprehensive, fully sourced stack ranking comparison between **AccuKnox** and **Red Hat Advanced Cluster Security (RHACS) for Kubernetes** in Excel (.xlsx) format, modeled after the existing AccuKnox comparison file in this directory.

This comparison will be used in a Nutanix sales engagement. The goal is to write the "question paper" such that AccuKnox scores 100/100 and RHACS scores below 60/100 — based on real, verifiable capabilities, not marketing claims. Make sure you do three runs, grounding, review, evidence collection, and scoring in each run, to ensure accuracy and completeness. There is enough reference content in this repo + online just scan things well.

---

## Step 1 — Research Phase (Do This First, Before Any Output)

### 1a. Red Hat ACS Deep Dive
- Scrape and thoroughly read: https://www.redhat.com/en/technologies/cloud-computing/openshift/advanced-cluster-security-kubernetes
- Follow and scrape all linked sub-pages (features, architecture, integrations, compliance, pricing/deployment, docs)
- Build a complete, sourced list of every capability RHACS claims — anchored to URLs

### 1b. AccuKnox Capability Extraction
Pull AccuKnox capabilities from these sources (all located relative to this directory):
- **utils/REF RFPs folder** — H&M, CNA, SABIC, Rakuten (if available), NSA Kubernetes Hardening Guide responses
- **docs/ (under this use case folder or integrations folder or getting started folder)** folder — use case docs, integration docs, support matrix
- **utils/PDFs/** folder — reference content and security collateral
- **Existing comparison file - `MAIN COMPARISON AccuKnox Container _ K8s Security.xlsx` ** — in the same directory as this file (use as the structural template) IMPORTANT: do not assume the existing content is fully accurate or comprehensive — verify every claim and add any missing capabilities surfaced from the above sources

> **Base URL for AccuKnox Help Docs:** All `docs/` content is published at **https://help.accuknox.com**. To resolve the live URL for any file under `docs/`, consult `mkdocs.yml` (in the repo root) for the full nav/sitemap — the path mappings there tell you exactly which URL each `.md` file corresponds to under `https://help.accuknox.com`. Use these resolved URLs as the source citations for every AccuKnox claim derived from the help docs.

> Do not fabricate capabilities. Every AccuKnox claim must be traceable to one of the above sources or a public URL.

---

## Step 2 — Comparison Categories

Organize all features into the following logical buckets (add sub-rows within each as needed):

| # | Category |
|---|----------|
| 1 | **Discovery** — asset discovery, workload visibility, SBOM, runtime inventory |
| 2 | **Risk Assessment & Prioritization** — CVE scoring, blast radius, exploitability, risk ranking |
| 3 | **Remediation Recommendations** — guided fixes, policy-driven remediation, ticketing integrations |
| 4 | **Enforcement** — admission control, runtime blocking, network policy enforcement, eBPF-based controls |
| 5 | **Continuous Compliance** — drift detection, policy-as-code, audit logging |
| 6 | **Compliance Templates** — CIS Benchmarks, NIST, PCI-DSS, SOC2, HIPAA, NSA Kubernetes Hardening, FedRAMP |
| 7 | **Deployment Models — Public Cloud** — AWS, GCP, Azure managed support |
| 8 | **Deployment Models — Private Cloud** — on-prem, bare metal |
| 9 | **Deployment Models — SaaS** — fully managed SaaS offering |
| 10 | **Deployment Models — Edge / IoT** — lightweight agent, resource-constrained nodes |
| 11 | **Deployment Models — Air-Gapped** — offline/disconnected environments |
| 12 | *(Additional categories surfaced from RFP review — H&M, CNA, SABIC, NSA, etc.)* |

---

## Step 3 — Scoring & Grounding Rules

For each feature row:
- **Score AccuKnox and RHACS** (e.g., Full / Partial / None, or 0–3 scale — match the existing file's convention)
- **Cite a source** for every claim — URL, RFP document name + section, or help doc path
- **Do not score a capability as "Full" without a verifiable source**
- Run at minimum **two passes** of verification: first pass builds the table, second pass cross-checks every RHACS claim against their actual docs and every AccuKnox claim against internal sources

---

## Step 4 — Deliverable

Produce a single **Excel (.xlsx) file** with:
- Executive Summary — top-level category scores, visual scoring summary
- detailed feature-level rows
- All URLs and document references cited throughout

Model the structure exactly on the existing AccuKnox comparison .xlsx in this directory. Do not create a new layout from scratch — extend and fill the existing one. Okay if you replace or improve the existing content, but maintain the same overall format and structure.

---

## Constraints

- Primary focus: **Kubernetes / container / cluster security**
- Secondary coverage: deployment flexibility (models in Step 2, items 7–11)
- No false claims — if a capability is unclear or unverifiable, mark it as "Unverified" rather than asserting it
- All RHACS claims must be backed by publicly accessible URLs
- All AccuKnox claims must be backed by RFP responses, help docs, or PDFs in this repo