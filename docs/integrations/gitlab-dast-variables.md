---
title: GitLab DAST Variables
description: Variables for GitLab CI/CD pipeline to scan web apps for security vulnerabilities using AccuKnox DAST integration.
---

The Dynamic Application Security Testing (DAST) scanning section of the GitLab CI/CD pipeline integrates with AccuKnox for scanning live web applications for security vulnerabilities.

Here’s the table that outlines the inputs and their descriptions, along with default values:

| Input               | Description                                                                                   | Default Value             |
|---------------------|-----------------------------------------------------------------------------------------------|---------------------------|
| STAGE              | Specifies the pipeline stage.                                                                 | test                      |
| TARGET_URL         | The URL of the web application to scan.                                                       | N/A (Required)            |
| SEVERITY_THRESHOLD | The minimum severity level (e.g., High, Medium, Low, Informational) that will cause the pipeline to fail if present in the report. | High                      |
| DAST_SCAN_TYPE     | Type of ZAP scan to run: 'baseline' or 'full-scan'.                                            | baseline                  |
| INPUT_SOFT_FAIL    | Do not return an error code if there are failed checks.                                        | true (boolean)            |
| ACCUKNOX_TOKEN     | The token for authenticating with the CSPM panel.                                             | N/A (Required)            |
| ACCUKNOX_TENANT    | ID of the tenant associated with the CSPM Panel panel.                                        | N/A (Required)            |
| ACCUKNOX_ENDPOINT  | URL of the CSPM panel to push the scan results to.                                            | cspm.demo.accuknox.com    |
| ACCUKNOX_LABEL     | Label created in AccuKnox SaaS for associating scan results.                                  | N/A (Required)            |
