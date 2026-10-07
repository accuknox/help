For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/how-to-guides/configure-listening-ports.md).

This guide shows you how to configure Prisma Cloud to listen on different ports. Typically this type of configuration is made at the load balancer layer, but it can be done directly with Prisma Cloud.

By default Prisma Cloud listens on:

- `8083` HTTPS management port for access to Console.

- `8084` WSS port for Defender **to** Console communication.


**If you are setting the port** _**below**_`1024` **then Prisma Cloud needs permission to access this privileged port. You must also set**`RUN_CONSOLE_AS_ROOT=${RUN_CONSOLE_AS_ROOT:-false}` **to true.**

1. Download and unpack the Prisma Cloud software.

2. Go to the directory where you unpacked the bits.

3. Open _twistlock.cfg_ for editing.









   - `MANAGEMENT_PORT_HTTP` sets the HTTP access port, leaving this blank disables HTTP access.











     Example: `MANAGEMENT_PORT_HTTP=${MANAGEMENT_PORT_HTTP-80}` configures Console to listen on port `80`.

   - `MANAGEMENT_PORT_HTTPS` sets the HTTPS access port.











     Example: `MANAGEMENT_PORT_HTTPS=443` configures Console to to listen on port `443`.

   - `COMMUNICATION_PORT` sets the WSS port used for Defender to Console communication.











     Example: `COMMUNICATION_PORT=9090` configures Console to listen on port `9090`.


4. Run `twistlock.sh` to install Prisma Cloud Console with your settings.











**If you are setting the port** _**below**_`1024` **then Prisma Cloud needs permission to access this privileged port. You must also set**`RUN_CONSOLE_AS_ROOT=${RUN_CONSOLE_AS_ROOT:-false}` **to true.**


[PreviousConfigure an ECS load balancer](https://docs.prismacloud.io/admin-guide/how-to-guides/configure-ecs-loadbalancer) [NextProvision tenant projects OpenShift](https://docs.prismacloud.io/admin-guide/how-to-guides/openshift-provision-tenant-projects)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
