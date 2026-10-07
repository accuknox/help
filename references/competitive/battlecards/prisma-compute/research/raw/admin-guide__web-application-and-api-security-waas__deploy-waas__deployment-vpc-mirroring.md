For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring.md).

WAAS agentless rules inspect HTTP requests and responses through a mirror of the traffic to provide WAAS detections. To optimize the CPU utlization while using WAAS, Prisma Cloud scanner samples only a subset of the mirrored data to discover just the APIs and the scanner does not inspect the request body field, the sensitive request, and the response data.

WAAS can observe a mirror of HTTP traffic flowing to and from CSP (AWS) instances, even if they are not protected by a Prisma Cloud Compute Defender.

VPC Observer is an EC2 instance running a Host defender for VPC Traffic Mirroring. The target instance is configured on a separate instance within the same VPC to receive Out-Of-Band traffic from the unprotected applications on the source instance. These Observers on the target instance inspect Out-Of-Band traffic and send audits of any events they identify to Prisma Cloud console.

To set up WAAS agentless with VPC traffic mirroring, specify the EC2 instances to mirror (exact names or using wildcards or tags) in a VPC, the ports to mirror, and other AWS parameters in a VPC traffic mirroring rule. For each VPC traffic mirroring rule, a VPC Observer will be created in a VPC machine to receive the mirrored traffic (the VPC Observer is an EC2 instance running a host Defender).

Monitoring applications with WAAS agentless through VPC traffic mirroring is subject to limitations, quotas, and checksum offloading as defined in the [AWS documentation](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-limits.html).

## Prerequisites[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#prerequisites)

