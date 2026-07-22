---
title: AWS IAM Permissions Reference
description: The 403 read-only IAM permissions the AccuKnox CSPM scanner requests for AWS, with the reason for each.
hide:
  - toc
---

# AWS IAM Permissions Reference

AccuKnox's AWS scanner uses **403 read-only IAM permissions** (`List`, `Describe`, and `Get` only) to inventory your resources and check their configuration. No write, delete, or data-download access, and it never reads object contents.

See the [overview](cspm-permissions-overview.md) to compare clouds, or the [AWS prerequisites](cspm-prereq-aws.md) for setup steps.

!!! tip "Reading this reference"
    Permissions are grouped by service; ones that serve the same purpose share a row. Hover (or tap) the **ⓘ** badge to see why AccuKnox needs each one.

<div class="iam-tables" markdown="1">

## IAM Access Analyzer (4)

| Permission | What it does |
|---|---|
| `access-analyzer:GetAnalyzer` | Read details of a specific IAM Access Analyzer resource in your account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers.">Why</span> |
| `access-analyzer:GetFinding` | Read details of a specific IAM Access Analyzer finding (external access or unused access). <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer findings.">Why</span> |
| `access-analyzer:ListAnalyzers` | List IAM Access Analyzer resources or findings in your account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers.">Why</span> |
| `access-analyzer:ListFindings` | List IAM Access Analyzer resources or findings in your account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers, IAM Access Analyzer findings.">Why</span> |

## ACM Private Certificate Authority (3)

| Permission | What it does |
|---|---|
| `acm-pca:DescribeCertificateAuthority` | Read-only permission to view configuration details for ACM Private Certificate Authority resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your acmpca certificate authority.">Why</span> |
| `acm-pca:ListCertificateAuthorities` `acm-pca:ListTags` | Read-only permission to list ACM Private Certificate Authority resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your acmpca certificate authority.">Why</span> |

## AWS Certificate Manager (ACM) (4)

| Permission | What it does |
|---|---|
| `acm:DescribeCertificate` | Read-only permission to view configuration details for AWS Certificate Manager (ACM) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates.">Why</span> |
| `acm:GetCertificate` | Read-only permission to read settings and metadata for AWS Certificate Manager (ACM) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates.">Why</span> |
| `acm:ListCertificates` `acm:ListTagsForCertificate` | Read-only permission to list AWS Certificate Manager (ACM) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates.">Why</span> |

## Amazon Managed Workflows for Apache Airflow (MWAA) (2)

| Permission | What it does |
|---|---|
| `airflow:GetEnvironment` | Read-only permission to read settings and metadata for Amazon Managed Workflows for Apache Airflow (MWAA) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Managed Workflows for Apache Airflow (MWAA) security settings against common misconfiguration and compliance checks.">Why</span> |
| `airflow:ListEnvironments` | Read-only permission to list Amazon Managed Workflows for Apache Airflow (MWAA) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Managed Workflows for Apache Airflow (MWAA) security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Amplify (2)

| Permission | What it does |
|---|---|
| `amplify:GetApp` | Read-only permission to read settings and metadata for AWS Amplify resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your amplify app.">Why</span> |
| `amplify:ListApps` | Read-only permission to list AWS Amplify resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your amplify app.">Why</span> |

## Amazon OpenSearch Serverless (3)

| Permission | What it does |
|---|---|
| `aoss:GetSecurityPolicy` | Read-only permission to read settings and metadata for Amazon OpenSearch Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon OpenSearch Serverless asset inventory. AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks.">Why</span> |
| `aoss:ListCollections` | Read-only permission to list Amazon OpenSearch Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks.">Why</span> |
| `aoss:ListSecurityPolicies` | Read-only permission to list Amazon OpenSearch Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon OpenSearch Serverless asset inventory. AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon API Gateway (1)

| Permission | What it does |
|---|---|
| `apigateway:GET` | Read-only access to read configuration for Amazon API Gateway resources (APIs, stages, methods, and related settings). <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon API Gateway asset inventory. AccuKnox uses this to evaluate Amazon API Gateway security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS AppConfig (2)

| Permission | What it does |
|---|---|
| `appconfig:ListApplications` `appconfig:ListConfigurationProfiles` | Read-only permission to list AWS AppConfig resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS AppConfig security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon AppFlow (1)

| Permission | What it does |
|---|---|
| `appflow:ListFlows` | Read-only permission to list Amazon AppFlow resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon AppFlow during security and inventory scans.">Why</span> |

## AWS App Mesh (4)

| Permission | What it does |
|---|---|
| `appmesh:DescribeMesh` `appmesh:DescribeVirtualGateway` | Read-only permission to view configuration details for AWS App Mesh resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks.">Why</span> |
| `appmesh:ListMeshes` `appmesh:ListVirtualGateways` | Read-only permission to list AWS App Mesh resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS App Runner (1)

| Permission | What it does |
|---|---|
| `apprunner:ListServices` | Read-only permission to list AWS App Runner resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS App Runner during security and inventory scans.">Why</span> |

## Amazon Athena (2)

| Permission | What it does |
|---|---|
| `athena:GetWorkGroup` | Read-only permission to read settings and metadata for Amazon Athena resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Athena security settings against common misconfiguration and compliance checks.">Why</span> |
| `athena:ListWorkGroups` | Read-only permission to list Amazon Athena resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Athena security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Audit Manager (9)

| Permission | What it does |
|---|---|
| `auditmanager:GetAssessment` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager assessment.">Why</span> |
| `auditmanager:GetAssessmentFramework` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager framework.">Why</span> |
| `auditmanager:GetEvidence` `auditmanager:GetEvidenceByEvidenceFolder` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence.">Why</span> |
| `auditmanager:GetEvidenceFolder` `auditmanager:GetEvidenceFoldersByAssessment` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence folder.">Why</span> |
| `auditmanager:GetSettings` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Audit Manager security settings against common misconfiguration and compliance checks.">Why</span> |
| `auditmanager:ListAssessmentFrameworks` | Read-only permission to list AWS Audit Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager framework.">Why</span> |
| `auditmanager:ListAssessments` | Read-only permission to list AWS Audit Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager assessment, auditmanager evidence, auditmanager evidence folder.">Why</span> |

