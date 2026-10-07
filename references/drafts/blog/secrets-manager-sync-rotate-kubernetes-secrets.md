---
title: "Sync Kubernetes secrets from AccuKnox Secrets Manager and rotate them with no code changes"
seo_title: "Sync Kubernetes Secrets With AccuKnox Secrets Manager"
meta_description: "Sync Kubernetes secrets from AccuKnox Secrets Manager with the External Secrets Operator. Change a database password and restart WordPress, no code changes."
slug: "secrets-manager-sync-rotate-kubernetes-secrets"
url: "https://accuknox.com/blog/secrets-manager-sync-rotate-kubernetes-secrets"
date: 2026-10-10
primary_keyword: "sync kubernetes secrets"
secondary_keywords: ["external secrets operator", "kubernetes secret rotation", "accuknox secrets manager", "wordpress mysql kubernetes secret"]
excerpt: "An External Secret object copies a password from AccuKnox Secrets Manager into a Kubernetes secret every 10 seconds. WordPress keeps reading the same secret, so its code never changes."
category: "Secrets Manager"
author: "Atharva Shah"
reading_time: "5 minutes"
word_count_target: 1000
audience: "platform engineer | DevOps engineer"
cover_image_prompt_claude: >
  Not used. The cover is the YouTube thumbnail for the demo video, kuiPcejfcHU.
cover_image_prompt_midjourney: >
  Not used. The cover is the YouTube thumbnail for the demo video, kuiPcejfcHU.
---

# Sync Kubernetes secrets from AccuKnox Secrets Manager and rotate them with no code changes

