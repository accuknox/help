> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/use-cases.md).

# Use Cases

To automatically discover all resources across all cloud services and deployment types, Prisma Cloud DSPM utilizes a distinctive technology for each deployment type.

## Managed Assets

These assets are managed by the cloud provider (S3, RDS, Azure SQL, etc.) and are conducted by cloud-native APIs. Prisma Cloud DSPM receives authorization from an IAM to utilize the APIs in the customer environment. The credentials used for managed asset discovery are strictly **read only**.

## Unmanaged Assets

These assets (e.g., MongoDB installed on a VM) are identified by scanning relevant volumes and looking for DB engine fingerprints and configurations. Prisma Cloud DSPM conducts the scan by deploying Orchestrator in the client’s environment (see System Components for an elaboration on Prisma Cloud DSPM’s Orchestrator). Orchestrator is deployed securely, protected from any external access, and restricted by IAM permissions. After all data is scanned, analyzed and processed, the only data that leaves the client’s environment is DB metadata, including misconfigurations. Orchestrator’s permissions are granted during onboarding via a simple script utilizing cloud-native APIs (e.g., Hashicorp Terraform, AWS cloudFormation, and AWS ARM templates). It also offers a least-privilege access corresponding to Prisma Cloud DSPM’s capabilities.

## DBaaS

This service (e.g., Snowflake connected to the client’s cloud account) is carried out by read-only permissions and APIs that analyze the connectivity status and data flows in and out of the external DB.

## Data Classification

To keep the client’s data safe, Prisma Cloud DSPM contextualizes and classifies data within the client’s environment via Orchestrator. The only data that leaves the client’s environment includes detected classifiers, the file names in which they were detected, and the number of matches for each classifier.

* Classification is performed via Prisma Cloud DSPMs proprietary engine, which includes pre-defined classifiers with contextual capabilities for minimizing the false-positive rate.
* Clients can also add their own customized classifiers.
* Prisma Cloud DSPM can analyze and classify both structured (e.g., RDS MySQL, Aurora, Postgresql) and unstructured data (e.g., S3 buckets, Blob storages) assets.
* Classification of any type does not require a connection to the DB, and is carried out through replicas of data stores, without affecting production or any other workload.

## Data Security Posture Management (DSPM)

Data security posture management (DSPM) is a set of practices and technologies used to assess, monitor, and reduce the risk related to data residing in cloud data stores – with a focus on multi-cloud environments. DSPM is data-centric: it looks at the context and content of the data being protected, placing the focus on sensitive records such as PII or medical records. Thus, it enables the client to prioritize their data assets’ most critical configurations, risks and usage by: \* Fixing data misconfigurations to lower the overall risk of an attack \* Tightening access permissions to reduce data exposure \* Accelerating assessments of how data security posture is enforced, thus involving data owners in decisions directly related to data access

## Detection and Response (DDR)

### Overview

The term DDR describes a set of technology-enabled solutions used to secure cloud data from exfiltration. DDR focuses on real-time monitoring, detection, and response. It provides dynamic monitoring on top of the static defense layers provided by DSPM tools. DDR solutions use real-time log analytics to monitor cloud environments that store data, and detect data risks as soon as they occur. Prisma Cloud DSPM leverages cloud-native logging capabilities, as well as its proprietary detection engine, to carry out DDR in near-real time (< 15 minutes detection time). This requires enabling cloud-native logging for protected projects (e.g., CloudTrail for AWS accounts, Activity Logs for Azure subscriptions, etc.) and enabling accessibility to Prisma Cloud DSPM. Prisma Cloud DSPM supports the following log configuration options: \* **Local logging** – logs stored locally on the actual monitored project \* **Centralized logging** – the logs for all monitored projects stored in a single monitored project The logs are collected and analyzed in Prisma Cloud DSPMDig’s own cloud environment.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/welcome/use-cases.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
