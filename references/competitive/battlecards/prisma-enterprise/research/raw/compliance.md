> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/compliance/compliance.md).

# Compliance

Prisma Cloud enables you to view, assess, report, monitor and review your cloud infrastructure health and compliance posture. Select **Cloud Security > Compliance** to see all available compliance standards.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c86fe8b7250bae4d78c33dd03bb43b28099b9d81%2Fcompliance.png?alt=media" alt="compliance"><figcaption></figcaption></figure>

| **What do you want to do?**                                                                                             | **Start here**                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create a dashboard to see all available compliance information from your Cloud Service Providers                        | <p><a href="/content-collections/dashboards/create-and-manage-dashboards.md">Add a Compliance Dashboard</a></p><p>The compliance widgets provide you with an hourly count of compliance findings. The <strong>Time Range</strong> filter in custom dashboards does not apply.</p> |
| Add your own personalized compliance standard for a Cloud Service Provider                                              | [Create a Custom Compliance Standard](/content-collections/compliance/custom-compliance-standard.md)                                                                                                                                                                              |
| See all compliance information for Kubernetes clusters, hosts, containers and serverless functions                      | [Compliance Explorer](/content-collections/runtime-security/compliance/visibility/compliance-explorer.md)                                                                                                                                                                         |
| See compliance reports for Kubernetes clusters, hosts, containers and serverless functions                              | [Create a Compliance Report](/content-collections/compliance/new-compliance-report.md)                                                                                                                                                                                            |
| See available compliance benchmarks for Kubernetes clusters, hosts, containers and serverless functions                 | [Available CIS Benchmarks](/content-collections/runtime-security/compliance/visibility/cis-benchmarks.md)                                                                                                                                                                         |
| See compliance checks that go beyond the benchmarks for Kubernetes clusters, hosts, containers and serverless functions | [Prisma Cloud Compliance Checks](/content-collections/runtime-security/compliance/visibility/prisma-cloud-compliance-checks.md)                                                                                                                                                   |
| See the compliance checks available for serverless functions                                                            | [Serverless Functions Compliance Checks](/content-collections/runtime-security/compliance/visibility/serverless.md)                                                                                                                                                               |
| See the compliance checks available for Windows                                                                         | [Windows Compliance Checks](/content-collections/runtime-security/compliance/visibility/windows.md)                                                                                                                                                                               |
| See the compliance checks available for Kubernetes and Docker                                                           | [Kubernetes and Docker Compliance Checks](/content-collections/runtime-security/compliance/visibility/disa-stig-compliance-checks.md)                                                                                                                                             |
| Add your own compliance checks                                                                                          | [Create Custom Compliance Checks](/content-collections/runtime-security/compliance/visibility/custom-compliance-checks.md)                                                                                                                                                        |
| Add and control trusted images                                                                                          | [Manage Trusted Images](#../runtime-security/compliance/operations/)                                                                                                                                                                                                              |
| Enforce and take action on compliance checks                                                                            | [Enforce Compliance Checks](/content-collections/runtime-security/compliance/operations/manage-compliance.md)                                                                                                                                                                     |
| Detect compliance issues on hosts                                                                                       | [Scan Hosts](/content-collections/runtime-security/compliance/operations/host-scanning.md)                                                                                                                                                                                        |
| Detect compliance issues on VM images                                                                                   | [Scan VM Images](/content-collections/runtime-security/compliance/operations/vm-image-scanning.md)                                                                                                                                                                                |
| Detect compliance issues using app-embedded Defenders                                                                   | [Scan Using App-Embedded Defenders](/content-collections/runtime-security/compliance/operations/app-embedded-scanning.md)                                                                                                                                                         |
| Detect sensitive information that is improperly secured inside images and containers                                    | [Detect Secrets](/content-collections/runtime-security/compliance/operations/detect-secrets.md)                                                                                                                                                                                   |
| Detect licenses for package dependencies in code repositories                                                           | [Scan Open Source Software Licenses](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/compliance/operations/oss-license-management.md)                                                                            |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/compliance/compliance.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
