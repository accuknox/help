---
hide:
  - toc
---

# **GCP Account onboarding**
Here, we will see the steps to onboard a GCP cloud account to the AccuKnox SaaS platform

## **GCP IAM Service Account Creation**

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

## **Onboarding in AccuKnox SaaS UI** 

**Step 1:** Click settings -> Cloud Accounts

**Step 2:** Click Add account

![](/getting-started/images/aws7.png)  

**Step 3:** Select GCP as the Cloud Account type

![](/getting-started/images/aws8.png)

**Step 4:** Select the Labels and Tags and click Next

![](/getting-started/images/aws9.png)

**Note:** If there are no labels and tags create new labels and tags via the settings

**Step 5:** Fill the Project ID, Client Email and Private Key(Copy paste the entire content of the JSON private key that was downloaded) then click Connect.

![](/getting-started/images/aws10.png)

**Note:** For Client Email Id copy the mail id from the Service Account > Details section

**Step 6:** Check Settings → Cloud Accounts. You will see your cloud account is added successfully.

![](/getting-started/images/aws11.png)

<!---Similarly, for Azure or GCP, follow guidelines on AccuKnox SaaS infrastructure in Cloud Onboarding Screen.-->

- - - 
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }