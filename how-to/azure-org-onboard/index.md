---
title: Onboarding Azure Organization
description: A step-by-step guide to onboarding your Azure Organization to the AccuKnox platform for centralized cloud security management.
---

# Onboarding Azure Organization

Managing security across multiple Azure subscriptions is complex. Onboarding your **Azure Organization** allows for centralized visibility and consistent policy enforcement across all subscriptions.

## 1. Configurations

AccuKnox provides a flexible way to selectively onboard your Azure environment. You can choose to onboard specific Management Groups and Subscriptions or onboard everything while excluding specific parts.

### 1. Onboarding Steps from AccuKnox Control Plane

**Step 1:** Select Microsoft Azure and choose Organization Account, then click Next to begin onboarding the Azure org.
![Azure org onboarding - select cloud provider and account type](image-38.png)

**Step 2:** Set the connection method (Terraform recommended), add a label and tag for the Azure organization, then proceed.
![Azure org onboarding - connection method and label configuration](image-39.png)

**Step 3:** Enter Tenant ID, Management Group, and Subscription scope details to define what the Azure org connection will monitor.
![Azure org onboarding - tenant ID and subscription scope configuration](image-40.png)

Choose the mode that best fits your organizational structure:

=== "Include Mode"

    **Best for:** Onboarding specific departments, staging environments, or a subset of your organization.

    *   **Included Management Groups (`included_management_group_ids`)**: [**Mandatory**]
        Specify the list of Management Group IDs you want to onboard. All subscriptions within these groups will be included.
    *   **Include Extra Subscriptions (`include_extra_subscription_ids`)**: [**Optional**]
        Specify individual Subscription IDs that are *outside* the selected Management Groups but should still be onboarded.
    *   **Exclude Subscriptions (`excluded_subscription_ids`)**: [**Optional**]
        Specify individual Subscription IDs that are *inside* the selected Management Groups but should NOT be onboarded.

=== "Exclude Mode"

    **Best for:** Onboarding the entire organization while omitting specific sensitive or sandbox environments.

    *   **Excluded Management Groups (`excluded_management_groups`)**: [**Mandatory**]
        Specify the list of Management Group IDs you want to **skip**. All other Management Groups under the root will be onboarded.
    *   **Excluded Subscriptions (`excluded_subscription_ids`)**: [**Optional**]
        Specify individual Subscription IDs that you want to **skip**, even if their Management Group is being onboarded.

**Step 4:** Run the provided Terraform script to establish secure connectivity and complete Azure organization onboarding in the Control Plane.
![Azure org onboarding - generate and run Terraform script](image-41.png)

### 2. Generate & Run Terraform Script

Once you have configured the parameters above, click **Generate Terraform**.

1.  **Download** the generated Terraform script.
2.  Open your terminal and execute the following commands:

    **Log in to Azure CLI:**

    ```bash
    az login
    ```

    **Initialize Terraform:**

    ```bash
    terraform init
    ```

    **Apply Configuration:**

    ```bash
    terraform apply
    ```

After a successful run, the user will be able to authorize and view their accounts on the AccuKnox Portal.

---
## 2. Auto-fetch New Subscriptions

Whenever a user creates a new subscription in their account that falls under the onboarded management group, AccuKnox automatically fetches and scans that subscription. To ensure this works correctly, please follow the steps below:

1.  Go to the Subscription in the Azure Portal and search for **Resource providers**.
   ![Resource Providers](image-35.png)
2.  Ensure the following providers are enabled:
    - `Microsoft.ManagedServices`
    - `Microsoft.PolicyInsights`

After approximately **30 minutes**, the subscription will be automatically delegated to AccuKnox, and resources will be queried.


- **User's Azure Account**
![User's Azure Account](image-36.png)
