For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/install/deploy-defender/uninstall-defender.md).

Prisma Cloud automatically uninstalls Defenders that haven’t connected to the Prisma Cloud console for more than a day. Removing the stale Defenders helps keep your view of the environment clean, where you can see the list of connected Defenders for any given 24-hour window, and conserves licenses. The refresh period can be configured up to a maximum of 365 days under **Manage > Defenders > Settings > Automatically remove disconnected Defenders after (days)**.

You can uninstall the decommissioned Defenders from the Console UI or by using the Prisma Cloud API.

We recommend that you let Prisma Cloud automatically uninstall stale Defenders rather than using the UI or API. Automatic removal is recommended in large scale environments.

## Delete Defenders Manually[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/uninstall-defender\#delete-defenders-manually)

**Delete Defenders from Console**

- Go to **Manage > Defenders: Deployed** to see a list of all the Defenders connected to Console.

- Under **Actions**, select **Delete** next to the respective Defender.


**Delete Defenders using the API**

The following endpoint can be used to delete a Defender.

**Path**

AskCopy

```
DELETE /api/v1/defenders/[hostname]
```

Refer to the [Delete a Defender API](https://pan.dev/compute/api/delete-defenders-id/) for more information.

## Force Uninstall Defender[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/uninstall-defender\#force-uninstall-defender)

If a Defender instance is not connected to Prisma Cloud console, or is otherwise not manageable through the UI, you can manually remove it.

Go to the Linux host where the Container Defender runs and use the following command:

AskCopy

```
$ sudo /var/lib/twistlock/scripts/twistlock.sh -u
```

If you run this command on the same Linux host where Prisma Cloud console is installed, it also uninstalls Prisma Cloud console.

On the Linux host where Host Defender runs, use the following command:

AskCopy

```
$ sudo /var/lib/twistlock/scripts/twistlock.sh -u defender-server
```

On the Windows host where Defender runs, use the following command:

AskCopy

```
C:\Program Files\Prisma Cloud\scripts\defender.ps1 -uninstall
```

## Uninstall all Prisma Cloud Resources in a Kubernetes Environment[Direct link to heading](https://docs.prismacloud.io/admin-guide/install/deploy-defender/uninstall-defender\#uninstall-all-prisma-cloud-resources-in-a-kubernetes-environment)

To uninstall all Prisma Cloud resources from a Kubernetes-based deployment, delete the `twistlock` namespace. Deleting this namespace deletes every resource within the namespace.

1. Delete the _twistlock_ namespace.

















AskCopy



```
$ kubectl delete namespaces twistlock
```

2. Clean up Cluster roles and role bindings

















AskCopy



```
$ kubectl delete clusterrole twistlock-view
$ kubectl delete clusterrolebinding twistlock-view-binding
```


[PreviousRedeploy Defenders](https://docs.prismacloud.io/admin-guide/install/deploy-defender/redeploy-defender) [NextDeploy Container Defender](https://docs.prismacloud.io/admin-guide/install/deploy-defender/container)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
