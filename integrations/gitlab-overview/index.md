---
title: Gitlab Integrations
description: Learn how to integrate gitlab with Rafay to automate security testing and deployment of your applications.
hide:
  - toc
---

<style>
.nt-card .nt-card-image{
  color: #005BFF;
}

.nt-card-title {
    text-align: -webkit-center;
}
</style>

# Gitlab Integrations

!!! tip "New: connect once, scan from the platform"
    You can now scan your repositories without adding a step to your CI/CD pipeline. Install the AccuKnox app on your organization, then choose repositories, branches, and scan types (SCA, Secrets, SAST, IaC) from the platform. See [Connect Source Code for Security Scanning](/how-to/code-source-onboarding/). The pipeline integrations below remain available.

::cards:: cols=3

- title: SQ-SAST (SonarQube)
  image: ./cicd-icons/sast.svg
  url: /integrations/gitlab-sast/
- title: SAST (Static Analysis)
  image: ./cicd-icons/opengrep-sast.svg
  url: /integrations/gitlab-opengrep/
- title: Container Scan
  image: ./cicd-icons/container.svg
  url: /integrations/gitlab-container-scan/
- title: IaC Scan
  image: ./cicd-icons/iac.svg
  url: /integrations/gitlab-iac-scan/
- title: IaC Scan (Gitlab Pipeline)
  image: ./cicd-icons/iac-scan-gitlab-pipeline.svg
  url: /integrations/gitlab-pipeline-iac-scan/
- title: DAST (Dynamic Analysis)
  image: ./cicd-icons/dast.svg
  url: /integrations/gitlab-dast/
- title: Secrets Scan (Gitlab Pipeline)
  image: ./cicd-icons/secret-scan.svg
  url: /integrations/gitlab-secret-scan/
::/cards::

## Scan Variables

::cards:: cols=2

- title: Container Variables
  image: ./cicd-icons/container.svg
  url: /integrations/gitlab-container-variables/
- title: IaC Variables
  image: ./cicd-icons/iac.svg
  url: /integrations/gitlab-iac-variables/
- title: DAST (Dynamic Analysis)
  image: ./cicd-icons/dast.svg
  url: /integrations/gitlab-dast-variables/
- title: SAST Variables
  image: ./cicd-icons/sast.svg
  url: /integrations/gitlab-sast-variables/

::/cards::

![image](https://i.ibb.co/cSX9f6VR/image.png)