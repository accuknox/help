> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/connect/connect-cloud-accounts.md).

# Connect Cloud Accounts

Prisma Cloud provides comprehensive security and compliance coverage to secure your cloud accounts and comply with various industry standards. With a simplified onboarding experience you can adapt to your organization’s security priorities in a streamlined manner with the security capabilities grouped as **Foundational** and **Advanced** (with a few enabled by default). Use the **Foundational** capabilities during the start of your organization’s cloud adoption journey to effectively manage assets in the cloud and on-premises. Use the **Advanced** capabilities to proactively control your cloud operations and identify and remediate issues before they manifest within your runtime environments.

To get the most out of your investment in Prisma Cloud and to begin monitoring the resources on your cloud infrastructure, you must first connect your public cloud accounts to Prisma Cloud. The onboarding process requires that you have the correct permissions on Prisma Cloud and your cloud accounts to authenticate and authorize the connection and retrieval of data. Prisma Cloud administrators with the System Administrator and Cloud Provisioning Administrator roles can use the cloud account onboarding process for a good first-run experience with the supported cloud service providers—Alibaba Cloud, Amazon Web Services, Microsoft Azure, Google Cloud Platform, and Oracle Cloud Infrastructure.

* [Onboard Your Amazon Web Services Account](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/connect/connect-cloud-accounts/onboard-aws/onboard-aws.md)
* [Onboard Your Microsoft Azure Account](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/connect/connect-cloud-accounts/onboard-your-azure-account/onboard-your-azure-account.md)
* [Onboard Your Google Cloud Platform Account](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/connect/connect-cloud-accounts/onboard-gcp/onboard-gcp.md)
* [Onboard Your Oracle Cloud Infrastructure Account](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/connect/connect-cloud-accounts/onboard-your-oci-account/onboard-your-oci-account.md)
* [Onboard Your Alibaba Cloud Account](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/connect/connect-cloud-accounts/onboard-your-alibaba-account/onboard-your-alibaba-account.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/connect/connect-cloud-accounts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
