---
title: VM Onboarding for Ubuntu
description: Prepare Ubuntu hosts and onboard a VM fleet to AccuKnox using the SSH-based fleet onboarding script.
---

# VM Onboarding for Ubuntu

Ubuntu host preparation, fleet onboarding, and scanner configuration.

This guide takes a VM fleet from zero to onboarded and protected on AccuKnox using the fleet onboarding script. The control plane runs the script over SSH against every host. Prepare the hosts, open the ports, set the tokens, configure the script, choose what to scan, then run.

## Fleet and Resource Requirements

The fleet has one control plane and one or more workers. The control plane also runs the onboarding script and must reach every worker over the internal network. Keep the control plane and workers on the same private network.

| Node | CPU | Memory | Disk |
|---|---|---|---|
| **Control plane** | 2 vCPU | 4 GB | 24 GB |
| **Worker** | 2 vCPU | 2 GB | 12 GB |

## 1. Prerequisites

Confirm each condition on every host before running the script.

| Prerequisite | What to Verify |
|---|---|
| **Access** | root or sudo on every host. The agents install to root paths and need privilege to protect the host. |
| **Docker** | Docker 19.03 or later and Docker Compose 1.27 or later. The onboarding script installs Docker automatically if it is missing. |
| **Kernel** | Version 5.8 or later with BPF LSM for container protection. Confirm with `uname -r`. |
| **BTF** | `/sys/kernel/btf/vmlinux` present on each host. |
| **Connectivity** | Control plane reaches every worker on the internal network, and reaches the AccuKnox endpoints outbound. |
| **SSH and sudo** | Control plane public key in `authorized_keys` on every host, passwordless sudo confirmed. |

## 2. Host Preparation

### 2.1 Kernel, BPF LSM, and BTF

Container protection needs a 5.8 or later kernel with BPF LSM, and BTF information present. Check all three on every host.

```bash
uname -r                                                  # 5.8 or later

[ -e /sys/kernel/btf/vmlinux ] && echo "BTF present" || echo "BTF not present"

cat /sys/kernel/security/lsm                              # bpf should appear in the list
```

If bpf is not in the list, enable BPF LSM by adding it to the kernel command line, then reboot and recheck.

```bash
sudo sed -i 's/^GRUB_CMDLINE_LINUX="/GRUB_CMDLINE_LINUX="lsm=lockdown,capability,yama,apparmor,bpf /' /etc/default/grub
sudo update-grub
sudo reboot

# verify after reboot
cat /sys/kernel/security/lsm
```

