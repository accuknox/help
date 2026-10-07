For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs.md).

Complete the steps on this page to deploy the Prisma Cloud console in an ECS cluster. This example deployment consists of a single infrastructure node and two worker nodes. The console runs on the infrastructure node. An instance of the Prisma Cloud Defender runs on every node in the cluster.

The Prisma Cloud console runs as a service in your ECS cluster to provide you a management interface. You can describe the parameters of the service in a task definition written in JSON format.

To protect the workloads in in your containerized environment, you set policies in the Prisma Cloud console. The Defender service enforces the policies you set running a service in your ECS cluster. You can [automatically deploy an instance of the Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs) on each node in your cluster.

This example provisions a highly available Prisma Cloud console. If the infrastructure node goes down, ECS reschedules the Prisma Cloud console service on any healthy node. You must attach storage that’s accessible from each of your infrastructure nodes to ensure high availability. The recommended option is the Amazon Elastic File System (EFS) to ensure that the Prisma Cloud console continues to have access to its state since your data persists across nodes.

When you have multiple infrastructure nodes, ECS can schedule Console on any of them. Defenders need a reliable way to connect to Console. A load balancer automatically directs traffic to the node where Console runs, and offers a stable interface that Defenders can use to connect to Console and that operators can use to access its web interface.

We assume you are deploying Prisma Cloud to the default VPC. If you are not using the default VPC, adjust your settings accordingly.

