## **High-Level Architecture Overview**

![](images/on-prem-deploy.png)

AccuKnox onprem deployment is based on Kubernetes native architecture.

### AccuKnox OnPrem k8s components

#### Microservices

Microservices implement the API logic and provide the corresponding service endpoints. AccuKnox uses Golang-based microservices for handling any streaming data (such as alerts and telemetry) and Python-based microservices for any other control-plane services.

#### Databases

PostgreSQL is used as a relational database and MongoDB is used for storing JSON events such as alerts and telemetry. Ceph storage is used to keep periodic scanned reports and the Ceph storage is deployed and managed using the Rook storage operator.

#### Secrets Management

Within the onprem setup, there are several cases where sensitive data and credentials have to be stored. Hashicorp’s Vault is made use of to store internal (such as DB username/password) and user secrets (such as registry tokens). The authorization is managed purely using k8s native model of service accounts. Every microservice has its own service account and uses its own service account token automounted by k8s to authenticate and subsequently authorize accesses to the secrets.

#### Scaling

K8s native horizontal and vertical pod autoscaling is enabled for most microservices with upper limits for resource requirements.

#### AccuKnox-Agents

Agents need to be deployed in target k8s clusters and virtual machines that have to be secured at runtime and to get workload forensics. Agents use Linux native technologies such as eBPF for workload telemetry and LSMs (Linux Security Modules) for preventing attacks/unknown execution in the target workloads. The security policies are orchestrated from the AccuKnox onprem control plane. AccuKnox leverages SPIFFE/SPIRE for workload/node attestation and certificate provisioning. This ensures that the credentials are not hardcoded and automatically rotated. This also ensures that if the cluster/virtual machine has to be deboarded then the control lies with the AccuKnox control plane.


## Installation steps

### Installation Package

- Onprem Deployment Installation Document (this document)
- Helm charts archive <accuknox-helm-charts.tgz\>
    + Kubectl and Helm tools are pre-requisite tools for using these helm charts

Use the following command to extract
```sh
tar xvf accuknox-helm-charts.tgz
cd Helm-charts
```
### Use of Private/Local Container Registry (or air-gapped mode)

If you want to use your private/local registry as the exclusive source of images in the ENTIRE cluster, please install the `accuknox-onmprem-mgr` component first.

| Value | Description | Provider |
|--|--|--|
|registry.username| Registry user | Customer |
|registry.password | Registry password | Customer |
|registry.address| The registry server address| Customer |
|ecr.user| Credential required to pull images from Accuknox registry </br>Value: <provided-by-accuknox\> | Accuknox |
|ecr.password| Credential required to pull images from Accuknox registry </br>Value: <provided-by-accuknox\> | Accuknox|

Execute the following commands:

```bash
cd airgapped-reg

# configure aws cli with AccuKnox  provided secrets

aws configure

# connect to docker Accuknox docker registry
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 956994857092.dkr.ecr.us-east-2.amazonaws.com

# connect to airgapped registry
docker login <registry.address>

# upload images to private registry

./upload_images.sh <registry.address>

# create a namespace
MGR_NS="accuknox-onprem-mgr"
CERT_MGR_NS="cert-manager"
kubectl create ns $MGR_NS
kubectl create ns $CERT_MGR_NS
kubectl create secret docker-registry airgapped-reg --docker-server=<registry.address> --docker-username=<registry.username> --docker-password=<registry.password> -n $MGR_NS
kubectl create secret docker-registry airgapped-reg --docker-server=<registry.address> --docker-username=<registry.username> --docker-password=<registry.password> -n $CERT_MGR_NS
# <registry_address> can include port as well
./install-certmanager.sh <registry_address>

./install-onprem-mgr.sh <registry_address>
```

### Update override values

**[ONLY FOR air-gapped/private registry ENVIRONMENT]**: Set `global.onprem.airgapped` to true in `override-values.yaml` file.


### Before you start

We offer three deployments models when it comes to SSL certificate to accomodate for client requirements.