## Amazon EC2 Auto Scaling (3)

| Permission | What it does |
|---|---|
| `autoscaling:DescribeAutoScalingGroups` `autoscaling:DescribeNotificationConfigurations` | Read-only permission to view configuration details for Amazon EC2 Auto Scaling resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon EC2 Auto Scaling security settings against common misconfiguration and compliance checks.">Why</span> |
| `autoscaling:DescribeLaunchConfigurations` | Read-only permission to view configuration details for Amazon EC2 Auto Scaling resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch configuration.">Why</span> |

## AWS Backup (14)

| Permission | What it does |
|---|---|
| `backup:DescribeBackupJob` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup jobs.">Why</span> |
| `backup:DescribeBackupVault` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults.">Why</span> |
| `backup:DescribeRecoveryPoint` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your backup recovery point.">Why</span> |
| `backup:DescribeRegionSettings` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Backup security settings against common misconfiguration and compliance checks.">Why</span> |
| `backup:GetBackupPlan` | Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans.">Why</span> |
| `backup:GetBackupSelection` | Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your backup selection.">Why</span> |
| `backup:GetBackupVaultAccessPolicy` `backup:GetBackupVaultNotifications` | Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults.">Why</span> |
| `backup:ListBackupJobs` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup jobs.">Why</span> |
| `backup:ListBackupPlans` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans.">Why</span> |
| `backup:ListBackupSelections` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your backup selection.">Why</span> |
| `backup:ListBackupVaults` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults.">Why</span> |
| `backup:ListRecoveryPointsByBackupVault` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your backup recovery point.">Why</span> |
| `backup:ListTags` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans, AWS Backup vaults, backup recovery point.">Why</span> |

## Amazon Bedrock (5)

| Permission | What it does |
|---|---|
| `bedrock:GetCustomModel` `bedrock:GetModelCustomizationJob` `bedrock:GetModelInvocationLoggingConfiguration` | Read-only permission to read settings and metadata for Amazon Bedrock resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks.">Why</span> |
| `bedrock:ListCustomModels` `bedrock:ListModelCustomizationJobs` | Read-only permission to list Amazon Bedrock resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS CloudFormation (9)

| Permission | What it does |
|---|---|
| `cloudformation:DescribeStackEvents` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS CloudFormation security settings against common misconfiguration and compliance checks.">Why</span> |
| `cloudformation:DescribeStackResource` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack resource.">Why</span> |
| `cloudformation:DescribeStackResources` `cloudformation:DescribeStacks` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks.">Why</span> |
| `cloudformation:DescribeStackSet` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack set.">Why</span> |
| `cloudformation:GetTemplate` | Read-only permission to read settings and metadata for AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks.">Why</span> |
| `cloudformation:ListStackResources` | Read-only permission to list AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack resource.">Why</span> |
| `cloudformation:ListStackSets` | Read-only permission to list AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack set.">Why</span> |
| `cloudformation:ListStacks` | Read-only permission to list AWS CloudFormation resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks, cloudformation stack resource.">Why</span> |

## Amazon CloudFront (9)

| Permission | What it does |
|---|---|
| `cloudfront:DescribeFunction` | Read-only permission to view configuration details for Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront function.">Why</span> |
| `cloudfront:GetCachePolicy` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront cache policy.">Why</span> |
| `cloudfront:GetDistribution` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFront distributions.">Why</span> |
| `cloudfront:GetDistributionConfig` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon CloudFront during security and inventory scans.">Why</span> |
| `cloudfront:GetFunction` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon CloudFront asset inventory.">Why</span> |
| `cloudfront:ListCachePolicies` | Read-only permission to list Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront cache policy.">Why</span> |
| `cloudfront:ListDistributions` `cloudfront:ListTagsForResource` | Read-only permission to list Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFront distributions.">Why</span> |
| `cloudfront:ListFunctions` | Read-only permission to list Amazon CloudFront resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront function.">Why</span> |

## AWS CloudTrail (7)

| Permission | What it does |
|---|---|
| `cloudtrail:DescribeTrails` | Read-only permission to view configuration details for CloudTrail trails and logging settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails.">Why</span> |
| `cloudtrail:GetChannel` | Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudtrail channel.">Why</span> |
| `cloudtrail:GetEventSelectors` `cloudtrail:GetInsightSelectors` `cloudtrail:GetTrailStatus` | Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails.">Why</span> |
| `cloudtrail:ListChannels` | Read-only permission to list CloudTrail trails and logging settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudtrail channel.">Why</span> |
| `cloudtrail:ListTags` | Read-only permission to list CloudTrail trails and logging settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails.">Why</span> |

## Amazon CloudWatch (3)

| Permission | What it does |
|---|---|
| `cloudwatch:DescribeAlarms` | Read-only permission to view configuration details for CloudWatch alarms and metrics in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudwatch alarm.">Why</span> |
| `cloudwatch:GetMetricStatistics` | Read-only permission to read settings and metadata for CloudWatch alarms and metrics in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon CloudWatch asset inventory. AccuKnox uses this to evaluate Amazon CloudWatch security settings against common misconfiguration and compliance checks.">Why</span> |
| `cloudwatch:ListTagsForResource` | Read-only permission to list CloudWatch alarms and metrics in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudwatch alarm.">Why</span> |

## AWS CodeArtifact (8)

