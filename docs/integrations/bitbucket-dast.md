---
title: Integrating DAST in BitBucket CI/CD Pipeline
description: See how to integrate AccuKnox and Dynamic Application Security Testing (DAST) into a Bitbucket pipeline to identify and resolve vulnerabilities in a web application.
---

# Integrating DAST in BitBucket CI/CD Pipeline

This guide demonstrates how to integrate AccuKnox and Dynamic Application Security Testing (DAST) into a Bitbucket pipeline to identify and resolve vulnerabilities in a web application. We also support Authenticated and MFA DAST, ensuring comprehensive security coverage for your applications. Below, we outline the process and outcomes.

## Pre-requisites

- Access to Bitbucket Pipelines

- AccuKnox Platform Access

## Steps for Integration

**Step 1**: Log in to AccuKnox Navigate to Settings and select Tokens to create an AccuKnox token for forwarding scan results to SaaS. For details on generating tokens, refer to [How to Create Tokens](https://help.accuknox.com/how-to/how-to-create-tokens/?h=token "https://help.accuknox.com/how-to/how-to-create-tokens/?h=token").

**Step 2:** Add the following variables in your Bitbucket repository settings: For details on configuring variables, refer to [How to Create CI/CD Variables in Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/ "https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/").

1. **ACCUKNOX_TOKEN**: AccuKnox API token for authorization.

2. **ACCUKNOX_TENANT**: Your AccuKnox tenant ID.

3. **ACCUKNOX_ENDPOINT**: The AccuKnox API URL (e.g., [cspm.demo.accuknox.com](http://cspm.demo.accuknox.com/ "http://cspm.demo.accuknox.com")).

4. **ACCUKNOX_LABEL**: The label for your scan.

**Step 3:** Configure Bitbucket Pipeline

Use the following YAML configuration for your `bitbucket-pipelines.yml` file:

```yaml
pipelines:
  branches:
    dast:
    - step:
        name: Accuknox DAST
        services:
          - docker
        script:
          - echo "Starting DAST scan..."
          - |
            docker run --rm -v $(pwd):/zap/wrk -t zaproxy/zap-stable zap-baseline.py -t https://juice-shop.herokuapp.com/ -J results.json -I
          - echo "Uploading results..."
          - |
            curl --location --request POST "https://${ACCUKNOX_ENDPOINT}/api/v1/artifact/?tenant_id=${ACCUKNOX_TENANT}&data_type=ZAP&label_id=${ACCUKNOX_LABEL}&save_to_s3=false" --header "Tenant-Id: ${ACCUKNOX_TENANT}" --header "Authorization: Bearer ${ACCUKNOX_TOKEN}" --form 'file=@"results.json"'
```

## Initial CI/CD Pipeline Without AccuKnox Scan

Initially, the CI/CD pipeline does not include the AccuKnox scan. When you push changes to the repository, no security checks are performed, potentially allowing security issues in the application.

## CI/CD Pipeline After AccuKnox Scan Integration

After integrating AccuKnox into your CI/CD pipeline, the next push triggers the CI/CD pipeline. The AccuKnox scan identifies potential vulnerabilities in the application.

![alt](./images/bitbucket-dast/1.png)

## View Results in AccuKnox SaaS

**Step 1**: After the workflow completes, navigate to the AccuKnox SaaS dashboard.

**Step 2**: Go to **Issues** > **Findings** and select **DAST Findings** to see identified vulnerabilities.

![alt](./images/bitbucket-dast/2.png)

**Step 3**: Click on a vulnerability to view more details.

![alt](./images/bitbucket-dast/3.png)

**Step 4**: Fix the Vulnerability

Follow the instructions in the Solutions tab to fix the vulnerability

![alt](./images/bitbucket-dast/4.png)

**Step 5**: Create a Ticket for Fixing the Vulnerability

Create a ticket in your issue-tracking system to address the identified vulnerability.

![alt](./images/bitbucket-dast/5.png)

**Step 6**: Review Updated Results

- After fixing the vulnerability, rerun the CI/CD pipeline.

- Navigate to the AccuKnox SaaS dashboard and verify that the vulnerability has been resolved.

## Conclusion

Integrating AccuKnox and DAST into Bitbucket pipelines enhances application security by identifying vulnerabilities early in the CI/CD process. This seamless integration ensures secure deployments and reduces risks in production environments.