- **Auto-generated self-signed certificate**: We auto generate the needed self signed certificates for the client.
To enabled this option, the ssl section the override values file should be set as follow:
```yaml
  ssl:
    selfsigned: true
    customcerts: false
``` 
- **Certificate signed by a known authority**: The client provies a certificate signed by a known signing authority.
To enabled this option, the ssl section the override values file should be set as follow:
```yaml
  ssl:
    selfsigned: false
    customcerts: true
``` 

- **Self-signed certificates** (provided by the customer): The client provides a self signed certificate.
To enabled this option, the ssl section the override values file should be set as follow:
```yaml
  ssl:
    selfsigned: true
    customcerts: true
``` 

AccuKnox installation package will contain `override-values.yaml` file that contains installation-specific options to be configured.

1. Override <your_domain.com\> to your domain 
2. Set your ssl preferences in the override values by changing the ssl block.


### Install AccuKnox base dependencies

```bash
kubectl  create  namespace  accuknox-chart

helm  upgrade  --install  -n  accuknox-chart  accuknox-base  accuknox-base-chart  --create-namespace -f  override-values.yaml
```
**IMPORTANT**

Some resources deployed in the above step require some time to provision. If the user executes the next command without waiting for the proper provisioning of the previous command the installation may break and will need to start over.

Run the below script to make sure that the provisioning was done succesfully.

```bash
while true
do
    status=$(kubectl get cephcluster -n accuknox-ceph  rook-ceph -o=jsonpath='{.status.phase}')
    [[ $(echo $status | grep -v Ready | wc -l) -eq 0 ]] && echo "You can procceed" && break
    echo "wait for initialization"
    sleep 1
done
```

### Install AccuKnox pre-chart

The user needs to set the required values as folows:

| Value | Description | Who provides it |
|--|--|--|
|email.user| The Email user that will send invitation, reports, etc. | Customer |
|email.password| Email password | Customer |
|email.host| The Email server address | Customer |
|ecr.user| Credential required to pull images from Accuknox registry </br>Value: <provided-by-accuknox\> | AccuKnox |
|ecr.password| Credential required to pull images from Accuknox registry </br>Value: <provided-by-accuknox\> | AccuKnox|

```bash
helm  upgrade  --install  -n  accuknox-chart  accuknox-pre  pre-chart  --create-namespace -f  override-values.yaml --set email.user="" --set email.password="" --set email.host="" --set ecr.user="<provided-by-accuknox>" --set ecr.password="<provided-by-accuknox>"
```

### Install AccuKnox microservices chart

```bash
helm  upgrade  --install  -n  accuknox-chart  accuknox-microservice  accuknox-microservice-chart  --create-namespace -f  override-values.yaml
```

### DNS mapping

Run the following script to generate the records you should add to your DNS zone

```bash
./generate_dns_entries.sh
```

### Installing certificates

#### Certificates signed by known authority

```bash
./install_certs.sh <certificate_path> <certificate_key_path> <ca_path>
```

#### Self-signed certificates (provided by customer)

```bash
./install_certs.sh <certificate_path> <certificate_key_path> <ca_path>
./istio-config.sh <ca_path>
```

####  Self-signed certificates

```bash
./istio-config-local.sh
```

### Verification of installation

- After successful installation, you should be able to point to https://frontend.<your-domain.com\> URL and get the sign-in page.
- https://cspm.<your-domain.com\>/admin/ page should be available.
- https://cwpp.<your-domain.com\>/cm/ page should be available.

## References

1. AccuKnox Deployment and Operations [FAQs](https://help.accuknox.com/faqs/troubleshooting-and-faqs/)
2. [AccuKnox Splunk Integration Guide](https://help.accuknox.com/integrations/splunk/)
3. [KubeArmor Splunk Integration Guide](https://help.accuknox.com/integrations/splunk_feeder_kubearmor/)
4. [CSPM: Use-cases & Scenarios](https://help.accuknox.com/use-cases/vulnerability/)
5. [CWPP: Use-cases & Scenarios](https://help.accuknox.com/use-cases/app-behavior/)
6. [Detailed Support Matrix](https://help.accuknox.com/getting-started/kubearmor-support-matrix/)


- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }