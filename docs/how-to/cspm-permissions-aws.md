---
title: AWS IAM Permissions Reference
description: The 403 read-only IAM permissions the AccuKnox CSPM scanner requests for AWS, with the reason for each.
hide:
  - toc
---

# AWS IAM Permissions Reference

AccuKnox's AWS scanner uses **403 read-only IAM permissions** (`List`, `Describe`, and `Get` only) to inventory your resources and check their configuration. No write, delete, or data-download access, and it never reads object contents.

Every permission is listed below, grouped by AWS service. Where several permissions serve the same purpose, they share one row. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [AWS prerequisites](cspm-prereq-aws.md) for setup steps.

<div class="iam-tables" markdown="1">

## IAM Access Analyzer (4)

| Permission | Rationale |
|---|---|
| `access-analyzer:GetAnalyzer` | **What it does:** Read details of a specific IAM Access Analyzer resource in your account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers. |
| `access-analyzer:GetFinding` | **What it does:** Read details of a specific IAM Access Analyzer finding (external access or unused access).<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer findings. |
| `access-analyzer:ListAnalyzers` | **What it does:** List IAM Access Analyzer resources or findings in your account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers. |
| `access-analyzer:ListFindings` | **What it does:** List IAM Access Analyzer resources or findings in your account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers, IAM Access Analyzer findings. |

## ACM Private Certificate Authority (3)

| Permission | Rationale |
|---|---|
| `acm-pca:DescribeCertificateAuthority` | **What it does:** Read-only permission to view configuration details for ACM Private Certificate Authority resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your acmpca certificate authority. |
| `acm-pca:ListCertificateAuthorities` `acm-pca:ListTags` | **What it does:** Read-only permission to list ACM Private Certificate Authority resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your acmpca certificate authority. |

## AWS Certificate Manager (ACM) (4)

| Permission | Rationale |
|---|---|
| `acm:DescribeCertificate` | **What it does:** Read-only permission to view configuration details for AWS Certificate Manager (ACM) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates. |
| `acm:GetCertificate` | **What it does:** Read-only permission to read settings and metadata for AWS Certificate Manager (ACM) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates. |
| `acm:ListCertificates` `acm:ListTagsForCertificate` | **What it does:** Read-only permission to list AWS Certificate Manager (ACM) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates. |

## Amazon Managed Workflows for Apache Airflow (MWAA) (2)

| Permission | Rationale |
|---|---|
| `airflow:GetEnvironment` | **What it does:** Read-only permission to read settings and metadata for Amazon Managed Workflows for Apache Airflow (MWAA) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Managed Workflows for Apache Airflow (MWAA) security settings against common misconfiguration and compliance checks. |
| `airflow:ListEnvironments` | **What it does:** Read-only permission to list Amazon Managed Workflows for Apache Airflow (MWAA) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Managed Workflows for Apache Airflow (MWAA) security settings against common misconfiguration and compliance checks. |

## AWS Amplify (2)

| Permission | Rationale |
|---|---|
| `amplify:GetApp` | **What it does:** Read-only permission to read settings and metadata for AWS Amplify resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your amplify app. |
| `amplify:ListApps` | **What it does:** Read-only permission to list AWS Amplify resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your amplify app. |

## Amazon OpenSearch Serverless (3)

| Permission | Rationale |
|---|---|
| `aoss:GetSecurityPolicy` | **What it does:** Read-only permission to read settings and metadata for Amazon OpenSearch Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon OpenSearch Serverless asset inventory. AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks. |
| `aoss:ListCollections` | **What it does:** Read-only permission to list Amazon OpenSearch Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks. |
| `aoss:ListSecurityPolicies` | **What it does:** Read-only permission to list Amazon OpenSearch Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon OpenSearch Serverless asset inventory. AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks. |

## Amazon API Gateway (1)

| Permission | Rationale |
|---|---|
| `apigateway:GET` | **What it does:** Read-only access to read configuration for Amazon API Gateway resources (APIs, stages, methods, and related settings).<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon API Gateway asset inventory. AccuKnox uses this to evaluate Amazon API Gateway security settings against common misconfiguration and compliance checks. |

## AWS AppConfig (2)

| Permission | Rationale |
|---|---|
| `appconfig:ListApplications` `appconfig:ListConfigurationProfiles` | **What it does:** Read-only permission to list AWS AppConfig resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS AppConfig security settings against common misconfiguration and compliance checks. |

## Amazon AppFlow (1)

| Permission | Rationale |
|---|---|
| `appflow:ListFlows` | **What it does:** Read-only permission to list Amazon AppFlow resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon AppFlow during security and inventory scans. |

## AWS App Mesh (4)

| Permission | Rationale |
|---|---|
| `appmesh:DescribeMesh` `appmesh:DescribeVirtualGateway` | **What it does:** Read-only permission to view configuration details for AWS App Mesh resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks. |
| `appmesh:ListMeshes` `appmesh:ListVirtualGateways` | **What it does:** Read-only permission to list AWS App Mesh resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks. |

## AWS App Runner (1)

| Permission | Rationale |
|---|---|
| `apprunner:ListServices` | **What it does:** Read-only permission to list AWS App Runner resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS App Runner during security and inventory scans. |

## Amazon Athena (2)

| Permission | Rationale |
|---|---|
| `athena:GetWorkGroup` | **What it does:** Read-only permission to read settings and metadata for Amazon Athena resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Athena security settings against common misconfiguration and compliance checks. |
| `athena:ListWorkGroups` | **What it does:** Read-only permission to list Amazon Athena resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Athena security settings against common misconfiguration and compliance checks. |

## AWS Audit Manager (9)

| Permission | Rationale |
|---|---|
| `auditmanager:GetAssessment` | **What it does:** Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager assessment. |
| `auditmanager:GetAssessmentFramework` | **What it does:** Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager framework. |
| `auditmanager:GetEvidence` `auditmanager:GetEvidenceByEvidenceFolder` | **What it does:** Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence. |
| `auditmanager:GetEvidenceFolder` `auditmanager:GetEvidenceFoldersByAssessment` | **What it does:** Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence folder. |
| `auditmanager:GetSettings` | **What it does:** Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Audit Manager security settings against common misconfiguration and compliance checks. |
| `auditmanager:ListAssessmentFrameworks` | **What it does:** Read-only permission to list AWS Audit Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager framework. |
| `auditmanager:ListAssessments` | **What it does:** Read-only permission to list AWS Audit Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager assessment, auditmanager evidence, auditmanager evidence folder. |

