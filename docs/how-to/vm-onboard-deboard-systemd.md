---
title: Onboarding and Deboarding VMs with Systemd
description: Step-by-step process to onboard VMs with Systemd/Docker mode on AccuKnox SaaS to enable automated security enforcement and monitoring.
---

# Onboarding and Deboarding VMs with Systemd

## Systemd

**Systemd** is a core component of modern Linux systems responsible for managing services and processes. It ensures that essential services start automatically during boot, remain running, and restart if they fail. In simple terms, systemd acts like a **controller** that organizes and oversees everything needed to keep the system stable and functional.

Currently, **root/sudo** permissions are needed for onboarding systemd. This is because KubeArmor requires privileges to protect the host and systemd services, packages are currently installed on the root directory.

Only in case of the control plane node, a working RabbitMQ server is required. This can be installed using Docker.

```
# Latest RabbitMQ 3.13
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

Alternatively, you can install RabbitMQ using a package manager:

- **Linux, BSD, UNIX**: [Debian, Ubuntu](https://www.rabbitmq.com/docs/install-debian "https://www.rabbitmq.com/docs/install-debian") | [RHEL, CentOS Stream, Fedora](https://www.rabbitmq.com/docs/install-rpm "https://www.rabbitmq.com/docs/install-rpm") | [Generic binary build](https://www.rabbitmq.com/docs/install-generic-unix "https://www.rabbitmq.com/docs/install-generic-unix") | [Solaris](https://www.rabbitmq.com/docs/install-solaris "https://www.rabbitmq.com/docs/install-solaris")

- **Windows**: [Chocolatey package](https://community.chocolatey.org/packages/rabbitmq "https://community.chocolatey.org/packages/rabbitmq") | [Windows Installer](https://www.rabbitmq.com/docs/install-windows "https://www.rabbitmq.com/docs/install-windows") | [Binary build](https://www.rabbitmq.com/docs/install-windows-manual "https://www.rabbitmq.com/docs/install-windows-manual")

- **MacOS**: [Homebrew](https://www.rabbitmq.com/docs/install-homebrew "https://www.rabbitmq.com/docs/install-homebrew") | [Generic binary build](https://www.rabbitmq.com/docs/install-generic-unix "https://www.rabbitmq.com/docs/install-generic-unix")

- [Erlang/OTP for RabbitMQ](https://www.rabbitmq.com/docs/which-erlang "https://www.rabbitmq.com/docs/which-erlang")

BTF support is needed. Any kernel version which has this should work. Check if BTF info is present with the script below:

```bash
if [ ! -e "/sys/kernel/btf/vmlinux" ]; then
  echo "BTF info not present"
else
  echo "BTF info present"
fi
```

If the script returns "BTF info not present," [BTF support is not available](https://help.accuknox.com/how-to/systemd-nonbtf/ "https://help.accuknox.com/how-to/systemd-nonbtf/"), and you should run the script below to build the required files on your system:

```bash
# Download KubeArmor
git clone https://github.com/kubearmor/KubeArmor/
cd KubeArmor/KubeArmor/packaging
./post-install.sh
```

!!! note
    For detailed instructions specific to SystemD Based Non-BTF Environments, please refer to this [guide](https://help.accuknox.com/how-to/systemd-nonbtf/ "https://help.accuknox.com/how-to/systemd-nonbtf/").

**Container Protection Requirements** (Optional)

If container protection is needed, a Linux Kernel with **BPF LSM** is desired. Generally, it is present in v5.8+. Here's a guide on enabling BPF LSM: [KubeArmor Getting Started FAQ](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/FAQ.md#checking-and-enabling-support-for-bpf-lsm "https://github.com/kubearmor/KubeArmor/blob/main/getting-started/FAQ.md#checking-and-enabling-support-for-bpf-lsm").

If BPF LSM is not available, AppArmor should still work out of the box for host policy application. However, follow the guide [Support for non orchestrated containers](https://github.com/kubearmor/KubeArmor/wiki/Support-for-non-orchestrated-containers "https://github.com/kubearmor/KubeArmor/wiki/Support-for-non-orchestrated-containers") for each container.

### Resource Requirements

#### Control Plane Node (Minimum)

| Resource | Requirement |
|----------|-------------|
| CPU      | 2 vCPU      |
| Memory   | 4 GB        |
| Disk     | 1 GB        |

#### Worker Node (Minimum)

| Resource | Requirement |
|----------|-------------|
| CPU      | 2 vCPU      |
| Memory   | 2 GB        |
| Disk     | 500 MB      |

## Network Requirements

Connectivity between control plane node and worker nodes is a must. They should either be:

- Part of the same private network **(recommended & secure)**

- Control plane has a public IP (not recommended)

Ports required on the control plane VM:

| **Component**                  | **Type**                              | **Ports**        | **Endpoint**                       | **Purpose**                                        |
|--------------------------------|--------------------------------------|------------------|-----------------------------------|---------------------------------------------------|
| Knox-Gateway                   | Outbound to SaaS                     | 3000             | `knox-gw.<env>.accuknox.com:3000`   | For Knox-Gateway service                          |
| PPS                            | Outbound to SaaS                     | 443              | `pps.<env>.accuknox.com`            | For PPS (Policy Provisioning Service)             |
| Spire-Server                   | Outbound to SaaS                     | 8081, 9090       | `spire.<env>.accuknox.com`       | For Spire-Server communication                    |
| KubeArmor Relay Server         | Inbound in Control Plane             | 32768            | -                                 | For KubeArmor relay server on control plane       |
| Shared Informer Agent          | Inbound in Control Plane             | 32769            | -                                 | For Shared Informer agent on control plane        |
| Policy Enforcement Agent (PEA) | Inbound in Control Plane             | 32770            | -                                 | For Policy Enforcement Agent on control plane     |
| Hardening Module               | Inbound in Control Plane             | 32771            | -                                 | For Discovery Engine Hardening Module             |
| VM Worker Nodes                | Outbound from worker node to Control Plane | 32768-32771     | -                                 | For VM worker nodes to connect to the control plane |

Check the CWPP documentation for more details on the [network requirements](https://help.accuknox.com/getting-started/cwpp-prereq/#minimum-resource-required "https://help.accuknox.com/getting-started/cwpp-prereq/#minimum-resource-required").

You can check the connectivity between nodes using curl. Upon a successful connection, the message returned by curl will be:

```
$ curl <control-plane-addr>:32770
curl: (1) Received HTTP/0.9 when not allowed
```

## Onboarding

Navigate to the onboarding page (Settings → Manage Cluster → Onboard Now) and choose the "VM" option on the instructions page. Then, provide a name for your cluster. You will be presented with instructions to download accuknox-cli and onboard your cluster.

The following agents will be installed:

1. **Feeder-service** which collects KubeArmor feeds.

2. **Shared-informer-agent** authenticates with your VMs and collects information regarding entities like hosts, containers, and namespaces.

3. **Policy-enforcement-agent** authenticates with your VMs and enforces labels and policies.

### Install knoxctl/accuknox-cli

`curl -sfL https://knoxctl.accuknox.com/install.sh | sudo sh -s -- -b /usr/bin`

