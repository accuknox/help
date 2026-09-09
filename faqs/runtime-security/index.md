---
title: Runtime Security (CWPP & KubeArmor) FAQs
description: Frequently asked questions about AccuKnox runtime security, CWPP, KubeArmor, inline mitigation, eBPF, LSM enforcement, and workload protection.
hide:
  - toc
---

# Runtime Security (CWPP & KubeArmor)

??? "**1. How does AccuKnox help to achieve Runtime security?**"
    AccuKnox's Cloud Workload Protection Platform (CWPP) achieves runtime security by leveraging CNCF sandbox project, KubeArmor, which is a cloud-native runtime security enforcement system by AccuKnox that restricts and have more granular control over the application behavior such as process execution, file access, and networking operation of containers and nodes at the system level.

??? "**2. What is the differentiation of AccuKnox in Runtime Security?**"
    AccuKnox leverages KubeArmor, which is a cloud-native runtime security enforcement system that leverages Linux Security Modules to secure the workloads. LSMs are really powerful but they weren't built with modern workloads including Containers and Orchestrators in mind. Hence, eBPF has provided us with the ability to extend capabilities and BPF LSM provide us with the ability to load our custom programs with decision-making into the kernel seamlessly helping us protect modern workloads. Therefore, KubeArmor helps to enforce security posture wherein any malicious attacks will be stopped before execution, known as in-line mitigation (mentioned by Forrester report)

??? "**3. What does KubeArmor leverage for enforcement and what are its advantages?**"
    KubeArmor leverages best of breed Linux Security Modules (LSMs) such as AppArmor, BPF-LSM, and SELinux for inline mitigation to reduce the attack surface of the pod/container/VM.LSMs have several advantages over any other techniques. By using LSMs, KubeArmor does not have to disturb pods/containers and also doesn't require change at host or CRI level to apply security policies.

    KubeArmor deploys as a non-privileged daemonset with certain capabilities that allows it to monitor other pods/containers and host. A given cluster can have multiple nodes utilizing different LSMs so KubeArmor abstracts away the complexities of the LSMs and provides an easy way for policy enforcement.

??? "**4. What role does AccuKnox Agents play in runtime-security?**"
    AccuKnox Enterprise version consists of various agents such as

    **KubeArmor:** KubeArmor is a cloud-native runtime security enforcement system that restricts the behavior (such as process execution, file access, and networking operation) of containers and nodes at the system level. KubeArmor dynamically set the restrictions on the pod. KubeArmor leverages Linux Security Modules (LSMs) to enforce policies at runtime.

    **Feeder Service:** It collects the feeds from kubeArmor and relays to the app.

    **Shared Informer Agent:** It collects information about the cluster like pods, nodes, namespaces etc.,

    **Policy Discovery Engine:** It discovers the policies using the workload and cluster information that is relayed by a shared informer Agent.

??? "**5. Does KubeArmor only support Kubernetes or it can support on-prem deployments like legacy VM, pure containerized workload as well?**"
    KubeArmor supports following types of workloads:

    + K8s orchestrated workloads: Workloads deployed as k8s orchestrated containers. In this case, KubeArmor is deployed as a k8s daemonset. Note, KubeArmor supports policy enforcement on both k8s-pods (KubeArmorPolicy) as well as k8s-nodes (KubeArmorHostPolicy).
    + VM/Bare-Metals workloads: Workloads deployed on Virtual Machines or Bare Metal i.e. workloads directly operating as host processes. In this case, KubeArmor is deployed in systemd mode.

??? "**6. What is the difference between Post-attack mitigation and in-line mitigation and which is better?**"
    Post-exploit Mitigation works by killing the suspicious process in response to an alert indicating malicious intent. In this case attacker will be allowed to is able to execute its binary and could possibly disable the security controls, access logs, etc to circumvent the attack detection. By the time the malicious process is killed, it might have already deleted, encrypted, or transmitted the sensitive contents.

    ![post attack mitigation](/faqs/images/post-attack-mitigation.png)

    Inline Mitigation on the other hand prevents the malicious attack at the time of happening itself. It doesn't allow the attack to happen by protecting the environment with security policy or firewall. AccuKnox's open source tool KubeArmor provides Inline Mitigation. KubeArmor uses inline mitigation to reduce the attack surface of pod/container/VM. KubeArmor leverages best of breed Linux Security Modules (LSMs) such as AppArmor, BPF-LSM, and SELinux (only for host protection) for inline mitigation

??? "**7. Does Inline remediation slowdown the process?**"
    LSMs are already enabled in the environment and use host based LSM security. Since the attacker usually has direct access to the pod, AccuKnox uses Inline remediation to stop the processes before executing. Therefore, inline remediation does not slow down the process

??? "**8. How to check running services in a VM?**"
    To troubleshoot or verify if required services are running inside a Virtual Machine, use the following commands:

    - To check if a specific service (e.g., `kubearmor`, `vm-adapter`) is running:

    ```sh
    sudo systemctl status <service_name>  # Replace with actual service name

    sudo systemctl status kubearmor
    sudo systemctl status vm-adapter
    ```

    - To list all currently running services:

    ```sh
    systemctl --type=service --state=running
    ```

    This helps confirm whether KubeArmor or other critical services are active inside the VM for proper enforcement and telemetry.

??? "**9. Onboarding an OpenShift cluster fails with the KubeArmor Operator pod not coming up. What should I check?**"
    This usually happens when OpenShift's Security Context Constraints (SCC) block the KubeArmor Operator because it isn't identified as a Red Hat certified operator. Symptoms include the operator pod stuck in `CrashLoopBackOff`/`Error` state, or errors such as `unable to validate against any security context constraint`.

    To fix this, add the following flags to the [onboarding helm command](../how-to/cluster-onboarding.md) for OpenShift clusters:

    ```sh
    --set kubearmor-operator.kubearmorOperator.env[0].name=REDHAT_CERTIFIED_OP \
    --set kubearmor-operator.kubearmorOperator.env[0].value=true \
    ```

    These flags mark the operator as Red Hat certified so it satisfies OpenShift's SCC requirements and deploys successfully.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
