---
title: DevSecOps
description: Integrate AccuKnox with CI pipeline and perform the scans and show the reports in the SaaS Dashboard.
---

## Overview

AccuKnox integrates seamlessly into your CI/CD pipeline to provide robust, agentless scanning capabilities, supporting a **Shift-Left Security** approach. By embedding security checks early in the software development lifecycle, AccuKnox enables developers to identify and remediate vulnerabilities, misconfigurations, and other security issues directly within their development tools and pipelines. The agentless scans run efficiently without requiring additional installations and can be configured to break pipelines when critical vulnerabilities are detected, ensuring that insecure code does not progress further. This proactive approach reduces the risks and costs associated with addressing issues late in the process while fostering secure, agile development.

## Types of Scanning

| **Scan Type**                     | **Description**                                                                                     |
|-----------------------------------|-----------------------------------------------------------------------------------------------------|
| **Static Application Security Testing (SAST)** | Scans application source code to detect security issues early in the development lifecycle.            |
| **Dynamic Application Security Testing (DAST)** | Identifies vulnerabilities in running applications during real-world execution.                       |
| **Software Composition Analysis (SCA)**       | Detects vulnerabilities in third-party libraries and open-source dependencies.                       |
| **Infrastructure as Code (IaC) Scanning**     | Verifies that infrastructure configurations comply with security best practices and standards.        |
| **Container Image Scanning**                  | Scans container images for security vulnerabilities, misconfigurations, and compliance issues before deployment. |

## Supported CI/CD Pipelines

AccuKnox supports integration with a wide range of CI/CD tools, enabling smooth adoption across various workflows, including on-premise pipelines.

- **Workflow**: A workflow integrates AccuKnox directly into the CI/CD pipeline, where security scans are triggered automatically as part of the build process. No additional installation is needed beyond pipeline configuration.

- **Plugin**: A plugin is an add-on module that integrates AccuKnox with a specific CI/CD tool. It simplifies the setup by allowing security scans to run within the pipeline with minimal configuration.

| **Pipeline/Tool**   | **Supported**                                                                                             |
|----------------------|---------------------------------------------------------------------------------------------------------|
| **Azure DevOps**     | [Workflow](https://help.accuknox.com/integrations/azure-dast/)                                          |
| **Google Cloud Build** | [Workflow](https://help.accuknox.com/integrations/google-dast/)                                       |
| **Harness**          | [Workflow](https://help.accuknox.com/integrations/harness-dast/)                                       |
| **Jenkins**          | [Plugin](https://help.accuknox.com/integrations/jenkins-container-scan/) / [Workflow](https://help.accuknox.com/integrations/jenkins-dast/) |
| **AWS CodePipeline** | [Workflow](https://help.accuknox.com/integrations/aws-dast/)                                           |
| **GitHub**           | [Plugin](https://github.com/marketplace?query=accuknox) / [Workflow](https://help.accuknox.com/how-to/github-iac-scan/) |
| **GitLab**           | [Plugin](https://gitlab.com/accu-knox/scan) / [Workflow](https://help.accuknox.com/integrations/gitlab-dast/) |
| **Bitbucket**        | [Plugin](https://bitbucket.org/accu-knox/scan) / [Workflow](https://help.accuknox.com/integrations/bitbucket-dast/) |

## Scanner Integrations

AccuKnox seamlessly integrates with leading, industry-recognized scanning tools to deliver comprehensive security coverage. By leveraging scanners such as OWASP ZAP, SonarQube, and other tools, it performs the following analyses:

- Scanning source code for vulnerabilities (SAST).

- Assessing running applications for security flaws (DAST).

- Identifying risks in dependencies (SCA).

- Evaluating cloud and container configurations for security gaps (IaC Scanning).

This agentless approach simplifies operations and ensures real-time security feedback without disrupting the development process.

![image-20241210-120638.png](./images/devsecops.png)

## Data Insights and Automation

AccuKnox consolidates all parsed data such as vulnerabilities, misconfigurations, and compliance violations into a unified dashboard. This enables quick visualization and actionable insights, allowing teams to prioritize and address issues effectively.

Key features include:

1. **Automated Alerts**: Instantly notifies teams of critical issues through email, Slack, or other communication channels.

2. **Ticket Creation**: Automatically logs issues into ticketing tools like **JIRA**, **ServiceNow**, **FreshService etc** streamlining incident tracking and resolution.

3. **Remediation Guidance**: Offers actionable recommendations to fix detected issues efficiently.

By integrating these capabilities, AccuKnox simplifies and strengthens DevSecOps implementation, empowering organizations to deliver secure, high-quality software at speed.
