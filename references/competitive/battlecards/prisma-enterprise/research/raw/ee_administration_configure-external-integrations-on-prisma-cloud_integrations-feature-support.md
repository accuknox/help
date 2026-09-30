> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrations-feature-support.md).

# Prisma Cloud Integrations—Supported Capabilities

Learn what capabilities are available with external integrations on Prisma Cloud.

The following table provides the details of features supported on each integration with Prisma Cloud.

| Integration             | Integration Method | User Attribution | Notification Template | Alert Notification Delay | Status Check | State Change Notification                                                                               | Alert Notification Grouping | Frequency of Alert Notification |
| ----------------------- | ------------------ | ---------------- | --------------------- | ------------------------ | ------------ | ------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------- |
| AWS Guard Duty          | Pull               | No               | No                    | No                       | No           | [Alert Notifications on State Change](/content-collections/alerts/alert-notifications-state-changes.md) | No                          | No                              |
| AWS Inspector           | Pull               | No               | No                    | No                       | No           | No                                                                                                      | No                          |                                 |
| AWS Security Hub        | Push               | No               | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Amazon SQS              | Push               | Yes              | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Amazon S3               | Push               | No               | No                    | Yes                      | Yes          | Yes                                                                                                     | No                          |                                 |
| Azure Service Bus Queue | Push               | Yes              | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Demisto                 | Push               | No               | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Email                   | Push               | No               | No                    | Yes                      | No           | Yes                                                                                                     | Yes                         |                                 |
| Google Cloud SCC        | Push               | No               | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Jira                    | Push               | Yes              | Yes                   | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Microsoft Teams         | Push               | No               | No                    | Yes                      | Yes          | Yes                                                                                                     | Yes                         |                                 |
| Okta                    | No                 | No               | No                    | No                       | Yes          | No                                                                                                      | No                          |                                 |
| PagerDuty               | Push               | No               | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| ServiceNow              | Push               | No               | Yes                   | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Slack                   | Push               | No               | No                    | Yes                      | Yes          | Yes                                                                                                     | Yes                         |                                 |
| Splunk                  | Push               | Yes              | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |
| Tenable                 | Pull               | No               | No                    | No                       | No           | No                                                                                                      | No                          |                                 |
| Qualys                  | Pull               | No               | No                    | Yes                      | No           | No                                                                                                      | No                          |                                 |
| Webhook                 | Push               | Yes              | No                    | Yes                      | Yes          | No                                                                                                      | No                          |                                 |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrations-feature-support.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
