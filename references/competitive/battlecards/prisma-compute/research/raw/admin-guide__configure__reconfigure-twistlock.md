For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/configure/reconfigure-twistlock.md).

In many cases, you will set up _twistlock.cfg_ before you install Prisma Cloud. However, in some cases, you might want to change some parameters in _twistlock.cfg_ after Prisma Cloud has already been installed. To reconfigure Prisma Cloud with an updated _twistlock.cfg_, run the _twistlock.sh_ installer script again.

1. Extract the release tarball to a new location on your host.











Make sure this location does not have any previous Prisma Cloud install files.

















AskCopy



```
$ tar -xvf twistlock_<VERSION>.tar.gz
```

2. Update _twistlock.cfg_ with your new settings.

















AskCopy



```
$ vim twistlock.cfg
```

3. Reload twistlock.cfg.

















AskCopy



```
$ sudo ./twistlock.sh onebox
```









This command assumes that both _twistlock.sh_ and _twistlock.cfg_ reside in the same directory. To specify a configuration file in a different directory, use the -c option.











The old configuration is stored in _/var/lib/twistlock/scripts/twistlock.cfg.old_


[PreviousLogon Settings](https://docs.prismacloud.io/admin-guide/configure/logon-settings) [NextSubject Alternative Names](https://docs.prismacloud.io/admin-guide/configure/subject-alternative-names)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
