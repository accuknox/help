---
title: Use Cases By Categories
description: Explore Accuknox's use cases by categories - ASPM, CSPM, CWPP, KSPM.
---


<style>
h2 {
  color: #000025;
  font-size: 1.5rem !important;
}
.nt-card .nt-card-image{
  color: #005BFF;

}


</style>

# Use Cases By Categories


## **ASPM Use Cases**

::cards:: cols=4

- title: IaC Scanning
  content:
  image: ./icons/cluster-misconfig-scan.svg
  url: /use-cases/iac-scan/

- title: Container Scanning
  content:
  image: ./icons/container-image-scan.svg
  url: /use-cases/container-scan/

- title: Static Application Security Testing (SAST)
  content:
  image: ./icons/sql-injection.svg
  url: /use-cases/sast-sq/

- title: Vulnerability Management
  content:
  image: ./icons/vuln-mgmt.svg
  url: /use-cases/vulnerability/

::/cards::

---

## **CSPM Use Cases**

::cards:: cols=3

- title: Asset Inventory
  image: ./icons/asset-inventory.svg
  url: /use-cases/asset-inventory/

- title: Cloud Misconfiguration & Drift Detection
  image: ./icons/cloud-misconfig-drift-detection.svg
  url: /use-cases/cloud-misconfigurations/

::/cards::

---

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

## **KSPM Use Cases**

::cards:: cols=3

- title: Cluster Misconfiguration
  content: Accuknox identifies and flags misconfigurations in your clusters, ensuring that components like RBAC, namespaces, and container security settings follow best practices and remain secure.
  image: ./icons/cluster-misconfig-scan.svg
  url: /use-cases/cluster-misconfiguration-scanning/

- title: CIS Benchmarking
  content: KSPM aligns with the CIS Kubernetes Benchmark, offering automated compliance checks against industry standards to ensure your clusters meet security requirements.
  image: ./icons/workload-hardening.svg
  url: /how-to/cis-benchmarking

- title: KIEM
  content: K8s Identity and Entitlement Management controls access to Kubernetes resources by managing identities and entitlements. It ensures appropriate permissions, secure access, and auditability for users, services, and applications.
  image: ./icons/pod-security-admission-controller.svg
  url: /use-cases/kiem/

::/cards::