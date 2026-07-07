"""
CompTIA A+ Core 2 (220-1202) – Performance-Based Questions (PBQs)
12 questions: ~4 pbq_matching, ~4 pbq_categorize, ~4 pbq_ordering
Domains 1-4 represented.
"""

QUESTIONS = [
    # ── PBQ_MATCHING ──────────────────────────────────────────────────────────

    {
        "id": "c2pbq-001",
        "domain": 1,
        "objective": "1.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician is troubleshooting a Windows 11 workstation. "
            "Match each command-line tool to its single correct purpose."
        ),
        "prompts": [
            {"id": "p1", "text": "sfc /scannow"},
            {"id": "p2", "text": "DISM /Online /Cleanup-Image /RestoreHealth"},
            {"id": "p3", "text": "bcdedit /enum"},
            {"id": "p4", "text": "net user Administrator /active:yes"},
            {"id": "p5", "text": "taskkill /IM notepad.exe /F"},
        ],
        "targets": [
            {"id": "t1", "text": "Scan and repair protected Windows system files using cached copies"},
            {"id": "t2", "text": "Repair the Windows component store (WinSxS) by downloading clean files"},
            {"id": "t3", "text": "List all Boot Configuration Data store entries"},
            {"id": "t4", "text": "Enable the built-in local Administrator account"},
            {"id": "t5", "text": "Forcefully terminate a running process by image name"},
            {"id": "t6", "text": "Display current TCP/IP configuration and release/renew DHCP lease"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "sfc /scannow uses the Windows File Protection cache to verify and restore protected system files in place.",
            "p2": "DISM /RestoreHealth contacts Windows Update (or a supplied source) to repair the component store that sfc draws from.",
            "p3": "bcdedit /enum displays every entry in the BCD store, showing boot managers, OS loaders, and their GUIDs.",
            "p4": "'net user Administrator /active:yes' re-enables the disabled built-in Administrator account without changing its password.",
            "p5": "taskkill /IM <image> /F sends a force-terminate signal to every process matching that executable name.",
        },
        "explanation": (
            "Know which command targets which layer: sfc repairs individual system files; "
            "DISM repairs the component store sfc relies on; bcdedit manages boot entries; "
            "net user manages local accounts; taskkill ends runaway processes. "
            "t6 (ipconfig) is a distractor—not used by any prompt here."
        ),
    },

    {
        "id": "c2pbq-002",
        "domain": 1,
        "objective": "1.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "Match each Windows administrative tool or snap-in to its primary function."
        ),
        "prompts": [
            {"id": "p1", "text": "eventvwr.msc"},
            {"id": "p2", "text": "services.msc"},
            {"id": "p3", "text": "lusrmgr.msc"},
            {"id": "p4", "text": "gpedit.msc"},
            {"id": "p5", "text": "perfmon.msc"},
        ],
        "targets": [
            {"id": "t1", "text": "View Windows application, security, and system event logs"},
            {"id": "t2", "text": "Start, stop, and configure startup type of Windows services"},
            {"id": "t3", "text": "Manage local user accounts and groups"},
            {"id": "t4", "text": "Configure local Group Policy settings"},
            {"id": "t5", "text": "Monitor real-time CPU, memory, disk, and network performance counters"},
            {"id": "t6", "text": "Manage hard disk partitions and drive letters"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "Event Viewer (eventvwr.msc) aggregates Application, Security, Setup, and System logs for diagnosis.",
            "p2": "The Services snap-in (services.msc) lets you configure each service's startup type and account, and start/stop on demand.",
            "p3": "Local Users and Groups (lusrmgr.msc) manages local accounts and group membership; unavailable on Home editions.",
            "p4": "Local Group Policy Editor (gpedit.msc) sets security and configuration policies enforced by the OS; Pro/Enterprise only.",
            "p5": "Performance Monitor (perfmon.msc) graphs real-time and logged performance counters across all subsystems.",
        },
        "explanation": (
            "Each msc file is a distinct MMC snap-in. t6 (disk partitions) belongs to diskmgmt.msc, "
            "which is deliberately omitted from the prompts as a distractor. "
            "lusrmgr vs gpedit is a common confusion point—they control different things."
        ),
    },

    {
        "id": "c2pbq-003",
        "domain": 2,
        "objective": "2.3",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Social engineering & attacks",
        "stem": (
            "A security awareness trainer presents attack scenarios. "
            "Match each scenario to the attack type it best illustrates."
        ),
        "prompts": [
            {"id": "p1", "text": "An attacker calls the help desk pretending to be an executive and requests a password reset."},
            {"id": "p2", "text": "A malicious open Wi-Fi hotspot at a coffee shop uses the same SSID as the legitimate network."},
            {"id": "p3", "text": "An unauthorized person follows an employee through a badge-controlled door without swiping."},
            {"id": "p4", "text": "An attacker watches a user type their PIN from a nearby table."},
            {"id": "p5", "text": "A mass email impersonates a bank and directs recipients to a fake login page."},
        ],
        "targets": [
            {"id": "t1", "text": "Vishing (voice phishing)"},
            {"id": "t2", "text": "Evil twin attack"},
            {"id": "t3", "text": "Tailgating / piggybacking"},
            {"id": "t4", "text": "Shoulder surfing"},
            {"id": "t5", "text": "Phishing"},
            {"id": "t6", "text": "Whaling"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "Vishing uses voice calls (phone/VoIP) to manipulate victims—here impersonating a high-ranking user to social-engineer IT.",
            "p2": "An evil twin is a rogue AP broadcasting a legitimate-looking SSID to intercept traffic via MitM.",
            "p3": "Tailgating (piggybacking) is physical intrusion by following an authorized person through a secured entry.",
            "p4": "Shoulder surfing is directly observing someone's screen, keyboard, or PIN pad to steal credentials.",
            "p5": "Phishing is a broad, mass-distributed fraudulent message (email most commonly) luring users to fake sites.",
        },
        "explanation": (
            "Whaling (t6) is phishing specifically targeting senior executives—not used here because p1 describes the attacker, "
            "not the victim. Vishing vs phishing: medium is the differentiator (voice vs email/web). "
            "Evil twin vs phishing: evil twin is a rogue wireless AP, not a message."
        ),
    },

    {
        "id": "c2pbq-004",
        "domain": 1,
        "objective": "1.4",
        "type": "pbq_matching",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A technician is administering a Linux workstation. "
            "Match each command to its primary function."
        ),
        "prompts": [
            {"id": "p1", "text": "chmod 640 report.txt"},
            {"id": "p2", "text": "chown alice:finance report.txt"},
            {"id": "p3", "text": "ps aux"},
            {"id": "p4", "text": "grep -r 'error' /var/log/"},
            {"id": "p5", "text": "dd if=/dev/sda of=/dev/sdb bs=4M"},
        ],
        "targets": [
            {"id": "t1", "text": "Set file permissions: owner read/write, group read-only, others none"},
            {"id": "t2", "text": "Transfer ownership of a file to user alice and group finance"},
            {"id": "t3", "text": "Display all running processes with full details for every user"},
            {"id": "t4", "text": "Recursively search all files under /var/log/ for the string 'error'"},
            {"id": "t5", "text": "Perform a block-level disk clone from sda to sdb"},
            {"id": "t6", "text": "Display real-time CPU and memory usage for running processes"},
        ],
        "answer": {"p1": "t1", "p2": "t2", "p3": "t3", "p4": "t4", "p5": "t5"},
        "rationales": {
            "p1": "chmod 640 sets rw- for owner (6), r-- for group (4), --- for others (0).",
            "p2": "chown user:group changes both the owning user and owning group of the specified file.",
            "p3": "'ps aux' shows all processes (a=all users, u=user-oriented format, x=include processes without a TTY).",
            "p4": "grep -r recurses through directories; the pattern 'error' is matched in every file under /var/log/.",
            "p5": "dd copies raw blocks; if= is input, of= is output—used for imaging, cloning, or wiping disks.",
        },
        "explanation": (
            "t6 (real-time CPU/memory) describes 'top' or 'htop', not ps. "
            "chmod vs chown is a classic confusion: chmod changes permission bits, chown changes ownership. "
            "dd is destructive; input/output direction matters critically."
        ),
    },

    # ── PBQ_CATEGORIZE ────────────────────────────────────────────────────────

    {
        "id": "c2pbq-005",
        "domain": 4,
        "objective": "4.1",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Backup types",
        "stem": (
            "A backup administrator is designing a recovery strategy. "
            "Classify each description by the backup type it defines."
        ),
        "categories": [
            {"id": "c1", "text": "Full"},
            {"id": "c2", "text": "Incremental"},
            {"id": "c3", "text": "Differential"},
        ],
        "items": [
            {"id": "i1", "text": "Copies all selected data every run; clears the archive bit after backup"},
            {"id": "i2", "text": "Backs up only files changed since the last backup of any type; clears the archive bit"},
            {"id": "i3", "text": "Backs up only files changed since the last full backup; does NOT clear the archive bit"},
            {"id": "i4", "text": "Fastest backup job to complete after the first full; slowest restore (requires full + every subsequent tape/set)"},
            {"id": "i5", "text": "Restore requires only two sets: the last full and the most recent instance of this type"},
            {"id": "i6", "text": "Grows larger each day until the next full backup is taken"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c2", "i5": "c3", "i6": "c3"},
        "rationales": {
            "i1": "A full backup copies everything and clears (resets) the archive bit on every backed-up file.",
            "i2": "Incremental captures only changes since the last backup of any type and resets the archive bit, keeping each set small.",
            "i3": "Differential does NOT clear the archive bit—it keeps accumulating all changes since the last full.",
            "i4": "Incrementals are the fastest to write (only day's changes) but slowest to restore (need full + every incremental in sequence).",
            "i5": "Differential restore needs only two sets—the base full and the latest differential—making restore faster than incremental.",
            "i6": "Because differential never resets the archive bit, it accumulates all changes since the last full, growing each day.",
        },
        "explanation": (
            "Key differentiator: archive-bit behavior. Full and incremental both CLEAR the archive bit; "
            "differential leaves it set. This causes differential sets to grow daily while incrementals stay small. "
            "Restore complexity is the inverse: incremental is hardest, differential needs only two tapes."
        ),
    },

    {
        "id": "c2pbq-006",
        "domain": 2,
        "objective": "2.6",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Malware types & removal",
        "stem": (
            "A security analyst is reviewing incident reports. "
            "Classify each malware description by its type."
        ),
        "categories": [
            {"id": "c1", "text": "Trojan"},
            {"id": "c2", "text": "Rootkit"},
            {"id": "c3", "text": "Ransomware"},
            {"id": "c4", "text": "Keylogger"},
            {"id": "c5", "text": "Spyware"},
        ],
        "items": [
            {"id": "i1", "text": "Malware disguised as a legitimate game installer that opens a remote backdoor"},
            {"id": "i2", "text": "Code that intercepts OS kernel calls to hide its own files, processes, and registry keys from the OS"},
            {"id": "i3", "text": "Malware that encrypts the user's Documents folder and demands Bitcoin payment for the decryption key"},
            {"id": "i4", "text": "Software that records every keystroke and periodically emails a log file to an attacker"},
            {"id": "i5", "text": "Application that silently monitors browsing history and transmits it to a third-party ad server"},
            {"id": "i6", "text": "Bootkit that loads before the OS and patches NTFS drivers to conceal attacker-planted files"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c3", "i4": "c4", "i5": "c5", "i6": "c2"},
        "rationales": {
            "i1": "A trojan masquerades as benign software (game installer) while carrying a malicious payload (backdoor).",
            "i2": "A rootkit uses kernel-level hooks to hide its own artifacts from the OS and security tools.",
            "i3": "Ransomware encrypts victim data and extorts payment (commonly cryptocurrency) for decryption.",
            "i4": "A keylogger records keystrokes to steal credentials, credit-card numbers, and other sensitive input.",
            "i5": "Spyware covertly collects and transmits user data (browsing habits, personal info) to external parties.",
            "i6": "A bootkit is a rootkit that persists in the MBR/VBR or UEFI and loads before the OS—still classified as a rootkit.",
        },
        "explanation": (
            "Adware (not listed) shows unwanted ads but does not transmit personal data—spyware does. "
            "A bootkit is a subtype of rootkit; both hook low-level OS mechanisms to hide themselves. "
            "Trojan vs virus: a trojan does not self-replicate; it relies on user execution."
        ),
    },

    {
        "id": "c2pbq-007",
        "domain": 2,
        "objective": "2.2",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "NTFS vs share permissions",
        "stem": (
            "A sysadmin is configuring file access on a Windows Server. "
            "Classify each statement as describing NTFS permissions or Share permissions."
        ),
        "categories": [
            {"id": "c1", "text": "NTFS Permissions"},
            {"id": "c2", "text": "Share Permissions"},
        ],
        "items": [
            {"id": "i1", "text": "Apply whether the user accesses the resource locally or over the network"},
            {"id": "i2", "text": "Apply only when the resource is accessed over the network via SMB"},
            {"id": "i3", "text": "Support granular control: Read, Write, Modify, Full Control, List Folder Contents, and special permissions"},
            {"id": "i4", "text": "Offer only three levels: Read, Change, and Full Control"},
            {"id": "i5", "text": "When combined with the other type, the most restrictive cumulative permission applies at network access"},
            {"id": "i6", "text": "Can be set on individual files as well as folders"},
        ],
        "answer": {"i1": "c1", "i2": "c2", "i3": "c1", "i4": "c2", "i5": "c1", "i6": "c1"},
        "rationales": {
            "i1": "NTFS permissions are enforced by the file system and apply to all access paths—local logon or UNC share.",
            "i2": "Share permissions are evaluated only during SMB network access; a local logon bypasses them entirely.",
            "i3": "NTFS supports fine-grained permissions including Modify, Write, Read & Execute, List Folder, and special (advanced) entries.",
            "i4": "Share permissions have exactly three options: Read, Change, and Full Control—much coarser than NTFS.",
            "i5": "When NTFS and share permissions differ, Windows uses the more restrictive effective permission at the network boundary.",
            "i6": "NTFS permissions can be applied at the individual file level; share permissions apply only to the shared folder root.",
        },
        "explanation": (
            "Best practice: grant Everyone Full Control at the share level and enforce granular access via NTFS permissions. "
            "The effective network permission is the intersection (most restrictive) of share and NTFS. "
            "Local access is governed solely by NTFS—share permissions are irrelevant when sitting at the console."
        ),
    },

    {
        "id": "c2pbq-008",
        "domain": 4,
        "objective": "4.8",
        "type": "pbq_categorize",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A technician encounters several script files during an audit. "
            "Classify each file extension by the OS or environment that natively executes it."
        ),
        "categories": [
            {"id": "c1", "text": "Windows only"},
            {"id": "c2", "text": "Linux/macOS (Unix-like) only"},
            {"id": "c3", "text": "Cross-platform"},
        ],
        "items": [
            {"id": "i1", "text": ".bat"},
            {"id": "i2", "text": ".ps1"},
            {"id": "i3", "text": ".sh"},
            {"id": "i4", "text": ".vbs"},
            {"id": "i5", "text": ".py"},
            {"id": "i6", "text": ".js (Node.js runtime)"},
        ],
        "answer": {"i1": "c1", "i2": "c1", "i3": "c2", "i4": "c1", "i5": "c3", "i6": "c3"},
        "rationales": {
            "i1": ".bat (batch) files are executed by cmd.exe; they are Windows-native with no native equivalent on Linux/macOS.",
            "i2": ".ps1 PowerShell scripts require PowerShell; although PowerShell Core runs on Linux, the extension itself is Windows-native and exam objectives treat it as Windows.",
            "i3": ".sh shell scripts are native to Unix/Linux/macOS shells (bash, sh, zsh); Windows has no native executor.",
            "i4": ".vbs (VBScript) is executed by Windows Script Host (wscript.exe/cscript.exe); it has no native runtime on Linux/macOS.",
            "i5": "Python (.py) has runtimes for Windows, Linux, and macOS, making it genuinely cross-platform.",
            "i6": "Node.js (.js) runs on Windows, Linux, and macOS via the Node.js runtime—cross-platform by design.",
        },
        "explanation": (
            "For A+ exam purposes: .bat and .vbs are Windows-only; .sh is Unix/Linux/macOS-only; .py and Node.js .js are cross-platform. "
            ".ps1 is Windows-centric in the A+ context even though PowerShell Core exists on Linux. "
            "Knowing which scripts to be suspicious of on which OS is a security-awareness objective."
        ),
    },

    # ── PBQ_ORDERING ──────────────────────────────────────────────────────────

    {
        "id": "c2pbq-009",
        "domain": 3,
        "objective": "3.3",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A help-desk technician suspects malware on a user's laptop. "
            "Arrange the CompTIA best-practice malware removal steps in the correct order."
        ),
        "items": [
            {"id": "i1", "text": "Identify and research malware symptoms to confirm the infection"},
            {"id": "i2", "text": "Quarantine the infected system (disconnect from network, isolate)"},
            {"id": "i3", "text": "Disable System Restore / Shadow Copies on Windows"},
            {"id": "i4", "text": "Remediate: update anti-malware definitions, then scan and remove (use safe mode or bootable AV if needed)"},
            {"id": "i5", "text": "Schedule recurring anti-malware scans and keep definitions and OS patches current"},
            {"id": "i6", "text": "Re-enable System Restore and create a new clean restore point"},
            {"id": "i7", "text": "Educate the end user on safe computing practices to prevent reinfection"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Step 1: Identify and verify malware symptoms before taking any action—confirm it is actually malware.",
            "i2": "Step 2: Quarantine immediately to prevent lateral spread across the network.",
            "i3": "Step 3: Disable System Restore so that infected VSS shadow copies cannot be used to re-infect after removal.",
            "i4": "Step 4: Remediate—update definitions first so the scanner recognizes the latest threats, then scan and remove.",
            "i5": "Step 5: Schedule scans and apply updates to maintain ongoing protection after clean-up.",
            "i6": "Step 6: Re-enable System Restore and create a known-clean restore point to allow future recovery.",
            "i7": "Step 7: Educate the user last—explain how the infection occurred and how to avoid it in the future.",
        },
        "explanation": (
            "CompTIA's 7-step process (220-1202 objective 3.3): "
            "1 Identify, 2 Quarantine, 3 Disable System Restore, 4 Remediate, "
            "5 Schedule scans/updates, 6 Re-enable System Restore + restore point, 7 Educate user. "
            "Common errors: remediating before quarantine lets malware spread; "
            "re-enabling System Restore before scanning creates infected restore points."
        ),
    },

    {
        "id": "c2pbq-010",
        "domain": 1,
        "objective": "1.2",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician is performing a clean install of Windows 11 on a new SSD. "
            "Arrange the steps in the correct order."
        ),
        "items": [
            {"id": "i1", "text": "Verify BIOS/UEFI settings: enable UEFI mode, Secure Boot, and TPM 2.0"},
            {"id": "i2", "text": "Boot from the Windows 11 installation media (USB or DVD)"},
            {"id": "i3", "text": "Select 'Custom: Install Windows only (advanced)' at the installation type screen"},
            {"id": "i4", "text": "Delete existing partitions and create a new partition on the target drive"},
            {"id": "i5", "text": "Complete Windows Setup: accept EULA, choose region, set up user account"},
            {"id": "i6", "text": "Install drivers (chipset, GPU, NIC, audio) and run Windows Update"},
            {"id": "i7", "text": "Install required applications and restore user data from backup"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "UEFI, Secure Boot, and TPM 2.0 are Windows 11 hardware requirements; verify before attempting install.",
            "i2": "Boot from installation media to launch the Windows Setup environment.",
            "i3": "'Custom' mode performs a clean install; 'Upgrade' would preserve the old OS (not desired here).",
            "i4": "Wiping and repartitioning ensures a clean target volume before file copy begins.",
            "i5": "Windows Setup then copies files, reboots, and runs OOBE to configure locale, licensing, and user account.",
            "i6": "Driver installation and Windows Update follow OOBE to ensure device functionality and security patches.",
            "i7": "Application installation and data restore are the final steps once the OS is fully patched and stable.",
        },
        "explanation": (
            "Windows 11 uniquely requires UEFI + Secure Boot + TPM 2.0—verify these before booting media. "
            "Always choose 'Custom' for a clean install; 'Upgrade' preserves the old OS. "
            "Driver and update installation must precede application deployment to avoid compatibility issues."
        ),
    },

    {
        "id": "c2pbq-011",
        "domain": 4,
        "objective": "4.2",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "An IT team is following a formal change-management process to deploy a firewall rule update. "
            "Arrange the change-management steps in the correct order."
        ),
        "items": [
            {"id": "i1", "text": "Submit a formal change request (RFC) documenting the proposed change, scope, and business justification"},
            {"id": "i2", "text": "Perform a risk analysis and assess the potential impact on affected systems"},
            {"id": "i3", "text": "Obtain approval from the Change Advisory Board (CAB) or change authority"},
            {"id": "i4", "text": "Test the change in a sandbox or staging environment and develop a rollback plan"},
            {"id": "i5", "text": "Implement the change in production during the approved maintenance window"},
            {"id": "i6", "text": "Verify the change was successful and that affected services function correctly"},
            {"id": "i7", "text": "Document the completed change, outcomes, lessons learned, and update configuration records"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "An RFC formally initiates the change process and provides the baseline record for tracking.",
            "i2": "Risk analysis before CAB review ensures the board has complete impact information when deciding.",
            "i3": "CAB approval is required before any testing or implementation begins in a mature change process.",
            "i4": "Sandbox testing and rollback planning reduce production risk; testing must precede live deployment.",
            "i5": "Implementation happens in production only after approval, testing, and rollback plans are in place.",
            "i6": "Post-implementation verification confirms the change achieved its goal and no regressions were introduced.",
            "i7": "Documentation closes the change record and feeds the CMDB/knowledge base for future reference.",
        },
        "explanation": (
            "CompTIA change-management sequence: RFC → Risk Analysis → CAB Approval → Sandbox Test + Rollback Plan "
            "→ Implement → Verify → Document. "
            "A common exam trap is placing documentation before verification, or testing after implementation. "
            "The rollback plan must exist BEFORE the maintenance window opens."
        ),
    },

    {
        "id": "c2pbq-012",
        "domain": 4,
        "objective": "4.4",
        "type": "pbq_ordering",
        "difficulty": "hard",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A technician discovers a workstation that may have been used in a data breach. "
            "Arrange the incident-response and evidence-handling steps in the correct order."
        ),
        "items": [
            {"id": "i1", "text": "Identify: recognize and confirm that a security incident has occurred"},
            {"id": "i2", "text": "Report the incident to the appropriate authority (security team, manager, CIRT)"},
            {"id": "i3", "text": "Preserve evidence: document the system state, photograph the scene, and avoid altering data"},
            {"id": "i4", "text": "Contain the affected system (isolate from network, prevent further damage or data loss)"},
            {"id": "i5", "text": "Collect and acquire evidence following chain-of-custody procedures (hash, tag, bag, log)"},
            {"id": "i6", "text": "Eradicate the threat and recover systems to normal operation"},
            {"id": "i7", "text": "Conduct a lessons-learned review and update policies or controls to prevent recurrence"},
        ],
        "answer": ["i1", "i2", "i3", "i4", "i5", "i6", "i7"],
        "rationales": {
            "i1": "Identification is always first: confirm an incident exists before taking any formal action.",
            "i2": "Report immediately after identification so stakeholders are aware and can authorize next steps.",
            "i3": "Preserve the scene before touching anything—volatile evidence (RAM, running processes) is lost if the machine is powered off carelessly.",
            "i4": "Containment stops the threat from spreading while still allowing evidence collection from a live system.",
            "i5": "Formal evidence acquisition with cryptographic hashing (MD5/SHA-256) and chain-of-custody logging ensures legal admissibility.",
            "i6": "Eradication and recovery restore business operations only after evidence is secured.",
            "i7": "Lessons-learned (post-mortem) is the final step—improving defenses based on what was discovered.",
        },
        "explanation": (
            "Incident-response order: Identify → Report → Preserve Evidence → Contain → Collect Evidence → Eradicate/Recover → Lessons Learned. "
            "Chain-of-custody requires every person who handles evidence to be logged with date/time. "
            "Hashing (MD5 or SHA-256) before and after acquisition proves evidence integrity in court. "
            "Powering off a machine before imaging loses volatile RAM contents—preserve before contain when volatile data matters."
        ),
    },
]
