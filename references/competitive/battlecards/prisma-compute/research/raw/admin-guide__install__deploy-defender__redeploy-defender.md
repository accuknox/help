For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/redeploy-defender.md).

1. You can **Redeploy** Defenders from under **Manage > Defenders > Auto-defend > DaemonSets** on the UI.











To redeploy Defenders using `twistcli`, generate a new \`DaemonSet\`configuration file:

















AskCopy



```
$ <PLATFORM>./twistcli defender export kubernetes \
       --address <https://yourconsole.example.com:8083> \
       --user <ADMIN_USER> \
       --cluster-address <Prisma Cloud Console address> \
       --container-runtime <value>
```









`--container-runtime`: Container runtime the node uses, either of: crio, containerd, or docker.

2. Delete the old Defenders using your old daemonset config file:

















AskCopy



```
$kubectl delete -f <old-daemonset>.yaml
```

3. To create new Defenders, apply the [in-place updates](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/#in-place-updates-of-resources) to your `Defender` resources.

















AskCopy



```
$ kubectl apply -f <new-daemonset>.yaml
```


[PreviousManage your Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/manage-defender) [NextUninstall Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/uninstall-defender)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
