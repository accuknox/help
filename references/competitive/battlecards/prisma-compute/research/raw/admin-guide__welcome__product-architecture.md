For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/welcome/product-architecture.md).

Prisma Cloud offers a rich set of cloud workload protection capabilities. Collectively, these features are called _Compute_. Compute has a dedicated management interface, called _Compute Console_, that can be accessed in one of two ways, depending on the product you have.

- **Prisma Cloud Enterprise Edition** — Hosted by Palo Alto Networks. Prisma Cloud Enterprise Edition is a SaaS offering. It includes both the Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP) modules. Access the Compute Console, which contains the CWPP module, from the **Compute** tab in the Prisma Cloud UI.

- **Prisma Cloud Compute Edition** \- Hosted by you in your environment. Prisma Cloud Compute Edition is a self-hosted offering that’s deployed and managed by you. It includes the Cloud Workload Protection Platform (CWPP) module only. Download the Prisma Cloud Compute Edition software from the Palo Alto Networks Customer Support Portal. Compute Console is delivered as a container image, so you can run it on any host with a container runtime (e.g. Docker Engine).


The following table summarizes the differences between the two offerings:

Capabilities

Prisma Cloud Enterprise Edition

Prisma Cloud Compute Edition

**Management interface**

Hosted by Palo Alto Networks (SaaS).

Deployed and managed by you in your environment (self-hosted).

**Modules**

CSPM and CWPP.

CWPP only.

**Security agents**

Deployed and managed by you.

Deployed and managed by you.

**User management**

Configure single sign-on in Prisma Cloud.

Configure single sign-on in Prisma Cloud Compute Edition. Compute Console exposes additional views for Active Directory and SAML integration when it’s run in self-hosted mode.

**Multi-tenancy**

Supported by Palo Alto Networks [Hub](https://apps.paloaltonetworks.com/).

Supported by a feature called Projects. Projects are enabled in Compute Edition only. It’s disabled in Enterprise Edition.

## Accessing Compute in Prisma Cloud Enterprise Edition[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/product-architecture\#accessing-compute-in-prisma-cloud-enterprise-edition)

In Prisma Cloud, click the **Compute** tab to access Compute.

You must have the Prisma Cloud System Admin role. Access is denied to users with any other role.

The following screenshot shows the Prisma Cloud administrative console. The format of the URL is:

AskCopy

```
https://app<opt-num>.<opt-region>.prismacloud.io
```

![prisma cloud arch1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-1d61f9d3e89d34177874415fc8789d42f542ecb6%252Fprisma_cloud_arch1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=96b99f59c2d5c532bfde7f36332e140d&sv=3)

The following screenshot shows the Compute tab on Prisma Cloud. To access the Compute tab, you must log in to the Prisma Cloud administrative console; it cannot be directly addressed in the browser. image::prisma\_cloud\_arch2.png\[width=800\]

You can find the address of Compute Console in Prisma Cloud under **Compute > Manage > System > Utilities**. The address for Compute Console has the following format:

AskCopy

```
https://<region>.cloud.twistlock.com/<customer>
```

The following Compute components directly connect to the Compute console address provided above:

- Defender, for Defender to Compute Console connectivity.

- twistcli

- Jenkins plugin

- Compute API


## Accessing Compute in Prisma Cloud Compute Edition[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/product-architecture\#accessing-compute-in-prisma-cloud-compute-edition)

In Compute Edition, Palo Alto Networks gives you the management interface to run in your environment. In this setup, you deploy Compute Console directly. There’s no outer or inner interface; there’s just a single interface, and it’s Compute Console. Compute Console’s address, whether an IP address or DNS name, is used for all interactions, namely:

- GUI access from a web browser.

- Defender to Compute Console connectivity.

- twistcli

- Jenkins plugin

- Compute API


[PreviousGetting started](https://docs.prismacloud.io/admin-guide/welcome/getting-started) [NextSupport lifecycle](https://docs.prismacloud.io/admin-guide/welcome/support-lifecycle)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
