---
title: CWPP (Cloud Workload Protection Platform)
description: AccuKnox CWPP secures workloads across hybrid clouds, providing runtime protection and visibility for Kubernetes, VMs, and containers.
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

CWPP is a workload-centric security solution that protects server workloads across hybrid and multi-cloud environments. It acts as the final defense layer, complementing KSPM with runtime protection against breaches, and gives consistent visibility into workload behavior across Kubernetes, virtual machines, containers, and serverless workloads.

## **The AccuKnox Runtime Security Journey**

Every workload moves through the same eight steps, from first onboarding to a fully enforced Zero Trust posture. Steps 1 through 4 build the baseline. Steps 5 through 8 refine it and lock it down.

![AccuKnox Runtime Security Journey, steps 1 to 4](../assets/images/runtime-security-journey-1.png)

![AccuKnox Runtime Security Journey, steps 5 to 8](../assets/images/runtime-security-journey-2.png)

!!! info "Continuous loop"
    Step 5 loops back to Step 2. As containers spawn cronjobs or new behaviors emerge, AccuKnox keeps learning, you accept or discard the changes, and the golden baseline keeps improving until policies are marked **STABLE** and moved to **BLOCK** mode.

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

## **Accuknox CWPP Core Capabilities**

### **Runtime security with granular control**

- Restricted file system access
- Process whitelisting
- Network access limitations

### **Key Technical Features**

- eBPF-based kernel-level monitoring
- Inline attack prevention using Linux Security Modules
- Real-time workload behavior auditing
- Comprehensive cluster visibility
- Policy-based hardening
- Admission controller validation
- Zero-day attack mitigation


!!! info
    For more information on our **CWPP** offerings, visit the [**AccuKnox CWPP Page**](https://www.accuknox.com/products/cwpp "https://www.accuknox.com/products/cwpp").
