---
title: API Security FAQs
description: Frequently asked questions about AccuKnox API Security — API discovery, shadow and zombie API detection, gateway integrations, OWASP API Top 10, runtime enforcement, compliance, and supported platforms including AWS API Gateway, Istio, NGINX, Kong, and F5.
hide:
  - toc
---

# API Security

## Core API Security & Platform

??? "**1. What is AccuKnox API Security and what does it cover?**"
    AccuKnox API Security is a continuous risk assessment and deep visibility module built into the AccuKnox Zero Trust CNAPP. It analyzes live traffic across all your API gateways and service meshes to discover, classify, and protect every API endpoint — documented or not.

    Core capabilities include:
    + **Real-Time API Inventory**: Automatically discovers APIs from live traffic with risk scoring based on authentication type, exposure level, and sensitive data handling.
    + **Shadow, Zombie, and Orphan API Detection**: Identifies undocumented, deprecated, and unowned APIs through continuous traffic analysis.
    + **Runtime Monitoring**: Analyzes traffic behavior, usage patterns, and anomalies mapped to users, services, and namespaces.
    + **Zero Trust Enforcement**: Blocks unauthorized API access and abnormal behavior using KubeArmor and eBPF-based controls.
    + **OWASP API Top 10 Coverage**: Detects injection, broken authentication, excessive data exposure, and other OWASP API vulnerabilities in real time.
    + **Logical Grouping and Collections**: Organize APIs by service, team, environment, or sensitivity for efficient tracking and management.
    + **Compliance Reporting**: Continuous mapping to PCI DSS v4.0.1, HIPAA, GDPR, DORA, and OWASP standards with automated audit evidence.

    **References:**
    - [AccuKnox API Security Platform](https://accuknox.com/platform/api-security)

??? "**2. Which API gateways and ingress controllers does AccuKnox integrate with?**"
    AccuKnox API Security integrates with all major API gateways and ingress controllers — no code changes required:
    + **AWS API Gateway**: CloudFormation-based integration forwards API Gateway logs to AccuKnox for analysis. Endpoints appear in the API inventory automatically once configured.
    + **Kubernetes Ingress Proxy**: Native K8s integration captures north-south and east-west API traffic across cluster workloads.
    + **Istio Service Mesh**: Sidecar-based integration captures full service-to-service API traffic including encrypted east-west communication.
    + **NGINX** (Ingress and Server): Integration for NGINX-proxied APIs in both Kubernetes ingress and standalone server deployments.
    + **Kong API Gateway**: Integration for Kong-managed API traffic including plugin-based policy enforcement.
    + **F5 BIG-IP**: Integration for F5-proxied API traffic with full inventory and risk classification.
    + **Azure API Management**: Support for Azure APIM-managed APIs.
    AccuKnox uses service mesh sidecars and eBPF to inspect actual API behavior — including encrypted traffic that WAFs and perimeter tools cannot see.

    **References:**
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)

