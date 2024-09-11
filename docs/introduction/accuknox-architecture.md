# AccuKnox Architecture (Enterprise CNAPP Suite)

Welcome to the AccuKnox Enterprise CNAPP Suite, your comprehensive solution for cloud-native application protection. AccuKnox is designed to offer end-to-end security throughout the software development lifecycle, integrating various security measures to ensure robust defense across all deployment phases.

## Cloud-Native Deployment Challenges

In cloud-native deployments, security challenges can arise at different stages -

1. **Code Build Phase**: Issues like vulnerable code, insecure configurations, and hardcoded secrets.

2. **Deployment Phase**: Problems with malicious images, image poisoning, and insecure CI/CD pipelines.

3. **Final Phase**: Runtime security threats such as zero-day attacks, crypto-mining, data exfiltrations, and undetected malware.

![Code to Cloud](/getting-started/images/code-to-cloud.png)

## AccuKnox Solution

AccuKnox's Cloud Native Application Protection Platform (CNAPP) is a unified solution that integrates various tools to provide comprehensive security from development to production. In the cloud-native deployment phases, there can be many security issues like vulnerable code, Insecure configurations, and Hardcoded secrets in the code-building phase. In the deploying phase, there can be issues with malicious images, image poisoning, insecure CI/CD pipelines, etc. In the final phase, there can be issues like runtime security issues like zero-day attacks, Crypto mining data exfiltrations, malware, and vulnerabilities that are still left out un-detected, etc.

Multiple tools are available to provide security at various stages of the software development life cycle. However, using these tools at different stages becomes difficult as there is no common connectivity between these tools to get reports and findings. Hence, we need a single tool that provides end-to-end solutions for cloud security, from the development to the production process. The Cloud Native Application Protection Platform tool, which is a one-stop solution that integrates various results and normalizes or correlates the findings to provide complete security to cloud resources, has become the need of the hour.

AccuKnox's cloud-native application protection platform is a single tool that provides both static and dynamic security. AccuKnox Enterprise Architecture consists of various microservices, like the vault for secret management, MongoDB for database-related connections, and an API gateway. The AccuKnox CSPM tool scans the infrastructure and stores the scan data in the S3 bucket, either created by AccuKnox or the S3 bucket created by the customer. It combines static and dynamic security measures and supports integration with CI/CD pipelines and SIEM tools like Jira, Slack, Splunk, and Rsyslog.

![AccuKnox Enterprise Architecture](/introduction/images/accuknox-architecture.png)

## AccuKnox Product Set

### CNAPP

Multi-cloud, hybrid cloud security with detailed telemetry for auditing and container forensics.

### CWPP

Automated zero-trust policy generation with customizable policy control and reduced alert fatigue.

### CSPM

Visibility and orchestration of multi-cloud resources with continuous compliance and auditing.

### KSPM

Container-level visibility with unique in-line mitigation enforcement to prevent zero-day attacks.

### IoT/Edge

Deep visibility and monitoring with automated zero-trust policy discovery and enforcement.

### 5G Security

Hardening of 5G control planes and secure microsegmentation of network and application traffic.

## Security Layers

* Identity Management
  * Kubernetes Identity and Entitlement Management (KIEM)

* Static Security
  * Cloud Security Posture Management (CSPM)

* Run-time Security
  * Cloud Workload Protection Platform (CWPP)

## Unique Capabilities

* Zero-Trust Security implements allow-based policies to ensure that only specific actions are permitted, following the principle of "never trust, always verify."

* Multi-Cloud Coverage for a consolidated dashboard and asset inventory across multiple cloud accounts.

* Multi-tool integration for a unified risk assessment view across cloud, container, cluster, and code assets (4C coverage).

* Inline Mitigation prevents attacks in real-time using advanced Linux Security Modules (LSMs) like AppArmor, BPF-LSM, and SELinux.

* Agent-Based and Agentless Scanning supports both methods for comprehensive infrastructure security.

* Shift Left Defense allows proactive thwarting of advanced "Zero Day" attacks by addressing security issues early in the development phase.

* Real-Time Protection with real-time defense mechanisms against zero-day attacks.

* Integrated Testing to incorporate Static Application Security Testing (SAST), Software Composition Analysis (SCA), and Dynamic Application Security Testing (DAST).

## Compliance

AccuKnox's CNAPP supports over 30 compliance frameworks, including HIPAA, GDPR, SOC2, ISO 27001, and more, ensuring adherence to a wide range of industry standards and regulations. We guarantee a robust, unified approach to cloud security that spans all stages of the development lifecycle, providing peace of mind and comprehensive protection against emerging threats.

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
