> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/application-security.md).

# Application Security

The Application Security on Prisma Cloud console provides comprehensive security for your software engineering environment, covering the entire software development lifecycle from code to cloud including Infrastructure as Code (IaC) security, Software Composition Analysis (SCA), Secrets Security, CI/CD pipeline security and container image scanning. Application Security is manifested through visibility, detection, prevention, and remediation capabilities. By leveraging these, you gain comprehensive insights into your engineering ecosystem and establish a robust security posture to protect your organization’s software development environment.

Application Security seamlessly integrates into your software delivery chain, capturing crucial information such as programming languages and frameworks, CI/CD pipelines and plugins. It then maps this information to their respective repositories, creating a comprehensive "Technical DNA" of your software engineering ecosystem, including robust Supply Chain security, providing a comprehensive inventory and visualization of application dependencies through a graphical interface designed to bridge developer, operations, and security workstreams. In addition, Application Security scans to detect Infrastructure-as-Code (IAC) resources, direct and indirect Software Composition Analysis (SCA) packages, and secrets declared in code.

This comprehensive visibility allows you to gain valuable insights into the various components of your engineering environment, enabling enhanced analysis, monitoring security and implementation of tailored security measures. It ensures that you can prioritize and address critical risks without disrupting your engineering processes. This ensures a complete understanding and security posture of your organization’s engineering ecosystem.

You can run scans through various interfaces, including a dedicated command line interface (CLI), integrated development environment (IDE), and version control system (VCS). The Application Security automates security engineering by identifying cloud infrastructure misconfigurations and vulnerabilities across IaC, SCA , Secrets, as well as CI/CD risks in the pipeline. Investigative capabilities provided by Prisma Cloud complement the module, providing insights on how best to resolve misconfigurations, evaluating whether packages are vulnerable and secrets are valid, and identifying potential attack vectors on pipelines.

The Application Security also automatically generates code fixes and patches to address vulnerabilities and secure your code. It offers integrated pull request comments, fixes, and smart fixes that automate the security code review process and streamline remediation efforts.

Out of the box policies and guardrails, as well as an option to create custom policies, allow you to prevent the deployment of misconfigured, vulnerable or leaked code. They also enable the implementation of recommended pipeline hardening controls to enhance the security of your software delivery processes.

## Supported Environments

The Application Security is available for Prisma Cloud tenants in the following environments:

* app.prismacloud.io
* app2.prismacloud.io
* app3.prismacloud.io
* app4.prismacloud.io
* app.anz.prismacloud.io
* app.ca.prismacloud.io
* app.eu.prismacloud.io
* app2.eu.prismacloud.io
* app2.ind.prismacloud.io
* app.id.prismacloud.io
* app.sg.prismacloud.io
* app.uk.prismacloud.io
* app.jp.prismacloud.io
* app.fr.prismacloud.io


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/application-security.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
