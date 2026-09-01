---
title: Bitbucket Container Scanning Variables
description: Configure Bitbucket CI/CD with AccuKnox container scanning variables to identify vulnerabilities in Docker images.
---

# Bitbucket Container Scanning Variables

The container scanning section of the Bitbucket CI/CD pipeline is designed to integrate with AccuKnox to scan Docker images for security vulnerabilities.

Here’s the table that outlines the inputs and their descriptions, along with default values:

| Input Value         | Description                                                         | Default Value                                |
|---------------------|---------------------------------------------------------------------|---------------------------------------------|
| DOCKERFILE_CONTEXT  | The context of the Dockerfile to use for building the image.        | Dockerfile                                  |
| REPOSITORY_NAME     | The name of the Docker image repository.                           | N/A (Required)                              |
| TAG                 | The tag for the Docker image.                                      | "$CI_JOB_ID"                                |
| SEVERITY            | Allows selection of severity level for the scan. Options include UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL. | UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL           |
| INPUT_SOFT_FAIL     | Do not return an error code if there are failed checks.            | true                                       |
| ACCUKNOX_TOKEN      | The token for authenticating with the CSPM panel.                 | N/A (Required)                              |
| ACCUKNOX_ENDPOINT   | The URL of the CSPM panel to push the scan results to.            | cspm.demo.accuknox.com                      |
| ACCUKNOX_LABEL      | The label created in AccuKnox SaaS for associating scan results.  | N/A (Required)                              |
