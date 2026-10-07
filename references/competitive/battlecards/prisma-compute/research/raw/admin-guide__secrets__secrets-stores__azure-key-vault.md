For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/azure-key-vault.md).

You can integrate Prisma Cloud with Azure Key Vault. First configure Prisma Cloud to access your Key Vault, then create rules to inject the relevant secrets into their associated containers.

**Prerequisites:** You have [created a secret](https://docs.microsoft.com/en-us/azure/key-vault/quick-create-portal#add-a-secret-to-key-vault) in Key Vault.

1. Create an Azure servicePrincipal in your Azure AD Tenant









1. Use [AZ CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest) to create a servicePrincipal and obtain the json credential file.

2. Authenticate to your Azure tenant.

















      AskCopy



      ```
      $ az login
      ```

3. Create a servicePrincipal

















      AskCopy



      ```
      $ az ad sp create-for-rbac
      ```

4. Save the resulting json output.+

















      AskCopy



      ```
      {
        "appId": "xxxxxxxx-xxxxx-xxxx-xxxxxxxx",
        "displayName": "azure-cli-2018-11-01-xx-xx-xx",
        "name": "http://azure-cli-2018-11-01-xx-xx-xx",
        "password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "tenant": "xxxxxxxxxxxxxxxxxxxxxxxxxxx"
      }
      ```

5. In the Azure Key Vault, add the servicePrincipal to the **Access Policies** with the following permissions:

















      AskCopy



      ```
      secrets/get permission
      secrets/list permission
      ```


2. In the Prisma Cloud Console, go to **Manage > Authentication > Secrets**.

3. Click **Add store**.









1. Enter a name for the vault. This name is used when you create rules to inject secrets into specific containers.

2. For **Type**, select **Azure Key Vault**.

3. For **Address**, enter **https://<vault-name>.vault.azure.net**. This address can be found in the Azure Key Vault’s properties in the _DNS Name_ element.

4. In **Credential**, click **Add new**.











      If you create a credential in the credentials store ( **Manage > Authentication > Credentials store**), your service principal authenticates with a password.

5. Enter a name for the credentials.

6. In **Type**, select **Azure**.

7. In **Service Key**, enter the JSON credentials returned from the _az ad sp create-for-rbac_ command.

8. Click **Save**.

9. Click **Add**.











      After adding the new store, Prisma Cloud tries conecting to your vault. If it is successful, the dialog closes, and an entry is added to the table. Otherwise, any connection errors are displayed directly in the configuration dialog.











      Next, [inject a secret into a container](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets).


[PreviousAWS Systems Manager Parameters Store](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/aws-systems-manager-parameters-store) [NextCyberArk Enterprise Password Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/cyberark-enterprise-password-vault)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
