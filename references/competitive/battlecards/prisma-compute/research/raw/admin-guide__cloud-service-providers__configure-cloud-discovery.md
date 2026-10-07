For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/cloud-service-providers/configure-cloud-discovery.md).

Set up Prisma Cloud to scan your cloud service provider accounts for cloud-native resources and services. Then configure Prisma Cloud to protect them with a single click.

**Prerequisite:** You create service accounts for your cloud service providers with the [minimum required permissions](https://docs.prismacloud.io/admin-guide/configure/permissions).

1. Log in to Prisma Cloud Compute Console.

2. Select **Compute > Manage > Cloud Accounts**.

3. Select the accounts to scan. If there are no accounts in the table, use the **\+ Add account** button to onboard your cloud accounts.









   - On GCP: If you select organization level GCP credentials, for an organization with hundreds of projects, the performance of the Google Cloud Registry discovery might be affected due to long query time from GCP. The best approach to reduce scan time and avoid potential timeouts is to divide the projects in your organization into multiple GCP folders. Then create a service account and credential for each folder, and use these credentials for cloud discovery.

   - On Azure: If you create a credential in the credentials store under **Manage > Authentication > Credentials store**, your service principal authenticates with a password. To authenticate with a certificate, [onboard the cloud service provider](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/cloud-service-providers/cloud-service-providers.md).


4. Enable **Cloud discovery**.

5. Click **Add account** to save the changes.

6. Review the scan report.









1. Go to **Compute > Manage > Cloud Accounts** to view the scan report as a table.









      1. Select the **Show account details** icon to see the discovery scan results for resources within the cloud account.















         ![cloud discovery details selfhosted](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-34da038e8446363475fc4cefc765e4a86628cdf3%252Fcloud_discovery_details_selfhosted.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=08447af50b743610dfc3a96eac669133&sv=3)


2. Go to **Radar** and select **Cloud** to view the scan report as a graphic.















      ![cloud discovery radar selfhosted](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-787445cd97489a8515adb130f0831bea859ae7e2%252Fcloud_discovery_radar_selfhosted.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=80056490c24cf38c7a3cbe993e8f6e46&sv=3)

3. Click **Defend** for the entities you want Prisma Cloud to scan for vulnerabilities.











      When you click **Defend**, a new scan rule is proposed. Select the appropriate credential, tweak the scan rule as desired, then click **Add**.

4. Go to the scan reports under **Monitor > Vulnerabilities**

5. Select **Hosts**, **Registry**, or **Functions** to see the pertinent report.


[PreviousCloud Discovery](https://docs.prismacloud.io/admin-guide/cloud-service-providers/cloud-accounts-discovery-pcce) [NextVulnerability Management](https://docs.prismacloud.io/admin-guide/vulnerability-management/vulnerability-management)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
