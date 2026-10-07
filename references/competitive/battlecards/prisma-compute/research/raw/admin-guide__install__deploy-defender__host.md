For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host.md).

Install Host Defender on each host that you want Prisma Cloud to protect.

Single Host Defenders can be configured in the Console UI, and then deployed with a curl-bash script. Alternatively, you can use `twistcli` to configure and deploy Defender directly on a host.

Prisma Cloud Defender requires real-time access to kernel events on the workloads it protects. The use of third-party runtime protection software, such as Microsoft Defender, may block access to these kernel events and disrupt the expected functionality of Prisma Cloud Defender. Ensure that workloads that are protected by Prisma Cloud Defender don’t have such third-party software installed. Deployments that have third-party runtime protection (or similar software that block access to kernel events) installed alongside Prisma Cloud Defender aren’t supported.

## Install a Host Defender (Console UI)[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host\#install-a-host-defender-console-ui)

Host Defenders are installed with a curl-bash script.

**Prerequisites**:

- Your system meets all minimum [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

- Ensure that the host machine where you installed the Defender can access the Prisma Cloud console the network.

- You have `sudo` access to the host where Defender will be installed.


1. Under **Deployment method**, select **Single Defender**.

2. In **Defender type**, select **Host Defender - Linux** or **Host Defender - Windows**.

3. (Optional) Set a custom communication port (4) for the Defender to use.

4. (Optional) Set a proxy (3) for the Defender to use for the communication with the Console.

5. (Optional) Under **Advanced Settings**, Enable **Assign globally unique names to Hosts** when you have multiple hosts that can have the same hostname (like autoscale groups, and overlapping IP addresses).











After setting the option to **ON**, Prisma Cloud appends a unique identifier, such as ResourceId, to the host’s DNS name. For example, an AWS EC2 host would have the following name: Ip-171-29-1-244.ec2internal-i-04a1dcee6bd148e2d.

6. Copy the install scripts command from the right side panel, which is generated according to the options you selected. On the host where you want to install Defender, paste the command into a shell window, and run it.


## Install a single Host Defender (twistcli)[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host\#install-a-single-host-defender-twistcli)

Use `twistcli` to install a single Host Defender on a Linux host.

**Prerequisites**:

- Your system meets all minimum [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

- Console can be accessed over the network from the host where you want to install Defender.

- You have sudo access to the host where Defender will be installed.


1. Verify that the host machine where you install Defender can connect to Console.

















AskCopy



```
$ curl -sk -D - https://<CONSOLE>/api/v1/_ping
```









If curl returns an HTTP response status code of 200, you have connectivity to Console. If you customized the setup when you installed Console, you might need to specify a different port.

2. SSH to the host where you want to install Defender.

3. Download `twistcli`.

















AskCopy



```
$ curl -k \
     -u <USER> \
     -L \
     -o twistcli \
     https://<CONSOLE>/api/v1/util/twistcli
```

4. Make the twistcli binary executable.

















AskCopy



```
$ chmod a+x ./twistcli
```

5. Install Defender.

















AskCopy



```
$ sudo ./twistcli defender install standalone host-linux \
     --address https://<CONSOLE> \
     --user <USER>
```


After the Defender installation is complete, you can configure the `HOST_FIM_MOUNTS` environment variable by updating the /var/lib/twistlock/scripts/defender.conf file. Set the value of this new variable to a colon separated list of the additional mountpoints to track (for example: "/mnt/mountpoint1:/mnt/mountpoint2"). This enables the Defender to track file integrity across the specified mount points.

## Verify the Install[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host\#verify-the-install)

Verify that the Defender is installed and connected to Console.

In Console, go to **Manage > Defenders > Defenders: Deployed**. Your new Defender should be listed in the table, and the status box should be green and checked.

Once the Defender installation is complete, to configure the HOST\_FIM\_MOUNTS environment variable, modify the /var/lib/twistlock/scripts/defender.conf file. Add a name-value pair, where the value is a colon-separated list of the additional mount points to be tracked (for example: "/mnt/mountpoint1:/mnt/mountpoint2"). After making the changes, restart the Defenders to apply the new configuration.

[PreviousInstall a single Container Defender using the CLI](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container/single-defender-cli) [NextAuto-defend Hosts](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host/auto-defend-host)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
