> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-october-2023.md).

# Features Introduced in October 2023

Learn about the new Compute capabilities on Prisma® Cloud Enterprise Edition (SaaS) in October 2023.

There are two releases in October 2023.

* `v31.02.137` on October 22, 2023 is a maintenance release with a security fix.
* `v31.02.133` on October 8, 2023, is a maintenance release with enhancement and other fixes

## 31.02.137

This release is a maintenance release with a security fix.

| HTTP/2 Rapid Reset Attack Vulnerability (CVE-2023-44487) | <p>This security update addresses the HTTP/2 Rapid Reset Attack Vulnerability (CVE-2023-44487).</p><ol><li>Go updated from 1.20.8 to 1.20.10 (<a href="https://go.dev/doc/devel/release#go1.20.10"><https://go.dev/doc/devel/release#go1.20.10></a>).</li><li>Go package "golang.org/x/net" was updated to version 0.17.0 (<a href="https://github.com/advisories/GHSA-4374-p667-p6c8"><https://github.com/advisories/GHSA-4374-p667-p6c8></a>).</li><li>The "nghttp2" package (installed in the Defender/Console images) updated by Red Hat (<a href="https://access.redhat.com/errata/RHSA-2023:5837"><https://access.redhat.com/errata/RHSA-2023:5837></a>).</li></ol><p><strong>Action</strong> - You do not need to make any updates to Compute console or the deployed Defenders.</p> |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## 31.02.133

* [New Features in Prisma Cloud Compute](#new-features-prisma-cloud-compute)
* [Enhancements](#enhancements)
* [API Changes](#api-changes)
* [End of Support Notifications](#end-of-support)
* See also [Known Issues](/release-notes/prisma-cloud-known-issues/known-fixed-issues.md)

## Enhancements

| **Support for Scanning Images based on Wolfi Linux**           | Prisma cloud now supports scanning Wolfi based and Chainguard images for vulnerabilities. The Intelligence Stream includes Chainguard and Wolfi feeds for CVE information.                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agentless - Secrets Scanning**                               | <p>Agentless scanning now supports <a href="https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/compliance/detect_secrets">secret scanning</a> across all workloads. Agentless scanning checks secrets in images, the container file systems, and the host file systems for AWS, Azure, GCP, and OCI. The following types of secrets are scanned.</p><ul><li>Cloud keys</li><li>API tokens</li><li>Passwords</li><li>Configuration files</li><li>Private keys</li><li>Certificates</li></ul> |
| **Add Admission Control (rego) Rules**                         | Prisma Cloud now provides new 81 OOTB admission rules written in Rego language.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Agentless Compliance Cluster Scanning**                      | <p>Agentless scans now provide compliance check results for working nodes in the following cluster types.</p><ul><li>AKS</li><li>EKS</li><li>GKE</li></ul>                                                                                                                                                                                                                                                                                                                                                                |
| **Explore Custom Rules Checks in Compliance Explorer**         | You can now click on a custom rule check in Compliance explorer and explore the resources that violate a compliance rule. This helps you to find and fix compliance issues.                                                                                                                                                                                                                                                                                                                                               |
| **Added Discovered Date for Vulnerability Identified on Host** | Added discovered date that includes the first instance when a specific package/application/binary vulnerability was detected on a host. The discovered date is available on the Console (**Monitor > Vulnerabilities > Hosts > Host details > Vulnerabilities**) and in the host vulnerabilities CSV report.                                                                                                                                                                                                              |

## End of Support Notifications

| **Ubuntu 18.04 LTS EOL** | Ubuntu 18.04 reached End of Standard Support May 31, 2023. If you still have devices in your fleet using Ubuntu 18, follow [Canonical’s guidance to keep your devices up and running](https://ubuntu.com/blog/ubuntu-18-04-eol-for-devices). Starting with Newton Update 2, Prisma Cloud Compute is no longer tested on devices running Ubuntu 18 and no support for those devices is available. |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-october-2023.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
