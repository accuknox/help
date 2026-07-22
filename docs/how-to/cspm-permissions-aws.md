---
title: AWS IAM Permissions Reference
description: The 403 read-only IAM permissions the AccuKnox CSPM scanner requests for AWS, with the reason for each.
hide:
  - toc
---

# AWS IAM Permissions Reference

AccuKnox's AWS scanner uses **403 read-only IAM permissions** (`List`, `Describe`, and `Get` only) to inventory your resources and check their configuration. No write, delete, or data-download access, and it never reads object contents.

Every permission is listed below, grouped by AWS service. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [AWS prerequisites](cspm-prereq-aws.md) for setup steps.


## IAM Access Analyzer (4)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `access-analyzer:GetAnalyzer` | Read details of a specific IAM Access Analyzer resource in your account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers. |
| `access-analyzer:GetFinding` | Read details of a specific IAM Access Analyzer finding (external access or unused access). | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer findings. |
| `access-analyzer:ListAnalyzers` | List IAM Access Analyzer resources or findings in your account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers. |
| `access-analyzer:ListFindings` | List IAM Access Analyzer resources or findings in your account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM Access Analyzer analyzers, IAM Access Analyzer findings. |


## ACM Private Certificate Authority (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `acm-pca:DescribeCertificateAuthority` | Read-only permission to view configuration details for ACM Private Certificate Authority resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your acmpca certificate authority. |
| `acm-pca:ListCertificateAuthorities` | Read-only permission to list ACM Private Certificate Authority resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your acmpca certificate authority. |
| `acm-pca:ListTags` | Read-only permission to list ACM Private Certificate Authority resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your acmpca certificate authority. |


## AWS Certificate Manager (ACM) (4)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `acm:DescribeCertificate` | Read-only permission to view configuration details for AWS Certificate Manager (ACM) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates. |
| `acm:GetCertificate` | Read-only permission to read settings and metadata for AWS Certificate Manager (ACM) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates. |
| `acm:ListCertificates` | Read-only permission to list AWS Certificate Manager (ACM) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates. |
| `acm:ListTagsForCertificate` | Read-only permission to list AWS Certificate Manager (ACM) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ACM TLS/SSL certificates. |


## Amazon Managed Workflows for Apache Airflow (MWAA) (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `airflow:GetEnvironment` | Read-only permission to read settings and metadata for Amazon Managed Workflows for Apache Airflow (MWAA) resources in your AWS account. | AccuKnox uses this to evaluate Amazon Managed Workflows for Apache Airflow (MWAA) security settings against common misconfiguration and compliance checks. |
| `airflow:ListEnvironments` | Read-only permission to list Amazon Managed Workflows for Apache Airflow (MWAA) resources in your AWS account. | AccuKnox uses this to evaluate Amazon Managed Workflows for Apache Airflow (MWAA) security settings against common misconfiguration and compliance checks. |


## AWS Amplify (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `amplify:GetApp` | Read-only permission to read settings and metadata for AWS Amplify resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your amplify app. |
| `amplify:ListApps` | Read-only permission to list AWS Amplify resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your amplify app. |


## Amazon OpenSearch Serverless (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `aoss:GetSecurityPolicy` | Read-only permission to read settings and metadata for Amazon OpenSearch Serverless resources in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon OpenSearch Serverless asset inventory. AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks. |
| `aoss:ListCollections` | Read-only permission to list Amazon OpenSearch Serverless resources in your AWS account. | AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks. |
| `aoss:ListSecurityPolicies` | Read-only permission to list Amazon OpenSearch Serverless resources in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon OpenSearch Serverless asset inventory. AccuKnox uses this to evaluate Amazon OpenSearch Serverless security settings against common misconfiguration and compliance checks. |


## Amazon API Gateway (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `apigateway:GET` | Read-only access to read configuration for Amazon API Gateway resources (APIs, stages, methods, and related settings). | AccuKnox uses this read-only call as part of building your Amazon API Gateway asset inventory. AccuKnox uses this to evaluate Amazon API Gateway security settings against common misconfiguration and compliance checks. |


## AWS AppConfig (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `appconfig:ListApplications` | Read-only permission to list AWS AppConfig resources in your AWS account. | AccuKnox uses this to evaluate AWS AppConfig security settings against common misconfiguration and compliance checks. |
| `appconfig:ListConfigurationProfiles` | Read-only permission to list AWS AppConfig resources in your AWS account. | AccuKnox uses this to evaluate AWS AppConfig security settings against common misconfiguration and compliance checks. |


## Amazon AppFlow (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `appflow:ListFlows` | Read-only permission to list Amazon AppFlow resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon AppFlow during security and inventory scans. |


## AWS App Mesh (4)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `appmesh:DescribeMesh` | Read-only permission to view configuration details for AWS App Mesh resources in your AWS account. | AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks. |
| `appmesh:DescribeVirtualGateway` | Read-only permission to view configuration details for AWS App Mesh resources in your AWS account. | AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks. |
| `appmesh:ListMeshes` | Read-only permission to list AWS App Mesh resources in your AWS account. | AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks. |
| `appmesh:ListVirtualGateways` | Read-only permission to list AWS App Mesh resources in your AWS account. | AccuKnox uses this to evaluate AWS App Mesh security settings against common misconfiguration and compliance checks. |


## AWS App Runner (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `apprunner:ListServices` | Read-only permission to list AWS App Runner resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS App Runner during security and inventory scans. |


## Amazon Athena (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `athena:GetWorkGroup` | Read-only permission to read settings and metadata for Amazon Athena resources in your AWS account. | AccuKnox uses this to evaluate Amazon Athena security settings against common misconfiguration and compliance checks. |
| `athena:ListWorkGroups` | Read-only permission to list Amazon Athena resources in your AWS account. | AccuKnox uses this to evaluate Amazon Athena security settings against common misconfiguration and compliance checks. |


## AWS Audit Manager (9)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `auditmanager:GetAssessment` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager assessment. |
| `auditmanager:GetAssessmentFramework` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager framework. |
| `auditmanager:GetEvidence` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence. |
| `auditmanager:GetEvidenceByEvidenceFolder` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence. |
| `auditmanager:GetEvidenceFolder` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence folder. |
| `auditmanager:GetEvidenceFoldersByAssessment` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager evidence folder. |
| `auditmanager:GetSettings` | Read-only permission to read settings and metadata for AWS Audit Manager resources in your AWS account. | AccuKnox uses this to evaluate AWS Audit Manager security settings against common misconfiguration and compliance checks. |
| `auditmanager:ListAssessmentFrameworks` | Read-only permission to list AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager framework. |
| `auditmanager:ListAssessments` | Read-only permission to list AWS Audit Manager resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your auditmanager assessment, auditmanager evidence, auditmanager evidence folder. |


