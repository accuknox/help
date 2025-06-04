---
title: CSPM Pre-requisite for GCP
description: Pre-requisites and setup instructions for onboarding GCP cloud accounts to AccuKnox SaaS for continuous compliance and security checks.
---

# CSPM Pre-requisite for GCP

When the AccuKnox control plane is hosted in a cloud environment, scanning is performed using Cloud account Readonly Access permissions.

![image](images/gcp-arch.png)

**Note:**
Make sure the Below API Library is enabled in your GCP Account for onboarding into AccuKnox SaaS:

1. Compute Engine API
2. Identity and Access Management (IAM) API
3. Cloud Resource Manager API
4. Cloud Functions API
5. KMS API
6. Kubernetes API
7. Cloud SQL Admin API

For GCP there is a requirement for IAM Service Account Access.

**Step 1:**  Log into your Google Cloud console and navigate to  IAM & Admin choose “Roles“ and Click “Create Role“

![image](images/gcp/gcp-0.png)

**Step 2:**  Name the “Role” and Click “Add Permission”

![image](images/gcp/gcp-1.png)

**Step 3:**  Use the Service: storage filter then value as “storage.buckets.getIamPolicy“

![image](images/gcp/gcp-2.png)

**Step 4:** Choose the permission and Click “Add“ then Click Create in the same page.

![image](images/gcp/gcp-3.png)

**Step 5:**  In the Navigation Panel, navigate to IAM Admin > Service Accounts.

![image](images/gcp/gcp-4.png)

**Step 6:** Click on "Create Service Account"

![image](images/gcp/gcp-5.png)

**Step 7:** Enter any name that you want on Service Account Name.

**Step 8:** Click on Continue.

![image](images/gcp/gcp-6.png)

**Step 9:** Select the role: Project > Viewer and click Add another Role.

![image](images/gcp/gcp-7.png)

**Step 10:** Click “Add Another Role” Choose “Custom“ Select the created Custom Role.

![image](images/gcp/gcp-8.png)

**Step 11:** Click on “Continue“ and ”Done”

![image](images/gcp/gcp-9.png)

**Step 12:** Go to the created Service Account, click on that Service Account navigate to the “Keys“ section.

![image](images/gcp/gcp-10.png)

**Step 13:** Click the “Add key“ button and “Create new key “ . Chosen Key type should be JSON format.

![image](images/gcp/gcp-11.png)

**Step 14:** Click the “Create“ button it will automatically download the JSON key.

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
