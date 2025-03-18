---
title: GitLab SAST Variables
description: Configure GitLab CI/CD variables for SAST with AccuKnox to automate code vulnerability detection and ensure secure, high-quality code deployment.
---


The Static Application Security Testing (SAST) scanning section of the GitLab CI/CD pipeline integrates with SonarQube for analyzing code quality and security vulnerabilities. The scan results are then pushed to the AccuKnox platform for further analysis and tracking.

| Input              | Description                                                | Default Value               |
|--------------------|------------------------------------------------------------|-----------------------------|
| STAGE             | Specifies the pipeline stage.                              | test                        |
| SONAR_TOKEN       | Token for authenticating with SonarQube.                   | N/A (Required)             |
| SONAR_HOST_URL    | The SonarQube host URL.                                    | N/A (Required)             |
| SONAR_PROJECT_KEY | The project key in SonarQube.                              | N/A (Required)             |
| ACCUKNOX_TOKEN    | Token for authenticating with the CSPM panel.              | N/A (Required)             |
| ACCUKNOX_TENANT   | The ID of the tenant associated with the CSPM panel.       | N/A (Required)             |
| ACCUKNOX_ENDPOINT | The URL of the CSPM panel to push the scan results to.     | cspm.demo.accuknox.com     |
| ACCUKNOX_LABEL    | Label created in AccuKnox SaaS for associating scan results. | N/A (Required)             |
