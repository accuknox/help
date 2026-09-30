# Does Prisma Cloud runtime defense detect fileless malware or processes executed from memory (memfd)?

I can’t find any Prisma Cloud runtime defense documentation that explicitly confirms detection of **fileless malware** or processes executed from **memory** (for example, Linux `memfd`).

What the docs *do* describe are runtime detections tied to observable host behaviors, such as:

* **Processes running from temporary storage** — detects processes running from temporary storage and can **alert/prevent** on file creation or execution. See [Runtime defense for hosts](/admin-guide/32/runtime-defense/runtime-defense-hosts.md).
* Malware/behavior detections like **encrypted/packed binaries**, **execution flow hijack**, **webshell attacks**, and others in [Runtime Audits](/content-collections/runtime-security/runtime-defense/runtime-audits.md) and [Runtime defense for hosts](/admin-guide/32/runtime-defense/runtime-defense-hosts.md).

Because the available docs don’t mention `memfd`/fileless execution specifically, I can’t say whether those exact techniques are detected.

# Suggested Follow-up Questions:

If you need more information, consider asking one of these follow-up questions by performing an HTTP GET request on the URL:

- [Do they detect memfd-based malware?](https://docs.prismacloud.io?ask=Do%20they%20detect%20memfd-based%20malware%3F)
- [Which runtime detections cover fileless methods?](https://docs.prismacloud.io?ask=Which%20runtime%20detections%20cover%20fileless%20methods%3F)
- [Where to find host memory-based alerts?](https://docs.prismacloud.io?ask=Where%20to%20find%20host%20memory-based%20alerts%3F)

# Sources:

- [Runtime Audits](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-audits.md)
- [Runtime audits](https://docs.prismacloud.io/admin-guide/32/runtime-defense/runtime-audits.md)
- [Runtime audits](https://docs.prismacloud.io/admin-guide/33/runtime-defense/runtime-audits.md)
- [Runtime audits](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-audits.md)
- [Scan for Malware](https://docs.prismacloud.io/admin-guide/32/vulnerability-management/malware-scanning.md)
- [Scan for Malware](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/malware-scanning.md)
- [Scan for Malware](https://docs.prismacloud.io/admin-guide/33/vulnerability-management/malware-scanning.md)
- [Scan for Malware](https://docs.prismacloud.io/admin-guide/vulnerability-management/malware-scanning.md)
- [Runtime defense for hosts](https://docs.prismacloud.io/admin-guide/32/runtime-defense/runtime-defense-hosts.md)
- [Runtime defense for hosts](https://docs.prismacloud.io/admin-guide/33/runtime-defense/runtime-defense-hosts.md)
- [Runtime defense for serverless](https://docs.prismacloud.io/admin-guide/32/runtime-defense/runtime-defense-serverless.md)
- [Runtime defense for serverless](https://docs.prismacloud.io/admin-guide/33/runtime-defense/runtime-defense-serverless.md)
- [Runtime defense for serverless](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-serverless.md)
- [Runtime Defense for Serverless](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-serverless.md)
- [Host Defender architecture](https://docs.prismacloud.io/admin-guide/33/technology-overviews/host-defender-architecture.md)
- [Host Defender Architecture](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/host/host-defender-architecture.md)
- [Host Defender architecture](https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture.md)
- [Runtime Defense for Hosts](https://docs.prismacloud.io/content-collections/runtime-security/runtime-defense/runtime-defense-hosts.md)

