---
title: AccuKnox CDR for Azure
description: Accuknox CDR documentation for Azure
---

# AccuKnox CDR for Azure

## Introduction

AccuKnox CDR for Azure can be deployed using a Terraform configuration. The
configuration deploys the following resources:

| Resource                                    | Purpose                                                |
|---------------------------------------------|--------------------------------------------------------|
| EventHub Namespace                          | Contains the EventHub                                  |
| EventHub                                    | Receives messages from the ActivityLog                 |
| EventHub Authorization Rule "activity_logs" | Allows ActivityLog to publish messages to the EventHub |
| EventHub Authorization Rule "logstash"      | Allows Logstash to subscribe to the EventHub messages  |

The Terraform configuration will be provided to you by the AccuKnox team in
the onboarding phase.

## Setup

To setup the integration please follow the steps below

### Step 1: Deploy the resources

In this step we assume you that you are authenticated to Azure via the `azure`
CLI. You can authenticate using this command.

```bash
az login
```

Before applying the Terraform configuration, please update the
`terraform.tfvars` with the appropriate values.

| Variable                       | Description                                                                            | Default Value  | Requirement |
|--------------------------------|----------------------------------------------------------------------------------------|----------------|-------------|
| `subscription_id`              | Azure account subscription ID                                                          |                | Mandatory   |
| `location`                     | Azure location where the resources will be created                                     | `East US`      | Optional    |
| `resource_group_name`          | Name of the resource group to be created                                               | `accuknox-cdr` | Optional    |
| `event_hub_namespace_name`     | Name of the event hub namespace to be created                                          | `accuknox-cdr` | Optional    |
| `event_hub_namespace_sku`      | Defines the event hub tier to be used. Possible values: "Basic", "Standard", "Premium" | `Basic`        | Optional    |
| `event_hub_namespace_capacity` | Capacity / throughput units                                                            | 1              | Optional    |
| `event_hub_name`               | Name of the event hub                                                                  | `default`      | Optional    |
| `event_hub_partition_count`    | Specifies the current number of shards on the Event Hub                                | 1              | Optional    |
| `event_hub_message_retention`  | Specifies the number of days to retain the events for this Event Hub                   | 1              | Optional    |

Please run the following commands to deploy the required resources:

```bash
terraform init
terraform plan
terraform apply
```

### Step 2: Get the EventHub Primary Connection String

```
terraform output -json
```

E.g.,

```
{
  "event_hub_primary_connection_string": {
    "sensitive": true,
    "type": "string",
    "value": "Endpoint=sb://accuknox-cdr.servicebus.windows.net/;SharedAccessKeyName=logstash;SharedAccessKey=REDACTED;EntityPath=default"
  },
  "event_hub_secondary_connection_string": {
    "sensitive": true,
    "type": "string",
    "value": "Endpoint=sb://accuknox-cdr.servicebus.windows.net/;SharedAccessKeyName=logstash;SharedAccessKey=REDACTED;EntityPath=default"
  }
}
```

## **Next Steps**

Provide the connection string to your AccuKnox Point of Contact to start the
onboarding process.
