> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/cloud-service-providers.md).

# Cloud Service Providers

Credentials for cloud service providers are managed in **Manage > Cloud accounts**. Other types of credentials are managed in the credentials store in **Manage > Authentication > Credentials store**.

## Onboard Cloud Service Provider Accounts to Prisma Cloud

Use the [guided onboarding flow](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/connect/connect-cloud-accounts/connect-cloud-accounts.md) to onboard cloud accounts onto your Prisma Cloud tenant to automatically create service accounts and roles in your cloud provider accounts. Prisma Cloud is then quickly integrated with your cloud providers.

The guided onboarding flow creates service accounts and roles for the following Compute-specific integrations.

| Feature             | AWS | Azure                      | GCP                        |
| ------------------- | --- | -------------------------- | -------------------------- |
| Cloud discovery     | Yes | Yes                        | Yes                        |
| Serverless radar    | Yes | Not applicable<sup>1</sup> | Not applicable<sup>1</sup> |
| Registry scanning   | Yes | No                         | Yes                        |
| Serverless scanning | Yes | Yes                        | Yes                        |
| VM image scanning   | Yes | No                         | Yes                        |
| Host auto-defend    | Yes | Yes                        | Yes                        |
| Kubernetes auditing | Yes | Yes                        | Yes                        |
| Agentless scanning  | Yes | Yes                        | Yes                        |

<sup>1</sup>Not applicable: The feature isn’t supported in the product for this cloud service provider.

By default, Compute feature-specific minimalist permissions are added to all CloudFormation Templates for AWS, Azure and GCP accounts onboarded to Prisma Cloud. The following two onboarding modes define these permissions: **Monitor** and **Monitor & Protect**.

Large scale deployments require you to manage the number of accounts that you onboard to ensure the number of accounts remains within the workload scanning thresholds. The threshold to ensure Prisma Cloud scans all workloads in your accounts is 5000 accounts. You can manage your accounts under **Runtime Security > Manage > Cloud Accounts**. You must delete any accounts you don’t want to scan to remain below the threshold.

You can review the [list of all features and their corresponding permissions](/content-collections/runtime-security/configure/permissions.md).

### Cloud Account Permission Status

Currently, cloud account status checks don’t take Prisma Cloud Compute permissions into account. They remain green even if Prisma Cloud Compute permissions are missing in order to accommodate Cloud Security Posture Management (CSPM) users who do not use Prisma Cloud Compute functionalities. For them, changing the account permissions status could cause confusion.

Contact support to request enablement of status checks on your tenant.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/cloud-service-providers.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
