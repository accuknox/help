For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp.md).

1. Log in to your Prisma Cloud Compute Console.

2. Go to **Manage > Cloud** Accounts.

3. Click **+Add account**.















![agentless add account](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6abfe7d92aefa65d5e6746164b1263d620670e87%252Fagentless-add-account.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=462dafad6870d89306830e698ab5cc51&sv=3)

4. Enter the following information for the hub account in the **Account config** page.















![agentless gcp account config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b9a283bfd71aea2f81432774b54559efc90a0846%252Fagentless-gcp-account-config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=beebb06c811f84303441bb12c3c2e4ee&sv=3)









1. **Select Cloud provider**: GCP

2. **Account ID:** Enter your Google project ID for the hub account.

3. **Description:** Provide an optional string.

4. **Service account:** Paste the contents of the downloaded service account key file for the hub account.

5. **API token:** Leave blank.


5. Click **Next**.

6. In the Agentless scanning page, complete the following steps.









1. Enable **Agentless scanning**.

2. Set the **Console URL** and **Port** to the address of your Prisma Cloud console that can be reached from the internet. To create an address or FQDN reachable from the internet, complete the [Subject Alternative Names procedure](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names).


7. **Hub account**: Enable the toggle to configure this account as a [hub account](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-modes).















![agentless hub toggle](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-70d8cd2ce59c2984d8792bc050c06fbfcaa59c3c%252Fagentless-hub-toggle.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4e0f0e2c8d5ca6daaffc115042c0304e&sv=3)

8. Expand the **Advanced settings** and provide the appropriate values based on your deployment for the following items.















![agentless gcp pcee advanced settings](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a6064275ac1610a1468daf4feeb5310370c0a5c2%252Fagentless-gcp-pcee-advanced-settings.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=93e9e7ad2bf4e3dffdde284a6ab0c18b&sv=3)

9. Click **Save** to return to **Compute > Manage > Cloud accounts**.


## Scan Settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#scan-settings)

