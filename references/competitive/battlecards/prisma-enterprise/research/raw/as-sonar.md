> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sonarqube-ingestion.md).

# Ingest SonarQube Data

You can ingest SAST findings directly from SonarQube into Prisma Cloud. This allows you to use Prisma Cloud Application Security’s analysis and visualization tools to identify critical vulnerabilities, prioritize remediation efforts, and improve your application code security.

## How to connect SonarQube with Prisma Cloud

1. Before you begin.
   1. Activate at least one CAS module that includes version control system (VCS) and repository integrations.
   2. [Generate and copy a SonarQube API token](https://docs.sonarsource.com/sonarqube-server/latest/user-guide/managing-tokens/#generating-a-token) Ensure to assign Web API scope to the API token.
   3. Add the [Prisma Cloud IP addresses](/content-collections/get-started/console-prerequisites.md) and hostname for Application Security to SonarQube’s allow list to enable access to the Prisma Cloud console.
   4. Grant the user integrating SonarQube with the following permissions:
      * In Prisma Cloud: 'System Admin', 'AppSec Admin' or GRBAC permissions
      * In SonarQube: A minimum of 'Browse' permissions is required
2. Under **Application Security**, select **Settings** > **Connect Provider** > **Code & Build Providers**.
3. Select **SonarQube** under the '3rd Party Ingestion' section in the catalog.
4. On the **Configure Integration** step of the integration wizard.
   1. Fill in the provided fields:
      * **API Token**: Paste the generated SonarQube API token
      * **URL and Port**: Provide the URL of your SonarQube instance. Port is optional
      * **Organization**: The SonarQube organization to be associated with the data ingestion. This is only required for SonarQube Cloud
   2. Click **Authorize**.

      By authorizing, you grant Prisma Cloud permission to (i) access data and execute tasks like suppression using SonarQube’s public API on your behalf, and (ii) process this data further to provide our services to you. You affirm that you have the authority to give this permission.
5. On the **Select Applications** step of the integration wizard.
   1. Select which SonarQube projects will be scanned:
      * All current projects
      * All current and future projects (This is the recommended option to ensure complete coverage and successful operation of all features)
      * Only selected projects > select the projects from the menu that is displayed
   2. Click **Next**.

      'Projects' in SonarQube and 'Repositories' in Prisma Cloud are identical artifacts.
6. On the **Map to Repositories** step of the integration wizard:
   1. Select an option:
      * Accept the displayed mapping as detected by Prisma Cloud. This does not require any action on your part
      * Manually configure mapping if Prisma Cloud could not match a project to a repository: Select Set in the Cortex Cloud Application Security Repository column, and select a repository from the list that is displayed
      * Automatically map future SonarQube projects
      * Manually modify mapping: Click Replace next to the existing mapped Cortex Cloud Application Security repository. This will open an option to select a different repository from the displayed list, allowing you to update the mapping

        Mapping establishes relationships between SonarQube Applications and Prisma Cloud code repositories, simplifying access management and enabling risk analysis at the repository level, including displaying findings on the tenant.
   2. Click **Next**.
7. Select **Done** on the **Status** step of the wizard to complete the integration, initiating an automatic ingestion of data from the integrated SonarQube applications.

## Verify Integration

1. On Application Security select **Settings** > **3rd Party Ingestion**.
2. Verify that the status of the relevant SonarQube project is listed as **Connected**.

   Periodic scans for Prisma Cloud scanners will not fail if SonarQube ingestion fails.

## Manage Connections

Manage integrations on the console from the **Providers** page under **Settings**.

1. On Application Security select **Settings** > **3rd Party Ingestion**.
2. Select an action under the **Actions** column of a project:
   * **Reselect Applications**: Redirects to the **Select Projects** step of the integration wizard, allowing you to manage selected applications
   * **Change Mapping**: Redirects to the **Map to Repositories** step of the wizard, allowing you to manage mapping
   * **Delete Application**: Deletes the application. Mapped repositories will be deleted accordingly. This option is available only if 'All current and future applications' is not selected
   * **Delete Entire Integration**: Deletes the integration

## Manage CWE Weaknesses

To view and manage CWE weaknesses from ingested SonarQube findings, refer to [Manage Third-Party Ingested Data](/content-collections/application-security/risk-management/monitor-and-manage-code-build/third-party-ingest-manage.md).

## Limitations

* The current SonarQube SAST ingestion supports SonarQube periodic and CLI scans
* History and deduplication are not supported


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/get-started/connect-code-and-build-providers/third-party-ingestion/sonarqube-ingestion.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