| Permission | What it does |
|---|---|
| `codeartifact:DescribeDomain` | Read-only permission to view configuration details for AWS CodeArtifact resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain.">Why</span> |
| `codeartifact:DescribeRepository` | Read-only permission to view configuration details for AWS CodeArtifact resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository.">Why</span> |
| `codeartifact:GetDomainPermissionsPolicy` | Read-only permission to read settings and metadata for AWS CodeArtifact resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain.">Why</span> |
| `codeartifact:GetRepositoryEndpoint` `codeartifact:GetRepositoryPermissionsPolicy` | Read-only permission to read settings and metadata for AWS CodeArtifact resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository.">Why</span> |
| `codeartifact:ListDomains` | Read-only permission to list AWS CodeArtifact resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain.">Why</span> |
| `codeartifact:ListRepositories` | Read-only permission to list AWS CodeArtifact resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository.">Why</span> |
| `codeartifact:ListTagsForResource` | Read-only permission to list AWS CodeArtifact resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain, codeartifact repository.">Why</span> |

## AWS CodeBuild (2)

| Permission | What it does |
|---|---|
| `codebuild:BatchGetProjects` | Read-only permission to read details for AWS CodeBuild resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codebuild project.">Why</span> |
| `codebuild:ListProjects` | Read-only permission to list AWS CodeBuild resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codebuild project.">Why</span> |

## AWS CodeDeploy (2)

| Permission | What it does |
|---|---|
| `codedeploy:GetDeploymentConfig` | Read-only permission to read settings and metadata for AWS CodeDeploy resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codedeploy deployment config.">Why</span> |
| `codedeploy:ListDeploymentConfigs` | Read-only permission to list AWS CodeDeploy resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codedeploy deployment config.">Why</span> |

## AWS CodePipeline (3)

| Permission | What it does |
|---|---|
| `codepipeline:GetPipeline` | Read-only permission to read settings and metadata for AWS CodePipeline resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codepipeline pipeline.">Why</span> |
| `codepipeline:ListPipelines` `codepipeline:ListTagsForResource` | Read-only permission to list AWS CodePipeline resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your codepipeline pipeline.">Why</span> |

## Amazon Cognito Identity Pools (2)

| Permission | What it does |
|---|---|
| `cognito-identity:DescribeIdentityPool` | Read-only permission to view configuration details for Amazon Cognito Identity Pools resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito identity pool.">Why</span> |
| `cognito-identity:ListIdentityPools` | Read-only permission to list Amazon Cognito Identity Pools resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito identity pool.">Why</span> |

## Amazon Cognito User Pools (2)

| Permission | What it does |
|---|---|
| `cognito-idp:DescribeUserPool` | Read-only permission to view configuration details for Amazon Cognito User Pools resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito user pool.">Why</span> |
| `cognito-idp:ListUserPools` | Read-only permission to list Amazon Cognito User Pools resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito user pool.">Why</span> |

## Amazon Comprehend (2)

| Permission | What it does |
|---|---|
| `comprehend:ListFlywheels` | Read-only permission to list Amazon Comprehend resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Comprehend during security and inventory scans.">Why</span> |
| `comprehend:ListSentimentDetectionJobs` | List Amazon Comprehend sentiment analysis jobs in your account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox checks whether Comprehend jobs use encryption for stored data and output.">Why</span> |

## AWS Compute Optimizer (1)

| Permission | What it does |
|---|---|
| `compute-optimizer:GetRecommendationSummaries` | Read-only permission to read settings and metadata for AWS Compute Optimizer resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Compute Optimizer security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Config (6)

| Permission | What it does |
|---|---|
| `config:DescribeConfigRules` `config:DescribeDeliveryChannels` | Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks.">Why</span> |
| `config:DescribeConfigurationRecorderStatus` `config:DescribeConfigurationRecorders` | Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Config recorders.">Why</span> |
| `config:GetComplianceDetailsByConfigRule` `config:GetDiscoveredResourceCounts` | Read-only permission to read settings and metadata for AWS Config rules and recorders in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Connect (3)

| Permission | What it does |
|---|---|
| `connect:DescribeInstanceStorageConfig` | Read-only permission to view configuration details for Amazon Connect resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon Connect asset inventory. AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks.">Why</span> |
| `connect:ListInstanceStorageConfigs` | Read-only permission to list Amazon Connect resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon Connect asset inventory. AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks.">Why</span> |
| `connect:ListInstances` | Read-only permission to list Amazon Connect resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Glue DataBrew (1)

| Permission | What it does |
|---|---|
| `databrew:ListJobs` | Read-only permission to list AWS Glue DataBrew resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Glue DataBrew during security and inventory scans.">Why</span> |

## Amazon DynamoDB Accelerator (DAX) (3)

| Permission | What it does |
|---|---|
| `dax:DescribeClusters` | Read-only permission to view configuration details for Amazon DynamoDB Accelerator (DAX) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your dax cluster.">Why</span> |
| `dax:DescribeSubnetGroups` | Read-only permission to view configuration details for Amazon DynamoDB Accelerator (DAX) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your dax subnet group.">Why</span> |
| `dax:ListTags` | Read-only permission to list Amazon DynamoDB Accelerator (DAX) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your dax cluster.">Why</span> |

## Amazon DevOps Guru (1)

| Permission | What it does |
|---|---|
| `devops-guru:ListNotificationChannels` | Read-only permission to list Amazon DevOps Guru resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon DevOps Guru during security and inventory scans.">Why</span> |

## Amazon Data Lifecycle Manager (2)

| Permission | What it does |
|---|---|
| `dlm:GetLifecyclePolicies` `dlm:GetLifecyclePolicy` | Read-only permission to read settings and metadata for Amazon Data Lifecycle Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Data Lifecycle Manager security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Database Migration Service (1)

| Permission | What it does |
|---|---|
| `dms:DescribeReplicationInstances` | Read-only permission to view configuration details for AWS Database Migration Service resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Database Migration Service security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon DocumentDB (elastic clusters) (3)

