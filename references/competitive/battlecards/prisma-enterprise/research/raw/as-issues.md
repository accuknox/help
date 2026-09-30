> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/monitor-code-build-issues.md).

# Monitor Code Build Issues

Prisma Cloud performs periodic scans on each integrated repository of the Version Control Systems (VCS) and event driven scans for CI/CD pipelines to find infrastructure misconfigurations, open source vulnerabilities, license compliance violations, CI/CD risks and exposed secrets.

The console initiates four types of scans.

* **VCS default branch scans**: Periodic scans performed on all main branches across repositories. During integration if you have not specified the branches for scan in your repository, Prisma Cloud by default considers the master branch.
* [Non-Default Branch Scan](/content-collections/application-security/get-started/non-default-branch-scan.md): Periodic scans performed across repositories on branches other than the default branch, as selected by the user.
* [VCS Pull Request scans](/content-collections/application-security/risk-management/monitor-and-manage-code-build/pull-request-scan.md): Event driven scans run on branches with open Pull Requests (PR) from your integrated repositories.
* **CLI and CI/CD runs**: Event driven scans performed on runs as configured by using the Enforcement parameters.

There are five code category views - **IaC misconfiguration, Vulnerabilities, Secrets,** and **Licenses**. In addition you can see a contextual summary of issues across code categories on **Overview**.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-428811c1fda5ad83294ffa6123f94843ae4f67b5%2Fproj.png?alt=media" alt="proj"><figcaption></figcaption></figure>

| Projects Code Category View | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Overview                    | A summary view of all your scan results across all code categories. The Overview lists errors by prioritizing build issues across the integrations.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| IaC Misconfiguration        | The view lists security issues after scanning integrated repositories, wherein the default branch of a repository lists all application security violations in the resource block with code tags, resource dependencies and resource history.                                                                                                                                                                                                                                                                                                                                                    |
| Vulnerabilities             | The error list in Vulnerabilities are open source dependency errors found in scanned open source packages and container image dependencies.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Secrets                     | A Secret is a programmatic access key that provides systems access to information, services, or assets. Secrets like API keys, encryption keys, OAuth tokens, certificates, PEM files, passwords, and passphrases are often explicitly stored in local or feature branches before being pushed to a main branch. In this view, see issues identified in your source code with remediation to perform a Manual Fix or Suppress the issue within the file where the issue originates. Scans also run on Git history to identify secrets that are removed from code but are present in Git history. |
| Licenses                    | Most open source software includes a license governing its use. License scanning identifies packages that violate open source usage policies. In this view, see the listing of licensing issues through periodic scans.                                                                                                                                                                                                                                                                                                                                                                          |
| VCS Pull Requests           | After configuring Enforcement, view issues for scans run on all open Pull Requests (PR) for your integrated repositories. On the Prisma Cloud console, you can access the scan result from the console or choose to access the VCS console and view the specific commit within PR for a manual fix.                                                                                                                                                                                                                                                                                              |
| CI/CD Runs                  | View issues for scans performing on runs of your integrated CI/CD pipelines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

To find relevant non-conformant scan results you can use filters or search using keywords or tags (if they are already a part of the code).

For each misconfiguration on **Projects**, you can either **Suppress** the issue, **Fix** it from the Prisma Cloud console, or access the repository in the Version Control System (VCS) to perform a manual fix.

## Issue Blocks

The scan results across code categories are seen as Issue Blocks. To help you prioritize the issues you can custom group the issues as a **Resource** or **Policy**.

* **Resource Issue Blocks**

  After periodic scans on resources, Prisma Cloud generates contextualized scanned results of each resource as a resource block. Scan results are vulnerabilities in the code or code errors found within the resource. Each resource block displays only five issues by default. Show More helps you display more issues within the resource.
* **Policy Issue Blocks**

  After periodic scans, Prisma Cloud generates a policy issue block. Within it are contextualized scan results with names and lists of all the resources violating the policy. As a default for event based scans on Licenses and VCS Pull Requests you will see issues as a policy issue block.

  In **Vulnerabilities** view, the grouping of policy issue blocks is according to the CVE severity.

### Types of Issue Blocks

Each code category can generate either a resource or a policy issue block. For understanding the types of blocks corresponding to the code category see the table.

| Resource Type/ Code Category | IaC Misconfiguration | Vulnerabilities | Licenses | Secrets | IaC Resource     |
| ---------------------------- | -------------------- | --------------- | -------- | ------- | ---------------- |
| ✔️                           | ✔️                   | ✔️              |          |         | Package          |
|                              | ✔️                   | ✔️              |          |         | File             |
|                              |                      |                 | ✔️       |         | Git Repository   |
|                              |                      |                 |          | ✔️      | Git Organization |
|                              |                      |                 |          | ✔️      | CI/CD pipeline   |

