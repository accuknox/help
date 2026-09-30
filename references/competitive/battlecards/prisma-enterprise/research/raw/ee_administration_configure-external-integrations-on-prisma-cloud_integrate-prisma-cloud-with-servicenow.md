> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow.md).

# Integrate Prisma Cloud with ServiceNow

Learn how to integrate Prisma® Cloud with ServiceNow to help you prioritize and respond to Security incidents on ServiceNow.

Integrate Prisma® Cloud with ServiceNow and get automatically notified about Prisma Cloud alerts through ServiceNow tickets to prioritize incidents and vulnerabilities that impact your business. Prisma Cloud integrates with the ITSM module (incident table), the Security Incident Response module (sn\_si\_incident table), and the Event Management modules (em\_event table) on ServiceNow to generate alerts in the form of ITSM Incident, Security Incident, and Event tickets.

Prisma Cloud also supports OAuth 2.0 for ServiceNow integration, establishing a standardized and secure authentication framework for heightened security, simplifying access token management, allowing Prisma Cloud to interact seamlessly with ServiceNow on your behalf, without exposing sensitive credentials. This reduces the risk of unauthorized access while ensuring a more efficient and secure integration experience.

After you enable the integration, when Prisma Cloud scans your cloud resources and detects a policy violation, it generates an alert and pushes it to ServiceNow as a ticket. When you dismiss an alert on Prisma Cloud, Prisma Cloud sends a state change notification to update the ticket status on ServiceNow. This integration seamlessly fits in to the existing workflows for incident management (ITSM), security operations management (Security Incident Response) or event management for your organization.

The Prisma Cloud integration with ServiceNow is qualified with the most recent cloud-based GA versions of ServiceNow; the on-premise versions are not supported.

If you are using a ServiceNow developer instance, make sure that it is not hibernating.

