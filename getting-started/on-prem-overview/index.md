---
title: On-Premises Overview
description: Overview of On-Premises Deployment for AccuKnox
hide:
  - toc
---


<style>
h2 {
  color: #000025;
  font-size: 1.5rem !important;
}
.nt-card .nt-card-image{
  color: #005BFF;

}

 .nt-card-title {
    text-align: -webkit-center;
}
</style>

# On-Prem Deployment Modes

::cards:: cols=3

 - title: Installation Guide
   image: ./icons/installation-guide.svg
   url: ../getting-started/on-prem-installation-guide.md
   description: Step-by-step guide for AccuKnox on-prem installation.

 - title: Single Node Installation
   image: ./icons/single-node-install.svg
   url: ../getting-started/on-prem-single-node-installation.md
   description: Deploy AccuKnox on a single node for quick setup.

 - title: Managed Installation (EKS, AKS, GKE)
   image: ./icons/managed-install.svg
   url: ../getting-started/onprem-eks-aks-gke.md
   description: Managed Kubernetes installation for AWS, Azure, and GCP.

 - title: Security on OpenShift
   image: ./icons/openshift-sec.svg
   url: ../getting-started/security-on-openshift.md
   description: Secure your OpenShift environment with AccuKnox.

 - title: Health Monitoring (RINC)
   image: ./icons/health-monitoring.svg
   url: ../how-to/RINC.md
   description: Monitor cluster health and runtime security (RINC).

 - title: AWS Control Plane Installation
   image: ./icons/control-plane.svg
   url: ../getting-started/aws-ami.md
   description: Install AccuKnox control plane on AWS for centralized management.

::/cards::

## High-Level Architecture Overview

![](./images/on-prem/3.png)

AccuKnox onprem deployment is based on Kubernetes native architecture.

## AccuKnox OnPrem k8s components

=== "Microservices"

  * Golang microservices handle streaming data (alerts, telemetry).
  * Python microservices manage control-plane services.

=== "Databases"

  * PostgreSQL stores relational data.
  * MongoDB stores JSON events (alerts, telemetry).
  * Ceph stores scanned reports, managed by Rook operator.

=== "Secrets Management"

  * Vault stores internal and user secrets.
  * Service accounts and tokens manage authorization.

=== "Scaling"

  * Horizontal and vertical pod autoscaling enabled for most microservices.
  * Resource limits are set for scaling.

=== "AccuKnox-Agents"

  * Agents run in k8s clusters and VMs for runtime security and forensics.
  * Use eBPF and LSMs for telemetry and attack prevention.
  * SPIFFE/SPIRE handles attestation and certificate rotation.

## Onboarding Steps for AccuKnox

The onboarding process for AccuKnox's on-prem security solution consists of four concise steps:

![on-prem](images/on-prem/user_journey.png)

=== "Hardware & Prerequisites"
	* Verify hardware, email user, and domain configurations.
	* Ensure your environment meets all requirements.
	* **Time:** Varies, allocate sufficient time for review.

=== "Staging Images (Airgapped)"
	* Stage AccuKnox container images in airgapped setups.
	* Reconfirm hardware, email user, and domain requirements.
	* **Time:** ~1 hour.

=== "Installation"
	* Install AccuKnox system in your environment.
	* Ensure all prerequisites remain satisfied.
	* **Time:** ~45 minutes.

=== "Verification/Validation"
	* Confirm all steps completed successfully.
	* Validate hardware, email user, and domain configurations.
	* **Time:** ~1 hour.

AccuKnox onprem deployment is based on Kubernetes native architecture.

[DOWNLOAD CONTROL PLANE ARCHITECTURE](/resources/assets/AccuKnox%20Control%20Plane%20Architecture%20Technical%20v3.4.pdf){ .md-button .md-button--primary download }
