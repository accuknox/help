> For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/manage-code-weakness-issues.md).

# Manage SAST code weakness issues

Ingest third-party SAST findings to create actionable issues, enabling you to prioritize and track remediation and enhancing your security posture.

SAST code weakness scanners safeguard your applications by analyzing custom source code for security flaws, such as injection vulnerabilities, authentication bypasses, insecure cryptographic usage, and unsafe data handling, that could lead to exploitation in production environments. By detecting code weaknesses at code-time, the SAST scanner closes the gap between development practices and production-time security posture, preventing injection attacks, cross-site scripting, insecure deserialization, and other OWASP Top 10 risks from silently propagating into live environments.

Currently, Cortex Cloud does not support native SAST scanners. You can ingest Static Application Security Testing (SAST) findings from supported third-party vendors. These findings are raw security observations from your external scanners that Cortex Cloud then enriches and prioritizes to produce actionable remediation to mitigate code weaknesses.

#### Supported SAST vendors

Currently, Cortex Cloud Application Security supports SAST data integration from the following vendors:

* [Semgrep](/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/semgrep.md)
* [Snyk](/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/snyk.md)
* [Sonarqube](/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/sonarqube.md)
* [Veracode](/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/veracode.md)

In addition, you can upload SAST findings in SARIF format from [Generic collectors](/application-security/application-security/onboard-data-sources/ingest-third-party-data-sources/generic-3rd-party-appsec-collector.md).

#### Core achievements

* **Shifting security left:** Detecting code weaknesses at code-time, before vulnerable code is deployed, reduces the cost and risk of post-deployment remediation
* **Reducing code weakness noise:** Urgency-based prioritization isolates the code weaknesses that affect deployed, internet-exposed, or business-critical assets from low-risk findings in development environments. CWE classification and data flow analysis further distinguish exploitable weaknesses from theoretical risks
* **Accelerating remediation:** Automated fix suggestions and manual remediation guidance enable developers to resolve code weaknesses directly in the source repository without context-switching to external tools
* **Establishing compliance baselines:** Mapping code weaknesses to CWE identifiers and OWASP Top 10 categories provides auditable evidence of compliance with OWASP Top 10, OWASP ASVS, NIST SSDF, and organizational secure coding standards

#### Prerequisites

Before viewing and acting on code weakness issues, verify the following:

| Prerequisite            | Description                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| **License**             | An active Cortex Cloud license with Application Security entitlements.                                |
| **RBAC Role**           | The AppSec Admin or SOC Analyst role, or an equivalent custom role with issue management permissions. |
| **VCS Integration**     | At least one Version Control System (GitHub, GitLab, Bitbucket, Azure DevOps) integrated and active.  |
| **SAST Scanner**        | The SAST scanner enabled for the target repositories.                                                 |
| **Periodic or PR Scan** | At least one completed periodic scan or PR scan that includes SAST scanning results.                  |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation by asking a question.

Perform an HTTP GET request on the following URL with the `ask` and `goal` query parameters:

```
GET https://cortex-docs.paloaltonetworks.com/application-security/application-security-posture-management-aspm/manage-code-weakness-issues.md?ask=<question>&goal=<user_goal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is what the user is ultimately trying to achieve, the reason they need the answer. Sharing it helps GitBook give you a better, more relevant answer. A goal is most helpful when it describes the outcome the user wants rather than restating the question. For example, with `ask=how do I create an API token`, a goal like `automate deployments from our CI pipeline` lets GitBook tailor the answer to that use case.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
