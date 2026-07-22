---
title: Azure IAM Permissions Reference
description: The 209 permissions in the AccuKnox CSPM Azure reader role, with the reason and impact for each.
hide:
  - toc
---

# Azure Permissions Reference

AccuKnox's Azure scanner uses the **AK Reader Aligned Role, 209 read-only permissions** on Azure Resource Manager (ARM) resources. It reads configuration to detect misconfigurations, with no write or delete access.

Every permission is listed below, grouped by resource provider. See the [overview](cspm-permissions-overview.md) to compare clouds, or the [Azure prerequisites](cspm-prereq-azure.md) for setup steps.


## Advisor (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Advisor/recommendations/read` | Reads Azure Advisor recommendations across cost, security, reliability, and performance | High-impact Advisor recommendations, cost optimization opportunities, reliability gaps | Cannot surface Azure-native optimization recommendations to the customer. |


## AlertsManagement (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.AlertsManagement/alerts/read` | Reads unified alerts management interface | Alerts management not consolidated, missing smart groups | Cannot audit alerts through the unified alerts API. |


## ApiManagement (4)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.ApiManagement/service/apis/read` | Reads APIs published through API Management | APIs without OAuth/OIDC, missing subscription key requirement, missing rate limiting | Cannot audit APIs exposed through APIM. |
| `Microsoft.ApiManagement/service/backends/read` | Reads backend service definitions in API Management | Backend using HTTP instead of HTTPS, missing certificate validation | Cannot audit APIM backend configurations. |
| `Microsoft.ApiManagement/service/products/read` | Reads API Management product definitions | Products with subscription required disabled, open products exposing sensitive APIs | Cannot audit product-level API grouping. |
| `Microsoft.ApiManagement/service/read` | Enumerates API Management instances | APIM with public access, missing VNet integration, using Consumption tier for critical APIs, weak SSL/TLS | Cannot audit APIM at all. |


## AppConfiguration (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.AppConfiguration/configurationStores/read` | Reads App Configuration store configurations | App Config with public access, missing private endpoint, missing CMK, missing purge protection | Cannot audit App Configuration security. |


## AppPlatform (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.AppPlatform/Spring/read` | Reads Azure Spring Cloud (Spring Apps) service configuration - apps, deployments, TLS settings, config servers  [NOTE] RETIRED - Retained to support existing Spring Cloud customers. | Public network access enabled, missing customer-managed encryption, missing diagnostic logging, weak TLS | Cannot audit Spring Cloud instances deployed before Microsoft retired the offering for new customers. |


## Authorization (4)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Authorization/denyAssignments/read` | Reads deny assignments (explicit denials layered over role assignments) | Missing deny assignments on production resources | Cannot audit denial-based access controls. |
| `Microsoft.Authorization/locks/read` | Reads management locks on subscriptions, resource groups, and individual resources | Resource groups without delete locks, critical resources without CanNotDelete locks, missing ReadOnly locks on shared resources | Cannot detect resources without protection against accidental deletion or modification. |
| `Microsoft.Authorization/roleAssignments/read` | Reads Azure RBAC role assignments (who has what role, at what scope) | Owner role assigned at subscription scope, guest users with elevated roles, service principals with Contributor at root, stale role assignments | Cannot audit privileged access or detect over-permissioned users and service principals. |
| `Microsoft.Authorization/roleDefinitions/read` | Reads Azure RBAC role definitions (built-in and custom roles) | Custom roles with wildcard actions, custom roles duplicating built-in roles, unused custom roles | Cannot audit custom role definitions for excessive permissions. |


## Automation (3)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Automation/automationAccounts/read` | Reads Azure Automation automation account | Runbook with plaintext credentials, variable without encryption, automation account with public access, missing managed identity | Cannot audit automation account security. |
| `Microsoft.Automation/automationAccounts/runbooks/read` | Reads Azure Automation runbooks | Runbook with plaintext credentials, variable without encryption, automation account with public access, missing managed identity | Cannot audit automation account security. |
| `Microsoft.Automation/automationAccounts/variables/read` | Reads Azure Automation variables | Runbook with plaintext credentials, variable without encryption, automation account with public access, missing managed identity | Cannot audit automation account security. |


## Batch (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Batch/batchAccounts/read` | Enumerates Azure Batch accounts used for large-scale parallel workloads | Batch with shared key auth, missing user subscription authentication, no CMK encryption, public network access | Cannot audit Batch account security. |


## Cache (5)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Cache/redis/firewallRules/read` | Reads configuration of Azure Cache for Redis (classic) instances - firewall rules, patch schedules, private endpoint connections, linked servers, TLS version  [NOTE] RETIRED - Microsoft is retiring classic Redis Cache. We retain this permission specifically to continue supporting customers who still run legacy Redis instances that pre-date the retirement announcement. | Weak TLS, missing private endpoint, missing firewall rules, insecure linked server, disabled non-SSL port, missing diagnostic settings | Cannot scan any existing Redis Cache instances. Customers running legacy Redis (from before Microsoft announced retirement) will have zero visibility into misconfigurations. |
| `Microsoft.Cache/redis/linkedServers/read` | Reads configuration of Azure Cache for Redis (classic) instances - firewall rules, patch schedules, private endpoint connections, linked servers, TLS version  [NOTE] RETIRED - Microsoft is retiring classic Redis Cache. We retain this permission specifically to continue supporting customers who still run legacy Redis instances that pre-date the retirement announcement. | Weak TLS, missing private endpoint, missing firewall rules, insecure linked server, disabled non-SSL port, missing diagnostic settings | Cannot scan any existing Redis Cache instances. Customers running legacy Redis (from before Microsoft announced retirement) will have zero visibility into misconfigurations. |
| `Microsoft.Cache/redis/patchSchedules/read` | Reads configuration of Azure Cache for Redis (classic) instances - firewall rules, patch schedules, private endpoint connections, linked servers, TLS version  [NOTE] RETIRED - Microsoft is retiring classic Redis Cache. We retain this permission specifically to continue supporting customers who still run legacy Redis instances that pre-date the retirement announcement. | Weak TLS, missing private endpoint, missing firewall rules, insecure linked server, disabled non-SSL port, missing diagnostic settings | Cannot scan any existing Redis Cache instances. Customers running legacy Redis (from before Microsoft announced retirement) will have zero visibility into misconfigurations. |
| `Microsoft.Cache/redis/privateEndpointConnections/read` | Reads configuration of Azure Cache for Redis (classic) instances - firewall rules, patch schedules, private endpoint connections, linked servers, TLS version  [NOTE] RETIRED - Microsoft is retiring classic Redis Cache. We retain this permission specifically to continue supporting customers who still run legacy Redis instances that pre-date the retirement announcement. | Weak TLS, missing private endpoint, missing firewall rules, insecure linked server, disabled non-SSL port, missing diagnostic settings | Cannot scan any existing Redis Cache instances. Customers running legacy Redis (from before Microsoft announced retirement) will have zero visibility into misconfigurations. |
| `Microsoft.Cache/redis/read` | Reads configuration of Azure Cache for Redis (classic) instances - firewall rules, patch schedules, private endpoint connections, linked servers, TLS version  [NOTE] RETIRED - Microsoft is retiring classic Redis Cache. We retain this permission specifically to continue supporting customers who still run legacy Redis instances that pre-date the retirement announcement. | Weak TLS, missing private endpoint, missing firewall rules, insecure linked server, disabled non-SSL port, missing diagnostic settings | Cannot scan any existing Redis Cache instances. Customers running legacy Redis (from before Microsoft announced retirement) will have zero visibility into misconfigurations. |