## Amazon EC2 Auto Scaling (3)

| Permission | Rationale |
|---|---|
| `autoscaling:DescribeAutoScalingGroups` `autoscaling:DescribeNotificationConfigurations` | **What it does:** Read-only permission to view configuration details for Amazon EC2 Auto Scaling resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon EC2 Auto Scaling security settings against common misconfiguration and compliance checks. |
| `autoscaling:DescribeLaunchConfigurations` | **What it does:** Read-only permission to view configuration details for Amazon EC2 Auto Scaling resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch configuration. |

## AWS Backup (14)

| Permission | Rationale |
|---|---|
| `backup:DescribeBackupJob` | **What it does:** Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup jobs. |
| `backup:DescribeBackupVault` | **What it does:** Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults. |
| `backup:DescribeRecoveryPoint` | **What it does:** Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your backup recovery point. |
| `backup:DescribeRegionSettings` | **What it does:** Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Backup security settings against common misconfiguration and compliance checks. |
| `backup:GetBackupPlan` | **What it does:** Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans. |
| `backup:GetBackupSelection` | **What it does:** Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your backup selection. |
| `backup:GetBackupVaultAccessPolicy` `backup:GetBackupVaultNotifications` | **What it does:** Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults. |
| `backup:ListBackupJobs` | **What it does:** Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup jobs. |
| `backup:ListBackupPlans` | **What it does:** Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans. |
| `backup:ListBackupSelections` | **What it does:** Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your backup selection. |
| `backup:ListBackupVaults` | **What it does:** Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults. |
| `backup:ListRecoveryPointsByBackupVault` | **What it does:** Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your backup recovery point. |
| `backup:ListTags` | **What it does:** Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans, AWS Backup vaults, backup recovery point. |

## Amazon Bedrock (5)

| Permission | Rationale |
|---|---|
| `bedrock:GetCustomModel` `bedrock:GetModelCustomizationJob` `bedrock:GetModelInvocationLoggingConfiguration` | **What it does:** Read-only permission to read settings and metadata for Amazon Bedrock resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks. |
| `bedrock:ListCustomModels` `bedrock:ListModelCustomizationJobs` | **What it does:** Read-only permission to list Amazon Bedrock resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks. |

## AWS CloudFormation (9)

| Permission | Rationale |
|---|---|
| `cloudformation:DescribeStackEvents` | **What it does:** Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS CloudFormation security settings against common misconfiguration and compliance checks. |
| `cloudformation:DescribeStackResource` | **What it does:** Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack resource. |
| `cloudformation:DescribeStackResources` `cloudformation:DescribeStacks` | **What it does:** Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks. |
| `cloudformation:DescribeStackSet` | **What it does:** Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack set. |
| `cloudformation:GetTemplate` | **What it does:** Read-only permission to read settings and metadata for AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks. |
| `cloudformation:ListStackResources` | **What it does:** Read-only permission to list AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack resource. |
| `cloudformation:ListStackSets` | **What it does:** Read-only permission to list AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack set. |
| `cloudformation:ListStacks` | **What it does:** Read-only permission to list AWS CloudFormation resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks, cloudformation stack resource. |

## Amazon CloudFront (9)

| Permission | Rationale |
|---|---|
| `cloudfront:DescribeFunction` | **What it does:** Read-only permission to view configuration details for Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront function. |
| `cloudfront:GetCachePolicy` | **What it does:** Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront cache policy. |
| `cloudfront:GetDistribution` | **What it does:** Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFront distributions. |
| `cloudfront:GetDistributionConfig` | **What it does:** Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon CloudFront during security and inventory scans. |
| `cloudfront:GetFunction` | **What it does:** Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon CloudFront asset inventory. |
| `cloudfront:ListCachePolicies` | **What it does:** Read-only permission to list Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront cache policy. |
| `cloudfront:ListDistributions` `cloudfront:ListTagsForResource` | **What it does:** Read-only permission to list Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFront distributions. |
| `cloudfront:ListFunctions` | **What it does:** Read-only permission to list Amazon CloudFront resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront function. |

## AWS CloudTrail (7)

| Permission | Rationale |
|---|---|
| `cloudtrail:DescribeTrails` | **What it does:** Read-only permission to view configuration details for CloudTrail trails and logging settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |
| `cloudtrail:GetChannel` | **What it does:** Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudtrail channel. |
| `cloudtrail:GetEventSelectors` `cloudtrail:GetInsightSelectors` `cloudtrail:GetTrailStatus` | **What it does:** Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |
| `cloudtrail:ListChannels` | **What it does:** Read-only permission to list CloudTrail trails and logging settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudtrail channel. |
| `cloudtrail:ListTags` | **What it does:** Read-only permission to list CloudTrail trails and logging settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |

## Amazon CloudWatch (3)

| Permission | Rationale |
|---|---|
| `cloudwatch:DescribeAlarms` | **What it does:** Read-only permission to view configuration details for CloudWatch alarms and metrics in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudwatch alarm. |
| `cloudwatch:GetMetricStatistics` | **What it does:** Read-only permission to read settings and metadata for CloudWatch alarms and metrics in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon CloudWatch asset inventory. AccuKnox uses this to evaluate Amazon CloudWatch security settings against common misconfiguration and compliance checks. |
| `cloudwatch:ListTagsForResource` | **What it does:** Read-only permission to list CloudWatch alarms and metrics in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudwatch alarm. |

## AWS CodeArtifact (8)

