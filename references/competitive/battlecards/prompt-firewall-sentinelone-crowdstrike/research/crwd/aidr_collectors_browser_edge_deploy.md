Scrape ID: 01a1361e-7efc-7687-a28d-59e2e9076be8
[Skip to main content](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#__docusaurus_skipToContent_fallback)

AI Detection and Response reaches end of support on November 30, 2026. AIDR capabilities continue in [Falcon Guardian](https://docs.crowdstrike.com/access?ft:originId=dt55byd3) with expanded AI security.

On this page

## Deploy Edge Collector v0.6.x [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#deploy-edge-collector "Direct link to Deploy Edge Collector v0.6.x")

note:

These instructions apply to the **Prompt Inspection Extension (0.6.x)**, distributed via Chrome Web Store.

This extension enables prompt inspection on supported AI sites.
It doesn't support

[Site Access](https://aidr-docs.crowdstrike.com/docs/aidr/policies/site-access) policy rules.

For **Site Access and Prompt Inspection Extension (1.x.x)**, see [Deploy 1.x.x](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy-v1).

Deploying a browser collector requires two steps:

- Install the browser extension.
- Save AIDR collector configuration in the extension's **Managed** storage.

### Managed storage [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#managed-storage "Direct link to Managed storage")

All deployment methods populate the browser extension's **Managed storage** with values required to connect to AIDR.

#### Configuration fields [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#configuration-fields "Direct link to Configuration fields")

- Required fields:


  - `registrationIdentity` \- Encoded credentials the extension uses to authenticate with the AIDR service and obtain an authorization token
  - `urlTemplate` \- AIDR API base URL

You can find collector-specific values for `registrationIdentity` and `urlTemplate` on the **Install** tab in the AIDR console.
Configuration files and templates on the **Install** tab include these values.

- Optional user identity fields that appear in AIDR event logs:
  - `userId` \- User identifier, such as an email address.
    Appears in AIDR logs and findings as a top-level field.
    If not provided, defaults to `user_<device-id>`.
  - `userFullName` \- User's display name.
    Appears in AIDR logs and findings under **Extra Info**.
    If not provided, defaults to `name_<device-id>`.
  - `hostname` \- Device hostname.
    Appears in AIDR logs and findings under **Extra Info**.
    If not configured, the value is empty.

#### System settings [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#system-paths "Direct link to System settings")

Jamf, Intune, Group Policy, and Self-Service apply extension configuration through OS-level settings: managed preference profiles on macOS or registry entries on Windows.

### Select extension version [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#select-extension-version "Direct link to Select extension version")

Choose the extension edition to deploy:

- **Prompt Inspection Extension (0.6.x)** \- Applies prompt inspection rules to supported AI sites. Does not support Site Access rules.

### Select distribution method [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#select-install-option "Direct link to Select distribution method")

On the collector details page in the AIDR console, switch to the **Install** tab.
This tab provides instructions, links, and templates for common deployment methods.
The following sections include step-by-step guides for specific methods.

- **Jamf** \- Enforce extension deployment and system-level settings on macOS with Apple-native Configuration Profiles.
- **Microsoft Intune** \- Deploy extensions and configuration profiles across Windows and macOS managed endpoints.
- [Group Policy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#group-policy) (Windows only) - Force-install the extension and configure managed storage via registry settings across domain-joined Windows endpoints.
- [Self-Service](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#self-service) \- Install the extension and apply a configuration profile on a single machine to quickly test the collector.

#### Group Policy (Windows) [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#group-policy "Direct link to Group Policy (Windows)")

Active Directory Group Policy lets you force-install the browser extension on domain-joined Windows endpoints and configure its managed storage through registry entries.

##### Requirements [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#requirements-gpo "Direct link to Requirements")

- Active Directory domain environment with Group Policy Management console (GPMC) installed.
- Permission to create, edit, and link Group Policy Objects (GPOs).
For example, membership in **Domain Admins** or **Group Policy Creator Owners**.
- Target computer and user accounts in Organizational Units (OUs) linked to the GPO.
Verify OU membership in Active Directory Users and Computers (`dsa.msc`).
- If you plan to force-install the extension through GPO, you need write access to the domain's SYSVOL share (`\\<domain>\SYSVOL\`) to install administrative templates.

##### Create or edit Group Policy Object [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#create-or-edit-group-policy-object-chrome-gpo "Direct link to Create or edit Group Policy Object")

1. Open **Group Policy Management** console (`gpmc.msc`).
2. Right-click your target OU and select **Create a GPO in this domain, and Link it here...**, or right-click an existing GPO and select **Edit...** to open **Group Policy Management Editor**.

##### Force-install extension [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#force-install-extension-chrome-gpo "Direct link to Force-install extension")

If the extension is already deployed through another method, such as Microsoft Intune, skip to [Configure computer-level registry settings](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#configure-computer-level-registry-settings-gpo).

###### Install administrative templates [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#install-administrative-templates-chrome-gpo "Direct link to Install administrative templates")

The Microsoft Edge administrative templates (ADMX/ADML files) aren't included with Windows. Check whether they're installed, and install them if needed.

1. In **Group Policy Management Editor**, go to **Computer Configuration** \> **Policies** \> **Administrative Templates**. If **Microsoft Edge** policy settings are already listed, skip to [Enable force-install policy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#enable-force-install-policy-chrome).
2. Go to [microsoft.com/edge/business/download](https://www.microsoft.com/en-us/edge/business/download) and click **Get policy files** \- not the main browser download.
3. Extract the downloaded `.cab` file:
1. Double-click the `.cab` file to open it in File Explorer. It contains a `.zip` archive.
2. Drag the `.zip` file to a convenient location, such as your Downloads folder.
3. Right-click the `.zip` file and select **Extract All...**.
4. Inside the extracted contents, locate the `windows\admx\` folder containing `.admx` files and language-specific subfolders, such as `en-US`, with `.adml` files.
5. Create the **Central Store** in SYSVOL. The Central Store is a `PolicyDefinitions` folder inside the domain's `Policies` folder. When this folder exists, GPMC reads administrative templates from the Central Store instead of the local machine. DFS Replication automatically copies the folder to all domain controllers. This folder doesn't exist by default - you must create it manually. Create `PolicyDefinitions\` and a subfolder for each language you need, such as `en-US\`:
   - `\\<domain>\SYSVOL\<domain>\Policies\PolicyDefinitions\`
   - `\\<domain>\SYSVOL\<domain>\Policies\PolicyDefinitions\en-US\`
6. Copy all `.admx` files to `PolicyDefinitions\` and the `.adml` files from each language subfolder to the matching subfolder under `PolicyDefinitions\`.
7. Close and reopen **Group Policy Management Editor** to load the new templates.

note:

If no Central Store exists in SYSVOL, GPMC reads templates from the local `C:\Windows\PolicyDefinitions\` folder on the machine running the console.
Every Windows installation includes this folder with built-in OS templates, but the contents aren't replicated to other domain controllers.
This approach works for single-admin environments and testing but isn't recommended for production.

###### Enable force-install policy [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#enable-force-install-policy-chrome "Direct link to Enable force-install policy")

1. In **Group Policy Management Editor**, go to: **Computer Configuration** \> **Policies** \> **Administrative Templates** \> **Microsoft Edge** \> **Extensions**.
2. Double-click **Control which extensions are installed silently**.
3. In the **Control which extensions are installed silently** dialog:
1. Click **Enabled**.
2. Click **Show...** under **Extension/App IDs and update URLs to be silently installed**.
3. In the **Show Contents** dialog, add the extension update URL:






      ```bash
      folndgmoekgkipoolphnkclopeopkecc;https://clients2.google.com/service/update2/crx
      ```

4. Click **OK** in the **Show Contents** dialog.
4. Click **OK** in the **Control which extensions are installed silently** dialog.

##### Configure computer-level registry settings [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#configure-computer-level-registry-settings-gpo "Direct link to Configure computer-level registry settings")

Add extension settings that apply to all users under **Computer Configuration**:

1. Go to **Computer Configuration** \> **Preferences** \> **Windows Settings** \> **Registry**.
2. Add AIDR base URL:
1. Right-click and select **New** \> **Registry Item**.
      Use these values in the **New Registry Properties** dialog:
      - **Action**: `Update`
      - **Hive**: `HKEY_LOCAL_MACHINE`
      - **Key Path**:






        ```bash
        SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc\policy
        ```

      - **Value name**:






        ```bash
        urlTemplate
        ```

      - **Value type**: `REG_SZ`
      - **Value data**: Copy the cloud-specific value from the collector's **Install** tab in the AIDR console.
        The AIDR base URL depends on your CrowdStrike cloud:


        - US-1





          ```bash
          https://api.crowdstrike.com/aidr/aiguard
          ```

        - US-2





          ```bash
          https://api.us-2.crowdstrike.com/aidr/aiguard
          ```

        - EU-1





          ```bash
          https://api.eu-1.crowdstrike.com/aidr/aiguard
          ```
2. Click **OK**.
3. Add collector credentials:
1. Right-click and select **New** \> **Registry Item**.
      Use these values in the **New Registry Properties** dialog:
      - **Action**: `Update`
      - **Hive**: `HKEY_LOCAL_MACHINE`
      - **Key Path**:






        ```bash
        SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc\policy
        ```

      - **Value name**:






        ```bash
        registrationIdentity
        ```

      - **Value type**: `REG_SZ`
      - **Value data**: Copy the value from the collector's **Install** tab in the AIDR console.
        The value is a base64-encoded string that looks like `eyJzIj...oxfQ==`.
2. Click **OK**.
4. Add device hostname:
1. Right-click and select **New** \> **Registry Item**.
      Use these values in the **New Registry Properties** dialog:
      - **Action**: `Update`
      - **Hive**: `HKEY_LOCAL_MACHINE`
      - **Key Path**:






        ```bash
        SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc\policy
        ```

      - **Value name**:






        ```bash
        hostname
        ```

      - **Value type**: `REG_SZ`
      - **Value data**:




        ```bash
        %COMPUTERNAME%
        ```
2. Click **OK**.

To edit a registry setting, right-click it and select **Properties**.

note:

- Group Policy Preferences expand variables, such as `%COMPUTERNAME%`, at processing time and write the target machine name to the registry as a static string. This differs from `REG_EXPAND_SZ`, where the OS expands variables each time the value is read.

Cleanup behavior:

GPO Registry Preferences don't remove registry entries when you delete the preference item from the GPO.
To enable automatic cleanup, click the **Common** tab of each registry item and select **Remove this item when it is no longer applied**.
Enable this setting before you apply the GPO to target machines.
If you didn't select this option before initial application, you must remove the registry entries manually or with a script.

##### Configure user-level registry settings [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#configure-user-level-registry-settings-chrome-gpo "Direct link to Configure user-level registry settings")

Because user-specific variables must resolve per user, add user identity settings under **User Configuration**.

note:

Windows processes **Computer Configuration** preferences during computer startup in the SYSTEM context, before any user logs in.
In that context, `%USERNAME%` resolves to the computer account name - for example, `WORKSTATION1$` \- not the logged-in user.

1. Go to **User Configuration** \> **Preferences** \> **Windows Settings** \> **Registry**.
2. Add user ID:
1. Right-click and select **New** \> **Registry Item**.
      Use these values in the **New Registry Properties** dialog:
      - **Action**: `Update`
      - **Hive**: `HKEY_CURRENT_USER`
      - **Key Path**:






        ```bash
        SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc\policy
        ```

      - **Value name**:






        ```bash
        userId
        ```

      - **Value type**: `REG_SZ`
      - **Value data**:






        ```bash
        %USERNAME%
        ```
2. Click **OK**.
3. Add user full name:
1. Right-click and select **New** \> **Registry Item**.
      Use these values in the **New Registry Properties** dialog:
      - **Action**: `Update`
      - **Hive**: `HKEY_CURRENT_USER`
      - **Key Path**:






        ```bash
        SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc\policy
        ```

      - **Value name**:






        ```bash
        userFullName
        ```

      - **Value type**: `REG_SZ`
      - **Value data**:






        ```bash
        %USERNAME%
        ```
2. Click **OK**.

To edit a registry setting, right-click it and select **Properties**.

note:

- Group Policy Preferences expand variables, such as `%USERNAME%`, at processing time and write the result to the registry as a static string.
This differs from `REG_EXPAND_SZ`, where the OS expands variables each time the value is read.

- `%USERNAME%` resolves to the Windows SAM account name, such as `jhammond`, not an email address or display name.

- Multi-domain environments

By default, `userId` is set to `%USERNAME%`.
In multi-domain environments, you can use `%USERDOMAIN%\%USERNAME%`, such as `INGENHQ\jhammond`, to distinguish users who share a SAM name across domains.


Cleanup behavior:

GPO Registry Preferences don't remove registry entries when you delete the preference item from the GPO.
To enable automatic cleanup, click the **Common** tab of each registry item and select **Remove this item when it is no longer applied**.
Enable this setting before you apply the GPO to target machines.
If you didn't select this option before initial application, you must remove the registry entries manually or with a script.

##### Link GPO and verify [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#link-gpo-and-verify-chrome-gpo "Direct link to Link GPO and verify")

1. Link the GPO to target OUs.

This GPO includes both **Computer Configuration** and **User Configuration** settings.
Both computer accounts and user accounts must be in OUs linked to the GPO.
If your computers and users are in different OUs, link the GPO to both, or to a parent OU that contains both.





note:





User accounts in the default `CN=Users` container don't receive **User Configuration** policies.
GPOs can't be linked to the default Users container.
Move user accounts to a proper OU.

2. On the **Scope** tab of the GPO, check the **Security Filtering** section.
By default, this section includes **Authenticated Users**, which covers all domain-joined accounts.
If your organization has narrowed filtering to a specific security group, confirm that target computer and user accounts are members.
Otherwise, no endpoints receive the policy.

3. Run `gpupdate /force` on a target machine and restart Microsoft Edge:





```bash
gpupdate /force
```

4. Verify the computer-level registry values:





```bash
reg query "HKLM\SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc\policy"
```









Confirm that `urlTemplate`, `registrationIdentity`, and `hostname` are present.

5. Verify the user-level registry values:





```bash
reg query "HKCU\SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc\policy"
```









Confirm that `userId` and `userFullName` are present with the logged-in user's name.

6. In Microsoft Edge on the target machine:
   - Go to `edge://extensions` and verify that the extension is installed.
     If you force-installed the extension through GPO, verify that users can't disable it.
   - Go to `edge://policy`.
     Confirm that the AIDR extension policy shows all five values with the correct per-user expansion.

Open the AIDR extension from the browser toolbar and verify its status.

After successful registration, the extension status progresses through **Configured** and **Ready** to **Active**.

To confirm that the extension connects to AIDR, see [Verify Deployment](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/verify).

#### Self-Service (testing) [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#self-service "Direct link to Self-Service (testing)")

The **Self-Service** option lets you quickly evaluate the collector on your own machine before deploying it at scale:

- Introduces the key browser collector deployment steps.
- Requires no management tools. Lets you perform both installation and configuration steps manually on your machine.
- Describes extension deployment parameters that also apply to production deployments.

Self-service limitations:

Self-service deployment is intended for testing and evaluation purposes.
It isn't a supported option for production deployments.

The first time you select this option, you must acknowledge these limitations in a confirmation dialog before proceeding.

##### Install and configure extension [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#install-and-configure-extension "Direct link to Install and configure extension")

1. Install the extension from the [Chrome Web Store](https://chromewebstore.google.com/detail/pangea-aidr/folndgmoekgkipoolphnkclopeopkecc).

2. Download and apply the configuration.
   - **macOS**

     Download the **configuration profile** from the collector's **Install** tab in the AIDR console.
     Example configuration profile (User scope)





     This profile populates the extension's managed storage with AIDR credentials.
     Apply at the **User** level (User Channel).







     ```xml
     <?xml version="1.0" encoding="UTF-8"?>
     <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
     <plist version="1.0">
     <dict>
       <key>PayloadContent</key>
       <array>
           <dict>
               <key>PayloadType</key>
               <string>com.microsoft.Edge.extensions.folndgmoekgkipoolphnkclopeopkecc</string>
               <key>PayloadIdentifier</key>
               <string>com.crowdstrike.aidr.edge.config</string>
               <key>PayloadUUID</key>
               <string>9b44c401-efdd-469e-bf88-ba0e29119034</string>
               <key>PayloadVersion</key>
               <integer>1</integer>
               <key>PayloadEnabled</key>
               <true/>
               <key>PayloadDisplayName</key>
               <string>AIDR Edge Extension Configuration</string>
               <key>urlTemplate</key>
               <string>https://api.crowdstrike.com/aidr/aiguard</string>
               <key>registrationIdentity</key>
               <string>eyJzIj...YiOjF9</string>
               <key>userId</key>
               <string>{{user-id}}</string>
               <key>userFullName</key>
               <string>{{user-full-name}}</string>
               <key>hostname</key>
               <string>replace-with-hostname</string>
           </dict>
       </array>
       <key>PayloadType</key>
       <string>Configuration</string>
       <key>PayloadIdentifier</key>
       <string>com.crowdstrike.aidr.edge.config.profile</string>
       <key>PayloadUUID</key>
       <string>5cfd4dcb-bdbf-4225-81ef-58bb76932c75</string>
       <key>PayloadVersion</key>
       <integer>1</integer>
       <key>PayloadScope</key>
       <string>User</string>
       <key>PayloadDisplayName</key>
       <string>AIDR Edge Extension Configuration Profile</string>
     </dict>
     </plist>
     ```














     Install the profile:


     1. Double-click the `.mobileconfig` file.
     2. Install in **System Settings** \> **General** \> **Device Management**.

note:

     - The exact path may vary depending on your macOS version.
     - If a previous profile for this extension exists, remove it first.

   - **Windows**

     Download the PowerShell script from the collector's **Install** tab in the AIDR console.
     Example PowerShell script





     This script creates the managed storage configuration in the Windows Registry.
     Run as **Administrator**.







     ```powershell
     # Edge AIDR Extension - Configuration
     $ErrorActionPreference = "Stop"

     $extensionId = "folndgmoekgkipoolphnkclopeopkecc"

     try {
         # --- Managed storage configuration ---
         $policyPath = "HKLM:\SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\$extensionId\policy"
         if (-not (Test-Path $policyPath)) {
             New-Item -Path $policyPath -Force | Out-Null
         }

         Set-ItemProperty -Path $policyPath -Name "registrationIdentity" `
             -Value "eyJzIj...YiOjF9" `
             -Type String -Force

         Set-ItemProperty -Path $policyPath -Name "urlTemplate" `
             -Value "https://api.crowdstrike.com/aidr/aiguard" `
             -Type String -Force

         # Use REG_EXPAND_SZ to expand %...% variables at read time
         # In multidomain environments, you can use %USERDOMAIN%\%USERNAME%
         New-ItemProperty -Path $policyPath -Name "userId" `
             -Value "%USERNAME%" -PropertyType ExpandString -Force | Out-Null

         New-ItemProperty -Path $policyPath -Name "userFullName" `
             -Value "%USERNAME%" -PropertyType ExpandString -Force | Out-Null

         New-ItemProperty -Path $policyPath -Name "hostname" `
             -Value "%COMPUTERNAME%" -PropertyType ExpandString -Force | Out-Null

         # Verify
         $config = Get-ItemProperty -Path $policyPath
         Write-Output "`nConfiguration applied successfully:"
         Write-Output "  - registrationIdentity: Set"
         Write-Output "  - urlTemplate: $($config.urlTemplate)"
         Write-Output "  - userId: $($config.userId)"
         Write-Output "  - userFullName: $($config.userFullName)"
         Write-Output "  - hostname: $($config.hostname)"

         Exit 0

     } catch {
         Write-Error "Failed: $($_.Exception.Message)"
         Exit 1
     }
     ```














     Run the script as **Administrator** to add the configuration to the Registry.







     warning:





     The script modifies only extension-specific key paths in the Windows Registry.
     As a precaution, back up the registry before running the script.
3. Restart the browser.

Fully close and restart your browser.
The extension connects to AIDR after the restart.


You can manage the extension on the `edge://extensions` page.

note:

The AIDR console pre-populates downloaded configuration files with values from the current session:

- `urlTemplate` \- The AIDR API URL for your CrowdStrike cloud.

- `registrationIdentity` \- Collector-specific credentials.

- `userId` and `userFullName` \- For macOS, the current AIDR console user's information.

If you distribute the configuration file to other users, update the `userId` and `userFullName` fields to match the target user's identity.

For Windows, the script uses environment variable expansion (`%USERNAME%`) to populate these fields automatically with the logged-in user's identity.

- `hostname` \- For macOS, populated with a placeholder value.
Replace it with the target machine's hostname.

For Windows, the script uses environment variable expansion (`%COMPUTERNAME%`) to populate this field automatically.


In production deployments, set these values dynamically per user with variables in your endpoint management tool or script.

##### Uninstall collector [​](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy\#uninstall-collector "Direct link to Uninstall collector")

When you're done testing, remove the browser extension and its configuration.

1. Remove the browser extension in your browser's extension manager.

2. Remove the system configuration:
   - **macOS** \- Remove the configuration profile in **System Settings** \> **General** \> **Device Management** \> **Profiles**.

     The exact path may vary depending on your macOS version.

   - **Windows** \- Remove the managed storage registry keys.





     warning:





     This modifies the Windows Registry.
     You can make a registry backup before proceeding.
     If you're unsure how to back up the Registry, contact your IT or system administrator.







     Run this command in a PowerShell session as **Administrator**:



     Remove extension configuration





     ```powershell
     Remove-Item -Path "HKLM:\SOFTWARE\Policies\Microsoft\Edge\3rdparty\extensions\folndgmoekgkipoolphnkclopeopkecc" -Recurse -ErrorAction SilentlyContinue
     ```









     Verify that no references to the extension remain:



     Verify extension removal





     ```powershell
     reg query "HKLM\SOFTWARE\Policies\Microsoft\Edge" /s /f "folndgmoekgkipoolphnkclopeopkecc"
     ```









     Expected output: `End of search: 0 match(es) found.`

- [Deploy Edge Collector v0.6.x](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#deploy-edge-collector)
  - [Managed storage](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#managed-storage)
    - [Configuration fields](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#configuration-fields)
    - [System settings](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#system-paths)
  - [Select extension version](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#select-extension-version)
  - [Select distribution method](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#select-install-option)
    - [Group Policy (Windows)](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#group-policy)
      - [Requirements](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#requirements-gpo)
      - [Create or edit Group Policy Object](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#create-or-edit-group-policy-object-chrome-gpo)
      - [Force-install extension](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#force-install-extension-chrome-gpo)
        - [Install administrative templates](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#install-administrative-templates-chrome-gpo)
        - [Enable force-install policy](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#enable-force-install-policy-chrome)
      - [Configure computer-level registry settings](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#configure-computer-level-registry-settings-gpo)
      - [Configure user-level registry settings](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#configure-user-level-registry-settings-chrome-gpo)
      - [Link GPO and verify](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#link-gpo-and-verify-chrome-gpo)
    - [Self-Service (testing)](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#self-service)
      - [Install and configure extension](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#install-and-configure-extension)
      - [Uninstall collector](https://aidr-docs.crowdstrike.com/docs/aidr/collectors/browser/edge/deploy#uninstall-collector)