## CognitiveServices (3)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.CognitiveServices/accounts/deployments/read` | Reads Cognitive Services / Azure OpenAI model deployments configuration | Account with public access, missing private endpoint, disabled local auth not enforced, missing CMK, missing diagnostic logging, weak network ACLs | Cannot audit AI service security. |
| `Microsoft.CognitiveServices/accounts/models/read` | Reads Cognitive Services / Azure OpenAI models configuration | Account with public access, missing private endpoint, disabled local auth not enforced, missing CMK, missing diagnostic logging, weak network ACLs | Cannot audit AI service security. |
| `Microsoft.CognitiveServices/accounts/read` | Reads Cognitive Services / Azure OpenAI account configuration | Account with public access, missing private endpoint, disabled local auth not enforced, missing CMK, missing diagnostic logging, weak network ACLs | Cannot audit AI service security. |


## Compute (17)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Compute/availabilitySets/read` | Reads VM availability sets used for HA within a single datacenter | VMs not placed in availability sets, availability set with insufficient fault domains | Cannot audit HA deployments. |
| `Microsoft.Compute/diskAccesses/read` | Reads disk access resources (private endpoint configurations for managed disks) | Disk with public network access when private endpoint is available, misconfigured disk access resource | Cannot verify private link is configured for disk imports/exports. |
| `Microsoft.Compute/diskEncryptionSets/read` | Reads disk encryption sets used to hold customer-managed keys for disk encryption | Disk encryption set using system-assigned identity, key rotation not configured, encryption at host not enabled | Cannot verify CMK-based disk encryption. |
| `Microsoft.Compute/disks/read` | Enumerates managed disks and reads their encryption, size, and attachment state | Unencrypted managed disks, disks without customer-managed keys, orphaned disks, disks with public network access | Cannot audit disk-level security. |
| `Microsoft.Compute/galleries/read` | Reads Compute Image Galleries used for shared VM images | Image gallery without CMK encryption, publicly accessible image versions, missing image replication | Cannot audit image gallery configuration. |
| `Microsoft.Compute/locations/vmSizes/read` | Reads catalog of available VM SKUs and sizes by region | None directly - reference data used by other checks. | Reduces accuracy of "VM using deprecated SKU" checks. |
| `Microsoft.Compute/skus/read` | Reads catalog of available VM SKUs and sizes by region | None directly - reference data used by other checks. | Reduces accuracy of "VM using deprecated SKU" checks. |
| `Microsoft.Compute/snapshots/read` | Enumerates managed disk snapshots and their encryption state | Unencrypted snapshots, snapshots with public access, stale snapshots | Cannot audit snapshot security. |
| `Microsoft.Compute/sshPublicKeys/read` | Reads SSH public keys stored as Azure resources | SSH keys without tags, SSH keys without associated resources | Cannot audit SSH key inventory. |
| `Microsoft.Compute/virtualMachineScaleSets/extensions/read` | Reads extensions on VMSS resources (security agents, monitoring) | VMSS without Log Analytics extension, VMSS without anti-malware, VMSS without dependency agent | Cannot detect missing security agents on scale set instances. |
| `Microsoft.Compute/virtualMachineScaleSets/instanceView/read` | Reads runtime status of VMSS scale set instances | VMSS instances failed, instances pending upgrade | Cannot detect unhealthy or misconfigured VMSS instances. |
| `Microsoft.Compute/virtualMachineScaleSets/read` | Enumerates Virtual Machine Scale Sets and their configuration (SKU, capacity, upgrade policy) | VMSS without managed identity, VMSS with password auth, VMSS without automatic OS upgrade, VMSS using outdated image | Cannot audit scale sets used for AKS node pools, application workloads. |
| `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/instanceView/read` | Reads runtime state of VMs (power state, agent status, patch status) | VM in stopped state, agent not ready, pending reboot after patches | Cannot detect VMs in unhealthy states or with agent problems. |
| `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/read` | Reads individual VM instances within a Virtual Machine Scale Set | VMSS instances out of sync, unhealthy instances, unpatched instances | Cannot audit VMSS instances at the VM level. |
| `Microsoft.Compute/virtualMachines/extensions/read` | Reads VM extensions installed on virtual machines (Log Analytics agent, anti-malware, Azure Backup, custom scripts) | Log Analytics agent missing, anti-malware not installed, Azure Backup extension missing, disk encryption extension absent, dependency agent missing | Cannot detect missing security agents on VMs. |
| `Microsoft.Compute/virtualMachines/instanceView/read` | Reads runtime state of VMs (power state, agent status, patch status) | VM in stopped state, agent not ready, pending reboot after patches | Cannot detect VMs in unhealthy states or with agent problems. |
| `Microsoft.Compute/virtualMachines/read` | Enumerates virtual machines and reads their configuration (OS, SKU, network profile, identity) | VMs without managed identity, VMs with password authentication, VMs without accelerated networking, unpatched OS versions, VMs on legacy SKUs | Cannot audit any virtual machines. |


