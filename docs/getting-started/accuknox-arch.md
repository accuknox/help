title: AccuKnox Enterprise Architecture Deep Dive
description: A concise and detailed overview of AccuKnox's CNAPP architecture, components, and operational workflows.

# AccuKnox Enterprise Architecture

AccuKnox's Cloud-Native Application Protection Platform (CNAPP) offers a unified **AppSec + CloudSec** solution, integrating modules like ASPM, CSPM, CWPP, KIEM, and GRC. This architecture ensures comprehensive security across the software development lifecycle.
![AccuKnox Enterprise Architecture](/introduction/images/accuknox-architecture.png)


## Core Components

### Control Plane Architecture

- **Microservices**:
    - _Divy_: Handles API requests.
    - _Celery_: Manages asynchronous tasks.
    - _Kueue_: Schedules Kubernetes-native jobs.
- **Parser Jobs**: Process asset and findings data, updating databases accordingly.
- **Alerts & Telemetry**: Ingested via RabbitMQ, processed for real-time insights.
- **Secure Onboarding**: Utilizes SPIFFE-based control plane for cluster onboarding.
- **Storage/Databases**:
    - _RDS_: Stores CSPM, KSPM, and ASPM data.
    - _MongoDB_: Handles streaming telemetry.
    - _Neo4j_: Manages metadata for KIEM.
- **Integrations**: Interfaces with SIEM tools (e.g., Splunk, Rsyslog) and ticketing systems (e.g., JIRA, Slack).

## Scaling Considerations

- **Playbook Jobs**:
    - Each AWS account can trigger up to 272 jobs across 68 regions.
    - _Kueue_ ensures resource allocation per tenant, preventing resource contention.
- **Parsing Jobs**:
    - Managed by _Celery_ tasks, processing reports and updating databases.
- **Telemetry Handling**:
    - Alerts from KubeArmor are processed via RabbitMQ.
    - High-volume telemetry is redirected to SIEM tools to prevent overload.

## Data Flow

1. **Playbook Execution**: Generates JSON/XML reports.
2. **Artifact API**: Receives reports, stores them in S3, and queues tasks.
3. **Celery Tasks**: Fetch reports from S3, parse data, and update databases.
4. **UI Interaction**: Users access data via Divy microservice APIs.

## Rules Engine Workflow

- **Event Generation**: Parser emits events on new or updated findings.
- **Rule Evaluation**: Rules Engine assesses events against tenant-specific rules.
- **Action Execution**: Triggers tasks like ticket creation or notifications via Celery.

## Integrations

![Integrations](/introduction/images/ak-offering.png)

- **Security Tools**:
    - _CLI-Based_: TruffleHog, Sonarqube, kubebench, trivy, zap.
    - _API-Based_: Checkmarx, Nessus.
- **CI/CD Pipelines**: Supports Jenkins, GitHub Actions, GitLab CI, Azure DevOps.
- **SIEM Tools**: Integrates with Splunk, Rsyslog, Azure Sentinel.
- **Ticketing Systems**: Interfaces with JIRA, ServiceNow, Freshservice.

_Integration timelines vary from 1 to 5 sprints based on complexity._

## Compliance Frameworks

![Compliance Frameworks](/getting-started/images/accuknox-arch/7.png)

Supports over 30 regulatory standards, including:

- **General**: ISO 27001, PCI DSS, SOC2.
- **Industry-Specific**: HIPAA, GDPR.

## Additional Resources

- [Deployment Models](https://help.accuknox.com/getting-started/deployment-models/)
- [Integrations Playbook](https://help.accuknox.com/how-to/playbook-integrations/)
- [Telemetry Logs](https://help.accuknox.com/integrations/telemetry-logs/)
- [On-Prem Installation Guide](https://help.accuknox.com/getting-started/on-prem-installation-guide/)

!!!info NOTE
    AccuKnox offers rapid protection for Kubernetes and other cloud workloads using Kernel Native Primitives like AppArmor, SELinux, and eBPF. For assistance in planning your cloud security strategy, feel free to reach out.

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
