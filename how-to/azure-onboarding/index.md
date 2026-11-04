---
title: Azure Account Onboarding
description: Step-by-step instructions for onboarding an Azure cloud account to AccuKnox SaaS for automated security management.
---

# Azure Account Onboarding

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

**Step 8:** Next, select Application Permissions and then search for Directory.Read.All and click on Add permissions

![image](images/azure5-2.png)

**Step 9:** Select ‘Grant Admin Consent’ for Default Directory and click on ‘Yes’

![image](images/azure5-3.png)

**Step 10:** Now we need to give Security read permissions to this registered Application , to do that go to subscriptions

![image](images/azure6.png)

**Step 11:** First save the subscription ID and click on the subscription name , here it is “Microsoft Azure Sponsorship“

![image](images/azure7.png)

**Step 12:** Navigate to Access control(IAM) and go to Roles , here select Add and Add role assignment

![image](images/azure8.png)

**Step 13:** Search for “Security Reader” Job function Role, select it and press *next*

![image](images/azure9.png)

**Step 14:** In the member section click on Select *members* it will open a dropdown menu on the right hand side

![image](images/azure10.png)

**Step 15:** Here search for the Application that you registered in the beginning , select the application and click on *review and assign*.

![image](images/azure11.png)

**Step 16:** Similarly, we have to add another role. This time, search for *Log Analytics Reader*. Select it and click *next*

![image](images/azure11-0.png)

**Step 17:** Now, click on *Select members*, select the application that was created similar to the previous role. Finally, click on *Review and Assign*.

![image](images/azure11-1.png)

## **From AccuKnox SaaS UI**

Configuring your Azure cloud account is complete. Now we need to onboard the cloud account onto the AccuKnox SaaS Platform.

**Step 1:** Go to **Settings → Cloud Accounts** and click on **Onboard Account**

![image](images/azure12.png)
![image](images/azure12-0.png)

**Step 2:** Select Microsoft Azure as Cloud Account Type

![image](images/azure13.png)

**Step 3:** Select or create label and Tags that will be associated with this Cloud Account

![image](images/azure14.png)

**Step 4:** Follow the steps presented on the next page.

![image](images/azure15.png)

**Step 5:** Enter the details saved earlier during app registration and the subscription ID from the Azure portal, then click **Connect**.

![image](images/azure15-0.png)

**Step 6:** After successfully connecting, your cloud account will show up in the list

![image](images/azure16.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }
