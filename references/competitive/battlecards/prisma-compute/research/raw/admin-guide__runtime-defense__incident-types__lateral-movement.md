For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/lateral-movement.md).

Lateral movement incidents indicate that an attacker is using tools and techniques that enable movement between resources on a network.

## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/lateral-movement\#investigation)

The following incident shows that netcat was used to establish a listener on port 9000.

![lateral movement incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-aaafaaa94bd1f103dc56b7cdf5a08fc358cdc2c2%252Flateral_movement_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=44b246184c643f19200aafff0028ec1e&sv=3)

This behavior is a probable precursor to creating a reverse shell, allowing network-based remote control of another resource.

Your investigation should focus on:

- Determining how the process in the alert, such as _nc.openbsd_, was executed. Review additional entries in Incident Explorer and other audits from the source, looking for unusual process execution, and explicit execution of commands.

- Reviewing container runtime audits to determine if the target successfully connected.

- If the target did successfully connect, determine what the attacker was able to do and if they were able to move further through the network.


## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/lateral-movement\#mitigation)

After determining the cause of the process execution, resolve the problem, whether it be an exposed vulnerability, a configuration issue, or something else.

For additional protection, enable the _prevent_ or _block_ actions in the applicable runtime rules to take action when anomalous processes, such as _netcat_, are executed.

[PreviousKubernetes attack](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/kubernetes-attack) [NextMalware](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/malware)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
