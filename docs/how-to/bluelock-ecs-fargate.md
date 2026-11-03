---
title: Deploy BlueLock on ECS Fargate
description: Deploy BlueLock on Amazon ECS Fargate with Terraform, onboard the tasks to AccuKnox as a VM cluster and block a command to confirm runtime enforcement.
---

# Deploy BlueLock on ECS Fargate

!!! info "Overview"
    Build an ECS Fargate test environment with Terraform, onboard it to AccuKnox as a VM cluster and block a command in a running task.

## Workflow at a Glance

<div class="bl-dia" role="img" aria-label="Six steps for ECS Fargate: get a join token, sign in to AWS and ECR, create the base infrastructure, deploy the sample service, confirm the nodes in AccuKnox, then test the block policy." data-bl="ecs-flow">
<svg viewBox="0 0 760 128" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="bl-ecs-flow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <path class="rail" d="M63 16 H697"/>
  <rect class="navy" x="27" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="63" y="20" text-anchor="middle">Step 1</text>
  <text class="b" x="63" y="56" text-anchor="middle">Get a join</text>
  <text class="b" x="63" y="74" text-anchor="middle">token</text>
  <text class="ms" x="63" y="100" text-anchor="middle">AccuKnox</text>
  <rect class="navy" x="154" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="190" y="20" text-anchor="middle">Step 2</text>
  <text class="b" x="190" y="56" text-anchor="middle">Sign in to</text>
  <text class="b" x="190" y="74" text-anchor="middle">AWS and ECR</text>
  <text class="ms" x="190" y="100" text-anchor="middle">aws configure</text>
  <rect class="navy" x="280" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="317" y="20" text-anchor="middle">Step 3</text>
  <text class="b" x="317" y="56" text-anchor="middle">Create base</text>
  <text class="b" x="317" y="74" text-anchor="middle">infrastructure</text>
  <text class="ms" x="317" y="100" text-anchor="middle">terraform</text>
  <rect class="navy" x="407" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="443" y="20" text-anchor="middle">Step 4</text>
  <text class="b" x="443" y="56" text-anchor="middle">Deploy the</text>
  <text class="b" x="443" y="74" text-anchor="middle">sample service</text>
  <text class="ms" x="443" y="100" text-anchor="middle">terraform</text>
  <rect class="navy" x="534" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="570" y="20" text-anchor="middle">Step 5</text>
  <text class="b" x="570" y="56" text-anchor="middle">Confirm the</text>
  <text class="b" x="570" y="74" text-anchor="middle">nodes</text>
  <text class="ms" x="570" y="100" text-anchor="middle">AccuKnox</text>
  <rect class="navy" x="660" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="697" y="20" text-anchor="middle">Step 6</text>
  <text class="b" x="697" y="56" text-anchor="middle">Test the</text>
  <text class="b" x="697" y="74" text-anchor="middle">block policy</text>
  <text class="ms" x="697" y="100" text-anchor="middle">socat</text>
</svg>
</div>

## How the Deployment Fits Together

