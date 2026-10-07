For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-helm.md).

Generate an updated Helm chart for the Defender DaemonSet, and then upgrade to it.

1. Create an updated Defender DaemonSet Helm chart.

















AskCopy



```
$ ./twistcli defender export kubernetes \
     --address <PATH_TO_CONSOLE> \
     --user <ADMIN_USER> \
     --cluster-address <REGION_CODE>.cloud.twistlock.com \
     --helm
```









Get the value for "--address" from "Compute > Manage > System > Utilities > Path to Console".











The value for "--cluster-address" will be only the region, with .cloud.twistlock.com appended.











Example command for the app4, us-west1 stack:

















AskCopy



```
./twistcli defender export kubernetes \
       --address https://us-west1.cloud.twistlock.com/us-4-xxxxxx \
       --user serviceAccountUsername \
       --cluster-address us-west1.cloud.twistlock.com \
       --helm
```









For Prisma Cloud Enterprise Edition, the user is either an access key, or a service account username.

2. Install the updated chart.

















AskCopy



```
$ helm upgrade twistlock-defender-ds \
     --namespace twistlock \
     --recreate-pods
     ./twistlock-defender-helm.tar.gz
```


[PreviousManually upgrade Defender DaemonSets](https://docs.prismacloud.io/admin-guide/upgrade/upgrade-defender-daemonset) [NextAgentless Scanning](https://docs.prismacloud.io/admin-guide/agentless-scanning/agentless-scanning)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
