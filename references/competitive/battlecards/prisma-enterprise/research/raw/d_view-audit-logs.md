> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/view-audit-logs.md).

# View Audit Logs

As part of compliance requirement for organizations, companies need to demonstrate they are proactively tracking security issues and taking steps to remediate issues as they occur. The Prisma Cloud Audit Logs section enables companies to prepare for such audits so that they can demonstrate compliance. The Audit logs list all actions initiated by Prisma Cloud administrators. It lists who did what and when, to help you identify any configuration changes and activity initiated on a cloud account of behalf of the administrator who initiated the action.

Audit logs older than 120 days are deleted.

1. Select **Settings > Audit Logs**.
2. Select a **Time Range** to view the activity details by users in the system.
3. Select **Add Filter** to make your search more efficient.
   * **Action Type**— Filter audit logs by the type of activity performed on a resource by a user or system, such as **Create**, **Read**, **Update**, **Delete**, **Login**, and **Test**.
   * **Name**— Enter the name of the resource that you want to find. You can enter up to 10 resource names.
   * **IP Address**— Enter the IP addresses that you want to find. You can enter up to 10 IP addresses.
   * **Resource**— Filter audit logs based on the resource categories. You can select up to 10 resource categories.
   * **User**— Search for the name of the user who performed an activity. You can select up to 10 users.
4. Select the columns you want to display and their order.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f28d037995c5633c189026e9158d723d05d5589e%2Fconfigure-audit-logs-1.png?alt=media" alt="configure audit logs 1"><figcaption></figcaption></figure>
5. After selecting the columns, you can **Download** all administrator activity.

   The details are in a CSV format.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-6546d258fda0dfe834c17a5aa6d6073ec1f45362%2Faudit-logs-1.png?alt=media" alt="audit logs 1"><figcaption></figcaption></figure>
6. View the data in the CSV file.

The **Load More** button retrieves additional audit log records, enhancing user experience. The maximum limit is 500 records per request. When the number of audit log records is below 500 for a request, the **Load More** button will be disabled.

## Audit Log Details

The Prisma Cloud audit log includes the following fields, which are available for ingestion in to your security and event management systems:

| **Field Name**   | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **action**       | Contains the entire content of the audit log, which describes the actions performed by the Prisma Cloud user and details of the resource changed by the action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **user**         | Name of the Prisma Cloud user that performed the action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **ipAddress**    | <p>IP address that the user logged-in with.</p><p>If the action is a background process, which is not triggered by a user with an IP address, the placeholder <strong>Prisma Public Cloud Internal IP</strong> value is displayed.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **actionType**   | Type of action performed on a resource by a user or system, such as **Create**, **Read**, **Update**, **Delete**, **Login**, and **Test**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **resourceName** | Prisma Cloud resource object that the activity was performed on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **resourceType** | <p>Category of the activity performed by the Prisma Cloud user.</p><p>The values for this field are:</p><ul><li>Account Group</li><li>Alert Config</li><li>Alert Rule</li><li>Alerts</li><li>Anomaly Settings</li><li>bridgecrew provision</li><li>CidrBlock</li><li>Cloud Account</li><li>Cloud Accounts</li><li>Data Pattern</li><li>Data Profile</li><li>Download Job</li><li>IaC Scan</li><li>iam provision</li><li>Integration</li><li>Investigate - Search</li><li>Login</li><li>Login Ip Whitelist Check</li><li>Notification Template</li><li>pcn provision</li><li>PublicNetwork</li><li>Saved Filter</li><li>Secure - Policy</li><li>Secure - Report</li><li>Security - SAML</li><li>Session Timeout</li><li>SSO Bypass Management</li><li>TenantConfig</li><li>twistlock provision</li><li>User Management</li><li>User Profile</li><li>User Role</li><li>Suppression</li><li>Enforcement exception rule</li><li>Enforcement default settings</li><li>Repository</li></ul> |
| **result**       | <p>Result of the action performed.</p><p>The values for this field are:</p><ul><li>Success</li><li>Successful</li><li>True</li><li>Failed</li><li>Failure</li><li>False</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **timestamp**    | Time that the Prisma Cloud audit event occurred, in epoch format and UTC timezone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Forward Audit Logs

Get ready for security audits by streamlining your workflow and integrating Prisma Cloud audit logs with your existing reporting infrastructure. With Prisma Cloud you can forward audit logs to AWS SQS or Webhooks.

Follow the steps below to enable audit log forwarding:

1. Select **Settings > Enterprise Settings**.
2. Enable **Send Audit Logs to integration**.
3. Select the AWS SQS or Webhooks notification channel from the **Select Integration** drop-down.
4. Choose the [Add Integration](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin/configure-external-integrations-on-prisma-cloud) option if you need to configure a new integration.

   All new audit logs that are generated after you enable the integration will be sent to this channel. You can view the audit logs on **Settings > Audit Logs** on Prisma Cloud.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/view-audit-logs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