<div class="bl-dia" role="img" aria-label="ECS Fargate architecture. A control plane node runs the AccuKnox agents and reaches AccuKnox SaaS. An ECS cluster on Fargate runs two tasks. Each task holds bluelock, armored-container and kubearmor-vm-adapter. The adapters connect to the control plane on ports 32768 to 32771. A test client reaches a task on port 1337." data-bl="ecs">
<svg viewBox="0 0 760 490" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="bl-ecs" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="navy" x="250" y="0" width="260" height="64" rx="10"/>
  <g class="ic-w" transform="translate(270 20) scale(1.0)"><path d="M7 18h10a4 4 0 0 0 .6-7.95A6 6 0 0 0 6 9.6 4.2 4.2 0 0 0 7 18z"/></g>
  <text class="wh" x="304" y="30">AccuKnox SaaS</text>
  <text class="ws" x="304" y="49">Policies and alerts</text>
  <rect class="card" x="0" y="150" width="180" height="160" rx="10"/>
  <g class="ic" transform="translate(16 166) scale(1.0)"><rect x="3" y="4" width="18" height="7" rx="2"/><rect x="3" y="13" width="18" height="7" rx="2"/><circle class="dot" cx="7" cy="7.5" r=".9"/><circle class="dot" cx="7" cy="16.5" r=".9"/></g>
  <text class="b" x="48" y="184">Control plane</text>
  <text class="s" x="16" y="214">EC2 or any VM</text>
  <text class="s" x="16" y="230">with a public IP</text>
  <rect class="navy" x="12" y="250" width="156" height="48" rx="8"/>
  <g class="ic-w" transform="translate(22 262) scale(0.9)"><path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/></g>
  <text class="wb" x="48" y="279">AccuKnox agents</text>
  <rect class="panel" x="260" y="110" width="500" height="300" rx="10"/>
  <g class="ic" transform="translate(276 124) scale(1.0)"><path d="M12 3 3.5 7.5v9L12 21l8.5-4.5v-9L12 3z"/><path d="M3.5 7.5 12 12l8.5-4.5M12 12v9"/></g>
  <text class="h" x="306" y="143">Amazon ECS on Fargate</text>
  <rect class="card" x="276" y="166" width="224" height="226" rx="10"/>
  <text class="b" x="292" y="194">Fargate task 1</text>
  <rect class="row" x="292" y="212" width="192" height="38" rx="8"/>
  <circle class="navy" cx="312" cy="231" r="10"/>
  <text class="num" x="312" y="235" text-anchor="middle">1</text>
  <text class="m" x="330" y="235">bluelock (init)</text>
  <rect class="row" x="292" y="262" width="192" height="38" rx="8"/>
  <circle class="navy" cx="312" cy="281" r="10"/>
  <text class="num" x="312" y="285" text-anchor="middle">2</text>
  <text class="m" x="330" y="285">armored-container</text>
  <rect class="row" x="292" y="312" width="192" height="38" rx="8"/>
  <circle class="navy" cx="312" cy="331" r="10"/>
  <text class="num" x="312" y="335" text-anchor="middle">3</text>
  <text class="m" x="330" y="335">kubearmor-vm-adapter</text>
  <text class="s" x="292" y="376">Public IP, port 1337</text>
  <rect class="card" x="520" y="166" width="224" height="226" rx="10"/>
  <text class="b" x="536" y="194">Fargate task 2</text>
  <rect class="row" x="536" y="212" width="192" height="38" rx="8"/>
  <circle class="navy" cx="556" cy="231" r="10"/>
  <text class="num" x="556" y="235" text-anchor="middle">1</text>
  <text class="m" x="574" y="235">bluelock (init)</text>
  <rect class="row" x="536" y="262" width="192" height="38" rx="8"/>
  <circle class="navy" cx="556" cy="281" r="10"/>
  <text class="num" x="556" y="285" text-anchor="middle">2</text>
  <text class="m" x="574" y="285">armored-container</text>
  <rect class="row" x="536" y="312" width="192" height="38" rx="8"/>
  <circle class="navy" cx="556" cy="331" r="10"/>
  <text class="num" x="556" y="335" text-anchor="middle">3</text>
  <text class="m" x="574" y="335">kubearmor-vm-adapter</text>
  <text class="s" x="536" y="376">Public IP, port 1337</text>
  <path class="ln" d="M276 232 H184" marker-end="url(#bl-ecs)"/>
  <text class="s" x="220" y="212" text-anchor="middle">32768-32771</text>
  <path class="ln" d="M90 150 V32 H246" marker-end="url(#bl-ecs)"/>
  <text class="s" x="102" y="100">outbound</text>
  <rect class="card" x="470" y="446" width="250" height="34" rx="8"/>
  <text class="m" x="595" y="468" text-anchor="middle">socat - TCP:TASK_IP:1337</text>
  <path class="ln" d="M595 446 V414" marker-end="url(#bl-ecs)"/>
</svg>
</div>

| Container | Role in the task |
|---|---|
| `bluelock` | Copies the binary into a shared volume, then exits |
| `armored-container` | Runs your app behind `/kubearmor/bluelock`. The sample runs `socat` on port 1337 |
| `kubearmor-vm-adapter` | Sends events to the control plane and receives policies |

## Prerequisites

| Requirement | Used for |
|---|---|
| AWS admin access | Creating the VPC, EC2 instance, IAM role, CloudWatch log group, ECS cluster and service |
| AWS CLI, configured | Terraform and the ECR login use your credentials |
| Terraform | Running both scripts |
| Docker | The `docker login` command in Step 2 |
| `git` | Cloning the BlueLock repository |
| `socat` | Connecting to the sample task in Step 6 |
| An EC2 key pair in `us-east-1` | The SSH key prompt in Step 3 |
| AccuKnox account | Getting a join token and viewing the results |

## Step 1. Get a Join Token From AccuKnox

In AccuKnox, open Settings, then Manage Cluster, then Onboard. Select the cluster type VM, enter a name and copy the join token from the `knoxctl onboard vm cp-node` command.

