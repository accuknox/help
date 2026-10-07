For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host.md).

Host auto-defend lets you automatically deploy Host Defenders on virtual machines/instances in your AWS, Azure and Google Cloud accounts. This covers AWS EC2 instances, Azure Virtual Machines, and GCP Compute Engine instances.

## Deployment process[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#deployment-process)

After setting up auto-defend for hosts, Prisma Cloud discovers and protects unsecured hosts as follows:

1. Discover - Prisma Cloud uses cloud provider APIs to get a list of all VM instances.

2. Identify - Prisma Cloud identifies unprotected instances.

3. Verify - Ensure unprotected resources meet auto-defend prerequisites.

4. Install - Prisma Cloud installs Host Defender on unprotected instances using cloud provider APIs.


Regardless of the underlying container runtime, the host deployment process skips your worker nodes.

## AWS EC2 instances[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#aws-ec2-instances)

Prisma Cloud uses AWS Systems Manager (formerly known as SSM) to deploy Defenders to EC2 instances.

### Minimum requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#minimum-requirements)

The following sections describe the minimum requires to auto-defend to hosts in AWS.

#### AWS Systems Manager[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#aws-systems-manager)

Prisma Cloud uses AWS Systems Manager (formerly known as SSM) to deploy Defenders to instances. This means that:

- The SSM Agent must be installed on every instance.

- AWS Systems Manager must have permission to perform actions on each instance.


