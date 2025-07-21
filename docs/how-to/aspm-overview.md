---
title: ASPM Overview
description: Learn how ASPM helps organizations identify and address security vulnerabilities in their applications throughout the software development lifecycle (SDLC).
hide:
  - toc
---

# ASPM Overview

## How Application Security Posture Management Works?

![image-20250115-113050.png](../getting-started/images/devsecops.png)

ASPM leverages a range of security tools, such as:

- **SAST** (Static Application Security Testing)

- **DAST** (Dynamic Application Security Testing)

- **SCA** (Software Composition Analysis)

- **IaC** (Infrastructure as Code) scanning

- **Secret scanning tools**

These tools are integrated at various stages of the **DevOps lifecycle**, ensuring comprehensive security coverage. The diagram above illustrates how ASPM aligns with the different phases of CI/CD to deliver continuous application security.

For more details on incorporating security into the DevOps lifecycle, visit the [**DevSecOps page**](https://help.accuknox.com/getting-started/devsecops/ "https://help.accuknox.com/getting-started/devsecops/").

## **Use Cases**

::cards:: cols=4
- title: IaC Scanning
  content:
  image: ./icons/iac.svg
  url: https://help.accuknox.com/use-cases/iac-scan/

- title: Container Scanning
  content:
  image: ./icons/container.svg
  url: https://help.accuknox.com/use-cases/container-scan/

- title: SAST
  content:
  image: ./icons/sast.svg
  url: https://help.accuknox.com/use-cases/sast-sq/

- title: Vulnerability Management
  content:
  image: ./icons/vuln-mgmt.svg
  url: https://help.accuknox.com/use-cases/vulnerability/

- title: DAST (MFA-Enabled)
  content:
  image: ./icons/dast-mfa.svg
  url: https://help.accuknox.com/use-cases/mfa-dast/

- title: DAST XSS Mitigation
  content:
  image: ./icons/dast-xss.svg
  url: https://help.accuknox.com/use-cases/dast-xss/

- title: Secret Scan in CI/CD
  content:
  image: ./icons/secret-scan-cicd.svg
  url: https://help.accuknox.com/use-cases/secret-scan-cicd-aws/

- title: Secrets in Code Repositories
  content:
  image: ./icons/secret-scan.svg
  url: https://help.accuknox.com/use-cases/aspm/

- title: Secrets in S3 Buckets & File Systems
  content:
  image: ./icons/access-keys.svg
  url: https://help.accuknox.com/use-cases/hashicorp/

- title: Rules Engine & Automated Ticket Creation
  content:
  image: ./icons/admission-controller.svg
  url: https://help.accuknox.com/use-cases/rules-engine-ticket-creation/

- title: EPSS Scoring for Prioritization
  content:
  image: ./icons/asset-inventory.svg
  url: https://help.accuknox.com/use-cases/epss-scoring/

- title: SCA
  content:
  image: ./icons/supply-chain-attacks.svg
  url: https://www.accuknox.com/solutions/software-composition-analysis

- title: Secrets in Container Images
  content:
  image: ./icons/secret-scan.svg
  url: https://app.storylane.io/share/hmt8tl3ovppy

- title: Secrets in Kubernetes ConfigMaps
  content:
  image: ./icons/secret-scan.svg
  url: https://app.storylane.io/share/2iw7zsxwougy

- title: IaC Security
  content:
  image: ./icons/cloud-misconfig-drift-detection.svg
  url: https://help.accuknox.com/integrations/azure-iac/

::/cards::

## Integrating AccuKnox ASPM

AccuKnox ASPM supports integration with popular CI/CD platforms, such as:

- **Azure DevOps**

- **GitHub Actions**

- **GitLab CI/CD**

- And many others.

AccuKnox offers plugins for various CI/CD platforms, which can be found in the [**CI/CD support matrix**](https://help.accuknox.com/support-matrix/cicd-support-matrix/ "https://help.accuknox.com/support-matrix/cicd-support-matrix/") **page**. To integrate AccuKnox ASPM with your specific CI/CD platform, refer to the [**CI/CD Integrations page**](https://help.accuknox.com/integrations/cicd-overview/ "https://help.accuknox.com/integrations/cicd-overview/") for step-by-step guidance.

By integrating AccuKnox ASPM, organizations can ensure their CI/CD pipelines are fortified with cutting-edge application security tools, reducing vulnerabilities and improving overall software quality.
