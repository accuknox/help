---
title: Data Usage Policy
description: AccuKnox data handling, privacy, and AI usage policies.
---

# Data Usage Policy

## For SaaS Deployment

AccuKnox hosts and manages the security control plane.

* **Residency**: Metadata, logs, and findings stored in AccuKnox cloud.
* **Management**: AccuKnox handles maintenance and retention (default 60 days).
* **Security**: Encrypted at rest and in transit.
* **Deployment Regions**:
    * **US**: `app.accuknox.com`
    * **Europe**: `app.eu.accuknox.com`
    * **Middle East**: `app.me.accuknox.com`
    * **India**: `app.in.accuknox.com`

## For On-Prem Deployment

Customer retains full control; data resides in customer infrastructure.

* **Residency**: All data remains in customer environment.
* **Transmission**: No external transmission unless explicitly configured (e.g., SIEM, GenAI).
* **Responsibility**: Customer manages retention, storage, and backups.

!!! note "How Are Updates Fetched on Airgapped/On-Prem Env?"
    <ANSWER>

## Use of AI

Powered by **OpenAI GPT-4o** for AskAI, Remediation, and Copilot.

### Data Transmitted

Only context required for analysis is sent:

* **Asset Context**: Name, ID, Resource Type.
* **Findings Data**: Technical details of the alert/vulnerability.
* **Exclusions**: No PII, raw payloads, or unrelated database content.

### Governance

* **Default**: Disabled.
* **Activation**: Strict **Opt-In**. Contact **<support@accuknox.com>** to enable AskAI features.
