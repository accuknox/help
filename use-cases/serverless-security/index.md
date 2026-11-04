---
title: Serverless Security Use Cases
description: Comprehensive security solutions for Serverless functions, images, and platforms including AWS Lambda and Knative.
---

# Serverless Security Use Cases

AccuKnox provides robust security for serverless architectures, ensuring visibility, compliance, and threat protection across functions and containerized serverless workloads.

AccuKnox delivers coverage for both function code and the underlying container images.

| Feature Area | Security Checks & Objectives |
| :--- | :--- |
| **Function Scan** | **Least Permissive IAM**: Analyze and enforce least privilege principles for function roles.<br>**Secrets Detection**: Scan function code for hardcoded secrets, keys, and tokens.<br>**Permissions Audit**: Ensure Block Public ACL and verify associated S3 security. |
| **Image Scan** | **Vulnerability Management**: Identify CVEs in serverless container images.<br>**Sensitive Data**: Detect embedded keys, passwords, and PII/PHI in image layers.<br>**Supply Chain**: Verify build pipeline integrity and base image security. |

## AWS Lambda Security

Beyond the function code, AccuKnox secures the deployment configuration and the ecosystem of connected services.

### Accessory Services Scanning

Ensure security for services that trigger or are triggered by Lambda functions.

| Service | Best Practices Checked |
| :--- | :--- |
| **Amazon S3** | • Verify buckets are not publicly readable/writable.<br>• Confirm Server-Side Encryption (SSE) is enabled. |
| **Amazon SQS & SNS** | • Validate encryption settings.<br>• Audit access policies. |

### Deployment Security

!!! check "Configuration Validation"
    *   **Template Scanning**: Validate `serverless.yml` or CloudFormation templates against security policies.
    *   **Access Control**: Ensure least-permissive access requirements are met before deployment.

### Example: Securing AWS Serverless Resources

The following `serverless.yml` snippet demonstrates a typical detailed configuration that AccuKnox can audit for misconfigurations (e.g., Public ACLs, missing encryption).

```yaml
service: appMicroservice
provider: aws

functions:
  myFunc:
    name: appus
    tags:
      RESOURCE: lambda
      PUBLIC: false
    iamRoleStatements:
      - Effect: Allow
        Action:
          - "lambda:InvokeFunction"
        Resource:
          - "arn:aws:lambda:#{AWS::Region}:#{AWS::AccountId}:function:invokedLambda"
    handler: Handler.requesthandle
    timeout: 300
    memorySize: 120

resources: # CloudFormation template
  Resources:
    S3BucketPublicRead:
      # AccuKnox flags if AccessControl is 'PublicRead' without justification
      Type: AWS::S3::Bucket
      Properties:
        AccessControl: PublicRead
        BucketEncryption:
          ServerSideEncryptionConfiguration:
            - ServerSideEncryptionByDefault:
                SSEAlgorithm: AES256
```

## Knative Serverless Security

For Kubernetes-native serverless models, AccuKnox leverages advanced runtime enforcement.

!!! info "Runtime Features"
    *   **Function Visibility**: Gain deep insights into function execution and network behavior.
    *   **Knative Security Guard**: Unlike traditional heavy sidecars, AccuKnox uses a lightweight model (via KubeArmor/eBPF) for per-node enforcement, offering superior performance.
    *   **Continuous Scanning**: Ongoing security assessment of the Knative cluster and served images.

## SecOps & Compliance

!!! success "Benefits & Outcomes"
    *   **Unified Dashboard**: Integrate Lambda function findings directly into your central security dashboard.
    *   **Policy Refinement**: Receive automatic suggestions for least-permissive access policies.
    *   **Data Protection**: Continuous verification of encryption (SSE) and public access blocks across all serverless assets.