| Permission | What it does |
|---|---|
| `docdb-elastic:GetCluster` | Read-only permission to read settings and metadata for Amazon DocumentDB (elastic clusters) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster.">Why</span> |
| `docdb-elastic:ListClusters` | Read-only permission to list Amazon DocumentDB (elastic clusters) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster.">Why</span> |
| `docdb-elastic:ListTagsForResource` | Read-only permission to list Amazon DocumentDB (elastic clusters) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster, docdb cluster snapshot.">Why</span> |

## Amazon DynamoDB (7)

| Permission | What it does |
|---|---|
| `dynamodb:DescribeBackup` | Read-only permission to view configuration details for DynamoDB tables in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your dynamodb backup.">Why</span> |
| `dynamodb:DescribeContinuousBackups` `dynamodb:DescribeKinesisStreamingDestination` `dynamodb:DescribeTable` | Read-only permission to view configuration details for DynamoDB tables in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables.">Why</span> |
| `dynamodb:ListBackups` | Read-only permission to list DynamoDB tables in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your dynamodb backup.">Why</span> |
| `dynamodb:ListTables` `dynamodb:ListTagsOfResource` | Read-only permission to list DynamoDB tables in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables.">Why</span> |

## Amazon EC2 (39)

| Permission | What it does |
|---|---|
| `ec2:DescribeAccountAttributes` `ec2:DescribeEgressOnlyInternetGateways` `ec2:DescribeFlowLogs` `ec2:DescribeImages` `ec2:DescribeInternetGateways` `ec2:DescribeVpcEndpointServicePermissions` `ec2:DescribeVpcEndpointServices` `ec2:DescribeVpcEndpoints` `ec2:DescribeVpcPeeringConnections` `ec2:DescribeVpnConnections` `ec2:DescribeVpnGateways` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks.">Why</span> |
| `ec2:DescribeAddresses` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your vpc eip.">Why</span> |
| `ec2:DescribeInstanceAttribute` `ec2:DescribeInstanceCreditSpecifications` `ec2:DescribeInstanceStatus` `ec2:DescribeInstances` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances).">Why</span> |
| `ec2:DescribeInstanceTypeOfferings` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 instance availability.">Why</span> |
| `ec2:DescribeKeyPairs` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 key pair.">Why</span> |
| `ec2:DescribeLaunchTemplateVersions` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch template version.">Why</span> |
| `ec2:DescribeLaunchTemplates` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch template.">Why</span> |
| `ec2:DescribeManagedPrefixLists` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 managed prefix list.">Why</span> |
| `ec2:DescribeNatGateways` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC NAT gateways.">Why</span> |
| `ec2:DescribeNetworkAcls` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC network ACLs.">Why</span> |
| `ec2:DescribeNetworkInterfaces` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 network interface.">Why</span> |
| `ec2:DescribeRegions` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS regions.">Why</span> |
| `ec2:DescribeReservedInstances` `ec2:DescribeReservedInstancesModifications` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 reserved instance.">Why</span> |
| `ec2:DescribeRouteTables` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC route tables.">Why</span> |
| `ec2:DescribeSecurityGroupRules` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your vpc security group rule.">Why</span> |
| `ec2:DescribeSecurityGroups` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC security groups, vpc security group rule.">Why</span> |
| `ec2:DescribeSnapshotAttribute` `ec2:DescribeSnapshots` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs snapshot.">Why</span> |
| `ec2:DescribeSubnets` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC subnets.">Why</span> |
| `ec2:DescribeVolumeAttribute` `ec2:DescribeVolumes` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs volume.">Why</span> |
| `ec2:DescribeVpcs` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC networks.">Why</span> |
| `ec2:GetEbsDefaultKmsKeyId` `ec2:GetEbsEncryptionByDefault` | Read-only permission to read settings and metadata for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks.">Why</span> |
| `ec2:GetLaunchTemplateData` | Read-only permission to read settings and metadata for EC2 compute and networking resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances).">Why</span> |

## Amazon ECR (container registry) (2)

| Permission | What it does |
|---|---|
| `ecr:DescribeRepositories` | Read-only permission to view configuration details for Amazon ECR (container registry) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon ECR (container registry) security settings against common misconfiguration and compliance checks.">Why</span> |
| `ecr:GetRepositoryPolicy` | Read-only permission to read settings and metadata for Amazon ECR (container registry) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon ECR (container registry) security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon ECS (5)

| Permission | What it does |
|---|---|
| `ecs:DescribeClusters` | Read-only permission to view configuration details for ECS clusters and services in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ECS clusters.">Why</span> |
| `ecs:DescribeServices` | Read-only permission to view configuration details for ECS clusters and services in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon ECS security settings against common misconfiguration and compliance checks.">Why</span> |
| `ecs:ListClusters` `ecs:ListTagsForResource` | Read-only permission to list ECS clusters and services in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ECS clusters.">Why</span> |
| `ecs:ListServices` | Read-only permission to list ECS clusters and services in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon ECS security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon EKS (2)

| Permission | What it does |
|---|---|
| `eks:DescribeCluster` | Read-only permission to view configuration details for EKS Kubernetes clusters in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your EKS Kubernetes clusters.">Why</span> |
| `eks:ListClusters` | Read-only permission to list EKS Kubernetes clusters in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your EKS Kubernetes clusters.">Why</span> |

## Amazon ElastiCache (5)

| Permission | What it does |
|---|---|
| `elasticache:DescribeCacheClusters` | Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ElastiCache clusters.">Why</span> |
| `elasticache:DescribeCacheSubnetGroups` `elasticache:DescribeReplicationGroups` `elasticache:DescribeReservedCacheNodes` | Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon ElastiCache security settings against common misconfiguration and compliance checks.">Why</span> |
| `elasticache:ListTagsForResource` | Read-only permission to list Amazon ElastiCache resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your ElastiCache clusters.">Why</span> |

## Amazon EFS (1)

| Permission | What it does |
|---|---|
| `elasticfilesystem:DescribeFileSystems` | Read-only permission to view configuration details for Amazon EFS resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon EFS security settings against common misconfiguration and compliance checks.">Why</span> |

