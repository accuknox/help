---
title: KSPM FAQs
description: Frequently asked questions about AccuKnox Kubernetes Security Posture Management (KSPM) - asset discovery, compliance automation, and CI/CD integration.
hide:
  - toc
---

# KSPM (Kubernetes Security Posture Management)

??? "**1. How does AccuKnox KSPM discover and monitor Kubernetes assets?**"
    AccuKnox **continuously maps** clusters, namespaces, nodes, pods, and services across hybrid and multi-cloud.

    - **Visibility**: Real-time visibility into all mapped assets.
    - **Attack paths**: Attack-path analysis across those assets.
    - **Unauthorized deployments**: Detection of unauthorized deployments.

??? "**2. How does KSPM automate compliance checks?**"
    AccuKnox runs **continuous scans** against three benchmark sets, and supports custom policies for organization-specific governance.

    - **CIS Benchmarks**
    - **NSA/CISA guidance**
    - **MITRE ATT&CK mappings**

??? "**3. How does KSPM integrate into CI/CD to secure workloads pre-deployment?**"
    AccuKnox scans for **misconfigurations and CVEs before deployment**, and enforces RBAC and IaC security controls.

    It scans these artifacts:

    - **Kubernetes manifests**
    - **Helm charts**
    - **Terraform files**
    - **Container images**

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
