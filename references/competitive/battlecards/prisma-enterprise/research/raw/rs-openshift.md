> For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/kubernetes/openshift.md).

# Deploy Defender on OpenShift v4

Prisma Cloud Defenders are deployed as a DaemonSet, which ensures that an instance of Defender runs on every node in the cluster. You can run Defenders on OpenShift master and infrastructure nodes by removing the taint from them.

The Prisma Cloud Defender container images can be stored either in the internal OpenShift registry or your own Docker v2 compliant registry. This guide shows you how to generate deployment YAML files for Defenders, and then deploy them to your OpenShift cluster with the *oc* client.

To better understand clusters, read our [cluster context](/content-collections/runtime-security/install/cluster-context.md) topic.

## Preflight checklist

To ensure that your installation on supported versions of OpenShift v4.x goes smoothly, work through the following checklist and validate that all requirements are met.

### Minimum system requirements

Validate that the components in your environment (nodes, host operating systems, orchestrator) meet the specs in [System requirements](/content-collections/runtime-security/install/system-requirements.md).

### Permissions

Validate that you have permission to:

* Push to a private docker registry. For most OpenShift setups, the registry runs inside the cluster as a service. You must be able to authenticate with your registry with docker login.
* Pull images from your registry. This might require the creation of a docker-registry secret.
* Have the correct role bindings to pull and push to the registry. For more information, see [Accessing the Registry](https://docs.openshift.com/container-platform/3.10/install_config/registry/accessing_registry.html).
* Create and delete projects in your cluster. For OpenShift installations, a project is created when you run *oc new-project*.
* Run *oc create* commands.

### Network connectivity

Validate that outbound connections to your Console can be made on port 443.

Use [*twistcli*](/content-collections/runtime-security/tools/twistcli.md) to install the Prisma Cloud Defenders in your OpenShift cluster. The *twistcli* utility is included with every release.

### Create an OpenShift project for Prisma Cloud

Create a project named *twistlock*.

1. Login to the OpenShift cluster and create the *twistlock* project:

   ```
     $ oc new-project twistlock
   ```

### (Optional) Push the Prisma Cloud images to a private registry

When Prisma Cloud is deployed to your cluster, the images are retrieved from a registry. You have a number of options for storing the Prisma Cloud Console and Defender images:

* OpenShift internal registry.
* Private Docker v2 registry. You must create a docker-secret to authenticate with the registry.

Your cluster nodes must be able to connect to the Prisma Cloud cloud registry (registry-auth.twistlock.com) with TLS on TCP port 443.

This guides shows you how to use both the OpenShift internal registry and the Prisma Cloud cloud registry. If you’re going to use the Prisma Cloud cloud registry, you can skip this section. Otherwise, this procedure shows you how to pull, tag, and upload the Prisma Cloud images to the OpenShift internal registry’s *twistlock* imageStream.

1. Determine the endpoint for your OpenShift internal registry. Use either the internal registry’s service name or cluster IP.

   ```
     $ oc get svc -n default
     NAME               TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)       AGE
     docker-registry    ClusterIP   172.30.163.181   <none>        5000/TCP      88d
   ```
2. Pull the image from the Prisma Cloud cloud registry using your access token. The major, minor, and patch numerals in the \<VERSION> string are separated with an underscore. For exampe, 18.11.128 would be 18\_11\_128.

   ```
     $ docker pull \
       registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/defender:defender_<VERSION>
   ```
3. Tag the image for the OpenShift internal registry.

   ```
     $ docker tag \
       registry-auth.twistlock.com/tw_<ACCESS_TOKEN>/twistlock/defender:defender_<VERSION> \
       172.30.163.181:5000/twistlock/private:defender_<VERSION>
   ```
4. Push the image to the *twistlock* project’s imageStream.

   ```
     $ docker push 172.30.163.181:5000/twistlock/private:defender_<VERSION>
   ```

## Use OC to Deploy the Defender

You can deploy Defenders using the [OpenShift OC](/content-collections/runtime-security/install/deploy-defender/kubernetes/declarative-object.md).

## Control Defender deployments with taint

You can deploy Defenders to all nodes in an OpenShift cluster (master, infra, compute). OpenShift Container Platform automatically taints infra and master nodes These taints have the NoSchedule effect, which means no pod can be scheduled on them.

To run the Defenders on these nodes, you can either remove the taint or add a toleration to the Defender DaemonSet. Once this is done, the Defender Daemonset will automatically be deployed to these nodes (no need to redeploy the Daemonset). Adjust the guidance in the following procedure according to your organization’s deployment strategy.

* **Option 1 - remove taint all nodes:**

  ```
  $ oc adm taint nodes --all node-role.kubernetes.io/master-
  ```
* **Option 2 - remove taint from specific nodes:**

  ```
  $ oc adm taint nodes <node-name> node-role.kubernetes.io/master-
  ```
* **Option 3 - add tolerations to the twistlock-defender-ds DaemonSet:**

  ```
  $ oc edit ds twistlock-defender-ds -n twistlock
  ```

  Add the following toleration in PodSpec (DaemonSet.spec.template.spec)

  ```
  tolerations:
  - key: "node-role.kubernetes.io/master"
    operator: "Exists"
    effect: "NoSchedule"
  ```

## Uninstall

To uninstall Prisma Cloud, delete the *twistlock* project.

1. Delete the *twistlock* Project

   ```
     $ oc delete project twistlock
   ```


---

# Agent Instructions
This documentation is published with GitBook. GitBook is the documentation platform designed so that both humans and AI agents can read, navigate, and reason over technical content effectively. Learn more at gitbook.com.

## Querying This Documentation
If you need additional information that is not directly available in this page, you can query the documentation dynamically by asking a question.

Perform an HTTP GET request on the current page URL with the `ask` query parameter, and the optional `goal` query parameter:

```
GET https://docs.prismacloud.io/content-collections/runtime-security/install/deploy-defender/kubernetes/openshift.md?ask=<question>&goal=<endgoal>
```

`ask` is the immediate question: it should be specific, self-contained, and written in natural language.
`goal` is optional and describes the broader end goal you are ultimately trying to accomplish on behalf of the user. GitBook uses it to tailor the answer towards what is most useful for that goal.

The response will contain a direct answer to the question and relevant excerpts and sources from the documentation.

Use this mechanism when the answer is not explicitly present in the current page, you need clarification or additional context, or you want to retrieve related documentation sections.
