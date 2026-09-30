> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/get-started/prisma-cloud-platform.md).

# Prisma Cloud Platform

## About Prisma Cloud

Prisma® Cloud ingests and processes data from your cloud environment to help you identify and mitigate security risks such as over privileged identities, and critical vulnerabilities, helping you secure your cloud estate against exploitation by bad actors.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a873fee342c883a76fa63eb226aefb33d29e89de%2Fdarwin-architecture.png?alt=media" alt="darwin architecture"><figcaption></figcaption></figure>

The architecture diagram above outlines how Prisma Cloud helps you Secure your Source Code, Cloud Infrastructure and Runtime environment by:

* Ingesting your data with the Prisma Cloud Ingestion Framework.
* Utilizing external integrations such as Splunk and Jira to read your data and help you track vulnerabilities in your cloud environment.
* The data gathered from multiple sources help Prisma Cloud surface risk and vulnerabilities in your Unified Data Repositories.
* The complete risk picture provided by the Security Data Mesh helps you reach your desired Cloud Outcomes such as risk prioritization and vulnerability management.

## Prisma Cloud Data Flow

To ensure the security of your data and high availability of Prisma Cloud, Palo Alto Networks makes Security a priority at every step. The Prisma Cloud architecture uses Cloudflare for DNS resolution of web requests and for protection against distributed denial-of-service (DDoS) attacks. The network flow diagram below outlines the infrastructure within a region:

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-bb8fcc29f26978e5a4e55969af795d9e4cef21be%2Fuser-flow.png?alt=media" alt="user flow"><figcaption></figcaption></figure>

* When you add a cloud account to Prisma Cloud, the IaaS Integration Services module ingests data from flow logs, configuration logs, and audit logs in your cloud environment over an encrypted connection and stores the encrypted metadata in RDS and Redshift instances within the Prisma Cloud AWS Services module.
* Using the Prisma Cloud administrative console or the APIs you can interact with this data to configure policies, to investigate and resolve alerts, to set up external integrations, and to forward alert notifications.
* The integration service also ingests information from your existing single sign-on (SSO) identity management system and allows you to feed information back into your existing SIEM tools and collaboration and helpdesk workflows.

### Data Redundancy and Security

To ensure optimal data redundancy of stateful components (RDS, Redshift) and stateless components (application stack, Redis (used as cache)), Prisma Cloud uses native AWS capabilities for automated snapshots in addition to data retention in S3 buckets using automation scripts. The following measures are taken to secure data through every stage of the application:

* Snapshots and other data at rest are secured using AWS Key Management Service (KMS) to encrypt and decrypt the data.
* Data in transit is secured, by terminating the TLS connection at the Elastic Load Balancer (ELB) and securing traffic between components within the data center using an internal certificate. This ensures that data in transit is encrypted using SSL.
* For workload isolation and micro segmentation, the built-in VPC security controls in AWS securely connect and monitor traffic between application workloads on AWS.

## Agent Environment Network Flow

Prisma Cloud also offers the Compute edition to help you secure your host, containers and serverless workloads. Compute is a self-hosted offering that’s deployed and managed by you.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-df59d338866ea6907c15f72caadf21cd953d75d5%2Fagent-flow.png?alt=media" alt="agent flow"><figcaption></figcaption></figure>

The Compute Console is delivered as a container image that you can run on any host with a container runtime (e.g. Docker Engine). Securing your data is central to our mission, so every application workload is secured using Virtual Private Cloud (VPC) security controls in AWS to secure, control and monitor traffic between application workloads.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/get-started/prisma-cloud-platform.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
