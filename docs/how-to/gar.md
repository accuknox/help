

## GAR Onboarding

When [Google Artifact Registry](https://cloud.google.com/artifact-registry/docs) with images is onboarded into AccuKnox SaaS platform, the images are scanned continuously. The risks and vulnerabilities associated with these images are identified and shown in the scan results. The vulnerabilities are classified based on the CVSS Scores.

### **Steps to create service account in GCP for onboarding GAR**

**Step 1**: Open the GCP Management Console and sign in with your GCP account credentials. Select the Project in which the GAR registry to be scanned is located

![](images/gar/gar-project.png)

**Step 2**: In the Navigation Menu, goto **IAM & Admin** → **Service Accounts**

![](images/gar/gar-navi.png)

**Step 3**: Create a Service Account by selecting **Create Service Account** at the top

![](images/gar/sa-create.png)

**Step 4**: Fill the Service Account Details such as name, description and then click **Create and Continue**

![](images/gar/sa-continue.png)

**Step 5**: Select Role as **Basic** → **Viewer** for this Service Account,then click **Continue** and **Done**

![](images/gar/sa-role.png)

**Step 6**: Click on the newly created service account from the list

![](images/gar/sa-click.png)

**Step 7**: Navigate to the **Keys** Section. Click on **ADD KEY** and select **Create new key**

![](images/gar/add-key.png)

**Step 8**: Choose the Key Type as **JSON** for the Service Account then **Create**

![](images/gar/select-json.png)

**Note:** The Private Key will be saved to your system automatically. We will require it for onboarding the GAR registry in AccuKnox SaaS.

### **Steps to onboard the registry on AccuKnox SaaS**

**Step 1:** Login to the AccuKnox SaaS and Navigate to Issues → Registry Scan. Click on **Add Registry**

![](images/gar/add-gar.png)

**Step 2:** Enter the Registry Name, Description, Registry Type, GCP Region where the GAR Registry is hosted and in the next field paste the ENTIRE content of the downloaded JSON key file for the service account.

Click on **Test Connection** and then click on the enabled **Save** button

![](images/gar/save-gar.png)

**Step 3:** A popup appears that the registry is added on successful onboarding. Navigate to Issues → Registry Scan to view the scan results. The status of the scan can be checked from the **Scan Queue** tab

![](images/gar/gar-result.png)

- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }