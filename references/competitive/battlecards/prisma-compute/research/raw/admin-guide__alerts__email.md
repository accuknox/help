For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/email.md).

Prisma Cloud can send email alerts when your policies are violated. Audits in **Monitor > Events** are the result of a policy violation. Prisma Cloud can be configured to notify the appropriate party by email when an entire policy, or even specific rules, are violated.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/email\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending email alerts[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/email\#sending-email-alerts)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

![email config 1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6142345b6cc606927adfce78009f824d2d19bb43%252Femail-config-1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9b3be7ab485c13db97363fcd22b0f692&sv=3)

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create a new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/email\#create-a-new-alert-profile)

1. In **Manage > Alerts**, select **Add profile**.

2. Enter a **Profile name**.

3. In **Provider**, select **Email**.

4. Select **Next**.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/email\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/email\#configure-the-channel)

1. In **SMTP address**, specify the hostname for your outgoing email server.

2. In **Port**, specify the port for email submissions.

3. In **Credential**, create the credentials required to access the email account that sends alerts. This isn’t a required field.









1. Select **Add new**.

2. Select **Basic authentication**.

3. Enter a username and password.


4. If you are using SMTPS, where the SMTP connection is encrypted when established, set **SSL** to **On**.











To support email alerts for SMTP connections encrypted using the `STARTTLS` command, disable **SSL**.

5. Set up your recipients.









1. Select **Add recipient**, and enter an email address. Every email alert profile must have at least one recipient, even if you’re using alert labels.

2. (Optional) Specify recipients using [alert labels](https://docs.prismacloud.io/admin-guide/audit/annotate-audits).


6. Select **Next**.

7. Review the **Summary** and test the configuration by selecting **Send test alert**.

8. Select **Save**.


## Troubleshooting[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/email\#troubleshooting)

### Unable to test Email Alerts for 'smtp.office365.com' on port 587.[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/email\#unable-to-test-email-alerts-for-smtp.office365.com-on-port-587)

**Error**: `tls: first record does not look like a TLS handshake`

![email alert failed handshake](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0724ad1689579cb697865f1e5c6f8e823dcc37bd%252Femail-alert-failed-handshake.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=aa0afb47e41bc907fe9f8bf08f079549&sv=3)

Prisma Cloud fails to send test alerts to 'smtp.office365.com' on port 587 after enabling **SSL**.

**Cause**:

In the SMTP protocol that Prisma Cloud Console uses to send Email Alerts, there is a following standard flow in which the client (Prisma Cloud Console) requests the server to convert an existing plain-text connection to an encrypted connection:

- The client (in this case the PCC console) sends the message “EHLO” to the server (e.g. smtp.office365.com).

- The server responds with available extensions, one of which is “STARTTLS“.

- The client responds with “STARTTLS“.

- The server acknowledges receiving the “STARTTLS”.

- The client issues a TLS handshake with the server.

- Once the handshake is successful, all communication with the server from here on is encrypted.


We support using 'STARTTLS' to encrypt Email Alerts sent over SMTP if the mail server supports it. With 'smtp.office365.com' and 'smtp-legacy.office365.com' using port 587, 'STARTTLS' is used, which encrypts subsequent communication even without 'SSL' toggle being enabled.

1. Configure the alert profile settings with the SMTP address on same port '587' with **SSL** disabled.


[PreviousCortex XSOAR](https://docs.prismacloud.io/admin-guide/alerts/xsoar) [NextGoogle Cloud Pub/Sub](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
