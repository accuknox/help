For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce.md).

This article describes the key differences between Compute in Prisma Cloud Enterprise Edition and Prisma Cloud Compute Edition. Use this guide to determine which option is right for you.

![pcee vs pcce overview](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-854bd8934044fbacd1aad37759834797ed23a2fe%252Fpcee_vs_pcce_overview.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d3807f5577096b872b9bbcfa9c85040b&sv=3)

## How is Compute delivered?[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce\#how-is-compute-delivered)

Compute is delivered in one of two packages:

- **Prisma Cloud Enterprise Edition (SaaS)** — Single pane of glass for both CSPM (Cloud Security Posture Management) & CWPP (Cloud Workload Protection Platform). Compute (formerly Twistlock, a CWPP solution) is delivered as part of the larger Prisma Cloud system. Palo Alto Networks runs, manages, and updates Compute Console for you. You deploy and manage Defenders in your environment. You access the Compute Console from a tab within the Prisma Cloud user interface.

- **Prisma Cloud Compute Edition (self-hosted)** — Stand-alone, self-operated version of Compute. Download the entire software suite, and run it in any environment. You deploy and manage both Console and Defenders.


## When should you use Enterprise Edition?[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce\#when-should-you-use-enterprise-edition)

Prisma Cloud Enterprise Edition is a good choice when:

- You want a single platform that protects both the service plane (public cloud resource configuration) and the compute plane.

- You want convenience. We manage your Console for you. We update it for you. You get the Prisma Cloud uptime SLA.


## When should you use Compute Edition?[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce\#when-should-you-use-compute-edition)

Prisma Cloud Compute Edition is a good choice when:

- You want full control over your data.

- You’re operating in an air-gapped environment.

- You want to implement enterprise-grade multi-tenancy with one Console per tenant. For multi-tenancy, Compute Edition offers a feature called Projects.


## What are the differences between Prisma Cloud Enterprise Edition and Compute Edition?[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce\#what-are-the-differences-between-prisma-cloud-enterprise-edition-and-compute-edition)

The following table summarizes the key differences between Enterprise Edition (SaaS) and Compute Edition (self-hosted). Consider these differences when deciding which edition is right for you.

Capability

Compute SaaS support

Projects

If you need Projects, use Compute Edition. Projects will not be ported to Prisma Cloud Enterprise Edition. However, PCEE does offer alternatives that support Project’s primary use cases. The use case for projects is isolation, where each team has a dedicated Console so that other teams can’t see each other’s data. PCEE supports isolation with multiple independent Prisma Cloud tenants, one per team, with one Compute Console per tenant. Within a single PCEE tenant, Compute Console also offers isolation to data access based on cloud account filtering.

Syslog

Supported for Defenders only. For more details, see the article on [logging](https://docs.prismacloud.io/admin-guide/audit/logging)

User management

Available centrally in the platform for Prisma Cloud Enterprise Edition.

Assigned collections

Available via Resource Lists. Read more about [assigning roles](https://docs.prismacloud.io/admin-guide/authentication/assign-roles).

Defender backward compatibility

Yes

Compute Edition to Enterprise Edition migration

Available - Must go through Customer Success team.

## How do Defender upgrades work?[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce\#how-do-defender-upgrades-work)

Upgrades work a little differently in each edition.

- **Prisma Cloud Enterprise Edition** — Console is automatically upgraded by PANW with notification posted in our status page at least 2 weeks in advance of upgrade. For more details, refer to [this article](https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/upgrade/upgrade_process_saas). Auto-upgrade function for Defenders is always turned ON ensuring that Defenders stay compatible with Console in each release.

- **Prisma Cloud Compute Edition (self-hosted)** — You fully control the upgrade process. When an upgrade is available, customers are notified via the bell icon in Console. Clicking on it directs you to the latest software download. Deploy the new version of Console first, then manually upgrade all of your deployed Defenders.


## Can you migrate from Compute Edition to Enterprise Edition (SaaS)?[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/pcee-vs-pcce\#can-you-migrate-from-compute-edition-to-enterprise-edition-saas)

Yes.

[PreviousLicensing](https://docs.prismacloud.io/admin-guide/welcome/licensing) [NextUtilities and plugins](https://docs.prismacloud.io/admin-guide/welcome/utilities-and-plugins)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
