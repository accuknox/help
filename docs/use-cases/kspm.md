---
hide:
  - navigation
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

- KSPM provides a robust security framework for managing and mitigating risks in Kubernetes environments. As Kubernetes becomes the backbone of modern containerized applications, securing it is critical for maintaining compliance and preventing security breaches. KSPM tools integrate seamlessly into Kubernetes clusters, continuously assessing configurations, detecting misconfigurations, and ensuring alignment with security best practices.

- KSPM delivers agentless security for Kubernetes, simplifying deployment and reducing overhead. It ensures compliance, monitors misconfigurations, manages risks, and provides real-time alerts, helping organizations maintain a robust security posture.

- Additionally, KSPM can act as a critical **layer of security** within a broader security framework. When integrated with a **Cloud Workload Protection Platform (CWPP)**, KSPM serves as the first line of defense, providing visibility and proactive risk management at the Kubernetes layer. If any issues are missed or bypassed, the CWPP acts as a fallback, providing deeper protection at the workload level. This combined approach ensures multi-layered security, mitigating risks across the entire containerized environment while optimizing operational efficiency.

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
