---
title: AWS Account onboarding
description: Step-by-step instructions for onboarding an AWS cloud account to AccuKnox SaaS for automated security management.
---

# AWS Account onboarding

In this section we can find the steps to onboard an AWS cloud account to the AccuKnox SaaS platform.

## **AWS IAM User Creation**

Please follow the following steps to provide a user with appropriate read access:

**Step 1:** Navigate to IAM → Users and click on Add Users

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

**Step 1:** To onboard Cloud Account Navigate to *Settings→cloud Accounts*

![image](images/cloud-onboarding-1.png)

**Step 2:** In the Cloud Account Page select *Add Account* option

![image](images/cloud-onboarding-2.png)

**Step 3:** Select the AWS option

![image](images/cloud-onboarding-3.png)

**Step 4:** In the next Screen select the labels and Tags field from the dropdown Menu.

![image](images/cloud-onboarding-5.png)

**Step 5:** After giving labels and Tag in the Next Screen Provide the AWS account’s Access Key and Secret Access Key ID and Select the Region of the AWS account.

![image](images/cloud-onboarding-6.png)

**Step 6:** AWS account is added to the AccuKnox using Access Key Method. We can see the onboarded cloud account by navigating to Settings→cloud Accounts option.

![image](images/cloud-onboarding-7.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
