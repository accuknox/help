> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/prisma-cloud-dspm-deployment/file-shares/on-premise-file-shares.md).

# On-premise File Shares

### Prerequisites

Prisma Cloud DSPM requires network connectivity to access and classify data stored in the file share. There are two primary methods for establishing this connectivity:

* Over the internet, which is easier to set up.
* Peering, which offers a more secure connection.

In addition to ensuring network connectivity, Prisma Cloud DSPM requires a user account within the Active Directory (AD) domain associated with the file share. During the onboarding process in the Prisma Cloud DSPM interface, users are prompted to input the relevant username and generate a cloud secret to securely store the associated password. This step is crucial for seamless integration and efficient functioning of Prisma Cloud DSPM in accessing and organizing data.

Access instructions for both methods are provided below.

### For AWS Based Orchestrators

**Enable internet access using the orchestrator IP**

1. Navigate to the AWS console in the orchestrator account.
2. Choose the desired region for the connection.
3. Access **EC2**.
4. Under **Network & Security**, located in the left menu, go to **Elastic IPs**.
5. Identify the IP labeled **Prisma-Cloud-DSPM**; this is the IP that requires connectivity allowance.

**Establish peering between on-premises and the VPC**

1. Navigate to the AWS console in the orchestrator account.
2. Choose the desired region for the connection.
3. Access **VPC**.
4. Under **Network & Security**, located in the left menu, go to **Your VPCs**.
5. Identify the VPC CIDR of the VPC labeled **Prisma-Cloud-DSPM**; this is the CIDR block needed for peering.

### For Azure Based Orchestrators

**Enable internet access using the orchestrator IP**

1. Navigate to the Azure portal in the orchestrator subscription.
2. Navigate to **Resource groups** and choose the one starts with "**Prisma-Cloud-DSPM-security**" in the desired region for the connection.
3. Under the list of resources, choose for the NAT gateway resource in the desired region.
4. Inside the NAT gateway. navigate to Outbound IP.
5. Identify the IP labeled **Prisma-Cloud-DSPM**; this is the IP that requires connectivity allowance.

**Establish peering between on-premises and the Vnet**

1. Navigate to the Azure portal in the orchestrator subscription.
2. Navigate to **Resource groups** and choose the one starts with "**Prisma-Cloud-DSPM**" in the desired region for the connection.
3. Under the list of resources, choose the virtual network in the desired region.
4. Create the peering between the Vnet to the on-prem network.

### For GCP Based Orchestrators

**Enable internet access using the orchestrator IP**

1. Navigate to the GCP console in the orchestrator project.
2. Under 'VPC Network', navigate to 'IP addresses'.
3. Identify the IP labeled **Prisma-Cloud-DSPM-region**; this is the IP that requires connectivity allowance.

**Establish peering between on-premises and the VPC**

1. Navigate to the GCP console in the orchestrator project.
2. Under 'VPC Network', navigate to 'VPC networks'.
3. Identify the Vnet named **Prisma-Cloud-DSPM** and navigate into its 'Subnets' tab.
4. Identify the subnet named **Prisma-Cloud-DSPM-region** and get its IPv4 range; this is the range that is required for peering.

### On-premise File Shares

1. Sign in to your Prisma Cloud DSPM account.
2. Go to **Preferences > Integrations**.
3. Navigate to the **Cloud Platforms** area, and select the **Fileshare** option.

   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f7427a9e8210ce95a6ada8cf0e1f338af6f09e78%2Fmedia_1518668ebac7eb5df882884a6e2fe414dc580083c.png?alt=media)
4. Click **Configure**.
5. Click **Add New**.

   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-b674c451112a4a8dd27431a7eb37ec7eb1b0a056%2Fmedia_14b636f8688be4438f5b60df1f7d4c37f30dadf3a.png?alt=media)
6. Enter the required details in the form:
   * Enter the **Username** corresponding to the Prisma Cloud DSPM user that has been created for this purpose.
   * Specify the desired **Orchestrator Cloud** from which the file share is to be scanned.
   * Indicate the specific **Orchestrator** that will be utilized for the scanning process.
   * Select the relevant **Region**.
   * Ensure that the **URI**  follows the specified format: \<IP of the machine> + ‘/’+ \<Share name>.
   * The entry in the **Name this account** field is the display name in Prisma Cloud DSPM.
   * Select the **File system type**. Presently, only the Windows file system is supported.
   * Choose a **label for the account**, for example Development, Staging, or Testing.

     ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-eca4cb3b0e6898e069e159f661bc2996a0937325%2Fmedia_18b6a256328bf05df90c11ce24173f714aec212cb.png?alt=media)
7. Click **Continue**.
8. After completing the form, choose one of the following options to safely store the credentials in the cloud secret manager in the chosen Orchestrator project.
   * Option 1: Use the Prisma Cloud DSPM template to add the password to your cloud secret manager.
   * Option 2: Use an existing secret if you have already added the password to your cloud secret manager.

#### Option 1: Use the Prisma Cloud DSPM template to add the password to your cloud secret manager

1. Generate a secret in the cloud secret manager utilizing a script provided by Prisma Cloud DSPM to store the password for the internal user.
2. Create the secret.
3. Make sure to input the password into the correct place.
4. Click **Done.**

   Prisma Cloud DSPM verifies the connection, and if everything is okay the new account is now listed in your configuration page.

#### Option 2: Use an existing secret if you have already added the password to your cloud secret manager

1. Provide Prisma Cloud DSPM with an existing secret from the cloud secret manager that contains the password for the internal user.

   Make sure your secret follows the format examples below:

   * **AWS secret ARN:**\
     *arn\<region>:\<account-id>:\<key-id>*
   * **Azure key vault ID:**\
     */subscriptions/\<subscription-id>/resourceGroups/\<resource-group>/providers/Microsoft.KeyVault/vaults/\<key-vault>*
   * **GCP secret ID:**\
     *projects/\<project-id>/secrets/\<secret-id>*
2. Input the secret ID.
3. Click **Done**.

   Prisma Cloud DSPM verifies the connection.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/prisma-cloud-dspm-deployment/file-shares/on-premise-file-shares.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
