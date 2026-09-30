> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/overview.md).

# Overview

This page displays a high-level overview of your monitored environment.

**Key:**

1. All the assets automatically discovered by Prisma Cloud DSPM in the last 30 days, and a breakdown of assets per platform.
2. A dashboard displaying the data security posture score and top risks.
3. The number of exposed issues and a short description about the exposed sensitive records.
4. The number of assets with data footprint issues including a short description about the assets.
5. The number of all sensitive records with DDR protection and a shortcut to improve the protection.
6. The number of open alerts and a shortcut to view the alert history.
7. A synopsis of the top assets most at risk.
8. An activity log.

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-ce7a78eb1626664467f9eeacf537ba8717e8d6ed%2Fmedia_1c2b614e11c11ea69115cc8ed7791cc0576193efa.png?alt=media)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/overview.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
