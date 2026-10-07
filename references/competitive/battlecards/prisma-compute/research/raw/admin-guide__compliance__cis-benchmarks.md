For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks.md).

The CIS Benchmarks provide consensus-oriented best practices for securely configuring systems. Prisma Cloud provides checks that validate the recommendations in the following CIS Benchmarks:

- [Docker Benchmark](https://www.cisecurity.org/benchmark/docker/)

- [Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/)

- [Openshift Benchmark](https://www.cisecurity.org/insights/blog/cis-benchmarks-march-2021-update)

- [Distribution Independent Linux](https://www.cisecurity.org/benchmark/distribution_independent_linux/)

- [Amazon Web Services Foundations](https://www.cisecurity.org/benchmark/amazon_web_services/)

- [GKE Benchmark (only for worker nodes checks)](https://workbench.cisecurity.org/benchmarks/11806s/)

- [Amazon Elastic Kubernetes Service (EKS) Benchmark v1.2.0](https://workbench.cisecurity.org/benchmarks/9058/)

- [Azure Kubernetes Service (AKS) Benchmark v1.2.0](https://workbench.cisecurity.org/benchmarks/9681/)


We have graded each check using a system of four possible scores: critical, high, medium, and low. This scoring system lets you create compliance rules that take action depending on the severity of the violation. If you want to be reasonably certain that your environment is secure, you should address all critical and high checks. By default, all critical and high checks are set to alert, and all medium and low checks are set to ignore. We expect customers to review, but probably never fix, medium and low checks.

There are just a handful of checks graded as critical. Critical is reserved for things where your container environment is exposed to the Internet, and can result in a direct attack by somebody on the outside. They should be addressed immediately.

Prisma Cloud has not implemented CIS checks marked as _Not Scored_. These checks are are hard to define in a strict way. Other checks are might not implemented because the logic is resource-heavy, results depend on user input, or files cannot be parsed reliably.

## Additional details about Prisma Cloud’s implementation of the CIS benchmarks[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks\#additional-details-about-prisma-clouds-implementation-of-the-cis-benchmarks)

The compliance rule dialog provides some useful information. Compliance rules for containers can be created under **Defend > Compliance > Containers and Images**, while compliance rules for hosts can be created under **Defend > Compliance > Hosts**.

**Benchmark versions** — To see which version of the CIS benchmark is supported in the product, click on the **All types** drop-down list.

![cis benchmarks versions](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a1a3df5a41be55245e8e2b82a50a88637b25e5c4%252Fcis_benchmarks_versions.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c9ea24f657c78e914955a269442ac7bf&sv=3)

**Grades** — To see Prisma Cloud’s grade for a check, see the corresponding **Severity** column.

![cis benchmarks grades](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-cc8be3c75699bbab57ab5c50d63aebc8ad256f4d%252Fcis_benchmarks_grades.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a281301e4532f33ec41ea192f8cb1c1a&sv=3)

**Built-in policy library** — To enable the checks for the PCI DSS, HIPAA, NIST SP 800-190, and GDPR standards, select the appropriate template.

![cis benchmarks templates](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e61b515079a98a4e81a17e82a6a54ecb1a6f79b1%252Fcis_benchmarks_templates.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=e56be3b962a2df6e8532f28248d70431&sv=3)

## Notes on the CIS OpenShift benchmark[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks\#notes-on-the-cis-openshift-benchmark)

When Prisma Cloud detects OpenShift Container Platform (OCP) 4, we assess the cluster against the CIS OpenShift benchmark. Prisma Cloud supports the CIS OpenShift benchmark on OCP 4.6 and later.

The following checks from the CIS OpenShift benchmark haven’t been implemented:

- 1.2.7 - Ensure that the --authorization-mode argument is not set to AlwaysAllow.

- 1.2.10 - Ensure that the APIPriorityAndFairness feature gate is enabled.

- 1.2.11 - Ensure that the admission control plugin AlwaysAdmit is not set.

- 1.2.16 - Ensure that the admission control plugin SecurityContextConstraint is set.

- 1.2.21 - Ensure that the healthz endpoint is protected by RBAC.

- 1.2.23 - Ensure that the audit logs are forwarded off the cluster for retention.

- 1.2.33 - Ensure that the --encryption-provider-config argument is set as appropriate.

- 1.2.34 - Ensure that encryption providers are appropriately configured.

- 1.2.35 - Ensure that the API Server only makes use of Strong Cryptographic Ciphers.

- 1.3.1 - Ensure that garbage collection is configured as appropriate.

- 1.3.2 - Ensure that controller manager healthz endpoints are protected by RBAC.

- 1.4.1 - Ensure that the healthz endpoints for the scheduler are protected by RBAC.

- 1.4.2 - Verify that the scheduler API service is protected by authentication and authorization.

- 3.1.1 - Client certificate authentication should not be used for users.

- 3.2.2 - Ensure that the audit policy covers key security concerns.

- 4.2.2 - Ensure that the --authorization-mode argument is not set to AlwaysAllow.

- 4.2.7 - Ensure that the --make-iptables-util-chains argument is set to true.

- 4.2.8 - Ensure that the --hostname-override argument is not set.

- 4.2.9 - Ensure that the kubeAPIQPS \[--event-qps\] argument is set to 0 or a level which ensures appropriate event capture.

- 4.2.13 - Ensure that the Kubelet only makes use of Strong Cryptographic Ciphers.

- Section 5 - Policies.


Prisma Cloud now supports OpenShift CIS Benchmark v1.3.0.

When updating the OpenShift CIS benchmark from v1.1.0 to v1.3.0, configure your clusters to follow the 600 permissions compliance instead of the 644. If you have configured a blocking action, change the action to alert until your clusters follow the new 600 compliance. Sign in to the [CIS website](https://workbench.cisecurity.org/) to review the details of the OpenShift 1.30 benchmarks.

## Notes on the CIS Distribution Independent Linux benchmark[Direct link to heading](https://docs.prismacloud.io/admin-guide/compliance/cis-benchmarks\#notes-on-the-cis-distribution-independent-linux-benchmark)

Prisma Cloud hasn’t implemented the following checks from the CIS Distribution Independent Linux benchmark:

- _1.7.2 - Ensure GDM login banner is configured_ — By default, most server distributions ship without a windows manager. A manual assessment is required.

- _2.2.1.2 - Ensure ntp (Network Time Protocol) is configured_ — CIS did not score this recommendation. A manual assessment is required.

- _2.2.1.3 - Ensure chrony is configured_ — CIS did not score this recommendation. A manual assessment is required.

- _5.3.1 - Ensure password creation requirements are configured_ — This recommendation cannot be implemented generically because password requirements vary from organization to organization. A manual assessment is required.


[PreviousManage compliance](https://docs.prismacloud.io/admin-guide/compliance/manage-compliance) [NextPrisma Cloud compliance checks](https://docs.prismacloud.io/admin-guide/compliance/prisma-cloud-compliance-checks)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