![The AccuKnox Cluster Onboarding page with VM selected and the knoxctl onboard command that carries the join token](images/bluelock-ecs-fargate/join-token.png)

Terraform runs that command on the new EC2 instance, so you only need the token.

## Step 2. Sign in to AWS and Public ECR

Enter your Access Key ID and Secret Access Key.

```bash
aws configure
```

Log in to public ECR.

```bash
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/k9v9d5v2
```

## Step 3. Create the Base Infrastructure

Clone the repository and open `base-infra`.

```bash
git clone https://github.com/accuknox/bluelock.git
cd bluelock/terraform/ecs-fargate/base-infra
```

Run Terraform.

```bash
terraform init
terraform apply
```

`terraform apply` prompts for `join_token` (from Step 1) and `ssh_key_name` (an existing EC2 key pair in `us-east-1`). To skip the prompts, pass `-var="join_token=<JOIN_TOKEN>"` and `-var="ssh_key_name=<KEY_PAIR_NAME>"`.

The script creates these resources in `us-east-1`:

| Resource | Details |
|---|---|
| Network | VPC `bluelock-vpc` (`10.0.0.0/16`), subnet `bluelock-subnet` (`10.0.1.0/24`), an internet gateway and a route table |
| Security group | `bluelock-sg` allows all inbound and outbound traffic |
| Control plane node | EC2 instance `cp-node`, Ubuntu 24.04 on `t3.medium` with a 20 GB `gp3` volume. It installs Docker and `knoxctl`, then runs `knoxctl onboard vm cp-node` with your token |
| Logging | CloudWatch log group `/ecs/armored-container` with 7-day retention |
| IAM | Role `ecsTaskExecutionRolePolicy` with the `AmazonECSTaskExecutionRolePolicy` policy |
| ECS | Cluster `bluelock-test` and task definition `worker-node` (256 CPU, 512 MB, X86_64 Linux) with the three containers |

!!! warning "The security group is open to the internet"
    `bluelock-sg` allows all inbound traffic from anywhere. Use it for testing only. In production, open only the ports the agents need.

The script onboards against `spire.demo.accuknox.com`, `pps.demo.accuknox.com` and `knox-gw.demo.accuknox.com:3000`. Edit `base-infra/main.tf` to use another environment.

## Step 4. Deploy the Sample Service

Run Terraform in `test-task`.

```bash
cd ../test-task
terraform init
terraform apply
```

Terraform creates the service `worker-test-service` on `bluelock-test`. It runs 2 Fargate tasks in `bluelock-subnet` with `bluelock-sg`, each with a public IP.

