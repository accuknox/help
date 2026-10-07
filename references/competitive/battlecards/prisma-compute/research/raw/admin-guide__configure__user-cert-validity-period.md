For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/user-cert-validity-period.md).

User certificates identify a user, and are used to enforce access control policies. You can control how long user certificates are valid. By default, user certificates are valid for 365 days.

## Configuring the validity period of user certificates[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/user-cert-validity-period\#configuring-the-validity-period-of-user-certificates)

Configure the validity period of user certs.

1. Open Console.

2. Go to **Manage > Authentication > Certificates**.

3. Under **Configuration**, enter a new value for **Number of days until expiration of certificate**.

4. Click **Save**.


## Expired user certificates[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/user-cert-validity-period\#expired-user-certificates)

The following message is printed when you try to authenticate with an expired certificate. This example command tries to run `docker ps` on a remote host named prod\_host1.

AskCopy

```
$ docker --tlsverify -H prod_host1:9998 ps
The server probably has client authentication (--tlsverify) enabled.
Please check your TLS client certification settings
```

## Generating new certificates[Direct link to heading](https://docs.prismacloud.io/admin-guide/configure/user-cert-validity-period\#generating-new-certificates)

When your certificates expire, you can generate new ones.

1. Go to Console.

2. Log in with your credentials to reauthenticate with Console. This step generates fresh certificates.









   - If you integrated Prisma Cloud with LDAP, log in with your LDAP credentials.

   - If you integrated with SAML, log in with your SAML credentials.

   - If you are using Prisma Cloud users, log in with your Prisma Cloud user credentials.


3. On the left menu, click **Manage > Authentication > User certificates**.

4. Copy the installation script, and run it on your local machine.











The script installs fresh certificates on your machine.

5. Verify that your certs are valid by running a Docker command on a host protected by Defender.

















AskCopy



```
$ docker --tlsverify -H prod_host1:9998 ps
```


[PreviousConfigure scan intervals](https://docs.prismacloud.io/admin-guide/configure/configure-scan-intervals) [NextEnable HTTP access to Console](https://docs.prismacloud.io/admin-guide/configure/enable-http-access-console)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
