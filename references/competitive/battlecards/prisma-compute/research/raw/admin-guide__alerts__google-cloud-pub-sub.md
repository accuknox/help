For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub.md).

[Google Cloud Pub/Sub](https://cloud.google.com/pubsub/) is a durable, scalable event ingestion and delivery system. It provides asynchronous messaging that decouples senders from receivers, and enables highly available communication between independently written applications.

Prisma Cloud can send alerts to Google Cloud Pub/Sub [topics](https://cloud.google.com/pubsub/architecture), where a topic is a message feed.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending alerts to Google Cloud Pub/Sub[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub\#sending-alerts-to-google-cloud-pub-sub)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![google cloud pub sub config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-85ba12cbe5d546487522ba07460bdc060042bcf6%252Fgoogle_cloud_pub_sub_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3fd2d9304ac0fc27bc7e107156d900a5&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub\#create-new-alert-profile)

Create a new alert profile.

**Prerequisite:** You’ve set up a Cloud Pub/Sub topic.

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a name for your alert profile.

3. In **Provider**, select **GCP Pub/Sub**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub\#configure-the-channel)

Configure the channel.

1. In **Credential**, click **Add new** or select an existing service account.











Create a new xref:~/authentication/credentials-store/gcp-credentials.adoc\[GCP credential\] as needed.

2. Enter a Cloud Pub/Sub topic.

3. Click **Send Test Alert** to test the connection.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


[PreviousEmail](https://docs.prismacloud.io/admin-guide/alerts/email) [NextGoogle Cloud SCC](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
