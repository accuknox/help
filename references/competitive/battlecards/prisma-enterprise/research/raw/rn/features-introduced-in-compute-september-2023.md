> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-september-2023.md).

# Features Introduced in September 2023

Learn about the new Compute capabilities on Prisma® Cloud Enterprise Edition (SaaS) in September 2023.

The host, container, and serverless capabilities on the **Compute** tab are being upgraded starting on September 10, 2023. When upgraded, the version will be 31.01.123.

* [New Features in Prisma Cloud Compute](#new-features-prisma-cloud-compute)
* [API Changes](#api-changes)
* [End of Support Notifications](#end-of-support)
* See also [Known Issues](/release-notes/prisma-cloud-known-issues/known-fixed-issues.md)

## New Features in Prisma Cloud Compute

| **Severity Based Actions for Packages in Vulnerability Rules** | <p><a href="https://docs.paloaltonetworks.com/prisma/prisma-cloud/prisma-cloud-admin-compute/vulnerability_management/vuln_management_rules">Vulnerability policy rules</a> can now be scoped based on the severity threshold per package, in addition to scoping the vulnerabilities by collections. You can now define the severity threshold per package type for alert and block actions.</p><p><img src="https://1815359018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0B0G9j3lh441nNaDZxLT%2Fuploads%2Fgit-blob-4e3b085ddd968c6977bcc939756370c0fab2964e%2Fvuln-rule-per-package-severity.png?alt=media" alt="" data-size="original"></p><p>The package type severity thresholds apply to all workload types: deployed images, CI Images, hosts, VM images, functions, and CI Functions. With this feature, you can monitor alerts at a granular level and focus on vulnerabilities in specific packages.</p> |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Parallel Registry Scanning**                                 | <p>You can now trigger a registry scan when configuring the registry under <strong>Defend > Vulnerabilities > Registry</strong>. As you add more registries, the new scans are queued until the previous scan finishes.</p><p><img src="https://1815359018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0B0G9j3lh441nNaDZxLT%2Fuploads%2Fgit-blob-33b91adc229d7568d8ae4dad76fb3c6e993c7d97%2Fnew-registry-add-and-scan.png?alt=media" alt="" data-size="original"></p><p>With this update, you can initiate a new scan from <strong>Monitor > Vulnerabilities</strong> while previous scans are in progress.</p>                                                                                                                                                                                                                                                                                                      |

## End of Support Notifications

| **End of Support for Docker Access Control** | Docker Access Control (**Defend > Access > Docker**) and the Access User role (**Manage > Authentication > Roles**) are no longer supported. |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |

## API Changes

| **End of Support for Docker Access Control** | <p>The following API will no longer include the docker information in the response:</p><ul><li>/api/v\_version/audits/access (uses the HTTP GET method)</li></ul> |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-compute-release-information/features-introduced-in-compute-september-2023.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