??? note "Set up manually instead of using Terraform"
    Replaces Steps 3 and 4. Create a VPC and a VM with a public IP first.

    **Control plane**

    1. Install Docker on the VM.
    2. Create a VM cluster on this VM, with only the control plane node, and onboard it to AccuKnox with the commands from Step 1.

        ![The AccuKnox Cluster Onboarding page with the control plane install commands](images/bluelock-ecs-fargate/join-token.png)

    3. Confirm that the cluster onboarded.

        ![The AccuKnox cluster panel showing the cluster as Connected](images/bluelock-ecs-fargate/control-plane-connected.png)

    **IAM role**

    1. In AWS IAM, create a role for the ECS task. Under Service, select `Elastic Container Service`. Under Use case, select `Elastic Container Service Task` and choose Next.

        ![The IAM Create role page with AWS service and Elastic Container Service Task selected](images/bluelock-ecs-fargate/iam-trusted-entity.png)

    2. Select `AmazonECSTaskExecutionRolePolicy` and choose Next.

        ![The IAM Add permissions page with AmazonECSTaskExecutionRolePolicy selected](images/bluelock-ecs-fargate/iam-permissions-policy.png)

    3. Name the role and save it.

        ![The IAM Name, review, and create page with the role name filled in](images/bluelock-ecs-fargate/iam-role-name.png)

    **CloudWatch log group**

    Open CloudWatch, then Log management, and create a log group named `/ecs/armored-container`.

    ![The CloudWatch Create log group page with the name /ecs/armored-container](images/bluelock-ecs-fargate/cloudwatch-log-group.png)

    **ECS cluster**

    Create an ECS cluster with the Fargate only option and the default settings.

    ![The ECS Create cluster page with Fargate only selected](images/bluelock-ecs-fargate/ecs-create-cluster.png)

    **Task definition**

    Create a task definition from the following JSON. Set `awslogs-region` to the region where you created the log group. In the `kubearmor-vm-adapter` commands, replace `<CONTROL-PLANE-IP>` with the IP address of the control plane node.

    ```json
    {
        "family": "worker-node",
        "containerDefinitions": [
            {
                "name": "armored-container",
                "image": "public.ecr.aws/k9v9d5v2/accuknox-bluelock/ka-socat-demo:latest",
                "cpu": 0,
                "portMappings": [
                    {
                        "containerPort": 1337,
                        "hostPort": 1337,
                        "protocol": "tcp",
                        "name": "armored-container-1337-tcp",
                        "appProtocol": "http"
                    }
                ],
                "essential": true,
                "command": [
                    "/kubearmor/bluelock",
                    "socat",
                    "TCP-LISTEN:1337,reuseaddr,fork",
                    "EXEC:bash,pty,stderr,setsid,sigint,sane"
                ],
                "environment": [
                    {
                        "name": "CONTAINERNAME",
                        "value": "armored-container"
                    },
                    {
                        "name": "K8S",
                        "value": "false"
                    }
                ],
                "mountPoints": [
                    {
                        "sourceVolume": "kubearmor-dir",
                        "containerPath": "/kubearmor",
                        "readOnly": true
                    }
                ],
                "volumesFrom": [],
                "dependsOn": [
                    {
                        "containerName": "bluelock",
                        "condition": "SUCCESS"
                    }
                ],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "/ecs/armored-container",
                        "awslogs-region": "us-east-1",
                        "awslogs-stream-prefix": "ecs"
                    }
                },
                "systemControls": []
            },
            {
                "name": "bluelock",
                "image": "public.ecr.aws/k9v9d5v2/accuknox-bluelock:v1.0.0",
                "cpu": 0,
                "portMappings": [],
                "essential": false,
                "environment": [],
                "mountPoints": [
                    {
                        "sourceVolume": "kubearmor-dir",
                        "containerPath": "/kubearmor",
                        "readOnly": false
                    }
                ],
                "volumesFrom": [],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "/ecs/armored-container",
                        "awslogs-region": "us-east-1",
                        "awslogs-stream-prefix": "ecs"
                    }
                },
                "systemControls": []
            },
            {
                "name": "kubearmor-vm-adapter",
                "image": "docker.io/accuknox/vm-adapter:v0.1.29",
                "cpu": 0,
                "portMappings": [],
                "essential": true,
                "command": [
                    "--kubearmor-addr=localhost:32767",
                    "--relay-server-addr=<CONTROL-PLANE-IP>:32768",
                    "--node-state-refresh=4",
                    "--policy-list-enable=true",
                    "--policy-list-relay-frequency=5m0s",
                    "--sia-addr=<CONTROL-PLANE-IP>:32769",
                    "--pea-addr=<CONTROL-PLANE-IP>:32770",
                    "--harden-addr=<CONTROL-PLANE-IP>:32771",
                    "--annotation-topic=annotation",
                    "--annotation-enable=true"
                ],
                "environment": [
                    {
                        "name": "test",
                        "value": "true"
                    }
                ],
                "mountPoints": [
                    {
                        "sourceVolume": "opt-storage",
                        "containerPath": "/opt",
                        "readOnly": false
                    }
                ],
                "volumesFrom": [],
                "dependsOn": [
                    {
                        "containerName": "armored-container",
                        "condition": "START"
                    }
                ],
                "logConfiguration": {
                    "logDriver": "awslogs",
                    "options": {
                        "awslogs-group": "/ecs/armored-container",
                        "awslogs-region": "us-east-1",
                        "awslogs-stream-prefix": "adapter"
                    }
                },
                "systemControls": []
            }
        ],
        "taskRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>",
        "executionRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/<ROLE_NAME>",
        "networkMode": "awsvpc",
        "volumes": [
            {
                "name": "kubearmor-dir",
                "host": {}
            },
            {
                "name": "opt-storage",
                "host": {}
            }
        ],
        "placementConstraints": [],
        "requiresCompatibilities": [
            "FARGATE"
        ],
        "cpu": "256",
        "memory": "512",
        "runtimePlatform": {
            "cpuArchitecture": "X86_64",
            "operatingSystemFamily": "LINUX"
        }
    }
    ```

    **Run the task**

    Run a new task from this task definition. In Networking, select the correct VPC and turn on `Public IP`. In Task overrides, select the task role and the task execution role that you created.

    ![The ECS Run task page with Public IP turned on and the task role and task execution role selected](images/bluelock-ecs-fargate/ecs-run-task.png)

    The security group of the task must allow all inbound traffic from anywhere. Use this for testing only.

## Step 5. Confirm the Nodes Appear in AccuKnox

In CloudWatch, the `armored-container` stream shows BlueLock starting `socat`.

