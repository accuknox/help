> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-iam-security.md).

# Configure IAM Security

Prisma Cloud IAM Security is the Cloud Infrastructure Entitlement Management (CIEM) offering that helps you address the security challenges of managing IAM in cloud environments. Prisma Cloud IAM security capabilities automatically calculate effective permissions across cloud service providers, detect overly permissive access, and suggest corrections to reach least privilege entitlements. It includes out-of-the-box (default) policies that govern IAM best practices to help you identify risky permissions and get to the ideal set of privileges for your deployment.

Because Prisma Cloud can correlate identity information with configuration data, it gives you the depth of visibility and control. For example, if you use the AWS S3 storage service, Prisma Cloud Data Security can discover and identify sensitive data, the cloud network analyzer capability can calculate true internet exposure, and the CIEM capability can provide granular insights into exactly who has access to the data and make appropriate recommendations to enforce least-privilege access.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-iam-security.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
