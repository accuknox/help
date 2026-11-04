---
title: Deploy BlueLock on EKS Fargate
description: Deploy BlueLock on an Amazon EKS Fargate cluster, onboard the cluster to AccuKnox and block a command in a sample workload to confirm runtime enforcement.
---

# Deploy BlueLock on EKS Fargate

!!! info "Overview"
    Deploy the BlueLock sample on EKS Fargate, onboard the cluster to AccuKnox and block `apt` in the sample pod. With an existing EKS Fargate cluster, start at [Step 2](#step-2-create-the-agents-namespace).

## Workflow at a Glance

<div class="bl-dia" role="img" aria-label="Six stages for EKS Fargate: create the cluster and namespace, sign in to public ECR, deploy the relay and sample workload, onboard the cluster, apply the block policy, then connect and test." data-bl="eks-flow">
<svg viewBox="0 0 760 128" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="bl-eks-flow" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <path class="rail" d="M63 16 H697"/>
  <rect class="navy" x="16" y="3" width="95" height="26" rx="13"/>
  <text class="num" x="63" y="20" text-anchor="middle">Steps 1-2</text>
  <text class="b" x="63" y="56" text-anchor="middle">Create cluster</text>
  <text class="b" x="63" y="74" text-anchor="middle">and namespace</text>
  <text class="ms" x="63" y="100" text-anchor="middle">eksctl</text>
  <rect class="navy" x="154" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="190" y="20" text-anchor="middle">Step 3</text>
  <text class="b" x="190" y="56" text-anchor="middle">Sign in to</text>
  <text class="b" x="190" y="74" text-anchor="middle">public ECR</text>
  <text class="ms" x="190" y="100" text-anchor="middle">helm</text>
  <rect class="navy" x="280" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="317" y="20" text-anchor="middle">Step 4</text>
  <text class="b" x="317" y="56" text-anchor="middle">Deploy relay</text>
  <text class="b" x="317" y="74" text-anchor="middle">and sample</text>
  <text class="ms" x="317" y="100" text-anchor="middle">kubectl</text>
  <rect class="navy" x="407" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="443" y="20" text-anchor="middle">Step 5</text>
  <text class="b" x="443" y="56" text-anchor="middle">Onboard the</text>
  <text class="b" x="443" y="74" text-anchor="middle">cluster</text>
  <text class="ms" x="443" y="100" text-anchor="middle">helm</text>
  <rect class="navy" x="534" y="3" width="72" height="26" rx="13"/>
  <text class="num" x="570" y="20" text-anchor="middle">Step 6</text>
  <text class="b" x="570" y="56" text-anchor="middle">Apply the</text>
  <text class="b" x="570" y="74" text-anchor="middle">block policy</text>
  <text class="ms" x="570" y="100" text-anchor="middle">AccuKnox</text>
  <rect class="navy" x="649" y="3" width="95" height="26" rx="13"/>
  <text class="num" x="697" y="20" text-anchor="middle">Steps 7-9</text>
  <text class="b" x="697" y="56" text-anchor="middle">Connect</text>
  <text class="b" x="697" y="74" text-anchor="middle">and test</text>
  <text class="ms" x="697" y="100" text-anchor="middle">socat</text>
</svg>
</div>

## What You Deploy Across Three Namespaces

<div class="bl-dia" role="img" aria-label="EKS Fargate architecture. In the default namespace the armored-application pod holds a bluelock init container and the armored-container. It reports to kubearmor-relay in kube-system. The relay feeds the AccuKnox agents in the agents namespace, which exchange alerts and policies with AccuKnox SaaS. Your terminal reaches the pod on port 1337 through kubectl port-forward and socat." data-bl="eks">
<svg viewBox="0 0 760 500" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="bl-eks" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="navy" x="500" y="0" width="260" height="64" rx="10"/>
  <g class="ic-w" transform="translate(520 20) scale(1.0)"><path d="M7 18h10a4 4 0 0 0 .6-7.95A6 6 0 0 0 6 9.6 4.2 4.2 0 0 0 7 18z"/></g>
  <text class="wh" x="554" y="30">AccuKnox SaaS</text>
  <text class="ws" x="554" y="49">Policies and alerts</text>
  <rect class="panel" x="150" y="110" width="610" height="380" rx="10"/>
  <g class="ic" transform="translate(166 124) scale(1.0)"><path d="M12 3 3.5 7.5v9L12 21l8.5-4.5v-9L12 3z"/><path d="M3.5 7.5 12 12l8.5-4.5M12 12v9"/></g>
  <text class="h" x="196" y="143">Amazon EKS on Fargate</text>
  <rect class="card" x="166" y="160" width="214" height="150" rx="10"/>
  <text class="s" x="182" y="182">namespace: default</text>
  <rect class="row" x="182" y="194" width="182" height="104" rx="8"/>
  <text class="b" x="196" y="216">armored-application</text>
  <rect class="card" x="196" y="226" width="154" height="28" rx="6"/>
  <text class="m" x="208" y="245">bluelock (init)</text>
  <rect class="card" x="196" y="262" width="154" height="28" rx="6"/>
  <text class="m" x="208" y="281">armored-container</text>
  <rect class="card" x="166" y="332" width="214" height="148" rx="10"/>
  <text class="s" x="182" y="354">namespace: kube-system</text>
  <rect class="row" x="182" y="366" width="182" height="100" rx="8"/>
  <g class="ic" transform="translate(194 376) scale(0.9)"><path d="M12 3 3.5 7.5v9L12 21l8.5-4.5v-9L12 3z"/><path d="M3.5 7.5 12 12l8.5-4.5M12 12v9"/></g>
  <text class="b" x="222" y="393">kubearmor-relay</text>
  <text class="s" x="196" y="424">gRPC 32767</text>
  <text class="s" x="196" y="444">HTTP 2801</text>
  <rect class="card" x="410" y="160" width="334" height="320" rx="10"/>
  <text class="s" x="426" y="182">namespace: agents</text>
  <rect class="navy" x="426" y="194" width="302" height="272" rx="8"/>
  <g class="ic-w" transform="translate(440 208) scale(0.95)"><path d="M12 3l8 3v6c0 4.5-3.2 8-8 9-4.8-1-8-4.5-8-9V6l8-3z"/></g>
  <text class="wh" x="470" y="226">AccuKnox agents</text>
  <text class="wm" x="442" y="266">agents-operator</text>
  <text class="wm" x="442" y="292">discovery-engine</text>
  <text class="wm" x="442" y="318">feeder-service</text>
  <text class="wm" x="442" y="344">policy-enforcement-agent</text>
  <text class="wm" x="442" y="370">shared-informer-agent</text>
  <text class="ws" x="442" y="420">KubeArmor operator</text>
  <text class="ws" x="442" y="438">disabled in this install</text>
  <rect class="card" x="0" y="214" width="118" height="100" rx="10"/>
  <g class="ic" transform="translate(16 230) scale(1.0)"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="m7 9 3 3-3 3M13 15h4"/></g>
  <text class="b" x="16" y="282">Your terminal</text>
  <text class="s" x="16" y="300">kubectl, socat</text>
  <path class="ln" d="M120 262 H190" marker-end="url(#bl-eks)"/>
  <path class="ln" d="M273 298 V364" marker-end="url(#bl-eks)"/>
  <path class="ln" d="M364 416 H424" marker-end="url(#bl-eks)"/>
  <path class="ln" d="M600 192 V68" marker-end="url(#bl-eks)"/>
  <text class="s" x="592" y="128" text-anchor="end">alerts</text>
  <path class="ln" d="M650 68 V192" marker-end="url(#bl-eks)"/>
  <text class="s" x="658" y="128">policies</text>
</svg>
</div>

## Prerequisites

| Requirement | Used for |
|---|---|
| AWS CLI and `eksctl`, configured | Creating the cluster and the Fargate profile |
| `kubectl`, `helm` and `socat` | Deploying the sample, installing the agents and reaching the pod |
| EKS admin access | Creating namespaces and cluster-level resources |
| AccuKnox SaaS access | Onboarding the cluster, applying the policy and viewing the alert |

## Step 1. Create an EKS Fargate Cluster

Create the cluster. The command creates a VPC, an EKS cluster, the Fargate profile `fp-default` for `default` and `kube-system`, and a few essential add-ons.

```shell
eksctl create cluster \
  --name kubearmor-fargate \
  --region us-east-2 \
  --fargate
```

Create a Fargate profile for the `agents` namespace.

```shell
eksctl create fargateprofile \
  --cluster kubearmor-fargate \
  --region us-east-2 \
  --name fp-agents \
  --namespace agents
```

!!! tip "Prefer the AWS console?"
    You can create the cluster and the profile there. An existing cluster needs Fargate profiles for `default`, `kube-system` and `agents`.

## Step 2. Create the Agents Namespace

```shell
kubectl create ns agents
```

!!! info "Pods on Fargate start slowly"
    AWS starts a separate VM for each pod. Wait and verify after each component.

## Step 3. Sign in to Public ECR

Helm pulls the agents chart from public ECR.

```shell
aws ecr-public get-login-password --region us-east-1 | helm registry login --username AWS --password-stdin public.ecr.aws
```

## Step 4. Deploy the Relay and the Sample Workload

### Install the KubeArmor Relay in kube-system

```shell
cat <<EOF | kubectl apply -f -
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: kubearmor
  namespace: kube-system
---
apiVersion: v1
kind: Service
metadata:
  name: kubearmor
  namespace: kube-system
  labels:
    kubearmor-app: kubearmor-relay
spec:
  selector:
    kubearmor-app: kubearmor-relay
  ports:
  - name: "grpc-port"
    port: 32767
    protocol: TCP
  - name: "http-port"
    port: 2801
    protocol: TCP
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kubearmor-relay
  namespace: kube-system
  labels:
    kubearmor-app: kubearmor-relay
spec:
  replicas: 1
  selector:
    matchLabels:
      kubearmor-app: kubearmor-relay
  template:
    metadata:
      labels:
        kubearmor-app: kubearmor-relay
      annotations:
        kubearmor-policy: audited
    spec:
      serviceAccountName: kubearmor
      containers:
      - name: kubearmor-relay-server
        image: docker.io/kubearmor/kubearmor-relay-server:latest
        imagePullPolicy: Always
        ports:
        - containerPort: 32767
        - containerPort: 2801
        resources:
          requests:
            cpu: 250m
            memory: 64Mi
          limits:
            cpu: 500m
            memory: 128Mi
EOF
```

### Install the KubeArmor Policy CRD

```shell
kubectl create -f https://raw.githubusercontent.com/kubearmor/KubeArmor/refs/heads/main/deployments/CRD/KubeArmorPolicy.yaml
```

### Deploy the Sample BlueLock Workload in default

The manifest:

- Copies the `bluelock` binary into a shared `emptyDir` volume with an init container.
- Starts `/kubearmor/bluelock` first in `armored-container`, with `socat` as its arguments.
- Points `SIDEKICK_URL` at the relay on port 2801.

```shell
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: armored-application
  labels:
    deployment: armored-application
spec:
  replicas: 1
  selector:
    matchLabels:
      kubearmor.io/container.name: armored-container
  template:
    metadata:
      labels:
        kubearmor.io/container.name: armored-container
    spec:
      serviceAccountName: kubearmor
      volumes:
        - emptyDir: {}
          name: kubearmor-dir
      initContainers:
        - name: bluelock
          image: public.ecr.aws/k9v9d5v2/accuknox-bluelock:v1.0.0
          imagePullPolicy: Always
          volumeMounts:
            - mountPath: /kubearmor
              name: kubearmor-dir
      containers:
        - name: armored-container
          image: public.ecr.aws/k9v9d5v2/accuknox-bluelock/ka-socat-demo:latest
          imagePullPolicy: Always
          command: ["/kubearmor/bluelock","socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:bash,pty,stderr,setsid,sigint,sane"]
          ports:
            - containerPort: 1337
          volumeMounts:
            - mountPath: /kubearmor
              name: kubearmor-dir
          env:
          - name: "SIDEKICK_URL"
            value: "http://kubearmor.kube-system.svc.cluster.local:2801"

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubearmor-clusterrolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: kubearmor
  namespace: default
- kind: ServiceAccount
  name: kubearmor
  namespace: kube-system
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: kubearmor
---
EOF
```

!!! warning "Use the sample in test clusters"
    The manifest binds the `kubearmor` service accounts in `default` and `kube-system` to `cluster-admin`. Review it before you reuse it outside a test cluster.

## Step 5. Onboard the Cluster to AccuKnox

Generate the Helm command as described in [Runtime Security Onboarding](cluster-onboarding.md). Add these two flags to leave KubeArmor out:

```shell
--set kubearmor-operator.enabled=false
--set kubearmor-operator.autoDeploy=false
```

After a few minutes, list the pods.

```shell
kubectl get pods -n agents
```

```text
NAME                                            READY   STATUS        RESTARTS   AGE
agents-operator-558786bbc5-z857l                1/1     Running       0          10m
cis-k8s-job-1779677622-rcq4j                    0/1     Pending       0          10m
discovery-engine-5c757f9fb9-vnk7s               2/2     Running       0          4m7s
feeder-service-5cc8664cd5-mvrfb                 1/1     Running       0          4m8s
k8s-risk-assessment-job-1779677622-vkscr        0/1     Completed     0          10m
kiem-job-1779677622-wrkmp                       0/1     Completed     0          10m
kubearmor-operator-77d98d4f9d-rcgln             1/1     Running       0          10m
kubeshield-controller-manager-7b44cd489-t58kw   0/1     Pending       0          10m
policy-enforcement-agent-b8d49b556-szjjh        1/1     Running       0          4m8s
shared-informer-agent-7859c8f4-2mh99            1/1     Running       0          4m8s
```

The CIS K8s job and `kubeshield-controller-manager` stay `Pending` because Fargate does not support them.

## Step 6. Apply the Sample Policy From AccuKnox

In AccuKnox, open Runtime Protection, then Policies, and create this policy. It denies `apt` and `apt-get`. Activate it after you save.

```yaml
apiVersion: security.kubearmor.com/v1
kind: KubeArmorPolicy
metadata:
  name: block-pkg-mgmt-tools-exec
spec:
  selector:
    matchLabels:
      kubearmor.io/container.name: armored-container
  process:
    matchPaths:
    - path: /usr/bin/apt
    - path: /usr/bin/apt-get
  action:
    Block
```

## Step 7. Port-Forward to the Sample Pod

```shell
kubectl port-forward pod/$(kubectl get pods --no-headers | grep armored-application | awk '{print $1}') 1337:1337
```

## Step 8. Connect to the Sample Application

In a second terminal:

```shell
socat - TCP:localhost:1337
```

## Step 9. Run a Blocked Command and Confirm the Denial

In the `socat` session:

```shell
apt -v
```

You get a permission denied error and an alert in AccuKnox.

## Step 10. Delete the Cluster When You Finish

```shell
eksctl delete cluster \
  --name kubearmor-fargate \
  --region us-east-2
```
