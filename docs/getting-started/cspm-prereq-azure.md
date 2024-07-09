

In SaaS model of deployment the Accuknox CNAPP will be hosted in our cloud environment and scan will be done using the Cloud account Readonly Access permission.

![](images/accuknox-architecture.png)

For Azure Onboarding it is required to register an App and giving Security read access to that App from the Azure portal.

**Step 1:** Go to your Azure Portal and search for *App registrations* and open it

![](images/azure1.png)

**Step 2:** Here click on *New registration*

![](images/azure2.png)


**Step 3:** Give your application a name, remember this name as it will be used again later, For the rest keep the default settings

![](images/azure3.png)


**Step 4:** Now your application is created,  save *Application ID* and *Directory ID* as they will be needed to for onboarding on Accuknox Saas and then click on ‘Add a certificate or secret’

![](images/azure4.png)


**Step 5:** Click on new client secret and enter the name and expiration date to get *secret id* and *secret value*, save this secret value as this will also be needed for onboarding.

![](images/azure5.png)

**Step 6:** Next, go to *API permissions* tab and click on 'Add  permission'

![](images/azure5-0.png)

**Step 7:** On the screen that appears, click on 'Microsoft Graph'

![](images/azure5-1.png)

**Step 8:** Next, select Application Permissions and then search for Directory.Read.All and click on Add permissions

![](images/azure5-2.png)

**Step 9:** Select ‘Grant Admin Consent’ for Default Directory and click on ‘Yes’

![](images/azure5-3.png)


**Step 10:** Now we need to give Security read permissions to this registered Application , to do that go to subscriptions

![](images/azure6.png)


**Step 11:** First save the subscription ID and click on the subscription name , here it is “Microsoft Azure Sponsorship“

![](images/azure7.png)


**Step 12:** Navigate to Access control(IAM) and go to Roles , here select Add and Add role assignment

![](images/azure8.png)


**Step 13:** Search for “Security Reader” Job function Role, select it and press *next*

![](images/azure9.png)


**Step 14:** In the member section click on Select *members* it will open a dropdown menu on the right hand side

![](images/azure10.png)


**Step 15:** Here search for the Application that you registered in the beginning , select the application and click on *review and assign*.

![](images/azure11.png)

**Step 16:** Similarly, we have to add another role. This time, search for *Log Analytics Reader*. Select it and click *next*

![](images/azure11-0.png)

**Step 17:** Now, click on *Select members*, select the application that was created similar to the previous role. Finally, click on *Review and Assign*.

![](images/azure11-1.png)


<!---Similarly, for Azure or GCP, follow guidelines on AccuKnox SaaS infrastructure in Cloud Onboarding Screen.-→

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }