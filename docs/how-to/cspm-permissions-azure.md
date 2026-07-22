---
title: Azure IAM Permissions Reference
description: The 209 permissions in the AccuKnox CSPM Azure reader role, with the reason and impact for each.
hide:
  - toc
---

# Azure Permissions Reference

AccuKnox's Azure scanner uses the **AK Reader Aligned Role, 209 read-only permissions** on Azure Resource Manager (ARM) resources. It reads configuration to detect misconfigurations, with no write or delete access.

Every permission is listed below, grouped by resource provider. Where several permissions serve the same purpose, they share one row. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [Azure prerequisites](cspm-prereq-azure.md) for setup steps.

<div class="iam-tables" markdown="1">

## Advisor (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Advisor/recommendations/read` | **Function:** Reads Azure Advisor recommendations across cost, security, reliability, and performance<br>**Findings:** High-impact Advisor recommendations, cost optimization opportunities, reliability gaps<br>**Impact if not granted:** Cannot surface Azure-native optimization recommendations to the customer. |

## AlertsManagement (1)

| Permission | Rationale |
|---|---|
| `Microsoft.AlertsManagement/alerts/read` | **Function:** Reads unified alerts management interface<br>**Findings:** Alerts management not consolidated, missing smart groups<br>**Impact if not granted:** Cannot audit alerts through the unified alerts API. |

## ApiManagement (4)

| Permission | Rationale |
|---|---|
| `Microsoft.ApiManagement/service/apis/read` | **Function:** Reads APIs published through API Management<br>**Findings:** APIs without OAuth/OIDC, missing subscription key requirement, missing rate limiting<br>**Impact if not granted:** Cannot audit APIs exposed through APIM. |
| `Microsoft.ApiManagement/service/backends/read` | **Function:** Reads backend service definitions in API Management<br>**Findings:** Backend using HTTP instead of HTTPS, missing certificate validation<br>**Impact if not granted:** Cannot audit APIM backend configurations. |
| `Microsoft.ApiManagement/service/products/read` | **Function:** Reads API Management product definitions<br>**Findings:** Products with subscription required disabled, open products exposing sensitive APIs<br>**Impact if not granted:** Cannot audit product-level API grouping. |
| `Microsoft.ApiManagement/service/read` | **Function:** Enumerates API Management instances<br>**Findings:** APIM with public access, missing VNet integration, using Consumption tier for critical APIs, weak SSL/TLS<br>**Impact if not granted:** Cannot audit APIM at all. |

## AppConfiguration (1)

| Permission | Rationale |
|---|---|
| `Microsoft.AppConfiguration/configurationStores/read` | **Function:** Reads App Configuration store configurations<br>**Findings:** App Config with public access, missing private endpoint, missing CMK, missing purge protection<br>**Impact if not granted:** Cannot audit App Configuration security. |

## AppPlatform (1)

| Permission | Rationale |
|---|---|
| `Microsoft.AppPlatform/Spring/read` | **Function:** Reads Azure Spring Cloud (Spring Apps) service configuration - apps, deployments, TLS settings, config servers  [NOTE] RETIRED - Retained to support existing Spring Cloud customers.<br>**Findings:** Public network access enabled, missing customer-managed encryption, missing diagnostic logging, weak TLS<br>**Impact if not granted:** Cannot audit Spring Cloud instances deployed before Microsoft retired the offering for new customers. |

## Authorization (4)

| Permission | Rationale |
|---|---|
| `Microsoft.Authorization/denyAssignments/read` | **Function:** Reads deny assignments (explicit denials layered over role assignments)<br>**Findings:** Missing deny assignments on production resources<br>**Impact if not granted:** Cannot audit denial-based access controls. |
| `Microsoft.Authorization/locks/read` | **Function:** Reads management locks on subscriptions, resource groups, and individual resources<br>**Findings:** Resource groups without delete locks, critical resources without CanNotDelete locks, missing ReadOnly locks on shared resources<br>**Impact if not granted:** Cannot detect resources without protection against accidental deletion or modification. |
| `Microsoft.Authorization/roleAssignments/read` | **Function:** Reads Azure RBAC role assignments (who has what role, at what scope)<br>**Findings:** Owner role assigned at subscription scope, guest users with elevated roles, service principals with Contributor at root, stale role assignments<br>**Impact if not granted:** Cannot audit privileged access or detect over-permissioned users and service principals. |
| `Microsoft.Authorization/roleDefinitions/read` | **Function:** Reads Azure RBAC role definitions (built-in and custom roles)<br>**Findings:** Custom roles with wildcard actions, custom roles duplicating built-in roles, unused custom roles<br>**Impact if not granted:** Cannot audit custom role definitions for excessive permissions. |

## Automation (3)

| Permission | Rationale |
|---|---|
| `Microsoft.Automation/automationAccounts/read` | **Function:** Reads Azure Automation automation account<br>**Findings:** Runbook with plaintext credentials, variable without encryption, automation account with public access, missing managed identity<br>**Impact if not granted:** Cannot audit automation account security. |
| `Microsoft.Automation/automationAccounts/runbooks/read` | **Function:** Reads Azure Automation runbooks<br>**Findings:** Runbook with plaintext credentials, variable without encryption, automation account with public access, missing managed identity<br>**Impact if not granted:** Cannot audit automation account security. |
| `Microsoft.Automation/automationAccounts/variables/read` | **Function:** Reads Azure Automation variables<br>**Findings:** Runbook with plaintext credentials, variable without encryption, automation account with public access, missing managed identity<br>**Impact if not granted:** Cannot audit automation account security. |

## Batch (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Batch/batchAccounts/read` | **Function:** Enumerates Azure Batch accounts used for large-scale parallel workloads<br>**Findings:** Batch with shared key auth, missing user subscription authentication, no CMK encryption, public network access<br>**Impact if not granted:** Cannot audit Batch account security. |

## Cache (5)

| Permission | Rationale |
|---|---|
| `Microsoft.Cache/redis/firewallRules/read` `Microsoft.Cache/redis/linkedServers/read` `Microsoft.Cache/redis/patchSchedules/read` `Microsoft.Cache/redis/privateEndpointConnections/read` `Microsoft.Cache/redis/read` | **Function:** Reads configuration of Azure Cache for Redis (classic) instances - firewall rules, patch schedules, private endpoint connections, linked servers, TLS version  [NOTE] RETIRED - Microsoft is retiring classic Redis Cache. We retain this permission specifically to continue supporting customers who still run legacy Redis instances that pre-date the retirement announcement.<br>**Findings:** Weak TLS, missing private endpoint, missing firewall rules, insecure linked server, disabled non-SSL port, missing diagnostic settings<br>**Impact if not granted:** Cannot scan any existing Redis Cache instances. Customers running legacy Redis (from before Microsoft announced retirement) will have zero visibility into misconfigurations. |

## CognitiveServices (3)

