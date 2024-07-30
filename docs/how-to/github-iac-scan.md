# Github IaC Scanning

IaC scans for GitHub are essential for identifying security vulnerabilities in your infrastructure code. By scanning your IaC, you can detect misconfigurations early, ensure compliance with security standards, and prevent potential security breaches. Integrating these scans into your CI/CD pipeline enhances your overall security posture by providing continuous monitoring and assessment.

## Configuration

### Prerequisites

For Github the IaC Scan from AccuKnox SaaS we require three prerequisites. They are as follows:

- Creating Fine-Grained tokens from GitHub for Private Repos only
- Label creation
- Adding the Code repository

### Create Fine-Grained Tokens from GitHub  

For generating the fine-grained access token from GitHub users need to do the following steps.

**Step 1**: Go to the Github profile and select Settings.

![IaC Scan Github](images/github-iac/image2.png)

**Step 2**: Select the Developer Settings in Settings options

![IaC Scan Github](images/github-iac/image5.png)

**Step 3**: Select the Personal Access token→ Fine-Grained Access token
![IaC Scan Github](images/github-iac/image9.png)

**Step 4**: Click on the Generate new token option

![IaC Scan Github](images/github-iac/image15.png)

**Step 5**: Fill out the token name, description, Duration, and Repository that you need to onboard, and in the Repository permission section select the content: Readonly

![IaC Scan Github](images/github-iac/image19.png)

**Step 6**: After this click on Generate token to get the Fine Grained access token with Read-only access to the Repository

![IaC Scan Github](images/github-iac/image6.png)

### Label Creation

After Creating the Fine-grained Access token user needs to create a label from AccuKnox SaaS. For this user need to navigate to the Settings→ label Section click on Add new label and create their label

![IaC Scan Github](images/github-iac/image20.png)

---

### Add Code Repository

After creating the token from Github and Creating the label from AccuKnox SaaS. Users can onboard the Source Code Repository by following the steps below.

**Step 1**: Navigate to the Settings→ Integrations and select the Code Source Configuration

![IaC Scan Github](images/github-iac/image7.png)

**Step 2**: Click on the Add Configuration button

![IaC Scan Github](images/github-iac/image18.png)

**Step3**: Fill in the name select the type as Github input the Repository URL and Fine-grained Access token and click on Verify

![IaC Scan Github](images/github-iac/image13.png)

**Step 4**: After successful Verification, you can select the branch and Label name that was created from the SaaS.

![IaC Scan Github](images/github-iac/image10.png)

**Step 5**: Click on save to add the Source code configuration

![IaC Scan Github](images/github-iac/image14.png)

## IaC scan
---

To create an IaC scan for the added Source Code Configuration users need to perform the following steps.

**Step 1**: Navigate to Settings→ Integrations and select IaC

![IaC Scan Github](images/github-iac/image8.png)

**Step 2**: Click on Add Configuration give the name and select the Repository for which you want to schedule the IaC Scan. Select the Framework type as Kubernetes yaml, helm, or Terraform and click on save to add the IaC configuration.

![IaC Scan Github](images/github-iac/image1.png)

**Step 3**: After saving the IaC Configuration the scan will start in the background and it will be completed sometime.

![IaC Scan Github](images/github-iac/image4.png)

**Step 4**: After the scan is completed the progress will change to 100% completed

![IaC Scan Github](images/github-iac/image11.png)

### Risk Assessment - Check Findings
After the IaC scan is completed to see the findings users need to navigate to the Issues→ Findings section and select IaC findings in the filter to see all the findings.

![IaC Scan Github](images/github-iac/image17.png)

We can filter the findings based on the Repository, Risk Factor, and so on.

---

### Remediation - Fix Problems/Create Tickets

To remediate any findings users will need to select the finding or group of findings From the issues→ Findings page and click Create Ticket as shown in the below screenshot.

![IaC Scan Github](images/github-iac/image12.png)

!!! info "NOTE"
    **Before this users must have integrated their Ticketing backend like Jira Servicenow or connects or Freshservice under Integrations → CSPM section**

After clicking on the create ticket Icon the next page will popup

![IaC Scan Github](images/github-iac/image3.png)

Once the user clicks on Create Ticket new page with all the information related to the IaC findings and with a predefined Priority based on the Risk Factor. The user has to click on Create to confirm the ticket creation.

![IaC Scan Github](images/github-iac/image16.png)
