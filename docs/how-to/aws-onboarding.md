---
title: AWS Account onboarding
description: Step-by-step instructions for onboarding an AWS cloud account to AccuKnox SaaS for automated security management.
---

# AWS Account Onboarding

In this section we can find the steps to onboard an AWS cloud account to the AccuKnox SaaS platform.

![image](https://i.ibb.co/PzbPnkxj/image.png)

## **AWS IAM User Creation**

Follow these steps to provide a user with appropriate read access:

**Step 1:** Navigate to IAM → IAM Users and click on Create user

![image](images/iam-user-0.png)

**Step 2:** Give a username to identify the user

![image](images/iam-user-1.png)

**Step 3:** In the "Set Permissions" screen:

a. Select "Attach policies directly"

b. Search "ReadOnly", Filter by Type: "AWS managed - job function" and select the policy

![image](images/iam-user-2.png)

c. Search "SecurityAudit", Filter by Type: "AWS managed - job function" and select the policy

![image](images/iam-user-3.png)

**Step 4:** Finish creating the user. Click on the newly created user and create the Access key and Secret Key from the Security Credentials tab to be used in the AccuKnox panel

![image](images/iam-user-4.png)

## **AWS Onboarding**

In this example we are onboarding AWS account using the Access Keys method.

**Step 1:** To onboard Cloud Account Navigate to *Settings → Cloud Accounts*

![image](images/cloud-onboarding-1.png)

**Step 2:** In the Cloud Account Page select *Onboard Account* option

![image](images/cloud-onboarding-2.png)

**Step 3:** Select the AWS option

![image](images/cloud-onboarding-3.png)

**Step 4:** In the next Screen select the labels and Tags field from the dropdown Menu.

![image](images/cloud-onboarding-4.png)

**Step 5:** After assigning a label and tag, on the next screen provide the AWS account’s Access Key and Secret Access Key ID and select the region of the AWS account.

![image](images/cloud-onboarding-5.png)
**Follow the given instruction to the bottom...**
![image](images/cloud-onboarding-6.png)

**Step 6:** The AWS account should have been added to AccuKnox using the Access Key method. You can view the onboarded cloud account by navigating to Settings → Cloud Accounts.

![image](images/cloud-onboarding-7.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