This guide assumes you know very little about AWS ECS. As such, it is extremely prescriptive, and includes step for building your cluster. If you are already familiar with AWS ECS and do not need assistance navigating the interface, simply read the section synopsis, which summarizes all key configurations. To better understand clusters, read our [cluster context](https://docs.prismacloud.io/admin-guide/install/cluster-context) topic.

## Get Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#get-prisma-cloud)

The Prisma Cloud release tarball contains all the release artifacts.

1. [Download](https://docs.prismacloud.io/admin-guide/welcome/releases#download) the latest recommended release.

2. Retrieve the release tarball.

















AskCopy



```
$ wget <LINK_TO_CURRENT_RECOMMENDED_RELEASE_LINK>
```

3. Unpack the Prisma Cloud release tarball.

















AskCopy



```
$ mkdir twistlock
$ tar xvzf prisma_cloud_compute_edition_<VERSION>.tar.gz  -C twistlock/
```


## Create a cluster[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#create-a-cluster)

Create an empty cluster named _pc-ecs-cluster_. Later, you will create launch configurations and auto-scaling groups to start EC2 instances in the cluster.

1. Log into the AWS Management Console.

2. Go to **Services > Containers > Elastic Container Service**.

3. Click **Create Cluster**.

4. Select **Networking only**, then click **Next Step**.

5. Enter a cluster name, such as **pc-ecs-cluster**.

6. Click **Create**.


## Create a security group[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#create-a-security-group)

Create a new security group named _pc-security-group_ that opens the following ports. This security group will be associated with resources in your cluster.

Port

Description

8083

Prisma Cloud Console’s UI and API.

8084

Prisma Cloud secure websocket for Console-Defender communication.

2049

NFS for Prisma Cloud Console to access its state.

22

SSH for managing nodes.

You can harden this configuration as required. For example, you might want to limit access to port 22 to specific source IPs.

01. Go to **Services > Compute > EC2**.

02. In the left menu, click **NETWORK & SECURITY > Security Groups**.

03. Click **Create Security Group**.

04. In **Security group name**, enter a name, such as **pc-security-group**.

05. In **Description**, enter **Prisma Cloud ports**.

06. In **VPC**, select your default VPC.

07. Under the **Inbound rules** section, click **Add Rule**.









    1. Under **Type**, select **Custom TCP**.

    2. Under **Port Range**, enter **8083-8084**.

    3. Under **Source**, select **Anywhere**.


08. Click **Add Rule**.









    1. Under **Type**, select **NFS**.

    2. Under **Source**, select **Anywhere**.


09. Click **Add Rule**.









    1. Under **Type**, select **SSH**.

    2. Under **Source**, select **Anywhere**.


10. Click **Create security group**.


## Create an EFS file system for Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#create-an-efs-file-system-for-console)

Create the Console EFS file system, and then get the command that will be used to mount the file system on every infrastructure node.

The EFS file system and ECS cluster must be in the same VPC and security group.

**Prerequisites:** Prisma Cloud Console depends on an EFS file system with the following performance characteristics:

- **Performance mode:** General purpose.

- **Throughput mode:** Provisioned. Provision 0.1 MiB/s per deployed Defender. For example, if you plan to deploy 10 Defenders, provision 1 MiB/s of throughput.


01. Log into the AWS Management Console.

02. Go to **Services > Storage > EFS**.

03. Click **Create File System**.

04. Enter a value for **Name**, such as **pc-efs-console**

05. Select a VPC.

06. Click **Customize**.

07. Set throughput mode to **Provisioned**, and set **Throughput** to 0.1 MiB/s per Defender to be deployed.











    For example, if you plan to deploy ten Defenders, set throughput to 1 MiB/s (10 Defenders \* 0.1 MiB/s = 1 MiB/s).

08. Click **Next**.

09. For each mount target, select the **pc-security-group**.

10. Click **Next**.

11. In **File System Policy**, click **Next**.

12. Review your settings and click **Create**.

13. Click **View file system**.

14. Click **Attach**, copy the NFS client mount command, and set it aside for later.











    You will use the mount command when setting up Console’s launch configuration.


## Set up a load balancer[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#set-up-a-load-balancer)

Set up an AWS Classic Load Balancer, and capture the Load Balancer DNS name.

You’ll create two load balancer listeners. One is used for Console’s UI and API, which are served on port 8083. Another is used for the websocket connection between Defender and Console, which is established on port 8084.

For detailed instructions on how to create a load balancer for Console, see [Configure an AWS Load Balancer for ECS](https://docs.prismacloud.io/admin-guide/how-to-guides/configure-ecs-loadbalancer).

## Use a private registry[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#use-a-private-registry)

For maximum control over your environment, you might want to store the Console container image in your own private registry, and then install Prisma Cloud from your private registry. When the Console service is started, ECS retrieves the image from your registry. This procedure shows you how to push the Console container image to Amazon’s Elastic Container Registry (ECR).

**Prerequisites:**

- AWS CLI is installed on your machine. It is required to push the Console image to your registry.


1. Go to the directory where you unpacked the Prisma Cloud release tarball.

















AskCopy



```
$ cd prisma_cloud_compute_edition/
```

2. Load the Console image.

















AskCopy



```
$ docker load < ./twistlock_console.tar.gz
```

3. Go to **Services > Containers > Elastic Container Service**.

4. In the left menu, click **Repositories**.

5. Click **Create repository**.

6. Follow the AWS instructions for logging in to the registry, tagging the Console image, and pushing it to your repo.











Be sure to update your Console task definition so that the value for `image` points to your private registry.


## Deploy Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#deploy-console)

Launch an infrastructure node that runs in the cluster, then start Prisma Cloud Console as a service on that node.

### Create a launch configuration for the infrastructure node[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#create-a-launch-configuration-for-the-infrastructure-node)

Launch configurations are templates that are used by an auto-scaling group to start EC2 instances in your cluster.

Create a launch configuration named _pc-infra-node_ that:

- Creates an instance type of t2.xlarge, or higher. For more information about Console’s minimum requirements, see the [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

- Runs Amazon ECS-Optimized Amazon Linux 2 AMI.

- Uses the ecsInstanceRole IAM role.

- Runs a user data script that joins the _pc-ecs-cluster_ and defines a custom attribute named _purpose_ with a value of _infra_. Console tasks will be placed to this instance.


01. Go to **Services > Compute > EC2**.

02. In the left menu, click **Auto Scaling > Launch Configurations**.

03. Click **Create launch configuration**.

04. In **Name**, enter a name for your launch configuration, such as **pc-infra-node**.

05. In Amazon machine image, select **Amazon ECS-Optimized Amazon Linux 2 AMI**.











    You can get a complete list of per-region Amazon ECS-optimized AMIs from [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html).

06. Under instance type, select **t2.xlarge**.

07. Under **Additional Configuration**:









    1. In **IAM instance profile**, select **ecsInstanceRole**.











       If this role doesn’t exist, create it. For complete details, see [Amazon ECS Container Instance IAM Role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/instance_IAM_role.html).

    2. Under **User data**, select **Text**, and paste the following code snippet, which installs the NFS utilities and mounts the EFS file system:

















       AskCopy



       ```
       #!/bin/bash
       cat <<'EOF' >> /etc/ecs/ecs.config
       ECS_CLUSTER=pc-ecs-cluster
       ECS_INSTANCE_ATTRIBUTES={"purpose": "infra"}
       EOF

       yum install -y nfs-utils
       mkdir /twistlock_console
       <CONSOLE_MOUNT_COMMAND> /twistlock_console

       mkdir -p /twistlock_console/var/lib/twistlock
       mkdir -p /twistlock_console/var/lib/twistlock-backup
       mkdir -p /twistlock_console/var/lib/twistlock-config
       ```









       **ECS\_CLUSTER** must match your cluster name. If you’ve named your cluster something other than **pc-ecs-cluster**, then update the user data script accordingly.











       **<CONSOLE\_MOUNT\_COMMAND>** is the Console mount command you copied from the AWS Management Console after creating your console EFS file system. The mount target must be _/twistlock\_console_, not the _efs_ mount target provided in the sample command.

    3. (Optional) In **IP Address Type**, select **Assign a public IP address to every instance**.











       With this option, you can easily SSH to this instance to troubleshoot issues.


08. Under **Security groups**:









    1. Select **Select an existing security group**.

    2. Select **pc-security-group**.


09. Under **Key pair (login)**, select an existing key pair, or create a new key pair so that you can access your instances.

10. Click **Create launch configuration**.


## Create an auto scaling group for the infrastructure node[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#create-an-auto-scaling-group-for-the-infrastructure-node)

Launch a single instance of the infrastructure node into your cluster.

1. Go to **Services > Compute > EC2**.

2. In the left menu, click **Auto Scaling > Auto Scaling Groups**.

3. Click **Create an Auto Scaling group**.

4. In **Choose launch template or configuration**:









1. In **Auto Scaling group Name**, enter **pc-infra-autoscaling**.

2. In **Launch template**, click **Switch to launch configuration**.

3. Select **pc-infra-node**.

4. Click **Next**.


5. Under **Configure settings**:









1. In **VPC**, select your default VPC.

2. In **Subnet**, select a public subnet, such as 172.31.0.0/20.

3. Click **Skip to review**.


6. Review the configuration and click **Create Auto Scaling Group**.











After the auto scaling group spins up (it will take some time), validate that your cluster has one container instance, where a container instance is the ECS vernacular for an EC2 instance that has joined the cluster and is ready to accept container workloads:









   - Go to **Services > Containers > Elastic Container Service**. The count for **Container instances** should be 1.

   - Click on the cluster, then click on the **ECS Instances** tab. In the status table, there should be a single entry. Click on the link under the **EC2 Instance** column. In the details page for the EC2 instance, record the **Public DNS**.


## Copy the Prisma Cloud config file into place[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#copy-the-prisma-cloud-config-file-into-place)

The Prisma Cloud API serves the version of the configuration file used to instantiate Console. Use scp to copy _twistlock.cfg_ from the Prisma Cloud release tarball to _/twistlock\_console/var/lib/twistlock-config_ on the infrastructure node.

1. Upload _twistlock.cfg_ to the infrastructure node.









1. Go to the directory where you unpacked the Prisma Cloud release tarball.

2. Copy _twistlock.cfg_ to the infrastructure node.

















      AskCopy



      ```
      $ scp -i <PATH-TO-KEY-FILE> twistlock.cfg ec2-user@<ECS_INFRA_NODE_DNS_NAME>:~
      ```


2. SSH to the infrastructure node.

















AskCopy



```
$ ssh -i <PATH-TO-KEY-FILE> ec2-user@<ECS_INFRA_NODE_DNS_NAME>
```

3. Copy the _twistlock.cfg_ file into place.

















AskCopy



```
$ sudo cp twistlock.cfg /twistlock_console/var/lib/twistlock-config
```

4. Close your SSH session.

















AskCopy



```
$ exit
```


## Create a Prisma Cloud Console task definition[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#create-a-prisma-cloud-console-task-definition)

Prisma Cloud provides a task definition template for Console. Download the template, then update the variables specific to your environment. Finally, load the task definition in ECS.

**Prerequisites:**

- The task definition provisions sufficient resources for Console to operate. The template specifies reasonable defaults. For more information, see the [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).


01. Download the [Prisma Cloud Compute Console task definition](https://cdn.twistlock.com/docs/attachments/amazon-ecs-task-pc-console.json), and open it for editing.

02. Update the value for `image`.











    Replace the following placeholder strings with the appropriate values:









    - `<ACCESS-TOKEN>` — Your Prisma Cloud access token. All characters must be lowercase.

    - `<VERSION>` — Version of the Console image to use. For example, for version `20.04.177`, specify `20_04_177`. The image and tag will look like `console:console_20_04_177`.


03. Update the value for\`IP:<ECS\_INFRA\_NODE\_IPADDR>\` if you are using the IP address or replace it with `DNS:<ECS_INFRA_NODE_DNS>` to use the Load Balancer’s DNS name.

04. Go to **Services > Containers > Elastic Container Service**.

05. In the left menu, click **Task Definitions**.

06. Click **Create new Task Definition**.

07. Select **EC2**, and then click **Next step**.

08. In **Step 2: Configure task and container definitions**, scroll to the bottom of the page and click **Configure via JSON**.

09. Delete the default task definition, and replace it with the Prisma Cloud Compute Console task definition.

10. Click **Save**.

11. (Optional) Change the name of the task definition. By default, its name is **pc-console**.

12. Click **Create**.


## Start the Prisma Cloud Console service[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#start-the-prisma-cloud-console-service)

Create the Console service using the previously defined task definition. A single instance of Console will run on the infrastructure node.

01. Go to **Services > Containers > Elastic Container Service**.

02. In the left menu, click **Clusters**.

03. Click on your cluster.

04. In the **Services** tab, then click **Create**.

05. In **Step 1: Configure service**:









    1. For **Launch type**, select **EC2**.

    2. For **Task Definition**, select **pc-console**.

    3. In **Service Name**, enter **pc-console**.

    4. In **Number of tasks**, enter **1**.

    5. Click **Next Step**.


06. In **Step 2: Configure network**:









    1. For **Load Balancer type**, select **Classic Load Balancer**.

    2. For **Service IAM role**, leave the default **ecsServiceRole**.

    3. For **Load Balancer Name**, select previously created load balancer.

    4. Unselect **Enable Service discovery integration**

    5. click **Next Step**.


07. In **Step 3: Set Auto Scaling**, accept the defaults, and click **Next**.

08. In **Step 4: Review**, click **Create Service**.

09. Wait for the service to launch, and then click **View Service**.

10. Wait for **Last status** to change to **RUNNING** (it can take a few minutes), and then proceed to the next step.


## Configure Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs\#configure-prisma-cloud-console)

Navigate to Console’s web interface, create your first admin account, and enter your license.

1. Start a browser, then navigate to https://<LB\_DNS\_NAME>:8083

2. At the login page, create your first admin account. Enter a username and password.

3. Enter your license key, then click **Register**.











You have successfully deployed the Prisma Cloud console on your ECS cluster. Next, deploy the Defender to protect your workloads.


[PreviousDeploy the Prisma Cloud Console on Kubernetes](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-kubernetes) [NextConsole on Fargate](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