## Elastic Load Balancing (ALB/NLB/CLB) (9)

| Permission | What it does |
|---|---|
| `elasticloadbalancing:DescribeInstanceHealth` `elasticloadbalancing:DescribeListeners` `elasticloadbalancing:DescribeLoadBalancerPolicies` `elasticloadbalancing:DescribeTargetGroupAttributes` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Elastic Load Balancing (ALB/NLB/CLB) security settings against common misconfiguration and compliance checks.">Why</span> |
| `elasticloadbalancing:DescribeLoadBalancerAttributes` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers.">Why</span> |
| `elasticloadbalancing:DescribeLoadBalancers` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers, ec2 load balancer listener.">Why</span> |
| `elasticloadbalancing:DescribeTags` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers, load balancer target groups.">Why</span> |
| `elasticloadbalancing:DescribeTargetGroups` `elasticloadbalancing:DescribeTargetHealth` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your load balancer target groups.">Why</span> |

## Amazon EMR (4)

| Permission | What it does |
|---|---|
| `elasticmapreduce:DescribeCluster` `elasticmapreduce:DescribeSecurityConfiguration` | Read-only permission to view configuration details for Amazon EMR resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks.">Why</span> |
| `elasticmapreduce:ListClusters` `elasticmapreduce:ListInstanceGroups` | Read-only permission to list Amazon EMR resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon OpenSearch Service (1)

| Permission | What it does |
|---|---|
| `es:ListDomainNames` | Read-only permission to list Amazon OpenSearch Service resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon OpenSearch Service during security and inventory scans.">Why</span> |

## Amazon EventBridge (2)

| Permission | What it does |
|---|---|
| `events:ListEventBuses` `events:ListRules` | Read-only permission to list Amazon EventBridge resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon EventBridge security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon FinSpace (1)

| Permission | What it does |
|---|---|
| `finspace:ListEnvironments` | Read-only permission to list Amazon FinSpace resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon FinSpace during security and inventory scans.">Why</span> |

## Amazon Kinesis Data Firehose (2)

| Permission | What it does |
|---|---|
| `firehose:DescribeDeliveryStream` | Read-only permission to view configuration details for Amazon Kinesis Data Firehose resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Kinesis Data Firehose security settings against common misconfiguration and compliance checks.">Why</span> |
| `firehose:ListDeliveryStreams` | Read-only permission to list Amazon Kinesis Data Firehose resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Kinesis Data Firehose security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Forecast (2)

| Permission | What it does |
|---|---|
| `forecast:ListDatasets` `forecast:ListForecastExportJobs` | Read-only permission to list Amazon Forecast resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Forecast during security and inventory scans.">Why</span> |

## Amazon Fraud Detector (1)

| Permission | What it does |
|---|---|
| `frauddetector:GetDetectors` | Read-only permission to read settings and metadata for Amazon Fraud Detector resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Fraud Detector during security and inventory scans.">Why</span> |

## Amazon FSx (1)

| Permission | What it does |
|---|---|
| `fsx:DescribeFileSystems` | Read-only permission to view configuration details for Amazon FSx resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon FSx during security and inventory scans.">Why</span> |

## Amazon S3 Glacier (1)

| Permission | What it does |
|---|---|
| `glacier:ListVaults` | Read-only permission to list Amazon S3 Glacier resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon S3 Glacier during security and inventory scans.">Why</span> |

## AWS Glue (2)

| Permission | What it does |
|---|---|
| `glue:GetDataCatalogEncryptionSettings` `glue:GetSecurityConfigurations` | Read-only permission to read settings and metadata for AWS Glue resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Glue security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon GuardDuty (7)

| Permission | What it does |
|---|---|
| `guardduty:DescribePublishingDestination` | Read-only permission to view configuration details for GuardDuty threat detection settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks.">Why</span> |
| `guardduty:GetDetector` `guardduty:GetFindings` `guardduty:GetMasterAccount` | Read-only permission to read settings and metadata for GuardDuty threat detection settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks.">Why</span> |
| `guardduty:ListDetectors` `guardduty:ListFindings` `guardduty:ListPublishingDestinations` | Read-only permission to list GuardDuty threat detection settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon HealthLake (1)

| Permission | What it does |
|---|---|
| `healthlake:ListFHIRDatastores` | Read-only permission to list Amazon HealthLake resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon HealthLake security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS IAM (31)

| Permission | What it does |
|---|---|
| `iam:GenerateCredentialReport` | Request generation of the IAM credential report (password age, access key rotation, MFA status). <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks.">Why</span> |
| `iam:GetAccountPasswordPolicy` `iam:GetAccountSummary` `iam:GetUserPolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks.">Why</span> |
| `iam:GetCredentialReport` | Download the IAM credential report after it has been generated. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS IAM during security and inventory scans.">Why</span> |
| `iam:GetGroup` `iam:GetGroupPolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups.">Why</span> |
| `iam:GetLoginProfile` `iam:GetUser` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users.">Why</span> |
| `iam:GetPolicy` `iam:GetPolicyVersion` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM customer-managed policies, attached aws iam policy.">Why</span> |
| `iam:GetRole` `iam:GetRolePolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles.">Why</span> |
| `iam:ListAccountAliases` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS account metadata.">Why</span> |
| `iam:ListAttachedGroupPolicies` `iam:ListGroupPolicies` `iam:ListGroups` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups.">Why</span> |
| `iam:ListAttachedRolePolicies` `iam:ListInstanceProfilesForRole` `iam:ListRolePolicies` `iam:ListRoles` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles.">Why</span> |
| `iam:ListAttachedUserPolicies` `iam:ListGroupsForUser` `iam:ListMFADevices` `iam:ListUserPolicies` `iam:ListUsers` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users.">Why</span> |
| `iam:ListEntitiesForPolicy` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your iam policy attachment.">Why</span> |
| `iam:ListPolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM customer-managed policies, attached aws iam policy.">Why</span> |
| `iam:ListSSHPublicKeys` `iam:ListServerCertificates` `iam:ListVirtualMFADevices` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks.">Why</span> |