## Amazon EC2 Auto Scaling (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `autoscaling:DescribeAutoScalingGroups` | Read-only permission to view configuration details for Amazon EC2 Auto Scaling resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 Auto Scaling security settings against common misconfiguration and compliance checks. |
| `autoscaling:DescribeLaunchConfigurations` | Read-only permission to view configuration details for Amazon EC2 Auto Scaling resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch configuration. |
| `autoscaling:DescribeNotificationConfigurations` | Read-only permission to view configuration details for Amazon EC2 Auto Scaling resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 Auto Scaling security settings against common misconfiguration and compliance checks. |


## AWS Backup (14)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `backup:DescribeBackupJob` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup jobs. |
| `backup:DescribeBackupVault` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults. |
| `backup:DescribeRecoveryPoint` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your backup recovery point. |
| `backup:DescribeRegionSettings` | Read-only permission to view configuration details for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox uses this to evaluate AWS Backup security settings against common misconfiguration and compliance checks. |
| `backup:GetBackupPlan` | Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans. |
| `backup:GetBackupSelection` | Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your backup selection. |
| `backup:GetBackupVaultAccessPolicy` | Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults. |
| `backup:GetBackupVaultNotifications` | Read-only permission to read settings and metadata for AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults. |
| `backup:ListBackupJobs` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup jobs. |
| `backup:ListBackupPlans` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans. |
| `backup:ListBackupSelections` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your backup selection. |
| `backup:ListBackupVaults` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup vaults. |
| `backup:ListRecoveryPointsByBackupVault` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your backup recovery point. |
| `backup:ListTags` | Read-only permission to list AWS Backup vaults, plans, and jobs in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Backup plans, AWS Backup vaults, backup recovery point. |


## Amazon Bedrock (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `bedrock:GetCustomModel` | Read-only permission to read settings and metadata for Amazon Bedrock resources in your AWS account. | AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks. |
| `bedrock:GetModelCustomizationJob` | Read-only permission to read settings and metadata for Amazon Bedrock resources in your AWS account. | AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks. |
| `bedrock:GetModelInvocationLoggingConfiguration` | Read-only permission to read settings and metadata for Amazon Bedrock resources in your AWS account. | AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks. |
| `bedrock:ListCustomModels` | Read-only permission to list Amazon Bedrock resources in your AWS account. | AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks. |
| `bedrock:ListModelCustomizationJobs` | Read-only permission to list Amazon Bedrock resources in your AWS account. | AccuKnox uses this to evaluate Amazon Bedrock security settings against common misconfiguration and compliance checks. |


## AWS CloudFormation (9)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `cloudformation:DescribeStackEvents` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. | AccuKnox uses this to evaluate AWS CloudFormation security settings against common misconfiguration and compliance checks. |
| `cloudformation:DescribeStackResource` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack resource. |
| `cloudformation:DescribeStackResources` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks. |
| `cloudformation:DescribeStackSet` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack set. |
| `cloudformation:DescribeStacks` | Read-only permission to view configuration details for AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks. |
| `cloudformation:GetTemplate` | Read-only permission to read settings and metadata for AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks. |
| `cloudformation:ListStackResources` | Read-only permission to list AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack resource. |
| `cloudformation:ListStackSets` | Read-only permission to list AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudformation stack set. |
| `cloudformation:ListStacks` | Read-only permission to list AWS CloudFormation resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFormation stacks, cloudformation stack resource. |


## Amazon CloudFront (9)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `cloudfront:DescribeFunction` | Read-only permission to view configuration details for Amazon CloudFront resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront function. |
| `cloudfront:GetCachePolicy` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront cache policy. |
| `cloudfront:GetDistribution` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFront distributions. |
| `cloudfront:GetDistributionConfig` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon CloudFront during security and inventory scans. |
| `cloudfront:GetFunction` | Read-only permission to read settings and metadata for Amazon CloudFront resources in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon CloudFront asset inventory. |
| `cloudfront:ListCachePolicies` | Read-only permission to list Amazon CloudFront resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront cache policy. |
| `cloudfront:ListDistributions` | Read-only permission to list Amazon CloudFront resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFront distributions. |
| `cloudfront:ListFunctions` | Read-only permission to list Amazon CloudFront resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudfront function. |
| `cloudfront:ListTagsForResource` | Read-only permission to list Amazon CloudFront resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudFront distributions. |


## AWS CloudTrail (7)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `cloudtrail:DescribeTrails` | Read-only permission to view configuration details for CloudTrail trails and logging settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |
| `cloudtrail:GetChannel` | Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudtrail channel. |
| `cloudtrail:GetEventSelectors` | Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |
| `cloudtrail:GetInsightSelectors` | Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |
| `cloudtrail:GetTrailStatus` | Read-only permission to read settings and metadata for CloudTrail trails and logging settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |
| `cloudtrail:ListChannels` | Read-only permission to list CloudTrail trails and logging settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudtrail channel. |
| `cloudtrail:ListTags` | Read-only permission to list CloudTrail trails and logging settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudTrail audit trails. |


## Amazon CloudWatch (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `cloudwatch:DescribeAlarms` | Read-only permission to view configuration details for CloudWatch alarms and metrics in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudwatch alarm. |
| `cloudwatch:GetMetricStatistics` | Read-only permission to read settings and metadata for CloudWatch alarms and metrics in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon CloudWatch asset inventory. AccuKnox uses this to evaluate Amazon CloudWatch security settings against common misconfiguration and compliance checks. |
| `cloudwatch:ListTagsForResource` | Read-only permission to list CloudWatch alarms and metrics in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cloudwatch alarm. |


## AWS CodeArtifact (8)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `codeartifact:DescribeDomain` | Read-only permission to view configuration details for AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain. |
| `codeartifact:DescribeRepository` | Read-only permission to view configuration details for AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository. |
| `codeartifact:GetDomainPermissionsPolicy` | Read-only permission to read settings and metadata for AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain. |
| `codeartifact:GetRepositoryEndpoint` | Read-only permission to read settings and metadata for AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository. |
| `codeartifact:GetRepositoryPermissionsPolicy` | Read-only permission to read settings and metadata for AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository. |
| `codeartifact:ListDomains` | Read-only permission to list AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain. |
| `codeartifact:ListRepositories` | Read-only permission to list AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact repository. |
| `codeartifact:ListTagsForResource` | Read-only permission to list AWS CodeArtifact resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codeartifact domain, codeartifact repository. |


