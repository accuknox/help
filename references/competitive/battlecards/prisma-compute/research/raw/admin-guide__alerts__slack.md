For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/slack.md).

Prisma Cloud lets you send alerts to Slack channels and users.

## Configuring Slack[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/slack\#configuring-slack)

To integrate Prisma Cloud with Slack, enable the incoming webhooks. Prisma Cloud uses incoming webhooks to post messages to Slack. You must have an admin role to perform this action.

1. Login to your Slack account and select **Apps** available inside the **More** menu in the top left of your sidebar.

2. In **App Directory** search and select **Incoming Webhooks**.

3. Click the green **Add Configuration** button.

4. Enter the channel name where you want Prisma Cloud to post.

5. Click **Add Incoming Webhooks Integration**.

6. Copy and save the **Webhook URL** to be used when configuring Prisma Cloud.


## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/slack\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending alerts to Slack[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/slack\#sending-alerts-to-slack)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

![slack config 1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-83e101a78970b2b452a93aeaac15fe14ace88ceb%252Fslack-config-1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cf5bf5c5789e8ab38d2d82600c9443d3&sv=3)

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![slack config 2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-da1303996166017469f88ea4f27e8e4346465b38%252Fslack-config-2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c7858a2874568f8f9fe87b260f1e2114&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create a new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/slack\#create-a-new-alert-profile)

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a **Profile name**.

3. In **Provider**, select **Slack**.

4. Click **Next**.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/slack\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/slack\#configure-the-channel)

1. In **Settings**, enter the **Incoming webhook URL** you generated in the first section.

2. Enter Slack **Users** or Slack channel to whom you want to send alerts.

3. Click **Next**.

4. Review the **Summary** and test the configuration by selecting **Send test alert**.

5. Click **Save**.


[PreviousServiceNow Vulnerability Response](https://docs.prismacloud.io/admin-guide/alerts/servicenow-vr) [NextSplunk](https://docs.prismacloud.io/admin-guide/alerts/splunk)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
