> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-application-security.md).

# Cortex Cloud Application Security

Discover Cortex XSIAM Application Security for ASPM, supply chain security, and code security.

The Cortex Cloud Application Security module provides comprehensive security for your applications throughout their entire lifecycle. It offers unified visibility and control over your application's security from development through to deployment.

## Use cases

* **Application Security Posture Management (ASPM)**: Provides a consolidated view of application risks and vulnerabilities across your environment, enabling you to understand and manage your overall security posture. For more information refer to [Application Security Posture Management (ASPM)](/application-security/application-security-posture-management-aspm/application-security-posture-management-aspm.md)
* **Supply Chain Security**: Focuses on securing your continuous integration and continuous delivery pipelines, ensuring the integrity and security of your automated build and deployment processes. For more information refer to [Software supply chain security](/application-security/software-supply-chain-security/software-supply-chain-security.md)
* **Code Security**: Identifies and helps mitigate security issues directly within your source code, including exposed secrets, vulnerabilities in Infrastructure-as-Code (IaC) and open-source components, license miscompliance and package operational risk. from the earliest stages of development. For more information refer to [Code Security](/application-security/code-security/code-security-scanners.md)

## License requirements

To enable and utilize the components of the Application Security module, an active base license is required.

While some features are included by default, others require a dedicated add-on purchase.

## Base licenses

You must have at least one of the following active base licenses to access the Application Security module:

* Cloud Posture Security or Cloud Runtime Security
* Cortex XSIAM Premium

### Module components

* Application Security Posture Management (ASPM): Included with base license
* Supply Chain Security: Included with base license
* Code security: Requires a separate **Application Security Add-on** purchase in addition to your existing Cloud (Posture or Runtime) or Cortex XSIAM Premium base license

For more information, see [Cortex Cloud Application Security](https://cortex-docs.paloaltonetworks.com/application-security/)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://cortex-docs.paloaltonetworks.com/cortex-xsiam/cloud-security/cortex-cloud-application-security.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
