---
title: Policy Management & Enforcement FAQs
description: Frequently asked questions about AccuKnox policy management, zero trust, microsegmentation, auto-discovered policies, and hardening.
hide:
  - toc
---

# Policy Management & Enforcement

??? "**1. How AccuKnox helps in Policy Version Control for Runtime Security?**"
    AccuKnox enables DevSecOps teams to embed security policies as code into their GitOps workflow. This provides a unified, collaborative view of the policies and enables them to be shipped and deployed along with the applications they are protecting. Hence, utilizing Gitops based policy version control, it will be easy to enforce changes to policies and keep track of versions in case of audit or rollback requirement along with approval mechanisms.

??? "**2. How AccuKnox helps to achieve Microsegmentation?**"
    AccuKnox CWPP provides micro-segmentation at the lowest possible granularity level which is also a smallest execution unit in Kubernetes i.e. Pods. We will help you to identify process execution request from the pods, network connections the pods are trying to make internally or externally and files-system the pods are accessing. By observing the behavior of a particular pod and restricting that behavior so that it functions according to the expected flow of process/events/traffic, one can develop a least permissive security posture from creating a whitelisting policies and auditing/denying everything else.

??? "**3. How AccuKnox helps to recommend Auto-Discovered Policies?**"
    AccuKnox CWPP solution provide Discovery Engine agent that assesses the security posture of your workloads and auto-discovers the policy-set required to put the workload in least-permissive mode. We also provide Shared Informer Agent which collects information about cluster like pods, nodes, namespaces etc. The Policy Discovery Engine discovers the policies using the workload and cluster information that is relayed by Shared Informer Agent.

??? "**4. How Does AccuKnox Generate Hardening Policies?**"
    AccuKnox operates KubeArmor to secure Kubernetes, container, and VM workloads by enforcing runtime hardening policies using Linux Security Modules (LSMs) and eBPF. The AccuKnox platform auto-discovers application behaviors and maps them to industry standards like CIS, MITRE, NIST, and STIG frameworks, generating tailored security policies to block unwanted activity at the system level. Policies can restrict process execution, file access, and network operations, helping achieve Zero Trust while maintaining compliance and visibility over what gets allowed or blocked in real time.

??? "**5. How AccuKnox helps to implement Zero Trust?**"
    By implementing a zero trust posture with KubeArmor, organizations can increase their security posture and reduce the risk of unauthorized access or activity within their Kubernetes clusters. This can help to protect sensitive data, prevent system breaches, and maintain the integrity of the cluster.
    KubeArmor supports allow-based policies which result in specific actions to be allowed and denying/auditing everything else. For example, a specific pod/container might only invoke a set of binaries at runtime. As part of allow-based rules you can specify the set of processes that are allowed and everything else is either audited or denied based on the default security posture.

??? "**6. What does AccuKnox measure, while doing security posture observation and how does it help in securing using policies?**"
    + Compliance Frameworks (MITRE, CIS, NIST) for hardening workloads are used to create hardening policies
    + Understanding the Application behaviour using LSMs enables creation of behavioural policies
    + Hardening policies are block based policies
    + Behavioural policies are allow based policies
    + An example of policies is FIM (File Integrity Monitoring) policy

??? "**7. Do you have any standard hardening rules onboarded and will the hardening policy show what is getting blocked?**"
    Yes, it can show up in terms of Application Behaviour & Logs

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
