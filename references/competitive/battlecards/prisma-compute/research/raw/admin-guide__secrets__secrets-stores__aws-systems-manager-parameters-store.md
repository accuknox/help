For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/aws-systems-manager-parameters-store.md).

You can integrate Prisma Cloud with AWS Systems Manager Parameters Store. First configure Prisma Cloud to access the Parameters Store, then create rules to inject the relevant secrets into the relevant containers.

**Prerequisites:**

- The service account Prisma Cloud uses to access the Parameters Store must have the following permissions. These permissions are part of pre-existing policy named AmazonSSMReadOnlyAccess. For more information, see [Configure User Access for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-access-user.html).









  - ssm:Get\*

  - ssm:List\*


- You have [created a secret](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-console.html) in your Parameters Store. Prisma Cloud supports all parameter types. Note, however, that StringList is injected "as-is". For example, if the value you specify for parameter of type StringList is `twistlock,test,value`, then the injected environment variable would look like this:

















AskCopy



```
ENV_VAR=twistlock,test,value
```













![aws systems manager parameter store param type](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6fba0f7f3a71f9a3917284965788987b193bb73f%252Faws_systems_manager_parameter_store_param_type.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6c28e7ec921473c4106dfabfeb8b6bd9&sv=3)


1. Open Prisma Cloud Console.

2. Integrate Prisma Cloud with the store.









1. Go to **Manage > Authentication > Secrets**, and click **Add store**.

2. Enter a name for the store. This name is used when you create rules to inject secrets into specific containers.

3. For **Type**, select **AWS Systems Manager Parameters Store**.

4. Fill out the rest of the form, specifying how to connect to the store.

5. Click **Add**.











      After clicking **Add**, Prisma Cloud tries conecting to your store. If it is successful, the dialog closes, and an entry is added to the table. Otherwise, any connection errors are displayed directly in the configuration dialog.











      Next, [inject a secret into a container](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets).


[PreviousAWS Secrets Manager](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/aws-secrets-manager) [NextAzure Key Vault](https://docs.prismacloud.io/admin-guide/secrets/secrets-stores/azure-key-vault)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
