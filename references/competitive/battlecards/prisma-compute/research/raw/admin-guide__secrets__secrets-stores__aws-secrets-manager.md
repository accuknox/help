For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/aws-secrets-manager.md).

You can integrate Prisma Cloud with AWS Secrets Manager. First, configure Prisma Cloud to access AWS Secrets Manager, then create rules to inject the relevant secrets into the relevant containers.

**Prerequisites:**

- The service account Prisma Cloud uses to access the secrets store must have the following permissions:









  - secretsmanager:GetSecretValue

  - secretsmanager:ListSecrets


- You have [created a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) in AWS Secrets Manager. Automatic rotation must be disabled. Prisma Cloud supports the key-value secret type only. When storing a new secret, select **Other type of secrets**, then **Secret key/value**.















![aws secrets manager secret type](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-30312370cfde30b29f04568a9b679ceb6ac9c2e9%252Faws_secrets_manager_secret_type.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c1307f136da86a81c53daff8b647b043&sv=3)


1. Open Prisma Cloud Console.

2. Integrate Prisma Cloud with the secrets store.









1. Go to **Manage > Authentication > Secrets**, and click **Add store**.

2. Enter a name for the store. This name is used when you create rules to inject secrets into specific containers.

3. For **Type**, select **AWS Secrets Manager**, then fill out the rest of the form, including your credentials.

4. Fill out the rest of the form, specifying how to connect to the Secrets Manager.

5. Click **Add**.











      After clicking **Add**, Prisma Cloud tries connecting to your secrets manager. If successful, the dialog closes, and an entry is added to the table. Otherwise, connection errors are displayed directly in the configuration dialog.











      Next, [inject a secret into a container](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets).


[PreviousSecrets stores](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores) [NextAWS Systems Manager Parameters Store](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/aws-systems-manager-parameters-store)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
