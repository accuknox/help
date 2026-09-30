> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/prisma-cloud-dspm-integrations/integrating-dig-with-jira.md).

# Integrate Prisma Cloud DSPM with Jira

### About this Article

This article describes how to do the following:

* Integrate Jira with Prisma Cloud DSPM
* Create Jira mapping fields
* Create a Jira ticket via Prisma Cloud DSPM

### Jira Overview

Jira is a proprietary issue tracking product developed by Atlassian that allows bug tracking and agile project management. Integrating Jira with Prisma Cloud DSPM allows you to create Jira tickets based on alerts received by Prisma Cloud DSPM. This enables seamless streamlining of your incident management workflow, and ensures efficient issue tracking and resolution.

### Prerequisite

To integrate Jira with Prisma Cloud DSPM, ensure that you have a Jira account with admin privileges.

### Integrate Jira With Prisma Cloud DSPM

#### Step 1 - In Jira

In this step, you need to create an API token in your Jira account to use it later in the integration process. To do so, follow the instructions [here](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

#### Step 2 - In Prisma Cloud DSPM

1. Go to **Preferences** > **Integrations**.
2. Under Jira, click **Connect**.\
   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a53b7847ab6acc0b15314197c05623d5a105161f%2Fmedia_1269234cfbea1cdf947dd030e285d1958df2489be.png?alt=media)
3. Add a new Jira integration:
   1. For **Client ID**, enter the email address of the user who created the API key
   2. For **Client Secret**, enter the API token you created in step 1.
   3. For **Subdomain**, enter the prefix of your Jira environment in atlassian (XXX.atlassian.com).
4. Click **Connect**.\
   ![image.png](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-ffc52ba9fbb0e0872d27e1595605d49e60312c5e%2Fmedia_11ce10c83785bdebe7d76b8e8bda98f34c9d63a00.png?alt=media)

### Create Jira Mapping Fields

The DSPM - Jira Mapping feature allows users to map relevant information directly from DSPM into Jira tickets. Additionally, users can manually customize data within various fields, providing greater flexibility and control:

**Key Features:**

* **Direct Mapping:** Seamlessly transfer pertinent information from DSPM to Jira tickets.
* **Field Customization:** Manually adjust data in different fields to suit specific needs.
* **Drop-down Selection:** Enjoy a user experience similar to Jira UI by selecting field values from drop down lists

#### Mapping Procedure

1. In the Jira window, click on the Connection to open the Jira side drawer.

   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-55c2e2a33224d8a32c04c0eac5315f69e8866982%2Fmedia_18e548141a6263dd9f8bc475b92334bfd4f7931e4.png?alt=media) ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c41102be64aa9db113f236bc704cd7813858605a%2Fmedia_1f2fd5c69b0acfd173ced64c4f02ccf9055cdc61d.png?alt=media)
2. In the side drawer, choose a project and issue type. The Field mapping view opens in the side draw. The displayed fields are Jira fields related to the selected project and issue type.\
   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e12189a3cdbd6765b99b36ad4890d00ea8b73f7c%2Fmedia_15fc1a8dcad63298902b6de5dd1b5d3d85e165e76.png?alt=media)
3. Customize the Jira integration by choosing a risk finding field in the Jira ticket.\
   For example, configure the Summary field in Jira to display the name of DSPM risk finding.\
   Fields that are not mapped are not displayed when a Jira ticket is opened by a user via the DSPM platform.\
   Each project and issue type displays a different set of fields that can be used for mapping.

   Alternatively, add custom text to the Jira ticket. In the drop-down lists, click **+ Add custom text** and enter free text. The free text is displayed in the Jira ticket.\
   Note that the Jira fields that prompt you to select an option from the drop-down menu are also displayed for mapping and the admin can select the requested value.\
   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-1bc09553a234e7862f970d97ae6ebf15ea3d69fa%2Fmedia_1be9fd56d7c3fdc732a16f9c75bb4b8c9c23b4bfb.png?alt=media)
4. Click **Save**.

### Create a Jira Ticket via Prisma Cloud DSPM

This section describes how to create a Jira ticket, via the DSPM platform, for every Risk finding detected by Prisma Cloud DSPM.

1. **Create a New Jira Ticket in DSPM**
   1. Go to the **Risks** page and select the **Findings** display. ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a2117c367127bc39362ea151dc056d43472ff4a8%2Fmedia_18950b65a61018dcedc787dcbc1d784af4268a91f.png?alt=media)
   2. Select a risk to open it, then select **Create Jira ticket** from the top right corner. ![image.png](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-0ef96cabc072001a8b996bc010351360fdbb4429%2Fmedia_1db86d77a6558b0d625fd56eff6cf2130da5a9dbf.png?alt=media)
2. **Select a pair (Project and Issue Type).** In the Create Jira ticket window, select the relevant pair (project and issue type) from the available options. A pair comprises an Issue Type and Project. For example, *Compliance* is the name of the issue type and *Data* is the name of the project.\
   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-2821ef8ded9e4f85e8dbbb0f9f41c7311c463e6b%2Fmedia_145568d35a3cc1a609543c1e4cb0c51e4ec425147.png?alt=media)
3. **Display Configured Jira Fields**
   1. Only the Jira fields that have been configured for the selected project and issue type will be displayed.
4. **Edit Field Values**
   1. The user can:
      * Choose a value from a list pulled from Jira.
      * Manually edit the field value defined by the admin during the mapping phase.
      * Reset any field to its automatically configured value. ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-4d526d4d46278f60a27fb7d2b44ae62331183e68%2Fmedia_1b068a4244a423e4e2811d3afffa100e3a0e7b38c.png?alt=media)
5. **Send the Jira Ticket**
   1. Click Create to submit the Jira ticket. The ticket will be sent to Jira, where the user can view it.
   2. After you create a Jira ticket for a risk finding, the Jira logo will be displayed next to this risk. Click the logo to view the ticket in Jira.

      ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-2bda2379432bfa32bc53df2a853a8e18f6561978%2Fmedia_1e954d02aa4270c918bab763ab609be1fafbb83e1.png?alt=media)
6. **View the Jira Ticket Status**
   1. After sending a Jira ticket, do the following to view the status of the ticket.
      * Go to Risks > Findings, and hover over Backlog. The Jira ticket number is displayed.
      * Click the Jira ticket number to review the ticket and its status. (Note that the various Jira ticket statuses are defined by the organization.)

        ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d389144692383ac7def21e33c391e508cedbadc8%2Fmedia_19067c4336ba0ccb72aa98ff5468f5f3267fd808c.png?alt=media)
7. **Error Handling**
   1. If any errors occur during configuration or ticket creation, clear and meaningful error messages are displayed to assist with troubleshooting.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/prisma-cloud-dspm-integrations/integrating-dig-with-jira.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
