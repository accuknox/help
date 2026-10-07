For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-ssh-access.md).

Backdoors give attackers a way to bypass normal authentication systems, and are used to secure remote access to a system.

Backdoor SSH access incidents indicate that an attacker might have changed the configuration of a resource to enable remote access to the resource.

## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-ssh-access\#investigation)

In the following incident, you can see two audits. The first audit is a file system event that shows a new certificate was created in _/etc/openvpn_. An attacker could use this certificate for follow-on access to the container.

![backdoor ssh access incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5380984bf99a48caa8681ef2a52a2e56cc55c3e5%252Fbackdoor_ssh_access_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=04ae58c941e577100b92deb7746c8666&sv=3)

The first step in an investigation is to validate that the changes represent a bona fide security incident. In this example, it’s unlikely that a change in the ca cert file is a valid one, but it might not always be so clear.

After validating that this is a security incident, the next step is determining how an attacker was able to modify the system configuration. This would, generally, be a post-compromise approach to maintain access to the compromised systems. Check Incident Explorer for other potentially related incidents. Review additional runtime audits for the source to see if there are other clues.

Review access to the container and ensure that accesses weren’t subsequently used for further access to systems and data.

## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-ssh-access\#mitigation)

A full mitigation strategy for this incident begins with resolving the issues that allowed the attacker to modify the system configuration.

Ensure that compliance benchmarks are appropriately applied to the affected resources. For example, if the critical file systems in the container are mounted read-only, it will be more difficult for an attacker to change a configuration to their advantage.

[PreviousBackdoor admin accounts](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-admin-accounts) [NextCrypto miners](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/crypto-miners)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
