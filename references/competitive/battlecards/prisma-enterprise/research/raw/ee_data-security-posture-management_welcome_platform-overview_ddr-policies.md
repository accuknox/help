> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/ddr-policies.md).

# DDR Policies

Prisma Cloud DSPM provides an out-of-the-box set of DDR policies that is continuously being integrated into the platform by our team of experienced data researchers. The policy categories currently supported are:

* First Move
* Attack
* Compliance

The **Policies** page displays an overview of the active policies in the environment. An explanation of the different policy categories is also available from this page - simply click on the category's name.

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-93c462891d249129a7097f758fe83e284a720f2c%2Fmedia_19f09bafad5b318983d5eea949833da8832c6e7da.png?alt=media)

For each policy, you can navigate to the **Open Alerts** associated with this policy by clicking on the number in the **Open Alerts** column. This takes you to the Alerts page.

From the **Actions** column, you can disable or enable a selected policy.

![policies\_actions.png](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-54ed0fc799c2d4ab592a175dc7808d35d31df16a%2Fmedia_1db3034ab463c94c5795d21a35242400740998160.png?alt=media)

Filtering and saving Views in the **DDR Policies** page is similar to previous pages.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview/ddr-policies.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