## AWS CodeBuild (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `codebuild:BatchGetProjects` | Read-only permission to read details for AWS CodeBuild resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codebuild project. |
| `codebuild:ListProjects` | Read-only permission to list AWS CodeBuild resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codebuild project. |


## AWS CodeDeploy (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `codedeploy:GetDeploymentConfig` | Read-only permission to read settings and metadata for AWS CodeDeploy resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codedeploy deployment config. |
| `codedeploy:ListDeploymentConfigs` | Read-only permission to list AWS CodeDeploy resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codedeploy deployment config. |


## AWS CodePipeline (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `codepipeline:GetPipeline` | Read-only permission to read settings and metadata for AWS CodePipeline resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codepipeline pipeline. |
| `codepipeline:ListPipelines` | Read-only permission to list AWS CodePipeline resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codepipeline pipeline. |
| `codepipeline:ListTagsForResource` | Read-only permission to list AWS CodePipeline resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your codepipeline pipeline. |


## Amazon Cognito Identity Pools (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `cognito-identity:DescribeIdentityPool` | Read-only permission to view configuration details for Amazon Cognito Identity Pools resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito identity pool. |
| `cognito-identity:ListIdentityPools` | Read-only permission to list Amazon Cognito Identity Pools resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito identity pool. |


## Amazon Cognito User Pools (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `cognito-idp:DescribeUserPool` | Read-only permission to view configuration details for Amazon Cognito User Pools resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito user pool. |
| `cognito-idp:ListUserPools` | Read-only permission to list Amazon Cognito User Pools resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your cognito user pool. |


## Amazon Comprehend (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `comprehend:ListFlywheels` | Read-only permission to list Amazon Comprehend resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Comprehend during security and inventory scans. |
| `comprehend:ListSentimentDetectionJobs` | List Amazon Comprehend sentiment analysis jobs in your account. | AccuKnox checks whether Comprehend jobs use encryption for stored data and output. |


## AWS Compute Optimizer (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `compute-optimizer:GetRecommendationSummaries` | Read-only permission to read settings and metadata for AWS Compute Optimizer resources in your AWS account. | AccuKnox uses this to evaluate AWS Compute Optimizer security settings against common misconfiguration and compliance checks. |


## AWS Config (6)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `config:DescribeConfigRules` | Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account. | AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks. |
| `config:DescribeConfigurationRecorderStatus` | Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Config recorders. |
| `config:DescribeConfigurationRecorders` | Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS Config recorders. |
| `config:DescribeDeliveryChannels` | Read-only permission to view configuration details for AWS Config rules and recorders in your AWS account. | AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks. |
| `config:GetComplianceDetailsByConfigRule` | Read-only permission to read settings and metadata for AWS Config rules and recorders in your AWS account. | AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks. |
| `config:GetDiscoveredResourceCounts` | Read-only permission to read settings and metadata for AWS Config rules and recorders in your AWS account. | AccuKnox uses this to evaluate AWS Config security settings against common misconfiguration and compliance checks. |


## Amazon Connect (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `connect:DescribeInstanceStorageConfig` | Read-only permission to view configuration details for Amazon Connect resources in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon Connect asset inventory. AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks. |
| `connect:ListInstanceStorageConfigs` | Read-only permission to list Amazon Connect resources in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon Connect asset inventory. AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks. |
| `connect:ListInstances` | Read-only permission to list Amazon Connect resources in your AWS account. | AccuKnox uses this to evaluate Amazon Connect security settings against common misconfiguration and compliance checks. |


## AWS Glue DataBrew (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `databrew:ListJobs` | Read-only permission to list AWS Glue DataBrew resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Glue DataBrew during security and inventory scans. |


## Amazon DynamoDB Accelerator (DAX) (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `dax:DescribeClusters` | Read-only permission to view configuration details for Amazon DynamoDB Accelerator (DAX) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your dax cluster. |
| `dax:DescribeSubnetGroups` | Read-only permission to view configuration details for Amazon DynamoDB Accelerator (DAX) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your dax subnet group. |
| `dax:ListTags` | Read-only permission to list Amazon DynamoDB Accelerator (DAX) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your dax cluster. |


## Amazon DevOps Guru (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `devops-guru:ListNotificationChannels` | Read-only permission to list Amazon DevOps Guru resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon DevOps Guru during security and inventory scans. |


## Amazon Data Lifecycle Manager (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `dlm:GetLifecyclePolicies` | Read-only permission to read settings and metadata for Amazon Data Lifecycle Manager resources in your AWS account. | AccuKnox uses this to evaluate Amazon Data Lifecycle Manager security settings against common misconfiguration and compliance checks. |
| `dlm:GetLifecyclePolicy` | Read-only permission to read settings and metadata for Amazon Data Lifecycle Manager resources in your AWS account. | AccuKnox uses this to evaluate Amazon Data Lifecycle Manager security settings against common misconfiguration and compliance checks. |


## AWS Database Migration Service (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `dms:DescribeReplicationInstances` | Read-only permission to view configuration details for AWS Database Migration Service resources in your AWS account. | AccuKnox uses this to evaluate AWS Database Migration Service security settings against common misconfiguration and compliance checks. |


## Amazon DocumentDB (elastic clusters) (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `docdb-elastic:GetCluster` | Read-only permission to read settings and metadata for Amazon DocumentDB (elastic clusters) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster. |
| `docdb-elastic:ListClusters` | Read-only permission to list Amazon DocumentDB (elastic clusters) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster. |
| `docdb-elastic:ListTagsForResource` | Read-only permission to list Amazon DocumentDB (elastic clusters) resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster, docdb cluster snapshot. |


## Amazon DynamoDB (7)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `dynamodb:DescribeBackup` | Read-only permission to view configuration details for DynamoDB tables in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your dynamodb backup. |
| `dynamodb:DescribeContinuousBackups` | Read-only permission to view configuration details for DynamoDB tables in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables. |
| `dynamodb:DescribeKinesisStreamingDestination` | Read-only permission to view configuration details for DynamoDB tables in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables. |
| `dynamodb:DescribeTable` | Read-only permission to view configuration details for DynamoDB tables in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables. |
| `dynamodb:ListBackups` | Read-only permission to list DynamoDB tables in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your dynamodb backup. |
| `dynamodb:ListTables` | Read-only permission to list DynamoDB tables in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables. |
| `dynamodb:ListTagsOfResource` | Read-only permission to list DynamoDB tables in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your DynamoDB tables. |


