For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/credentials-store.md).

Prisma Cloud seamlessly integrates with multiple third-party services and cloud providers, ensuring robust security and operational efficiency.

To streamline credential management, the **Credentials Store** (accessible under **Manage > Authentication > Credentials Store**) serves as a secure repository for storing and managing authentication credentials used in integrations.

**Prisma Cloud makes a clear distinction between third-party integration credentials and cloud account credentials.**

- **Third-party credentials**—such as those used for scanning container registries, sending alerts, or managing Defender deployments—are securely stored and managed within the Credentials Store.

- **Cloud account credentials**, however, are handled separately. They are not stored in the Credentials Store but are instead onboarded through the **Manage > Cloud Accounts** page, where Prisma Cloud manages authentication and permissions required for cloud workload protection.


## Supported Integrations[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store\#supported-integrations)

The Credentials Store manages credentials used for:

- Scanning container registries, serverless functions, and other environments

- Sending alerts via third-party services (e.g., Slack, ServiceNow, email)

- Deploying and managing Defender DaemonSets

- Injecting secrets into running containers


The following diagram shows the architecture of the the credentials store.

![credentials store arch](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e29145c8610dc8eb21bee1ced14c1376194041a2%252Fcredentials_store_arch.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f6d9c38bad77d7b09de1b8f7708f0c1a&sv=3)

## Managing Third-Party Credentials in Credentials Store[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store\#managing-third-party-credentials-in-credentials-store)

If a credential is actively in use, it cannot be deleted. To check its usage, select an entry from the credentials table and review the **Usages** list.

![credentials store usage](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fdc7054f2b00d2d4ee562991d912279784f28c95%252Fcredentials_store_usage.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a3bcc26a5f135149cd91ddd148e3a383&sv=3)

You can refresh a credential’s values without deleting and reconfiguring the integration. If an integration relies on a credential and you update its parameters (e.g., username, password), Prisma Cloud automatically propagates the new values across the relevant modules.

## Managing Cloud Account Credentials[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store\#managing-cloud-account-credentials)

To manage cloud account credentials, use the **Manage > Cloud Accounts** page under the **Runtime Security** component. This section handles the authentication and permissions required for cloud workload protection.

For information on onboarding cloud provider accounts, see the following topics:

- [Amazon Web Services](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/authentication/credentials-store/onboard-aws.md)

- [Microsoft Azure](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/authentication/credentials-store/onboard-azure.md)

- [Google Cloud Platform](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/authentication/credentials-store/onboard-gcp.md)

- [Oracle Cloud Infrastructure](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/authentication/credentials-store/onboard-oci.md)


[PreviousAssign roles](https://docs.prismacloud.io/admin-guide/authentication/assign-roles) [NextAWS Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
