For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/kubernetes-attack.md).

Exploiting weaknesses in the container orchestrator to manipulate cluster settings is known as a Kubernetes attack. This incident indicates attempts to directly access Kubernetes infrastructure from within a running container. This may be an attempt to compromise the orchestrator.

Actions that can trigger this incident include attempts to download and use Kubernetes administrative tools within a container, in addition to any attempts to access Kubernetes metadata.

To detect Kubernetes attacks, you must have a runtime rule with the **Detect Kubernetes attacks** option enabled.

## Investigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/kubernetes-attack\#investigation)

The following incident shows that a container queried kubelet metric API, which might be an attempt to compromise the orchestrator.

![kubernetes attack incident](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-5c14112fbc27223cc869d6f97f03797ff857cbc1%252Fkubernetes_attack_incident.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=00e1821ea77cad094678c25d262909fc&sv=3)

The first step in an investigation is to validate that the changes represent a bona fide security incident. Having determined that this is a bona fide incident, then the next steps focus on determining how an attacker would have gained access to the resources with access to the Kubernetes cluster. Also, it is important to restrict access to your cluster by following best practices regarding access control.

Review your Kubernetes cluster to ensure that no actions were taken to compromise your cluster. In addition, closely review the audit actions and the forensic data available through incident explorer to understand the scope of the incident.

## Mitigation[Direct link to heading](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/kubernetes-attack\#mitigation)

A full mitigation strategy for this incident begins with resolving the issues that allowed the attacker to attempt to access the Kubernetes infrastructure.

For additional protection, customize your runtime rules to _prevent_ or _block_ actions that access the metadata services or the open local kubelet port. Compliance rules should include checks set to _alert_ or _block_ to ensure your containers and hosts are following the best practices for Kubernetes.

[PreviousExecution flow hijack attempt](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/execution-flow-hijack-attempt) [NextLateral movement](https://docs.prismacloud.io/admin-guide/runtime-defense/incident-types/lateral-movement)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