#### IaC Misconfiguration Issue Block

For each IaC misconfiguration issue, there is extensive information in the issue block. As a default view, issues found for IaC misconfigurations are viewable as a Resource issue block. In this example you see a Resource issue block.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-4fa4644b4a97bdf572a8a8ff4e36ca2df863965e%2Fproj-2.png?alt=media" alt="proj 2"><figcaption></figcaption></figure>

1. **Resource Name and Path**: Displays the resource name and the code path. If you choose to group issues by **Policy** then you will see the **Policy** and the **Severity**.
2. **Total number of Issues**: Displays the total number of issues identified in the resource.
3. **Additional Information**: Displays columns of the information regarding the issue.

Learn more about the issue from the table here.

| Column Name        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Repository**     | View the precise path of the repository where the issue is located.                                                                                                                                                                                                                                                                                                                                                                                             |
| **Policy**         | Gain insight into non-conformant policies, along with their associated severity levels.                                                                                                                                                                                                                                                                                                                                                                         |
| **Labels**         | <p>Each issue is accompanied by a specific label, providing clear categorization for better organization and understanding.</p><ul><li><strong>Has Fix</strong>: If an automated fix is available through Prisma Cloud, the issue will be flagged with this label for swift resolution.</li><li><strong>Custom Policy</strong>: Issues stemming from custom policies are identified with this label, distinguishing them from standard policy alerts.</li></ul> |
| **Git User**       | Access the name of the last Git user who made contributions prior to the identification of the issue, aiding in traceability.                                                                                                                                                                                                                                                                                                                                   |
| **First Detected** | Know exactly when the issue was first detected, providing a historical context for effective troubleshooting and resolution.                                                                                                                                                                                                                                                                                                                                    |

#### Vulnerabilities Issue Block

For Vulnerabilities, the issue block provides comprehensive details regarding the affected packages.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-5bb2c3ed893b86a317640289746afe5bf92fbcfd%2Fproj-3.png?alt=media" alt="proj 3"><figcaption></figcaption></figure>

1. **Package Name and Path**: Displays the package name and the code path. If you choose to group issues by **Policy** then you will see the **CVE**,**Severity** and the path of the resource.
2. **Total number of Issues**: Displays the total number of issues identified in the package.
3. **Additional Information**: Displays columns of the information regarding the issue.

Learn more about the issue from the table here.

| Column Name          | Description                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CVE**              | Provides the name of the Common Vulnerabilities and Exposures (CVE) and the associated severity level, offering critical information regarding the violation.                                                                                                                                                                                          |
| **Package**          | Gain insights into the violated package, indicating whether it is a core 'Root' package or a dependent one. In the case of a dependent package exposing the CVE, you can also identify the name of the dependent package, providing valuable context for remediation.                                                                                  |
| **Root fix version** | View the recommended version for the root package that requires an update to address the vulnerability, ensuring a clear path to resolution.                                                                                                                                                                                                           |
| **CVSS**             | Provides the Common Vulnerability Scoring System (CVSS) score, providing a standardized measure of the vulnerability’s severity, aiding in risk assessment.                                                                                                                                                                                            |
| **Risk Factors**     | Utilizes predefined values on Prisma Cloud to assess the risk associated with the CVE. Factors considered include the availability of a fix, attachment complexity, potential Denial of Service (DoS) attacks, attack vector, and potential for remote code execution, offering a comprehensive understanding of the vulnerability’s potential impact. |
| **First Detected**   | Know exactly when the issue was first detected, providing a historical context for effective troubleshooting and resolution.                                                                                                                                                                                                                           |

#### Secrets Issue Block

The secrets issue scans run at the file level rather than on a repository. As a result, you will find detailed information on file-related issues within the issue block.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-632b5ade42c8bc9138cbd4c023a5d2964efeb9b3%2Fproj-4.png?alt=media" alt="proj 4"><figcaption></figcaption></figure>

1. **Secret Name and Path**: Displays the repository name and the code path. If you choose to group issues by **Policy** then you will see the **Secret type** with **Severity**.
2. **Total number of Issues**: Displays the total number of issues identified in the file.
3. **Additional Information**: Displays columns of the information regarding the issue.

