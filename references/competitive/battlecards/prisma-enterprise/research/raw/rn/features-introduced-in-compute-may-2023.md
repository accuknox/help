> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-may-2023.md).

# Features Introduced in May 2023

Learn about the new Compute capabilities on Prisma® Cloud Enterprise Edition (SaaS) in May 2023.

The host, container, and serverless capabilities on the **Compute** tab are being upgraded starting on May 23, 2023. When upgraded, the version will be 30.01.152.

* [New Features in Prisma Cloud Compute](#new-features-prisma-cloud-compute)
* [API Changes](#api-changes)
* [End of Support Notifications](#end-of-support)
* See also [Known Issues](/release-notes/prisma-cloud-known-issues/known-fixed-issues.md)

## New Features in Prisma Cloud Compute

| Feature                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enhancements**                                                     |                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Support for New Operating Systems**                                | <ul><li>Support for TAS 4.0</li><li>Support for Amazon Linux 2023</li><li>Extended support for TalOS with Runtime defense for containers; available on Container Orchestrator Defenders.</li></ul>                                                                                                                                                                                                        |
| **New Features in Agentless Security**                               |                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Support for Third-Party Packages on Windows**                      | This feature adds support for scanning vulnerabilities on third-party packages on Windows machines: Node-Node.js, Python, Ruby-Gems, Java-JAR, and NuGet.                                                                                                                                                                                                                                                 |
| **Selective Scanning of Hosts with Include Tags** CWP-46156          | The new **Include hosts by tag** option allows you to select a subset of your hosts for scanning based on their tags. The tags interface is enhanced to help you view and manage your tags more easily. Additionally, you can now use wildcards to exclude or include hosts that match a certain tag pattern. For example, you can use `web-*` to include all hosts that have a tag starting with `web-`. |
| **Agentless scanning in AWS: Specify a subnet and use a private IP** | You can now specify a subnet name and use a private IP from that subnet to report the agentless scanning results back to Prisma Cloud.                                                                                                                                                                                                                                                                    |
| **New Features in Host Security**                                    |                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Discovery Date for Host Vulnerability Scan Results** CWP-47858     | <p>Add Discovery date for the vulnerabilities discovered on the host.</p><p><img src="https://1815359018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0B0G9j3lh441nNaDZxLT%2Fuploads%2Fgit-blob-e31b1a52bf85fd54ffcf8dde2c468a86261e67a2%2Fhost-vulnerabilites-scan-result.png?alt=media" alt="" data-size="original"></p>                                                         |

## API Changes

| CHANGE                          | <p>DESCRIPTION</p><p>CWP-40109</p>                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **API URLs versioned as 30.01** | Following the versioning number format for 30.xx, all the supported API endpoints will be versioned as 30.01 in this release. If you are using the 30.00 endpoints in your automation workflows and scripts, they will continue to be supported.                                                                                                                                                                   |
| **Feeds**                       | <p>Supports the following APIs:</p><ul><li>feeds/custom/custom-vulnerabilities, GET</li><li>feeds/custom/custom-vulnerabilities, PUT</li><li>feeds/custom/malware, PUT</li></ul>                                                                                                                                                                                                                                   |
| **Settings**                    | <p>Supports the following APIs:</p><ul><li>settings/certs, GET</li><li>settings/custom-labels, POST</li><li>settings/intelligence, GET</li><li>settings/license, GET</li><li>settings/logging, GET</li><li>settings/logging, POST</li><li>settings/logon, GET</li><li>settings/proxy, GET</li><li>settings/proxy, POST</li><li>settings/saml, GET</li><li>settings/scan, GET</li><li>settings/scan, POST</li></ul> |
| **TAS Droplets**                | <p>Supports the following APIs:</p><ul><li>tas-droplets, GET</li><li>tas-droplets/download, GET</li><li>tas-droplets/progress, GET</li><li>tas-droplets/scan, POST</li><li>tas-droplets/stop, POST</li></ul>                                                                                                                                                                                                       |
| **Trust Data**                  | <p>Supports the following APIs:</p><ul><li>trust/data, GET</li><li>trust/data, PUT</li></ul>                                                                                                                                                                                                                                                                                                                       |

## End of Support Notifications

| Notices                                                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **TLS Cipher Support Update**                                | <p>Ends the support for the following TLS ciphers for WAAS:</p><ul><li>TLS\_RSA\_WITH\_AES\_128\_GCM\_SHA256</li><li>TLS\_RSA\_WITH\_AES\_256\_GCM\_SHA384</li><li>TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA</li><li>TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA</li></ul>                                                                                                                                                                                                                      |
| **AWS Announcement for Phase 1 Deprecation of.NET Core 3.1** | <p>AWS Lambda runtimes entered .NET Core 3.1 into phase 1 of deprecation on April 3 2023, and Prisma Cloud has updated the supported AWS Lambda runtimes in the <a href="https://docs.paloaltonetworks.com/prisma/prisma-cloud/30/prisma-cloud-compute-edition-admin/install/system_requirements">system requirements</a>.</p><p>See the <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">AWS Lamba runtimes documentation</a> for more details.</p> |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-may-2023.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
