For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/logon-settings.md).

You can control how users access Prisma Cloud with logon settings.

## Setting Console’s token validity period[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/logon-settings\#setting-consoles-token-validity-period)

Prisma Cloud lets you set up long-lived tokens for access to the Console web interface and the API.

For security, users are redirected to the login page when an inactive Console session exceeds a configurable timeout. By default, the timeout is 30 minutes. This configurable timeout value also controls the validity period for API tokens.

For Console web interface tokens:

- If a user explicitly logs out, the claim to access Console is revoked.

- If Console is restarted, all users are automatically logged out.


## Setting Console’s token validity period[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/logon-settings\#setting-consoles-token-validity-period-1)

Tokens are issued to control access to both Console’s web interface and the API. You can set a timeout for Console sessions and a validity period for API tokens.

1. Open Console.

2. Go to **Manage > Authentication > Logon**.

3. Specify a value for **Timeout for inactive Console sessions**.











This value controls:









   - Time, in minutes, that a Console session can be inactive. After the timeout expires, the user is redirected to the login page. In an active session, the token is automatically renewed when the time elapsed is greater than or equal to half the timeout value.

   - Time, in minutes, that an API token is valid. After the token expires, a new one must be retrieved.











     The maximum value permitted for **Timeout for inactive Console sessions** is 71580 minutes.


4. Click **Save**.











After you save your changes, Console redirects you to the login page for your changes to take effect.


## Single sign-on to the Prisma Cloud Support[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/logon-settings\#single-sign-on-to-the-prisma-cloud-support)

Prisma Cloud can allow single sign on and contextual help from the "?" button in the upper right hand corner of each Console page.

Our [https://docs.twistlock.com](https://docs.twistlock.com/) site allows access when a valid token is issued from the Customer. Or in this case, the "?" contextual links can embed the token into the URL used to access the page.

1. Open Console.

2. Go to **Manage > Authentication > Logon**.

3. Set the toggle for **Enable context sensitive help and single sign on to the Twistlock Support site**.











When set to on (default), the token will be embedded into the contextual help link. when set to off, it will not be and you will need to enter the token manually.

4. Click **Save**.











After saving your changes, Console redirects you to the login page for your changes to take effect.


## Basic authentication to Console and API[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/logon-settings\#basic-authentication-to-console-and-api)

Twistlock lets you disable basic authentication to the Console and API. Basic authentication is used in connections from _twistcli_, the API, and Jenkins.

With _twistcli_, you need to use the ' _--token_' option to authenticate with the Console for image scanning and other operations that access Console. This is the same token you receive form the /api/v1/authenticate API endpoint. For more information, see the [API documentation](https://pan.dev/compute/api/).

With the API, you would have use the authenticate endpoint to generate an authentication token to access any of the endpoints. Accessing the APi with Basic Authentication would not be allowed.

With Jenkins, there is no option at this point to use the Jenkins plugin and have basic authentication disabled. An option would be to use _twistcli_ within Jenkins. this would require a step in the pipeline to retrieve an authentication token from the API for the scan to be completed.

1. Open Console.

2. Go to **Manage > Authentication > Logon**.

3. Set the toggle for **Disable basic authentication to Console and API**.











When set to on, basic authentication will be disabled for the Console and API. You will not loose access to the Console from the login page. All of your user account will still be active and will still have access to login to the Console.

4. Click **Save**.











After saving your changes, Console redirects you to the login page for your changes to take effect.


## Strict certificate validation in Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/logon-settings\#strict-certificate-validation-in-defender)

Twistlock Console provides Defender installation scripts which use _curl_ to transfer data from Console. By default, scripts copied from Console append the ' _-k_' option, also known as ' _--insecure_', to curl commands. This option lets curl proceed even if server connections are otherwise considered insecure.

Console provides a global option to disable the ' _-k_' argument for curl commands.

1. Open Console.

2. Go to **Manage > Authentication > Logon**.

3. Set the toggle for **Require strict certificate validation in Defender installation links**.











When set to **On**, Defender installation scripts copied from Console do not use the ' _-k_' option with curl when transferring data from Console. In addition, the piped _sudo bash_ command passes the ' _-v_' option to defender.sh to secure secondary curl commands in the defender.sh script.

4. Click **Save**.











After saving your changes, Console redirects you to the login page for your changes to take effect.


## Strong passwords for local accounts[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/logon-settings\#strong-passwords-for-local-accounts)

Twistlock can enforce the use of a strong password. A strong password has the following requirements:

- Cannot be the same as the username.

- Must be at least 12 characters.

- Must contain one of each of the following: uppercase character, lowercase character, number, special character.

- List of special characters: `~!@#$%^&*()-_=+|[{}];:'\",<.>/?"`


1. Open Console.

2. Go to **Manage > Authentication > Logon**.

3. Set the toggle for **Require strong passwords for local accounts**.











When enabled, strong passwords are required for passwords of newly created accounts or when existing passwords are changed. Enabling this setting doesn’t force existing accounts to change their password or disable access to any accounts.

4. Click **Save**.











After saving your changes, Console redirects you to the login page for your changes to take effect.


[PreviousTags](https://docs.prismacloud.io/admin-guide/configure/tags) [NextReconfigure Prisma Cloud](https://docs.prismacloud.io/admin-guide/configure/reconfigure-twistlock)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