## Amazon EC2 (39)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `ec2:DescribeAccountAttributes` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeAddresses` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your vpc eip. |
| `ec2:DescribeEgressOnlyInternetGateways` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeFlowLogs` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeImages` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeInstanceAttribute` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances). |
| `ec2:DescribeInstanceCreditSpecifications` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances). |
| `ec2:DescribeInstanceStatus` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances). |
| `ec2:DescribeInstanceTypeOfferings` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 instance availability. |
| `ec2:DescribeInstances` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances). |
| `ec2:DescribeInternetGateways` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeKeyPairs` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 key pair. |
| `ec2:DescribeLaunchTemplateVersions` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch template version. |
| `ec2:DescribeLaunchTemplates` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 launch template. |
| `ec2:DescribeManagedPrefixLists` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 managed prefix list. |
| `ec2:DescribeNatGateways` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC NAT gateways. |
| `ec2:DescribeNetworkAcls` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC network ACLs. |
| `ec2:DescribeNetworkInterfaces` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 network interface. |
| `ec2:DescribeRegions` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS regions. |
| `ec2:DescribeReservedInstances` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 reserved instance. |
| `ec2:DescribeReservedInstancesModifications` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ec2 reserved instance. |
| `ec2:DescribeRouteTables` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC route tables. |
| `ec2:DescribeSecurityGroupRules` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your vpc security group rule. |
| `ec2:DescribeSecurityGroups` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC security groups, vpc security group rule. |
| `ec2:DescribeSnapshotAttribute` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs snapshot. |
| `ec2:DescribeSnapshots` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs snapshot. |
| `ec2:DescribeSubnets` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC subnets. |
| `ec2:DescribeVolumeAttribute` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs volume. |
| `ec2:DescribeVolumes` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ebs volume. |
| `ec2:DescribeVpcEndpointServicePermissions` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeVpcEndpointServices` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeVpcEndpoints` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeVpcPeeringConnections` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeVpcs` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your VPC networks. |
| `ec2:DescribeVpnConnections` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:DescribeVpnGateways` | Read-only permission to view configuration details for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:GetEbsDefaultKmsKeyId` | Read-only permission to read settings and metadata for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:GetEbsEncryptionByDefault` | Read-only permission to read settings and metadata for EC2 compute and networking resources in your AWS account. | AccuKnox uses this to evaluate Amazon EC2 security settings against common misconfiguration and compliance checks. |
| `ec2:GetLaunchTemplateData` | Read-only permission to read settings and metadata for EC2 compute and networking resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your EC2 virtual machines (instances). |


## Amazon ECR (container registry) (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `ecr:DescribeRepositories` | Read-only permission to view configuration details for Amazon ECR (container registry) resources in your AWS account. | AccuKnox uses this to evaluate Amazon ECR (container registry) security settings against common misconfiguration and compliance checks. |
| `ecr:GetRepositoryPolicy` | Read-only permission to read settings and metadata for Amazon ECR (container registry) resources in your AWS account. | AccuKnox uses this to evaluate Amazon ECR (container registry) security settings against common misconfiguration and compliance checks. |


## Amazon ECS (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `ecs:DescribeClusters` | Read-only permission to view configuration details for ECS clusters and services in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ECS clusters. |
| `ecs:DescribeServices` | Read-only permission to view configuration details for ECS clusters and services in your AWS account. | AccuKnox uses this to evaluate Amazon ECS security settings against common misconfiguration and compliance checks. |
| `ecs:ListClusters` | Read-only permission to list ECS clusters and services in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ECS clusters. |
| `ecs:ListServices` | Read-only permission to list ECS clusters and services in your AWS account. | AccuKnox uses this to evaluate Amazon ECS security settings against common misconfiguration and compliance checks. |
| `ecs:ListTagsForResource` | Read-only permission to list ECS clusters and services in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ECS clusters. |


## Amazon EKS (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `eks:DescribeCluster` | Read-only permission to view configuration details for EKS Kubernetes clusters in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your EKS Kubernetes clusters. |
| `eks:ListClusters` | Read-only permission to list EKS Kubernetes clusters in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your EKS Kubernetes clusters. |


## Amazon ElastiCache (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `elasticache:DescribeCacheClusters` | Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ElastiCache clusters. |
| `elasticache:DescribeCacheSubnetGroups` | Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account. | AccuKnox uses this to evaluate Amazon ElastiCache security settings against common misconfiguration and compliance checks. |
| `elasticache:DescribeReplicationGroups` | Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account. | AccuKnox uses this to evaluate Amazon ElastiCache security settings against common misconfiguration and compliance checks. |
| `elasticache:DescribeReservedCacheNodes` | Read-only permission to view configuration details for Amazon ElastiCache resources in your AWS account. | AccuKnox uses this to evaluate Amazon ElastiCache security settings against common misconfiguration and compliance checks. |
| `elasticache:ListTagsForResource` | Read-only permission to list Amazon ElastiCache resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your ElastiCache clusters. |


## Amazon EFS (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `elasticfilesystem:DescribeFileSystems` | Read-only permission to view configuration details for Amazon EFS resources in your AWS account. | AccuKnox uses this to evaluate Amazon EFS security settings against common misconfiguration and compliance checks. |


## Elastic Load Balancing (ALB/NLB/CLB) (9)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `elasticloadbalancing:DescribeInstanceHealth` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox uses this to evaluate Elastic Load Balancing (ALB/NLB/CLB) security settings against common misconfiguration and compliance checks. |
| `elasticloadbalancing:DescribeListeners` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox uses this to evaluate Elastic Load Balancing (ALB/NLB/CLB) security settings against common misconfiguration and compliance checks. |
| `elasticloadbalancing:DescribeLoadBalancerAttributes` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers. |
| `elasticloadbalancing:DescribeLoadBalancerPolicies` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox uses this to evaluate Elastic Load Balancing (ALB/NLB/CLB) security settings against common misconfiguration and compliance checks. |
| `elasticloadbalancing:DescribeLoadBalancers` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers, ec2 load balancer listener. |
| `elasticloadbalancing:DescribeTags` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Application load balancers, Network load balancers, load balancer target groups. |
| `elasticloadbalancing:DescribeTargetGroupAttributes` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox uses this to evaluate Elastic Load Balancing (ALB/NLB/CLB) security settings against common misconfiguration and compliance checks. |
| `elasticloadbalancing:DescribeTargetGroups` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your load balancer target groups. |
| `elasticloadbalancing:DescribeTargetHealth` | Read-only permission to view configuration details for load balancers and target groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your load balancer target groups. |


## Amazon EMR (4)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `elasticmapreduce:DescribeCluster` | Read-only permission to view configuration details for Amazon EMR resources in your AWS account. | AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks. |
| `elasticmapreduce:DescribeSecurityConfiguration` | Read-only permission to view configuration details for Amazon EMR resources in your AWS account. | AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks. |
| `elasticmapreduce:ListClusters` | Read-only permission to list Amazon EMR resources in your AWS account. | AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks. |
| `elasticmapreduce:ListInstanceGroups` | Read-only permission to list Amazon EMR resources in your AWS account. | AccuKnox uses this to evaluate Amazon EMR security settings against common misconfiguration and compliance checks. |


## Amazon OpenSearch Service (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `es:ListDomainNames` | Read-only permission to list Amazon OpenSearch Service resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon OpenSearch Service during security and inventory scans. |


## Amazon EventBridge (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `events:ListEventBuses` | Read-only permission to list Amazon EventBridge resources in your AWS account. | AccuKnox uses this to evaluate Amazon EventBridge security settings against common misconfiguration and compliance checks. |
| `events:ListRules` | Read-only permission to list Amazon EventBridge resources in your AWS account. | AccuKnox uses this to evaluate Amazon EventBridge security settings against common misconfiguration and compliance checks. |


## Amazon FinSpace (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `finspace:ListEnvironments` | Read-only permission to list Amazon FinSpace resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon FinSpace during security and inventory scans. |


## Amazon Kinesis Data Firehose (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `firehose:DescribeDeliveryStream` | Read-only permission to view configuration details for Amazon Kinesis Data Firehose resources in your AWS account. | AccuKnox uses this to evaluate Amazon Kinesis Data Firehose security settings against common misconfiguration and compliance checks. |
| `firehose:ListDeliveryStreams` | Read-only permission to list Amazon Kinesis Data Firehose resources in your AWS account. | AccuKnox uses this to evaluate Amazon Kinesis Data Firehose security settings against common misconfiguration and compliance checks. |


## Amazon Forecast (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `forecast:ListDatasets` | Read-only permission to list Amazon Forecast resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Forecast during security and inventory scans. |
| `forecast:ListForecastExportJobs` | Read-only permission to list Amazon Forecast resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Forecast during security and inventory scans. |


## Amazon Fraud Detector (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `frauddetector:GetDetectors` | Read-only permission to read settings and metadata for Amazon Fraud Detector resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Fraud Detector during security and inventory scans. |


## Amazon FSx (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `fsx:DescribeFileSystems` | Read-only permission to view configuration details for Amazon FSx resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon FSx during security and inventory scans. |


## Amazon S3 Glacier (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `glacier:ListVaults` | Read-only permission to list Amazon S3 Glacier resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon S3 Glacier during security and inventory scans. |


## AWS Glue (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `glue:GetDataCatalogEncryptionSettings` | Read-only permission to read settings and metadata for AWS Glue resources in your AWS account. | AccuKnox uses this to evaluate AWS Glue security settings against common misconfiguration and compliance checks. |
| `glue:GetSecurityConfigurations` | Read-only permission to read settings and metadata for AWS Glue resources in your AWS account. | AccuKnox uses this to evaluate AWS Glue security settings against common misconfiguration and compliance checks. |


## Amazon GuardDuty (7)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `guardduty:DescribePublishingDestination` | Read-only permission to view configuration details for GuardDuty threat detection settings in your AWS account. | AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:GetDetector` | Read-only permission to read settings and metadata for GuardDuty threat detection settings in your AWS account. | AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:GetFindings` | Read-only permission to read settings and metadata for GuardDuty threat detection settings in your AWS account. | AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:GetMasterAccount` | Read-only permission to read settings and metadata for GuardDuty threat detection settings in your AWS account. | AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:ListDetectors` | Read-only permission to list GuardDuty threat detection settings in your AWS account. | AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:ListFindings` | Read-only permission to list GuardDuty threat detection settings in your AWS account. | AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |
| `guardduty:ListPublishingDestinations` | Read-only permission to list GuardDuty threat detection settings in your AWS account. | AccuKnox uses this to evaluate Amazon GuardDuty security settings against common misconfiguration and compliance checks. |


