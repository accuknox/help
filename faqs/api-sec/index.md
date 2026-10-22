---
title: API Security FAQs
description: Frequently asked questions about AccuKnox API Security: API discovery, shadow and zombie API detection, gateway integrations, OWASP API Top 10, runtime enforcement, compliance, and supported platforms including AWS API Gateway, Istio, NGINX, Kong, and F5.
hide:
  - toc
---

# API Security

## Core API Security & Platform

??? "**1. What is AccuKnox API Security and what does it cover?**"
    AccuKnox API Security is a continuous risk assessment and deep visibility module in the **AccuKnox Zero Trust CNAPP**. It analyzes live traffic across all your API gateways and service meshes. It discovers, classifies and protects every API endpoint, documented or not.

    Core capabilities:

    - **Real-Time API Inventory**: Discovers APIs from live traffic and scores risk by authentication type, exposure level and sensitive data handling.
    - **Shadow, Zombie, and Orphan API Detection**: Finds undocumented, deprecated and unowned APIs through continuous traffic analysis.
    - **Runtime Monitoring**: Tracks traffic behavior, usage patterns and anomalies, mapped to users, services and namespaces.
    - **Zero Trust Enforcement**: Blocks unauthorized API access and abnormal behavior with KubeArmor and eBPF-based controls.
    - **OWASP API Top 10 Coverage**: Detects injection, broken authentication, excessive data exposure and other OWASP API vulnerabilities in real time.
    - **Logical Grouping and Collections**: Groups APIs by service, team, environment or sensitivity for tracking and management.
    - **Compliance Reporting**: Maps continuously to PCI DSS v4.0.1, HIPAA, GDPR, DORA and OWASP standards, with automated audit evidence.

    **References:**

    - [AccuKnox API Security Platform](https://accuknox.com/platform/api-security)

??? "**2. Which API gateways and ingress controllers does AccuKnox integrate with?**"
    AccuKnox API Security integrates with all major API gateways and ingress controllers, with **no code changes required**:

    - **AWS API Gateway**: A CloudFormation-based integration forwards API Gateway logs to AccuKnox. Endpoints appear in the API inventory automatically once configured.
    - **Kubernetes Ingress Proxy**: A native K8s integration captures north-south and east-west API traffic across cluster workloads.
    - **Istio Service Mesh**: A sidecar-based integration captures all service-to-service API traffic, including encrypted east-west communication.
    - **NGINX** (Ingress and Server): Covers NGINX-proxied APIs in both Kubernetes ingress and standalone server deployments.
    - **Kong API Gateway**: Covers Kong-managed API traffic, including plugin-based policy enforcement.
    - **F5 BIG-IP**: Covers F5-proxied API traffic with full inventory and risk classification.
    - **Azure API Management**: Supports Azure APIM-managed APIs.

    AccuKnox uses service mesh sidecars and eBPF to inspect actual API behavior. This includes **encrypted traffic** that WAFs and perimeter tools cannot see.

    **References:**

    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)

