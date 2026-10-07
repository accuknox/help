For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results.md).

Agentless scanning lets you inspect the risks and vulnerabilities of a cloud workload without having to install an agent or affecting the execution of the workload. Prisma Cloud gives you the flexibility to choose between agentless and agent-based security using Defenders. Prisma Cloud supports agentless scanning on AWS, GCP and Azure hosts, clusters, and containers for vulnerabilities and compliance. Prisma Cloud only supports agentless scanning of hosts for vulnerabilities and compliance on OCI.

See [scanning modes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md#scanning-modes) to review the scanning options and [to configure agentless scanning](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/onboard-accounts/onboard-accounts.md) on your accounts.

## Vulnerability Scan[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#vulnerability-scan)

Agentless scan results are cohesively integrated with Defender results throughout the Console to provide seamless experience.

Vulnerability scan rules control the data surfaced in Prisma Cloud Console, including scan reports and Radar visualizations. To modify these rules, see [vulnerability scan rules](https://docs.prismacloud.io/admin-guide/vulnerability-management/vuln-management-rules).

### View Scan Results[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#view-scan-results)

Navigate to **Monitor > Vulnerabilities > Hosts** to view agentless vulnerability scan results. You can see a column named **Scanned by** in the results page. On the rows where entry is **Agentless**, scan results are provided by agentless scanning.

Agentless scans provide risk factors associated with each vulnerability such as package in use, exposed to internet, etc. ([here](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/compliance/compliance_explorer)). You can add tags and create policies in alert mode for exceptions. Agentless scanning is integrated with Vulnerability Explorer and Host Radar.

![agentless results](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7326b30e20a921fd5738f7ee05be0bf0bdedf5ad%252Fagentless_results.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=525692e989ae89f455330d4239f46332&sv=3)

## Compliance Scans[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#compliance-scans)

Navigate to **Monitor > Compliance > Hosts** to view agentless compliance scan results. You can see a column named **Scanned by** in the results page. On the rows where entry is **Agentless**, scan results are provided by agentless scanning.

![agentless compex](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-9cbd527858eb5e0ed21ebcd5baf5ade380c03759%252Fagentless_compex.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b8f366c89187ff36659987bc8b9d872f&sv=3)

Agentless scans provide risk factors associated with each compliance issue and overall compliance rate for host benchmarks. (learn more [here](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/vulnerability_management/vuln_explorer)). You can add tags and create policies in alert mode for exceptions. Agentless scanning is integrated with Compliance Explorer and Host Radar.

### Custom Compliance Scans[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#custom-compliance-scans)

You can create custom compliance checks on file systems for your host and add them to your compliance policy for scanning. [Follow the instructions](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/compliance/custom_compliance_checks) to enable custom compliance checks in a single step for both Defenders and Agentless scans.

## Pending OS Updates[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#pending-os-updates)

Unpatched OSes lead to security risks and greater possibility of exploits. Through agentless scanning, find pending OS security updates as a compliance check.

![agentless pendingOS](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-275a16b6fb3e0f41af975830208dc9d6ea4472e1%252Fagentless_pendingOS.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8e288e76c34622f2bdefca349e43240f&sv=3)

You can search for all hosts with pending OS updates by searching for "Ensure no pending OS updates" string in Compliance explorer page (Monitor > Compliance > Compliance eExplorer tab).

**Syntax:** <package name> \[<current version>\] (<new version available> …)

## Cloud Discovery Integration[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#cloud-discovery-integration)

When cloud discovery is enabled, agentless scans are automatically integrated with the results to provide visibility into all regions and cloud accounts where agentless scanning is not enabled along with undefended hosts, containers, and serverless functions.

![agentless cloud](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7aa05a2075fe0b4838c2783032f06e7afa3c6821%252Fagentless_cloud.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=44e6c202a7ec0052f6608a5494e0d35b&sv=3)

## Pre-flight checks[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#pre-flight-checks)

Before scanning, Prisma Cloud performs pre-flight checks and shows any missing permissions. You can see the status of the credentials without waiting for the scan to fail. This gives you proactive visibility into errors and missing permissions allowing you to fix them to ensure successful scans. The following image shows the notification of a missing permission.

![agentless preflight](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-33f13a7e29359f2c25022b624c9892cdca573e5a%252Fagentless_preflight.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3cd09414bc72450fc25aa4be9b682218&sv=3)

## Agentless Hosts Coverage Report[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#agentless-hosts-coverage-report)

To view the details of the scans performed on a cloud account, take the following steps.

1. Go to **Manage > Cloud Accounts**.

2. Select **Show account details** under the **Actions** column.















![agentless scanning results 1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-28a7e661958992eea7be6d397aab65c24652520b%252Fagentless-scanning-results-1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=274adab93e5cb0f46541826ed9bbce6b&sv=3)

3. The **Scan status** section shows the **Total hosts** scanned and their status.















![agentless scanning results 2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4238c1ce27a23800fe2c90d1f127620f29ebdfca%252Fagentless-scanning-results-2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=48e19549d032868d97a903621c223193&sv=3)

4. The **Region** table shows you a summary for each region under **Scan coverage**.

5. Select the host count for a given region to see the detailed report for that region.















![agentless scanning results 3](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f3821e11d8a8da12e69d1c1bc56c1adb9f0a0390%252Fagentless-scanning-results-3.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=10aa61aec852ce8b643d7d907e21c8d2&sv=3)









1. The detailed report for a region shows a summary of all hosts in a region.

2. Select a status on the **Scan status** pie chart to filter the hosts in the table to show only the hosts with that status.

3. Click on the **Status** of a given host in the table to see the following information.









      1. If the host was scanned, you see the the host’s scan results.

      2. If the host wasn’t scanned, you see a sidecar with the details on why it wasn’t scanned and recommended steps to get it scanned when applicable.


### Agentless Scanning for Cloud Accounts[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#agentless-scanning-for-cloud-accounts)

- **During Onboarding**: When cloud accounts are onboarded to Prisma Cloud with the "Agentless Scanning" option enabled, scanning starts immediately. This provides instant visibility into the vulnerabilities and configurations risks for the account. If this option is disabled before onboarding, Prisma Cloud does not scan the workloads in the account. The account remains unscanned until agentless scanning is enabled.











To modify the scan settings, see [Edit Agentless Scan Settings](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results#enable-agentless-scan).

- **For existing accounts**: Enabling agentless scanning for existing accounts in Prisma Cloud does not initiate an immediate scan. Instead, these accounts are added to the next scheduled scan cycle, which occurs every 24 hours by default. This ensures that scans are conducted systematically according to the scan cycle, rather than starting immediately upon enabling.











To modify the scan cycle, see [Modify the Agentless Scan Interval](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results#modifying-the-agentless-scan-interval).


### Account Origin Filter[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#account-origin-filter)

The **Account Origin** filter on the **Runtime Security > Manage > Cloud Accounts** page categorizes cloud accounts based on their source, making it easier to distinguish them during onboarding and scanning:

- **Local accounts** – Accounts created in Runtime Security only (not present in the Prisma Cloud console).

- **Manually imported accounts** – Accounts manually imported from the Prisma Cloud console to Runtime Security before the **Lagrange release (end of 2022)**.

- **Auto-imported accounts** – Accounts that originated in the Prisma Cloud console and were automatically imported into Runtime Security.


### Edit Agentless Scan Settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#edit-agentless-scan-settings)

You can safely enable agentless scanning settings for disabled accounts on the **Runtime Security** \> **Manage** \> **Cloud accounts** page. After enabling agentless scan, the scan will trigger with the correct configuration in place.

To edit agentless scan settings, complete the following steps:

1. Go to **Runtime Security > Manage > Cloud accounts**.

2. Select **Edit Account** icon from the Actions column for the account.

3. In **Account and Agentless setup**, go to **Agentless scanning** section.

4. Modify the agentless configuration options in this section.

5. Select **Save**.


After the configuration is modified, the next scan uses the updated settings.

### Modify the Agentless Scan Interval[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#modify-the-agentless-scan-interval)

By default, agentless scans are triggered every 24 hours.

To change the interval, complete the following steps.

1. Go to **Runtime Security > Manage > System**.

2. Select the **Scan** tab.

3. In the **Scheduling** section, in **Agentless** box, type the new duration for the scan cycle.

4. Select **Save**















![agentless interval](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-af1ea409113442abcee677d8a86023d8d530a52d%252Fagentless-interval.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=152c0a224ab7f47dd87301bd012847fc&sv=3)


### Manually Start Agentless Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-results\#manually-start-agentless-scanning)

To manually start a scan, complete the following steps.

1. Go to **Runtime Security > Manage > Cloud accounts**.

2. In the **Scan in your environment** section, select **Start Agentless scan**.















![agentless start scan](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0a9198920cabc0674720643c8f5cd8e36e6e083d%252Fagentless-start-scan.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8e8239bd97ee84762d879277e8fe7ab6&sv=3)











Note: Scanning starts for all the accounts that have the agentless scanning option enabled.

3. Select the Scan icon in the top-right corner of the console to view the scan status.

4. To view the results, complete the following steps.









1. Go to **Runtime Security > Monitor > Vulnerabilities > Hosts** or **Runtime Security > Monitor > Vulnerabilities > Images**.

2. Select **Filter hosts**.















      ![vulnerability results filters](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0ce0924e017fef7c5cc69d9e8bd335a7669cde44%252Fvulnerability-results-filters.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=734354b1ccb932bf5b107cae98ac28f1&sv=3)

3. Select the **Scanned by** filter.















      ![vulnerability results scanned by](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-708ed5c8f76fdf15da6cf77dfb39dd19cc3518b2%252Fvulnerability-results-scanned-by.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ade57670aaed6cd10bfeb2eb70455fc7&sv=3)

4. Select the **Agentless** filter.















      ![vulnerability results scanned by agentless](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-145154f40397d08a33ca7daca44df8885f45de4a%252Fvulnerability-results-scanned-by-agentless.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ef0f7b4478143559d999ccfa08c86ef0&sv=3)


[PreviousConfigure Agentless Scanning for OCI](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-oci) [NextTechnology overviews](https://docs.prismacloud.io/admin-guide/technology-overviews/technology-overviews)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
