> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome.md).

# Welcome to Prisma Cloud DSPM

Prisma Cloud DSPM is an agentless, multi-cloud, data security platform that discovers, classifies, protects, and governs sensitive data. As more and more organizations shift to manage their data assets in the cloud, this process requires implementation of better data monitoring capabilities. Prisma Cloud DSPM’s mission is to provide organizations with such capabilities, in order to ensure complete visibility and real-time control over potential security risks to their data.

| **What do you want to do?**                   | **Start here**                                                                                                                                                                     |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Learn about the system components             | [System Components](/content-collections/data-security-posture-management/welcome/system-components.md)                                                                            |
| Get an overview of the platform               | [Platform Overview](/content-collections/data-security-posture-management/welcome/platform-overview/overview.md)                                                                   |
| Risks overview                                | [Risks](/content-collections/data-security-posture-management/welcome/platform-overview/risks.md)                                                                                  |
| Data detection and response policies overview | [DDR](/content-collections/data-security-posture-management/welcome/platform-overview/ddr-policies.md)                                                                             |
| Alerts overview                               | [Alerts](/content-collections/data-security-posture-management/welcome/platform-overview/alerts.md)                                                                                |
| Reports overview                              | [Reports](/content-collections/data-security-posture-management/welcome/platform-overview/reports.md)                                                                              |
| Settings overview                             | [Settings](/content-collections/data-security-posture-management/welcome/platform-overview/settings.md)                                                                            |
| Entities overview                             | [Entities](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/data-security-posture-management/welcome/platform-overview/entities.md) |
| Compliance overview                           | [Compliance](/content-collections/data-security-posture-management/welcome/platform-overview/compliance.md)                                                                        |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