## Amazon HealthLake (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `healthlake:ListFHIRDatastores` | Read-only permission to list Amazon HealthLake resources in your AWS account. | AccuKnox uses this to evaluate Amazon HealthLake security settings against common misconfiguration and compliance checks. |


## AWS IAM (31)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `iam:GenerateCredentialReport` | Request generation of the IAM credential report (password age, access key rotation, MFA status). | AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:GetAccountPasswordPolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:GetAccountSummary` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:GetCredentialReport` | Download the IAM credential report after it has been generated. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS IAM during security and inventory scans. |
| `iam:GetGroup` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups. |
| `iam:GetGroupPolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups. |
| `iam:GetLoginProfile` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:GetPolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM customer-managed policies, attached aws iam policy. |
| `iam:GetPolicyVersion` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM customer-managed policies, attached aws iam policy. |
| `iam:GetRole` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:GetRolePolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:GetUser` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:GetUserPolicy` | Read-only permission to read settings and metadata for IAM users, roles, groups, and policies in your AWS account. | AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:ListAccountAliases` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS account metadata. |
| `iam:ListAttachedGroupPolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups. |
| `iam:ListAttachedRolePolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:ListAttachedUserPolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:ListEntitiesForPolicy` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your iam policy attachment. |
| `iam:ListGroupPolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups. |
| `iam:ListGroups` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM groups. |
| `iam:ListGroupsForUser` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:ListInstanceProfilesForRole` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:ListMFADevices` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:ListPolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM customer-managed policies, attached aws iam policy. |
| `iam:ListRolePolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:ListRoles` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM roles. |
| `iam:ListSSHPublicKeys` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:ListServerCertificates` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |
| `iam:ListUserPolicies` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:ListUsers` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your IAM users. |
| `iam:ListVirtualMFADevices` | Read-only permission to list IAM users, roles, groups, and policies in your AWS account. | AccuKnox uses this to evaluate AWS IAM security settings against common misconfiguration and compliance checks. |


## EC2 Image Builder (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `imagebuilder:ListComponents` | Read-only permission to list EC2 Image Builder resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of EC2 Image Builder during security and inventory scans. |
| `imagebuilder:ListContainerRecipes` | Read-only permission to list EC2 Image Builder resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of EC2 Image Builder during security and inventory scans. |
| `imagebuilder:ListImagePipelines` | Read-only permission to list EC2 Image Builder resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of EC2 Image Builder during security and inventory scans. |
| `imagebuilder:ListImageRecipes` | Read-only permission to list EC2 Image Builder resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of EC2 Image Builder during security and inventory scans. |
| `imagebuilder:ListInfrastructureConfigurations` | Read-only permission to list EC2 Image Builder resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of EC2 Image Builder during security and inventory scans. |


