---
title: API Security Integrations
description: Overview of API Security capabilities and supported integrations.
hide:
  - toc
---


<style>
h2 {
  color: #000025;
  font-size: 1.5rem !important;
}
.nt-card .nt-card-image{
  color: #005BFF;

}

 .nt-card-title {
    text-align: -webkit-center;
}
</style>

# API Security Integrations

The **API Security** module provides deep visibility and continuous risk assessment for your APIs by analyzing live traffic, identifying unknown endpoints, and highlighting security exposures.

::cards:: cols=3

- title: AWS API Gateway
  image: ./aws-api-gateway.png
  url: ../integrations/api-aws.md
  description: Monitor and secure APIs running on AWS API Gateway

- title: K8s API Security Proxy
  image: ./k8s.png
  url: ../integrations/api-k8s.md
  description: Secure APIs in Kubernetes environments

- title: Istio
  image: ./istio.png
  url: ../integrations/api-istio.md
  description: Integrate with Istio service mesh for API security

- title: Nginx Ingress
  image: ./image-13.png
  url: ../integrations/api-nginx.md
  description: Protect APIs exposed via Nginx Ingress Controller

- title: F5
  image: https://logowik.com/content/uploads/images/f5-networks7669.jpg
  url: ../integrations/f5.md
  description: Secure APIs exposed via F5

- title: Kong
  image: ./kong-logo.svg
  url: ../integrations/kong.md
  description: Secure APIs managed by Kong Gateway

- title: Nginx Server
  image: ./nginx.png
  url:
  description: Secure APIs served by Nginx web server

- title: Azure API Management
  image: ./image-12.png
  url:
  description: Monitor APIs managed through Azure API Management

::/cards::



## Key Capabilities

- **Real-Time Inventory**: Automatically discovers APIs from traffic with risk scoring based on authentication, exposure, and sensitive data
- **Risk Detection**: Identifies Shadow, Zombie, and Orphan APIs through continuous traffic analysis
- **Logical Grouping**: Organize APIs for efficient tracking and management

!!! tip "**Use Cases**"
    Proceed to the [API Security Use Case](../use-cases/api-security.md) to learn how to view your API inventory, create collections, upload OpenAPI specifications, and scan for security findings.

![AccuKnox API Security integration overview](image-17.png)