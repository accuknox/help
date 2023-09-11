---
hide:
  - toc
---

# **Cloud Account Prerequisites**

AccuKnox Saas Platform supports AWS, Microsoft Azure, Google Cloud Platform accounts onboarding. In this section we can find the prerequisites to onboard the cloud accounts

??? "**AWS Cloud Account**"

    AWS onboarding requires creation of an IAM user. Please follow the following steps to provide a user with appropriate read access:

    **Step 1:** Navigate to IAM -> Users and click on Add Users 

    ![](/getting-started/images/iam-user-0.png)

    **Step 2:** Give a username to identify the user

    ![](/getting-started/images/iam-user-1.png)

    **Step 3:** In the "Set Permissions" screen:

    a. Select "Attach policies directly"

    b. Search "ReadOnly", Filter by Type: "AWS managed - job function" and select the policy

    ![](/getting-started/images/iam-user-2.png)

    c. Search "SecurityAudit", Filter by Type: "AWS managed - job function" and select the policy

    ![](/getting-started/images/iam-user-3.png)

    **Step 4:** Finish creating the user. Click on the newly created user and create the Access key and Secret Key from the Security Credentials tab to be used in the Accuknox panel

    ![](/getting-started/images/iam-user-4.png)


??? "**GCP Cloud Account**"

    For GCP there is a requirement for IAM Service Account Access.

    **Step 1:** Log into your Google Cloud console and navigate to IAM Admin > Service Accounts

    ![](/getting-started/images/aws1.png)

    **Step 2:** Click on "Create Service Account".

    ![](/getting-started/images/aws2.png)

    **Step 3:** Enter "AccuKnox" in the "Service account name", then enter "Accuknox API Access" in the description.

    **Step 4:** Click on Continue.

    ![](/getting-started/images/aws3.png)

    **Step 5:** Select the role: Project > Viewer and click Continue.

    ![](/getting-started/images/aws4.png)

    **Step 6:** Click on “Done”

    **Step 7:** To create a “Key” click the created service account

    ![](/getting-started/images/aws5.png)

    **Step 8:** Click Add Key and Create new key

    **Step 9:** Check  the JSON file and create.

    **Note:** The created JSON private key file will be downloaded to your local machine by default.

    ![](/getting-started/images/aws6.png)


??? "**Azure Cloud Account**"

    For Azure Onboarding it is required to register an App and giving Security read access to that App from the Azure portal.

    **Step 1:** Go to your Azure Portal and search for *App registrations* and open it

    ![](/getting-started/images/azure1.png)

    **Step 2:** Here click on *New registration*

    ![](/getting-started/images/azure2.png)


    **Step 3:** Give your application a name, remember this name as it will be used again later, For the rest keep the default settings

    ![](/getting-started/images/azure3.png)


    **Step 4:** Now your application is created,  save *Application ID* and *Directory ID* as they will be needed to for onboarding on Accuknox Saas and then click on ‘Add a certificate or secret’

    ![](/getting-started/images/azure4.png)


    **Step 5:** Click on new client secret and enter the name and expiration date to get *secret id* and *secret value*, save this secret value as this will also be needed for onboarding.

    ![](/getting-started/images/azure5.png)

    **Step 6:** Next, go to *API permissions* tab and click on 'Add  permission'

    ![](/getting-started/images/azure5-0.png)

    **Step 7:** On the screen that appears, click on 'Microsoft Graph'

    ![](/getting-started/images/azure5-1.png)

    **Step 8:** Next, select Application Permissions and then search for Directory.Read.All and click on Add permissions

    ![](/getting-started/images/azure5-2.png)

    **Step 9:** Select ‘Grant Admin Consent’ for Default Directory and click on ‘Yes’

    ![](/getting-started/images/azure5-3.png)


    **Step 10:** Now we need to give Security read permissions to this registered Application , to do that go to subscriptions

    ![](/getting-started/images/azure6.png)


    **Step 11:** First save the subscription ID and click on the subscription name , here it is “Microsoft Azure Sponsorship“

    ![](/getting-started/images/azure7.png)


    **Step 12:** Navigate to Access control(IAM) and go to Roles , here select Add and Add role assignment 

    ![](/getting-started/images/azure8.png)


    **Step 13:** Search for “Security Reader” Job function Role, select it and press *next*

    ![](/getting-started/images/azure9.png)


    **Step 14:** In the member section click on Select *members* it will open a dropdown menu on the right hand side

    ![](/getting-started/images/azure10.png)


    **Step 15:** Here search for the Application that you registered in the beginning , select the application and click on *review and assign*.

    ![](/getting-started/images/azure11.png)

    **Step 16:** Similarly, we have to add another role. This time, search for *Log Analytics Reader*. Select it and click *next*

    ![](/getting-started/images/azure11-0.png)

    **Step 17:** Now, click on *Select members*, select the application that was created similar to the previous role. Finally, click on *Review and Assign*.

    ![](/getting-started/images/azure11-1.png)


<!---Similarly, for Azure or GCP, follow guidelines on AccuKnox SaaS infrastructure in Cloud Onboarding Screen.-->

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }