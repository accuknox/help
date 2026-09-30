> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-amazon-security-lake.md).

# Integrate Prisma Cloud with Amazon Security Lake

Learn how to integrate Prisma Cloud with Amazon Security Lake.

Amazon Security Lake offers a comprehensive view of security data across sources of your choice in your cloud and on-premises environments. Prisma Cloud delivers security intelligence to Amazon Security Lake using the Open Cybersecurity Schema Framework (OCSF) standard. Integrating Prisma Cloud with Amazon Security Lake helps you protect your cloud workloads, applications, and data with greater visibility and context into cloud security issues.

1. Log in to Prisma Cloud.
2. Select **Settings > Integrations & Notifications > Integrations**.
3. Select **Add Integration > Amazon Security Lake**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-644699a09719726d8e00ff46715ce6b2fa9bfbce%2Fintegrate-amazon-security-lake-1.png?alt=media" alt="integrate amazon security lake 1"><figcaption></figcaption></figure>
4. Enter the details of the Amazon Security Lake S3 bucket.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a37adfefddac80edbdbb3730a694ec9405502445%2Fintegrate-amazon-security-lake-2.png?alt=media" alt="integrate amazon security lake 2"><figcaption></figcaption></figure>

   1. Enter an **Integration Name** and (optional) **Description**.
   2. Enter the **AWS Region** in which you created the S3 bucket.
   3. Enter the **Role ARN** of the IAM role.
   4. Enter **S3 URI** for the S3 bucket or folder path in the format: `s3://bucketname/` or `s3://bucketname/foldername/`.
   5. **Generate** the **External ID** to associate it with the IAM role which is required for Prisma Cloud to be able to write notifications to the S3 bucket.
   6. Click **Next**.
5. Review the **Summary** and then **Test Integration**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-db992c1858b0c7de5536ec9479b0d4085a587dcb%2Fintegrate-amazon-security-lake-3.png?alt=media" alt="integrate amazon security lake 3"><figcaption></figcaption></figure>
6. **Save** and **Close** after the testing is successful.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-c23ae78a434c1f0bf2c4adac71ed2781625efcff%2Fintegrate-amazon-security-lake-4.png?alt=media" alt="integrate amazon security lake 4"><figcaption></figcaption></figure>

You should receive a success message and a test message should be posted to your S3 bucket. The integration will be listed on the **Integrations** page, where you can **View**, **Edit**, or **Delete** the integration from the **Actions** panel.

Navigate to the S3 bucket in your AWS environment. You should be able to see the findings sent to the S3 bucket in the parquet format.

Prisma Cloud allows only one Security Lake integration at a time. From Prisma Cloud, only **Host vulnerability findings** are written in to Security Lake.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-amazon-security-lake.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
