For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/xsoar.md).

[Cortex XSOAR](https://www.paloaltonetworks.com/cortex/xsoar) is a security orchestration, automation, and response (SOAR) platform. Prisma Cloud can send alerts, vulnerabilities, and compliance issues to XSOAR when your policies are violated. Prisma Cloud can be configured to send data when an entire policy, or even specific rules, are violated.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xsoar\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Send alerts to XSOAR[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xsoar\#send-alerts-to-xsoar)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![cortex xsoar config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0c3c0d397134f7614c63aa6c08e5cc17c051b9b7%252Fcortex_xsoar_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=25eef108be3142cd6a3709ff34216476&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create a new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xsoar\#create-a-new-alert-profile)

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a **Profile name**.

3. In **Provider**, select **Cortex**.

4. In **Application**, select **XSOAR**.

5. Click **Next**.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xsoar\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xsoar\#configure-the-channel)

1. In **Settings**, enter a **Console Name** that XSOAR should use to access your Prisma Cloud console.

2. Copy the **Console URL** and save it for creating the integration in XSOAR.

3. Copy the **CA certificate** and save it for creating the integration in XSOAR.

4. Click **Next**.

5. Review the **Summary** and click **Save**.


## Configure XSOAR[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/xsoar\#configure-xsoar)

Create a new Prisma Cloud Compute integration in XSOAR.

1. Log into Cortex XSOAR.

2. Go to **Settings > Integrations**.

3. Search for **Prisma Cloud Compute** and click **Add instance**.















![demisto add integration](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-714470f9e99c525ad240976a0b9301c411aa1e2d%252Fdemisto_add_integration.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3b13c1b8ab4b8bd851359ffe2285257c&sv=3)

4. Under the **Settings**:









1. **Name**: Enter the name for the integration.

2. Check the **Fetch incidents** checkbox.

3. **Prisma Cloud Compute Console URL and Port**: Paste the URL of the console that you copied from Prisma Cloud.

4. (optional) **Prisma Cloud Compute Project Name**: Enter the name of the project in Prisma Cloud.

5. **Credentials**: Enter the Prisma Cloud username that XSOAR should use to communicate with your Prisma Cloud console.

6. **Password**: Enter the password for the username you provided.

7. **Prisma Cloud Compute CA Certificate**: Paste the CA Certificate you copied from Prisma Cloud, or enter your own CA Certificate (if using a custom certificate to access your Prisma Cloud console).


5. Click **Test** to check the connection to Prisma Cloud console.

6. Click **Done** to save the integration.

7. Go to **Incidents** to see the alerts received from Prisma Cloud.


[PreviousCortex XDR](https://docs.prismacloud.io/admin-guide/alerts/xdr) [NextEmail](https://docs.prismacloud.io/admin-guide/alerts/email)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
