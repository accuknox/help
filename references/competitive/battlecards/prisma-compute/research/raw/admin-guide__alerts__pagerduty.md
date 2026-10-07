For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/pagerduty.md).

You can configure Prisma Cloud to route alerts to PagerDuty. When Prisma Cloud detects anomalies, it generates alerts. Alerts are raised when the rules that make up your policy are violated.

## Configuring PagerDuty[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/pagerduty\#configuring-pagerduty)

Create a new Prisma Cloud service, and get an integration key.

1. Log into PagerDuty.

2. Go to **Configuration > Services**.

3. Click **New Service**.















![pagerduty create new service](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-86c25adebf28a25090e68b382c971d13586fe224%252Fpagerduty_create_new_service.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=346f6e87cf89cc3db72e11279fd21ec9&sv=3)

4. Under **General Settings**:









1. **Name**: Enter **Prisma Cloud**.


5. Under **Integration Settings**:









1. **Integration Type**: Select **Use our API directly**, the select **Events API v2**.

2. **Integration Name**: Enter **Prisma Cloud**.















      ![pagerduty add service form](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ba030c928a5df356256bed9e72081107059d4e6c%252Fpagerduty_add_service_form.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bca3ed635548a01aa7068ca92e017774&sv=3)


6. Click **Add Service**. You’re taken to **Integrations** tab for the Prisma Cloud service.















![pagerduty add service](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-02b2be14aafb2c694c7538b6d0b2b20aa7f85561%252Fpagerduty_add_service.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3aca24601dd2e1d9df6a6d702c7cee1d&sv=3)

7. Copy the **Integration Key**, and set it aside. You’ll use it to configure the integration in Prisma Cloud Console.















![pagerduty integration key](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-311ee29d4f5893921b562ca344b6970531bdecf5%252Fpagerduty_integration_key.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7845b0b9c7a4d90c60194811c8015ad2&sv=3)


## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/pagerduty\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending alerts to PagerDuty[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/pagerduty\#sending-alerts-to-pagerduty)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![pagerduty config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-491b398cffefcf64936241a4d0376b3dad3189aa%252Fpagerduty_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=76e802dc827c2798f3283a4c90500714&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/pagerduty\#create-new-alert-profile)

Create a new alert profile.

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a name for your alert profile.

3. In **Provider**, select **PagerDuty**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/pagerduty\#configure-the-channel)

Configure the channel.

1. In **Routing Key**, enter the integration key you copied from PagerDuty.

2. In **Summary**, enter a brief description, which will appear in the PagerDuty dashboard alongside your alerts.

3. For **Severity**, select the urgency of the alert.

4. Click **Send Test Alert** to validate the integration.











If the integration is set up properly, you will see a sample alert in PagerDuty. In the PagerDuty dashboard, click **Alerts**.















![pagerduty review test alert](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-eefbf1a4e0212b167629c98903109414d7832a9d%252Fpagerduty_review_test_alert.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bd5b93b15bfea32a95bc138cc3645442&sv=3)


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/pagerduty\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


[PreviousJIRA](https://docs.prismacloud.io/admin-guide/alerts/jira) [NextServiceNow Security Incident Response](https://docs.prismacloud.io/admin-guide/alerts/servicenow-sir)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
