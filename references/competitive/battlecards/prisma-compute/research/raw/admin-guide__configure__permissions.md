For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/permissions.md).

When you set up Prisma Cloud Compute to secure your cloud workloads, you’ll need to ensure you’ve granted Prisma Cloud the right permissions. The following tables list the permissions required for each of Compute’s protection capabilities.

You can review the permissions needed for each cloud service provider:

- [AWS required permissions](https://docs.prismacloud.io/admin-guide/configure/permissions#aws)

- [Azure required permissions](https://docs.prismacloud.io/admin-guide/configure/permissions#azure)

- [GCP required permissions](https://docs.prismacloud.io/admin-guide/configure/permissions#gcp)


You can review the permissions needed for agentless scanning in each cloud service provider:

- [AWS required permission for agentless scanning](https://docs.prismacloud.io/admin-guide/configure/permissions#aws-agentless)

- [Azure required permission for agentless scanning](https://docs.prismacloud.io/admin-guide/configure/permissions#azure-agentless)

- [GCP required permission for agentless scanning](https://docs.prismacloud.io/admin-guide/configure/permissions#gcp-agentless)


## AWS[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/permissions\#aws)

The following table shows the required permissions needed if you are using AWS. You can also review the [permissions needed for agentless scanning in AWS](https://docs.prismacloud.io/admin-guide/configure/permissions#aws-agentless).

Capability

Feature

Permissions

Role/Policy

Condition

Workload Discovery

Workload Discovery

Serverless Radar

cloudwatch:DescribeAlarms

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

iam:GetPolicyVersion

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

iam:GetRole

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

iam:GetPolicy

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

iam:GetRolePolicy

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

iam:ListRolePolicies

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

iam:ListAttachedRolePolicies

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

lambda:ListFunctions

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

lambda:GetFunction

PrismaCloud-ReadOnly-Policy-Compute

Workload Discovery

Serverless Radar

lambda:ListAliases

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

lambda:ListEventSourceMappings

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

lambda:GetPolicy

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

kms:Decrypt

PrismaCloud-ReadOnly-Policy-Compute

Workload Discovery

Serverless Radar

logs:DescribeSubscriptionFilters

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

s3:GetBucketNotification

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

elasticloadbalancing:DescribeListeners

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

elasticloadbalancing:DescribeTargetGroups

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

elasticloadbalancing:DescribeListenerCertificates

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

elasticloadbalancing:DescribeRules

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

cloudfront:ListDistributions

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

events:ListRules

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

Serverless Radar

apigateway:GET

arn:aws:iam::aws:policy/SecurityAudit

Workload Discovery

VM Tags Discovery

ec2:DescribeTags

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Agent-Based Workload Scan

Registry Scanning

ecr:GetAuthorizationToken

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Registry Scanning

ecr:BatchCheckLayerAvailability

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Registry Scanning

ecr:GetDownloadUrlForLayer

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Registry Scanning

ecr:GetRepositoryPolicy

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Registry Scanning

ecr:DescribeRepositories

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Registry Scanning

ecr:ListImages

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Registry Scanning

ecr:DescribeImages

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Registry Scanning

ecr:BatchGetImage

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Registry Scanning

ecr:GetLifecyclePolicy

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Registry Scanning

ecr:GetLifecyclePolicyPreview

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Registry Scanning

ecr:ListTagsForResource

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Registry Scanning

ecr:DescribeImageScanFindings

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

lambda:PublishLayerVersion

PrismaCloud-Remediation-Compute-Policy-ServerlessAutoDefend

Agent-Based Workload Scan

Serverless Auto Defend

lambda:UpdateFunctionConfiguration

PrismaCloud-IAM-Remediation-Policy

Agent-Based Workload Scan

Serverless Auto Defend

lambda:GetLayerVersion

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Serverless Auto Defend

lambda:GetFunctionConfiguration

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

iam:SimulatePrincipalPolicy

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

lambda:GetFunction

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Serverless Auto Defend

lambda:ListFunctions

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

iam:GetPolicyVersion

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

iam:GetRole

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

iam:ListRolePolicies

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

iam:ListAttachedRolePolicies

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

iam:GetRolePolicy

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

iam:GetPolicy

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

lambda:ListLayerVersions

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

lambda:ListLayers

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Serverless Auto Defend

lambda:DeleteLayerVersion

PrismaCloud-Remediation-Compute-Policy-ServerlessAutoDefend

Agent-Based Workload Scan

Serverless Auto Defend

kms:Decrypt

PrismaCloud-ReadOnly-Policy-Compute

Agent-Based Workload Scan

Serverless Auto Defend

kms:Encrypt

PrismaCloud-Remediation-Compute-Policy-AgentlessScanning

Agent-Based Workload Scan

Serverless Auto Defend

kms:CreateGrant

PrismaCloud-Remediation-Compute-Policy-AgentlessScanning

Agent-Based Workload Scan

VM Images Scan

ec2:CreateSecurityGroup

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:DescribeSecurityGroups

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

VM Images Scan

ec2:RevokeSecurityGroupEgress

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:AuthorizeSecurityGroupIngress

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:DeleteSecurityGroup

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:RunInstances

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:DescribeInstances

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

VM Images Scan

ec2:TerminateInstances

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:DescribeImages

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

VM Images Scan

ec2:CreateTags

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:AuthorizeSecurityGroupEgress

PrismaCloud-Remediation-Compute-Policy-AMIScan

Agent-Based Workload Scan

VM Images Scan

ec2:DescribeSubnets

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

VM Images Scan

ec2:DescribeVpcs

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

VM Images Scan

ec2:DescribeInstanceTypeOfferings

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Host Auto-Defend

ec2:DescribeImages

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Host Auto-Defend

ec2:DescribeInstances

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Host Auto-Defend

ssm:SendCommand

PrismaCloud-Remediation-Compute-Policy-HostAutoDefend

Agent-Based Workload Scan

Host Auto-Defend

ssm:DescribeInstanceInformation

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Host Auto-Defend

ssm:ListCommandInvocations

PrismaCloud-Remediation-Compute-Policy-HostAutoDefend

Agent-Based Workload Scan

Host Auto-Defend

ssm:CancelCommand

PrismaCloud-Remediation-Compute-Policy-HostAutoDefend

Agent-Based Workload Scan

Host Auto-Defend

ssm:CreateAssociation

PrismaCloud-Remediation-Compute-Policy-HostAutoDefend

Agent-Based Workload Scan

Host Auto-Defend

ec2:DescribeRegions

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Host Auto-Defend

ec2:DescribeTags

arn:aws:iam::aws:policy/SecurityAudit

Agent-Based Workload Scan

Secrets Manager

Agent-Based Workload Scan

Alert Provider

securityhub:BatchImportFindings

PrismaCloud-ReadOnly-Policy-Compute

Serverless Function Scanning

Serverless Function Scanning

lambda:ListFunctions

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

lambda:GetFunction

PrismaCloud-ReadOnly-Policy-Compute

Serverless Function Scanning

iam:GetPolicy

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

iam:GetPolicyVersion

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

iam:GetRole

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

iam:GetRolePolicy

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

iam:ListAttachedRolePolicies

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

iam:ListRolePolicies

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

lambda:GetLayerVersion

PrismaCloud-ReadOnly-Policy-Compute

Serverless Function Scanning

kms:Decrypt

PrismaCloud-ReadOnly-Policy-Compute

Serverless Function Scanning

ec2:DescribeTags

arn:aws:iam::aws:policy/SecurityAudit

Serverless Function Scanning

### AWS Agentless Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/permissions\#aws-agentless-permissions)

The following table shows the required permissions, conditions, and resources for agentless scanning.

Go to the [AWS documentation for the official list of permissions needed to support EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#ebs-encryption-requirements).

Permission

Same Account

Hub Account

Target Account

Condition

Resource

Purpose

Mandatory

Removal Effect

ec2:CreateSnapshots

Yes

No

Yes

-

\*

Create snapshots of hosts to be scanned by the scanner instance

Yes

ec2:CreateSnapshot

Yes

No

Yes

-

\*

Create snapshot of hosts to be scanned by the scanner instance

Yes

ec2:DeleteSnapshot

Yes

No

Yes

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Delete snapshot of hosts that were created during the scan process

Yes

ec2:TerminateInstances

Yes

Yes

No

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Terminate scanner instance

Yes

ec2:DescribeVolumes

Yes

No

Yes

-

\*

Discovering volumes to scan

Yes

ec2:DescribeInstances

Yes

Yes

Yes

-

\*

Discovering instances to scan

Yes

ec2:DescribeSnapshots

Yes

No

Yes

-

\*

Acquire snapshot status to allow deploying the scanner only when all snapshots up and running

Yes

ec2:RunInstances

Yes

Yes

No

-

\*

Run the scanner instance

Yes

ec2:DescribeInstanceStatus

Yes

Yes

No

-

\*

Track scanner instance status

Yes

ec2:DescribeSubnets

Yes

Yes

No

-

\*

Validate subnet status - ensure subnet exists

Yes

ec2:DescribeSecurityGroups

Yes

Yes

No

-

\*

Validate security group status - ensure security group exists

Yes

ec2:CreateTags

Yes

Yes

No

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

"arn:aws:ec2:\*:\*:instance/\*"
"arn:aws:ec2:\*:\*:volume/\*"

Tag PCC resources created during the scan process

Yes

ec2:CreateTags

Yes

No

Yes

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

"arn:aws:ec2:\*::snapshot/\*"

Tag PCC resources created during the scan process

Yes

ec2:DescribeInstanceTypes

Yes

No

Yes

-

\*

Get available VM types on the region for grouping

Yes

sts:DecodeAuthorizationMessage

Yes

Yes

Yes

-

\*

Decode UnauthorizedOperation response from the AWS API

Yes

ssm:GetParameters

Yes

Yes

No

-

\*

Discover the scanner AMI

Yes

ec2:DescribeImages

Yes

No

Yes

-

\*

Disocver specifc AMIs metadata

Yes

sts:GetCallerIdentity

Yes

Yes

Yes

-

\*

Get metadata about the account (e.g., check for disabled regions, ec2 instances metadata)

Yes

iam:SimulatePrincipalPolicy

Yes

Yes

Yes

-

\*

Validate the effective permissions granted to the Prisma Cloud role

Yes

iam:CreateServiceLinkedRole

Yes

Yes

No

"arn:aws:iam::\*:role/aws-service-role/spot.amazonaws.com/\*"

"iam:AWSServiceName": "spot.amazonaws.com"

Create a linked service role for spot instance request

Yes

ec2:DescribeVPCs

Yes

Yes

No

-

\*

Discover the VPC to be used by the scanner instance

Yes

account:GetRegionOptStatus

Yes

Yes

Yes

-

\*

Discover regions statuses

Yes

ec2:DescribeNetworkInterfaces

Yes

Yes

No

-

\*

Discover the network interfaces to be used by the scanner instance

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:DeleteNetworkInterface

Yes

Yes

No

-

\*

Delete the network interface used by the scanner instance. Network interface is untaggable since it is created implicitly as part of instance creation. This permission only applies to detached network interfaces, so the scope effect is minimal

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:CreateTags

Yes

Yes

No

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

"arn:aws:ec2:\*:\*:vpc/\*"
"arn:aws:ec2:\*:\*:subnet/\*"
"arn:aws:ec2:\*:\*:internet-gateway/\*"

Tag PCC resources created during the scan process

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:CreateVpc

Yes

Yes

No

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

\*

Create scanner instance VPC

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:CreateInternetGateway

Yes

Yes

No

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

\*

Create scanner instance internet gateway

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:CreateSubnet

Yes

Yes

No

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

\*

Create scanner instance subnet

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:CreateSubnet

Yes

Yes

No

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Attach the scanner subnet to the VPC

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:DeleteSubnet

Yes

Yes

No

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Delete subnet attached to scanner

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:DetachInternetGateway

Yes

Yes

No

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Detach internet gateway from scanner subnet

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:DeleteVpc

Yes

Yes

No

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Delete the VPC used by the scanner instance

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:DeleteInternetGateway

Yes

Yes

No

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Delete the internet gateway used by the scanner instance

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:AttachInternetGateway

Yes

Yes

No

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Attach internet gateway to scanner subnet

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:CreateRoute

Yes

Yes

No

-

\*

Create route to the gateway to allow outbound traffic

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:DescribeRouteTables

Yes

Yes

No

-

\*

Retrieve the main route table associated by default to every subnet under the VPC

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

ec2:DescribeInternetGateways

Yes

Yes

No

-

\*

Discover the internet gateway to be used by the scanner instance

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

kms:Decrypt

Yes

Yes

Yes

-

\*

Required to support EBS encryption

No

Denies support for encrypted volumes

kms:GenerateDataKeyWithoutPlaintext

Yes

Yes

Yes

-

\*

Required to support EBS encryption

No

Denies support for encrypted volumes

kms:ReEncryptFrom

Yes

Yes

Yes

-

\*

Required to support EBS encryption

No

Denies support for encrypted volumes

kms:ReEncryptTo

Yes

Yes

Yes

-

\*

Required to support EBS encryption

No

Denies support for encrypted volumes

kms:DescribeKey

Yes

Yes

Yes

-

\*

Required to support EBS encryption

No

Denies support for encrypted volumes

kms:CreateGrant

Yes

No

Yes

-

\*

Required to support EBS encryption

No

Denies support for encrypted volumes

ec2:ModifySnapshotAttribute

No

No

Yes

"ec2:ResourceTag/created-by": "prismacloud-agentless-scan"

\*

Share snapshot with the hub account

Yes

Denies scanning snapshots in hub mode

kms:CreateKey

No

No

Yes

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

\*

Create a new shareable (with hub) PCC KMS key to re-encrypt the snapshots

No

Denies support for encrypted volumes in hub mode

kms:TagResource

No

No

Yes

"aws:RequestTag/created-by": "prismacloud-agentless-scan"

\*

Create the PCC KMS key with tags

No

Denies support for encrypted volumes in hub mode

ec2:CopySnapshot

No

No

Yes

-

\*

Create copies of encrypted snapshots, using the PCC KMS key

No

Denies support for encrypted volumes in hub mode

kms:ListKeys

No

No

Yes

-

\*

Discover and reuse existing PCC KMS key, also required for the cleanup process

No

Denies support for encrypted volumes in hub mode

## GCP[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/permissions\#gcp)

[Follow these instructions](https://docs.prismacloud.io/en/compute-edition/32/admin-guide/agentless-scanning/onboard-accounts/configure-gcp#gcp-encrypted-volumes) to scan encrypted volumes with the hub mode.

The following table shows the required permissions needed if you are using GCP. You can also review the [permissions needed for agentless scanning in GCP](https://docs.prismacloud.io/admin-guide/configure/permissions#gcp-agentless).

Capability

Feature

Permissions

Role/Policy

Workload Discovery

Cloud Discovery

Workload Discovery

Cloud Discovery

roles/storage.objectViewer

roles/viewer

Workload Discovery

Cloud Discovery

roles/container.clusterViewer

roles/viewer

Workload Discovery

Cloud Discovery

roles/cloudfunctions.viewer

roles/viewer

Workload Discovery

Cloud Discovery

compute.instances.list

Prisma Cloud Viewer

Workload Discovery

Cloud Discovery

compute.zones.list

Prisma Cloud Viewer

Workload Discovery

Cloud Discovery

compute.projects.get

Prisma Cloud Viewer

Workload Discovery

Cloud Discovery

compute.disks.get

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

Agent-Based Workload Scan

Host Auto Defend

osconfig.patchJobs.exec

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

osconfig.patchJobs.list

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

osconfig.patchJobs.get

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

storage.buckets.create

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

storage.buckets.delete

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

storage.objects.create

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

storage.objects.delete

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

storage.objects.get

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

storage.objects.list

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

compute.disks.get

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

compute.instances.list

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

compute.zones.list

Prisma Cloud Viewer

Agent-Based Workload Scan

Host Auto Defend

compute.projects.get

Prisma Cloud Viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.repositories.list

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.repositories.get

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.repositories.downloadArtifacts

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.files.list

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.files.get

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.packages.list

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.packages.listTagBindings

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.repositories.listEffectiveTags

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.packages.list

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.tags.list

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.tags.get

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.versions.list

roles/viewer

Agent-Based Workload Scan

Google Artifact Registry Scan

artifactregistry.versions.get

roles/viewer

Agent-Based Workload Scan

Google Container Registry Scan

Agent-Based Workload Scan

Google Container Registry Scan

storage.objects.get

Storage Object Viewer

Agent-Based Workload Scan

Google Container Registry Scan

storage.objects.list

Storage Object Viewer

Agent-Based Workload Scan

VM Images Scan

Agent-Based Workload Scan

VM Images Scan

compute.disks.create

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.images.get

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.images.list

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.images.useReadOnly

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.instances.create

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.instances.delete

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.instances.get

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.instances.list

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.instances.setMetadata

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.instances.setTags

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.networks.get

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.networks.updatePolicy

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.networks.use

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.networks.useExternalIp

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.subnetworks.use

Prisma Cloud Viewer

Agent-Based Workload Scan

VM Images Scan

compute.subnetworks.useExternalIp

Prisma Cloud Viewer

Serverless Function Scanning

Serverless Scanning

Serverless Function Scanning

Serverless Scanning

cloudfunctions.functions.sourceCodeGet

Serverless Function Scanning

Serverless Scanning

cloudfunctions.functions.get

roles/viewer

Serverless Function Scanning

Serverless Scanning

cloudfunctions.functions.list

roles/viewer

Serverless Function Scanning

Serverless Scanning

cloudfunctions.locations.get

roles/viewer

Serverless Function Scanning

Serverless Scanning

cloudfunctions.locations.list

roles/viewer

Serverless Function Scanning

Serverless Scanning

cloudfunctions.operations.get

roles/viewer

Serverless Function Scanning

Serverless Scanning

cloudfunctions.operations.list

roles/viewer

Serverless Function Scanning

Serverless Scanning

cloudfunctions.runtimes.list

roles/viewer

NOTE:

- The purpose for `Microsoft.Web/sites/config/list/Action` is to list Web App’s security sensitive settings, such as publishing credentials, app settings, and connection strings.

- The purpose for `Microsoft.ContainerInstance/containerGroups/containers/exec/action` is to allow execution within a specific container, which is essential for compute workload discovery. Get/list permissions only provide external cloud object information and do not access critical node-level details like container runtime or Kubernetes version. This permission is necessary to ensure accurate and comprehensive workload discovery.


### GCP Agentless Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/permissions\#gcp-agentless-permissions)

The following table shows the required permissions for agentless scanning.

Permission

Same Account

Hub Account

Target Account

Condition

Purpose

Mandatory

Removal Effect

compute.disks.create

Yes

Yes

No

Create disks from the snapshots to attach to the scanner instance

Yes

compute.instances.create

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Create the scanner instance

Yes

compute.instances.delete

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Delete the scanner instance

Yes

compute.instances.get

Yes

Yes

No

Retrieve information about scanner instance

Yes

compute.instances.setLabels

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Set the scanner instance labels

Yes

compute.instances.setMetadata

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Set the scanner instance metadata

Yes

compute.zones.list

Yes

Yes

Yes

Discover for zonal resources (e.g. iterating instances within zones)

Yes

compute.disks.get

Yes

No

Yes

Get disks attached to the scanner instance

Yes

compute.projects.get

Yes

No

Yes

Discover and get metadata of the project resource

Yes

compute.disks.createSnapshot

Yes

Yes

Yes

Create snapshots of instances to scan. If using hub mode, this permissions is required on every target that is not part of the same org as the hub account

Yes

compute.instances.list

Yes

Yes

Yes

Discover instances to scan

Yes

compute.snapshots.create

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Create snapshot of hosts to be scanned by the scanner instance

Yes

compute.snapshots.delete

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Delete snapshot of hosts that were created during the scan process

Yes

compute.snapshots.list

Yes

Yes

No

List snapshots within a project

Yes

compute.snapshots.setLabels

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Set labels on a snapshot so it can be associated with the scanner instance

Yes

compute.snapshots.useReadOnly

Yes

Yes

No

Create a disk from read-only snapshots when creating a scanner instance

Yes

compute.subnetworks.use

Yes

Yes

No

When deploying a scanner with custom network resources the permission to use subnets is required

Yes

compute.networks.use

Yes

Yes

No

Attach network to the scanner instance

Yes

compute.networks.get

Yes

Yes

No

Retrieve information about the scanner instance network

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.regionOperations.get

Yes

Yes

No

Required for regional APIs (e.g. bulk insert) and for creating regional resources (e.g. subnet)

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.subnetworks.get

Yes

Yes

No

Retrieve the scanner instance subnet

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.networks.useExternalIp

Yes

Yes

No

The scanner instance uses an exetrnal IP by default. Safe to remove if using custom network resources

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.subnetworks.useExternalIp

Yes

Yes

No

The scanner instance uses an exetrnal IP by default. Safe to remove if using custom network resources

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.networks.create

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Create scanner instance network

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.networks.delete

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Delete scanner instance network

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.networks.updatePolicy

Yes

Yes

No

Modify the scanner instance network policy

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.subnetworks.create

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Create scanner instance subnet

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.subnetworks.delete

Yes

Yes

No

"expression": "(resource.name.endsWith(\\"-prisma-agentless-scan\\") && resource.service == \\"compute.googleapis.com\\") \|\| resource.type == \\"cloudresourcemanager.googleapis.com/Project\\"", "description": "Grant scoped permissions only if the resource name ends with -prisma-agentless-scan and service is compute",

Delete scanner instance subnet

No

Denies automated creation of network infrastructure - safe to remove if configuring custom network resources

compute.subnetworks.use

No

-

-

Required only when using a shared VPC - to be applied on the shared VPC host project

No

Denies ability to use a shared VPC

compute.subnetworks.useExternalIp

No

-

-

Required only when using a shared VPC - to be applied on the shared VPC host project

No

Denies ability to use a shared VPC

## Azure[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/permissions\#azure)

The following table shows the required permissions needed if you are using Azure. You can also review the [permissions needed for agentless scanning in Azure](https://docs.prismacloud.io/admin-guide/configure/permissions#azure-agentless).

Capability

Feature

Permissions

Role/Policy

Workload Discovery

Workload Discovery

Microsoft.ContainerRegistry/registries/read

Reader

Workload Discovery

Microsoft.ContainerRegistry/registries/pull/read

Workload Discovery

Microsoft.ContainerRegistry/registries/metadata/read

Reader

Workload Discovery

Microsoft.ContainerService/managedClusters/read

Reader

Workload Discovery

Microsoft.Web/sites/Read

Reader

Workload Discovery

Microsoft.ContainerInstance/containerGroups/read

Reader

Workload Discovery

Microsoft.ContainerInstance/containerGroups/containers/exec/action

Prisma Cloud custom role

Workload Discovery

Microsoft.Compute/virtualMachines/read

Reader

Workload Discovery

Microsoft.Compute/hostGroups/read

Serverless Function Scanning

Serverless Function Scanning

Microsoft.Web/sites/Read

Reader

Serverless Function Scanning

Microsoft.Web/sites/config/list/Action

Prisma Cloud custom role

Serverless Function Scanning

Microsoft.web/sites/functions/action

Prisma Cloud custom role

Serverless Function Scanning

Microsoft.web/sites/functions/read

Reader

Serverless Function Scanning

Microsoft.Web/sites/publishxml/Action

Prisma Cloud custom role

Agent-Based Workload Scan

Host Auto Defend

Agent-Based Workload Scan

Host Auto Defend

Microsoft.Compute/virtualMachines/runCommand/action

Prisma Cloud custom role

Agent-Based Workload Scan

Host Auto Defend

Microsoft.Compute/locations/operations/read

Reader

Agent-Based Workload Scan

Host Auto Defend

Microsoft.Resources/subscriptions/locations/read

Reader

Agent-Based Workload Scan

VM Images Scan

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/locations/publishers/artifacttypes/offers/skus/versions/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/images/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/galleries/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/galleries/images/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/galleries/images/versions/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Resources/subscriptions/resourceGroups/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Resources/subscriptions/resourceGroups/write

Prisma Cloud custom role

Agent-Based Workload Scan

VM Images Scan

Microsoft.Resources/subscriptions/resourceGroups/delete

Prisma Cloud custom role

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkSecurityGroups/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkSecurityGroups/write

Network Contributor

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkSecurityGroups/join/action

Network Contributor

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkSecurityGroups/delete

Network Contributor

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkInterfaces/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkInterfaces/write

Network Contributor

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkInterfaces/join/action

Network Contributor

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/networkInterfaces/delete

Network Contributor

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/disks/write

Prisma Cloud custom role

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/disks/delete

Prisma Cloud custom role

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/virtualNetworks/subnets/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Network/virtualNetworks/subnets/join/action

Network Contributor

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/virtualMachines/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/virtualMachines/write

Prisma Cloud custom role

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/virtualMachines/start/action

Prisma Cloud custom role

Agent-Based Workload Scan

VM Images Scan

Microsoft.Compute/virtualMachines/delete

Prisma Cloud custom role

Agent-Based Workload Scan

VM Images Scan

Microsoft.KeyVault/vaults/keys/read

Reader

Agent-Based Workload Scan

VM Images Scan

Microsoft.KeyVault/vaults/keys/wrap/action

Key Vault Crypto Service Encryption User

Agent-Based Workload Scan

VM Images Scan

Microsoft.KeyVault/vaults/keys/unwrap/action

Key Vault Crypto Service Encryption User

### Azure Agentless Permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/permissions\#azure-agentless-permissions)

The following table shows the required permissions for agentless scanning.

Permission

Same Account

Hub Account

Target Account

Purpose

Mandatory

Removal Effect

Microsoft.Authorization/locks/read

Yes

Yes

Yes

Ensure no Azure scope locks preventing resources cleanup

Yes

Microsoft.Compute/disks/beginGetAccess/action

Yes

Yes

Yes

Create disks from the snapshots to attach to the scanner instance

Yes

Microsoft.Compute/disks/read

Yes

No

Yes

Attach disks to the scanner instance

Yes

Microsoft.Compute/disks/delete

Yes

Yes

No

Delete disk in case failed to attach to scanner

Yes

Microsoft.Compute/disks/write

Yes

Yes

No

Create disks from the snapshots to attach to the scanner instance

Yes

Microsoft.Compute/snapshots/read

Yes

Yes

No

Read all snapshots created by the scan process

Yes

Microsoft.Compute/snapshots/write

Yes

Yes

No

Create snapshots of hosts to be scanned by the scanner instance

Yes

Microsoft.Compute/snapshots/delete

Yes

Yes

No

Delete snapshots of hosts that were created during the scan process

Yes

Microsoft.Compute/virtualMachines/read

Yes

Yes

Yes

Discover instances to scan

Yes

Microsoft.Compute/virtualMachines/write

Yes

Yes

No

Create the scanner instance

Yes

Microsoft.Compute/virtualMachines/delete

Yes

Yes

No

Delete the scanner instance

Yes

Microsoft.Compute/virtualMachines/instanceView/read

Yes

No

Yes

Check if the scanner instance is running, and check for running/non-running hosts

Yes

Microsoft.Compute/virtualMachineScaleSets/read

Yes

No

Yes

Discover scale sets (e.g, for AKS support)

Yes

Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read

Yes

No

Yes

Discover hosts within scale sets (e.g, for AKS support)

Yes

Microsoft.Compute/virtualMachineScaleSets/virtualMachines/instanceView/read

Yes

No

Yes

Check for running/non-running hosts in a scale set (e.g, for AKS support)

Yes

Microsoft.ContainerService/managedClusters/read

Yes

No

Yes

Discover AKS clusters names

Yes

Microsoft.Network/natGateways/read

Yes

Yes

No

Read NAT gateways

Microsoft.Network/natGateways/write

Yes

Yes

No

Write NAT gateways

Microsoft.Network/natGateways/delete

Yes

Yes

No

Delete NAT gateways

Microsoft.Network/networkInterfaces/read

Yes

Yes

No

Discover the scanner instance network interface

Yes

Microsoft.Network/networkInterfaces/write

Yes

Yes

No

Create the scanner instance network interface

Yes

Microsoft.Network/networkInterfaces/delete

Yes

Yes

No

Delete the scanner instance network interface

Yes

Microsoft.Network/networkInterfaces/join/action

Yes

Yes

No

Attach the network interface to the scanner instance

Yes

Microsoft.Network/networkSecurityGroups/read

Yes

Yes

No

Discover the scanner instance security group

Yes

Microsoft.Network/networkSecurityGroups/write

Yes

Yes

No

Create the scanner instance security group

Yes

Microsoft.Network/networkSecurityGroups/delete

Yes

Yes

No

Delete the scanner instance security group

Yes

Microsoft.Network/networkSecurityGroups/join/action

Yes

Yes

No

Attach the security group to the subnet of the scanner instance

Yes

Microsoft.Network/publicIPAddresses/read

Yes

Yes

No

Gets a public IP address definition.

Microsoft.Network/publicIPAddresses/write

Yes

Yes

No

Creates a public IP address or updates an existing public IP address.

Microsoft.Network/publicIPAddresses/delete

Yes

Yes

No

Deletes a public IP address.

Microsoft.Network/virtualNetworks/read

Yes

Yes

No

Discover the scanner instance network

Yes

Microsoft.Network/virtualNetworks/write

Yes

Yes

No

Create the scanner instance network

Yes

Microsoft.Network/virtualNetworks/delete

Yes

Yes

No

Delete the scanner instance network

Yes

Microsoft.Network/virtualNetworks/subnets/read

Yes

Yes

No

Discover the scanner instance subnet

Yes

Microsoft.Network/virtualNetworks/subnets/join/action

Yes

Yes

No

Attach the subnet to the scanner instance

Yes

Microsoft.Resources/subscriptions/resourceGroups/read

Yes

Yes

Yes

Retrieve the agentless scan resource group

Yes

Microsoft.Resources/subscriptions/resourceGroups/write

Yes

Yes

Yes

Create the agentless scan resource group to isolate the scan process

No

Optionally create a resource group named "PCCAgentlessScanResourceGroup" before enabling the scan, after which you can safely remove this permission.

[PreviousClustered-DB](https://docs.prismacloud.io/admin-guide/configure/clustered-db) [NextAuthentication](https://docs.prismacloud.io/admin-guide/authentication/authentication)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
