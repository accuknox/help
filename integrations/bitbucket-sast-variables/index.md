---
title: Bitbucket Static Application Security Testing (SAST) Scanning Variables
description: Variables used in the Bitbucket CI/CD pipeline for Static Application Security Testing (SAST) scanning
---

# Bitbucket Static Application Security Testing (SAST) Scanning Variables

The Static Application Security Testing (SAST) scanning section of the Bitbucket CI/CD pipeline integrates with SonarQube for analyzing code quality and security vulnerabilities. The scan results are then pushed to the AccuKnox platform for further analysis and tracking.

Here’s the table that outlines the inputs and their descriptions, along with default values:


| **Input**            | **Description**                                    | **Default Value**           |
|-----------------------|----------------------------------------------------|-----------------------------|
| **SONAR_TOKEN**       | Token for authenticating with SonarQube.           | N/A (Required)             |
| **SONAR_HOST_URL**    | The SonarQube host URL.                            | N/A (Required)             |
| **SONAR_PROJECT_KEY** | The project key in SonarQube.                      | N/A (Required)             |
| **ACCUKNOX_TOKEN**    | Token for authenticating with the CSPM panel.      | N/A (Required)             |
| **ACCUKNOX_ENDPOINT** | The URL of the CSPM panel to push the scan results to. | cspm.demo.accuknox.com      |
| **ACCUKNOX_LABEL**    | Label created in AccuKnox SaaS for associating scan results. | N/A (Required)             |
