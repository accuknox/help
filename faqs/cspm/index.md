---
title: CSPM FAQs
description: Frequently asked questions about AccuKnox Cloud Security Posture Management (CSPM) - agentless scanning, onboarding, compliance, and cloud integration.
hide:
  - toc
---

# CSPM (Cloud Security Posture Management)

??? "**1. What does AccuKnox CSPM solve for my cloud security program?**"
    AccuKnox CSPM gives you a unified, multi-cloud view of cloud assets, misconfigurations, compliance gaps, and risk. It helps teams discover cloud resources, identify security and compliance issues, prioritize fixes, and track remediation from a single platform.

??? "**2. Which cloud providers does AccuKnox CSPM support?**"
    AccuKnox CSPM supports AWS, Azure, and GCP. It can onboard public cloud accounts using read-only access, scan cloud resources, and provide consistent posture reporting across all three major clouds.

??? "**3. What is the typical CSPM onboarding journey?**"
    The onboarding journey begins with cloud account registration, followed by permission validation, initial discovery scan, and then asset inventory and compliance dashboards. Once onboarding is complete, CSPM runs scheduled scans and updates findings, compliance scores, and drift detection continuously.

??? "**4. What prerequisites are required for AWS onboarding?**"
    For AWS, you need an IAM user with `ReadOnlyAccess` and `SecurityAudit` or equivalent permissions. This account is used only for discovery and posture scanning, and no changes are made to your cloud resources.

??? "**5. What are the CSPM prerequisites for Azure and GCP?**"
    Azure and GCP also require read-only service credentials with the least privileges needed for cloud asset discovery and posture checks. In GCP, this is typically a service account with a JSON private key, and in Azure a service principal with delegated read permissions.

??? "**6. Does AccuKnox CSPM require agents in the cloud accounts?**"
    No. For public cloud accounts, CSPM is agentless and uses cloud APIs to discover assets and configurations. Agent-based collection is only needed for private or behind-firewall environments where remote node access is required.

??? "**7. What cloud assets does CSPM discover and monitor?**"
    CSPM discovers hosts, applications, web APIs, containers, clusters, storage services, databases, IAM resources, and other cloud infrastructure components. It maintains an automated asset inventory that reflects additions and removals after each scan.

??? "**8. How does AccuKnox CSPM detect misconfigurations and drift?**"
    After onboarding, AccuKnox performs scheduled scans against your cloud resources and compares current configurations to compliance baselines. It detects drift when a resource deviates from the expected secure configuration and tracks that as a misconfiguration finding.

??? "**9. Which compliance frameworks and modules does CSPM support?**"
    CSPM supports 30+ compliance programs including CIS Benchmarks, PCI DSS, HIPAA, GDPR, SOC 2, ISO 27001, NIST, FedRAMP, and more. The platform includes compliance reporting, detailed findings, and mapping of misconfigurations to framework controls.

??? "**10. Can I integrate CSPM findings with ticketing or ITSM tools?**"
    Yes. AccuKnox CSPM integrates with ticketing systems and ITSM workflows so you can auto-create, update, and manage remediation tickets from findings. Supported integrations include Jira, Freshservice, ConnectWise, and other connectors under CSPM integrations.

??? "**11. How do I map CSPM findings into Jira, Freshservice, or ConnectWise?**"
    In the CSPM channel integration page, create a connector, provide your service credentials, configure the project or service queue, and map priorities or issue types. Once enabled, findings can automatically generate tickets and keep remediation work tracked.

??? "**12. How often are cloud scans and inventory updates performed?**"
    CSPM runs periodic scans after onboarding and refreshes asset inventory on a regular schedule. This ensures cloud asset counts and compliance posture remain accurate as your environment changes.

??? "**13. What are the recommended first steps after my first CSPM scan completes?**"
    Review the asset inventory, open the cloud misconfiguration dashboard, inspect high-risk findings, and validate compliance scores. Then prioritize remediation tickets, configure drift monitoring for critical assets, and enable reports for stakeholders.

??? "**14. How can I verify my cloud account onboarding was successful?**"
    Successful onboarding is confirmed when your cloud account appears in the inventory, initial assets are discovered, and CSPM scans report findings. You can also verify by checking the compliance summary and asset discovery pages for the new account.

??? "**15. Where can I find CSPM troubleshooting and support documentation?**"
    Use the AccuKnox CSPM troubleshooting guide, cloud onboarding prerequisite pages, and the CSPM use-case documentation for asset inventory, misconfigurations, and compliance. These resources explain setup steps, common prerequisites, and guidance for resolving onboarding or scan issues.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
