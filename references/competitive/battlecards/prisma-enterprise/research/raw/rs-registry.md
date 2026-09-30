> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/registry-scanning.md).

# Registry Scanning

Configure Prisma Cloud to scan your registries.

* [Scan images in Sonatype Nexus Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-nexus.md)
* [Scan images in Alibaba Cloud Container Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-alibaba.md)
* [Scan images in Amazon Elastic Container Registry (ECR)](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-ecr.md)
* [Scan images in Azure Container Registry (ACR)](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-acr.md)
* [Scan images in Docker Registry v2](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-docker.md)
* [Scan Images in GitLab Container Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-gitlab.md)
* [Scan images in Google Artifact Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-gar.md)
* [Scan images in Google Container Registry (GCR)](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-gcr.md)
* [Scan images in Harbor Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-harbor.md)
* [Scan images in IBM Cloud Container Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-ibm.md)
* [Scan images in JFrog Artifactory Docker Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-artifactory.md)
* [Scan Images in OpenShift integrated Docker Registry](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-openshift.md)
* [Scan Images in CoreOS Quay](/content-collections/runtime-security/vulnerability-management/registry-scanning/scan-coreos-quay.md)
* [Trigger Registry scans with webhooks](/content-collections/runtime-security/vulnerability-management/registry-scanning/webhooks.md)


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/vulnerability-management/registry-scanning.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
