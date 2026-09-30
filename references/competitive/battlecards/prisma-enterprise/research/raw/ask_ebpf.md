# Does Prisma Cloud Defender use eBPF for runtime monitoring?

No — the Prisma Cloud Defender runtime monitoring docs don’t mention eBPF.

Instead, the documented Defender architecture is **user-space** and **not a kernel module**. Defender “runs as a systemd or system module (not a kernel module) in user space,” where it **intercepts syscall interactions and file changes**, then blocks or alerts based on Console rules ([Host Defender Architecture](/content-collections/runtime-security/install/deploy-defender/host/host-defender-architecture.md), [Defender Architecture](/content-collections/runtime-security/install/deploy-defender/defender-architecture.md)).

For network monitoring/firewalls, the docs also describe **iptables rules** being created on the host to observe network traffic ([Defender Architecture](/content-collections/runtime-security/install/deploy-defender/defender-architecture.md)).

So, based on the content available in these docs: **eBPF isn’t documented as part of runtime monitoring**.

# Suggested Follow-up Questions:

If you need more information, consider asking one of these follow-up questions by performing an HTTP GET request on the URL:

- [Is eBPF mentioned elsewhere?](https://docs.prismacloud.io?ask=Is%20eBPF%20mentioned%20elsewhere%3F)
- [How does Defender monitor CPU calls if not eBPF?](https://docs.prismacloud.io?ask=How%20does%20Defender%20monitor%20CPU%20calls%20if%20not%20eBPF%3F)
- [What kernel features does Defender rely on?](https://docs.prismacloud.io?ask=What%20kernel%20features%20does%20Defender%20rely%20on%3F)

# Sources:

- [Runtime defense for serverless](https://docs.prismacloud.io/admin-guide/32/runtime-defense/runtime-defense-serverless.md)
- [Deploy Defender](https://docs.prismacloud.io/admin-guide/32/install/deploy-defender/orchestrator.md)
- [Runtime defense for serverless](https://docs.prismacloud.io/admin-guide/33/runtime-defense/runtime-defense-serverless.md)
- [Deploy Defender](https://docs.prismacloud.io/admin-guide/33/install/deploy-defender/orchestrator.md)
- [Runtime Defense for Serverless](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-serverless.md)
- [Deploy Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator.md)
- [Runtime defense for serverless](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-serverless.md)
- [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/33/runtime-defense/runtime-defense-app-embedded.md)
- [Firewalls](https://docs.prismacloud.io/content-collections/runtime-security/firewalls.md)
- [Runtime defense for App-Embedded](https://docs.prismacloud.io/admin-guide/32/runtime-defense/runtime-defense-app-embedded.md)
- [Host Defender architecture](https://docs.prismacloud.io/admin-guide/33/technology-overviews/host-defender-architecture.md)
- [Host Defender Architecture](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/host/host-defender-architecture.md)
- [Host Defender architecture](https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture.md)
- [Host Defender architecture](https://docs.prismacloud.io/admin-guide/32/technology-overviews/host-defender-architecture.md)
- [Deploy Orchestrator Defender](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/kubernetes.md)
- [Defender Architecture](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/defender-architecture.md)
- [Deploy the Prisma Cloud Defender](https://docs.prismacloud.io/admin-guide/33/install/deploy-defender.md)