| Permission | Rationale |
|---|---|
| `Microsoft.CognitiveServices/accounts/deployments/read` | **Function:** Reads Cognitive Services / Azure OpenAI model deployments configuration<br>**Findings:** Account with public access, missing private endpoint, disabled local auth not enforced, missing CMK, missing diagnostic logging, weak network ACLs<br>**Impact if not granted:** Cannot audit AI service security. |
| `Microsoft.CognitiveServices/accounts/models/read` | **Function:** Reads Cognitive Services / Azure OpenAI models configuration<br>**Findings:** Account with public access, missing private endpoint, disabled local auth not enforced, missing CMK, missing diagnostic logging, weak network ACLs<br>**Impact if not granted:** Cannot audit AI service security. |
| `Microsoft.CognitiveServices/accounts/read` | **Function:** Reads Cognitive Services / Azure OpenAI account configuration<br>**Findings:** Account with public access, missing private endpoint, disabled local auth not enforced, missing CMK, missing diagnostic logging, weak network ACLs<br>**Impact if not granted:** Cannot audit AI service security. |

## Compute (17)

| Permission | Rationale |
|---|---|
| `Microsoft.Compute/availabilitySets/read` | **Function:** Reads VM availability sets used for HA within a single datacenter<br>**Findings:** VMs not placed in availability sets, availability set with insufficient fault domains<br>**Impact if not granted:** Cannot audit HA deployments. |
| `Microsoft.Compute/diskAccesses/read` | **Function:** Reads disk access resources (private endpoint configurations for managed disks)<br>**Findings:** Disk with public network access when private endpoint is available, misconfigured disk access resource<br>**Impact if not granted:** Cannot verify private link is configured for disk imports/exports. |
| `Microsoft.Compute/diskEncryptionSets/read` | **Function:** Reads disk encryption sets used to hold customer-managed keys for disk encryption<br>**Findings:** Disk encryption set using system-assigned identity, key rotation not configured, encryption at host not enabled<br>**Impact if not granted:** Cannot verify CMK-based disk encryption. |
| `Microsoft.Compute/disks/read` | **Function:** Enumerates managed disks and reads their encryption, size, and attachment state<br>**Findings:** Unencrypted managed disks, disks without customer-managed keys, orphaned disks, disks with public network access<br>**Impact if not granted:** Cannot audit disk-level security. |
| `Microsoft.Compute/galleries/read` | **Function:** Reads Compute Image Galleries used for shared VM images<br>**Findings:** Image gallery without CMK encryption, publicly accessible image versions, missing image replication<br>**Impact if not granted:** Cannot audit image gallery configuration. |
| `Microsoft.Compute/locations/vmSizes/read` `Microsoft.Compute/skus/read` | **Function:** Reads catalog of available VM SKUs and sizes by region<br>**Findings:** None directly - reference data used by other checks.<br>**Impact if not granted:** Reduces accuracy of "VM using deprecated SKU" checks. |
| `Microsoft.Compute/snapshots/read` | **Function:** Enumerates managed disk snapshots and their encryption state<br>**Findings:** Unencrypted snapshots, snapshots with public access, stale snapshots<br>**Impact if not granted:** Cannot audit snapshot security. |
| `Microsoft.Compute/sshPublicKeys/read` | **Function:** Reads SSH public keys stored as Azure resources<br>**Findings:** SSH keys without tags, SSH keys without associated resources<br>**Impact if not granted:** Cannot audit SSH key inventory. |
| `Microsoft.Compute/virtualMachineScaleSets/extensions/read` | **Function:** Reads extensions on VMSS resources (security agents, monitoring)<br>**Findings:** VMSS without Log Analytics extension, VMSS without anti-malware, VMSS without dependency agent<br>**Impact if not granted:** Cannot detect missing security agents on scale set instances. |
| `Microsoft.Compute/virtualMachineScaleSets/instanceView/read` | **Function:** Reads runtime status of VMSS scale set instances<br>**Findings:** VMSS instances failed, instances pending upgrade<br>**Impact if not granted:** Cannot detect unhealthy or misconfigured VMSS instances. |
| `Microsoft.Compute/virtualMachineScaleSets/read` | **Function:** Enumerates Virtual Machine Scale Sets and their configuration (SKU, capacity, upgrade policy)<br>**Findings:** VMSS without managed identity, VMSS with password auth, VMSS without automatic OS upgrade, VMSS using outdated image<br>**Impact if not granted:** Cannot audit scale sets used for AKS node pools, application workloads. |
| `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/instanceView/read` `Microsoft.Compute/virtualMachines/instanceView/read` | **Function:** Reads runtime state of VMs (power state, agent status, patch status)<br>**Findings:** VM in stopped state, agent not ready, pending reboot after patches<br>**Impact if not granted:** Cannot detect VMs in unhealthy states or with agent problems. |
| `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read` | **Function:** Reads individual VM instances within a Virtual Machine Scale Set<br>**Findings:** VMSS instances out of sync, unhealthy instances, unpatched instances<br>**Impact if not granted:** Cannot audit VMSS instances at the VM level. |
| `Microsoft.Compute/virtualMachines/extensions/read` | **Function:** Reads VM extensions installed on virtual machines (Log Analytics agent, anti-malware, Azure Backup, custom scripts)<br>**Findings:** Log Analytics agent missing, anti-malware not installed, Azure Backup extension missing, disk encryption extension absent, dependency agent missing<br>**Impact if not granted:** Cannot detect missing security agents on VMs. |
| `Microsoft.Compute/virtualMachines/read` | **Function:** Enumerates virtual machines and reads their configuration (OS, SKU, network profile, identity)<br>**Findings:** VMs without managed identity, VMs with password authentication, VMs without accelerated networking, unpatched OS versions, VMs on legacy SKUs<br>**Impact if not granted:** Cannot audit any virtual machines. |

## Consumption (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Consumption/usageDetails/read` | **Function:** Reads billing and cost management data<br>**Findings:** Cost anomalies flagged by Advisor, unusual spending patterns<br>**Impact if not granted:** Cannot correlate cost anomalies with security posture. |

## ContainerInstance (1)

| Permission | Rationale |
|---|---|
| `Microsoft.ContainerInstance/containerGroups/read` | **Function:** Reads Azure Container Instances (ACI) - serverless containers<br>**Findings:** ACI without private VNet integration, ACI with public IP, ACI using latest tag, ACI with excessive resource allocation<br>**Impact if not granted:** Cannot audit ACI deployments. |

## ContainerRegistry (3)

| Permission | Rationale |
|---|---|
| `Microsoft.ContainerRegistry/registries/read` | **Function:** Reads Azure Container Registry registry configuration<br>**Findings:** Registry with public access, admin user enabled, missing content trust, missing quarantine policy, missing image scanning<br>**Impact if not granted:** Cannot audit container image registries. |
| `Microsoft.ContainerRegistry/registries/replications/read` | **Function:** Reads Azure Container Registry registry replications configuration<br>**Findings:** Registry with public access, admin user enabled, missing content trust, missing quarantine policy, missing image scanning<br>**Impact if not granted:** Cannot audit container image registries. |
| `Microsoft.ContainerRegistry/registries/webhooks/read` | **Function:** Reads Azure Container Registry registry webhooks configuration<br>**Findings:** Registry with public access, admin user enabled, missing content trust, missing quarantine policy, missing image scanning<br>**Impact if not granted:** Cannot audit container image registries. |

## ContainerService (4)

