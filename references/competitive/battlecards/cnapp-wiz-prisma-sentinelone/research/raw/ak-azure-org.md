[Skip to content](https://help.accuknox.com/how-to/azure-org-onboard/#onboarding-azure-organization)

Copy page

Copy page

Copy page as Markdown for LLMs

View as Markdown ↗

View this page as plain text

Open in ChatGPT ↗

Ask questions about this page

Open in Claude ↗

Ask questions about this page

# Onboarding Azure Organization [¶](https://help.accuknox.com/how-to/azure-org-onboard/\#onboarding-azure-organization "Permanent link")

Managing security across multiple Azure subscriptions is complex. Onboarding your **Azure Organization** allows for centralized visibility and consistent policy enforcement across all subscriptions.

## 1\. Configurations [¶](https://help.accuknox.com/how-to/azure-org-onboard/\#1-configurations "Permanent link")

AccuKnox provides a flexible way to selectively onboard your Azure environment. You can choose to onboard specific Management Groups and Subscriptions or onboard everything while excluding specific parts.

### 1\. Onboarding Steps from AccuKnox Control Plane [¶](https://help.accuknox.com/how-to/azure-org-onboard/\#1-onboarding-steps-from-accuknox-control-plane "Permanent link")

**Step 1:** Select Microsoft Azure and choose Organization Account, then click Next to begin onboarding the Azure org.
![Azure org onboarding - select cloud provider and account type](https://help.accuknox.com/how-to/image-38.png)

**Step 2:** Set the connection method (Terraform recommended), add a label and tag for the Azure organization, then proceed.
![Azure org onboarding - connection method and label configuration](https://help.accuknox.com/how-to/image-39.png)

**Step 3:** Enter Tenant ID, Management Group, and Subscription scope details to define what the Azure org connection will monitor.
![Azure org onboarding - tenant ID and subscription scope configuration](https://help.accuknox.com/how-to/image-40.png)

Choose the mode that best fits your organizational structure:

[Include Mode](https://help.accuknox.com/how-to/azure-org-onboard/#__tabbed_1_1)[Exclude Mode](https://help.accuknox.com/how-to/azure-org-onboard/#__tabbed_1_2)

**Best for:** Onboarding specific departments, staging environments, or a subset of your organization.

- **Included Management Groups (`included_management_group_ids`)**: \[ **Mandatory**\]
Specify the list of Management Group IDs you want to onboard. All subscriptions within these groups will be included.
- **Include Extra Subscriptions (`include_extra_subscription_ids`)**: \[ **Optional**\]
Specify individual Subscription IDs that are _outside_ the selected Management Groups but should still be onboarded.
- **Exclude Subscriptions (`excluded_subscription_ids`)**: \[ **Optional**\]
Specify individual Subscription IDs that are _inside_ the selected Management Groups but should NOT be onboarded.

**Best for:** Onboarding the entire organization while omitting specific sensitive or sandbox environments.

- **Excluded Management Groups (`excluded_management_groups`)**: \[ **Mandatory**\]
Specify the list of Management Group IDs you want to **skip**. All other Management Groups under the root will be onboarded.
- **Excluded Subscriptions (`excluded_subscription_ids`)**: \[ **Optional**\]
Specify individual Subscription IDs that you want to **skip**, even if their Management Group is being onboarded.

**Step 4:** Run the provided Terraform script to establish secure connectivity and complete Azure organization onboarding in the Control Plane.
![Azure org onboarding - generate and run Terraform script](https://help.accuknox.com/how-to/image-41.png)

### 2\. Generate & Run Terraform Script [¶](https://help.accuknox.com/how-to/azure-org-onboard/\#2-generate-run-terraform-script "Permanent link")

Once you have configured the parameters above, click **Generate Terraform**.

1. **Download** the generated Terraform script.
2. Open your terminal and execute the following commands:

**Log in to Azure CLI:**



```
az login
```



**Initialize Terraform:**



```
terraform init
```



**Apply Configuration:**



```
terraform apply
```


After a successful run, the user will be able to authorize and view their accounts on the AccuKnox Portal.

* * *

## 2\. Auto-fetch New Subscriptions [¶](https://help.accuknox.com/how-to/azure-org-onboard/\#2-auto-fetch-new-subscriptions "Permanent link")

Whenever a user creates a new subscription in their account that falls under the onboarded management group, AccuKnox automatically fetches and scans that subscription. To ensure this works correctly, please follow the steps below:

1. Go to the Subscription in the Azure Portal and search for **Resource providers**.
    ![Resource Providers](https://help.accuknox.com/how-to/image-35.png)
2. Ensure the following providers are enabled:
   - `Microsoft.ManagedServices`
   - `Microsoft.PolicyInsights`

After approximately **30 minutes**, the subscription will be automatically delegated to AccuKnox, and resources will be queried.

- **User's Azure Account** ![User's Azure Account](https://help.accuknox.com/how-to/image-36.png)

Was this page helpful?











Thanks for your feedback!












Thanks for your feedback! Help us improve this page by using our [feedback form](https://help.accuknox.com/how-to/azure-org-onboard/...).


Back to top