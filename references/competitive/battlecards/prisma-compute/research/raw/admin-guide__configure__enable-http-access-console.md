For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/enable-http-access-console.md).

By default, Prisma Cloud only creates an HTTPS listener for access to Console. In some circumstances, you may wish to enable an HTTP listener as well. Notice that accessing Console over plain, unencrypted HTTP isn’t recommended, as sensitive information can be exposed.

Enabling an HTTP listener simply requires providing a value for it in twistlock.cfg. At first, your configuration file would look like this:

AskCopy

```
#############################################
#     Network configuration
#############################################
# Each port must be set to a unique value (multiple services cannot share the same port)
###### Management console ports #####
# Sets the ports that the Prisma Cloud management website listens on
# The system that you use to configure Prisma Cloud must be able to connect to the Prisma Cloud Console on these ports
# To disable a listener, leave the value empty (e.g. MANAGEMENT_PORT_HTTP=)
# Accessing Console over plain, unencrypted HTTP isn't recommended, as sensitive information can be exposed
MANAGEMENT_PORT_HTTP=
MANAGEMENT_PORT_HTTPS=8083
```

To enable the HTTP listener, your configuration file should look like this:

AskCopy

```
#############################################
#     Network configuration
#############################################
# Each port must be set to a unique value (multiple services cannot share the same port)
###### Management console ports #####
# Sets the ports that the Prisma Cloud management website listens on
# The system that you use to configure Prisma Cloud must be able to connect to the Prisma Cloud Console on these ports
# To enable the HTTP listener, set the value of MANAGEMENT_PORT_HTTP (e.g. MANAGEMENT_PORT_HTTP=8081)
# Accessing Console over plain, unencrypted HTTP isn't recommended, as sensitive information can be exposed
MANAGEMENT_PORT_HTTP=8081
MANAGEMENT_PORT_HTTPS=8083
```

After you’ve updated the configuration file, just rerun _twistlock.sh_ for the changes to take effect. For example:

AskCopy

```
$ sudo ./twistlock.sh -s console
```

[PreviousUser certificate validity period](https://docs.prismacloud.io/admin-guide/configure/user-cert-validity-period) [NextSet different paths for Console and Defender (with daemon sets)](https://docs.prismacloud.io/admin-guide/configure/set-diff-paths-daemon-sets)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
