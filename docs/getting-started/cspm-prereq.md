---
hide:
  - toc
---

## **Cloud Account**
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


Similarly, for Azure or GCP, follow guidelines on AccuKnox SaaS infrastructure in Cloud Onboarding Screen.

