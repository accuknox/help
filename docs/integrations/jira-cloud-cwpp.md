---
hide:
  - toc
---

## Jira Integration

Integrate AccuKnox with Jira and receive AccuKnox alert notifications in your Jira accounts. With this integration, you can automate the process of generating Jira tickets with your existing security workflow.

To set up this integration, you need to coordinate with your Jira administrator and gather the inputs needed to enable communication between AccuKnox and Jira.

### Integration of JIRA:
#### **a. Prerequisites**

+ You need a Jira Site URL , Email, UserID & API token, Project key for this integration.
+ To create JIRA token go to https://id.atlassian.com/manage-profile/security/api-tokens, and click on **create API token**.
#### **b. Steps to Integrate:**
+ Go to Channel Integration.
+ Click integrate now on JIRA

![](/integrations/images/Jira-int.png)

+ Enter the following details to configure JIRA.

   + **Integration Name:** Enter the name for the integration. You can set any name. e.g.,```sh Test JIRA ```
   + **Site:** Enter the site name of your organisation. e.g., ```sh https://jiratest.atlassian.net/ ```
   + **User Email:** Enter your Jira account email address here.e.g., ```sh jira@organisation.com ```
   + **Token:** Enter the generated Token here from ```sh https://id.atlassian.com/manage-profile/security/api-tokens. .e.g., kRVxxxxxxxxxxxxx39 ```
   + **User ID:** Enter your Jira user ID here. You can visit people section and search your name to see the User ID. For more details check here. e.g., ```sh 5bbxxxxxxxxxx0103780 ```
   + **Project ID:** Enter your Project key here, each project in an organisation starts with some keyvalue and is case sensitive. Breakdown of a jira ticket to identify Project ID: ```sh https://[JIRA-SITE]/browse/[PROJECT ID]-1414 ```, e.g., ```sh DEVSECOPS ```
   + **Issue Summary:** Enter the summary for the JIRA tickets to be viewed in each JIRA tickets created. e.g., ```sh Issue generated form High Severity Incidents on onboarded cluster. ```
   + **Issue Type:** You can choose from the dropdown. i.e., ```sh Story and Bug ```
+ Click **Test** to check if the entered details are being validated, If you receive Test Successful, you have entered a valid JIRA credentials.

+ Click **Save** to save the Integration.

You can now configure Alert Triggers for JIRA .