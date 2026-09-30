> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-december-2023.md).

# Features Introduced in December 2023

Learn about the new Compute capabilities on Prisma™ Cloud Enterprise Edition (SaaS) in December 2023.

The host, container, and serverless capabilities on the **Compute** tab are being upgraded starting on December 03, 2023. When upgraded, the version will be 32.00.

## 32.00

* [Defender Upgrade](#defender-upgrade)
* [Deprecation Notice](#deprecation-notice)
* [End of Support Notifications](#end-of-support)
* See also [Known Issues](/release-notes/prisma-cloud-known-issues/known-fixed-issues.md)

## Defender Upgrade

| Plan to Upgrade Defender Versions 22.12 and Earlier | With the `v32.00` (O’Neal) release, Defender versions supported (n, n-1, and n-2) are `v32.00`, `v31.00`, and `v30.00`. To prepare for this update, you must upgrade your Defenders from version `v22.12` (Lagrange) or earlier to a later version. Failure to upgrade Defenders will result in disconnection of any Defender version below `v30.00`, such as `v22.12`. |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## New Features in Prisma Cloud Compute

| **Added the agentless scanning report.** | The agentless scanning report is now available under **Runtime Security > Cloud Accounts**. This report provides you with complete visibility of all hosts in your cloud account at the account and regional level. It includes clear reporting of each host, the corresponding scan status, and further details. |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## Enhancements

| **Agentless malware scanning now includes all supported binaries.** | Agentless malware scanning detects all supported binaries and shared libraries on both Linux and Windows operating systems. For example, malicious ELF files on Windows machines are now detected. |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## Deprecation Notices

| Deprecate the `aggregated` and `rest` fields                             | The `aggregated` and `rest` macros from the webhook custom JSON alerts are being deprecated and replaced by `AggregatedAlerts` and `Dropped` macros respectively. |
| ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deprecate `AccountID` macro from the Alerts payload to be verified by PM | The `AccountID` macro in the Alerts payload is deprecated and replaced by the `AccountIDs` macro.                                                                 |

## End of Support Notifications

| Support for Cloud Native Network Segmentation (CNNS) | The ability to create CNNS policies that Defenders use to limit traffic from containers and hosts is being removed. The configuration settings on the console (**Runtime Security > Defend > CNNS**) and the corresponding APIs for CNNS will be removed in `v32.00`. Radar has a container and a host view, where you can view the network topology for your containerized apps and hosts respectively, and this will continue to be available. |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-december-2023.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
