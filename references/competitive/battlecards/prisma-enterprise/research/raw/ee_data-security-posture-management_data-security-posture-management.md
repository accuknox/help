> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/data-security-posture-management/data-security-posture-management.md).

# Data Security Posture Management

**Prisma Cloud DSPM**  is an agentless, multi-cloud, data security platform that discovers, classifies, protects, and governs sensitive data. As more and more organizations shift to manage their data assets in the cloud, this process requires implementation of better data monitoring capabilities. Prisma Cloud DSPM's mission is to provide organizations with such capabilities, in order to ensure complete visibility and real-time control over potential security risks to their data.

Prisma Cloud DSPM Overview Page

![](https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-b450dfdf6edeb2645950955a476e1502fc9c2f2b%2Fmedia_1f109ba83dfd4ed673e4fa4e14d5fcb3c2bc0f447.png?alt=media)

### Capabilities

As a cloud-native data security solution, Prisma Cloud DSPM utilizes several technologies to discover, contextualize, monitor, and protect the client’s cloud data assets in real time. Prisma Cloud DSPM collects data from a variety of cloud deployments and data servers - both managed (e.g., buckets, file storage, databases) and unmanaged (e.g., MongoDB and MySQL running on virtual machines). The platform also discovers data analytic environments (DBaaS) such as Snowflake, offering you a complete data landscape view.

By using cloud-native APIs and methods, Prisma Cloud DSPM collects the metadata of the monitored assets and administrative logs, e.g., CloudTrail, activity logs and audit logs. Using this information, Prisma Cloud DSPM can detect and remediate the following issues or risks:

* **Shadow data**  - for example, database snapshots and backups created by development teams as they make changes to files or move them around the cloud. This kind of “shadow data” is not protected by existing data governance frameworks, and security teams often do not even not know it exists, even though it may contain sensitive information.
* **Compliance violations**  - the flexibility of cloud infrastructure makes it harder for organizations to stay compliant with security regulations such as HIPAA, GDPR, PCI, etc. - and to be able to prove it to auditors. Prisma Cloud DSPM provides compliance teams with an easy way to classify data under these regulations and ensure it is handled properly, and intervene in case a violation is detected.
* **Data exfiltration or theft**  - Prisma Cloud DSPM enables organizations to easily detect exposures in the data element layer and limit access to them in a way that prevents cybersecurity attacks and data breaches.
* **Ransomware**  - Prisma Cloud DSPM’s real-time threat detection tools enable organizations to stop ransomware attacks early in the kill chain.
* **Data misuse**  - while typically not malicious, data misuse can lead to unintentional data compromise. Prisma Cloud DSPM can prevent that by enforcing security policies across multi-cloud architectures, which prevents users and developers from storing files in inappropriate places.

### Benefits

Using Prisma Cloud DSPM’s data detection and security capabilities enables you to:

* Discover and visualize all your data assets across the different cloud services, which will help you understand where the sensitive data is, how it is used and how it is moving across the organization.
* Reduce the attack surface on your sensitive data by identifying and eliminating the data threat vector early in the kill chain.
* Protect all of your data in real time.
* Combine different technology sets such as DSPM and DDR capabilities to provide the highest level of data protection. See [Use Cases](https://docs.prismacloud.io/en/enterprise-edition/content-collections/data-security-posture-management/welcome/use-cases) for further elaboration on these capabilities.
* Create a centralized view of all data exposure issues by applying a single policy across multiple cloud deployments.
* Reduce costs by avoiding the use of multiple data security solutions, as Prisma Cloud DSPM's coverage extends across all your cloud data assets - including major cloud providers such as AWS, Azure, GCP, etc. With Prisma Cloud DSPM, you can protect any data asset on any cloud deployment using a single, consolidated policy engine.
* Integrate seamlessly with your existing security workflows to ensure rapid resolution and increased resilience against any data security issue, including integrations with notification and IT tracking platforms such as Slack, email, and Webhooks.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/data-security-posture-management/data-security-posture-management.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
