---
title: AI SAST, Product Notes
updated: 2026-09-26
tier: A unless a row says otherwise
---

# AI SAST

AI SAST puts code security recommendations in the developer's IDE and in the CI/CD pipeline, before
and after a commit. The AI value is a contextual, probabilistic fix recommendation for each finding.
A pattern match alone does not give that. Tier A.

## Public Docs Already Cover AI Analysis of SAST Findings

These facts are tier D and can ship anywhere today.

- Opt-in AI analysis of SAST findings marks false positives and assesses severity. Anthropic powers
  it. Source: `docs/getting-started/3.4-release.md`.
- An "AI Enabled SAST" option in the scan-type selector adds AI analysis on top of the static scan.
  Source: `docs/getting-started/3.7-release.md`.

The website nav already lists "AI-Accelerated SAST Scanning" under Secure Code, but the link points
to `accuknox.com/#`. A page for it does not exist yet.

## The IDE Comes First, Then the Pipeline

| Surface | Status | Notes |
| --- | --- | --- |
| IDE plugins | The first delivery target | Recommendations appear while the developer writes code. [confirm the supported IDEs] |
| CI/CD pipeline | Supported | Builds on the existing AccuKnox SAST pipeline integrations |
| Auto PR decorator | In development | Annotates a pull request with AI security context and a fix suggestion |
| Cloud-based development environments | Not a target | All value lands in the local environment and the pipeline |

The AccuKnox AI Gateway is the model routing layer under AI SAST. No third-party gateway sits in
that path. Tier A.

## Black Duck Is the Competitive Anchor

AccuKnox positions AI SAST against two Black Duck products. Tier A. Confirm the Black Duck claims
against a Black Duck source before a comparison page uses them.

| Black Duck product | What it does, as the product team described it |
| --- | --- |
| Signal | Real-time, as-you-type security recommendations, with no commit required |
| Context AI | Fix recommendations enriched with 20+ years of manual remediation data |

AI SAST targets the same space, inline IDE recommendations plus pipeline integration, native to the
AccuKnox CNAPP.

## False Positives Are the Known Limit

The first release will raise some false positives. The team is reducing that noise, and the
recommendations get narrower as the model gets more context. Tell the buyer this before the pilot,
because a buyer who finds it alone loses trust in the rest of the demo. Tier A.

## Four Lines Answer the AE Questions on AI SAST

- Lead with "shift-left AI security in your IDE and pipeline, so issues get caught before they reach
  a pull request."
- Competitive anchor. "Similar to what Black Duck does with Context AI, but native to your CNAPP."
- State the caveat. False positive reduction is in progress.
- Upsell. AI SAST plus AI DAST covers the AppSec lifecycle, from pre-commit to a runtime pentest.
