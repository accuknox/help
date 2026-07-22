---
title: AWS IAM Permissions Reference
description: The 403 read-only IAM permissions the AccuKnox CSPM scanner requests for AWS, with the reason and impact for each.
hide:
  - toc
---

# AWS IAM Permissions Reference

AccuKnox's AWS scanner uses **403 read-only IAM permissions** (`List`, `Describe`, and `Get` only) to inventory your resources and check their configuration. No write, delete, or data-download access, and it never reads object contents.

Review the full list below before onboarding. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [AWS prerequisites](cspm-prereq-aws.md) for setup steps.

!!! tip "How to use this reference"
    Permissions are grouped by service. **Hover** over any permission (or tap it on mobile, or focus it with the keyboard) to see the full rationale: what it does, why AccuKnox needs it, and what you lose if it is not granted. Use the **search box** to find a permission, service, or keyword, and the **service filter** to narrow the list.

<div class="iam-perms" data-src="../../assets/data/iam-perms-aws.json" markdown="0"></div>

## Permissions by service

How the 403 permissions break down across AWS services, split between asset-inventory reads and security-configuration checks.

| AWS Service | Total | Asset inventory | Security checks |
|---|---|---|---|
| Amazon EC2 | 39 | 26 | 13 |
| AWS IAM | 31 | 23 | 7 |
| Amazon S3 | 22 | 20 | 1 |
| Amazon RDS | 15 | 10 | 7 |
| AWS Backup | 14 | 13 | 1 |
| AWS Audit Manager | 9 | 8 | 1 |
| AWS CloudFormation | 9 | 8 | 1 |
| Amazon CloudFront | 9 | 8 | 0 |
| Elastic Load Balancing (ALB/NLB/CLB) | 9 | 5 | 4 |
| AWS CodeArtifact | 8 | 8 | 0 |
| AWS CloudTrail | 7 | 7 | 0 |
| Amazon DynamoDB | 7 | 7 | 0 |
| Amazon GuardDuty | 7 | 0 | 7 |
| AWS KMS | 7 | 6 | 1 |
| Amazon Redshift | 7 | 4 | 3 |
| AWS Config | 6 | 2 | 4 |
| AWS Lambda | 6 | 4 | 2 |
| Amazon Route 53 | 6 | 5 | 1 |
| Amazon Bedrock | 5 | 0 | 5 |
| Amazon ECS | 5 | 3 | 2 |
| Amazon ElastiCache | 5 | 2 | 3 |
| EC2 Image Builder | 5 | 0 | 0 |
| Amazon Redshift Serverless | 5 | 5 | 0 |
| Amazon SageMaker | 5 | 3 | 2 |
| Amazon SNS | 5 | 5 | 0 |
| AWS Systems Manager | 5 | 0 | 5 |
| Amazon WorkSpaces | 5 | 2 | 3 |
| IAM Access Analyzer | 4 | 4 | 0 |
| AWS Certificate Manager (ACM) | 4 | 4 | 0 |
| AWS App Mesh | 4 | 0 | 4 |
| Amazon EMR | 4 | 0 | 4 |
| Amazon CloudWatch Logs | 4 | 3 | 1 |
| AWS WAFv2 | 4 | 0 | 4 |
| ACM Private Certificate Authority | 3 | 3 | 0 |
| Amazon OpenSearch Serverless | 3 | 2 | 3 |
| Amazon EC2 Auto Scaling | 3 | 1 | 2 |
| Amazon CloudWatch | 3 | 3 | 1 |
| AWS CodePipeline | 3 | 3 | 0 |
| Amazon Connect | 3 | 2 | 3 |
| Amazon DynamoDB Accelerator (DAX) | 3 | 3 | 0 |
| Amazon DocumentDB (elastic clusters) | 3 | 3 | 0 |
| Amazon Managed Blockchain | 3 | 0 | 3 |
| AWS Organizations | 3 | 1 | 2 |
| Amazon Route 53 Domains | 3 | 3 | 0 |
| Amazon SES (email) | 3 | 0 | 1 |
| AWS Shield | 3 | 0 | 0 |
| Amazon SQS | 3 | 3 | 0 |
| Amazon Managed Workflows for Apache Airflow (MWAA) | 2 | 0 | 2 |
| AWS Amplify | 2 | 2 | 0 |
| AWS AppConfig | 2 | 0 | 2 |
| Amazon Athena | 2 | 0 | 2 |
| AWS CodeBuild | 2 | 2 | 0 |
| AWS CodeDeploy | 2 | 2 | 0 |
| Amazon Cognito Identity Pools | 2 | 2 | 0 |
| Amazon Cognito User Pools | 2 | 2 | 0 |
| Amazon Comprehend | 2 | 0 | 1 |
| Amazon Data Lifecycle Manager | 2 | 0 | 2 |
| Amazon ECR (container registry) | 2 | 0 | 2 |
| Amazon EKS | 2 | 2 | 0 |
| Amazon EventBridge | 2 | 0 | 2 |
| Amazon Kinesis Data Firehose | 2 | 0 | 2 |
| Amazon Forecast | 2 | 0 | 0 |
| AWS Glue | 2 | 0 | 2 |
| Amazon Kinesis Data Streams | 2 | 0 | 2 |
| Amazon MQ | 2 | 0 | 2 |
| AWS Secrets Manager | 2 | 0 | 2 |
| AWS Security Hub | 2 | 0 | 2 |
| AWS Resource Groups Tagging API | 2 | 0 | 2 |
| Amazon Timestream | 2 | 0 | 1 |
| Amazon API Gateway | 1 | 1 | 1 |
| Amazon AppFlow | 1 | 0 | 0 |
| AWS App Runner | 1 | 0 | 0 |
| AWS Compute Optimizer | 1 | 0 | 1 |
| AWS Glue DataBrew | 1 | 0 | 0 |
| Amazon DevOps Guru | 1 | 0 | 0 |
| AWS Database Migration Service | 1 | 0 | 1 |
| Amazon EFS | 1 | 0 | 1 |
| Amazon OpenSearch Service | 1 | 0 | 0 |
| Amazon FinSpace | 1 | 0 | 0 |
| Amazon Fraud Detector | 1 | 0 | 0 |
| Amazon FSx | 1 | 0 | 0 |
| Amazon S3 Glacier | 1 | 0 | 0 |
| Amazon HealthLake | 1 | 0 | 1 |
| AWS IoT SiteWise | 1 | 0 | 0 |
| Amazon MSK (Kafka) | 1 | 0 | 1 |
| Amazon Kendra | 1 | 0 | 0 |
| Amazon Kinesis Video Streams | 1 | 0 | 0 |
| Amazon Lex | 1 | 0 | 0 |
| Amazon Lookout for Equipment | 1 | 0 | 0 |
| Amazon MemoryDB | 1 | 0 | 0 |
| Amazon Connect Customer Profiles | 1 | 0 | 0 |
| AWS Proton | 1 | 0 | 0 |
| AWS Service Quotas | 1 | 0 | 1 |
| AWS STS | 1 | 0 | 1 |
| AWS Transfer Family | 1 | 0 | 1 |
| Amazon Translate | 1 | 0 | 0 |
| AWS WAF (Regional Classic) | 1 | 0 | 0 |
| AWS WAF (Classic) | 1 | 0 | 0 |
| AWS X-Ray | 1 | 0 | 0 |
