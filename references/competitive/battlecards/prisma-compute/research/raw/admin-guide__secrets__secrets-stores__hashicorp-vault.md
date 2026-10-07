For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/hashicorp-vault.md).

You can integrate Prisma Cloud with HashiCorp Vault. Prisma Cloud supports the K/V Secrets Engine v2 in Vault 0.10.x, and K/V Secrets Engine v1 in Vault 0.9.x and older. Prisma Cloud does not support K/V Secrets Engine v1 in Vault 0.10.x.

First configure Prisma Cloud to access HashiCorp Vault, then create rules to inject the relevant secrets into the relevant containers.

1. In Console, go to **Manage > Authentication > Secrets**.

2. Click **Add store**.









1. Enter a name for the vault. This name is used when you create rules to inject secrets into specific containers.

2. For **Type**, select **HashiCorp Vault**. Choose the version that matches the version of Vault installed in your environment.

3. Fill out the rest of the form, specifying how to connect to your vault.

4. Click **Add**.











      After clicking **Add**, Prisma Cloud tries conecting to your vault. If it is successful, the dialog closes, and an entry is added to the table. Otherwise, any connection errors are displayed directly in the configuration dialog.











      Next, [inject a secret into a container](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets).


[PreviousCyberArk Enterprise Password Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/cyberark-enterprise-password-vault) [NextInject secrets into containers](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