| Permission | Rationale |
|---|---|
| `Microsoft.ContainerService/locations/orchestrators/read` | **Function:** Reads available Kubernetes orchestrator versions per region<br>**Findings:** None directly - reference data.<br>**Impact if not granted:** Reduced accuracy of version-currency checks. |
| `Microsoft.ContainerService/managedClusters/agentPools/read` | **Function:** Reads AKS node pool configuration<br>**Findings:** Node pool without auto-upgrade, spot instances without eviction handling, node pool without private network, insufficient max pods<br>**Impact if not granted:** Cannot audit AKS node pools. |
| `Microsoft.ContainerService/managedClusters/read` | **Function:** Enumerates AKS clusters and reads their configuration (Kubernetes version, network profile, identity, RBAC settings)<br>**Findings:** AKS with kubenet instead of Azure CNI, missing private cluster, RBAC disabled, missing Entra ID integration, insecure API server, network policy not enforced, missing pod security policies<br>**Impact if not granted:** Cannot audit any AKS clusters. |
| `Microsoft.ContainerService/managedClusters/upgradeProfiles/read` | **Function:** Reads available Kubernetes version upgrades for AKS clusters<br>**Findings:** AKS running deprecated K8s version, cluster more than 2 minor versions behind current<br>**Impact if not granted:** Cannot detect clusters running outdated Kubernetes versions. |

## DBforMySQL (3)

| Permission | Rationale |
|---|---|
| `Microsoft.DBforMySQL/flexibleServers/configurations/read` | **Function:** Reads MySQL Flexible Server server parameters (my.cnf)<br>**Findings:** Server with public access, SSL disabled, weak firewall rules, missing binlog configuration, insecure server parameters<br>**Impact if not granted:** Cannot audit MySQL Flex configurations. |
| `Microsoft.DBforMySQL/flexibleServers/firewallRules/read` | **Function:** Reads MySQL Flexible Server firewall rules<br>**Findings:** Server with public access, SSL disabled, weak firewall rules, missing binlog configuration, insecure server parameters<br>**Impact if not granted:** Cannot audit MySQL Flex configurations. |
| `Microsoft.DBforMySQL/flexibleServers/read` | **Function:** Reads MySQL Flexible Server server<br>**Findings:** Server with public access, SSL disabled, weak firewall rules, missing binlog configuration, insecure server parameters<br>**Impact if not granted:** Cannot audit MySQL Flex configurations. |

## DBforPostgreSQL (3)

| Permission | Rationale |
|---|---|
| `Microsoft.DBforPostgreSQL/flexibleServers/configurations/read` | **Function:** Reads PostgreSQL Flexible Server server parameters (postgresql.conf)<br>**Findings:** Server with public access, SSL enforcement disabled, weak firewall rules, missing Entra ID auth, insecure server parameters (log_statement, log_connections), missing backup configuration<br>**Impact if not granted:** Cannot audit PostgreSQL Flex configurations. |
| `Microsoft.DBforPostgreSQL/flexibleServers/firewallRules/read` | **Function:** Reads PostgreSQL Flexible Server firewall rules<br>**Findings:** Server with public access, SSL enforcement disabled, weak firewall rules, missing Entra ID auth, insecure server parameters (log_statement, log_connections), missing backup configuration<br>**Impact if not granted:** Cannot audit PostgreSQL Flex configurations. |
| `Microsoft.DBforPostgreSQL/flexibleServers/read` | **Function:** Reads PostgreSQL Flexible Server server<br>**Findings:** Server with public access, SSL enforcement disabled, weak firewall rules, missing Entra ID auth, insecure server parameters (log_statement, log_connections), missing backup configuration<br>**Impact if not granted:** Cannot audit PostgreSQL Flex configurations. |

## DataFactory (6)

| Permission | Rationale |
|---|---|
| `Microsoft.DataFactory/factories/datasets/read` `Microsoft.DataFactory/factories/linkedservices/read` `Microsoft.DataFactory/factories/pipelines/read` `Microsoft.DataFactory/factories/privateEndpointConnections/read` `Microsoft.DataFactory/factories/read` `Microsoft.DataFactory/factories/triggers/read` | **Function:** Reads Azure Data Factory + datasets + pipelines configuration<br>**Findings:** ADF without managed identity, missing customer-managed key, linked services with plaintext credentials, pipeline exposed to public network<br>**Impact if not granted:** Cannot audit data pipeline security. |

## Databricks (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Databricks/workspaces/read` | **Function:** Enumerates Azure Databricks workspaces<br>**Findings:** Databricks with public IP, missing VNet injection, missing customer-managed key, missing private link<br>**Impact if not granted:** Cannot audit Databricks workspaces. |

## Devices (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Devices/IotHubs/read` | **Function:** Reads Azure IoT Hub configuration<br>**Findings:** IoT Hub with public access, weak SAS policies, missing device authentication policies, weak encryption<br>**Impact if not granted:** Cannot audit IoT Hub security. |

## EventGrid (2)

| Permission | Rationale |
|---|---|
| `Microsoft.EventGrid/domains/read` | **Function:** Reads Event Grid domain configuration (custom topics grouped as domains)<br>**Findings:** Domain with public network access, missing private endpoint, weak input schema, missing CMK<br>**Impact if not granted:** Cannot audit Event Grid domain security. |
| `Microsoft.EventGrid/topics/read` | **Function:** Reads Event Grid topic configuration<br>**Findings:** Topic with public access, missing IP firewall, missing managed identity for delivery<br>**Impact if not granted:** Cannot audit Event Grid topic security. |

## EventHub (4)

| Permission | Rationale |
|---|---|
| `Microsoft.EventHub/namespaces/authorizationRules/read` | **Function:** Reads shared access authorization rules on Event Hub namespaces<br>**Findings:** SAS keys with Manage rights, root SAS keys still active, missing key rotation<br>**Impact if not granted:** Cannot audit Event Hub access keys. |
| `Microsoft.EventHub/namespaces/eventhubs/read` | **Function:** Reads individual Event Hubs within namespaces<br>**Findings:** Event Hub with excessive retention, missing capture configuration<br>**Impact if not granted:** Cannot audit individual event hubs. |
| `Microsoft.EventHub/namespaces/networkRuleSets/read` | **Function:** Reads network rules (IP and VNet) on Event Hub namespaces<br>**Findings:** Event Hub with default action Allow, missing VNet rules, wide-open IP filter<br>**Impact if not granted:** Cannot audit network-level Event Hub access controls. |
| `Microsoft.EventHub/namespaces/read` | **Function:** Enumerates Event Hub namespaces<br>**Findings:** Event Hub with public access, missing private endpoint, weak minimum TLS<br>**Impact if not granted:** Cannot audit Event Hub namespaces. |

## GuestConfiguration (1)

| Permission | Rationale |
|---|---|
| `Microsoft.GuestConfiguration/guestConfigurationAssignments/read` | **Function:** Reads guest configuration assignments (in-guest policy on VMs)<br>**Findings:** VMs without guest configuration extension, non-compliant OS baselines, missing password policies, missing audit policies<br>**Impact if not granted:** Cannot audit VM in-guest OS-level policy compliance. Defender for Servers loses visibility. |

## Insights (6)