## EC2 Image Builder (5)

| Permission | What it does |
|---|---|
| `imagebuilder:ListComponents` `imagebuilder:ListContainerRecipes` `imagebuilder:ListImagePipelines` `imagebuilder:ListImageRecipes` `imagebuilder:ListInfrastructureConfigurations` | Read-only permission to list EC2 Image Builder resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of EC2 Image Builder during security and inventory scans.">Why</span> |

## AWS IoT SiteWise (1)

| Permission | What it does |
|---|---|
| `iotsitewise:DescribeDefaultEncryptionConfiguration` | Read-only permission to view configuration details for AWS IoT SiteWise resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS IoT SiteWise during security and inventory scans.">Why</span> |

## Amazon MSK (Kafka) (1)

| Permission | What it does |
|---|---|
| `kafka:ListClusters` | Read-only permission to list Amazon MSK (Kafka) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon MSK (Kafka) security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Kendra (1)

| Permission | What it does |
|---|---|
| `kendra:ListIndices` | Read-only permission to list Amazon Kendra resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Kendra during security and inventory scans.">Why</span> |

## Amazon Kinesis Data Streams (2)

| Permission | What it does |
|---|---|
| `kinesis:DescribeStream` | Read-only permission to view configuration details for Amazon Kinesis Data Streams resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Kinesis Data Streams security settings against common misconfiguration and compliance checks.">Why</span> |
| `kinesis:ListStreams` | Read-only permission to list Amazon Kinesis Data Streams resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Kinesis Data Streams security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Kinesis Video Streams (1)

| Permission | What it does |
|---|---|
| `kinesisvideo:ListStreams` | Read-only permission to list Amazon Kinesis Video Streams resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Kinesis Video Streams during security and inventory scans.">Why</span> |

## AWS KMS (7)

| Permission | What it does |
|---|---|
| `kms:DescribeKey` | Read-only permission to view configuration details for KMS encryption keys in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys.">Why</span> |
| `kms:GetKeyPolicy` `kms:GetKeyRotationStatus` | Read-only permission to read settings and metadata for KMS encryption keys in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys.">Why</span> |
| `kms:ListAliases` `kms:ListKeys` `kms:ListResourceTags` | Read-only permission to list KMS encryption keys in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys.">Why</span> |
| `kms:ListGrants` | Read-only permission to list KMS encryption keys in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS KMS security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Lambda (6)

| Permission | What it does |
|---|---|
| `lambda:GetFunction` `lambda:GetFunctionUrlConfig` `lambda:GetPolicy` | Read-only permission to read settings and metadata for Lambda functions in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions.">Why</span> |
| `lambda:GetFunctionCodeSigningConfig` `lambda:GetFunctionConfiguration` | Read-only permission to read settings and metadata for Lambda functions in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Lambda security settings against common misconfiguration and compliance checks.">Why</span> |
| `lambda:ListFunctions` | Read-only permission to list Lambda functions in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions.">Why</span> |

## Amazon Lex (1)

| Permission | What it does |
|---|---|
| `lex:ListBots` | Read-only permission to list Amazon Lex resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Lex during security and inventory scans.">Why</span> |

## Amazon CloudWatch Logs (4)

| Permission | What it does |
|---|---|
| `logs:DescribeLogGroups` | Read-only permission to view configuration details for CloudWatch Logs log groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups.">Why</span> |
| `logs:DescribeMetricFilters` | Read-only permission to view configuration details for CloudWatch Logs log groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon CloudWatch Logs security settings against common misconfiguration and compliance checks.">Why</span> |
| `logs:GetDataProtectionPolicy` | Read-only permission to read settings and metadata for CloudWatch Logs log groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups.">Why</span> |
| `logs:ListTagsForResource` | Read-only permission to list CloudWatch Logs log groups in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups.">Why</span> |

## Amazon Lookout for Equipment (1)

| Permission | What it does |
|---|---|
| `lookoutequipment:ListDatasets` | Read-only permission to list Amazon Lookout for Equipment resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Lookout for Equipment during security and inventory scans.">Why</span> |

## Amazon Managed Blockchain (3)

| Permission | What it does |
|---|---|
| `managedblockchain:GetMember` | Read-only permission to read settings and metadata for Amazon Managed Blockchain resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Managed Blockchain security settings against common misconfiguration and compliance checks.">Why</span> |
| `managedblockchain:ListMembers` `managedblockchain:ListNetworks` | Read-only permission to list Amazon Managed Blockchain resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Managed Blockchain security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon MemoryDB (1)

| Permission | What it does |
|---|---|
| `memorydb:DescribeClusters` | Read-only permission to view configuration details for Amazon MemoryDB resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon MemoryDB during security and inventory scans.">Why</span> |

## Amazon MQ (2)

| Permission | What it does |
|---|---|
| `mq:DescribeBroker` | Read-only permission to view configuration details for Amazon MQ resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon MQ security settings against common misconfiguration and compliance checks.">Why</span> |
| `mq:ListBrokers` | Read-only permission to list Amazon MQ resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon MQ security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Organizations (3)

| Permission | What it does |
|---|---|
| `organizations:DescribeOrganization` | Read-only permission to view configuration details for AWS Organizations account structure in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS account metadata.">Why</span> |
| `organizations:ListAccounts` `organizations:ListHandshakesForAccount` | Read-only permission to list AWS Organizations account structure in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Organizations security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Connect Customer Profiles (1)

| Permission | What it does |
|---|---|
| `profile:ListDomains` | Read-only permission to list Amazon Connect Customer Profiles resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Connect Customer Profiles during security and inventory scans.">Why</span> |

## AWS Proton (1)

| Permission | What it does |
|---|---|
| `proton:ListEnvironmentTemplates` | Read-only permission to list AWS Proton resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Proton during security and inventory scans.">Why</span> |

