> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/familiarize-application-security.md).

# Familiarize Yourself with Application Security

Learn more about Application Security through multiple functionalities that help you secure your software development lifecycle.

## Comprehensive Visibility

Real time, ongoing, comprehensive and accurate analysis of your technical stack, visualized through the following features:

* [Repositories](/content-collections/application-security/visibility/repositories.md): A broad overview view of your organization’s assets, providing detailed analysis of more than 600 programming languages and frameworks, technologies and integrations in its environment. You can see information about all your connected repositories, VCS in use, technologies, CI/CD pipelines, and more. In addition, a summary of IaC misconfigurations, secrets exposed, SCA violations and CI/CD Risks is displayed, giving you a comprehensive and accurate view of your organization’s repositories.
* [Technologies](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/application-security/visibility/technologies/technologies.md): An inventory of 100+ SDLC technologies in use across your software development delivery lifecycle. In addition you can view Supply Chain 3rd party inventories of all the apps and webhooks, Jenkins plugins and pipeline tools detected in your environment.
* [SBOM](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/application-security/visibility/sbom.md): A detailed inventory of third-party components in the code, highlighting open-source packages and enabling tracking of both direct and indirect dependencies. It places a particular emphasis on identifying and addressing vulnerable software packages.
* [Application Security Dashboard](/content-collections/dashboards/dashboards-application-security.md): The Application/Code Security dashboard provides a unified view of the most critical application security vulnerabilities and misconfigurations detected during scans. This view provides a contextual understanding of high priority errors categorized by severity, common policy errors, licensing errors, IaC misconfigurations, CVE vulnerabilities and more.

## Investigate Application Security

View your software development life cycle (SLDC) as a graphical representation. This visibility allows you to perform an in-depth analysis of security issues across your entire engineering ecosystem. You can digest and understand the assets in your environment, and the relationships between them.

For more see [Application Asset Queries](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/search-and-investigate/application-asset-queries/application-asset-queries.md).

## Risk Prevention

Address root causes, preemptively mitigate risks in code, and stop real-time cloud breaches using precise, contextual and expert remediation through the following features.

* [Projects](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/application-security/risk-management/monitor-and-manage-code-build/monitor-and-manage-code-build.md): A consolidated view of application security scan results performed by Prisma Cloud, categorized into the following code categories: IaC misconfigurations, Vulnerabilities, Secrets, and Licenses, across periodic scans of default , CI/CD runs and pull requests. A contextual summary of all issues across code categories is displayed under the Overview.
* [CI/CD Risks](/content-collections/application-security/risk-management/ci-cd-risks.md): Displays all vulnerabilities detected in your CI/CD pipelines, including details such as the risk severity, the location and suggested remediation.

## Developer Integrations

* **Detection**: You can run automated scans through various interfaces, including a dedicated command line interface (CLI), integrated development environment (IDE), and version control system (VCS) to identify cloud infrastructure misconfigurations and vulnerabilities across IaC, SCA, Secrets and Licenses. Remediation.
* **Remediation**: The Application Security module automatically generates code fixes and patches to address vulnerabilities and secure your code. It offers integrated pull request comments, fixes, and smart fixes that automate the security code review process and streamline remediation efforts.

Refer to [IDE](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/ides/ides.md) for more on the Prisma Cloud plugin for your IDE.

## Fundamental Concepts

Familiarize yourself with the following fundamental concepts.

| Concept                       | Definition                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AppSec                        | The practices and tools used to protect applications from external threats and ensure their confidentiality, integrity, and availability. This includes identifying and addressing security vulnerabilities in the application code, as well as ensuring that security controls are implemented throughout the application development lifecycle.                      |
| SIP                           | Security In the Pipeline (SIP) addresses the risk of code with security flaws flowing through the pipeline, providing the most effective measures tailored to the organization stack in order to detect such issues.                                                                                                                                                   |
| SAP                           | Security Around the Pipeline (SAP) addresses the risk of the pipeline being bypassed.                                                                                                                                                                                                                                                                                  |
| SOP                           | Security Of the Pipeline (SOP) addresses the security posture and the risk of security settings in pipeline systems such as the source control, CI, artifact repositories and container registries being compromised. SOP prevents the abuse of software delivery systems and processes in order to access the production environment.                                 |
| Repositories                  | A comprehensive view of an organization’s engineering technical stack from repository to deployment. See [Repositories](/content-collections/application-security/visibility/repositories.md) for more information.                                                                                                                                                    |
| Application Graph/ Graph View | The repository’s path to production and connectivity between artifacts, presented in graph view. See [Repository Application Graphs](/content-collections/application-security/visibility/repositories.md) for more information.                                                                                                                                       |
| Technologies                  | An inventory of technologies in use across your organization’s engineering environment. Includes applications and webhooks, Jenkins plugins and pipeline tools. See [Technologies](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/application-security/visibility/technologies/technologies.md) for more information. |
| CI/CD pipeline                | A set of practices and tools used to automate the building, testing, and deployment of software applications, facilitating the software development process.                                                                                                                                                                                                           |
| CI/CD risks                   | Risks in the CI/CD pipeline detected in the organization’s VCS, CI and artifacts, as well as cross-system risks. See [CI/CD Risks](/content-collections/application-security/risk-management/ci-cd-risks.md) for more information.                                                                                                                                     |
| CI/CD risk categories         | Categories of CI/CD risks resulting from research into attack vectors associated with CI/CD, and the analysis of high profile breaches and security flaws as published by [OWASP](https://owasp.org/www-project-top-10-ci-cd-security-risks/), allowing organizations to identify focus areas for securing their CI/CD ecosystems.                                     |
| Suppress CI/CD risks          | Intentionally silence a specific warning of a risk detected in the CI/CD pipeline. This is often done when the issue is deemed low-risk or otherwise unimportant, and the developer wishes to prevent the warning or error message from appearing in future code scans or builds. See here for more on suppressing CI/CD risks.                                        |
| VCS 3rd Parties               | Applications and webhooks connected to the VCS. See [VCS 3rd Parties](/content-collections/application-security/visibility/technologies/vcs-third-parties.md) for more information.                                                                                                                                                                                    |
| Jenkins Servers               | An inventory of Jenkins server instances in the system. See [Jenkins Servers](/content-collections/application-security/visibility/technologies/jenkins-plugins.md) for more information.                                                                                                                                                                              |
| Pipeline Tools                | An inventory of third party services and tools found in CI files. See [Pipeline Tools](/content-collections/application-security/visibility/technologies/pipeline-tools.md) for more information.                                                                                                                                                                      |
| Policies                      | A set of rules defining the expected behavior and configurations of resources such as cloud services. Policies cover a wide range of areas such as access control, encryption and compliance.                                                                                                                                                                          |
| Resource                      | A resource is a Cloud Platform entity, for example, an Amazon EC2 instance, a CloudFormation stack, or an Amazon S3 bucket.                                                                                                                                                                                                                                            |
| Incident                      | During each scan, incidents corresponding to each instance of non-conformance to a policy in IaC, SCA, and Secrets files in buildtime environments are created.                                                                                                                                                                                                        |
| Errors                        | During each scan, errors corresponding to each instance of non-conformance to a policy in runtime environments are created.                                                                                                                                                                                                                                            |
| Suppression                   | Suppression indicates that an incident is not problematic. You can Suppress an incident for all relevant resources or for a specific resource only.                                                                                                                                                                                                                    |
| Remediation                   | The following types of remediation are available, depending on the type of incident : Open Jira Ticket, Run Playbook, Open Fix PR.                                                                                                                                                                                                                                     |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/familiarize-application-security.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