| Permission | Rationale |
|---|---|
| `Microsoft.Insights/actionGroups/read` | **Function:** Reads action group configurations (who gets notified when alerts fire)<br>**Findings:** Alert rules without action groups, action groups without recipients, action groups with SMS-only notification<br>**Impact if not granted:** Cannot verify alert notifications are configured. |
| `Microsoft.Insights/activityLogAlerts/read` | **Function:** Reads activity log alert rules (alerts triggered by control-plane events)<br>**Findings:** Missing alert for NSG changes, missing alert for role assignment changes, missing alert for Key Vault operations, missing alert for firewall rule changes<br>**Impact if not granted:** Cannot verify alerts exist for security-relevant events. |
| `Microsoft.Insights/autoscalesettings/read` | **Function:** Reads autoscale rules on VM Scale Sets, App Service Plans<br>**Findings:** Missing autoscale on production workloads, autoscale limits too low/high, single-instance production deployments<br>**Impact if not granted:** Cannot audit autoscale configurations. |
| `Microsoft.Insights/components/read` | **Function:** Reads Application Insights instances<br>**Findings:** App Insights without workspace mode, missing sampling policies, missing CMK encryption<br>**Impact if not granted:** Cannot audit App Insights deployment. |
| `Microsoft.Insights/metricAlerts/read` | **Function:** Reads metric-based alert rules<br>**Findings:** Missing CPU alerts, missing network transfer alerts, missing failed sign-in alerts<br>**Impact if not granted:** Cannot audit performance and security metric alerts. |
| `Microsoft.Insights/metrics/read` | **Function:** Reads Azure Monitor metric definitions<br>**Findings:** None directly - metric data.<br>**Impact if not granted:** Cannot query resource metrics for alerting rules. |

## KeyVault (7)

| Permission | Rationale |
|---|---|
| `Microsoft.KeyVault/checkNameAvailability/read` `Microsoft.KeyVault/locations/deletedVaults/read` `Microsoft.KeyVault/locations/operationResults/read` `Microsoft.KeyVault/operations/read` | **Function:** Reads Key Vault service-level metadata (name availability, operation results, locations)<br>**Findings:** None directly - service catalog data.<br>**Impact if not granted:** Reduced fidelity of Key Vault enumeration. |
| `Microsoft.KeyVault/vaults/keys/read` | **Function:** Enumerates keys stored in Key Vaults and reads their metadata<br>**Findings:** Keys without expiration date, keys older than rotation policy, keys without automatic rotation, weak key sizes<br>**Impact if not granted:** Cannot audit encryption key rotation and lifecycle. |
| `Microsoft.KeyVault/vaults/read` | **Function:** Enumerates Key Vaults and reads their SKU, access policies, and network ACLs<br>**Findings:** Key Vault with public network access, missing purge protection, soft-delete disabled, missing private endpoint, RBAC not enabled, access policies with wildcard permissions<br>**Impact if not granted:** Cannot audit Key Vaults - one of the most sensitive Azure resources. |
| `Microsoft.KeyVault/vaults/secrets/read` | **Function:** Enumerates secrets stored in Key Vaults (metadata only, not values)<br>**Findings:** Secrets without expiration, disabled secrets not cleaned up, secrets past expiration still in use<br>**Impact if not granted:** Cannot audit secret lifecycle. |

## Kusto (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Kusto/clusters/read` | **Function:** Reads Azure Data Explorer (Kusto) cluster configuration<br>**Findings:** Kusto cluster with public access, missing private endpoint, missing CMK, weak network configuration<br>**Impact if not granted:** Cannot audit ADX cluster security. |

## MachineLearningServices (2)

| Permission | Rationale |
|---|---|
| `Microsoft.MachineLearningServices/workspaces/computes/read` | **Function:** Reads Azure Machine Learning compute clusters and instances configuration<br>**Findings:** ML workspace with public access, missing HBI (High Business Impact) flag, missing CMK, compute with public IP, missing SSH restriction, missing diagnostic logging<br>**Impact if not granted:** Cannot audit ML workspace security. |
| `Microsoft.MachineLearningServices/workspaces/read` | **Function:** Reads Azure Machine Learning workspace configuration<br>**Findings:** ML workspace with public access, missing HBI (High Business Impact) flag, missing CMK, compute with public IP, missing SSH restriction, missing diagnostic logging<br>**Impact if not granted:** Cannot audit ML workspace security. |

## Maintenance (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Maintenance/maintenanceConfigurations/read` | **Function:** Reads maintenance configurations (planned patching windows)<br>**Findings:** VMs without maintenance configuration, patch orchestration missing<br>**Impact if not granted:** Cannot audit maintenance scheduling. |

## ManagedServices (2)

| Permission | Rationale |
|---|---|
| `Microsoft.ManagedServices/registrationAssignments/read` `Microsoft.ManagedServices/registrationDefinitions/read` | **Function:** Reads Azure Lighthouse delegated resource management assignments<br>**Findings:** Excessive Lighthouse delegations, missing tenant boundaries<br>**Impact if not granted:** Cannot audit cross-tenant management relationships. |

## Network (37)