??? "**3. How does AccuKnox discover APIs without requiring code changes?**"
    AccuKnox uses **multi-vector discovery** that connects to your existing infrastructure. You do not instrument application code.

    - **Runtime Traffic Analysis**: Service mesh sidecars and eBPF inspect live traffic to find the APIs that production actually calls.
    - **Static Spec Analysis**: An OpenAPI/Swagger upload classifies documented endpoints against observed traffic instantly.
    - **Platform-Native Integrations**: Kubernetes, AWS CloudTrail, Azure and GCP integrations surface API activity from cloud control planes.
    - **OpenTelemetry**: OTel exports provide telemetry from applications already instrumented with OpenTelemetry.
    - **Gateway Log Forwarding**: AWS API Gateway, Kong, NGINX, Istio and F5 forward logs to AccuKnox for parsing and analysis.

    This approach finds documented APIs. It also finds shadow, zombie and orphan APIs that run in production traffic but are missing from your spec.

    **References:**

    - [API Security That Goes Deeper](https://accuknox.com/blog/api-security-discovery-visibility)


## Shadow, Zombie, and Orphan APIs

??? "**4. What are Shadow, Zombie, and Orphan APIs, and how does AccuKnox detect them?**"
    These three API categories are your highest-risk undiscovered attack surface:

    - **Shadow APIs**: Endpoints that receive production traffic but do not exist in your OpenAPI/Swagger specification. Examples are debug hooks, quick fixes and forgotten routes that no one monitors or secures. 68% of organizations lack visibility into their shadow APIs.
    - **Zombie APIs**: Deprecated API versions (for example, a V1 endpoint replaced by V2) that still receive live production calls. They carry old vulnerabilities, often have weaker authentication, and should be decommissioned.
    - **Orphan APIs**: APIs in your specification that production traffic has not touched for an extended period. They may be gone from code but still documented. This creates a misleading attack surface and breaks incident response ownership.

    AccuKnox detects all three by **comparing observed live traffic against your uploaded OpenAPI specification**. If you have no spec, AccuKnox generates one from observed traffic automatically. The generated spec captures the full request body structure, including sensitive fields detected in live traffic.

    **References:**

    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)

