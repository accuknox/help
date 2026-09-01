---
title: CI/CD Support Matrix
description: Check out the integration mechanisms and feature availability for key DevOps and security functionalities across popular CI/CD platforms.
hide:
  - toc
---

<style>
    table:first-of-type td:first-child img{
    display: block;
    height: 3rem;
    }

​    .nt-card-title {
​    text-align: -webkit-center;
​    }

 /* align tables to center */

 table{
    margin-left: auto;
    margin-right: auto;
    }

</style>

# CI/CD Security Support Matrix

Get a quick overview of integration types and security features supported across major CI/CD platforms. Use this matrix to choose the best tools for your DevOps workflows and ensure robust security and compliance.

::cards:: cols=3

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
  ::/cards::


## **Integration Types**

These are the three supported methods for integrating CI/CD tools with AccuKnox :-

=== "Workflow File"
    **Description**: A workflow file is a configuration file within the CI/CD tool where you define the steps of your build, test, and deploy pipeline. It allows you to automate tasks using specific syntax and structure (often YAML or JSON).

=== "Plugin Support"
    **Description**: This method refers to using external plugins to extend the functionality of the CI/CD tool. Plugins integrate the tool with third-party services or features, such as code scanning, security checks, or deployment to cloud platforms.

=== "Native Integration"
    **Description**: Native integration refers to the seamless, built-in capability of AccuKnox to directly connect with CI/CD tools and platforms, without the need for external plugins. This method utilizes the internal features of AccuKnox to interact with and manage security policies, scans, and assessments within the CI/CD pipeline.


| CI/CD Tool                                                                                                                                            | Workflow file (Direct Steps) | Plugin Support |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------- |
| ![GitHub Actions](./cicd-icons/github.png) **[GitHub Actions](https://github.com/marketplace?query=accuknox)**                                        | Available                    | Available      |
| ![GitLab CI/CD](./cicd-icons/gitlab.png) **[GitLab CI/CD](https://gitlab.com/accu-knox/scan)**                                                        | Available                    | Available      |
| ![Jenkins](./cicd-icons/jenkins.png) **Jenkins**                                                                                                      | Available                    | Available      |
| ![Azure DevOps](./cicd-icons/azure.png) **[Azure DevOps](https://marketplace.visualstudio.com/search?term=accuknox&target=AzureDevOps&category=All)** | Available                    | Available      |
| ![AWS CodePipeline](./cicd-icons/aws.png) **AWS CodePipeline**                                                                                        | Available                    | Coming Soon    |
| ![Bitbucket](./cicd-icons/bitbucket.png) **[Bitbucket](https://bitbucket.org/accu-knox/scan/)**                                                       | Available                    | Available      |
| ![CircleCI](./cicd-icons/circle.png) **[CircleCI](https://circleci.com/developer/orbs/orb/accuknox/scan)** | Available | Available |
| ![GCP Cloud Build](./cicd-icons/gcp.png) **GCP Cloud Build**                                                                                          | Available                    | Coming Soon    |
| ![Harness](./cicd-icons/harness.png) **Harness**                                                                                                      | Available                    | Coming Soon    |

---

| Repository      | Native Integration (IaC) |
| --------------- | ------------------------ |
| **GitHub**      | Available                |
| **GitLab**      | Available                |
| **Bitbucket**   | Available                |
| **Azure Repos** | Coming Soon              |

## Feature Support Table (Plugins)

| CI/CD Tool                                                   | SAST                                                         | DAST                                                         | IaC Scanning                                                 | Container Scanning                                           | Secrets Scanning                                             | CI/CD Pipeline Monitoring                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![GitHub Actions](./cicd-icons/github.png) **GitHub Actions** | [Available (v1.0.1)](https://github.com/marketplace/actions/accuknox-sast) | [Available (v1.0.0)](https://github.com/marketplace/actions/accuknox-dast) | [Available (v0.0.1)](https://github.com/marketplace/actions/accuknox-iac) | [Available (v0.0.1)](https://github.com/marketplace/actions/accuknox-container-scan) | [Available (v1.0.0)](https://github.com/marketplace/actions/accuknox-secret-scan) | [Available (v0.3.15)](https://github.com/marketplace/actions/accuknox-report) |
| ![GitLab CI/CD](./cicd-icons/gitlab.png) **GitLab CI/CD**    | [Available (v1.0.3)](https://gitlab.com/accu-knox/scan)      | [Available (v1.0.3)](https://gitlab.com/accu-knox/scan)      | [Available (v1.0.3)](https://gitlab.com/accu-knox/scan)      | [Available (v1.0.3)](https://gitlab.com/accu-knox/scan)      | [Available (v1.0.3)](https://gitlab.com/accu-knox/scan)      | Coming Soon                                                  |
| ![Jenkins](./cicd-icons/jenkins.png) **Jenkins**             | Available                                                    | Available                                                    | Available                                                    | Available                                                    | Available                                                    | Coming Soon                                                  |
| ![Azure DevOps](./cicd-icons/azure.png) **Azure DevOps**     | [Available ( (v1.0.4)](https://marketplace.visualstudio.com/items?itemName=AccuKnox.accuknox-SAST) | [Available (v1.0.0)](https://marketplace.visualstudio.com/items?itemName=AccuKnox.accuknox-dast&ssr=false#overview) | [Available (v1.0.7)](https://marketplace.visualstudio.com/items?itemName=AccuKnox.accuknox-iac) | [Available (v1.0.0)](https://marketplace.visualstudio.com/items?itemName=AccuKnox.accuknox-container-scan) | [Available (v1.0.5)](https://marketplace.visualstudio.com/items?itemName=AccuKnox.accuknox-secret-scan) | Coming Soon                                                  |
| ![Bitbucket](./cicd-icons/bitbucket.png) **Bitbucket**       | [Available (v1.0.5)](https://bitbucket.org/accu-knox/scan/)  | [Available (v1.0.5)](https://bitbucket.org/accu-knox/scan/)  | [Available (v1.0.5)](https://bitbucket.org/accu-knox/scan/)  | [Available (v1.0.5)](https://bitbucket.org/accu-knox/scan/)  | [Available (v1.0.5)](https://bitbucket.org/accu-knox/scan/)  | Coming Soon                                                  |
| ![CircleCI](./cicd-icons/circle.png) **[CircleCI](https://circleci.com/developer/orbs/orb/accuknox/scan)** | [Available](https://circleci.com/developer/orbs/orb/accuknox/scan) | [Available](https://circleci.com/developer/orbs/orb/accuknox/scan) | [Available](https://circleci.com/developer/orbs/orb/accuknox/scan) | [Available](https://circleci.com/developer/orbs/orb/accuknox/scan) | [Available](https://circleci.com/developer/orbs/orb/accuknox/scan) | Coming Soon |
| ![Harness](./cicd-icons/harness.png) **Harness**             | Coming Soon                                                  | Coming Soon                                                  | Coming Soon                                                  | Coming Soon                                                  | Coming Soon                                                  | Coming Soon                                                  |
