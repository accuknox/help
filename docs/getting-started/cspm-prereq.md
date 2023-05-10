---
hide:
  - toc
---

## **Cloud Account**

??? "**Onboarding AWS Cloud Account**"

    **1. Rapid Onboarding (via AWS)** 

    For AWS there is a requirement for ARN number related to AWS Account
    Login to AWS Account & click top right name icon to get Account ID

    Create a new IAM role & select “trusted entity type” as “AWS service”
    ![](/getting-started/images/cspm-1.jpg)



    ![](/getting-started/images/cspm-2.jpg)

        a.Select S3 service
        b.Ensure “Require MFA” is not selected
        c.Select the “Security Audit” managed policy
        d.Enter a role name and create the role
        e.Click on role name & copy the role ARN

    **2. From AccuKnox SaaS UI** 


    + Click settings -> Cloud Accounts

    + Click Add account

    ![](/getting-started/images/cspm-3.png)

    + Select the Cloud Account type to AWS
    + Select the Connection method to Access key

    ![](/getting-started/images/cspm-4.png)

    + Select the Labels and Tags

        *Note:* If there are no labels and tags create new labels and tags via the settings

    ![](/getting-started/images/cspm-5.png)

    + Fill the fields with Access key and Secret access key of the AWS account

    ![](/getting-started/images/cspm-6.png)

    + Select the regions and click connect

        *Note:* Only the regions that have been specified will have resources scanned.

    + Check Settings → Cloud Accounts. You will see your cloud account is added successfully.

    ![](/getting-started/images/cspm-7.png)

??? "**Onboarding GCP Cloud Account**"

    **1. Rapid Onboarding (via GCP)**

    For GCP there is a requirement for IAM Service Account Access.
    + Log into your Google Cloud console and navigate to IAM Admin > Service Accounts

    ![](/getting-started/images/aws1.png)

    + Click on "Create Service Account".

    ![](/getting-started/images/aws2.png)

    + Enter "AccuKnox" in the "Service account name", then enter "Accuknox API Access" in the description.

    + Click on Continue.

    ![](/getting-started/images/aws3.png)

    + Select the role: Project > Viewer and click Continue.

    ![](/getting-started/images/aws4.png)

    + Click on “Done”

    + To create a “Key” click the created service account

    ![](/getting-started/images/aws5.png)

    + Click Add Key and Create new key

    + Check  the JSON file and create.

    Note: The created JSON private key file will be downloaded to your local machine by default.

    ![](/getting-started/images/aws6.png)

    **2. From AccuKnox SaaS UI** 

    + Click settings -> Cloud Accounts

    + Click Add account

    ![](/getting-started/images/aws7.png)  

    + Select the Cloud Account type to GCP and Click Next

    ![](/getting-started/images/aws8.png)

    + Select the Labels and Tags and click Next

    ![](/getting-started/images/aws9.png)

    Note: If there are no labels and tags create new labels and tags via the settings

    + Fill the Project ID, Client Email and Private Key then click Connect.

    ![](/getting-started/images/aws10.png)

    Note: For Client Email Id copy the mail id from the Service Account > Details section

    + Check Settings → Cloud Accounts. You will see your cloud account is added successfully.

    ![](/getting-started/images/aws11.png)

??? "**Onboarding Azure Cloud Account**"

    **1. Rapid Onboarding (via Azure)** 

    For Azure Onboarding it is required to register an App and giving Security read access to that App from the Azure portal.

    + Go to your Azure Portal and search for App registrations and open it

    ![](/getting-started/images/azure1.png)

    + Here click on New registration 

    ![](/getting-started/images/azure2.png)


    + Give your application a name, remember this name as it will be used again later, For the rest keep the default settings

    ![](/getting-started/images/azure3.png)


    + Now your application is created,  save Application ID and Directory ID as they will be needed to for onboarding on Accuknox Saas and then click on ‘Add a certificate or secret’

    ![](/getting-started/images/azure4.png)


    + Click on new client secret and enter the name and expiration date to get secret id and secret value, save this secret value as this will also be needed for onboarding.

    ![](/getting-started/images/azure5.png)


    + Now we need to give Security read permissions to this registered Application , to do that go to subscriptions

    ![](/getting-started/images/azure6.png)


    + First save the subscription ID and click on the subscription name , here it is “Microsoft Azure Sponsorship“

    ![](/getting-started/images/azure7.png)


    + Navigate to Access control(IAM) and go to Roles , here select Add and Add role assignment 

    ![](/getting-started/images/azure8.png)


    + Search for “Security Reader” Job function Role, select it and press next

    ![](/getting-started/images/azure9.png)


    + In the member section click on Select members it will open a dropdown menu on the right hand side

    ![](/getting-started/images/azure10.png)


    + Here search for the Application that you registered in the beginning , select the application and click on review and assign.

    ![](/getting-started/images/azure11.png)


    **2. From AccuKnox SaaS UI** 

    Configuring your Azure cloud account is complete, now we need to onboard the cloud account onto Accuknox Saas Platform.

    + Go to settings-> Cloud Account and click on Add Account

    ![](/getting-started/images/azure12.png)


    + Select Microsoft Azure as Cloud Account Type and click on next 

    ![](/getting-started/images/azure13.png)


    + Select or create label and Tags that will be associated with this Cloud Account

    ![](/getting-started/images/azure14.png)


    + Enter the details that we saved earlier during the steps for app registration and subscription id from subscriptions in azure portal and click on connect
    
    ![](/getting-started/images/azure15.png)


    + After successfully connecting your cloud account will show up in the list 

    ![](/getting-started/images/azure16.png)


<!---Similarly, for Azure or GCP, follow guidelines on AccuKnox SaaS infrastructure in Cloud Onboarding Screen.-->

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }