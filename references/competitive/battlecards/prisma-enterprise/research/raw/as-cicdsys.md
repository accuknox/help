> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-systems.md).

# CI/CD Systems

Integrate Prisma Cloud with your CI/CD systems in order to gain visibility into, and monitor the system technologies, configurations and pipelines that could compromise your systems. Additionally, this integration allows you to conduct security scans to detect issues like CI/CD pipeline risks, vulnerabilities, and exposed secrets in your Jenkins and CircleCI environments.

| **What do you want to do?**                                                                    | **Start here**                                   |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| Understand which VCS systems provide out-of-the-box support for CI/CD scanning when integrated | [Out-of-the-Box CI/CD Scan Support](#out-of-box) |
| Integrate systems that do not support CI/CD scanning by default                                | [CI/CD System Integration](#cicd-integration)    |

## Out-of-the-Box CI/CD Scan Support

The following table provides an inventory of the systems that currently support out-of-the-box CI/CD scanning when integrated with Prisma Cloud.

| **System**                   | **Type** | **SaaS** | **On-Prem** |
| ---------------------------- | -------- | -------- | ----------- |
| Azure Repos                  | VCS      | Yes      | No          |
| Azure Pipelines              | CI/CD    | Yes      | No          |
| Bitbucket                    | VCS      | Yes      | No          |
| Bitbucket Data Center/Server | VCS      | Yes      | No          |
| CircleCI                     | CI/CD    | Yes      | No          |
| GitHub                       | VCS      | Yes      | Yes         |
| GitHub Actions               | CI/CD    | Yes      | No          |
| GitLab                       | VCS      | Yes      | Yes         |
| GitLab CI                    | CI/CD    | Yes      | Yes         |
| Jenkins                      | CI/CD    | N/A      | Yes         |

## CI/CD System Integration

The following systems must be integrated in order to support CI/CD system scanning:

* [Jenkins Plugins](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-systems/add-jenkins-cicd-system.md)
* [CircleCI](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-systems/add-circleci-cicd-system.md)

## Verify CI/CD System Integration

To verify integration, in **Application Security**, select **Home** > **Settings** > **CICD Systems** tab. Check that the status of the integrated system displays **Active**.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-0924fd12fcde471370f8de7e915fd5040028f55f%2Fcicd-system-verify3.0.png?alt=media" alt="cicd system verify3.0"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-systems.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
