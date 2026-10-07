For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/servicenow-sir.md).

ServiceNow is a workflow management platform. It offers a number of security operations applications. You can configure Prisma Cloud to route alerts to ServiceNow’s Security Incident Response application.

Prisma Cloud audits are mapped to a ServiceNow security incident as follows:

- Audits and incidents are mapped to individual ServiceNow security incidents.

- Vulnerabilities are aggregated by resource (currently image) and mapped to individual ServiceNow security incidents. ServiceNow short description field lists the resource. ServiceNow description field lists the details of each finding.

- Compliance issues are aggregated by resource (image/container/host) and mapped to individual ServiceNow security incidents. ServiceNow short description field lists the resource. ServiceNow description field lists the details of each finding.


Compliance alerts will be sent to ServiceNow in real time (right after compliance scan), unlike the other alert providers which send compliance alerts every 24 hours.

Compliance alerts will be sent if the resource is new, or if there’s a difference in the number of compliance issues for this resource after its scan. All the compliance issues of the resource will be sent (not only the new ones).

ServiceNow security incident

Field description

Prisma Cloud audit data

State

The current state of the security incident. Upon security incident creation, this field defaults to Draft.

Draft (automatically set by ServiceNow)

Priority

Select the order in which to address this security incident, based on the urgency. If this value is changed after the record is saved, it can affect the Business impact calculation.

Vulnerabilities: Max severity from the image’s new vulnerabilities. ServiceNow’s priorities map one-to-one to Prisma Cloud severities (Critical - Critical, High - High, Medium - Medium, Low - Low).

Compliance: Max severity from the image/container/host’s compliance issues. ServiceNow’s priorities map one-to-one to Prisma Cloud severities (Critical - Critical, High - High, Medium - Medium, Low - Low).

Incidents and audits: runtime audits priority set in the alert profile.

Business impact

Select the importance of this security incident to your business. The default value is Non-critical. If, after the security incident record has been saved, you change the value in the Priority and/or Risk fields, the Business impact is recalculated.

Automatically calculated by ServiceNow

Assignment group

The group to which this security incident is assigned.

Assignment group set in the alert profile

Assigned to

The individual assigned to analyze this security incident.

Assignee set in the alert profile

Short description

A brief description of the security incident.

Vulnerabilities: Prisma Cloud Compute vulnerabilities for image <image name>

Compliance: Prisma Cloud Compute compliance issues for image/container/host <image/container/host name>

Incidents and audits: Prisma Cloud Compute Audit - <audit type> - <message>

Category

Set to "None"

Sub-category

Set to "None"

Description

Description

Vulnerabilities:

- Related resource details

- CVEs IDs list (with each CVE’s details)

- Project

- Collections


Compliance:

- Related resource details

- Compliance issues list (with each issue’s details)

- Project

- Collections


Incidents and audits:

- Description

- Related resource

- Collections

- Project

- Time created

- Then add all the other fields this type of Incident/Audit has


Note that the **Project** field will specify **Central Console** even when projects aren’t enabled.

Note that the **Collections** field will exist only for the following runtime audits: Admission Audits, Docker Audits, App Embedded Audits, Host Activities, Host Log Inspection, WAAS audits, Incidents, Defender Disconnected.

## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/servicenow-sir\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending findings to ServiceNow[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/servicenow-sir\#sending-findings-to-servicenow)

Alert profiles specify which events trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with ServiceNow and specify the people or places where alerts should be sent. You can specify assignees and assignment groups.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![servicenow sir config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b243f203a19d11a54a9e5eb8bacbc036f6407852%252Fservicenow_sir_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8e147b7ffa2519744200a4776a709acf&sv=3)

## Create new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/servicenow-sir\#create-new-alert-profile)

Create a new alert profile.

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a name for your alert profile.

3. In **Provider**, select **ServiceNow**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/servicenow-sir\#configure-the-channel)

Configure Prisma Cloud to send alerts to ServiceNow, then validate the setup by sending a test alert.

**Prerequisites:** You’ve created a service account in ServiceNow with a base role of web\_service\_admin.

1. In **Application**, select **Security Incident Response**.

2. In **URL**, specify the base URL of your ServiceNow tenant.











For example, `https://ena03291.service-now.com`

3. In **Credential**, click **Add New**.









1. In **Type**, select **Basic authentication**.











      This is currently the only auth method supported.

2. Enter a username and password.


4. (Optional) In **Assignee**, enter the name of a user in ServiceNow that will be assigned the security incident.











This value isn’t case sensitive.

5. (Mandatory) In **Assignment Group**, enter the name of a group in ServiceNow that will be assigned the security incident. The default value is **Security Incident Assignment**.











If **Assignment Group** is set without specifying **Assignee**, the first user from the group is set on the security incident (ServiceNow’s logic).











If the **Assignee** set in the profile isn’t a part of the **Assignment Group**, the security incident won’t be created (ServiceNow’s logic).

6. (Optional) In **CA certificate**, enter a CA certificate in PEM format. Relevant only for on-premises deployments of ServiceNow.

7. Click **Send Test Alert**. If everything looks good, and you get an alert in ServiceNow, save the profile.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/servicenow-sir\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


[PreviousPagerDuty](https://docs.prismacloud.io/admin-guide/alerts/pagerduty) [NextServiceNow Vulnerability Response](https://docs.prismacloud.io/admin-guide/alerts/servicenow-vr)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
