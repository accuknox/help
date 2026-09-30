# Prisma Cloud Enterprise Edition Is Still Documented and Shipping as of September 2026

Checked on 2026-09-30.

## Palo Alto Networks Still Ships Monthly Enterprise Edition Releases

The Enterprise Edition release notes run to August 2026. The August page says "This release includes updates for Prisma Cloud Enterprise Edition version 26.8.1 and Runtime updates for version 34.05."
Source: https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/features-introduced-in-2026/features-introduced-in-august-2026

The look-ahead page plans changes for release 26.10.1, for example the deprecation of the alerts/job endpoint.
Source: https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/look-ahead-secure-the-infrastructure

The docs moved to GitBook. The Enterprise Edition pages now sit under `https://docs.prismacloud.io/content-collections/`. The Compute Edition pages sit under `https://docs.prismacloud.io/admin-guide/`. The old `/en/enterprise-edition/` paths are the previous layout.

## Enterprise Edition Is SaaS Only

The docs say "Prisma Cloud is available in two deployment models - SaaS (Prisma Cloud Enterprise Edition) and Self Hosted (Prisma Cloud Compute Edition)."
Source: https://docs.prismacloud.io/content-collections/get-started/welcome-to-prisma-cloud

For Enterprise Edition, "Palo Alto Networks runs, manages, and updates Compute Console for you." The same page recommends Compute Edition when "You’re operating in an air-gapped environment."
Source: https://docs.prismacloud.io/content-collections/runtime-security/pcee-vs-pcce

## Cortex Cloud Is the Successor Brand, but No End of Sale Was Found

In February 2025, Palo Alto Networks launched Cortex Cloud. The press release says "Existing Prisma Cloud customers will experience a seamless upgrade to Cortex Cloud." It also says "Cortex Cloud will be available to customers later in Q3 FY25."
Source: https://www.paloaltonetworks.com/company/press/2025/palo-alto-networks-introduces-cortex-cloud--the-future-of-real-time-cloud-security

The Prisma Cloud product page still exists at https://www.paloaltonetworks.com/prisma/cloud with the title "Prisma Cloud | Comprehensive Cloud Security". Its hero banner promotes Cortex Cloud with a "MEET CORTEX CLOUD" call to action.

The official end-of-life page lists no end-of-sale or end-of-life date for Prisma Cloud Enterprise Edition. Its only Prisma Cloud entry is Bridgecrew standalone, which reached end of life on 31 December 2023.
Source: https://www.paloaltonetworks.com/services/support/end-of-life-announcements

Some third-party sites (appsecsanta.com, distribuee.com) say that the migration of existing customers to Cortex Cloud is complete. Palo Alto Networks did not confirm this on any page I read, so do not cite it. A LIVEcommunity post titled "End of Sale for Prisma Cloud Data Security" exists at https://live.paloaltonetworks.com/t5/community-blogs/end-of-sale-for-prisma-cloud-data-security/ba-p/595382. That page returned HTTP 403, so its dates are unverified. The post probably covers the older Data Security module. I could not confirm whether it also affects the current DSPM module.

## The Battlecard Can Target Enterprise Edition With One Footnote

Enterprise Edition is documented, receives releases and has no published end-of-sale date. A buyer can still meet it in a deal. Palo Alto Networks sells Cortex Cloud as the upgrade path, so the battlecard needs a footnote. The footnote says that Enterprise Edition customers may move to Cortex Cloud and that Cortex Cloud facts differ. One example is native SAST, which is marketed for Cortex Cloud and not documented for Enterprise Edition.

## FedRAMP High Authorization Was Announced in December 2024

The Palo Alto Networks blog calls Prisma Cloud "the world's only cloud-native application protection platform (CNAPP) to achieve FedRAMP High Authorization". The blog is dated 19 December 2024 and does not list which modules the authorization covers. The government tenant is `app.gov.prismacloud.io` in AWS GovCloud US-West, per the console prerequisites page.
Sources: https://www.paloaltonetworks.com/blog/cloud-security/prisma-cloud-achieves-fedramp-high-authorization/ and https://docs.prismacloud.io/content-collections/get-started/console-prerequisites
