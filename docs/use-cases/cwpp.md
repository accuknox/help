---
hide:
  - navigation
  - toc
---
# CWPP (Cloud Workload Protection Platform)

According to **Gartner**, CWPPs are workload-centric security solutions that protect server workloads in hybrid and multi-cloud data center environments. CWPPs deliver consistent security across:

- **K8s**

- **Virtual Machines (VMs)**

- **Containers**

- **Serverless Workloads**

CWPPs ensure visibility and control over the security of these workloads, regardless of where they are deployed---on-premises, in public clouds, or in hybrid environments.

### CWPP in Accuknox

**Accuknox CWPP** provides **runtime security** for Kubernetes and cloud-native workloads. By leveraging **KubeArmor**, Accuknox offers granular control over application behavior at the system level. Key capabilities include:

- **File System Access**: Restricts file access for specific processes.

- **Process Whitelisting**: Limits what processes can be spawned within pods.

- **Network Access**: Restricts the capabilities available to processes.

Accunkox prevents malicious activity based on **Attack framework** and other indicators of compromise (IOCs) at runtime, without fully quarantining workloads. It utilizes **inline remediation** via **BPF LSM**, **AppArmor**, and **SELinux**, ensuring that attacks are blocked before they escalate.

### Key Features of Accuknox CWPP

1. **eBPF-Based Monitoring:** Provides contextual, real-time logs by monitoring critical activities like **file access**, **network access**, and **process behavior** at the kernel level. This allows for detailed visibility into workload interactions, helping detect abnormal activity or security threats. Real-time insights enable faster detection and response to potential security events.

2. **Inline Remediation:** Prevents attacks proactively by blocking malicious behavior before it starts using **Linux Security Modules** (LSMs).

3. **Auditing of Behavior:** Tracks **workload actions** to ensure compliance and improve visibility into environment activity.

4. **Visibility Over Cluster:** Offers comprehensive **cluster visibility**, enabling monitoring and management of all workloads for better security control.

5. **Hardening Policies & Compliance:** Enforces **hardening policies** based on **Attack Frameworks** and **compliance standards**, ensuring workloads are secured and meet regulatory requirements.

6. **Admission Controller:** Validates workload configurations against security policies before deployment, preventing insecure workloads from entering the environment.

7. **Zero-Day Protection:** Uses **inline mitigation** to block zero-day attacks in real-time, stopping new threats before they can exploit vulnerabilities.

Accuknox CWPP serves as a **last layer of defense** in your security architecture. It works in conjunction with other security solutions, such as **KSPM**, to provide comprehensive protection. While KSPM secures Kubernetes configurations and compliance at the cluster level, Accuknox CWPP acts as an additional safeguard at runtime, preventing malicious activity within workloads. Its proactive **inline mitigation** and **real-time protection** stop attacks before they escalate, ensuring that even if a breach bypasses earlier defenses, your workloads are still protected.

## **CWPP Use Cases**

### Container Security

::cards:: cols=3

- title: Container Image Scan
  image: images/uc/container-scan.png
  url: /use-cases/image-scan/

- title: Runtime Application Hardening
  image: images/uc/runtime-hardening.png
  url: /use-cases/app-hardening/

- title: Workload Hardening
  image: images/uc/workload-hardening.png
  url: /use-cases/hardening/

- title: Network Micro-segmentation
  image: images/uc/network-microsegmentation.png
  url: /use-cases/network-segmentation/

- title: Cluster Misconfiguration Scan
  image: images/uc/cluster-misconfig.png
  url: /use-cases/cluster-misconfiguration-scanning/

- title: Pod Security Admission Control
  image: images/uc/pod-security.png
  url: /use-cases/pod-security-admission-controller/

- title: Admission Controller
  image: images/uc/admission-controller.png
  url: /use-cases/admission-controller-knoxguard/

::/cards::

### Least Permissive Posture Assessment

::cards:: cols=3

- title: Runtime Application Behavior Discovery
  image: images/uc/behavior-discovery.png
  url: /use-cases/app-behavior/

- title: Audit/Forensics
  image: images/uc/audit-forensics.png
  url: /use-cases/forensics/

- title: Zero Trust Security
  image: images/uc/zero-trust.png
  url: /use-cases/zero-trust/

::/cards::

### AI Workload Security & Advanced Persistent Threat

::cards:: cols=3

- title: Jupyter Notebook
  image: images/uc/jupyter-notebook.png
  url: /use-cases/jupyter-notebook/

- title: Cryptojacking
  image: images/uc/cryptojacking.png
  url: /use-cases/crypto-mining/

- title: Hildegard
  image: images/uc/hildegard.png
  url: /use-cases/hildegard/

::/cards::

### Host Security

::cards:: cols=3

- title: Host Scan
  image: images/uc/host-scan.png
  url: /use-cases/host-sec/

- title: Malware Scan
  image: images/uc/malware-scan.png
  url: /use-cases/malware-scan/

- title: VM Hardening
  image: images/uc/vm-hardening.png
  url: /use-cases/vm-hardening/

::/cards::

### Securing Secrets Manager

::cards:: cols=3

- title: HashiCorp Vault Hardening
  image: images/uc/hashicorp-vault.png
  url: /use-cases/hashicorp/

- title: CyberArk Conjur Hardening
  image: images/uc/cyberark-conjur.png
  url: /use-cases/cyberark-conjur/

::/cards::

