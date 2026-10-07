For the complete documentation index, see [llms.txt](https://docs.prismacloud.io/llms.txt). This page is also available as [Markdown](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent.md).

Prisma Cloud provides a dynamic [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) for Kubernetes and OpenShift that is built on the [Open Policy Agent (OPA)](https://www.openpolicyagent.org/docs/latest/). In Console, you can manage and compose rules in Rego, which is OPA’s native query language. Rules can allow or deny (alert or block) pods. Console pushes your policies to Defender, which enforces them. Decisions made by the system are logged.

There is currently no support for Windows.

## Open Policy Agent[Direct link to heading](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent\#open-policy-agent)

The Open Policy Agent is an open source, general-purpose policy engine that lets you consolidate policy enforcement in a single place. OPA can enforce policies in microservices, Kubernetes clusters, CI/CD pipelines, API gateways, and so on. OPA provides a high-level declarative language called Rego, which lets you specify policy as code. The OPA APIs let you offload policy decision-making from your software.

OPA decouples policy decision-making from policy enforcement. When your software needs to make policy decisions, it queries OPA and supplies structured data, such as JSON, as input. The data can be inspected and transformed using OPA’s native query language Rego. OPA generates policy decisions by evaluating the query input and against policies and data.

Prisma Cloud operationalizes OPA by:

- Extending Console to manage and compose policies in Rego.

- Integrating OPA’s decision-making library into Defender.

- Connecting Defender’s enforcement capabilities to OPA’s decisions.


## Admission webhook[Direct link to heading](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent\#admission-webhook)

An admission controller is code that intercepts requests to the API server for creating objects. There are two types of admission controllers: built-in and dynamic. Prisma Cloud implements a dynamic admission controller.

Dynamic admission controllers are built as webhooks. After registering to intercept admission requests, they assess requests against policy, and then accept or reject those requests. In Kubernetes terms, these are known as _validating admission webhooks_.

The Prisma Cloud validating admission webhook handles the API server’s AdmissionReview requests, and returns decisions in an AdmissionReview object. When configuring Prisma Cloud, you’ll create a ValidatingWebhookConfiguration object, which sets up the Defender service to intercept all create, update, and connect calls to the API server.

The default ValidatingWebhookConfiguration provided here sets failurePolicy to Ignore. The failure policy specifies how your cluster handles unrecognized errors and timeout errors from the admission webhook. When set to Ignore, the API request is allowed to continue.

## Configuring the webhook[Direct link to heading](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent\#configuring-the-webhook)

Configure the API server to route AdmissionReview requests to Prisma Cloud.

**Prerequisites:**

- You have a running instance of Prisma Cloud Compute Console.

- You have a Kubernetes cluster. Minimum supported version is v1.16.

- Defender has been deployed to your cluster as a DaemonSet. In Console, you can verify Defenders are running and connected under **Manage > Defenders > Manage**.


1. Go to **Defend > Access > Admission**

2. Enable admission control.

3. Click the **Admission controller** link and **Copy configuration** and save it to a file. Name this file `webhook.yaml`.











If the Defender CA has been rotated and the old certificate still hasn’t expired, you may have Defenders using an old certificate. For daemonset which its Defenders are using an old certificate, you need to retrieve the old Defender CA certificate from the daemonset yaml file you deployed this daemonset with.











Search for `defender-ca.pem` within the daemonset yaml, copy its content, then paste it to replace the content of the `caBundle` field of the webhook. If `defender-ca.pem` doesn’t exist in the daemonset yaml, use the content of the `ca.pem` field.











If you don’t have the yaml file you used to deploy the daemonset, you can retrieve the old CA bundle from the Console certificates folder under `old-defender-ca.pem`.











To identify whether your Defenders are using an old certificate, see [Console-Defender communication certificates](https://docs.prismacloud.io/admin-guide/configure/certificates).

4. Create the webhook configuration object.

















AskCopy



```
$ kubectl apply -f webhook.yaml
```









After creating the object, the Kubernetes API server directs AdmissionReview requests to Defender.


## Validating your setup[Direct link to heading](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent\#validating-your-setup)

Validate that your webhook has been properly set up with one of the predefined admission rules.

The order in which the rules appear is the order in which they are evaluated. Higher rules take precedence over lower rules. Rules can be reordered. Use the hamburger icon to drag and drop rules into the right place.

Notice that the processing of rules stops at the first match. To make sure the severe action will be taken in a case of more than one rule match, place the rules with action "Block" first.

1. Navigate to **Defend > Access > Admission** and verify there exist default admission rules and they are all enabled by default.

2. Create the following YAML file to test the **Twistlock Labs - CIS - Privileged pod created** rule.









1. Create the following YAML file: **priv-pod.yaml**

















      AskCopy



      ```
      apiVersion: v1
      kind: Pod
      metadata:
        name: nginx
        labels:
          app: nginx
      spec:
        containers:
  - name: nginx
    image: nginx
    ports:
    - containerPort: 80
    securityContext:
      privileged: true
```

3. Create the privileged pod.

















   AskCopy



   ```
   $ kubectl apply -f priv-pod.yaml
   ```

4. Verify an audit is created under **Monitor > Events > Admission Audits**.

5. Clean up. Delete the pod.

















   AskCopy



   ```
   kubectl delete -f priv-pod.yaml
   ```


## Creating custom admission rules[Direct link to heading](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent\#creating-custom-admission-rules)

Use [Rego syntax](https://www.openpolicyagent.org/docs/latest/policy-language/) to create custom rules. To learn more about the syntax, review the predefined rules that ship with Prisma Cloud. Rules scripts are based on the admission review input JSON structure. For more information, see: [https://github.com/kubernetes/api/blob/master/admission/v1beta1/types.go](https://github.com/kubernetes/api/blob/master/admission/v1beta1/types.go).

## Examples[Direct link to heading](https://docs.prismacloud.io/admin-guide/access-control/open-policy-agent\#examples)

The following examples should give you some ideas about how you can create your own policies by using the Rego language.

Do not allow new namespaces to be created:

AskCopy

```
match[{"msg": msg}] {
    input.request.operation == "CREATE"
    input.request.kind.kind == "Namespace"
    msg := "It's not allowed to create new namespace!"
}
```

Do not allow a specific image (for example nginx) in new pods:

AskCopy

```
match[{"msg": msg}] {
    input.request.operation == "CREATE"
    input.request.kind.kind == "Pod"
    input.request.resource.resource == "pods"
    input.request.object.spec.containers[_].image == "nginx"
    msg := "It's not allowed to use the nginx Image!"
}
```

Do not allow new pods to expose TCP port 80:

AskCopy

```
match[{"msg": msg}] {
    input.request.operation == "CREATE"
    input.request.kind.kind == "Pod"
    input.request.resource.resource == "pods"
    input.request.object.spec.containers[_].ports[_].containerPort == 80
    msg := "It's not allowed to use port 80 (HTTP) with a Pod configuration!"
}
```

Control the scope of your the policy rules by checking the object’s metadata, such as namespace or labels.

Do not allow new pods in namespace _sock-shop_ without the _owner_ label:

AskCopy

```
match[{"msg": msg}] {
    input.request.operation == "CREATE"
    input.request.kind.kind == "Pod"
    input.request.resource.resource == "pods"
        input.request.object.metadata.namespace == "sock-shop"
        not input.request.metadata.labels.owner
    msg := "Pod in namespace sock-shop is missing the owner label"
}
```

[PreviousAccess control](https://docs.prismacloud.io/admin-guide/access-control/access-control) [NextContinuous integration](https://docs.prismacloud.io/admin-guide/continuous-integration/continuous-integration)

Last updated 3 months ago

Was this helpful?

This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](https://policies.gitbook.com/privacy/cookies).

AcceptReject
