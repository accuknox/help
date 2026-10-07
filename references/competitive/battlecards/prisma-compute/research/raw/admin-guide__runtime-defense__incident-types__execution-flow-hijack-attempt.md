For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/execution-flow-hijack-attempt.md).

An execution flow hijack attempt incident indicates that a possible attempt to hijack a program execution flow was observed. Special Linux library system files, which have a system-wide effect, were altered (this is usually undesirable, and is typically employed only as an emergency remedy or maliciously).

## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/execution-flow-hijack-attempt\#investigation)

The following incident shows that the binary _sudo_ wrote to _ld.so.preload_ file, which is a special Linux system file that impacts the entire system. By editing the Linux dynamic loader or files relied upon by the loader such as _ld.so.preload_, the attacker can inject malicious code to any binary execution.

For further information about these files, see the following [link](https://man7.org/linux/man-pages/man8/ld.so.8.html).

![execution flow hijack attempt incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6d83c8df76083bf7a51e3a61e1de50e88ceafc8e%252Fexecution_flow_hijack_attempt_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=60fc4bc5159a4298ed2506c2e54d5e30&sv=3)

Your investigation should focus on:

- Determining the process that opened the Special Linux file.

- If the source of the alteration was an interactive process (such as shell), determine how an attacker gained access to that process.

- Review the forensics date for the host, other entries in the Incident Explorer, and audits from the source, looking for unusual process execution, hijacked processes, and explicit execution of commands.


## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/execution-flow-hijack-attempt\#mitigation)

A full mitigation strategy for this incident begins by resolving the issues that allowed the attacker to access and modify the system file.

In addition, track the change that was done to the configuration in the system file. For example, in case of detected modification to the _ld.so.preload_ file, look for the shared library that was added to the file and determine the source of this malicious shared library.

Ensure that compliance benchmarks are appropriately applied to the affected resources. For example, if the critical file systems in the host are mounted read-only, it will be more difficult for an attacker to change system files and configurations to their advantage.

[PreviousCrypto miners](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/crypto-miners) [NextKubernetes attack](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/kubernetes-attack)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
