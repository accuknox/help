---
title: Bitbucket Infrastructure as Code (IaC) Scanning Variables
description: Variables used in the Bitbucket CI/CD pipeline for Infrastructure as Code (IaC) scanning
---

# Bitbucket Infrastructure as Code (IaC) Scanning Variables

The Infrastructure as Code (IaC) scanning section of the Bitbucket CI/CD pipeline is designed to integrate with AccuKnox to scan infrastructure code files (e.g., Terraform) for security vulnerabilities.

Here’s the table that outlines the inputs and their descriptions, along with default values:

| Input Value        | Description                                                                 | Default Value                |
|--------------------|-----------------------------------------------------------------------------|------------------------------|
| **INPUT_FILE**     | Specify a file for scanning (e.g., ".tf" for Terraform). Cannot be used with directory input. | "" (empty, optional)         |
| **INPUT_DIRECTORY**| Directory with infrastructure code and/or package manager files to scan.    | "." (current directory)      |
| **INPUT_COMPACT**  | Do not display code blocks in the output.                                   | true (boolean)               |
| **INPUT_QUIET**    | Display only failed checks.                                                 | true (boolean)               |
| **INPUT_SOFT_FAIL**| Do not return an error code if there are failed checks.                     | true (boolean)               |
| **INPUT_FRAMEWORK**| Run only on a specific infrastructure (Kubernetes or Terraform).            | "" (empty, optional)         |
| **ACCUKNOX_TOKEN** | The token for authenticating with the CSPM panel.                           | N/A (Required)               |
| **ACCUKNOX_ENDPOINT** | URL of the CSPM panel to push the scan results to.                       | cspm.demo.accuknox.com       |
| **ACCUKNOX_LABEL** | Label created in AccuKnox SaaS for associating scan results.                | N/A (Required)               |
