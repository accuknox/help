> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/compliance/new-compliance-report.md).

# Add a New Compliance Report

Monitor your single or multi-cloud environment for adherence to mandated compliance standards, with Prisma Cloud’s compliance reporting tools. [Create reports](/content-collections/reports/create-and-manage-reports.md#compliance) based on a cloud compliance standard for immediate viewing or download, or schedule recurring reports to continue monitoring compliance over time. Each report provides you with a consolidated view of cloud account compliance with a selected standard. The report lists resources and accounts currently monitored against the standard, and details their compliance status. Cloud resources are tracked for compliance against every section of a given standard and detailed findings for each section are included along with remediation for non-compliant sections.

1. Log in to Prisma Cloud.
2. Select **Cloud Security > Compliance > Create Compliance Report** and select a standard from the standards list below the dashboard.
3. Enter the following required information.
   1. Enter a descriptive **Name** for the report.
   2. Select the **Cloud Type** for the report.
   3. Select the **Date** for the report.
   4. Select report frequency, **One Time** or **Recurring**.

      If you select **Recurring** specify how often and when you want the report to run.
4. Enter the following optional information.
   1. The **Account Groups** that the report should include.
   2. The **Cloud Accounts** that the report should include.
   3. The **Cloud Regions** that the report should include.
   4. **Email Address(es)** to which you would like to send the scheduled report. Select the Custom Email Template checkbox if you wish to use a pre-selected notification template.
5. Select **Save Report**.

## View and Manage Reports

Compliance reports once generated, automatically run at the scheduled time. Select **Reports > Compliance** to view a list of all available [compliance reports](/content-collections/reports/create-and-manage-reports.md#compliance).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/compliance/new-compliance-report.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
