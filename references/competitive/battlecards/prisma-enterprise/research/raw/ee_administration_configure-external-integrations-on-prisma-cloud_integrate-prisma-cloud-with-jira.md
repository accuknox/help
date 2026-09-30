> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-jira.md).

# Integrate Prisma Cloud with Jira

Learn how to integrate Prisma® Cloud with Jira and receive Prisma Cloud alerts in your Jira accounts.

Integrate Prisma® Cloud with Jira to receive Prisma Cloud alert notifications directly in your Jira accounts. This integration automates the process of generating Jira tickets with your existing security workflow.

This integration is compatible with all Jira Cloud and Jira On-Premise versions.

If you have an existing Jira Integration on Prisma Cloud for versions below 9.0 and want to upgrade to Jira 9.0 or higher, you need to [configure](#configure-pc-on-jira-for-9-0-and-above) and [set up a new Jira Integration](#setup-pc-on-jira-for-9-0-and-above). You cannot edit the existing integration to support the newer version.

Additionally, after creating a new Jira integration to support version 9.0 and above, you must add a new [Jira notification template](https://docs.prismacloud.io/en/enterprise-edition/content-collections/administration/configure-external-integrations-on-prisma-cloud/add-notification-template#add-jira-notification-template) to ensure you receive alert notifications. You cannot update the existing notification template to support the newer version as it can lead to errors and will prevent you from receiving notifications.

## Prerequisites

1. To set up this integration, ensure network reachability and [Enable Access to the Prisma Cloud Console](/content-collections/get-started/console-prerequisites.md) if you have a firewall or cloud Network Security Group between the internet and your Jira On-Premise version.
2. You must have Jira administrator privileges to configure Prisma Cloud in your Jira account.

   If you do not have these privileges, coordinate with your Jira administrator to gather the necessary information for enabling communication between Prisma Cloud and Jira.

## Configure Prisma Cloud in your Jira account for Versions prior to 9.0.

Follow these steps to configure Prisma Cloud in your Jira account for versions prior to 9.0.

1. Login to Jira as a Jira Administrator.
2. Locate **Application Links**.
   * For Jira Cloud, select **Jira Settings > Products > Application Links**.

     <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-1ea91dec9e53d7b3091ddfec85fe38d923165079%2Fjira-cloud.png?alt=media" alt="jira cloud"><figcaption></figcaption></figure>
   * For Jira On-Premises, select **Settings > Applications > Application Links**.

     <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-8fdcb41f2a8b32638e9c8142bf8c85e43f1dfaf2%2Fjira-on-prem.png?alt=media" alt="jira on prem"><figcaption></figcaption></figure>
3. Enter the URL for your Prisma Cloud instance in **Configure Application Links** and **Create new link**.

   Refer to [Access Prisma Cloud](/content-collections/get-started/access-prisma-cloud.md) for details on the URL.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-972644c3187587b27c0aab8faedc45724519a53e%2Fjira-create-application.png?alt=media" alt="jira create application"><figcaption></figcaption></figure>
4. Ignore the message in **Configure Application URL** and **Continue**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-2f61b65fe50cc5fc95e3d7b902900b3a0a099eb5%2Fjira-configure-application-url.png?alt=media" alt="jira configure application url"><figcaption></figcaption></figure>
5. Enter the **Application Name**.
6. Select **Generic Application** as the **Application Type**.
7. Enable **Create incoming Link** and select **Continue**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-8750971590966f8025d5805edf8775862c7b8683%2FStep-1-6.png?alt=media" alt="Step 1 6"><figcaption></figcaption></figure>
8. On **Link Applications**, specify a **Consumer Key** and a **Consumer Name**.

   Save the **Consumer Key** for later use when entering information in Prisma Cloud.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-321cbc0065efbf114dfc903223f9f9890c0eeb51%2Fjira-consumer-key.png?alt=media" alt="jira consumer key"><figcaption></figcaption></figure>
9. Copy and paste the **Public Key** shown below and select **Continue**.

   ```
   MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnYoXB+BZ555jUIFyN+0b3g7haTchsyeWwDcUrTcebbDN1jy5zjZ/vp31//L9HzA0WCFtmgj5hhaFcMl1bCFY93oiobsiWsJmMLgDyYBghpManIQ73TEHDIAsV49r2TLtX01iRWSW65CefBHD6b/1rvrhxVDDKjfxgCMLojHBPb7nLqXMxOKrY8s1yCLXyzoFGTN6ankFgyJ0BQh+SMj/hyB59LPVin0bf415ME1FpCJ3yow258sOT7TAJ00ejyyhC3igh+nVQXP+1V0ztpnpfoXUypA7UKvdI0Qf1ZsviyHNwiNg7xgYc+H64cBmAgfcfDNzXyPmJZkM7cGC2y4ukQIDAQAB
   ```

   Prisma Cloud is now successfully configured in your Jira account.

## Setup Jira Integration on Prisma Cloud for Versions prior to 9.0.

Follow these steps to setup Jira integration on Prisma Cloud for versions prior to 9.0.

1. Login to Prisma Cloud.
2. Navigate to **Settings > Integrations & Notifications > Integrations**.
3. Select **Add Integration** and choose **Jira** from the list.
4. Enter the **Integration Name** and optionally, add a **Description**.
5. Do **not** enable the **I am using Jira Server/Data Centre 9.x onwards** checkbox.
6. Enter the **JIRA Login URL**.

   (tt:\[NOTE]) Make sure the URL starts with "https" and does not have a trailing slash (‘/’) at the end.
7. Enter the **Consumer Key** that you created when setting up the Prisma Cloud application in Jira and select **Next**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a61e059c195f2850d010f8b05aa3e87a9a626b29%2Fjira-integration-step-2-7.png?alt=media" alt="jira integration step 2 7"><figcaption></figcaption></figure>
8. Click the secret key URL link to retrieve your secret key.

   The URL with the verification code is valid for only 10 minutes.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-81002a190a8139c0637558e1b30a6fb804c56ba1%2FStep-2-7.png?alt=media" alt="Step 2 7"><figcaption></figcaption></figure>
9. When redirected to the **Welcome to JIRA** page, **Allow** Prisma Cloud read and write access to data in your Jira account.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-2a80778e9679ac307d455e73b4b37ff90a668226%2FStep-2-10.png?alt=media" alt="Step 2 10"><figcaption></figcaption></figure>
10. After allowing access to Prisma Cloud, copy the verification code displayed on the page and paste it as the **Secret Key** in Prisma Cloud.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-af56f63f746fc5a025a52fa0b2418a2713a33832%2Fsecret-verification-1.png?alt=media" alt="secret verification 1"><figcaption></figcaption></figure>

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a23250d5b72d9e3c068bcb29088b37cfd16b4092%2Fsecret-verification-2.png?alt=media" alt="secret verification 2"><figcaption></figcaption></figure>
11. Select **Create Token**.

    Once you see the **Token Created!** message, click **Next**.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-484585a2e131da8362305cdbae0bb553122fbb95%2FStep-2-11.png?alt=media" alt="Step 2 11"><figcaption></figcaption></figure>
12. Review the **Summary** and then **Test Integration**.
13. **Save Integration** if the test is successful.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-3df0cb8dda0ebd472af6f07659f3b3375c74e319%2Fjira-integration-step-2-13.png?alt=media" alt="jira integration step 2 13"><figcaption></figcaption></figure>
14. After successfully setting up the integration, you will find it listed on the **Integrations** page. Use the **Actions** panel to **View**, **Edit**, or **Delete** the integration. You can also periodically check the integration status by clicking on the **Get Status** link.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-a524bd923133f7570b7a1988efcf18b0c49d783a%2Fjira-success-below-9-0.png?alt=media" alt="jira success below 9 0"><figcaption></figcaption></figure>
15. **Next Step**

    [Add a Jira Notification Template](/content-collections/administration/configure-external-integrations-on-prisma-cloud/add-notification-template.md) to configure alert notifications triggered by an alert rule to create Jira tickets.

## Configure Prisma Cloud in your Jira account for Versions 9.0. and Above

Follow these steps to configure Prisma Cloud in your Jira account for versions 9.0 and above.

1. Login to Jira as a Jira Administrator.
2. Navigate to **Applications > Integrations > Application Links**.

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-e2df3bf3f2c02d9c384f7fa20837fe43778027af%2Fconfig-jira-9-0-1.png?alt=media" alt="config jira 9 0 1"><figcaption></figcaption></figure>
3. Select **Create Link**.
4. On the **Create Link** page, specify the following details:
   1. For **Application type**, select **External application**.
   2. For **Direction**, select **Incoming**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f9fe372a4e8e89b71afda2dc6e11ea0d6ef8df13%2Fconfig-jira-9-0-2.png?alt=media" alt="config jira 9 0 2"><figcaption></figcaption></figure>
   3. Select **Continue**.
   4. Enter your Jira admin credentials if prompted. This will take you to the **Configure Incoming Link** page.
5. In the **Configure Incoming Link** page, provide the following details:
   1. Enter a **Name** to identify Prisma Cloud.
   2. Under **Application details > Redirect URL**, enter your Prisma Cloud instance URL in the following format.

      [https://\<your-prisma-cloud-api-url>/auth-code/preview](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/enterprise-edition/content-collections/administration/configure-external-integrations-on-prisma-cloud/https:/%3Cyour-prisma-cloud-api-url%3E/auth-code/preview/README.md).

      For example, if your Prisma Cloud Admin Console URL is <https://app.prismacloud.io>, enter <https://api.prismacloud.io/authcode/preview>

      Refer to the [Prisma Cloud API URL](https://pan.dev/prisma-cloud/api/cspm/api-urls/) for specific URL details.
   3. For **Application Permissions**, choose **Write** permission from the drop-down list.
   4. Select **Save**.

      <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-292c500defe29ee9d826c93249873f53084dbcd6%2Fconfig-jira-9-0-3.png?alt=media" alt="config jira 9 0 3"><figcaption></figcaption></figure>
6. Copy and save the **Client ID** and **Client Secret** from the **Credentials** page. You will need these details when you [set up Jira integration on Prisma Cloud](#setup-pc-on-jira-for-9-0-and-above).

   <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-5ee23c952520f23a7356301cd87ad128cb7d3654%2Fconfig-jira-9-0-4.png?alt=media" alt="config jira 9 0 4"><figcaption></figcaption></figure>

## Setup Jira Integration on Prisma Cloud for Versions 9.0. and Above

Follow these steps to enable Jira integration for versions 9.0 and above on Prisma Cloud.

1. Login to Prisma Cloud.
2. Navigate to **Settings > Integrations & Notifications > Integrations**.
3. Select **Add Integration** and choose **Jira** from the list.
4. Enter the **Integration Name** and, optionally, add a **Description**.
5. Enable the **I am using Jira Server/Data Centre 9.x onwards** checkbox.
6. Enter the **JIRA Login URL**.
7. Enter the **Client ID** copied from your Jira Instance.
8. Enter the **Client Secret** copied from your Jira Instance.
9. **Redirect URI** is automatically populated.

   Verify that the URI in Prisma Cloud matches with the **Redirect URL** in your Jira Instance.
10. Select **Next**.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-5c41d03ef4667883d85f33123c6c81443629fbeb%2Fsetup-jira-9-0-1.png?alt=media" alt="setup jira 9 0 1"><figcaption></figcaption></figure>
11. Click the Auth Code URL link to retrieve your authentication code.

    The URL with the auth code is valid for only 10 minutes.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-2e6cce13da68d9b69f0e70af6bdcca71f0bf564d%2Fsetup-jira-9-0-2.png?alt=media" alt="setup jira 9 0 2"><figcaption></figcaption></figure>
12. When redirected to the JIRA page, **Allow** Prisma Cloud to read and write access to data in your Jira account.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-f20415f3290c3f9b2c2f4ff34cfbcdc112031d25%2Fsetup-jira-9-0-3.png?alt=media" alt="setup jira 9 0 3"><figcaption></figcaption></figure>
13. After allowing access to Prisma Cloud, copy the authentication code displayed on the page and paste it as the **Auth Code** in Prisma Cloud.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-581b74fdbb74dce03c45ee39e8c882d5c9a23055%2Fsetup-jira-9-0-4.png?alt=media" alt="setup jira 9 0 4"><figcaption></figcaption></figure>

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-31e9ad495d037720fd9c7271a5980b83fa47758b%2Fsetup-jira-9-0-5.png?alt=media" alt="setup jira 9 0 5"><figcaption></figcaption></figure>
14. Select **Create Token**.

    Once you see the **Token Created!** message, click **Next**.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-d06b4577522ae114742553bf49a30b514eeab4f7%2Fsetup-jira-9-0-6.png?alt=media" alt="setup jira 9 0 6"><figcaption></figcaption></figure>
15. Review the **Summary** and then **Test Integration**.
16. **Save Integration** if the test is successful.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-abe034a0cdc11011aae5dac88228405a647174b8%2Fsetup-jira-9-0-7.png?alt=media" alt="setup jira 9 0 7"><figcaption></figcaption></figure>
17. After successfully setting up the integration, you will find it listed on the **Integrations** page. Use the **Actions** panel to **View**, **Edit**, or **Delete** the integration. You can also periodically check the integration status by clicking on the **Get Status** link.

    <figure><img src="https://3990409212-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyqPwsbMSaogAot23rTIu%2Fuploads%2Fgit-blob-65046e83d8596a5f3bae220493c1b9274ade97aa%2Fsetup-jira-9-0-8.png?alt=media" alt="setup jira 9 0 8"><figcaption></figcaption></figure>
18. **Next Step**

    [Add a Jira Notification Template](/content-collections/administration/configure-external-integrations-on-prisma-cloud/add-notification-template.md) to configure alert notifications triggered by an alert rule to create Jira tickets.


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/administration/configure-external-integrations-on-prisma-cloud/integrate-prisma-cloud-with-jira.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
