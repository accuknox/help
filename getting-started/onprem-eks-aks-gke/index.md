---
title: On-Prem Installation Guide On EKS, AKS and GKE
description: Step-by-step guide for installing AccuKnox on managed Kubernetes clusters.
---

# On-Prem Installation Guide On EKS, AKS, and GKE

This guide outlines the installation process for setting up AccuKnox on EKS, AKS, or GKE clusters.

## Installation Steps

### Step 1: Download & Extract the Bundle
First, download the AccuKnox Installation Bundle and extract the bundle to your desired directory.

### Step 2: Push Images to Private/Local Container Registry (Air-gapped)

!!! info "Air-gapped Environments"
    If you are operating in an air-gapped environment or using a private container registry, you must push the images to your registry first.

Connect to your air-gapped registry and push the tarball images:

```bash
# Connect to airgapped registry
docker login --username <username> --password "<pwd>" <registry_address>/<reponame>

# Upload images to private registry
sudo ./push_tar_images.sh <registry_address>/<reponame>
```

### Step 3: Install Certmanager & On-Prem Manager (Air-gapped)

Run the installation script to create `Certmanager` and the `onprem-manager` components in your private setup:

```bash
cd airgapped-reg
./airgapped-install.sh <registry_address>/<reponame> <dummyusername> <dummypassword>
cd ..
```

### Step 4: Configure Deployment Values

Update the necessary fields in your `override-values.yaml` file:

* **StorageClass:** Update the values with your default storage class name (`<storageclass>`).
* **Domain:** Replace `example.com` with your actual domain name.

!!! warning "Disable Certmanager for Air-gapped / Private Registries"
    If the environment is air-gapped or using a private registry, ensure you disable the Certmanager installation in your overrides:

    ```yaml title="override-values.yaml"
    ssl:
      certmanager:
        install: false
    ```

### Step 5: Configure Certificates

AccuKnox auto-generates the needed self-signed certificates for the client. To enable this option, set the `ssl` section as follows:

```yaml title="override-values.yaml"
ssl:
  selfsigned: true
  customcerts: false
```

### Step 6: Enable Istio LoadBalancer

Ensure that the Istio LoadBalancer is enabled in your configuration:

```yaml title="override-values.yaml"
istio_loadbalancer: true
```

### Step 7: Install AccuKnox Charts

Execute the chart installation script:

```bash
./install_chart.sh
```

### Step 8: DNS Mapping

Run the following script to generate the records you should add to your DNS zone. This maps the DNS with the Istio LoadBalancer IP:

```bash
./generate_dns_entries.sh
```

### Step 9: Access the UI

1. Open the UI in a browser using your configured domain/IP.
2. Follow the on-screen instructions to complete the sign-up.