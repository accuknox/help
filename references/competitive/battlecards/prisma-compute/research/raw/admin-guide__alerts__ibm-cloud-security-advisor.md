For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor.md).

IBM Cloud Security Advisor is a centralized security dashboard. Prisma Cloud can be configured to send security findings to your service dashboard.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending alerts to Security Advisor[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor\#sending-alerts-to-security-advisor)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![ibm cloud security advisor config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-36b443e6df21fbe0f40dc303d2e255f2fcfaa57e%252Fibm_cloud_security_advisor_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=33562630ab36605b9e3d95a5969ae320&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor\#create-new-alert-profile)

Create a new alert profile.

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a name for your alert profile.

3. In **Provider**, select **IBM Cloud Security Advisor**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor\#configure-the-channel)

Configure the channel.

1. In **Credential**, click **Add new** or select an existing service account.











Create a new xref:~/authentication/credentials-store/ibm-credentials.adoc\[IBM Cloud credential\] as needed.

2. Copy the configuration URL, and set it aside. You’ll need it for the next step.

3. Go to the Security Advisor dashboard, and then follow the steps in [Prisma Cloud partner integration](https://console.bluemix.net/docs/services/security-advisor/partners.html#setup-twistlock) to complete the setup process.

4. Click **Send Test Alert** to test the connection.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


[PreviousGoogle Cloud SCC](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc) [NextJIRA](https://docs.prismacloud.io/admin-guide/alerts/jira)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
