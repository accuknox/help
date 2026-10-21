---
title: Policy Management & Enforcement FAQs
description: Frequently asked questions about AccuKnox policy management, zero trust, microsegmentation, auto-discovered policies, and hardening.
hide:
  - toc
---

# Policy Management & Enforcement

??? "**1. How AccuKnox helps in Policy Version Control for Runtime Security?**"
    AccuKnox lets DevSecOps teams embed **security policies as code** in their GitOps workflow. Teams get a unified, collaborative view of the policies. The policies ship and deploy with the applications they protect.

    GitOps-based policy version control gives you:

    - **Change enforcement**: Enforce policy changes easily.
    - **Version tracking**: Keep track of versions for audit or rollback.
    - **Approvals**: Use approval mechanisms for policy changes.

??? "**2. How AccuKnox helps to achieve Microsegmentation?**"
    AccuKnox CWPP gives **micro-segmentation at the pod level**. The pod is the smallest execution unit in Kubernetes and the lowest possible granularity level.

    AccuKnox helps you identify what each pod does:

    - **Processes**: The process execution requests from the pods.
    - **Network**: The internal and external network connections the pods try to make.
    - **Files**: The file systems the pods access.

    Observe a pod's behavior, then restrict it to the expected flow of processes, events and traffic. Create allow-list policies and audit or deny everything else. This builds a least-permissive security posture.

??? "**3. How AccuKnox helps to recommend Auto-Discovered Policies?**"
    The AccuKnox CWPP **Discovery Engine agent** assesses the security posture of your workloads. It auto-discovers the policy set that puts each workload in least-permissive mode.

    Two agents work together:

    - **Shared Informer Agent**: It collects cluster information such as pods, nodes and namespaces.
    - **Policy Discovery Engine**: It discovers policies from the workload and cluster information that the Shared Informer Agent relays.

??? "**4. How Does AccuKnox Generate Hardening Policies?**"
    AccuKnox **auto-discovers application behaviors** and maps them to CIS, MITRE, NIST and STIG frameworks. It then generates tailored security policies that block unwanted activity at the system level.

    AccuKnox runs **KubeArmor** to secure Kubernetes, container and VM workloads. KubeArmor enforces runtime hardening policies with Linux Security Modules (LSMs) and eBPF. Policies can restrict process execution, file access and network operations.

    These policies help you achieve Zero Trust and stay compliant. You also keep real-time visibility into what gets allowed or blocked.

??? "**5. How AccuKnox helps to implement Zero Trust?**"
    AccuKnox implements Zero Trust with **allow-based KubeArmor policies**. These policies allow specific actions and deny or audit everything else.

    For example, a specific pod or container might only invoke a set of binaries at runtime. An allow-based rule lists the processes that may run. KubeArmor audits or denies every other process, based on the default security posture.

    A Zero Trust posture with KubeArmor reduces the risk of unauthorized access or activity in your Kubernetes clusters. It helps protect sensitive data, prevent system breaches and maintain cluster integrity.

??? "**6. What does AccuKnox measure, while doing security posture observation and how does it help in securing using policies?**"
    AccuKnox measures **compliance framework requirements and application behavior**, and turns each into a policy type.

    - **Hardening policies**: AccuKnox creates them from compliance frameworks (MITRE, CIS, NIST) for hardening workloads. Hardening policies are block-based.
    - **Behavioral policies**: AccuKnox creates them by observing application behavior through LSMs. Behavioral policies are allow-based.
    - **Example**: A FIM (File Integrity Monitoring) policy is one example of these policies.

??? "**7. Do you have any standard hardening rules onboarded and will the hardening policy show what is getting blocked?**"
    Yes. Blocked activity shows up in **Application Behaviour & Logs**.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
