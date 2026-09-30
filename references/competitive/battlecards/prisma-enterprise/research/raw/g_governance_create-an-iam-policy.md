> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/governance/create-an-iam-policy.md).

# Create an IAM Policy

Prisma Cloud provides the ability to create custom IAM policies to fulfill your organization’s IAM requirements. You can build a new IAM policy based on the `config from iam` RQL query and monitor the identities across your cloud environment.

1. Select **Governance**.
2. Select **Add Policy > IAM**.
3. Enter your policy details—**Policy Name** and **Severity**.

   (Optional) Add a **Description** and **Labels**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-b8b4a8891e0466daca20aa2d0bb1de36ccf09028%2Fiam-excessive-permissions.png?alt=media" alt="iam excessive permissions"><figcaption></figcaption></figure>
4. Check `Use Group/Cloud Service Account as violating resource` if you wish to view alert results on AWS role, Azure service principal or GCP account group.
5. Select **Next** and build your RQL query.

   The default option of **New Search** enables you to build a new RQL query from scratch while **Saved Search** enables you to use a RQL query that you previously saved. For example:

   * `config from iam where source.cloud.service.name = 'iam' and source.cloud.resource.type = 'user' and source.cloud.resource.name = 'my-user'`

     Returns the net effective permissions of a user in your cloud account named *my-user*.
   * `config from iam where grantedby.cloud.entity.type = 'group' AND source.cloud.resource.type = 'user'`

     Lists all effective permissions that have been granted to a user by any AWS IAM group.

     A green check mark displays if you entered a valid query.
6. Select the search button.
7. **Save** the policy.

   After you successfully create your new policy, it displays on the **Policies** page.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d2d9945a045037567d55380f23f383dc129f381c%2Fcreate-an-iam-policy-success.png?alt=media" alt="create an iam policy success"><figcaption></figcaption></figure>
8. Use the **Filter** to search for custom or default (out-of-the-box) policies.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-86acbd6f3a68924d0b3137211a78fa7a60a0ba9f%2Fiam-policy-filter-ootb.png?alt=media" alt="iam policy filter ootb"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/governance/create-an-iam-policy.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
