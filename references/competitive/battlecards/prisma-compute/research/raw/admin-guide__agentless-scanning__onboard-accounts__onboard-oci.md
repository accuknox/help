For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci.md).

Agentless scanning lets you inspect the risks and vulnerabilities of a virtual machine without having to install an agent or affecting the execution of the instance. Prisma Cloud gives you the flexibility to choose between agentless and agent-based security using Defenders. Currently, Prisma Cloud supports agentless scanning on Oracle Cloud Infrastructure (OCI) for vulnerabilities and compliance. To learn more about how agentless scanning works, see the [How Agentless Scanning Works?](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/agentless-scanning/agentless-scanning.md)

The procedure shows you how to complete the following tasks.

1. Create an OCI compartment to run the needed instances in OCI that perform the agentless scanning.

2. Create a new OCI user for Prisma Cloud to access OCI.

3. Create an API key in OCI for the new user.

4. Configure the Prisma Cloud console to access the OCI resources.

5. Apply the needed permissions in OCI.

6. Start an agentless scan.


## Create an OCI Compartment[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#create-an-oci-compartment)

1. Go to the Oracle Cloud console.















![agentless oci home](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8a1c24724236e8766f0070ccc2e8710df644149c%252Fagentless-oci-home.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=be2f7d3d874cb18ed4ca8b6f05b4a42a&sv=3)

2. In the menu, go to **Identity & Security > Compartments**.















![agentless oci id menu compartments](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cd382832d5929ffc9f1651b7d0bb4cfb01a29a7e%252Fagentless-oci-id-menu-compartments.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2f8420f4521098154ea0c33e81423250&sv=3)

3. Click **Create Compartment**.















![agentless oci create compartments](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5462b3a6b59f88bcf521af5f1726436d150f2543%252Fagentless-oci-create-compartments.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8c967787c34a7e27fb15430edfce2294&sv=3)

4. Enter a name and a description for the compartment.















![agentless oci create compartments name](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8529db26c39b2649cf17622058a116e7c95749f3%252Fagentless-oci-create-compartments-name.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=dd4d597eed55655f4804c436cb671a19&sv=3)

5. Click **Create Compartment**.











To scan all resources across all regions, you must create the resources for the different regions in the compartment. Make sure to create all needed resources with the same name in all regions.


## Create a New OCI User[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#create-a-new-oci-user)

1. In the menu, go to **Identity & Security > Users**.















![agentless oci id menu users](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-76049127a8d3c37030803ffc40ba038c047e07a2%252Fagentless-oci-id-menu-users.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=34747880b4a70eb3e88a88a6aa997c01&sv=3)

2. Click **Create User**.















![agentless oci create user](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ee8a09de710cd6ddfefe7ad7b18dd71eb687108a%252Fagentless-oci-create-user.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3728411095a130aab662e5b6292dfbbb&sv=3)

3. Select **IAM User**.

4. Enter a **Name** and a **Description** for the user.















![agentless oci create user fields](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fc98e6d0c2d1243ac3e417a6220f126f654bd9b6%252Fagentless-oci-create-user-fields.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5043295470ea1afc7dc5660ba0c53295&sv=3)

5. Click **Create**.















![agentless oci create user button](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-271fb5ad1c50a4c4b81c82bba34e2effe273a666%252Fagentless-oci-create-user-button.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5d0f38299042a93586b54fcce732f536&sv=3)


## Create an API Access Key[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#create-an-api-access-key)

1. On the user page, go to **Resources > API Key**.















![agentless oci user](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4e1b0c0781c731a771c5d1add166186cd505daa1%252Fagentless-oci-user.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=657280b2d42048c987a2391d25e25a5e&sv=3)

2. Select **Generate API Key Pair**.















![agentless oci api keys](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5699ed74001f75e5393ac9988d35fd4e3b0458c1%252Fagentless-oci-api-keys.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=31b7c80e55bd771a9cc52ff50e53ba56&sv=3)

3. Click **Download Private Key**.















![agentless oci download private key](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-bd61cb9885aca3c5b16f140f0ee8b6c8f2575d9f%252Fagentless-oci-download-private-key.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=db06a6db608372661606285f56ec3132&sv=3)

4. Click **Add**.















![agentless oci add key button](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d353bfae45145b120692205b0dad07022115819f%252Fagentless-oci-add-key-button.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2234c6881b2bb4baa7918c5abde84936&sv=3)

5. The **Configuration File Preview** opens.















![agentless oci configuration file preview](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3f46b3deb32c3caf7da7210d036cddff27e89e5f%252Fagentless-oci-configuration-file-preview.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=65bba1b7261d7363329102627d71f7f1&sv=3)









1. Copy the key-value pair for `user` into a text file.

2. Copy the key-value pair for `fingerprint` into a text file.

3. Copy the key-value pair for `tenancy` into a text file.















      ![agentless oci configuration file preview fields](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4e825fa44f92a392e90d2b53d10d0d8b94f85b42%252Fagentless-oci-configuration-file-preview-fields.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=acd531dd4e8d54d72fddc9156f2bda78&sv=3)

