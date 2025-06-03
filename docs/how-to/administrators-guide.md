---
hide:
  - toc
---

# Administrator's Guide

!!! info "Purpose of this Guide"
    This page serves as a focused documentation index for administrators looking for **step-by-step onboarding, deployment, configuration, and operational guidance**. This documentation is suitable for users deploying AccuKnox in real-world cloud-native environments. This curated guide is tailored for technical administrators and DevSecOps engineers who are looking for **concrete, task-oriented onboarding assets**, **installation steps**, and **configuration references**.

## Custom Onboarding Pages

These two pages are specially prepared for high-level onboarding context.

<div style="display: flex; gap: 20px; justify-content: center; align-items: flex-start; flex-wrap: wrap;">
  <!-- First Image Block -->
  <div style="flex: 1; min-width: 300px; max-width: 600px; text-align: center;">
    <a href="../high-level-onboarding" style="text-decoration: none; color: blue;">
      <img id="img1" src="https://i.ibb.co/7dFjz13S/support-worklaods.png" alt="AccuKnox Onboarding Assets"
           style="width: 100%; height: auto; border: 1px solid #ccc; border-radius: 8px;">
      <p style="margin-top: 10px; font-weight: bold;">AccuKnox Onboarding Assets</p>
    </a>
  </div>

  <!-- Second Image Block -->
  <div style="flex: 1; min-width: 300px; max-width: 600px; text-align: center;">
    <a href="../k8s-security-onboarding" style="text-decoration: none; color: blue;">
      <img id="img2" src="https://i.ibb.co/Z1wCCbhv/Screenshot-2025-06-03-203641.png" alt="Kubernetes Security Onboarding"
           style="width: 100%; height: 100%; object-fit: cover; border: 1px solid #ccc; border-radius: 8px;">
      <p style="margin-top: 10px; font-weight: bold;">Detailed Kubernetes Security Onboarding</p>
    </a>
  </div>
</div>

<script>
  // Match heights of both images after loading
  window.onload = function() {
    const img1 = document.getElementById('img1');
    const img2 = document.getElementById('img2');
    if (img1 && img2) {
      img2.style.height = img1.clientHeight + "px";
    }
  };
</script>


## Table of Contents

??? note "Getting Started & Installation"

    - [On-prem Installation](../getting-started/on-prem-installation-guide.md)
    - [Runtime Security Prerequisites](../getting-started/cwpp-prereq.md)
    - [Signup/Login via SSO](../how-to/sso.md)

??? note "Cloud Accounts Onboarding"

    - [AWS Prerequisites](../how-to/cspm-prereq-aws.md)
    - [Azure Prerequisites](../how-to/cspm-prereq-azure.md)
    - [GCP Prerequisites](../how-to/cspm-prereq-gcp.md)
    - [AWS Onboarding](../how-to/aws-onboarding.md)
    - [Azure Onboarding](../how-to/azure-onboarding.md)
    - [GCP Onboarding](../how-to/gcp-onboarding.md)
    - [Offboard Cloud Account](../how-to/cloud-offboarding.md)

??? note "Kubernetes Security Onboarding"

    - [Runtime Security Onboarding](../how-to/cluster-onboarding.md)
    - [Cluster Onboarding with Access Keys](../how-to/cluster-onboarding-access-keys.md)
    - [Cluster Misconfiguration Scan Onboarding](../how-to/cluster-misconfig-scan-onboarding.md)
    - [CIS Benchmarking](../how-to/cis-benchmarking.md)
    - [Cluster Offboarding](../how-to/cluster-offboarding.md)
    - [Security on OpenShift](../getting-started/security-on-openshift.md)

??? note "VM / Host-Based Workload Onboarding"

    - [VM Onboard/Deboard with Docker](../how-to/vm-onboard-deboard-docker.md)
    - [VM Onboard/Deboard with SystemD](../how-to/vm-onboard-deboard-systemd.md)
    - [SystemD Based Non-BTF Environments](../how-to/systemd-nonbtf.md)
    - [VM Onboarding with Access Keys](../how-to/vm-onboard-access-keys.md)

??? note "Container Registry & Scanner Setup"

    - [In-Cluster Image Scanner via Helm](../how-to/in-cluster-image-scan-helm.md)
    - [DockerHub Registry Integration](../how-to/dockerhub.md)
    - [JFrog Container Registry Setup](../how-to/jfrog-container.md)

??? note "Reports, Monitoring & Health Tools"

    - [Generate CWPP Reports](../how-to/cwpp-reports-generation.md)
    - [Configure Custom Report](../how-to/custom-reports.md)
    - [Health Monitoring (RINC)](../how-to/RINC.md)

!!! note "Need Help?"
    For troubleshooting, advanced configuration support, or integration queries, please refer to:

    - [CWPP Troubleshooting](../resources/troubleshooting.md)
    - [CSPM Troubleshooting](../resources/cspm-troubleshooting.md)
    - [Technical Support Guide](../resources/technical-support-guide.md)