## Consumption (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Consumption/usageDetails/read` | Reads billing and cost management data | Cost anomalies flagged by Advisor, unusual spending patterns | Cannot correlate cost anomalies with security posture. |


## ContainerInstance (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.ContainerInstance/containerGroups/read` | Reads Azure Container Instances (ACI) - serverless containers | ACI without private VNet integration, ACI with public IP, ACI using latest tag, ACI with excessive resource allocation | Cannot audit ACI deployments. |


## ContainerRegistry (3)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.ContainerRegistry/registries/read` | Reads Azure Container Registry registry configuration | Registry with public access, admin user enabled, missing content trust, missing quarantine policy, missing image scanning | Cannot audit container image registries. |
| `Microsoft.ContainerRegistry/registries/replications/read` | Reads Azure Container Registry registry replications configuration | Registry with public access, admin user enabled, missing content trust, missing quarantine policy, missing image scanning | Cannot audit container image registries. |
| `Microsoft.ContainerRegistry/registries/webhooks/read` | Reads Azure Container Registry registry webhooks configuration | Registry with public access, admin user enabled, missing content trust, missing quarantine policy, missing image scanning | Cannot audit container image registries. |


## ContainerService (4)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.ContainerService/locations/orchestrators/read` | Reads available Kubernetes orchestrator versions per region | None directly - reference data. | Reduced accuracy of version-currency checks. |
| `Microsoft.ContainerService/managedClusters/agentPools/read` | Reads AKS node pool configuration | Node pool without auto-upgrade, spot instances without eviction handling, node pool without private network, insufficient max pods | Cannot audit AKS node pools. |
| `Microsoft.ContainerService/managedClusters/read` | Enumerates AKS clusters and reads their configuration (Kubernetes version, network profile, identity, RBAC settings) | AKS with kubenet instead of Azure CNI, missing private cluster, RBAC disabled, missing Entra ID integration, insecure API server, network policy not enforced, missing pod security policies | Cannot audit any AKS clusters. |
| `Microsoft.ContainerService/managedClusters/upgradeProfiles/read` | Reads available Kubernetes version upgrades for AKS clusters | AKS running deprecated K8s version, cluster more than 2 minor versions behind current | Cannot detect clusters running outdated Kubernetes versions. |


## DBforMySQL (3)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.DBforMySQL/flexibleServers/configurations/read` | Reads MySQL Flexible Server server parameters (my.cnf) | Server with public access, SSL disabled, weak firewall rules, missing binlog configuration, insecure server parameters | Cannot audit MySQL Flex configurations. |
| `Microsoft.DBforMySQL/flexibleServers/firewallRules/read` | Reads MySQL Flexible Server firewall rules | Server with public access, SSL disabled, weak firewall rules, missing binlog configuration, insecure server parameters | Cannot audit MySQL Flex configurations. |
| `Microsoft.DBforMySQL/flexibleServers/read` | Reads MySQL Flexible Server server | Server with public access, SSL disabled, weak firewall rules, missing binlog configuration, insecure server parameters | Cannot audit MySQL Flex configurations. |


## DBforPostgreSQL (3)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.DBforPostgreSQL/flexibleServers/configurations/read` | Reads PostgreSQL Flexible Server server parameters (postgresql.conf) | Server with public access, SSL enforcement disabled, weak firewall rules, missing Entra ID auth, insecure server parameters (log_statement, log_connections), missing backup configuration | Cannot audit PostgreSQL Flex configurations. |
| `Microsoft.DBforPostgreSQL/flexibleServers/firewallRules/read` | Reads PostgreSQL Flexible Server firewall rules | Server with public access, SSL enforcement disabled, weak firewall rules, missing Entra ID auth, insecure server parameters (log_statement, log_connections), missing backup configuration | Cannot audit PostgreSQL Flex configurations. |
| `Microsoft.DBforPostgreSQL/flexibleServers/read` | Reads PostgreSQL Flexible Server server | Server with public access, SSL enforcement disabled, weak firewall rules, missing Entra ID auth, insecure server parameters (log_statement, log_connections), missing backup configuration | Cannot audit PostgreSQL Flex configurations. |


## DataFactory (6)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.DataFactory/factories/datasets/read` | Reads Azure Data Factory + datasets + pipelines configuration | ADF without managed identity, missing customer-managed key, linked services with plaintext credentials, pipeline exposed to public network | Cannot audit data pipeline security. |
| `Microsoft.DataFactory/factories/linkedservices/read` | Reads Azure Data Factory + datasets + pipelines configuration | ADF without managed identity, missing customer-managed key, linked services with plaintext credentials, pipeline exposed to public network | Cannot audit data pipeline security. |
| `Microsoft.DataFactory/factories/pipelines/read` | Reads Azure Data Factory + datasets + pipelines configuration | ADF without managed identity, missing customer-managed key, linked services with plaintext credentials, pipeline exposed to public network | Cannot audit data pipeline security. |
| `Microsoft.DataFactory/factories/privateEndpointConnections/read` | Reads Azure Data Factory + datasets + pipelines configuration | ADF without managed identity, missing customer-managed key, linked services with plaintext credentials, pipeline exposed to public network | Cannot audit data pipeline security. |
| `Microsoft.DataFactory/factories/read` | Reads Azure Data Factory + datasets + pipelines configuration | ADF without managed identity, missing customer-managed key, linked services with plaintext credentials, pipeline exposed to public network | Cannot audit data pipeline security. |
| `Microsoft.DataFactory/factories/triggers/read` | Reads Azure Data Factory + datasets + pipelines configuration | ADF without managed identity, missing customer-managed key, linked services with plaintext credentials, pipeline exposed to public network | Cannot audit data pipeline security. |


## Databricks (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Databricks/workspaces/read` | Enumerates Azure Databricks workspaces | Databricks with public IP, missing VNet injection, missing customer-managed key, missing private link | Cannot audit Databricks workspaces. |


## Devices (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Devices/IotHubs/read` | Reads Azure IoT Hub configuration | IoT Hub with public access, weak SAS policies, missing device authentication policies, weak encryption | Cannot audit IoT Hub security. |


## EventGrid (2)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.EventGrid/domains/read` | Reads Event Grid domain configuration (custom topics grouped as domains) | Domain with public network access, missing private endpoint, weak input schema, missing CMK | Cannot audit Event Grid domain security. |
| `Microsoft.EventGrid/topics/read` | Reads Event Grid topic configuration | Topic with public access, missing IP firewall, missing managed identity for delivery | Cannot audit Event Grid topic security. |


## EventHub (4)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.EventHub/namespaces/authorizationRules/read` | Reads shared access authorization rules on Event Hub namespaces | SAS keys with Manage rights, root SAS keys still active, missing key rotation | Cannot audit Event Hub access keys. |
| `Microsoft.EventHub/namespaces/eventhubs/read` | Reads individual Event Hubs within namespaces | Event Hub with excessive retention, missing capture configuration | Cannot audit individual event hubs. |
| `Microsoft.EventHub/namespaces/networkRuleSets/read` | Reads network rules (IP and VNet) on Event Hub namespaces | Event Hub with default action Allow, missing VNet rules, wide-open IP filter | Cannot audit network-level Event Hub access controls. |
| `Microsoft.EventHub/namespaces/read` | Enumerates Event Hub namespaces | Event Hub with public access, missing private endpoint, weak minimum TLS | Cannot audit Event Hub namespaces. |


## GuestConfiguration (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.GuestConfiguration/guestConfigurationAssignments/read` | Reads guest configuration assignments (in-guest policy on VMs) | VMs without guest configuration extension, non-compliant OS baselines, missing password policies, missing audit policies | Cannot audit VM in-guest OS-level policy compliance. Defender for Servers loses visibility. |


## Insights (6)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Insights/actionGroups/read` | Reads action group configurations (who gets notified when alerts fire) | Alert rules without action groups, action groups without recipients, action groups with SMS-only notification | Cannot verify alert notifications are configured. |
| `Microsoft.Insights/activityLogAlerts/read` | Reads activity log alert rules (alerts triggered by control-plane events) | Missing alert for NSG changes, missing alert for role assignment changes, missing alert for Key Vault operations, missing alert for firewall rule changes | Cannot verify alerts exist for security-relevant events. |
| `Microsoft.Insights/autoscalesettings/read` | Reads autoscale rules on VM Scale Sets, App Service Plans | Missing autoscale on production workloads, autoscale limits too low/high, single-instance production deployments | Cannot audit autoscale configurations. |
| `Microsoft.Insights/components/read` | Reads Application Insights instances | App Insights without workspace mode, missing sampling policies, missing CMK encryption | Cannot audit App Insights deployment. |
| `Microsoft.Insights/metricAlerts/read` | Reads metric-based alert rules | Missing CPU alerts, missing network transfer alerts, missing failed sign-in alerts | Cannot audit performance and security metric alerts. |
| `Microsoft.Insights/metrics/read` | Reads Azure Monitor metric definitions | None directly - metric data. | Cannot query resource metrics for alerting rules. |


## KeyVault (7)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.KeyVault/checkNameAvailability/read` | Reads Key Vault service-level metadata (name availability, operation results, locations) | None directly - service catalog data. | Reduced fidelity of Key Vault enumeration. |
| `Microsoft.KeyVault/locations/deletedVaults/read` | Reads Key Vault service-level metadata (name availability, operation results, locations) | None directly - service catalog data. | Reduced fidelity of Key Vault enumeration. |
| `Microsoft.KeyVault/locations/operationResults/read` | Reads Key Vault service-level metadata (name availability, operation results, locations) | None directly - service catalog data. | Reduced fidelity of Key Vault enumeration. |
| `Microsoft.KeyVault/operations/read` | Reads Key Vault service-level metadata (name availability, operation results, locations) | None directly - service catalog data. | Reduced fidelity of Key Vault enumeration. |
| `Microsoft.KeyVault/vaults/keys/read` | Enumerates keys stored in Key Vaults and reads their metadata | Keys without expiration date, keys older than rotation policy, keys without automatic rotation, weak key sizes | Cannot audit encryption key rotation and lifecycle. |
| `Microsoft.KeyVault/vaults/read` | Enumerates Key Vaults and reads their SKU, access policies, and network ACLs | Key Vault with public network access, missing purge protection, soft-delete disabled, missing private endpoint, RBAC not enabled, access policies with wildcard permissions | Cannot audit Key Vaults - one of the most sensitive Azure resources. |
| `Microsoft.KeyVault/vaults/secrets/read` | Enumerates secrets stored in Key Vaults (metadata only, not values) | Secrets without expiration, disabled secrets not cleaned up, secrets past expiration still in use | Cannot audit secret lifecycle. |


## Kusto (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Kusto/clusters/read` | Reads Azure Data Explorer (Kusto) cluster configuration | Kusto cluster with public access, missing private endpoint, missing CMK, weak network configuration | Cannot audit ADX cluster security. |


## MachineLearningServices (2)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.MachineLearningServices/workspaces/computes/read` | Reads Azure Machine Learning compute clusters and instances configuration | ML workspace with public access, missing HBI (High Business Impact) flag, missing CMK, compute with public IP, missing SSH restriction, missing diagnostic logging | Cannot audit ML workspace security. |
| `Microsoft.MachineLearningServices/workspaces/read` | Reads Azure Machine Learning workspace configuration | ML workspace with public access, missing HBI (High Business Impact) flag, missing CMK, compute with public IP, missing SSH restriction, missing diagnostic logging | Cannot audit ML workspace security. |


## Maintenance (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Maintenance/maintenanceConfigurations/read` | Reads maintenance configurations (planned patching windows) | VMs without maintenance configuration, patch orchestration missing | Cannot audit maintenance scheduling. |


## ManagedServices (2)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.ManagedServices/registrationAssignments/read` | Reads Azure Lighthouse delegated resource management assignments | Excessive Lighthouse delegations, missing tenant boundaries | Cannot audit cross-tenant management relationships. |
| `Microsoft.ManagedServices/registrationDefinitions/read` | Reads Azure Lighthouse delegated resource management assignments | Excessive Lighthouse delegations, missing tenant boundaries | Cannot audit cross-tenant management relationships. |


