---
title: Terraform Cloud Onboarding
description: Onboard standalone AWS, Azure, and GCP cloud accounts to the AccuKnox platform using Terraform. Pick a cloud provider to get the prerequisites, Terraform configuration, onboarding steps, and verification process.
hide:
  - toc
---

# Terraform Cloud Onboarding

<style>
  .nt-card-title{
    text-align: center;
  }

  .nt-card-img img{
    color: #00025;
  }
</style>

## Overview

Terraform Cloud Onboarding provides step-by-step instructions for onboarding supported standalone cloud accounts to the AccuKnox platform using Terraform.

This documentation covers Terraform onboarding for:

- AWS Standalone Account
- Microsoft Azure Standalone Subscription
- Google Cloud Platform (GCP) Standalone Project

Each guide includes the prerequisites, Terraform configuration, onboarding steps, and verification process.

## Choose a Cloud Provider

::cards:: cols=3

- title: AWS
  content: Onboard a standalone AWS account with a Terraform-provisioned IAM user.
  image: ./icons/aws-vm.svg
  url: /how-to/terraform-aws-onboarding/

- title: Azure
  content: Onboard a standalone Azure subscription with a Terraform-provisioned AD application.
  image: ./icons/azure-vm.svg
  url: /how-to/terraform-azure-onboarding/

- title: GCP
  content: Onboard a standalone GCP project with a Terraform-provisioned service account.
  image: ./icons/gcp-vm.svg
  url: /how-to/terraform-gcp-onboarding/

::/cards::
