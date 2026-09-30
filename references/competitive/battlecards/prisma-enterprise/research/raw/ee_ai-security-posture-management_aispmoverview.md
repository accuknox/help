> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview.md).

# AI-SPM Overview

AI-SPM provides a comprehensive overview of the AI assets within an organization. It is designed to ensure AI security by offering tools to review and prioritize AI risks effectively.

**AI-SPM Overview Page**\
The AI-SPM Overview page serves as the central hub for information on the AI ecosystem within the organization. It provides a comprehensive overview of AI security posture and is designed to help users quickly access relevant information. The page’s layout and organization are tailored to guide users in understanding the AI environment and determining the next steps to take for effective AI management.

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-ad72d30e06f87b6f5867c12e4ef1d00844e18e73%2Fmedia_10540726a1a565847f39fa83bea8d74559632bed1.png?alt=media)

The icons on the left (Model Endpoints, Inference Datasets, Training Datasets, and Plugins), allow you to filter and view specific categories of assets and findings relating to different components of the AI ecosystem.\
Clicking "View Training Datasets" reveals all training datasets and their data types, while "View Inference Datasets" displays all inference datasets and their data types. Additionally, selecting "View All" in the "Top AI Assets at Risk" section takes you to the AI Assets page sorted by risks.\
The AI risk findings by severity section shows the number of findings categorized by their severity, giving you a clear understanding of the risk landscape in your AI environment.

**AI Assets Inventory**

The AI Asset Inventory page allows for viewing all AI assets in your environment, regardless of deployment mode or cloud provider. Connected assets are discovered, contextualized, and presented with detailed information. To dive deeper into the asset context, click on the asset name to navigate to the AI Asset page.

**AI Risks**

AI-SPM provides risk assessment for the supported AI assets, with risk rules crafted by the Prisma Cloud research team. These risk rules are designed to detect misconfigurations and security flaws in AI assets and alert on them. In addition to the default risk rules, AI-SPM also supports custom risk rule creation - allowing organizations to codify and integrate internal policies into the AI-SPM risk engine, streamlining remediation efforts. In order to create a custom risk rule, enter the rule definition as a query in the AI-SPM inventory, and click ‘Create custom risk’.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/ai-security-posture-management/aispmoverview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
