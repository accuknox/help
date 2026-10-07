For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs.md).

This guide shows you how to deploy Prisma Cloud Defenders in an ECS cluster.

The Defender protects your containerized environment according to the policies you set in Prisma Cloud Console. It runs as a service in your ECS cluster. The parameters of the service are described in a task definition, and the task definition is written in JSON format. To automatically deploy an instance of Defender on each node in your cluster, you’ll run the Defender task as a _daemon_ service.

The Defender deployment process consists of the following steps.

1. Create worker nodes in your ECS cluster.

2. Create a task definition for the Prisma Cloud Defender.

3. Create a service of type `Daemon` to deploy Defender to every node in the cluster.


This deployment guide includes the following steps you need to take in AWS before you deploy the Defender if you haven’t provisioned a cluster.

1. [Create your ECS cluster](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs#create-ecs-cluster).

2. [Create a launch configuration for worker nodes](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs#create-launch-configuration)

3. [Create an auto scaling group for worker nodes](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs#create-auto-scaling-group)


If you already have an AWS ECS cluster with worker nodes and are familiar with the AWS interface, you can skip directly to [creating the Defender task definition](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs#create-task-definition).

Before you create the task definition, ensure that the launch configuration for your worker nodes in ECS includes the following actions.

- Run the Amazon ECS-Optimized Amazon Linux 2 AMI.

- Use the `ecsInstanceRole` IAM role.

- Run the following script for worker nodes to join the cluster and install the Defender.

















AskCopy



```
#!/bin/bash
echo ECS_CLUSTER=pc-ecs-cluster >> /etc/ecs/ecs.config
```


`ECS_CLUSTER` must match your cluster name. Replace `pc_ecs_cluster` with the name of the cluster where you create launch configurations and auto-scaling groups to start EC2 instances for Prisma Cloud. Modify your user data scripts accordingly.

To better understand clusters, read our [cluster context](https://docs.prismacloud.io/admin-guide/install/cluster-context) topic.

## Create your ECS Cluster[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs\#create-your-ecs-cluster)

Create an empty cluster named `pc-ecs-cluster`. This is the cluster where you will create launch configurations and auto-scaling groups to start EC2 instances.

1. Log into the AWS Management Console.

2. Go to **Services > Containers > Elastic Container Service**.

3. Click **Create Cluster**.

4. Select **Networking only**, then click **Next Step**.

5. Enter a cluster name, such as `pc-ecs-cluster`.

6. Click **Create**.


## Create a launch configuration for worker nodes[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs\#create-a-launch-configuration-for-worker-nodes)

Create a launch configuration named `pc-worker-node` that:

- Runs the Amazon ECS-Optimized Amazon Linux 2 AMI.

- Uses the `ecsInstanceRole` IAM role.

- Runs a user data script that joins the pc-ecs-cluster and runs the commands required to install Defender.


01. Go to **Services > Compute > EC2**.

02. In the left menu, click **Auto Scaling > Launch Configurations**.

03. Click **Create Launch Configuration**

04. In **Name**, enter a name for your launch configuration, such as `pc-worker-node`.

05. In Amazon machine image, select **Amazon ECS-Optimized Amazon Linux 2 AMI**.











    You can get a complete list of per-region Amazon ECS-optimized AMIs from [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html).

06. Choose an instance type, such as `t2.medium`.

07. Under **Additional configuration**:









    1. In **IAM instance profile**, select `ecsInstanceRole`.

    2. Under **User data**, select **Text**, and paste the following code snippet:

















       AskCopy



       ```
       #!/bin/bash
       echo ECS_CLUSTER=pc-ecs-cluster >> /etc/ecs/ecs.config
       ```









       Where:









       - `ECS_CLUSTER` must match your cluster name. If you’ve named your cluster something other than `pc_ecs_cluster`, then modify your user data script accordingly.


    3. (Optional) In **IP Address Type**, select **Assign a public IP address to every instance**.











       With this option, you can easily SSH to this instance to troubleshoot issues.


08. Under **Security groups**:









    1. Select **Select an existing security group**.

    2. Select **pc-security-group**.


09. Under **Key pair (login)**, select an existing key pair, or create a new key pair so that you can access your instances.

10. Click **Create launch configuration**.


## Create an auto scaling group for worker nodes[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs\#create-an-auto-scaling-group-for-worker-nodes)

Launch two worker nodes into your cluster.

1. Go to **Services > Compute > EC2**.

2. In the left menu, click **Auto Scaling > Auto Scaling Groups**.

3. Click **Create an Auto Scaling group**.

4. In **Choose launch template or configuration**:









1. In **Auto Scaling group Name**, enter **pc-worker-autoscaling**.

2. In **Launch template**, click **Switch to launch configuration**.

3. Select **pc-worker-node**.

4. Click **Next**.


5. Under **Configure settings**:









1. In **VPC**, select your default VPC.

2. In **Subnet**, select a public subnet, such as 172.31.0.0/20.

3. Click **Next**.


6. In **Configure advanced options**, accept the defaults, and click **Next**.

7. In **Configure group size and scaling policies**:









1. Set **Desired capacity** to **2**.

2. Leave **Minimum capacity** at **1**.

3. Set **Maximum capacity** to **2**.

4. Click **Skip to review**.


8. Review the configuration and click **Create Auto Scaling Group**.











After the auto scaling group spins up (it will take some time), validate that your cluster has three container instances.









1. Go to **Services > Containers > Elastic Container Service**.


## Create a Prisma Cloud Defender task definition[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs\#create-a-prisma-cloud-defender-task-definition)

Generate a task definition for Defender in Prisma Cloud Console.

01. Log into Prisma Cloud Compute Console.

02. Go to **Manage > Defenders > Deploy > Defenders**.

03. In **Deployment method**, select **Orchestrator**.

04. For orchestrator type, select **ECS**.

05. In **Specify a cluster name**, leave the field blank.











    The Prisma Cloud console automatically retrieves the cluster name from AWS. Only enter a value if you want to override the cluster name assigned in AWS.

06. In **Specify ECS task name**, leave the field blank.











    By default, the task name is `pc-defender`.

07. Click **Download** to download the task definition.

08. Log into AWS.

09. Go to **Services > Containers > Elastic Container Service**.

10. In the left menu, click **Task Definitions**.

11. Click **Create new Task Definition**.

12. In **Step 1: Select launch type compatibility**, select **EC2**, then click **Next step**.

13. In **Step 2: Configure task and container definitions**, scroll to the bottom of the page and click **Configure via JSON**.

14. Delete the contents of the window, and replace it with the Prisma Cloud Console task definition you just generated.

15. Click **Save**.

16. (Optional) Change the name of the task definition before creating it. The default name is `pc-defender`.

17. Click **Create**.


### Start the Prisma Cloud Defender Service[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-amazon-ecs\#start-the-prisma-cloud-defender-service)

Create the Defender service using the task definition. With Daemon scheduling, ECS schedules one Defender per node.

01. Go to **Services > Containers > Elastic Container Service**.

02. In the left menu, click **Clusters**.

03. Click on your cluster.

04. In the **Services** tab, click **Create**.

05. In **Step 1: Configure service**:









    1. For **Launch type**, select **EC2**.

    2. For **Task Definition**, select **pc-defender**.

    3. In **Service Name**, enter **pc-defender**.

    4. In **Service Type**, select **Daemon**.

    5. Click **Next Step**.


06. In **Step 2: Configure network**, accept the defaults, and click **Next step**.

07. In **Step 3: Set Auto Scaling**, accept the defaults, and click **Next step**.

08. In **Step 4: Review**, click **Create Service**.

09. Click **View Service**.

10. Verify that you have Defenders running on each node in your ECS cluster.


[PreviousDeploy Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator) [NextAutomatically Install Container Defender in a Cluster](https://docs.prismacloud.io/admin-guide/install/deploy-defender/orchestrator/install-cluster-container-defender)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
