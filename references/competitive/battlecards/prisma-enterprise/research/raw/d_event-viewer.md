> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/audit/event-viewer.md).

# Event Viewer

Prisma Cloud creates and stores audit event records (audits) for all major subsystems. Audits can be reviewed in **Monitor > Events**, or they can be retrieved from the [Prisma Cloud Compute API](https://pan.dev/compute/api/get-audits-access/). If you have a centralized syslog collector, you can [integrate Prisma Cloud](/content-collections/runtime-security/audit/logging.md) with your existing infrastructure by configuring Prisma Cloud to send all audit events to syslog in [RFC5424](https://tools.ietf.org/html/rfc5424)-compliant format.

You can review some of the limits on storing [audit events](/content-collections/runtime-security/deployment-patterns/caps.md).

When you’re reviewing audits in a dialog, the list of audits isn’t updated in real-time. To retrieve all the latest data, close the dialog. If the **Refresh** button is decorated with a red indicator, click it to refresh the view with the latest data, then reopen the dialog.

## Access audits

Access to any container resource protected by Defender is logged and aggregated in Console. You can also configure Prisma Cloud to [record audits for sudo, SSH, and other events](/content-collections/runtime-security/audit/host-activity.md) that are executed on hosts protected by Defender. This audit trail links access to system components to individual users. Access events can be viewed in Console under **Monitor > Events**.

## Runtime audits

Prisma Cloud records an audit every time a runtime sensor (process, network, file system, and system call) detects activity that deviates from the sum of the predictive model plus any runtime rules you’ve defined. For example, a file system audit event is emitted when Prisma Cloud detects malware in a container. Runtime events for containers can be viewed in Console under **Monitor > Events**. Runtime events for hosts can be viewed in Console under **Monitor > Events**.

## Firewall audits

Web Application and API Security (WAAS) is a layer 7 filtering engine that ensures only safe, clean traffic ever reaches your web app. Audits are generated when WAAS detects an attack, such as SQL injection or cross-site scripting. WAAS audits can be viewed under **Monitor > Events**.

## Admin activity

All Prisma Cloud [administrative activity](/content-collections/runtime-security/audit/audit-admin-activity.md) can viewed under **Manage > View Logs**.

Prisma Cloud limits viewing of audit trails to those with a job-related need. To view audit events, you must log into Console. Only users with Administrator, Operator, Defender Manager, or Auditor [roles](/content-collections/runtime-security/authentication/user-roles.md) can view audit data in Console. Similarly, only users with the above-mentioned roles can retrieve audit data from the Prisma Cloud API.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/audit/event-viewer.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