1. [Set Up Permissions on ServiceNow](#idce37e68b-d094-4b6b-a5d4-ab21d092fd36)
2. [Enable the ServiceNow Integration on Prisma Cloud](#idc4548ecb-5da3-4de2-8072-7f0c3df02de3)
3. [View Alerts](#id46a9b2b8-8b2a-4b68-b65e-d8c15dd574d2)
4. [Manage your ServiceNow integration](#manage-snow-integration)

If you see errors, review how to [Interpret Error Messages](#iddd0aaa90-d099-4a99-a3ed-bde105354340).

## Set Up Permissions on ServiceNow

To integrate Prisma Cloud and ServiceNow, you must have the privileges on ServiceNow to configure users, roles, fields on ServiceNow, which then allow you to set up the data mapping for the Notification Templates on Prisma Cloud.

If you do not have the privileges required listed below, you must work with your ServiceNow administrator.

1. **Prerequisites for the Prisma Cloud and ServiceNow Integration**
   1. You must have permissions to create a local user account on ServiceNow.

      Create a `Username` and `password` that are local on the instance itself. A local user account is a requirement because the ServiceNow web services cannot authenticate against an LDAP or SSO Identity provider and it is unlike the authentication flow that ServiceNow supports for typical administrative users who access the service using a web browser.Refer to the [ServiceNow documentation](https://docs.servicenow.com/bundle/london-platform-administration/page/administer/roles/reference/r_BaseSystemRoles.html) for more information.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-81880fb1a95e9ab81c992fc09ef433a4cc640a63%2Fservicenow-dev-instance.png?alt=media" alt="servicenow dev instance"><figcaption></figcaption></figure>
   2. Review the ServiceNow roles required.

      Prisma Cloud has verified that the following roles provide the required permissions. If your implementation has different roles and RBAC mechanisms, work with your ServiceNow administrator.

      **New York, Orlando, and Paris**

      * tt:\[Optional] `personalize` for accessing tables.

        Personalize role is recommended to support type-ahead fields in notification templates for ServiceNow on Prisma Cloud. With this permission, when you enter a minimum of three characters in a type-ahead field, this role enables you to view the list of available options. If you do not enable personalize permissions, you must give table specific read-access permissions for type-ahead inputs.
      * `evt_mgmt_integration` basic role has create access to the Event \[em\_event] and Registered Nodes \[em\_registered\_nodes] tables to integrate with external event sources.
      * `itil` role is required for the incident table actions.
      * `sn_si.basic` role is required for the sn\_si.incident security incident table actions.
   3. For the user you added earlier, create a custom role with the permissions listed above.

      These permissions are required to create tickets and access the data in the respective ITSM, Events, and Security Incident Response tables and fields on ServiceNow.

      Prisma Cloud needs access to the Plugins (**V\_plugin**), Dictionary (**sys\_dictionary**), and Choice Lists (**sys\_choices**) tables to fetch data from the ServiceNow fields. You can view this information in the ServiceNow notification templates that enable you to customize Prisma Cloud alerts in ServiceNow.

      1. Select **User Administration > Roles** to create a new role and assign it to the local administrative user you created earlier.
      2. Pick a table, such as the **Plugins** table, and select the menu (“hamburger”) icon next to a table column header to **Configure > Table**.
      3. [Elevate the role](https://docs.servicenow.com/bundle/madrid-servicenow-platform/page/administer/security/task/t_ElevateToAPrivilegedRole.html) to security\_admin to enable modification of the access control list (ACL).

         <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-fe47820f994214e4e4459335e69c8b54b61fec34%2Fservicenow-elevate-role.png?alt=media" alt="servicenow elevate role"><figcaption></figcaption></figure>
      4. Select **Access Controls > New**.
      5. Set **Operation** to **Read** and assign this permission to the role.

         <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-be279ea51e2a63a4c9884558f878d11753cd2310%2Fservicenow-assign-role.png?alt=media" alt="servicenow assign role"><figcaption></figcaption></figure>
      6. Enable permissions for the remaining tables and assign them to the same role.

         Verify that all three tables—Plugins (**V\_plugin**), Dictionary (**sys\_dictionary**), and Choice Lists (**sys\_choices**) have the role and the required permission especially if you have defined field-level ACL rules to restrict access to objects in your ServiceNow implementation.
   4. You must be familiar with the fields and field-types in your ServiceNow implementation to set up the Notification templates on Prisma Cloud. Because this knowledge is essential for setting up the mapping of the Prisma Cloud alert payload to the corresponding fields on ServiceNow, you must work with your ServiceNow administrator to successfully enable this integration.
2. **Prerequisites for the Security Incident Module**

   The Security Incident Response plugin is optional but is required if you want to generate Security Incident tickets. To create Security Incident tickets, you must also have the Security Incident Response plugin installed on your ServiceNow instance.

   Verify that the Security Incident Response plugin is activated. To activate a plugin you must be ServiceNow administrator; if you do not see the plugin in the list, verify that you have purchased the subscription.
3. **Prerequisites for the Event Management Module**

   The Event Management plugin is optional but is required if you want to generate Event tickets on ServiceNow. To create Event tickets, you must have the Event Management subscription and the plugin installed on your ServiceNow instance.

   Verify that the Event Management plugin is [activated](https://docs.servicenow.com/bundle/newyork-it-operations-management/page/product/event-management/task/t_EMActivatePlugin.html). To activate a plugin you must be ServiceNow administrator; if you do not see the plugin in the list, verify that you have purchased the subscription.
4. **Prerequisites to set up OAuth 2.0**

   Setting up Oauth 2.0 is optional. If you want to connect ServiceNow using OAuth 2.0, you must complete the following prerequisite steps on your ServiceNow instance to set up OAuth 2.0 for Inbound REST APIs.

   1. Log in to your ServiceNow instance using Admin credentials and go to the **System OAuth > Application Registry**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-558d3829d8646045e4178ef5008ca434681d64e0%2Fsetup-snow-1.png?alt=media" alt="setup snow 1"><figcaption></figcaption></figure>
   2. Select **New**, you will be directed to the Interceptor page.
   3. Select **Create an OAuth API endpoint for external clients** and enter the following details.
      * **Name** - Enter a meaningful name to identify Prisma Cloud.
      * **Client ID** - The ServiceNow OAuth server will automatically generate this.
      * **Client Secret** - Leave the Client Secret blank for the ServiceNow OAuth server to generate a secret automatically.
      * **Refresh Token Lifespan** - The default value is 8,640,000 seconds (100 days) and can be increased or decreased. This means, that after 100 days, you must reauthorize the OAuth connection. As a best practice, increasing the lifespan to a larger value reduces manual reauthorization. The max value is 2,147,483,647 seconds (\~68 years).
      * **Access Token Lifespan** - The default value is 1800 seconds (30 Minutes) and can be increased or decreased.

        <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e75d82a0b2ec09b7bcb48dc8c2229068c186c8be%2Fsetup-snow-2.png?alt=media" alt="setup snow 2"><figcaption></figcaption></figure>
   4. Click **Submit**. You will be directed to the **Application Registries** page.
   5. Select the record that you added. For example, PrismaCloudOAuth2.0.
   6. Copy the **Client ID**, **Client Secret**, and **Refresh Token Lifespan** details.

      You will need to enter the token while [enabling ServiceNow as an external integration](#idc4548ecb-5da3-4de2-8072-7f0c3df02de3) on Prisma Cloud.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-db16a68e05e256e24292d577f6b773e124db6592%2Fsetup-snow-3.png?alt=media" alt="setup snow 3"><figcaption></figcaption></figure>
5. **Generate Refresh Token**

   Perform the following steps to generate a refresh token to be added while connecting ServiceNow using OAuth 2.0.

   (tt:\[NOTE]) As a best practice, use Postman to generate the refresh token.

   1. Log in to **Postman** and set the **HTTP Method as POST**.
      1. Enter the Endpoint URL as follows: [https://\<your-servicenow-instanceName>.service-now.com/oauth\_token.do](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/administration/configure-external-integrations-on-prisma-cloud/https:/%3Cyour-servicenow-instanceName%3E.service-now.com/oauth_token.do)

         This is the default endpoint for getting access tokens.

         For example: <https://dev123456.service-now.com/oauth_token.do>
      2. Request Parameters must be sent in the HTTP POST **Body**.
      3. Requests should be formatted as `x-www-form-urlencoded`.
   2. Enter the following request parameters (JSON Key Values) and then click **Send**.
      * `grant_type`— `password`
      * `client_id`— `<client_id-generated-in-servicenow-instance>`
      * `client_secret`— `<client_secret-generated-in-service-now-instance>`
      * `username`— `<your-servicenow-instance-username>`
      * `password`— `<your-servicenow-password>`

        <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-9082089932f0635597d04fa85e7eae4ef02b79a1%2Fgenerate-oauth-token-1.png?alt=media" alt="generate oauth token 1"><figcaption></figcaption></figure>
   3. Copy the `refresh_token` from the response.

      You will need to enter the token when you [Enable ServiceNow as an external integration](#idc4548ecb-5da3-4de2-8072-7f0c3df02de3) on Prisma Cloud.

## Enable the ServiceNow Integration on Prisma Cloud

Perform the following steps to set up ServiceNow as an external integration on Prisma Cloud. If you have an existing ServiceNow Integration on Prisma Cloud, skip to [Edit your ServiceNow Integration to enable Oauth 2.0](#edit-snow-integration).

1. Login to Prisma Cloud, and under **Settings**, select **Integrations & Notifications**.
2. Select **Add Integration > ServiceNow**.
3. Enter a meaningful **Integration Name** and a **Description**.
4. Enter your **FQDN** for accessing ServiceNow.

   Make sure to provide the FQDN for ServiceNow—not the SSO redirect URL or a URL that enables you to bypass the SSO provider (such as sidedoor or login.do) for local authentication on ServiceNow. For example, enter `<yourservicenowinstance>.com` and not any of the following:

   ```
   https://www.<yourservicenowinstance>.com

   <yourservicenowinstance>.com/

   <yourservicenowinstance>.com/sidedoor.do

   <yourservicenowinstance>.com/login.do
   ```

   (tt:\[NOTE]) You cannot modify the FQDN after you save the integration. If you want to change the FQDN for your ServiceNow instance, add a new integration.
5. Choose either **Basic** or **Oauth 2.0** as the **Authentication**.
   1. For **Basic Authentication**, perform the following steps:
      1. Enter the **Username** and **Password** for the ServiceNow administrative user account.

         The ServiceNow web services use the SOAP API that supports basic authentication, whereby the administrative credentials are checked against the instance itself and not against any LDAP or SSO Identity provider. Therefore, you must create a local administrative user account and enter the credentials for that local user account here instead of the SSO credentials of the administrator. This method is standard for SOAP APIs that pass a basic authentication header with the SOAP request.
      2. Select the Service Type for which you want to generate tickets—**Incident**, **Security**, and/or **Event**.

         You must have the plugin installed to create **Security** incident tickets or **Event** tickets; make sure to work with your ServiceNow administrator to install and configure the Security Incident Response module or Event Management module. If you select **Security** only, Prisma Cloud generates all tickets as Security Incident Response (SIR) on ServiceNow.

         <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-ad1a2d1f5d578a7b4829f2cbd851abf8a3d91913%2Fsnow-basic-auth-1.png?alt=media" alt="snow basic auth 1"><figcaption></figcaption></figure>
   2. tt:\[Optional] For **Oauth 2.0 Authentication**, perform the following steps:
      1. Enter the **Client ID** that you had copied earlier from the ServiceNow instance.
      2. Enter the **Client Secret** that you had copied earlier from the ServiceNow instance.
      3. Enter the **Refresh Token** that you had copied from the response in Postman.

         Once the **Refresh Token** expires, you must perform step 5— Generate Refresh Token as described in [Set Up Permissions on ServiceNow](#idce37e68b-d094-4b6b-a5d4-ab21d092fd36) and include it in the Prisma Cloud UI. For example, if you set the token value as 8,640,000 seconds (100 days), then after 100 days, you must reauthorize the OAuth connection.
      4. Enter the **Token Lifespan (In Seconds)** that you had copied earlier from the ServiceNow instance.
      5. Select the **Service Type** for which you want to generate tickets—**Incident**, **Security**, and/or **Event**.

         You must have the plugin installed to create **Security** incident tickets or **Event** tickets; make sure to work with your ServiceNow administrator to install and configure the Security Incident Response module or Event Management module. If you select **Security** only, Prisma Cloud generates all tickets as Security Incident Response (SIR) on ServiceNow.

         <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e570c3c287a4ce4c14610bdf3f91e5a3b0fe389e%2Fsnow-oauth-1.png?alt=media" alt="snow oauth 1"><figcaption></figcaption></figure>
6. Click **Next**, review the **Summary** and then **Test Integration**.

   If you have omitted any of the permissions listed in [Set Up Permissions on ServiceNow](#idce37e68b-d094-4b6b-a5d4-ab21d092fd36), an HTTP 403 error displays.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d4b8104540737035e849e0195c0a9bc6f9d8ec2e%2Fadd-snow-auth-summary.png?alt=media" alt="add snow auth summary"><figcaption></figcaption></figure>
7. **Save Integration** after the testing is successful.

   The integration will be listed on the Integrations page.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-6996d4e12b855d37a807a3f42acb4ae2dba236b9%2Fadd-snow-auth-test.png?alt=media" alt="add snow auth test"><figcaption></figcaption></figure>
8. **Next Steps**

   Continue with setting up the [notification template](/content-collections/administration/configure-external-integrations-on-prisma-cloud/add-notification-template.md), and then verify the status of the integration on **Settings > Integrations**.

## Interpret Error Messages

The following table displays the most common errors when you enable the ServiceNow integration on Prisma Cloud.

<table data-header-hidden><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td>What is Wrong?</td><td>Error Message that Displays</td><td></td></tr><tr><td>The ServiceNow URL you entered is incorrect.</td><td>You must provide an IP address or an FQDN without the protocol http or https</td><td><pre><code>invalid_snow_base_url
</code></pre></td></tr><tr><td>The ServiceNow URL you entered is invalid.</td><td>The FQDN is invalid it should be a valid host name or IP address.</td><td><pre><code>invalid_snow_fqdn
</code></pre></td></tr><tr><td>The ServiceNow URL you entered is not reachable.</td><td>The FQDN provided is either not reachable or is an invalid ServiceNow instance.</td><td><pre><code>snow_network_error
</code></pre></td></tr><tr><td>A required field is missing in the ServiceNow configuration.</td><td>Missing Required Field - {{param}}</td><td><pre><code>missing_required_param, subject - {{param}}
</code></pre></td></tr><tr><td>Your ServiceNow username or password is not valid or is inaccurate.</td><td>Invalid Credentials</td><td><pre><code>invalid_credentials
</code></pre></td></tr><tr><td>The ServiceNow permissions you have enabled are not adequate.</td><td>Required roles or Plugins is/are missing for {{table}}</td><td><pre><code>missing_role_or_plugin, subject - {{table}}
</code></pre></td></tr><tr><td>The Notification template for this integration does not have adequate permissions.</td><td>Insufficient permission to read the field from {{table}} table</td><td><pre><code>insufficient_permission_to_read, subject - {{table}}
</code></pre></td></tr><tr><td>Error Fetching Suggestions For {{table}}</td><td><pre><code>error_fetching_fields_for, subject - {{table}}
</code></pre></td><td></td></tr><tr><td>The ServiceNow integration is not successfully configured.</td><td>Failed Service Now Test - {{reason}}</td><td><pre><code>failed_service_now_test, subject - {{reason}}
</code></pre></td></tr></tbody></table>

## View Alerts

Verify that the integration is working as expected. On the incidents view in ServiceNow, add the Created timestamp in addition to the same columns you enabled in the Prisma Cloud notification template to easily correlate alerts across both administrative consoles.

1. Modify an existing Alert Rule or create a new Alert Rule to [send alert notifications](/content-collections/alerts/send-prisma-cloud-alert-notifications-to-third-party-tools.md) to ServiceNow.
2. Login to ServiceNow to view Prisma Cloud alerts.

   When alert states are updated in Prisma Cloud, they are automatically updated in the corresponding ServiceNow tickets.

   (tt:\[NOTE]) If Prisma Cloud is set to create a new ServiceNow incident through the notification template when an alert state changes from **Resolved > Open** (re-open), do not manually update the incident state. Prisma Cloud will automatically update the incident once the alert is resolved. Manually changing the incident will stop notifications from being sent.

   1. To view incidents (incident table), select **Incidents**.

      In ServiceNow, all the Open Prisma Cloud have an incident state of **New** and all the Resolved or Dismissed alerts have an incident state of **Resolved**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-99a4d2165f897e9e993ee0e833ced04fc088de28%2Fservicenow-alerts.png?alt=media" alt="servicenow alerts"><figcaption></figcaption></figure>
   2. To view security incidents (sn\_si\_incident table), select **Security Incidents**.

      In ServiceNow, all the Open Prisma Cloud alerts have a state of **Draft** and all the Resolved or Dismissed alerts have a state of **Review**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e3552533f987e5aba389e5720d8a9c55b2a81124%2Fservicenow-security-incidents-alerts.png?alt=media" alt="servicenow security incidents alerts"><figcaption></figcaption></figure>
   3. To view event incidents (events table), select **Event Management > All Events**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-942a7e623e308314c0774cbae91ba0c94ecdc4b2%2Fservicenow-event-incidents-alerts.png?alt=media" alt="servicenow event incidents alerts"><figcaption></figcaption></figure>

## Manage your ServiceNow integration

If you have an existing ServiceNow Integration on Prisma Cloud, you can view, edit, or delete an integration from the **Actions** panel on the **Integrations & Notifications** page. The **Actions** panel provides options to manage your integrations and notifications on Prisma Cloud.

<figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-8b7a7947e39c63552f1d20188c151775a8cae455%2Fmanage-snow-integration.png?alt=media" alt="manage snow integration"><figcaption></figcaption></figure>

* **View—** Select the **View** Integration icon on the **Actions** pane. The View ServiceNow Integration page will appear, displaying the current configuration details of the ServiceNow integration.
* **Edit—** Select the **Edit** icon on the **Actions** pane. The Edit ServiceNow Integration page will appear, allowing you to modify relevant configuration details such as enabling Oauth 2.0 Authentication or updating Refresh Token details.
* **Delete—** Select the **Delete** icon on the **Actions** pane to remove the integration.

## Edit your ServiceNow Integration to enable Oauth 2.0

If you have an existing ServiceNow Integration on Prisma Cloud and want to enable the Oauth 2.0 instead of the Basic (default) authentication, then you must perform the following steps.

1. Perform steps 4 and 5 as described in [Set Up Permissions on ServiceNow](#idce37e68b-d094-4b6b-a5d4-ab21d092fd36)
2. Log in to Prisma Cloud and under **Settings**, select **Integrations & Notifications**.
3. Locate the ServiceNow account you want to Edit.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d0d3a1cd09179e0e47782dde437db90b93466a36%2Fedit-snow-integration-1.png?alt=media" alt="edit snow integration 1"><figcaption></figcaption></figure>
4. Select the **Edit** icon on the **Actions** pane. The **Edit ServiceNow Integration** page will appear, allowing you to modify relevant information.
5. Select **Oauth 2.0** as the **Authentication**.
6. Enter the **Client ID** that you had copied earlier from the ServiceNow instance.
7. Enter the **Client Secret** that you had copied earlier from the ServiceNow instance.
8. Enter the **Refresh Token** that you had copied from the response in Postman.

   When the **Refresh Token** expires, you must perform step 5— **Generate Refresh Token** as described in [Set Up Permissions on ServiceNow](#idce37e68b-d094-4b6b-a5d4-ab21d092fd36) and include it in the Prisma Cloud UI. For example, if you set the token value as 8,640,000 seconds (100 days), then after 100 days, you must reauthorize the OAuth connection.
9. Enter the **Token Lifespan (In Seconds)** that you had copied earlier from the ServiceNow instance.
10. Click **Next**.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-1b7253dd8c3a638c5dff3c2efef29b168ecf5bdd%2Fedit-snow-integration-2.png?alt=media" alt="edit snow integration 2"><figcaption></figcaption></figure>
11. Review the **Summary** and then **Test Integration**.
12. **Save Integration** after the testing is successful.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-121ac6de101f8ade2f9c8cebc1db5ea26ee96887%2Fedit-snow-integration-3.png?alt=media" alt="edit snow integration 3"><figcaption></figcaption></figure>


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-servicenow.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
