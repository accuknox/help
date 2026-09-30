> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/compliance/custom-compliance-standard.md).

# Create a Custom Compliance Standard

You can create your own custom compliance standards that are tailored to your own business needs, standards, and organizational policies. When defining a custom compliance standard, you can add requirements and sections. A custom compliance standard that has a minimum of one requirement and one section can be associated with policies that check for adherence to your standards.

You can create an all new standard or clone an existing compliance standard and edit it.

1. Clone an existing compliance standard to customize.
   1. On Prisma Cloud, select **Compliance > Standards**.
   2. Hover over the standard you want to clone, and click **Clone**.

      When you clone, it creates a new standard with the same name with Copy in the prefix. You can then edit the cloned compliance standard to include the requirements, sections, and policies you need.
2. Create a compliance standard from scratch.
   1. On Prisma Cloud, select **Compliance > Standards > + Add New**.
   2. Enter a name and description for the new standard and select **Save**.
   3. Add requirements to your custom compliance standard.
      1. Select the custom compliance standard you just added and click **+ Add New**.
      2. Enter a requirement, name and a description and select **Save**.
   4. Add sections to your custom compliance standard after adding the requirement.
      1. Select the requirement for which you are adding the section and click **+ Add New**.
      2. Enter a name for the **Section** a **Description** and select **Save**.

         Although you have added the custom standard to Prisma Cloud, it is not listed on the Compliance Standards table on **Compliance > Overview** until you add at least one policy to it.
   5. Add policies to your custom compliance standard.

      You must associate Prisma Cloud Default policies or your custom policies to the compliance standard to monitor your cloud resources for adherence to the internal guidelines or benchmarks that matter to you. The RQL in the policy specifies the check for the resource configuration, anomaly or event.

      1. Select **Policies**.

         Filter the policies you want to associate with the standard. You can filter by cloud type, policy type and policy severity, to find the rules you want to attach.
      2. Select the policy rule to edit, on **3 Compliance Standards** select **+** and associate the policy with the custom compliance standard.
      3. **Confirm** your changes.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/compliance/custom-compliance-standard.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