## Network (37)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Network/applicationGatewayWebApplicationFirewallPolicies/read` | Reads WAF policies attached to Application Gateways | WAF in Detection mode instead of Prevention, missing OWASP rule set, WAF policy without custom rules for known threats | Cannot audit WAF rule configurations. |
| `Microsoft.Network/applicationGateways/read` | Reads Application Gateway configuration (listeners, SSL, WAF) | App Gateway without WAF, weak SSL policy, missing HTTP to HTTPS redirect, self-signed certificates | Cannot audit L7 load balancer security. |
| `Microsoft.Network/applicationSecurityGroups/read` | Reads Network applicationSecurityGroups configuration | Depends on the specific plugin using this permission. | Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/azureFirewalls/read` | Reads Azure Firewall and firewall policy configuration | Firewall in Alert-only mode, missing IDPS, threat intel not enabled, permissive application rules | Cannot audit Azure-native firewall rules. |
| `Microsoft.Network/bastionHosts/read` | Reads Azure Bastion hosts | Bastion with Basic SKU (weaker features), Bastion without native client support, missing shareable link controls | Cannot audit Bastion configuration for secure jump access. |
| `Microsoft.Network/dnszones/read` | Reads public and private DNS zones | DNS zone without DNSSEC, private DNS not linked to VNet, dangling DNS records | Cannot audit DNS configuration. |
| `Microsoft.Network/expressRouteCircuits/read` | Reads ExpressRoute circuit configurations for private hybrid connectivity | ExpressRoute without BGP MD5 authentication, missing FastPath, weak peering configuration | Cannot audit ExpressRoute security posture. |
| `Microsoft.Network/loadBalancers/backendAddressPools/read` | Reads load balancer backend address pools configuration | LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services | Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/frontendIPConfigurations/read` | Reads load balancer frontend IP configurations configuration | LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services | Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/inboundNatRules/read` | Reads load balancer inbound NAT rules configuration | LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services | Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/loadBalancingRules/read` | Reads load balancer rules configuration | LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services | Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/outboundRules/read` | Reads load balancer outbound rules configuration | LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services | Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/probes/read` | Reads load balancer health probes configuration | LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services | Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/loadBalancers/read` | Reads load balancer configuration | LB with public IP where private would suffice, missing health probes, insecure LB rules exposing internal services | Cannot audit load balancer routing and health checks. |
| `Microsoft.Network/locations/serviceTags/read` | Reads Azure service tag definitions used for NSG rule reasoning | None directly - reference data. | NSG rule analysis cannot distinguish "AzureFrontDoor.Backend" from a generic Internet range. |
| `Microsoft.Network/locations/usages/read` | Reads Network locations usages configuration | Depends on the specific plugin using this permission. | Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/natGateways/read` | Reads NAT Gateway configuration for outbound connectivity | Subnets without NAT Gateway using default outbound (deprecated), missing NAT for private endpoints | Cannot audit NAT Gateway assignments. |
| `Microsoft.Network/networkInterfaces/ipConfigurations/read` | Reads Network networkInterfaces ipConfigurations configuration | Depends on the specific plugin using this permission. | Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/networkInterfaces/read` | Reads network interfaces attached to VMs | NIC with IP forwarding enabled, NIC without NSG association, NIC with accelerated networking disabled | Cannot correlate VMs to their networking configuration. |
| `Microsoft.Network/networkProfiles/read` | Reads network profiles used by Container Instances | Container instance in public subnet, ACI without private subnet integration | Cannot audit ACI network configurations. |
| `Microsoft.Network/networkSecurityGroups/defaultSecurityRules/read` | Reads default (built-in) NSG rules that Azure provides automatically | None directly - reference data used to distinguish default vs custom rules. | Reduced context when analyzing effective NSG posture. |
| `Microsoft.Network/networkSecurityGroups/read` | Enumerates NSGs and their associated subnets and network interfaces | Subnets without NSG association, NSG with all rules permissive, orphaned NSGs, NSG missing on public-facing subnet | Cannot audit network security groups at all. |
| `Microsoft.Network/networkSecurityGroups/securityRules/read` | Reads custom inbound and outbound security rules defined on Network Security Groups | Wide-open inbound rules (0.0.0.0/0), SSH/RDP open to Internet, database ports exposed publicly, permissive outbound rules | Cannot audit NSG rule configurations - a critical network security control. |
| `Microsoft.Network/networkWatchers/flowLogs/read` | Reads NSG flow log configuration | NSG without flow logs enabled, flow logs without traffic analytics, insufficient flow log retention | Cannot verify network traffic is being logged. |
| `Microsoft.Network/networkWatchers/read` | Reads Network Watcher services per region | Network Watcher not enabled in region | Cannot verify Network Watcher is enabled for troubleshooting and flow logs. |
| `Microsoft.Network/privateDnsZones/read` | Reads public and private DNS zones | DNS zone without DNSSEC, private DNS not linked to VNet, dangling DNS records | Cannot audit DNS configuration. |
| `Microsoft.Network/privateDnsZones/virtualNetworkLinks/read` | Reads public and private DNS zones | DNS zone without DNSSEC, private DNS not linked to VNet, dangling DNS records | Cannot audit DNS configuration. |
| `Microsoft.Network/privateEndpoints/read` | Reads Network privateEndpoints configuration | Depends on the specific plugin using this permission. | Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/publicIPAddresses/read` | Enumerates public IP addresses and their associations | Orphaned public IPs, public IPs on non-production resources, basic SKU public IPs (deprecated), public IPs without DDoS protection | Cannot audit externally exposed IP addresses. |
| `Microsoft.Network/routeTables/read` | Reads user-defined routes (UDRs) and route tables | Missing default route to firewall/NVA, UDR bypassing security appliances | Cannot audit custom routing. |
| `Microsoft.Network/routeTables/routes/read` | Reads Network routeTables routes configuration | Depends on the specific plugin using this permission. | Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Network/virtualNetworkGateways/read` | Reads VPN and ExpressRoute gateways for hybrid connectivity | Gateway using weak SKU, missing active-active configuration, weak IPsec policy | Cannot audit hybrid network gateways. |
| `Microsoft.Network/virtualNetworks/read` | Enumerates virtual networks and reads their address space and configuration | VNets without DDoS protection, VNets with overlapping ranges, VNets without flow logs | Cannot audit VNet topology. |
| `Microsoft.Network/virtualNetworks/subnets/read` | Reads subnets within virtual networks (address range, delegation, service endpoints, private endpoint policy) | Subnet without NSG, subnet without service endpoints, subnet allowing multiple delegations, subnet with overly permissive private endpoint policy | Cannot audit subnet-level segmentation. |
| `Microsoft.Network/virtualNetworks/subnets/resourceNavigationLinks/read` | Reads links between subnets and the resources that use them | None directly - dependency data for other checks. | Cannot trace subnet-to-resource associations. |
| `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/read` | Reads links between subnets and the resources that use them | None directly - dependency data for other checks. | Cannot trace subnet-to-resource associations. |
| `Microsoft.Network/virtualNetworks/virtualNetworkPeerings/read` | Reads VNet peering configurations between virtual networks | Peering without gateway transit control, peering allowing forwarded traffic, unauthorized cross-tenant peerings | Cannot audit cross-VNet connectivity. |


## OperationalInsights (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.OperationalInsights/workspaces/read` | Reads Log Analytics workspace configuration | Missing Log Analytics workspace, workspace with default retention (too short), missing security solutions installed, workspace not linked to Defender | Cannot verify Log Analytics is receiving logs. Breaks 30+ Defender and monitor checks. |


