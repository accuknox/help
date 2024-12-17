---
title: Quay Registry Onboarding
description: Steps to onboard Quay Registry on AccuKnox for scanning and monitoring container images for vulnerabilities and compliance.
---

# Quay Registry Onboarding
Red Hat Quay is a fully managed hosted container image registry that offers both public and private repository options and an automated lifecycle of your containerized artifacts.

## Pre-requisites

- A valid [Quay.io](http://quay.io/ "http://Quay.io") account

- Container Images stored in the account

- User creds with at least image pull permission

![image-20241216-115454.png](./images/quay/1.png)

## **Steps to Onboard Quay Registry on AccuKnox**

**Step 1:** In the **AccuKnox dashboard**, under **Issues**, click on **"Registry Scan"**

- Alternatively you can go to "Settings → Integration → Registry Scan"

Now, click on **"Add Registry"**

![image-20241216-115621.png](./images/quay/2.png)

**Step 2:** Give the registry name, select **Label**, and select **"Quay"** from the **Registry type** dropdown. Then, provide the user credentials.

![image-20241216-115231.png](./images/quay/3.png)

Provide the **Tag pattern** and schedule a time( using the cron expression) for the scanning. If you need to trigger the scan after saving, click the **"Trigger scan on save"** checkbox.

**Step 3:** After providing all the information, click on **"Test Connection"**, it should show **"Registry Tested Successfully"**.

Now, click on **Save**.

![image-20241216-120033.png](./images/quay/4.png)

After saving the registry, the scan will start based on the scheduled time, if Trigger scan on save is checked the scan will start right after save. After saving the scan user will be redirected to **Settings** -> **Integrations** -> **Registry**. Here, we can see the list of onboarded registries and their details.

![image-20241216-115319.png](./images/quay/5.png)

Alternatively, you can click on "**View Registry Scan**" from the list view and this will redirect to **Issues → Registry Scan**

Once the scanning is completed, we can see the scan results

![image-20241216-120422.png](./images/quay/6.png)

Under **"Findings"**, you can find the scanned registry.

To view the details of your registry, you can use filters such as **"registry_type"**, and then select the **"quay"** registry you can also use the filter **"registry_name"** and provide the name of your registry.

![image-20241216-121542.png](./images/quay/7.png)

By clicking on the repositories, we can get more details about the scan results.

![image-20241216-121813.png](./images/quay/8.png)
