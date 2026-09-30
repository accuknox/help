> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/search-and-investigate/audit-event-queries.md).

# Audit Event Queries

Use audit event queries to investigate audit data for insight into privileged activities and suspicious or anomalous activities.

Prisma Cloud ingests various services and associated user and event data from AWS, Azure, and GCP cloud services. You can investigate console and API access, monitor privileged activities, and detect account compromise and unusual user behavior in your cloud environment. Because Cloud Service Provider audit logs can be high volume, Prisma Cloud regularly evaluates these logs and filters them out if they are found to be of negligible security value; such logs are not persisted in Prisma Cloud and cannot be used in RQL queries.

To investigate events, use `event from cloud.audit_logs where` queries in the search box. The query uses the event data that Prisma Cloud ingested from the audit logs to help you learn who did what and when on your cloud assets. After you run audit event search queries, you can view the results in **Graph View** or **Table View**.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/search-and-investigate/audit-event-queries.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