## Amazon RDS (15)

| Permission | What it does |
|---|---|
| `rds:DescribeCertificates` `rds:DescribeOrderableDBInstanceOptions` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances.">Why</span> |
| `rds:DescribeDBClusterSnapshotAttributes` `rds:DescribeDBClusterSnapshots` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this read-only call as part of building your Amazon RDS asset inventory. AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks.">Why</span> |
| `rds:DescribeDBClusters` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS/Aurora database clusters.">Why</span> |
| `rds:DescribeDBEngineVersions` `rds:DescribeDBParameterGroups` `rds:DescribeDBParameters` `rds:DescribeDBSnapshotAttributes` `rds:DescribeDBSnapshots` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks.">Why</span> |
| `rds:DescribeDBInstances` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances, docdb cluster instance.">Why</span> |
| `rds:DescribeDBProxies` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your rds db proxy.">Why</span> |
| `rds:DescribeDBSubnetGroups` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your rds db subnet group.">Why</span> |
| `rds:DescribePendingMaintenanceActions` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances, RDS/Aurora database clusters.">Why</span> |
| `rds:ListTagsForResource` | Read-only permission to list RDS and Aurora databases in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster instance, rds db proxy, rds db subnet group.">Why</span> |

## Amazon Redshift Serverless (5)

| Permission | What it does |
|---|---|
| `redshift-serverless:GetNamespace` | Read-only permission to read settings and metadata for Amazon Redshift Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace.">Why</span> |
| `redshift-serverless:GetWorkgroup` | Read-only permission to read settings and metadata for Amazon Redshift Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless workgroup.">Why</span> |
| `redshift-serverless:ListNamespaces` | Read-only permission to list Amazon Redshift Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace.">Why</span> |
| `redshift-serverless:ListTagsForResource` | Read-only permission to list Amazon Redshift Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace, redshiftserverless workgroup.">Why</span> |
| `redshift-serverless:ListWorkgroups` | Read-only permission to list Amazon Redshift Serverless resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless workgroup.">Why</span> |

## Amazon Redshift (7)

| Permission | What it does |
|---|---|
| `redshift:DescribeClusterParameterGroups` `redshift:DescribeClusterParameters` `redshift:DescribeReservedNodes` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Redshift security settings against common misconfiguration and compliance checks.">Why</span> |
| `redshift:DescribeClusterSubnetGroups` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your redshift subnet group.">Why</span> |
| `redshift:DescribeClusters` `redshift:DescribeLoggingStatus` `redshift:DescribeScheduledActions` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Redshift clusters.">Why</span> |

## Amazon Route 53 (6)

| Permission | What it does |
|---|---|
| `route53:GetDNSSEC` `route53:GetHostedZone` | Read-only permission to read settings and metadata for Route 53 DNS zones and records in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones.">Why</span> |
| `route53:ListHostedZones` `route53:ListQueryLoggingConfigs` `route53:ListTagsForResource` | Read-only permission to list Route 53 DNS zones and records in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones.">Why</span> |
| `route53:ListResourceRecordSets` | Read-only permission to list Route 53 DNS zones and records in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon Route 53 security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Route 53 Domains (3)

| Permission | What it does |
|---|---|
| `route53domains:GetDomainDetail` | Read-only permission to read settings and metadata for Amazon Route 53 Domains resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your route53 domain.">Why</span> |
| `route53domains:ListDomains` `route53domains:ListTagsForDomain` | Read-only permission to list Amazon Route 53 Domains resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your route53 domain.">Why</span> |

## Amazon S3 (22)

| Permission | What it does |
|---|---|
| `s3:GetAccelerateConfiguration` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon S3 during security and inventory scans.">Why</span> |
| `s3:GetAccessPoint` `s3:GetAccessPointPolicy` `s3:GetAccessPointPolicyStatus` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point.">Why</span> |
| `s3:GetBucketAcl` `s3:GetBucketLogging` `s3:GetBucketNotification` `s3:GetBucketObjectLockConfiguration` `s3:GetBucketOwnershipControls` `s3:GetBucketPolicy` `s3:GetBucketPolicyStatus` `s3:GetBucketPublicAccessBlock` `s3:GetBucketTagging` `s3:GetBucketVersioning` `s3:GetBucketWebsite` `s3:GetEncryptionConfiguration` `s3:GetLifecycleConfiguration` `s3:GetReplicationConfiguration` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets.">Why</span> |
| `s3:GetBucketLocation` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon S3 security settings against common misconfiguration and compliance checks.">Why</span> |
| `s3:ListAccessPoints` | Read-only permission to list S3 buckets and bucket settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point.">Why</span> |
| `s3:ListAllMyBuckets` `s3:ListBucket` | Read-only permission to list S3 buckets and bucket settings in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets.">Why</span> |

## Amazon SageMaker (5)

| Permission | What it does |
|---|---|
| `sagemaker:DescribeDomain` | Read-only permission to view configuration details for Amazon SageMaker resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your sagemaker domain.">Why</span> |
| `sagemaker:DescribeNotebookInstance` | Read-only permission to view configuration details for Amazon SageMaker resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon SageMaker security settings against common misconfiguration and compliance checks.">Why</span> |
| `sagemaker:ListDomains` `sagemaker:ListTags` | Read-only permission to list Amazon SageMaker resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your sagemaker domain.">Why</span> |
| `sagemaker:ListNotebookInstances` | Read-only permission to list Amazon SageMaker resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon SageMaker security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Secrets Manager (2)

| Permission | What it does |
|---|---|
| `secretsmanager:DescribeSecret` | Read-only permission to view configuration details for Secrets Manager secrets in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Secrets Manager security settings against common misconfiguration and compliance checks.">Why</span> |
| `secretsmanager:ListSecrets` | Read-only permission to list Secrets Manager secrets in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Secrets Manager security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Security Hub (2)

