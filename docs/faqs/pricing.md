---
title: Pricing & Billing FAQs
description: Frequently asked questions about AccuKnox licensing model, billing, asset counts, and pricing for CNAPP modules.
hide:
  - toc
---

# Pricing & Billing

??? "**1. What is AccuKnox's licensing model?**"
    AccuKnox licensing is **modular and custom-quoted**. You buy individual security modules by number of units (CWPP nodes, CSPM cloud assets, etc.). Or you buy a full CNAPP bundle.

    You can buy modules such as KSPM, CSPM, ASPM or CWPP independently. Pricing is typically based on:

    - **Cloud assets**: Number of cloud assets normalized to units.
    - **Container images**: Number of container images.
    - **Worker nodes**: Number of worker nodes.
    - **AppSec tools**: Number of tools in SCA, SAST, DAST and IaC.
    - **AI/LLM models**: Number of AI/LLM models.
    - **APIs**: Bundles of 1000 APIs.

    You pay only for the modules you choose.

??? "**2. How would I know what assets are included for billing?**"
    Use the <a href="https://help.accuknox.com/resources/count-assets/" target="_blank">asset counting guide</a> to count your assets. Billable assets include:

    - **AWS**: EC2 instances, S3 buckets, RDS databases.
    - **Azure**: Virtual Machines, Storage Accounts, SQL Databases.
    - **GCP**: Compute Engine VMs, Cloud Storage buckets, Cloud SQL instances.

    AccuKnox **normalizes assets into units** to estimate billing. See the question above for details.

??? "**3. What happens if we exceed the asset count for a few days or weeks within a month?**"
    Nothing happens right away. The AccuKnox Control Plane **does not block usage above the quota**. If usage stays more than 30% over the quota for a longer period, the AccuKnox support team contacts you for clarification.

??? "**4. We have thousands of unused container images in our registry. Would they all be scanned?**"
    No, not if you filter them. During onboarding, you **control which images AccuKnox scans**:

    - **Regex filters**: Use inclusion or exclusion regex for `repo/image:tag`.
    - **Age filters**: Scan only images updated in the last **X days** or pulled within the last **Y days**.
    - **Count alerts**: AccuKnox notifies you if the container image count exceeds 5000.

    AccuKnox also scans images **in Kubernetes clusters or virtual machines directly**, so it scans only runtime images. This cuts the number of images scanned and the findings noise.

??? "**5. How is licensing handled in SaaS and on-prem environments?**"
    Licensing is generally **subscription-based** for both SaaS and on-prem. On-prem customers are expected to buy **Platinum Support**.

??? "**6. Who to reach out to for a custom quote for CNAPP?**"
    Email the AccuKnox team:

    - **Sales questions**: info@accuknox.com
    - **Technical questions**: support@accuknox.com

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
