> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/system-components.md).

# System Components

Prisma Cloud DSPM uses native, built-in deployment methods for each public cloud. You can integrate Prisma Cloud DSPM with any cloud provider to provide real-time monitoring capabilities without affecting the monitored environment’s performance, making it a completely out-of-band solution.

Prisma Cloud DSPM’s scanning and monitoring tool consists of three main components:

### Prisma Cloud DSPM Orchestrator

Prisma Cloud DSPM Orchestrator is the component responsible for analyzing data from your environment. This component enables Prisma Cloud DSPM’s compute resources - e.g., EC2 for AWS, VM for Azure - to scan and analyze your different accounts across the selected cloud platform. You can either install Orchestrator in a single dedicated account (a security tooling account) while monitoring other scanned accounts, or install it in each scanned account separately; installation is configurable in order to meet the client’s needs.

### Prisma Cloud DSPM Read-Only Permissions

Used as read-only access for the client’s environment, read-only permissions enable Prisma Cloud DSPM to access assets’ metadata such as size, name and region, as well as collect logs for DDR capabilities. This component is installed in every account monitored by Prisma Cloud DSPM and enables asset discovery and protection.

### Prisma Cloud DSPM Scanner Permissions

Scanner permissions enable Prisma Cloud DSPM to discover and scan data for analysis and classification. It is installed in every account monitored by Prisma Cloud DSPM (in addition to read-only permissions), and cannot be used outside the client’s environment. This ensures that all sensitive data discovered, scanned, and classified by Prisma Cloud DSPM’s resources never leaves the client's environment.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/system-components.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
