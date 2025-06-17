---
title: Integrating SAST in BitBucket CI/CD Pipeline
description: Integrate SonarQube SAST into Bitbucket CI/CD with AccuKnox to detect and fix code vulnerabilities before deployment.
---


# Integrating SAST in BitBucket CI/CD Pipeline

This guide explains how to integrate AccuKnox into your Bitbucket Pipelines to enhance code security using SonarQube for SAST scanning. It identifies potential vulnerabilities and sends the results to AccuKnox for further analysis and remediation.

## Pre-requisites

- Access to Bitbucket Pipelines

- AccuKnox Platform Access

- SonarQube Access

## Steps for Integration

**Step 1**: Log in to AccuKnox Navigate to Settings and select Tokens to create an AccuKnox token for forwarding scan results to SaaS. For details on generating tokens, refer to [How to Create Tokens](https://help.accuknox.com/how-to/how-to-create-tokens/?h=token "https://help.accuknox.com/how-to/how-to-create-tokens/?h=token").

**Step 2:** Add the following variables in your Bitbucket repository settings:. For details on configuring variables, refer to [How to Create CI/CD Variables in Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/ "https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/").

1. **ACCUKNOX_TOKEN**: AccuKnox API token for authorization.

2. **ACCUKNOX_TENANT**: Your AccuKnox tenant ID.

3. **ACCUKNOX_ENDPOINT**: The AccuKnox API URL (e.g., [cspm.demo.accuknox.com](http://cspm.demo.accuknox.com/ "http://cspm.demo.accuknox.com")).

4. **ACCUKNOX_LABEL**: The label for your scan.

5. **SONAR_TOKEN**: Your SonarQube API token.

6. **SONAR_HOST_URL**: The URL of your SonarQube server.

7. **SONAR_PROJECT_KEY**: The project key for your SonarQube project.

**Step 3:** Configure Bitbucket Pipeline

Use the following YAML configuration for your `bitbucket-pipelines.yml` file:

```yaml
pipelines:
  branches:
    main:
    - step:
        name: AccuKnox SAST
        script:
          - pipe: accu-knox/scan:1.0.0
            variables:
              SCAN_TYPE: SAST
              INPUT_SOFT_FAIL: "true"
              SONAR_TOKEN: ${SONAR_TOKEN}
              SONAR_HOST_URL: ${SONAR_HOST_URL}
              SONAR_PROJECT_KEY: ${SONAR_PROJECT_KEY}
              ACCUKNOX_TOKEN: ${ACCUKNOX_TOKEN}
              ACCUKNOX_TENANT: ${ACCUKNOX_TENANT}
              ACCUKNOX_ENDPOINT: ${ACCUKNOX_ENDPOINT}
              ACCUKNOX_LABEL: ${ACCUKNOX_LABEL}
        services:
          - docker
```

## Initial CI/CD Pipeline Without AccuKnox Scan

Initially, the CI/CD pipeline does not include the AccuKnox scan. Vulnerabilities in the code could go unnoticed without security checks.

## CI/CD Pipeline After AccuKnox Integration

After integrating AccuKnox into the pipeline, pushing changes triggers the SonarQube scan, which sends its results to AccuKnox. AccuKnox helps identify potential code vulnerabilities.

![image-20241209-123435.png](./images/bitbucket-sast/1.png)

![image-20241209-123500.png](./images/bitbucket-sast/2.png)

## View Results in AccuKnox SaaS

**Step 1**: After the workflow completes, navigate to the AccuKnox SaaS dashboard.

**Step 2**: Go to **Issues** > **Findings** and select **SAST Findings** to see identified vulnerabilities.

![image-20241126-033109.png](./images/bitbucket-sast/3.png)

**Step 3**: Click on a vulnerability to view more details.

![image-20241126-033149.png](./images/bitbucket-sast/4.png)

**Step 4**: Fix the Vulnerability

Follow the instructions in the Solutions tab to fix the vulnerability

![image-20241126-033211.png](./images/bitbucket-sast/5.png)

**Step 5**: Create a Ticket for Fixing the Vulnerability

Create a ticket in your issue-tracking system to address the identified vulnerability.

![image-20241126-033237.png](./images/bitbucket-sast/6.png)

**Step 6**: Review Updated Results

- After fixing the vulnerability, rerun the CI/CD pipeline.

- Navigate to the AccuKnox SaaS dashboard and verify that the vulnerability has been resolved.

## Conclusion

Integrating SonarQube with AccuKnox in Bitbucket Pipelines helps detect and remediate vulnerabilities early in the development lifecycle, ensuring a secure deployment environment.
