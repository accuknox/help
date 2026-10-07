For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure.md).

1. Log in to your Prisma Cloud Compute Console.

2. Go to **Manage > Cloud** Accounts.

3. Click **+Add account**.

4. Enter the needed information in the **Account config** pane.















![azure managed identity auth](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-95e6687816e453343e4cee5f62c2bcf4a544cfe1%252Fazure-managed-identity-auth.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a5f7654f3e3dc7cd69577b93ee48bbfe&sv=3)









1. **Select Cloud provider**: Azure

2. **Name:** For example: PCC Azure Agentless.

3. **Description:** Provide an optional string, for example: <Product-name> release.

4. **Authentication method:**









      1. **Service key**: Paste the JSON object for the Service Principal you created.

      2. **Certificate**: Use a client certificate for authentication.

      3. **Managed Identity**: Use [Managed Identity](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure#configure-managed-identity) authentication to access Azure resources without entering any client secrets or certificates.


5. Click Next.

6. Complete the configuration in the **Scan account** pane:















![agentless azure scan config basic](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-41af27b9d66a6d64338295e25251913596840d3b%252Fagentless-azure-scan-config-basic.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=ec5796ca96983f9934c3f3f66848b7b1&sv=3)









1. Enable **Agentless scanning**.

2. Set the **Console URL** and **Port** to the address of your Prisma Cloud console that can be reached from the internet. To create an address or FQDN reachable from the internet, complete the [Subject Alternative Names procedure](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names).

3. **Hub account**: Enable the toggle to configure this account as a [hub account](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning-modes).















      ![agentless hub toggle](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-70d8cd2ce59c2984d8792bc050c06fbfcaa59c3c%252Fagentless-hub-toggle.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4e0f0e2c8d5ca6daaffc115042c0304e&sv=3)

4. Expand **Advanced settings** and provide the appropriate values based on your deployment for the following items.















      ![agentless configuration azure](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-aaa8fdd1d1cc599ac7cc35c58795fc8e16c265e6%252Fagentless-configuration-azure.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e82a4067a2919947af1ff2908d1d63f9&sv=3)


7. Click **Save** to return to **Compute > Manage > Cloud accounts**.


## Scan Settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#scan-settings)

**Select where to scan**: For Azure accounts, you can decide between [two scanning modes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md#scanning-modes).

- **Same Account**: Perform the agentless scanning process using this account.

- **Hub Account**: Perform the agentless scanning process using a centralized hub account. Select another account from the list to use as the centralized hub account to scan this account.


## Auto-scale Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#auto-scale-scanning)

Automatically create the required amount of scanners to scan all of the hosts within a region, up to a limit of 50 scanners. To use a different limit specify the **Max number of scanners**.

**Max number of scanners**: Enter the upper limit of scanners that Prisma Cloud can automatically spin up within a region in your account for faster results.

## Enforce Permissions Check[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#enforce-permissions-check)

When enabled, this account isn’t scanned in case of failure to validate the required permissions.

When disabled, the pre-scan check to validate permissions is skipped. If permissions are missing or blocked by an organizational policy, the scan fails at that stage.

Review the [needed permissions to enable agentless scanning in Azure](https://docs.prismacloud.io/admin-guide/configure/permissions#azure-agentless).

## Proxy[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#proxy)

Enter a **Proxy** value if traffic leaving your Azure tenant uses a proxy.

Provide the proxy’s CA certificate.

## Custom Tags[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#custom-tags)

**Custom tags**: Apply custom tags to any resources Prisma Cloud creates during agentless scanning.

## Scan Scope[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#scan-scope)

Under **Scan scope** you can refine the scope of the scanning by **Regions** or using tags.

![tags scope](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f7de430832616881821fd4ab9048664f54f4cfce%252Ftags-scope.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=74c2bdee08aa5d2f4bcba56849fc95b9&sv=3)

- **All regions**: Scan in all Azure regions.

- **Custom regions**: Specify the Azure regions, which you want scanned.

- **Scan non running hosts**: Choose whether or not to scan hosts that aren’t running.

- **Exclude hosts by tags**: Select a subset of hosts which you want to exclude from the scan process











You can use wildcards to specify a range of tags in both keys and values following these examples:

















AskCopy



```
"abcd*"
"*abcd"
"abcd"
"*"
"*abcd*"
```

- **Include hosts by tags**: Select a subset of hosts to scan











You can use wildcards to specify a range of tags in both keys and values following these examples:

















AskCopy



```
"abcd*"
"*abcd"
"abcd"
"*"
"*abcd*"
```


## Network Resources[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#network-resources)

Configure custom network resources for agentless scanning. When using custom network resources, Prisma Cloud assumes those resources have a path to communicate outbound data to the Prisma Cloud backend, as explained in the [networking infrastructure section](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md#networking-infrastructure). If left blank, Prisma Cloud creates the needed [networking resources with default settings](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md#networking-infrastructure).

- **Subnet ID**: The ID of the subnet resource in your Azure account.

- **Security group ID**: The ID of the security group resource in your Azure account.


In Azure, Prisma Cloud does not use the network resources configured directly due to current limit of specifying only one identifier for each subnet or security group across all regions. Azure’s policy prohibits having duplicate subnet or security group IDs within the same resource group, making it unfeasible to ensure these resources exist in every region.

As a result, Prisma Cloud creates these network resources within the `PCCAgentlessScanResourceGroup` resource group, mirroring the configuration of the provided resources for the subnet and security group. Prisma Cloud copies the route table data to the new resources since this data may contain various addresses that might not necessarily align with the new subnet, such as private IP addresses.

## Known Limitation[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-azure\#known-limitation)

- **Ephemeral OS Disks Unsupported:** Agentless scanning is not supported for Ephemeral disks since Azure does [not support](https://learn.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks#unsupported-features) taking snapshots of hosts with Ephemeral OS disks.


[PreviousOnboard Azure Accounts](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-azure) [NextOnboard GCP Accounts](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-gcp)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