| Permission | Rationale |
|---|---|
| `codeartifact:DescribeDomain` | **What it does:** Read-only permission to view configuration details for AWS CodeArtifact resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain. |
| `codeartifact:DescribeRepository` | **What it does:** Read-only permission to view configuration details for AWS CodeArtifact resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository. |
| `codeartifact:GetDomainPermissionsPolicy` | **What it does:** Read-only permission to read settings and metadata for AWS CodeArtifact resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain. |
| `codeartifact:GetRepositoryEndpoint` `codeartifact:GetRepositoryPermissionsPolicy` | **What it does:** Read-only permission to read settings and metadata for AWS CodeArtifact resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository. |
| `codeartifact:ListDomains` | **What it does:** Read-only permission to list AWS CodeArtifact resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain. |
| `codeartifact:ListRepositories` | **What it does:** Read-only permission to list AWS CodeArtifact resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository. |
| `codeartifact:ListTagsForResource` | **What it does:** Read-only permission to list AWS CodeArtifact resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain, codeartifact repository. |

## AWS CodeBuild (2)

| Permission | Rationale |
|---|---|
| `codebuild:BatchGetProjects` | **What it does:** Read-only permission to read details for AWS CodeBuild resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codebuild project. |
| `codebuild:ListProjects` | **What it does:** Read-only permission to list AWS CodeBuild resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codebuild project. |

## AWS CodeDeploy (2)

| Permission | Rationale |
|---|---|
| `codedeploy:GetDeploymentConfig` | **What it does:** Read-only permission to read settings and metadata for AWS CodeDeploy resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codedeploy deployment config. |
| `codedeploy:ListDeploymentConfigs` | **What it does:** Read-only permission to list AWS CodeDeploy resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codedeploy deployment config. |

## AWS CodePipeline (3)

| Permission | Rationale |
|---|---|
| `codepipeline:GetPipeline` | **What it does:** Read-only permission to read settings and metadata for AWS CodePipeline resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codepipeline pipeline. |
| `codepipeline:ListPipelines` `codepipeline:ListTagsForResource` | **What it does:** Read-only permission to list AWS CodePipeline resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your codepipeline pipeline. |

## Amazon Cognito Identity Pools (2)

| Permission | Rationale |
|---|---|
| `cognito-identity:DescribeIdentityPool` | **What it does:** Read-only permission to view configuration details for Amazon Cognito Identity Pools resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito identity pool. |
| `cognito-identity:ListIdentityPools` | **What it does:** Read-only permission to list Amazon Cognito Identity Pools resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito identity pool. |

## Amazon Cognito User Pools (2)

| Permission | Rationale |
|---|---|
| `cognito-idp:DescribeUserPool` | **What it does:** Read-only permission to view configuration details for Amazon Cognito User Pools resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito user pool. |
| `cognito-idp:ListUserPools` | **What it does:** Read-only permission to list Amazon Cognito User Pools resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito user pool. |

## Amazon Comprehend (2)

| Permission | Rationale |
|---|---|
| `comprehend:ListFlywheels` | **What it does:** Read-only permission to list Amazon Comprehend resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Comprehend during security and inventory scans. |
| `comprehend:ListSentimentDetectionJobs` | **What it does:** List Amazon Comprehend sentiment analysis jobs in your account.<br>**Why AccuKnox needs it:** AccuKnox checks whether Comprehend jobs use encryption for stored data and output. |

## AWS Compute Optimizer (1)

| Permission | Rationale |
|---|---|
| `compute-optimizer:GetRecommendationSummaries` | **What it does:** Read-only permission to read settings and metadata for AWS Compute Optimizer resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Compute Optimizer security settings against common misconfiguration and compliance checks. |

## AWS Config (6)

| Permission | Rationale |
|---|---|
| `config:DescribeConfigRules` `config:DescribeDeliveryChannels` | **What it does:** Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks. |
| `config:DescribeConfigurationRecorderStatus` `config:DescribeConfigurationRecorders` | **What it does:** Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Config recorders. |
| `config:GetComplianceDetailsByConfigRule` `config:GetDiscoveredResourceCounts` | **What it does:** Read-only permission to read settings and metadata for AWS Config rules and recorders in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks. |

## Amazon Connect (3)

| Permission | Rationale |
|---|---|
| `connect:DescribeInstanceStorageConfig` | **What it does:** Read-only permission to view configuration details for Amazon Connect resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon Connect asset inventory. AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks. |
| `connect:ListInstanceStorageConfigs` | **What it does:** Read-only permission to list Amazon Connect resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon Connect asset inventory. AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks. |
| `connect:ListInstances` | **What it does:** Read-only permission to list Amazon Connect resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks. |

## AWS Glue DataBrew (1)

| Permission | Rationale |
|---|---|
| `databrew:ListJobs` | **What it does:** Read-only permission to list AWS Glue DataBrew resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Glue DataBrew during security and inventory scans. |

## Amazon DynamoDB Accelerator (DAX) (3)

| Permission | Rationale |
|---|---|
| `dax:DescribeClusters` | **What it does:** Read-only permission to view configuration details for Amazon DynamoDB Accelerator (DAX) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your dax cluster. |
| `dax:DescribeSubnetGroups` | **What it does:** Read-only permission to view configuration details for Amazon DynamoDB Accelerator (DAX) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your dax subnet group. |
| `dax:ListTags` | **What it does:** Read-only permission to list Amazon DynamoDB Accelerator (DAX) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your dax cluster. |

## Amazon DevOps Guru (1)

| Permission | Rationale |
|---|---|
| `devops-guru:ListNotificationChannels` | **What it does:** Read-only permission to list Amazon DevOps Guru resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon DevOps Guru during security and inventory scans. |

## Amazon Data Lifecycle Manager (2)

| Permission | Rationale |
|---|---|
| `dlm:GetLifecyclePolicies` `dlm:GetLifecyclePolicy` | **What it does:** Read-only permission to read settings and metadata for Amazon Data Lifecycle Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Data Lifecycle Manager security settings against common misconfiguration and compliance checks. |

## AWS Database Migration Service (1)

| Permission | Rationale |
|---|---|
| `dms:DescribeReplicationInstances` | **What it does:** Read-only permission to view configuration details for AWS Database Migration Service resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Database Migration Service security settings against common misconfiguration and compliance checks. |

## Amazon DocumentDB (elastic clusters) (3)

| Permission | Rationale |
|---|---|
| `docdb-elastic:GetCluster` | **What it does:** Read-only permission to read settings and metadata for Amazon DocumentDB (elastic clusters) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster. |
| `docdb-elastic:ListClusters` | **What it does:** Read-only permission to list Amazon DocumentDB (elastic clusters) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster. |
| `docdb-elastic:ListTagsForResource` | **What it does:** Read-only permission to list Amazon DocumentDB (elastic clusters) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster, docdb cluster snapshot. |

