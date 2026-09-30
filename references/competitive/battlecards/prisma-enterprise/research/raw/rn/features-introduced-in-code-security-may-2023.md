> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-code-security-release-information/features-introduced-in-code-security-may-2023.md).

# Features Introduced in May 2023

Learn about the new Code Security capabilities on Prisma® Cloud Enterprise Edition (SaaS) in May 2023.

The following new features or enhancements are available for Prisma Cloud Code Security. These capabilities help agile teams add security checks to their development process and enforce security throughout the build lifecycle.

* [New Features](#new-features)
* [Changes in Existing Behavior](#changes-in-existing-behavior)

## New Features

| FEATURE                                                  | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Code Security Dashboard**                              | <p>Code Security dashboard (<strong>Dashboard > Code Security</strong>) enables you to analyze error trends across code integrations on Prisma Cloud. While emphasizing the critical and high severity code issues, the dashboard also gives you an understanding of the potentially vulnerable vectors in repositories, policy errors including secrets, non-compliant package licenses, vulnerabilities and IaC misconfigurations. See the historical trend for Code Issues and Pull Requests to make informed decisions to prevent the recurrence of the trend. The vectors for repositories, policy errors, non-compliant package licenses, CVEs and IaC misconfigurations ensure you see the latest real time data after scans. The error counts direct you to <strong>Code Security > Projects</strong> where you get more context and can take remediation action for the errors, as necessary.</p><p><img src="https://1815359018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0B0G9j3lh441nNaDZxLT%2Fuploads%2Fgit-blob-b2cdaf89ae200f8ddb7f3f8a99954802431cffde%2Fcodesec-rn-23.5.2.png?alt=media" alt="" data-size="original"></p> |
| **Additional `Read` permissions for GitHub integration** | <p>The GitHub app is being updated to improve security coverage and visibility of your Git and CI/CD security posture. If you have set up the GitHub integration on Prisma Cloud Code Security, you will be prompted to grant additional Read permissions to the application on GitHub.</p><p>Approving these permissions will enable you to use the enhanced capabilities that security teams can use to monitor and optimize their Git and CI/CD Security posture across the organization, when it becomes available.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## Changes in Existing Behavior

| FEATURE                                                  | DESCRIPTION                                                                                                                                                                                                                                                          |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Support for Multiple IaC Frameworks on Visual Editor** | Visual Editor is being enhanced to support multiple IaC frameworks when creating custom build policies. This support enables you to differentiate between Terraform and CloudFormation framework policies and is creating support for Kubernetes framework policies. |
| **Projects View**                                        | The **Projects** non-enhanced view is being replaced with the enhanced view where you can continue monitoring your code errors and vulnerabilities.                                                                                                                  |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-code-security-release-information/features-introduced-in-code-security-may-2023.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
