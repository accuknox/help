---
title: CSPM Assets Support
description:  This document provides a list of assets supported by Accuknox Cloud Security Posture Management (CSPM) across AWS, Azure, and GCP clouds.
---

<style>
    .md-typeset__scrollwrap{
        width: 140%;
    }
</style>

# CSPM Assets Support

| **Category** | **AWS** | **Azure** | **GCP** |
|--------------|---------|-----------|---------|
| **Cloud Account** | `aws_account` | `azure_subscription` | `gcp_project` |
| **IAM** | `aws_iam_user`, `aws_iam_role`, `aws_iam_group`, `aws_accessanalyzer_analyzer`, `aws_cognito_identity_pool`, `aws_cognito_identity_provider`, `aws_cognito_user_pool`, `aws_iam_policy` | `azure_role_assignment` | `gcp_iam_policy`, `gcp_iam_role`, `gcp_service_account`, `gcp_secret_manager_secret`, `gcp_service_account_key` |
| **Security Monitoring** | `aws_accessanalyzer_finding` | `azure_log_alert` | - |
| **Certificate Management** | `aws_acm_certificate`, `aws_acmpca_certificate_authority` | - | - |
| **Serverless** | `aws_amplify_app`, `aws_lambda_function`, `aws_redshiftserverless_namespace`, `aws_redshiftserverless_workgroup` | `azure_app_configuration`, `azure_app_service_environment`, `azure_app_service_function_app`, `azure_app_service_plan`, `azure_app_service_web_app`, `azure_app_service_web_app_slot` | - |
| **API Management** | `aws_api_gateway_authorizer`, `aws_api_gateway_rest_api`, `aws_api_gateway_domain_name`, `aws_api_gateway_stage`, `aws_api_gateway_usage_plan`, `aws_api_gatewayv2_api`, `aws_api_gatewayv2_domain_name`, `aws_api_gatewayv2_integration`, `aws_api_gatewayv2_route`, `aws_api_gatewayv2_stage` | `azure_api_management` | `gcp_apikeys_key` |
| **Backup & Disaster Recovery** | `aws_backup_job`, `aws_backup_plan`, `aws_backup_recovery_point`, `aws_backup_selection`, `aws_backup_vault`, `aws_drs_job`, `aws_drs_recovery_instance`, `aws_drs_recovery_snapshot`, `aws_drs_source_server`, `aws_dynamodb_backup` | `azure_recovery_services_vault` | - |
| **Deployment** | `aws_cloudformation_stack`, `aws_cloudformation_stack_resource`, `aws_cloudformation_stack_set` | - | - |
| **CDN** | `aws_cloudfront_cache_policy`, `aws_cloudfront_distribution`, `aws_cloudfront_function`, `aws_cloudfront_origin_request_policy`, `aws_cloudfront_response_headers_policy`, `aws_cloudsearch_domain` | - | - |
| **Audit Logging** | `aws_cloudtrail_channel`, `aws_cloudtrail_trail` | - | `gcp_logging_bucket`, `gcp_logging_sink` |
| **CodeArtifact** | `aws_codeartifact_domain`, `aws_codeartifact_repository` | - | - |
| **CI/CD** | `aws_codebuild_build`, `aws_codebuild_project`, `aws_codebuild_source_credential`, `aws_codecommit_repository`, `aws_codedeploy_app`, `aws_codedeploy_deployment_config`, `aws_codedeploy_deployment_group`, `aws_codepipeline_pipeline` | - | - |
| **Miscellaneous** | `aws_config_aggregate_authorization`, `aws_config_configuration_recorder`, `aws_dlm_lifecycle_policy`, `aws_ec2_launch_configuration`, `aws_ec2_launch_template`, `aws_ec2_launch_template_version`, `aws_ec2_managed_prefix_list`, `aws_redshift_event_subscription` | `azure_search_service`, `azure_servicebus_namespace`, `azure_spring_cloud_service`, `azure_stream_analytics_job` | - |
| **Cluster** | `aws_dax_cluster`, `aws_ecs_cluster`, `aws_eks_cluster`, `aws_elasticache_cluster` | `azure_kubernetes_cluster` | `gcp_kubernetes_cluster` |
| **Networking** | `aws_dax_subnet_group`, `aws_ec2_application_load_balancer`, `aws_ec2_classic_load_balancer`, `aws_ec2_gateway_load_balancer`, `aws_ec2_load_balancer_listener`, `aws_ec2_network_interface`, `aws_ec2_network_load_balancer`, `aws_ec2_target_group`, `aws_ec2_transit_gateway`, `aws_ec2_transit_gateway_route`, `aws_ec2_transit_gateway_route_table`, `aws_ec2_transit_gateway_vpc_attachment`, `aws_elasticache_subnet_group`, `aws_rds_db_proxy`, `aws_rds_db_subnet_group`, `aws_route53_domain`, `aws_route53_zone`, `aws_s3_access_point`, `aws_vpc`, `aws_vpc_subnet`, `aws_vpc_eip`, `aws_vpc_nat_gateway`, `aws_vpc_security_group`, `aws_vpc_security_group_rule`, `aws_vpc_network_acl`, `aws_vpc_route`, `aws_vpc_route_table` | `azure_network_interface`, `azure_virtual_network`, `azure_subnet`, `azure_public_ip`, `azure_network_security_group`, `azure_application_security_group`, `azure_lb`, `azure_route_table`, `azure_application_gateway`, `azure_dns_zone`, `azure_eventgrid_domain`, `azure_eventgrid_topic`, `azure_eventhub_namespace`, `azure_express_route_circuit`, `azure_firewall`, `azure_firewall_policy`, `azure_lb_nat_rule`, `azure_lb_outbound_rule`, `azure_lb_probe`, `azure_lb_rule`, `azure_nat_gateway`, `azure_network_watcher`, `azure_private_dns_zone`, `azure_signalr_service`, `azure_virtual_network_gateway` | `gcp_compute_firewall`, `gcp_compute_forwarding_rule`, `gcp_compute_global_address`, `gcp_compute_snapshot`, `gcp_compute_network`, `gcp_compute_subnetwork` |
| **Data Analytics** | `aws_dms_replication_instance` | - | `gcp_pubsub_snapshot`, `gcp_pubsub_subscription`, `gcp_pubsub_topic` |
| **DocumentDB** | `aws_docdb_cluster`, `aws_docdb_cluster_instance`, `aws_docdb_cluster_snapshot` | - | - |
| **Database** | `aws_dynamodb_global_table`, `aws_dynamodb_table`, `aws_rds_db_cluster`, `aws_rds_db_instance`, `aws_redshift_cluster`, `aws_redshift_snapshot`, `aws_redshift_subnet_group` | `azure_redis_cache`, `azure_sql_database`, `azure_sql_server`, `azure_mssql_elasticpool`, `azure_mssql_managed_instance`, `azure_mysql_flexible_server`, `azure_mysql_server`, `azure_postgresql_flexible_server`, `azure_postgresql_server`, `azure_storage_account`, `azure_storage_table` | `gcp_bigquery_dataset`, `gcp_bigtable_instance`, `gcp_sql_backup`, `gcp_sql_database`, `gcp_sql_database_instance` |
| **Block Storage** | `aws_ebs_volume`, `aws_ebs_snapshot` | `azure_compute_disk`, `azure_hpc_cache` | `gcp_compute_disk` |
| **Compute** | `aws_ec2_ami`, `aws_ec2_autoscaling_group`, `aws_ec2_capacity_reservation`, `aws_ec2_reserved_instance` | `azure_batch_account`, `azure_cognitive_account`, `azure_compute_availability_set`, `azure_compute_disk_access`, `azure_compute_disk_encryption_set`, `azure_compute_snapshot`, `azure_compute_ssh_key`, `azure_compute_virtual_machine_scale_set`, `azure_compute_virtual_machine_scale_set_vm` | `gcp_compute_address`, `gcp_compute_autoscaler`, `gcp_compute_instance_group`, `gcp_compute_instance_template`, `gcp_compute_node_group`, `gcp_compute_node_template`, `gcp_compute_target_pool` |
| **Host** | `aws_ec2_instance`, `aws_ec2_instance_availability` | `azure_compute_virtual_machine`, `azure_bastion_host` | `gcp_compute_instance` |
| **Key Management** | `aws_ec2_key_pair`, `aws_kms_key` | `azure_key_vault`, `azure_key_vault_key`, `azure_key_vault_key_version`, `azure_key_vault_managed_hardware_security_module` | - |
| **Object Storage** | `aws_s3_bucket` | `azure_storage_container`, `azure_storage_blob_service` | `gcp_storage_bucket` |
| **AI + Machine Learning** | `aws_sagemaker_app`, `aws_sagemaker_domain` | `azure_databricks_workspace`, `azure_machine_learning_workspace` | `gcp_vertex_ai_model`, `gcp_vertex_ai_endpoint` |
| **Developer Tools** | `aws_ses_email_identity`, `aws_sns_topic`, `aws_sns_subscription`, `aws_sqs_queue` | - | - |
| **Workspace** | `aws_workspaces_workspace` | - | - |
| **Operations** | - | `azure_application_insight` | - |
| **Automation** | - | `azure_automation_account`, `azure_automation_variable` | - |
| **Containers** | - | `azure_container_group`, `azure_container_registry` | `gcp_artifact_registry_repository` |
| **Pipeline** | - | `azure_data_factory_pipeline` | - |
| **IOT** | - | `azure_iothub` | - |
| **Analytics** | - | `azure_kusto_cluster` | - |
| **Management** | - | `azure_maintenance_configuration`, `azure_management_lock`, `azure_tenant` | - |
| **Miscellaneous** | - | `azure_search_service`, `azure_servicebus_namespace`, `azure_spring_cloud_service`, `azure_stream_analytics` | - |


- - -
[SCHEDULE DEMO](https://www.accuknox.com/contact-us){ .md-button .md-button--primary }