**Docs:** [Enable BPF LSM, KubeArmor getting started](https://github.com/kubearmor/KubeArmor/blob/main/getting-started/FAQ.md)

### 2.2 SSH Between Nodes

The script runs from the control plane and connects to every host over SSH, including the control plane itself. Generate a key on the control plane with no passphrase so the script runs non-interactively.

```bash
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

Add the public key to `authorized_keys` on every host, each worker and the control plane.

```bash
mkdir -p ~/.ssh && chmod 700 ~/.ssh
echo '<control-plane-public-key>' >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

Before running the non-interactive SSH checks, connect to each host and control plane from the control plane once and verify its SSH host key. This saves the host as trusted in the control plane's `known_hosts` file.

Then verify passwordless SSH access from the control plane to every host, including the control plane itself:

```bash
ssh -o BatchMode=yes <user>@<cp-ip> hostname
ssh -o BatchMode=yes <user>@<worker-ip> hostname

### 2.3 Passwordless Sudo

If the login user is not root, the script needs passwordless sudo on each host. Check and set it.

```bash
sudo -n true 2>/dev/null && echo ok || echo "needs setup"

echo "<user> ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/<user>
sudo chmod 440 /etc/sudoers.d/<user>
```

## 3. Firewall Ports

### 3.1 Inbound, on the Control Plane

Open the agent ports on the control plane. Workers make outbound connections, so they need no inbound rule.

```bash
# Allow SSH before enabling UFW.
# If SSH uses the default port:
sudo ufw allow OpenSSH

# If SSH uses a custom port, use this instead:
# sudo ufw allow <ssh-port>/tcp

# Open the AccuKnox agent ports on the control plane
sudo ufw allow 32768:32771/tcp

# Enable UFW if it is not already active
sudo ufw --force enable

# Verify the firewall rules
sudo ufw status numbered
```

| Port | Component | Open On |
|---|---|---|
| **32768** | kubearmor-relay-server | Control plane |
| **32769** | shared-informer-agent | Control plane |
| **32770** | policy-enforcement-agent | Control plane |
| **32771** | hardening-module | Control plane |

### 3.2 Outbound, from the Control Plane

The control plane connects to the required AccuKnox endpoints. By default, UFW allows outbound traffic, so no additional rules are required unless outbound traffic is explicitly restricted or denied.

> **Note:** Use the endpoint values provided in the `knoxctl onboard` command generated by AccuKnox. Do not assume the `<env>` value.

```bash
# Check the current UFW configuration
sudo ufw status verbose

# Run these only if the outbound policy is restricted or set to deny
sudo ufw allow out 3000/tcp
sudo ufw allow out 443/tcp
sudo ufw allow out 8081/tcp
sudo ufw allow out 9090/tcp

# Reload and verify the firewall configuration
sudo ufw reload
sudo ufw status numbered
```

| Port | Endpoint | Purpose |
|---|---|---|
| **3000** | `knox-gw.<env>.accuknox.com` | Knox Gateway |
| **443** | `pps.<env>.accuknox.com` | Policy Provisioning |
| **8081, 9090** | `spire.<env>.accuknox.com` | SPIRE Server |

### Verify Outbound Connectivity

From the control plane, verify that each required endpoint and port is reachable:

```bash
nc -zv knox-gw.<env>.accuknox.com 3000
nc -zv pps.<env>.accuknox.com 443
nc -zv spire.<env>.accuknox.com 8081
nc -zv spire.<env>.accuknox.com 9090
```

A successful result confirms TCP connectivity from the control plane to the corresponding endpoint and port.

## 4. Onboarding Inputs

Access the onboarding script from here: [vm_onboarding.sh](https://gist.github.com/VanishaParwal/3cd31a55009d96ecd8c30c4cfcba57ad). Collect four inputs before editing the script: the inventory file, the join token, the artifact label, and the scanner API token.

### 4.1 Inventory

The script reads a CSV inventory that lists which hosts to process, how to reach them, and the role of each. Create it in the same directory as the script.

```bash
cat > inventory.csv <<'EOF'
hostname,ip,ssh_user,ssh_key_path,role,scan
<hostname>,<ip>,<ssh_user>,<ssh_key_path>,cp,<true|false>
<hostname>,<ip>,<ssh_user>,<ssh_key_path>,node,<true|false>
EOF
```

| Column | Description |
|---|---|
| **hostname** | Host identifier recorded in run logs and the status report. |
| **ip** | Internal IP address the control plane connects to over SSH. |
| **ssh_user** | SSH login user for this host. Overrides the global `SSH_USER` when set. |
| **ssh_key_path** | Path to the SSH private key for this host. Overrides the global `SSH_KEY` when set. |
| **role** | `cp` for the control plane, `node` for a worker. Exactly one `cp` is allowed. |
| **scan** | `true` installs the omni and RRA scanners on this host, `false` skips them. |

If no row sets role to `cp`, the script elects the first row as control plane and warns. Declare the `cp` role explicitly.

### 4.2 Join Token

The join token authenticates each host to your tenant. In the console, open **Settings**, then **Manage Cluster**, click **Onboard Now**, and select **VM**. The console generates a knoxctl onboard command. The join token sits in the `--join-token` flag, and the `spire-host`, `pps-host`, and `knox-gateway` values come from the same command. Export the token rather than pasting it into the script.

```bash
export AK_JOIN_TOKEN="<your_join_token>"
```

**Docs:** [VM Onboarding with Docker](https://help.accuknox.com/how-to/vm-onboard-deboard-docker/) · [VM Onboarding with Systemd](https://help.accuknox.com/how-to/vm-onboard-deboard-systemd/)

### 4.3 Artifact Label

An artifact label groups scanner findings under a named bucket in the dashboard. Create it in the console under **Settings**, then **Labels**, and copy the name exactly. Set it as `ARTIFACT_LABEL` in the config.

**Docs:** [Create Labels](https://help.accuknox.com/how-to/how-to-create-labels/)

### 4.4 Scanner API Token

The scanner uses a separate API token, `OMNI_ARTIFACT_API_TOKEN`, which authorizes scan results to upload to your tenant. Generate it in the console under **Settings**, then **Tokens**, and export it. Both tokens must be exported in the same shell session before you run the script.

```bash
export OMNI_ARTIFACT_API_TOKEN="<your_api_token>"
```

**Docs:** [Create Tokens](https://help.accuknox.com/how-to/how-to-create-tokens/)

## 5. Changes in the Onboarding Script

Open `vm_onboarding.sh`. The configuration is one block at the top. Fill in the values you collected and edit only this block.

```bash
# --- SSH ---
SSH_USER=""                                   # default login user for all hosts
SSH_KEY=""                                    # default private key path

# --- cluster onboarding (from Manage Cluster) ---
ONB_VERSION="v0.12.2"
SPIRE_HOST="spire.<env>.accuknox.com"
PPS_HOST="pps.<env>.accuknox.com"
KNOX_GATEWAY="knox-gw.<env>.accuknox.com:3000"
VM_MODE="docker"                             # docker | systemd

# --- secrets (exported before running, not pasted here) ---
AK_JOIN_TOKEN="${AK_JOIN_TOKEN}"
OMNI_API_TOKEN="${OMNI_ARTIFACT_API_TOKEN}"

# --- scanner ---
SCANNER_ENABLED=1
SCANNER_RRA=1                                # STIG and compliance container
SCANNER_OMNI=1                               # vulnerability agent
SCANNER_MODE="every_vm"                       # every_vm | selected_vms | control_plane_only
TENANT_ID="<your-tenant-id>"
CSPM_URL="<your-cspm-endpoint>"
ARTIFACT_LABEL=""                             # label from step 4.3
CLUSTER_NAME=""                               # cluster name from step 4.2
ENABLE_MALWARE=0

# --- policies ---
POLICY_MODE="audit"                          # audit | block
POLICIES_DIR="policies"

# --- behaviour ---
PARALLEL=20
AUTO_INSTALL_DOCKER=1
INVENTORY="inventory.csv"
```

| Field | Value or Source |
|---|---|
| **ONB_VERSION** | The version shown in the console onboard command. |
| **SPIRE_HOST, PPS_HOST, KNOX_GATEWAY** | Copied from the knoxctl onboard command in Manage Cluster. |
| **AK_JOIN_TOKEN** | Exported environment variable from step 4.2. |
| **OMNI_API_TOKEN** | Exported environment variable from step 4.4. |
| **TENANT_ID** | Tenant UUID from the console Settings page. |
| **CSPM_URL** | CSPM endpoint from the console Settings page. |
| **ARTIFACT_LABEL** | Label name from step 4.3. |
| **CLUSTER_NAME** | Cluster name from step 4.2. |
| **POLICY_MODE** | Keep `audit` until you have reviewed findings, then switch to `block`. |

## 6. Scanner Configuration by Objective

The scanner block decides what runs on each host. Set the flags to match what you want to scan for. The runtime agent installs regardless. The omni and RRA scanners are optional and controlled by the flags below.

| Objective | Config Flags | What It Does |
|---|---|---|
| **Runtime security only** | `SCANNER_ENABLED=0`, `POLICY_MODE=audit` then `block` | Installs the runtime agent only. Enforces process, file, and network policy on the host. |
| **Vulnerability scanning** | `SCANNER_ENABLED=1`, `SCANNER_OMNI=1`, `ENABLE_MALWARE=0` | Adds the omni agent. Scans installed packages for known CVEs and builds an SBOM per host. |
| **Malware scanning** | `SCANNER_ENABLED=1`, `SCANNER_OMNI=1`, `ENABLE_MALWARE=1` | Adds malware detection to the omni agent alongside vulnerability scanning. |
| **Compliance and STIG** | `SCANNER_ENABLED=1`, `SCANNER_RRA=1` | Adds the RRA container. Runs STIG and CIS style benchmark checks and reports control failures by severity. |
| **Which hosts** | `SCANNER_MODE = every_vm, selected_vms`, or `control_plane_only` | Scopes where scanners run. With `selected_vms` the inventory scan column decides per host. |

### Runtime Security

The runtime agent watches process, file, and network activity on the host and enforces policy. In audit mode it observes and reports, in block mode it enforces. After onboarding, the console autodiscovers least privilege policies from observed behavior under **Runtime Protection**, then **Policies**, then **Discovered Policies**. Review in audit first, then move to block.

**Docs:** [VM Onboarding with Docker](https://help.accuknox.com/how-to/vm-onboard-deboard-docker/) · [VM Onboarding with Systemd](https://help.accuknox.com/how-to/vm-onboard-deboard-systemd/)

### Vulnerability Scanning

The omni agent inventories installed packages and software on each host, reports known CVEs with component and license counts, and generates an SBOM for the host. Set `SCANNER_OMNI` to `1` and leave `ENABLE_MALWARE` at `0` for vulnerabilities only.

**Docs:** [Host Vulnerability & Malware Scan](https://help.accuknox.com/use-cases/vm-host-scan/)

### Malware Scanning

Malware scanning runs inside the omni agent. Set `ENABLE_MALWARE` to `1` in addition to `SCANNER_OMNI` to scan hosts for malware alongside the vulnerability pass. Results land under the same artifact label.

**Docs:** [Malware Scan](https://help.accuknox.com/use-cases/vm-malware-scan/)

### Compliance and STIG

The RRA container runs compliance and hardening checks against STIG and CIS style benchmarks and reports control failures mapped to the standard, with remediation guidance. Set `SCANNER_RRA` to `1` to include it.

**Docs:** [CIS Benchmarking](https://help.accuknox.com/how-to/cis-benchmarking/)

## 7. Run the Script

With the inventory created, both tokens exported, and the config block filled in, make the script executable and run the commands in order.

```bash
chmod +x vm_onboarding.sh

# preflight, reads everything and changes nothing
./vm_onboarding.sh readiness

# dry run, prints the plan with secrets redacted
./vm_onboarding.sh onboard --dry-run

# onboard the fleet
./vm_onboarding.sh onboard

# resume after a partial failure, skips completed stages
./vm_onboarding.sh onboard --resume

# status at any time
./vm_onboarding.sh status
```

Every host must show ready in the readiness check before you proceed. The script onboards the control plane first, waits for it to become healthy, then onboards workers in parallel. After all hosts complete it pushes policies and prints a per-host status report.

## 8. What the Script Does Per Host

Each host passes through a seven-stage pipeline. Completed stages are checkpointed, so a resume skips them.

| Stage | Action | Notes |
|---|---|---|
| **1 of 7** | Preflight checks | SSH reachability, passwordless sudo, kernel version, CPU, RAM, and disk minimums, BPF LSM, internet connectivity, Docker presence. |
| **2 of 7** | Docker install | Skipped if Docker is present. Installs it when `AUTO_INSTALL_DOCKER` is `1`. |
| **3 of 7** | knoxctl install | Installs the AccuKnox CLI if not already present. |
| **4 of 7** | Onboard host | Control plane runs the cp-node onboard and captures the worker join command. Workers run the node onboard with it. |
| **5 of 7** | Scanner install | Installs RRA and omni per `SCANNER_MODE`. |
| **6 of 7** | Connectivity check | Workers verify they reach the control plane on port 32770. |
| **7 of 7** | Agent verification | Confirms all required containers are running. |

On failure, a bundle is written to `reports/failed/<hostname>/` with system info, container logs, and a failure JSON. The host is marked failed in the run report and skipped on the next resume.

## 9. Deboarding

To remove AccuKnox from the fleet, run deboard. It tears down workers first, then the control plane.

```bash
./vm_onboarding.sh deboard
```

## 10. Quick Reference

```bash
# 1. host preparation on every host: Docker, kernel and BPF LSM, SSH keys, sudo

# 2. firewall (ufw): open 32768-32771 inbound on the control plane, allow egress if default policy denies

# 3. inventory on the control plane
vi inventory.csv        # hostname,ip,ssh_user,ssh_key_path,role,scan

# 4. tokens and label
export AK_JOIN_TOKEN="<join_token>"
export OMNI_ARTIFACT_API_TOKEN="<api_token>"

# 5. edit the config block in vm_onboarding.sh

# 6. run
./vm_onboarding.sh readiness
./vm_onboarding.sh onboard --dry-run
./vm_onboarding.sh onboard
./vm_onboarding.sh status
./vm_onboarding.sh onboard --resume
./vm_onboarding.sh deboard
```

## Related Help Docs

- [VM Onboarding with Docker](https://help.accuknox.com/how-to/vm-onboard-deboard-docker/)
- [VM Onboarding with Systemd](https://help.accuknox.com/how-to/vm-onboard-deboard-systemd/)
- [Create Tokens](https://help.accuknox.com/how-to/how-to-create-tokens/)
- [Create Labels](https://help.accuknox.com/how-to/how-to-create-labels/)
- [Host Vulnerability & Malware Scan](https://help.accuknox.com/use-cases/vm-host-scan/)
- [Malware Scan](https://help.accuknox.com/use-cases/vm-malware-scan/)
- [CIS Benchmarking](https://help.accuknox.com/how-to/cis-benchmarking/)
