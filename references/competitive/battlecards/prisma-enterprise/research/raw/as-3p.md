> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion.md).

# Third-Party Ingestion

By ingesting static application security testing (SAST) findings from supported third-party tools, Prisma Cloud consolidates and enriches your security vulnerability data within a single management platform, providing a deeper understanding of SAST violations through contextual enrichment.

Supported third party ingestion includes:

* [Veracode](/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/veracode-ingestion.md)
* [SonarQube](/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sonarqube-ingestion.md)
* [SARIF](/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sarif-ingestion.md)

Only onboarded and scanned repositories can be mapped. It is recommended to use supported third-party vendor integrations for data ingestion over manual SARIF file uploads. Native integrations provide automated synchronization of periodic scan data and increased data precision.

## Manage ingested data

To view and manage ingested third-party ingested data, refer to [Manage Third-Party Ingested Data](/content-collections/application-security/risk-management/monitor-and-manage-code-build/third-party-ingest-manage.md).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
