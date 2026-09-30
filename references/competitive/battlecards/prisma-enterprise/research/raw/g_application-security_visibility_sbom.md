> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/application-security/visibility/sbom.md).

# SBOM

'SBOM' provides a comprehensive inventory of third-party dependencies detected in your environment, including vulnerabilities and security insights. This information allows you to analyze your software components, libraries, and dependencies, in order to identify and remediate vulnerabilities and security risks. In addition, SBOM provides allows efficient management of patches and updates, and fosters collaboration between development, operations, and security teams.

For more information about SBOM’s, refer to [CISA](https://www.cisa.gov/sbom).

## Access SBOM

1. Before you can access the 'SBOM' page and view its resources, you must subscribe to the SCA module. For more on SCA licenses, refer to [Application Security Licenses](/content-collections/application-security/get-started/application-security-license-types.md).
2. In **Application Security**, select > **Home** > **SBOM**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-7aa618c0bb91b86a92a0e4fdbf6e8af90ff52b4a%2Fsbom-intro5.1.png?alt=media" alt="sbom intro5.1"><figcaption></figcaption></figure>

The SBOM inventory displays dependencies or packages in your organization, including the following details:

* **Package**: The name of the package
* **Version**: The version of the package
* [Package Operational Risks](#package-op-risk)
* **License**: The package license
* **Found In**: The repositories in which the package was detected. The number in the column represents the amount of repositories in which the package is found
* **Vulnerabilities**: The vulnerabilities detected in the package, with a link to a CVE database for further information. The number in the column represents the amount of multiple vulnerabilities detected in the package
* **Highest Severity**: The highest severity of a vulnerability found in a package when multiple vulnerabilities are detected, or the severity of a single vulnerability
* [Identify AI/ML Open Source Packages](#aispm)

Selecting a package from the inventory table opens the **Resource Explorer** displaying additional information about the entity.

* The **Details** tab (default) provides metadata about the package. Additionally, details of factors that define the package Operational Risk are displayed. See [Package Operational Risk](#package-op-risk) for more information

  <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e33f93c628ef0cc9377cd0f890068d5b41ecf28f%2Fsbom-details5.0.png?alt=media" alt="sbom details5.0"><figcaption></figcaption></figure>
* The **Issues** tab includes a list and details of all vulnerabilities detected in the package

  <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a090f93bc9c591be5e8133afce431910b5c7ce67%2Fsbom-issues-3.0.png?alt=media" alt="sbom issues 3.0"><figcaption></figcaption></figure>
* The **Repositories** tab includes details of the repositories hosting the packages

  <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-b52605796846073a8fa208091d900d6a80a0c386%2Fsbom-repositories3.1.png?alt=media" alt="sbom repositories3.1"><figcaption></figcaption></figure>

## Filters

You can apply the following filters to narrow down a search for a package.

* **Repository**: Filter packages by repository. Only repositories that include packages are listed
* [Filter by AI/ML Category](#aiml-category)
* **Ecosystem**: Filter by the package manager hosting the dependency
* **Operational Risk**: Filter by [Package Operational Risk](#package-op-risk). Values: 'high', 'Medium', 'Low'
* **Popularity**: A factor contributing to the Operational Risk rating. Values: 'High', 'Medium', 'Low'
* **Maintenance**: A factor contributing to the Operational Risk rating. Values: 'Frequently Maintained', 'Moderately Maintained', 'Infrequently Maintained', 'Deprecated'
* **License**: Filter packages by their license
* **Vulnerabilities**: Filter vulnerabilities by their CVE ID
* **Severity**: Filter vulnerabilities by their severity
* **'Show only vulnerable'**: Toggle **ON** to display vulnerable packages only

## Package Operational Risks

'Package Operational Risk' assesses the operational risk and potential impact of each package in your codebase by examining factors such as package maintainers, popularity, and other relevant metrics. This analysis results in open-source package operational risk severity levels categorized into 'High', 'Medium' and 'Low'. By prioritizing risks based on these categories, you can effectively focus remediation efforts on the most critical issues.

**Limitation**: Package operational risk analysis currently supports npm packages stored in GitHub version control systems for Prisma Cloud customers located in US regions.

You can view a package’s operational risk through the **Operational Risk** column on the 'SBOM' page. Hover over a risk in the inventory table for details. The expanded card’s **Details** tab provides comprehensive details. Additionally, the [Application Graph](/content-collections/application-security/visibility/repositories.md#app-graph) on the 'Repositories' page displays package Operational Risks. You can also filter by Operational Risk, Popularity and Maintenance for targeted searches.

## AI/ML Open Source Packages

Prisma Cloud identifies AI/ML functionalities within JavaScript and Python open-source packages used in your codebase. It then leverages this information to build a comprehensive inventory of the machine learning packages in your environment, allowing you to make informed security decisions and effectively mitigate associated risks.

The SBOM table includes an **AI/ML Categories** column, displaying the associated AI/ML categories for each relevant package. The **Details** sidecar provides additional information about the AI/ML categories utilized by that package.

### Filter by AI/ML Category

The **AI/ML Category** filter lets you choose specific categories like deep learning or natural language processing. By selecting a category, you’ll get a focused view of the packages in your project that are associated with that particular AI/ML functionality.

AI/ML Category values include:

* Generative AI
* Artificial Intelligence (AI)
* Machine Learning (ML)
* Deep Learning
* Natural Language Processing (NLP)
* GPT
* OpenAI
* Gemini
* ChatGPT
* Large Language Models (LLM)
* LLaMA
* Neural Network
* Computer Vision
* Data Science
* Reinforcement Learning (RL)

### AI/ML Packages API

The AI/ML Packages API empowers developers and tools to discover AI/ML categories programmatically. This API provides functionalities to retrieve comprehensive information about the AI/ML categories included within software packages used in your environment. For more information refer to the [SBOM](https://pan.dev/prisma-cloud/api/code/sbom/) API documentation.

## Generate SBOM

You can generate a SBOM for you repository. You can choose to generate an SBOM that contains all of the data types in a single file, or you can choose to generate separate SBOMs for each data type. When applying filters, the generated data will only include filtered data.

The following data types are available for SBOM generation:

* All - download all data types in a single file
* Open source packages
* Infrastructure-as Code
* Images

1. In 'Application Security', select **Home** > **Projects > Menu (in the top right corner) > Generate SBOM**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-471f75bac2292c4cb587dfab54ed9161b89263a9%2Fsbom-menu-generate3.1.png?alt=media" alt="sbom menu generate3.1"><figcaption></figcaption></figure>
2. In the popup.
   1. Select a repository.
   2. Select a type of output. Values: CycloneDX, CSV files.
   3. Select a data type.
   4. Click **Generate**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-53d0bc4587068d06094d85b84e211d39b9110caa%2Fsbom-generate-popup3.0.png?alt=media" alt="sbom generate popup3.0"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/application-security/visibility/sbom.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
