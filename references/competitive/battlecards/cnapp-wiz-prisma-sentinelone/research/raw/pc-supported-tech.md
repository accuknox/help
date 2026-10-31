For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/supported-technologies.md).

Prisma Cloud Application Security supports the following technologies and frameworks.

## Supported Package Managers and Languages[Direct link to heading](https://docs.prismacloud.io/content-collections/application-security/supported-technologies\#supported-package-managers-and-languages)

Prisma Cloud Application Security supports the following package managers and languages. For a list of supported package managers for Software Composition Analysis, refer to [Supported Package Managers for Software Composition Analysis (SCA)](https://docs.prismacloud.io/content-collections/application-security/supported-technologies#sca-package-support) below.

## Supported IaC Frameworks[Direct link to heading](https://docs.prismacloud.io/content-collections/application-security/supported-technologies\#supported-iac-frameworks)

ARM

Bicep

CloudFormation

Dockerfile

Helm

Kubernetes

Kustomize

OpenAPI

OpenTofu

Serverless Framework

Serverless Application Model (AWS SAM)

Terraform

Terraform Plan

Ansible

-

-

## Supported Package Managers for Software Composition Analysis (SCA)[Direct link to heading](https://docs.prismacloud.io/content-collections/application-security/supported-technologies\#supported-package-managers-for-software-composition-analysis-sca)

For SCA scans, Prisma Cloud supports the following package managers.

**Limitations**

- Prisma Cloud SCA frameworks do not scan development or test dependencies, such as `devDependencies` in JavaScript or the `test` scope in Java

- Maven and Gradle multi-module projects are only supported in periodic scans and are not available for CLI, IDE or CI/CD scans


Language

Package Manager

Manifest file

Dependency Tree

Licenses

Docker

docker

dockerfile

✔️

✔️

Go

Go Modules

go.mod

✔️

✔️

go.sum

✔️

✔️

HCL

Terraform

main.tf

✔️

Java

Maven

pom.xml (including parent POMs)

✔️

✔️

Gradle

build.gradle gradle.properties gradle-wrapper.properties

✔️

✔️

JavaScript

npm

package.json package-lock.json npm-shrinkwrap.json

✔️

✔️

yarn

yarn.lock

✔️

✔️

Bower

bower.json

✔️

✔️

Kotlin

Gradle

build.gradle.kts

✔️

✔️

Python

pip

req\*.txt

✔️

✔️

pipfile

pipfile.lock

✔️

✔️

Ruby

RubyGems

Gemfile
gemfile.lock
Gemspec

✔️

✔️

.NET (C#, F#)

NuGet
Paket

\*.csproj, [Directory.Packages.props](https://learn.microsoft.com/en-us/nuget/consume-packages/central-package-management)
packages.config
Paket

✔️

✔️

PHP

Composer

composer.lock composer.json

✔️

✔️

[PreviousFamiliarize Yourself with Application Security](https://docs.prismacloud.io/content-collections/application-security/familiarize-application-security) [NextGet Started with Application Security](https://docs.prismacloud.io/content-collections/application-security/get-started)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject