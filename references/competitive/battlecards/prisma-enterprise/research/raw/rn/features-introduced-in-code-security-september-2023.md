> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-code-security-release-information/features-introduced-in-code-security-september-2023.md).

# Features Introduced in September 2023

Learn about the new Application Security capabilities on Prisma® Cloud Enterprise Edition (SaaS) in September 2023.

The following new features or enhancements are available for Prisma Cloud Application Security. These capabilities help agile teams add security checks to their development process and enforce security throughout the build lifecycle.

* [New Policies](#new-policies)
* [REST API Updates](#rest-api-update)

## New Policies

Prisma Cloud has included the following new Application Security configuration build policies. You will receive alert notifications for these policy violations only if you have enabled the **CI/CD Security** subscription on Prisma Cloud Application Security (CAS).

| POLICY NAME                                                                                             | SEVERITY |
| ------------------------------------------------------------------------------------------------------- | -------- |
| Pull request reviews are not required in Azure Repos before merging to the default branch               | Medium   |
| Requestors allowed to self-approve pull requests on default branch in Azure Repos                       | Medium   |
| Approvals for pull requests on the default branch in GitHub are not revoked when new commits are pushed | Medium   |
| Forking of private repositories in the GitHub organization is allowed                                   | Medium   |
| Forking of a private GitHub repository is allowed                                                       | Medium   |
| Private repository forks can lead to code leakage in GitHub                                             | Medium   |
| GitHub organization secret not scoped                                                                   | Medium   |
| Any organization member in GitHub can create internal repositories                                      | Low      |
| GitHub Actions workflow allows command execution through the standard output stream                     | Medium   |
| Code owners reviews are not required in GitHub before merging to the default branch                     | Medium   |
| GitHub organization’s identity not confirmed with a verified badge                                      | Info     |
| Any organization member In GitHub can create private repositories                                       | Low      |
| Environment variables exposed when printed to log in Azure Pipelines                                    | Low      |
| Certificate not verified by Azure Pipelines pipeline command                                            | Medium   |
| Azure Pipelines commands transmit data over an unencrypted channel                                      | Medium   |
| Push restrictions are not enforced on the default branch in GitHub                                      | Low      |
| Merging to default branch with outdated code allowed in GitHub                                          | Low      |
| Missing integrity check for downloaded executable in Azure Pipelines pipeline                           | Medium   |
| Packages insecurely installed through “npm install” command in Azure Pipelines pipeline                 | Medium   |
| GitLab project configured for group-wide access using job token                                         | Medium   |
| GitLab CI/CD accesses cloud provider using insecure long-term credentials                               | Medium   |
| Excessive GitHub Actions pipeline permissions on the repository                                         | Medium   |
| Secrets found in logs of an Azure Pipelines pipeline                                                    | Medium   |
| Project Service hooks sent over unencrypted channel                                                     | Low      |
| Project service hook SSL verification is disabled                                                       | Low      |
| Forking of a private Azure repository is allowed                                                        | Medium   |
| Self-hosted runner group allows public repositories                                                     | High     |
| Default branch does not require signed commits in GitHub                                                | Low      |
| CirceCI pipeline vulnerable to command injection                                                        | Critical |
| Insecure definition of secret variable in Azure pipeline                                                | Medium   |
| Mutable orb used in the CircleCI pipeline                                                               | Medium   |
| Public repository created in GitHub                                                                     | Info     |

## REST API Updates

| FEATURE                                                                              | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **New endpoints to retrieve the code errors detected by Application Security scans** | <p>The <a href="https://pan.dev/prisma-cloud/api/code/errors/">Errors</a> category of the Prisma Cloud Application Security API includes two new endpoints to retrieve the code errors detected by Application Security scans.</p><ul><li><a href="https://pan.dev/prisma-cloud/api/code/get-periodic-findings/">Get Code Issues from Periodic Scans</a></li><li><a href="https://pan.dev/prisma-cloud/api/code/get-cicd-findings/">Get Code Issues from Pull Requests Scans and CICD Runs</a></li></ul><p>Both endpoints have the following request parameters for filtering the results:</p><ul><li>Repositories</li><li>Branch (relevant for VCS default branch scanning)</li><li>Pull request (relevant for Pull Request scans)</li><li>Commit (relevant for Pull Request scans)</li><li>CI/CD run ID (relevant for CI/CD run scans)</li><li>Code Categories</li><li>Issue Status</li><li>Severities</li><li>File types</li><li>Git users (not supported for Vulnerability scanning)</li><li>Vulnerability risk factors</li><li>Secrets risk factors</li><li>IaC Categories</li><li>IaC labels</li><li>IaC resource tags</li></ul> |


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/release-notes/prisma-cloud-release-information/classic-releases/prisma-cloud-code-security-release-information/features-introduced-in-code-security-september-2023.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
