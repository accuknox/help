---
title: CDR FAQs
description: Frequently asked questions about AccuKnox Cloud Detection and Response (CDR) - log ingestion, automated remediation, and threat mapping.
hide:
  - toc
---

# CDR (Cloud Detection & Response)

??? "**1. How does AccuKnox CDR collect security logs from cloud accounts?**"
    AccuKnox ingests audit logs **directly from cloud providers**, with a method tuned to each provider.

    - **AWS**: Push-based, through CloudTrail → S3 → ingestion.
    - **GCP / Azure**: Pull-based, through Pub/Sub or Event Hub subscriptions.

??? "**2. What is required to enable automated remediation?**"
    You need **GitHub Actions** and **admin-level cloud permissions**.

    - **GitHub Actions**: Remediation scripts run from your controlled repository.
    - **Cloud Permissions**: Admin-level access (AWS IAM admin, Azure Subscription Owner, GCP Owner) lets AccuKnox apply fixes.

??? "**3. How does AccuKnox map detected threats to remediation actions?**"
    AccuKnox links **each rule violation to a specific remediation script**.

    *Example:* A VM with a public IP triggers a script that removes the IP automatically.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
