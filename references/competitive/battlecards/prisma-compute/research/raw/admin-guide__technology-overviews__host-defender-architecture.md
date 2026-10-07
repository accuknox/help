For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/technology-overviews/host-defender-architecture.md).

Because we’ve built Prisma Cloud expressly for cloud native stacks, the architecture of our agent (what we call Defender) is quite different. Rather than having to install a kernel module, or modify the host OS at all, Defender instead runs as a systemd or system module (not a kernel module) in user space, intercepting every syscall interaction and file changes, and actively blocking or alerting according to the rules defined in Console.

![host defender architecture](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-da066608292d255c8862784fbd2c610f391fe10c%252Fhost_defender_architecture.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0acad4b66a647abfe1c4fb43b775502d&sv=3)

[PreviousDefender architecture](https://docs.prismacloud.io/admin-guide/technology-overviews/defender-architecture) [NextTLS v1.2 cipher suites](https://docs.prismacloud.io/admin-guide/technology-overviews/tls-v12-cipher-suites)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
