---
title: Auth0 SSO with AccuKnox
description: Integrate Auth0 with AccuKnox using OpenID Connect (OIDC) for Single Sign-On (SSO) authentication.
---

# Auth0 SSO with AccuKnox

This guide helps you integrate **Auth0** with **AccuKnox** using **OpenID Connect (OIDC)** for Single Sign-On (SSO).

## Prerequisites

- Auth0 account with admin access.
- Access to AccuKnox Tenant for user invitation

## 1. Create Auth0 Application Integration

1. Sign in to your [**Auth0 Dashboard**](https://manage.auth0.com/dashboard/).
2. Navigate to **Applications > Applications**.
![Navigating to Auth0 Applications section](image-18.png)

1. Click **Default Application**.
2. **App Integration Settings**:
    - **App integration name**: Any meaningful name (e.g., `AccuKnox SSO`).
    - **Sign-in redirect URIs**:
      Enter: `https://cspm.accuknox.com/oidc/callback/`
![Auth0 app integration settings with sign-in redirect URI](image-20.png)

1. Leave the other settings including Cross-Origin Authentication as on.
2. Click **Save**.

## 2. Gather Required Information

Once the application is created, you will be redirected to the application's **General** tab. You need to collect specific details to complete the setup with AccuKnox.

- Copy the **Domain**.
- Copy the **Client ID**.
- Copy the **Client Secret**.

![Auth0 application credentials — domain, client ID, client secret](image-19.png)

!!! info "Provide Details to AccuKnox"
    === "SaaS Users"
        - Share the **Client ID**, **Client Secret**, and **Auth0 Domain** securely with the AccuKnox support team.
        - The team will configure the OIDC backend for your organization.

    === "On-Premise Users"
        - You can directly input the configuration into your admin portal: [IDP Providers Configuration Page](https://cspm.accuknox.com/admin/accuknox_oidc_client/idpprovider/)
        - Here is a sample configuration using your Auth0 details:
        ![IDP provider configuration in AccuKnox admin portal](image-47.png)

## 3. Invite Auth0 Users to AccuKnox

1. Log in to the **AccuKnox SaaS console**.
2. Go to **User Management > Invite User**.
3. Enter the **email address** of the user along with other details and send the invite.
![Invite Auth0 user in AccuKnox User Management](image-23.png)

!!! info "Note"
    Ensure the invited Auth0 user has their **email field filled in** within their Auth0 profile. The email must **exactly match** the one used during the AccuKnox invitation.

## 4. Logging in to AccuKnox via Auth0 SSO

1. Navigate to the [AccuKnox Login Page](https://cspm.demo.accuknox.com/).
2. Click **OpenID**.
3. Enter your **organization name**.
![AccuKnox login page with OpenID option selected](image-21.png)

4. You will be redirected to Auth0. Sign in using your **Auth0 credentials**.
5. Upon successful authentication, you will be logged into the AccuKnox dashboard.
![AccuKnox dashboard after successful Auth0 SSO authentication](image-22.png)
