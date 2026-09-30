> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs.md).

# CI/CD Runs

Integrate Prisma Cloud with your CI/CD runs in order to scan and detect misconfigurations in your infrastructure-as-code (IaC) files, vulnerabilities in your software composition analysis (SCA) packages, exposed secrets and license noncompliance in your code.

CI/CD Run integrations include:

* [Azure Pipelines](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-azure-pipelines.md)
* [AWS Code Build](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-aws-codebuild.md)
* [CircleCI](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-circleci.md)
* [Checkov](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-checkov.md)
* [GitHub Actions](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-github-actions.md)
* [GitLab Runner](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-gitlab-runner.md)
* [Jenkins](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-jenkins.md)
* [Terraform Cloud (Sentinel)](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-terraform-cloud-sentinel.md)
* [Terraform Cloud (Run Tasks)](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-terraform-run-tasks.md)
* [Terraform Enterprise (Sentinel)](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-terraform-enterprise.md)
* [Terraform Enterprise (Run Tasks)](/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs/add-terraform-enterprise-run-tasks.md)

## Verify CI/CD Run Integration

To verify integration, in **Application Security**, select **Home** > **Settings** > **CICD Runs** tab. Check that your repository is displayed.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f9db26b2cbb0d06906c5645ea95772008b1be496%2Fci-cd-run-verify3.0.png?alt=media" alt="ci cd run verify3.0"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/ci-cd-runs.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