## Amazon DynamoDB (7)

| Permission | Rationale |
|---|---|
| `dynamodb:DescribeBackup` | **What it does:** Read-only permission to view configuration details for DynamoDB tables in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your dynamodb backup. |
| `dynamodb:DescribeContinuousBackups` `dynamodb:DescribeKinesisStreamingDestination` `dynamodb:DescribeTable` | **What it does:** Read-only permission to view configuration details for DynamoDB tables in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables. |
| `dynamodb:ListBackups` | **What it does:** Read-only permission to list DynamoDB tables in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your dynamodb backup. |
| `dynamodb:ListTables` `dynamodb:ListTagsOfResource` | **What it does:** Read-only permission to list DynamoDB tables in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables. |

## Amazon EC2 (39)

| Permission | Rationale |
|---|---|
| `ec2:DescribeAccountAttributes` `ec2:DescribeEgressOnlyInternetGateways` `ec2:DescribeFlowLogs` `ec2:DescribeImages` `ec2:DescribeInternetGateways` `ec2:DescribeVpcEndpointServicePermissions` `ec2:DescribeVpcEndpointServices` `ec2:DescribeVpcEndpoints` `ec2:DescribeVpcPeeringConnections` `ec2:DescribeVpnConnections` `ec2:DescribeVpnGateways` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeAddresses` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your vpc eip. |
| `ec2:DescribeInstanceAttribute` `ec2:DescribeInstanceCreditSpecifications` `ec2:DescribeInstanceStatus` `ec2:DescribeInstances` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances). |
| `ec2:DescribeInstanceTypeOfferings` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 instance availability. |
| `ec2:DescribeKeyPairs` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 key pair. |
| `ec2:DescribeLaunchTemplateVersions` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch template version. |
| `ec2:DescribeLaunchTemplates` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch template. |
| `ec2:DescribeManagedPrefixLists` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 managed prefix list. |
| `ec2:DescribeNatGateways` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC NAT gateways. |
| `ec2:DescribeNetworkAcls` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC network ACLs. |
| `ec2:DescribeNetworkInterfaces` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 network interface. |
| `ec2:DescribeRegions` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS regions. |
| `ec2:DescribeReservedInstances` `ec2:DescribeReservedInstancesModifications` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 reserved instance. |
| `ec2:DescribeRouteTables` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC route tables. |
| `ec2:DescribeSecurityGroupRules` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your vpc security group rule. |
| `ec2:DescribeSecurityGroups` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC security groups, vpc security group rule. |
| `ec2:DescribeSnapshotAttribute` `ec2:DescribeSnapshots` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs snapshot. |
| `ec2:DescribeSubnets` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC subnets. |
| `ec2:DescribeVolumeAttribute` `ec2:DescribeVolumes` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs volume. |
| `ec2:DescribeVpcs` | **What it does:** Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC networks. |
| `ec2:GetEbsDefaultKmsKeyId` `ec2:GetEbsEncryptionByDefault` | **What it does:** Read-only permission to read settings and metadata for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:GetLaunchTemplateData` | **What it does:** Read-only permission to read settings and metadata for EC2 compute and networking resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances). |

## Amazon ECR (container registry) (2)

| Permission | Rationale |
|---|---|
| `ecr:DescribeRepositories` | **What it does:** Read-only permission to view configuration details for Amazon ECR (container registry) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon ECR (container registry) security settings against common misconfiguration and compliance checks. |
| `ecr:GetRepositoryPolicy` | **What it does:** Read-only permission to read settings and metadata for Amazon ECR (container registry) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon ECR (container registry) security settings against common misconfiguration and compliance checks. |

## Amazon ECS (5)

| Permission | Rationale |
|---|---|
| `ecs:DescribeClusters` | **What it does:** Read-only permission to view configuration details for ECS clusters and services in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ECS clusters. |
| `ecs:DescribeServices` | **What it does:** Read-only permission to view configuration details for ECS clusters and services in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon ECS security settings against common misconfiguration and compliance checks. |
| `ecs:ListClusters` `ecs:ListTagsForResource` | **What it does:** Read-only permission to list ECS clusters and services in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ECS clusters. |
| `ecs:ListServices` | **What it does:** Read-only permission to list ECS clusters and services in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon ECS security settings against common misconfiguration and compliance checks. |

## Amazon EKS (2)

| Permission | Rationale |
|---|---|
| `eks:DescribeCluster` | **What it does:** Read-only permission to view configuration details for EKS Kubernetes clusters in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your EKS Kubernetes clusters. |
| `eks:ListClusters` | **What it does:** Read-only permission to list EKS Kubernetes clusters in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your EKS Kubernetes clusters. |

## Amazon ElastiCache (5)

| Permission | Rationale |
|---|---|
| `elasticache:DescribeCacheClusters` | **What it does:** Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ElastiCache clusters. |
| `elasticache:DescribeCacheSubnetGroups` `elasticache:DescribeReplicationGroups` `elasticache:DescribeReservedCacheNodes` | **What it does:** Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon ElastiCache security settings against common misconfiguration and compliance checks. |
| `elasticache:ListTagsForResource` | **What it does:** Read-only permission to list Amazon ElastiCache resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your ElastiCache clusters. |

## Amazon EFS (1)

| Permission | Rationale |
|---|---|
| `elasticfilesystem:DescribeFileSystems` | **What it does:** Read-only permission to view configuration details for Amazon EFS resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon EFS security settings against common misconfiguration and compliance checks. |

## Elastic Load Balancing (ALB/NLB/CLB) (9)

