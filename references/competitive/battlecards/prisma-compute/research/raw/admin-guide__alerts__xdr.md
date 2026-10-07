For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/xdr.md).

[Cortex XDR](https://www.paloaltonetworks.com/cortex/cortex-xdr) is a detection and response app that natively integrates network, endpoint and cloud data to stop sophisticated attacks. Prisma Cloud can send runtime alerts to XDR when your policies are violated. Prisma Cloud can be configured to send data when an entire policy, or even specific rules, are violated.

Prisma Cloud uses webhooks to send the alerts to Cortex XDR. When an event occurs, Prisma Cloud notifies the web service with an HTTP POST request that contains a JSON body.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xdr\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Send alerts to XDR[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xdr\#send-alerts-to-xdr)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![cortex xdr config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1b51051d0950d2211803b521ff4b0f310725f013%252Fcortex_xdr_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c90b2bee0ea49e194653e1f069ba8f6d&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create a new alert channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xdr\#create-a-new-alert-channel)

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a **Profile name**.

3. In **Provider**, select **Cortex**.

4. In **Application**, select **XDR**.

5. Click **Next**.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xdr\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![cortex xdr config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c11d473bd05bb088167ff525f15450b8f8f11f09%252Fcortex-xdr-config-triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0a2070c78895483d1d4fb289d8f7af8c&sv=3)

3. Click **Next**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xdr\#configure-the-channel)

1. Under **Settings**, in **Incoming webhook URL** enter the Cortex XDR endpoint where Prisma Cloud should submit the alerts.

2. (Optional) In **Credential**, specify a basic auth credential if your endpoint requires authentication.

3. (Optional) In **CA Certificate**, enter a CA cert in PEM format.











When using a CA cert to secure communication, only one-way SSL authentication is supported. If two-way SSL authentication is configured, alerts will not be sent.

4. Click **Next**.

5. Review the **Summary** and test the configuration by selecting **Send test alert**.

6. Click **Save**.


[PreviousAWS Security Hub](https://docs.prismacloud.io/admin-guide/alerts/aws-security-hub) [NextCortex XSOAR](https://docs.prismacloud.io/admin-guide/alerts/xsoar)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
