# Onboarding Assets – High-Level Overview

<img src="https://i.ibb.co/7dFjz13S/support-worklaods.png" alt="support-worklaods" border="0">

## Customer Environments

**Cloud:**

- AWS Accounts
- Azure Accounts
- AWS SageMaker / Bedrock

**Data Center / Hybrid:**

- Kubernetes Clusters (EKS / On-Prem / Fargate)
- Virtual Machines (EC2 / On-Prem)

**Workload Types:**

- K8s Clusters
- Virtual Machines
- Serverless (Fargate)
- AI/ML Services (SageMaker, Bedrock)

**Security and Telemetry Flow:**

- Agentless scan initiated from SaaS
- CNAPP control plane processes telemetry
- Alerts and detections sent to SIEM

---

## Cloud Onboarding Options

- Fully Agentless Mode
- Account/Subscription Onboarding:

  - CloudFormation (recommended)
  - Terraform
  - Manual

- AWS Organization Unit Onboarding:

  - Using cross-account tenant roles

---

## Kubernetes – AWS EKS / On-Prem / Fargate

### Risk Assessment

- CIS Benchmarks
- Misconfigurations
- KIEM Policies
- Agentless methods:

  - Remote scanning via `kubeconfig`
  - Kubernetes job-based scanning

### Runtime Security & Hardening

- Helm-based installation
- In-cluster image scanning:

  - Operator and job-based deployment via Helm

### Fargate Runtime

- Supported via sidecar model
- Deployable using Helm or Kubernetes manifests

---

## Virtual Machines – EC2 / On-Prem

- Misconfiguration scanning via cloud account onboarding (agentless)
- Risk assessment / STIGs scanning requires lightweight VM agent

---

## Container Registry

### SaaS-Based Scanning

- Registry onboarded via control plane
- Credentials: Username + API Token

### On-Prem Scanning

- Requires AccuKnox collector deployed on VM
- Local scanning of registries enabled

---

## AI/ML Workloads – SageMaker / Bedrock

- Fully agentless
- Selectable during cloud account onboarding:

  - General Cloud Assets
  - General Cloud + AI/ML Assets

---

## Deployment References

- Separate detailed documentation provided for Helm charts, job configurations, and onboarding automation (CloudFormation, Terraform).
