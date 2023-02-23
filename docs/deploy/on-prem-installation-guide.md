# **AccuKnox On-prem Deployment Guide**

Follow this section to get to know about deploying Accuknox in On-premise environment. 

## **Infrastructure Deployment:**

Create Cluster and VPC by running the following terraform script:

**Step 1:** Download Terraform and Terraform script
You can download Terraform [here](https://developer.hashicorp.com/terraform/downloads)
Use the **aws configure** command to log into your AWS account before executing the Terraform scripts.
```sh
git clone https://github.com/accuknox/onprem-resources-tf.git
```

**Step 2:** Change the Directory
```sh
cd onprem-resources-tf
```
**Note :**

Create a S3 bucket in order to save the  terraform-states. And update the name & region of the bucket in backend.tf

+ In openprem-resources-tf/variables.tf  

Update the **region,vpc_name&cluster_name**

+ In openprem-resources-tf/vpc.tf  

Update the cidr, private_subnets & public_subnets

**Step 3:** Run the following commands to create Cluster and VPC
```sh
terraform init
terraform plan
terraform apply
terraform output > terraform_output.txt
```

Directly from the user interface, download the records (Legacy TXT record and DKIM tokens) for **SES**. Alter the ses domain name in the **variable.tf** as well. 

Run below command to get out of the directory
```sh
cd ..
```

**Helm Pull Registry:**
```sh
export ACCOUNT_ID="xxxxxxxx"
export REGION="us-east-2"
export ACCESS_KEY_ID="xxxxxxxxxxxxxxxx"
export SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxx"
export AWS_ECR_REPO="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
```

```sh
AWS_ACCESS_KEY_ID=${ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${SECRET_ACCESS_KEY} aws ecr get-login-password --region ${REGION} | helm registry login --username AWS --password-stdin ${AWS_ECR_REPO}
```

Pull Helm chart from repository
```sh 
helm pull oci://${AWS_ECR_REPO}/onprem/pre-requisites-installation-chart --untar
```
```sh
cd pre-requisites-installation-chart
```

###**Prerequisites, EBS and EFS and namespaces :**

+ Run the below command to Create or update a kubeconfig file for your cluster. Replace region-code with the AWS Region that your cluster is in and replace my-cluster with the name of your cluster.
+ aws eks update-kubeconfig --name <my cluster> --region <your-region>
+ Execute the scripts to install Prerequisites EBS and EFS CSI drivers.
+ Before execution make sure the file is executable if not, run the below command

```sh
chmod +x createnamespace.sh &&  ./createnamespace.sh
```
```sh
chmod +x  pre-ebs-efs.sh && ./pre-ebs-efs.sh
```
```sh

### **DB & Istio & Keycloak Installation Script:**                                 
```sh
chmod +x install.sh && ./install.sh
```

This script is used for installation and restoration of schema for Mysql, Mongodb & Pulsar.

**Note:**	==After the script completes, a **"passwords.txt"** file is created which contains the **mysql & mongodb passwords** for the admin and application user for databases. You can refer to this file to obtain the passwords.==

**[Optional] Mysql Commands:** To verify database and table inside the database 
```bash
kubectl run -n accuknox-mysqldb -i --rm --tty percona-client --image=percona:8.0 --restart=Never -- bash -il
```
To login as a Admin 
```bash
mysql -h accuknox-mysql-haproxy -u operator -p'<operator_password>'
```

**[Optional]MongoDB Commands :** To Login as a admin: (Replace the admin password in <password>)

```bash
kubectl run -i -n accuknox-mongodb --rm --tty percona-client --image=percona/percona-server-mongodb:4.4.16-16 --restart=Never -- mongo "mongodb+srv://userAdmin:<password>@accuknox-mongodb-rs0.accuknox-mongodb.svc.cluster.local/admin?replicaSet=rs0&ssl=false"
```

 **[Optional]Pulsar command :** Namespaces list in accuknox tenant
```sh
kubectl exec -it -n accuknox-pulsar pod/pulsar-toolset-0 -- bin/pulsar-admin namespaces list accuknox
```

Run below command to get out of the directory
```sh
cd ..
```

## **Installing Istio Gateway**

Pull Helm chart from repository

```sh
helm pull oci://${AWS_ECR_REPO}/onprem/istio-gateway-chart --untar
```

Run the following command

```sh
helm install istio-gateway oci://${AWS_ECR_REPO}/onprem/istio-gateway-chart \
        --set global.hosts.cwpp="example.com" \
        --set  global.hosts.keycloak="example.com" \ 
        --set global.hosts.cspm="*.example.com" \
        --set global.hosts.soarcast="example.com" \
        --set issuerName="letsencrypt-example" \
        --set issuerEmailid="example@xyz.com" \
        -n accuknox-chart

```
## **Vault Installation**

**Step 1:** Pull Helm chart from repository
```sh
helm pull oci://${AWS_ECR_REPO}/onprem/vault-chart  --untar
```

```sh
cd vault-chart/
```

**Note :** 
Make sure that EBS is configured on the cluster to deploy consul. storage class for EBS with the name of **“ebs-sc”**
		
Before running the following script, AWS CLI needs to configure with the user which has admin access for IAM, KMS and EKS Cluster using **aws configure** on your local machine 

Run the following command to Install Vault
```sh
 chmod +x vault_install.sh && ./vault_install.sh
```

*Above script will create an IAM user, KMS key, consul and vault.

**Step 2:** Add secrets for the all microservices in vault

**Note :** Need Vault binary on your local to run the following script. 
Refer documentation [Install | Vault | HashiCorp Developer](https://developer.hashicorp.com/vault/downloads)

Below **TOKEN** & **PASSWORD** are required **vault/microservice_secrets.sh** script file:

+ Your vault root token,

+ MySQL accuknox_user user password, 

+ Mongo-DB deo user password,

+ Mongo-DB datapipeline user password

Run the following command in another terminal to port-forward the vault server to access on local:
```sh
kubectl port-forward service/vault 8200:8200 -n accuknox-vault
```

Run the following commands create **secrets**, **policy** & **roles** for kubernetes auth method for all microservices:
```sh
./microservices_secrets.sh
```

##**Keycloak**

**Step 1:** Configuring KeyCloak

Once the keycloak pod is up and running open the Url which you configured in Istio gateway.   

+ Click on the administration console → login with Keycloak username & password.

+ Click **Select realm → Accuknox**

+ Then Click on **Clients → create** then import **accuknox-ui.json file.** (file available in keycloak-chart/ directory)


**Note :** Before uploading edit DNS in four marked places in **accuknox-ui.json** file.
```bash

    "rootUrl": "https://onprem.keycloak.example.com/*",
    "adminUrl": "https:/onprem.keycloak.example.com/",
    "redirectUris": [
        "http://localhost:3000/*",
        "https://onprem.keycloak.example.com/*"
    ],
    "webOrigins": [
        "https://onprem.keycloak.example.com"

```
+ Click on **Clients** → **accuknox-ui** → **Credential**
![](/deploy/images/image-1.png)

**Note :** Kindly note the client secret and client id to install user-management
+ Now Keycloak has been configured

## **Microservices Deployment:**
```sh
export ACCOUNT_ID="xxxxxxxxx"
export REGION="us-east-2"
export ACCESS_KEY_ID="xxxxxxxxxxx"
export SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxxx"
export AWS_ECR_REPO="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
export REDIS_PASSWORD="xxxxxxxxx"
export GIT_PVT_KEY_PATH="/path/to/key"
export GIT_PUB_KEY_PATH="/path/to/key"
export SALT_EFS_VOLUME_ID="fs-***"
export CWPP_API_URL="https://cwpp.example.com"
export CSPM_API_URL="https://cspm.example.com"
export CSPM_APP_CONFIG_PATH="/path/to/config"
export EXT_ELASTICACHE=""
export EXT_RDS=""
export DIVY_STATICFILES_EFS_VOLUME_ID="fs-***"
export DIVY_MEDIA_EFS_VOLUME_ID="fs-**"
```


+ Run the below command

```sh
helm upgrade --install accuknox-services oci://${AWS_ECR_REPO}/onprem/accuknox-services \
	--set-file global.saltstack.master.keys.git_pvt=${GIT_PVT_KEY_PATH} \
	--set-file global.saltstack.master.keys.git_pub=${GIT_PUB_KEY_PATH} \
	--set-file global.cspm.appconfig=${CSPM_APP_CONFIG_PATH} \
	--set aws.accounId=${ACCOUNT_ID} \
	--set aws.accessKeyId=${ACCESS_KEY_ID} \
	--set aws.secretAccessKey=${SECRET_ACCESS_KEY} \
	--set aws.region=${REGION} \
	--set global.hosts.cwpp=${CWPP_API_URL} \
	--set global.hosts.cspm=${CSPM_API_URL} \
	--set global.redis.conf.password=${REDIS_PASSWORD} \
	--set extsvc.elasticache.externalName=${EXT_ELASTICACHE} \
	--set extsvc.rds.externalName=${EXT_RDS} \
	--set extraPersistentVolume.divystaticfiles.spec.csi.volumeHandle=${DIVY_STATICFILES_EFS_VOLUME_ID} \
	--set extraPersistentVolume.divymedia.spec.csi.volumeHandle=${DIVY_MEDIA_EFS_VOLUME_ID} \
	--set extraPersistentVolume.minionkeys.spec.csi.volumeHandle=${SALT_EFS_VOLUME_ID} 
```

##**CSPM**

**Step 1:** CSPM API Deployment

Create database on RDS by running the following commands in the cluster which is running on same VPC
```bash
kubectl run my-shell --rm -i --tty --image ubuntu -- bash
```
```sh
apt update
```

Run the following command to install postgresql-client
```sh
apt install postgresql-client
```
![](/deploy/images/image-2.png)
** Note:**  Find the RDS endpoints from AWS RDS console → Databases → <database name>

```sh
psql --host=<aws endpoint> --port=5432 --username=<username> --password --dbname=postgres
```

To create Database run the following command
```sh
CREATE DATABASE divy; 
CREATE DATABASE soarcast; 
```

Pull Helm chart from repository
```sh
helm pull oci://${AWS_ECR_REPO}/onprem/divy-backend-chart --untar
```


**Note:** divy-backend-chart/secretfiles/appconfig.json

Once database created, update the **appconfig.json** with above newly created creds for RDS,ElastiCache,SMTP,Vault & Keycloak use the following repo to deploy Divy api.

```sh
// Setting this to 1 turns debug mode on and setting it to 0 turns it off. It is highly recommended to turn off debug mode in a production environment because the debug messages can reveal sensitive data, but it is helpful for debugging in a test environment.
DEBUG: 0 
// email for user verification
EMAIL_FROM: ""
// add smtp endpoint (get it from smtp setting) 
EMAIL_HOST: ""
// add starttls port (get it from smtp setting)
EMAIL_PORT: "587" 
// get the smtp credential username from terraform_output.txt
EMAIL_USERNAME: "" 
//get the smtp credential password from terraform_output.txt
EMAIL_PASSSWORD: ""
POSTGRES_DB: divy 
// Must be set to "postgres"
POSTGRES_HOST: postgres 
// Must be set to "5432"
POSTGRES_PORT: "5432"
POSTGRES_USER: pgadmin 
// get RDS password from terraform_output.txt
POSTGRES_PASSWORD: “” 
// Must be set to "redis"
REDIS_HOST: redis
// Must be set to "6379"
REDIS_PORT: "6379"
// REDIS_USER: default
REDIS_SSL: true
// get Elasticache password from terraform_output.txt 
REDIS_PASSWORD: “”
// This determines whether the public Redis endpoint should verify the TLS certificate. Keep this blank unless you are using a certificate common name that matches the endpoint domain, otherwise this will result in an error.
REDIS_VERIFY_SSL: "" 
// Must be set to "https://vault.vault:8200" (FQDN for vault server)
VAULT_HOST: https://vault.vault:8200 
// Set this to "divy" for divy
VAULT_ROOT_PATH: divy
VAULT_VERIFY_CERTIFICATE: "" 
// get the vault token from vault_key.txt (Divy-token)
VAULT_TOKEN: “”
The URL for the React frontend app.
FRONTEND_HOST: “”
// Set this to "1"
DOCKER_RUN: 1 
The domain for the backend API (example cspm.onprem.example.com which is created from *.onprem.example.com)
API_HOST: “”
// keycloak client id
KEYCLOAK_CLIENT_ID: “” 
KEYCLOAK_DEFAULT_ACCESS: "ALLOW",
KEYCLOAK_METHOD_VALIDATE_TOKEN: "DECODE"
// keycloak endpoint url keycloak.example.com/auth
KEYCLOAK_SERVER_URL: “”
// keycloak client secret key
KEYCLOAK_CLIENT_SECRET_KEY: “” 

KEYCLOAK_ADMIN_URL : //keycloak endpoint url
KEYCLOAK_ADMIN_USERNAME : //keycloak admin username
KEYCLOAK_ADMIN_PASSWORD : //keycloak admin password
KEYCLOAK_ADMIN_REALM_NAME : xxxxxxx
KEYCLOAK_ADMIN_USER_REALM_NAME: xxxxxx
// This is used for providing logging to help troubleshoot bugs. This field can be left blank for basic deployment.
SENTRY_KEY: “”  
SALTSTACK_API_URL:“https://saltmaster-service.accuknox-saltstack.svc.cluster.local:8000”
//saltmaster password
SALTSTACK_USERNAME: "soarcast-api"
SALTSTACK_PASSWORD: ""
 //redis url
SALT_REDIS_HOST:""
//redis port
SALT_REDIS_PORT: 31400 
//redis password
SALT_REDIS_PASSWORD: ""
//keycloak endpoint URL
KEYCLOAK_URL:""
//API url for cwpp
CWPP_BASE_URL: ""
 //API url for cspm
CSPM_BASE_URL: ""
//To onboard s3
MAIN_AWS_ACCESS_KEY_ID: "" 
//To onboard s3
MAIN_AWS_ACCESS_KEY_SECRET: "" 
```
**Note:**  Find the **RDS endpoints** from AWS RDS console → Databases → <database name>

**Note:** Find the **Elasticache endpoints** from ElastiCache console → redis cluster → <clustername> → primary endpoint

**Note:**  Kindly update the endpoint of **RDS**, **ElastiCache** and **EFS _ID**
EFS_ID -> from aws EFS console with the name CSPM-STATICFILES filesystem

Run the following command to install Divy
```sh
helm install divy divy-backend-chart \
	--set redisExternalServices.externalName=<RDS-ENDPOINT>  \
	--set postgresExternalServices.externalName=<ELASTICACHE-ENDPOINT> \
	--set pv.spec.csi.volumeHandle=<DIVY-MEDIA> \
	--set pv1.spec.csi.volumeHandle=<CSPM-STATICFILES-EFS-ID> \
	-n accuknox-divy 
```

**Deploy Nginx:**

Pull Helm chart from repository
```sh
helm pull oci://${AWS_ECR_REPO}/onprem/divy-nginx-chart --untar
```


Divy backend uses NGINX as a reverse proxy in front of the web application

In the secret directory, create files called cert and key. Paste the ca cert bundle and private key for your domain respectively. You may need to get new certs for the new domains eg: ***.onprem.example.com**  that you are using that matches the current product names and uses these certs.

**Note:** Kindly update the certificates in the nginx helm chart secrets.

Run the following command to install nginx
```sh
helm install nginx nginx-chart -n accuknox-divy
```

To check the deployed pods
```sh
kubectl get pods -n accuknox-divy
```
![](/deploy/images/image-3.png)


**Create a Root Tenant in Divy:**

*Divy web pod
```sh
kubectl exec -it uswgi-*** -- bash -n <namespace>

python3 manage.py shell

from tenant.models import Client, Domain

tenant = Client(schema_name='root', name='root')
tenant.save()

domain = Domain()
domain.domain = '127.0.0.1' # Replace with your domain name you created earlier.
domain.tenant = tenant
domain.is_primary = True
domain.save()
exit
```


**Create a Superuser:**

In the same container run the following command to create superuser
```sh
python3 manage.py createsuperuser
```

Enter the new username, email address and password

You can access the divy api UI on **https://<domain name>/admin/** use above created superuser for login

##**Soarcast**

**Step 1:** Soarcast API Deployment

Pull Helm chart from repository
```sh
helm pull oci://${AWS_ECR_REPO}/onprem/soarcast-chart --untar
```

**Note:** soarcast-chart/secretfiles/appconfig.json

Once database created update the **appconfig.json** with  previously created creds for RDS(same has divy ), ElastiCache, SMTP & Vault  use the following repo to deploy soarcast api
```sh
DEBUG: 0 // Setting this to 1 turns debug mode on and setting it to 0 turns it off. It is highly recommended to turn off debug mode in a production environment because the debug messages can reveal sensitive data, but it is helpful for debugging in a test environment.

"EMAIL_HOST": "", //add smtp endpoint (get it from smtp setting)
"EMAIL_PORT": "587", //add starttls port 
"EMAIL_USERNAME":"",//get the smtp credential username from terraform_output.txt
"EMAIL_PASSWORD": "",//get the smtp credential password from terraform_output.txt
"USE_TLS": "true",
"USE_SSL": "",
"EMAIL_FROM": "", //email for user verification

POSTGRES_DB: soarcast
POSTGRES_HOST: postgres
POSTGRES_PORT: "5432"
POSTGRES_USER: pgadmin
POSTGRES_PASSWORD: password // get RDS password from terraform_output.txt 

REDIS_HOST: redis // Must be set to "redis."
REDIS_PORT: "6379" // Must be set to "6379"
REDIS_SSL: true // Set this to "true" or "True" in order to encrypt traffic to Redis. This is highly recommended for a production environment. 
REDIS_USER: default
REDIS_PASSWORD: password //get Elasticache password from terraform_output.txt 
REDIS_VERIFY_SSL: "" /

VAULT_HOST: https://vault.vault:8200 // VAULT_ROOT_PATH: mission // Set this to "mission" for soarcast
VAULT_VERIFY_CERTIFICATE: ""

VAULT_TOKEN: // get the vault token from vault_key.txt (soarcast-token)

FRONTEND_HOST: The URL for the React frontend app.
DOCKER_RUN: 1 // Set this to "1".
DOMAIN_URL: The domain for the backend API (example soarcast.onprem.example.com)
```



**Note:**  Find the **RDS endpoints** from AWS RDS console → Databases → <database name>

**Note:** Find the **Elasticache endpoints** from ElastiCache console → redis cluster → <clustername> → primary endpoint
Note: Kindly update the endpoint of **RDS**, **ElastiCache** and **EFS _ID**
EFS_ID -> from aws EFS console with the name **CSPM-STATICFILES** filesystem

Run the following command to install Soarcast
``sh
helm install soarcast-chart --set redisExternalServices.externalName=<RDS-ENDPOINT>  --set postgresExternalServices.externalName=<ELASTICACHE-ENDPOINT> --set pvspec.csi.volumeHandle=<CSPM-STATICFILES-EFS-ID> -n accuknox-soarcast
```

**Deploy Nginx:**

Pull Helm chart from repository

```sh
helm pull oci://${AWS_ECR_REPO}/onprem/soarcast-nginx-charts --untar
```

Soarcast uses NGINX as a reverse proxy in front of the web application

In the secret directory, create files called cert and key. Paste the ca cert bundle and private key for your domain respectively. You may need to get new certs for the new domains eg: **saoarcast.onprem.example.com**  that you are using that matches the current product names and uses these certs.
**Note:** Kindly update the certificates in the nginx helm chart secrets.

Run the following command to install nginx
```sh
helm install nginx nginx-chart -n accuknox-divy
```

To check the deployed pods
```sh
kubectl get pods -n accuknox-divy
```
![](/deploy/images/image-3a.png)


**Create a Superuser:**

*soarcast web pod
run the following command to create superuser
```sh
kubectl exec -it uswgi-*** -- bash -n <namespace>
```
```sh
python3 manage.py createsuperuser
```

Enter the new username, email address and password

You can access the soarcast api UI on https://saoarcast.onprem.example.com use above created superuser for login


Login to cspm ui to generate swagger token 

cspmurl: https://cspm.example.com/admin/
Username:   //use the divy superuser login 
password:  // use the divy superuser pass
swaggerurl : https://cspm.example.com/api/swagger/

+ Click on → **POST/token** and then click → **try it out**
![](/deploy/images/image-4.png)

+ Data object (to be blank) , click on → Execute and 201 status code (view token)
![](/deploy/images/image-5.png)


