For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/system-requirements.md).

Before installing Prisma Cloud, verify that your environment meets the minimum requirements.

For information about when Prisma Cloud adds and drops support for third party software, see our [support lifecycle](https://docs.prismacloud.io/admin-guide/welcome/support-lifecycle#third-party-software) page.

The following sections describe the system requirements in detail.

## Hardware[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#hardware)

Prisma Cloud supports **x86\_64** and **ARM64** architectures. Ensure that your systems meet the following hardware requirements.

RAM

Minimum Without Registry Scanning

Minimum With Registry Scanning

Minimum with WAAS OOB

Less than 1,000 Defenders

1,001 - 10,000 Defenders

More than 10,000

CPU

2 cores

2 cores

4 cores

8 cores

\> 8 cores

RAM

512MB

2 GB

4 GB

8 GB

30 GB

\> 30 GB

Storage

8GB

20GB

100 GB

500 GB

\> 500 GB

Storage per image scanned

Not applicable

1.5 times the size of the largest image to scan times the number of executors

### Defender Resource Requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#defender-resource-requirements)

Each Defender requires 256MB of RAM and 8GB of host storage.

The Defender uses `cgroups` v1 or v2 to cap resource usage at 512MB of RAM and 900 CPU shares where a typical load is ~1-5% CPU and 30-70MB RAM.

For every additional 5,000 Defenders beyond 10,000 Defenders, you need 4 CPUs and 10GB RAM. For example, if there are 20,000 connected Defenders, you require 16 vCPUs, 50GB of RAM, and 500GB SSD of persistent storage.

If Defenders provide registry scanning they require the following resources:

- 2GB of RAM

- 20GB of storage

- 2 CPU cores


For Defenders that are a part of CI integrations such as Jenkins and twistcli, the amount of storage space required depends on the size of the scanned images. You will need disk space that is 1.5 times the size of the largest image to be scanned, per executor. For example, if you have a Jenkins instance with two executors and your largest container image is 500MB, you will need at least 1.5GB of storage space (500MB x 1.5 x 2).

Keep the following caveats in mind when determining Defender storage and memory requirements:

- The Defender stores its data in the `/var` folder. When allocating disk space for Defender, ensure the required space is available in the `/var` folder.

- Defenders are designed to be portable containers that collect data. Any data that must be persisted is sent to the Prisma Cloud Console for storage.

- Defenders do not require persistent storage. Deploying persistent storage for Defenders can corrupt Defender files.

- For Web Application and API Security (WAAS):









  - Inline - Increase the pod memory to 4GB if the Defender is protecting more than 10 workloads.

  - Out-Of-Band - Increase the pod memory to 4GB.


## Virtual Machines (VMs)[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#virtual-machines-vms)

Prisma Cloud has been tested on the following hypervisors:

- VMware for Tanzu Kubernetes Grid Multicloud (TKGM)

- VMware for Tanzu Kubernetes Grid Integrated (TKGI)


## Cloud Platforms[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#cloud-platforms)

Prisma Cloud can run on nearly any cloud Infrastructure as a Service (IaaS) platform.

Prisma Cloud has been tested on the following services:

- Amazon Web Services (AWS)

- Google Cloud Platform

- IBM Cloud

- Microsoft Azure

- Oracle Cloud Infrastructure (OCI)

- Alibaba Cloud: You can deploy Defenders on VMs, hosts running containers, and clusters on Alibaba Cloud using the instructions for the supported host operating systems and orchestrator versions. Specific deployment instructions for Alibaba Cloud are not documented and Cloud discovery is not supported.


## ARM Architecture Requirements[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#arm-architecture-requirements)

The following setups support Prisma Cloud on ARM64 architecture:

- Cloud provider









  - **AWS** Graviton2 processors

  - **GCP** GKE on ARM using the [Tau T2A machine series](https://cloud.google.com/compute/docs/general-purpose-machines#t2a_machines)


- Supported Defenders:









  - Orchestrator Defenders on AWS and GCP

  - Host Defenders including auto-defend on AWS


The `twistcli` is supported on Linux ARM64 instances.

Learn more in the [Supported Operating Systems on ARM64](https://docs.prismacloud.io/admin-guide/install/system-requirements#arm64-os) and [Supported Orchestrators on ARM64](https://docs.prismacloud.io/admin-guide/install/system-requirements#supported-orchestrators-on-arm64) sections.

The Prisma Cloud Console doesn’t support running on ARM64 systems.

## Operating Systems for bare-metal Hosts and Virtual Machines[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#operating-systems-for-bare-metal-hosts-and-virtual-machines)

Prisma Cloud is supported on both x86\_64 and ARM64

### Supported Operating Systems on x86\_64[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#supported-operating-systems-on-x86_64)

Prisma Cloud is supported on the following host operating systems on x86\_64 architecture:

Distro

Version

Kernel

Supported Kubelet

Supported runtime

Notes

Amazon Linux 2

AMI name: amzn2-ami-hvm-2.0.20230727.0-x86\_64-gp2
AMI ID: ami-09748abeb7370d1bc

4.14.322-244.536.amzn2.x86\_64

Amazon Linux 2023

AMI ID:ami-02396cdd13e9a1257

6.1.23-36.46.amzn2023.x86\_64

Azure Linux docker image

20230426

Bottlerocket OS

1.50.0

6.12.53

aws-k8s-1.33

containerd://2.0.6+bottlerocket

Defenders must be installed as privileged on Bottlerocket.
The following features are not available for Bottlerocket:
\- Vulnerability and compliance blocking policies
\- RunC
\- Prevent on containerd runtime
\- Compliance for containerd

Bottlerocket OS

1.50.0

6.12.53

aws-k8s-1.34

containerd://2.1.4+bottlerocket

Defenders must be installed as privileged on Bottlerocket.
The following features are not available for Bottlerocket:
\- Vulnerability and compliance blocking policies
\- RunC
\- Prevent on containerd runtime
\- Compliance for containerd

CentOS

8

CentOS

9

Debian

11

Debian

12

GCOOS

latest

GCOOS is purposefully minimalistic. It doesn’t support installing new packages or writing new bins. Hence, Prisma Cloud’s vulnerability detection on GCOOS only covers Docker and Kubernetes package binary detection.
Runtime prevent capability is supported only for DNS events. Other prevent capabilities are not supported.

Oracle Enterprise Linux (OEL)

7

Oracle Enterprise Linux (OEL)

8

Oracle Enterprise Linux (OEL)

9

Agentless scanning is not supported for OEL 9. Vulnerabilities are matched by architecture, which leads to ARM images showing x86 relevant vulnerabilities and vice versa.

Red Hat Enterprise Linux (RHEL)

8

Red Hat Enterprise Linux (RHEL)

9

Red Hat Enterprise Linux (RHEL)

10

No support in CNNF, no complaince

Red Hat Enterprise Linux CoreOS (RHCOS)

All versions included in OpenShift versions: 4.14, 4.15 and 4.16

Rocky Linux

8.0

Rocky Linux

9.0

Rocky Linux

10.0

SUSE

SLES-12 SP3

OpenSUSE is not tested. Need to be with open ssl above version 1.1 for working WAAS features, runtime cryptominer file creation cause no runtime audit

SUSE

SLES-12 SP5

SUSE

SLES 15 SP1 - SP6

OpenSUSE is not tested.

Talos OS

1.12.4

6.18.9-talos

1.33

containerd 2.1.6

The following features are not available for Talos OS:
\- Scanning of underlying hosts
\- Agentless scanning
\- Vulnerability and compliance blocking policies
\- WAAS defense

Talos OS

1.11.5

6.12.57-talos

1.33

containerd 2.1.5

The following features are not available for Talos OS:
\- Scanning of underlying hosts
\- Agentless scanning
\- Vulnerability and compliance blocking policies
\- WAAS defense

Talos OS

1.9.5

6.12.25-talos

1.32.3

containerd 2.0.5

The following features are not available for Talos OS:
\- Scanning of underlying hosts
\- Agentless scanning
\- Vulnerability and compliance blocking policies
\- WAAS defense

Talos OS

1.9.4

6.12.13-talos

1.29.5

containerd 2.0.2

The following features are not available for Talos OS:
\- Scanning of underlying hosts
\- Agentless scanning
\- Vulnerability and compliance blocking policies
\- WAAS defense

Ubuntu

24.04 LTS

Ubuntu

22.04 LTS

Ubuntu

20.04 LTS

VMWare Photon OS

4.0

The following use features are currently not supported in Photon 4.0:
\- SSHD application in host runtime events and empty SSH events on Host observations
\- Vulnerabilities in Layers view

VMWare Photon OS

5.0

The following use features are currently not supported in Photon 4.0:
\- SSHD application in host runtime events and empty SSH events on Host observations
\- Vulnerabilities in Layers view

Windows

Server 2016

Server 2016 Long-Term Servicing Channel (LTSC) support includes only following features:
\- Vulnerabilty scanning
\- Compliance scanning
\- CNNS defense for container
\- WAAS defense for hosts

Windows

Server 2019

Server 2019 Long-Term Servicing Channel (LTSC) support includes only following features:
\- Vulnerabilty scanning
\- Compliance scanning
\- CNNS defense for container
\- WAAS defense for hosts
\- Runtime defense for container

Windows

Server 2022

Server 2022 Long-Term Servicing Channel (LTSC) support includes only following features:
\- Vulnerabilty scanning
\- Compliance scanning
\- CNNS defense for container
\- WAAS defense for hosts
\- Runtime defense for container

Windows

Server 2025

Server 2025 Long-Term Servicing Channel (LTSC) support includes only following features:
\- Vulnerabilty scanning
\- Compliance scanning
\- CNNS defense for container
\- WAAS defense for hosts
\- Runtime defense for container

Panos

11.0.4-h1

Agentless scanning host only

Panos

11.1.4

Agentless scanning host only

Panos

11.2.3-h3

Agentless scanning host only

Talos OS

1.9.1

6.12.6-talos

1.29.5

containerd 2.0.1

The following features are not available for Talos OS:
\- Vulnerability and compliance blocking policies
\- Agentless scanning

Ubuntu

24.04 LTS

Ubuntu

22.04 LTS

Ubuntu

20.04 LTS

almalinux-8

8.1

4.18.0-553.47.1.el8\_10.x86\_64

Correct Vulnerabilities detected only

almalinux-9

9.5

5.14.0-503.35.1.el9\_5.x86\_64

Correct Vulnerabilities detected only

### Supported Operating Systems on ARM64[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#supported-operating-systems-on-arm64)

Prisma Cloud supports host Defenders on the following host operating systems on ARM64 architecture in AWS.

Distro

Version

Kernel

Supported Kubelet

Supported runtime

Notes

Amazon Linux 2

AMI Image: amzn-ami-hvm-2018.03.0.20220315.0-x86\_64-gp2
AMI ID: ami-0f7691f59fd7c47af

5.10.96-90.460.amzn2.aarch64

graviton2

Debian

11

graviton3

Redhat Enterprise Linux (RHEL)

8

graviton4

Redhat Enterprise Linux (RHEL)

9

graviton2

Redhat Enterprise Linux (RHEL)

10

graviton2

Ubuntu

20

graviton2

Ubuntu

22

graviton2

Ubuntu

24

graviton2

Oracle Enterprise Linux (OEL)

8

Oracle Enterprise Linux (OEL)

9

## Kernel Capabilities[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#kernel-capabilities)

Prisma Cloud Defender requires the following kernel capabilities. Refer to the the Linux capabilities [man page](https://man7.org/linux/man-pages/man7/capabilities.7.html) for more details on each capability.

- CAP\_NET\_ADMIN

- CAP\_NET\_RAW

- \`CAP\_SYS\_ADMIN

- CAP\_SYS\_PTRACE

- CAP\_SYS\_CHROOT

- CAP\_MKNOD

- CAP\_SETFCAP

- CAP\_IPC\_LOCK

- The Prisma Cloud App-Embedded Defender requires CAP\_SYS\_PTRACE only.

- Embedding defender in an application that is running in a non-privileged mode and that invokes another application/process with sudo, may cause the defender process to panic.


Embedding Defender in an application that is running in a non-privileged mode and that invokes another application/process with sudo, may cause the defender process to panic

When running on a Docker host, Prisma Cloud Defender uses the following files/folder on the host:

- /var/run/docker.sock — Required for accessing Docker runtime.

- /var/lib/twistlock — Required for storing Prisma Cloud data.

- /dev/log — Required for writing to syslog.


## Docker Engine[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#docker-engine)

Prisma Cloud supports only the versions of the Docker Engine supported by Docker itself. Prisma Cloud supports only the following official mainstream Docker releases and later versions.

Edition

Version

Community Edition (CE)

24.0.7

Community Edition (CE)

25.0.3

Community Edition (CE)

26.0.0

Enterprise Edition (EE)

19.03.4

Enterprise Edition (EE)

19.03.8

The following storage drivers are supported: \* `overlay2` \\* `overlay` \\* `devicemapper`

For more information, review Docker’s guide to [select a storage driver](https://docs.docker.com/storage/storagedriver/select-storage-driver).

The versions of Docker Engine listed apply to versions you independently install on a host. The versions shipped as a part of an orchestrator, such as Red Hat OpenShift, might defer. Prisma Cloud supports the version of Docker Engine that ships with any Prisma Cloud-supported version of the orchestrator.

## Container Runtimes[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#container-runtimes)

Prisma Cloud supports several container runtimes depending on the orchestrator. Supported versions are listed in the [orchestration](https://docs.prismacloud.io/admin-guide/install/system-requirements#orchestrators) section

## Podman[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#podman)

Podman is a daemon-less container engine for developing, managing, and running OCI containers on Linux.

The twistcli tool uses the pre-installed Podman binary to scan CRI images. The supported Podman versions are 1.6.4, 3.4.2, and 4.0.2.

Prisma Cloud also supports deploying Defenders on Podman containers. Podman version 4.9 is the supported version for this feature.

## Helm[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#helm)

Helm is a package manager for Kubernetes that allows developers and operators to package, configure, and deploy applications and services onto Kubernetes clusters.

Helm v3.10, v3.10.3, and 3.11 are supported.

## Orchestrators[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#orchestrators)

Prisma Cloud is supported on the following orchestrators. We support the following versions of official mainline vendor/project releases.

### Supported Orchestrators on x86\_64[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#supported-orchestrators-on-x86_64)

Orchestrator

Version

Operating System

Image

Runtime

Kernel

Tested in

Notes

Azure Kubernetes Service (AKS)

v1-29-2

Linux

-

containerd://1.7.7-1

34

Azure Kubernetes Service (AKS)

v1.30.4

Linux

-

containerd://1.7.20-1

34

Azure Kubernetes Service (AKS)

v1.31.2

Linux

-

containerd://1.7.25-1

34

Azure Kubernetes Service (AKS)

v1.29.13

Linux (Mariner)

-

containerd://1.6.26

34

Azure Kubernetes Service (AKS)

v1.30.4

Linux

-

containerd://1.7.20-1

34.01

Azure Kubernetes Service (AKS)

v1.31.2

Linux

-

containerd://1.7.27-1

34.01

Azure Kubernetes Service (AKS)

v1.32.3

Linux

-

containerd://1.7.27-1

34.01

Azure Kubernetes Service (AKS)

v1.29.15

Linux (Mariner)

-

containerd://1.6.26

34.01

Azure Kubernetes Service (AKS)

v1.30.4

Linux

-

containerd://1.7.20-1

34.02

Azure Kubernetes Service (AKS)

v1.31.2

Linux

-

containerd://1.7.27-1

34.02

Azure Kubernetes Service (AKS)

v1.32.3

Linux

-

containerd://1.7.27-1

34.02

Azure Kubernetes Service (AKS)

v1.33.0

Linux

-

containerd://2.0.0

34.02

Azure Kubernetes Service (AKS)

v1.29.13

Linux (Mariner)

-

containerd://1.6.26

34.02

Azure Kubernetes Service (AKS)

v1.32.7

Linux

-

containerd://1.7.28-1

34.03

Azure Kubernetes Service (AKS)

v1.33.3

Linux

-

containerd://1.7.28-1

34.03

Azure Kubernetes Service (AKS)

v1.34.0

Linux

-

containerd://1.7.28-1

34.03

Azure Kubernetes Service (AKS)

v1.30.14

Linux (Mariner)

-

containerd://1.6.26

34.03

Azure Kubernetes Service (AKS)

v1.32.7

Linux

-

containerd://1.7.28-1

34.04

Azure Kubernetes Service (AKS)

v1.33.3

Linux

-

containerd://1.7.28-1

34.04

Azure Kubernetes Service (AKS)

v1.34.0

Linux

-

containerd://1.7.28-1

34.04

Azure Kubernetes Service (AKS)

v1.30.14

Linux (Mariner)

-

containerd://1.6.26

34.04

Azure Kubernetes Service (AKS)

v1.33.3

Linux

-

containerd://1.7.28-1

34.05

Azure Kubernetes Service (AKS)

v1.34.0

Linux

-

containerd://1.7.28-1

34.05

Azure Kubernetes Service (AKS)

v1.35.0

Linux

-

containerd://2.3.3-2

34.05

Elastic Container Service (ECS)

1.87.1

Linux

al2023-ami-ecs-hvm-2023.0.20241031-kernel-6.1-x86\_64

Docker version: 25.0.6

-

34

Elastic Kubernetes Service (EKS)

v1.29.0-eks-5e0fdde

Linux

-

containerd://1.7.11

34

Elastic Kubernetes Service (EKS)

v1.30.0-eks-036c24b

Linux

-

containerd://1.7.11

34

Elastic Kubernetes Service (EKS)

v1.31.0-eks-a737599

Linux

-

containerd://1.7.22

34

Elastic Kubernetes Service (EKS)

v1.32.1-eks-5d632ec

Linux

-

containerd://1.7.25

34

Elastic Kubernetes Service (EKS)

v1.30.0-eks-036c24b

Linux

-

containerd://1.7.11

34.01

Elastic Kubernetes Service (EKS)

v1.31.0-eks-a737599

Linux

-

containerd://1.7.22

34.01

Elastic Kubernetes Service (EKS)

v1.32.1-eks-5d632ec

Linux

-

containerd://1.7.25

34.01

Elastic Kubernetes Service (EKS)

v1.31.0-eks-a737599

Linux

-

containerd://1.7.22

34.02

Elastic Kubernetes Service (EKS)

v1.32.1-eks-5d632ec

Linux

-

containerd://1.7.25

34.02

Elastic Kubernetes Service (EKS)

v1.33.0-eks-802817d

Linux

-

containerd://1.7.27

34.02

Elastic Kubernetes Service (EKS)

v1.31.13-eks-113cf36

Linux

-

containerd://1.7.27

34.03

Elastic Kubernetes Service (EKS)

v1.32.9-eks-113cf36

Linux

-

containerd://1.7.27

34.03

Elastic Kubernetes Service (EKS)

v1.33.0-eks-802817d

Linux

-

containerd://1.7.27

34.03

Elastic Kubernetes Service (EKS)

v1.34.1-eks-113cf36

Linux

-

containerd://2.1.4

34.03

Elastic Kubernetes Service (EKS)

v1.32.9-eks-113cf36

Linux

-

containerd://1.7.27

34.04

Elastic Kubernetes Service (EKS)

v1.33.0-eks-802817d

Linux

-

containerd://1.7.27

34.04

Elastic Kubernetes Service (EKS)

v1.34.1-eks-113cf36

Linux

-

containerd://2.1.4

34.04

Elastic Kubernetes Service (EKS)

v1.35.0-33+37970203ae1a44

Linux

-

containerd://2.1.5

34.04

Elastic Kubernetes Service (EKS)

1.36.2-20260714

Linux

-

containerd://2.2.4

34.05

Elastic Kubernetes Service (EKS) Bottlerocket

v1.31.1-eks-1b3e656

Linux

-

containerd://1.7.22+bottlerocket

34

Elastic Kubernetes Service (EKS) Bottlerocket

v1.32.0-eks-2e66e76

Linux

-

containerd://1.7.24+bottlerocket

34

Elastic Kubernetes Service (EKS) Bottlerocket

v1.31.1-eks-1b3e656

Linux

-

containerd://1.7.22+bottlerocket

34.01

Elastic Kubernetes Service (EKS) Bottlerocket

v1.32.0-eks-2e66e76

Linux

-

containerd://1.7.24+bottlerocket

34.01

Elastic Kubernetes Service (EKS) Bottlerocket

v1.32.0-eks-2e66e76

Linux

-

containerd://1.7.24+bottlerocket

34.02

Elastic Kubernetes Service (EKS) Bottlerocket

v1.33.1-eks-b9364f6

Linux

-

containerd://2.0.5+bottlerocket

34.02

Elastic Kubernetes Service (EKS) Bottlerocket

v1.33.4-eks-e386d34

Linux

-

containerd://2.0.6+bottlerocket

34.03

Elastic Kubernetes Service (EKS) Bottlerocket

v1.34.0-eks-642f211

Linux

-

containerd://2.1.4+bottlerocket

34.03

Elastic Kubernetes Service (EKS) Bottlerocket

v1.34.0-eks-642f211

Linux

-

containerd://2.1.4+bottlerocket

34.04

Elastic Kubernetes Service (EKS) Bottlerocket

v1.35.0-eks-ac2d5a0

Linux

-

containerd://2.1.6+bottlerocket

34.04

Google Kubernetes Engine (GKE)

v1.29.10-gke.1227000

Linux

-

containerd://1.7.23

34

Google Kubernetes Engine (GKE)

v1.30.6-gke.1125000

Linux

-

containerd://1.7.23

34

Google Kubernetes Engine (GKE)

v1.31.2-gke.1518000

Linux

-

containerd://1.7.23

34

Google Kubernetes Engine (GKE)

v1.32.1-gke.1489001

Linux

-

containerd://1.7.24

34

Google Kubernetes Engine (GKE)

v1.30.6-gke.1125000

Linux

-

containerd://1.7.23

34.01

Google Kubernetes Engine (GKE)

v1.31.2-gke.1518000

Linux

-

containerd://1.7.23

34.01

Google Kubernetes Engine (GKE)

v1.32.1-gke.1489001

Linux

-

containerd://1.7.24

34.01

Google Kubernetes Engine (GKE)

v1.31.2-gke.1518000

Linux

-

containerd://1.7.23

34.02

Google Kubernetes Engine (GKE)

v1.32.1-gke.1489001

Linux

-

containerd://1.7.24

34.02

Google Kubernetes Engine (GKE)

1.33.2-gke.1240000

Linux

-

containerd://2.0.4

34.02

Google Kubernetes Engine (GKE)

1.31.13-gke.1023000

Linux

-

containerd://1.7.23

34.03

Google Kubernetes Engine (GKE)

v1.32.9-gke.1130000

Linux

-

containerd://1.7.28

34.03

Google Kubernetes Engine (GKE)

v1.33.5-gke.1162000

Linux

-

containerd://2.0.6

34.03

Google Kubernetes Engine (GKE)

v1.32.11-gke.1211000

Linux

-

containerd://1.7.29

34.04

Google Kubernetes Engine (GKE)

v1.33.5-gke.2326000

Linux

-

containerd://2.0.6

34.04

Google Kubernetes Engine (GKE)

v1.34.3-gke.1318000

Linux

-

containerd://2.1.5

34.04

Google Kubernetes Engine (GKE)

1.35.6-gke.1641000

Linux

-

containerd://2.1.7

34.05

Google Kubernetes Engine (GKE)

1.36.2-gke.2064000

Linux

-

containerd://2.2.3

34.05

Google Kubernetes Engine (GKE) autopilot

v1.31.6-gke.1020000

Linux

-

containerd://1.7.24

34

Google Kubernetes Engine (GKE) autopilot

v1.32.2-gke.1297002

Linux

-

containerd://1.7.24

34.01

Google Kubernetes Engine (GKE) autopilot

v1.33.2-gke.1240000

Linux

-

containerd://2.0.4

34.02

Google Kubernetes Engine (GKE) autopilot

v1.34.1-gke.1829001

Linux

-

containerd://2.1.3

34.03

Google Kubernetes Engine (GKE) autopilot

1.35.0-gke.2745003

Linux

-

containerd://2.1.5

34.04

Oracle Kubernetes Engine (OKE)

v1.30.1

Linux

-

cri-o://1.30.0-296.el8

34

Oracle Kubernetes Engine (OKE)

v1.32.1

Linux

-

cri-o://1.32.2-4.aa4f43777b7.el8

34.01

Oracle Kubernetes Engine (OKE)

v1.34.1

Linux

-

cri-o://1.34.0-66.1c4616d3c11.el8

34.03

Oracle Kubernetes Engine (OKE)

v1.34.2

Linux

-

cri-o://1.34.0-66.1c4616d3c11.el8

34.04

Kubernetes (k8s)

v1.29.5

Linux

-

containerd://1.6.32

34

Kubernetes (k8s)

v1.29.5

Linux

-

cri-o://1.29.5

34

Kubernetes (k8s)

v1.30.1

Linux

-

containerd://1.6.31

34

Kubernetes (k8s)

v1.30.1

Linux

-

cri-o://1.30.1

34

Kubernetes (k8s)

v1.31.1

Linux

-

containerd://1.7.22

34

Kubernetes (k8s)

v1.31.1

Linux

-

cri-o://1.31.0

34

Kubernetes (k8s)

v1.32.0

Linux

-

containerd://1.7.24

34

Kubernetes (k8s)

v1.32.0

Linux

-

cri-o://1.32.0

34

Kubernetes (k8s)

v1.30.1

Linux

-

containerd://1.7.25

34.01

Kubernetes (k8s)

v1.30.1

Linux

-

cri-o://1.30.1

34.01

Kubernetes (k8s)

v1.31.6

Linux

-

containerd://1.7.25

34.01

Kubernetes (k8s)

v1.31.1

Linux

-

cri-o://1.31.0

34.01

Kubernetes (k8s)

v1.32.3

Linux

-

containerd://1.7.27

34.01

Kubernetes (k8s)

v1.32.0

Linux

-

cri-o://1.32.0

34.01

Kubernetes (k8s)

v1.33.0

Linux

-

containerd://1.7.27

34.01

Kubernetes (k8s)

v1.30.1

Linux

-

containerd://1.7.25

34.02

Kubernetes (k8s)

v1.30.1

Linux

-

cri-o://1.30.1

34.02

Kubernetes (k8s)

v1.31.6

Linux

-

containerd://1.7.25

34.02

Kubernetes (k8s)

v1.31.1

Linux

-

cri-o://1.31.0

34.02

Kubernetes (k8s)

v1.32.3

Linux

-

containerd://1.7.27

34.02

Kubernetes (k8s)

v1.32.0

Linux

-

cri-o://1.32.0

34.02

Kubernetes (k8s)

v1.33.0

Linux

-

containerd://1.7.27

34.02

Kubernetes (k8s)

v1.33.1

Linux

-

cri-o://1.33.0

34.02

Kubernetes (k8s)

v1.32.9

Linux

-

containerd://1.7.28

34.03

Kubernetes (k8s)

v1.32.9

Linux

-

cri-o://1.32.9

34.03

Kubernetes (k8s)

v1.33.0

Linux

-

containerd://1.7.27

34.03

Kubernetes (k8s)

v1.33.1

Linux

-

cri-o://1.33.0

34.03

Kubernetes (k8s)

v1.34.1

Linux

-

containerd://1.7.28

34.03

Kubernetes (k8s)

v1.34.1

Linux

-

cri-o://1.34.1

34.03

Kubernetes (k8s)

v1.33.7

Linux

-

containerd://2.2.1

34.04

Kubernetes (k8s)

v1.33.7

Linux

-

cri-o://1.33.9

34.04

Kubernetes (k8s)

v1.34.1

Linux

-

containerd://1.7.28

34.04

Kubernetes (k8s)

v1.34.1

Linux

-

cri-o://1.34.1

34.04

Kubernetes (k8s)

v1.35.0

Linux

-

containerd://2.2.1

34.04

Kubernetes (k8s)

v1.35.1

Linux

-

cri-o://1.35.0

34.04

Kubernetes (k8s)

v1.34.1

Linux

-

containerd://1.7.28

34.05

Kubernetes (k8s)

v1.34.1

Linux

-

cri-o://1.34.1

34.05

Kubernetes (k8s)

v1.35.0

Linux

-

containerd://2.2.1

34.05

Kubernetes (k8s)

v1.35.1

Linux

-

cri-o://1.35.0

34.05

Kubernetes (k8s)

v1.36.3

Linux

-

containerd://2.2.6

34.05

Kubernetes (k8s)

v1.36.3

Linux

-

cri-o://1.36.2

34.05

Lightweight Kubernetes (k3s)

v1.31.5+k3s1

Linux

-

containerd://1.7.23-k3s1

34

Lightweight Kubernetes (k3s)

v1.32.3+k3s1

Linux

-

containerd://2.0.4-k3s2

34.01

Lightweight Kubernetes (k3s)

v1.33.2+k3s1

Linux

-

containerd://2.0.5-k3s1

34.02

Lightweight Kubernetes (k3s)

v1.33.5+k3s1

Linux

-

containerd://2.1.4-k3s1

34.03

Lightweight Kubernetes (k3s)

v1.34.3+k3s1

Linux

-

containerd://2.1.5-k3s1

34.04

Lightweight Kubernetes (k3s)

v1.36.2+k3s1

Linux

-

containerd://2.3.2-k3s2

34.05

mirantis

v1.27.10-mirantis-1

Linux

-

docker://26.0.1

34

mirantis

v1.27.10-mirantis-1

Linux

-

docker://26.0.1

34.01

mirantis

v1.27.10-mirantis-1

Linux

-

docker://26.0.1

34.02

mirantis

v1.27.10-mirantis-1

Linux

-

docker://26.0.1

34.03

mirantis

v1.31.12-mirantis-2

Linux

-

docker://25.0.14 (MCR)

34.03

mirantis

v1.31.12-mirantis-2

Linux

-

docker://25.0.14 (MCR)

34.04

mirantis

v1.31.12-mirantis-2

Linux

-

docker://25.0.14 (MCR)

34.05

mirantis

v1.34.3-mirantis-1

Linux

-

docker://25.0.14 (MCR)

34.05

mirantis

v1.34.9-mirantis-2

Linux

-

docker://25.0.14 (MCR)

34.05

OpenShift

4.15

-

-

cri-o://1.28.3.14.rhaos4.15.git33aabd8.el9

34

OpenShift

4.16

-

-

cri-o://1.29.5.5.rhaos4.16.git7032128.el9

34

OpenShift

4.17

-

-

cri-o://1.30.5.7.rhaos4.17.git2e89940.el9

34

OpenShift

4.12

-

-

cri-o://1.25.5.30.rhaos4.12.git53dc492.el8

34.01

OpenShift

4.13

-

-

cri-o://1.26.5.26.rhaos4.13.giteb3d487.el9

34.01

OpenShift

4.14

-

-

cri-o://1.27.8.15.rhaos4.14.gite1422c1.el9

34.01

OpenShift

4.15

-

-

cri-o://1.28.3.14.rhaos4.15.git33aabd8.el9

34.01

OpenShift

4.16

-

-

cri-o://1.29.5.5.rhaos4.16.git7032128.el9

34.01

OpenShift

4.17

-

-

cri-o://1.30.5.7.rhaos4.17.git2e89940.el9

34.01

OpenShift

4.12

-

-

cri-o://1.25.5.30.rhaos4.12.git53dc492.el8

34.02

OpenShift

4.13

-

-

cri-o://1.26.5.26.rhaos4.13.giteb3d487.el9

34.02

OpenShift

4.14

-

-

cri-o://1.27.8.15.rhaos4.14.gite1422c1.el9

34.02

OpenShift

4.15

-

-

cri-o://1.28.3.14.rhaos4.15.git33aabd8.el9

34.02

OpenShift

4.16

-

-

cri-o://1.29.5.5.rhaos4.16.git7032128.el9

34.02

OpenShift

4.17

-

-

cri-o://1.30.5.7.rhaos4.17.git2e89940.el9

34.02

OpenShift

4.12

-

-

cri-o://1.25.5.30.rhaos4.12.git53dc492.el8

34.03

OpenShift

4.13

-

-

cri-o://1.26.5.26.rhaos4.13.giteb3d487.el9

34.03

OpenShift

4.14

-

-

cri-o://1.27.8.15.rhaos4.14.gite1422c1.el9

34.03

OpenShift

4.15

-

-

cri-o://1.28.3.14.rhaos4.15.git33aabd8.el9

34.03

OpenShift

4.16

-

-

cri-o://1.29.5.5.rhaos4.16.git7032128.el9

34.03

OpenShift

4.17

-

-

cri-o://1.30.5.7.rhaos4.17.git2e89940.el9

34.03

OpenShift

4.18

-

-

cri-o://1.31.9-3.rhaos4.18.git0f69ddd.el9

34.03

OpenShift

4.19

-

-

cri-o://1.32.9-2.rhaos4.19.git2de10fd.el9

34.03

OpenShift

4.20

-

-

cri-o://1.33.5-3.rhaos4.20.gitd0ea985.el9

34.03

OpenShift

4.12

-

-

cri-o://1.25.5.30.rhaos4.12.git53dc492.el8

34.04

OpenShift

4.13

-

-

cri-o://1.26.5.26.rhaos4.13.giteb3d487.el9

34.04

OpenShift

4.14

-

-

cri-o://1.27.8.15.rhaos4.14.gite1422c1.el9

34.04

OpenShift

4.15

-

-

cri-o://1.28.3.14.rhaos4.15.git33aabd8.el9

34.04

OpenShift

4.16

-

-

cri-o://1.29.5.5.rhaos4.16.git7032128.el9

34.04

OpenShift

4.17

-

-

cri-o://1.30.5.7.rhaos4.17.git2e89940.el9

34.04

OpenShift

4.18

-

-

cri-o://1.31.9-3.rhaos4.18.git0f69ddd.el9

34.04

OpenShift

4.19

-

-

cri-o://1.32.9-2.rhaos4.19.git2de10fd.el9

34.04

OpenShift

4.20

-

-

cri-o://1.33.5-3.rhaos4.20.gitd0ea985.el9

34.04

OpenShift

4.21

-

-

cri-o://1.34.3-2.rhaos4.21.gitd80d17d.el9

34.04

OpenShift

4.17

-

-

cri-o://1.30.5.7.rhaos4.17.git2e89940.el9

34.05

OpenShift

4.18

-

-

cri-o://1.31.9-3.rhaos4.18.git0f69ddd.el9

34.05

OpenShift

4.19

-

-

cri-o://1.32.9-2.rhaos4.19.git2de10fd.el9

34.05

OpenShift

4.20

-

-

cri-o://1.33.5-3.rhaos4.20.gitd0ea985.el9

34.05

OpenShift

4.21

-

-

cri-o://1.34.3-2.rhaos4.21.gitd80d17d.el9

34.05

OpenShift

4.22

-

-

cri-o://1.35.6-4.rhaos4.22.git41f610b.el9

34.05

RKE

v1.31.5

Linux

-

docker://26.0.0

34

RKE

v1.32.3

Linux

-

docker://26.0.0

34.01

RKE

v1.32.5

Linux

-

docker://26.0.0

34.02

RKE2

v1.32.1+rke2r1

Linux

-

containerd://1.7.23-k3s2

34

RKE2

v1.32.1+rke2r1

Linux

-

containerd://1.7.23-k3s2

34.01

RKE2

v1.33.2+rke2r1

Linux

-

containerd://2.0.5-k3s1

34.02

RKE2

v1.34.1+rke2r1

Linux

-

containerd://2.1.4-k3s2

34.03

RKE2

v1.34.1+rke2r1

Linux

-

containerd://2.1.4-k3s2

34.04

RKE2

v1.35.1+rke2r1

Linux

-

containerd://2.1.5-k3s1

34.05

RKE2

v1.36.2+rke2r1

Linux

-

containerd://2.3.2-k3s2

34.05

TalOS

v1.33.0

Talos

Talos (v1.13.1)

containerd://2.2.3

6.18.29-talos

34.05

TalOS

v1.33.0

Talos

Talos (v1.12.4)

containerd://2.1.6

6.18.9-talos

34.04

TalOS

v1.33.0

Talos

Talos (v1.11.5)

containerd://2.1.5

6.12.57-talos

34.03

TalOS

v1.33.0

Talos

Talos (v1.10.1)

containerd://2.0.5

6.12.25-talos

34.02

TalOS

v1.32.3

Talos

Talos (v1.10.1)

containerd://2.0.5

6.12.25-talos

34.01

TalOS

v1.32.3

Talos

Talos (v1.9.5)

containerd://2.0.5

6.12.25-talos

34.01

TalOS

v1.29.5

Talos

Talos (v1.9.4)

containerd://2.0.2

6.12.13-talos

34

VMware Tanzu Application Service (TAS)

6

Linux

-

-

-

34

Agentless scan not supported

VMware Tanzu Application Service (TAS)

5

Linux

-

-

-

34

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Linux

-

-

-

34

Agentless scan not supported

VMware Tanzu Application Service (TAS)

6

Windows

-

-

-

34

Agentless scan not supported

VMware Tanzu Application Service (TAS)

5

Windows

-

-

-

34

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Windows

-

-

-

34

Agentless scan not supported

VMware Tanzu Application Service (TAS)

6

Linux

-

-

-

34.01

Agentless scan not supported

VMware Tanzu Application Service (TAS)

5

Linux

-

-

-

34.01

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Linux

-

-

-

34.01

Agentless scan not supported

VMware Tanzu Application Service (TAS)

6

Windows

-

-

-

34.01

Agentless scan not supported

VMware Tanzu Application Service (TAS)

5

Windows

-

-

-

34.01

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Windows

-

-

-

34.01

Agentless scan not supported

VMware Tanzu Application Service (TAS)

6

Linux

-

-

-

34.02

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Linux

-

-

-

34.02

Agentless scan not supported

VMware Tanzu Application Service (TAS)

6

Windows

-

-

-

34.02

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Windows

-

-

-

34.02

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Windows

-

-

-

34.03

Agentless scan not supported

VMware Tanzu Application Service (TAS)

6

Windows

-

-

-

34.04

Agentless scan not supported

VMware Tanzu Application Service (TAS)

10

Windows

-

-

-

34.04

Agentless scan not supported

VMware Tanzu Application Service (TAS)

6.0.29+LTS-T

Linux

-

-

-

34.05

VMware Tanzu Application Service (TAS)

10.2.12+LTS-T

Linux

-

-

-

34.05

VMware Tanzu Application Service (TAS)

6.0.29+LTS-T

Windows

-

-

-

34.05

VMware Tanzu Application Service (TAS)

10.2.12+LTS-T

Windows

-

-

-

34.05

vSphere Kubernetes Service (VKS)

v1.30.7+vmware.1

Ubuntu 22.04.1 LTS

-

containerd://1.7.23+vmware.2

5.15.0-133-generic

34

vSphere Kubernetes Service (VKS)

v1.30.7+vmware.1

Ubuntu 22.04.1 LTS

-

containerd://1.7.23+vmware.2

5.15.0-133-generic

34.01

vSphere Kubernetes Service (VKS)

v1.30.7+vmware.1

Ubuntu 22.04.1 LTS

-

containerd://1.7.23+vmware.2

5.15.0-133-generic

34.02

vSphere Kubernetes Service (VKS)

v1.30.7+vmware.1

Ubuntu 22.04.1 LTS

-

containerd://1.7.23+vmware.2

5.15.0-133-generic

34.03

vSphere Kubernetes Service (VKS)

v1.30.7+vmware.1

Ubuntu 22.04.1 LTS

-

containerd://1.7.23+vmware.2

5.15.0-133-generic

34.04

vSphere Kubernetes Service (VKS)

v1.30.7

Ubuntu 22.04.1 LTS

-

containerd://1.7.23

5.15.0-133-generic

34.05

### Supported Orchestrators on ARM64[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#supported-orchestrators-on-arm64)

Prisma Cloud supports the official releases of the following orchestrators for the ARM64 architecture.

Orchestrator

Version

Operating System

Image

Runtime

Kernel

Tested in

notes

Elastic Container Service (ECS)

1.87.1

-

al2023-ami-ecs-hvm-2023.0.20241031-kernel-6.1-arm64

Docker version: 25.0.6

-

34

Elastic Kubernetes Service (EKS)

v1.31.2-eks-94953ac.arm

-

-

containerd://1.7.23

34

Elastic Kubernetes Service (EKS)

v1.32.1-eks-5d632ec.arm

-

-

containerd://1.7.25

34

Elastic Kubernetes Service (EKS)

v1.31.2-eks-94953ac.arm

-

-

containerd://1.7.23

34.01

Elastic Kubernetes Service (EKS)

v1.32.1-eks-5d632ec.arm

-

-

containerd://1.7.25

34.01

Elastic Kubernetes Service (EKS)

v1.32.1-eks-5d632ec.arm

-

-

containerd://1.7.25

34.02

Elastic Kubernetes Service (EKS)

v1.33.0-eks-802817d.arm

-

-

containerd://1.7.27

34.02

Elastic Kubernetes Service (EKS)

v1.33.0-eks-802817d

-

-

containerd://1.7.27

34.03

Elastic Kubernetes Service (EKS)

v1.34.1-eks-113cf36

-

-

containerd://2.1.4

34.03

Elastic Kubernetes Service (EKS)

v1.34.1-eks-113cf36

-

-

containerd://2.1.4

34.04

Elastic Kubernetes Service (EKS)

v1.35.0-33+37970203ae1a44

-

-

containerd://2.1.5

34.04

Elastic Kubernetes Service (EKS)

1.36.2-20260714

-

-

containerd://2.2.4

34.05

Oracle Kubernetes Engine (OKE)

V.1.30.1

-

-

cri-o://1.30.0-296.el8

34

Oracle Kubernetes Engine (OKE)

V.1.32.1

-

-

cri-o://1.32.2-4.aa4f43777b7.el8

34.01

Oracle Kubernetes Engine (OKE)

v1.34.1

-

-

cri-o://1.34.0-66.1c4616d3c11.el8

34.03

Oracle Kubernetes Engine (OKE)

v1.34.2

-

-

cri-o://1.34.0-66.1c4616d3c11.el8

34.04

Google Kubernetes Engine (GKE)

1.32.1-gke.1489001

-

containerd://1.7.24

34

Google Kubernetes Engine (GKE)

1.32.1-gke.1489001

-

containerd://1.7.24

34.01

Google Kubernetes Engine (GKE)

v1.33.2-gke.1240000

-

containerd://2.0.4

34.02

Google Kubernetes Engine (GKE)

v1.33.2-gke.1240000

-

containerd://2.0.4

34.03

Google Kubernetes Engine (GKE)

v1.34.3-gke.1318000

-

containerd://2.1.5

34.04

Google Kubernetes Engine (GKE) autopilot on ARM

v1.30.9-gke.1046000

-

containerd://1.7.24

34

Google Kubernetes Engine (GKE) autopilot on ARM

v1.31.6-gke.1064001

-

containerd://1.7.24

34.01

Google Kubernetes Engine (GKE) autopilot on ARM

v1.32.4-gke.1415000

-

containerd://1.7.27

34.02

Google Kubernetes Engine (GKE) autopilot on ARM

v1.33.5-gke.1162000

-

containerd://2.0.6

34.03

Google Kubernetes Engine (GKE) autopilot on ARM

v1.33.5-gke.2228001

-

containerd://2.0.6

34.04

Azure Kubernetes Service (AKS)

v1.33.0

Linux

-

containerd://2.0.0

34.02

Azure Kubernetes Service (AKS)

v1.34.0

Linux

-

containerd://2.0.0

34.03

Azure Kubernetes Service (AKS)

v1.34.0

Linux

-

containerd://2.0.0

34.04

Azure Kubernetes Service (AKS)

v1.33.0

Linux

-

containerd://2.0.0

34.05

## Istio[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#istio)

Prisma Cloud supports Istio 1.16.1.

Any infrastructure containers with `istio` or `proxy` in the name don’t appear in the results shown in the Prisma Cloud console.

## Jenkins[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#jenkins)

Prisma Cloud was tested with Jenkins 2.346.3 and the 2.361.4 container version.

The Prisma Cloud Jenkins plugin supports Jenkins LTS releases greater than 2.319.1. For any given release of Prisma Cloud, the plugin supports those Jenkins LTS releases supported by the Jenkins project at the time of the Prisma Cloud release.

The Jenkins plugin is not supported on ARM64 architecture.

## Image Base Layers[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#image-base-layers)

Prisma Cloud can protect containers built on nearly any base layer operating system. Comprehensive Common Vulnerabilities and Exposures (CVE) data is provided for the following base layers for all versions except EOL versions:

- Alpine

- [Amazon Linux container image](http://docs.aws.amazon.com/AmazonECR/latest/userguide/amazon_linux_container_image.html)

- Amazon Linux 2

- BusyBox

- CentOS

- Debian

- Oracle Linux

- Red Hat Enterprise Linux

- SUSE

- Ubuntu (LTS releases only)

- Windows Server

- Chainguard Wolfi Linux


If a CVE doesn’t have an architecture identifier, the CVE is related to all architectures.

## Serverless Runtimes[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#serverless-runtimes)

Prisma Cloud offers multiple features to help you secure your serverless runtimes on AWS, Azure, and GCP. The following sections show the supported languages for each feature available for serverless scanning in each cloud service provider.

### Vulnerability Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#vulnerability-scanning)

Feature

Platform

Language

Versions

Conditions

Vulnerability scanning

AWS

Node.js

16

Vulnerability scanning

AWS

Node.js

18

Vulnerability scanning

AWS

Node.js

20

Vulnerability scanning

AWS

Python

3.7

Vulnerability scanning

AWS

Python

3.8

Vulnerability scanning

AWS

Python

3.9

Vulnerability scanning

AWS

Python

3.10

Vulnerability scanning

AWS

Python

3.11

Vulnerability scanning

AWS

Python

3.12

Vulnerability scanning

AWS

Java

11

Vulnerability scanning

AWS

Java

17

Vulnerability scanning

AWS

Java

21

Vulnerability scanning

AWS

Ruby

3.2

Vulnerability scanning

AWS

Go

1.x

Vulnerability scanning

Azure

Python

3.8

Vulnerability scanning

Azure

Python

3.9

Vulnerability scanning

Azure

Python

3.10

Vulnerability scanning

Azure

Python

3.11

Vulnerability scanning

Azure

Node.js

16

Vulnerability scanning

Azure

Node.js

18

Vulnerability scanning

Azure

Node.js

20

Vulnerability scanning

Azure

Java

17

Vulnerability scanning

Azure

Java

21

Vulnerability scanning

GCP

Node.js

14

Vulnerability scanning

GCP

Node.js

16

Vulnerability scanning

GCP

Node.js

18

Vulnerability scanning

GCP

Node.js

20

Vulnerability scanning

GCP

Python

3.7

Vulnerability scanning

GCP

Python

3.9

Vulnerability scanning

GCP

Python

3.10

Vulnerability scanning

GCP

Python

3.11

Vulnerability scanning

GCP

Python

3.12

Vulnerability scanning

GCP

Java

11

Vulnerability scanning

GCP

Java

17

Vulnerability scanning

GCP

Java

21

Vulnerability scanning

GCP

Go

1.x

Vulnerability scanning

GCP

Ruby

2.7

Vulnerability scanning

GCP

Ruby

3.0

Vulnerability scanning

GCP

Ruby

3.2

### Compliance Scanning[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#compliance-scanning)

Feature

Platform

Language

Versions

Conditions

Compliance scanning

AWS

Node.js

16

Compliance scanning

AWS

Node.js

18

Compliance scanning

AWS

Node.js

20

Compliance scanning

AWS

Python

3.7

Compliance scanning

AWS

Python

3.8

Compliance scanning

AWS

Python

3.9

Compliance scanning

AWS

Python

3.11

Compliance scanning

AWS

Python

3.12

Compliance scanning

AWS

Java

17

Compliance scanning

AWS

Ruby

3.2

Compliance scanning

AWS

Go

1.x

Limited scans available

Compliance scanning

Azure

Node.js

20

Compliance scanning

Azure

Python

3.9

Compliance scanning

Azure

Java

17

Compliance scanning

GCP

Node.js

20

Compliance scanning

GCP

Python

3.7

Compliance scanning

GCP

Python

3.9

Compliance scanning

GCP

Java

17

### Runtime Protection with Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#runtime-protection-with-defender)

Feature

Platform

Language

Versions

Conditions

Runtime protection with Defender

AWS

Node.js

18

Runtime protection with Defender

AWS

Node.js

20

Runtime protection with Defender

AWS

Node.js

22

Runtime protection with Defender

AWS

Python

3.9

Runtime protection with Defender

AWS

Python

3.10

Runtime protection with Defender

AWS

Python

3.11

Runtime protection with Defender

AWS

Python

3.12

Runtime protection with Defender

AWS

Python

3.13

Runtime protection with Defender

AWS

Java

8.al2

Runtime protection with Defender

AWS

Java

11

Runtime protection with Defender

AWS

Java

17

Runtime protection with Defender

AWS

Java

21

Runtime protection with Defender

GCP

-

-

Not available

### WaaS with Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#waas-with-defender)

Feature

Platform

Language

Versions

Conditions

WAAS with Defender

AWS

Node.js

18

WAAS with Defender

AWS

Node.js

20

WAAS with Defender

AWS

Node.js

22

WAAS with Defender

AWS

Python

3.9

WAAS with Defender

AWS

Python

"3.10"

WAAS with Defender

AWS

Python

3.11

WAAS with Defender

AWS

Python

3.12

WAAS with Defender

AWS

Python

3.13

WAAS with Defender

AWS

Java

11

Gradle

WAAS with Defender

AWS

Java

11

Maven

WAAS with Defender

AWS

Java

17

Gradle

WAAS with Defender

AWS

Java

17

maven

WAAS with Defender

AWS

Java

21

Gradle

WAAS with Defender

AWS

Java

21

maven

WAAS with Defender

Azure

-

-

Not available

WAAS with Defender

GCP

-

-

Not available

### Auto-Defend[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#auto-defend)

Feature

Platform

Language

Versions

Conditions

Auto-Defend

AWS

Node.js

18

Auto-Defend

AWS

Node.js

20

Auto-Defend

AWS

Node.js

22

Auto-Defend

AWS

Python

3.9

Auto-Defend

AWS

Python

3.1

Auto-Defend

AWS

Python

3.11

Auto-Defend

AWS

Python

3.12

Auto-Defend

AWS

Python

3.13

Auto-Defend

Azure

-

-

Not available

Auto-Defend

GCP

-

-

Not available

## Go[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#go)

Prisma Cloud can detect vulnerabilities in Go executables for Go versions 1.13 and greater.

## Shells[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#shells)

For Linux, Prisma Cloud depends on the Bash shell. For Windows, Prisma Cloud depends on PowerShell.

The shell environment variable `DOCKER_CONTENT_TRUST` should be set to `0` or unset before running any commands that interact with the Prisma Cloud cloud registry, such as Defender installs or upgrades.

## Browsers[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#browsers)

Prisma Cloud supports the latest versions of Chrome, Safari, and Edge.

For Microsoft Edge, only the new Chromium-based version (80.0.361 and later) is supported.

## Cortex XDR[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/system-requirements\#cortex-xdr)

Palo Alto Networks does not support the concurrent deployment of Cortex XDR and Prisma Cloud Defender on a single workload, as both solutions provide overlapping security capabilities. Deploying both agents simultaneouly, results in redundant coverage and may lead to conflicts, resource contention, and system instability.

[PreviousGetting started](https://docs.prismacloud.io/admin-guide/install/getting-started) [NextCluster Context](https://docs.prismacloud.io/admin-guide/install/cluster-context)

Last updated 12 days ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
