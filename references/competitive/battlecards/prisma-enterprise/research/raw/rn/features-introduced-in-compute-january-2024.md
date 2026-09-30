> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-january-2024.md).

# Features Introduced in January 2024

Learn about the new Compute capabilities on Prisma™ Cloud Enterprise Edition (SaaS) in January 2024.

The host, container, and serverless capabilities on the **Compute** tab are being upgraded starting on January 07, 2024. When upgraded, the version will be 32.01.

* [Defender Upgrade](#defender-upgrade)
* [New Features in Prisma Cloud Compute](#new-features-prisma-cloud-compute)
* [API Changes](#api-changes)
* [Deprecation Notice](#deprecation-notice)
* See also [Known Issues](/release-notes/prisma-cloud-known-issues/known-fixed-issues.md)

## Defender Upgrade

| Plan to Upgrade Defender Versions 22.12 and Earlier | With the `v32.00` (O’Neal) release, Defender versions supported (n, n-1, and n-2) are `v32.00`, `v31.00`, and `v30.00`. To prepare for this update, you must upgrade your Defenders from version `v22.12` (Lagrange) or earlier to a later version. Failure to upgrade Defenders will result in disconnection of any Defender version below `v30.00`, such as `v22.12`. |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## New Features in Prisma Cloud Compute

| FEATURE                      | DESCRIPTION                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Agentless Scanning**       | Added agentless scanning support of encrypted volumes in Azure for the hub account mode.                                                                                       |
| **Agentless Scanning**       | Added agentless scanning hub account mode for Azure.                                                                                                                           |
| **Vulnerability Management** | Added support for Debian Bullseye and Bookworm Security fixes.                                                                                                                 |
| **Operating System Support** | Added support for OpenShift 4.14.                                                                                                                                              |
| **Vulnerability Management** | Added support to detect IBM Java version 1.8 and earlier. IBM Java version 1.9 and later are partially supported. The detection depends on the `jdk/release` file being found. |

## API Changes

| **API Changes** | The [Add a New Collection](https://pan.dev/prisma-cloud/api/cwpp/post-collections/)endpoint is updated to fix resolve an issue that caused collections that were added by invoking this endpoint with one or more empty fields: such collections did not display in the Console. Now, all request body fields of this endpoint, except `name`, are optional. Any optional field that is not provided will default to the wildcard value '\*'. |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## Deprecation Notices

| **Runtime Security Alerts** | <p>Deprecated the <code>AccountID</code> and <code>Cluster</code> macros used in alerts. This removes the <code>AccountID</code> and <code>Cluster</code> fields in the following alerts using the macros.</p><ul><li>Webhook</li><li>AWS SQS</li><li>Prisma Cortex Alert</li><li>Splunk</li></ul> |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-january-2024.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
