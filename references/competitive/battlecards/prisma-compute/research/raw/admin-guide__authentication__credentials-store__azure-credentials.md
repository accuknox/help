For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/azure-credentials.md).

This section discusses Azure credentials.

## Authenticate with Azure using a certificate[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/azure-credentials\#authenticate-with-azure-using-a-certificate)

You can authenticate with Azure using a certificate as a secret. As with password authentication, the certificate is stored with the Azure service principal. For more information, see the Microsoft docs [here](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-auth-service-principal#use-with-certificate).

01. Log into Compute Console.

02. Go to **Manage > Cloud accounts**

03. Click **Add account**.

04. In **Select cloud provider**, choose **Azure**.

05. Enter a name for the credential.

06. In **Subtype**, select **Certificate**.

07. In **Certificate**, enter your service principal’s certificate in PEM format.











    The certificate must include the private key. Concatenate public cert with private key (e.g., cat client-cert.pem client-key.pem).

08. Enter a tenant ID.

09. Enter a client ID.

10. Enter a subscription ID.

11. Click **Next**.

12. In **Scan account**, disable **Agentless scanning**.

13. Click **Next**.

14. Click **Add account**.

15. Validate the credential.











    Your Azure credential is now available to be used in the various integration points in the product, including registry scanning, serverless function scanning, and so on. If authentication with a certificate is supported, it’s shown in the credential drop-down in the setup dialog. For example, the following screenshot shows the setup dialog for scanning Azure Container Registry:















    ![cloud accounts acr scanning](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0803b24b06861c0186656b99151eed7b923ec40e%252Fcloud_accounts_acr_scanning.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f3d95e682df733f610a81ee76423b53e&sv=3)











    After setting up your integrations, you can review how and where the credential is being used by going to **Manage > Authentication > Credentials store** and clicking on the credential.















    ![cloud accounts cred usage](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b9d3e99c53d28414d0f16c43c49de1f390574716%252Fcloud_accounts_cred_usage.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=1aebfaf1c9341ae1c0d6befecd7a159e&sv=3)


## Create an Azure Service Principal[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/azure-credentials\#create-an-azure-service-principal)

Create an Azure Service Principal so that Prisma Cloud Console can scan your Azure tenant for microservices. To get a service key:

1. Download and [install the Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest).

2. Create a service principal and configure its access to Azure resources.

















AskCopy



```
$ az ad sp create-for-rbac \
     --name <user>-twistlock-azure-cloud-discovery-<contributor|reader> \
     --role <reader|contributor> \
     --scopes /subscriptions/<yourSubscriptionID> \
     --json-auth
```









'--sdk-auth' has been deprecated and will be removed in a future release. Starting from Azure CLI versions `2.51.0` use `--json-auth` instead.











The **--role** value depends upon the type of scanning:









   - contributor = Cloud Discovery + Azure Container Registry Scanning + Azure Function Apps Scanning

   - reader = Cloud Discovery + Azure Container Registry Scanning


3. Copy the output of the command and save it to a text file. You will use the output as the **Service Key** when creating an Azure credential.

















AskCopy



```
{
     "clientId": "bc968c1e-67g3-4ba5-8d05-f807abb54a57",
     "clientSecret": "5ce0f4ec-5291-42f8-gbe3-90bb3f42ba14",
     "subscriptionId": "ae01981e-e1bf-49ec-ad81-80rf157a944e",
     "tenantId": "d189c61b-6c27-41d3-9749-ca5c9cc4a622",
     "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
     "resourceManagerEndpointUrl": "https://management.azure.com/",
     "activeDirectoryGraphResourceId": "https://graph.windows.net/",
     "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
     "galleryEndpointUrl": "https://gallery.azure.com/",
     "managementEndpointUrl": "https://management.core.windows.net/"
}
```


## Storing the credential in Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/azure-credentials\#storing-the-credential-in-prisma-cloud)

Store the service principal’s credentials in Console so that Prisma Cloud can authenticate with Azure for scanning.

1. Open Console, and go to **Manage > Authentication > Credentials Store**.

2. Click **Add credential**, and enter the following values:









1. Enter a descriptive **Name** for the credential.

2. In the **Type** field, select **Azure**.

3. Enter the **Service Key**.











      Copy and paste the contents of the text file you saved earlier when you created the service principal.

4. **Save** your changes.


[PreviousAWS Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/aws-credentials) [NextGCP Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/gcp-credentials)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