- To configure WAAS agentless with AWS VPC traffic mirroring, apply the permission template ending in [agentless\_app\_firewall\_permissions\_template.yaml](https://redlock-public.s3.amazonaws.com/waas/aws/agentless_app_firewall_permissions_template.yaml) to AWS CloudFormation console for your account. For detailed instructions on how to apply cloud formation templates, refer to the [AWS documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).











Amazon EC2 Auto Scaling is integrated with this AWS CloudFormation permission template.











Edit the template and replace the "USER-agentless-app-firewall" value with the actual username that you want to grant these permissions.











WAAS agentless permissions policies created in AWS:















![aws agentless permissions stack](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-89d4163688a60b84810345d5cd66338b85a5ff30%252Faws_agentless_permissions_stack.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=5df5d8ce61d98c78982da9870dc490ae&sv=3)











WAAS agentless resources stack deployed in AWS:















![aws agentless setup stack](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-4034e547613440643eb5240868a32752770b95bd%252Faws_agentless_setup_stack.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=b1dcb41c8876b0a2e5ca71f3a6958f26&sv=3)











Optionally, if you onboard your AWS accounts using Prisma Cloud, you can add the necessary WAAS agentless permissions to the same role used by Prisma Cloud. During the setup, provide the Prisma Cloud role as a parameter in the [agentless\_attach\_to\_role\_cft.template](https://redlock-public.s3.amazonaws.com/waas/aws/agentless_attach_to_role_cft.template).

- Create an AWS Cloud account under **Compute > Manage > Cloud accounts** using the `Access key` from your AWS account.











Cloud accounts require **Cloud discovery** to be enabled to discover the EC2 instances to mirror.


## Create a WAAS Agentless Rule for VPC Traffic Mirroring[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#create-a-waas-agentless-rule-for-vpc-traffic-mirroring)

To deploy WAAS agentless with VPC traffic mirroring, create a new rule, configure VPC, define application endpoints, and select protections.

1. Create a WAAS rule under **Defend > WAAS > Agentless > Add rule**.

2. Enter a **Rule Name** and **Notes** (Optional) for describing the rule.

3. Add **VPC Configuration** to allow the mirrored traffic to flow from the source instance to the Prisma Cloud Observer deployed on the target instance.









01. Select **Console address** as the hostname of the Console to connect to.

02. Select the credentials for the AWS **Cloud account** that you configured under **Manage > Cloud accounts**.

03. Choose the AWS **Region** where the mirrored VMs are located in.

04. Enter the **VPC ID** to look for instances to mirror and to deploy the Observer in.

05. Enter the **VPC Subnet ID** to look for instances to be mirrored only in the selected Subnet ID, and to deploy the Observer in.

06. Specify the **Tags** or wildcards identifying the EC2 instances to mirror in any of the following format:









       1. `<key:value>` = Match tags by key and value pair.

       2. `<key:>` = Match tags with key and empty value (for example, AWS tags allow just a key, with no value (empty string)).

       3. `*` = Match all tags.


07. Enter **Instance names** or wildcards to identify the EC2 instances to mirror.











       The instance to mirror is mapped by machine tags:instance names.

08. Enter the **Ports** to mirror.











       You can enter a maximum of 5 ports. Port ranges are not supported.

09. Select the **Observer Instance type** to use for the VPC Observer instance.

10. Enable **Auto scaling** to automatically scale WAAS Observers to handle a large amount of traffic volume or sudden decrease in traffic volume. You can set a limit of maximum instances between 1 and 10.

11. Select **Add**.















       ![create vpc configuration](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-87748daeca7aabe86263fa152c920a2e85c7ac2e%252Fcreate-vpc-configuration.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6496281f89d38dd6f6021abca6197b06&sv=3)











       The Deployment will be done using a dynamically constructed AWS CloudFormation template, programmatically with CloudFormation API. The WAAS rule is not immediately applied, there will be stages of the rules as the VPC configuration is being deployed in AWS. You can track the status of the deployment in the AWS CloudFormation stack, and also on Prisma Cloud Console.


4. (Optional) Toggle to enable **API endpoint discovery**.











When enabled, the Observer inspects the mirrored traffic to and from the remote applications. The Observer reports a list of the endpoints and their resource path in **Compute > Monitor > WAAS > API discovery**.

5. **Save** the rule.











A scheduled scan runs every hour to check for new and deleted EC2 instances based on the VPC configurations instance names and tags. If a change is found in the list of EC2 instances to mirror, the AWS VPC traffic mirroring setup will be updated.











To force a scan, you can click **Update**.


## Add an App (policy) to the Rule[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#add-an-app-policy-to-the-rule)

01. Select a WAAS rule to add an App in.

02. Select **Add app**.

03. In the **App Definition** tab, enter an **App ID**.











    The combination of **Rule name** and **App ID** must be unique across In-Line and Out-Of-Band WAAS policies for Containers, Hosts, and App-Embedded.











    If you have a Swagger or OpenAPI file, click **Import**, and select the file to load.











    If you do not have a Swagger or OpenAPI file, manually define each endpoint by specifying the host, port, and path.









    1. In **Endpoint Setup**, select **Add endpoint**.

    2. Specify an endpoint in your web application that should be protected. Each defined application can have multiple protected endpoints.















       ![add an app vpc traffic mirroring](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-3e81ef1402cc2db3c8b01b0b832630e37ddf011a%252Fadd-an-app-vpc-traffic-mirroring.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=fbcb91bd39534b88fceb5d4579453aa9&sv=3)

    3. Enter **HTTP host** (optional, wildcards supported).











       HTTP hostnames are specified in the form of \[hostname\]:\[external port\].











       The external port is defined as the TCP port on the host, listening for inbound HTTP traffic. If the value of the external port is "80" for non-TLS endpoints or "443" for TLS endpoints, it can be omitted. Examples: "\*.example.site", "docs.example.site", "www.example.site:8080", etc.

    4. Enter **Base path** (optional, wildcards supported) for WAAS to match.











       Examples: "/admin", "/" (root path only), "/\*", /v2/api", etc.

    5. Enable **TLS** if your application uses the TLS protocol.

    6. Select **Create**.

    7. To facilitate inspection, after creating all endpoints, select **View TLS settings** in the endpoint setup menu.











       WAAS TLS settings:









       - **Certificate** \- Copy and paste your server’s certificate and private key into the certificate input box (e.g., `cat server-cert.pem server-key > certs.pem`).


    8. If your application requires [API protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection), select the "API Protection" tab and define for each path the allowed methods, parameters, types, etc. See detailed definition instructions in the [API protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-api-protection) help page.


04. Continue to **App Firewall** tab, and select the protections as shown in the screenshot below:















    ![waas out of band app firewall](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-26e481e5f0e524da11fbd912201f14a7c8132622%252Fwaas_out_of_band_app_firewall.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=43ca53a48b112e984622c647dd00f8fc&sv=3)











    For more information, see [App Firewall settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall).

05. Continue to **DoS protection** tab and select [DoS protection](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-dos-protection) to enable.

06. Continue to **Access Control** tab and select [access controls](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-access-control) to enable.

07. Continue to **Bot protection** tab, and select the protections as shown in the screenshot below:















    ![waas out of band bot protection](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-85d8ce2d7dff8d77a2e2c3c767eee955bef6f798%252Fwaas_out_of_band_bot_protection.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=18fa512f62137e519ab9903657321324&sv=3)











    For more information, see [Bot protections](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-bot-protection).

08. Continue to **Custom rules** tab and select [Custom rules](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-custom-rules) to enable.

09. Continue to **Advanced settings** tab, and set the options shown in the screenshot below:















    ![waas out of band advanced settings](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-d90bdb6e1b431de39a57bca49bce7aa44245a0b1%252Fwaas_out_of_band_advanced_settings.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=7863961d7a701ebbed337e42cd278094&sv=3)











    For more information, see [Advanced settings](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-advanced-settings).

10. Select **Save**.

11. You should be redirected to the **Rule Overview** page.











    Select the created new rule to display **Rule Resources** and for each application a list of **protected endpoints** and **enabled protections**.















    ![waas out of band rule overview](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-76d2c34bdf9d7e3ad0aff8334bdd025bb4bcec8a%252Fwaas_out_of_band_rule_overview.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=df9c4c2e877dd5f436a7c2936280c833&sv=3)

12. Test protected endpoint using the following [sanity tests](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-app-firewall#sanity-tests).

13. Go to **Monitor > Events > WAAS for Agentless** to observe the events generated.











    For more information, see the [WAAS analytics help page](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/waas-analytics)


## VPC Configuration Status[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#vpc-configuration-status)

Once the VPC configuration is saved, a CloudFormation template will be created and deployed in the selected region. You can track the stack deployment stages through Prisma Console.

- **Deploying**: The WAAS rule is getting ready as the Observer is being deployed in the AWS instance and the session is being established between the Observer and the resources.











**Refresh** to view the updated deployment status.

- **Ready**: The WAAS rule is ready to be protecting the selected resources. The Observer will check for new instances (based on the selected tags or instance names) once every hour.

- **Error**: The rule is in error and the deployment failed. Fix the error, and click **Update** to reapply the configuration.

- **Deletion in progress**: The Observer deployment is being torn down, and the session is being terminated.

- **Deletion error**: Error in tearing down the Observer setup on AWS VPC.


![waas agentless rules](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-a5d113ee1ad9ab6c9f3240863fa210144bdd2896%252Fwaas-agentless-rules.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=cf8776f61e5caba8eb45bdd1b97ae940&sv=3)

Use **Refresh** to see the updated status of the rules on the UI.

When the VPC configuration is in **Error** status, an **Update** is allowed to reapply the configuration.

You can **Delete** an Agentless rule, that will tear down the entire VPC stack configuration and resources. Once the rule deletion is complete, the rule will disappear from the Console and the Observer will be uninstalled.

The VPC Observer is installed under **Manage > Defenders > Defenders: Deployed**. A VPC observer can only be deleted if you delete the rule from the Console.

## Update VPC Configurations[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#update-vpc-configurations)

You can edit the VPC configurations only to update the Tags, Instance names, Ports, and Observer instance type. This will update the AWS CloudFormation template, and AWS will create/destroy only the updated AWS resources.

If you update the instance type of the VPC Observer, then AWS will recreate the EC2 instance and there will be a downtime.

![vpc configuration](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-2ef262ac0bc309d637a7facdbaf75ee46aa4cc4a%252Fvpc-configuration.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=0ef5e950940fef03dea6e2dbd1bc3a3b&sv=3)

Edit the fields and **Save** to reapply the configurations.

## WAAS Actions for Out-Of-Band Traffic[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#waas-actions-for-out-of-band-traffic)

The following actions are applicable for the HTTP requests or responses related to the **Out-Of-Band traffic**:

- **Alert** \- An audit is generated for visibility.

- **Disable** \- The WAAS action is disabled.


## Limitations[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#limitations)

**Limitations for setting traffic mirroring imposed by AWS**

- Not all AWS instance types support traffic mirroring, for example, T2 is not supported (relevant for both source and target EC2 instances).

- Some regions don’t currently support the 'm5n.2xlarge' and 'm5n.4xlarge' instance types, so these types cannot be used for VPC Observer (For example, Paris).


**TLS Limitations**

- TLS settings for agentless support TLS 1.0, 1.1, and 1.2.

- Only the following RSA Key Exchange cipher suites are supported:









  - TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA256

  - TLS\_RSA\_WITH\_3DES\_EDE\_CBC\_SHA

  - TLS\_RSA\_WITH\_RC4\_128\_SHA


- TLS connections using extended\_master\_secret(23) in the negotiation are not supported as part of this feature.

- Out-Of-Band does not support HTTP/2 protocol.

- DHKE is not supported due to a lack of information required to generate the encryption key.

- The full handshake process must be captured. Partial transmission or session resumption process inspection won’t be decrypted.

- Same VPC configuration cannot be used to inspect both HTTP and HTTPS traffic, you must create two different Agentless rules, one for each HTTP and HTTPS traffic monitoring.











You must upgrade the VPC Observer through **Manage > Defenders**.


**WAAS Agentless Limitations**

- An EC2 instance can only be attached to one agentless rule.

- An agentless rule can only inspect machines from one VPC and Subnet combination.

- Each agentless rule can only have a maximum of 5 ports in the VPC configuration.

- Changing the VPC observer instance types involves downtime.

- Once the AWS setup is created/updated in the agentless rule, the Observer status is only available on **Manage > Defenders > Defenders: Deployed** page.


## Troubleshoot VPC Traffic Mirroring Errors[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#troubleshoot-vpc-traffic-mirroring-errors)

`Failed to set up VPC traffic mirroring: failed creating AWS stack, status ROLLBACK_COMPLETE`.

When the configuration status shows the following error, as shown in the screenshot below, check the AWS CloudFormation stack events for the error.

![err1 failed to setup vpc](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-49336c38d50b7d6c884e07e427054284e9735f80%252Ferr1-failed-to-setup-vpc.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=d80e24b726aafdf997467ef80f214c65&sv=3)

Some scenarios in the AWS CloudFormation that may lead to the above error are as follows:

### You are not authorized to perform this operation[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#you-are-not-authorized-to-perform-this-operation)

This is because the selected AWS cloud account doesn’t have enough permissions for deployment.

![err2 not authorized](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-e390ce5018836b8370cd78869f39dc3229d2ec17%252Ferr2-not-authorized.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=66d053f031579b46ce54a49852bf72b0&sv=3)

1. Modify the account with the correct permissions as mentioned in the [agentless\_app\_firewall\_permissions\_template.json](https://redlock-public.s3.amazonaws.com/waas/aws/agentless_app_firewall_permissions_template.json) file, and select **Update** to retry the deployment.

2. Delete the rule in error and create a new rule in the AWS Cloud account with the permissions as mentioned in the [agentless\_app\_firewall\_permissions\_template.json](https://redlock-public.s3.amazonaws.com/waas/aws/agentless_app_firewall_permissions_template.json) file to AWS CloudFormation console for your account.


### SessionNumber 1 already in use for eni-\*[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#sessionnumber-1-already-in-use-for-eni)

Trying to mirror an already mirrored EC2 instance (either by WAAS or another product).

![err3 session already in use](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-114b2575ea55ba6a3a7e52f46e7a403cb4583f48%252Ferr3-session-already-in-use.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=56f2a0f0268a7b26420acfe5cbcf683f&sv=3)

1. Edit the VPC configuration and remove the instance from the tags or instance names list, and click **Update** to retry the deployment.

2. Remove the mirroring from the machine from the other rule/other product, and click **Update** to retry the deployment.


### WaitCondition received failed message: 'Defender deployment failed' for uniqueid: i-xxxx.[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#waitcondition-received-failed-message-defender-deployment-failed-for-uniqueid-i-xxxx)

AWS CloudFormation stack failed to deploy the WAAS agentless resources because Prisma Console is not accessible from AWS.

![err4 failedcondition received](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-172c491bcc58fb74b18b298370330687c12fa77e%252Ferr4-failedcondition-received.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3cfa53b248af292b6d54ad0e5612487a&sv=3)

1. Make sure that the IP address of Prisma Console in the VPC configuration is public.

2. Check if the Defender instance has a public IP address.

3. Check if [AWS account can connect with the Prisma Cloud Console](https://docs.prismacloud.io/admin-guide/agentless-scanning/onboard-accounts/onboard-aws) with Console URL that you selected in the VPC configuration.









1. If the Console is not reachable, delete the rule and create a new rule with a valid Prisma Cloud Console URL.

2. If the Console is not reachable due to a firewall rule or other blocking rules, fix the rule to allow the connectivity to the Console, and click **Update** to retry the deployment.

3. Ensure that the Console’s IP address and the ports are reachable by the Defender. Also, the firewall is open with the relevant port and source IPs.


### Failed to find VMs to mirror[Direct link to heading](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-vpc-mirroring\#failed-to-find-vms-to-mirror)

The security token included in the request is invalid.

![err5 failed to find vms](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-c0bc6ce75706d24b5a0da67b3a03d0d62a08753e%252Ferr5-failed-to-find-vms.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=3cf6ce56bd7aefdb72005637d281d588&sv=3)

1. **Edit Configuration** to ensure that the AWS cloud account exists for the user, and also ensure that a correct secret key is used, **Save** the configuration.

2. Click **Update** to reapply the configuration.


[PreviousDeploy WAAS for Serverless](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-serverless) [NextTroubleshooting WAAS](https://docs.prismacloud.io/admin-guide/web-application-and-api-security-waas/deploy-waas/deployment-troubleshooting)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
