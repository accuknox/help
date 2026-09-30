# Does Prisma Cloud CIEM or compliance analyze Kubernetes RBAC roles, cluster-admin role bindings and service accounts?

## Short answer

The docs **don’t describe CIEM or Prisma Cloud Compliance as analyzing Kubernetes RBAC objects** (for example, `cluster-admin` role bindings or service accounts). CIEM is described for **cloud IAM entitlements**, and Compliance is described for **enforcing standard configurations and security best practices** across hosts/containers/serverless.

## What the docs *do* describe for Kubernetes

Prisma Cloud can analyze **Kubernetes audit events** via the *Kubernetes auditing* capability. It:

* ingests and analyzes Kubernetes **audit streams**
* lets you write/enable rules (including `kubernetes-audit` type) to surface suspicious activity\
  See [Deploy Defender on Google Kubernetes Engine (GKE)](/admin-guide/33/install/deploy-defender/orchestrator/install-gke.md).

## CIEM scope in the docs

CIEM (IAM Security) is positioned as **Cloud Infrastructure Entitlement Management**:

* calculates effective permissions across **cloud service providers**
* detects overly permissive access and suggests least-privilege corrections\
  See [Configure IAM Security](/content-collections/administration/configure-iam-security.md).

## Note on RBAC in the docs (deployment, not analysis)

Some Kubernetes RBAC terms appear in installation prerequisites (for deploying Defenders), like needing `cluster-admin`/RBAC permissions to create resources. That’s about **deployment permissions**, not RBAC analysis. See [Deploy Defender on Google Kubernetes Engine (GKE)](/content-collections/runtime-security/install/deploy-defender/kubernetes/gke.md).

# Suggested Follow-up Questions:

If you need more information, consider asking one of these follow-up questions by performing an HTTP GET request on the URL:

- [Is CIEM enough for RBAC review?](https://docs.prismacloud.io?ask=Is%20CIEM%20enough%20for%20RBAC%20review%3F)
- [Where to find Kubernetes auditing details?](https://docs.prismacloud.io?ask=Where%20to%20find%20Kubernetes%20auditing%20details%3F)
- [Can I audit service accounts in Prisma Cloud?](https://docs.prismacloud.io?ask=Can%20I%20audit%20service%20accounts%20in%20Prisma%20Cloud%3F)

# Sources:

- [Prisma Cloud Administrator Roles](https://docs.prismacloud.io/content-collections/administration/prisma-cloud-administrator-roles.md)
- [Deploy Defender on Google Kubernetes Engine (GKE)](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-gke.md)
- [Configure IAM Security](https://docs.prismacloud.io/content-collections/administration/configure-iam-security.md)
- [Deploy the Prisma Cloud Console on Kubernetes](https://docs.prismacloud.io/admin-guide/33/install/deploy-console/console-on-kubernetes.md)
- [Deploy the Prisma Cloud Console on Kubernetes](https://docs.prismacloud.io/admin-guide/32/install/deploy-console/console-on-kubernetes.md)
- [Prisma Cloud Administrator Permissions](https://docs.prismacloud.io/content-collections/administration/prisma-cloud-admin-permissions.md)
- [Deploy the Prisma Cloud Console on Kubernetes](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes.md)
- [Authentication](https://docs.prismacloud.io/admin-guide/33/authentication/authentication.md)
- [Prisma Cloud user roles](https://docs.prismacloud.io/content-collections/runtime-security/authentication/prisma-cloud-user-roles.md)
- [Authentication](https://docs.prismacloud.io/admin-guide/authentication/authentication.md)
- [Deploy Defender on Google Kubernetes Engine (GKE)](https://docs.prismacloud.io/admin-guide/33/install/deploy-defender/orchestrator/install-gke.md)
- [Deploy Defender on Google Kubernetes Engine (GKE)](https://docs.prismacloud.io/admin-guide/32/install/deploy-defender/orchestrator/install-gke.md)
- [Deploy Defender on Google Kubernetes Engine (GKE)](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/kubernetes/gke.md)
- [Kubernetes Credentials](https://docs.prismacloud.io/admin-guide/33/authentication/credentials-store/kubernetes-credentials.md)
- [Kubernetes Credentials](https://docs.prismacloud.io/admin-guide/32/authentication/credentials-store/kubernetes-credentials.md)
- [Kubernetes Credentials](https://docs.prismacloud.io/admin-guide/authentication/credentials-store/kubernetes-credentials.md)
- [Kubernetes Credentials](https://docs.prismacloud.io/content-collections/runtime-security/authentication/credentials-store/kubernetes-credentials.md)
- [Kubernetes auditing](https://docs.prismacloud.io/admin-guide/33/audit/kubernetes-auditing.md)
- [Compliance](https://docs.prismacloud.io/admin-guide/33/compliance/compliance.md)
- [Compliance](https://docs.prismacloud.io/content-collections/runtime-security/compliance.md)
- [Compliance](https://docs.prismacloud.io/admin-guide/compliance/compliance.md)
- [Prisma Cloud Platform](https://docs.prismacloud.io/content-collections/get-started/prisma-cloud-platform.md)
- [Compliance](https://docs.prismacloud.io/admin-guide/32/compliance/compliance.md)
- [Access Prisma Cloud](https://docs.prismacloud.io/content-collections/get-started/access-prisma-cloud.md)