| Permission | Rationale |
|---|---|
| `Microsoft.Network/applicationGatewayWebApplicationFirewallPolicies/read` | **Function:** Reads WAF policies attached to Application Gateways<br>**Findings:** WAF in Detection mode instead of Prevention, missing OWASP rule set, WAF policy without custom rules for known threats<br>**Impact if not granted:** Cannot audit WAF rule configurations. |
| `Microsoft.Network/applicationGateways/read` | **Function:** Reads Application Gateway configuration (listeners, SSL, WAF)<br>**Findings:** App Gateway without WAF, weak SSL policy, missing HTTP to HTTPS redirect, self-signed certificates<br>**Impact if not granted:** Cannot audit L7 load balancer security. |
| `Microsoft.Network/applicationSecurityGroups/read` | **Function:** Reads Network applicationSecurityGroups configuration<br>**Findings:** Depends on the specific plugin using this permission.<br>**Impact if not granted:** Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/azureFirewalls/read` | **Function:** Reads Azure Firewall and firewall policy configuration<br>**Findings:** Firewall in Alert-only mode, missing IDPS, threat intel not enabled, permissive application rules<br>**Impact if not granted:** Cannot audit Azure-native firewall rules. |
| `Microsoft.Network/bastionHosts/read` | **Function:** Reads Azure Bastion hosts<br>**Findings:** Bastion with Basic SKU (weaker features), Bastion without native client support, missing shareable link controls<br>**Impact if not granted:** Cannot audit Bastion configuration for secure jump access. |
| `Microsoft.Network/dnszones/read` `Microsoft.Network/privateDnsZones/read` `Microsoft.Network/privateDnsZones/virtualNetworkLinks/read` | **Function:** Reads public and private DNS zones<br>**Findings:** DNS zone without DNSSEC, private DNS not linked to VNet, dangling DNS records<br>**Impact if not granted:** Cannot audit DNS configuration. |
| `Microsoft.Network/expressRouteCircuits/read` | **Function:** Reads ExpressRoute circuit configurations for private hybrid connectivity<br>**Findings:** ExpressRoute without BGP MD5 authentication, missing FastPath, weak peering configuration<br>**Impact if not granted:** Cannot audit ExpressRoute security posture. |
| `Microsoft.Network/loadBalancers/backendAddressPools/read` | **Function:** Reads load balancer backend address pools configuration<br>**Findings:** LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services<br>**Impact if not granted:** Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/frontendIPConfigurations/read` | **Function:** Reads load balancer frontend IP configurations configuration<br>**Findings:** LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services<br>**Impact if not granted:** Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/inboundNatRules/read` | **Function:** Reads load balancer inbound NAT rules configuration<br>**Findings:** LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services<br>**Impact if not granted:** Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/loadBalancingRules/read` | **Function:** Reads load balancer rules configuration<br>**Findings:** LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services<br>**Impact if not granted:** Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/outboundRules/read` | **Function:** Reads load balancer outbound rules configuration<br>**Findings:** LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services<br>**Impact if not granted:** Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/probes/read` | **Function:** Reads load balancer health probes configuration<br>**Findings:** LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services<br>**Impact if not granted:** Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/read` | **Function:** Reads load balancer configuration<br>**Findings:** LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services<br>**Impact if not granted:** Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/locations/serviceTags/read` | **Function:** Reads Azure service tag definitions used for NSG rule reasoning<br>**Findings:** None directly - reference data.<br>**Impact if not granted:** NSG rule analysis cannot distinguish "AzureFrontDoor.Backend" from a generic Internet range. |
| `Microsoft.Network/locations/usages/read` | **Function:** Reads Network locations usages configuration<br>**Findings:** Depends on the specific plugin using this permission.<br>**Impact if not granted:** Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/natGateways/read` | **Function:** Reads NAT Gateway configuration for outbound connectivity<br>**Findings:** Subnets without NAT Gateway using default outbound (deprecated), missing NAT for private endpoints<br>**Impact if not granted:** Cannot audit NAT Gateway assignments. |
| `Microsoft.Network/networkInterfaces/ipConfigurations/read` | **Function:** Reads Network networkInterfaces ipConfigurations configuration<br>**Findings:** Depends on the specific plugin using this permission.<br>**Impact if not granted:** Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/networkInterfaces/read` | **Function:** Reads network interfaces attached to VMs<br>**Findings:** NIC with IP forwarding enabled, NIC without NSG association, NIC with accelerated networking disabled<br>**Impact if not granted:** Cannot correlate VMs to their networking configuration. |
| `Microsoft.Network/networkProfiles/read` | **Function:** Reads network profiles used by Container Instances<br>**Findings:** Container instance in public subnet, ACI without private subnet integration<br>**Impact if not granted:** Cannot audit ACI network configurations. |
| `Microsoft.Network/networkSecurityGroups/defaultSecurityRules/read` | **Function:** Reads default (built-in) NSG rules that Azure provides automatically<br>**Findings:** None directly - reference data used to distinguish default vs custom rules.<br>**Impact if not granted:** Reduced context when analyzing effective NSG posture. |
| `Microsoft.Network/networkSecurityGroups/read` | **Function:** Enumerates NSGs and their associated subnets and network interfaces<br>**Findings:** Subnets without NSG association, NSG with all rules permissive, orphaned NSGs, NSG missing on public-facing subnet<br>**Impact if not granted:** Cannot audit network security groups at all. |
| `Microsoft.Network/networkSecurityGroups/securityRules/read` | **Function:** Reads custom inbound and outbound security rules defined on Network Security Groups<br>**Findings:** Wide-open inbound rules (0.0.0.0/0), SSH/RDP open to Internet, database ports exposed publicly, permissive outbound rules<br>**Impact if not granted:** Cannot audit NSG rule configurations - a critical network security control. |
| `Microsoft.Network/networkWatchers/flowLogs/read` | **Function:** Reads NSG flow log configuration<br>**Findings:** NSG without flow logs enabled, flow logs without traffic analytics, insufficient flow log retention<br>**Impact if not granted:** Cannot verify network traffic is being logged. |
| `Microsoft.Network/networkWatchers/read` | **Function:** Reads Network Watcher services per region<br>**Findings:** Network Watcher not enabled in region<br>**Impact if not granted:** Cannot verify Network Watcher is enabled for troubleshooting and flow logs. |
| `Microsoft.Network/privateEndpoints/read` | **Function:** Reads Network privateEndpoints configuration<br>**Findings:** Depends on the specific plugin using this permission.<br>**Impact if not granted:** Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/publicIPAddresses/read` | **Function:** Enumerates public IP addresses and their associations<br>**Findings:** Orphaned public IPs, public IPs on non-production resources, basic SKU public IPs (deprecated), public IPs without DDoS protection<br>**Impact if not granted:** Cannot audit externally exposed IP addresses. |
| `Microsoft.Network/routeTables/read` | **Function:** Reads user-defined routes (UDRs) and route tables<br>**Findings:** Missing default route to firewall/NVA, UDR bypassing security appliances<br>**Impact if not granted:** Cannot audit custom routing. |
| `Microsoft.Network/routeTables/routes/read` | **Function:** Reads Network routeTables routes configuration<br>**Findings:** Depends on the specific plugin using this permission.<br>**Impact if not granted:** Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/virtualNetworkGateways/read` | **Function:** Reads VPN and ExpressRoute gateways for hybrid connectivity<br>**Findings:** Gateway using weak SKU, missing active-active configuration, weak IPsec policy<br>**Impact if not granted:** Cannot audit hybrid network gateways. |
| `Microsoft.Network/virtualNetworks/read` | **Function:** Enumerates virtual networks and reads their address space and configuration<br>**Findings:** VNets without DDoS protection, VNets with overlapping ranges, VNets without flow logs<br>**Impact if not granted:** Cannot audit VNet topology. |
| `Microsoft.Network/virtualNetworks/subnets/read` | **Function:** Reads subnets within virtual networks (address range, delegation, service endpoints, private endpoint policy)<br>**Findings:** Subnet without NSG, subnet without service endpoints, subnet allowing multiple delegations, subnet with overly permissive private endpoint policy<br>**Impact if not granted:** Cannot audit subnet-level segmentation. |
| `Microsoft.Network/virtualNetworks/subnets/resourceNavigationLinks/read` `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/read` | **Function:** Reads links between subnets and the resources that use them<br>**Findings:** None directly - dependency data for other checks.<br>**Impact if not granted:** Cannot trace subnet-to-resource associations. |
| `Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read` | **Function:** Reads VNet peering configurations between virtual networks<br>**Findings:** Peering without gateway transit control, peering allowing forwarded traffic, unauthorized cross-tenant peerings<br>**Impact if not granted:** Cannot audit cross-VNet connectivity. |

## OperationalInsights (1)

| Permission | Rationale |
|---|---|
| `Microsoft.OperationalInsights/workspaces/read` | **Function:** Reads Log Analytics workspace configuration<br>**Findings:** Missing Log Analytics workspace, workspace with default retention (too short), missing security solutions installed, workspace not linked to Defender<br>**Impact if not granted:** Cannot verify Log Analytics is receiving logs. Breaks 30+ Defender and monitor checks. |

## RecoveryServices (3)

| Permission | Rationale |
|---|---|
| `Microsoft.RecoveryServices/vaults/backupPolicies/read` | **Function:** Reads backup policies configured in Recovery Services vaults<br>**Findings:** Backup retention below policy minimum, missing weekly backups, missing yearly backups for compliance<br>**Impact if not granted:** Cannot audit backup retention and frequency. |
| `Microsoft.RecoveryServices/vaults/backupProtectedItems/read` | **Function:** Reads items protected by Azure Backup (VMs, SQL DBs, file shares)<br>**Findings:** Critical VMs without backup, databases without backup, backup jobs failing repeatedly<br>**Impact if not granted:** Cannot verify what is actually being backed up. |
| `Microsoft.RecoveryServices/vaults/read` | **Function:** Enumerates Recovery Services vaults<br>**Findings:** Vault with soft delete disabled, missing immutability, missing CMK, missing private endpoint, cross-subscription restore disabled<br>**Impact if not granted:** Cannot audit backup vault security. |

