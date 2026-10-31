> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners.md).

# Code Security scanners

The Code Security module provides automated, native scanning tools designed to enhance the security posture of your applications and infrastructure. Integrating these scanners into your development workflow facilitates a "shift-left" approach to security, enabling the proactive identification and remediation of vulnerabilities early in your software development lifecycle (SDLC).

The module includes both native scanners and the capability to ingest data from third-party scanners, giving you comprehensive visibility into your security posture.

Code Security scanners include:

* **Software Composition Analysis** (SCA) scanners: Modern applications frequently incorporate numerous open-source and third-party packages. Code Security SCA scanners automate the inspection of these dependencies. They identify known vulnerabilities (tracked as CVEs), assess license compliance to mitigate legal risks, and detect package operational risks such as outdated or unmaintained components. This provides critical insight into your software's complete composition, enabling informed decisions about external code. For more information refer to [Software Composition Analysis (SCA ) scanners](/application-security/code-security/code-security-scanners/software-composition-analysis-sca-scanners.md)
* **Secrets** scanner: The accidental exposure of sensitive credentials—including API keys, passwords, or tokens—within source code or configuration files represents a significant security risk. The Code Security module secrets scanner detects hardcoded secrets across your repositories and code. Early identification of these exposures prevents unauthorized access and potential data breaches. For more information refer to [Secrets scans](/application-security/code-security/code-security-scanners/secrets-scans.md)
* **Infrastructure as Code (IaC )misconfiguration** scanner: Analyze your infrastructure configuration files prior to deployment to detect misconfigurations, insecure defaults, and compliance violations, thereby preventing the introduction of vulnerabilities into your operational environments. For more information refer to [Infrastructure as Code (IaC) misconfiguration scanner](/application-security/code-security/code-security-scanners/infrastructure-as-code-iac-misconfiguration-scanner.md)
* **IaC Drift detection** scanner: Identifies discrepancies between the desired state defined in your Infrastructure as Code templates and the actual state of deployed cloud resources. By detecting unauthorized changes, manual overrides, and configuration drift, this scanner ensures that your code repository remains the single source of truth and helps you address security-critical deviations before they introduce vulnerabilities into your live environments. For more information refer to [IaC Drift Detection scans](/application-security/code-security/code-security-scanners/iac-drift-detection-scans.md)

In addition to the native code security scanners, Cortex Cloud Cloud ingests data from third-party scanners. This allows you to consolidate your security findings and manage them all within a single platform for a holistic view of your security posture. For more information about third party scanners, refer to [Ingest third-party SCA data](/application-security/software-supply-chain-security/risk-and-remediation/software-composition-analysis-sca-scanners/ingest-third-party-sca-data.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://cortex-docs.paloaltonetworks.com/application-security/code-security/code-security-scanners.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