![CloudWatch log events for the armored-container, ending with the socat command that BlueLock runs](images/bluelock-ecs-fargate/armored-container-logs.png)

The `kubearmor-vm-adapter` stream shows the connection to the control plane.

![CloudWatch log events for the kubearmor-vm-adapter, showing connections to the relay server and policy enforcement agent](images/bluelock-ecs-fargate/vm-adapter-logs.png)

In AccuKnox, the cluster shows its nodes, workloads and namespaces after a few minutes.

![The AccuKnox cluster panel for the ECS cluster, showing 2 nodes, 11 workloads and 1 namespace](images/bluelock-ecs-fargate/saas-cluster-nodes.png)

## Step 6. Test Enforcement With a Block Policy

1. In the ECS console, open `bluelock-test`, then `worker-test-service`, and copy a task's public IP.

2. Connect to the task.

    ```bash
    socat - TCP:<task-ip>:1337
    ```

3. Run this. It succeeds because no policy exists yet.

    ```bash
    ls /etc/ssl/certs
    ```

    ![A terminal session that lists the files in /etc/ssl/certs](images/bluelock-ecs-fargate/socat-ls-allowed.png)

4. In AccuKnox, open Runtime Protection, then Policies, and create this policy. [`ksp-block-file-dir-recursive.yaml`](https://raw.githubusercontent.com/accuknox/bluelock/refs/heads/master/terraform/ksp-block-file-dir-recursive.yaml) holds the same rules.

    ```yaml
    apiVersion: security.kubearmor.com/v1
    kind: KubeArmorPolicy
    metadata:
      name: bluelock-test-policy
      namespace: container_namespace
    spec:
      action: Block
      file:
        matchDirectories:
        - dir: /etc/ssl/
          recursive: true
        - dir: /etc/pki/
          recursive: true
        - dir: /usr/local/share/ca-certificates/
          recursive: true
      message: Credentials modification denied
      selector:
        matchLabels:
          kubearmor.io/container.name: armored-container
      severity: 1
      tags:
      - MITRE
      - MITRE_T1552_unsecured_credentials
    ```

5. Select the policy and choose Activate.

    ![The AccuKnox Policies page showing bluelock-test-policy with the status Active](images/bluelock-ecs-fargate/policy-activated.png)

6. In CloudWatch, the `armored-container` stream reports the policy.

    ![CloudWatch log events showing the line Detected a Container Security Policy for bluelock-test-policy](images/bluelock-ecs-fargate/policy-detected-cloudwatch.png)

7. Run the command again. It now fails.

    ```bash
    ls /etc/ssl/certs
    ```

    ![A terminal session where ls /etc/ssl/certs returns Permission denied](images/bluelock-ecs-fargate/socat-ls-denied.png)

8. Open the alert in AccuKnox.

    ![The AccuKnox alert Credentials modification denied with action Block and result Permission Denied](images/bluelock-ecs-fargate/alert-credentials-denied.png)

??? example "Raw alert"
    ```json
    {
      "Action":"Block",
      "ClusterName":"bluelock-test",
      "ContainerID":"3173432111",
      "ContainerName":"armored-container",
      "Data":"syscall=openat fd=4294967196 flags=591872 mode=0",
      "Enforcer":"Ptrace enforcer",
      "HostName":"47d63a5ab7e24ec4b10769bc027b8dcd-3173432111",
      "Message":"Credentials modification denied",
      "Operation":"File",
      "PID":22,
      "PPID":18,
      "ParentProcessName":"/usr/bin/bash",
      "PolicyName":"bluelock-test-policy",
      "ProcessName":"/usr/bin/ls",
      "Resource":"/etc/ssl/certs",
      "Result":"Permission denied",
      "Severity":"1",
      "Source":"/usr/bin/ls",
      "Suppressed":false,
      "Tags":"MITRE,MITRE_T1552_unsecured_credentials",
      "Timestamp":1777238300,
      "Type":"MatchedPolicy",
      "UID":0,
      "_id":"<ALERT_ID>",
      "cluster_id":"<CLUSTER_ID>",
      "component_name":"kubearmor",
      "instanceGroup":"0",
      "instanceID":"0",
      "tenant_id":"<TENANT_ID>",
      "workload":"1"
    }
    ```

## Step 7. Destroy the Test Environment When You Finish

Destroy the service first, then the base infrastructure. `base-infra` prompts for the join token and SSH key name again.

```bash
cd bluelock/terraform/ecs-fargate/test-task
terraform destroy
cd ../base-infra
terraform destroy
```
