---
title: Deploy BlueLock on EKS Fargate
description: Deploy BlueLock on an Amazon EKS Fargate cluster, onboard the cluster to AccuKnox and block a command in a sample workload to confirm runtime enforcement.
---

# Deploy BlueLock on EKS Fargate

!!! info "Overview"
    This guide creates an Amazon EKS Fargate cluster, deploys the BlueLock sample workload, onboards the cluster to AccuKnox and blocks `apt` inside the sample pod. If you already have an EKS Fargate cluster, start at [Step 2](#step-2-create-the-agents-namespace). Read [BlueLock Runtime Security for Serverless Containers](bluelock.md) first if you want the background.

## Workflow at a Glance

<div class="ak-dia" role="img" aria-label="Six-phase workflow for EKS Fargate. Steps 1 and 2 create the cluster and the agents namespace. Step 3 logs in to public ECR. Step 4 deploys the KubeArmor relay, the policy CRD and the sample BlueLock workload. Step 5 onboards the cluster with AccuKnox agents and KubeArmor disabled. Step 6 applies a policy that denies apt and apt-get. Steps 7 to 9 port-forward to the pod, connect with socat and run apt -v to see the denial.">
<svg viewBox="0 0 640 292" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="mekf" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
    <marker id="mekfa" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head-acc" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="p" x="8" y="8" width="200" height="126" rx="8"/>
  <circle class="step" cx="32" cy="32" r="12"/>
  <text class="t-step" x="32" y="36" text-anchor="middle">1</text>
  <text class="t-s" x="54" y="36">Steps 1 and 2</text>
  <text class="t-h" x="24" y="70">Create the cluster</text>
  <text class="t-h" x="24" y="87">and namespace</text>
  <text class="t-s" x="24" y="109">eksctl, then</text>
  <text class="t-s" x="24" y="124">kubectl create ns</text>
  <path class="ln" d="M209 71 H227" marker-end="url(#mekf)"/>
  <rect class="p" x="228" y="8" width="200" height="126" rx="8"/>
  <circle class="step" cx="252" cy="32" r="12"/>
  <text class="t-step" x="252" y="36" text-anchor="middle">2</text>
  <text class="t-s" x="274" y="36">Step 3</text>
  <text class="t-h" x="244" y="70">Log in to</text>
  <text class="t-h" x="244" y="87">public ECR</text>
  <text class="t-s" x="244" y="109">helm registry login</text>
  <text class="t-s" x="244" y="124">with the AWS CLI</text>
  <path class="ln" d="M429 71 H447" marker-end="url(#mekf)"/>
  <rect class="p" x="448" y="8" width="200" height="126" rx="8"/>
  <circle class="step" cx="472" cy="32" r="12"/>
  <text class="t-step" x="472" y="36" text-anchor="middle">3</text>
  <text class="t-s" x="494" y="36">Step 4</text>
  <text class="t-h" x="464" y="70">Deploy relay and</text>
  <text class="t-h" x="464" y="87">sample workload</text>
  <text class="t-s" x="464" y="109">KubeArmor relay, CRD</text>
  <text class="t-s" x="464" y="124">and bluelock sample</text>
  <rect class="acc" x="8" y="162" width="200" height="126" rx="8"/>
  <circle class="step" cx="32" cy="186" r="12"/>
  <text class="t-step" x="32" y="190" text-anchor="middle">4</text>
  <text class="t-s" x="54" y="190">Step 5</text>
  <text class="t-h" x="24" y="224">Onboard the</text>
  <text class="t-h" x="24" y="241">cluster</text>
  <text class="t-s" x="24" y="263">AccuKnox agents,</text>
  <text class="t-s" x="24" y="278">KubeArmor disabled</text>
  <path class="ln" d="M209 225 H227" marker-end="url(#mekf)"/>
  <rect class="acc" x="228" y="162" width="200" height="126" rx="8"/>
  <circle class="step" cx="252" cy="186" r="12"/>
  <text class="t-step" x="252" y="190" text-anchor="middle">5</text>
  <text class="t-s" x="274" y="190">Step 6</text>
  <text class="t-h" x="244" y="224">Apply the block</text>
  <text class="t-h" x="244" y="241">policy</text>
  <text class="t-s" x="244" y="263">Denies apt and</text>
  <text class="t-s" x="244" y="278">apt-get</text>
  <path class="ln" d="M429 225 H447" marker-end="url(#mekf)"/>
  <rect class="good" x="448" y="162" width="200" height="126" rx="8"/>
  <circle class="step" cx="472" cy="186" r="12"/>
  <text class="t-step" x="472" y="190" text-anchor="middle">6</text>
  <text class="t-s" x="494" y="190">Steps 7 to 9</text>
  <text class="t-h" x="464" y="224">Connect and</text>
  <text class="t-h" x="464" y="241">test</text>
  <text class="t-s" x="464" y="263">port-forward, socat,</text>
  <text class="t-s" x="464" y="278">then run apt -v</text>
  <path class="ln" d="M548 135 V148 H108 V161" marker-end="url(#mekf)"/>
</svg>
</div>

## What You Deploy Across Three Namespaces

<div class="ak-dia" role="img" aria-label="EKS Fargate architecture. In the default namespace, the armored-application pod holds a bluelock init container and the armored-container. The pod reports to the kubearmor-relay service in the kube-system namespace through SIDEKICK_URL. The relay feeds the AccuKnox agents in the agents namespace, which run without KubeArmor. The agents send alerts to AccuKnox SaaS and receive policies. Your terminal reaches the pod on port 1337 through kubectl port-forward and socat.">
<svg viewBox="0 0 920 444" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="meks" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head" d="M0 0 L8 4 L0 8 z"/>
    </marker>
    <marker id="meksa" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto">
      <path class="head-acc" d="M0 0 L8 4 L0 8 z"/>
    </marker>
  </defs>
  <rect class="p" x="8" y="136" width="150" height="84" rx="8"/>
  <text class="t-h" x="22" y="164">Your terminal</text>
  <text class="t-s" x="22" y="184">kubectl port-forward</text>
  <text class="t-s" x="22" y="200">then socat to :1337</text>
  <rect class="p2" x="190" y="40" width="540" height="376" rx="8"/>
  <text class="t-h" x="206" y="64">Amazon EKS cluster on Fargate</text>
  <rect class="hollow" x="206" y="80" width="250" height="160" rx="8"/>
  <text class="t-s" x="222" y="98">namespace: default</text>
  <rect class="acc" x="222" y="108" width="218" height="120" rx="8"/>
  <text class="t-h" x="236" y="130">armored-application pod</text>
  <rect class="p" x="236" y="142" width="190" height="30" rx="6"/>
  <text class="t-b" x="246" y="162">bluelock (init container)</text>
  <rect class="p" x="236" y="180" width="190" height="30" rx="6"/>
  <text class="t-b" x="246" y="200">armored-container</text>
  <rect class="hollow" x="206" y="270" width="250" height="134" rx="8"/>
  <text class="t-s" x="222" y="288">namespace: kube-system</text>
  <rect class="p" x="222" y="298" width="218" height="94" rx="8"/>
  <text class="t-h" x="236" y="320">kubearmor-relay</text>
  <text class="t-s" x="236" y="342">Service ports</text>
  <text class="t-s" x="236" y="358">32767 gRPC, 2801 HTTP</text>
  <rect class="hollow" x="480" y="80" width="234" height="324" rx="8"/>
  <text class="t-s" x="496" y="98">namespace: agents</text>
  <rect class="acc" x="496" y="108" width="202" height="284" rx="8"/>
  <text class="t-h" x="510" y="130">AccuKnox agents</text>
  <text class="t-mono" x="510" y="160">agents-operator</text>
  <text class="t-mono" x="510" y="184">discovery-engine</text>
  <text class="t-mono" x="510" y="208">feeder-service</text>
  <text class="t-mono" x="510" y="232">policy-enforcement-agent</text>
  <text class="t-mono" x="510" y="256">shared-informer-agent</text>
  <text class="t-s" x="510" y="300">KubeArmor operator is</text>
  <text class="t-s" x="510" y="316">disabled in this install.</text>
  <rect class="plane" x="766" y="140" width="146" height="92" rx="8"/>
  <text class="t-plane" x="839" y="176" text-anchor="middle">AccuKnox SaaS</text>
  <text class="t-pill" x="839" y="198" text-anchor="middle">Policies, alerts</text>
  <text class="t-pill" x="839" y="216" text-anchor="middle">and inventory</text>
  <path class="ln" d="M158 168 H222" marker-end="url(#meks)"/>
  <path class="ln" d="M331 228 V298" marker-end="url(#meks)"/>
  <text class="t-s" x="340" y="258">SIDEKICK_URL</text>
  <path class="ln" d="M440 345 H496" marker-end="url(#meks)"/>
  <path class="ln-acc" d="M698 172 H766" marker-end="url(#meksa)"/>
  <path class="ln-acc" d="M766 204 H698" marker-end="url(#meksa)"/>
</svg>
</div>

The sample pod runs your application behind the `bluelock` binary. An init container copies the binary into a shared volume, and the container command starts `/kubearmor/bluelock` with your application as its arguments. The pod sends events to the `kubearmor-relay` service, and the AccuKnox agents in the `agents` namespace carry them to AccuKnox.

## Prerequisites

| Requirement | Used for |
|---|---|
| AWS CLI and `eksctl`, configured | Creating the cluster and the Fargate profile |
| `kubectl`, `helm` and `socat` | Deploying the sample, installing the agents and reaching the pod |
| EKS admin access | Creating namespaces and cluster-level resources |
| AccuKnox SaaS access | Onboarding the cluster, applying the policy and viewing the alert |

## Step 1. Create an EKS Fargate Cluster

Create the cluster with `eksctl`. The command creates a VPC, an EKS cluster, a Fargate profile named `fp-default` for the `default` and `kube-system` namespaces and a few essential EKS add-ons.

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
    You can create both the cluster and the profile in the AWS console. If you use your own cluster, it needs Fargate profiles that cover the `default`, `kube-system` and `agents` namespaces.

## Step 2. Create the Agents Namespace

```shell
kubectl create ns agents
```

!!! info "Pods on Fargate start slowly"
    Wait and verify after you install each component in a Fargate profile namespace. A pod takes a while to schedule because AWS starts a separate VM for each pod.

## Step 3. Sign in to Public ECR

Helm pulls the AccuKnox agents chart from public ECR. Log in with your AWS credentials.

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

The manifest does three things:

- The `bluelock` init container copies the `bluelock` binary into a shared `emptyDir` volume.
- The `armored-container` command starts `/kubearmor/bluelock` first, with `socat` as its arguments.
- The `SIDEKICK_URL` variable points the pod at the relay on port 2801.

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
    The sample manifest binds the `kubearmor` service accounts in `default` and `kube-system` to the `cluster-admin` role. Review the binding before you reuse this manifest outside a test cluster.

## Step 5. Onboard the Cluster to AccuKnox

Install the AccuKnox agents from the AccuKnox console, but leave KubeArmor out. Generate the Helm command as described in [Runtime Security Onboarding](cluster-onboarding.md), then add these two flags to it:

```shell
--set kubearmor-operator.enabled=false
--set kubearmor-operator.autoDeploy=false
```

After a few minutes, list the pods in the `agents` namespace.

```shell
kubectl get pods -n agents
```

The output looks like this:

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

The CIS K8s job and `kubeshield-controller-manager` stay in `Pending` on Fargate because Fargate does not support them.

## Step 6. Apply the Sample Policy From AccuKnox

In the AccuKnox console, open Runtime Protection, then Policies, and create the following policy. It denies execution of the package managers `apt` and `apt-get`. Activate it after you save it.

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

Open a second terminal and connect with `socat`.

```shell
socat - TCP:localhost:1337
```

## Step 9. Run a Blocked Command and Confirm the Denial

In the `socat` session, run `apt -v`.

```shell
apt -v
```

You get a permission denied error, and an alert appears in AccuKnox.

## What This Test Proves

- A policy you apply in AccuKnox reaches the cluster and enforces on the BlueLock workload.
- The block raises an alert that you can read in AccuKnox.

## Step 10. Delete the Cluster When You Finish

```shell
eksctl delete cluster \
  --name kubearmor-fargate \
  --region us-east-2
```
