For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container/single-defender-cli.md).

Use the `twistcli` CLI tool to install a single Container Defender on a Linux host.

**Prerequisites**:

- Your system meets all minimum [system requirements](https://docs.prismacloud.io/admin-guide/install/system-requirements).

- You have sudo access to the host where you want to deploy the Defender.

- You’ve created a service account with the Defender Manager role. twistcl uses the service account to access Console.


1. Verify that the host where you install Defender can connect to the Prisma Cloud console.

2. SSH to the host where you want to install Defender.

3. Download twistcli.

















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
$ sudo ./twistcli defender install standalone container-linux \
     --address https://<CONSOLE> \
     --user <USER>
```

6. Verify Defender was installed correctly.

















AskCopy



```
$ sudo docker ps
CONTAINER ID   IMAGE                                  COMMAND                  CREATED          STATUS         PORTS     NAMES
677c9883c4b6   twistlock/private:defender_21_04_333   "/usr/local/bin/defe…"   11 seconds ago   Up 10 seconds            twistlock_defender_21_04_333
```


## Verify the install[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container/single-defender-cli\#verify-the-install)

Verify that Defender is installed and connected to Console.

Defender can be deployed and run with full functionality when dockerd is configured with SELinux enabled (--selinux-enabled=true). All features will work normally and without any additional configuration steps required. Prisma Cloud automatically detects the SELinux configuration on a per-host basis and self-configures itself as needed. No action is needed from the user.

1. In the Prisma Cloud console, go to **Manage > Defenders > Defenders: Deployed**.











Your new Defender should be listed in the table, and the status box should be green and checked.















![install defender deploy page](https://docs.prismacloud.io/~gitbook/image?url=https%3A%2F%2F991698089-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FjkReOE2QgjHPl2bpbcR3%252Fuploads%252Fgit-blob-6796b54e85de180c48c0a15a70750aadfedda104%252Finstall-defender-deploy-page.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=85e55d54ee2e87a33de0a74ff5bcb61b&sv=3)


[PreviousDeploy Container Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container) [NextDeploy Host Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/host)

Last updated 2 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
