---
title: Registry Scanning Support Matrix
description: Check out our integration with various container registries, enabling users to onboard their registries. Once onboarded, scanning begins automatically in the background. Upon completion, the findings are populated in the Registry Scan Dashboard.
---

# Registry Scanning Support Matrix

::cards:: cols=2

- title: Amazon Elastic Container Registry
  content: AccuKnox CSPM scans images in Amazon ECR, identifies vulnerabilities, and categorizes them by severity for easy remediation via the dashboard.
  image: ./registry-icons/ecr.png
  url: /how-to/ecr/

- title: Google Container Registry
  content: Once Google Container Registry images are onboarded into AccuKnox SaaS, they are scanned for risks and vulnerabilities. Results are categorized based on CVSS scores and displayed in the dashboard.
  image: ./registry-icons/gar.png
  url: /how-to/gar/

- title: Azure Container Registry (ACR)
  content: AccuKnox CSPM scans images in the onboarded Azure Container Registry, identifies associated risks and vulnerabilities, and provides a detailed view on the dashboard for remediation.
  image: ./registry-icons/acr.png
  url: /how-to/acr/

- title: Nexus Registry
  content: AccuKnox CSPM leverages open-source scanning tools to identify vulnerabilities and risks in onboarded Nexus Registry images. Findings are classified based on severity.
  image: ./registry-icons/nexus.png
  url: /how-to/sonatype-nexus/

- title: DockerHub Registry
  content: Integrated DockerHub registries are scanned for vulnerabilities and risks, with results categorized into Critical, High, and Low severity on the AccuKnox dashboard.
  image: ./registry-icons/docker.png
  url: /how-to/dockerhub/

- title: Harbor Registry
  content: Once onboarded, Harbor Registry images are scanned for vulnerabilities and risks. Users get detailed insights, including security issues, image layers, sensitive data, and vulnerabilities, classified by CVSS scores.
  image: ./registry-icons/harbor.png
  url: /how-to/harbor/

- title: Quay
  content: AccuKnox supports Quay registry onboarding and scanning. Images are analyzed for vulnerabilities and risks, with results categorized by severity.
  image: ./registry-icons/quay.png
  url: /how-to/quay/

- title: JFrog Registry
  content: AccuKnox scans images in onboarded JFrog registries, identifying risks and vulnerabilities. Findings are classified based on their severity.
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
| **Google Container Registry (GCR)** | Service Account Authentication | Compatible with GCR for container storage               |
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
