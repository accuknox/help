---
hide:
  - toc
---


<style>
  .nt-card-title{
    text-align: center;
  }

  .nt-card-img img{
    color: #00025;
  }
</style>

# CWPP (Cloud Workload Protection Platform)

## **CWPP Use Cases**

### **Container Security**

::cards:: cols=3

- title: Container Image Scan
  image: ./icons/container-image-scan.svg
  url: /use-cases/image-scan/

- title: Runtime Application Hardening
  image: ./icons/runtime-app-hardening.svg
  url: /use-cases/app-hardening/

- title: Workload Hardening
  image: ./icons/workload-hardening.svg
  url: /use-cases/hardening/

- title: Network Micro-segmentation
  image: ./icons/network-segmentation.svg
  url: /use-cases/network-segmentation/

- title: Cluster Misconfiguration Scan
  image: ./icons/cluster-misconfig-scan.svg
  url: /use-cases/cluster-misconfiguration-scanning/

- title: Pod Security Admission Control
  image: ./icons/pod-security-admission-controller.svg
  url: /use-cases/pod-security-admission-controller/

- title: Admission Controller
  image: ./icons/admission-controller.svg
  url: /use-cases/admission-controller-knoxguard/

::/cards::

---

### **Least Permissive Posture Assessment**

::cards:: cols=3

- title: Runtime Application Behavior Discovery
  image: ./icons/runtime-application-behaviour-discovery.svg
  url: /use-cases/app-behavior/

- title: Audit/Forensics
  image: ./icons/audit-forensics.svg
  url: /use-cases/forensics/

- title: Zero Trust Security
  image: ./icons/zt-security.svg
  url: /use-cases/zero-trust/

::/cards::

---

### **AI Workload Security & Advanced Persistent Threat**

::cards:: cols=3

- title: Jupyter Notebook
  image: ./icons/jupyter-nb.svg
  url: /use-cases/jupyter-notebook/

- title: Cryptojacking
  image: ./icons/cryptojacking.svg
  url: /use-cases/crypto-mining/

- title: Hildegard
  image: ./icons/hildegard.svg
  url: /use-cases/hildegard/

::/cards::

---

### **Host Security**

::cards:: cols=3

- title: Host Scan
  image: ./icons/host-scan.svg
  url: /use-cases/host-sec/

- title: Malware Scan
  image: ./icons/malware-scan.svg
  url: /use-cases/malware-scan/

- title: VM Hardening
  image: ./icons/vm-hardening.svg
  url: /use-cases/vm-hardening/

::/cards::

---

### **Securing Secrets Manager**

::cards:: cols=3

- title: HashiCorp Vault Hardening
  image: ./icons/hashicorp.svg
  url: /use-cases/hashicorp/

- title: CyberArk Conjur Hardening
  image: ./icons/cyberark.svg
  url: /use-cases/cyberark-conjur/

::/cards::

---

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

