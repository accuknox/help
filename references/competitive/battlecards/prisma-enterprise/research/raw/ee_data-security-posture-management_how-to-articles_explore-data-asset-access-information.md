> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information.md).

# Explore Data Asset Access Information

This article describes how to do the following:

* Obtain a comprehensive visibility into cloud IAM principals with access to specific assets.
* Filter access information based on permission types, originating projects, and other crucial criteria such as risk indicators.

### Prerequisites

* This information is calculated by Prisma Cloud CIEM (Cloud Identity and Entitlement Management). In order for access information to be visible in the Prisma Cloud console, the tenant needs to be subscribed both to DSPM and CIEM.

### Access information

Access information is available for the following services:

* AWS
  * S3
  * RDS
  * EFS
  * Aurora
  * OpenSearch
  * DynamoDB
* Azure
  * Storage account
  * NetApp File share
  * SQL Server
  * Azure SQL
  * CosmosDB
* GCP
  * GCS
  * BigTable
  * CloudSQL
  * BigQuery

The access information shows all users and roles who have access to the data asset scope, including access levels (e.g. Read, Write, List and Manage) and public access

This feature is enabled by default, no action is required to enable access information on data assets.

### View asset access details

1. Navigate to the asset whose access details you wish to view.
   1. In Prisma Cloud DSPM, click Inventory.
   2. In Inventory, click the name of the specific asset you want to view.\
      ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-23d0e19fd86c48d37aaedbbbc7dd3a25d02365a6%2Fmedia_184f11f2ae35c51c53abf28f4dd6dff258e81ea35.png?alt=media)
   3. Click the Access tab to view the DAG (data access governance) for the asset.\
      ![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-56ef8ec9cc1fe03ed83cb93b9baab3ca16ec24cb%2Fmedia_1f7b5f7f88d1acacd38b06839da4054ef47991edb.png?alt=media)
2. Use the Access mapping graph or Access list to identify and monitor all the roles and users with access permissions to the asset.

#### Access mapping graph

The access mapping graph opens by default when you click the Access tab.

* Use the mapping graph to instantly view a snapshot of each users’ relationship to the asset.
* View the permissions associated to each identity.
* Mouse hover over the bucket, project, user groups, and roles to view more details about users' access details.

### Access list

In the Access tab click the toggle at the top right to view the access information in list form. (To return to the mapping graph, click the mapping icon.)

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-41428bf8ac307b3aad1716dc0f9b3e3f64dab146%2Fmedia_18a80298511a4e27ee9709da392025a2a676e5e4a.png?alt=media)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
