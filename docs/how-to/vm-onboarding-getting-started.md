# Onboarding VMs

## Systemd

Currently, **root/sudo** permissions are needed for onboarding systemd. This is because KubeArmor requires privileges to protect the host and systemd services, packages are currently installed on the root directory.

Only in case of the control plane node, a working RabbitMQ server is required. This can be installed using Docker.

```bash
# Latest RabbitMQ 3.13
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

Alternatively, you can install RabbitMQ using a package manager:

- **Linux, BSD, UNIX**: [Debian, Ubuntu](https://www.rabbitmq.com/docs/install-debian) | [RHEL, CentOS Stream, Fedora](https://www.rabbitmq.com/docs/install-rpm) | [Generic binary build](https://www.rabbitmq.com/docs/install-generic-unix) | [Solaris](https://www.rabbitmq.com/docs/install-solaris)
- **Windows**: [Chocolatey package](https://community.chocolatey.org/packages/rabbitmq) | [Windows Installer](https://www.rabbitmq.com/docs/install-windows) | [Binary build](https://www.rabbitmq.com/docs/install-windows-manual)
- **MacOS**: [Homebrew](https://www.rabbitmq.com/docs/install-homebrew) | [Generic binary build](https://www.rabbitmq.com/docs/install-generic-unix)
- [Erlang/OTP for RabbitMQ](https://www.rabbitmq.com/docs/which-erlang)

BTF support is needed. Any kernel version which has this should work. Check if BTF info is present with the script below:

```bash
if [ ! -e "/sys/kernel/btf/vmlinux" ]; then
  echo "BTF info not present"
else
  echo "BTF info present"
fi
```

If the script returns "BTF info not present," [BTF support is not available](../resources/systemd-nonbtf.md), and you should run the script below to build the required files on your system:

```bash
# Download KubeArmor
git clone https://github.com/kubearmor/KubeArmor/
cd KubeArmor/KubeArmor/packaging
./post-install.sh
```

**If container protection is not needed - No additional requirements**

If container protection is needed, a Linux Kernel with **BPF LSM** is desired. Generally, it is present in v5.8+.
Here's a guide on enabling BPF LSM: [KubeArmor Getting Started FAQ](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/FAQ.md#checking-and-enabling-support-for-bpf-lsm).

If BPF LSM is not available, AppArmor should still work out of the box for host policy application. However, follow the guide [Support for non orchestrated containers](https://github.com/kubearmor/KubeArmor/wiki/Support-for-non-orchestrated-containers) for each container.

### Resource Requirements

| Node Type          | CPU   | Memory | Disk  |
|--------------------|-------|--------|-------|
| Control plane node | 2vCPU | 4 GB   | 1 GB  |
| Worker node        | 2vCPU | 2 GB   | 500 MB |

## Network Requirements

Connectivity between control plane node and worker nodes is a must. They should either be:

- Part of the same private network **(recommended & secure)**
- Control plane has a public IP (not recommended)

Ports required on the control plane VM:

- kubearmor-relay-server: 32768
- shared-informer-agent: 32769
- policy-enforcement-agent: 32770

Check the CWPP documentation for more details on the [network requirements](../getting-started/cwpp-prereq.md#minimum-resource-required).

You can check the connectivity between nodes using curl. Upon a successful connection, the message returned by curl will be:

```bash
$ curl <control-plane-addr>:32770
curl: (1) Received HTTP/0.9 when not allowed
```

## Docker

Docker v19.0.3 and Docker Compose v1.27.0+ are required. Follow the latest [Install Docker Engine](https://docs.docker.com/engine/install/) for downloading. Ensure you also add your user to the docker user group: [Linux post-installation steps for Docker Engine](https://docs.docker.com/engine/install/linux-postinstall/).

Linux Kernel v5.8+ with BPF LSM support is needed. See how to [enable BPF LSM](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/FAQ.md#checking-and-enabling-support-for-bpf-lsm).

If Linux v5.8+ or BPF LSM is not supported in the given environment, host enforcement will still work out of the box. For protecting containers, new containers will have to be created with special options. See [Support for non orchestrated containers](https://github.com/kubearmor/KubeArmor/wiki/Support-for-non-orchestrated-containers) for the same.

### Resource Requirements

| Node Type          | CPU   | Memory | Disk  |
|--------------------|-------|--------|-------|
| Control plane node | 2vCPU | 4 GB   | 24 GB |
| Worker node        | 2vCPU | 2 GB   | 12 GB |

### Network Requirements

Connectivity between control plane node and worker nodes is a must. They should either be:

- Part of the same private network **(recommended & secure)**
- Control plane has a public IP (not recommended)

Ports required on the control plane VM:

- kubearmor-relay-server: 32768
- shared-informer-agent: 32769
- policy-enforcement-agent: 32770

By default, the network created by onboarding commands reserves the subnet `172.20.32.0/27`. If you want to change it for your environment, you can use the `--network-cidr` flag.

You can check the connectivity between nodes using curl. Upon a successful connection, the message returned by curl will be:

```bash
$ curl <control-plane-addr>:32770
curl: (1) Received HTTP/0.9 when not allowed
```

## Onboarding

Go to the onboarding page (Settings → Manage Cluster → Onboard Now) and give a name to your cluster.

The following agents are installed:

1. **Feeder-service** which collects KubeArmor feeds.
2. **Shared-informer-agent**  authenticates with your VMs and collects information regarding entities like hosts, containers, and namespaces.
3. **Policy-enforcement-agent** authenticates with your VMs and enforces labels and policies.

Select type "VM" on the instructions page. You'll see instructions for downloading accuknox-cli and onboarding your cluster.

### Install knoxctl/accuknox-cli

```bash
curl -sfL https://knoxctl.accuknox.com/install.sh | sudo sh -s -- -b /usr/bin
```

### Onboarding Control Plane

The command may look something like this:

```bash
$ knoxctl onboard vm cp-node \
  --version "v0.2.10" \
  --join-token="843ef458-cecc-4fb9-b5c7-9f1bf7c34567" \
  --spire-host="spire.dev.accuknox.com" \
  --pps-host="pps.dev.accuknox.com" \
  --knox-gateway="knox-gw.dev.accuknox.com:3000"
```

The above command will emit the command to onboard worker nodes. You may also use the `--cp-node-addr` flag to specify the address that other nodes will use to connect with your cluster.

By default, the network created by onboarding commands reserves the subnet `172.20.32.0/27` for the `accuknox-net` Docker network. If you want to change it for your environment, you can use the `--network-cidr` flag.

**Systemd Mode**

By default, if Docker is not found, systemd mode of installation would be used. If you want to explicitly onboard using systemd services, add the `--vm-mode=systemd` flag to the above command.

### Onboarding Worker Nodes

The second command will be for onboarding worker nodes. It may look something like this:

```bash
knoxctl onboard vm node --cp-node-addr=<control-plane-addr>
```

Example:

```bash
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

If you encounter any issues while onboarding, use the commands below to debug:

```bash
docker logs spire-agent -f
docker logs shared-informer-agent -f
docker logs kubearmor-init -f
docker logs kubearmor -f
```

## Deboarding

Deboard the cluster from SaaS first.

To deboard the worker-vm/Node:

```sh
knoxctl deboard vm node
```

To deboard the Control-Plane VM:

```sh
knoxctl deboard vm cp-node
```

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

```sh
sudo rm -rf ~/.accuknox-config
```

For deboarding any worker node, run the below command

```sh
knoxctl deboard vm node
```

After that cleanup the ~/.accuknox-config directory

```sh
rm -rf ~/.accuknox-config
```
