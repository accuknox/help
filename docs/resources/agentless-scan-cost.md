---
title: Cloud Cost of Agentless VM Scanning
description: Estimate the AWS, Azure and GCP bill for one AccuKnox agentless VM scanner, including usage charges, cross-zone scanning and the per-zone scanner trade-off.
---

<!--
Source notes for reviewers. This comment does not render on the page.
- Prices: provider price data and pricing pages, checked 2026-10-16. See the Sources section.
- The resource lists, the `multi-az-support` default of `false`, and the running-versus-stopped VM scan behavior come from the agentless scanner cost draft. The Terraform is not in this repo, so check them against it when the Terraform changes.
- The GCP snapshot rows assume the scanner sets no snapshot location, so Google's default US multi-region applies. If the Terraform sets a regional location, change the snapshot rate to $0.05 per GiB-month and delete the snapshot upload and download row.
-->

# Cloud cost of agentless VM scanning

Agentless VM scanning runs a scanner VM inside your own cloud account. Your cloud provider bills you for the resources `terraform apply` creates. One scanner in one region costs about $68 a month on AWS, $67 on Azure and $30 on GCP at list prices. Usage charges come on top. AccuKnox licensing is separate and is not covered here.

## One Scanner Costs $30 to $68 a Month Before Usage

Terraform creates one set of resources per region you deploy into. Prices are on-demand list rates for one region per cloud, in USD, on a 730-hour month, checked October 2026. Your rates depend on your region, agreement and discounts.

=== "AWS"

    These prices are for the `us-east-1` region, US East in Northern Virginia. The scanner scans only running VMs, and only their boot disks.

    | Resource | When | Price |
    | --- | --- | --- |
    | EC2 instance, `t3.medium` | Always on | $0.0416 per hour |
    | NAT gateway | Always on | $0.045 per hour, plus $0.045 per GB processed |
    | Elastic IP on the NAT gateway | Always on | $0.005 per hour |
    | 10 GB `gp3` root volume, encrypted | Always on | $0.08 per GB-month |
    | VPC, subnets, internet gateway, route tables, security group | Always on | No charge |
    | IAM role, inline policy, instance profile | Always on | No charge |
    | EBS snapshot of each boot disk | Per scan | $0.05 per GB-month |
    | Clone volume, `gp2` | Per scan | $0.10 per GB-month |

    **Example:** one scanner in one region costs about **$67.67 a month** in always-on charges. The instance is $30.37, the NAT gateway $32.85, the IP $3.65 and the root volume $0.80.

=== "Azure"

    These prices are for East US. The scanner scans only OS disks. It scans stopped VMs too.

    | Resource | When | Price |
    | --- | --- | --- |
    | Linux VM, `Standard_B2s` | Always on | $0.0416 per hour |
    | NAT gateway | Always on | $0.045 per hour, plus $0.045 per GB processed |
    | Standard public IP | Always on | $0.005 per hour |
    | OS managed disk, `Standard_LRS` | Always on | By size tier, for example $1.54 a month for 32 GiB |
    | Resource group, VNet, subnet, NIC, NSG | Always on | No charge |
    | Custom role, managed identity, role assignment | Always on | No charge |
    | Snapshot of each OS disk | Per scan | $0.05 per GB-month |
    | Clone disk | Per scan | By size tier |

    **Example:** one scanner in one region costs about **$66.87 a month** before the OS disk. The VM is $30.37, the NAT gateway $32.85 and the IP $3.65. The Terraform does not set an OS disk size, so the disk inherits the image size. Check your deployment to price it.

=== "GCP"

    These prices are for us-central1 (Iowa). The scanner scans only boot disks. It scans stopped VMs too.

    | Resource | When | Price |
    | --- | --- | --- |
    | Compute instance, `e2-medium` | Always on | $0.0335 per hour |
    | Cloud NAT | Always on | $0.0014 per VM-hour, plus $0.045 per GiB processed |
    | External IP used by Cloud NAT | Always on | $0.005 per hour |
    | 10 GB `pd-balanced` boot disk | Always on | $0.10 per GiB-month |
    | VPC, subnet, Cloud Router, firewall rule | Always on | No charge |
    | Service account, custom IAM role, bindings | Always on | No charge |
    | Snapshot of each boot disk | Per scan | $0.065 per GiB-month, US multi-region (the default location) |
    | Snapshot upload and download | Per scan | $0.02 per GiB each, US multi-region |
    | Clone disk, `pd-standard` | Per scan | $0.04 per GiB-month |

    **Example:** one scanner in one region costs about **$30.13 a month** in always-on charges. The instance is $24.46, Cloud NAT $1.02, the IP $3.65 and the boot disk $1.00.

## How the Cost Behaves