4. Save the text file.


6. Click **Close**.















![agentless oci configuration file preview close](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-00166bb3471ad08187a316aa96b51fa51e916403%252Fagentless-oci-configuration-file-preview-close.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=2254c4a70d5c51b560fa7f986233a631&sv=3)


## Configure Agentless Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#configure-agentless-scanning)

Complete the [agentless scanning configuration](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-oci#configure-oci-agentless) for your OCI accounts.

## Apply the Permissions in OCI[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#apply-the-permissions-in-oci)

1. Go to the Oracle Cloud console.















![agentless oci home](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-8a1c24724236e8766f0070ccc2e8710df644149c%252Fagentless-oci-home.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=be2f7d3d874cb18ed4ca8b6f05b4a42a&sv=3)

2. Click on the terminal icon on the right hand corner and select **Cloud Shell**.















![agentless oci cloud shell](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-fae77f3b3e9f3620509b84507a5e6d36643091b7%252Fagentless-oci-cloud-shell.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=9095379fd9aabce73052791cbc886cf8&sv=3)

3. Click the gear icon on the shell, and select **Upload File**.















![agentless oci upload file](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f70f26b32be4d81c8ff30ef3f3426cf0b56aeac1%252Fagentless-oci-upload-file.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0b592e4535bc35475ed2b2c6355e996f&sv=3)

4. Select the `pcc-apply-permissions.sh` permission template you downloaded from the Prisma Cloud Console.

5. Make the file executable with the following command.

















AskCopy



```
chmod +x pcc-apply-permissions.sh
```

6. Apply the permissions with the following command. Replace <OCI-Compartment> with the name of the created compartment.

















AskCopy



```
apply ./pcc-apply-permissions.sh <OCI-Compartment>
```

7. Verify that the changed statements for the policy are correct and enter `y` to continue.

8. Enter `y` to dismiss the warning about tags.

9. Once the permissions are applied, you have an OCI user with the needed permissions.


### Agentless Scanning for Cloud Accounts[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#agentless-scanning-for-cloud-accounts)

- **During Onboarding**: When cloud accounts are onboarded to Prisma Cloud with the "Agentless Scanning" option enabled, scanning starts immediately. This provides instant visibility into the vulnerabilities and configurations risks for the account. If this option is disabled before onboarding, Prisma Cloud does not scan the workloads in the account. The account remains unscanned until agentless scanning is enabled.











To modify the scan settings, see [Edit Agentless Scan Settings](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci#enable-agentless-scan).

- **For existing accounts**: Enabling agentless scanning for existing accounts in Prisma Cloud does not initiate an immediate scan. Instead, these accounts are added to the next scheduled scan cycle, which occurs every 24 hours by default. This ensures that scans are conducted systematically according to the scan cycle, rather than starting immediately upon enabling.











To modify the scan cycle, see [Modify the Agentless Scan Interval](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci#modifying-the-agentless-scan-interval).


### Account Origin Filter[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#account-origin-filter)

The **Account Origin** filter on the **Runtime Security > Manage > Cloud Accounts** page categorizes cloud accounts based on their source, making it easier to distinguish them during onboarding and scanning:

- **Local accounts** – Accounts created in Runtime Security only (not present in the Prisma Cloud console).

- **Manually imported accounts** – Accounts manually imported from the Prisma Cloud console to Runtime Security before the **Lagrange release (end of 2022)**.

- **Auto-imported accounts** – Accounts that originated in the Prisma Cloud console and were automatically imported into Runtime Security.


### Edit Agentless Scan Settings[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#edit-agentless-scan-settings)

You can safely enable agentless scanning settings for disabled accounts on the **Runtime Security** \> **Manage** \> **Cloud accounts** page. After enabling agentless scan, the scan will trigger with the correct configuration in place.

To edit agentless scan settings, complete the following steps:

1. Go to **Runtime Security > Manage > Cloud accounts**.

2. Select **Edit Account** icon from the Actions column for the account.

3. In **Account and Agentless setup**, go to **Agentless scanning** section.

4. Modify the agentless configuration options in this section.

5. Select **Save**.


After the configuration is modified, the next scan uses the updated settings.

### Modify the Agentless Scan Interval[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#modify-the-agentless-scan-interval)

By default, agentless scans are triggered every 24 hours.

To change the interval, complete the following steps.

1. Go to **Runtime Security > Manage > System**.

2. Select the **Scan** tab.

3. In the **Scheduling** section, in **Agentless** box, type the new duration for the scan cycle.

4. Select **Save**















![agentless interval](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-af1ea409113442abcee677d8a86023d8d530a52d%252Fagentless-interval.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=152c0a224ab7f47dd87301bd012847fc&sv=3)


### Manually Start Agentless Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-oci\#manually-start-agentless-scanning)

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


[PreviousConfigure Agentless Scanning for GCP](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-gcp) [NextConfigure Agentless Scanning for OCI](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/configure-oci)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
