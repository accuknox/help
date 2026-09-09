---
title: CDR FAQs
description: Frequently asked questions about AccuKnox Cloud Detection and Response (CDR) - log ingestion, automated remediation, and threat mapping.
hide:
  - toc
---

# CDR (Cloud Detection & Response)

??? "**1. How does AccuKnox CDR collect security logs from cloud accounts?**"
    AccuKnox ingests audit logs directly from cloud providers using provider-optimized methods:
    - **AWS**: Push-based via CloudTrail → S3 → ingestion.
    - **GCP / Azure**: Pull-based via Pub/Sub or Event Hub subscriptions.

??? "**2. What is required to enable automated remediation?**"
    - **GitHub Actions**: Remediation scripts run from your controlled repository.
    - **Cloud Permissions**: Admin-level access (AWS IAM admin, Azure Subscription Owner, GCP Owner) to apply fixes.

??? "**3. How does AccuKnox map detected threats to remediation actions?**"
    Each rule violation is linked to a specific remediation script.
    *Example:* A VM with a public IP triggers a script that removes the IP automatically.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
