For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information.md).

This article describes how to do the following:

- Obtain a comprehensive visibility into cloud IAM principals with access to specific assets.

- Filter access information based on permission types, originating projects, and other crucial criteria such as risk indicators.


### Prerequisites[Direct link to heading](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information\#prerequisites)

- This information is calculated by Prisma Cloud CIEM (Cloud Identity and Entitlement Management). In order for access information to be visible in the Prisma Cloud console, the tenant needs to be subscribed both to DSPM and CIEM.


### Access information[Direct link to heading](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information\#access-information)

Access information is available for the following services:

- AWS





  - S3

  - RDS

  - EFS

  - Aurora

  - OpenSearch

  - DynamoDB


- Azure





  - Storage account

  - NetApp File share

  - SQL Server

  - Azure SQL

  - CosmosDB


- GCP





  - GCS

  - BigTable

  - CloudSQL

  - BigQuery


The access information shows all users and roles who have access to the data asset scope, including access levels (e.g. Read, Write, List and Manage) and public access

This feature is enabled by default, no action is required to enable access information on data assets.

### View asset access details[Direct link to heading](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information\#view-asset-access-details)

1. Navigate to the asset whose access details you wish to view.





1. In Prisma Cloud DSPM, click Inventory.

2. In Inventory, click the name of the specific asset you want to view.
      ![](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F3990409212-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FyqPwsbMSaogAot23rTIu%252Fuploads%252Fgit-blob-23d0e19fd86c48d37aaedbbbc7dd3a25d02365a6%252Fmedia_184f11f2ae35c51c53abf28f4dd6dff258e81ea35.png%3Falt%3Dmedia&width=300&dpr=3&quality=100&sign=2bef35e9a79e646648270f21f1642e82&sv=3)

3. Click the Access tab to view the DAG (data access governance) for the asset.
      ![](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F3990409212-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FyqPwsbMSaogAot23rTIu%252Fuploads%252Fgit-blob-56ef8ec9cc1fe03ed83cb93b9baab3ca16ec24cb%252Fmedia_1f7b5f7f88d1acacd38b06839da4054ef47991edb.png%3Falt%3Dmedia&width=300&dpr=3&quality=100&sign=d5f9a50bed413574a3b3463f86775ad4&sv=3)


2. Use the Access mapping graph or Access list to identify and monitor all the roles and users with access permissions to the asset.


#### Access mapping graph[Direct link to heading](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information\#access-mapping-graph)

The access mapping graph opens by default when you click the Access tab.

- Use the mapping graph to instantly view a snapshot of each users’ relationship to the asset.

- View the permissions associated to each identity.

- Mouse hover over the bucket, project, user groups, and roles to view more details about users' access details.


### Access list[Direct link to heading](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/explore-data-asset-access-information\#access-list)

In the Access tab click the toggle at the top right to view the access information in list form. (To return to the mapping graph, click the mapping icon.)

![](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F3990409212-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FyqPwsbMSaogAot23rTIu%252Fuploads%252Fgit-blob-41428bf8ac307b3aad1716dc0f9b3e3f64dab146%252Fmedia_18a80298511a4e27ee9709da392025a2a676e5e4a.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6d2e038fe4be9cd09685b1c2580d20c3&sv=3)

[PreviousCreate and edit custom risk rules](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/create-and-edit-custom-risks) [NextMonitor and Identify AWS Activities](https://docs.prismacloud.io/content-collections/data-security-posture-management/how-to-articles/monitor-and-identify-aws-activities)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject