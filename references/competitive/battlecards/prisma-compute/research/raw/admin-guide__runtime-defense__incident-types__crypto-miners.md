For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/crypto-miners.md).

Cryptominers are software used to generate new coins in cryptocurrencies such as Bitcoin and Monero. These can be used legitimately by individuals; however, in containerized environments, they are often executed by attackers as a means of monetizing compromised hosts.

Unless you are intentionally running a cryptominer, this alert most likely indicates a security incident in which an attacker was able to introduce a cryptominer into your infrastructure and execute it.

![crypto miner incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-844b7651c89f4537bdd3fa22e8b7446f3da49d3b%252Fcrypto_miner_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=87c3305093e7fb95cd13219453152458&sv=3)

Our research indicates that the potential attack vectors include:

- A Kubernetes or Docker endpoint exposed to the Internet that allows unauthenticated access, or that is protected with weak credentials.

- A registry exposed to the Internet that allows unauthenticated users, or users with weak or common passwords, to make changes to stored images.

- Vulnerable code in a containerized service that has been exploited, followed by lateral movement and remote code execution.


## Enable Runtime Monitoring for Detection of Cryptominers[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/crypto-miners\#enable-runtime-monitoring-for-detection-of-cryptominers)

1. Ensure **Defend > Runtime > Container policy > Enable automatic runtime learning** is set to **on.**











Known cryptominers are part of the IS feed on Prisma Cloud and they detect high CPU consumption and network communications.

2. Add a new runtime rule.











When you add a new rule for container policy or serverless policy, it is enabled to alert you for cryptominer detection. You can modify this to block the activity.















![crypto miner action](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3bf359bb9d8f97b227cb60e975d8ffb5046152d3%252Fcrypto_miner_action.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4be5f5999d86d9ec6562b7a316a7e7f5&sv=3)


## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/crypto-miners\#investigation)

The first step in determining how the crypto miner was introduced is to determine if this is an existing image which has had unwanted processes introduced into it or if this is an entirely unwanted image. You can inspect the image itself in the Prisma Cloud Console.

![crypto miner image report](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-485aa85c0b75de18694f3a6472732de777f7dc1f%252Fcrypto_miner_image_report.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a6c69c9adc6df429e6f76fb718f4580b&sv=3)

We can see that this image comes from Docker Hub and that it is not an image that was developed internally. In this case, we would want to dig deeper into how the image was pulled and the container executed. You may have many sources of this information including the Prisma Cloud Docker access logs (Monitor/Access/Docker), which have been exported to CSV and filtered here:

![crypto miner csv](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c151b8410e786611bd4d597c53cd7768fa442f5b%252Fcrypto_miner_csv.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fd1ae190dc674b1994652ec918034a43&sv=3)

This shows that a user account, ‘alice’, was used to run ‘docker exec’ and start the container, and that the command was run locally. From here, we would want to review authentication logs on the system to determine how ‘alice’ was able to logon and to review other data to determine what else ‘alice’ was able to accomplish.

If the image was an existing one that the enterprise legitimately uses, the next steps in the investigation would be to determine how the image was modified to include the crypto miner. Start by reviewing the image in any registry where it is stored and looking at a history of changes made to the image. It may be necessary to walk through the entire CI/CD pipeline to determine if changes were made prior to being pushed to the registry.

## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/crypto-miners\#mitigation)

As soon as the investigation is complete, remove all instances of the running container (docker stop quirky\_payne \| docker rm quirky\_payne in this case). If the container(s) were started with an orchestrator like Kubernetes, it may be necessary to remove any configuration that would cause them to restart.

If the image was pushed to a registry, take steps to remove affected versions from the registry.

Secure all access, starting with any point of entry that was found. Ensure that only needed endpoints are exposed to the Internet and that authentication is required at each endpoint that could, directly or indirectly, result in remote code execution. Ensure accounts have strong passwords and, where possible, two-factor authentication.

Investigate any successful attack vectors that were found in the investigation. This may not be the only successful attack to have used this approach; instead, it may just be the most visible one.

[PreviousBackdoor SSH access](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-ssh-access) [NextExecution flow hijack attempt](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/execution-flow-hijack-attempt)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