**Select where to scan**: For GCP accounts, you can decide between [two scanning modes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md#scanning-modes).

- **Same Account**: Perform the agentless scanning process using this account.

- **Hub Account**: Perform the agentless scanning process using a centralized hub account. Select another account from the list to use as the centralized hub account to scan this account.











If you wish Prisma Cloud to scan encrypted volumes on the target accounts, follow the steps on [encrypted volumes](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp#gcp-encrypted-volumes).


## Auto-scale Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#auto-scale-scanning)

Automatically create the required amount of scanners to scan all of the hosts within a region, up to a limit of 50 scanners. To use a different limit specify the **Max number of scanners**.

**Max number of scanners**: Enter the upper limit of scanners that Prisma Cloud can automatically spin up within a region in your account for faster results.

## Enforce Permissions Check[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#enforce-permissions-check)

When enabled, this account isn’t scanned in case of failure to validate the required permissions.

When disabled, the pre-scan check to validate permissions is skipped. If permissions are missing or blocked by an organizational policy, the scan fails at that stage.

Review the [needed permissions to enable agentless scanning in GCP](https://docs.prismacloud.io/admin-guide/configure/permissions#gcp-agentless).

## Proxy[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#proxy)

Enter a **Proxy** value if traffic leaving your GCP tenant uses a proxy.

Provide the proxy’s CA certificate.

## Custom Labels[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#custom-labels)

Apply **Custom labels** to any resources Prisma Cloud creates during agentless scanning.

## Scan Scope[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#scan-scope)

Under **Scan scope** you can refine the scope of the scanning by **Regions** or using labels. image::tags-scope.png\[width=300\]

- **All regions**: Scan in all GCP regions.

- **Custom regions**: Specify the GCP regions, which you want scanned.

- **Scan non running hosts**: Choose whether or not to scan hosts that aren’t running.

- **Exclude hosts by labels**: Select a subset of hosts which you want to exclude from the scan process











You can use wildcards to specify a range of labels in both keys and values following these examples:

















AskCopy



```
"abcd*"
"*abcd"
"abcd"
"*"
"*abcd*"
```

- **Include hosts by labels**: Select a subset of hosts to scan











You can use wildcards to specify a range of labels in both keys and values following these examples:

















AskCopy



```
"abcd*"
"*abcd"
"abcd"
"*"
"*abcd*"
```


## Network Resources[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#network-resources)

Configure custom network resources for agentless scanning

- **Subnet**: If left blank, agentless scanning uses the default [networking infrastructure](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md#networking-infrastructure) and assigns scanners with a public IP. Specify a subnet name to use an existing subnet in your environment and to use a private IP. The subnet must be unique and identical across all regions. If you are configuring a hub account, this requirement only applies to the hub account and not for the targets.

- **Shared VPC**: If you are using a shared VPC, enter the shared VPC path in this field with the following convention. Replace `{host_project_name}` with the ID of the project that owns the shared VPC.

















AskCopy



```
projects/{host_project_name}/regions/{region_name}/subnetworks/{subnet_name}
```









Using a shared VPC requires [additional permissions](https://docs.prismacloud.io/admin-guide/configure/permissions#gcp-agentless) on the shared VPC host project. Refer to the GCP documentation to [learn more about shared VPCs](https://cloud.google.com/vpc/docs/shared-vpc).


## Scan Encrypted Volumes When Using Hub Mode[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#scan-encrypted-volumes-when-using-hub-mode)

This section applies to scenarios where the following conditions are not met:

1. Your hub project is part of a GCP organization, and permissions were applied through organization onboarding.

2. Your encryption keys are not customer-managed encryption keys (CMEK).


If both the above conditions are met, no further action is required.

When you use [hub and target projects](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-modes), you can configure your hub project to access the encrypted volumes of the target accounts. To use encrypted volumes the service account of Google Compute Engine needs to have the `cloudkms.cryptoKeyEncrypterDecrypter` role. Without it, the service agent of the the hub project can’t access the KMS keys.

The Compute Engine service agent for your hub project is labeled with the following convention. `service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com` Replace `PROJECT_NUMBER` with the number of your hub project.

1. Use the following command to apply the grant the role and permissions to the Compute Engine service agent.

















AskCopy



```
gcloud projects add-iam-policy-binding KMS_PROJECT_ID \
       --member serviceAccount:service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com \
       --role roles/cloudkms.cryptoKeyEncrypterDecrypter
```

2. Replace `KMS_PROJECT_ID` with any project you need to use. The KMS project isn’t required to be the hub account or the target accounts you wish to scan.


### Agentless Scanning for Cloud Accounts[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#agentless-scanning-for-cloud-accounts)

- **During Onboarding**: When cloud accounts are onboarded to Prisma Cloud with the "Agentless Scanning" option enabled, scanning starts immediately. This provides instant visibility into the vulnerabilities and configurations risks for the account. If this option is disabled before onboarding, Prisma Cloud does not scan the workloads in the account. The account remains unscanned until agentless scanning is enabled.











To modify the scan settings, see [Edit Agentless Scan Settings](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp#enable-agentless-scan).

- **For existing accounts**: Enabling agentless scanning for existing accounts in Prisma Cloud does not initiate an immediate scan. Instead, these accounts are added to the next scheduled scan cycle, which occurs every 24 hours by default. This ensures that scans are conducted systematically according to the scan cycle, rather than starting immediately upon enabling.











To modify the scan cycle, see [Modify the Agentless Scan Interval](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp#modifying-the-agentless-scan-interval).


### Account Origin Filter[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#account-origin-filter)

The **Account Origin** filter on the **Runtime Security > Manage > Cloud Accounts** page categorizes cloud accounts based on their source, making it easier to distinguish them during onboarding and scanning:

- **Local accounts** – Accounts created in Runtime Security only (not present in the Prisma Cloud console).

- **Manually imported accounts** – Accounts manually imported from the Prisma Cloud console to Runtime Security before the **Lagrange release (end of 2022)**.

- **Auto-imported accounts** – Accounts that originated in the Prisma Cloud console and were automatically imported into Runtime Security.


### Edit Agentless Scan Settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#edit-agentless-scan-settings)

You can safely enable agentless scanning settings for disabled accounts on the **Runtime Security** \> **Manage** \> **Cloud accounts** page. After enabling agentless scan, the scan will trigger with the correct configuration in place.

To edit agentless scan settings, complete the following steps:

1. Go to **Runtime Security > Manage > Cloud accounts**.

2. Select **Edit Account** icon from the Actions column for the account.

3. In **Account and Agentless setup**, go to **Agentless scanning** section.

4. Modify the agentless configuration options in this section.

5. Select **Save**.


After the configuration is modified, the next scan uses the updated settings.

### Modify the Agentless Scan Interval[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#modify-the-agentless-scan-interval)

By default, agentless scans are triggered every 24 hours.

To change the interval, complete the following steps.

1. Go to **Runtime Security > Manage > System**.

2. Select the **Scan** tab.

3. In the **Scheduling** section, in **Agentless** box, type the new duration for the scan cycle.

4. Select **Save**















![agentless interval](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-af1ea409113442abcee677d8a86023d8d530a52d%252Fagentless-interval.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=152c0a224ab7f47dd87301bd012847fc&sv=3)


### Manually Start Agentless Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#manually-start-agentless-scanning)

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


This section lists the conventions used for identifying resources that are created by agentless scanning in Google Cloud Platform (GCP) services.

These conventions ensure that resources are effectively managed and uniformly identified in GCP cloud environments. In Google Cloud Platform (GCP), labels are used to identify resources created by agentless scanning.

## Resource Labeling[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp\#resource-labeling)

This section lists the conventions used for identifying resources that are created by agentless scanning in Google Cloud Platform (GCP) services.

These conventions ensure that resources are effectively managed and uniformly identified in GCP cloud environments. In Google Cloud Platform (GCP), labels are used to identify resources created by agentless scanning.

Here are the details for the different types of resources.

Here are the details for the different types of resources. **Agentless Scanner VMs**

- Name format: `prismacloud-scan-<scan-unique-id>-prisma-agentless-scan`

- Labels:









  - `created-by: prismacloud-agentless-scan`

  - `prismacloud-agentless-unique-id:<console-unique-id>`


`scan-unique-id` is a unique identifier generated for each scan. It changes with every scan, resulting in a distinct name for the resources created during that scan.

`console-unique-id` is a unique number associated with each console.

For Prisma Cloud SaaS customers, it remains constant even after upgrades. For on-premises setups, it may change if a new console is created without using data from the previous console. This ID is used to track resources and facilitate their cleanup after the scan is completed.

**Disks**

- Name format: `prismacloud-scan-<scan-unique-id>-prisma-agentless-scan`

- Labels: Not applicable


**Snapshots**

- Name format: `prismacloud-scan-<scan-unique-id>-prisma-agentless-scan`

- Labels:









  - `created-by: prismacloud-agentless-scan`

  - `prismacloud-agentless-unique-id: <console-unique-id>`


Virtual Private Cloud (VPC)

- Name format: `prismacloud-agentless-scan-vpc`

- Labels: GCP does not support labeling VPCs


[PreviousOnboard GCP Accounts](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-gcp) [NextOnboard OCI Accounts](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
