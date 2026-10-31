For the complete documentation index, see [llms.txt](https://cortex-docs.paloaltonetworks.com/llms.txt). This page is also available as [Markdown](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans.md).

Cortex Cloud Posture Management and Cortex Cloud Runtime Security licensing is provided via an annual subscription, based on the number and type of cloud resources protected. The fundamental metric for consumption is the protected workload. You must procure a license capacity sufficient to cover the total number of workloads you intend to secure.

Licensing is subject to a metering system or Fair Usage policy. This mechanism defines how usage is tracked and what happens when the average consumption of protected workloads exceeds the purchased license capacity. Cortex Cloud accounts for workload utilization based on a 90-day average to smooth spikes and drops in usage of highly ephemeral workloads. Exceeding capacity often triggers a notification, but usually does not immediately disable security functions to ensure your workloads don't lose their protection.

To view the product license and add-ons associated with your tenant, go to **Settings** → **Cortex License** .

### Protected workloads[Direct link to heading](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans\#protected-workloads)

A workload represents any active compute entity that requires protection. These workloads count toward your Cortex Cloud license usage. Examples include:

Table 1. Billable Workload Units

**Workload Type**

**Billable Units**

VMs not running containers

1 VM

VMs running containers

1 VM

Endpoint

1 Endpoint

CaaS (Container As A Service

10 Agent Protected Managed Containers

Cloud Buckets

10 Cloud Buckets

Managed Cloud Database (PaaS)

2 PaaS Databases

DBaaS TB Stored

DBaaS 1TB Stored

SaaS Users

10 SaaS Users

On-Premise Data assets

1 Connection

Cloud ASM – Service

4 Unmanaged Assets

Container Images in Registries

**Free quota**:10 container image scans per deployed workload (VM/CaaS)

**Beyond free quota**:10 container image scans

CLI Image Scans

-

Cortex Cloud Posture Management and Cortex Cloud Runtime Security are available in multiple license configurations, either individually or as part of a bundled package. For more information on bundling options with other Cortex products, see [Cortex XSIAM product licenses](https://cortex-docs.paloaltonetworks.com/cortex-xsiam/learn-about-cortex-xsiam/cortex-xsiam-product-licenses).

**License**

**Configuration**

Cloud Posture Management

Agentless comprehensive visibility across your cloud environment. Includes the following:

- Cloud Security Posture Management (CSPM)

- Cloud Infrastructure Entitlement Management (CIEM)

- Application Security Posture Management (ASPM)

- Data Security Posture Management (DSPM)

- Artificial Intelligence Security Posture Management (AI-SPM)

- Cloud Attack Surface Management (ASM)

- Kubernetes Security Posture Management (KSPM)

- CI/CD Posture Management

- Agentless Workload Scanning


Cloud Runtime Security

Full cloud protection, detection, and response. Includes the following:

- Cloud Posture Management

- Cloud Workload Protection (CWP)

- Web Application & API Security (WAAS)


### Add-ons[Direct link to heading](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans\#add-ons)

- **Security add-ons**: You can purchase security add-ons to expand the core capabilities of your Cortex Cloud Posture Management and Cortex Cloud Runtime Security licenses.





  - Data Ingestion

  - Application Security (IAC Security, SCA, Secrets Security)

  - Enterprise Runtime Security (XDR)

  - Identity Threat Detection and Response (IDTR)

  - Forensics investigation

  - Host Insights

  - Extended Threat Hunting (XTH)

  - Advanced Email Security

  - Data Loss Prevention (DLP) - Beta


- **Capacity add-ons**: You can purchase capability add-ons to extend the duration that security and telemetry data are retained for investigation and compliance purposes





  - Data Retention: Cortex Cloud Posture Management and Cortex Cloud Runtime Security retention per dataset.

  - Query Capacity (compute units): A single Compute Unit add-on.


### License usage and overflow rules[Direct link to heading](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans\#license-usage-and-overflow-rules)

Cortex tracks license usage to ensure that your purchased capacity is used efficiently. The system distinguishes between different workload types and applies clear rules to avoid double-counting and handle usage that exceeds purchased limits.

Cortex categorizes workloads as follows:

- **Cloud Posture Workloads** – Total workloads purchased with a Cloud Posture Management license, including any security add-ons.

- **Cloud Runtime Workloads** – Total workloads purchased with a Cloud Runtime license.


### Note[Direct link to heading](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans\#note)

A Cloud Runtime license includes both Posture Scanning and Runtime Protection on the same asset. Usage, including any overflow, is tracked automatically to ensure accurate reporting across both licenses without duplicate counting.

#### Overflow rules[Direct link to heading](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans\#overflow-rules)

The following table outlines how the system counts workloads based on your purchased licenses and current usage:

Licenses purchased

Usage scenario

License counter display

Overflow behaviour

Cloud Posture Only

Total posture workloads exceed quota.

All usage counts are shown under Cloud Posture Workload

All workload usage, including over-quota workloads, counts toward the Posture license.

Cloud Runtime Only

Total runtime workloads exceed quota.

All usage counts are shown under Cloud Runtime Workload

All workload usage, including over-quota workloads, counts toward the Runtime license.

Both Cloud Posture and Cloud Runtime

Workloads are within quota limits.

Posture: Counts toward Posture quota.

Runtime: Counts toward Runtime quota.

No workload overflow. Counters show usage within purchased quotas.

Both Cloud Posture and Cloud Runtime

Posture exceeds quota, Runtime has remaining capacity

Posture: 100% full usage.

Runtime: Partial or full usage count due to spillover.

Spillover occurs only from Posture to Runtime; it does not occur in reverse. Excess Posture workloads use the available Runtime quota until it’s full.

Both Cloud Posture and Cloud Runtime

Runtime quota full

Posture: Total usage (including excess).

Runtime: Total usage (over-quota)

Spillover only occurs from Posture to Runtime; it does not occur in the reverse. Excess Posture workloads are added back to the Posture counter, and any over-quota usage is shown there.

[PreviousFair Usage policy for Cortex Cloud](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/fair-usage-policy-for-cortex-cloud) [NextData retention](https://cortex-docs.paloaltonetworks.com/cortex-cloud-posture-management/get-started/understand-license-plans/data-retention)

Last updated 23 days ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://www.paloaltonetworks.com/legal-notices/privacy).

AcceptReject