| Permission | Rationale |
|---|---|
| `elasticloadbalancing:DescribeInstanceHealth` `elasticloadbalancing:DescribeListeners` `elasticloadbalancing:DescribeLoadBalancerPolicies` `elasticloadbalancing:DescribeTargetGroupAttributes` | **What it does:** Read-only permission to view configuration details for load balancers and target groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Elastic Load Balancing (ALB/NLB/CLB) security settings against common misconfiguration and compliance checks. |
| `elasticloadbalancing:DescribeLoadBalancerAttributes` | **What it does:** Read-only permission to view configuration details for load balancers and target groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers. |
| `elasticloadbalancing:DescribeLoadBalancers` | **What it does:** Read-only permission to view configuration details for load balancers and target groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers, ec2 load balancer listener. |
| `elasticloadbalancing:DescribeTags` | **What it does:** Read-only permission to view configuration details for load balancers and target groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers, load balancer target groups. |
| `elasticloadbalancing:DescribeTargetGroups` `elasticloadbalancing:DescribeTargetHealth` | **What it does:** Read-only permission to view configuration details for load balancers and target groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your load balancer target groups. |

## Amazon EMR (4)

| Permission | Rationale |
|---|---|
| `elasticmapreduce:DescribeCluster` `elasticmapreduce:DescribeSecurityConfiguration` | **What it does:** Read-only permission to view configuration details for Amazon EMR resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks. |
| `elasticmapreduce:ListClusters` `elasticmapreduce:ListInstanceGroups` | **What it does:** Read-only permission to list Amazon EMR resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks. |

## Amazon OpenSearch Service (1)

| Permission | Rationale |
|---|---|
| `es:ListDomainNames` | **What it does:** Read-only permission to list Amazon OpenSearch Service resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon OpenSearch Service during security and inventory scans. |

## Amazon EventBridge (2)

| Permission | Rationale |
|---|---|
| `events:ListEventBuses` `events:ListRules` | **What it does:** Read-only permission to list Amazon EventBridge resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon EventBridge security settings against common misconfiguration and compliance checks. |

## Amazon FinSpace (1)

| Permission | Rationale |
|---|---|
| `finspace:ListEnvironments` | **What it does:** Read-only permission to list Amazon FinSpace resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon FinSpace during security and inventory scans. |

## Amazon Kinesis Data Firehose (2)

| Permission | Rationale |
|---|---|
| `firehose:DescribeDeliveryStream` | **What it does:** Read-only permission to view configuration details for Amazon Kinesis Data Firehose resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Kinesis Data Firehose security settings against common misconfiguration and compliance checks. |
| `firehose:ListDeliveryStreams` | **What it does:** Read-only permission to list Amazon Kinesis Data Firehose resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Kinesis Data Firehose security settings against common misconfiguration and compliance checks. |

## Amazon Forecast (2)

| Permission | Rationale |
|---|---|
| `forecast:ListDatasets` `forecast:ListForecastExportJobs` | **What it does:** Read-only permission to list Amazon Forecast resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Forecast during security and inventory scans. |

## Amazon Fraud Detector (1)

| Permission | Rationale |
|---|---|
| `frauddetector:GetDetectors` | **What it does:** Read-only permission to read settings and metadata for Amazon Fraud Detector resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Fraud Detector during security and inventory scans. |

## Amazon FSx (1)

| Permission | Rationale |
|---|---|
| `fsx:DescribeFileSystems` | **What it does:** Read-only permission to view configuration details for Amazon FSx resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon FSx during security and inventory scans. |

## Amazon S3 Glacier (1)

| Permission | Rationale |
|---|---|
| `glacier:ListVaults` | **What it does:** Read-only permission to list Amazon S3 Glacier resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon S3 Glacier during security and inventory scans. |

## AWS Glue (2)

| Permission | Rationale |
|---|---|
| `glue:GetDataCatalogEncryptionSettings` `glue:GetSecurityConfigurations` | **What it does:** Read-only permission to read settings and metadata for AWS Glue resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Glue security settings against common misconfiguration and compliance checks. |

## Amazon GuardDuty (7)

| Permission | Rationale |
|---|---|
| `guardduty:DescribePublishingDestination` | **What it does:** Read-only permission to view configuration details for GuardDuty threat detection settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:GetDetector` `guardduty:GetFindings` `guardduty:GetMasterAccount` | **What it does:** Read-only permission to read settings and metadata for GuardDuty threat detection settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:ListDetectors` `guardduty:ListFindings` `guardduty:ListPublishingDestinations` | **What it does:** Read-only permission to list GuardDuty threat detection settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |

## Amazon HealthLake (1)

| Permission | Rationale |
|---|---|
| `healthlake:ListFHIRDatastores` | **What it does:** Read-only permission to list Amazon HealthLake resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon HealthLake security settings against common misconfiguration and compliance checks. |

## AWS IAM (31)

| Permission | Rationale |
|---|---|
| `iam:GenerateCredentialReport` | **What it does:** Request generation of the IAM credential report (password age, access key rotation, MFA status).<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:GetAccountPasswordPolicy` `iam:GetAccountSummary` `iam:GetUserPolicy` | **What it does:** Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:GetCredentialReport` | **What it does:** Download the IAM credential report after it has been generated.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS IAM during security and inventory scans. |
| `iam:GetGroup` `iam:GetGroupPolicy` | **What it does:** Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups. |
| `iam:GetLoginProfile` `iam:GetUser` | **What it does:** Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:GetPolicy` `iam:GetPolicyVersion` | **What it does:** Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM customer-managed policies, attached aws iam policy. |
| `iam:GetRole` `iam:GetRolePolicy` | **What it does:** Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:ListAccountAliases` | **What it does:** Read-only permission to list IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS account metadata. |
| `iam:ListAttachedGroupPolicies` `iam:ListGroupPolicies` `iam:ListGroups` | **What it does:** Read-only permission to list IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups. |
| `iam:ListAttachedRolePolicies` `iam:ListInstanceProfilesForRole` `iam:ListRolePolicies` `iam:ListRoles` | **What it does:** Read-only permission to list IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:ListAttachedUserPolicies` `iam:ListGroupsForUser` `iam:ListMFADevices` `iam:ListUserPolicies` `iam:ListUsers` | **What it does:** Read-only permission to list IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:ListEntitiesForPolicy` | **What it does:** Read-only permission to list IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your iam policy attachment. |
| `iam:ListPolicies` | **What it does:** Read-only permission to list IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM customer-managed policies, attached aws iam policy. |
| `iam:ListSSHPublicKeys` `iam:ListServerCertificates` `iam:ListVirtualMFADevices` | **What it does:** Read-only permission to list IAM users, roles, groups, and policies in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |

## EC2 Image Builder (5)

