For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-onebox.md).

Upgrade Prisma Cloud Onebox. First upgrade Console. Console will then automatically upgrade all deployed Defenders for you.

If Console fails to upgrade one or more Defenders, manually upgrade your Defenders.

You must manually upgrade App-Embedded Defenders.

## Upgrading Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-onebox\#upgrading-console)

To upgrade Console, rerun the install script for the latest version of Prisma Cloud. Use this method for any Console that was originally installed with the _twistlock.sh_ script.

1. [Download](https://docs.prismacloud.io/admin-guide/welcome/releases#download) the latest recommended release.

2. Unpack the downloaded tarball.











Optional: you may wish to unpack the tarball to a different folder than any previous tarballs.

















AskCopy



```
$ mkdir twistlock_<VERSION>
$ tar -xzf prisma_cloud_compute_edition_<VERSION>.tar.gz -C twistlock_<VERSION>/
```









The setup package contains updated versions of _twistlock.sh_ and _twistlock.cfg_.

3. Check the version of Prisma Cloud that will be installed:

















AskCopy



```
$ grep DOCKER_TWISTLOCK_TAG twistlock.cfg
```

4. Upgrade Prisma Cloud while retaining your current data and configs by using the _-j_ option. The _-j_ option merges your current configuration with any new configuration settings in the new version of the software.











You must use the same install target in your upgrade as your original installation. There are two install targets: `onebox` and `console`, where `onebox` installs both Console and Defender onto a host and `console` just installs Console.











To upgrade your `onebox` install, run:

















AskCopy



```
$ sudo ./twistlock.sh -syj onebox
```









To upgrade your `console` install, run:

















AskCopy



```
$ sudo ./twistlock.sh -syj console
```

5. Go to **Manage > Defenders > Manage** and validate that Console has upgraded your Defenders.


[PreviousUpgrade process](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-process-self-hosted) [NextKubernetes](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-kubernetes)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