## AWS IoT SiteWise (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `iotsitewise:DescribeDefaultEncryptionConfiguration` | Read-only permission to view configuration details for AWS IoT SiteWise resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS IoT SiteWise during security and inventory scans. |


## Amazon MSK (Kafka) (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `kafka:ListClusters` | Read-only permission to list Amazon MSK (Kafka) resources in your AWS account. | AccuKnox uses this to evaluate Amazon MSK (Kafka) security settings against common misconfiguration and compliance checks. |


## Amazon Kendra (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `kendra:ListIndices` | Read-only permission to list Amazon Kendra resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Kendra during security and inventory scans. |


## Amazon Kinesis Data Streams (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `kinesis:DescribeStream` | Read-only permission to view configuration details for Amazon Kinesis Data Streams resources in your AWS account. | AccuKnox uses this to evaluate Amazon Kinesis Data Streams security settings against common misconfiguration and compliance checks. |
| `kinesis:ListStreams` | Read-only permission to list Amazon Kinesis Data Streams resources in your AWS account. | AccuKnox uses this to evaluate Amazon Kinesis Data Streams security settings against common misconfiguration and compliance checks. |


## Amazon Kinesis Video Streams (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `kinesisvideo:ListStreams` | Read-only permission to list Amazon Kinesis Video Streams resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Kinesis Video Streams during security and inventory scans. |


## AWS KMS (7)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `kms:DescribeKey` | Read-only permission to view configuration details for KMS encryption keys in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:GetKeyPolicy` | Read-only permission to read settings and metadata for KMS encryption keys in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:GetKeyRotationStatus` | Read-only permission to read settings and metadata for KMS encryption keys in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:ListAliases` | Read-only permission to list KMS encryption keys in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:ListGrants` | Read-only permission to list KMS encryption keys in your AWS account. | AccuKnox uses this to evaluate AWS KMS security settings against common misconfiguration and compliance checks. |
| `kms:ListKeys` | Read-only permission to list KMS encryption keys in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |
| `kms:ListResourceTags` | Read-only permission to list KMS encryption keys in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your KMS encryption keys. |


## AWS Lambda (6)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `lambda:GetFunction` | Read-only permission to read settings and metadata for Lambda functions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions. |
| `lambda:GetFunctionCodeSigningConfig` | Read-only permission to read settings and metadata for Lambda functions in your AWS account. | AccuKnox uses this to evaluate AWS Lambda security settings against common misconfiguration and compliance checks. |
| `lambda:GetFunctionConfiguration` | Read-only permission to read settings and metadata for Lambda functions in your AWS account. | AccuKnox uses this to evaluate AWS Lambda security settings against common misconfiguration and compliance checks. |
| `lambda:GetFunctionUrlConfig` | Read-only permission to read settings and metadata for Lambda functions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions. |
| `lambda:GetPolicy` | Read-only permission to read settings and metadata for Lambda functions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions. |
| `lambda:ListFunctions` | Read-only permission to list Lambda functions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Lambda functions. |


## Amazon Lex (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `lex:ListBots` | Read-only permission to list Amazon Lex resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Lex during security and inventory scans. |


## Amazon CloudWatch Logs (4)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `logs:DescribeLogGroups` | Read-only permission to view configuration details for CloudWatch Logs log groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups. |
| `logs:DescribeMetricFilters` | Read-only permission to view configuration details for CloudWatch Logs log groups in your AWS account. | AccuKnox uses this to evaluate Amazon CloudWatch Logs security settings against common misconfiguration and compliance checks. |
| `logs:GetDataProtectionPolicy` | Read-only permission to read settings and metadata for CloudWatch Logs log groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups. |
| `logs:ListTagsForResource` | Read-only permission to list CloudWatch Logs log groups in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your CloudWatch log groups. |


## Amazon Lookout for Equipment (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `lookoutequipment:ListDatasets` | Read-only permission to list Amazon Lookout for Equipment resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Lookout for Equipment during security and inventory scans. |


## Amazon Managed Blockchain (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `managedblockchain:GetMember` | Read-only permission to read settings and metadata for Amazon Managed Blockchain resources in your AWS account. | AccuKnox uses this to evaluate Amazon Managed Blockchain security settings against common misconfiguration and compliance checks. |
| `managedblockchain:ListMembers` | Read-only permission to list Amazon Managed Blockchain resources in your AWS account. | AccuKnox uses this to evaluate Amazon Managed Blockchain security settings against common misconfiguration and compliance checks. |
| `managedblockchain:ListNetworks` | Read-only permission to list Amazon Managed Blockchain resources in your AWS account. | AccuKnox uses this to evaluate Amazon Managed Blockchain security settings against common misconfiguration and compliance checks. |


## Amazon MemoryDB (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `memorydb:DescribeClusters` | Read-only permission to view configuration details for Amazon MemoryDB resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon MemoryDB during security and inventory scans. |


## Amazon MQ (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `mq:DescribeBroker` | Read-only permission to view configuration details for Amazon MQ resources in your AWS account. | AccuKnox uses this to evaluate Amazon MQ security settings against common misconfiguration and compliance checks. |
| `mq:ListBrokers` | Read-only permission to list Amazon MQ resources in your AWS account. | AccuKnox uses this to evaluate Amazon MQ security settings against common misconfiguration and compliance checks. |


## AWS Organizations (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `organizations:DescribeOrganization` | Read-only permission to view configuration details for AWS Organizations account structure in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your AWS account metadata. |
| `organizations:ListAccounts` | Read-only permission to list AWS Organizations account structure in your AWS account. | AccuKnox uses this to evaluate AWS Organizations security settings against common misconfiguration and compliance checks. |
| `organizations:ListHandshakesForAccount` | Read-only permission to list AWS Organizations account structure in your AWS account. | AccuKnox uses this to evaluate AWS Organizations security settings against common misconfiguration and compliance checks. |


## Amazon Connect Customer Profiles (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `profile:ListDomains` | Read-only permission to list Amazon Connect Customer Profiles resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Connect Customer Profiles during security and inventory scans. |


## AWS Proton (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `proton:ListEnvironmentTemplates` | Read-only permission to list AWS Proton resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Proton during security and inventory scans. |


