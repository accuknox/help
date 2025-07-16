---
title: "Container image scanner"
weight: 4
summary: "Knoxctl can scan container images running on a perticular VM and submit the results to SaaS"
hide:
  - toc
---

# Container image scanner

AccuKnox offers a container image scanning solution designed to periodically inspect container images running on your machine.

## 🛠 Installation Guide

Follow these steps to deploy the container image scanner:

### 1. Create a Label

In the AccuKnox Control Plane, create a unique [**Label**](https://app.accuknox.com/settings/labels). This will be associated with the container image scan reports.

### 2. Generate a Token

From the AccuKnox Control Plane:

- Generate an [**Artifact Token**](https://app.accuknox.com/settings/tokens)
- Note down both the **Token** and your **Tenant ID**

### 3. Scan your machine

Use the following command to scan your machine:


```bash
knoxctl --artifactEndpoint="<url>" \
    --token="<authToken>" \
    --label="<label>" \
    --tenantId="<tenantId>"
```

Replace the parameters (`<tenantId>` , `<authToken>`, `<url>` and `<label>`) with the appropriate values.

if you want to scan the machine on a regular basis you can configure the scan to be run by crontab as follow

- run `crontab -e`, this command will open the contab file using your faviorite text editor
- add the following line at the end of the contab file

```
30 9 * * *  knoxctl --artifactEndpoint="<url>" --token="<authToken>" --label="<label>" --tenantId="<tenantId>"
```
Replace the parameters (`<tenantId>` , `<authToken>`, `<url>` and `<label>`) with the appropriate values.
The above will run the scan daily at 9:30am, you can change the execution time by modifying the cron expression


### ⚙️ Parameters:

| Variable  | Sample Value      | Description                |
| --------- | ----------------- | -------------------------- |
| tenantId  | 11                | AccuKnox Tenant ID         |
| authToken | eyJhbGc...        | AccuKnox Token {JWT}       |
| url       | cspm.accuknox.com | AccuKnox CSPM API Endpoint |
| label     | kubeshield        | AccuKnox Label             |


### ✅ Post-Installation

Once the scan is completed, results will be visible in the [**Findings**](https://app.accuknox.com/issues/findings/findings-summary) or [**Registry Scan**](https://app.accuknox.com/issues/registry-scan) sections within the AccuKnox Control Plane.

- Navigate to [**Issues -> Findings**](https://app.accuknox.com/issues/findings/findings-summary)
- Switch to **Findings** tab
- Select **Container Image Findings** & do **Group by** based on **Label Name**
- You should be able to see the data for the **Label** used in above command

---