To view all SSM managed instances, go to the AWS console [here](https://console.aws.amazon.com/systems-manager/managed-instances).

**SSM Agent**

Prisma Cloud uses the [SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/prereqs-ssm-agent.html) to deploy Host Defender on an instance. The SSM Agent must be installed prior to deploying the Host Defenders. The SSM Agent is installed by default on the following distros.

- Amazon Linux

- Amazon Linux 2

- Amazon Linux 2 ECS-Optimized AMIs

- Ubuntu Server 16.04, 18.04, and 20.04


The SSM Agent doesn’t come installed out of the box but supported on the following distributions. Ensure its installed [ahead of time](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-manual-agent-install.html) before proceeding. :

- CentOS

- Debian Server

- Oracle Linux

- Red Hat Enterprise Linux

- SUSE Linux Enterprise Server


**IAM instance profile for Systems Manager**

By default, AWS Systems Manager doesn’t have permission to perform actions on your instances. You must grant it access with an IAM instance profile.

If you’ve used System Manager’s Quick Setup feature, assign the **AmazonSSMRoleForInstancesQuickSetup** role to your instances.

#### Required permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#required-permissions)

Prisma Cloud needs a service account with the following permissions to automatically protect EC2 instances in your AWS account. Add the following policy to an IAM user or role:

AskCopy

```
{
    "Version": "2012-10-17",
    "Statement": [\
        {\
            "Sid": "VisualEditor0",\
            "Effect": "Allow",\
            "Action": [\
                "ec2:DescribeImages",\
                "ec2:DescribeInstances",\
                "ssm:SendCommand",\
                "ssm:DescribeInstanceInformation",\
                "ssm:ListCommandInvocations",\
                "ssm:CancelCommand",\
                "ec2:DescribeRegions",  //You can ignore if you already have these permissions as apart of the discovery feature\
                "ec2:DescribeTags",//You can ignore if you already have these permissions as apart of the discovery feature\
                "ssm:SendCommand"\
            ],\
            "Resource": "*"\
        }\
    ]
}
```

## Azure virtual machines[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#azure-virtual-machines)

Prisma Cloud uses the Azure VM agent [Run Command](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/run-command) option to invoke the script to deploy Host defenders. You are required to configure the permissions below in your subscription and create host deploy rules to begin installing Defenders.

### Minimum requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#minimum-requirements-1)

The following sections describe the minimum requires to auto-defend to hosts on Azure.

#### Azure Linux VM agent & Run command[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#azure-linux-vm-agent-and-run-command)

Prisma Cloud uses the `run command` action on the Azure Linux VM agent to deploy Defenders on instances.

The VM Agent must be on every instance. By default, the VM agent is available on most Linux OS machines. Refer to the documentation for more information.

Currently cancelling running operation is not supported. Dangling command will automatically timeout after 90 minutes. Also, run command is only supported on Linux VMs.

#### Required permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#required-permissions-1)

In addition to the [Reader](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#reader) role to get the list and details of the virtual machines, the Azure credential user needs permissions to invoke the runcommand.

AskCopy

```
Microsoft.Compute/virtualMachines/runCommand/action
```

Typically, the Virtual Machine [Contributor](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#virtual-machine-contributor) role and higher levels have this permission. You can either directly use the role or create a custom role with the above permission.

## GCP Compute Engine instances[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#gcp-compute-engine-instances)

The installation uses [OS Patch Management](https://cloud.google.com/compute/docs/os-patch-management) service. Prisma Cloud creates an OS patch job with the information of the installation script stored in the temporarily created storage bucket and the list of instances to deploy the Host defender on the instances.

### Minimum requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#minimum-requirements-2)

The following sections describe the minimum requires to auto-defend hosts on GCP.

#### Storage Buckets[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#storage-buckets)

Prisma cloud auto creates a temporary storage bucket in the region you selected for the auto-defend rule. The bucket is named 'prisma-defender-bucket-<hash>' where <hash> is a randomly generated string, e.g., 'prisma-defender-bucket-346a7e425d344c8a7dd9ce75da674970'. The Prisma defender installation script 'prisma-defender-script.sh' is stored in the bucket.

The service account user needs permissions to be able to create and delete the bucket.

#### OS Patch Management[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#os-patch-management)

[VM Manager](https://cloud.google.com/compute/docs/vm-manager) is a suite of tools that can be used to manage operating systems for large virtual machine (VM) fleets running Windows and Linux on Compute Engine. Prisma cloud uses [OS Patch Management service](https://cloud.google.com/compute/docs/os-patch-management) which is a part of a broader VM Manager service to deploy the host defenders.

- Setup VM Manager for OS patch management. Users can do auto enablement of VM Manager from the Google cloud console as shown [here](https://cloud.google.com/compute/docs/manage-os#automatic)

- VM is supported on most of the active OS versions for Linux. For more information, refer to [Operating system](https://cloud.google.com/compute/docs/images/os-details#vm-manager) for details.

- In Google Cloud project, [OS Config API](https://cloud.google.com/compute/docs/manage-os#enable-service-api) should be enabled. This needs to be done via the google cloud console.


#### Required permissions[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#required-permissions-2)

Prisma Cloud needs a service account with the following permissions to automatically protect GCP compute instances in your Google project. Add the following permissions:

AskCopy

```
Compute.instances.list
Compute.zones.list
Compute.projects.get
osconfig.patchJobs.exec
osconfig.patchJobs.get
osconfig.patchJobs.list
storage.buckets.create
storage.buckets.delete
storage.objects.create
storage.objects.delete
storage.objects.get
storage.objects.list
compute.disks.get
```

## Instance types[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#instance-types)

Auto-defend is supported only on Linux hosts. All hosts must meet the system requirements and have either `wget` or `curl` installed.

Auto-defend is supported only for stand-alone hosts, and not for hosts that are part of any GCP-managed instance group or clusters.

For hosts that are part of clusters, use one of the cluster-native install options (e.g., DaemonSets on Kubernetes).

When configuring the scope of hosts that should be auto-defended, ensure that the scope doesn’t include any hosts that are part of a cluster or that run containers. Auto-defend doesn’t currently check if a host is part of cluster. If you mistakenly include nodes that are part of a cluster in an auto-defend rule, and the cluster is not already protected, the auto-defend rule will deploy Host Defenders to the cluster nodes.

## Add a host auto-defend rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host\#add-a-host-auto-defend-rule)

Host auto-defend rules let you specify which hosts you want to protect. You can define a specific account by referencing the relevant credential or collection. Each auto-defend rule is evaluated separately.

1. Open Compute Console, and go to **Manage > Defenders > Deploy > Host auto-defend**.

2. Click on **Add rule**.

3. In the dialog, enter the following settings:









1. Enter a rule name.

2. In **Provider** \- AWS, Azure and GCP are currently supported.

3. In **Console**, specify a DNS name or IP address that the installed Defender can use to connect back to Console after it’s installed.

4. (Optional) In **Scope**, target the rule to specific hosts.











      Create a new collection. Supported attributes are hosts, images, labels, account IDs.











      The following example shows a collection that is based on hosts labels, in this case a label of host\_demo with the value centos.















      ![auto defend collection example](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-7c622dc7a60c5538299c6c4af65881fa098449c0%252Fauto_defend_collection_example.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=89f7a1b0f2537cede629a64f2c656be4&sv=3)

5. Set up these options for specific Cloud Service Providers.









      - (For AWS only) Specify the Scanning scope for the AWS region- Commercial or regular, Government, or China.

      - (For GCP only) Specify the Bucket region. Prisma cloud auto creates a temporary storage bucket named 'prisma-bucket' in the region and deletes it after the process of creating the rule is completed.


6. Select or [create credentials](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/authentication/credentials-store/credentials-store.md) so Prisma Cloud can access your account. The service account must have the [minimum permissions](https://docs.prismacloud.io/admin-guide/configure/permissions).

7. Click **Add**.











      The new rule appears in the table of rules.


4. Click **Apply Defense**.











Select the rule to start the scan. By default, host auto-protect rules are evaluated every 24 hours. Click the **Apply Defense** button to force a new scan.











The following screenshot shows that the `auto-defend-testgroup` discovered two EC2 instances and deployed two Defenders (2/2).















![auto defend host rule](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-711d111ca6e5584257c2e85ed6a9ddcf55dd7041%252Fauto_defend_host_rule.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=8a0d09e6eadf9ef7186a8ec44d5ddf82&sv=3)


[PreviousDeploy Host Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host) [NextWindows Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/windows-host)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
