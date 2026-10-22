---
title: Onboarding a Private GitHub Repository
description: Provides the steps to onboard a private GitHub repository on AccuKnox SaaS for secure monitoring and vulnerability detection.
---

# Onboarding a Private GitHub Repository

## Configuration

### Prerequisites

For GitHub IaC Scans from AccuKnox SaaS we require three prerequisites. They are as follows:

- Creating Fine-Grained tokens from GitHub for Private Repos only
- Label creation
- Adding the Code repository

### Creating fine-grained tokens from GitHub  

For generating the fine-grained access token from GitHub users need to do the following steps.

**Step 1:** Go to your GitHub profile and select **Settings**.

![private-gh-onboarding](images/private-gh-onboarding/image2.png)

**Step 2:** Select the Developer Settings in Settings options

![private-gh-onboarding](images/private-gh-onboarding/image5.png)

**Step 3:** Select **Personal Access Tokens → Fine-Grained Access Tokens**
![private-gh-onboarding](images/private-gh-onboarding/image9.png)

**Step 4:** Click on the Generate new token option

![private-gh-onboarding](images/private-gh-onboarding/image15.png)

**Step 5:** Fill out the token name, description, duration, and repository to onboard. In the **Repository permissions** section, set **Contents** to **Read-only**.

![private-gh-onboarding](images/private-gh-onboarding/image19.png)

**Step 6:** After this click on Generate token to get the Fine Grained access token with Read-only access to the Repository

![private-gh-onboarding](images/private-gh-onboarding/image6.png)

### Label Creation

After creating the Fine-Grained Access Token, create a label in AccuKnox SaaS by navigating to **Settings → Labels**, clicking **Add New Label**, and creating a label.

![private-gh-onboarding](images/private-gh-onboarding/image20.png)

### Adding code Repository

After creating the token from Github and Creating the label from AccuKnox SaaS. Users can onboard the Source Code Repository by following the steps below.

**Step 1:** Navigate to **Settings → Integrations** and select **Code Source Configuration**.

![private-gh-onboarding](images/private-gh-onboarding/image7.png)

**Step 2:** Click **Add Configuration**.

![private-gh-onboarding](images/private-gh-onboarding/image18.png)

**Step 3:** Fill in the name, select the type as **GitHub**, enter the Repository URL and Fine-Grained Access Token, then click **Verify**.

![private-gh-onboarding](images/private-gh-onboarding/image13.png)

**Step 4:** After successful Verification, you can select the branch and Label name that was created from the SaaS.

![private-gh-onboarding](images/private-gh-onboarding/image10.png)

**Step 5:** Click **Save** to add the Source Code Configuration.

![private-gh-onboarding](images/private-gh-onboarding/image14.png)

## IaC scan

To create an IaC scan for the added Source Code Configuration users need to perform the following steps.

**Step 1:** Navigate to **Settings → Integrations** and select **IaC**.

![private-gh-onboarding](images/private-gh-onboarding/image8.png)

**Step 2:** Click on Add Configuration give the name and select the Repository for which you want to schedule the IaC Scan. Select the Framework type as Kubernetes yaml, helm, or Terraform and click on save to add the IaC configuration.

![private-gh-onboarding](images/private-gh-onboarding/image1.png)

**Step 3:** After saving the IaC Configuration the scan will start in the background and it will be completed sometime.

![private-gh-onboarding](images/private-gh-onboarding/image4.png)

**Step 4:** After the scan is completed the progress will change to 100% completed

![private-gh-onboarding](images/private-gh-onboarding/image11.png)

## Risk Assessment: How to check Findings?

After the IaC scan is completed to see the findings users need to navigate to **Issues → Findings** and select **IaC** in the filter to see all findings.

![private-gh-onboarding](images/private-gh-onboarding/image17.png)

We can filter the findings based on the Repository, Risk Factor, and so on.

## Remediation: How to fix problems? How to create tickets?

To remediate any findings, select the finding or group of findings from the **Issues → Findings** page and click **Create Ticket** as shown below.

![private-gh-onboarding](images/private-gh-onboarding/image12.png)

!!! info
    Before this users must have integrated their Ticketing backend like Jira Servicenow or connects or Freshservice under Integrations->CSPM section

After clicking on the create ticket Icon the next page will popup

![private-gh-onboarding](images/private-gh-onboarding/image3.png)

Once the user clicks on Create Ticket new page with all the information related to the IaC findings and with a predefined Priority based on the Risk Factor. The user has to click on Create to confirm the ticket creation.

![private-gh-onboarding](images/private-gh-onboarding/image16.png)
