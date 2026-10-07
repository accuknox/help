For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/secrets/secrets-manager.md).

Containers often require sensitive information, such as passwords, SSH keys, encryption keys, and so on. You can integrate Prisma Cloud with many common secrets management platforms to securely distribute secrets from those stores to the containers that need them.

Enterprise secret stores reduce the risk of data breaches that could occur when sensitive information is littered across an organization, often in places where they should not be, such as email inboxes, source code repositories, developer workstations, and Dropbox. Secret stores provide a central and secure location for managing and distributing secrets to the apps that need them. They give you a way to account for all the secrets in your organization with audit trails that show how they are being used.

Orchestrators such as kubernetes and openshift, offer their own built-in secret stores with support for creating secrets, listing them, deleting them, and injecting them into containers. However, if you already have an enterprise secrets store, then you probably want to extend it to handle to your container environment. Utilizing the orchestrator’s built-in secrets management capabilities when you already have an enterprise secrets store is unappealing because it represents another silo of sensitive information that needs to be carefully secured. It undermines the principal benefit of a secrets store, which is managing all sensitive data in a single location.

## Theory of Operation[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/secrets-manager\#theory-of-operation)

When a user or orchestrator starts a container, Defender injects the secrets you specify into the container. In order for secret injection to work, all Docker commands must be routed through Defender. Refer to [Inject Secrets into Containers](https://docs.prismacloud.io/admin-guide/secrets/inject-secrets). There are several moving parts in the solution:

![secrets manager 791688](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a888375cf9bbaf3216e710b01b8098220100063f%252Fsecrets_manager_791688.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=db3361cf48a8539233b3e93b30001a73&sv=3)

**A**. Secret values are fetched, encrypted, and stored in Console’s database when a rule is created or modified. Secret values in Console’s database are periodically synced with the secrets store to provide resiliency in the case of connectivity outages and to optimize performance. All secrets cached on disk, both in Defender and in Console, are protected with 256 bit AES encryption. If you change a secret’s value in the secrets store and you need it synced immediately, you can click the refresh button in the Console UI to refetch all secrets from their configured stores.

**1**. Operator (or orchestrator) starts a container with docker run.

**2**. Defender assesses the command against the policy installed in Console.

**3**.The secret is returned to Defender. Defender starts the container using the Docker API, which is exposed through the Docker daemon’s local UNIX socket, and injects the secret into the container.

## Capabilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/secrets-manager\#capabilities)

The Prisma Cloud secrets manager has the following capabilities:

- Supports integration with common secrets management platforms.

- Manages the distribution of secrets from the secret store to your containers through policies. In Console, you create the rules that control which secrets get injected into which containers.

- Injects secrets into containers as either environment variables or files.

- Secrets injected as environment variables are presented in-the-clear from within the container. They are redacted from the outside to prevent exposure by the docker inspect command.

- Secrets injected as files are provided from an in-memory filesystem (on /run/secrets/<SECRET\_NAME>) that is mounted into the container when it is created. When the container is stopped, the secrets directory is unmounted and deleted.


## Best practices[Direct link to heading](https://docs.prismacloud.io/admin-guide/secrets/secrets-manager\#best-practices)

There are a number of ways that secrets can be compromised.

**Defender is bypassed.** If Defender is bypassed, an attacker can execute Docker commands directly against the Docker daemon’s local UNIX socket, and he will be able to expose your secrets. Be sure that your hosts are secured with least privilege access so that users can only run docker commands through Defender.

![secrets manager 790254](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-b243c45de5e701fdf0f58447226dc0403b1507c0%252Fsecrets_manager_790254.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e3936860ce44d9bab43423cb8273a1e2&sv=3)

**Limit lower privileged users to monitoring commands, such as docker ps and docker inspect.** Prisma Cloud automatically encrypts secrets injected as environment variables when accessed from docker inspect. Restrict commands such as docker exec and docker run to just the operators that need them because these commands can reveal secrets injected into a container by giving the user shell access inside the container, where variables are in the clear. For example, docker exec printenv on a running container, or docker run <IMAGE\_ID> printenv on an image, can reveal environment variables that are otherwise encrypted with docker inspect. The following diagram shows one way to grant access to Docker functions based on a user’s role. This is the way that Docker Datacenter Universal Control Plane (UCP) grants permissions, and you can implement the same scheme with Prisma Cloud’s access control rules.

![secrets manager 790256](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5eecaa2e7e75c2c071b4446f07f30e6635c9eeda%252Fsecrets_manager_790256.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e8f782983b933d61148e3407f8c2e463&sv=3)

[PreviousSecrets](https://docs.prismacloud.io/admin-guide/secrets/secrets) [NextIntegrate with a secrets store](https://docs.prismacloud.io/admin-guide/secrets/integrate-with-secrets-stores)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
