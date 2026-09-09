---
title: Kong Gateway Integration with AccuKnox API Security
description: Integrate Kong Gateway with AccuKnox API Security to monitor API traffic and enforce security policies.
---

# Kong Gateway Integration with AccuKnox API Security

This guide describes how to integrate Kong Gateway with AccuKnox API Security for API security monitoring.

## Prerequisites

- Kubernetes cluster (e.g., kind, EKS, GKE)
- kubectl configured
- Helm 3.x installed
- AccuKnox agents installed

## Steps

![AccuKnox API Security with Kong integration workflow](image-58.png)

### 1. Install Kong Gateway

```shell
helm repo add kong https://charts.konghq.com
helm repo update

# Install Kong with default settings
helm install kong kong/kong \
  --namespace kong \
  --create-namespace \
  --set ingressController.installCRDs=false \
  --set admin.enabled=true \
  --set admin.type=NodePort
```


### 2. Deploy AccuKnox API Security (Initial - Creates ConfigMap)

Deploy AccuKnox API Security with Kong receiver enabled. This creates the `sentryflow-log-plugin` ConfigMap in the 'kong' namespace containing the plugin Lua code.

> **Note:** This step may show a warning about the `KongClusterPlugin` failing validation - this is expected because Kong hasn't loaded the plugin yet. AccuKnox API Security itself and the ConfigMap will still be created.

> **Note:** Minimum Required Version for AccuKnox API Security Kong integration is `v0.1.8`. Check the AccuKnox API Security [release](https://github.com/accuknox/SentryFlow/releases) page to install the latest version.

```shell
helm upgrade --install sentryflow \
  oci://public.ecr.aws/k9v9d5v2/sentryflow-helm-charts \
  --namespace sentryflow \
  --create-namespace \
  --version v0.1.8 \
  --set config.receivers.kongGateway.enabled=true \
  --set config.receivers.kongGateway.namespace=kong \
  --set config.receivers.kongGateway.deploymentName=kong-kong \
  --set config.receivers.kongGateway.plugin.httpEndpoint=http://sentryflow.sentryflow.svc.cluster.local:8081/api/v1/events \
  --set config.receivers.kongGateway.plugin.timeout=10000 \
  --set config.receivers.kongGateway.plugin.keepalive=60000
```

Verify the ConfigMap was created:

```shell
kubectl get configmap sentryflow-log-plugin -n kong
```

### 3. Patch Kong Deployment

Now we need to configure Kong to load the `sentryflow-log` plugin. This requires:

1. Mounting the ConfigMap containing the plugin code
2. Setting the `KONG_PLUGINS` environment variable

**Mount the plugin and enable it:**

```shell
# Mount the plugin ConfigMap
kubectl patch deployment kong-kong -n kong --type=json -p='[
  {
    "op": "add",
    "path": "/spec/template/spec/volumes/-",
    "value": {
      "name": "sentryflow-log-plugin",
      "configMap": {
        "name": "sentryflow-log-plugin"
      }
    }
  },
  {
    "op": "add",
    "path": "/spec/template/spec/containers/1/volumeMounts/-",
    "value": {
      "name": "sentryflow-log-plugin",
      "mountPath": "/usr/local/share/lua/5.1/kong/plugins/sentryflow-log",
      "readOnly": true
    }
  }
]'

# Enable the plugin in Kong
kubectl set env deployment/kong-kong -n kong KONG_PLUGINS=bundled,sentryflow-log
```

> **Note:** The `volumeMount` is applied to the `proxy` container (index 1). Adjust if your Kong deployment has a different container order.

Wait for Kong to restart and become ready:

```shell
kubectl -n kong rollout status deployment/kong-kong
```

### 4. Create KongClusterPlugin


Now that Kong has loaded the plugin, re-run the Helm chart to create the `KongClusterPlugin` resource:

```shell
helm upgrade --install sentryflow \
  oci://public.ecr.aws/k9v9d5v2/sentryflow-helm-charts \
  --namespace sentryflow \
  --create-namespace \
  --version v0.1.8 \
  --set config.receivers.kongGateway.enabled=true \
  --set config.receivers.kongGateway.namespace=kong \
  --set config.receivers.kongGateway.deploymentName=kong-kong \
  --set config.receivers.kongGateway.plugin.httpEndpoint=http://sentryflow.sentryflow.svc.cluster.local:8081/api/v1/events \
  --set config.receivers.kongGateway.plugin.timeout=10000 \
  --set config.receivers.kongGateway.plugin.keepalive=60000
```

Verify the KongClusterPlugin was created:

```shell
kubectl get kongclusterplugins
```

You should see:
```
NAME             PLUGIN-TYPE      AGE   PROGRAMMED
sentryflow-log   sentryflow-log   Xs
```

### 5. Patch Discovery Engine


Update the discovery-engine ConfigMap (`discovery-engine-sumengine`) to use AccuKnox API Security and restart the deployment.

```shell
kubectl -n agents edit configmap discovery-engine-sumengine
```

Update the configuration:

```yaml
data:
  app.yaml: |
    ...
    summary-engine:
      accuknox-api-security:
        cron-interval: 0h0m30s
        decode-jwt: true
        enabled: true
        include-bodies: true
        redact-sensitive-data: false
        sensitive-rules-files-path:
        - /var/lib/sumengine/sensitive-data-rules.yaml
        threshold: 10000
    watcher:
    ...
      accuknox-api-security:
        enabled: true
        event-type:
          access-log: true
          metric: false
        service:
          enabled: true
          name: accuknox-api-security
          port: "8080"
          url: "accuknox-api-security.sentryflow"
```

Restart discovery-engine:

```shell
kubectl -n agents rollout restart deployment/discovery-engine
```

## Verification Guide

### 1. Deploy Sample Application

Deploy the Google Microservices Demo `frontend` service (or any HTTP service).

```shell
# Verify frontend service exists
kubectl get svc
```

### 2. Create Ingress Resource


Create an Ingress to route traffic through Kong to your service.

```shell
kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: frontend-ingress
  namespace: <your_namespace>
  annotations:
    konghq.com/strip-path: "true"
spec:
  ingressClassName: kong
  rules:
    - http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: frontend
                port:
                  number: 80
EOF
```

### 3. Generate Traffic

Port-forward the Kong proxy and send requests.

```shell
# Port forward Kong Proxy
kubectl port-forward -n kong svc/kong-kong-proxy 8000:80 &

# Send traffic
sleep 2
curl -s http://localhost:8000/ > /dev/null
curl -s http://localhost:8000/cart > /dev/null
```


### 4. Verify AccuKnox API Security Logs

Check AccuKnox API Security logs to confirm it received the events.

```shell
kubectl -n sentryflow logs deployment/sentryflow --tail=50
```

You should see logs indicating receipt of events:
```
{"level":"INFO",...,"msg":"Received API Event from kong"}
```

## Troubleshooting

### KongClusterPlugin Validation Error

If you see:

```
Error: admission webhook "validations.kong.konghq.com" denied the request: plugin failed schema validation
```

This means Kong hasn't loaded the plugin yet. Ensure:

1. The `sentryflow-log-plugin` ConfigMap exists in the `kong` namespace
2. Kong deployment has the ConfigMap mounted at `/usr/local/share/lua/5.1/kong/plugins/sentryflow-log`
3. `KONG_PLUGINS` environment variable includes `sentryflow-log`
4. Kong pods have restarted and are `Running`

### Kong Pods in CrashLoopBackOff

If Kong pods crash after setting `KONG_PLUGINS`:

- The ConfigMap may not be mounted yet
- Apply the patch to mount the ConfigMap and wait for pods to restart

