For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/supported-assets.md).

The Prisma Cloud Data Security Posture Management (DSPM) solution, previously known as Dig Security platform, helps you discover, classify, protect, and govern your data across multi-cloud environments. With Prisma Cloud DSPM, you can reduce data misuse, achieve compliance, and prevent ransomware attacks and data breaches.

Prisma Cloud offers data classification for the following assets and services.

- **AWS**





  - Storage: Simple Storage Service (S3), and Elastic File System (EFS)

  - Databases: Aurora, RDS (MySQL, MariaDB, PostgreSQL), OpenSearch (Serverless), DynamoDB, and Unmanaged Database instances (database running on AWS EC2)

  - Analytics: Redshift (standard deployment only)


- **Azure**





  - Storage: Blob Storage and NetApp Files

  - Databases: SQL Server, Azure SQL, CosmosDB (NoSQL and MongoDB), and Unmanaged SQL instances


For CosmosDB, only public instances scanning is supported. For SQL Managed Instance, customer-managed TDE is not supported.

- **GCP**





  - Storage: Cloud Storage

  - Databases: Cloud BigTable, Cloud SQL (MySQL, PostgreSQL, SQL Server), and Unmanaged Database instances

  - Analytics: BigQuery


- **DBaaS**





  - Snowflake


- **SaaS**





  - Microsoft Office 365 (OneDrive and Sharepoint Sites)


- **Unmanaged Databases** (hosted on VMs)





  - PostgreSQL (Linux only)

  - MongoDB

  - MySQL

  - MariaDB

  - MSSQL


Prisma Cloud DSPM metering depends on the type of data assets being secured:

- For IaaS and PaaS assets, DSPM requires 1 credit per data asset.

- For DBaaS assets, DSPM requires 1 credit per TB of data volume (i.e. size of the data asset).

- For SaaS assets, DSPM requires 0.1 credit per user in supported SaaS applications.


While the above list refers to only data classification, Prisma Cloud discovers and monitors most cloud assets and services for usage and misconfigurations.

[PreviousSystem Components](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/system-components) [NextPlatform Overview](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/platform-overview)

Last updated 4 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject