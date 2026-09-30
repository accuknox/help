> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/risks.md).

# Risks

This Risks page has two tabs:

* **Overview** - an overview of all the risks associated with all the assets in your environment, sorted by risk type, category and severity.\
  ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c6aa8fc94f171a505f76c58c126e52e5b4f78e35%2Fmedia_16a1adf2a79d46e01868026c93b863f97328bcfda.png?alt=media)
* **Findings** - displays further information on each risk, such as the assets it was detected in and labels associated with it. Clicking on a risk from the **Overview** display takes you to its own **FIndings** page.\
  ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f943f286c20294aa7b99cd5fbfadcdbfb546c573%2Fmedia_165aa2e080e48d206da9fc94f6fa954880c5e37b2.png?alt=media)

From the risk’s **Findings** page, you can click on the risk name to get its full info, such as the compliance regulations it violates; or click on the asset to go to its **Asset Page**.

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-20b98c13147bd1569df72b0bc03d1915e3ad24c1%2Fmedia_15085a8c6851327d9a3cbe9b110a20e31e4c1bec6.png?alt=media)

Filtering and saving Views in the **Risks** page is similar to previous pages.

Refer to the article Assess Your Posture with Various Standards and Regulations to learn about compliance standards.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/risks.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
