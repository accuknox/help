For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/vm-image-scanning.md).

Prisma Cloud can scan the virtual machine (VM) images in your cloud environment for the following types of vulnerabilities:

- **Host configuration**: Vulnerabilities in the VM image setup.

- **Docker daemon configuration**: Vulnerabilities that stem from misconfiguring your Docker daemon. The Docker daemon derives its configuration from various files, including `/etc/sysconfig/docker` or `/etc/default/docker`.

- **Docker daemon configuration files**: Vulnerabilities that arise from setting incorrect permissions on critical configuration files.

- **Docker security operations**: Recommendations and reminders for extending your current security best practices to include containers.

- **Linux configuration**: Compliance of Linux hosts. For example, ensure mounting of the `hfs` filesystem is disabled.


## Reviewing VM image scan reports[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/vm-image-scanning\#reviewing-vm-image-scan-reports)

To view the health of the VM images in your environment:

1. Open Console, then go to **Monitor > Compliance > Hosts > VM images**.











Select **CSV** or **PDF** to export all the compliance issues identified in the latest VM image scan to a CSV or a PDF file respectively.

2. Click on a VM image on the list.











A report for the compliance issues on the VM image is shown.


[PreviousHost scanning](https://docs.prismacloud.io/admin-guide/compliance/host-scanning) [NextApp-Embedded scanning](https://docs.prismacloud.io/admin-guide/compliance/app-embedded-scanning)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