### Onboarding Control Plane

The command may look something like this:

```
$ knoxctl onboard vm cp-node \
  --version "v0.2.10" \
  --join-token="843ef458-cecc-4fb9-b5c7-9f1bf7c34567" \
  --spire-host="spire.dev.accuknox.com" \
  --pps-host="pps.dev.accuknox.com" \
  --knox-gateway="knox-gw.dev.accuknox.com:3000"
```

!!! note
    By default, if Docker is not found, systemd mode of installation would be used. If you want to explicitly onboard using systemd services, add the `--vm-mode=systemd` flag to the above command.

The above command will emit the command to onboard worker nodes. You may also use the `--cp-node-addr` flag to specify the address that other nodes will use to connect with your cluster.

## Onboarding Worker Nodes

The second command will be for onboarding worker nodes. It may look something like this:

`knoxctl onboard vm node --cp-node-addr=<control-plane-addr>`

Example:

```
$ knoxctl onboard vm node --cp-node-addr=192.168.56.106
Pulling kubearmor-init       ... done
Pulling kubearmor            ... done
Pulling kubearmor-vm-adapter ... done
Creating network "accuknox-config_accuknox-net" with the default driver
Creating kubearmor-init ... done
Creating kubearmor      ... done
Creating kubearmor-vm-adapter ... done
onboard-vm-node.go:41: VM successfully joined with control-plane!
```

![image-20241111-053236.png](https://i.ibb.co/z4Jc6Dn/2-F01-D559-950-C-45-CC-AEF5-9-DE947-D92-BAB.png)

## Troubleshooting

If you encounter any issues while onboarding, use the commands below to debug:

`sudo journalctl -xeu <service-name>.service`

Replace `<service-name>` with one of the following:

- `kubearmor`: Logs show policy enforcement and monitor Kubernetes workloads; useful for debugging misconfigurations or runtime issues.

- `kubearmor-relay-server`: Bridges KubeArmor clients with external log systems; logs debug communication or relay errors.

- `kubearmor-vm-adapter`: Tracks policy enforcement in VMs; logs diagnose policy application on non-Kubernetes workloads.

- `accuknox-policy-enforcement-agent`: Enforces security policies; logs troubleshoot policy errors or conflicts.

- `accuknox-shared-informer-agent`: Shares Kubernetes resource data; logs debug metadata collection issues.

- `accuknox-sumengine`: Processes telemetry data; logs resolve performance or data processing errors.

- `accuknox-discover-agent`: Discovers potential policies; logs analyze policy suggestions.

- `spire-agent`: Manages workload identities; logs debug identity issuance and attestation issues.

- `accuknox-hardening-agent`: Automates system hardening; logs troubleshoot configuration and hardening conflicts.

## Deboarding

Deboard the cluster from SaaS first.

To deboard the worker-vm/Node:

`knoxctl deboard vm node`

To deboard the Control-Plane VM:

`knoxctl deboard vm cp-node`

Sample Output:

```sh
$ knoxctl deboard vm cp-node
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
