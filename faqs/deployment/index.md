---
title: Deployment & Architecture FAQs
description: Frequently asked questions about AccuKnox deployment architecture, on-premise setup, air-gapped environments, distributed architecture, and regional availability.
hide:
  - toc
---

# Deployment & Architecture

??? "**1. What is the deployment architecture?**"
    AccuKnox's platform can be deployed in several flexible ways to suit different operational and security requirements:

    - **AccuKnox SaaS**: This model offers a scalable, easy-to-use, and quick deployment experience, with upgrades and maintenance managed by AccuKnox.
    - **AccuKnox Managed OEM/MSSP**: Designed for managed deployments where AccuKnox handles upgrades and maintenance for partners.
    - **AWS On-prem (Hybrid)**: This is a hybrid solution that combines cloud services from AWS with on-premises deployments.
    - **Full On-premises or Air-gapped**: Provides maximum security and isolation, making it suitable for sensitive and highly regulated industries.

    The on-premises deployment is based on a Kubernetes-native architecture, utilizing microservices and databases like PostgreSQL and MongoDB to manage API logic and data.

    AccuKnox utilizes both agent-based and agentless approaches to provide comprehensive security across different environments:

    - **Agentless Security**: For public cloud infrastructure security, AccuKnox operates in an agentless mode, using API scans for SaaS-based usage.
    - **Agent-Based Security**: AccuKnox also offers robust agent-based protection for workloads:
        - **For Kubernetes**: The platform uses a Daemonset for Kubernetes deployments.
        - **For Containers and VMs**: AccuKnox leverages a Systemd mode for deployment on containers and virtual machines.
        - **On-Premises Infrastructure**: For on-premises or data center deployments, the solution can be installed using Helm charts.

??? "**2. How AccuKnox helps achieve protection for Edge, 5G workloads?**"
    AccuKnox addresses the unique security challenges of Edge and 5G environments by leveraging its core capabilities:

    - **Zero Trust on Kubernetes and VMs**: The platform extends its Zero Trust security model to virtual machines and Kubernetes at the edge.
    - **Real-time Enforcement**: Offers preemptive, prevention-based security for 5G control planes. The platform provides a unified view of application behavior and communication patterns in 5G networks.
    - **Lightweight Agent**: Uses a low-footprint runtime protection agent (from the open-source project [KubeArmor](https://github.com/kubearmor/KubeArmor)), leveraging eBPF and Linux Security Modules (LSM) to ensure that only necessary access and behavior rules are enforced at the OS level, even in isolated environments.
    - **Policy & Testing for 5G**: Provides tools for creating policies for xApp/RIC, certifying security for CNF/ORAN parts, and simulating attacks for 5G networks.

??? "**3. What happens if the AccuKnox Control Plane goes down? Will runtime protection still work?**"
    Yes. Runtime security enforcement continues even if the Control Plane is unavailable. The availability of the Control Plane does not impact the customer's Data Plane or production operations.

??? "**4. Can AccuKnox be deployed in a distributed architecture?**"
    Yes. AccuKnox can deploy its Control Plane across multiple regions to achieve redundancy and disaster recovery.

    + Uses **native Kubernetes concepts** for distributed deployment.
    + Nodes can span multiple Availability Zones (AZs) and regions.
    + **Requirement:** Reliable network bandwidth between AZs/regions.

??? "**5. Can AccuKnox reuse existing infrastructure (e.g., NAT, firewalls) during on-prem deployment of the Control Plane?**"
    AccuKnox requires an **independent Kubernetes cluster** for deployment. We strongly recommend **not** using an existing cluster running customer applications.

??? "**6. Does AccuKnox integrate with virtualization platforms such as VMware or Hyper-V?**"
    AccuKnox does not integrate directly with virtualization platforms (VMware, Hyper-V, KVM, Nutanix AHV).

    + Instead, AccuKnox secures VMs created on these platforms.
    + Security is provided either **agentlessly (via snapshots)** or through **lightweight scanning agents**.

??? "**7. What is the typical timeline for a Proof of Concept (PoC)?**"
    Typical Proof of Concept (PoC) timelines are:
    * **SaaS PoC:** ~1–2 weeks (infrastructure already in place).
    * **On-Prem PoC:** ~2–3 weeks (depends on environment complexity and readiness).
    * **Air-gapped On-Prem:** Additional time required for staging container images.

    *Note:* In some cases where prerequisites are fully prepared, on-prem deployment has been completed in just a few hours.

    * [On-Prem Installation Guide](https://help.accuknox.com/getting-started/on-prem-installation-guide/)
    * [POC Checklist Questionnaire](https://docs.google.com/spreadsheets/d/129ZEMzo7oaKRyifprFFRXLf4J6lE7XypBj7Vp9PdXWU/edit?usp=sharing)

??? "**8. For on-prem deployment of AccuKnox Control Plane, what are the challenges/considerations?**"
    AccuKnox supports deployment in completely isolated environments, but some considerations apply:

    - **Vulnerability Database Updates**:
      In SaaS environments, updates are applied twice daily. In isolated deployments, customers must configure automated pipelines to push updates.

    - **Container Images**:
      Customers must stage required container images in their private registry. AccuKnox provides the image list and instructions.

    - **Monitoring & Alerts**:
      In SaaS, AccuKnox SRE practices provide automated monitoring and notifications. In isolated setups, customers need equivalent procedures.

    - **Backups**:
      Customers must configure backup/snapshot procedures, supported by AccuKnox SRE/DevOps.

??? "**9. Does AccuKnox support backup and auditing in isolated deployments?**"
    Yes. Customers should configure **backup and snapshot procedures** in coordination with AccuKnox SRE/DevOps. In isolated deployments, customers are responsible for setting up monitoring and audit workflows, while AccuKnox provides guidance and support.

??? "**10. In which regions is AccuKnox deployed in?**"
    AccuKnox is deployed in the following regions:

    - **US (Americas)**: [app.accuknox.com](https://app.accuknox.com)
    - **Europe**: [app.eu.accuknox.com](https://app.eu.accuknox.com)
    - **Middle East**: [app.me.accuknox.com](https://app.me.accuknox.com)
    - **India**: [app.in.accuknox.com](https://app.in.accuknox.com)

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
