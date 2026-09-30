> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/reports/prisma-cloud-reports.md).

# Get Started with Reports

Keep your stakeholders updated on your progress in securing your cloud environment, by sharing timely information on the status of your cloud assets, with Prisma Cloud **Reports**. Easily discover, create, and share reports on data such as compliance and configuration status, risk assessment, resources with open alerts, operationalization overview, and more from one centralized location. You can create a new report and access previously created reports from the top navigation panel on the Prisma Cloud administrative console.

## Reports At a Glance

Focus in and share the metrics that matter most to you and your team. Learn more about the various types of **Reports** you can currently generate in Prisma Cloud in the table below.

| **Report Type**    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alerts**         | <p>Two types of alerts reports are available:</p><ul><li>Cloud Security Assessment report: A PDF report that summarizes the risks from open alerts in monitored cloud accounts for any given cloud.</li><li>Business Unit report: A .csv file that lists all resources with open alerts trigerred by policies based on a compliance standard. Generate the report on an on-demand basis or set up a recurring schedule.</li></ul> |
| **Cloud Security** | A comprehensive report that captures the outcomes your team has delivered. Also included is an extensive Metrics Overview capturing key data points such as, anomalous threats detected, vulnerability trends and regulatory compliance achieved. Generate reports on an on-demand basis or set up a recurring schedule.                                                                                                          |
| **Command Center** | Share Command Center reports with stakeholders to keep them abreast of the security and compliance status of your cloud assets, and to prioritize the resolution of alerts. Command Center reports are not recurring and have to be generated from the Command Center dashboard.                                                                                                                                                  |
| **Compliance**     | Create reports based on a cloud compliance standard for immediate viewing or download, or schedule recurring reports to monitor compliance over time.                                                                                                                                                                                                                                                                             |

## Next Steps

* [Create and Manage Reports](/content-collections/reports/create-and-manage-reports.md)
* [Manage Generated Reports](/content-collections/reports/create-and-manage-reports.md#manage)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/reports/prisma-cloud-reports.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
