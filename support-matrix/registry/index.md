---
title: Registry Scanning Support Matrix
description: Learn how to integrate the AccuKnox registry for enhanced Zero Trust CNAPP-based container security and vulnerability management.
---

# Registry Scanning Support Matrix

::cards:: cols=2

- title: Amazon Elastic Container Registry
  content: AccuKnox scans Amazon ECR images to identify vulnerabilities and risks, categorizing them by severity. Users can view and remediate these issues via the dashboard.
  image: ./registry-icons/ecr.png
  url: /how-to/ecr/

- title: Google Artifact Registry
  content: Google Artifact Registry images are continuously scanned for vulnerabilities, classified by CVSS scores. AccuKnox provides actionable remediation insights in the dashboard.
  image: ./registry-icons/gar.png
  url: /how-to/gar/

- title: Azure Container Registry (ACR)
  content: AccuKnox scans Azure Container Registry images for vulnerabilities, presenting categorized results in the dashboard for easy remediation.
  image: ./registry-icons/acr.png
  url: /how-to/acr/

- title: Nexus Registry
  content: AccuKnox continuously scans Sonatype Nexus Registry images for risks, offering real-time insights to secure DevOps environments.
  image: ./registry-icons/nexus.png
  url: /how-to/sonatype-nexus/

- title: DockerHub Registry
  content: AccuKnox scans Docker Hub images regularly, categorizing vulnerabilities by severity and presenting results for proactive issue resolution.
  image: ./registry-icons/docker.png
  url: /how-to/dockerhub/

- title: Harbor Registry
  content: AccuKnox performs scheduled scans of Harbor registries, providing detailed risk insights to address vulnerabilities efficiently.
  image: ./registry-icons/harbor.png
  url: /how-to/harbor/

- title: Quay
  content: Red Hat Quay registries are scanned by AccuKnox to identify vulnerabilities, with actionable results accessible through the dashboard.
  image: ./registry-icons/quay.png
  url: /how-to/quay/

- title: JFrog Registry
  content: AccuKnox scans JFrog registries for vulnerabilities, ensuring secure environments in both cloud and air-gapped deployments.
  image: ./registry-icons/jfrog.png
  url: /how-to/jfrog-container/

::/cards::

AccuKnox seamlessly integrates with popular container registries like Docker Hub, Nexus, GCR, and ECR, enabling users to onboard and scan their registries automatically. Once scanning completes, results are displayed on the Registry Scan Dashboard with prioritized findings for quick remediation.

The detailed view provides insights across four tabs—Vulnerabilities, Resources, Sensitive Data, and Layers—to help users analyze and address issues effectively. The scanning process runs in the background, ensuring a smooth experience while delivering comprehensive visibility into vulnerabilities and sensitive data within container registries.

---

## 1. **Registry Types Supported**

Accuknox CSPM supports a variety of container registries to ensure seamless vulnerability scanning and sensitive data detection across your environment.

| **Registry Type**         | **Authentication Type**      | **Notes**                                                |
|----------------------------|------------------------------|----------------------------------------------------------|
| **Docker Hub Registry**    | Basic Authentication         | Supports Personal, Organization, Docker Trusted Registry |
| **AWS ECR**                | IAM-based Authentication     | Full integration with AWS Elastic Container Registry     |
| **Google Artifact Registry (GAR)** | Service Account Authentication | Compatible with GCR for container storage               |
| **Azure Container Registry (ACR)** | Basic Authentication         | Supports integration with Azure-based registries         |
| **Harbor Registry**        | Basic Authentication         | Open-source registry for cloud-native applications       |
| **Quay Registry**          | Basic Authentication         | Red Hat's container registry solution                    |
| **JFrog Registry**         | Basic Authentication         | Supports both cloud-hosted and self-hosted setups        |
| **Google Artifact Registry (GAR)** | Service Account Authentication | Google’s advanced container artifact storage solution    |
| **Sonatype Nexus Repository** | Basic Authentication      | Popular repository manager supporting various artifact formats |

---

## 2. **Registry Deployments Supported**

Accuknox offers multiple integration types to cater to diverse infrastructure needs, including **cloud-native**, **on-premises**, and **hybrid** configurations.

| **Integration Type** | **Description**                                           |
|-----------------------|-----------------------------------------------------------|
| **Cloud-Native**      | Integrates directly with cloud environments (AWS, Azure, GCP). |
| **On-Premises**       | Supports integration with on-prem systems.               |
| **Hybrid**            | Combines both cloud-native and on-premises configurations.|

---

## 3. **On-Prem Scan Modes**

Accuknox provides flexible deployment modes for on-prem environments to meet scalability and integration requirements.

| **Mode**            | **Description**                                                        |
|----------------------|------------------------------------------------------------------------|
| **Standalone Mode**  | Runs everything on one server; ideal for small or self-contained environments. |
| **Cluster Mode**     | Uses multiple servers for better scalability and performance.         |
| **Agentless Mode**   | Monitors and scans without installing extra software on your servers. |

---

## 4. **Scalability**

Accuknox is designed to scale seamlessly as your infrastructure grows, adapting to meet increasing demands.

| **Scaling Type**      | **Description**                                               |
|-----------------------|---------------------------------------------------------------|
| **Horizontal Scaling** | Scale by adding more nodes to the environment.                |
| **Vertical Scaling**   | Scale by upgrading resources (CPU, memory) of existing nodes. |

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ /-button /-button--primary }
