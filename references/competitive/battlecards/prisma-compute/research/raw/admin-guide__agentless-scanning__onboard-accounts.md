For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts.md).

Agentless scanning provides visibility into vulnerabilities and compliance risks on cloud workloads by scanning the root volumes of snapshots. The agentless scanning architecture lets you inspect a host and the container images in that host without having to install an agent or affecting its execution.

To learn more about the architecture and scan results, see [How agentless scanning works?](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md)

## Bulk Actions[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts\#bulk-actions)

Prisma Cloud supports performing agentless configuration at scale. Different cloud providers and authentication subtypes require different configuration fields, which also limits your ability to change accounts in bulk. The Prisma Cloud Console displays all the configuration fields that can be changed across all the selected accounts, and hides those that differ to prevent accidental misconfiguration.

Only change the configuration of multiple accounts from the same cloud provider and of the same authentication subtype. If you select accounts from different providers, you can’t change agentless configuration fields.

The following procedure shows the steps needed to configure agentless scanning for multiple accounts at the same time.

1. Go to **Compute > Manage > Cloud accounts**















![manage cloud accounts](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7aff09ed150a0937293d6ea0a29dfd527d589f06%252Fmanage-cloud-accounts.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=35fa2893ccfd4e6a01018e4b9661a6da&sv=3)

2. Select multiple accounts.











Only select accounts from the same cloud provider and of the same authentication subtype. If you select accounts from different providers, you can’t change agentless configuration fields.

3. Click the **Bulk actions** dropdown.

4. Select the **Agentless configuration** button.















![bulk actions](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-11e72b0f6d69900368e4a38776ccceae84aa40a1%252Fbulk-actions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=af50da7fea718bace15f88a1461bdaf5&sv=3)

5. Change the configuration values for the selected accounts.















![agentless configuration bulk](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cfc6bbf427694aad7ac4288f77626300dbbb2318%252Fagentless-configuration-bulk.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8862cab49618842c93a099d41730de3c&sv=3)









   - Select **Save** to save the configuration for the selected accounts.


### Agentless Scanning for Cloud Accounts[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts\#agentless-scanning-for-cloud-accounts)

- **During Onboarding**: When cloud accounts are onboarded to Prisma Cloud with the "Agentless Scanning" option enabled, scanning starts immediately. This provides instant visibility into the vulnerabilities and configurations risks for the account. If this option is disabled before onboarding, Prisma Cloud does not scan the workloads in the account. The account remains unscanned until agentless scanning is enabled.











To modify the scan settings, see [Edit Agentless Scan Settings](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts#enable-agentless-scan).

- **For existing accounts**: Enabling agentless scanning for existing accounts in Prisma Cloud does not initiate an immediate scan. Instead, these accounts are added to the next scheduled scan cycle, which occurs every 24 hours by default. This ensures that scans are conducted systematically according to the scan cycle, rather than starting immediately upon enabling.











To modify the scan cycle, see [Modify the Agentless Scan Interval](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts#modifying-the-agentless-scan-interval).


### Account Origin Filter[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts\#account-origin-filter)

The **Account Origin** filter on the **Runtime Security > Manage > Cloud Accounts** page categorizes cloud accounts based on their source, making it easier to distinguish them during onboarding and scanning:

- **Local accounts** – Accounts created in Runtime Security only (not present in the Prisma Cloud console).

- **Manually imported accounts** – Accounts manually imported from the Prisma Cloud console to Runtime Security before the **Lagrange release (end of 2022)**.

- **Auto-imported accounts** – Accounts that originated in the Prisma Cloud console and were automatically imported into Runtime Security.


### Edit Agentless Scan Settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts\#edit-agentless-scan-settings)

You can safely enable agentless scanning settings for disabled accounts on the **Runtime Security** \> **Manage** \> **Cloud accounts** page. After enabling agentless scan, the scan will trigger with the correct configuration in place.

To edit agentless scan settings, complete the following steps:

1. Go to **Runtime Security > Manage > Cloud accounts**.

2. Select **Edit Account** icon from the Actions column for the account.

3. In **Account and Agentless setup**, go to **Agentless scanning** section.

4. Modify the agentless configuration options in this section.

5. Select **Save**.


After the configuration is modified, the next scan uses the updated settings.

### Modify the Agentless Scan Interval[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts\#modify-the-agentless-scan-interval)

By default, agentless scans are triggered every 24 hours.

To change the interval, complete the following steps.

1. Go to **Runtime Security > Manage > System**.

2. Select the **Scan** tab.

3. In the **Scheduling** section, in **Agentless** box, type the new duration for the scan cycle.

4. Select **Save**















![agentless interval](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-af1ea409113442abcee677d8a86023d8d530a52d%252Fagentless-interval.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=152c0a224ab7f47dd87301bd012847fc&sv=3)


### Manually Start Agentless Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts\#manually-start-agentless-scanning)

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


[PreviousAgentless Scanning Modes](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-modes) [NextOnboard AWS Accounts](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-aws)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