| Column Name        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Secret type**    | Provides the severity level of the exposed secret within the code giving you a valuable insight into a potential impact.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Risk Factors**   | <p>Key risk factors are assessed for secrets:</p><ul><li><strong>Private or Public</strong>: Distinguishes if the repository housing the secret is publicly accessible or restricted to private access, influencing the potential exposure risk.</li><li><strong>Last Modified By</strong>: Identifies the name of the user who last made contributions before the issue was identified, offering traceability and accountability.</li><li><strong>Modified On</strong>: Specifies the date of the last modification to the relevant code, aiding in contextual understanding and assessment.</li><li><strong>Validity</strong>: Utilizes public APIs to assess the validity of a secret, categorizing it as Valid (to be prioritized), Invalid (can be deprioritized), or Unknown if Prisma Cloud is unable to determine its validity.</li><li><strong>Privileged</strong>: Determines if the exposed AWS Access Key possesses privileged permissions, based on IAM Security capabilities.</li><li><strong>Found in History</strong>: If the secret no longer exists in the current commit, but was found in history scanning.</li><li><strong>IaC Resource</strong>: Identifies if a secret is located within an Infrastructure as Code (IaC) resource block.</li></ul> |
| **First Detected** | Know exactly when the issue was first detected, providing a historical context for effective troubleshooting and resolution.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

#### Licensing Issue Block

For licensing issues, there is extensive information in the resource block for packages using the open source licensing.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-fa01b1af36c3a2248a49d5e68b3ae1bd160c2eca%2Fproj-5.png?alt=media" alt="proj 5"><figcaption></figcaption></figure>

1. **Package Name and Path**: Displays the package name and the code path. If you choose to group issues by **Policy** then you will see the **Policy** with **Severity**.
2. **Total number of Issues**: Displays the total number of issues identified in the package.
3. **Additional Information**: Displays columns of the information regarding the issue.

| Column Name        | Description                                                                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Repository**     | View the precise path of the repository where the issue is located, allowing for quick navigation and resolution.                                                                                |
| **Policy**         | Provides details on the severity level of the policy violation, particularly relevant when utilizing open source licensing packages, offering insight into potential risks.                      |
| **License Type**   | Identifies the source of the license, distinguishing between whether it originates from the root package or a dependent package, aiding in understanding licensing obligations and dependencies. |
| **Package**        | Specifies the name of the package, offering a clear identification of the component under consideration. This information is essential for precise issue resolution and management.              |
| **First Detected** | Know exactly when the issue was first detected, providing a historical context for effective troubleshooting and resolution.                                                                     |

#### Sorting Issues

On **Projects** in addition to prioritizing issues by grouping you can sort the issues by highest **Severity** or **Count**.

* **Severity**: Viewable as a default sorting across all code category views. Severity enables you to sort issues with the highest severity of Critical followed by the other severity levels.
* **Count**: You can choose to view issues by the highest count to prioritize remediative solutions.

## Additional Information in Side Panel

In helping you make informed decisions, Prisma Cloud provides detailed insights on each issue through the Resource Explorer, offering additional information accessible via the side panel. Subsequently, all identified issues are efficiently addressed through the Fix Cart for swift remediation.

### Resource Explorer

The Resource Explorer enables you to make well-informed decisions regarding security violations, allowing you to discern if the violation is linked as a dependency to other resources within the repository. Additionally, you can delve into the change log of the resource for further insights. This contextualized information is conveniently organized across four tabs for easy navigation and comprehension.

* **Details**: Offers you insights into the connections between resources, empowering you to make informed decisions about their criticality or necessity.

  <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c1e935d7e20f203009094bf3262dfe01dbbb6b64%2Fproj-7.png?alt=media" alt="proj 7"><figcaption></figcaption></figure>
* **Issues**: Enables you you can comprehensively review security concerns spanning all resource types, with package severity thresholds. This information equips you to take corrective action, be it fixing, suppressing, or manually addressing the issue.
* **History**: Explore comprehensive details about a resource, including suppression records, change logs, and applied fixes.

  <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-da19dfce622b9c6713020d1b2a63af391215b952%2Fproj-9.png?alt=media" alt="proj 9"><figcaption></figcaption></figure>
* **Traceability**: Effortlessly explore and monitor connections between build-time and runtime resources, ensuring a thorough understanding of your system’s architecture.

  The support for History and Traceability is currently only IaC resources, and the support for Errors is currently only available for packages.

### Fix Cart

The Fix Cart showcases the selected issues you intend to address before initiating a Pull Request.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a6a3b7891815397b50283f71f213be311929e9db%2Fproj-10.png?alt=media" alt="proj 10"><figcaption></figcaption></figure>

