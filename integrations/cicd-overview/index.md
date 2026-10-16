---
title: CI/CD Integrations Overview
description: Check out the integration mechanisms and feature availability for key DevOps and security functionalities across popular CI/CD platforms.
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

# CI/CD Integrations Overview

The CI/CD Support Matrix summarizes integration capabilities and security features across major CI/CD platforms for streamlined DevOps workflows.

::cards:: cols=4

- title: Azure DevOps
  image: ./cicd-icons/azure.png
  url: /integrations/azure-overview/
- title: Bamboo CI
  image: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQIU0fOwGQAo3Au8cCsOLeY18DOWWEdpj-1g&s
  url: /integrations/bamboo-overview/
- title: Google Cloud Build
  image: ./cicd-icons/gcp.png
  url: /integrations/google-overview/
- title: Harness
  image: ./cicd-icons/harness.png
  url: /integrations/harness-overview/
- title: Jenkins
  image: ./cicd-icons/jenkins.png
  url: /integrations/jenkins-overview/
- title: AWS Code Pipeline
  image: ./cicd-icons/aws.png
  url: /integrations/aws-overview/
- title: GitHub
  image: ./cicd-icons/github.png
  url: /integrations/github-overview/
- title: Gitlab
  image: ./cicd-icons/gitlab.png
  url: /integrations/gitlab-overview/
- title: Bitbucket
  image: ./cicd-icons/bitbucket.png
  url: /integrations/bitbucket-overview/
- title: Checkmarx
  image: ./cicd-icons/checkmarx.png
  url: /integrations/checkmarx/
- title: CircleCI
  image: ./cicd-icons/circleci.png
  url: /integrations/circleci-overview/

::/cards::

![image](https://i.ibb.co/cSX9f6VR/image.png)

=== "Continuous API Security"
    !!! tip ""
        🚀 Instead of relying on infrequent manual penetration tests,
        our solution integrates **DAST** into your CI/CD pipeline.

        - Continuous, automated endpoint testing
        - Real-time alerts for new flaws
        - Prevents risks from frequent updates

=== "Integrated SAST & Secrets Scanning"
    !!! success ""
        🔒 Enable dev teams to **scan code and configs inline** with PRs.

        - Static Application Security Testing (SAST)
        - Secrets & sensitive data detection
        - Blocks merges until baseline is met

=== "CI/CD Pipeline Hardening"
    !!! warning ""
        🛡️ Secure your software supply chain by **validating executions**.

        - Monitors CI/CD for improper behavior
        - Detects unauthorized execution paths
        - Prevents hidden supply chain attacks