## RecoveryServices (3)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.RecoveryServices/vaults/backupPolicies/read` | Reads backup policies configured in Recovery Services vaults | Backup retention below policy minimum, missing weekly backups, missing yearly backups for compliance | Cannot audit backup retention and frequency. |
| `Microsoft.RecoveryServices/vaults/backupProtectedItems/read` | Reads items protected by Azure Backup (VMs, SQL DBs, file shares) | Critical VMs without backup, databases without backup, backup jobs failing repeatedly | Cannot verify what is actually being backed up. |
| `Microsoft.RecoveryServices/vaults/read` | Enumerates Recovery Services vaults | Vault with soft delete disabled, missing immutability, missing CMK, missing private endpoint, cross-subscription restore disabled | Cannot audit backup vault security. |


## ResourceGraph (4)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.ResourceGraph/operations/read` | Enables cross-scope resource querying via Azure Resource Graph | None directly - foundational for Defender inventory. | Defender for Cloud cannot enumerate resources across management scopes. |
| `Microsoft.ResourceGraph/resourceChanges/read` | Enables cross-scope resource querying via Azure Resource Graph | None directly - foundational for Defender inventory. | Defender for Cloud cannot enumerate resources across management scopes. |
| `Microsoft.ResourceGraph/resources/read` | Enables cross-scope resource querying via Azure Resource Graph | None directly - foundational for Defender inventory. | Defender for Cloud cannot enumerate resources across management scopes. |
| `Microsoft.ResourceGraph/resourcesHistory/read` | Enables cross-scope resource querying via Azure Resource Graph | None directly - foundational for Defender inventory. | Defender for Cloud cannot enumerate resources across management scopes. |


## Resources (9)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Resources/deployments/read` | Reads ARM deployment history for the subscription | Failed deployments retained, sensitive parameters in deployment history | Cannot audit ARM template usage or deployment metadata. |
| `Microsoft.Resources/links/read` | Reads resource links (cross-resource dependencies) | Undocumented cross-resource dependencies | Cannot map dependencies between related resources. |
| `Microsoft.Resources/providers/read` | Reads the list of registered Azure resource providers | Deprecated providers still registered, security-relevant providers not registered | Cannot verify which Azure services are enabled in the subscription. |
| `Microsoft.Resources/resources/read` | Enumerates all Azure resources across the subscription regardless of resource group | Orphaned resources, resources without tags, resources missing required governance metadata | Scanner cannot build a complete resource inventory. |
| `Microsoft.Resources/subscriptions/locations/read` | Reads the list of Azure regions available to the subscription | None - reference data used by region-scoped scans. | Scanner cannot iterate through regions correctly. |
| `Microsoft.Resources/subscriptions/read` | Enumerates the Azure subscription and its metadata (tenant ID, tags, state, quota) | None - this is foundational. Without it, no findings can be produced. | Scanner cannot see the subscription at all. Total scan blackout. |
| `Microsoft.Resources/subscriptions/resourceGroups/read` | Enumerates resource groups within the subscription | Resource groups without tags, resource groups without management locks, empty resource groups | Scanner cannot enumerate resources organized by resource group. |
| `Microsoft.Resources/subscriptions/resources/read` | Enumerates all Azure resources across the subscription regardless of resource group | Orphaned resources, resources without tags, resources missing required governance metadata | Scanner cannot build a complete resource inventory. |
| `Microsoft.Resources/tenants/read` | Reads Entra tenant metadata visible to the subscription | None - reference data. | Cannot correlate subscription with its parent tenant. |


## Search (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Search/searchServices/read` | Reads Azure Cognitive Search services | Search with public access, missing private endpoint, admin keys not rotated, missing CMK encryption | Cannot audit search service configuration. |


## ServiceBus (5)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.ServiceBus/namespaces/authorizationRules/read` | Reads Service Bus authorization rules configuration | SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled | Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/privateEndpointConnections/read` | Reads Service Bus private endpoints configuration | SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled | Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/queues/read` | Reads Service Bus queues configuration | SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled | Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/read` | Reads Service Bus namespace configuration | SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled | Cannot audit Service Bus messaging security. |
| `Microsoft.ServiceBus/namespaces/topics/read` | Reads Service Bus topics configuration | SB namespace with public access, missing private endpoint, permissive SAS keys, wildcard IP filter, missing local auth disabled | Cannot audit Service Bus messaging security. |


## SignalRService (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.SignalRService/SignalR/read` | Reads Azure SignalR Service configuration for real-time messaging | SignalR with public access, missing private endpoint, weak feature flags | Cannot audit SignalR security. |


