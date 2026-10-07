For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-admin-accounts.md).

Backdoors are a method for bypassing normal authentication systems, and are used to secure remote access to a system.

Backdoor admin account incidents surface event patterns that indicate an actor might have created or modified a configuration to enable the continued use of a privileged account.

## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-admin-accounts\#investigation)

In the following incident, you can see that a python script was used to modify _/etc/passwd_, potentially enabling an attacker to add or change a user account. In addition, there was other suspicious network activity that was made by the same python process.

![backdoor admin access incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7453dde6b5994b65e5e54a51f0c8314d80779314%252Fbackdoor_admin_access_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=38621be60ec3aa3bd42ff7bba60396ce&sv=3)

The first step in an investigation is to validate that the changes represent a bona fide security incident. In this case, the events that led to the incident seem to indicate a valid security incident, but you should examine the changes to _/etc/passwd_ to see if they represent the potential for an attacker to maintain persistence.

Having determined that this is a bona fide incident, then the next steps focus on determining how an attacker was able to modify the system configuration. This would, generally, be a post-compromise approach to maintain access to the compromised systems. Check Incident Explorer for additional incidents. Review additional runtime audits for the source to see if there are other clues.

Review access to the container and ensure that the affected account(s) weren’t subsequently used for further access to systems and data.

## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-admin-accounts\#mitigation)

A full mitigation strategy for this incident begins with resolving the issues that allowed the attacker to modify the system configuration.

Ensure that compliance benchmarks are appropriately applied to the affected resources. For example, if the critical file systems in the container are mounted read-only, it will be more difficult for an attacker to change a configuration to their advantage.

[PreviousAltered binary](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/altered-binary) [NextBackdoor SSH access](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/backdoor-ssh-access)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