??? "**5. Can AccuKnox automatically generate an OpenAPI specification from observed traffic?**"
    **Yes.** If you have no OpenAPI/Swagger document, AccuKnox generates one from observed live traffic.

    - **One click**: Generates a downloadable OpenAPI specification from real traffic on any collection.
    - **Full body structure**: Captures the request body structure, including sensitive fields like credit card numbers or PII found in live traffic.
    - **Dev team reuse**: Gives your dev team a base to bootstrap or update documentation.
    - **Instant classification**: Lets you upload your existing Swagger doc alongside it. AccuKnox then classifies endpoints as Shadow, Zombie or Orphan right away.
    - **Continuous updates**: Updates the spec as new endpoints appear in traffic, so your API inventory stays current without manual work.

    **References:**

    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)
    - [API Security That Goes Deeper](https://accuknox.com/blog/api-security-discovery-visibility)

---

## Gateway-Specific Integrations

??? "**6. How does the AWS API Gateway integration work?**"
    AccuKnox connects to AWS API Gateway through **CloudFormation templates**, with no code changes to your APIs.

    - **Two stacks**: You deploy them in sequence. The base stack creates the IAM role and permissions. The standard stack deploys once per stage (Dev, Staging, Prod).
    - **Log forwarding**: Logging turns on for your API Gateway stages. A Lambda function forwards the logs to the AccuKnox Control Plane.
    - **Automatic inventory**: Logs then flow continuously, and endpoints appear in the API inventory automatically.
    - **API types**: The integration supports all API Gateway deployment types, including REST APIs and HTTP APIs.
    - **Clean reversion**: The base stack can delete all newly created resources if you remove the integration.

    **References:**

    - [AWS API Gateway Integration](https://help.accuknox.com/integrations/api-aws/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)

??? "**7. How does the Istio integration work for east-west API visibility?**"
    AccuKnox integrates with the Istio service mesh to give you **full east-west API traffic visibility**.

    - **Encrypted traffic**: Istio sidecar proxies capture service-to-service API traffic, including mTLS traffic that perimeter tools cannot inspect.
    - **Threat analysis**: AccuKnox analyzes Istio telemetry for shadow APIs, unauthorized service calls, authentication anomalies and policy violations.
    - **Observed inventory**: The API inventory comes from actual Istio-observed traffic, not only from the mesh configuration.
    - **Workload mapping**: East-west API calls map to Kubernetes workload identities, namespaces and service accounts for precise authorization analysis.
    - **Runtime enforcement**: AccuKnox can block service-to-service calls that violate least-privilege API access policies.

    **References:**

    - [Istio Integration](https://help.accuknox.com/integrations/api-istio/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)
    - [AccuKnox API Security Platform](https://accuknox.com/platform/api-security)

??? "**8. How do Kong and F5 integrate with AccuKnox API Security?**"
    AccuKnox supports **both Kong and F5** as API traffic sources.

    - **Kong**: AccuKnox ingests request and response metadata from Kong-managed traffic for inventory, risk scoring and anomaly detection. Kong plugin integration adds policy-based enforcement at the gateway layer, alongside AccuKnox runtime controls.
    - **F5 BIG-IP**: F5 forwards logs of proxied API traffic to the AccuKnox Control Plane. Endpoints proxied through F5 appear in the API inventory with full risk classification.
    - **Combined view**: Both integrations are additive. AccuKnox correlates gateway-level visibility with eBPF and service mesh telemetry. Neither source alone gives this complete picture.

    **References:**

    - [Kong Integration](https://help.accuknox.com/integrations/kong/)
    - [F5 Integration](https://help.accuknox.com/integrations/f5/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)


??? "**9. How does AccuKnox handle NGINX-proxied APIs?**"
    AccuKnox supports both **NGINX Ingress Controller** (Kubernetes) and standalone NGINX Server deployments.

    - **NGINX Ingress**: AccuKnox captures API traffic routed through the Kubernetes ingress layer and builds inventory from north-south traffic.
    - **NGINX Server**: Log forwarding sends request metadata to the AccuKnox Control Plane for API discovery and risk analysis.
    - **Spec classification**: AccuKnox classifies NGINX-observed endpoints against your OpenAPI specification immediately. Shadow, zombie and orphan APIs show in the same inventory as other gateway sources.
    - **Risk scoring**: Scores apply the same way to NGINX-proxied endpoints, based on authentication type, sensitive data exposure and traffic volume.

    **References:**

    - [NGINX Integration](https://help.accuknox.com/integrations/api-nginx/)
    - [Kubernetes Proxy Integration](https://help.accuknox.com/integrations/api-k8s/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)


## API Risk Prioritization

??? "**10. How does AccuKnox score and prioritize API risk?**"
    AccuKnox gives **every discovered API endpoint a risk score** based on these factors:

    - **Authentication**: Endpoints without proper authentication controls (OAuth 2.0, JWT, mTLS, API keys, SAML) get a higher risk score.
    - **Sensitive Data Exposure**: AccuKnox scans live requests and responses for PII, PHI and financial data (credit card numbers, SSNs). Endpoints that handle sensitive data move up in priority.
    - **Exposure**: External (north-south) APIs score differently from internal (east-west) service calls. Publicly exposed, unauthenticated endpoints carry the highest risk scores.
    - **API Category**: Shadow, Zombie and Orphan APIs get separate flags with category-specific risk context.
    - **OWASP API Top 10**: Endpoints that show patterns of broken object level authorization (BOLA), broken authentication or other OWASP API vulnerabilities score accordingly.

    You can filter the full inventory by response code, sensitivity, auth type, status code and exposure. This surfaces the highest-priority endpoints without a manual review of thousands of entries.


??? "**11. How does AccuKnox price API Security, and is it based on traffic volume?**"
    **No.** AccuKnox API Security pricing is based on **unique endpoint count**, not traffic volume.

    - **One endpoint is one endpoint**: An endpoint called one million times per day counts the same as one called once per day.
    - **Sizing rule**: Divide your total endpoint count by 50 to get a rough unit count.
    - **Predictable cost**: Traffic spikes do not change the price. This is a deliberate choice over ingestion-based models, which scale with volume and are hard to forecast.
    - **Deduplication**: AccuKnox counts unique endpoints across all connected gateway integrations. An endpoint seen in both NGINX and Istio counts once.

    **References:**

    - [API Security That Goes Deeper](https://accuknox.com/blog/api-security-discovery-visibility)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)


??? "**12. How does AccuKnox cover the OWASP API Top 10?**"
    AccuKnox gives **continuous detection and runtime enforcement** for OWASP API Top 10 vulnerabilities:

    - **BOLA (Broken Object Level Authorization)**: Detects mismatched identity-to-object logic in API responses. BOLA is the most common API vulnerability and the hardest to catch without runtime traffic analysis.
    - **Broken Authentication**: Finds brute force attempts, token misuse, expired credential reuse and APIs exposed without proper auth controls.
    - **Excessive Data Exposure**: Scans API responses in live traffic for PII, PHI and financial data, not just at the spec level.
    - **Injection Attacks**: Detects SQL injection, command injection and other injection patterns in API requests through traffic signatures.
    - **Security Misconfiguration**: Maps API configuration against CIS, NIST and OWASP baseline controls through OpenAPI spec analysis.
    - **Improper Inventory Management**: Shadow, Zombie and Orphan API detection directly addresses the OWASP "Improper Assets Management" category.
    - **DoS Protection**: eBPF XDP technology detects and mitigates API-level denial of service attacks with ultra-low latency.
    - **TLS Misconfigurations**: Finds TLS and certificate issues and manages secure API connections.

    **References:**

    - [Top 10 API Security Tools for OWASP Compliance 2026](https://accuknox.com/blog/top-10-api-security-testing-tools-for-owasp-compliance-2026)


## Authentication & Access Control

??? "**13. What authentication protocols does AccuKnox support and monitor for APIs?**"
    AccuKnox supports and monitors **all modern API authentication mechanisms**:

    - **OAuth 2.0**: Detects broken OAuth flows, token misuse and APIs where OAuth is configured but not enforced.
    - **JWT**: Watches for expired, malformed or improperly validated JWT tokens in API requests.
    - **API Keys**: Finds APIs that use static API keys. Flags endpoints where key-based auth is too weak for the data they expose.
    - **mTLS**: Supports mutual TLS for east-west service-to-service authentication, enforced through SPIFFE/SPIRE SVIDs for cryptographic workload identity.
    - **SAML**: Monitors SAML-authenticated API access patterns for anomalies.
    - **No Auth Detection**: Flags APIs in production traffic that have no authentication controls at all, whatever the spec claims.

    Each endpoint's risk score reflects its authentication posture. Unauthenticated endpoints that handle sensitive data go straight to **critical priority**.

    **References:**

    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)
    - [AccuKnox API Security Platform](https://accuknox.com/platform/api-security)
    - [API Security for Internal APIs](https://accuknox.com/blog/api-security-platforms-internal-apis)


??? "**14. Does AccuKnox API Security work with Kubernetes-native environments and service meshes?**"
    **Yes.** AccuKnox is built from the ground up for Kubernetes-native and cloud-native API environments.

    - **Native K8s integration**: Captures all API traffic through the Kubernetes proxy layer, both north-south ingress and east-west pod-to-pod traffic.
    - **Istio sidecar integration**: Gives full service mesh visibility, including encrypted mTLS east-west traffic between services.
    - **Workload context**: Maps endpoints to Kubernetes namespaces, deployments and service accounts, so every endpoint has precise ownership.
    - **KIEM (Kubernetes Identity and Entitlement Management)**: Connects API access patterns to RBAC roles and service account permissions to surface over-privileged API consumers.
    - **KubeArmor runtime enforcement**: Enforces least-privilege API access policies at the kernel level and blocks unauthorized API calls before they complete.
    - **Admission control**: Stops deployments that add shadow or misconfigured API endpoints from reaching production.

    **References:**

    - [Kubernetes Proxy Integration](https://help.accuknox.com/integrations/api-k8s/)
    - [Istio Integration](https://help.accuknox.com/integrations/api-istio/)
    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)
    - [API Security for Internal APIs](https://accuknox.com/blog/api-security-platforms-internal-apis)

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
