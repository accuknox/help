For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-daemonset.md).

Upgrade the Defender DaemonSets in your environment.

## Upgrade the Defender DaemonSets with twistcli (Kubernetes)[Direct link to heading](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-daemonset\#upgrade-the-defender-daemonsets-with-twistcli-kubernetes)

Delete the Defender DaemonSet, then rerun the original install procedure.

**Prerequisites:** You know all the parameters passed to _twistcli_ when you initially deployed the Defender DaemonSet. You’ll need them to recreate a working configuration file for your environment.

1. Delete the Defender DaemonSet.

















AskCopy



```
$ kubectl -n twistlock delete ds twistlock-defender-ds
$ kubectl -n twistlock delete sa twistlock-service
$ kubectl -n twistlock delete secret twistlock-secrets
```


## Upgrade the Defender DaemonSets with twistcli (OpenShift)[Direct link to heading](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-daemonset\#upgrade-the-defender-daemonsets-with-twistcli-openshift)

Delete the Defender DaemonSet, then rerun the original install procedure.

**Prerequisites:** You know all the parameters passed to _twistcli_ when you initially deployed the Defender DaemonSet. You’ll need them to recreate a working configuration file for your environment.

1. Delete the Defender DaemonSet.

















AskCopy



```
$ oc -n twistlock delete ds twistlock-defender-ds
$ oc -n twistlock delete sa twistlock-service
$ oc -n twistlock delete secret twistlock-secrets
```


## Upgrade the Defender DaemonSets from Console[Direct link to heading](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-daemonset\#upgrade-the-defender-daemonsets-from-console)

Upgrade the Defender DaemonSets directly from the Console UI.

If you can’t access your cluster with kubectl or oc, then you can upgrade Defender DaemonSets directly from the Console UI.

**Prerequisites:** You’ve created a xref:~/authentication/credentials-store/kubernetes-credentials.adoc\[kubeconfig credential\] for your cluster so that Prisma Cloud can access it to upgrade the Defender DaemonSet.

1. Log into Prisma Cloud Console.

2. Go to **Manage > Defenders > Manage**.

3. Click **DaemonSets**.

4. For each cluster in the table, click **Actions > Upgrade**.











The table shows a count of deployed Defenders and their new version number.


[PreviousManually upgrade single Container Defenders](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-single-container) [NextManually upgrade Defender DaemonSets (Helm)](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-helm)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