??? "**3. How does AccuKnox discover APIs without requiring code changes?**"
    AccuKnox uses multi-vector discovery that connects to your existing infrastructure — no instrumentation of application code needed:
    + **Runtime Traffic Analysis**: Service mesh sidecars and eBPF inspect live traffic patterns to discover what APIs are actually being called in production.
    + **Static Spec Analysis**: OpenAPI/Swagger specification upload classifies existing documented endpoints against observed traffic instantly.
    + **Platform-Native Integrations**: Kubernetes, AWS CloudTrail, Azure, and GCP integrations surface API activity from cloud control planes.
    + **OpenTelemetry**: OTel exports provide comprehensive telemetry from applications already instrumented with OpenTelemetry.
    + **Gateway Log Forwarding**: AWS API Gateway, Kong, NGINX, Istio, and F5 forward logs to AccuKnox for parsing and analysis.
    This multi-vector approach discovers both documented APIs and shadow, zombie, and orphan APIs that exist in production traffic but are missing from your spec.

    **References:**
    - [API Security That Goes Deeper](https://accuknox.com/blog/api-security-discovery-visibility)


## Shadow, Zombie, and Orphan APIs

??? "**4. What are Shadow, Zombie, and Orphan APIs — and how does AccuKnox detect them?**"
    These three API categories represent your highest-risk undiscovered attack surface:

    + **Shadow APIs**: Endpoints deployed and receiving production traffic that do not exist in your OpenAPI/Swagger specification. These are undocumented endpoints — debug hooks, quick fixes, or forgotten routes — that no one is actively monitoring or securing. 68% of organizations lack visibility into their shadow APIs.
    + **Zombie APIs**: Deprecated API versions (e.g., a V1 endpoint replaced by V2) that are marked as deprecated in the spec but are still receiving live production calls. These carry old vulnerabilities, often have weaker authentication, and should be decommissioned.
    + **Orphan APIs**: APIs present in your specification that have not been seen in production traffic for an extended period. They may be removed from code but still documented — creating a misleading attack surface and breaking incident response ownership.

    AccuKnox detects all three by comparing observed live traffic against your uploaded OpenAPI specification. If you do not have a spec, AccuKnox generates one from observed traffic automatically — capturing full request body structure including sensitive fields detected in live traffic.

    **References:**
    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)

