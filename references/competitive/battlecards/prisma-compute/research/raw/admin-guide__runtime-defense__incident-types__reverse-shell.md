For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/reverse-shell.md).

Reverse shell is a method used by attackers for gaining access to a victim’s system. A reverse shell is a established by a malicious payload executed on a targeted resource which connects to a pre-configured host and provides an attacker the means to execute interactive shell commands through that connection.

## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/reverse-shell\#investigation)

In the following incident, you can see that a reverse shell was used to provide a remote user interactive shell on this host, potentially enabling an attacker to execute any command that the user used to launch the reverse shell is authorized to execute.

![reverse shell](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-62a10c5ac800add77bcdf8306ee77c8e92b04647%252Freverse_shell.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=05958b8bf935b3d4f15b2626c59cd1ce&sv=3)

The first step in an investigation is to validate that the reverse shell represent a bona fide security incident. While it is unlikely that a legitimate application or user is using a reverse shell for legitimate reasons, the first step should be validation that the reported application and user have not used reverse shell intentionally.

In this case it appears that a user used nc in order to allow a remote shell via ssh. "View forensics data" can be used to gain better understanding on what was done via the shell and understand whether this was for legitimate activity.

Having determined that this is a bona fide incident, the next steps focus on determining how an attacker managed to execute the process that allowed them to initiate the remote shell.

Check Incident Explorer for additional incidents. Review additional runtime audits for the source to see if there are other clues.

Review access to the resources and ensure that the affected account(s) weren’t subsequently used for further access to systems and data.

## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/reverse-shell\#mitigation)

A full mitigation strategy for this incident begins with resolving the issues that allowed the attacker to execute the process that initiated the remote shell.

Ensure that compliance benchmarks and patches are appropriately applied to the affected resources. For example, an unpatched critical vulnerability can be abused to execute a process that allows for the remote shell to be triggered remotely.

[PreviousPort scanning](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/port-scanning) [NextSuspicious binary](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/suspicious-binary)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
