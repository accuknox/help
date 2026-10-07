For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate.md).

You can run Prisma Cloud Console in AWS Fargate.

This procedure assumes you’ve already created an ECS cluster.

## Create a security group[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate\#create-a-security-group)

Create a security group that opens ports 8083-8084 for Prisma Cloud Console and port 2049 for NFS.

1. In the AWS console, go to **Services > Compute > EC2 > Security Groups**.

2. Click **Create security group**.

3. In **Security group name**, enter a name, such as **pc-security-group**.

4. In **Description**, enter **Prisma Cloud Compute Console on Fargate**.

5. In **VPC**, select the VPC where your ECS cluster runs.

6. Create an inbound rule for Prisma Cloud Console ports.









1. Under **Inbound rules** , click **Add rule**.

2. Under **Type**, select **Custom TCP**.

3. Under **Port range**, enter **8083-8084**.

4. Under **Source**, select **Anywhere**.


7. Create an inbound rule for NFS, where Console stores its data.









1. Click **Add rule**.

2. Under **Type**, select **NFS**.

3. Under **Source**, select **Anywhere**.


8. Click **Create security group**.

9. Write down the security group ID and save it for later.


## Create an EFS file system[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate\#create-an-efs-file-system)

Create a highly available file system for Console to store its data.

01. In the AWS console, go to **Services > Storage > EFS**.

02. Click **Create file system**.

03. Click **Customize** to open a more detailed dialog.

04. Enter a value for **Name**, such as **pc-efs-console**.

05. Set the throughput mode to **Provisioned**.

06. Set **Provisioned Throughput (MiB/s)** to 0.1 MiB/s per Defender that will be deployed.

07. Click **Next**.

08. In **VPC**, select the VPC where your EC2 cluster runs and the relevant mount targets.

09. For each mount target, change the security group to the ID of the pc-security-group.

10. Click **Next**, accepting all defaults, until the file system is created.

11. Write down the file system ID and save it for later.


## Create target groups[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate\#create-target-groups)

Create two target groups for the load balancer, one for port 8083 and one for port 8084.

01. In the AWS console, go to **Services > Compute > EC2 > Load Balancing > Target Groups**.

02. Click **Create target group**.

03. In **Basic configuration**, select **IP addresses**.

04. Enter a value for **Name**, such as **pc-tgt-8083** or **pc-tgt-8084**.

05. Set **Protocol** to **TCP** and **Port** to **8083** or **8084** respectively.

06. In VPC, select the VPC where your ECS cluster runs.

