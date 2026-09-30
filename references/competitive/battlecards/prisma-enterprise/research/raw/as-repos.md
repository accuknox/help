> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories.md).

# Code Repositories

Integrate Prisma Cloud with your code repository version control systems to scan for misconfigurations in your infrastructure-as-code (IaC) files, vulnerabilities in your software composition analysis (SCA) packages, secrets exposed in your code and license non-compliance. Prisma Cloud also scans for CI/CD pipeline risks when the system supports this feature. For more information, refer to the relevant integration guide.

Code repository integrations include:

* [AWS CodeCommit](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-aws-codecommit.md)
* [Azure Repos](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-azurerepos.md)
* [Bitbucket](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-bitbucket.md)
* [Bitbucket Server](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-bitbucket-server.md)
* [GitHub](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-github.md)
* [GitHub Server](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-github-server.md)
* [GitLab](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-gitlab.md)
* [Gitlab Self-managed](/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories/add-gitlab-selfmanaged.md)

## Verify Integration

To verify an integration, in **Application Security**, select **Home** > **Settings** > **Code & Build Providers** tab. Check that the status of the integrated system displays **Connected**.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-652f24b772497285936a8d68d5624484bcc2f7ca%2Fverify-code-and-build-permissions.png?alt=media" alt="verify code and build permissions"><figcaption></figcaption></figure>

## Disclaimer

While we provide guidance during integration and explain the steps involved when you are redirected to third party’s platforms (such as GitHub and so on), we cannot assume responsibility for changes or variations in their processes. For accuracy, always refer to the official documentation of the third party to ensure you are following their most current and precise instructions.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/code-repositories.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
