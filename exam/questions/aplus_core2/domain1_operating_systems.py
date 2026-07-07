"""
CompTIA A+ Core 2 (220-1202) — Domain 1: Operating Systems
44 hard/expert scenario-based questions.
"""

QUESTIONS = [
    # ── 1.1 Windows Editions ──────────────────────────────────────────────
    {
        "id": "c2d1-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "A small law firm wants workstations that can join an Active Directory domain, "
            "use BitLocker drive encryption, and be managed via Group Policy. The budget is "
            "tight and the firm does not need virtualization rights or more than 128 GB RAM. "
            "Which Windows 11 edition is the MINIMUM that satisfies all three requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows 11 Home",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Home does not support joining an Active Directory "
                    "domain or using the Local Group Policy Editor (gpedit.msc), and its "
                    "BitLocker support is limited to Device Encryption, not the full BitLocker "
                    "management suite."
                ),
            },
            {
                "id": "b",
                "text": "Windows 11 Pro",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 Pro supports Active Directory domain join, full "
                    "BitLocker drive encryption, and the Local Group Policy Editor—all at a "
                    "lower cost than Pro for Workstations or Enterprise."
                ),
            },
            {
                "id": "c",
                "text": "Windows 11 Pro for Workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Pro for Workstations satisfies all three requirements but "
                    "costs more than Pro and adds features (ReFS, NVDIMM, persistent memory) "
                    "the firm does not need, making it more than the MINIMUM required edition."
                ),
            },
            {
                "id": "d",
                "text": "Windows 11 Enterprise",
                "correct": False,
                "rationale": (
                    "Incorrect. Enterprise also meets the requirements but requires volume "
                    "licensing, making it neither the minimum nor cost-effective for a small firm."
                ),
            },
        ],
        "explanation": (
            "Windows 11 Pro is the minimum edition that provides Active Directory domain join, "
            "full BitLocker, and the Local Group Policy Editor. Home lacks these features; "
            "Pro for Workstations and Enterprise both qualify but are unnecessary and more expensive."
        ),
    },
    {
        "id": "c2d1-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "A technician is configuring a new workstation for a video-rendering department. "
            "The workstation has dual Intel Xeon processors and 512 GB of RAM. After installing "
            "Windows 11 Pro, Task Manager shows only 128 GB of RAM recognized. What is the "
            "MOST likely reason, and what edition would resolve it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The BIOS is limiting RAM; re-enabling XMP/EXPO will expose all 512 GB under Pro.",
                "correct": False,
                "rationale": (
                    "Incorrect. XMP/EXPO affects memory speed, not the OS-level RAM ceiling. "
                    "Windows 11 Pro has a hard limit of 128 GB of RAM regardless of BIOS settings."
                ),
            },
            {
                "id": "b",
                "text": "Windows 11 Pro supports a maximum of 128 GB; upgrading to Pro for Workstations or Enterprise is required.",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 Pro is capped at 128 GB of physical RAM. Pro for "
                    "Workstations and Enterprise support up to 2 TB, which is needed for this "
                    "512 GB configuration."
                ),
            },
            {
                "id": "c",
                "text": "Dual-socket systems require Windows 11 Enterprise; Pro for Workstations does not support multiple physical CPUs.",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Pro for Workstations explicitly supports up to two "
                    "physical processors (sockets), making it suitable for dual-Xeon workstations."
                ),
            },
            {
                "id": "d",
                "text": "The RAM slots are not fully seated; the OS is not the limiting factor.",
                "correct": False,
                "rationale": (
                    "Incorrect. While physical seating can cause missing RAM, 128 GB is exactly "
                    "the documented Windows 11 Pro software limit, making the edition the "
                    "most likely explanation."
                ),
            },
        ],
        "explanation": (
            "Windows 11 Pro is limited to 128 GB of physical RAM. When a workstation has more, "
            "the OS simply ignores the excess. Windows 11 Pro for Workstations and Enterprise "
            "both support up to 2 TB. Pro for Workstations also adds support for dual physical "
            "CPUs, persistent memory (NVDIMM), and the ReFS file system."
        ),
    },
    {
        "id": "c2d1-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows editions",
        "stem": (
            "An enterprise deploys Windows 11 images using Microsoft Deployment Toolkit. "
            "The security team requires DirectAccess, AppLocker policy enforcement, and "
            "Windows Defender Credential Guard. A technician proposes Windows 11 Pro. "
            "Which feature will NOT be available on Windows 11 Pro?"
        ),
        "options": [
            {
                "id": "a",
                "text": "BitLocker To Go",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker To Go (for removable drives) is available on "
                    "Windows 11 Pro, not just Enterprise."
                ),
            },
            {
                "id": "b",
                "text": "Windows Defender Credential Guard",
                "correct": True,
                "rationale": (
                    "Correct. Credential Guard is an Enterprise-only (and Education) feature. "
                    "It uses virtualization-based security to isolate LSASS and is not available "
                    "on Windows 11 Pro."
                ),
            },
            {
                "id": "c",
                "text": "Remote Desktop host (accepting inbound RDP connections)",
                "correct": False,
                "rationale": (
                    "Incorrect. Although the stem is about Credential Guard, Windows 11 Pro "
                    "does support acting as an RDP host, so this is not the missing feature."
                ),
            },
            {
                "id": "d",
                "text": "Local Group Policy Editor (gpedit.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. gpedit.msc is available on Windows 11 Pro; it is absent only "
                    "in Windows 11 Home."
                ),
            },
        ],
        "explanation": (
            "Windows Defender Credential Guard requires Windows 11 Enterprise or Education. "
            "It leverages Hyper-V virtualization-based security to prevent credential theft. "
            "AppLocker enforcement and DirectAccess also require Enterprise, so the entire "
            "proposal should be rejected in favor of Windows 11 Enterprise."
        ),
    },
    # ── 1.2 Command-Line Tools ────────────────────────────────────────────
    {
        "id": "c2d1-004",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician runs 'ipconfig /all' on a Windows workstation and sees the "
            "default gateway is 192.168.1.1, but the PC cannot reach the internet. "
            "Ping to 192.168.1.1 succeeds, but ping to 8.8.8.8 fails. "
            "Which command will BEST help determine whether the problem is DNS or routing?"
        ),
        "options": [
            {
                "id": "a",
                "text": "nslookup google.com",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup tests DNS name resolution, but if ping to 8.8.8.8 "
                    "(an IP, not a hostname) fails, DNS is not the issue—something is blocking "
                    "the route beyond the gateway."
                ),
            },
            {
                "id": "b",
                "text": "tracert 8.8.8.8",
                "correct": True,
                "rationale": (
                    "Correct. tracert traces the path to 8.8.8.8 hop-by-hop, revealing "
                    "exactly where packets stop—within the ISP, at the router, or at the "
                    "gateway—helping isolate the routing break."
                ),
            },
            {
                "id": "c",
                "text": "netstat -an",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat shows current connections and listening ports; it does "
                    "not trace the path to a remote host or isolate a routing failure."
                ),
            },
            {
                "id": "d",
                "text": "pathping 192.168.1.1",
                "correct": False,
                "rationale": (
                    "Incorrect. Pathping to the gateway (which already responds to ping) "
                    "will show the local hop only and won't reveal where connectivity breaks "
                    "beyond the gateway. Pathping to 8.8.8.8 would be more useful, but "
                    "tracert provides faster hop-by-hop isolation."
                ),
            },
        ],
        "explanation": (
            "Because ping to the IP 8.8.8.8 fails (ruling out DNS), tracert 8.8.8.8 is the "
            "best tool: it sends TTL-limited probes hop-by-hop, showing exactly which router "
            "drops the packets. pathping combines ping and tracert but takes longer. "
            "nslookup tests DNS, which is not the issue here."
        ),
    },
    {
        "id": "c2d1-005",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician needs to view all active TCP connections on a Windows PC along "
            "with the executable name that owns each connection, without stopping any "
            "services. Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "netstat -ano",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat -ano shows connections with PID numbers but not the "
                    "executable name. You would need to cross-reference with Task Manager "
                    "or tasklist."
                ),
            },
            {
                "id": "b",
                "text": "netstat -b",
                "correct": True,
                "rationale": (
                    "Correct. netstat -b displays active connections and includes the "
                    "executable involved in creating each connection or listening port, "
                    "requiring elevation but no service interruption."
                ),
            },
            {
                "id": "c",
                "text": "net use",
                "correct": False,
                "rationale": (
                    "Incorrect. net use manages mapped network drives and printer connections; "
                    "it does not display active TCP connections."
                ),
            },
            {
                "id": "d",
                "text": "hostname",
                "correct": False,
                "rationale": (
                    "Incorrect. hostname simply displays the computer's NetBIOS/DNS name "
                    "and provides no network connection information."
                ),
            },
        ],
        "explanation": (
            "netstat -b (run as Administrator) lists active connections and the binary "
            "responsible for each. netstat -ano gives PIDs instead of names, requiring "
            "a secondary lookup. net use manages shares/drives; hostname shows the machine name."
        ),
    },
    {
        "id": "c2d1-006",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows command-line tools",
        "stem": (
            "An administrator runs 'chkdsk C: /f /r' on a live Windows system and receives "
            "the message: 'Chkdsk cannot run because the volume is in use by another process. "
            "Would you like to schedule this volume to be checked the next time the system "
            "restarts?' After confirming, the check runs on the NEXT reboot. "
            "What is the technical reason the check could not run immediately?"
        ),
        "options": [
            {
                "id": "a",
                "text": "chkdsk requires Safe Mode to access the NTFS journal.",
                "correct": False,
                "rationale": (
                    "Incorrect. Safe Mode is not required for chkdsk. The constraint is "
                    "exclusive access to the volume, not a mode requirement."
                ),
            },
            {
                "id": "b",
                "text": "The C: volume is mounted and locked by Windows; chkdsk needs exclusive access to repair it.",
                "correct": True,
                "rationale": (
                    "Correct. Windows keeps the system volume (C:) mounted and in use at all "
                    "times. chkdsk /f (fix errors) and /r (recover bad sectors) require "
                    "exclusive volume access, so the repair is deferred to early boot before "
                    "the OS mounts the volume."
                ),
            },
            {
                "id": "c",
                "text": "The /r switch is only valid during Windows PE; it has no effect on a running OS.",
                "correct": False,
                "rationale": (
                    "Incorrect. /r is a valid switch in the full OS but requires exclusive "
                    "volume access. The deferral is caused by the volume being in use, "
                    "not by an invalid switch."
                ),
            },
            {
                "id": "d",
                "text": "chkdsk must be run from an elevated command prompt; without elevation it always defers.",
                "correct": False,
                "rationale": (
                    "Incorrect. Elevation is required, but the reason for the deferral "
                    "specifically is that the system volume is actively mounted—even an "
                    "elevated chkdsk cannot get exclusive access while Windows is running."
                ),
            },
        ],
        "explanation": (
            "NTFS volumes that are actively mounted cannot be checked in repair mode because "
            "chkdsk /f and /r need exclusive, unmounted access. Windows schedules the check "
            "in the registry (HKLM\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\BootExecute) "
            "so it runs during the early boot phase before the volume is fully mounted by the OS."
        ),
    },
    {
        "id": "c2d1-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician needs to copy an entire directory tree from C:\\ProjectFiles to "
            "\\\\FileServer\\Backup, preserving NTFS permissions, timestamps, and skipping "
            "files that already exist with the same timestamp. Which command is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "xcopy C:\\ProjectFiles \\\\FileServer\\Backup /e /h",
                "correct": False,
                "rationale": (
                    "Incorrect. xcopy can copy subdirectories and hidden files but does NOT "
                    "preserve NTFS security permissions and has less robust timestamp "
                    "comparison than robocopy."
                ),
            },
            {
                "id": "b",
                "text": "copy C:\\ProjectFiles \\\\FileServer\\Backup /y",
                "correct": False,
                "rationale": (
                    "Incorrect. The basic copy command does not recurse directories, preserve "
                    "NTFS permissions, or skip already-synchronized files."
                ),
            },
            {
                "id": "c",
                "text": "robocopy C:\\ProjectFiles \\\\FileServer\\Backup /e /copyall /xo",
                "correct": True,
                "rationale": (
                    "Correct. robocopy /e copies all subdirectories including empty ones, "
                    "/copyall preserves all file attributes including NTFS ACLs and "
                    "timestamps, and /xo excludes (skips) files older than the destination, "
                    "effectively skipping already-current files."
                ),
            },
            {
                "id": "d",
                "text": "robocopy C:\\ProjectFiles \\\\FileServer\\Backup /mir",
                "correct": False,
                "rationale": (
                    "Incorrect. /mir (mirror) would also DELETE files in the destination that "
                    "are not in the source, which is destructive for a backup scenario. "
                    "The question requires skipping, not mirroring."
                ),
            },
        ],
        "explanation": (
            "robocopy is the preferred tool for directory replication. /e copies all "
            "subdirectories including empty ones; /copyall copies data, attributes, timestamps, "
            "NTFS security (ACLs), owner, and auditing information; /xo skips files where "
            "the source is older than the destination. xcopy does not preserve ACLs; "
            "copy does not recurse; /mir deletes unmatched destination files."
        ),
    },
    {
        "id": "c2d1-008",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician runs 'gpupdate /force' after adding a new GPO. The command "
            "completes successfully, but the policy does not appear to be applied. "
            "Which command should the technician run to confirm whether the policy "
            "reached the local machine and show detailed policy application results?"
        ),
        "options": [
            {
                "id": "a",
                "text": "gpedit.msc",
                "correct": False,
                "rationale": (
                    "Incorrect. gpedit.msc shows the local Group Policy Object editor for "
                    "authoring policies, not the resultant set of applied policies from "
                    "domain GPOs."
                ),
            },
            {
                "id": "b",
                "text": "gpresult /r",
                "correct": True,
                "rationale": (
                    "Correct. gpresult /r displays the Resultant Set of Policy (RSoP) for "
                    "the current user and computer, showing which GPOs were applied, denied, "
                    "or filtered, helping confirm whether the new policy reached the machine."
                ),
            },
            {
                "id": "c",
                "text": "net user /domain",
                "correct": False,
                "rationale": (
                    "Incorrect. net user /domain queries domain user account information; "
                    "it provides no Group Policy application data."
                ),
            },
            {
                "id": "d",
                "text": "winver",
                "correct": False,
                "rationale": (
                    "Incorrect. winver displays the Windows version and build number; it "
                    "has no relationship to Group Policy application status."
                ),
            },
        ],
        "explanation": (
            "gpresult /r (or /h for an HTML report) displays the Resultant Set of Policy, "
            "showing applied GPOs, their precedence, denied GPOs, and reasons for filtering "
            "(security group, WMI filter, etc.). This is the definitive command to audit "
            "GPO application after gpupdate."
        ),
    },
    {
        "id": "c2d1-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician uses diskpart to prepare a new 3 TB drive. After typing 'select disk 1' "
            "and 'clean', which sequence of commands creates a single GPT partition that uses "
            "the entire disk and formats it as NTFS with the label 'DATA'?"
        ),
        "options": [
            {
                "id": "a",
                "text": "convert mbr → create partition primary → format fs=ntfs label=DATA quick",
                "correct": False,
                "rationale": (
                    "Incorrect. MBR (Master Boot Record) only supports partitions up to "
                    "2 TB. A 3 TB drive requires GPT. 'convert mbr' is the wrong conversion."
                ),
            },
            {
                "id": "b",
                "text": "convert gpt → create partition primary → format fs=ntfs label=DATA quick",
                "correct": True,
                "rationale": (
                    "Correct. After 'clean', 'convert gpt' sets the partition table to "
                    "GUID Partition Table (required for >2 TB), 'create partition primary' "
                    "allocates the full disk, and 'format fs=ntfs label=DATA quick' formats "
                    "it as NTFS with the specified label."
                ),
            },
            {
                "id": "c",
                "text": "create partition primary size=3000000 → format fs=exfat label=DATA quick",
                "correct": False,
                "rationale": (
                    "Incorrect. Without 'convert gpt', the disk remains MBR (post-clean), "
                    "which cannot address >2 TB. Also, exFAT lacks journaling and is not "
                    "the preferred format for a data drive."
                ),
            },
            {
                "id": "d",
                "text": "create partition primary → assign letter=D → format fs=ntfs label=DATA",
                "correct": False,
                "rationale": (
                    "Incorrect. Without first running 'convert gpt', the new partition table "
                    "remains MBR, which will limit the usable space to ~2 TB on the 3 TB drive."
                ),
            },
        ],
        "explanation": (
            "Disks larger than 2 TB require a GPT partition table. After 'clean' wipes the "
            "partition table, 'convert gpt' replaces MBR with GPT before any partition is "
            "created. Then 'create partition primary' spans the full disk, and "
            "'format fs=ntfs label=DATA quick' applies the file system. MBR is limited to "
            "2 TiB addressable space."
        ),
    },
    {
        "id": "c2d1-010",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A help desk technician needs to add a local user account named 'labuser' "
            "with the password 'P@ssw0rd1' and then add that account to the local "
            "Administrators group—all from the command line. Which two commands "
            "accomplish this in the correct order?"
        ),
        "options": [
            {
                "id": "a",
                "text": "net user labuser P@ssw0rd1 /add → net localgroup Administrators labuser /add",
                "correct": True,
                "rationale": (
                    "Correct. 'net user labuser P@ssw0rd1 /add' creates the local account, "
                    "then 'net localgroup Administrators labuser /add' places it in the "
                    "local Administrators group."
                ),
            },
            {
                "id": "b",
                "text": "net localgroup Administrators labuser /add → net user labuser P@ssw0rd1 /add",
                "correct": False,
                "rationale": (
                    "Incorrect. The account must exist before it can be added to a group. "
                    "Running the localgroup command first will fail with 'The user name "
                    "could not be found.'"
                ),
            },
            {
                "id": "c",
                "text": "net user labuser /add /passwordreq:yes → net group Administrators labuser /add",
                "correct": False,
                "rationale": (
                    "Incorrect. 'net group' manages domain groups on a domain controller, "
                    "not local groups. For local groups, 'net localgroup' is required."
                ),
            },
            {
                "id": "d",
                "text": "net user labuser /create P@ssw0rd1 → net localgroup Administrators /add labuser",
                "correct": False,
                "rationale": (
                    "Incorrect. The /create switch does not exist for net user; the correct "
                    "switch is /add. The syntax 'net localgroup Administrators /add labuser' "
                    "also has the switches in the wrong order."
                ),
            },
        ],
        "explanation": (
            "'net user <username> <password> /add' creates a local account. "
            "'net localgroup <group> <username> /add' adds an existing local or domain user "
            "to a local group. 'net group' applies only to domain groups on a DC. "
            "The account must be created before it can be added to any group."
        ),
    },
    # ── 1.3 Windows Features/Tools ────────────────────────────────────────
    {
        "id": "c2d1-011",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A technician needs to create a custom management console that combines "
            "Device Manager, Disk Management, and Event Viewer for a junior technician "
            "to use without granting full administrative access to each individual tool. "
            "Which Windows utility enables this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Task Manager",
                "correct": False,
                "rationale": (
                    "Incorrect. Task Manager is a standalone application that shows running "
                    "processes, performance, and services; it cannot host other tools or "
                    "be customized with snap-ins."
                ),
            },
            {
                "id": "b",
                "text": "MSConfig (System Configuration)",
                "correct": False,
                "rationale": (
                    "Incorrect. MSConfig manages startup options, services at boot, and "
                    "boot parameters; it is not a snap-in host and cannot combine other tools."
                ),
            },
            {
                "id": "c",
                "text": "Microsoft Management Console (mmc.exe)",
                "correct": True,
                "rationale": (
                    "Correct. mmc.exe is the host framework for snap-ins. A technician can "
                    "open a blank MMC (mmc /a), add snap-ins (Device Manager, Disk Management, "
                    "Event Viewer), save the custom .msc file, and distribute it with "
                    "Author/User mode restrictions."
                ),
            },
            {
                "id": "d",
                "text": "Resource Monitor",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource Monitor displays real-time CPU, memory, disk, and "
                    "network usage data and cannot host arbitrary snap-ins."
                ),
            },
        ],
        "explanation": (
            "mmc.exe is the Microsoft Management Console framework. Administrators add snap-ins "
            "(Device Manager, Disk Management, Event Viewer, etc.) to create a custom .msc file. "
            "The console can be saved in User Mode (limited) to prevent snap-in changes, then "
            "distributed to junior staff. Task Manager, MSConfig, and Resource Monitor are "
            "fixed-function tools, not snap-in hosts."
        ),
    },
    {
        "id": "c2d1-012",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A user reports that Windows is sluggish and a specific background service "
            "is consuming 40% CPU. The technician wants to stop the service AND prevent "
            "it from restarting automatically after a reboot, without uninstalling it. "
            "Which tool provides the MOST direct way to change the service startup type?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Task Manager → Services tab → right-click → Stop",
                "correct": False,
                "rationale": (
                    "Incorrect. Task Manager can stop a service but does not expose the "
                    "startup type setting. The service will restart on reboot if it is "
                    "set to Automatic."
                ),
            },
            {
                "id": "b",
                "text": "services.msc → open service properties → change Startup type to Disabled",
                "correct": True,
                "rationale": (
                    "Correct. services.msc (Services snap-in) allows viewing and modifying "
                    "the startup type (Automatic, Manual, Disabled) and immediately stopping "
                    "or starting a service in a single interface."
                ),
            },
            {
                "id": "c",
                "text": "MSConfig → Services tab → uncheck the service",
                "correct": False,
                "rationale": (
                    "Incorrect. MSConfig's Services tab can suppress a service at boot, "
                    "but this is a diagnostic tool. Unchecking a service in MSConfig leaves "
                    "the system in a modified boot state. services.msc is the authoritative "
                    "tool for permanent startup-type changes."
                ),
            },
            {
                "id": "d",
                "text": "regedit → HKLM\\SYSTEM\\CurrentControlSet\\Services → set Start to 4",
                "correct": False,
                "rationale": (
                    "Incorrect. Editing the registry directly works but is not the 'most "
                    "direct' method. services.msc provides a GUI with the same outcome and "
                    "less risk of error."
                ),
            },
        ],
        "explanation": (
            "services.msc is the dedicated Services management snap-in. It exposes the "
            "Startup Type property (Automatic, Manual, Disabled, Automatic [Delayed Start]) "
            "and allows immediate Start/Stop. MSConfig is a troubleshooting bootstrap tool, "
            "not intended for permanent configuration. Task Manager cannot change startup types."
        ),
    },
    {
        "id": "c2d1-013",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "After installing a new driver, a technician notices that a USB device is "
            "shown with a yellow exclamation mark in the Windows interface. "
            "Which tool should the technician open FIRST to identify the error code "
            "and attempt a driver rollback?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Event Viewer → System log",
                "correct": False,
                "rationale": (
                    "Incorrect. Event Viewer records driver errors in the System log, but "
                    "it does not provide a driver rollback function. Device Manager is the "
                    "correct first stop."
                ),
            },
            {
                "id": "b",
                "text": "Device Manager",
                "correct": True,
                "rationale": (
                    "Correct. Device Manager displays the yellow exclamation mark, shows "
                    "the Windows error code in device Properties → General tab, and provides "
                    "the Roll Back Driver button on the Driver tab if a previous driver is available."
                ),
            },
            {
                "id": "c",
                "text": "Disk Management",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk Management handles storage volumes and partitions; it "
                    "does not manage drivers or show device error codes."
                ),
            },
            {
                "id": "d",
                "text": "Performance Monitor",
                "correct": False,
                "rationale": (
                    "Incorrect. Performance Monitor tracks real-time and historical performance "
                    "counters; it does not manage device drivers."
                ),
            },
        ],
        "explanation": (
            "Device Manager is the primary tool for hardware and driver management. A yellow "
            "exclamation (!) means a device has a problem. Opening the device's Properties "
            "shows the error code (e.g., Code 43, Code 10) and the Driver tab provides "
            "Update Driver, Rollback Driver, and Uninstall Device options. Event Viewer "
            "complements this with detailed error logs."
        ),
    },
    # ── 1.4 Control Panel ─────────────────────────────────────────────────
    {
        "id": "c2d1-014",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "Users in an office report that their browsers display a certificate error "
            "when accessing the internal company web portal. The portal uses a certificate "
            "signed by the company's private CA. Where in Windows should a technician "
            "import the CA's root certificate so ALL users on a standalone workstation "
            "trust it system-wide?"
        ),
        "options": [
            {
                "id": "a",
                "text": "certmgr.msc → Current User → Trusted Root Certification Authorities",
                "correct": False,
                "rationale": (
                    "Incorrect. certmgr.msc manages the current user's certificate store. "
                    "Importing here trusts the CA only for that user's processes, not for "
                    "all system services or other user accounts."
                ),
            },
            {
                "id": "b",
                "text": "certlm.msc → Local Computer → Trusted Root Certification Authorities",
                "correct": True,
                "rationale": (
                    "Correct. certlm.msc (or MMC with the Certificates snap-in scoped to "
                    "Computer Account) manages the local machine's certificate store. "
                    "Importing the root CA here makes it trusted system-wide for all users "
                    "and processes on the workstation."
                ),
            },
            {
                "id": "c",
                "text": "Internet Options → Content → Certificates → Import",
                "correct": False,
                "rationale": (
                    "Incorrect. Internet Options → Content → Certificates opens the user-level "
                    "certificate store (same as certmgr.msc), not the computer-level store. "
                    "It would only fix the issue for the currently logged-in user."
                ),
            },
            {
                "id": "d",
                "text": "Windows Defender Firewall → Advanced Settings → Inbound Rules",
                "correct": False,
                "rationale": (
                    "Incorrect. Firewall rules control network traffic, not certificate trust. "
                    "This would not resolve a certificate error."
                ),
            },
        ],
        "explanation": (
            "Certificate trust operates at two scopes: user (certmgr.msc) and computer (certlm.msc). "
            "For system-wide trust—affecting all users and services—the CA root certificate must "
            "be imported into the Computer account's Trusted Root Certification Authorities store. "
            "In a domain environment, Group Policy can push this automatically via Computer "
            "Configuration → Windows Settings → Security Settings → Public Key Policies."
        ),
    },
    {
        "id": "c2d1-015",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A laptop user reports that the screen goes blank after 3 minutes of inactivity, "
            "even when the laptop is plugged into AC power during a presentation. "
            "Which Control Panel path MOST directly resolves this by adjusting the "
            "display timeout for the plugged-in power plan?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → System → Advanced System Settings → Performance Options",
                "correct": False,
                "rationale": (
                    "Incorrect. Advanced System Settings → Performance Options controls "
                    "visual effects and virtual memory; it does not manage power plan "
                    "display timeouts."
                ),
            },
            {
                "id": "b",
                "text": "Control Panel → Display → Screen Resolution",
                "correct": False,
                "rationale": (
                    "Incorrect. Screen Resolution controls display output configuration "
                    "(resolution, orientation, multiple monitors); it does not adjust "
                    "power management timeouts."
                ),
            },
            {
                "id": "c",
                "text": "Control Panel → Power Options → Change plan settings → Change when the display turns off (Plugged in)",
                "correct": True,
                "rationale": (
                    "Correct. Power Options → Change plan settings exposes separate timeout "
                    "values for battery and plugged-in states. Increasing or setting 'Never' "
                    "for the plugged-in display timeout prevents blanking during presentations."
                ),
            },
            {
                "id": "d",
                "text": "Control Panel → Personalization → Screen Saver → Wait",
                "correct": False,
                "rationale": (
                    "Incorrect. The screen saver timeout can blank the screen but is separate "
                    "from the power plan display timeout. Adjusting the screen saver alone "
                    "does not fix the power-plan-driven display shutoff."
                ),
            },
        ],
        "explanation": (
            "Windows Power Options controls display and sleep timeouts independently for "
            "battery and plugged-in modes. Setting the 'Turn off the display' value to "
            "'Never' when plugged in prevents the display from blanking during presentations. "
            "Screen Saver and Personalization settings are separate from power plan timeouts."
        ),
    },
    {
        "id": "c2d1-016",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A user wants to completely remove a desktop application and all its "
            "registered components from Windows. Which Control Panel applet is the "
            "correct tool, and why is it preferred over deleting the program folder?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Programs and Features; it calls the application's uninstaller, removing registry entries, services, and Start menu shortcuts—things folder deletion misses.",
                "correct": True,
                "rationale": (
                    "Correct. Programs and Features invokes the registered uninstall routine, "
                    "which removes registry keys (HKLM/HKCU), services, COM objects, file "
                    "associations, and shortcuts. Simply deleting the folder leaves these "
                    "artifacts and can break Windows."
                ),
            },
            {
                "id": "b",
                "text": "User Accounts; it revokes per-user install permissions, effectively blocking the application.",
                "correct": False,
                "rationale": (
                    "Incorrect. User Accounts manages credentials and account types; it "
                    "cannot uninstall applications."
                ),
            },
            {
                "id": "c",
                "text": "Device Manager; removing the device driver associated with the application uninstalls it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Manager handles hardware drivers, not application "
                    "software. Most desktop applications do not have device driver components."
                ),
            },
            {
                "id": "d",
                "text": "Indexing Options; removing the program location from the index deletes the application files.",
                "correct": False,
                "rationale": (
                    "Incorrect. Indexing Options configures search index locations; removing "
                    "a folder from the index only affects search results—it does not delete "
                    "files or uninstall software."
                ),
            },
        ],
        "explanation": (
            "Programs and Features (appwiz.cpl) calls the application's MSI or custom "
            "uninstaller, which performs a clean removal: registry keys, services, COM "
            "registrations, shortcuts, and file associations. Manual folder deletion leaves "
            "registry entries and other OS artifacts (orphaned entries, broken file "
            "associations) that accumulate over time and can cause instability."
        ),
    },
    # ── 1.5 Windows Settings ──────────────────────────────────────────────
    {
        "id": "c2d1-017",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "A Windows 11 laptop is connected to a mobile hotspot. The user notices "
            "that Windows Update is downloading a large feature update, consuming most "
            "of the limited data. Which Windows Settings option should the technician "
            "enable to prevent large background data usage on this connection?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → Windows Update → Pause updates for 7 days",
                "correct": False,
                "rationale": (
                    "Incorrect. Pausing updates is a temporary workaround limited to 35 "
                    "days maximum, and it affects all network connections, not just the "
                    "metered one. It does not address the root cause of background data usage."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Network & Internet → Wi-Fi → [current network] → Set as metered connection",
                "correct": True,
                "rationale": (
                    "Correct. Marking the connection as metered signals Windows (and "
                    "compatible apps) to reduce background data usage. Windows Update will "
                    "defer non-critical downloads, and the Store will pause automatic app "
                    "updates over metered connections."
                ),
            },
            {
                "id": "c",
                "text": "Settings → Privacy & Security → General → Let apps use advertising ID",
                "correct": False,
                "rationale": (
                    "Incorrect. The advertising ID setting controls ad personalization; "
                    "it has no effect on network data usage or Windows Update behavior."
                ),
            },
            {
                "id": "d",
                "text": "Settings → Apps → Startup → Disable Microsoft Store",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the Store from startup affects app launch at "
                    "login, not background update downloads over the current connection."
                ),
            },
        ],
        "explanation": (
            "Setting a Wi-Fi or cellular connection as 'metered' in Settings → Network & "
            "Internet tells Windows to treat it as a limited-data connection. This causes "
            "Windows Update to defer feature updates, the Microsoft Store to pause automatic "
            "updates, and sync services to reduce frequency. It is the purpose-built control "
            "for mobile data conservation."
        ),
    },
    {
        "id": "c2d1-018",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "An administrator needs to ensure that a Windows 11 PC only runs apps "
            "downloaded from the Microsoft Store for security reasons. Where in "
            "Windows Settings is this restriction configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → Privacy & Security → Windows Security → App & Browser Control → Smart App Control",
                "correct": False,
                "rationale": (
                    "Incorrect. Smart App Control blocks known-malicious apps using cloud "
                    "intelligence, but it does not restrict installs to Store-only apps."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Apps → Advanced app settings → Choose where to get apps → The Microsoft Store only",
                "correct": True,
                "rationale": (
                    "Correct. This setting (formerly 'Installing apps' under Apps & features) "
                    "enforces a Store-only installation policy, warning or blocking installs "
                    "from sources outside the Microsoft Store."
                ),
            },
            {
                "id": "c",
                "text": "Settings → Accounts → Family & other users → Add a child account",
                "correct": False,
                "rationale": (
                    "Incorrect. Family accounts with parental controls can restrict app "
                    "installs, but this is a per-user family feature, not the system-wide "
                    "installation restriction the question describes."
                ),
            },
            {
                "id": "d",
                "text": "Settings → System → Optional features → Microsoft Store apps",
                "correct": False,
                "rationale": (
                    "Incorrect. Optional features manages Windows optional components "
                    "(like RSAT or media features); it does not control where apps can be "
                    "installed from."
                ),
            },
        ],
        "explanation": (
            "Settings → Apps → Advanced app settings → 'Choose where to get apps' provides "
            "three enforcement levels: Anywhere (no restriction), Anywhere with a warning "
            "(recommends Store), and The Microsoft Store only (blocks non-Store installs). "
            "This is the consumer-facing equivalent of AppLocker's publisher rules."
        ),
    },
    # ── 1.6 Windows Networking ────────────────────────────────────────────
    {
        "id": "c2d1-019",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A technician sets up a new Windows 11 PC on the corporate network. "
            "After joining the Active Directory domain, the user's home drive (H:) "
            "is not mapping at login. The drive mapping is defined in a domain GPO. "
            "Which command should the technician run to apply the policy immediately "
            "without rebooting?"
        ),
        "options": [
            {
                "id": "a",
                "text": "net use H: \\\\fileserver\\users\\%username%",
                "correct": False,
                "rationale": (
                    "Incorrect. This manually maps the drive for the session only but does "
                    "not fix the GPO-driven mapping, which should persist automatically. "
                    "The underlying policy issue would recur at the next login."
                ),
            },
            {
                "id": "b",
                "text": "gpupdate /force",
                "correct": True,
                "rationale": (
                    "Correct. gpupdate /force immediately re-applies all Computer and User "
                    "Group Policies, including drive mapping preferences, without requiring "
                    "a reboot. It is the standard way to trigger GPO application on demand."
                ),
            },
            {
                "id": "c",
                "text": "ipconfig /flushdns",
                "correct": False,
                "rationale": (
                    "Incorrect. Flushing the DNS cache clears stale name resolution entries "
                    "but does not trigger GPO application or drive mapping."
                ),
            },
            {
                "id": "d",
                "text": "net start Workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. The Workstation service (LanmanWorkstation) handles SMB "
                    "client functions, but restarting it does not trigger Group Policy "
                    "to re-apply drive mappings."
                ),
            },
        ],
        "explanation": (
            "Drive mappings configured via Group Policy Preferences are applied when GPO "
            "is processed—at login or when gpupdate runs. 'gpupdate /force' reprocesses "
            "all policies (even unchanged ones) immediately for both Computer and User "
            "contexts, triggering the drive mapping. Manual net use creates a temporary "
            "session mapping but does not fix the policy application."
        ),
    },
    {
        "id": "c2d1-020",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A Windows workstation connected to a public Wi-Fi network at a coffee shop "
            "suddenly has its Network Location set to 'Private'. A technician is concerned "
            "this makes file and printer sharing discoverable. Which Network Location "
            "setting should be applied, and what is the MAIN security implication of each?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Set to Domain; domain networks apply the most restrictive firewall profile.",
                "correct": False,
                "rationale": (
                    "Incorrect. The Domain profile is applied automatically when the PC is "
                    "joined to and authenticated against an Active Directory domain—it cannot "
                    "be manually selected for arbitrary networks."
                ),
            },
            {
                "id": "b",
                "text": "Set to Public; Public disables network discovery and file/printer sharing by default, applying the most restrictive firewall rules.",
                "correct": True,
                "rationale": (
                    "Correct. The Public network location turns off network discovery, file "
                    "sharing, and printer sharing, and applies the most restrictive Windows "
                    "Firewall profile—appropriate for untrusted networks like coffee shops."
                ),
            },
            {
                "id": "c",
                "text": "Set to Private; Private enables full network discovery for easier file sharing.",
                "correct": False,
                "rationale": (
                    "Incorrect. Private allows network discovery and is designed for trusted "
                    "networks (home or office). Using Private on a public network exposes "
                    "the workstation to other users on that network."
                ),
            },
            {
                "id": "d",
                "text": "Network Location does not affect Windows Firewall; only Windows Defender settings matter.",
                "correct": False,
                "rationale": (
                    "Incorrect. Network Location directly determines which Windows Firewall "
                    "profile (Domain, Private, or Public) is active. Each profile has "
                    "distinct inbound/outbound rules."
                ),
            },
        ],
        "explanation": (
            "Windows applies three firewall profiles based on Network Location: Domain "
            "(when on an AD domain), Private (trusted networks—discovery and sharing on), "
            "and Public (untrusted—discovery and sharing off, most restrictive rules). "
            "Untrusted Wi-Fi should always use the Public profile to minimize attack surface."
        ),
    },
    # ── 1.7 Application Installation ─────────────────────────────────────
    {
        "id": "c2d1-021",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application installation requirements",
        "stem": (
            "A 64-bit Windows 10 workstation has 4 GB of RAM. A user wants to install "
            "a legacy 32-bit application that lists a minimum of 2 GB RAM on its system "
            "requirements card. After installation, the application crashes immediately. "
            "Which factor is the MOST likely cause specific to the 32-bit process model?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A 32-bit application cannot run on a 64-bit OS.",
                "correct": False,
                "rationale": (
                    "Incorrect. 64-bit Windows includes WOW64 (Windows-on-Windows 64-bit), "
                    "an emulation layer that allows 32-bit applications to run on a 64-bit OS."
                ),
            },
            {
                "id": "b",
                "text": "A 32-bit process is limited to 2 GB (or 4 GB with LAA) of virtual address space, regardless of physical RAM.",
                "correct": True,
                "rationale": (
                    "Correct. A 32-bit process can address at most 4 GB of virtual address "
                    "space, of which only 2 GB is user space by default (or 3–4 GB if the "
                    "application is built with Large Address Awareness). If the app tries to "
                    "allocate more than its VA limit, it crashes regardless of available RAM."
                ),
            },
            {
                "id": "c",
                "text": "32-bit applications require a 32-bit OS; WOW64 provides execution but denies memory allocation.",
                "correct": False,
                "rationale": (
                    "Incorrect. WOW64 allows full execution AND memory allocation up to the "
                    "32-bit address space limit. WOW64 does not deny memory allocation."
                ),
            },
            {
                "id": "d",
                "text": "The system has insufficient RAM; upgrading to 8 GB would resolve the crash.",
                "correct": False,
                "rationale": (
                    "Incorrect. 4 GB of physical RAM exceeds the 2 GB minimum. The crash "
                    "is caused by the 32-bit virtual address space limit, not physical RAM "
                    "shortage. Adding more RAM would not change the per-process VA ceiling."
                ),
            },
        ],
        "explanation": (
            "32-bit processes run in a 4 GB virtual address space (2 GB user / 2 GB kernel "
            "by default on x86). Even on a 64-bit OS with ample RAM, a 32-bit app cannot "
            "use more than its VA limit. Applications must be compiled with the /LARGEADDRESSAWARE "
            "flag to use up to 4 GB user space on 64-bit Windows. WOW64 allows execution "
            "of 32-bit code on 64-bit Windows without restriction."
        ),
    },
    {
        "id": "c2d1-022",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application installation requirements",
        "stem": (
            "A company needs to silently deploy a 500 MB application installer to 200 "
            "workstations overnight. The applications team uses an MSI package. "
            "Which distribution method avoids distributing individual USB drives and "
            "minimizes internet bandwidth usage?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Email the MSI to all 200 users and have them install it in the morning.",
                "correct": False,
                "rationale": (
                    "Incorrect. Email is not designed for 500 MB binary attachments, requires "
                    "user intervention, and cannot ensure a silent, unattended install."
                ),
            },
            {
                "id": "b",
                "text": "Upload the MSI to a network share and deploy via Group Policy Software Installation (GPSI) or SCCM/Intune.",
                "correct": True,
                "rationale": (
                    "Correct. Hosting the MSI on a network file share and pushing it through "
                    "GPSI or a configuration manager (SCCM/Intune) enables silent, "
                    "scheduled, unattended deployment to all 200 machines using only internal "
                    "network bandwidth."
                ),
            },
            {
                "id": "c",
                "text": "Copy the ISO to each machine via USB then run the installer.",
                "correct": False,
                "rationale": (
                    "Incorrect. This requires physical access to all 200 machines and manual "
                    "installation steps, which does not scale and is not silent."
                ),
            },
            {
                "id": "d",
                "text": "Post the installer on a public cloud URL and have each machine download it from the internet.",
                "correct": False,
                "rationale": (
                    "Incorrect. Downloading from the internet multiplies the 500 MB by 200 "
                    "machines (100 GB total), consumes WAN bandwidth, and raises security "
                    "concerns about public file hosting."
                ),
            },
        ],
        "explanation": (
            "Network-based deployment via Group Policy Software Installation (GPSI) or "
            "endpoint management platforms (SCCM/Microsoft Endpoint Manager/Intune) is the "
            "standard enterprise method for silently pushing MSI packages. The MSI is "
            "stored once on a network share; clients pull from the LAN, eliminating "
            "per-machine internet download and manual intervention."
        ),
    },
    # ── 1.8 File Systems & OS Types ──────────────────────────────────────
    {
        "id": "c2d1-023",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A technician needs to format a 256 GB USB flash drive so it can store "
            "single files larger than 4 GB AND be natively readable (without drivers) "
            "on both Windows 10 and macOS Ventura. Which file system satisfies both "
            "requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FAT32",
                "correct": False,
                "rationale": (
                    "Incorrect. FAT32 is readable on both Windows and macOS but has a "
                    "maximum individual file size of 4 GB minus 1 byte, which fails the "
                    "first requirement."
                ),
            },
            {
                "id": "b",
                "text": "NTFS",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS supports files larger than 4 GB, but macOS can only "
                    "read NTFS volumes natively (not write without third-party drivers). "
                    "While read-only access may seem acceptable, it is not 'natively "
                    "readable' in a full sense, and write capability is expected."
                ),
            },
            {
                "id": "c",
                "text": "exFAT",
                "correct": True,
                "rationale": (
                    "Correct. exFAT (Extended FAT) supports files larger than 4 GB "
                    "(theoretical maximum ~16 EB) and is natively supported for both read "
                    "and write on Windows (XP SP2+) and macOS (10.6.5+) without additional "
                    "drivers."
                ),
            },
            {
                "id": "d",
                "text": "ext4",
                "correct": False,
                "rationale": (
                    "Incorrect. ext4 is a Linux file system. Windows and macOS do not "
                    "natively read ext4 without third-party drivers."
                ),
            },
        ],
        "explanation": (
            "exFAT was designed for flash drives and portable storage. It eliminates FAT32's "
            "4 GB file size limit and is natively supported on Windows Vista+ and macOS "
            "10.6.5+. NTFS lacks native write support on macOS; FAT32 cannot store files "
            ">4 GB; ext4 requires additional drivers on both Windows and macOS."
        ),
    },
    {
        "id": "c2d1-024",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A company's Windows Server 2019 file server is running an NTFS volume "
            "that houses critical databases. A storage administrator recommends "
            "migrating the data volume to ReFS. Which capability does ReFS provide "
            "that NTFS does NOT natively offer, making it advantageous for large "
            "data integrity workloads?"
        ),
        "options": [
            {
                "id": "a",
                "text": "File-level encryption (EFS)",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS supports EFS (Encrypting File System); ReFS does "
                    "NOT support EFS. This is actually a capability NTFS has that ReFS lacks."
                ),
            },
            {
                "id": "b",
                "text": "Proactive data integrity scrubbing with automatic corruption detection and repair using parity (Storage Spaces).",
                "correct": True,
                "rationale": (
                    "Correct. ReFS uses checksums on both metadata and (with Storage Spaces) "
                    "file data, enabling proactive integrity scrubbing that detects and "
                    "corrects corruption automatically using redundant data. NTFS only "
                    "checksums metadata, not file data."
                ),
            },
            {
                "id": "c",
                "text": "Disk quotas per user",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS supports disk quotas; ReFS does NOT support disk quotas. "
                    "This is a limitation of ReFS compared to NTFS."
                ),
            },
            {
                "id": "d",
                "text": "Compression and sparse file support",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS supports both compression and sparse files. ReFS does "
                    "NOT support NTFS-style file compression, making this another NTFS "
                    "advantage, not a ReFS advantage."
                ),
            },
        ],
        "explanation": (
            "ReFS (Resilient File System) was designed for large-scale storage resilience. "
            "Its key advantages over NTFS include: checksums on both metadata AND data "
            "(with Storage Spaces), proactive integrity scrubbing that repairs corruption "
            "from redundant copies, and support for very large volumes (>256 TB). "
            "ReFS lacks EFS, disk quotas, compression, and 8.3 filename support—features "
            "NTFS provides."
        ),
    },
    {
        "id": "c2d1-025",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A macOS Monterey system's primary drive uses APFS. A technician connects "
            "an older external drive formatted as HFS+. Which statement about APFS "
            "is CORRECT compared to HFS+?"
        ),
        "options": [
            {
                "id": "a",
                "text": "APFS uses B-tree structures exclusively for all metadata, identical to HFS+.",
                "correct": False,
                "rationale": (
                    "Incorrect. While APFS uses B-trees for some structures, it introduces "
                    "copy-on-write semantics and a different container/volume architecture "
                    "not found in HFS+."
                ),
            },
            {
                "id": "b",
                "text": "APFS supports native file-level encryption with multi-key encryption and is optimized for SSDs with copy-on-write metadata.",
                "correct": True,
                "rationale": (
                    "Correct. APFS was designed for SSDs and Flash. It supports per-file "
                    "multi-key encryption (single-key, multi-key, and no encryption per "
                    "file/directory), copy-on-write to reduce write amplification, and "
                    "space sharing across volumes in a container."
                ),
            },
            {
                "id": "c",
                "text": "APFS does not support journaling, which is why it replaced HFS+ Journaled.",
                "correct": False,
                "rationale": (
                    "Incorrect. APFS uses copy-on-write transactions that provide stronger "
                    "consistency guarantees than traditional journaling. It does not rely "
                    "on a journal in the HFS+ sense, but this is an improvement, not an absence."
                ),
            },
            {
                "id": "d",
                "text": "APFS volumes cannot be accessed from Windows even with Boot Camp.",
                "correct": False,
                "rationale": (
                    "Incorrect. While Windows (via Boot Camp) cannot natively read APFS, "
                    "Apple provides the APFS driver for Windows in Boot Camp to allow "
                    "reading macOS APFS partitions."
                ),
            },
        ],
        "explanation": (
            "APFS replaced HFS+ as Apple's default file system starting in macOS High Sierra "
            "(2017). Key features: native multi-key encryption (per-file, directory, or volume), "
            "copy-on-write for crash safety without a separate journal, space sharing (multiple "
            "volumes in one container), cloning (zero-copy file duplicates), and optimized "
            "performance on SSDs and NVMe storage."
        ),
    },
    # ── 1.9 OS Installation & Upgrade ─────────────────────────────────────
    {
        "id": "c2d1-026",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician needs to deploy Windows 11 to 50 new identical workstations "
            "with a pre-configured application set, domain membership, and user settings. "
            "The goal is to minimize setup time per machine. Which installation method "
            "is MOST efficient?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clean install from USB on each machine, then manually install applications.",
                "correct": False,
                "rationale": (
                    "Incorrect. A clean install from USB followed by manual application "
                    "installation does not scale for 50 machines—it maximizes labor per unit."
                ),
            },
            {
                "id": "b",
                "text": "In-place upgrade from Windows 10 on each machine.",
                "correct": False,
                "rationale": (
                    "Incorrect. The machines are new (no existing OS), so an in-place upgrade "
                    "is not applicable."
                ),
            },
            {
                "id": "c",
                "text": "Image-based deployment using a pre-built WIM or WDS image pushed via PXE boot.",
                "correct": True,
                "rationale": (
                    "Correct. Image-based (unattended) deployment via WDS/PXE or Microsoft "
                    "Deployment Toolkit pushes a pre-configured Windows image (WIM) with all "
                    "applications and settings across the network simultaneously, minimizing "
                    "per-machine setup time to minutes."
                ),
            },
            {
                "id": "d",
                "text": "Network install using each machine's optical drive connected to a shared ISO.",
                "correct": False,
                "rationale": (
                    "Incorrect. Modern workstations typically lack optical drives, and a "
                    "shared ISO still requires per-machine clean installation steps without "
                    "the pre-configuration benefit of an image deployment."
                ),
            },
        ],
        "explanation": (
            "Image-based deployment (WIM images distributed via WDS/PXE or MDT) is the "
            "standard enterprise method for identical hardware sets. A reference machine is "
            "configured, captured with sysprep, and the resulting WIM is deployed to all "
            "target machines over the network. PXE boot eliminates physical media entirely. "
            "Unattended answer files (unattend.xml) further automate OOBE and domain join."
        ),
    },
    {
        "id": "c2d1-027",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Partitioning (GPT vs MBR)",
        "stem": (
            "A technician is installing Windows 11 on a new PC with UEFI firmware. "
            "During setup, the installer reports that Windows cannot be installed "
            "on the selected disk because 'the disk is of the GPT partition style'. "
            "Actually, the error shown is the OPPOSITE: 'Windows cannot be installed "
            "to this disk. The selected disk has an MBR partition table. On EFI systems, "
            "Windows can only be installed to GPT disks.' What must the technician do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable UEFI and enable Legacy BIOS (CSM) mode to allow MBR installation.",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 requires UEFI and Secure Boot; it cannot be "
                    "installed in Legacy/CSM mode. Disabling UEFI would cause the install "
                    "to fail for different reasons (TPM 2.0 and Secure Boot requirements)."
                ),
            },
            {
                "id": "b",
                "text": "Boot to the Windows installer, open a command prompt, use diskpart to clean and convert the disk to GPT, then retry setup.",
                "correct": True,
                "rationale": (
                    "Correct. In the Windows installer, press Shift+F10 to open a command "
                    "prompt, run diskpart, select the disk, run 'clean', then 'convert gpt'. "
                    "This converts the MBR disk to GPT (destroying all data) so UEFI-mode "
                    "setup can proceed."
                ),
            },
            {
                "id": "c",
                "text": "Delete all existing partitions in the installer GUI; Windows will automatically convert MBR to GPT.",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting partitions in the installer leaves unallocated space "
                    "but does NOT convert the partition table from MBR to GPT. diskpart's "
                    "'convert gpt' command is required."
                ),
            },
            {
                "id": "d",
                "text": "Install Windows on the MBR disk and run mbr2gpt.exe after installation to convert.",
                "correct": False,
                "rationale": (
                    "Incorrect. mbr2gpt.exe can non-destructively convert a Windows-bootable "
                    "MBR disk to GPT, but the installer itself cannot proceed on an MBR disk "
                    "in UEFI mode. The conversion must happen before installation completes."
                ),
            },
        ],
        "explanation": (
            "UEFI firmware requires GPT partition tables; BIOS/Legacy requires MBR. "
            "Windows 11 mandates UEFI + Secure Boot, so all system disks must be GPT. "
            "During setup, Shift+F10 opens a command prompt → diskpart → select disk → "
            "clean → convert gpt resolves the error. mbr2gpt.exe works post-install for "
            "converting existing Windows installations non-destructively."
        ),
    },
    {
        "id": "c2d1-028",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician performs an in-place upgrade from Windows 10 to Windows 11. "
            "After the upgrade, the user reports that several applications stopped working "
            "and a legacy USB scanner driver is gone. Where does Windows store the old "
            "installation files to allow rollback, and what is the default retention period?"
        ),
        "options": [
            {
                "id": "a",
                "text": "C:\\$RECYCLE.BIN; retained for 30 days before auto-deletion.",
                "correct": False,
                "rationale": (
                    "Incorrect. $RECYCLE.BIN is the Recycle Bin for user-deleted files, not "
                    "the in-place upgrade rollback storage."
                ),
            },
            {
                "id": "b",
                "text": "C:\\Windows.old; retained for 10 days before Windows Storage Sense or Disk Cleanup removes it.",
                "correct": True,
                "rationale": (
                    "Correct. Windows saves the previous installation in C:\\Windows.old. "
                    "The rollback option ('Go back to Windows 10') in Settings → System → "
                    "Recovery is available for 10 days; after that, Windows.old is "
                    "automatically removed."
                ),
            },
            {
                "id": "c",
                "text": "C:\\WinSxS; retained indefinitely until manually cleaned with Disk Cleanup.",
                "correct": False,
                "rationale": (
                    "Incorrect. WinSxS is the Windows component store (side-by-side), used "
                    "for feature installations and updates—not the in-place upgrade rollback folder."
                ),
            },
            {
                "id": "d",
                "text": "C:\\Recovery; retained for 30 days and protected by the recovery agent.",
                "correct": False,
                "rationale": (
                    "Incorrect. C:\\Recovery typically contains recovery tools and the WinRE "
                    "image, not the previous OS installation files."
                ),
            },
        ],
        "explanation": (
            "In-place upgrades save the previous Windows installation to C:\\Windows.old. "
            "Users can roll back within 10 days via Settings → System → Recovery → "
            "'Go back'. After 10 days, Windows.old is automatically deleted by Storage "
            "Sense or Disk Cleanup. To extend the rollback window, the folder can be "
            "preserved manually, but Microsoft does not support longer windows officially."
        ),
    },
    # ── 1.10 macOS Features & Tools ───────────────────────────────────────
    {
        "id": "c2d1-029",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A macOS user accidentally deleted a critical Keynote presentation and "
            "emptied the Trash. The Mac has Time Machine configured to a USB external "
            "drive. Which steps recover the file?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open Finder → right-click the external drive → Restore from Time Machine.",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no 'Restore from Time Machine' option in the "
                    "Finder right-click context menu on the external drive itself."
                ),
            },
            {
                "id": "b",
                "text": "Open Time Machine from System Settings → navigate back to the date before deletion → locate the file → click Restore.",
                "correct": True,
                "rationale": (
                    "Correct. Launching Time Machine (from the menu bar icon or System "
                    "Settings) opens the time-travel interface where the user can navigate "
                    "to a previous backup, find the deleted file, and click Restore to "
                    "recover it to its original location."
                ),
            },
            {
                "id": "c",
                "text": "Boot to macOS Recovery (Cmd+R) and use Disk Utility to restore the entire volume from Time Machine.",
                "correct": False,
                "rationale": (
                    "Incorrect. Restoring the entire volume from macOS Recovery would "
                    "overwrite all data since that backup—a disproportionate action to "
                    "recover a single file. The Time Machine app supports granular "
                    "single-file recovery."
                ),
            },
            {
                "id": "d",
                "text": "Use Spotlight to search for the file; deleted files remain indexed until the index is rebuilt.",
                "correct": False,
                "rationale": (
                    "Incorrect. Spotlight indexes live files; once a file is deleted and "
                    "the Trash is emptied, it is removed from the Spotlight index and "
                    "cannot be found or recovered via Spotlight."
                ),
            },
        ],
        "explanation": (
            "Time Machine provides versioned backups with an intuitive time-travel GUI. "
            "Users can recover individual files, folders, or entire volumes. For a single "
            "file, launching the Time Machine interface, browsing to the last good backup "
            "date, and clicking Restore is the correct granular recovery method—no need "
            "to restore the entire volume."
        ),
    },
    {
        "id": "c2d1-030",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A macOS user downloads a DMG application from a developer's personal website. "
            "When they try to open it, macOS displays: 'Cannot be opened because the developer "
            "cannot be verified.' The user trusts the developer. Which macOS security "
            "feature is blocking the app and what is the SAFEST way to allow it?"
        ),
        "options": [
            {
                "id": "a",
                "text": "FileVault is blocking the app; disable FileVault temporarily to run unsigned apps.",
                "correct": False,
                "rationale": (
                    "Incorrect. FileVault is full-disk encryption; it has nothing to do with "
                    "application code signing verification."
                ),
            },
            {
                "id": "b",
                "text": "Gatekeeper is blocking the app; right-click the app → Open, then confirm in the dialog to run it this once.",
                "correct": True,
                "rationale": (
                    "Correct. Gatekeeper enforces code signing and notarization checks. "
                    "Right-clicking (or Control-clicking) the app and selecting Open bypasses "
                    "the standard Gatekeeper block for this specific app and allows the user "
                    "to confirm they trust it, rather than disabling Gatekeeper system-wide."
                ),
            },
            {
                "id": "c",
                "text": "Gatekeeper is blocking the app; open System Settings → Privacy & Security → disable Gatekeeper entirely.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling Gatekeeper entirely removes protection for ALL "
                    "future downloads. The right-click → Open method is safer because it "
                    "grants an exception only for that specific app."
                ),
            },
            {
                "id": "d",
                "text": "Keychain is blocking the app because the developer's certificate is not in the trusted keychain; import the certificate manually.",
                "correct": False,
                "rationale": (
                    "Incorrect. Keychain manages stored credentials and certificates, but "
                    "the Gatekeeper mechanism (not a missing Keychain certificate) triggers "
                    "the 'developer cannot be verified' message for unsigned/unnotarized apps."
                ),
            },
        ],
        "explanation": (
            "Gatekeeper is the macOS feature that enforces code-signing and notarization. "
            "Apps from outside the App Store must be signed and notarized for automatic "
            "approval. For a trusted but unnotarized app, right-click → Open presents an "
            "override dialog specific to that app, leaving Gatekeeper active for all other "
            "downloads. Disabling Gatekeeper system-wide is a security risk."
        ),
    },
    {
        "id": "c2d1-031",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A technician needs to install the 'wget' command-line utility on macOS Ventura. "
            "macOS does not include wget by default. Which tool is the de-facto package "
            "manager for installing open-source Unix utilities on macOS?"
        ),
        "options": [
            {
                "id": "a",
                "text": "App Store (mas command-line tool)",
                "correct": False,
                "rationale": (
                    "Incorrect. The App Store (and the mas CLI) distributes sandboxed macOS "
                    "applications; it does not manage Unix/command-line utilities like wget."
                ),
            },
            {
                "id": "b",
                "text": "Homebrew (brew install wget)",
                "correct": True,
                "rationale": (
                    "Correct. Homebrew is the most widely used third-party package manager "
                    "for macOS. 'brew install wget' downloads, compiles/installs, and links "
                    "wget to /usr/local/bin (Intel) or /opt/homebrew/bin (Apple Silicon)."
                ),
            },
            {
                "id": "c",
                "text": "MacPorts (port install wget) — the only supported method on Apple Silicon.",
                "correct": False,
                "rationale": (
                    "Incorrect. MacPorts is a valid alternative package manager, but it is "
                    "NOT the only supported method on Apple Silicon—Homebrew supports Apple "
                    "Silicon natively since Homebrew 3.0. MacPorts is not the 'de-facto' standard."
                ),
            },
            {
                "id": "d",
                "text": "Disk Utility → Install Package (pkg) → locate wget.pkg",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk Utility manages disks and volumes; it does not install "
                    "software packages and has no 'Install Package' feature."
                ),
            },
        ],
        "explanation": (
            "Homebrew (brew) is the de-facto open-source package manager for macOS and Linux. "
            "It installs Unix tools, libraries, and applications not included with macOS. "
            "'brew install wget' resolves dependencies and installs the binary. "
            "MacPorts is an older alternative but less commonly used. The App Store handles "
            "sandboxed GUI apps, not command-line tools."
        ),
    },
    # ── 1.11 Linux Commands ───────────────────────────────────────────────
    {
        "id": "c2d1-032",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator runs 'ls -la /var/www/html/config.php' and sees:\n"
            "-rwxr--r-- 1 www-data developers 4096 May 10 09:00 config.php\n"
            "The file must be readable and writable ONLY by the owner, with no access "
            "for group or others. Which chmod command sets the correct permissions?"
        ),
        "options": [
            {
                "id": "a",
                "text": "chmod 644 config.php",
                "correct": False,
                "rationale": (
                    "Incorrect. 644 = rw-r--r-- (owner read/write, group read, others read). "
                    "This grants read access to group and others, violating the requirement."
                ),
            },
            {
                "id": "b",
                "text": "chmod 600 config.php",
                "correct": True,
                "rationale": (
                    "Correct. 600 = rw------- (owner read/write, no permissions for group "
                    "or others). This satisfies: readable and writable by owner only."
                ),
            },
            {
                "id": "c",
                "text": "chmod 700 config.php",
                "correct": False,
                "rationale": (
                    "Incorrect. 700 = rwx------ (owner read/write/execute). Adding execute "
                    "permission to a PHP config file is unnecessary and potentially a "
                    "security risk; the requirement specifies read and write only."
                ),
            },
            {
                "id": "d",
                "text": "chmod 400 config.php",
                "correct": False,
                "rationale": (
                    "Incorrect. 400 = r-------- (owner read only). This denies write access "
                    "to the owner, violating the 'readable and writable by owner' requirement."
                ),
            },
        ],
        "explanation": (
            "Linux permissions use octal notation: owner/group/others, each as r(4)+w(2)+x(1). "
            "chmod 600 sets rw------- : owner has read (4) + write (2) = 6; group = 0; "
            "others = 0. This is the secure standard for private config files containing "
            "credentials or keys."
        ),
    },
    {
        "id": "c2d1-033",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux file permissions",
        "stem": (
            "A junior Linux admin wants to give another user named 'alice' ownership of "
            "the file /opt/app/data.db. The admin is logged in as root. "
            "Which command correctly changes the file owner to alice AND the group to 'appgroup'?"
        ),
        "options": [
            {
                "id": "a",
                "text": "chmod alice:appgroup /opt/app/data.db",
                "correct": False,
                "rationale": (
                    "Incorrect. chmod changes file permissions (read/write/execute bits), "
                    "not ownership. It does not accept a username as an argument in this format."
                ),
            },
            {
                "id": "b",
                "text": "chown alice /opt/app/data.db && chgrp appgroup /opt/app/data.db",
                "correct": False,
                "rationale": (
                    "Incorrect. This works but is verbose; chown supports user:group syntax "
                    "in a single command, making this approach unnecessarily complex."
                ),
            },
            {
                "id": "c",
                "text": "chown alice:appgroup /opt/app/data.db",
                "correct": True,
                "rationale": (
                    "Correct. chown user:group file changes both the owner and group in a "
                    "single command. 'chown alice:appgroup /opt/app/data.db' sets owner "
                    "to alice and group to appgroup atomically."
                ),
            },
            {
                "id": "d",
                "text": "usermod -G appgroup alice && mv /opt/app/data.db /home/alice/",
                "correct": False,
                "rationale": (
                    "Incorrect. usermod -G appgroup modifies alice's group membership but "
                    "does not change file ownership. Moving the file to alice's home "
                    "directory is not equivalent to changing ownership and is destructive "
                    "to the application path."
                ),
            },
        ],
        "explanation": (
            "chown (change owner) accepts the syntax 'user:group' to set both owner and "
            "group simultaneously. chown alice:appgroup /opt/app/data.db is the canonical "
            "single-command solution. chmod changes permission bits only; chgrp changes "
            "group only. Only root or the current file owner can use chown."
        ),
    },
    {
        "id": "c2d1-034",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux technician needs to install security updates on an Ubuntu 22.04 LTS "
            "server. Which sequence of commands correctly refreshes the package list and "
            "installs available security updates?"
        ),
        "options": [
            {
                "id": "a",
                "text": "sudo yum update -y && sudo yum upgrade -y",
                "correct": False,
                "rationale": (
                    "Incorrect. yum is the package manager for Red Hat/CentOS/Fedora "
                    "distributions. Ubuntu uses the APT package manager (apt/apt-get)."
                ),
            },
            {
                "id": "b",
                "text": "sudo apt-get update && sudo apt-get upgrade -y",
                "correct": True,
                "rationale": (
                    "Correct. On Ubuntu (Debian-based), 'apt-get update' refreshes the "
                    "package index from repositories, and 'apt-get upgrade -y' installs "
                    "available upgrades including security patches. The -y flag confirms "
                    "all prompts non-interactively."
                ),
            },
            {
                "id": "c",
                "text": "sudo dnf update --security -y",
                "correct": False,
                "rationale": (
                    "Incorrect. dnf is the package manager for Fedora, RHEL 8+, and "
                    "CentOS Stream. Ubuntu uses apt/apt-get, not dnf."
                ),
            },
            {
                "id": "d",
                "text": "sudo brew update && sudo brew upgrade",
                "correct": False,
                "rationale": (
                    "Incorrect. Homebrew (brew) is a third-party package manager primarily "
                    "for macOS (and optionally Linux), not the native Ubuntu package manager. "
                    "Also, brew should not be run with sudo."
                ),
            },
        ],
        "explanation": (
            "Ubuntu (and other Debian-based distributions) use APT (Advanced Package Tool). "
            "'apt-get update' synchronizes the local package database with repositories. "
            "'apt-get upgrade' installs newer versions of installed packages. "
            "yum and dnf are Red Hat family tools; brew is for macOS. "
            "For security-only updates, 'apt-get upgrade' with unattended-upgrades configured "
            "or 'apt-get install --only-upgrade <pkg>' can be used."
        ),
    },
    {
        "id": "c2d1-035",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux technician needs to find all files modified in the last 24 hours "
            "within /var/log that contain the string 'FAILED'. "
            "Which command achieves this efficiently in one pipeline?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ls /var/log | grep FAILED",
                "correct": False,
                "rationale": (
                    "Incorrect. This searches for 'FAILED' in filenames only, not file "
                    "contents, and does not filter by modification time."
                ),
            },
            {
                "id": "b",
                "text": "find /var/log -mtime -1 -exec grep -l 'FAILED' {} \\;",
                "correct": True,
                "rationale": (
                    "Correct. 'find /var/log -mtime -1' finds files modified within the "
                    "last 24 hours (-mtime -1 means less than 1 day ago). '-exec grep -l "
                    "FAILED {} \\;' searches each found file for the string 'FAILED' and "
                    "prints only filenames containing it."
                ),
            },
            {
                "id": "c",
                "text": "cat /var/log/* | grep -r FAILED --include='*.log'",
                "correct": False,
                "rationale": (
                    "Incorrect. cat piped to grep does not filter by modification time and "
                    "grep -r cannot be used meaningfully after cat. Also, grep -r already "
                    "recurses directories without needing cat."
                ),
            },
            {
                "id": "d",
                "text": "grep -rl FAILED /var/log",
                "correct": False,
                "rationale": (
                    "Incorrect. grep -rl recursively searches all files in /var/log for "
                    "'FAILED' and lists matching filenames, but it does not filter by "
                    "modification time (last 24 hours)."
                ),
            },
        ],
        "explanation": (
            "The 'find' command with '-mtime -1' (files modified less than 1 full day ago) "
            "combined with '-exec grep -l' (search content, list filename) accomplishes both "
            "filtering tasks in one pipeline. '-mtime 0' would mean today only; '-mtime -1' "
            "includes the past 24 hours. grep -rl alone cannot filter by timestamp."
        ),
    },
    # ── Multiple Response Questions (6) ───────────────────────────────────
    {
        "id": "c2d1-036",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "A systems administrator is evaluating which Windows 11 editions can act as "
            "an RDP host (accept incoming Remote Desktop connections from other machines) "
            "AND support joining an Active Directory domain. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows 11 Home",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Home does not support acting as an RDP host "
                    "(it can only use RDP as a client) and cannot join an Active Directory domain."
                ),
            },
            {
                "id": "b",
                "text": "Windows 11 Pro",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 Pro supports both acting as an RDP host and joining "
                    "an Active Directory domain."
                ),
            },
            {
                "id": "c",
                "text": "Windows 11 Pro for Workstations",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 Pro for Workstations supports both RDP host "
                    "functionality and Active Directory domain join, in addition to its "
                    "enhanced hardware support."
                ),
            },
            {
                "id": "d",
                "text": "Windows 11 SE",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 SE is designed for education devices (low-cost "
                    "hardware managed by institutions); it does not support acting as an "
                    "RDP host for general enterprise use."
                ),
            },
        ],
        "explanation": (
            "RDP host capability (accepting inbound RDP connections) requires Windows Pro "
            "or higher—Home editions are RDP client-only. Both Windows 11 Pro and "
            "Pro for Workstations (and Enterprise) support RDP hosting and AD domain join. "
            "Windows 11 SE is a restricted education SKU without these enterprise features."
        ),
    },
    {
        "id": "c2d1-037",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A technician is comparing file system features. Which TWO file systems "
            "natively support journaling to aid in recovery after an unexpected power loss? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "FAT32",
                "correct": False,
                "rationale": (
                    "Incorrect. FAT32 does not support journaling. It is particularly "
                    "vulnerable to corruption from interrupted writes because there is "
                    "no transaction log."
                ),
            },
            {
                "id": "b",
                "text": "NTFS",
                "correct": True,
                "rationale": (
                    "Correct. NTFS uses a transaction log ($LogFile) that records metadata "
                    "changes before they are committed, enabling roll-back of incomplete "
                    "transactions after a crash."
                ),
            },
            {
                "id": "c",
                "text": "ext4",
                "correct": True,
                "rationale": (
                    "Correct. ext4 (and its predecessors ext3) use a journal (the journal "
                    "inode) to record file system transactions, providing crash consistency "
                    "and fast recovery compared to ext2."
                ),
            },
            {
                "id": "d",
                "text": "exFAT",
                "correct": False,
                "rationale": (
                    "Incorrect. exFAT does not include a journaling mechanism. It uses a "
                    "simple allocation table and is not crash-consistent in the way NTFS "
                    "or ext4 are."
                ),
            },
        ],
        "explanation": (
            "Journaling file systems write metadata changes to a log before applying them, "
            "allowing recovery after crashes. NTFS uses $LogFile for metadata journaling; "
            "ext3/ext4 use the jbd2 journal. FAT32 and exFAT lack journaling—both use "
            "simple allocation tables and are vulnerable to corruption from interrupted writes."
        ),
    },
    {
        "id": "c2d1-038",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician is planning a Windows 11 deployment. Which TWO methods can "
            "be used to boot a machine and install Windows without requiring physical "
            "optical media or a USB drive? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "PXE (Preboot Execution Environment) boot from Windows Deployment Services (WDS).",
                "correct": True,
                "rationale": (
                    "Correct. PXE boot allows a machine to load a Windows PE environment "
                    "over the network from a WDS server, then install Windows from a network "
                    "share—no physical media needed."
                ),
            },
            {
                "id": "b",
                "text": "Network boot via HTTP from a Windows Assessment and Deployment Kit (ADK) distribution share.",
                "correct": True,
                "rationale": (
                    "Correct. Modern deployment tools (WDS, MDT, SCCM) can serve Windows PE "
                    "and installation files over HTTP/HTTPS, enabling media-free deployments. "
                    "This is supported via TFTP/HTTP boot in the DHCP/WDS configuration."
                ),
            },
            {
                "id": "c",
                "text": "Booting from a printed QR code that links to the Windows installer.",
                "correct": False,
                "rationale": (
                    "Incorrect. A QR code is a visual reference tool and cannot be used as "
                    "a boot medium. Computers boot from storage devices or network interfaces, "
                    "not printed codes."
                ),
            },
            {
                "id": "d",
                "text": "Inserting a Windows 11 product key triggers an automatic OTA install from Microsoft servers.",
                "correct": False,
                "rationale": (
                    "Incorrect. A product key alone does not trigger a full OS installation. "
                    "Keys activate an already-installed OS; they do not bootstrap a bare-metal "
                    "installation."
                ),
            },
        ],
        "explanation": (
            "Media-free OS deployment methods include PXE (network boot using TFTP + boot "
            "image from WDS/SCCM) and network HTTP/HTTPS distribution shares via MDT or "
            "SCCM. Both allow a bare-metal machine to boot and install Windows using only "
            "the NIC. Physical USB or optical media are not required."
        ),
    },
    {
        "id": "c2d1-039",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A technician needs to investigate why a Windows workstation is running slowly. "
            "Which TWO tools provide real-time CPU, memory, disk, and network utilization "
            "data to identify the bottleneck? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource Monitor (resmon.exe)",
                "correct": True,
                "rationale": (
                    "Correct. Resource Monitor provides real-time, per-process breakdowns of "
                    "CPU, memory (working set, commit), disk (I/O per process), and network "
                    "(bytes sent/received per process and connection), making it ideal for "
                    "identifying the bottleneck."
                ),
            },
            {
                "id": "b",
                "text": "Performance Monitor (perfmon.exe)",
                "correct": True,
                "rationale": (
                    "Correct. Performance Monitor offers real-time and historical performance "
                    "counter graphs and data collector sets for CPU, memory, disk, and "
                    "network metrics with customizable counters."
                ),
            },
            {
                "id": "c",
                "text": "MSConfig (System Configuration)",
                "correct": False,
                "rationale": (
                    "Incorrect. MSConfig manages boot options and startup services—it does "
                    "not provide real-time performance monitoring."
                ),
            },
            {
                "id": "d",
                "text": "Event Viewer",
                "correct": False,
                "rationale": (
                    "Incorrect. Event Viewer shows logged errors and warnings but does not "
                    "provide real-time utilization metrics for CPU, memory, disk, or network."
                ),
            },
        ],
        "explanation": (
            "Resource Monitor and Performance Monitor both provide real-time hardware utilization "
            "data. Resource Monitor (launched from Task Manager → Performance → Open Resource "
            "Monitor) gives per-process breakdowns across all four subsystems. "
            "Performance Monitor offers customizable counters and data logging for trend analysis. "
            "MSConfig and Event Viewer are diagnostic and configuration tools, not real-time monitors."
        ),
    },
    {
        "id": "c2d1-040",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator needs to identify which processes are currently running "
            "and consuming the most CPU on a production server. Which TWO commands display "
            "running process information? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "top",
                "correct": True,
                "rationale": (
                    "Correct. top is an interactive real-time process viewer that displays "
                    "running processes sorted by CPU usage (by default), along with memory "
                    "consumption, PID, and more. It updates every few seconds."
                ),
            },
            {
                "id": "b",
                "text": "ps aux",
                "correct": True,
                "rationale": (
                    "Correct. 'ps aux' (BSD syntax) lists all running processes for all "
                    "users with CPU% and memory% columns, providing a point-in-time "
                    "snapshot useful for piping to grep or sort."
                ),
            },
            {
                "id": "c",
                "text": "df -h",
                "correct": False,
                "rationale": (
                    "Incorrect. df (disk free) reports file system disk space usage—it "
                    "does not display process information."
                ),
            },
            {
                "id": "d",
                "text": "chmod 755",
                "correct": False,
                "rationale": (
                    "Incorrect. chmod modifies file permission bits; it is not related to "
                    "process monitoring."
                ),
            },
        ],
        "explanation": (
            "top provides an interactive, continuously refreshing view of running processes "
            "ordered by CPU consumption. 'ps aux' produces a full process listing snapshot "
            "that can be sorted and filtered with other commands (e.g., 'ps aux --sort=-%cpu'). "
            "df -h reports disk utilization; chmod manages permissions—neither relates to "
            "process monitoring."
        ),
    },
    {
        "id": "c2d1-041",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A technician is troubleshooting internet connectivity on a Windows workstation. "
            "Which TWO ipconfig switches display DNS resolver cache and force renewal "
            "of DHCP-assigned IP configuration respectively? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ipconfig /displaydns",
                "correct": True,
                "rationale": (
                    "Correct. ipconfig /displaydns shows all entries currently cached in "
                    "the local DNS resolver cache, including TTL values and resolved addresses. "
                    "This helps diagnose stale DNS records."
                ),
            },
            {
                "id": "b",
                "text": "ipconfig /renew",
                "correct": True,
                "rationale": (
                    "Correct. ipconfig /renew sends a DHCP Request to renew the DHCP lease "
                    "for all network adapters, refreshing the IP address, subnet mask, "
                    "gateway, and DNS server assignments."
                ),
            },
            {
                "id": "c",
                "text": "ipconfig /release6",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /release6 releases the DHCPv6 lease (IPv6 only). "
                    "It does not display the DNS cache or renew an IPv4 DHCP lease."
                ),
            },
            {
                "id": "d",
                "text": "ipconfig /registerdns",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /registerdns forces a re-registration of the "
                    "computer's DNS name with the DNS server—it does not display the DNS "
                    "cache or renew the DHCP lease."
                ),
            },
        ],
        "explanation": (
            "ipconfig /displaydns shows the local DNS resolver cache (useful for diagnosing "
            "stale or poisoned records). ipconfig /renew requests a new DHCP lease, refreshing "
            "all IP configuration from the DHCP server. ipconfig /flushdns clears the cache; "
            "/release releases the DHCP lease; /registerdns re-registers the hostname in DNS."
        ),
    },
    # ── Remaining Hard Questions ──────────────────────────────────────────
    {
        "id": "c2d1-042",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A Windows 10 workstation displays an error that the system cannot boot and "
            "suggests running 'bootrec'. A technician boots from a Windows USB installation "
            "drive and opens a command prompt. The BCD (Boot Configuration Data) store is "
            "corrupt. Which bootrec command rebuilds the BCD from scratch?"
        ),
        "options": [
            {
                "id": "a",
                "text": "bootrec /fixmbr",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec /fixmbr writes a new Master Boot Record to the "
                    "system partition. It does not repair or rebuild the Boot Configuration "
                    "Data (BCD) store."
                ),
            },
            {
                "id": "b",
                "text": "bootrec /fixboot",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec /fixboot writes a new boot sector to the system "
                    "partition (for NTFS/FAT). It repairs the volume boot record but does "
                    "not rebuild the BCD store."
                ),
            },
            {
                "id": "c",
                "text": "bootrec /rebuildbcd",
                "correct": True,
                "rationale": (
                    "Correct. bootrec /rebuildbcd scans all disks for Windows installations "
                    "and prompts the technician to add them to the BCD store, effectively "
                    "rebuilding a corrupt or missing BCD."
                ),
            },
            {
                "id": "d",
                "text": "bootrec /scanos",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec /scanos scans for Windows installations not currently "
                    "in the BCD store but only reports them—it does not add them or rebuild "
                    "the BCD store."
                ),
            },
        ],
        "explanation": (
            "bootrec.exe has four switches: /fixmbr (writes new MBR), /fixboot (writes new "
            "volume boot record), /scanos (lists Windows installs not in BCD), and "
            "/rebuildbcd (scans and lets you add installations to a new BCD). /rebuildbcd "
            "is the command that actually reconstructs the BCD store when it is corrupt "
            "or missing."
        ),
    },
    {
        "id": "c2d1-043",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Control Panel utilities",
        "stem": (
            "An administrator configures Windows Defender Firewall with Advanced Security "
            "to block all outbound traffic except explicitly allowed applications. A "
            "new line-of-business app at C:\\LOBApp\\lob.exe cannot reach its cloud "
            "service. The technician wants to allow only HTTPS (TCP 443) outbound for "
            "this specific executable. Which firewall rule configuration accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Inbound rule → Program: C:\\LOBApp\\lob.exe → Protocol: TCP → Local port: 443 → Action: Allow.",
                "correct": False,
                "rationale": (
                    "Incorrect. Inbound rules control traffic coming INTO the machine. "
                    "The app needs to reach out to the cloud service, so an OUTBOUND rule "
                    "is required."
                ),
            },
            {
                "id": "b",
                "text": "Outbound rule → Program: C:\\LOBApp\\lob.exe → Protocol: TCP → Remote port: 443 → Action: Allow.",
                "correct": True,
                "rationale": (
                    "Correct. An outbound rule specifying the program path (lob.exe), "
                    "protocol TCP, and REMOTE port 443 (the destination port the app "
                    "connects to) allows only HTTPS traffic from that specific executable "
                    "outbound."
                ),
            },
            {
                "id": "c",
                "text": "Outbound rule → All Programs → Protocol: TCP → Remote port: 443 → Action: Allow.",
                "correct": False,
                "rationale": (
                    "Incorrect. Applying the rule to 'All Programs' would allow ANY "
                    "application to make HTTPS outbound connections, which violates the "
                    "principle of least privilege and the requirement to restrict to a "
                    "specific executable."
                ),
            },
            {
                "id": "d",
                "text": "Disable the outbound block default rule; all traffic will then be permitted.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling the default outbound block removes all outbound "
                    "filtering, which is insecure. The administrator wants selective "
                    "allow rules, not to eliminate outbound control entirely."
                ),
            },
        ],
        "explanation": (
            "Windows Defender Firewall with Advanced Security (wf.msc) supports program-specific "
            "outbound rules. Specifying the full executable path restricts the rule to that "
            "binary; setting Protocol: TCP and Remote Port: 443 limits it to HTTPS only. "
            "Local port refers to the source port on this machine; Remote port is the "
            "destination—for client-to-server HTTPS, the remote (server) port is 443."
        ),
    },
    {
        "id": "c2d1-044",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "During a Windows 11 unattended installation using an answer file (unattend.xml), "
            "the technician needs to inject a third-party RAID controller driver that "
            "Windows does not include natively, so the installer can see the disk array. "
            "At which installation phase must the driver be available?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OOBE (Out-of-Box Experience) phase, after Windows files are copied.",
                "correct": False,
                "rationale": (
                    "Incorrect. OOBE runs after Windows is installed; the RAID controller "
                    "driver must be present before the installer can even detect the disk "
                    "to write files to it."
                ),
            },
            {
                "id": "b",
                "text": "Windows PE (WinPE) phase, specifically during the 'windowsPE' configuration pass.",
                "correct": True,
                "rationale": (
                    "Correct. The Windows installer runs inside Windows PE. Storage "
                    "controller drivers must be injected during the windowsPE configuration "
                    "pass so that WinPE can detect and write to the RAID array before "
                    "installation begins."
                ),
            },
            {
                "id": "c",
                "text": "Specialize phase, when the system customizes hardware settings for the local machine.",
                "correct": False,
                "rationale": (
                    "Incorrect. The specialize phase runs after Windows is installed and "
                    "files are copied. The driver must be present in the WinPE phase so "
                    "the disk is visible during the initial installation."
                ),
            },
            {
                "id": "d",
                "text": "Audit mode, when the technician adds drivers before handing the system to the user.",
                "correct": False,
                "rationale": (
                    "Incorrect. Audit mode is a post-installation OEM customization phase. "
                    "The RAID driver must be available during WinPE so the disk array is "
                    "accessible during setup."
                ),
            },
        ],
        "explanation": (
            "Windows Setup runs inside Windows PE. If the setup cannot see the target disk "
            "(because the RAID controller driver is missing from WinPE), it cannot proceed. "
            "Drivers for storage controllers must be injected into the WinPE image using "
            "DISM (Add-WindowsDriver) or provided via the 'Load driver' button during setup, "
            "which corresponds to the 'windowsPE' configuration pass in an answer file. "
            "Later passes (specialize, OOBE, audit) run only after the disk is accessible."
        ),
    },
]