## Amazon RDS (15)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `rds:DescribeCertificates` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances. |
| `rds:DescribeDBClusterSnapshotAttributes` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon RDS asset inventory. AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBClusterSnapshots` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox uses this read-only call as part of building your Amazon RDS asset inventory. AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBClusters` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS/Aurora database clusters. |
| `rds:DescribeDBEngineVersions` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBInstances` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances, docdb cluster instance. |
| `rds:DescribeDBParameterGroups` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBParameters` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBProxies` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your rds db proxy. |
| `rds:DescribeDBSnapshotAttributes` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBSnapshots` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox uses this to evaluate Amazon RDS security settings against common misconfiguration and compliance checks. |
| `rds:DescribeDBSubnetGroups` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your rds db subnet group. |
| `rds:DescribeOrderableDBInstanceOptions` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances. |
| `rds:DescribePendingMaintenanceActions` | Read-only permission to view configuration details for RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your RDS database instances, RDS/Aurora database clusters. |
| `rds:ListTagsForResource` | Read-only permission to list RDS and Aurora databases in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your docdb cluster instance, rds db proxy, rds db subnet group. |


## Amazon Redshift Serverless (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `redshift-serverless:GetNamespace` | Read-only permission to read settings and metadata for Amazon Redshift Serverless resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace. |
| `redshift-serverless:GetWorkgroup` | Read-only permission to read settings and metadata for Amazon Redshift Serverless resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless workgroup. |
| `redshift-serverless:ListNamespaces` | Read-only permission to list Amazon Redshift Serverless resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace. |
| `redshift-serverless:ListTagsForResource` | Read-only permission to list Amazon Redshift Serverless resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless namespace, redshiftserverless workgroup. |
| `redshift-serverless:ListWorkgroups` | Read-only permission to list Amazon Redshift Serverless resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your redshiftserverless workgroup. |


## Amazon Redshift (7)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `redshift:DescribeClusterParameterGroups` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. | AccuKnox uses this to evaluate Amazon Redshift security settings against common misconfiguration and compliance checks. |
| `redshift:DescribeClusterParameters` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. | AccuKnox uses this to evaluate Amazon Redshift security settings against common misconfiguration and compliance checks. |
| `redshift:DescribeClusterSubnetGroups` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your redshift subnet group. |
| `redshift:DescribeClusters` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Redshift clusters. |
| `redshift:DescribeLoggingStatus` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Redshift clusters. |
| `redshift:DescribeReservedNodes` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. | AccuKnox uses this to evaluate Amazon Redshift security settings against common misconfiguration and compliance checks. |
| `redshift:DescribeScheduledActions` | Read-only permission to view configuration details for Redshift data warehouses in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Redshift clusters. |


## Amazon Route 53 (6)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `route53:GetDNSSEC` | Read-only permission to read settings and metadata for Route 53 DNS zones and records in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones. |
| `route53:GetHostedZone` | Read-only permission to read settings and metadata for Route 53 DNS zones and records in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones. |
| `route53:ListHostedZones` | Read-only permission to list Route 53 DNS zones and records in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones. |
| `route53:ListQueryLoggingConfigs` | Read-only permission to list Route 53 DNS zones and records in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones. |
| `route53:ListResourceRecordSets` | Read-only permission to list Route 53 DNS zones and records in your AWS account. | AccuKnox uses this to evaluate Amazon Route 53 security settings against common misconfiguration and compliance checks. |
| `route53:ListTagsForResource` | Read-only permission to list Route 53 DNS zones and records in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your Route 53 hosted zones. |


## Amazon Route 53 Domains (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `route53domains:GetDomainDetail` | Read-only permission to read settings and metadata for Amazon Route 53 Domains resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your route53 domain. |
| `route53domains:ListDomains` | Read-only permission to list Amazon Route 53 Domains resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your route53 domain. |
| `route53domains:ListTagsForDomain` | Read-only permission to list Amazon Route 53 Domains resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your route53 domain. |


## Amazon S3 (22)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `s3:GetAccelerateConfiguration` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon S3 during security and inventory scans. |
| `s3:GetAccessPoint` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point. |
| `s3:GetAccessPointPolicy` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point. |
| `s3:GetAccessPointPolicyStatus` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point. |
| `s3:GetBucketAcl` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketLocation` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox uses this to evaluate Amazon S3 security settings against common misconfiguration and compliance checks. |
| `s3:GetBucketLogging` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketNotification` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketObjectLockConfiguration` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketOwnershipControls` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketPolicy` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketPolicyStatus` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketPublicAccessBlock` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketTagging` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketVersioning` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetBucketWebsite` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetEncryptionConfiguration` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetLifecycleConfiguration` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:GetReplicationConfiguration` | Read-only permission to read settings and metadata for S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:ListAccessPoints` | Read-only permission to list S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your s3 access point. |
| `s3:ListAllMyBuckets` | Read-only permission to list S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |
| `s3:ListBucket` | Read-only permission to list S3 buckets and bucket settings in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your S3 storage buckets. |


## Amazon SageMaker (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `sagemaker:DescribeDomain` | Read-only permission to view configuration details for Amazon SageMaker resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your sagemaker domain. |
| `sagemaker:DescribeNotebookInstance` | Read-only permission to view configuration details for Amazon SageMaker resources in your AWS account. | AccuKnox uses this to evaluate Amazon SageMaker security settings against common misconfiguration and compliance checks. |
| `sagemaker:ListDomains` | Read-only permission to list Amazon SageMaker resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your sagemaker domain. |
| `sagemaker:ListNotebookInstances` | Read-only permission to list Amazon SageMaker resources in your AWS account. | AccuKnox uses this to evaluate Amazon SageMaker security settings against common misconfiguration and compliance checks. |
| `sagemaker:ListTags` | Read-only permission to list Amazon SageMaker resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your sagemaker domain. |


## AWS Secrets Manager (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `secretsmanager:DescribeSecret` | Read-only permission to view configuration details for Secrets Manager secrets in your AWS account. | AccuKnox uses this to evaluate AWS Secrets Manager security settings against common misconfiguration and compliance checks. |
| `secretsmanager:ListSecrets` | Read-only permission to list Secrets Manager secrets in your AWS account. | AccuKnox uses this to evaluate AWS Secrets Manager security settings against common misconfiguration and compliance checks. |


## AWS Security Hub (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `securityhub:DescribeHub` | Read-only permission to view configuration details for Security Hub findings and hub configuration in your AWS account. | AccuKnox uses this to evaluate AWS Security Hub security settings against common misconfiguration and compliance checks. |
| `securityhub:GetFindings` | Read-only permission to read settings and metadata for Security Hub findings and hub configuration in your AWS account. | AccuKnox uses this to evaluate AWS Security Hub security settings against common misconfiguration and compliance checks. |