07. For port 8083 only, specify the following health check configuration:









    - **Health check protocol**: **HTTPS**

    - **Health check path**: **/**

    - **Port**: **Traffic port**

    - Accept the default values for all other settings.


08. Click **Next**, and then click **Create target group**.

09. Repeat the process for port 8084, but accept the default values for the health check configuration.











    The health check protocol for 8084 must be **TCP**.

10. Write down the ARN for both target groups, and save them for later.


## Create a load balancer[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate\#create-a-load-balancer)

Create a network load balancer to route traffic to the Console container.

1. In the AWS console, go to **Services > Compute > EC2 > Load Balancers**.

2. Click **Create Load Balancer**.

3. Choose **Network Load Balancer** and **Create**.

4. Enter a value for **Name**, such as **pc-ecs-lb**.

5. Under **Network mapping**, select the VPC and subnet where the Prisma Cloud Console task will run.

6. Under **Listeners and routing**, create a listener for port 8083.









1. Set **Protocol** to **TCP**.

2. Set **Port** to **8083**.

3. Set **Default action** to **Forward to: pc-tgt-8083**.


7. Create a listener for port 8084.









1. Click **Add listener**.

2. Set **Protocol** to **TCP**.

3. Set **Port** to **8084**.

4. Set **Default action** to **Forward to: pc-tgt-8084**.


8. Click **Create load balancer**.

9. Write down the DNS name for the load balancer, and save it for later.


## Create task definition[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate\#create-task-definition)

Use twistcli to generate a task definition for Console.

Each task definition’s Console can support up to 1000 deployed Defenders.

The following table lists valid values for cpu-limit and memory-limit:

CPU limit

Memory limit (MiB)

1024 (1 vCPU)

2048 (2 GB), 3072 (3 GB), 4096 (4 GB), 5120 (5 GB), 6144 (6 GB), 7168 (7 GB), 8192 (8 GB)

2048 (2 vCPU)

Between 4096 (4 GB) and 16384 (16 GB) in increments of 1024 (1 GB)

4096 (4 vCPU)

Between 8192 (8 GB) and 30720 (30 GB) in increments of 1024 (1 GB)

01. Download the Prisma Cloud Compute Edition release tarball, and unpack it.

02. Run twistcli to create the task definition.

















    AskCopy



    ```
    ./<PLATFORM>/twistcli console export fargate \
    --registry-token <registry token>  \
    --cluster-ip <load balancer dns name> \
    --memory-limit <memory limit number> \
    --cpu-limit <cpu limit number> \
    --efs-volume <efs ID>
    ```









    For example:

















    AskCopy



    ```
    ./linux/twistcli console export fargate \
    --registry-token <my_registry_token_id_string>  \
    --cluster-ip my-fargate-console-dns-address.elb.us-east-1.amazonaws.com \
    --memory-limit 8192 \
    --cpu-limit 2048 \
    --efs-volume fs-12345678
    ```

03. In the AWS console, go to **Services > Containers > Elastic Container Service > Task Definitions**.

04. Click **Create new Task Definition**.

05. Click **Fargate**, then **Next step**.

06. Scroll to the bottom of the page, and click **Configure via JSON**.

07. Clear the text box, paste the contents of **twistlock-console.json** which was generated by twistcli, and click **Save**.

08. In **Task Role**, specify **ecsTaskExecutionRole**.

09. Click **Create**.

10. Click **View Task Definition**.

11. Copy the task definition name and revision (e.g., **pc-console:1**).


## Create Fargate service[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate\#create-fargate-service)

Create the Fargate service.

1. In the AWS console, go to **Services > Networking & Content Delivery > VPC > Subnets**.

2. Filter the subnets by the VPC where your ECS cluster runs, and write down subnet IDs of the relevant availability zones.

3. Fill out the ECS service JSON with all values you’ve set aside until now.











Replace the strings between the `< >` characters, and save the file with the name fargate-pc-console-service.json.

















AskCopy



```
{
       "cluster": "<cluster name>",
       "serviceName": "pc-console",
       "taskDefinition": "<task definition name>:<revision>",
       "loadBalancers": [\
                   {\
                       "targetGroupArn": "<pc-tgt-8083 ARN>",\
                       "containerName": "twistlock-console",\
                       "containerPort": 8083\
                   },\
                                   {\
                       "targetGroupArn": "<pc-tgt-8083 ARN>",\
                       "containerName": "twistlock-console",\
                       "containerPort": 8084\
                   }\
       ],
       "desiredCount": 1,
       "launchType": "FARGATE",
       "deploymentConfiguration": {
           "maximumPercent": 100,
           "minimumHealthyPercent": 0
       },
       "platformVersion": "1.4.0",
       "networkConfiguration": {
           "awsvpcConfiguration": {
               "subnets": [\
                   "<subnet ID>",\
                   "<subnet ID>"\
               ],
               "securityGroups": [\
                   "<security group ID>"\
               ],
               "assignPublicIp": "ENABLED"
           }
       },
       "enableECSManagedTags": true
}
```

4. Create the service using awscli.

















AskCopy



```
aws ecs create-service --cli-input-json file://path/to/fargate-pc-console-service.json
```









If successful the service is successfully created, awscli outputs the full JSON for the service being deployed.

5. In the AWS console, go to **Services > Containers > Elastic Container Service > Clusters**, click your cluster.

6. In the **Services** tab, click the service name ( **pc-console**).











You should see the details for load balancing and network access.

7. In the **Tasks** tab, you should find details about the running container.


## Log into Prisma Cloud Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate\#log-into-prisma-cloud-console)

Open a web browser and go to `https://<Load balancer DNS name>:8083`. Create an initial admin account, and then enter your license to activate Console.

[PreviousDeploy the Prisma Cloud Console on Amazon ECS](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-amazon-ecs) [NextDeploy the Prisma Cloud Console on Onebox](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
