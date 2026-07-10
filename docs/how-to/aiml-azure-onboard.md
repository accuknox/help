---
title: Azure AI/ML Cloud Onboarding
description: Step-by-step instructions for onboarding an Azure cloud account and AI/ML assets within it to AccuKnox SaaS for automated security management.
---

# Azure AI/ML Cloud Onboarding

In this section we can find the steps to onboard an Azure cloud account to the AccuKnox SaaS platform.

## **Rapid Onboarding (via Azure)**

For Azure Onboarding it is required to register an App and grant Security read access to that App from the Azure portal.

**Step 1:** Go to your Azure Portal and search for *App registrations* and open it

![image](images/azure1.png)

**Step 2:** Here click on *New registration*

![image](images/azure2.png)

**Step 3:** Give your application a name, remember this name as it will be used again later, For the rest keep the default settings

![image](images/azure3.png)

**Step 4:** Now your application is created. Save the *Application ID* and *Directory ID* as they will be needed for onboarding on AccuKnox SaaS, then click on 'Add a certificate or secret'

![image](images/azure4.png)

**Step 5:** Click on new client secret and enter the name and expiration date to get *secret id* and *secret value*, save this secret value as this will also be needed for onboarding.

![image](images/azure5.png)

**Step 6:** Next, go to *API permissions* tab and click on 'Add permission'

![image](images/azure5-0.png)

**Step 7:** On the screen that appears, click on 'Microsoft Graph'

![image](images/azure5-1.png)

**Step 8:** Select Application Permissions and add each of the following permissions:

- `Directory.Read.All`
- `Application.Read.All`
- `AuditLog.Read.All`
- `AuditLogsQuery-CRM.Read.All`
- `AuditLogsQuery.Read.All`

![image](images/azure5-2.png)

**Step 9:** Select ‘Grant Admin Consent’ for Default Directory and click on ‘Yes’. Confirm all permissions show a Granted status.

![image](images/azure5-3.png)

**Step 10:** Now we need to give Security read permissions to this registered Application , to do that go to subscriptions

![image](images/azure6.png)

**Step 11:** First save the subscription ID and click on the subscription name , here it is “Microsoft Azure Sponsorship“

![image](images/azure7.png)

**Step 12:** Navigate to Access control(IAM) and go to Roles , here select **Add > Add Custom Role**

![image](https://learn.microsoft.com/en-us/azure/role-based-access-control/media/custom-roles-portal/add-custom-role-menu.png)

Create a custom role with the following actions:

```
Microsoft.MachineLearningServices/workspaces/onlineEndpoints/score/action
Microsoft.MachineLearningServices/workspaces/serverlessEndpoints/listKeys/action
Microsoft.MachineLearningServices/workspaces/datastores/listSecrets/action
Microsoft.MachineLearningServices/workspaces/listStorageAccountKeys/action
Microsoft.CognitiveServices/accounts/listKeys/action
Microsoft.CognitiveServices/accounts/deployments/read
Microsoft.Storage/storageAccounts/listKeys/action
```

It will look similar to this (use the above listed permissions):
![Azure custom role JSON editor view in Azure Portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/media/custom-roles-portal/json.png)

**Step 13:** Apply the following built-in roles to the registered application: **Reader**, **Cognitive Services OpenAI User**, **Cognitive Services User**, and **Storage Blob Data Reader**.

For each role:

1. Go to **Azure Portal** → **Subscriptions** (or **Resource Groups**) → select your target scope.
2. Open **Access control (IAM)** → click **Add > Add role assignment**.
3. In the **Role** tab, search for and select the role, then click **Next**.

    *Example: selecting the Reader role*

    ![image](images/azure-aiml-reader.png)

    *Example: selecting the Storage Blob Data Reader role*

    ![image](images/azure-aiml-blob-role.png)

4. In the **Members** tab, click **Select members** and search for the application you registered.

    ![image](images/azure-aiml-blob-member.png)

5. Select the application (e.g., AccuKnox Azure CSPM Org Scanner) and click **Review + assign**.

    ![image](images/azure-aiml-blob-selected.png)

Repeat this process for all four roles.


!!! tip "Using Copilot Studio?"
    If you're integrating with Microsoft Copilot Studio (CP Studio), complete the [Copilot Studio integration steps](https://help.accuknox.com/integrations/copilot-studio/) before proceeding to the AccuKnox SaaS UI onboarding below.

## **From AccuKnox SaaS UI**

Configuring your Azure cloud account is complete. Now we need to onboard the cloud account onto the AccuKnox SaaS Platform.

**Step 1:** Go to **Settings → Cloud Accounts** and click on **Add Account**

![image](images/azure12.png)

**Step 2:** Select Microsoft Azure as Cloud Account Type

![image](images/azure13.png)

**Step 3:** Select or create label and Tags that will be associated with this Cloud Account

![image](images/azure14.png)

**Step 4:** Enter the details saved during app registration (Application ID, Directory ID, Secret Value) and the Subscription ID from the Azure portal. **Check the "AI/ML Assets" box** to enable AI/ML asset discovery and monitoring. Click Connect.

![image](images/azure-onboarding-options.png)

**Step 5:** After successfully connecting your cloud account will show up in the list

![image](images/azure16.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