| Permission | Rationale |
|---|---|
| `imagebuilder:ListComponents` `imagebuilder:ListContainerRecipes` `imagebuilder:ListImagePipelines` `imagebuilder:ListImageRecipes` `imagebuilder:ListInfrastructureConfigurations` | **What it does:** Read-only permission to list EC2 Image Builder resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of EC2 Image Builder during security and inventory scans. |

## AWS IoT SiteWise (1)

| Permission | Rationale |
|---|---|
| `iotsitewise:DescribeDefaultEncryptionConfiguration` | **What it does:** Read-only permission to view configuration details for AWS IoT SiteWise resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS IoT SiteWise during security and inventory scans. |

## Amazon MSK (Kafka) (1)

| Permission | Rationale |
|---|---|
| `kafka:ListClusters` | **What it does:** Read-only permission to list Amazon MSK (Kafka) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon MSK (Kafka) security settings against common misconfiguration and compliance checks. |

## Amazon Kendra (1)

| Permission | Rationale |
|---|---|
| `kendra:ListIndices` | **What it does:** Read-only permission to list Amazon Kendra resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Kendra during security and inventory scans. |

## Amazon Kinesis Data Streams (2)

| Permission | Rationale |
|---|---|
| `kinesis:DescribeStream` | **What it does:** Read-only permission to view configuration details for Amazon Kinesis Data Streams resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Kinesis Data Streams security settings against common misconfiguration and compliance checks. |
| `kinesis:ListStreams` | **What it does:** Read-only permission to list Amazon Kinesis Data Streams resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Kinesis Data Streams security settings against common misconfiguration and compliance checks. |

## Amazon Kinesis Video Streams (1)

| Permission | Rationale |
|---|---|
| `kinesisvideo:ListStreams` | **What it does:** Read-only permission to list Amazon Kinesis Video Streams resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Kinesis Video Streams during security and inventory scans. |

## AWS KMS (7)

