---
title: GCP Account Onboarding
description: Step-by-step guide for onboarding GCP (Google Cloud Platform) accounts to AccuKnox SaaS for automated security and compliance monitoring.
---

# GCP Account Onboarding

Here, we will see the steps to onboard a GCP cloud account to the AccuKnox SaaS platform.

!!! note
    Ensure the following API Libraries are enabled in your GCP account before onboarding to AccuKnox SaaS:

1. Compute Engine API
2. Identity and Access Management (IAM) API
3. Cloud Resource Manager API
4. Cloud Functions API
5. KMS API
6. Kubernetes API
7. Cloud SQL Admin API

For GCP there is a requirement for IAM Service Account Access.

**Step 1:** Log into your Google Cloud console, navigate to IAM & Admin → Roles, and click “Create custom role”

![image](images/gcp/gcp-0.png)

**Step 2:**  Name the Role and Click “Add Permission”

![image](images/gcp/gcp-1.png)

**Step 3:**  Use the Service: storage filter then value as “storage.buckets.getIamPolicy“

![image](images/gcp/gcp-2.png)

**Step 4:** Choose the permission and Click “Add“ then Click Create in the same page.

![image](images/gcp/gcp-3.png)
![image](images/gcp/gcp-3-0.png)

**Step 5:**  In the Navigation Panel, navigate to IAM Admin > Service Accounts.

![image](images/gcp/gcp-4.png)

**Step 6:** Click on "Create Service Account"

![image](images/gcp/gcp-5.png)

**Step 7:** Enter any name that you want on Service Account Name.

**Step 8:** Click on Continue.

![image](images/gcp/gcp-6.png)

**Step 9:** Select the role: Project > Viewer and click Add another Role.

![image](images/gcp/gcp-7.png)

**Step 10:** Click **Add Another Role**, choose **Custom**, then select the created custom role.

![image](images/gcp/gcp-8.png)

**Step 11:** Click on “Continue“ and ”Done”

![image](images/gcp/gcp-9.png)

**Step 12:** Go to the created Service Account, click on it, then navigate to the **Keys** section.

![image](images/gcp/gcp-10.png)

**Step 13:** Click the “Add key“ button and “Create new key “ . Chosen Key type should be JSON format.

![image](images/gcp/gcp-11.png)

**Step 14:** Click the “Create“ button it will automatically download the JSON key.

## From AccuKnox SaaS UI

**Step 1:** Go to the AccuKnox SaaS. Navigate to the “Settings” → “Cloud Accounts” then “Onboard Account”.

![image](images/gcp/gcp-saas-0.png)
![image](images/gcp/gcp-saas-01.png)

**Step 2:** Select the “Google Cloud Platform” options and click "Next"

![image](images/gcp/gcp-saas-1.png)

**Step 3:** Select or create a label and Tags that will be associated with this Cloud Account

![image](images/gcp/gcp-saas-2.png)

**Step 4:** Follow the instructions on the next page

!!! note
    Ensure to enter the "Project ID" before copying and adding the Terraform script

![image](images/gcp/gcp-saas-3.png)

**Step 5:**  Scroll down and enter the “Client Email”(The Service Account mail ID) and  “Private Key” from the downloaded File.
Copy paste the entire downloaded file into the ”Private Key” field . Then Click “Connect“

![image](images/gcp/gcp-saas-3-0.png)

The cloud account has been onboarded successfully

![image](images/gcp/gcp-saas-4.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