## ResourceGraph (4)

| Permission | Rationale |
|---|---|
| `Microsoft.ResourceGraph/operations/read` `Microsoft.ResourceGraph/resourceChanges/read` `Microsoft.ResourceGraph/resources/read` `Microsoft.ResourceGraph/resourcesHistory/read` | **Function:** Enables cross-scope resource querying via Azure Resource Graph<br>**Findings:** None directly - foundational for Defender inventory.<br>**Impact if not granted:** Defender for Cloud cannot enumerate resources across management scopes. |

## Resources (9)

| Permission | Rationale |
|---|---|
| `Microsoft.Resources/deployments/read` | **Function:** Reads ARM deployment history for the subscription<br>**Findings:** Failed deployments retained, sensitive parameters in deployment history<br>**Impact if not granted:** Cannot audit ARM template usage or deployment metadata. |
| `Microsoft.Resources/links/read` | **Function:** Reads resource links (cross-resource dependencies)<br>**Findings:** Undocumented cross-resource dependencies<br>**Impact if not granted:** Cannot map dependencies between related resources. |
| `Microsoft.Resources/providers/read` | **Function:** Reads the list of registered Azure resource providers<br>**Findings:** Deprecated providers still registered, security-relevant providers not registered<br>**Impact if not granted:** Cannot verify which Azure services are enabled in the subscription. |
| `Microsoft.Resources/resources/read` `Microsoft.Resources/subscriptions/resources/read` | **Function:** Enumerates all Azure resources across the subscription regardless of resource group<br>**Findings:** Orphaned resources, resources without tags, resources missing required governance metadata<br>**Impact if not granted:** Scanner cannot build a complete resource inventory. |
| `Microsoft.Resources/subscriptions/locations/read` | **Function:** Reads the list of Azure regions available to the subscription<br>**Findings:** None - reference data used by region-scoped scans.<br>**Impact if not granted:** Scanner cannot iterate through regions correctly. |
| `Microsoft.Resources/subscriptions/read` | **Function:** Enumerates the Azure subscription and its metadata (tenant ID, tags, state, quota)<br>**Findings:** None - this is foundational. Without it, no findings can be produced.<br>**Impact if not granted:** Scanner cannot see the subscription at all. Total scan blackout. |
| `Microsoft.Resources/subscriptions/resourceGroups/read` | **Function:** Enumerates resource groups within the subscription<br>**Findings:** Resource groups without tags, resource groups without management locks, empty resource groups<br>**Impact if not granted:** Scanner cannot enumerate resources organized by resource group. |
| `Microsoft.Resources/tenants/read` | **Function:** Reads Entra tenant metadata visible to the subscription<br>**Findings:** None - reference data.<br>**Impact if not granted:** Cannot correlate subscription with its parent tenant. |

## Search (1)

| Permission | Rationale |
|---|---|
| `Microsoft.Search/searchServices/read` | **Function:** Reads Azure Cognitive Search services<br>**Findings:** Search with public access, missing private endpoint, admin keys not rotated, missing CMK encryption<br>**Impact if not granted:** Cannot audit search service configuration. |

## ServiceBus (5)

| Permission | Rationale |
|---|---|
| `Microsoft.ServiceBus/namespaces/authorizationRules/read` | **Function:** Reads Service Bus authorization rules configuration<br>**Findings:** SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled<br>**Impact if not granted:** Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/privateEndpointConnections/read` | **Function:** Reads Service Bus private endpoints configuration<br>**Findings:** SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled<br>**Impact if not granted:** Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/queues/read` | **Function:** Reads Service Bus queues configuration<br>**Findings:** SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled<br>**Impact if not granted:** Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/read` | **Function:** Reads Service Bus namespace configuration<br>**Findings:** SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled<br>**Impact if not granted:** Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/topics/read` | **Function:** Reads Service Bus topics configuration<br>**Findings:** SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled<br>**Impact if not granted:** Cannot audit Service Bus messaging security. |

## SignalRService (1)

| Permission | Rationale |
|---|---|
| `Microsoft.SignalRService/SignalR/read` | **Function:** Reads Azure SignalR Service configuration for real-time messaging<br>**Findings:** SignalR with public access, missing private endpoint, weak feature flags<br>**Impact if not granted:** Cannot audit SignalR security. |

## Sql (28)

