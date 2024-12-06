---
title: Azure Sentinel Feeder Integration
description: This document contains the process of integrating AccuKnox Feeder Service with Azure Sentinel. By integrating AccuKnox Feeder Service with Azure Sentinel, you can forward the alerts based on policy violation to Azure Sentinel.
---

## **Overview**
Azure Sentinel is a cloud-native SIEM solution by Microsoft that helps organizations detect, investigate, and respond to security threats. It collects data from various sources, applies AI and ML for intelligent analytics, and offers real-time insights. Key features include comprehensive data ingestion, threat detection with customizable rules, interactive investigation and hunting capabilities, automation through playbooks, and seamless integration with Microsoft and third-party security solutions. Azure Sentinel enables organizations to enhance security operations, improve threat detection and response, and protect their digital assets across hybrid and multi-cloud environments.

## Prerequisites
- [Azure Logic App - Webhook](/integrations/azure-sentinel-feeder-integration/#creating-webhook-using-the-azure-logic-app)
- Azure Sentinel Subscription
- Feeder Service Running on Client's cluster

## Configuration
To forward the Alerts based on Policy Violation to Azure sentinel set the following environment variables `AZURE_SENTINEL_ENABLED` and `AZURE_SENTINEL_ALERTS_ENABLED` to true and to forward Logs `AZURE_SENTINEL_LOGS_ENABLED` to true in your Feeder Agent manifest.

Also set the environment variables `AZURE_SENTINEL_GROUP_NAME`, `AZURE_SENTINEL_GROUP_VALUE`, `AZURE_SENTINEL_URL` of the Azure Logic App Deployed.
To start editing the chart:
``` sh
 kubectl edit configmap azuresentinel-vars -n accuknox-agents
```
Edit the following Environment Variables mentioned below:

```yaml
AZURE_SENTINEL_ALERTS_ENABLED: "true"
AZURE_SENTINEL_ENABLED: "true"
AZURE_SENTINEL_GROUP_NAME: "Preferred Name"
AZURE_SENTINEL_GROUP_VALUE: "Preffered Value"
AZURE_SENTINEL_LOGS_ENABLED: "true"
AZURE_SENTINEL_URL: "https://xyz.xxxxx.log ic.azu re.com:443/workflows/xxxxxxxx"
```

## Environment variables for Azure sentinel Integration
The following is the list of environment variables available for the Feeder-Service-Agent

| Env Variable | Description |
| - | - |
| `AZURE_SENTINEL_ALERTS_ENABLED` | Setting this to true forward the Policy Violated Alerts to Azure sentinel |
| `AZURE_SENTINEL_ENABLED` | Setting this to true forward the Logs and Alerts to Azure sentinel |
| `AZURE_SENTINEL_GROUP_NAME` | You can specify any group name based on your prefernece, this can be used to filter the events. This works as a key value pair, where key is Group | Name and Group Value is the value for the Key Group Name. e.g., `K8s Cluster` |
| `AZURE_SENTINEL_GROUP_VALUE` | You can add any value to this group value. e.g., `Dev Team Cluster` |
| `AZURE_SENTINEL_LOGS_ENABLED` | Setting this to true forward the Logs to Azure sentinel |
| `AZURE_SENTINEL_URL` | Enter your Azure Logic App's Webhook URL here. e.g., `https://xyz.xxxxx.log ic.azu re.com:443/workflows/xxxxxxxx` |

## Creating webhook using the Azure Logic App
About the logic app:
Azure Logic Apps is a cloud platform where you can create and run automated workflows with little to no code. Using the visual designer and selecting from prebuilt operations, you can quickly build a workflow that integrates and manages your apps, data, services, and systems. To create a webhook using the logic app.

Step 1: Search for the logic app in the Azure portal.

Step 2: Add the new logic app and fill in the relevant details.

Step 3: After creating the logic it will appear in the logic app dashboard.

Step 4: Open the app and click on the go-to resource button.

Step 5: Select the http request to receive the logs.

Step 6: Click on the new step and click HTTP after that click on the Azure log analytics to receive the alert data.

Step 7: Add the connection name, workspaceID, and workspace key you can get workspace id and key in the log analytics workspace tab.

Step 8: Click on the Integration and click on the Agents tab.

Step 9: Click on the Azure log analytics data collector and click JSON request body as the body and log name, After the setup is done you will receive a webhook URL.

Multiple options can be selected.
Add label