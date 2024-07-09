## Azure Sentinel Integration

To forward the events to Azure Sentinel you must first set up the [Azure Sentinel Integration](https://app.accuknox.com/settings/integrations/azure).

###  Integration of Azure Sentinel:
#### a. Prerequisites:
- Azure Logic App - Webhook.
- Azure Sentinel Subscription.

#### b. Steps to Integrate:
- Go to Settings -→ Integrations -→ CWPP(Tab).
- Click integrate now on Azure Sentinel.
- Fill up the following fields:
  - <b>Integration Name:</b> Enter the name for the integration. You can set any name of your choice.
   e.g., `Container Security Alerts`

  - <b>Webhook URL:</b> Enter your Azure Logic App's Webhook URL here.
   e.g., `https://xyz.xxxxx.log ic.azu re.com:443/workflows/xxxxxxxx`

  - <b>Group Name: </b>You can specify any group name based on your prefernece, this can be used to filter the events. This works as a key value pair, where key is Group Name and Group Value is the value for the Key Group Name.
    e.g., `K8s Cluster`

  - <b>Group Value: </b> You can add any value to this group value.
     e.g., `Dev Team Cluster`
-  Click  **Test**  to check the new functionality, You will receive the test message on configured Azure Sentinel.
-`Test message Please ignore !!`
- Click **Save** to save the Integration.
You can now configure [Alert Triggers](./logs_summary/triggers.md) for Azure Sentinel Events


###  Creating webhook using the Azure Logic App
#### About the logic app:
Azure Logic Apps is a cloud platform where you can create and run automated workflows with little to no code. Using the visual designer and selecting from prebuilt operations, you can quickly build a workflow that integrates and manages your apps, data, services, and systems. To create a webhook using the logic app.<br>
- <b>Step 1:</b> Search for the logic app in the Azure portal. <br>
- <b>Step 2:</b> Add the new logic app and fill in the relevant details.<br>
- <b>Step 3:</b> After creating the logic it will appear in the logic app dashboard. <br>
- <b>Step 4:</b> Open the app and click on the go-to resource button.<br>
- <b>Step 5:</b> Select the http request to receive the logs.<br>
- <b>Step 6:</b> Click on the new step and click HTTP after that click on the Azure log analytics to receive the alert data.<br>
- <b>Step 7:</b> Add the connection name, workspaceID, and workspace key you can get workspace id and key in the log analytics workspace tab.<br>
- <b>Step 8:</b> Click on the Integration and click on the Agents tab. <br>
- <b>Step 9:</b> Click on the Azure log analytics data collector and click JSON request body as the body and log name, After the setup is done you will receive a webhook URL. <br>

####  To see Logs in the Sentinel.
- <b>Step 1: </b> Open Microsoft Sentinel in the portal.<br>
- <b>Step 2: </b> Click on the integrations.<br>
- <b>Step 3: </b> Click on the logs tab and go to custom logs and select the time range and click on run the query to get the logs.<br>