| Permission | Rationale |
|---|---|
| `Microsoft.Sql/managedInstances/read` | **Function:** Reads Sql managedInstances configuration<br>**Findings:** Depends on the specific plugin using this permission.<br>**Impact if not granted:** Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Sql/servers/administrators/read` | **Function:** Reads SQL server Entra ID administrator configuration<br>**Findings:** SQL server without Entra ID admin, SQL admin is a user instead of a group<br>**Impact if not granted:** Cannot verify Entra ID authentication is enforced. |
| `Microsoft.Sql/servers/advancedThreatProtectionSettings/read` `Microsoft.Sql/servers/securityAlertPolicies/read` | **Function:** Reads Advanced Threat Protection and security alert policies on SQL servers<br>**Findings:** ATP disabled, alert emails not configured, security alerts not sent to admins<br>**Impact if not granted:** Cannot verify SQL ATP is configured. |
| `Microsoft.Sql/servers/auditingSettings/read` | **Function:** Reads server-level SQL auditing configuration<br>**Findings:** Server auditing disabled, audit log destination missing, insufficient retention<br>**Impact if not granted:** Cannot verify SQL server auditing. |
| `Microsoft.Sql/servers/connectionPolicies/read` | **Function:** Reads SQL server connection policy (Default vs Proxy vs Redirect)<br>**Findings:** Connection policy set to Proxy where Redirect would be more secure<br>**Impact if not granted:** Cannot audit connection routing. |
| `Microsoft.Sql/servers/databases/auditingSettings/read` | **Function:** Reads SQL database auditing configuration<br>**Findings:** Database auditing disabled, audit log retention too short, audit not sent to Log Analytics/storage<br>**Impact if not granted:** Cannot verify database auditing is enabled. |
| `Microsoft.Sql/servers/databases/automaticTuning/read` | **Function:** Reads automatic tuning settings on SQL databases<br>**Findings:** Automatic tuning disabled, force plan not enabled<br>**Impact if not granted:** Cannot verify performance tuning configuration. |
| `Microsoft.Sql/servers/databases/backupShortTermRetentionPolicies/read` | **Function:** Reads short-term backup retention policy on SQL databases<br>**Findings:** Backup retention below regulatory minimum, missing PITR configuration<br>**Impact if not granted:** Cannot audit backup retention. |
| `Microsoft.Sql/servers/databases/currentSensitivityLabels/read` `Microsoft.Sql/servers/databases/sensitivityLabels/read` | **Function:** Reads sensitivity labels (data classification) on SQL database columns<br>**Findings:** Sensitive columns unclassified, missing PII classification, no confidentiality labels<br>**Impact if not granted:** Cannot verify data classification. |
| `Microsoft.Sql/servers/databases/dataMaskingPolicies/read` | **Function:** Reads dynamic data masking rules on SQL databases<br>**Findings:** No data masking on PII columns, data masking disabled<br>**Impact if not granted:** Cannot audit data masking for sensitive columns. |
| `Microsoft.Sql/servers/databases/ledgerDigestUploads/read` | **Function:** Reads Ledger digest upload configuration (SQL Ledger tamper evidence)<br>**Findings:** Ledger enabled without digest uploads, missing digest storage<br>**Impact if not granted:** Cannot audit Ledger tamper-evidence configuration. |
| `Microsoft.Sql/servers/databases/read` | **Function:** Enumerates SQL databases within SQL servers<br>**Findings:** Databases without TDE, databases in wrong SKU, deprecated compatibility levels, databases without backup configuration<br>**Impact if not granted:** Cannot audit any SQL databases. |
| `Microsoft.Sql/servers/databases/syncGroups/read` | **Function:** Reads SQL Data Sync group configuration<br>**Findings:** Sync group without conflict resolution policy<br>**Impact if not granted:** Cannot audit database sync configurations. |
| `Microsoft.Sql/servers/databases/transparentDataEncryption/read` | **Function:** Reads Transparent Data Encryption (TDE) status on SQL databases<br>**Findings:** TDE disabled, TDE using service-managed key instead of customer-managed key<br>**Impact if not granted:** Cannot verify at-rest encryption is enabled. |
| `Microsoft.Sql/servers/databases/vulnerabilityAssessments/read` `Microsoft.Sql/servers/databases/vulnerabilityAssessments/scans/read` | **Function:** Reads SQL database vulnerability assessment configuration and scan results<br>**Findings:** Vulnerability assessment not configured, missing storage for scan results, unresolved high-severity findings<br>**Impact if not granted:** Cannot verify vulnerability scanning is configured. |
| `Microsoft.Sql/servers/devOpsAuditingSettings/read` | **Function:** Reads DevOps auditing settings on SQL servers<br>**Findings:** DevOps auditing not enabled<br>**Impact if not granted:** Cannot audit DDL change tracking. |
| `Microsoft.Sql/servers/elasticPools/read` | **Function:** Reads SQL elastic pool configuration<br>**Findings:** Elastic pool overprovisioned, elastic pool with wrong SKU, single-database configuration where elastic pool would be more efficient<br>**Impact if not granted:** Cannot audit elastic pool utilization. |
| `Microsoft.Sql/servers/encryptionProtector/read` | **Function:** Reads encryption protector (CMK) configuration on SQL servers<br>**Findings:** SQL server using service-managed key instead of CMK, encryption protector not rotated<br>**Impact if not granted:** Cannot verify SQL uses customer-managed keys. |
| `Microsoft.Sql/servers/failoverGroups/read` | **Function:** Reads SQL failover group configuration for HA/DR<br>**Findings:** Missing failover group, secondary in same region as primary, manual failover configured for critical DB<br>**Impact if not granted:** Cannot audit HA/DR posture. |
| `Microsoft.Sql/servers/firewallRules/read` `Microsoft.Sql/servers/outboundFirewallRules/read` | **Function:** Reads SQL server firewall rules<br>**Findings:** Firewall rule allowing 0.0.0.0-255.255.255.255, permissive Azure services rule, missing IP restriction<br>**Impact if not granted:** Cannot detect wide-open SQL exposure. |
| `Microsoft.Sql/servers/read` | **Function:** Enumerates SQL servers and reads their configuration<br>**Findings:** SQL server with public network access, missing minimum TLS version, missing Entra ID admin, weak firewall rules<br>**Impact if not granted:** Cannot audit any SQL servers. |
| `Microsoft.Sql/servers/restorableDroppedDatabases/read` | **Function:** Reads databases marked for deletion but still recoverable<br>**Findings:** Excessive number of dropped databases retained, dropped databases containing sensitive data<br>**Impact if not granted:** Cannot audit dropped-database retention. |
| `Microsoft.Sql/servers/virtualNetworkRules/read` | **Function:** Reads VNet rules on SQL servers (private access through subnets)<br>**Findings:** SQL server without VNet rules, VNet rules missing ignore-missing-endpoint flag<br>**Impact if not granted:** Cannot verify network-level SQL access controls. |
| `Microsoft.Sql/servers/vulnerabilityAssessments/read` | **Function:** Reads server-level vulnerability assessment configuration<br>**Findings:** Server-level VA not configured, VA storage account missing<br>**Impact if not granted:** Cannot verify VA is set up at server scope. |

## Storage (14)

| Permission | Rationale |
|---|---|
| `Microsoft.Storage/storageAccounts/blobServices/containers/immutabilityPolicies/read` | **Function:** Reads WORM (Write Once Read Many) immutability policies on blob containers<br>**Findings:** Container without immutability policy where required, unlocked immutability policies, insufficient retention period<br>**Impact if not granted:** Cannot verify compliance requirements for immutable data (financial records, healthcare). |
| `Microsoft.Storage/storageAccounts/blobServices/containers/read` | **Function:** Enumerates blob containers within storage accounts and reads their access level<br>**Findings:** Anonymous public read access, publicly accessible container, missing CMK encryption on container, missing immutability policy<br>**Impact if not granted:** Cannot detect publicly accessible blob containers - a top source of data breaches. |
| `Microsoft.Storage/storageAccounts/blobServices/read` | **Function:** Reads blob service properties (versioning, soft delete, change feed, encryption)<br>**Findings:** Blob soft delete disabled, versioning disabled, missing change feed, insufficient retention<br>**Impact if not granted:** Cannot verify blob-level data protection controls. |
| `Microsoft.Storage/storageAccounts/encryptionScopes/read` | **Function:** Reads encryption scope configurations on storage accounts<br>**Findings:** Encryption scope using Microsoft-managed key instead of CMK, infrastructure encryption disabled<br>**Impact if not granted:** Cannot verify granular encryption scope settings. |
| `Microsoft.Storage/storageAccounts/fileServices/read` `Microsoft.Storage/storageAccounts/fileServices/shares/read` | **Function:** Enumerates Azure File shares and reads share-level access settings<br>**Findings:** File share with public access, missing SMB security settings, insecure share permissions<br>**Impact if not granted:** Cannot audit file share exposure. |
| `Microsoft.Storage/storageAccounts/localUsers/read` | **Function:** Reads local users configured on storage accounts (SFTP feature)<br>**Findings:** SFTP enabled without home directory, SSH key auth disabled, weak permission scope<br>**Impact if not granted:** Cannot audit SFTP user access on storage accounts. |
| `Microsoft.Storage/storageAccounts/managementPolicies/read` | **Function:** Reads lifecycle management policies on storage accounts<br>**Findings:** Missing lifecycle policy, no tier-down policy for cold data, missing automatic deletion for expired blobs<br>**Impact if not granted:** Cannot audit blob tiering and deletion policies. |
| `Microsoft.Storage/storageAccounts/privateEndpointConnections/read` | **Function:** Reads private endpoint connections on storage accounts<br>**Findings:** Storage account with public network access despite having private endpoint, dangling private endpoint connections<br>**Impact if not granted:** Cannot verify private endpoint configuration on storage. |
| `Microsoft.Storage/storageAccounts/queueServices/queues/read` `Microsoft.Storage/storageAccounts/queueServices/read` | **Function:** Enumerates storage queues and reads queue service logging<br>**Findings:** Queue service logging disabled, queue without CMK encryption<br>**Impact if not granted:** Cannot audit queue-level logging. |
| `Microsoft.Storage/storageAccounts/read` | **Function:** Enumerates storage accounts and their properties (SKU, kind, encryption, TLS version, network rules)<br>**Findings:** Public blob access enabled, TLS 1.0/1.1 allowed, HTTPS not enforced, network access unrestricted, missing customer-managed key encryption, insecure default action<br>**Impact if not granted:** Cannot audit storage accounts at all. |
| `Microsoft.Storage/storageAccounts/tableServices/read` `Microsoft.Storage/storageAccounts/tableServices/tables/read` | **Function:** Enumerates storage tables and reads table service logging<br>**Findings:** Table service logging disabled, table without CMK encryption<br>**Impact if not granted:** Cannot audit table-level logging. |

## StorageCache (1)

| Permission | Rationale |
|---|---|
| `Microsoft.StorageCache/caches/read` | **Function:** Reads Azure HPC Cache configuration (high-performance storage caching)<br>**Findings:** HPC Cache without encryption, missing network security, exposed cache endpoints<br>**Impact if not granted:** Cannot audit HPC Cache instances used for HPC workloads. |

## StorageSync (1)

| Permission | Rationale |
|---|---|
| `Microsoft.StorageSync/storageSyncServices/read` | **Function:** Reads Azure File Sync services, sync groups, and registered servers<br>**Findings:** File Sync without cloud tiering security, unregistered sync endpoints, sync group with public network access<br>**Impact if not granted:** Cannot audit hybrid file sync configurations. |

## StreamAnalytics (4)

| Permission | Rationale |
|---|---|
| `Microsoft.StreamAnalytics/streamingjobs/inputs/read` `Microsoft.StreamAnalytics/streamingjobs/outputs/read` `Microsoft.StreamAnalytics/streamingjobs/read` `Microsoft.StreamAnalytics/streamingjobs/transformations/read` | **Function:** Reads Stream Analytics job configuration<br>**Findings:** Stream Analytics job without managed identity, missing CMK on input/output storage, jobs with excessive privileges<br>**Impact if not granted:** Cannot audit stream processing jobs. |

## Web (10)

| Permission | Rationale |
|---|---|
| `Microsoft.Web/hostingEnvironments/read` | **Function:** Reads App Service Environment (ASE) configuration<br>**Findings:** ASE with internal load balancer misconfigured, ASE without WAF, weak inbound network rules<br>**Impact if not granted:** Cannot audit dedicated ASE deployments. |
| `Microsoft.Web/serverFarms/read` | **Function:** Enumerates App Service Plans and reads their SKU and capacity<br>**Findings:** App Service Plan with basic SKU (no autoscale, no staging slots), single-instance plans without HA<br>**Impact if not granted:** Cannot audit App Service Plan configuration. |
| `Microsoft.Web/serverFarms/sites/read` | **Function:** Reads the list of sites within each App Service Plan<br>**Findings:** None directly - relational data.<br>**Impact if not granted:** Cannot correlate apps to their plans. |
| `Microsoft.Web/sites/config/read` | **Function:** Reads Web App / Function App configuration (auth, HTTPS settings, TLS version, remote debugging)<br>**Findings:** HTTPS not enforced, weak minimum TLS, remote debugging enabled, client cert not required, insecure FTP state, weak CORS policy, missing Always On<br>**Impact if not granted:** Cannot audit app-level security settings. |
| `Microsoft.Web/sites/functions/read` | **Function:** Reads Function App function definitions<br>**Findings:** Functions with anonymous auth level, missing function-level auth<br>**Impact if not granted:** Cannot enumerate individual functions within Function Apps. |
| `Microsoft.Web/sites/read` | **Function:** Enumerates Web Apps, Function Apps, and Logic Apps and reads their metadata<br>**Findings:** App with public network access, missing managed identity, using deprecated runtime, missing diagnostic logging<br>**Impact if not granted:** Cannot audit any App Services. |
| `Microsoft.Web/sites/slots/config/read` | **Function:** Reads configuration of App Service deployment slots (staging, production)<br>**Findings:** Slot with different security config than production, slot missing HTTPS enforcement<br>**Impact if not granted:** Cannot audit slot-specific security settings. |
| `Microsoft.Web/sites/slots/read` | **Function:** Enumerates App Service deployment slots<br>**Findings:** Slot without VNet integration, slot with default hostname exposed<br>**Impact if not granted:** Cannot audit slot inventory. |
| `Microsoft.Web/sites/sourceControls/read` | **Function:** Reads source control integration (GitHub, Azure DevOps) on App Services<br>**Findings:** App deploying from untrusted repository, credentials stored in source control config<br>**Impact if not granted:** Cannot audit deployment source security. |
| `Microsoft.Web/sites/virtualNetworkConnections/read` | **Function:** Reads VNet integration configuration on App Services<br>**Findings:** App Service without VNet integration, missing regional VNet integration<br>**Impact if not granted:** Cannot verify apps are integrated with private networks. |

</div>

## Support for retired Azure services

The role deliberately keeps permissions for several Azure services Microsoft has retired for new customers. Many customers still run legacy instances, so retaining these permissions means AccuKnox continues to report the full security posture during migration instead of showing a misleadingly clean scan.

| Retired service | Retirement status | Permission retained | Support this provides |
|---|---|---|---|
| Redis Cache (classic) | Microsoft is migrating customers to Azure Managed Redis. Existing classic Redis instances continue to work. | `Microsoft.Cache/redis/*` | Full scan of TLS enforcement, firewall rules, private endpoint, non-SSL port, diagnostic settings on legacy Redis instances. |
| Azure Spring Cloud | Retired for new customers. Existing Spring Cloud services still operational. | `Microsoft.AppPlatform/*` | Continued audit of Spring app deployments, TLS settings, network access, encryption for existing customers. |
| PostgreSQL Single Server | Retired by Microsoft in March 2025. Customers must migrate to Flexible Server but many have not yet. | `Microsoft.DBforPostgreSQL/servers/read` | Continued audit of SSL enforcement, log_checkpoints, firewall rules, threat detection on legacy PG single-server instances during migration period. |
| MySQL Single Server | Retired by Microsoft. Customers must migrate to MySQL Flexible Server. | `Microsoft.DBforMySQL/servers/read` | Continued audit of SSL enforcement, weak TLS, threat detection, firewall rules on legacy MySQL single-server instances. |
| Azure Front Door (classic) | Microsoft strongly encourages migration to Front Door Standard/Premium. Classic Front Door still operational. | `Microsoft.Network/frontdoors/*` | Continued audit of classic Front Door WAF policies, SSL configuration, custom rules until customers migrate. |

!!! info "Customer value"
    By retaining these permissions, we provide continuous security posture visibility during the customer's migration window from legacy to current-generation Azure services. A competitor scanner that only supports current-generation services will show a clean scan while legacy services remain unaudited. Our scanner reports the full picture, including the legacy services where security incidents are more likely due to reduced Microsoft support.
