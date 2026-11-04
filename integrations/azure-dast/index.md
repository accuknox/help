---
title: AccuKnox DAST with Azure DevOps
description: Integrate AccuKnox DAST with Azure DevOps to automate the detection and resolution of runtime vulnerabilities in web applications.
---

# AccuKnox DAST with Azure DevOps

To demonstrate the benefits of incorporating AccuKnox DAST into an Azure DevOps CI/CD pipeline for enhanced security, this document outlines the steps to configure the integration, run DAST scans, and view results in the AccuKnox SaaS platform.

![image](https://i.ibb.co/xKgxF9KK/image.png)

## **Prerequisites**

- Access to an Azure DevOps project.

- Access to the AccuKnox platform.

- A configured Azure DevOps agent for pipeline execution.

## **Steps for Integration**

### **Step 1: Install the AccuKnox DAST Extension**

1.  Navigate to the Azure DevOps Marketplace.

2.  Search for **AccuKnox DAST** and click **Get it free** to install the extension in your Azure DevOps organization.
![image-20250108-110253.png](./images/azure-devops/1.png)

3.  Select an Azure organization and click on **Install**.
![image-20250108-110409.png](./images/azure-devops/2.png)

4.  Once installed, the AccuKnox DAST extension will be ready to use in your pipelines.

![image-20250108-110441.png](./images/azure-devops/3.png)

### **Step 2: Generate AccuKnox Token**

1.  Log in to AccuKnox.

2.  Navigate to **Settings** > **Tokens** and create an AccuKnox token.

3.  Copy the generated token and store it securely for later use. For detailed steps, refer to [How to Create Tokens](https://help.accuknox.com/how-to/how-to-create-tokens/ "https://help.accuknox.com/how-to/how-to-create-tokens/").

### **Step 3: Configure Variables in Azure DevOps**

1.  Navigate to your Azure DevOps project.

2.  Go to **Project Settings** > **Pipelines** > **Library** > **+ Variable Group**.

3.  Add the following variables:

| **Secret Name**    | **Description**                      |
| ------------------ | ------------------------------------ |
| `targetUrl`        | URL of the web application to scan.  |
| `accuknoxEndpoint` | URL of the AccuKnox CSPM API.        |
| `accuknoxToken`    | AccuKnox API token.                  |
| `accuknoxLabel`    | Label to group findings in AccuKnox. |

### **Step 4: Add AccuKnox DAST Task to the Pipeline**

1.  Open your Azure DevOps pipeline YAML file or create a new one.

2.  Add the following task under the `steps` block:

```
steps:
  - task: accuknox-dast@2.0.0
    inputs:
      targetURL: $(TARGET_URL)
      accuknoxEndpoint: $(ACCUKNOX_ENDPOINT)
      accuknoxToken: $(ACCUKNOX_TOKEN)
      accuknoxLabel: $(ACCUKNOX_LABEL)
      scanType: $(SCAN_TYPE)
      qualityGate: $(QUALITY_GATE)

```

### **Step 5: Run the Pipeline**

1.  Trigger the pipeline manually or through a code change.

2.  Monitor the pipeline logs to verify that the AccuKnox DAST task is running successfully.
![image-20250108-114305.png](./images/azure-devops/4.png)

## View Results in AccuKnox SaaS

**Step 1**: After the workflow completes, navigate to the AccuKnox SaaS dashboard.

**Step 2**: Go to Issues > Findings and select DAST Findings to see identified vulnerabilities.
![image-20250108-114539.png](./images/azure-devops/5.png)

**Step 3**: Click on a vulnerability to view more details.
![image-20250108-114612.png](./images/azure-devops/6.png)

**Step 4**: Fix the Vulnerability

Follow the instructions in the Solutions tab to fix the vulnerability.
![image-20250108-114659.png](./images/azure-devops/7.png)

**Step 5**: Create a Ticket for Fixing the Vulnerability

Create a ticket in your issue tracking system to address the identified vulnerability.
![image-20250108-114752.png](./images/azure-devops/8.png)

**Step 6:** Review Updated Results

- After fixing the vulnerability, rerun the Azure pipeline.

- Navigate to the AccuKnox SaaS dashboard and verify that the vulnerability has been resolved.

### **Conclusion**

Integrating AccuKnox DAST with Azure DevOps pipelines ensures continuous security by identifying vulnerabilities during the build process. It provides visibility into security issues and enhances deployment safety. AccuKnox DAST supports a wide range of CI/CD tools, making it a versatile choice for secure DevOps practices.

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