See [Fix Issues in Scan](/content-collections/application-security/risk-management/monitor-and-manage-code-build/fix-code-issues.md) to know more on how to add issues to a fix cart.

### Filter Scan Results

Prisma Cloud enables you to filter your scan results across all code categories. You can filter your scan results across five default filters.

* [Repositories](#repositories-)
* [Branch](#branch-)
* [Code Categories](#code-categories)
* [Issue Status](#issue-status)
* [Severities](#severities-)
* [Add Filter](#add-filter)

#### Repositories

A list of integrated repositories.

#### Branch

A list of the supported branches of a VCS branch scan. Currently, the repository’s default branch is selected by default and cannot be configured. This configuration is applicable for views - Overview, IaC Misconfiguration, Vulnerabilities, Secrets, and Licenses.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f06212f29eaac104af0d89bfee5bec1b86f5572a%2Fproj-15.png?alt=media" alt="proj 15"><figcaption></figcaption></figure>

#### Code Categories

A Category filters resources according to Compute, Drift, General, IAM, Kubernetes, Licenses, Monitoring, Networking, Public, Secrets, Storage, and Vulnerabilities. During the time of repositories integration on Prisma Cloud Application Security, your defined Categories associated with the repositories also help with filters.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-00c0ec36b91a1501a2071bbe9be1a8ad45da54ca%2Fproj-13.png?alt=media" alt="proj 13"><figcaption></figcaption></figure>

#### Issue Status

Status for each scanned repository is created based on the non-conformance to a policy. The repository status can be further filtered as Errors, Suppressed and Passed.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d4105fd875a869a04bca3b63313986a6be725304%2Fproj-11.png?alt=media" alt="proj 11"><figcaption></figcaption></figure>

| Status      | Description                                                                                                                                                                                                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Error       | A resource appears with an error status when it is non-conformant to a policy.                                                                                                                                                                                                     |
| Passed      | A resource that has conformant policies or may have a history of fixed errors.                                                                                                                                                                                                     |
| Suppressed  | A resource previously appeared with a non-conformant policy but is suppressed with a Suppress action. To suppress a non-conformant policy in a resource is when you absolve the scanned result with a definitive explanation indicating the non-conformance to be not problematic. |
| Fix Pending | A fix awaiting a PR merge in your VCS console.                                                                                                                                                                                                                                     |

Your scanned resources appear on **Application Security > Projects** with an active Error filter by default. You can choose to add more filters or remove the Error filter.

#### Severities

A Severities indicates an impact on a non-conformant resource in your repository. Resources can be filtered as Critical,High, Medium, Low and Informational in severity.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-3a2cbf3f96fcf8b4fd45d2043acd254d49441bff%2Fproj-12.png?alt=media" alt="proj 12"><figcaption></figcaption></figure>

#### Add Filter

You can add additional filters to the default views or create granular customization for your custom view using these filters.

| Filter                     | Description                                                                                                                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Git Users                  | A list of Git users who contribute to the code of the selected repositories.                                                                                                                                                                                                                 |
| Vulnerability Risk Factors | Filters issues as - Has Fix, Attack Complexity, DoS, Attack Vector, and Remote Execution.                                                                                                                                                                                                    |
| IaC Categories             | Filters resources according to General, Compute, Drift, IAM, Kubernetes, Monitoring, Networking, Public, and Storage. During the time of repositories integration on Prisma Cloud Application Security, your defined categories associated with the repositories also help with this filter. |
| Secrets Risk Factor        | Filters secrets issues using the risk factors of Public or Private Repository. You can select a single or both risk factors at a time.                                                                                                                                                       |
| File Types                 | Filters issues using the list of supported file formats.                                                                                                                                                                                                                                     |
| IaC Labels                 | Filters resources as - Has Fix or Custom Policy.                                                                                                                                                                                                                                             |
| IaC Tags                   | Filters issues using the tags used in the resources.                                                                                                                                                                                                                                         |

## Last Scan Date of a Repository

Currently, the last scan date of a repository only relates to completed Infrastructure-as-Code (IaC) scans. The IaC module must be enabled to display this feature.

To find the last scan of a repository in **Application Security**, select **Settings** > **Code & Build Providers** tab. The last scan of a repository is displayed under the **Last Scan Date** column.

By default, the **Providers** tab under the **Manage** section in the left navigation menu is selected. If it is not selected, ensure to select it.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e726f87bc91ab9a27cf9cf8ef4e753dd92558a6c%2Fmonitor-code-build-last-scan-date.png?alt=media" alt="monitor code build last scan date"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/risk-management/monitor-and-manage-code-build/monitor-code-build-issues.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
