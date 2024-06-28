AccuKnox CSPM tool provides with registry scan where the user can onboard their Docker Hub, Nexus, GCR, and ECR registries. Once the registry is onboarded, the scanning of the registry starts automatically in the background. After the scanning is completed, the findings will be populated in the registry scan dashboard.The detailed view of the registry scan on the AccuKnox dashboard gives you scan results and prioritization. In the detailed view that opens, you can click on the tabs - Vulnerabilities, Resources, Sensitive data, Layers for further information.

AccuKnox Zero Trust CNAPP supports onboarding the following container registries to scan for vulnerabilities and sensitive data.

## Amazon Elastic Container Registry

Accuknox CSPM security tool scans images that are present in the onboarded [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) and identifies any known vulnerabilities and risks associated with those images. These are then categorized based on their severity. User will be getting comprehensive view of these risks and vulnerabilities in the dashboard which can be remediated.

[**Steps to Onboard**](./../getting-started/ecr.md)

## Google Container Registry

[Google Container Registry](https://cloud.google.com/container-registry/docs) with images once onboarded into AccuKnox SaaS platform, the images are scanned. The risks and vulnerabilities associated with these images are identified and shown in the scan results. The vulnerabilities are classified based on the CVSS Scores.

[**Steps to Onboard**](./../getting-started/gar.md)

## Nexus Registry

AccuKnox CSPM Security leverages various open source scanning tools to scan the images present in the onboarded Nexus Repository. It identifies the common vulnerabilities and exploits associated with those images and risks. These Vulnerabilities and risks are classified based on their severity.

## DockerHub Registry

[DockerHub](https://hub.docker.com/) Repositories can be integrated with AccuKnox SaaS. Once these registries are onboarded, the images are scanned for vulnerabilities and risks. These findings are populated in the dashboard with Critical, High, low vulnerabilities.

## Azure Container Registry(ACR)

Accuknox CSPM security tool scans images that are present in the onboarded [Azure Container Registry](https://learn.microsoft.com/en-us/azure/container-registry/) and has the capability to find the risks and vulnerabilities associated with these images. The risks are identified and shown in the scan results.
Users will be getting a comprehensive view of these risks and vulnerabilities in the dashboard which can be remediated.

[**Steps to Onboard**](./../getting-started/acr.md)

## Harbor Registry

Once [Harbor Registry](https://goharbor.io/docs/2.9.0/install-config/) is onboarded in Accuknox SaaS, Scan will be initiated for that registry and come up with images and vulnerabilities. These Vulnerabilities and risks are classified based on their severity according to CVSS Scores. Here user can easily get to know about the image in detail such as security issues, Layers of the images, Sensitive data and Vulnerabilities present in their images.

## Quay

We support registry onboarding and scanning for [Quay](https://www.redhat.com/en/technologies/cloud-computing/quay) registry. Once the registry is onboarded, the images are scanned for vulnerabilities and risks. The vulnerabilities are classified based on their severity.

## JFrog Registry

AccuKnox can scan images present in the onboarded [JFrog](https://jfrog.com/) registry. The images are scanned for vulnerabilities and risks. The vulnerabilities are classified based on their severity.

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
