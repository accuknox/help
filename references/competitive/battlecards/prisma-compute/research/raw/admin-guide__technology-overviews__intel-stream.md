For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/technology-overviews/intel-stream.md).

The Prisma Cloud Intelligence Stream (IS) is a real-time feed that contains vulnerability data and threat intelligence from a variety of certified upstream sources. Prisma Cloud continuously pulls data from known vulnerability databases, official vendor feeds and commercial providers to provide the most accurate vulnerability detection results.

In addition to the information collected from official feeds, Prisma Cloud feeds are enriched with vulnerability data curated by a dedicated research team. Our security researchers monitor cloud and open source projects to identify security issues through automated and manual means. As a result, Prisma Cloud can detect new vulnerabilities that were only recently disclosed, and even vulnerabilities that were quietly patched.

The Prisma Cloud Console automatically connects to the Intelligence Stream server and downloads updates without any special configuration required. The Intelligence Stream (IS) is updated several times per day, and the consoles check continuously for updates.

## Multiple Intelligence Stream (IS) Builders[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/intel-stream\#multiple-intelligence-stream-is-builders)

Prisma Cloud has introduced versioning for Intelligence Stream (IS) to ensure compatibility across different Console and Defender versions.

The purpose of Intelligence Stream (IS) versioning is to:

- **Maintain functionality for older Consoles and Defenders**: IS versioning ensures that older Consoles and Defenders continue to operate properly, even if they cannot support the latest intelligence feeds. For example, if the intelligence feed undergoes a change in its external data format, this change will not disrupt the functionality of older Consoles and Defenders.

- **Reduce disruptions**: Versioning helps minimize disruptions caused by updates, such as changes in downloaded JSON file fields that could impact CVE accuracy or result in duplicate CVEs.


To ensure consistency in vulnerability reporting across all Intelligence Stream (IS) versions, the following approach is implemented:

- **New Intelligence Stream (IS) logic updates**: Enhancements, bug fixes, and updates to the IS logic, will always be applied to the latest IS version. When customers upgrade to the latest Console version, they will receive the most recent IS logic updates.

- **Vulnerability data**: All IS versions will continue to provide up-to-date vulnerability information, and changes in IS logic or algorithms will not affect the vulnerability metrics and reporting in the Console.


The following table lists the Prisma Console releases and their corresponding Intelligence Stream (IS) versions. For Prisma Cloud release 33.00 and later, IS versions are automatically aligned with the Prisma Cloud release. For Prisma Cloud releases 32.xx and 31.xx, the applicable IS versions are listed in the following table.

Prisma Console Release

Self-hosted Console Version / Intelligence Stream Version

33.02

33.02

33.01

33.01

33.00

33.00

32.xx

33.00

31.xx

33.00

**Note**: Updates related to the Intelligence Stream will be notified in the **Intelligence Stream Updates** section of the Prisma Cloud Release Notes.

[PreviousTechnology overviews](https://docs.prismacloud.io/admin-guide/technology-overviews/technology-overviews) [NextPrisma Cloud Advanced Threat Protection](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-advanced-threat-protection)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