![AccuKnox Secrets Manager demo thumbnail: sync and rotate Kubernetes secrets with no code changes](https://img.youtube.com/vi/kuiPcejfcHU/maxresdefault.jpg)

*The demo this post follows, from the AccuKnox YouTube channel.*

## TL;DR

- An External Secret object copies a password from AccuKnox Secrets Manager into a Kubernetes secret and checks for changes every 10 seconds.
- A new version saved in AccuKnox Secrets Manager reaches the Kubernetes secret in about 10 seconds.
- WordPress reads the password through a secret key reference, so the application code does not change.
- A running pod does not reload the secret, so you restart the WordPress pod after each change.
- The Kubernetes secret holds a copy of the password, and anyone who can read the namespace can read it.

## One External Secret Object Keeps Kubernetes in Step With AccuKnox Secrets Manager

To sync Kubernetes secrets from AccuKnox Secrets Manager, store the password there once. The [External Secrets Operator](https://external-secrets.io/) copies it into a normal Kubernetes secret. Your application keeps reading the secret it reads today.

This post follows a two-minute demo. One namespace holds two deployments, WordPress and MySQL. WordPress needs the MySQL password, and that password now lives in AccuKnox Secrets Manager instead of a hand-made Kubernetes secret. AccuKnox Secrets Manager runs as its own control plane, and the operator runs in the application cluster.

Check four things before you start.

| Requirement | Detail |
| --- | --- |
| AccuKnox Secrets Manager | Running, with a KV version 2 engine at `secret`. See the [Deployment Guide](https://help.accuknox.com/secrets-manager/deployment/) |
| External Secrets Operator | Installed in the cluster, with a ready `ClusterSecretStore` |
| A role and a policy | Role `demo-access`, which reads `demo/mysql` only |
| `kubectl` | Pointed at the cluster |

The password sits at the path `demo/mysql`, under the key `password`.

![The demo/mysql secret in AccuKnox Secrets Manager, with its password key and masked value](https://media.zernio.com/temp/1791272935085_rtp3v3hb_m02-secret-in-accuknox.jpg)

*Caption: The password lives in one place, at the path demo/mysql in AccuKnox Secrets Manager.*

The External Secret object tells the operator what to copy.

```yaml
apiVersion: external-secrets.io/v1
kind: ExternalSecret
metadata:
  name: mysql-pass
spec:
  refreshInterval: "10s"
  secretStoreRef:
    name: vault-backend-demo
    kind: ClusterSecretStore
  target:
    name: mysql-pass
  data:
  - secretKey: password
    remoteRef:
      key: demo/mysql
      property: password
```

The `refreshInterval` of `10s` sets how often the operator checks AccuKnox Secrets Manager. The `secretStoreRef` names the `ClusterSecretStore` that holds the server address and the login. The `target` is the Kubernetes secret `mysql-pass`, and `remoteRef` is the path to read.

![The External Secret YAML in k9s with callouts for the sync interval, the link to AccuKnox, the Kubernetes secret name and the path in AccuKnox](https://media.zernio.com/temp/1791272933175_byycdejt_m01-externalsecret.jpg)

*Caption: The External Secret in the demo, with its 10 second sync, its link to AccuKnox, the Kubernetes secret name and the path in AccuKnox.*

## Apply the External Secret and the Kubernetes Secret Appears

Apply the file.

```bash
kubectl apply -f demo-access-mysql.yaml
```

The operator creates `mysql-pass` straight away, holding the value from AccuKnox Secrets Manager. You wrote no Kubernetes secret by hand. The operator then checks AccuKnox Secrets Manager every 10 seconds and rewrites `mysql-pass` only when the value changes.

![The Kubernetes secret mysql-pass described in k9s, with its password value highlighted](https://media.zernio.com/temp/1791272937402_ksyrcpbs_m03-value-in-k8s.jpg)

*Caption: The Kubernetes secret mysql-pass holds the value copied from AccuKnox Secrets Manager.*

Now change the value at the source. Open `demo/mysql`, click **Create new version**, enter a new password and click **Save**. Within about 10 seconds, `mysql-pass` holds the new value. Nobody touched Kubernetes.

![The Create new version form in AccuKnox Secrets Manager with a new password entered](https://media.zernio.com/temp/1791272939076_fd1k8kwq_m04-new-version-form.jpg)

*Caption: Create new version in AccuKnox Secrets Manager: enter the new password and save it.*

![The Kubernetes secret mysql-pass described in k9s after the sync, marked Synced from AccuKnox](https://media.zernio.com/temp/1791272940826_jjspj2zl_m05-synced.jpg)

*Caption: Seconds later, mysql-pass shows the new value, marked Synced from AccuKnox, with no kubectl edit.*

## WordPress Reads the Same Secret With No Code Change

Deploy the standard WordPress and MySQL example from the Kubernetes documentation.

```bash
kubectl apply -f https://k8s.io/examples/application/wordpress/mysql-deployment.yaml
kubectl apply -f https://k8s.io/examples/application/wordpress/wordpress-deployment.yaml
```

The WordPress deployment file is the stock one. It reads the database password from `mysql-pass` through `secretKeyRef`.

![The WordPress deployment YAML with the secretKeyRef highlighted and the label Reads mysql-pass](https://media.zernio.com/temp/1791272942530_dipw5tbc_m06-wordpress-reads.jpg)

*Caption: The WordPress deployment reads the database password from mysql-pass through secretKeyRef.*

```yaml
env:
  - name: WORDPRESS_DB_PASSWORD
    valueFrom:
      secretKeyRef:
        name: mysql-pass
        key: password
```

WordPress connects to MySQL and loads. The application never learns that AccuKnox Secrets Manager exists. It reads a Kubernetes secret, as it always did.

![The WordPress installer language screen, which shows that WordPress is running and connected](https://media.zernio.com/temp/1791272944313_5l1dwz0l_m07-wordpress-up.jpg)

*Caption: WordPress is up and connected to MySQL.*

## A Changed Password Breaks WordPress Until the Pod Restarts

The demo now breaks the connection on purpose. Change the MySQL password by hand, so the database no longer matches the Kubernetes secret. WordPress loses its database connection and shows `Error establishing a database connection`.

![The WordPress page that shows Error establishing a database connection](https://media.zernio.com/temp/1791272947662_toxi9ji7_m09-db-error.jpg)

*Caption: WordPress shows Error establishing a database connection after the MySQL password changes.*

Fix it from the source. Save the new password in AccuKnox Secrets Manager as a new version of `demo/mysql`. The operator syncs it into `mysql-pass` within the refresh interval.

![The Create new version form in AccuKnox Secrets Manager with the corrected password entered](https://media.zernio.com/temp/1791272949358_v5sxmd9u_m10-new-version-12.jpg)

*Caption: The corrected password goes into AccuKnox Secrets Manager as a new version of demo/mysql.*

The running WordPress pod still holds the old password, because it read the secret at startup. Restart the deployment.

```bash
kubectl rollout restart deployment/wordpress
```

> **Warning.** The sync alone does not fix a running application. The operator updates the Kubernetes secret, and the restart makes WordPress use it. Plan a restart after every password change.

The demo deletes the pod from k9s instead, which has the same effect, because Kubernetes starts a new pod. The new pod reads the updated `mysql-pass`, and WordPress connects to MySQL again.

![The k9s pod list with a delete confirmation for the WordPress pod](https://media.zernio.com/temp/1791272950948_xmh275kp_m11-pod-delete.jpg)

*Caption: In k9s, the demo deletes the WordPress pod, and Kubernetes starts a new one.*

![The Kubernetes secret mysql-pass described in k9s, marked Updated secret](https://media.zernio.com/temp/1791272952658_b7xl7q0z_m12-updated-secret.jpg)

*Caption: mysql-pass shows the updated password, marked Updated secret.*

![The WordPress installer language screen loading again after the restart](https://media.zernio.com/temp/1791272955324_zfxps18q_m13-wordpress-restored.jpg)

*Caption: WordPress loads again after the restart, which shows it reached MySQL with the new password.*

## The Copy in the Namespace Is the Price of No Code Change

The External Secrets Operator is one of two ways to connect an application to AccuKnox Secrets Manager. The other is the SDK or REST API, which needs a few lines of code.

| | Direct SDK or REST API | External Secrets Operator |
| --- | --- | --- |
| Application code change | A few lines | None |
| Where the secret lives | In application memory only | In a Kubernetes secret |
| Picks up a new value | On the next read | After the application restarts |
| Runs on | Kubernetes and virtual machines | Kubernetes only |

> **Limitation.** The operator leaves a copy of the password in `mysql-pass`, and anyone with read access to that namespace can read it. It also does not reload a running application. Use the SDK for a secret that must stay out of the namespace, or for a virtual machine.

The demo changes the password by hand. In production, your application logic or a rotation job can write the new version. The password still lives in one place, with versions and an audit log, and the Kubernetes secret follows it.

## See the Sync, the Break and the Restart on a Live Cluster

The video runs the whole flow in under two minutes, in the order of this post.

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/kuiPcejfcHU" title="AccuKnox Secrets Manager Demo: Sync and Rotate Kubernetes Secrets with No Code Changes" frameborder="0" allowfullscreen></iframe>
```

[Watch the demo on YouTube](https://www.youtube.com/watch?v=kuiPcejfcHU).

## FAQs

### Does my application need a code change to read a synced secret?

Your application needs no code change. The External Secret creates a normal Kubernetes secret, and WordPress reads it through the same `secretKeyRef` it used before. The deployment file in the demo is the stock one.

### Does the application pick up the new password on its own?

The application does not reload it. The Kubernetes secret updates within about 10 seconds of a change in AccuKnox Secrets Manager. A running pod keeps the value it read at startup. Restart the deployment with `kubectl rollout restart deployment/wordpress`.

### Who can read the password inside Kubernetes?

Anyone with read access to the namespace can read the `mysql-pass` secret. If the secret must stay out of the namespace, call AccuKnox Secrets Manager from the application with the SDK instead.
