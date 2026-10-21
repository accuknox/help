---
title: Deployment & Architecture FAQs
description: Frequently asked questions about AccuKnox deployment architecture, on-premise setup, air-gapped environments, distributed architecture, and regional availability.
hide:
  - toc
---

# Deployment & Architecture

??? "**1. What is the deployment architecture?**"
    AccuKnox offers **four deployment models**. Pick the one that fits your operational and security needs.

    - **AccuKnox SaaS**: AccuKnox runs the platform and manages upgrades and maintenance. It scales and deploys quickly.
    - **AccuKnox Managed OEM/MSSP**: AccuKnox handles upgrades and maintenance for partners in managed deployments.
    - **AWS On-prem (Hybrid)**: This hybrid model combines AWS cloud services with on-premises deployments.
    - **Full On-premises or Air-gapped**: This model gives maximum security and isolation for sensitive and highly regulated industries.

    The on-premises deployment uses a **Kubernetes-native architecture**. Microservices and databases such as PostgreSQL and MongoDB manage the API logic and data.

    AccuKnox uses both agentless and agent-based security across environments:

    - **Agentless Security**: AccuKnox scans public cloud infrastructure through APIs for SaaS-based usage.
    - **Agent-Based Security**: AccuKnox protects workloads with agents.
        - **For Kubernetes**: The platform deploys as a Daemonset.
        - **For Containers and VMs**: AccuKnox deploys in Systemd mode.
        - **On-Premises Infrastructure**: You install the solution in on-premises or data center deployments with Helm charts.

??? "**2. How AccuKnox helps achieve protection for Edge, 5G workloads?**"
    AccuKnox brings its core runtime capabilities to **Edge and 5G environments**.

    - **Zero Trust on Kubernetes and VMs**: The platform extends its Zero Trust model to VMs and Kubernetes at the edge.
    - **Real-time Enforcement**: AccuKnox gives preemptive, prevention-based security for 5G control planes. It also shows a unified view of application behavior and communication patterns in 5G networks.
    - **Lightweight Agent**: The low-footprint runtime agent comes from the open-source project [KubeArmor](https://github.com/kubearmor/KubeArmor). It uses eBPF and Linux Security Modules (LSM) to enforce only the necessary access and behavior rules. Enforcement runs at the OS level, even in isolated environments.
    - **Policy & Testing for 5G**: AccuKnox has tools to create policies for xApp/RIC, certify security for CNF/ORAN parts, and simulate attacks on 5G networks.

??? "**3. What happens if the AccuKnox Control Plane goes down? Will runtime protection still work?**"
    Yes. **Runtime enforcement continues** when the Control Plane is unavailable. A Control Plane outage does not affect your Data Plane or production operations.

??? "**4. Can AccuKnox be deployed in a distributed architecture?**"
    Yes. AccuKnox can deploy its Control Plane across multiple regions for redundancy and disaster recovery.

    - **Method**: The deployment uses native Kubernetes concepts.
    - **Scope**: Nodes can span multiple Availability Zones (AZs) and regions.
    - **Requirement**: You need reliable network bandwidth between AZs and regions.

??? "**5. Can AccuKnox reuse existing infrastructure (e.g., NAT, firewalls) during on-prem deployment of the Control Plane?**"
    AccuKnox needs an **independent Kubernetes cluster** for the Control Plane. We strongly recommend that you do not use an existing cluster that runs customer applications.

??? "**6. Does AccuKnox integrate with virtualization platforms such as VMware or Hyper-V?**"
    No. AccuKnox does not integrate directly with VMware, Hyper-V, KVM or Nutanix AHV. Instead, AccuKnox **secures the VMs you create on these platforms**.

    - **Agentless**: AccuKnox scans VMs through snapshots.
    - **Agent-based**: AccuKnox scans VMs with lightweight scanning agents.

??? "**7. What is the typical timeline for a Proof of Concept (PoC)?**"
    A typical Proof of Concept (PoC) takes **1 to 3 weeks**, based on the deployment type.

    - **SaaS PoC**: About 1 to 2 weeks, because the infrastructure is already in place.
    - **On-Prem PoC**: About 2 to 3 weeks, based on environment complexity and readiness.
    - **Air-gapped On-Prem**: This needs additional time to stage container images.

    *Note:* When all prerequisites are ready, some on-prem deployments finished in just a few hours.

    - [On-Premise Installation Guide](https://help.accuknox.com/getting-started/on-prem-installation-guide/)
    - [POC Checklist Questionnaire](https://docs.google.com/spreadsheets/d/129ZEMzo7oaKRyifprFFRXLf4J6lE7XypBj7Vp9PdXWU/edit?usp=sharing)

??? "**8. For on-prem deployment of AccuKnox Control Plane, what are the challenges/considerations?**"
    AccuKnox runs in fully isolated environments, but **you take on four tasks** that AccuKnox handles in SaaS.

    - **Vulnerability Database Updates**: SaaS gets updates twice daily. In isolated deployments, you configure automated pipelines to push updates.
    - **Container Images**: You stage the required container images in your private registry. AccuKnox gives you the image list and instructions.
    - **Monitoring & Alerts**: In SaaS, AccuKnox SRE practices give automated monitoring and notifications. In isolated setups, you need equivalent procedures.
    - **Backups**: You configure backup and snapshot procedures, with support from AccuKnox SRE/DevOps.

??? "**9. Does AccuKnox support backup and auditing in isolated deployments?**"
    Yes. You configure **backup and snapshot procedures** with AccuKnox SRE/DevOps. In isolated deployments, you set up monitoring and audit workflows. AccuKnox gives guidance and support.

??? "**10. In which regions is AccuKnox deployed in?**"
    AccuKnox runs in **four regions**:

    - **US (Americas)**: [app.accuknox.com](https://app.accuknox.com)
    - **Europe**: [app.eu.accuknox.com](https://app.eu.accuknox.com)
    - **Middle East**: [app.me.accuknox.com](https://app.me.accuknox.com)
    - **India**: [app.in.accuknox.com](https://app.in.accuknox.com)

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
