For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/audit/annotate-audits.md).

Prisma Cloud lets you surface and display designated labels in events and reports. For example, you might already use labels to classify resources according to team name or cost center. With _alert labels_, you can specify which of these key-value pairs are appended to events (audits, incidents, syslog, alerts) and reports.

Labels are key-value string pairs that can be attached to objects such as images, containers, or pods. In Console, specify a list of Docker and Kubernetes labels that contain the metadata you want to append to Prisma Cloud events. When an event fires, if the associated object has any of the specified labels, they are appended to the event.

## Specifying labels to append to Prisma Cloud events[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/annotate-audits\#specifying-labels-to-append-to-prisma-cloud-events)

Specify which labels to append to Prisma Cloud events.

1. Open Console.

2. Go to **Manage > Alerts > Alert Labels**.

3. Click **Add Label**.















![alert labels](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-eb20e5c8fab3ed27017b2e0372841fc45b7c5a4c%252Falert_labels.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b751ef81f000aff45788c65688d083dc&sv=3)

4. Enter the name of the label to be appended to Prisma Cloud events.

5. Click **Create**.















![alert labels audit](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2823370d0aaa99984f2fb58591a2df7b695f2f93%252Falert_labels_audit.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f516844346ba73dfa713c8ebb732692c&sv=3)


## Email alerts[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/annotate-audits\#email-alerts)

The contents of a label can be used as a dynamic target for email alerts. Specify the labels that contain a comma delimited list of email addresses, and when an event fires, the recipients will be notified.

Before setting up your email alerts, be sure you’ve specified a list of labels to be appended to Prisma Cloud events, where at least one label contains a comma-delimited list of email addresses.

Kubernetes labels don’t support special characters, such as `@`, which are required to specify email addresses. Therefore, only Docker labels can be used as a dynamic address list for email alerts.

[Configure email alerts](https://docs.prismacloud.io/admin-guide/alerts/email)

## JIRA alerts[Direct link to heading](https://docs.prismacloud.io/admin-guide/audit/annotate-audits\#jira-alerts)

The contents of a label can be used to dynamically specify project keys, JIRA labels, and assignees for new JIRA issues.

Before setting up your JIRA alerts, be sure you’ve specified a list of labels to be appended to Prisma Cloud events, where the labels contain the type of information you need to dynamically route JIRA issues to the right team.

[Configure JIRA alerts](https://docs.prismacloud.io/admin-guide/alerts/jira)

[PreviousAdmin activity](https://docs.prismacloud.io/admin-guide/audit/audit-admin-activity) [NextSyslog and stdout integration](https://docs.prismacloud.io/admin-guide/audit/logging)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
