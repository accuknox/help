For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/cyberark-enterprise-password-vault.md).

You can integrate Prisma Cloud with CyberArk Enterprise Password Vault (EPV). To retrieve passwords from the vault, Prisma Cloud uses the CyberArk Central Credential Provider (CCP) web service. Prisma Cloud supports CyberArk CCP version 12.1.0 with Digital Vault version 12.2.0. To integrate with CyberArk EPV, first configure Prisma Cloud to access CyberArk Enterprise Password Vault, then create rules to inject the relevant secrets into the relevant containers.

1. In Console, go to **Manage > Authentication > Secrets**.

2. Click **Add store**.









1. Enter a name for the vault. This name is used when you create rules to inject secrets into specific containers.

2. For **Secret type**, select **CyberArk Enterprise Password Vault**.

3. In **Settings**, fill out the form as follows:









      1. Address: the address and port of the Central Credential Provider web service.

      2. Application ID: The application ID that Prisma Cloud should use to issue each password request. To configure this for CCP 12.1, see [here](https://docs.cyberark.com/Product-Doc/OnlineHelp/AAM-CP/12.1/en/Content/Common/Adding-Applications.htm?tocpath=Administration%7CManage%20applications).

      3. CA certificate (Optional): for an application configured to authenticate using a client certificate, the certificate of the CA that signed the CyberArk server’s certificate in PEM format. For more information about this authentication method for CCP 12.1 see [here](https://docs.cyberark.com/Product-Doc/OnlineHelp/AAM-CP/12.1/en/Content/CP%20and%20ASCP/Application-Authentication-Methods-general.htm?tocpath=Administration%7CManage%20applications%7CApplication%20authentication%7CApplication%20authentication%20methods).

      4. Client certificate (Optional): for an application configured to authenticate using a client certificate, the client certificate in PEM format.


4. Click **Add**.











      After clicking **Add**, Prisma Cloud tries conecting to your vault. If it is successful, the dialog closes, and an entry is added to the table. Otherwise, any connection errors are displayed directly in the configuration dialog.











      Next, [inject a secret into a container](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets).


[PreviousAzure Key Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/azure-key-vault) [NextHashiCorp Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/hashicorp-vault)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
