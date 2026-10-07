For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/integrate-with-secrets-stores.md).

To inject secrets into your containers, you must first integrate Prisma Cloud with your secrets manager, and then set up rules for injecting specific secrets into specific containers.

Prisma Cloud can integrate with the following secrets managers:

- [AWS Secrets Manager](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/aws-secrets-manager)

- [AWS Systems Manager Parameters Store](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/aws-systems-manager-parameters-store)

- [Azure Key Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/azure-key-vault)

- [CyberArk Enterprise Password Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/cyberark-enterprise-password-vault)

- [HashiCorp Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/hashicorp-vault) (versions 0.9.x and older, and versions 0.10 and later)


## Refresh interval[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/integrate-with-secrets-stores\#refresh-interval)

By default, the refresh interval is disabled. That means if you change a secret’s value in the secrets store, you must force Prisma Cloud to update its list of values. In Console, go to **Defend > Access > Secrets** and click **Refresh secrets** to force Prisma Cloud to fetch the latest values of all secrets from their configured stores.

You can also configure Prisma Cloud to periodically retrieve the latest values of all the secrets from their stores. In Console, go to **Manage > Authentication > Secrets**, click **Edit** next to the **Secrets refresh interval** field, and specify an integer value in hours. Setting the refresh interval to 0 disables automatic periodic refreshes.

[PreviousSecrets manager](https://docs.prismacloud.io/admin-guide/secrets/secrets-manager) [NextSecrets stores](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
