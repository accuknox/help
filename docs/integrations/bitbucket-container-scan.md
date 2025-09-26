---
title: Bitbucket Container Scan
description: Integrate AccuKnox with Bitbucket CI/CD to scan and fix container image vulnerabilities before deployment to ensure Bitbucket Container Security.
---

# Enhancing Docker Image Security in Bitbucket Pipelines

This guide demonstrates integrating AccuKnox into a Bitbucket pipeline to identify and remediate vulnerabilities in Docker images. Below, we compare the state of the pipeline before and after integrating AccuKnox, highlighting the security improvements.

### Prerequisites

Before beginning, ensure the following:

- A **Bitbucket repository** with **Pipelines enabled**.

- Access to **AccuKnox**

### Integration Steps

#### Step 1: Generate AccuKnox API Token

Log in to AccuKnox. Navigate to Settings and select Tokens to create an AccuKnox token to forward scan results to AccuKnox. For details on generating tokens, refer to [How to Create Tokens](https://help.accuknox.com/how-to/how-to-create-tokens/?h=token "https://help.accuknox.com/how-to/how-to-create-tokens/?h=token").

#### Step 2: Configure Bitbucket Pipeline Variables

- Navigate to your Bitbucket repository.

- Go to **Repository Settings > Repository Variables** and click **Add Variable**. Refer to [**How to Create CI/CD Variables in Bitbucket**](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/ "https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/").

| **Name**             | **Description**                                                                        |
| -------------------- | -------------------------------------------------------------------------------------- |
| `ACCUKNOX_ENDPOINT`  | The URL of the CSPM panel to push the scan results to (e.g., `cspm.demo.accuknox.com`) |
| `ACCUKNOX_TENANT_ID` | The ID of the tenant associated with the CSPM panel                                    |
| `ACCUKNOX_TOKEN`     | Token for authenticating with the AccuKnox CSPM panel                                  |
| `ACCUKNOX_LABEL`     | Label to categorize or tag the scan results                                            |

The label used to categorize and identify scan results in AccuKnox. [Create a new label](https://help.accuknox.com/how-to/how-to-create-labels/ "https://help.accuknox.com/how-to/how-to-create-labels/") if it is not available

#### Step 3: Define the Bitbucket Pipelines YAML File

**Inputs for AccuKnox Container Scanning**

| **Input**           | **Description**                                                                                           | **Default Value**                  |
| ------------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| `IMAGE_NAME`        | Docker image name.                                                                                        | N/A (**Required**)                 |
| `TAG`               | The tag for the Docker image.                                                                             | N/A (**Required**)                 |
| `SEVERITY`          | Allows selection of severity level for the scan. Options: `UNKNOWN`, `LOW`, `MEDIUM`, `HIGH`, `CRITICAL`. | `UNKNOWN,LOW,MEDIUM,HIGH,CRITICAL` |
| `SOFT_FAIL`         | Do not return an error code if there are failed checks.                                                   | `true`                             |
| `ACCUKNOX_TENANT`   | The ID of the tenant associated with the CSPM panel.                                                      | N/A (**Required**)                 |
| `ACCUKNOX_ENDPOINT` | The URL of the CSPM panel to push the scan results to.                                                    | N/A (**Required**)                 |
| `ACCUKNOX_LABEL`    | The label created in AccuKnox SaaS for associating scan results.                                          | N/A (**Required**)                 |
| `ACCUKNOX_TOKEN`    | The token for authenticating with the CSPM panel.                                                         | N/A (**Required**)                 |

Create or modify your `bitbucket-pipelines.yml` as follows:

```yaml
pipelines:
  branches:
    main:
    - step:
        name: Set Variables and Scan
        services:
          - docker
        script:
          - export IMAGE_NAME="bitbucket"
          - export TAG="test"
          - docker build -t $IMAGE_NAME:$TAG .
          - pipe: accu-knox/scan:2.0.0
            variables:
              SCAN_TYPE: CONTAINER
              SOFT_FAIL: "true"
              IMAGE_NAME: $IMAGE_NAME
              TAG: $TAG
              ACCUKNOX_TOKEN: ${ACCUKNOX_TOKEN}
              ACCUKNOX_TENANT: ${ACCUKNOX_TENANT}
              ACCUKNOX_ENDPOINT: ${ACCUKNOX_ENDPOINT}
              ACCUKNOX_LABEL: ${ACCUKNOX_LABEL}
```

### After AccuKnox Integration:

- **Workflow Enhancements**:

  - The pipeline scans Docker images during the build process.

  - Critical vulnerabilities halt the pipeline, ensuring only secure images are deployed.

- **Outcome**:

  - Vulnerabilities are identified and remediated before the image reaches production.

  - Secure images are pushed to the registry with confidence.

![image-20250502-054152.png](./images/bitbucket-container-scan/1.png)

### View Results in AccuKnox SaaS

**Step 1:** Once the scan is complete, the user can go into the AccuKnox SaaS and navigate to Issues → RegistryScan, where they can find their repository name and select it to see the associated findings
![image-20250502-054502.png](./images/bitbucket-container-scan/2.png)

**Step 2:** After clicking on the image name, the user will see the metadata for the image that was built during the workflow execution.
![image-20250502-054526.png](./images/bitbucket-container-scan/3.png)

**Step 3:** In the `Findings` section, the user can see the image-specific vulnerabilities in a list manner that contains relevant information. These findings will also be available in the `Issues → Findings` section, where the user can manage these findings with others.
![image-20250502-054553.png](./images/bitbucket-container-scan/4.png)

**Step 4:** The `Resources` section contains information about packages and modules that were used to build the code base into a container image.
![image-20250502-054621.png](./images/bitbucket-container-scan/5.png)

**Step 5:** The user can see the scan history of every scan that happened while triggering the workflow.
![image-20250502-054644.png](./images/bitbucket-container-scan/6.png)

### Conclusion

Integrating AccuKnox into Bitbucket pipelines improves Docker image security by detecting and mitigating vulnerabilities during the development lifecycle. This ensures that only secure images are deployed, reducing risks in production environments.
