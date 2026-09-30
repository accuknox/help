> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/defender-architecture.md).

# Defender Architecture

Customers often ask how Prisma Cloud Defender really works under the covers. Prisma Cloud leverages Docker’s ability to grant advanced kernel capabilities to enable Defender to protect your whole stack, while being completely containerized and utilizing a least privilege security design.

## Defender Design

Because we’ve built Prisma Cloud expressly for cloud native stacks, the architecture of our agent (what we call Defender) is quite different. Rather than having to install a kernel module, or modify the host OS at all, Defender instead runs as a Docker container and takes only those specific system privileges required for it to perform its job. It does not run as --privileged and instead takes the specific system capabilities of net\_admin, sys\_admin, sys\_ptrace, mknod, and setfcap that it needs to run in the host namespace and interact with both it and other containers running on the system. You can see this clearly by inspecting the Defender container:

```bash
# docker inspect twistlock_defender_<VERSION> | grep -e CapAdd -A 7 -e Priv
            "CapAdd": [
                "NET_ADMIN",
                "SYS_ADMIN",
                "SYS_PTRACE",
                "MKNOD",
                "SETFCAP"
            ],
--
            "Privileged": false,
```

This architecture allows Defender to have a near real time view of the activity occurring at the kernel level. Because we also have detailed knowledge of the operations of each container, we can correlate the kernel data with the container data to get a comprehensive view of process, file system, network, and system call activity from the kernel and all the containers running on it. This access also allows us to take preventative actions like stopping compromised containers and blocking anomalous processes and file system writes.

Critically, though, Defender runs as a user mode process. If Defender were to fail (and if that were to happen, it would be restarted immediately), there would be no impact on the containers on the host, nor the host kernel itself. Additionally, we can and do apply `cgroups` to set hard limits on CPU and memory consumption, guaranteeing it will be a ‘good neighbor' on the host and not interfere with host performance or stability.

In the event of a communications failure with Console, Defender continues running and enforcing the active policy that was last pushed by the management point. Events that would be pushed back to Console are cached locally until it is once again reachable.

## Why not a kernel module?

Given the broad range of security protection Prisma Cloud provides, not just for containers, but also for the hosts they run on, you might assume that we use a kernel module - with all the associated baggage that goes along with that. However, that’s not actually how Prisma Cloud works.

Kernel modules are compiled software components that can be inserted into the kernel at runtime and typically provide enhanced capabilities for low level functionality like process scheduling or file monitoring. Because they run as part of the kernel, these components are very powerful and privileged. This allows them to perform a wide range of functions but also greatly increases the operational and security risks on a given system. The kernel itself is extensively tested across broad use cases, while these modules are often created by individual companies with far fewer resources and far more narrow test coverage.

Because kernel modules have unrestricted system access, a security flaw in them is a system wide exposure. A single unchecked buffer or other error in such a low level component can lead to the complete compromise of an otherwise well designed and hardened system. Further, kernel modules can introduce significant stability risks to a system. Again, because of their wide access, a poorly performing kernel module that’s frequently called can drag down performance of the entire host, consume excessive resources, and lead to kernel panics. For these reasons, many modern operating systems designed for cloud native apps, like Google Container-Optimized OS, explicitly prevent the usage of kernel modules.

## Defender-Console communication

By default, Defender connects to Console with a websocket on TCP port 443. All traffic between Defender and Console is TLS encrypted.

Defender has no privileged access to Console or the underlying host where Console is installed. By design, Console and Defender don’t trust each other and Defender mutual certificate-based authentication is required to connect. For more information about the Console-Defender communication certificates, see the [certificates article](/content-collections/runtime-security/configure/certificates.md). Pre-auth, connections are blocked. Post-auth, Defender’s capabilities are limited to getting policies from Console and sending event data to Console.

If Defender were to be compromised, the risk would be local to the system where it is deployed, the privilege it has on the local system, and the possibility of it sending garbage data to Console. Console communication channels are separated, with no ability to jump channels.

Defender has no ability to interact with Console beyond the websocket. Both Console’s API and web interfaces, served on port 443 (HTTPS), require authentication over a different channel with different credentials (e.g. username and password, access key, and so on), none of which Defender holds.

## Blocking rules

Defender is responsible for enforcing vulnerability and compliance blocking rules. When a blocking rule is created, Defender moves the original runC binary to a new path and inserts a Prisma Cloud runC shim binary in its place.

When a command to create a container is issued, it propagates down the layers of the container orchestration stack, eventually terminating at runC. Regardless of your environment (Docker, Podman, Kubernetes, or OpenShift) and underlying CRI provider, runC does the actual work of instantiating a container.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d44641311f82e7c1cb2bcb041e7d52b1cd4c1054%2Fdefender-runc.png?alt=media" alt="defender runc"><figcaption></figcaption></figure>

When starting a container in a Prisma Cloud-protected environment:

1. The Prisma Cloud runC shim binary intercepts calls to the runC binary.
2. The shim binary calls the Defender container to determine whether the new container should be created based on the installed policy.
   * If Defender replies affirmatively, the shim calls the original runC binary to create the container, and then exits.
   * If Defender replies negatively, the shim terminates the request.
   * If Defender does not reply within 60 seconds, the shim calls the original runC binary to create the container and then exits.

The last step guarantees that Defender always fails open, which is important for the resiliency of your environment. Even if the Defender process terminates, becomes unresponsive, or cannot be restarted, a failed Defender will not hinder deployments or the normal operation of a node.

## Firewalls

Defender enforces WAF policies (WAAS) and monitors layer 4 traffic (CNNS). In both cases, Defender creates iptables rules on the host so it can observe network traffic. For more information, see [CNNS](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/firewalls/cnns-saas.md) and [WAAS architecture](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/runtime-security/waas/waas.md).


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/defender-architecture.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
