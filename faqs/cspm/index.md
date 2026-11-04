---
title: CSPM FAQs
description: Frequently asked questions about AccuKnox Cloud Security Posture Management (CSPM) - agentless scanning, onboarding, compliance, and cloud integration.
hide:
  - toc
---

# CSPM (Cloud Security Posture Management)

??? "**1. What does AccuKnox CSPM solve for my cloud security program?**"
    AccuKnox CSPM gives you **one multi-cloud view** of cloud assets, misconfigurations, compliance gaps and risk. From a single platform, your teams can:

    - **Discover**: Find cloud resources.
    - **Identify**: Spot security and compliance issues.
    - **Prioritize**: Rank the fixes.
    - **Track**: Follow remediation to completion.

??? "**2. Which cloud providers does AccuKnox CSPM support?**"
    AccuKnox CSPM supports **AWS, Azure and GCP**. It onboards public cloud accounts with read-only access and scans cloud resources. It gives consistent posture reporting across all three clouds.

??? "**3. What is the typical CSPM onboarding journey?**"
    Onboarding takes **four steps**, then CSPM runs on its own.

    1. Register the cloud account.
    2. Validate the permissions.
    3. Run the initial discovery scan.
    4. Review the asset inventory and compliance dashboards.

    After onboarding, CSPM runs scheduled scans. It updates findings, compliance scores and drift detection continuously.

??? "**4. What prerequisites are required for AWS onboarding?**"
    You need an **IAM user with `ReadOnlyAccess` and `SecurityAudit`** or equivalent permissions. AccuKnox uses this account only for discovery and posture scanning. It makes no changes to your cloud resources.

??? "**5. What are the CSPM prerequisites for Azure and GCP?**"
    Both need **read-only service credentials** with the least privileges for asset discovery and posture checks.

    - **GCP**: Typically a service account with a JSON private key.
    - **Azure**: A service principal with delegated read permissions.

??? "**6. Does AccuKnox CSPM require agents in the cloud accounts?**"
    No. For public cloud accounts, **CSPM is agentless**. It uses cloud APIs to discover assets and configurations. You need agent-based collection only for private or behind-firewall environments that require remote node access.

??? "**7. What cloud assets does CSPM discover and monitor?**"
    CSPM discovers these **cloud asset types**:

    - **Compute**: Hosts, containers and clusters.
    - **Applications**: Applications and web APIs.
    - **Data**: Storage services and databases.
    - **Identity**: IAM resources.
    - **Other**: Other cloud infrastructure components.

    CSPM keeps an automated asset inventory. Each scan adds new assets and removes deleted ones.

??? "**8. How does AccuKnox CSPM detect misconfigurations and drift?**"
    AccuKnox runs **scheduled scans** and compares current configurations to compliance baselines. When a resource deviates from the expected secure configuration, AccuKnox flags drift. It tracks that drift as a misconfiguration finding.

??? "**9. Which compliance frameworks and modules does CSPM support?**"
    CSPM supports **30+ compliance programs**, including CIS Benchmarks, PCI DSS, HIPAA, GDPR, SOC 2, ISO 27001, NIST, FedRAMP and more. The platform gives you:

    - **Reports**: Compliance reporting.
    - **Findings**: Detailed findings.
    - **Mapping**: Misconfigurations mapped to framework controls.

??? "**10. Can I integrate CSPM findings with ticketing or ITSM tools?**"
    Yes. AccuKnox CSPM integrates with **ticketing systems and ITSM workflows**. You can auto-create, update and manage remediation tickets from findings. Supported integrations include Jira, Freshservice, ConnectWise and other connectors under CSPM integrations.

??? "**11. How do I map CSPM findings into Jira, Freshservice, or ConnectWise?**"
    Set it up on the **CSPM channel integration page**.

    1. Create a connector.
    2. Enter your service credentials.
    3. Configure the project or service queue.
    4. Map priorities or issue types.

    After you enable the connector, findings can create tickets automatically and keep remediation work tracked.

??? "**12. How often are cloud scans and inventory updates performed?**"
    CSPM runs **periodic scans** after onboarding and refreshes the asset inventory on a regular schedule. This keeps asset counts and compliance posture accurate as your environment changes.

??? "**13. What are the recommended first steps after my first CSPM scan completes?**"
    Start with the **asset inventory**, then work through the findings.

    1. Review the asset inventory.
    2. Open the cloud misconfiguration dashboard.
    3. Inspect high-risk findings.
    4. Validate compliance scores.
    5. Prioritize remediation tickets.
    6. Configure drift monitoring for critical assets.
    7. Enable reports for stakeholders.

??? "**14. How can I verify my cloud account onboarding was successful?**"
    Onboarding succeeded when **three things are true**:

    - **Inventory**: Your cloud account appears in the inventory.
    - **Discovery**: CSPM discovers the initial assets.
    - **Findings**: CSPM scans report findings.

    You can also check the compliance summary and asset discovery pages for the new account.

??? "**15. Where can I find CSPM troubleshooting and support documentation?**"
    Use these **AccuKnox CSPM resources**:

    - **Troubleshooting guide**: Guidance for resolving onboarding or scan issues.
    - **Cloud onboarding prerequisite pages**: Setup steps and common prerequisites.
    - **CSPM use-case documentation**: Asset inventory, misconfigurations and compliance.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