??? "**5. Can AccuKnox automatically generate an OpenAPI specification from observed traffic?**"
    Yes. If you do not have an existing OpenAPI/Swagger document, AccuKnox generates one from observed live traffic:
    + One click generates a downloadable OpenAPI specification from real traffic observed on any collection.
    + The generated spec captures full request body structure — including sensitive fields like credit card numbers or PII detected in live traffic.
    + The generated spec can be used by your dev team to bootstrap or update documentation.
    + Once generated, you can upload your existing Swagger doc alongside it — AccuKnox will immediately classify endpoints as Shadow, Zombie, or Orphan based on the comparison.
    + The generated spec is updated continuously as new endpoints appear in traffic, keeping your API inventory current without manual maintenance.

    **References:**
    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)
    - [API Security That Goes Deeper](https://accuknox.com/blog/api-security-discovery-visibility)

---

## Gateway-Specific Integrations

??? "**6. How does the AWS API Gateway integration work?**"
    AccuKnox connects to AWS API Gateway using CloudFormation templates — no code changes to your APIs:
    + Two CloudFormation stacks are deployed in sequence: a base stack that creates the necessary IAM role and permissions, and a standard stack deployed once per deployment stage (Dev, Staging, Prod).
    + Logging is enabled for your API Gateway stages, and a Lambda function is configured to forward logs to the AccuKnox Control Plane.
    + Once deployed, AWS API Gateway is fully integrated — logs are forwarded continuously and endpoints begin appearing in the API inventory automatically.
    + The integration supports all API Gateway deployment types including REST APIs and HTTP APIs.
    + Clean reversion is built in — the base stack can delete all newly created resources if the integration needs to be removed.

    **References:**
    - [AWS API Gateway Integration](https://help.accuknox.com/integrations/api-aws/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)

??? "**7. How does the Istio integration work for east-west API visibility?**"
    AccuKnox integrates with Istio service mesh to provide full east-west API traffic visibility:
    + Istio sidecar proxies capture service-to-service API traffic including encrypted mTLS communication that perimeter tools cannot inspect.
    + AccuKnox receives Istio telemetry and analyzes it for shadow APIs, unauthorized service calls, authentication anomalies, and policy violations.
    + API inventory is built from actual Istio-observed traffic — not just what is registered in the mesh configuration.
    + East-west API calls are mapped to Kubernetes workload identities, namespaces, and service accounts for precise authorization analysis.
    + Runtime enforcement can be applied to block service-to-service calls that violate least-privilege API access policies.

    **References:**
    - [Istio Integration](https://help.accuknox.com/integrations/api-istio/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)
    - [AccuKnox API Security Platform](https://accuknox.com/platform/api-security)

??? "**8. How do Kong and F5 integrate with AccuKnox API Security?**"
    Both Kong and F5 are supported as API traffic sources for AccuKnox:
    + **Kong**: AccuKnox connects to Kong-managed API traffic, ingesting request and response metadata for inventory building, risk scoring, and anomaly detection. Kong plugin integration enables policy-based enforcement at the gateway layer alongside AccuKnox's runtime controls.
    + **F5 BIG-IP**: AccuKnox integrates with F5-proxied API traffic, forwarding logs to the AccuKnox Control Plane for analysis. Endpoints proxied through F5 appear in the API inventory with full risk classification.
    + Both integrations are additive — AccuKnox correlates gateway-level visibility with eBPF and service mesh telemetry to provide a complete picture that neither source alone delivers.

    **References:**
    - [Kong Integration](https://help.accuknox.com/integrations/kong/)
    - [F5 Integration](https://help.accuknox.com/integrations/f5/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)


??? "**9. How does AccuKnox handle NGINX-proxied APIs?**"
    AccuKnox supports both NGINX Ingress Controller (Kubernetes) and standalone NGINX Server deployments:
    + For NGINX Ingress, AccuKnox captures API traffic routed through the Kubernetes ingress layer, building inventory from observed north-south traffic.
    + For NGINX Server, log forwarding sends request metadata to the AccuKnox Control Plane for API discovery and risk analysis.
    + NGINX-observed endpoints are classified against your OpenAPI specification immediately — surfacing shadow, zombie, and orphan APIs in the same unified inventory as other gateway sources.
    + Risk scoring applies consistently across NGINX-proxied endpoints — based on authentication type, sensitive data exposure, and traffic volume.

    **References:**
    - [NGINX Integration](https://help.accuknox.com/integrations/api-nginx/)
    - [Kubernetes Proxy Integration](https://help.accuknox.com/integrations/api-k8s/)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)


## API Risk Prioritization

??? "**10. How does AccuKnox score and prioritize API risk?**"
    AccuKnox assigns risk scores to every discovered API endpoint based on multiple dimensions:
    + **Authentication**: Endpoints without proper authentication controls (OAuth 2.0, JWT, mTLS, API keys, SAML) are flagged and scored higher risk.
    + **Sensitive Data Exposure**: Live traffic is scanned for PII, PHI, and financial data (credit card numbers, SSNs) in API requests and responses. Endpoints handling sensitive data are elevated in priority.
    + **Exposure**: External (north-south) APIs are scored differently from internal (east-west) service calls. Publicly exposed unauthenticated endpoints carry the highest risk scores.
    + **API Category**: Shadow APIs, Zombie APIs, and Orphan APIs are flagged separately with category-specific risk context.
    + **OWASP API Top 10**: Endpoints exhibiting patterns associated with broken object level authorization (BOLA), broken authentication, or other OWASP API vulnerabilities are scored accordingly.
    The full inventory can be filtered by response code, sensitivity, auth type, status code, and exposure to surface the highest-priority endpoints without manually reviewing thousands of entries.


??? "**11. How does AccuKnox handle API pricing — is it based on traffic volume?**"
    AccuKnox API Security pricing is based on unique endpoint count — not traffic volume:
    + An endpoint called one million times per day counts the same as one called once per day — it is still one endpoint.
    + A rough sizing rule: divide your total endpoint count by 50 to get your unit count.
    + This keeps pricing predictable regardless of traffic spikes — a deliberate design choice over ingestion-based models, which scale with volume and can be difficult to forecast.
    + Unique endpoints are determined across all connected gateway integrations — deduplicated so an endpoint seen in both NGINX and Istio counts once.

    **References:**
    - [API Security That Goes Deeper](https://accuknox.com/blog/api-security-discovery-visibility)
    - [API Security Integrations Overview](https://help.accuknox.com/integrations/api-overview/)


??? "**12. How does AccuKnox cover the OWASP API Top 10?**"
    AccuKnox provides continuous detection and runtime enforcement for OWASP API Top 10 vulnerabilities:
    + **BOLA (Broken Object Level Authorization)**: Detects mismatched identity-to-object logic in API responses — the most common API vulnerability and the hardest to catch without runtime traffic analysis.
    + **Broken Authentication**: Identifies brute force attempts, token misuse, expired credential reuse, and APIs exposed without proper auth controls.
    + **Excessive Data Exposure**: Scans API responses for PII, PHI, and financial data exposure in live traffic — not just at the spec level.
    + **Injection Attacks**: Detects SQL injection, command injection, and other injection patterns in API requests using traffic signatures.
    + **Security Misconfiguration**: Maps API configuration against CIS, NIST, and OWASP baseline controls via OpenAPI spec analysis.
    + **Improper Inventory Management**: Shadow, Zombie, and Orphan API detection directly addresses OWASP's "Improper Assets Management" category.
    + **DoS Protection**: eBPF XDP technology enables ultra-low-latency detection and mitigation of API-level denial of service attacks.
    + **TLS Misconfigurations**: Identifies TLS/certificate issues and manages secure API connections.

    **References:**
    - [Top 10 API Security Tools for OWASP Compliance 2026](https://accuknox.com/blog/top-10-api-security-testing-tools-for-owasp-compliance-2026)


## Authentication & Access Control

??? "**13. What authentication protocols does AccuKnox support and monitor for APIs?**"
    AccuKnox supports and monitors all modern API authentication mechanisms:
    + **OAuth 2.0**: Detects broken OAuth flows, token misuse, and APIs where OAuth is configured but not properly enforced.
    + **JWT**: Monitors for expired, malformed, or improperly validated JWT tokens in API requests.
    + **API Keys**: Identifies APIs using static API keys and flags endpoints where key-based auth is insufficient for the data they expose.
    + **mTLS**: Supports mutual TLS for east-west service-to-service authentication — enforced via SPIFFE/SPIRE SVIDs for cryptographic workload identity.
    + **SAML**: Monitors SAML-authenticated API access patterns for anomalies.
    + **No Auth Detection**: Automatically flags APIs observed in production traffic with no authentication controls at all — regardless of what the spec claims.
    Risk scoring reflects the authentication posture of each endpoint — unauthenticated endpoints handling sensitive data are immediately elevated to critical priority.

    **References:**
    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)
    - [AccuKnox API Security Platform](https://accuknox.com/platform/api-security)
    - [API Security for Internal APIs](https://accuknox.com/blog/api-security-platforms-internal-apis)


??? "**14. Does AccuKnox API Security work with Kubernetes-native environments and service meshes?**"
    Yes. AccuKnox is designed from the ground up for Kubernetes-native and cloud-native API environments:
    + Native K8s integration captures all API traffic through the Kubernetes proxy layer — north-south ingress traffic and east-west pod-to-pod communication.
    + Istio sidecar integration provides full service mesh visibility including encrypted mTLS east-west traffic between services.
    + API inventory maps endpoints to Kubernetes namespaces, deployments, and service accounts — giving precise ownership and workload context for every endpoint.
    + KIEM (Kubernetes Identity and Entitlement Management) connects API access patterns to RBAC roles and service account permissions, surfacing over-privileged API consumers.
    + KubeArmor-based runtime enforcement enforces least-privilege API access policies at the kernel level — blocking unauthorized API calls before they complete.
    + Admission control integration prevents deployments that introduce shadow or misconfigured API endpoints from reaching production.

    **References:**
    - [Kubernetes Proxy Integration](https://help.accuknox.com/integrations/api-k8s/)
    - [Istio Integration](https://help.accuknox.com/integrations/api-istio/)
    - [API Security Use Case](https://help.accuknox.com/use-cases/api-security/)
    - [API Security for Internal APIs](https://accuknox.com/blog/api-security-platforms-internal-apis)

---

[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }