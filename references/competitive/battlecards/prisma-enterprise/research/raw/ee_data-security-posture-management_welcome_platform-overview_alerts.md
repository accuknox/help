> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/alerts.md).

# Alerts

The Alerts page provides an overview of all the alerts in your environment.

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-aa4f7691f92e078f5bff5d576542b877d86d0468%2Fmedia_1a7fbcf779f15692afb4075dd6634ddc6f3cae5b3.png?alt=media)\
The **Alerts** page includes open, in-progress and handled alerts, as well as alerts that were marked as Wrong or Unimportant. You can change an alert’s status from the **Status** column.\
![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-7f481122ddd425923c7e5b2452f951c06c214c8f%2Fmedia_14bcab6b983040a7e536093a7fcca508cca5f5414.png?alt=media)\
The details provided for each alert include the cloud and asset it was detected in, its severity, its category (the DDR policy it violates), and more. Click on an alert’s row to view additional information.

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-bf165d028febe369de40a550b6895e97a646b066%2Fmedia_16f69d4053a45f63e139b78820f8b87fa083d3a22.png?alt=media)

Filtering and saving Views in the **Alerts** page is similar to previous pages.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/alerts.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
