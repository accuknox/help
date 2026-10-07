For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/splunk.md).

Splunk is a software platform to search, analyze, and visualize machine-generated data gathered from websites, applications, sensors, and devices.

Prisma Cloud continually scans your environment for vulnerabilities, Compliance, Runtime behavior, WAAS violations and more. You can now monitor your Prisma Cloud alerts in Splunk using a native integration.

## Send Alerts to Splunk[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/splunk\#send-alerts-to-splunk)

Follow the instructions below to send alerts from your Prisma Cloud Console to Splunk Enterprise or Splunk Cloud Platform.

### Set Up Splunk HTTP Event Collector (HEC)[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/splunk\#set-up-splunk-http-event-collector-hec)

Splunk HEC lets you send data and application events to a Splunk deployment over the HTTP and HTTPS protocols. Set up Splunk HEC to view alert notifications from Prisma Cloud in Splunk and consolidate alert notifications from Prisma Cloud into Splunk. This integration enables your operations team to review and take action on the alerts.

1. To set up HEC, use the instructions in [Splunk documentation](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector). The default **source type** is **\_json**.

2. Go to **Settings > Data inputs > HTTP Event**.

3. Select **Collector** and ensure that HEC is on the list with the **Enabled** the status.


## Message Structure - JSON Schema[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/splunk\#message-structure-json-schema)

The integration with Splunk generates a consistent event format.

The JSON schema includes the following default fields:

- `app`: Prisma Cloud Compute Alert Notification.

- `message`: Contains the alert content in a JSON format as defined in the **Custom JSON** field. For example:









  - `command`: Shows the command which triggered the runtime alert.

  - `namespaces`: Lists the Kubernetes namespaces associated with the running image.

  - `startup process`: Shows the executed process activated when the container is initiated.


- `sender`: Prisma Cloud Compute Alert Notification.

- `sentTs`: Event sending timestamp as Unix time.

- `type`: Shows the message type as `alert`.


AskCopy

```
{
   app: Prisma Cloud Compute Alert Notification
   message: { [+] }
   sender: Prisma Cloud Compute Alert Notification
   sentTs: 1637843439
   type: alert
}
```

You can learn more about the Alert JSON macros and customizations in the [Webhook Alert documentation](https://docs.prismacloud.io/admin-guide/alerts/webhook)

[PreviousSlack](https://docs.prismacloud.io/admin-guide/alerts/slack) [NextWebhook](https://docs.prismacloud.io/admin-guide/alerts/webhook)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
