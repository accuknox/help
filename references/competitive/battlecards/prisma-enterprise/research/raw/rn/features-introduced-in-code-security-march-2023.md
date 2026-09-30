> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-code-security-release-information/features-introduced-in-code-security-march-2023.md).

# Features Introduced in March 2023

Learn about the new Code Security capabilities on Prisma® Cloud Enterprise Edition (SaaS) in March 2023.

The following new features or enhancements are available for Prisma Cloud Code Security. These capabilities help agile teams add security checks to their existing IaC (Infrastructure-as-Code) model and enforce security throughout the build lifecycle.

* [New Features](#new-features)
* [Policy Updates](#policy-updates)

## New Features

| FEATURE                                                                 | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Custom Prisma Cloud Permission group for Code Security capabilities** | <p>As a part of custom Prisma Cloud roles for Code Security, administrators can now define explicit permissions for Code Security workflows from Permission Group <strong>(Settings > Access Control > Add > Permission Group)</strong>. In addition to the existing System Admin permission you can define roles for:</p><ul><li>View access Permissions: Provide view access for Code Security Configuration, Projects, Supply Chain and Development Pipelines pages.</li><li>Repository permissions: Provide integrate, view, update and delete access to Repositories.</li></ul><p><img src="https://1815359018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0B0G9j3lh441nNaDZxLT%2Fuploads%2Fgit-blob-52eb28fa3eed417c816e3167c96f93de804ac111%2Fcodesec-rn-23.3.1.png?alt=media" alt="" data-size="original"></p>                                                            |
| **Enhancements to Audit Logs**                                          | <p>In addition to the existing Audit Logs <strong>(Settings > Audit Logs)</strong>, you can now see a list of all actions initiated by Prisma Cloud administrators on Code Security. The actions on the Audit Logs help you identify any configuration changes and activities initiated on the repositories behalf of the administrator. Here are the kind of actions you can track.</p><ul><li><strong>Suppression Management</strong>: Creating or deleting a suppression rule for the default branch on Projects <strong>(Code Security > Projects)</strong></li><li><strong>Enforcement</strong>: Adding a new Enforcement rule or reconfiguring an existing Enforcement rule by editing or deleting the rule. This also includes modifying the default thresholds of Enforcement parameters.</li><li><strong>Repository</strong>: Addition, deletion and updating integrated repositories.</li></ul> |
| **Secrets Scanning on Git History**                                     | <p>In addition to the current scans run on your repositories, Prisma Cloud now scans Git history to find exposed secrets that are deleted from code. You can view the scan results in the resource block on Projects <strong>(Code Security > Projects)</strong>, Secrets code category view. On Resource Explorer, you can also see the commit history on when the secret was added or removed.</p><p><img src="https://1815359018-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F0B0G9j3lh441nNaDZxLT%2Fuploads%2Fgit-blob-30a852de8bf6f59cdc2df4727dc9607dcc7091ab%2Fcodesec-rn-2-23.3.1.png?alt=media" alt="" data-size="original"></p>                                                                                                                                                                                                                                          |

## Policy Updates

| POLICY UPDATES                                                                  | DESCRIPTION                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AWS EBS volume region with encryption is disabled**                           | <p><strong>Changes-</strong> The Build remediation instructions are being updated.</p><p><strong>Impact-</strong> No impact on Code Security findings.</p>                                                                 |
| **Basic Auth Credentials**                                                      | <p><strong>Changes-</strong> The policy name is being updated.</p><p><strong>Current Policy Name-</strong> Basic Authentication Credentials</p><p><strong>Impact-</strong> No impact on Code Security findings.</p>        |
| **Policy Deletions**                                                            |                                                                                                                                                                                                                            |
| **AWS EC2 instance is not configured with VPC**                                 | <p><strong>Changes-</strong> This policy is deleted because resources are configured in VPC by default.</p><p><strong>Impact-</strong> Code Security findings for this policy will no longer be surfaced in scans.</p>     |
| **My SQL server enables public network access (duplication of CKV\_AZURE\_53)** | <p><strong>Changes-</strong> This policy is a duplication of an existing policy, therefore will be deleted.</p><p><strong>Impact-</strong> Code Security findings for this policy will no longer be surfaced in scans.</p> |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-code-security-release-information/features-introduced-in-code-security-march-2023.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
