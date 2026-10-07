For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/welcome/security-assurance-policy.md).

Prisma Cloud adheres to the guidelines outlined in the [Palo Alto Networks Product Security Assurance Policy](https://www.paloaltonetworks.com/product-security-assurance).

As per this policy, Prisma Cloud Compute may have security releases outside of the regular release schedule.

Security releases are used for the sole purpose of remediating vulnerabilities that affect Prisma Cloud Compute, whether in its codebase or its dependencies.

We frequently analyze new vulnerabilities between releases to determine if any issue warrants a security release before the next scheduled release. This section outlines which issues are addressed in security releases.

With each new release of Prisma Cloud Compute, software dependencies are kept up-to-date to eliminate any known and confirmed vulnerabilities in third-party dependencies.

When new vulnerabilities are discovered in Prisma Cloud Compute dependencies after an official release, these vulnerabilities are addressed in the newer releases with the exceptions noted below.

Therefore, as a best practice, always upgrade to the latest release of Prisma Cloud Compute.

## Vulnerability Triage[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/security-assurance-policy\#vulnerability-triage)

New releases of Prisma Cloud Compute are signed off with up-to-date dependencies. Vulnerabilities that meet the below criteria are analyzed between releases:

### Vulnerabilities Analyzed[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/security-assurance-policy\#vulnerabilities-analyzed)

- Any vulnerability with severity high and above, regardless of having a fix or not.

- Any vulnerability with moderate severity when a fix is available.


### Vulnerabilities Not Analyzed[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/security-assurance-policy\#vulnerabilities-not-analyzed)

- Any vulnerability with a severity lower than high that does not have an existing fix.

- Any vulnerability with severity low; this includes vulnerabilities that the vendor will not fix as they are considered as having negligible impact.


### Exceptions[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/security-assurance-policy\#exceptions)

We also review vulnerabilities of any other severity when there is a known exploit or proof-of-concept that affects Prisma Cloud Compute. Including product vulnerabilities identified during development, and reported by customers or third-party researchers. To report a vulnerability in Prisma Cloud Compute, submit the vulnerability details to our [PSIRT](https://www.paloaltonetworks.com/product-security-assurance) team.

### Frequently Asked Questions[Direct link to heading](https://docs.prismacloud.io/admin-guide/welcome/security-assurance-policy\#frequently-asked-questions)

- Which Prisma Cloud Compute releases receive security updates?


Prisma Cloud has an 'n-2' support policy which means the current release ('n') and the previous two releases ('n-1' and 'n-2') receive support. Security fixes will be backported only for supported releases. End of Life (EOL) releases will not receive security fixes. For more information, see [support lifecycle](https://docs.prismacloud.io/admin-guide/welcome/support-lifecycle).

**Are security fixes provided for both Prisma Cloud Enterprise and Compute editions?**

Yes, security vulnerabilities are addressed in both editions.

**Do I have to upgrade my console/defender to get security updates?**

If security fixes are released, you may be required to upgrade either or both the Console and Defender. We recommend that all security releases are adopted immediately.

For the full details of which vulnerabilities were fixed in a release, refer to the [release notes](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/rn/release-information/release-information.md).

**What is the minimum severity for vulnerabilities to warrant a security release?**

See the triage criteria above.

**What is the frequency of security releases for Prisma Cloud Compute?**

There is no schedule for security releases. Security releases happens anytime a new vulnerability that meets the criteria outlined above is discovered in Prisma Cloud Compute.

**Where do you take information on severity and fix details when triaging?**

Console and Defender images are based on Red Hat Universal Base Images (ubi8/ubi-minimal). For known vulnerabilities that are assigned a [CVE identifier](https://www.cve.org/About/Overview), we rely on severity ratings and fixes released by Red Hat. For zero-days or undocumented vulnerabilities (such as PRISMA-IDs), we rely on severity determined by our researchers.

**A new vulnerability is affecting Prisma Cloud Compute, but a security release was not issued.** If the vulnerability affects the latest release, meets the criteria for a security release outlined above, but has not yet been addressed, report it to [Palo Alto Networks Support](https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClNSCA0) or to [PSIRT](https://www.paloaltonetworks.com/product-security-assurance).

[PreviousSupport lifecycle](https://docs.prismacloud.io/admin-guide/welcome/support-lifecycle) [NextLicensing](https://docs.prismacloud.io/admin-guide/welcome/licensing)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
