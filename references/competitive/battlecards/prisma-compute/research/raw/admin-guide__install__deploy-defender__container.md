For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container.md).

Install Container Defender on each host that you want Prisma Cloud to protect.

Single Container Defenders can be configured in the Console UI, and then deployed with a curl-bash script. Alternatively, you can use [twistcli to configure](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container/single-defender-cli) and deploy Defender directly on a host.

## Install a single Container Defender (Console UI)[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container\#install-a-single-container-defender-console-ui)

Configure how a single Container Defender will be installed, and then install it with the resulting curl-bash script.

**Prerequisites**:

- Your system meets all minimum [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

- Ensure that the host machine where you installed the Defender can access the Prisma Cloud console the network.

- You have sudo access to the host where you want to deploy the Defender.


\+ image::install-defender-deploy-page.png\[width=800\]

1. Under **Deployment method**, select **Single Defender**.

2. In **Defender type**, select **Container Defender - Linux** or **Container Defender - Windows**.











When you select **Container Defender - Linux**, **Container Runtime Type** field appears.

3. In **Container Runtime Type**, select **Podman** or **Docker**.











When you select Podman, the installation script includes the `--install-podman` argument. If your infrastructure uses a custom Podman runtime socket path, you can specify it using the `--podman-socket` argument.











For example, to use Podman with a custom runtime socket path, the final command would look like this:











`curl -sSL --header "<Bearer TOKEN>###" -X POST <TENANT URL>/api/v1/scripts/defender.sh | sudo bash -s — -c "stage-consoles-cwp.cloud.twistlock.com" -v --install-podman --podman-socket "<custom_runtime_socket_path>"`

4. (Optional) Set a custom communication port (4) for the Defender to use.

5. (Optional) Set a proxy (3) for the Defender to use for the communication with the Console.

6. (Optional) Under **Advanced Settings**, Enable **Assign globally unique names to Hosts** when you have multiple hosts that can have the same hostname (like autoscale groups, and overlapping IP addresses).











After setting the option to **ON**, Prisma Cloud appends a unique identifier, such as ResourceId, to the host’s DNS name. For example, an AWS EC2 host would have the following name: Ip-171-29-1-244.ec2internal-i-04a1dcee6bd148e2d.

7. Copy the installation script command from the right-side panel, which is generated based on the options you have selected. On the target host where Defender is to be installed, paste the command into a shell window and execute it.


The `HOST_FIM_MOUNTS` parameter permits Defender to specify additional host mounts to be monitored. This facilitates the tracking of an expanded set of mount points on the host, in addition to those monitored by default. To configure the `HOST_FIM_MOUNTS` environment variable and install the container defender on a tenant, perform the following steps:

1. Select all the options as per requirement till step 7 above, and copy the install scripts command from the right side panel with details of all options you have selected:

















AskCopy



```
curl -sSL -k --header "authorization: "#####<Bearer TOKEN>####" -X POST https://app0.cloud.twistlock.com/app0panwdev-1234/api/v1/scripts/defender.sh -d '{"port":123}' | sudo bash -s -- -c "app0.cloud.twistlock.com"  --install-podman.
```

2. Remove the tenant and podman(if selected) details from the command to download the defender.sh file using the following command:

















AskCopy



```
curl -sSL -k --header "authorization: "#####<Bearer TOKEN>####" -X POST https://app0.cloud.twistlock.com/app0panwdev-1234/api/v1/scripts/defender.sh -d '{"port":123} > defender.sh
```

3. Edit the downloaded defender.sh to include the `env` variable in the following command:

















AskCopy



```
cat twistlock.sh | bash -s -- ${additional_defender_parameters} -s -a "${console_cn}" --env "HOST_FIM_MONUTS=/mnt/mountpoint1:/mnt/mountpoint2" -b "#####<base64 format>####"  "${defender_type}"
```

4. (Optional) If you have selected Podman in the consolue UI, include\`--install-podman\` argument as below to the install the defender.

















AskCopy



```
sudo defender.sh -c <TENANT URL> --install-podman
```

5. (Optional) If your infrastructure uses a custom Podman runtime socket path, you can specify it using the `--podman-socket` argument. For example, to use Podman with a custom runtime socket path, the final install command would look like this:

















AskCopy



```
sudo defender.sh -c <TENANT URL> --install-podman --podman-socket "<custom_runtime_socket_path>"
```

6. If Podman details are not inlcuded, execute the following command to install the defender on the tenant.

















AskCopy



```
sudo defender.sh -c <TENANT URL>
```


## Verify the Install[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container\#verify-the-install)

Verify that the Defender is installed and connected to Console.

Defender can be deployed and run with full functionality when dockerd is configured with SELinux enabled (--selinux-enabled=true). All features will work normally and without any additional configuration steps required. Prisma Cloud automatically detects the SELinux configuration on a per-host basis and self-configures itself as needed. No action is needed from the user.

1. In Console, go to **Manage > Defenders > Defenders: Deployed**.











Your new Defender should be listed in the table, and the status box should be green and checked.


[PreviousUninstall Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/uninstall-defender) [NextInstall a single Container Defender using the CLI](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container/single-defender-cli)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