## Sql (28)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Sql/managedInstances/read` | Reads Sql managedInstances configuration | Depends on the specific plugin using this permission. | Loss of visibility into this specific resource type or sub-resource. |
| `Microsoft.Sql/servers/administrators/read` | Reads SQL server Entra ID administrator configuration | SQL server without Entra ID admin, SQL admin is a user instead of a group | Cannot verify Entra ID authentication is enforced. |
| `Microsoft.Sql/servers/advancedThreatProtectionSettings/read` | Reads Advanced Threat Protection and security alert policies on SQL servers | ATP disabled, alert emails not configured, security alerts not sent to admins | Cannot verify SQL ATP is configured. |
| `Microsoft.Sql/servers/auditingSettings/read` | Reads server-level SQL auditing configuration | Server auditing disabled, audit log destination missing, insufficient retention | Cannot verify SQL server auditing. |
| `Microsoft.Sql/servers/connectionPolicies/read` | Reads SQL server connection policy (Default vs Proxy vs Redirect) | Connection policy set to Proxy where Redirect would be more secure | Cannot audit connection routing. |
| `Microsoft.Sql/servers/databases/auditingSettings/read` | Reads SQL database auditing configuration | Database auditing disabled, audit log retention too short, audit not sent to Log Analytics/storage | Cannot verify database auditing is enabled. |
| `Microsoft.Sql/servers/databases/automaticTuning/read` | Reads automatic tuning settings on SQL databases | Automatic tuning disabled, force plan not enabled | Cannot verify performance tuning configuration. |
| `Microsoft.Sql/servers/databases/backupShortTermRetentionPolicies/read` | Reads short-term backup retention policy on SQL databases | Backup retention below regulatory minimum, missing PITR configuration | Cannot audit backup retention. |
| `Microsoft.Sql/servers/databases/currentSensitivityLabels/read` | Reads sensitivity labels (data classification) on SQL database columns | Sensitive columns unclassified, missing PII classification, no confidentiality labels | Cannot verify data classification. |
| `Microsoft.Sql/servers/databases/dataMaskingPolicies/read` | Reads dynamic data masking rules on SQL databases | No data masking on PII columns, data masking disabled | Cannot audit data masking for sensitive columns. |
| `Microsoft.Sql/servers/databases/ledgerDigestUploads/read` | Reads Ledger digest upload configuration (SQL Ledger tamper evidence) | Ledger enabled without digest uploads, missing digest storage | Cannot audit Ledger tamper-evidence configuration. |
| `Microsoft.Sql/servers/databases/read` | Enumerates SQL databases within SQL servers | Databases without TDE, databases in wrong SKU, deprecated compatibility levels, databases without backup configuration | Cannot audit any SQL databases. |
| `Microsoft.Sql/servers/databases/sensitivityLabels/read` | Reads sensitivity labels (data classification) on SQL database columns | Sensitive columns unclassified, missing PII classification, no confidentiality labels | Cannot verify data classification. |
| `Microsoft.Sql/servers/databases/syncGroups/read` | Reads SQL Data Sync group configuration | Sync group without conflict resolution policy | Cannot audit database sync configurations. |
| `Microsoft.Sql/servers/databases/transparentDataEncryption/read` | Reads Transparent Data Encryption (TDE) status on SQL databases | TDE disabled, TDE using service-managed key instead of customer-managed key | Cannot verify at-rest encryption is enabled. |
| `Microsoft.Sql/servers/databases/vulnerabilityAssessments/read` | Reads SQL database vulnerability assessment configuration and scan results | Vulnerability assessment not configured, missing storage for scan results, unresolved high-severity findings | Cannot verify vulnerability scanning is configured. |
| `Microsoft.Sql/servers/databases/vulnerabilityAssessments/scans/read` | Reads SQL database vulnerability assessment configuration and scan results | Vulnerability assessment not configured, missing storage for scan results, unresolved high-severity findings | Cannot verify vulnerability scanning is configured. |
| `Microsoft.Sql/servers/devOpsAuditingSettings/read` | Reads DevOps auditing settings on SQL servers | DevOps auditing not enabled | Cannot audit DDL change tracking. |
| `Microsoft.Sql/servers/elasticPools/read` | Reads SQL elastic pool configuration | Elastic pool overprovisioned, elastic pool with wrong SKU, single-database configuration where elastic pool would be more efficient | Cannot audit elastic pool utilization. |
| `Microsoft.Sql/servers/encryptionProtector/read` | Reads encryption protector (CMK) configuration on SQL servers | SQL server using service-managed key instead of CMK, encryption protector not rotated | Cannot verify SQL uses customer-managed keys. |
| `Microsoft.Sql/servers/failoverGroups/read` | Reads SQL failover group configuration for HA/DR | Missing failover group, secondary in same region as primary, manual failover configured for critical DB | Cannot audit HA/DR posture. |
| `Microsoft.Sql/servers/firewallRules/read` | Reads SQL server firewall rules | Firewall rule allowing 0.0.0.0-255.255.255.255, permissive Azure services rule, missing IP restriction | Cannot detect wide-open SQL exposure. |
| `Microsoft.Sql/servers/outboundFirewallRules/read` | Reads SQL server firewall rules | Firewall rule allowing 0.0.0.0-255.255.255.255, permissive Azure services rule, missing IP restriction | Cannot detect wide-open SQL exposure. |
| `Microsoft.Sql/servers/read` | Enumerates SQL servers and reads their configuration | SQL server with public network access, missing minimum TLS version, missing Entra ID admin, weak firewall rules | Cannot audit any SQL servers. |
| `Microsoft.Sql/servers/restorableDroppedDatabases/read` | Reads databases marked for deletion but still recoverable | Excessive number of dropped databases retained, dropped databases containing sensitive data | Cannot audit dropped-database retention. |
| `Microsoft.Sql/servers/securityAlertPolicies/read` | Reads Advanced Threat Protection and security alert policies on SQL servers | ATP disabled, alert emails not configured, security alerts not sent to admins | Cannot verify SQL ATP is configured. |
| `Microsoft.Sql/servers/virtualNetworkRules/read` | Reads VNet rules on SQL servers (private access through subnets) | SQL server without VNet rules, VNet rules missing ignore-missing-endpoint flag | Cannot verify network-level SQL access controls. |
| `Microsoft.Sql/servers/vulnerabilityAssessments/read` | Reads server-level vulnerability assessment configuration | Server-level VA not configured, VA storage account missing | Cannot verify VA is set up at server scope. |