| Permission | What it does |
|---|---|
| `securityhub:DescribeHub` | Read-only permission to view configuration details for Security Hub findings and hub configuration in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Security Hub security settings against common misconfiguration and compliance checks.">Why</span> |
| `securityhub:GetFindings` | Read-only permission to read settings and metadata for Security Hub findings and hub configuration in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Security Hub security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Service Quotas (1)

| Permission | What it does |
|---|---|
| `servicequotas:ListServiceQuotas` | Read-only permission to list AWS Service Quotas resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Service Quotas security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon SES (email) (3)

| Permission | What it does |
|---|---|
| `ses:DescribeActiveReceiptRuleSet` | Read-only permission to view configuration details for Amazon SES (email) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon SES (email) during security and inventory scans.">Why</span> |
| `ses:GetIdentityDkimAttributes` | Read DKIM signing settings for your Amazon SES email identities. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox checks whether outbound email identities have DKIM enabled to reduce spoofing risk.">Why</span> |
| `ses:ListIdentities` | Read-only permission to list Amazon SES (email) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon SES (email) during security and inventory scans.">Why</span> |

## AWS Shield (3)

| Permission | What it does |
|---|---|
| `shield:DescribeEmergencyContactSettings` `shield:DescribeSubscription` | Read-only permission to view configuration details for AWS Shield resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Shield during security and inventory scans.">Why</span> |
| `shield:ListProtections` | Read-only permission to list AWS Shield resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Shield during security and inventory scans.">Why</span> |

## Amazon SNS (5)

| Permission | What it does |
|---|---|
| `sns:GetSubscriptionAttributes` | Read-only permission to read settings and metadata for SNS topics and subscriptions in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your sns subscription.">Why</span> |
| `sns:GetTopicAttributes` | Read-only permission to read settings and metadata for SNS topics and subscriptions in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your SNS notification topics.">Why</span> |
| `sns:ListSubscriptions` | Read-only permission to list SNS topics and subscriptions in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your sns subscription.">Why</span> |
| `sns:ListTagsForResource` `sns:ListTopics` | Read-only permission to list SNS topics and subscriptions in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your SNS notification topics.">Why</span> |

## Amazon SQS (3)

| Permission | What it does |
|---|---|
| `sqs:GetQueueAttributes` | Read-only permission to read settings and metadata for SQS queues in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your SQS message queues.">Why</span> |
| `sqs:ListQueueTags` `sqs:ListQueues` | Read-only permission to list SQS queues in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your SQS message queues.">Why</span> |

## AWS Systems Manager (5)

| Permission | What it does |
|---|---|
| `ssm:DescribeInstanceInformation` `ssm:DescribeParameters` `ssm:DescribeSessions` | Read-only permission to view configuration details for AWS Systems Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks.">Why</span> |
| `ssm:GetServiceSetting` | Read-only permission to read settings and metadata for AWS Systems Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks.">Why</span> |
| `ssm:ListAssociations` | Read-only permission to list AWS Systems Manager resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS STS (1)

| Permission | What it does |
|---|---|
| `sts:GetCallerIdentity` | Confirm which AWS account and identity is being used — required for onboarding and credential validation. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS STS security settings against common misconfiguration and compliance checks.">Why</span> |

## AWS Resource Groups Tagging API (2)

| Permission | What it does |
|---|---|
| `tag:GetResources` `tag:GetTagKeys` | Read-only permission to read settings and metadata for resource tags across your AWS environment in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Resource Groups Tagging API security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Timestream (2)

| Permission | What it does |
|---|---|
| `timestream:DescribeEndpoints` | Read-only permission to view configuration details for Amazon Timestream resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Timestream during security and inventory scans.">Why</span> |
| `timestream:ListDatabases` | List Amazon Timestream databases in your account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox verifies that Timestream databases have encryption enabled.">Why</span> |

## AWS Transfer Family (1)

| Permission | What it does |
|---|---|
| `transfer:ListServers` | Read-only permission to list AWS Transfer Family resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS Transfer Family security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon Translate (1)

| Permission | What it does |
|---|---|
| `translate:ListTextTranslationJobs` | Read-only permission to list Amazon Translate resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Translate during security and inventory scans.">Why</span> |

## AWS WAF (Regional Classic) (1)

| Permission | What it does |
|---|---|
| `waf-regional:ListWebACLs` | Read-only permission to list AWS WAF (Regional Classic) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS WAF (Regional Classic) during security and inventory scans.">Why</span> |

## AWS WAF (Classic) (1)

| Permission | What it does |
|---|---|
| `waf:ListWebACLs` | Read-only permission to list AWS WAF (Classic) resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS WAF (Classic) during security and inventory scans.">Why</span> |

## AWS WAFv2 (4)

| Permission | What it does |
|---|---|
| `wafv2:GetLoggingConfiguration` `wafv2:GetWebACL` | Read-only permission to read settings and metadata for AWS WAF web ACLs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks.">Why</span> |
| `wafv2:ListResourcesForWebACL` `wafv2:ListWebACLs` | Read-only permission to list AWS WAF web ACLs in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks.">Why</span> |

## Amazon WorkSpaces (5)

| Permission | What it does |
|---|---|
| `workspaces:DescribeIpGroups` `workspaces:DescribeWorkspaceDirectories` `workspaces:DescribeWorkspacesConnectionStatus` | Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox uses this to evaluate Amazon WorkSpaces security settings against common misconfiguration and compliance checks.">Why</span> |
| `workspaces:DescribeTags` `workspaces:DescribeWorkspaces` | Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox needs this to discover and maintain an up-to-date inventory of your workspaces workspace.">Why</span> |

## AWS X-Ray (1)

| Permission | What it does |
|---|---|
| `xray:GetEncryptionConfig` | Read-only permission to read settings and metadata for AWS X-Ray resources in your AWS account. <span class="iam-why" tabindex="0" role="button" aria-label="Why AccuKnox needs it" title="AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS X-Ray during security and inventory scans.">Why</span> |

</div>
