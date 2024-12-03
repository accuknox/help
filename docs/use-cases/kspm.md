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

# KSPM (Kubernetes Security Posture Management)

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

- KSPM provides a security framework for Kubernetes, continuously assessing configurations and detecting misconfigurations to prevent security breaches.
- Delivers agentless Kubernetes security with compliance monitoring, risk management, and real-time alerting.
- Serves as a critical security layer when integrated with Cloud Workload Protection Platforms (CWPP), offering multi-layered defense across containerized environments by providing visibility and proactive risk management.

!!!info
    **For more details, refer [KSPM on AccuKnox Website](https://www.accuknox.com/products/kspm)**
