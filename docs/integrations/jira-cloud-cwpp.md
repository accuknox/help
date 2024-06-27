

## Jira Integration

Integrate AccuKnox with Jira and receive AccuKnox alert notifications in your Jira accounts. With this integration, you can automate the process of generating Jira tickets with your existing security workflow.

To set up this integration, you need to coordinate with your Jira administrator and gather the inputs needed to enable communication between AccuKnox and Jira.

### Integration of JIRA:
#### **Prerequisites**

+ You need a Jira Site URL , Email, UserID & API token, Project key for this integration.
+ To create JIRA token go to https://id.atlassian.com/manage-profile/security/api-tokens, and click on **create API token**.

??? "JIRA integration for CWPP"

    #### **Steps to Integrate:**
    + Go to Channel Integration.
    + Click integrate now on JIRA

    ![](images/Jira-int.png)

    + Enter the following details to configure JIRA.

      + **Integration Name:** Enter the name for the integration. You can set any name. e.g.,``` Test JIRA ```
      + **Site:** Enter the site name of your organisation. e.g., ``` https://jiratest.atlassian.net/ ```
      + **User Email:** Enter your Jira account email address here.e.g., ``` jira@organisation.com ```
      + **Token:** Enter the generated Token here from ``` https://id.atlassian.com/manage-profile/security/api-tokens. .e.g., kRVxxxxxxxxxxxxx39 ```
      + **User ID:** Enter your Jira user ID here. You can visit people section and search your name to see the User ID. For more details check here. e.g., ``` 5bbxxxxxxxxxx0103780 ```
      + **Project ID:** Enter your Project key here, each project in an organisation starts with some keyvalue and is case sensitive. Breakdown of a jira ticket to identify Project ID: ``` https://[JIRA-SITE]/browse/[PROJECT ID]-1414 ```, e.g., ``` DEVSECOPS ```
      + **Issue Summary:** Enter the summary for the JIRA tickets to be viewed in each JIRA tickets created. e.g., ``` Issue generated form High Severity Incidents on onboarded cluster. ```
      + **Issue Type:** You can choose from the dropdown. i.e., ``` Story and Bug ```
    + Click **Test** to check if the entered details are being validated, If you receive Test Successful, you have entered a valid JIRA credentials.

    + Click **Save** to save the Integration.

??? "JIRA integration for CSPM"
    #### **Steps to Integrate:**
    + Go to Channel Integration -> CSPM.
    + Click on add connector and select JIRA Cloud

    ![](images/jiracspm1.png)
    ![](images/jiracspm2.png)

    Enter the following details to configure JIRA.

    + **Integration Name:** Enter the name for the integration. You can set any name. e.g.,``` Test JIRA ```
    + **Site:** Enter the site name of your organisation. e.g., ``` https://jiratest.atlassian.net/ ```
    + **User Email:** Enter your Jira account email address here.e.g., ``` jira@organisation.com ```
    + **Token:** Enter the generated Token here from ``` https://id.atlassian.com/manage-profile/security/api-tokens. .e.g., kRVxxxxxxxxxxxxx39 ```

    ![](images/jiracspm3.png)

    Click on the Jira ticketing backend to add configuration.

    Here Enter the following details:

      + **Configuration name:** this name will be displayed under ticket configuration while creating tickets.
      + **Default template:** to specify the of data that this configuration will be used for making tickets.
      + **Project name:** From the list of project select the project where you want your tickets to be created.
      + **Issue Type:** You can choose from the dropdown.
      + Fill the priority mapping according to your choice and press **save**.

You can now configure Alert Triggers for JIRA .

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }