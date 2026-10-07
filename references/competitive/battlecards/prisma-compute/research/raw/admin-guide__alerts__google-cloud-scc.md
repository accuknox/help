For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc.md).

Prisma Cloud can be configured as a security source that provides security findings to Google Cloud Security Command Center (SCC). This lets you see all security tool findings in a single place.

Prisma Cloud is a registered Google Cloud Platform Marketplace partner.

## Configuring Google Cloud Security Command Center[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc\#configuring-google-cloud-security-command-center)

In Google Cloud Platform (GCP), create a service account in your project that has the **Cloud Security Command Center API** enabled. You will need the service account keys, API, and Organization ID to enable this feature.

You should have already enabled and onboarded [Prisma Cloud as a Security Source in Google Security Command Center](https://console.cloud.google.com/marketplace/details/twistlock/twistlock). Prisma Cloud supports the alpha and beta versions of Google Security Command Center. The following instructions show how to configure the beta version.

01. Log into your GCP tenant and select the project that has the Cloud Security Command Center API enabled.

02. Go to **IAM & admin > Service accounts**.

03. Click **Create Service Account**.

04. Enter a name and description for the service account.















    ![alerts gcss svc account](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-861267b45c442d2fe709d18dcaf862bb90850de0%252Falerts_gcss_svc_account.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=f2ec254e4f735991e185c49526f47dd6&sv=3)

05. **Grant this service account access to project (optional)** click **continue**. Do not grant a role to the account at this time.

06. **Grant user account to this service account** click **create key**.

07. Set key type to **JSON**, and click **create**. Save the downloaded JSON key.

08. Go to the project’s **APIs & Services > Credentials**.

09. Click **Create credentials > API key**.















    ![alerts gcss api key1](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-ab4ee97f4450e89e76f4291b41e2fea48c39995c%252Falerts_gcss_api_key1.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=de0fb70f4c549eca7725d8850b650cde&sv=3)

10. Save the API key. We recommended that you restrict the key to the **Cloud Security Command Center API**.















    ![alerts gcss api key2](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-54266016ba52c258e9426fa4d52c51eebca56bad%252Falerts_gcss_api_key2.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=a32b3d1ea16797371d91689fa8f37f10&sv=3)

11. Go to the Google tenant’s organizational **IAM & admin**.











    This setting is configured at the organizational level, not the project level.

12. In the **IAM** window click **+Add**.

13. Paste in the name of the service account that has been created.

14. Select Role: **Security Center > Security Center Editor**.















    ![alerts gcss role](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6436b66359eaefbe8203d7c41181476087f6dd53%252Falerts_gcss_role.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=bc2953683e057cbb50ef871bc282a3ba&sv=3)


## Configuring alert frequency[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc\#configuring-alert-frequency)

You can configure the rate at which alerts are emitted. This is a global setting that controls the spamminess of the alert service. Alerts received during the specified period are aggregated into a single alert. For each alert profile, an alert is sent as soon as the first matching event is received. All subsequent alerts are sent once per period.

1. Open Console, and go to **Manage > Alerts**.

2. In **General settings**, select the default frequency for all alerts.











You can specify the following frequencies.









   - **10 Minutes**

   - **1 Hour**

   - **1 Day**.


## Sending alerts to Google Cloud SCC[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc\#sending-alerts-to-google-cloud-scc)

Alert profiles specify which events should trigger the alert machinery, and to which channel alerts are sent. You can send alerts to any combination of channels by creating multiple alert profiles.

Alert profiles consist of two parts:

**(1) Alert settings — Who should get the alerts, and on what channel?** Configure Prisma Cloud to integrate with your messaging service and specify the people or places where alerts should be sent. For example, configure the email channel and specify a list of all the email addresses where alerts should be sent. Or for JIRA, configure the project where the issue should be created, along with the type of issue, priority, assignee, and so on.

**(2) Alert triggers — Which events should trigger an alert to be sent?** Specify which of the rules that make up your overall policy should trigger alerts.

![google cloud scc config](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-0294cfeea2f80896428766ae03688c1501583ef1%252Fgoogle_cloud_scc_config.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3428a7ce98aa01ca2fc24343be3e1d36&sv=3)

If you use multi-factor authentication, you must create an exception or app-specific password to allow Console to authenticate to the service.

## Create new alert profile[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc\#create-new-alert-profile)

Create a new alert profile.

1. In **Manage > Alerts**, click **Add profile**.

2. Enter a name for your alert profile.

3. In **Provider**, select **Security Center**.


## Configure the channel[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc\#configure-the-channel)

Configure the channel.

1. In **Credential**, click **Add new** or select an existing service account.











To create a new xref:~/authentication/credentials-store/gcp-credentials.adoc\[GCP credential\] as needed.

2. In **Source Name**, enter the resource path for a source that’s already been created.











The source name has the following format:

















AskCopy



```
organizations/<organization_id>/sources/<source_id>
```









Where organization\_id and source\_id are numeric identifiers. For example:

















AskCopy



```
organizations/111122222444/sources/43211234
```

3. Click **Send Test Alert** to test the connection.


## Configure the triggers[Direct link to heading](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-scc\#configure-the-triggers)

1. In **Select triggers**, select the events that should trigger an alert to be sent.

2. To specify specific rules that should trigger an alert, deselect **All rules**, and then select any individual rules.















![frag config triggers](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-f044b74e7910113b8b2440284017fa0fc2fcd3ae%252Ffrag_config_triggers.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=01361751c2394c9197d566bd8cc47ebc&sv=3)

3. Click **Next**.


[PreviousGoogle Cloud Pub/Sub](https://docs.prismacloud.io/admin-guide/alerts/google-cloud-pub-sub) [NextIBM Cloud Security Advisor](https://docs.prismacloud.io/admin-guide/alerts/ibm-cloud-security-advisor)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
