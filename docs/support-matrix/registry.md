# Registry Scanning Support Matrix

Accuknox offers seamless integration with various container registries, enabling users to onboard their registries. Once onboarded, scanning begins automatically in the background. Upon completion, the findings are populated in the **Registry Scan Dashboard**.

The detailed view of the registry scan on the Accuknox dashboard provides a comprehensive overview of the scan results, with prioritization for easy remediation. Users can explore different tabs—**Vulnerabilities**, **Resources**, **Sensitive Data**, and **Layers**—to gain deeper insights into the scan findings.

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
| **Auto-scaling**       | Automatically adjusts resources based on workload demands.    |

---

AccuKnox CSPM tool provides with registry scan where the user can onboard their Docker Hub, Nexus, GCR, and ECR registries. Once the registry is onboarded, the scanning of the registry starts automatically in the background. After the scanning is completed, the findings will be populated in the registry scan dashboard.The detailed view of the registry scan on the AccuKnox dashboard gives you scan results and prioritization. In the detailed view that opens, you can click on the tabs - Vulnerabilities, Resources, Sensitive data, Layers for further information.

AccuKnox Zero Trust CNAPP supports onboarding the following container registries to scan for vulnerabilities and sensitive data.

## Amazon Elastic Container Registry

AccuKnox CSPM security tool scans images that are present in the onboarded [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) and identifies any known vulnerabilities and risks associated with those images. These are then categorized based on their severity. User will be getting comprehensive view of these risks and vulnerabilities in the dashboard which can be remediated.

[Steps To Onboard ECR](../how-to/ecr.md){ .md-button .md-button--primary }

## Google Container Registry

[Google Container Registry](https://cloud.google.com/container-registry/docs) with images once onboarded into AccuKnox SaaS platform, the images are scanned. The risks and vulnerabilities associated with these images are identified and shown in the scan results. The vulnerabilities are classified based on the CVSS Scores.

[Steps To Onboard GAR](../how-to/gar.md){ .md-button .md-button--primary }

## Azure Container Registry(ACR)

AccuKnox CSPM security tool scans images that are present in the onboarded [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/) and has the capability to find the risks and vulnerabilities associated with these images. The risks are identified and shown in the scan results.
Users will be getting a comprehensive view of these risks and vulnerabilities in the dashboard which can be remediated.

[Steps To Onboard ACR](../how-to/acr.md){ .md-button .md-button--primary }

## Nexus Registry

AccuKnox CSPM Security leverages various open source scanning tools to scan the images present in the onboarded Nexus Repository. It identifies the common vulnerabilities and exploits associated with those images and risks. These Vulnerabilities and risks are classified based on their severity.

## DockerHub Registry

[DockerHub](https://hub.docker.com/) Repositories can be integrated with AccuKnox SaaS. Once these registries are onboarded, the images are scanned for vulnerabilities and risks. These findings are populated in the dashboard with Critical, High, low vulnerabilities.

## Harbor Registry

Once [Harbor Registry](https://goharbor.io/docs/2.9.0/install-config/) is onboarded in AccuKnox SaaS, Scan will be initiated for that registry and come up with images and vulnerabilities. These Vulnerabilities and risks are classified based on their severity according to CVSS Scores. Here user can easily get to know about the image in detail such as security issues, Layers of the images, Sensitive data and Vulnerabilities present in their images.

## Quay

We support registry onboarding and scanning for [Quay](https://www.redhat.com/en/technologies/cloud-computing/quay) registry. Once the registry is onboarded, the images are scanned for vulnerabilities and risks. The vulnerabilities are classified based on their severity.

## JFrog Registry

AccuKnox can scan images present in the onboarded [JFrog](https://jfrog.com/) registry. The images are scanned for vulnerabilities and risks. The vulnerabilities are classified based on their severity.

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
