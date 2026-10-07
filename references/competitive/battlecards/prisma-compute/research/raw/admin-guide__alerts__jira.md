For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/jira.md).

Prisma Cloud continually scans your environment for vulnerabilities using the threat data in the Intelligence Stream. Prisma Cloud can open JIRA issues when new vulnerabilities are detected in your environment. This mechanism lets you implement continuous vulnerability assessment and remediation by hooking directly into the developer’s workflow.

New JIRA issues are opened when new vulnerabilities are found. A new issue is created for each discovery. Each JIRA issue lists the new vulnerabilities discovered, and a list of vulnerabilities that have already been reported but were still detected.

JIRA issues are opened based on policy. For example, an issue would be created when all of the following conditions are met:

- You have a rule that alerts on critical vulnerabilities,

- The rule is associated with your JIRA alert profile,

- The Prisma Cloud scanner finds a critical vulnerability in an image in your environment.


## Intelligent issue routing[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#intelligent-issue-routing)

You can leverage image labels to intelligently route alerts to the right team, and eliminate manual ticket triage. For example, if team-a is responsible for image-a, and a vulnerability is found in image-a, you could set up the alert to flow directly to team-a’s JIRA queue.

Intelligent routing depends on a Prisma Cloud feature called [alert labels](https://docs.prismacloud.io/admin-guide/audit/annotate-audits), where you define labels that Prisma Cloud should watch. When rules trigger, Prisma Cloud extracts the value of the label from the resource, and applies it to the next phase of alert processing. For JIRA alerts, you can use labels to specify the JIRA project key, JIRA labels, and JIRA issue assignee.

For example, if you have an image with the following labels:

AskCopy

```
group=front-end-group
team=client-team
business-app=my-business-app
```

You could configure Prisma Cloud to open issues about this specific image in the JIRA project defined by the _group_ label.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Integrating Prisma Cloud with JIRA[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#integrating-prisma-cloud-with-jira)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![jira config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f1a84dfe830155e10f1a4b5d1e4ebd88f87f4c84%252Fjira_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f392ec93022a46867cf7a3220f6b1b45&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#create-new-alert-profile)

Create a new alert profile.

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a name for your alert profile.

3. In **Provider**, select **JIRA**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#configure-the-channel)

Configure the channel.

1. In **Base URL**, specify the location of your JIRA service.

2. In **Credential**, select the API Token that you added in the **Manage > Authentication > Credentials Store** page.











For more information, see [Managing Jira Authentication in Prisma Cloud](https://docs.prismacloud.io/admin-guide/alerts/jira#_managing_jira_authentication_in_prisma_cloud).

3. In **CA certificate**, enter a copy of the CA certificate in PEM format.

4. In **Project key**, enter a project key.











Alternatively, you can dynamically specify the project key based on a label. When an alert fires, the project key is taken from the label of the resource that triggered the action. To do so, click **Select labels…​**, and choose a label that you know will contain the project key. If there are no labels in the drop-down list, go to **Manage > Alerts > Alert Labels**, and define them.

5. Enter an issue type.

6. Enter a priority.

7. Enter a comma delimited list of JIRA labels to apply to the issue.











You can dynamically define the list from a label. Click **Select labels…​**, and select one or more labels.

8. Enter an assignee for the new issue.











You can dynamically define the assignee from a label. Click **Select labels…​**, and select one or more labels.

9. Click **Send Test Alert** to test the connection.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config jira triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4c8125439aed61efb0b92455fa98257312dca7b7%252Ffrag_config_jira_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d88d15f495ebf1e16dab87c835131348&sv=3)

3. Click **Next**.


## Managing Jira Authentication in Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#managing-jira-authentication-in-prisma-cloud)

To integrate Jira with Prisma Cloud, you must configure authentication using API tokens. Jira Cloud and Jira Data Center (DC) no longer support password-based authentication for REST API access. Instead:

- Jira Cloud requires an API token generated from your Atlassian account.

- Jira DC supports authentication using Personal Access Tokens.


This section provides procedures for adding API tokens to the Credentials Store, updating existing credentials, and replacing credentials in Jira alert profiles.

### Adding API Tokens in Credentials Store for Jira DC Authentication[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#adding-api-tokens-in-credentials-store-for-jira-dc-authentication)

To integrate Jira DC with Prisma Cloud, generate a Personal Access Token in Jira, store it in the Credentials Store in Prisma Cloud, and use it when adding a Jira profile.

Jira Data Center (DC) supports authentication with Personal Access Tokens instead of traditional passwords. For more information, see [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html).

To add an API token for Jira DC authentication, do the following:

1. Navigate to **Manage > Authentication > Credentials Store**.

2. Click **Add Credential**.

3. In the **Create Credential** window, complete the following fields:









   - **Name** – Enter a name for the credential.

   - **Description** – Add a description.

   - **Type** – Select **Basic authentication**.

   - **Username** – Add the email address used for the Jira DC account.

   - **Password**: Enter the API token (use the **Personal Access Token** created in Jira DC)


4. Click **Save** to store the credential.


## Adding API Tokens in Credentials Store for Jira Cloud Authentication[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#adding-api-tokens-in-credentials-store-for-jira-cloud-authentication)

Jira Cloud requires an **API token** for authentication instead of traditional passwords. To integrate Jira Cloud with Prisma Cloud, generate an API token in Jira Cloud, store it in the Credentials Store in Prisma Cloud, and use it when adding a Jira profile.

For more information on creating cloud token from your Jira Cloud account, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)

To add an API token for Jira Cloud authentication, do the following:

1. Navigate to **Manage > Authentication > Credentials Store**.

2. Click **Add Credential**.

3. In the **Create Credential** window, complete the following fields:









   - **Name** – Enter a name for the credential.

   - **Description** – Add a description.

   - **Type** – Select **Basic authentication**.

   - **Username** – Add the email address used for the Jira Cloud account.

   - **Password**: Enter the API token (use the **API token** created in Jira Cloud)


4. Click **Save** to store the credential.


### Updating Jira Cloud Credentials to Use an API Token[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#updating-jira-cloud-credentials-to-use-an-api-token)

Jira Cloud no longer supports basic authentication with passwords. If you previously stored Jira Cloud credentials using a password, you must update the credential by replacing the password with an API token.

To update Jira Cloud credentials, do the following:

1. Navigate to **Manage > Authentication > Credentials Store**.

2. Select the Jira Cloud credential in the table, and click the **Edit** icon.

3. In the **Edit Credential** window, update the following fields:









   - **Password** – Replace the existing password with the API token generated in Jira Cloud.


4. Click **Save** to update the credential.


## Troubleshooting[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#troubleshooting)

### Issue 1[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#issue-1)

Unable to Send Test Alert in JIRA due to the Error 'Failed to send JIRA test alert, error: request failed with status 400: Specify an issue type' despite configuring the Issue Type

**Symptom**

Unable to send test alert in JIRA due to the following error despite configuring the issue type:

`Failed to send JIRA test alert, error: request failed with status 400: Specify an issue type`

![troubleshooting 1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-819981d7f87ae7761f57559f37aeae4a49a8769c%252Ftroubleshooting-1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2d22b92d69ad9278ac0b207887fefd49&sv=3)

**Reason** The Issue Type configured in Prisma Cloud does not match the one set up in your JIRA environment.

**Resolution**

1. Log into your JIRA account

2. Navigate to the Project and check the available [Issue Type](https://support.atlassian.com/jira-cloud-administration/docs/configure-issue-types/)


![troubleshooting 2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2cc58606d0efc5dc49b9f97d541e2bbe0eb24407%252Ftroubleshooting-2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=70196808114c025a45399c8abef2f6b5&sv=3)

1. Update the Issue type in Prisma Cloud to match the one in JIRA (In the above example, the issue type is 'Email request')


### Issue 2[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/jira\#issue-2)

Unable to Send Test Alert in JIRA due to the Error 'Failed to send jira test alert, error: request failed with status 400: Priority name '<name>' is not valid' despite configuring the Priority

**Symptom**

Unable to send test alert in JIRA due to the following error despite configuring the priority:

`Failed to send jira test alert, error: request failed with status 400: Priority name '<name>' is not valid`

![troubleshooting 3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-80dbc648d68ff472c5a9f1ba9f80227009c504a7%252Ftroubleshooting-3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f602705d631a150bfd6f428bf875abdf&sv=3)

**Reason** The Priority configured in Prisma Cloud does not match the one set up in your JIRA environment

**Resolution**

1. Log into your JIRA account

2. Navigate to the Project and check the configured [Priority](https://support.atlassian.com/jira-cloud-administration/docs/manage-priorities/).


![troubleshooting 4](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5613b95411b30823c722e655688f6310e751e9bd%252Ftroubleshooting-4.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bac3a4376ad21b172d7a8ef2b9b02529&sv=3)

1. Update the Priority in Prisma Cloud to match the one in JIRA (In the above example, the Priority configured in JIRA is P1)


[PreviousIBM Cloud Security Advisor](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor) [NextPagerDuty](https://docs.prismacloud.io/admin-guide/alerts/pagerduty)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