## Storage (14)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Storage/storageAccounts/blobServices/containers/immutabilityPolicies/read` | Reads WORM (Write Once Read Many) immutability policies on blob containers | Container without immutability policy where required, unlocked immutability policies, insufficient retention period | Cannot verify compliance requirements for immutable data (financial records, healthcare). |
| `Microsoft.Storage/storageAccounts/blobServices/containers/read` | Enumerates blob containers within storage accounts and reads their access level | Anonymous public read access, publicly accessible container, missing CMK encryption on container, missing immutability policy | Cannot detect publicly accessible blob containers - a top source of data breaches. |
| `Microsoft.Storage/storageAccounts/blobServices/read` | Reads blob service properties (versioning, soft delete, change feed, encryption) | Blob soft delete disabled, versioning disabled, missing change feed, insufficient retention | Cannot verify blob-level data protection controls. |
| `Microsoft.Storage/storageAccounts/encryptionScopes/read` | Reads encryption scope configurations on storage accounts | Encryption scope using Microsoft-managed key instead of CMK, infrastructure encryption disabled | Cannot verify granular encryption scope settings. |
| `Microsoft.Storage/storageAccounts/fileServices/read` | Enumerates Azure File shares and reads share-level access settings | File share with public access, missing SMB security settings, insecure share permissions | Cannot audit file share exposure. |
| `Microsoft.Storage/storageAccounts/fileServices/shares/read` | Enumerates Azure File shares and reads share-level access settings | File share with public access, missing SMB security settings, insecure share permissions | Cannot audit file share exposure. |
| `Microsoft.Storage/storageAccounts/localUsers/read` | Reads local users configured on storage accounts (SFTP feature) | SFTP enabled without home directory, SSH key auth disabled, weak permission scope | Cannot audit SFTP user access on storage accounts. |
| `Microsoft.Storage/storageAccounts/managementPolicies/read` | Reads lifecycle management policies on storage accounts | Missing lifecycle policy, no tier-down policy for cold data, missing automatic deletion for expired blobs | Cannot audit blob tiering and deletion policies. |
| `Microsoft.Storage/storageAccounts/privateEndpointConnections/read` | Reads private endpoint connections on storage accounts | Storage account with public network access despite having private endpoint, dangling private endpoint connections | Cannot verify private endpoint configuration on storage. |
| `Microsoft.Storage/storageAccounts/queueServices/queues/read` | Enumerates storage queues and reads queue service logging | Queue service logging disabled, queue without CMK encryption | Cannot audit queue-level logging. |
| `Microsoft.Storage/storageAccounts/queueServices/read` | Enumerates storage queues and reads queue service logging | Queue service logging disabled, queue without CMK encryption | Cannot audit queue-level logging. |
| `Microsoft.Storage/storageAccounts/read` | Enumerates storage accounts and their properties (SKU, kind, encryption, TLS version, network rules) | Public blob access enabled, TLS 1.0/1.1 allowed, HTTPS not enforced, network access unrestricted, missing customer-managed key encryption, insecure default action | Cannot audit storage accounts at all. |
| `Microsoft.Storage/storageAccounts/tableServices/read` | Enumerates storage tables and reads table service logging | Table service logging disabled, table without CMK encryption | Cannot audit table-level logging. |
| `Microsoft.Storage/storageAccounts/tableServices/tables/read` | Enumerates storage tables and reads table service logging | Table service logging disabled, table without CMK encryption | Cannot audit table-level logging. |


## StorageCache (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.StorageCache/caches/read` | Reads Azure HPC Cache configuration (high-performance storage caching) | HPC Cache without encryption, missing network security, exposed cache endpoints | Cannot audit HPC Cache instances used for HPC workloads. |


## StorageSync (1)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.StorageSync/storageSyncServices/read` | Reads Azure File Sync services, sync groups, and registered servers | File Sync without cloud tiering security, unregistered sync endpoints, sync group with public network access | Cannot audit hybrid file sync configurations. |


## StreamAnalytics (4)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.StreamAnalytics/streamingjobs/inputs/read` | Reads Stream Analytics job configuration | Stream Analytics job without managed identity, missing CMK on input/output storage, jobs with excessive privileges | Cannot audit stream processing jobs. |
| `Microsoft.StreamAnalytics/streamingjobs/outputs/read` | Reads Stream Analytics job configuration | Stream Analytics job without managed identity, missing CMK on input/output storage, jobs with excessive privileges | Cannot audit stream processing jobs. |
| `Microsoft.StreamAnalytics/streamingjobs/read` | Reads Stream Analytics job configuration | Stream Analytics job without managed identity, missing CMK on input/output storage, jobs with excessive privileges | Cannot audit stream processing jobs. |
| `Microsoft.StreamAnalytics/streamingjobs/transformations/read` | Reads Stream Analytics job configuration | Stream Analytics job without managed identity, missing CMK on input/output storage, jobs with excessive privileges | Cannot audit stream processing jobs. |


## Web (10)

| Permission | Function | Findings this enables | Impact if not granted |
|---|---|---|---|
| `Microsoft.Web/hostingEnvironments/read` | Reads App Service Environment (ASE) configuration | ASE with internal load balancer misconfigured, ASE without WAF, weak inbound network rules | Cannot audit dedicated ASE deployments. |
| `Microsoft.Web/serverFarms/read` | Enumerates App Service Plans and reads their SKU and capacity | App Service Plan with basic SKU (no autoscale, no staging slots), single-instance plans without HA | Cannot audit App Service Plan configuration. |
| `Microsoft.Web/serverFarms/sites/read` | Reads the list of sites within each App Service Plan | None directly - relational data. | Cannot correlate apps to their plans. |
| `Microsoft.Web/sites/config/read` | Reads Web App / Function App configuration (auth, HTTPS settings, TLS version, remote debugging) | HTTPS not enforced, weak minimum TLS, remote debugging enabled, client cert not required, insecure FTP state, weak CORS policy, missing Always On | Cannot audit app-level security settings. |
| `Microsoft.Web/sites/functions/read` | Reads Function App function definitions | Functions with anonymous auth level, missing function-level auth | Cannot enumerate individual functions within Function Apps. |
| `Microsoft.Web/sites/read` | Enumerates Web Apps, Function Apps, and Logic Apps and reads their metadata | App with public network access, missing managed identity, using deprecated runtime, missing diagnostic logging | Cannot audit any App Services. |
| `Microsoft.Web/sites/slots/config/read` | Reads configuration of App Service deployment slots (staging, production) | Slot with different security config than production, slot missing HTTPS enforcement | Cannot audit slot-specific security settings. |
| `Microsoft.Web/sites/slots/read` | Enumerates App Service deployment slots | Slot without VNet integration, slot with default hostname exposed | Cannot audit slot inventory. |
| `Microsoft.Web/sites/sourceControls/read` | Reads source control integration (GitHub, Azure DevOps) on App Services | App deploying from untrusted repository, credentials stored in source control config | Cannot audit deployment source security. |
| `Microsoft.Web/sites/virtualNetworkConnections/read` | Reads VNet integration configuration on App Services | App Service without VNet integration, missing regional VNet integration | Cannot verify apps are integrated with private networks. |


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
