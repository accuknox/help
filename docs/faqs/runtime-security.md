---
title: Runtime Security (CWPP & KubeArmor) FAQs
description: Frequently asked questions about AccuKnox runtime security, CWPP, KubeArmor, inline mitigation, eBPF, LSM enforcement, and workload protection.
hide:
  - toc
---

# Runtime Security (CWPP & KubeArmor)

??? "**1. How does AccuKnox help to achieve Runtime security?**"
    AccuKnox's Cloud Workload Protection Platform (CWPP) uses **KubeArmor** for runtime security. KubeArmor is a CNCF sandbox project and a cloud-native runtime security enforcement system by AccuKnox.

    KubeArmor gives you granular control over application behavior at the system level:

    - **Process execution**: KubeArmor restricts which processes run in containers and nodes.
    - **File access**: KubeArmor restricts which files containers and nodes can access.
    - **Networking operations**: KubeArmor restricts the network operations of containers and nodes.

??? "**2. What is the differentiation of AccuKnox in Runtime Security?**"
    AccuKnox **stops malicious attacks before they execute**. This is known as in-line mitigation (mentioned by Forrester report).

    KubeArmor, the AccuKnox enforcement system, uses Linux Security Modules (LSMs) to secure workloads. LSMs were not built with modern workloads such as containers and orchestrators in mind. eBPF lets AccuKnox extend LSM capabilities. BPF LSM lets AccuKnox load custom decision-making programs into the kernel to protect modern workloads.

??? "**3. What does KubeArmor leverage for enforcement and what are its advantages?**"
    KubeArmor uses **Linux Security Modules (LSMs)** such as AppArmor, BPF-LSM and SELinux for inline mitigation. This reduces the attack surface of the pod, container or VM.

    LSMs have advantages over other techniques:

    - **No disruption**: KubeArmor does not have to disturb pods or containers.
    - **No host changes**: KubeArmor needs no change at the host or CRI level to apply security policies.
    - **One abstraction**: Nodes in one cluster can use different LSMs. KubeArmor hides that complexity and gives one easy way to enforce policy.

    KubeArmor deploys as a **non-privileged daemonset** with certain capabilities. These capabilities let it monitor other pods, containers and the host.

??? "**4. What role does AccuKnox Agents play in runtime-security?**"
    AccuKnox Enterprise version runs **four agents**:

    - **KubeArmor**: This cloud-native runtime security enforcement system restricts container and node behavior at the system level. That behavior includes process execution, file access and networking operations. KubeArmor sets restrictions on the pod dynamically and uses Linux Security Modules (LSMs) to enforce policies at runtime.
    - **Feeder Service**: It collects the feeds from KubeArmor and relays them to the app.
    - **Shared Informer Agent**: It collects cluster information such as pods, nodes and namespaces.
    - **Policy Discovery Engine**: It discovers policies from the workload and cluster information that the Shared Informer Agent relays.

??? "**5. Does KubeArmor only support Kubernetes or it can support on-prem deployments like legacy VM, pure containerized workload as well?**"
    No, KubeArmor is not limited to Kubernetes. It supports **two types of workloads**:

    - **K8s orchestrated workloads**: These run as k8s orchestrated containers. KubeArmor deploys as a k8s daemonset. KubeArmor enforces policy on both k8s-pods (KubeArmorPolicy) and k8s-nodes (KubeArmorHostPolicy).
    - **VM/Bare-Metal workloads**: These run directly as host processes on Virtual Machines or Bare Metal. KubeArmor deploys in systemd mode.

??? "**6. What is the difference between Post-attack mitigation and in-line mitigation and which is better?**"
    **Inline mitigation is better**, because it stops the attack before it happens. Post-attack mitigation acts only after the attacker runs code.

    Post-exploit mitigation kills the suspicious process after an alert shows malicious intent. Until then, the attacker can execute its binary. The attacker could disable security controls or access logs to avoid detection. By the time the process dies, it might have deleted, encrypted or sent out sensitive content.

    ![post attack mitigation](/faqs/images/post-attack-mitigation.png)

    Inline mitigation prevents the attack at the moment it happens. It protects the environment with a security policy or firewall, so the attack never runs. AccuKnox's open-source tool **KubeArmor** provides inline mitigation to reduce the attack surface of the pod, container or VM. KubeArmor uses LSMs such as AppArmor, BPF-LSM and SELinux (only for host protection).

??? "**7. Does Inline remediation slowdown the process?**"
    No. **Inline remediation does not slow down the process.** LSMs are already enabled in the environment and use host-based LSM security. Attackers usually have direct access to the pod, so AccuKnox stops the processes before they execute.

??? "**8. How to check running services in a VM?**"
    Use `systemctl` to check that the required services run inside a Virtual Machine.

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

    These commands confirm that **KubeArmor** and other critical services are active inside the VM for enforcement and telemetry.

??? "**9. Onboarding an OpenShift cluster fails with the KubeArmor Operator pod not coming up. What should I check?**"
    Check OpenShift's **Security Context Constraints (SCC)**. SCC blocks the KubeArmor Operator because OpenShift does not identify it as a Red Hat certified operator.

    In one symptom, the operator pod is stuck in `CrashLoopBackOff`/`Error` state. In another, you see errors such as `unable to validate against any security context constraint`.

    To fix this, add these flags to the [onboarding helm command](../how-to/cluster-onboarding.md) for OpenShift clusters:

    ```sh
    --set kubearmor-operator.kubearmorOperator.env[0].name=REDHAT_CERTIFIED_OP \
    --set kubearmor-operator.kubearmorOperator.env[0].value=true \
    ```

    These flags mark the operator as Red Hat certified. The operator then meets OpenShift's SCC requirements and deploys.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
