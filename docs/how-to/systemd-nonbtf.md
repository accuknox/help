# SystemD Based Non-BTF Environments

## Compiling system monitor

Some Kernels don't have BTF information available which is required by KubeArmor's system monitor to work out of the box. Thus, the monitor has to be built either on the target machine or on a machine which matches the kernel version of the target machine.

There are two ways to do it, you can chose either one:

### Compile system monitor using Docker (Recommended and reliable)

1. Dependencies:

    - Make sure you have docker installed

    - Make sure you have linux-headers installed for your package

2. Run the kubearmor-init container using the below command which will generate the file `/tmp/system_monitor.bpf.o`.

```bash
sudo docker run --rm -d --name=kubearmor-init --privileged \
-v "/tmp:/opt/kubearmor/BPF:rw" \
-v "/lib/modules:/lib/modules:ro" \
-v "/sys/kernel/security:/sys/kernel/security:ro" \
-v "/sys/kernel/debug:/sys/kernel/debug:ro" \
-v "/media/root/etc/os-release:/media/root/etc/os-release:ro" \
-v "/usr/src:/usr/src" \
kubearmor/kubearmor-init:stable
```

### Compile system monitor directly (Might not work for some versions)

Get the KubeArmor version from [Release v1.4.3 - kubearmor/KubeArmor](https://github.com/kubearmor/KubeArmor/releases/latest)

Fetch and install KubeArmor by running

```bash
VER="1.4.3" # set according to the latest version
curl -sfLO <https://github.com/kubearmor/KubeArmor/releases/download/v${VER}/kubearmor_${VER}_linux-amd64.deb>
sudo apt install ./kubearmor_${VER}_linux-amd64.deb
```

The above will generate the system monitor file at `/opt/kubearmor/BPF/system_monitor.bpf.o`. Copy it to some other path.

## Onboard the node

Once you've compiled the monitor, you can specify it while onboarding the control plane/node.

Install `knoxctl` - the accuknox CLI by running the below command

```bash
curl -sfL <https://knoxctl.accuknox.com/install.sh> | sudo sh -s -- -b /usr/local/bin
```

Onboard your node/control plane by running the respective command with the below additional flags

```bash
sudo knoxctl onboard vm cp-node \
... usual flags
--skip-btf-check=true \
--system-monitor-path=/tmp/system_monitor.bpf.o
```
