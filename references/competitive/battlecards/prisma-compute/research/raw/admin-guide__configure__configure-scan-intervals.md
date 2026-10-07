For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals.md).

You can specify how often Prisma Cloud scans your environment for vulnerabilities and compliance issues. By default, Prisma Cloud scans your environment every 24 hours. Images are re-scanned when changes are detected. For example, pulling a new image triggers a scan.

Prisma Cloud scans for vulnerabilities and/or compliance issues in:

- Images

- VMware Tanzu blobstores

- Containers

- Serverless functions

- Hosts

- Cloud platforms

- Registries

- VM images


Scan intervals can be separately configured for each type of object.

## Configuring scan intervals[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals\#configuring-scan-intervals)

The scan frequency is configurable. By default, Prisma Cloud scans your environment every 24 hours.

1. Open Console.

2. Go to **Manage > System > Scan**.

3. Scroll down to the **Scheduling** section.

4. Set the scan intervals for each type according to your requirements.











Scan intervals are specified in hours.

5. Scroll to the bottom of the page, and click **Save**.


## Last scan time[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals\#last-scan-time)

Console reports the last time Defender scanned your environment. Go to **Manage > Defenders > Manage**, and click a row in the table to get a detailed status report for each deployed Defender. The sidecar shows the last time Defender scanned the containers and images on the host where it runs.

## Scan performance[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals\#scan-performance)

Scanning for malware in archives in container images consumes a lot of resources. The scanner unpacks each archive to search for malicious software. Checksums must be individually calculated for each file. Because of the performance impact and the way containers tend to be used, malware in archives is an unlikely threat. As such, **Scan for malware within archives in images** is disabled by default.

If this option is enabled, Prisma Cloud supports the following archive file types.

- ZIP

- GZ

- TAR

- WAR

- JAR

- EAR


If the archive is over 512Mb, Prisma Cloud will not scan it.

## Scan Running Images[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals\#scan-running-images)

The scan Running Images toggle optimizes resource usage by limiting scans to images tied to active containers. This is especially useful in production environments, where many images on a host may never be executed, making their scanning unnecessary.

- When enabled, Defenders will scan only images linked to currently running containers.

- When disabled, Defenders will scan all images on the host, regardless of their container status.


In dynamic environments, it’s possible for images that were recently running to still be scanned, even if they are no longer active at the time of the scan. This may give the impression that non-running images are being scanned.

## Scan JavaScript components in manifest but not on disk[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals\#scan-javascript-components-in-manifest-but-not-on-disk)

The purpose of this option is to show vulnerabilities in dependencies that might not exist on disk (which are often development dependencies).

Most Node.js packages contain a package.json that lists all of its dependencies (both dependencies, and devDependencies). When parsing a Node.js package discovered during a scan, if this option is enabled, Prisma Cloud appends the all packages found in each package.json to the list of packages to be assessed for vulnerabilities. This option isn’t recommended for production scenarios because it can generate a significant number of false positives.

If this option is disabled (default), Prisma Cloud only evaluates the packages that are actually found on disk during scan. This is the recommended setting for production scenarios.

- When scanning images with twistcli, use `--include-js-dependencies` to enable this option.

- For agentless scanning, this option is enabled by default and cannot be disabled. The agentless scan includes all JavaScript package dependencies listed in the `package.json` file, which may result in identifying vulnerabilities in dependencies that are not physically present on the disk. This can lead to differences in reported vulnerabilities compared to other scanning methods.


## Unrated vulnerabilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals\#unrated-vulnerabilities)

When **Show vulnerabilities that are of negligible severity** is enabled, the scanner reports CVEs that aren’t scored yet or have a negligible severity. Negligible severity vulnerabilities don’t pose a security risk, and are often designated with a status of "will not fix" or similar labels by the vendor. They are typically theoretical, require a very special (unlikely) situation to be exploited, or cause no real damage when exploited.

By default, this setting is disabled to strip unactionable noise from your scan reports.

## Orchestration[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals\#orchestration)

Kubernetes and other orchestrators have control plane components implemented as containers. By default, Prisma Cloud doesn’t scan orchestrator utility containers for vulnerability and compliance issues.

[PreviousCertificates](https://docs.prismacloud.io/admin-guide/configure/certificates) [NextUser certificate validity period](https://docs.prismacloud.io/admin-guide/configure/user-cert-validity-period)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
