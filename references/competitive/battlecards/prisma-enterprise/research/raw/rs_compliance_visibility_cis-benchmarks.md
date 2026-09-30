> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/compliance/visibility/cis-benchmarks.md).

# CIS Benchmarks

The CIS Benchmarks provide consensus-oriented best practices for securely configuring systems. Prisma Cloud provides checks that validate the recommendations in the following CIS Benchmarks:

* [Docker Benchmark](https://www.cisecurity.org/benchmark/docker/)
* [Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/)
* [Openshift Benchmark](https://www.cisecurity.org/insights/blog/cis-benchmarks-march-2021-update)
* [Distribution Independent Linux](https://workbench.cisecurity.org/)
* [Amazon Web Services Foundations](https://www.cisecurity.org/benchmark/amazon_web_services/)
* [GKE Benchmark (only for worker nodes checks)](https://workbench.cisecurity.org/benchmarks/11806s/)
* [Amazon Elastic Kubernetes Service (EKS) Benchmark v1.2.0](https://workbench.cisecurity.org/benchmarks/9058/)
* [Azure Kubernetes Service (AKS) Benchmark v1.2.0](https://workbench.cisecurity.org/benchmarks/9681/)

We have graded each check using a system of four possible scores: critical, high, medium, and low. This scoring system lets you create compliance rules that take action depending on the severity of the violation. If you want to be reasonably certain that your environment is secure, you should address all critical and high checks. By default, all critical and high checks are set to alert, and all medium and low checks are set to ignore. We expect customers to review, but probably never fix, medium and low checks.

There are just a handful of checks graded as critical. Critical is reserved for things where your container environment is exposed to the Internet, and can result in a direct attack by somebody on the outside. They should be addressed immediately.

Prisma Cloud has not implemented CIS checks marked as *Not Scored*. These checks are are hard to define in a strict way. Other checks are might not implemented because the logic is resource-heavy, results depend on user input, or files cannot be parsed reliably.

## Additional details about Prisma Cloud’s implementation of the CIS benchmarks

The compliance rule dialog provides some useful information. Compliance rules for containers can be created under **Defend > Compliance > Containers and Images**, while compliance rules for hosts can be created under **Defend > Compliance > Hosts**.

**Benchmark versions** — To see which version of the CIS benchmark is supported in the product, click on the **All types** drop-down list.

**Grades** — To see Prisma Cloud’s grade for a check, see the corresponding **Severity** column.

* High
* Medium
* Low

**Built-in policy library** — To enable the checks for the PCI DSS, HIPAA, NIST SP 800-190, and GDPR standards, select the appropriate template.

## Notes on the CIS OpenShift benchmark

When Prisma Cloud detects OpenShift Container Platform (OCP) 4, we assess the cluster against the CIS OpenShift benchmark. Prisma Cloud supports the CIS OpenShift benchmark on OCP 4.6 and later.

The following checks from the CIS OpenShift benchmark haven’t been implemented:

* 1.2.7 - Ensure that the --authorization-mode argument is not set to AlwaysAllow.
* 1.2.10 - Ensure that the APIPriorityAndFairness feature gate is enabled.
* 1.2.11 - Ensure that the admission control plugin AlwaysAdmit is not set.
* 1.2.16 - Ensure that the admission control plugin SecurityContextConstraint is set.
* 1.2.21 - Ensure that the healthz endpoint is protected by RBAC.
* 1.2.23 - Ensure that the audit logs are forwarded off the cluster for retention.
* 1.2.33 - Ensure that the --encryption-provider-config argument is set as appropriate.
* 1.2.34 - Ensure that encryption providers are appropriately configured.
* 1.2.35 - Ensure that the API Server only makes use of Strong Cryptographic Ciphers.
* 1.3.1 - Ensure that garbage collection is configured as appropriate.
* 1.3.2 - Ensure that controller manager healthz endpoints are protected by RBAC.
* 1.4.1 - Ensure that the healthz endpoints for the scheduler are protected by RBAC.
* 1.4.2 - Verify that the scheduler API service is protected by authentication and authorization.
* 3.1.1 - Client certificate authentication should not be used for users.
* 3.2.2 - Ensure that the audit policy covers key security concerns.
* 4.2.2 - Ensure that the --authorization-mode argument is not set to AlwaysAllow.
* 4.2.7 - Ensure that the --make-iptables-util-chains argument is set to true.
* 4.2.8 - Ensure that the --hostname-override argument is not set.
* 4.2.9 - Ensure that the kubeAPIQPS \[--event-qps] argument is set to 0 or a level which ensures appropriate event capture.
* 4.2.13 - Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers.
* Section 5 - Policies.

Prisma Cloud now supports OpenShift CIS Benchmark v1.3.0.

When updating the OpenShift CIS benchmark from v1.1.0 to v1.3.0, configure your clusters to follow the 600 permissions compliance instead of the 644. If you have configured a blocking action, change the action to alert until your clusters follow the new 600 compliance. Sign in to the [CIS website](https://workbench.cisecurity.org/) to review the details of the OpenShift 1.30 benchmarks.

## Notes on the CIS Distribution Independent Linux benchmark

Prisma Cloud hasn’t implemented the following checks from the CIS Distribution Independent Linux benchmark:

* *1.7.2 - Ensure GDM login banner is configured* — By default, most server distributions ship without a windows manager. A manual assessment is required.
* *2.2.1.2 - Ensure ntp (Network Time Protocol) is configured* — CIS did not score this recommendation. A manual assessment is required.
* *2.2.1.3 - Ensure chrony is configured* — CIS did not score this recommendation. A manual assessment is required.
* *5.3.1 - Ensure password creation requirements are configured* — This recommendation cannot be implemented generically because password requirements vary from organization to organization. A manual assessment is required.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/compliance/visibility/cis-benchmarks.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
