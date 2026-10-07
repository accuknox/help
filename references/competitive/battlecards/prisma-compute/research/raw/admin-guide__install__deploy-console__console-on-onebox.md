For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox.md).

Onebox provides a quick, simple way to install both Console and Defender onto a single host. It provides a fully functional, self-contained environment that is suitable for evaluating Prisma Cloud.

## Install Prisma Cloud[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox\#install-prisma-cloud)

Install Onebox with the _twistlock.sh_ install script.

**Prerequisites:**

- Your host meets the minimum [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

- You have a license key.

- Port 8083 is open. Port 8083 (HTTPS) serves the Console UI. You can configure alternative ports in _twistlock.cfg_ before installing.

- Port 8084 is open. Console and Defender communicate with each other on this port.


1. [Download](https://docs.prismacloud.io/admin-guide/welcome/releases#download) the latest Prisma Cloud release to the host where you’ll install Onebox.

2. Extract the tarball. All files must be in the same directory when you run the install.

















AskCopy



```
$ mkdir twistlock
$ tar -xzf prisma_cloud_compute_<VERSION>.tar.gz -C twistlock/
```

3. Configure Prisma Cloud for your environment.











Open _twistlock.cfg_ and review the default settings. The default settings are acceptable for most environments.











If your Docker socket is in a custom location, update _twistlock.cfg_ before continuing. By default, Prisma Cloud expects to find the Docker socket in _/var/run/docker.sock_. If it’s not located there on your host, open _twistlock.cfg_ in an editor, find the DOCKER\_SOCKET variable, and update the path.

4. Install Prisma Cloud.

















AskCopy



```
$ sudo ./twistlock.sh -s onebox
```



























`-s`



















Agree to EULA.























`-z`



















(Optional) Print additional debug messages. Useful for troubleshooting install issues.























`onebox`



















Install both Console and Defender on the same host, which is the recommended configuration. Specify `console` to install just Console.

5. Verify that Prisma Cloud is installed and running:

















AskCopy



```
$ docker ps --format "table {{.ID}}\t{{.Status}}\t{{.Names}}"
CONTAINER ID        STATUS              NAMES
764ecb72207e        Up 5 minutes        twistlock_defender_<VERSION>
be5e385fea32        Up 5 minutes        twistlock_console
```


## Configure Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox\#configure-console)

Create your first admin user and enter your license key.

1. Open Prisma Cloud Console. In a browser window, navigate to 'https://<CONSOLE>:8083', where <CONSOLE> is the IP address or DNS name of the host where Console runs.

2. Create your first admin user.











Consider using _admin_ as the username. It’s a convenient choice because _admin_ is the default user for many of Prisma Cloud’s utilities, including twistcli.

3. Enter your license key.


## Uninstall[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox\#uninstall)

Use the _twistlock.sh_ script to uninstall Prisma Cloud from your host. The script stops and removes all Prisma Cloud containers, removes all Prisma Cloud images, and deletes the _/var/lib/twistlock_ directory, which contains your logs, certificates, and database.

1. Uninstall Prisma Cloud.

















AskCopy



```
$ sudo ./twistlock.sh -u
```

2. Verify that all Prisma Cloud containers have been stopped and removed from your host.

















AskCopy



```
$ docker ps -a
```

3. Verify that all Prisma Cloud images have been removed from your host.

















AskCopy



```
$ docker images
```


## What’s next?[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-onebox\#whats-next)

[Install Defender](https://github.com/PaloAltoNetworks/pc-docs-md/tree/main/compute-edition/34/admin-guide/install/deploy-defender/container/container.md) on each additional host you want to protect.

[PreviousConsole on Fargate](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-fargate) [NextDeploy the Prisma Cloud Console on ACK](https://docs.prismacloud.io/admin-guide/install/deploy-console/console-on-ack)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