| Permission | Rationale |
|---|---|
| `kms:DescribeKey` | **What it does:** Read-only permission to view configuration details for KMS encryption keys in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:GetKeyPolicy` `kms:GetKeyRotationStatus` | **What it does:** Read-only permission to read settings and metadata for KMS encryption keys in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:ListAliases` `kms:ListKeys` `kms:ListResourceTags` | **What it does:** Read-only permission to list KMS encryption keys in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:ListGrants` | **What it does:** Read-only permission to list KMS encryption keys in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS KMS security settings against common misconfiguration and compliance checks. |

## AWS Lambda (6)

| Permission | Rationale |
|---|---|
| `lambda:GetFunction` `lambda:GetFunctionUrlConfig` `lambda:GetPolicy` | **What it does:** Read-only permission to read settings and metadata for Lambda functions in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions. |
| `lambda:GetFunctionCodeSigningConfig` `lambda:GetFunctionConfiguration` | **What it does:** Read-only permission to read settings and metadata for Lambda functions in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Lambda security settings against common misconfiguration and compliance checks. |
| `lambda:ListFunctions` | **What it does:** Read-only permission to list Lambda functions in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions. |

## Amazon Lex (1)

| Permission | Rationale |
|---|---|
| `lex:ListBots` | **What it does:** Read-only permission to list Amazon Lex resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Lex during security and inventory scans. |

## Amazon CloudWatch Logs (4)

| Permission | Rationale |
|---|---|
| `logs:DescribeLogGroups` | **What it does:** Read-only permission to view configuration details for CloudWatch Logs log groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups. |
| `logs:DescribeMetricFilters` | **What it does:** Read-only permission to view configuration details for CloudWatch Logs log groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon CloudWatch Logs security settings against common misconfiguration and compliance checks. |
| `logs:GetDataProtectionPolicy` | **What it does:** Read-only permission to read settings and metadata for CloudWatch Logs log groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups. |
| `logs:ListTagsForResource` | **What it does:** Read-only permission to list CloudWatch Logs log groups in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups. |

## Amazon Lookout for Equipment (1)

| Permission | Rationale |
|---|---|
| `lookoutequipment:ListDatasets` | **What it does:** Read-only permission to list Amazon Lookout for Equipment resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Lookout for Equipment during security and inventory scans. |

## Amazon Managed Blockchain (3)

| Permission | Rationale |
|---|---|
| `managedblockchain:GetMember` | **What it does:** Read-only permission to read settings and metadata for Amazon Managed Blockchain resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Managed Blockchain security settings against common misconfiguration and compliance checks. |
| `managedblockchain:ListMembers` `managedblockchain:ListNetworks` | **What it does:** Read-only permission to list Amazon Managed Blockchain resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Managed Blockchain security settings against common misconfiguration and compliance checks. |

## Amazon MemoryDB (1)

| Permission | Rationale |
|---|---|
| `memorydb:DescribeClusters` | **What it does:** Read-only permission to view configuration details for Amazon MemoryDB resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon MemoryDB during security and inventory scans. |

## Amazon MQ (2)

| Permission | Rationale |
|---|---|
| `mq:DescribeBroker` | **What it does:** Read-only permission to view configuration details for Amazon MQ resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon MQ security settings against common misconfiguration and compliance checks. |
| `mq:ListBrokers` | **What it does:** Read-only permission to list Amazon MQ resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon MQ security settings against common misconfiguration and compliance checks. |

## AWS Organizations (3)

| Permission | Rationale |
|---|---|
| `organizations:DescribeOrganization` | **What it does:** Read-only permission to view configuration details for AWS Organizations account structure in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS account metadata. |
| `organizations:ListAccounts` `organizations:ListHandshakesForAccount` | **What it does:** Read-only permission to list AWS Organizations account structure in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Organizations security settings against common misconfiguration and compliance checks. |

## Amazon Connect Customer Profiles (1)

| Permission | Rationale |
|---|---|
| `profile:ListDomains` | **What it does:** Read-only permission to list Amazon Connect Customer Profiles resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Connect Customer Profiles during security and inventory scans. |

## AWS Proton (1)

| Permission | Rationale |
|---|---|
| `proton:ListEnvironmentTemplates` | **What it does:** Read-only permission to list AWS Proton resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Proton during security and inventory scans. |

## Amazon RDS (15)

| Permission | Rationale |
|---|---|
| `rds:DescribeCertificates` `rds:DescribeOrderableDBInstanceOptions` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances. |
| `rds:DescribeDBClusterSnapshotAttributes` `rds:DescribeDBClusterSnapshots` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this read-only call as part of building your Amazon RDS asset inventory. AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBClusters` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS/Aurora database clusters. |
| `rds:DescribeDBEngineVersions` `rds:DescribeDBParameterGroups` `rds:DescribeDBParameters` `rds:DescribeDBSnapshotAttributes` `rds:DescribeDBSnapshots` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBInstances` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances, docdb cluster instance. |
| `rds:DescribeDBProxies` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your rds db proxy. |
| `rds:DescribeDBSubnetGroups` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your rds db subnet group. |
| `rds:DescribePendingMaintenanceActions` | **What it does:** Read-only permission to view configuration details for RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances, RDS/Aurora database clusters. |
| `rds:ListTagsForResource` | **What it does:** Read-only permission to list RDS and Aurora databases in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster instance, rds db proxy, rds db subnet group. |

## Amazon Redshift Serverless (5)

| Permission | Rationale |
|---|---|
| `redshift-serverless:GetNamespace` | **What it does:** Read-only permission to read settings and metadata for Amazon Redshift Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace. |
| `redshift-serverless:GetWorkgroup` | **What it does:** Read-only permission to read settings and metadata for Amazon Redshift Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless workgroup. |
| `redshift-serverless:ListNamespaces` | **What it does:** Read-only permission to list Amazon Redshift Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace. |
| `redshift-serverless:ListTagsForResource` | **What it does:** Read-only permission to list Amazon Redshift Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace, redshiftserverless workgroup. |
| `redshift-serverless:ListWorkgroups` | **What it does:** Read-only permission to list Amazon Redshift Serverless resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless workgroup. |

## Amazon Redshift (7)

| Permission | Rationale |
|---|---|
| `redshift:DescribeClusterParameterGroups` `redshift:DescribeClusterParameters` `redshift:DescribeReservedNodes` | **What it does:** Read-only permission to view configuration details for Redshift data warehouses in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Redshift security settings against common misconfiguration and compliance checks. |
| `redshift:DescribeClusterSubnetGroups` | **What it does:** Read-only permission to view configuration details for Redshift data warehouses in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your redshift subnet group. |
| `redshift:DescribeClusters` `redshift:DescribeLoggingStatus` `redshift:DescribeScheduledActions` | **What it does:** Read-only permission to view configuration details for Redshift data warehouses in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Redshift clusters. |

## Amazon Route 53 (6)

| Permission | Rationale |
|---|---|
| `route53:GetDNSSEC` `route53:GetHostedZone` | **What it does:** Read-only permission to read settings and metadata for Route 53 DNS zones and records in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones. |
| `route53:ListHostedZones` `route53:ListQueryLoggingConfigs` `route53:ListTagsForResource` | **What it does:** Read-only permission to list Route 53 DNS zones and records in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones. |
| `route53:ListResourceRecordSets` | **What it does:** Read-only permission to list Route 53 DNS zones and records in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon Route 53 security settings against common misconfiguration and compliance checks. |

## Amazon Route 53 Domains (3)

| Permission | Rationale |
|---|---|
| `route53domains:GetDomainDetail` | **What it does:** Read-only permission to read settings and metadata for Amazon Route 53 Domains resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your route53 domain. |
| `route53domains:ListDomains` `route53domains:ListTagsForDomain` | **What it does:** Read-only permission to list Amazon Route 53 Domains resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your route53 domain. |

## Amazon S3 (22)

| Permission | Rationale |
|---|---|
| `s3:GetAccelerateConfiguration` | **What it does:** Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon S3 during security and inventory scans. |
| `s3:GetAccessPoint` `s3:GetAccessPointPolicy` `s3:GetAccessPointPolicyStatus` | **What it does:** Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point. |
| `s3:GetBucketAcl` `s3:GetBucketLogging` `s3:GetBucketNotification` `s3:GetBucketObjectLockConfiguration` `s3:GetBucketOwnershipControls` `s3:GetBucketPolicy` `s3:GetBucketPolicyStatus` `s3:GetBucketPublicAccessBlock` `s3:GetBucketTagging` `s3:GetBucketVersioning` `s3:GetBucketWebsite` `s3:GetEncryptionConfiguration` `s3:GetLifecycleConfiguration` `s3:GetReplicationConfiguration` | **What it does:** Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketLocation` | **What it does:** Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon S3 security settings against common misconfiguration and compliance checks. |
| `s3:ListAccessPoints` | **What it does:** Read-only permission to list S3 buckets and bucket settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point. |
| `s3:ListAllMyBuckets` `s3:ListBucket` | **What it does:** Read-only permission to list S3 buckets and bucket settings in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |

## Amazon SageMaker (5)

| Permission | Rationale |
|---|---|
| `sagemaker:DescribeDomain` | **What it does:** Read-only permission to view configuration details for Amazon SageMaker resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your sagemaker domain. |
| `sagemaker:DescribeNotebookInstance` | **What it does:** Read-only permission to view configuration details for Amazon SageMaker resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon SageMaker security settings against common misconfiguration and compliance checks. |
| `sagemaker:ListDomains` `sagemaker:ListTags` | **What it does:** Read-only permission to list Amazon SageMaker resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your sagemaker domain. |
| `sagemaker:ListNotebookInstances` | **What it does:** Read-only permission to list Amazon SageMaker resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon SageMaker security settings against common misconfiguration and compliance checks. |

## AWS Secrets Manager (2)

| Permission | Rationale |
|---|---|
| `secretsmanager:DescribeSecret` | **What it does:** Read-only permission to view configuration details for Secrets Manager secrets in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Secrets Manager security settings against common misconfiguration and compliance checks. |
| `secretsmanager:ListSecrets` | **What it does:** Read-only permission to list Secrets Manager secrets in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Secrets Manager security settings against common misconfiguration and compliance checks. |

## AWS Security Hub (2)

