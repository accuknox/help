> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/add-notification-template.md).

# Add Notification Template

Learn how to send Prisma Cloud alert notifications to your existing tools so that you can incorporate cloud security into your existing operational procedures.

Alert rules define which policy violations trigger an alert in a selected set of cloud accounts. When you create an Alert Rule for runtime checks, you can also configure the rule to send the Alert Payload that the rule triggers to one or more third-party tools. For all channels except email, to enable notification of policy violations in your cloud environments in your existing operational workflows, you must [configure external integrations on Prisma Cloud](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/administration/configure-external-integrations-on-prisma-cloud/configure-external-integrations-on-prisma-cloud.md). You can either set up an integration before you create the alert rule or use the inline link in the alert rule creation process to set up the integration when you need it.

Refer to the following topics to enable an alert notification channel with third-party tools:

* [Send Alert Notifications Through Email](#add-email-notification-template)
* [Send Alert Notifications to Jira](#add-jira-notification-template)
* [Send Alert Notifications to ServiceNow](#add-servicenow-notification-template)

## Send Alert Notifications Through Email

To send email notifications for alerts triggered by an alert rule, Prisma Cloud provides a default email notification template. You can customize the message in the template using the in-app rich text editor and attach the template to an alert rule. In the alert notification, you can configure Prisma Cloud to send the alert details as an uncompressed CSV file or as a compressed zip file, of 9 MB maximum attachment size.

All email notifications from Prisma Cloud include the domain name to support Domain-based Message Authentication, Reporting & Conformance (DMARC), and the email address used is <noreply@prismacloud.paloaltonetworks.com>.

1. (tt:\[Optional]) Set up a custom message for your email notification template.

   Prisma Cloud provides a default email template for your convenience, and you can customize the lead-in message within the body of the email using the rich-text editor.

   1. Select **Settings > Integrations & Notifications > Notification Templates**.
   2. Select **Add Notification Template > Email** notification template from the list.
   3. Enter a **Template Name**.

      The total length of the template name can be up to 99 characters and should not include special ASCII characters: (‘<’, ‘>’, ‘!’, ‘=’, ‘\n’, ‘\r’).

      If you had previously created a template that includes the unsupported characters and you try to update the template, an error message will indicate that the template name is invalid.
   4. Enter a **Custom Note** and select **Next**.

      The preview on the right gives you an idea of how your content will look.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-ed8b52930069c74c3112a1a0b1437a3f7c7314db%2Fadd-email-notification-template-1.png?alt=media" alt="add email notification template 1"><figcaption></figcaption></figure>
   5. **Review Status** and **Save Template**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-345e38596d1ca82b575687acef0138c5d893cc59%2Fadd-email-notification-template-2.png?alt=media" alt="add email notification template 2"><figcaption></figcaption></figure>
2. Select **Alerts > Alert Rules** and either create an Alert Rule for runtime checks or select an existing rule to edit.
3. Select **Configure Notifications > Email**.
4. Enter or select the **Emails** for which to send the alert notifications.

   You can include multiple email addresses and can send email notifications to email addresses in your domain and to guests external to your organization.
5. Set the toggle to **Enabled** to send alert notifications and **Next**.
6. (tt:\[Optional]) Select your custom email **Template**, if you have one.
7. Set the **Frequency** at which to send email notifications.
   * **Instantly**—Sends an email to the recipient list each time the alert rule triggers an alert.
   * **Recurring**—You can select the time interval as Daily, Weekly, or Monthly. Prisma Cloud sends a single email to the recipient list that lists all alerts triggered by the alert rule on that day, during that week, or the month.
8. Specify whether to include an attachment to the email.

   Including an attachment provides a way for you to include information on the alerts generated and the remediation steps required to fix the violating resource. When you select **Attach detailed report**, you can choose whether to **Include remediation instructions** to fix the root cause for the policy that triggered each alert, and opt to send it as a zip file (**Compress attachment(s)**).

   Each email can include up to 10 attachments. An attachment in the zip file format can have 60000 rows, while a CSV file can have 900 rows. If the number of alerts exceeds the maximum number of attachments, the alerts with the older timestamps are omitted.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-0f706479496eea190a16ec0d29d28b949018ae96%2Falerts-alert-rules-set-alert-notification.png?alt=media" alt="alerts alert rules set alert notification"><figcaption></figcaption></figure>
9. Review the **Summary** and **Save** the new alert rule or changes to an existing alert rule.
10. Verify the alert notification emails.

    The email alert notification specifies the alert rule, account name, cloud type, policies that were violated, the number of alerts each policy violated, and the affected resources. Click the **\<number>** of alerts to view the Prisma Cloud **Alerts > Overview** page.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-4eb3a3d353289933aeb2fff90ea1a1c26fe1c8f9%2Falerts-email-notification.png?alt=media" alt="alerts email notification"><figcaption></figcaption></figure>

## Send Alert Notifications to Jira

You can configure alert notifications triggered by an alert rule to create Jira tickets.

1. [Integrate Prisma Cloud with Jira](/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-jira.md).
2. Select **Settings > Integrations & Notifications > Notification Templates**.
3. Select **Add Notification Template > Jira** notification template from the list.
4. Enter a **Template Name** and select your **Integration**.

   Use descriptive names to easily identify the notification templates.

   The total length of the template name can be up to 99 characters and should not include special ASCII characters: (‘<’, ‘>’, ‘!’, ‘=’, ‘\n’, ‘\r’).
5. Select your **Project**.
   * (tt:\[NOTE]) Select the project where you want to receive Prisma Cloud alerts. As a best practice, create and use a dedicated project for Prisma Cloud ticketing and issue management because every alert converts to a Jira ticket.
   * If you want to enable both **Open** and **Resolved** alert notification states on Prisma Cloud, make sure your Jira workflow for the configured project can handle the transition of states from **Open > Resolved > Open** (re-open). Failure to do so will result in the `Jira state transition is not possible for configured state` error. When the project supports these transition states, a new Jira ticket is created for each new alert, and the same ticket is updated once the alert status changes.
6. Select your **Issue Type**.
7. Optionally, you can use toggle to set the **Resolved** alert state to **Enabled** and click **Next**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-8541f9dae6cce136426eb6e91b0035601887d495%2Fadd-jira-notification-template-1.png?alt=media" alt="add jira notification template 1"><figcaption></figcaption></figure>
8. To **Configure Open State** for alerts in Jira:
   1. Select the **Jira Fields** that you would like to populate.

      (tt:\[NOTE]) The Jira fields that are defined as mandatory in your project are already selected and included in the alert.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e7c61067f447302bc46c1a1f13d5f3af00527482%2Fadd-jira-notification-template-2.png?alt=media" alt="add jira notification template 2"><figcaption></figcaption></figure>
   2. Select the Jira **State**.
   3. Select information that goes in to **Summary** and **Description** from the alert payload.
   4. Select the **Reporter** for your alert from users listed in your Jira project.

      (tt:\[NOTE]) This option is available only if the administrator who set up this integration has the appropriate privileges to modify the reporter settings on Jira.
9. If you have **Enabled** the **Resolved** alert state, then repeat the above steps to **Configure Resolved State** for alerts in Jira.
10. Select **Next**.
11. Check the **Review Status** summary and click **Test Template**.
12. **Save Template** after you receive the Notification template tested successfully message.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-0ddf4e3a711a14486bd6237e2c2fca401497037a%2Fadd-jira-notification-template-3.png?alt=media" alt="add jira notification template 3"><figcaption></figcaption></figure>

    You can clone, edit, or delete the notification from **Actions**.

    After you set up the integration successfully, you can use the Get Status link in **Settings > Integrations & Notifications > Integrations** to periodically check the integration status.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e9b2c283e1bea94bacba3cb14ebaf4cc8eee199c%2Fget-status.png?alt=media" alt="get status"><figcaption></figcaption></figure>

## Send Alert Notifications to ServiceNow

You can send alert notifications to ServiceNow. Notification templates allow you to map the Prisma Cloud alert payload to the incident fields (referred to as *ServiceNow fields* on the Prisma Cloud interface in the screenshot) on your ServiceNow instance. Because the incident, security, and event tables are independent on ServiceNow, to view alerts in the corresponding table, you must set up the notification template for each service type — **Incidents**, **Events** or **Security Incidents** on Prisma Cloud.

If you see errors, review how to [Interpret Error Messages](/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow.md#iddd0aaa90-d099-4a99-a3ed-bde105354340).

1. [Integrate Prisma Cloud with ServiceNow](/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow.md).
2. Select **Settings > Integrations & Notifications > Notification Templates**.
3. Select **Add Notification Template > ServiceNow** notification template from the list.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-11fe70b140fad87a0d40a66cd9e02bbef53439dd%2Fadd-servicenow-notification-template-1.png?alt=media" alt="add servicenow notification template 1"><figcaption></figcaption></figure>
4. Enter a **Template Name** and select your **Integration**.

   Use descriptive names to easily identify the notification templates.

   The total length of the template name can be up to 99 characters and should not include special ASCII characters: (‘<’, ‘>’, ‘!’, ‘=’, ‘\n’, ‘\r’).
5. Set the **Service Type** to **Incident**, **Security**, or **Event**.

   The options in this drop-down match what you selected when you enabled the ServiceNow integration on Prisma Cloud.
6. Select the alert status for which you want to set up the ServiceNow fields.

   You can choose different fields for the Open, Dismissed, or Resolved states. The fields for the Snoozed state are the same as that for the Dismissed state.
7. (tt:\[Optional]) Enable the checkbox if you want to create a new ServiceNow incident when the alert state changes from **Resolved > Open** (re-open) states.

   (tt:\[NOTE]) Prisma Cloud will automatically update the incident once the alert is resolved. So, do not manually update the **Incident state** in ServiceNow. Manually changing the incident will stop notifications from being sent.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-bf1a158215b7fce56777ffa6818b7672238b32bc%2Fservicenow-notification-template.png?alt=media" alt="servicenow notification template"><figcaption></figcaption></figure>
8. Click **Next**.
9. Select the **ServiceNow Fields** that you want to include in the alert.

   Prisma Cloud retrieves the list of fields from your ServiceNow instance dynamically, and it does not store any data. Depending on how your IT administrator has set up your ServiceNow instance, the configurable fields may support a drop-down list, long-text field, or type-ahead. For a type-ahead field, you must enter a minimum of three characters to view a list of available options. When selecting the configurable fields in the notification template, at a minimum, you must include the fields that are defined as mandatory in your ServiceNow implementation.

   In this example, **Description** is a long-text field, hence you can select and include the Prisma Cloud Alert Payload fields that you want in your ServiceNow Alerts. You must include a value for each field you select to make sure that it is included in the alert notification. See [Alert Payload](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/alerts/alert-payload.md) for details on the context you can include in alerts.

   If the text in this field exceeds a certain number of characters (limit may differ based on ServiceNow default field size), you must adjust the maximum length for the fields on your ServiceNow implementation to ensure that the details are not truncated when it’s sent from Prisma Cloud.

   (tt:\[Optional]) To generate a ServiceNow Event, Message Key and Severity are required. The Message key determines whether to create a new alert or update an existing one, and you can map the Message Key to Account Name or to Alert ID based on your preference for logging Prisma Cloud alerts as a single alert or multiple alerts on ServiceNow. Severity is required to ensure that the event is created on ServiceNow and can be processed without error; without severity, the event is in an Error state on ServiceNow.

   For **Number**, use AlertID from the Prisma Cloud alert payload for ease of scanning and readability of incidents on ServiceNow.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f633419a93ecd9200559daea469b9ca04daa25f2%2Fservicenow-notification-template-alert-id.png?alt=media" alt="servicenow notification template alert id"><figcaption></figcaption></figure>

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-9c80f9e4661c7d183d3af1d4ce510a11c34b11d6%2Fservicenow-notification-template-fields.png?alt=media" alt="servicenow notification template fields"><figcaption></figcaption></figure>
10. Review the **Summary** status, **Test Template**, and **Save Template**.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-15462cbc0a165e77ea0dfed4dcb06574c827e07c%2Fsnow-notification-review-status.png?alt=media" alt="snow notification review status"><figcaption></figcaption></figure>

    You can clone, edit, or delete the notification from **Actions**.

    After you set up the integration and configure the notification template, Prisma Cloud uses this template to send a test alert to your ServiceNow instance. The test workflow creates a ticket that transitions through the different alert states that you have configured in the template. When the communication is successful, a success message displays.

    For an on-demand status check, use the **Get Status** icon on **Settings > Integrations**. These checks help you validate that the ServiceNow instance URL is reachable and that your credentials are valid.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e9b2c283e1bea94bacba3cb14ebaf4cc8eee199c%2Fget-status.png?alt=media" alt="get status"><figcaption></figcaption></figure>
11. **Next Steps**

    Verify that the integration is working as expected and [view alerts](/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow.md#id46a9b2b8-8b2a-4b68-b65e-d8c15dd574d2).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/add-notification-template.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
