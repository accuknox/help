---
title: AWS AI/ML Cloud Onboarding
description: Step-by-step instructions for onboarding an AWS cloud account and AI/ML assets within it to AccuKnox SaaS for automated security management.
---

# AWS AI/ML Cloud Onboarding

In this section we can find the steps to onboard an AWS cloud account with AI/ML asset scanning to the AccuKnox SaaS platform.

## **AWS IAM User Creation**

Follow these steps to create an IAM user with the permissions required for AI/ML asset scanning:

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

**Step 4:** Go to **Add Permissions > Create inline policy** and attach the following policy to grant access to AI/ML services:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AccuKnoxAIMLPermissions",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeAgent",
                "sagemaker:InvokeEndpoint",
                "sagemaker:ListTags",
                "bedrock-agentcore:InvokeAgentRuntime",
                "bedrock-agentcore:StopRuntimeSession",
                "aws-marketplace:Subscribe",
                "aws-marketplace:ViewSubscriptions"
            ],
            "Resource": "*"
        }
    ]
}
```

!!! note
    `aws-marketplace:Subscribe` and `aws-marketplace:ViewSubscriptions` are required for invoking certain models (e.g., Claude Opus 4.5) that are distributed through AWS Marketplace.

**Step 5:** Finish creating the user. Click on the newly created user and create the Access key and Secret Key from the Security Credentials tab to be used in the AccuKnox panel

![image](images/iam-user-4.png)

## **AWS Onboarding**

In this example we are onboarding AWS account using the Access Keys method.

**Step 1:** To onboard Cloud Account, navigate to *Settings → Cloud Accounts*

![image](images/cloud-onboarding-1.png)

**Step 2:** In the Cloud Account Page select *Add Account* option

![image](images/cloud-onboarding-2.png)

**Step 3:** Select the AWS option

![image](images/cloud-onboarding-3.png)

**Step 4:** In the next Screen select the labels and Tags field from the dropdown Menu.

![image](images/cloud-onboarding-5.png)

**Step 5:** After giving labels and tag, provide the AWS account’s Access Key and Secret Access Key ID and select the region. **Check the "AI/ML Assets" box** to enable AI/ML asset discovery and monitoring. Click "Add Account" to complete onboarding.

![image](images/ai-checkbox.png)

**Step 6:** AWS account is added to AccuKnox using the Access Key method. You can view the onboarded cloud account by navigating to Settings → Cloud Accounts.

![image](images/cloud-onboarding-7.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
