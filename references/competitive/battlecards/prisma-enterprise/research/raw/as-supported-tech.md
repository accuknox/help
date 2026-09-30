> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/supported-technologies.md).

# Supported Technologies

Prisma Cloud Application Security supports the following technologies and frameworks.

## Supported Package Managers and Languages

Prisma Cloud Application Security supports the following package managers and languages. For a list of supported package managers for Software Composition Analysis, refer to [Supported Package Managers for Software Composition Analysis (SCA)](#sca-package-support) below.

## Supported IaC Frameworks

| ARM            | Bicep                | CloudFormation                         | Dockerfile |
| -------------- | -------------------- | -------------------------------------- | ---------- |
| Helm           | Kubernetes           | Kustomize                              | OpenAPI    |
| OpenTofu       | Serverless Framework | Serverless Application Model (AWS SAM) | Terraform  |
| Terraform Plan | Ansible              | -                                      | -          |

## Supported Package Managers for Software Composition Analysis (SCA)

For SCA scans, Prisma Cloud supports the following package managers.

**Limitations**

* Prisma Cloud SCA frameworks do not scan development or test dependencies, such as `devDependencies` in JavaScript or the `test` scope in Java
* Maven and Gradle multi-module projects are only supported in periodic scans and are not available for CLI, IDE or CI/CD scans

| Language      | Package Manager                                          | Manifest file                                                                                                                                                            | Dependency Tree | Licenses |
| ------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | -------- |
| Docker        | docker                                                   | dockerfile                                                                                                                                                               | ✔️              | ✔️       |
| Go            | Go Modules                                               | go.mod                                                                                                                                                                   | ✔️              | ✔️       |
| go.sum        | ✔️                                                       | ✔️                                                                                                                                                                       |                 |          |
| HCL           | Terraform                                                | main.tf                                                                                                                                                                  |                 | ✔️       |
| Java          | Maven                                                    | pom.xml (including parent POMs)                                                                                                                                          | ✔️              | ✔️       |
| Gradle        | build.gradle gradle.properties gradle-wrapper.properties | ✔️                                                                                                                                                                       | ✔️              |          |
| JavaScript    | npm                                                      | package.json package-lock.json npm-shrinkwrap.json                                                                                                                       | ✔️              | ✔️       |
| yarn          | yarn.lock                                                | ✔️                                                                                                                                                                       | ✔️              |          |
| Bower         | bower.json                                               | ✔️                                                                                                                                                                       | ✔️              |          |
| Kotlin        | Gradle                                                   | build.gradle.kts                                                                                                                                                         | ✔️              | ✔️       |
| Python        | pip                                                      | req\*.txt                                                                                                                                                                | ✔️              | ✔️       |
| pipfile       | pipfile.lock                                             | ✔️                                                                                                                                                                       | ✔️              |          |
| Ruby          | RubyGems                                                 | <p>Gemfile<br>gemfile.lock<br>Gemspec</p>                                                                                                                                | ✔️              | ✔️       |
| .NET (C#, F#) | <p>NuGet<br>Paket</p>                                    | <p>\*.csproj, <a href="https://learn.microsoft.com/en-us/nuget/consume-packages/central-package-management">Directory.Packages.props</a><br>packages.config<br>Paket</p> | ✔️              | ✔️       |
| PHP           | Composer                                                 | composer.lock composer.json                                                                                                                                              | ✔️              | ✔️       |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/supported-technologies.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
