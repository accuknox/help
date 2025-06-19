# 📘 Knoxctl CLI Usage Cheatsheet

This document provides a quick reference guide for common `knoxctl` CLI operations. These commands help you interact with AccuKnox-managed Kubernetes clusters, nodes, and alerts. Use them to efficiently filter, inspect, and debug workloads across your cloud environments.

> ✅ Tip: Use the `--json` flag to get machine-readable output and integrate with other tools.

---

## 🔍 Cluster and Node Operations

| **Use Case** | **Command** |
|--------------|-------------|
| List all clusters with `"substring"` in name and list their nodes | `knoxctl api cluster list --clusterjq '.[] \| select(.ClusterName\|test("substring"))' --nodes` |
| List all nodes in cluster named `"nrs"` | `knoxctl api cluster list --clusterjq '.[] \| select(.ClusterName == "nrs")' --nodes` |
| Show node `"store03460"` in cluster `"nrs"` | `knoxctl api cluster list --clusterjq '.[] \| select(.ClusterName == "nrs")' --nodes --nodejq '.result[] \| select(.NodeName == "store03460")'` |
| Use page size of 100 for output | `--page-size 100` |
| Output results in JSON format | `--json` |

---

## 🚨 Alerts and Violations

| **Use Case** | **Command** |
|--------------|-------------|
| List alerts received in last 5 minutes on cluster `"nrs"` | `knoxctl api cluster alerts --clusterjq '.[] \| select(.ClusterName == "nrs")' --stime $(date --date='5 minutes ago' +%s) --json` |
| Identify unique policy violations / alert messages in last 5 minutes | `knoxctl api cluster alerts --clusterjq '.[] \| select(.ClusterName == "nrs")' --stime $(date --date='5 minutes ago' +%s) --alertjq '.response[] \| "\( .Message )"' --json \| jq -r '.[]' \| sort \| uniq -c` |
| Get alerts from node `"store04281"` in last 15 minutes | `knoxctl api cluster alerts --filters '{"field":"HostName","value":"store04281","op":"match"}' --stime $(date --date='15 minutes ago' +%s)` |
| Match substring `"idtrs"` in `Resource` field of alerts (last 15 mins) | `knoxctl api cluster alerts --alertjq '.response[] \| select(.Resource // "unknown" \| test("idtrs"))' --stime $(date --date='15 minutes ago' +%s)` |

---

!!!info
    For more help and examples, visit the official documentation at [help.accuknox.com](https://help.accuknox.com).