## AWS Service Quotas (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `servicequotas:ListServiceQuotas` | Read-only permission to list AWS Service Quotas resources in your AWS account. | AccuKnox uses this to evaluate AWS Service Quotas security settings against common misconfiguration and compliance checks. |


## Amazon SES (email) (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `ses:DescribeActiveReceiptRuleSet` | Read-only permission to view configuration details for Amazon SES (email) resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon SES (email) during security and inventory scans. |
| `ses:GetIdentityDkimAttributes` | Read DKIM signing settings for your Amazon SES email identities. | AccuKnox checks whether outbound email identities have DKIM enabled to reduce spoofing risk. |
| `ses:ListIdentities` | Read-only permission to list Amazon SES (email) resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon SES (email) during security and inventory scans. |


## AWS Shield (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `shield:DescribeEmergencyContactSettings` | Read-only permission to view configuration details for AWS Shield resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Shield during security and inventory scans. |
| `shield:DescribeSubscription` | Read-only permission to view configuration details for AWS Shield resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Shield during security and inventory scans. |
| `shield:ListProtections` | Read-only permission to list AWS Shield resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS Shield during security and inventory scans. |


## Amazon SNS (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `sns:GetSubscriptionAttributes` | Read-only permission to read settings and metadata for SNS topics and subscriptions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your sns subscription. |
| `sns:GetTopicAttributes` | Read-only permission to read settings and metadata for SNS topics and subscriptions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your SNS notification topics. |
| `sns:ListSubscriptions` | Read-only permission to list SNS topics and subscriptions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your sns subscription. |
| `sns:ListTagsForResource` | Read-only permission to list SNS topics and subscriptions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your SNS notification topics. |
| `sns:ListTopics` | Read-only permission to list SNS topics and subscriptions in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your SNS notification topics. |


## Amazon SQS (3)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `sqs:GetQueueAttributes` | Read-only permission to read settings and metadata for SQS queues in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your SQS message queues. |
| `sqs:ListQueueTags` | Read-only permission to list SQS queues in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your SQS message queues. |
| `sqs:ListQueues` | Read-only permission to list SQS queues in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your SQS message queues. |


## AWS Systems Manager (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `ssm:DescribeInstanceInformation` | Read-only permission to view configuration details for AWS Systems Manager resources in your AWS account. | AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |
| `ssm:DescribeParameters` | Read-only permission to view configuration details for AWS Systems Manager resources in your AWS account. | AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |
| `ssm:DescribeSessions` | Read-only permission to view configuration details for AWS Systems Manager resources in your AWS account. | AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |
| `ssm:GetServiceSetting` | Read-only permission to read settings and metadata for AWS Systems Manager resources in your AWS account. | AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |
| `ssm:ListAssociations` | Read-only permission to list AWS Systems Manager resources in your AWS account. | AccuKnox uses this to evaluate AWS Systems Manager security settings against common misconfiguration and compliance checks. |


## AWS STS (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `sts:GetCallerIdentity` | Confirm which AWS account and identity is being used — required for onboarding and credential validation. | AccuKnox uses this to evaluate AWS STS security settings against common misconfiguration and compliance checks. |


## AWS Resource Groups Tagging API (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `tag:GetResources` | Read-only permission to read settings and metadata for resource tags across your AWS environment in your AWS account. | AccuKnox uses this to evaluate AWS Resource Groups Tagging API security settings against common misconfiguration and compliance checks. |
| `tag:GetTagKeys` | Read-only permission to read settings and metadata for resource tags across your AWS environment in your AWS account. | AccuKnox uses this to evaluate AWS Resource Groups Tagging API security settings against common misconfiguration and compliance checks. |


## Amazon Timestream (2)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `timestream:DescribeEndpoints` | Read-only permission to view configuration details for Amazon Timestream resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Timestream during security and inventory scans. |
| `timestream:ListDatabases` | List Amazon Timestream databases in your account. | AccuKnox verifies that Timestream databases have encryption enabled. |


## AWS Transfer Family (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `transfer:ListServers` | Read-only permission to list AWS Transfer Family resources in your AWS account. | AccuKnox uses this to evaluate AWS Transfer Family security settings against common misconfiguration and compliance checks. |


## Amazon Translate (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `translate:ListTextTranslationJobs` | Read-only permission to list Amazon Translate resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of Amazon Translate during security and inventory scans. |


## AWS WAF (Regional Classic) (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `waf-regional:ListWebACLs` | Read-only permission to list AWS WAF (Regional Classic) resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS WAF (Regional Classic) during security and inventory scans. |


## AWS WAF (Classic) (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `waf:ListWebACLs` | Read-only permission to list AWS WAF (Classic) resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS WAF (Classic) during security and inventory scans. |


## AWS WAFv2 (4)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `wafv2:GetLoggingConfiguration` | Read-only permission to read settings and metadata for AWS WAF web ACLs in your AWS account. | AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks. |
| `wafv2:GetWebACL` | Read-only permission to read settings and metadata for AWS WAF web ACLs in your AWS account. | AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks. |
| `wafv2:ListResourcesForWebACL` | Read-only permission to list AWS WAF web ACLs in your AWS account. | AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks. |
| `wafv2:ListWebACLs` | Read-only permission to list AWS WAF web ACLs in your AWS account. | AccuKnox uses this to evaluate AWS WAFv2 security settings against common misconfiguration and compliance checks. |


## Amazon WorkSpaces (5)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `workspaces:DescribeIpGroups` | Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account. | AccuKnox uses this to evaluate Amazon WorkSpaces security settings against common misconfiguration and compliance checks. |
| `workspaces:DescribeTags` | Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your workspaces workspace. |
| `workspaces:DescribeWorkspaceDirectories` | Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account. | AccuKnox uses this to evaluate Amazon WorkSpaces security settings against common misconfiguration and compliance checks. |
| `workspaces:DescribeWorkspaces` | Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account. | AccuKnox needs this to discover and maintain an up-to-date inventory of your workspaces workspace. |
| `workspaces:DescribeWorkspacesConnectionStatus` | Read-only permission to view configuration details for Amazon WorkSpaces resources in your AWS account. | AccuKnox uses this to evaluate Amazon WorkSpaces security settings against common misconfiguration and compliance checks. |


## AWS X-Ray (1)

| Permission | What it does | Why AccuKnox needs it |
|---|---|---|
| `xray:GetEncryptionConfig` | Read-only permission to read settings and metadata for AWS X-Ray resources in your AWS account. | AccuKnox identified this as a required read-only permission to ensure complete coverage of AWS X-Ray during security and inventory scans. |
