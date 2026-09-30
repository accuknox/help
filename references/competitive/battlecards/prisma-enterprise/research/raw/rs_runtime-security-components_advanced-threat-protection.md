> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/runtime-security-components/advanced-threat-protection.md).

# Prisma Cloud Advanced Threat Protection

Prisma Cloud Advanced Threat Protection (ATP) is a collection of malware signatures and IP reputation lists aggregated from commercial threat feeds, open source threat feeds, and Prisma Cloud Labs. It is delivered to your installation via the Prisma Cloud Intelligence Stream.

The data in ATP is used by Prisma Cloud’s runtime defense system to detect suspicious activities, such as a container communicating with a botnet herder or Tor entry node. You can augment ATP by [importing custom malware data](/content-collections/runtime-security/configure/custom-feeds.md#import-malware-signatures) and [importing IP reputation lists](/content-collections/runtime-security/configure/custom-feeds.md#import-ip-reputation-lists). ATP is the combination of both the Prisma Cloud-provided data set and your own custom data set.

The following hypothetical scenario illustrates how ATP protects your cloud workloads:

1. An attacker exploits a vulnerability in an app running in a container.
2. The attacker attempts to download malware into a workload from a distribution point.
3. Based on the ATP feed, Prisma Cloud runtime defense detects both the connection to the malware server and the write of the malicious file to the workload file system.
4. Alerts/prevention is applied based on the runtime configuration.

## Enabling ATP

ATP is enabled in the default rules that ship with the product, with the effect set to alert. You can impose more stringent control by setting effect to prevent or block. [Runtime defense for file systems](/content-collections/runtime-security/runtime-defense/runtime-defense-containers.md) lets you actively stop (block) any container that tries to download malware. To disable ATP, create or modify a runtime rule, select the **General** tab, and set **Enable Prisma Cloud Advanced Threat Protection** to **Off**. When ATP is disabled, container interaction with malicious files or IP endpoints does not trigger a runtime event.

## Serverless ATP

In Serverless, Prisma Cloud Advanced Threat Protection (ATP) has a slightly different functionality. It’s a collection of paths (researched by Prisma Cloud Labs) that define which file system and process activity is allowed within the function. Activities that do not match these paths will raise a security audit. When enabled, it creates an automatic hardening for the function in runtime, without the need to manually configure the runtime policy.

Serverless ATP is enabled by default when creating a new runtime rule. It’s effect is similar to the effects configured under the Processes/File System tabs. To disable ATP, create or modify a runtime rule, select the **General** tab, and set **Prisma Cloud advanced threat protection** to **Off**.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/runtime-security-components/advanced-threat-protection.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
