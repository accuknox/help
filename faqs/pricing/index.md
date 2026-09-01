---
title: Pricing & Billing FAQs
description: Frequently asked questions about AccuKnox licensing model, billing, asset counts, and pricing for CNAPP modules.
hide:
  - toc
---

# Pricing & Billing

??? "**1. What is AccuKnox's licensing model?**"
    You can get a custom quote and select individual security modules based on number of units (CWPP nodes, CSPM cloud assets, etc) or a comprehensive CNAPP bundle. AccuKnox offers a flexible licensing approach tailored to customer needs. It's not a one-size-fits-all model.

    Customers have the flexibility to purchase specific modules such as KSPM, CSPM, ASPM, or CWPP independently.
    Pricing is modular and typically based on:
    - Number of cloud assets normalized to units
    - Number of container images
    - Number of worker nodes
    - Number of Tools in SCA, SAST, DAST, IaC
    - Number of AI/LLM Model
    - Bundle of per 1000 APIs
    Customers only pay for the modules they choose.

??? "**2. How would I know what assets are included for billing?**"
    <a href="https://help.accuknox.com/resources/count-assets/" target="_blank">Count your assets here.</a>
    AWS: EC2 instances, S3 buckets, RDS databases
    Azure: Virtual Machines, Storage Accounts, SQL Databases
    GCP: Compute Engine VMs, Cloud Storage buckets, Cloud SQL instances

    To estimate billing, AccuKnox normalizes assets into units, refer the question above for details.

??? "**3. What happens if we exceed the asset count for a few days or weeks within a month?**"
    The AccuKnox Control Plane will not stop you from exceeding the quota. However, if the quota consistently exceeds by more than 30% over a longer period, the AccuKnox support team will reach out for clarifications.

??? "**4. We have thousands of unused container images in our registry. Would they all be scanned?**"
    During onboarding, you can apply filters to control which images get scanned:
    - Use inclusion/exclusion regex for `repo/image:tag`.
    - Configure to scan only images updated in the last **X days** or pulled within the last **Y days**.
    - AccuKnox will notify you if the container image count exceeds 5000.
    Additionally, AccuKnox supports scanning images **in Kubernetes clusters or virtual machines directly**, ensuring only runtime images are scanned. This reduces both the number of images scanned and findings noise.

??? "**5. How is licensing handled in SaaS and on-prem environments?**"
    + Licensing is generally **subscription-based** for both SaaS and on-prem.
    + On-prem customers are expected to procure **Platinum Support**.

??? "**6. Who to reach out to for a custom quote for CNAPP?**"
    You can reach out to:
    - Sales Q's - info@accuknox.com
    - Technical Q's - support@accuknox.com

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
