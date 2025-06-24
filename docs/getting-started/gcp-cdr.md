---
title: AccuKnox CDR for GCP
description: Accuknox CDR documentation for GCP
---

# **AccuKnox CDR for GCP**

## **Introduction**
AccuKnox CDR for GCP is deployed using terraform scripts, the scripts deployes the following resources:

| Resource    | Purpose |
| :-------- | :------- |
| Log Sink | Routes Logs to a Sink |
| Pub/Sub Topic | Recieves logs from Log Sink |
| Pub/Sub Subscription | Consumers subscribes to the Log sent by the Log sink |
| Service Account | Service account to subscribe to the Pub/Sub subscription |

In addition, the scripts will enable the following API's if they are disabled:

- pubsub.googleapis.com
- iam.googleapis.com
- logging.googleapis.com

The terraform script will be provided to you by AccuKnox team in the onboarding phase.

## **Setup**

To setup the integration please follow the steps below


### **Step 1: Deploy the resources**

In this step we assume you that you are authenticated to GCP via CLI.
You can authenticate using this command.

```bash
gcloud auth application-default login
```

Before applying the terraform scripts, please update the `terraform.tfvars` with the appropriate values

|Value| Purpose|
|:--:|--|
|project_id|GCP project ID|
|region| any valid region (required by the terraform provider)|
|pubsub_topic_name| Pub/Sub Topic name |
|subscription_name| Pub/Sub Subscription name |
|service_account_id| Service Account name|
|sink_name| Log Sink name|

Please run the following commands to deploy the required resources:
```bash
terraform init
terraform plan
terraform apply
```

### **Step 2: Generate Service account keys **

1. Navigate to Service Accounts under IAM & Admin > Service Accounts
1. Click on the Service Account Email (highlited in blue)
1. Generate Keys under Keys > Add Key

Save the generated keys in a safe place and transmit them as well to your AccuKnox Point of Contact to start the onboarding process

## **Next Steps**
