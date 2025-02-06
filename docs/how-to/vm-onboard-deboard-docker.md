---
title: Onboarding and Deboarding VMs with Docker
description: Steps to onboard and deboard VMs with Docker to the AccuKnox SaaS platform for monitoring and enforcing security policies.
---

# Onboarding and Deboarding VMs with Docker

## **Docker**

Docker v19.0.3 and Docker Compose v1.27.0+ are required. Follow the latest [Install Docker Engine](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/") for downloading. Ensure you also add your user to the docker user group: [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/ "https://docs.docker.com/engine/install/linux-postinstall/").

Linux Kernel v5.8+ with BPF LSM support is needed. See how to [enable BPF LSM](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/FAQ.md#checking-and-enabling-support-for-bpf-lsm "https://github.com/kubearmor/KubeArmor/blob/main/getting-started/FAQ.md#checking-and-enabling-support-for-bpf-lsm").

If the environment does not support Linux v5.8+ or BPF LSM and instead uses AppArmor, host enforcement will still work out of the box. However, to protect containers, new containers must be created with special options. Refer to the "[Support for Non-Orchestrated Containers](https://github.com/kubearmor/KubeArmor/wiki/Support-for-non-orchestrated-containers "https://github.com/kubearmor/KubeArmor/wiki/Support-for-non-orchestrated-containers")" documentation for more details.

### Resource Requirements

| Node Type           | vCPU | Memory | Disk  |
|----------------------|------|--------|-------|
| Control Plane Node  | 2    | 4 GB   | 24 GB |
| Worker Node         | 2    | 2 GB   | 12 GB |

### Network Requirements

Connectivity between control plane node and worker nodes is a must. They should either be:

- Part of the same private network **(recommended & secure)**

- Control plane has a public IP (not recommended)

Ports required on the control plane VM:


| Component                       | Type                           | Ports          | Endpoint                          | Purpose                                           |
|---------------------------------|--------------------------------|----------------|----------------------------------|--------------------------------------------------|
| Knox-Gateway                    | Outbound to SaaS               | 3000           | `knox-gw.<env>.accuknox.com:3000`  | For Knox-Gateway service                         |
| PPS                             | Outbound to SaaS               | 443            | `pps.<env>.accuknox.com`           | For PPS (Policy Provisioning Service)            |
| Spire-Server                    | Outbound to SaaS               | 8081, 9090     | `spire.<env>.accuknox.com`         | For Spire-Server communication                   |
| KubeArmor Relay Server          | Inbound in Control Plane       | 32768          | -                                | For KubeArmor relay server on control plane      |
| Shared Informer Agent           | Inbound in Control Plane       | 32769          | -                                | For Shared Informer agent on control plane       |
| Policy Enforcement Agent (PEA)  | Inbound in Control Plane       | 32770          | -                                | For Policy Enforcement Agent on control plane    |
| Hardening Module                | Inbound in Control Plane       | 32771          | -                                | For Discovery Engine Hardening Module            |
| VM Worker Nodes                 | Outbound from worker node to Control Plane | 32768-32771   | -                                | For VM worker nodes to connect to the control plane |


By default, the network created by onboarding commands reserves the subnet `172.20.32.0/27`. If you want to change it for your environment, you can use the `--network-cidr` flag.

You can check the connectivity between nodes using curl. Upon a successful connection, the message returned by curl will be:

```
$ curl <control-plane-addr>:32770
curl: (1) Received HTTP/0.9 when not allowed
```

## Onboarding

Navigate to the onboarding page (Settings → Manage Cluster → Onboard Now) and choose the "VM" option on the instructions page. Then, provide a name for your cluster. You will be presented with instructions to download accuknox-cli and onboard your cluster.

The following agents are installed:

1. **Feeder-service** which collects KubeArmor feeds.

2. **Shared-informer-agent** authenticates with your VMs and collects information regarding entities like hosts, containers, and namespaces.

3. **Policy-enforcement-agent** authenticates with your VMs and enforces labels and policies.

### Install knoxctl/accuknox-cli

`curl -sfL https://knoxctl.accuknox.com/install.sh | sudo sh -s -- -b /usr/bin`

### Onboarding Control Plane

The command may look something like this:

```sh
$ knoxctl onboard vm Control Plane-node \
  --version "v0.2.10" \
  --join-token="843ef458-cecc-4fb9-b5c7-9f1bf7c34567" \
  --spire-host="spire.dev.accuknox.com" \
  --pps-host="pps.dev.accuknox.com" \
  --knox-gateway="knox-gw.dev.accuknox.com:3000"
```

The above command will emit the command to onboard worker nodes. You may also use the `--Control Plane-node-addr` flag to specify the address that other nodes will use to connect with your cluster.

By default, the network created by onboarding commands reserves the subnet `172.20.32.0/27` for the `accuknox-net` Docker network. If you want to change it for your environment, you can use the `--network-cidr` flag.

### Onboarding Worker Nodes

The second command will be for onboarding worker nodes. It may look something like this:

`knoxctl onboard vm node --Control Plane-node-addr=<control-plane-addr>`

Example:

```sh
$ knoxctl onboard vm node --Control Plane-node-addr=192.168.56.106
Pulling kubearmor-init       ... done
Pulling kubearmor            ... done
Pulling kubearmor-vm-adapter ... done
Creating network "accuknox-config_accuknox-net" with the default driver
Creating kubearmor-init ... done
Creating kubearmor      ... done
Creating kubearmor-vm-adapter ... done
onboard-vm-node.go:41: VM successfully joined with control-plane!
```

## Troubleshooting

If you encounter any issues while onboarding, use the commands below to debug:

```sh
docker logs spire-agent -f
docker logs shared-informer-agent -f
docker logs kubearmor-init -f
docker logs kubearmor -f
```

## Deboarding

Deboard the cluster from SaaS first.

To deboard the worker-vm/Node:

`knoxctl deboard vm node`

To deboard the Control-Plane VM:

`knoxctl deboard vm Control Plane-node`

Sample Output:

```sh
$ knoxctl deboard vm Control Plane-node
[+] Running 10/10
 ✔ Container shared-informer-agent       Removed                                                                   0.6s
 ✔ Container feeder-service              Removed                                                                   0.6s
 ✔ Container policy-enforcement-agent    Removed                                                                   0.8s
 ✔ Container wait-for-it                 Removed                                                                   0.0s
 ✔ Container kubearmor-vm-adapter        Removed                                                                   5.6s
 ✔ Container kubearmor-relay-server      Removed                                                                   1.5s
 ✔ Container spire-agent                 Removed                                                                   0.5s
 ✔ Container kubearmor                   Removed                                                                  10.4s
 ✔ Container kubearmor-init              Removed                                                                   0.0s
 ✔ Network accuknox-config_accuknox-net  Removed                                                                   0.3s
Please remove any remaining resources at /home/user/.accuknox-config
Control plane node deboarded successfully.
```

After that cleanup the ~/.accuknox-config directory

`sudo rm -rf ~/.accuknox-config`
