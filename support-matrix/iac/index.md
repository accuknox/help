---
title: Accuknox IaC Security Support Matrix
description: AccuKnox provides robust IaC security scanning, analyzing misconfigurations and compliance issues for various formats and file types.
---

# Accuknox IaC Security Support Matrix

Accuknox provides comprehensive support for Infrastructure as Code (IaC) security scanning, enabling users to analyze their IaC files for misconfigurations, vulnerabilities, and compliance issues. Below is a detailed support matrix outlining the supported formats, file types, and additional features.

## **1. Supported IaC Frameworks**

| IaC Format         | Description                                                  |
|---------------------|--------------------------------------------------------|
| Terraform           | Supports both HCL and JSON configurations.            |
| Terraform Plan      | Scans Terraform execution plans.                      |
| Terraform JSON      | Supports JSON-based Terraform configurations.         |
| Kubernetes YAML     | Scans Kubernetes manifests for security issues.       |
| Helm Charts         | Scans Helm templates for Kubernetes workloads.        |
| Docker File         | Analyzes Dockerfile for security best practices.      |
| CloudFormation      | YAML and JSON templates are supported.                |
| Kustomize           | Scans Kustomize overlays and resources.               |
| Serverless Framework| Analyzes serverless configurations for compliance and security. |
| Ansible             | Covers playbooks, roles, and tasks.                   |
| Bicep               | Supports Microsoft Bicep templates.                   |
| ARM                 | Analyzes Azure Resource Manager templates.            |
| AWS CDK             | Scans AWS Cloud Development Kit projects for misconfigurations. |

## **2. Integration Support**

| Integration         | Description                                            |
|---------------------|--------------------------------------------------------|
| CI/CD Pipelines     | Supports Jenkins, GitHub Actions, GitLab CI/CD, etc.  |
| Extensions          | GitHub, GitLab, Bitbucket, Jenkins.                   |
| Accuknox UI         | GitLab, GitHub, Bitbucket.                            |

## **3. Features and Coverage**

| Feature                 | Description                                        |
|--------------------------|----------------------------------------------------|
| Misconfiguration Detection | Identifies insecure configurations.             |
| Secrets Detection        | Scans for hardcoded secrets like API keys, tokens, and passwords. |
| Drift Detection          | Identifies configuration drift from live environments. |

Accuknox’s IaC support ensures robust security and compliance checks, empowering teams to identify and remediate issues early in the development lifecycle.
