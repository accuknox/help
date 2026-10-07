For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-advanced-threat-protection.md).

Prisma Cloud Advanced Threat Protection (ATP) is a collection of malware signatures and IP reputation lists aggregated from commercial threat feeds, open source threat feeds, and Prisma Cloud Labs. It is delivered to your installation via the Prisma Cloud Intelligence Stream.

The data in ATP is used by Prisma Cloud’s runtime defense system to detect suspicious activities, such as a container communicating with a botnet herder or Tor entry node. You can augment ATP by [importing custom malware data](https://docs.prismacloud.io/admin-guide/configure/custom-feeds#import-malware-signatures) and [importing IP reputation lists](https://docs.prismacloud.io/admin-guide/configure/custom-feeds#import-ip-reputation-lists). ATP is the combination of both the Prisma Cloud-provided data set and your own custom data set.

The following hypothetical scenario illustrates how ATP protects your cloud workloads:

1. An attacker exploits a vulnerability in an app running in a container.

2. The attacker attempts to download malware into a workload from a distribution point.

3. Based on the ATP feed, Prisma Cloud runtime defense detects both the connection to the malware server and the write of the malicious file to the workload file system.

4. Alerts/prevention is applied based on the runtime configuration.


## Enabling ATP[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-advanced-threat-protection\#enabling-atp)

ATP is enabled in the default rules that ship with the product, with the effect set to alert. You can impose more stringent control by setting effect to prevent or block. [Runtime defense for file systems](https://docs.prismacloud.io/admin-guide/runtime-defense/runtime-defense-containers) lets you actively stop (block) any container that tries to download malware. To disable ATP, create or modify a runtime rule, select the **General** tab, and set **Enable Prisma Cloud Advanced Threat Protection** to **Off**. When ATP is disabled, container interaction with malicious files or IP endpoints does not trigger a runtime event.

## Serverless ATP[Direct link to heading](https://docs.prismacloud.io/admin-guide/technology-overviews/twistlock-advanced-threat-protection\#serverless-atp)

In Serverless, Prisma Cloud Advanced Threat Protection (ATP) has a slightly different functionality. It’s a collection of paths (researched by Prisma Cloud Labs) that define which file system and process activity is allowed within the function. Activities that do not match these paths will raise a security audit. When enabled, it creates an automatic hardening for the function in runtime, without the need to manually configure the runtime policy.

Serverless ATP is enabled by default when creating a new runtime rule. It’s effect is similar to the effects configured under the Processes/File System tabs. To disable ATP, create or modify a runtime rule, select the **General** tab, and set **Prisma Cloud advanced threat protection** to **Off**.

[PreviousIntelligence Stream](https://docs.prismacloud.io/admin-guide/technology-overviews/intel-stream) [NextApp-specific network intelligence](https://docs.prismacloud.io/admin-guide/technology-overviews/app-specific-network-intelligence)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
