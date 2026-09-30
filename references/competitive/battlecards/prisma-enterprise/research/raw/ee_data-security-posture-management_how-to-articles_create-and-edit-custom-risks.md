> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/create-and-edit-custom-risks.md).

# Create and edit custom risk rules

This article describes how to do the following:

* Create custom risk rules from any search in the inventory and save them.
* Edit the severity of risk rules and disable out-of-the-box (OOB) risk rules as needed.
* Manage and distinguish between custom and system-generated risk rules.

### Create a custom risk rule

There are two options to create a custom risk:

**Option 1:**

In Prisma Cloud DSPM, click Inventory to open the Inventory window, and then proceed to step 4 below.

**Option 2:**

1. In Prisma Cloud DSPM, click Risks. The Risks Overview tab opens by default.

   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-feaec84a9306ebb24613588c45c51994fd155db2%2Fmedia_19397a76712ec0c3e6b779c69454ac84a33016f47.png?alt=media)
2. In the Custom Risk thumbnail click Create.
3. In the pop-up, click Go to Inventory to open the Inventory window.
4. In the custom risk rules field, specify the rules for the custom risk. For example, create a custom risk to view developer secrets that are open to the world.

   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-8e2f84bd56271369a9d8745c62eb7445af562102%2Fmedia_10c78350649365c0a934abd5053d95aa94a8d5529.png?alt=media)
5. Click Create Custom Risk.

   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-ea84b143d01fabbf59835fe203664be1241b2b03%2Fmedia_1560fc32ca190b398c5568e9b1936b1ad7f608104.png?alt=media)
6. In the New Custom Risk drawer, do the following:
   1. Give a meaningful name to the risk.
   2. Enter a description for the risk.
   3. Specify the severity of the risk.
   4. Specify if the risk affects security and/or compliance.
   5. Click Create to create the custom risk. Note that it takes approximately 15-minutes for Prisma Cloud DSPM to identify the risk findings associated with the new custom risk.

      ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-64e335ce5e50a7a678b2e5fda78699f79cb7eeaf%2Fmedia_14bceb92fb37432d75b91278c1320fe35f902da98.png?alt=media)
7. After creating a custom risk, its thumbnail appears in the Risks Overview tab.
   * A custom risk thumbnail is denoted by the word Custom to distinguish it from out-of-the-box risks.\
     ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a9db06623074e987a38d0b8e82df1d53f845627e%2Fmedia_1011f6252b9de8c65f00f0d30a370bd006e23df09.png?alt=media)
   * The number on the thumbnail indicates the number of risk findings associated with the custom risk rules.

### Edit a custom risk rule

1. In Prisma Cloud DSP side menu, click Risks. The Risks Overview tab opens by default.
2. Navigate to the custom risk you want to edit.
3. Click the Settings icon, located at the top right of the thumbnail, to open the custom risk’s drawer.

   ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a47e4860d78db1fb5a89394b8768e8b5c70aea63%2Fmedia_1975f2d8369e2d21cb203b1622e33d62b064078ae.png?alt=media)
4. Edit the custom risk as required. For example, change the severity level, or stop creating risk findings for the custom rule.
5. Click Save.

### Delete a custom risk

1. In Prisma Cloud DSPM, click Risks. The Risks Overview tab opens by default.
2. Navigate to the custom risk you want to delete.
3. Click the Settings icon, located at the top right of the thumbnail, to open the custom risk’s drawer.
4. In the custom risk drawer, click Delete this risk.
5. When prompted, click Remove. The custom risk is deleted from Prisma Cloud DSPM.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/create-and-edit-custom-risks.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
