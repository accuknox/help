---
title: AccuKnox Enterprise Architecture
description: A concise and detailed overview of AccuKnox's CNAPP architecture, components, and operational workflows.
---

# AccuKnox Enterprise Architecture

AccuKnox's Cloud-Native Application Protection Platform (CNAPP) offers a unified **AppSec + CloudSec** solution, integrating modules like ASPM, CSPM, CWPP, KIEM, and GRC. This architecture ensures comprehensive security across the software development lifecycle.

[DOWNLOAD CONTROL PLANE ARCHITECTURE](/resources/assets/AccuKnox%20Control%20Plane%20Architecture%20Technical%20v3.4.pdf){ .md-button .md-button--primary download }


## Core Components

### Control Plane

![](./images/deep-arch/control-plane-arch.png)

**Key Components**

1. Playbook job scheduling: Microservices (Divy), Kueue scheduler, Celery tasks
2. Parser jobs for asset + findings database
3. Alerts and telemetry handling via RabbitMQ
4. SPIFFE-based secure cluster onboarding
5. Storage layer: RDS, MongoDB, Neo4j
6. External integrations & triggers handling

## Cloud Architecture

![](./images/deep-arch/cloud-arch.png)

- SaaS and On-Prem support identical services (except AskADA AI Copilot – SaaS only)
- Tenant-level feature control
- Models:
      1. SaaS: AWS-managed (Aurora, S3)
      2. On-Prem: Full in-cluster setup (for air-gapped environments)
      3. Externalized: Uses customer DB/storage

## Externalized Storage Architecture

![](./images/deep-arch/externalized-storage.png)

- Supports deployments with customer-managed storage
- Enables hybrid cloud use cases
- Flexible DB integration (e.g., existing RDS, MongoDB, etc.)

## On-Premises Deployment Architecture

![](./images/deep-arch/onprem-arch.png)

- K8s-native deployment
- No reliance on AWS managed services
- Designed for high-security & compliance environments

[Deployment Models →](/getting-started/deployment-models/)

## Scaling & High Availability

![](./images/deep-arch/scan-alert-flow.png)

AccuKnox scales horizontally using native Kubernetes constructs — new nodes are added dynamically based on CPU, memory, and queue-depth thresholds. Most services are stateless, meaning any instance can serve any request and pods can be restarted without data loss.

**Noisy Neighbor Isolation**

- Per-tenant Kubernetes namespaces with resource quotas prevent a single tenant from consuming disproportionate resources
- [Kueue](https://kueue.sigs.k8s.io/) provides fair scheduling for batch workloads (playbooks, scans, parsing) across tenants
- RabbitMQ telemetry overload is managed via thresholds with offload to SIEM

**High Availability**

The AccuKnox control plane is deployed across multiple Availability Zones (AZs):

- Kubernetes control plane nodes are spread across AZs (odd-number quorum for etcd)
- Stateful services (databases, object storage, message bus) use multi-AZ replication
- Pod anti-affinity rules and topology spread constraints prevent co-location failures
- In case of an AZ failure, ingress shifts traffic automatically and pods are rescheduled in remaining AZs

## Log & Data Storage

- **RDS**: CSPM, KSPM, ASPM (per-tenant tables)
- **MongoDB**: Telemetry logs (per-tenant collections)
- **Neo4j**: GraphDB for metadata (KIEM), expanding to assets/findings in v3.0

## Customer Data Flow

![](./images/deep-arch/customer-data-flow.png)

Asset and findings data flows from customer environments to the AccuKnox control plane via token-authenticated APIs. Playbooks execute in the control plane (or customer environment for CDR), generate reports, and store results in S3 — where Celery tasks parse and update RDS, MongoDB, and Neo4j. The UI fetches all data via AccuKnox APIs. All data in transit is encrypted; no direct DB access is exposed externally.

## Rules Engine Architecture

![](./images/deep-arch/rules-engine-arch.png)

- Parser emits events → Rules Engine evaluates
- Tenant-specific rule specs evaluated
- Actions (e.g., notifications, tickets) sent as Celery tasks
- Fully asynchronous, scalable via queues


## Integrations Architecture

![](./images/deep-arch/integrations.png)

- **CLI-based**: Secret scanning, SAST, container & vulnerability scanning, DAST, and Kubernetes CIS benchmark scanning
- **API-based**: Checkmarx, Nessus
- **SIEM**: One-way push (e.g., Splunk, Sentinel)
- **Ticketing**: Bidirectional (e.g., Jira, ServiceNow)

**Integration Timelines**

- CLI-based: 1 sprint
- API-based: 2–3 weeks
- SIEM: 1 sprint
- Ticketing: 3–5 sprints

[Explore Integrations →](/integrations/)

## Compliance Frameworks

![Compliance Frameworks](/getting-started/images/accuknox-arch/7.png)

Supports over 30 regulatory standards, including:

- **General**: ISO 27001, PCI DSS, SOC2.
- **Industry-Specific**: HIPAA, GDPR.

## SLA Commitments

| Objective | Commitment |
|---|---|
| **RTO** (Recovery Time Objective) | 6 hours — core platform restored after a major incident |
| **RPO** (Recovery Point Objective) | 24 hours — maximum data loss in a catastrophic failure scenario |

> Runtime enforcement on customer clusters continues to operate independently during any control plane recovery.

[View full SLA & Escalation Matrix →](/resources/sla-escalation-matrix/)

## Additional Resources

- [Deployment Models](https://help.accuknox.com/getting-started/deployment-models/)
- [Integrations Playbook](https://help.accuknox.com/how-to/playbook-integrations/)
- [Telemetry Logs](https://help.accuknox.com/integrations/telemetry-logs/)
- [On-Prem Installation Guide](https://help.accuknox.com/getting-started/on-prem-installation-guide/)

!!! info "Note"
    AccuKnox offers rapid protection for Kubernetes and other cloud workloads using Kernel Native Primitives like AppArmor, SELinux, and eBPF. For assistance in planning your cloud security strategy, feel free to reach out.

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
