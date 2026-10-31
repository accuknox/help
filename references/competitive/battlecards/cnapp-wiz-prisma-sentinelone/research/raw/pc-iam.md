For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-iam-security/what-is-prisma-cloud-iam-security.md).

Prisma Cloud IAM security capabilities help you evaluate the effective permissions assigned to users, workloads, and data (also called entitlements) on your cloud provider so that you can properly administer identity and access management (IAM) policies and enforce access using the principle of least privilege.

![vgr diagram](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F3990409212-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FyqPwsbMSaogAot23rTIu%252Fuploads%252Fgit-blob-35d58b404bbc79250a6dd9d9d94b2a0c78dfdf12%252Fvgr-diagram.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=20dc8bbb6592e497c676dcec47c0b13d&sv=3)

IAM Security provides:

- **Visibility**—Improve the visibility of effective permissions to resources in the cloud accounts. The ability to query all relevant IAM entities including all the relationships between the different entities and the entities’ effective permissions across multiple cloud environments.

- **Governance**—Monitor excess and unused privileges, provide out-of-the-box (default) security best practices policies, and review cloud identity compliance posture.

- **Response**—Enables you to automatically adjust effective IAM permissions to take action and reduce risk.


Prisma Cloud IAM security runs a proprietary algorithm to calculate effective permissions of the users across your cloud service providers. For example, the algorithm combines various cloud sources such as AWS IAM roles, AWS IAM policies, AWS IAM groups, AWS resource based policies, and AWS service control policies (SCPs) to compute the net effective permissions of cloud resources. It extends the Config query in RQL (`config from iam where`) to help you gain visibility into the entities in your cloud environment.

For example, with the net effective permissions calculation you can now discover the permissions for a specific user in your AWS, Azure, or GCP environment, such as, a user who has access to a AWS S3 bucket, Azure storage account, or Google storage bucket.

[PreviousConfigure IAM Security](https://docs.prismacloud.io/content-collections/administration/configure-iam-security) [NextEnable IAM Security](https://docs.prismacloud.io/content-collections/administration/configure-iam-security/enable-iam-security)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject