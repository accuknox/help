> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-splunk.md).

# Integrate Prisma Cloud with Splunk

Learn how to integrate Prisma® Cloud with Splunk.

Splunk is a software platform to search, analyze, and visualize machine-generated data gathered from websites, applications, sensors, and devices.

Prisma® Cloud integrates with Splunk and monitors your assets and sends alerts for resource misconfigurations, compliance violations, network security risks, and anomalous user activities to Splunk.

1. Set up Splunk HTTPS Event Collector (HEC) to view alert notifications from Prisma Cloud in Splunk. Note that only HTTPS Splunk integrations are supported.

   Splunk HEC lets you send data and application events to a Splunk deployment over secure HTTP (HTTPS) protocols. This helps consolidate alert notifications from Prisma Cloud in to Splunk so that your operations team can review and take action on the alerts.

   If you have a firewall or cloud Network Security Group between the internet and Splunk, you need to ensure network reachability and [Enable Access to the Prisma Cloud Console](/content-collections/get-started/access-prisma-cloud.md).

   1. To set up HEC, use instructions in [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector).

      For **source type**, **\_json** is the default; if you specify a custom string on Prisma Cloud, that value will overwrite anything you set here.

      By default, Splunk restricts the JSON payloads to 10,000 bytes (characters). When the size of Prisma Cloud alert notifications exceeds the default limit, you might receive incomplete payloads due to this limitation.
   2. Select **Settings > Data inputs > HTTP Event Collector** and make sure you see HEC added in the list and that the status shows that it is **Enabled**.
2. Set up the Splunk integration in Prisma Cloud.
   1. Log in to Prisma Cloud.
   2. Select **Settings > Integrations & Notifications > Integrations**.
   3. Select **Add Integration > Splunk** from the list.
   4. Enter an **Integration Name**, optionally, a **Description**.
   5. Enter the **Splunk HEC URL** that you set up earlier.

      The Splunk HEC URL is a Splunk endpoint for sending event notifications to your Splunk deployment. You must use HTTPS for this purpose. Since Prisma Cloud sends data about an alert or error in JSON format, make sure to include `/services/collector` endpoint as part of the Splunk HEC URL.
   6. Enter **Auth Token**.

      The integration uses token-based authentication between Prisma Cloud and Splunk to authenticate connections to Splunk HEC. A token is a 32-bit number that is presented in Splunk.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c0d181fc2fd52e441e0d9e5e476f7c96404c3518%2Fsplunk-add-integration-in-prisma-cloud.png?alt=media" alt="splunk add integration in prisma cloud"><figcaption></figcaption></figure>
   7. (tt:\[Optional]) Specify the **Source Type** if you want all Prisma Cloud alerts to include this custom name in the alert payload.
   8. Click **Next**, review the **Summary**, and then **Test Integration**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c2f63b65c20652c842bb068ab07935b157ca6e7e%2Fsplunk-add-integration-in-pc-2.png?alt=media" alt="splunk add integration in pc 2"><figcaption></figcaption></figure>
   9. **Save Integration** after the testing is successful.
   10. The integration will be listed on the **Integrations** page, where you can **View**, **Edit**, or **Delete** the integration from the **Actions** panel.

       <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-8fd99d6b247939412b4611989583c64ce3018421%2Fsplunk-add-integration-in-pc-3.png?alt=media" alt="splunk add integration in pc 3"><figcaption></figcaption></figure>

       After you set up the integration successfully, you can use the Get Status link to periodically check the integration status.

       <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e9b2c283e1bea94bacba3cb14ebaf4cc8eee199c%2Fget-status.png?alt=media" alt="get status"><figcaption></figcaption></figure>
3. [Create an Alert Rule for Run-Time Checks](/content-collections/alerts/create-an-alert-rule-cloud-infrastructure.md) or modify an existing rule to [receive alerts](/content-collections/alerts/send-prisma-cloud-alert-notifications-to-third-party-tools.md) in Splunk.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-splunk.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