- **Fixed charges dominate.** The instance, NAT gateway and IP bill by the hour whether you scan five VMs or five hundred.
- **Snapshots and clones bill only while they exist.** Each lives for the length of one scan. They matter at high scan frequency or a large total volume of disk scanned.
- **Everything multiplies per region.** Two regions is two of every always-on charge.

## Cross-Zone Scanning Adds No Data Transfer Charge

A scanner in zone A scans a VM in zone B in four steps. It snapshots the VM disk, copies the disk into zone A, scans the copy and deletes it. No live traffic crosses a zone boundary. The three clouds also do not bill the snapshot restore as zone-to-zone transfer.

| Cloud | Why a cross-zone restore adds no transfer charge |
| --- | --- |
| AWS | EBS replicates snapshot data across all Availability Zones in the Region, so you can restore a volume in any of them. [AWS bills snapshot data transfer for copies across Regions](https://aws.amazon.com/ebs/pricing/), not within one. |
| Azure | Azure [bills data transfer between regions, not between services in one region](https://azure.microsoft.com/en-us/pricing/details/bandwidth/). |
| GCP | Google bills snapshot network fees by snapshot location, a region or a multi-region, and never by zone. The US multi-region fee in the GCP table applies to every scan, in any zone. |

The `multi-az-support` setting controls zone coverage. It defaults to `false`, which scans only the scanner's own zone. Set it to `true` to cover every zone in the region with the same single scanner.

## Choose One Scanner per Region Unless a Zone Outage Is Unacceptable

Zone coverage is a resilience decision, not a cost decision. Cross-zone scanning costs nothing extra, so one scanner reaches every zone.

| Option | Always-on cost | Zones covered | Trade-off |
| --- | --- | --- | --- |
| One scanner per region, `multi-az-support = true` | 1x the fixed charges | Every zone in the region | Scans for the whole region stop while the scanner's zone is down. |
| One scanner per region, `multi-az-support = false` | 1x the fixed charges | The scanner's own zone only | VMs in other zones are never scanned. |
| One scanner per zone | Zone count x the fixed charges | Every zone, each by its own scanner | Scanning continues when one zone is down. Each extra scanner adds the full fixed charge. |

Decide in two steps.

1. Start with one scanner per region and `multi-az-support = true`. It covers every zone at 1x the fixed charges.
2. Add a scanner per zone only if a scan gap during a zone outage is not acceptable. Multiply the fixed charges above by your zone count. On AWS, three zones cost about $203 a month, against $67.67 for one scanner.

## Usage Charges Depend on How Much You Scan

Two charges depend on volume and are not in the examples above.

- **Per-scan storage.** A snapshot and a clone exist for the length of each scan, at the per-scan rates in the tables. On GCP, snapshot upload and download add $0.02 per GiB each.
- **NAT data.** The scanner downloads vulnerability database and malware signature updates, cached after the first run, and uploads findings.

Your cloud provider also bills internet egress beyond the NAT charge. It bills key management if you encrypt with your own keys, plus support plans and taxes. To price your own usage, use the [AWS Pricing Calculator](https://calculator.aws/), the [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) or the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator).

## Prices Come From the Cloud Providers' Pricing Pages

- AWS: [EC2 on-demand pricing](https://aws.amazon.com/ec2/pricing/on-demand/), [VPC pricing](https://aws.amazon.com/vpc/pricing/), [EBS pricing](https://aws.amazon.com/ebs/pricing/) and [EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
- Azure: [Linux VM pricing](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/), [NAT gateway pricing](https://azure.microsoft.com/en-us/pricing/details/azure-nat-gateway/), [public IP pricing](https://azure.microsoft.com/en-us/pricing/details/ip-addresses/), [managed disks pricing](https://azure.microsoft.com/en-us/pricing/details/managed-disks/) and [bandwidth pricing](https://azure.microsoft.com/en-us/pricing/details/bandwidth/)
- GCP: [Compute Engine VM pricing](https://cloud.google.com/compute/vm-instance-pricing), [Cloud NAT pricing](https://cloud.google.com/nat/pricing), [disk and snapshot pricing](https://cloud.google.com/compute/disks-image-pricing) and [VPC network pricing](https://cloud.google.com/vpc/network-pricing)

## Related

- [Cloud Based VM Scanning (Agentless)](../how-to/vm-security/agentless/cloud-vm-scanning.md) for AWS, GCP and Azure
- [Agentless Azure VM Scanning](../how-to/vm-security/agentless/azure-cloud-vm.md)
- [OpenShift VM Scanning (Agentless)](../how-to/vm-security/agentless/openshift-vm-scanning.md)
- [Get Billable Asset Count (Multi-Cloud)](asset-billable-check.md)
