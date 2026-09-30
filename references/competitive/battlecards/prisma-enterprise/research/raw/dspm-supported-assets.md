> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/supported-assets.md).

# Supported Assets

The Prisma Cloud Data Security Posture Management (DSPM) solution, previously known as Dig Security platform, helps you discover, classify, protect, and govern your data across multi-cloud environments. With Prisma Cloud DSPM, you can reduce data misuse, achieve compliance, and prevent ransomware attacks and data breaches.

Prisma Cloud offers data classification for the following assets and services.

* **AWS**
  * Storage: Simple Storage Service (S3), and Elastic File System (EFS)
  * Databases: Aurora, RDS (MySQL, MariaDB, PostgreSQL), OpenSearch (Serverless), DynamoDB, and Unmanaged Database instances (database running on AWS EC2)
  * Analytics: Redshift (standard deployment only)
* **Azure**
  * Storage: Blob Storage and NetApp Files
  * Databases: SQL Server, Azure SQL, CosmosDB (NoSQL and MongoDB), and Unmanaged SQL instances

For CosmosDB, only public instances scanning is supported. For SQL Managed Instance, customer-managed TDE is not supported.

* **GCP**
  * Storage: Cloud Storage
  * Databases: Cloud BigTable, Cloud SQL (MySQL, PostgreSQL, SQL Server), and Unmanaged Database instances
  * Analytics: BigQuery
* **DBaaS**
  * Snowflake
* **SaaS**
  * Microsoft Office 365 (OneDrive and Sharepoint Sites)
* **Unmanaged Databases** (hosted on VMs)
  * PostgreSQL (Linux only)
  * MongoDB
  * MySQL
  * MariaDB
  * MSSQL

Prisma Cloud DSPM metering depends on the type of data assets being secured:

* For IaaS and PaaS assets, DSPM requires 1 credit per data asset.
* For DBaaS assets, DSPM requires 1 credit per TB of data volume (i.e. size of the data asset).
* For SaaS assets, DSPM requires 0.1 credit per user in supported SaaS applications.

While the above list refers to only data classification, Prisma Cloud discovers and monitors most cloud assets and services for usage and misconfigurations.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/supported-assets.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
