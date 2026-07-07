"""
CompTIA A+ Core 2 (220-1202) — Domain 1: Operating Systems
Study notes aligned to Professor Messer's 220-1202 Domain 1 playlist order.
"""

NOTES = [
    {
        "domain": 1,
        "topic": "Windows editions",
        "objective": "1.1",
        "video": "Windows Editions",
        "study_topics": ["Windows editions"],
        "body": (
            "<p>CompTIA A+ focuses on the currently supported consumer and business editions "
            "of Windows 10 and Windows 11. Understanding feature differences between editions "
            "is essential for exam success.</p>"
            "<p><strong>Windows 10 / 11 Home</strong> — Designed for consumers. Supports "
            "BitLocker on Pro and above only; lacks domain join, Group Policy editor (gpedit.msc), "
            "and Remote Desktop host capability.</p>"
            "<p><strong>Windows 10 / 11 Pro</strong> — Adds BitLocker drive encryption, "
            "domain join, Group Policy editor, Remote Desktop host, Hyper-V (64-bit), and "
            "Windows Sandbox.</p>"
            "<p><strong>Windows 10 / 11 Pro for Workstations</strong> — Supports ReFS file "
            "system, up to 6 TB RAM, Non-Uniform Memory Access (NUMA), and persistent memory.</p>"
            "<p><strong>Windows 10 / 11 Enterprise</strong> — Adds DirectAccess, AppLocker, "
            "BranchCache, Windows To Go (Win 10 only), Credential Guard, and Device Guard. "
            "Available via volume licensing only.</p>"
            "<ul>"
            "<li>Home: no BitLocker, no domain join, no gpedit.msc</li>"
            "<li>Pro: BitLocker, domain join, Hyper-V, Remote Desktop host</li>"
            "<li>Pro for Workstations: ReFS, &gt;2 TB RAM support (up to 6 TB)</li>"
            "<li>Enterprise: AppLocker, BranchCache, Credential Guard</li>"
            "<li>Windows 11 minimum: 1 GHz dual-core 64-bit CPU, 4 GB RAM, 64 GB storage, "
            "TPM 2.0, UEFI Secure Boot, DirectX 12</li>"
            "</ul>"
        ),
        "key_points": [
            "Home edition lacks BitLocker, domain join, and Group Policy editor",
            "Pro adds BitLocker, domain join, Hyper-V, and Remote Desktop host",
            "Enterprise adds AppLocker, BranchCache, Credential Guard (volume license only)",
            "Windows 11 requires TPM 2.0 and UEFI Secure Boot",
            "Pro for Workstations supports ReFS and up to 6 TB RAM",
        ],
    },
    {
        "domain": 1,
        "topic": "Windows command-line tools",
        "objective": "1.2",
        "video": "Windows Command Line Tools",
        "study_topics": ["Windows command-line tools"],
        "body": (
            "<p>The Windows command-line environment (cmd.exe and PowerShell) provides powerful "
            "tools for system administration and troubleshooting. The A+ exam tests both syntax "
            "and appropriate use of these utilities.</p>"
            "<table>"
            "<tr><th>Command</th><th>Purpose</th><th>Key Flags / Notes</th></tr>"
            "<tr><td><code>ipconfig</code></td><td>Display IP configuration</td>"
            "<td><code>/all</code> (MAC, DHCP, DNS), <code>/release</code>, "
            "<code>/renew</code>, <code>/flushdns</code></td></tr>"
            "<tr><td><code>ping</code></td><td>Test ICMP connectivity</td>"
            "<td><code>-t</code> continuous, <code>-n &lt;count&gt;</code></td></tr>"
            "<tr><td><code>nslookup</code></td><td>DNS name resolution queries</td>"
            "<td>Interactive mode or single query; test forward/reverse lookup</td></tr>"
            "<tr><td><code>sfc</code></td><td>System File Checker — repair OS files</td>"
            "<td><code>/scannow</code> scans and repairs; run as admin</td></tr>"
            "<tr><td><code>chkdsk</code></td><td>Check disk for errors and bad sectors</td>"
            "<td><code>/f</code> fix errors, <code>/r</code> locate bad sectors (implies /f)</td></tr>"
            "<tr><td><code>diskpart</code></td><td>Disk partitioning utility</td>"
            "<td>Interactive; commands: <code>list disk</code>, <code>select</code>, "
            "<code>create partition</code>, <code>format</code>, <code>active</code></td></tr>"
            "<tr><td><code>format</code></td><td>Format a volume with a file system</td>"
            "<td><code>/fs:ntfs</code>, <code>/q</code> quick format</td></tr>"
            "<tr><td><code>robocopy</code></td><td>Robust file copy with mirroring</td>"
            "<td><code>/mir</code> mirror, <code>/z</code> restartable, "
            "<code>/log</code> output to file</td></tr>"
            "<tr><td><code>gpupdate</code></td><td>Force Group Policy refresh</td>"
            "<td><code>/force</code> reapplies all policies; <code>/boot</code> restarts</td></tr>"
            "<tr><td><code>gpresult</code></td><td>Show applied Group Policy results</td>"
            "<td><code>/r</code> summary, <code>/h report.html</code> HTML report</td></tr>"
            "</table>"
            "<p><strong>Additional tools:</strong> <code>netstat</code> (active connections), "
            "<code>tracert</code> (route hops), <code>pathping</code> (combines ping/tracert), "
            "<code>net use</code> (map drives), <code>tasklist</code> / <code>taskkill</code>.</p>"
        ),
        "key_points": [
            "sfc /scannow repairs corrupted Windows system files (run as admin)",
            "chkdsk /r locates bad sectors and recovers readable data (implies /f)",
            "diskpart is the interactive command-line disk management tool",
            "ipconfig /flushdns clears the local DNS resolver cache",
            "gpupdate /force reapplies all Group Policy settings immediately",
            "robocopy /mir mirrors a directory tree including deletions",
        ],
    },
    {
        "domain": 1,
        "topic": "Windows administrative tools (MMC snap-ins)",
        "objective": "1.2",
        "video": "Windows Administrative Tools",
        "study_topics": ["Windows administrative tools (MMC snap-ins)"],
        "body": (
            "<p>The Microsoft Management Console (MMC) hosts snap-ins that administrators use "
            "to manage Windows systems. Many built-in tools are pre-configured MMC snap-ins "
            "accessible from Administrative Tools (Control Panel) or by typing their executable "
            "name in Run (<strong>Win+R</strong>).</p>"
            "<ul>"
            "<li><strong>Computer Management (compmgmt.msc)</strong> — Umbrella console: "
            "Event Viewer, Device Manager, Disk Management, Services, Shared Folders, "
            "Local Users and Groups, Task Scheduler, Performance.</li>"
            "<li><strong>Device Manager (devmgmt.msc)</strong> — View/update drivers, "
            "disable hardware, view resource conflicts. Yellow <code>!</code> = driver problem.</li>"
            "<li><strong>Disk Management (diskmgmt.msc)</strong> — Create/delete/format volumes, "
            "change drive letters, convert basic to dynamic disk.</li>"
            "<li><strong>Event Viewer (eventvwr.msc)</strong> — Windows Logs: Application, "
            "Security, System; custom views. Error/Warning/Information levels.</li>"
            "<li><strong>Local Security Policy (secpol.msc)</strong> — Account policies, "
            "audit policies, user rights. Available on Pro and above.</li>"
            "<li><strong>Group Policy Editor (gpedit.msc)</strong> — Pro and above only; "
            "Computer/User configuration, Software/Windows/Administrative Templates.</li>"
            "<li><strong>Services (services.msc)</strong> — Start/stop/disable services, "
            "set recovery options and startup type (Automatic, Manual, Disabled).</li>"
            "<li><strong>Task Scheduler (taskschd.msc)</strong> — Create scheduled tasks "
            "triggered by time, event, logon, or startup.</li>"
            "<li><strong>Certificate Manager (certmgr.msc / certlm.msc)</strong> — Manage "
            "user or computer certificate stores.</li>"
            "<li><strong>Performance Monitor (perfmon.msc)</strong> — Real-time counters "
            "and Data Collector Sets for baselining.</li>"
            "</ul>"
            "<p>Custom MMC consoles can be built by opening <code>mmc.exe</code> and adding "
            "snap-ins via File &gt; Add/Remove Snap-in.</p>"
        ),
        "key_points": [
            "compmgmt.msc is an umbrella console combining many snap-ins",
            "devmgmt.msc — yellow ! indicates a driver problem",
            "diskmgmt.msc manages volumes, drive letters, and disk types",
            "eventvwr.msc — Application, Security, and System logs are the core Windows logs",
            "gpedit.msc (Group Policy Editor) is only available on Pro and above",
            "services.msc sets startup type: Automatic, Manual, or Disabled",
        ],
    },
    {
        "domain": 1,
        "topic": "Control Panel utilities",
        "objective": "1.2",
        "video": "Control Panel Utilities",
        "study_topics": ["Control Panel utilities"],
        "body": (
            "<p>Control Panel remains a key location for system configuration in Windows 10/11, "
            "even as Microsoft migrates settings to the Settings app. The A+ exam tests "
            "knowledge of specific applets and their functions.</p>"
            "<ul>"
            "<li><strong>System (sysdm.cpl)</strong> — Computer name, domain/workgroup, "
            "hardware, Remote Desktop, System Protection (restore points), Advanced "
            "(virtual memory, performance options, environment variables).</li>"
            "<li><strong>Device Manager</strong> — Also accessible from System applet; "
            "view hardware and update/rollback drivers.</li>"
            "<li><strong>Programs and Features</strong> — Uninstall or change programs; "
            "Turn Windows features on/off (IIS, Hyper-V, Telnet client, etc.).</li>"
            "<li><strong>Network and Sharing Center</strong> — View network status, "
            "set up connections, change adapter settings, HomeGroup (legacy), "
            "advanced sharing settings.</li>"
            "<li><strong>Internet Options (inetcpl.cpl)</strong> — IE/legacy Edge settings: "
            "security zones, privacy, trusted sites, connections, advanced.</li>"
            "<li><strong>User Accounts</strong> — Manage local accounts, passwords, "
            "Credential Manager, UAC settings.</li>"
            "<li><strong>Windows Firewall (wf.msc / firewall.cpl)</strong> — Allow apps "
            "through firewall, advanced rules via Windows Defender Firewall with "
            "Advanced Security.</li>"
            "<li><strong>BitLocker Drive Encryption</strong> — Enable/manage BitLocker; "
            "requires Pro/Enterprise and TPM (or USB key).</li>"
            "<li><strong>Indexing Options</strong> — Control which folders are indexed "
            "for Windows Search.</li>"
            "<li><strong>Power Options (powercfg.cpl)</strong> — Balanced, Power Saver, "
            "High Performance plans; sleep/hibernate/hybrid sleep settings.</li>"
            "<li><strong>Display / Screen Resolution</strong> — Resolution, refresh rate, "
            "multiple monitors, scaling (DPI).</li>"
            "</ul>"
        ),
        "key_points": [
            "sysdm.cpl — System Properties: computer name, Remote Desktop, restore points, virtual memory",
            "Programs and Features — uninstall apps and toggle Windows features (IIS, Hyper-V, Telnet)",
            "Network and Sharing Center — change adapter settings, set network profile",
            "inetcpl.cpl — Internet Options: security zones, trusted sites, proxy settings",
            "wf.msc — Windows Defender Firewall with Advanced Security for inbound/outbound rules",
            "powercfg.cpl — power plans and sleep/hibernate configuration",
        ],
    },
    {
        "domain": 1,
        "topic": "Windows Settings",
        "objective": "1.2",
        "video": "Windows Settings",
        "study_topics": ["Windows Settings"],
        "body": (
            "<p>The Settings app (Win+I) is the modern configuration hub in Windows 10/11 and "
            "is gradually replacing Control Panel. The A+ exam covers key settings categories "
            "and what can be configured in each.</p>"
            "<ul>"
            "<li><strong>System</strong> — Display (resolution, night light, HDR), Sound, "
            "Notifications, Focus Assist, Power &amp; sleep, Storage Sense, Remote Desktop, "
            "Clipboard history, Projecting to this PC.</li>"
            "<li><strong>Bluetooth &amp; devices</strong> — Pair Bluetooth, manage USB/printers, "
            "touchpad settings, AutoPlay.</li>"
            "<li><strong>Network &amp; Internet</strong> — Wi-Fi, Ethernet, VPN, "
            "Mobile hotspot, Airplane mode, Proxy settings, Dial-up.</li>"
            "<li><strong>Personalization</strong> — Background, Colors (light/dark mode), "
            "Lock screen, Themes, Fonts, Start menu, Taskbar.</li>"
            "<li><strong>Apps</strong> — Apps &amp; features (uninstall), Default apps, "
            "Optional features, Startup apps.</li>"
            "<li><strong>Accounts</strong> — Your info (Microsoft vs. local account), "
            "Email &amp; accounts, Sign-in options (PIN, Windows Hello, picture password), "
            "Family &amp; other users, Access work or school.</li>"
            "<li><strong>Time &amp; Language</strong> — Date/time (NTP sync), Region, "
            "Language packs, Speech.</li>"
            "<li><strong>Gaming</strong> — Xbox Game Bar, Captures, Game Mode.</li>"
            "<li><strong>Privacy &amp; security</strong> — App permissions (camera, mic, "
            "location), Windows Security dashboard, Find My Device, "
            "Windows permissions (diagnostics, activity history).</li>"
            "<li><strong>Windows Update</strong> — Check for updates, pause updates, "
            "update history, delivery optimization (P2P), advanced options.</li>"
            "</ul>"
            "<p><strong>Windows 11 change:</strong> Settings is reorganized into a single-pane "
            "layout with a left navigation panel, making navigation more consistent.</p>"
        ),
        "key_points": [
            "Win+I opens the Settings app in Windows 10 and 11",
            "Accounts > Sign-in options — configure PIN, Windows Hello face/fingerprint, picture password",
            "Windows Update > Advanced options — pause updates and delivery optimization",
            "Apps > Startup — control which apps launch at boot (replaces Task Manager Startup tab path)",
            "Privacy & security — manage per-app permissions for camera, microphone, and location",
            "Network & Internet — VPN configuration, proxy settings, mobile hotspot",
        ],
    },
    {
        "domain": 1,
        "topic": "Windows networking (workgroup/domain)",
        "objective": "1.3",
        "video": "Windows Network Settings",
        "study_topics": ["Windows networking (workgroup/domain)"],
        "body": (
            "<p>Windows supports two primary network models: workgroups (peer-to-peer) and "
            "domains (client-server). Understanding the differences is critical for A+ Core 2.</p>"
            "<p><strong>Workgroup (Peer-to-Peer)</strong></p>"
            "<ul>"
            "<li>Each computer maintains its own local user accounts and security database.</li>"
            "<li>No central authentication — credentials are managed on each machine.</li>"
            "<li>Suitable for small networks (typically &lt;10 devices).</li>"
            "<li>All workgroup PCs must be on the same subnet or reachable via broadcasting.</li>"
            "<li>Default workgroup name: <code>WORKGROUP</code>.</li>"
            "</ul>"
            "<p><strong>Domain (Client-Server)</strong></p>"
            "<ul>"
            "<li>Centralized authentication via Active Directory Domain Services (AD DS) "
            "running on a Domain Controller (DC).</li>"
            "<li>Users log in with domain credentials valid on any domain-joined computer.</li>"
            "<li>Group Policy applied from DC to all members.</li>"
            "<li>Requires Windows Pro, Pro for Workstations, or Enterprise to join a domain.</li>"
            "<li>DNS is required — clients must resolve the domain controller's name.</li>"
            "</ul>"
            "<p><strong>Key networking settings:</strong></p>"
            "<ul>"
            "<li>Change domain/workgroup: System Properties &gt; Computer Name tab &gt; Change.</li>"
            "<li>Network profile: Domain, Private, or Public (affects firewall rules and discovery).</li>"
            "<li>Shared resources: <code>\\\\computername\\sharename</code> UNC path.</li>"
            "<li><code>net use Z: \\\\server\\share</code> — map a network drive from CLI.</li>"
            "<li>HomeGroup — deprecated in Windows 10 (1803+); use workgroup sharing instead.</li>"
            "</ul>"
        ),
        "key_points": [
            "Workgroup: decentralized, each PC manages its own accounts, best for <10 devices",
            "Domain: centralized AD DS authentication, Group Policy, requires Pro/Enterprise",
            "Domain join requires DNS resolution of the Domain Controller",
            "UNC path format: \\\\server\\share — used to access shared network resources",
            "Network profiles (Domain/Private/Public) control firewall discovery rules",
            "HomeGroup is deprecated in Windows 10 version 1803 and later",
        ],
    },
    {
        "domain": 1,
        "topic": "Application installation requirements",
        "objective": "1.4",
        "video": "Application Installation",
        "study_topics": ["Application installation requirements"],
        "body": (
            "<p>Before installing software, a technician must verify that the system meets "
            "hardware, OS, and security requirements. The A+ exam tests both the requirements "
            "themselves and the installation process.</p>"
            "<p><strong>System Requirements to Check</strong></p>"
            "<ul>"
            "<li><strong>CPU speed and architecture</strong> — 32-bit (x86) vs. 64-bit (x64); "
            "64-bit OS can run 32-bit apps (via WOW64) but not vice versa.</li>"
            "<li><strong>RAM</strong> — minimum vs. recommended; insufficient RAM causes "
            "sluggish performance or installation failure.</li>"
            "<li><strong>Storage space</strong> — check free disk space; installations may "
            "require 2–3× the installed size for temporary extraction files.</li>"
            "<li><strong>OS compatibility</strong> — specific Windows version required "
            "(e.g., requires Windows 10 64-bit or later).</li>"
            "<li><strong>Graphics / DirectX version</strong> — especially for games and "
            "media applications.</li>"
            "<li><strong>Network connectivity</strong> — some installers download components "
            "during setup (online vs. offline installer).</li>"
            "</ul>"
            "<p><strong>Security and Account Requirements</strong></p>"
            "<ul>"
            "<li>Local admin rights typically required for system-wide installation.</li>"
            "<li>UAC prompt — standard users must supply admin credentials.</li>"
            "<li>Impact on device/network: malware risk, licensing compliance, "
            "bandwidth usage, and compatibility conflicts.</li>"
            "</ul>"
            "<p><strong>Installation methods:</strong> Automated/silent install "
            "(<code>/quiet</code>, <code>/s</code> flags), MSI via Group Policy "
            "(Software Installation), application virtualization (App-V), and "
            "side-loading (Android apps on Windows 11 via Amazon Appstore).</p>"
        ),
        "key_points": [
            "64-bit OS can run 32-bit apps (WOW64); 32-bit OS cannot run 64-bit apps",
            "Check CPU architecture, RAM, free disk space, and OS version before installing",
            "Local administrator rights are typically required for system-wide installation",
            "UAC prompts standard users to supply admin credentials during installation",
            "Silent/unattended install uses /quiet or /s flags for scripted deployments",
            "Online installers download components at runtime; offline installers are self-contained",
        ],
    },
    {
        "domain": 1,
        "topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "objective": "1.5",
        "video": "File Systems",
        "study_topics": ["File systems (NTFS/FAT32/exFAT/APFS/ext4)"],
        "body": (
            "<p>File systems define how data is stored, organized, and accessed on a volume. "
            "The A+ exam tests key attributes of each file system including size limits, "
            "journaling, and encryption support.</p>"
            "<table>"
            "<tr><th>File System</th><th>Max File Size</th><th>Max Volume Size</th>"
            "<th>Journaling</th><th>Encryption</th><th>Use Case</th></tr>"
            "<tr><td><strong>NTFS</strong></td><td>~16 TB (practical)</td>"
            "<td>~256 TB (practical)</td><td>Yes</td>"
            "<td>EFS, BitLocker</td><td>Windows OS/data drives</td></tr>"
            "<tr><td><strong>FAT32</strong></td><td><strong>4 GB</strong></td>"
            "<td>2 TB (32 GB in Windows format tool)</td><td>No</td>"
            "<td>No</td><td>USB drives, legacy devices</td></tr>"
            "<tr><td><strong>exFAT</strong></td><td>16 EB (effectively unlimited)</td>"
            "<td>128 PB</td><td>No</td><td>No</td>"
            "<td>Flash drives, SD cards, cross-platform</td></tr>"
            "<tr><td><strong>APFS</strong></td><td>8 EB</td><td>8 EB</td>"
            "<td>Yes (copy-on-write)</td><td>Yes (native)</td>"
            "<td>macOS 10.13+, iOS, SSD-optimized</td></tr>"
            "<tr><td><strong>ext4</strong></td><td>16 TB</td><td>1 EB</td>"
            "<td>Yes</td><td>Via dm-crypt / LUKS</td>"
            "<td>Linux default file system</td></tr>"
            "</table>"
            "<ul>"
            "<li><strong>NTFS</strong>: Supports permissions (ACLs), compression, encryption "
            "(EFS), hard links, shadow copies, and alternate data streams. Required for "
            "Windows OS installations.</li>"
            "<li><strong>FAT32</strong>: 4 GB per-file limit is the most tested A+ fact. "
            "Windows format tool limits volumes to 32 GB; third-party tools go up to 2 TB.</li>"
            "<li><strong>exFAT</strong>: Designed to replace FAT32 for flash media; "
            "no journaling but no file-size limitation. Cross-platform (Windows, macOS, Linux).</li>"
            "<li><strong>APFS</strong>: Apple File System; copy-on-write journaling, "
            "native encryption, space sharing between containers, optimized for SSDs.</li>"
            "<li><strong>ext4</strong>: Fourth extended filesystem; delayed allocation, "
            "extents, journal checksumming; default on most Linux distros.</li>"
            "</ul>"
        ),
        "key_points": [
            "FAT32 maximum individual file size is 4 GB — most tested file system fact on A+",
            "NTFS supports ACL permissions, EFS encryption, compression, and shadow copies",
            "exFAT replaces FAT32 for flash media with no practical file size limit",
            "APFS is copy-on-write, natively encrypted, and SSD-optimized for macOS/iOS",
            "ext4 is the default Linux file system with journaling and extents support",
            "Only NTFS is supported for Windows OS drive installations",
        ],
    },
    {
        "domain": 1,
        "topic": "OS installation & upgrade methods",
        "objective": "1.6",
        "video": "OS Installation and Upgrade Methods",
        "study_topics": ["OS installation & upgrade methods"],
        "body": (
            "<p>The A+ exam tests both the types of OS installations and the various methods "
            "used to deploy them in home and enterprise environments.</p>"
            "<p><strong>Installation Types</strong></p>"
            "<ul>"
            "<li><strong>Clean install</strong> — Format the drive and install a fresh OS. "
            "All existing data and settings are lost. Preferred when upgrading hardware "
            "or resolving deep OS corruption.</li>"
            "<li><strong>Upgrade install (in-place upgrade)</strong> — Installs new OS "
            "version over existing one, preserving apps, files, and settings. "
            "Windows 10 → 11 supports in-place upgrade on compatible hardware.</li>"
            "<li><strong>Repair install / Upgrade repair</strong> — Re-installs OS files "
            "while keeping user data and apps; fixes corrupted system files.</li>"
            "<li><strong>Multiboot / Dual-boot</strong> — Multiple OSes on same machine; "
            "install each to a separate partition. Boot manager (BCD) handles selection.</li>"
            "<li><strong>Unattended / Automated</strong> — Uses answer file "
            "(<code>unattend.xml</code> / <code>autounattend.xml</code>) to automate "
            "installation prompts. Used with Windows Deployment Services (WDS) or SCCM.</li>"
            "<li><strong>Image-based / WIM deployment</strong> — Capture a configured system "
            "image (WIM file) and deploy to multiple machines using DISM or WDS.</li>"
            "<li><strong>PXE boot (network boot)</strong> — Boot from NIC; WDS server "
            "delivers OS image over the network. Requires DHCP and TFTP.</li>"
            "<li><strong>USB / optical media</strong> — Bootable USB (Rufus, Media "
            "Creation Tool) or DVD used for standalone installs.</li>"
            "</ul>"
            "<p><strong>Post-installation tasks:</strong> Activate Windows, install drivers "
            "(chipset first), apply Windows Updates, install applications, configure "
            "user accounts, and verify backup/restore points.</p>"
        ),
        "key_points": [
            "Clean install wipes all data; upgrade/in-place preserves apps, files, and settings",
            "unattend.xml / autounattend.xml automate Windows Setup prompts for unattended installs",
            "PXE boot requires DHCP, TFTP, and a WDS server to deliver OS images over the network",
            "Image-based deployment uses WIM files captured with DISM and deployed to multiple PCs",
            "Repair install re-installs OS files while keeping user data and installed applications",
            "Post-install: activate Windows, install chipset drivers, then apply Windows Updates",
        ],
    },
    {
        "domain": 1,
        "topic": "Partitioning (GPT vs MBR)",
        "objective": "1.5",
        "video": "Partitioning",
        "study_topics": ["Partitioning (GPT vs MBR)"],
        "body": (
            "<p>Partition tables define how disk space is divided into sections (partitions). "
            "The A+ exam contrasts MBR and GPT partition styles, their limitations, "
            "and their relationship to firmware (BIOS vs. UEFI).</p>"
            "<p><strong>MBR (Master Boot Record)</strong></p>"
            "<ul>"
            "<li>Located in the first 512-byte sector of the disk.</li>"
            "<li>Maximum disk size: <strong>2 TB</strong> (32-bit LBA addressing).</li>"
            "<li>Maximum <strong>4 primary partitions</strong>; workaround: convert one to "
            "an extended partition containing logical drives.</li>"
            "<li>Compatible with legacy BIOS (CSM) systems.</li>"
            "<li>Boot code stored in MBR itself — single point of failure.</li>"
            "</ul>"
            "<p><strong>GPT (GUID Partition Table)</strong></p>"
            "<ul>"
            "<li>Part of the UEFI specification; uses 64-bit LBA addressing.</li>"
            "<li>Maximum disk size: <strong>~9.4 ZB</strong> (theoretically); practically "
            "limited by OS and hardware.</li>"
            "<li>Supports up to <strong>128 partitions</strong> on Windows (no extended "
            "partition needed).</li>"
            "<li>Contains a protective MBR for backward compatibility.</li>"
            "<li>Redundant partition table stored at both the start and end of the disk.</li>"
            "<li>Each partition identified by a globally unique identifier (GUID).</li>"
            "<li>Required for booting Windows on UEFI systems with Secure Boot.</li>"
            "</ul>"
            "<p><strong>Key partition types (GPT/Windows):</strong> EFI System Partition "
            "(ESP, FAT32, ~100 MB), Microsoft Reserved Partition (MSR, ~16 MB), "
            "Windows OS partition (NTFS), Recovery partition (WinRE).</p>"
            "<p>Convert MBR to GPT without data loss using <code>mbr2gpt.exe /convert</code> "
            "(Windows 10+) or the <code>diskpart</code> <code>convert gpt</code> command "
            "(destroys data).</p>"
        ),
        "key_points": [
            "MBR: max 2 TB disk, max 4 primary partitions, compatible with legacy BIOS",
            "GPT: supports disks >2 TB, up to 128 partitions on Windows, requires UEFI",
            "GPT stores redundant partition tables at both ends of the disk for fault tolerance",
            "EFI System Partition (ESP) is a FAT32 partition required for UEFI booting",
            "mbr2gpt.exe /convert migrates MBR to GPT without data loss on Windows 10+",
            "GPT required for Windows Secure Boot; BIOS systems use MBR",
        ],
    },
    {
        "domain": 1,
        "topic": "macOS features & tools",
        "objective": "1.7",
        "video": "macOS Features and Tools",
        "study_topics": ["macOS features & tools"],
        "body": (
            "<p>The A+ Core 2 exam tests macOS features, built-in utilities, and system "
            "preferences relevant to end-user support scenarios.</p>"
            "<p><strong>Key macOS Features</strong></p>"
            "<ul>"
            "<li><strong>Finder</strong> — File manager; Go &gt; Connect to Server "
            "(<code>smb://</code>) to access network shares.</li>"
            "<li><strong>Spotlight (Cmd+Space)</strong> — System-wide search for files, "
            "apps, and web results.</li>"
            "<li><strong>Mission Control (F3 / Ctrl+Up)</strong> — View all open windows "
            "and virtual desktops (Spaces).</li>"
            "<li><strong>Time Machine</strong> — Automated local and external drive backup; "
            "hourly snapshots, daily for 1 month, weekly for all previous months.</li>"
            "<li><strong>FileVault</strong> — Full-disk encryption using XTS-AES-128 "
            "(Intel) or APFS encryption (Apple Silicon). Recovery key or iCloud "
            "account for unlocking.</li>"
            "<li><strong>Gatekeeper</strong> — Restricts app installation to App Store "
            "and/or identified developers; prevents unauthorized software.</li>"
            "<li><strong>iCloud</strong> — Cloud storage and sync for documents, photos, "
            "keychain, and device backups.</li>"
            "<li><strong>AirDrop</strong> — Peer-to-peer file sharing over Wi-Fi and "
            "Bluetooth (no internet required).</li>"
            "</ul>"
            "<p><strong>Key Utilities</strong></p>"
            "<ul>"
            "<li><strong>System Preferences / System Settings</strong> (macOS Ventura+) "
            "— Central configuration for display, network, users, security.</li>"
            "<li><strong>Disk Utility</strong> — Format drives (APFS, HFS+, ExFAT), "
            "First Aid (fsck), RAID, partitioning.</li>"
            "<li><strong>Activity Monitor</strong> — CPU, memory, energy, disk, network "
            "usage; force-quit processes.</li>"
            "<li><strong>Terminal</strong> — Unix shell (zsh default since macOS Catalina); "
            "access to command-line tools.</li>"
            "<li><strong>Keychain Access</strong> — Stores passwords, certificates, and "
            "secure notes.</li>"
            "</ul>"
        ),
        "key_points": [
            "Time Machine performs hourly/daily/weekly backups and supports local snapshots",
            "FileVault provides full-disk encryption using APFS encryption on Apple Silicon",
            "Gatekeeper restricts installs to App Store and/or identified developers",
            "Disk Utility — format drives, run First Aid (fsck), manage RAID/partitions",
            "Activity Monitor is the macOS equivalent of Windows Task Manager",
            "Spotlight (Cmd+Space) provides system-wide search across files, apps, and web",
        ],
    },
    {
        "domain": 1,
        "topic": "Linux commands",
        "objective": "1.8",
        "video": "Linux Commands",
        "study_topics": ["Linux commands"],
        "body": (
            "<p>The A+ Core 2 exam expects familiarity with common Linux shell commands "
            "used for file management, process control, networking, and system information. "
            "Most distributions use bash or zsh as the default shell.</p>"
            "<table>"
            "<tr><th>Command</th><th>Purpose</th><th>Example</th></tr>"
            "<tr><td><code>ls</code></td><td>List directory contents</td>"
            "<td><code>ls -la</code> (long + hidden)</td></tr>"
            "<tr><td><code>cd</code></td><td>Change directory</td>"
            "<td><code>cd /home/user</code></td></tr>"
            "<tr><td><code>pwd</code></td><td>Print working directory</td>"
            "<td><code>pwd</code></td></tr>"
            "<tr><td><code>cp</code></td><td>Copy files/directories</td>"
            "<td><code>cp -r src/ dest/</code></td></tr>"
            "<tr><td><code>mv</code></td><td>Move or rename files</td>"
            "<td><code>mv old.txt new.txt</code></td></tr>"
            "<tr><td><code>rm</code></td><td>Remove files/directories</td>"
            "<td><code>rm -rf dir/</code> (recursive, force)</td></tr>"
            "<tr><td><code>mkdir</code></td><td>Make directory</td>"
            "<td><code>mkdir -p path/to/dir</code></td></tr>"
            "<tr><td><code>grep</code></td><td>Search text patterns</td>"
            "<td><code>grep -r 'error' /var/log/</code></td></tr>"
            "<tr><td><code>find</code></td><td>Find files by criteria</td>"
            "<td><code>find / -name '*.conf'</code></td></tr>"
            "<tr><td><code>ps</code></td><td>List processes</td>"
            "<td><code>ps aux</code></td></tr>"
            "<tr><td><code>top</code></td><td>Real-time process monitor</td>"
            "<td><code>top</code> (<code>q</code> to quit)</td></tr>"
            "<tr><td><code>kill</code></td><td>Send signal to process</td>"
            "<td><code>kill -9 PID</code> (force kill)</td></tr>"
            "<tr><td><code>sudo</code></td><td>Run command as superuser</td>"
            "<td><code>sudo apt update</code></td></tr>"
            "<tr><td><code>apt / yum / dnf</code></td><td>Package manager</td>"
            "<td><code>sudo apt install nginx</code></td></tr>"
            "<tr><td><code>ifconfig / ip addr</code></td><td>Network interface info</td>"
            "<td><code>ip addr show</code></td></tr>"
            "<tr><td><code>df</code></td><td>Disk free space</td>"
            "<td><code>df -h</code> (human-readable)</td></tr>"
            "<tr><td><code>du</code></td><td>Disk usage of files/dirs</td>"
            "<td><code>du -sh /var/</code></td></tr>"
            "<tr><td><code>man</code></td><td>Manual pages</td>"
            "<td><code>man ls</code></td></tr>"
            "</table>"
            "<p><strong>Piping and redirection:</strong> <code>|</code> pipes output, "
            "<code>&gt;</code> redirects to file (overwrite), <code>&gt;&gt;</code> appends. "
            "Example: <code>ps aux | grep nginx</code></p>"
        ),
        "key_points": [
            "ls -la shows all files (including hidden dot-files) in long format",
            "rm -rf removes directories recursively and forcefully — use with caution",
            "sudo elevates privileges for a single command without switching to root shell",
            "ps aux lists all running processes with user, PID, CPU, and memory usage",
            "grep -r searches recursively through directories for a pattern",
            "df -h and du -sh provide disk usage in human-readable format",
            "| (pipe) chains commands; > overwrites file output; >> appends to file",
        ],
    },
    {
        "domain": 1,
        "topic": "Linux file permissions",
        "objective": "1.8",
        "video": "Linux File Permissions",
        "study_topics": ["Linux file permissions"],
        "body": (
            "<p>Linux uses a discretionary access control (DAC) model with three permission "
            "types and three ownership categories applied to every file and directory.</p>"
            "<p><strong>Permission Types (rwx)</strong></p>"
            "<ul>"
            "<li><strong>r (read, 4)</strong> — File: view contents. Directory: list contents.</li>"
            "<li><strong>w (write, 2)</strong> — File: modify/delete. Directory: create/delete "
            "files within it.</li>"
            "<li><strong>x (execute, 1)</strong> — File: run as program. Directory: "
            "traverse (cd into) the directory.</li>"
            "</ul>"
            "<p><strong>Ownership Categories</strong></p>"
            "<ul>"
            "<li><strong>Owner (u)</strong> — The user who owns the file.</li>"
            "<li><strong>Group (g)</strong> — The group associated with the file.</li>"
            "<li><strong>Others (o)</strong> — All other users.</li>"
            "</ul>"
            "<p><strong>Reading permissions:</strong> <code>-rwxr-xr--</code> breaks down as:</p>"
            "<ul>"
            "<li><code>-</code> = file type (- file, d directory, l symlink)</li>"
            "<li><code>rwx</code> = owner: read, write, execute</li>"
            "<li><code>r-x</code> = group: read, no write, execute</li>"
            "<li><code>r--</code> = others: read only</li>"
            "</ul>"
            "<p><strong>chmod — Change permissions</strong></p>"
            "<ul>"
            "<li>Numeric (octal): each category summed — r=4, w=2, x=1</li>"
            "<li><code>chmod 755 file</code> → owner: rwx (7), group: r-x (5), others: r-x (5)</li>"
            "<li><code>chmod 644 file</code> → owner: rw- (6), group: r-- (4), others: r-- (4)</li>"
            "<li><code>chmod 600 file</code> → owner: rw- (6), group: --- (0), others: --- (0) "
            "(private key files)</li>"
            "<li>Symbolic: <code>chmod u+x file</code> (add execute for owner), "
            "<code>chmod go-w file</code> (remove write from group and others)</li>"
            "</ul>"
            "<p><strong>chown</strong> — Change file owner: <code>chown user:group file</code>. "
            "Requires root/sudo. <strong>chgrp</strong> changes group only.</p>"
            "<p><strong>Special bits:</strong> SUID (4), SGID (2), Sticky bit (1). "
            "Example: <code>chmod 4755</code> sets SUID + 755.</p>"
        ),
        "key_points": [
            "Permissions are rwx for owner, group, and others — represented as 3 octal digits",
            "r=4, w=2, x=1; sum the values per category (e.g., rwx = 7, r-x = 5, r-- = 4)",
            "chmod 755: owner full, group/others read+execute — typical for executables",
            "chmod 644: owner read+write, group/others read-only — typical for data files",
            "chown user:group file changes both owner and group (requires sudo)",
            "Directory x permission allows traversal (cd); without it, contents are inaccessible",
            "SUID bit (4) runs executable with owner's privileges rather than caller's",
        ],
    },
]