| Permission | Rationale |
|---|---|
| `securityhub:DescribeHub` | **What it does:** Read-only permission to view configuration details for Security Hub findings and hub configuration in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Security Hub security settings against common misconfiguration and compliance checks. |
| `securityhub:GetFindings` | **What it does:** Read-only permission to read settings and metadata for Security Hub findings and hub configuration in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Security Hub security settings against common misconfiguration and compliance checks. |

## AWS Service Quotas (1)

| Permission | Rationale |
|---|---|
| `servicequotas:ListServiceQuotas` | **What it does:** Read-only permission to list AWS Service Quotas resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Service Quotas security settings against common misconfiguration and compliance checks. |

## Amazon SES (email) (3)

| Permission | Rationale |
|---|---|
| `ses:DescribeActiveReceiptRuleSet` | **What it does:** Read-only permission to view configuration details for Amazon SES (email) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon SES (email) during security and inventory scans. |
| `ses:GetIdentityDkimAttributes` | **What it does:** Read DKIM signing settings for your Amazon SES email identities.<br>**Why AccuKnox needs it:** AccuKnox checks whether outbound email identities have DKIM enabled to reduce spoofing risk. |
| `ses:ListIdentities` | **What it does:** Read-only permission to list Amazon SES (email) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon SES (email) during security and inventory scans. |

## AWS Shield (3)

| Permission | Rationale |
|---|---|
| `shield:DescribeEmergencyContactSettings` `shield:DescribeSubscription` | **What it does:** Read-only permission to view configuration details for AWS Shield resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Shield during security and inventory scans. |
| `shield:ListProtections` | **What it does:** Read-only permission to list AWS Shield resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Shield during security and inventory scans. |

## Amazon SNS (5)

| Permission | Rationale |
|---|---|
| `sns:GetSubscriptionAttributes` | **What it does:** Read-only permission to read settings and metadata for SNS topics and subscriptions in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your sns subscription. |
| `sns:GetTopicAttributes` | **What it does:** Read-only permission to read settings and metadata for SNS topics and subscriptions in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your SNS notification topics. |
| `sns:ListSubscriptions` | **What it does:** Read-only permission to list SNS topics and subscriptions in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your sns subscription. |
| `sns:ListTagsForResource` `sns:ListTopics` | **What it does:** Read-only permission to list SNS topics and subscriptions in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your SNS notification topics. |

## Amazon SQS (3)

| Permission | Rationale |
|---|---|
| `sqs:GetQueueAttributes` | **What it does:** Read-only permission to read settings and metadata for SQS queues in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your SQS message queues. |
| `sqs:ListQueueTags` `sqs:ListQueues` | **What it does:** Read-only permission to list SQS queues in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your SQS message queues. |

## AWS Systems Manager (5)

| Permission | Rationale |
|---|---|
| `ssm:DescribeInstanceInformation` `ssm:DescribeParameters` `ssm:DescribeSessions` | **What it does:** Read-only permission to view configuration details for AWS Systems Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |
| `ssm:GetServiceSetting` | **What it does:** Read-only permission to read settings and metadata for AWS Systems Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |
| `ssm:ListAssociations` | **What it does:** Read-only permission to list AWS Systems Manager resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |

## AWS STS (1)

| Permission | Rationale |
|---|---|
| `sts:GetCallerIdentity` | **What it does:** Confirm which AWS account and identity is being used — required for onboarding and credential validation.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS STS security settings against common misconfiguration and compliance checks. |

## AWS Resource Groups Tagging API (2)

| Permission | Rationale |
|---|---|
| `tag:GetResources` `tag:GetTagKeys` | **What it does:** Read-only permission to read settings and metadata for resource tags across your AWS environment in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Resource Groups Tagging API security settings against common misconfiguration and compliance checks. |

## Amazon Timestream (2)

| Permission | Rationale |
|---|---|
| `timestream:DescribeEndpoints` | **What it does:** Read-only permission to view configuration details for Amazon Timestream resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Timestream during security and inventory scans. |
| `timestream:ListDatabases` | **What it does:** List Amazon Timestream databases in your account.<br>**Why AccuKnox needs it:** AccuKnox verifies that Timestream databases have encryption enabled. |

## AWS Transfer Family (1)

| Permission | Rationale |
|---|---|
| `transfer:ListServers` | **What it does:** Read-only permission to list AWS Transfer Family resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS Transfer Family security settings against common misconfiguration and compliance checks. |

## Amazon Translate (1)

| Permission | Rationale |
|---|---|
| `translate:ListTextTranslationJobs` | **What it does:** Read-only permission to list Amazon Translate resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Translate during security and inventory scans. |

## AWS WAF (Regional Classic) (1)

| Permission | Rationale |
|---|---|
| `waf-regional:ListWebACLs` | **What it does:** Read-only permission to list AWS WAF (Regional Classic) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS WAF (Regional Classic) during security and inventory scans. |

## AWS WAF (Classic) (1)

| Permission | Rationale |
|---|---|
| `waf:ListWebACLs` | **What it does:** Read-only permission to list AWS WAF (Classic) resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS WAF (Classic) during security and inventory scans. |

## AWS WAFv2 (4)

| Permission | Rationale |
|---|---|
| `wafv2:GetLoggingConfiguration` `wafv2:GetWebACL` | **What it does:** Read-only permission to read settings and metadata for AWS WAF web ACLs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks. |
| `wafv2:ListResourcesForWebACL` `wafv2:ListWebACLs` | **What it does:** Read-only permission to list AWS WAF web ACLs in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks. |

## Amazon WorkSpaces (5)

| Permission | Rationale |
|---|---|
| `workspaces:DescribeIpGroups` `workspaces:DescribeWorkspaceDirectories` `workspaces:DescribeWorkspacesConnectionStatus` | **What it does:** Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox uses this to evaluate Amazon WorkSpaces security settings against common misconfiguration and compliance checks. |
| `workspaces:DescribeTags` `workspaces:DescribeWorkspaces` | **What it does:** Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox needs this to discover and maintain an up-to-date inventory of your workspaces workspace. |

## AWS X-Ray (1)

| Permission | Rationale |
|---|---|
| `xray:GetEncryptionConfig` | **What it does:** Read-only permission to read settings and metadata for AWS X-Ray resources in your AWS account.<br>**Why AccuKnox needs it:** AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS X-Ray during security and inventory scans. |

</div>
