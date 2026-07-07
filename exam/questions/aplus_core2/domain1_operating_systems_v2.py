"""
CompTIA A+ Core 2 (220-1202) — Domain 1: Operating Systems  v2
38 new hard/expert scenario-based questions (IDs c2d1v2-001 through c2d1v2-038).
All study_topic labels match those in domain1_operating_systems.py.
~33 multiple_choice + 5 multiple_response.
"""

QUESTIONS = [
    # ── Windows editions ─────────────────────────────────────────────────────
    {
        "id": "c2d1v2-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "A hospital uses Windows workstations that are NOT joined to an Active Directory "
            "domain but must store patient data encrypted at rest using BitLocker, comply "
            "with HIPAA audit requirements via local audit policies, and run Hyper-V to host "
            "a legacy medical imaging virtual machine. Which is the MINIMUM Windows 11 edition "
            "that satisfies all three requirements on a standalone workstation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows 11 Home",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Home does not include the full BitLocker management "
                    "suite, the Local Group Policy Editor for audit policies, or Hyper-V hypervisor "
                    "support."
                ),
            },
            {
                "id": "b",
                "text": "Windows 11 Pro",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 Pro includes full BitLocker drive encryption, the Local "
                    "Group Policy Editor (gpedit.msc) for configuring audit policies, and the "
                    "Client Hyper-V feature—all on a standalone (non-domain) workstation."
                ),
            },
            {
                "id": "c",
                "text": "Windows 11 Home with BitLocker Device Encryption enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Encryption in Home is a limited subset of BitLocker "
                    "managed through Settings only; full BitLocker management (manage-bde, GPO "
                    "integration) requires Pro or higher. Home also lacks gpedit.msc and Hyper-V."
                ),
            },
            {
                "id": "d",
                "text": "Windows 11 Enterprise",
                "correct": False,
                "rationale": (
                    "Incorrect. Enterprise satisfies all three requirements but requires volume "
                    "licensing, making it more than the MINIMUM cost-effective edition for a "
                    "standalone workstation."
                ),
            },
        ],
        "explanation": (
            "Windows 11 Pro is the minimum edition providing full BitLocker (manage-bde, TPM "
            "management, GPO-controlled recovery keys), Local Group Policy Editor for HIPAA-aligned "
            "audit settings, and the Client Hyper-V feature. Home lacks all three; Enterprise "
            "qualifies but is over-specified for a non-domain environment."
        ),
    },
    {
        "id": "c2d1v2-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows editions",
        "stem": (
            "An IT manager reviews a quote for 300 Windows 11 workstations that includes "
            "Windows 11 Pro for Workstations. The workstations are standard Dell OptiPlex "
            "desktops with single Intel Core i7 CPUs, 32 GB RAM, and standard NVMe SSDs. "
            "The fleet will be domain-joined, managed via Intune, and run standard office "
            "productivity software. The manager asks why Pro for Workstations was specified "
            "instead of Pro. Which answer BEST justifies choosing Pro for Workstations over Pro "
            "in this scenario—or identifies that it is NOT justified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pro for Workstations is required for Intune enrollment.",
                "correct": False,
                "rationale": (
                    "Incorrect. Both Windows 11 Pro and Pro for Workstations support Microsoft "
                    "Intune MDM enrollment. Intune management does not require Pro for Workstations."
                ),
            },
            {
                "id": "b",
                "text": "Pro for Workstations is required for domain join.",
                "correct": False,
                "rationale": (
                    "Incorrect. Domain join is supported by Windows 11 Pro; Pro for Workstations "
                    "is not required for this feature."
                ),
            },
            {
                "id": "c",
                "text": "Pro for Workstations is NOT justified; the hardware and workload do not use its differentiating features (dual-socket CPUs, >128 GB RAM, ReFS, NVDIMM).",
                "correct": True,
                "rationale": (
                    "Correct. Pro for Workstations adds support for up to two physical CPUs, "
                    "up to 6 TB RAM, ReFS, and persistent memory (NVDIMM). None of these apply "
                    "to single-socket desktops with 32 GB RAM running office software. Windows 11 "
                    "Pro provides all required features at lower cost."
                ),
            },
            {
                "id": "d",
                "text": "Pro for Workstations provides faster Windows Update delivery, reducing patch windows.",
                "correct": False,
                "rationale": (
                    "Incorrect. Pro for Workstations does not provide a faster Windows Update "
                    "pipeline compared to Pro. Update policies are managed by Intune/WSUS "
                    "regardless of edition."
                ),
            },
        ],
        "explanation": (
            "Windows 11 Pro for Workstations is designed for high-end multi-socket servers "
            "repurposed as workstations (CAD, rendering, simulation) that need >128 GB RAM, "
            "dual CPUs, ReFS, or NVDIMM. Standard single-socket office PCs gain nothing from "
            "Pro for Workstations; specifying it wastes budget. The correct edition here is "
            "Windows 11 Pro."
        ),
    },
    # ── Windows command-line tools ────────────────────────────────────────────
    {
        "id": "c2d1v2-003",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A Windows 10 workstation's C: drive reports SMART errors. The technician wants "
            "to run System File Checker to verify the integrity of Windows system files and "
            "repair any corrupted files automatically. The technician runs 'sfc /scannow' from "
            "an elevated command prompt, but SFC reports it cannot repair some files and refers "
            "to the CBS.log. What should the technician run NEXT to repair the Windows component "
            "store before re-running SFC?"
        ),
        "options": [
            {
                "id": "a",
                "text": "chkdsk C: /f",
                "correct": False,
                "rationale": (
                    "Incorrect. chkdsk /f fixes file system errors but does not repair the "
                    "Windows component store (WinSxS). Component store corruption requires DISM."
                ),
            },
            {
                "id": "b",
                "text": "DISM /Online /Cleanup-Image /RestoreHealth",
                "correct": True,
                "rationale": (
                    "Correct. DISM /Online /Cleanup-Image /RestoreHealth contacts Windows Update "
                    "(or a specified source) to repair the component store. After DISM completes "
                    "successfully, re-running 'sfc /scannow' can replace corrupted files from "
                    "the now-healthy store."
                ),
            },
            {
                "id": "c",
                "text": "bcdedit /export C:\\BCD_Backup",
                "correct": False,
                "rationale": (
                    "Incorrect. bcdedit manages the Boot Configuration Data; exporting a BCD "
                    "backup does not repair system files or the component store."
                ),
            },
            {
                "id": "d",
                "text": "bootrec /rebuildbcd",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec /rebuildbcd rebuilds the BCD store for boot issues; it "
                    "has no effect on Windows component store integrity or SFC repairs."
                ),
            },
        ],
        "explanation": (
            "When SFC cannot repair files, the Windows component store (WinSxS) is likely "
            "corrupted. DISM (Deployment Image Servicing and Management) with "
            "/Cleanup-Image /RestoreHealth repairs the component store by downloading correct "
            "files from Windows Update. After a successful DISM repair, sfc /scannow can "
            "then pull replacement files from the healthy store."
        ),
    },
    {
        "id": "c2d1v2-004",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician is at the command line on a Windows Server and needs to see the "
            "current routing table to verify that traffic destined for the 10.20.0.0/16 "
            "subnet is using the correct gateway. Which command displays the IPv4 routing table?"
        ),
        "options": [
            {
                "id": "a",
                "text": "netstat -r",
                "correct": True,
                "rationale": (
                    "Correct. 'netstat -r' (or equivalently 'route print') displays the IP "
                    "routing table, showing all IPv4 and IPv6 routes, gateways, and interface "
                    "metrics currently configured on the host."
                ),
            },
            {
                "id": "b",
                "text": "arp -a",
                "correct": False,
                "rationale": (
                    "Incorrect. 'arp -a' displays the ARP cache (MAC address-to-IP mappings "
                    "for recently contacted hosts on the local subnet); it does not show routing "
                    "table entries."
                ),
            },
            {
                "id": "c",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /all shows adapter-level configuration (IP address, "
                    "subnet mask, gateway, DNS) but does not display the full routing table with "
                    "all static and dynamic routes."
                ),
            },
            {
                "id": "d",
                "text": "nbtstat -n",
                "correct": False,
                "rationale": (
                    "Incorrect. nbtstat -n lists registered NetBIOS names on the local machine; "
                    "it provides no routing information."
                ),
            },
        ],
        "explanation": (
            "'netstat -r' and 'route print' both display the IPv4 and IPv6 routing tables on "
            "Windows, including the network destination, netmask, gateway, interface, and "
            "metric for each entry. arp -a shows Layer 2 ARP cache; ipconfig /all shows "
            "adapter settings; nbtstat is for NetBIOS name resolution."
        ),
    },
    {
        "id": "c2d1v2-005",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A Windows workstation's pagefile.sys has grown to fill the drive. A technician "
            "needs to immediately terminate a specific unresponsive process with PID 4812 "
            "from the command line without opening Task Manager's GUI. Which command "
            "accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "net stop 4812",
                "correct": False,
                "rationale": (
                    "Incorrect. 'net stop' requires a service name, not a PID. It also only "
                    "stops Windows services, not arbitrary user-mode processes."
                ),
            },
            {
                "id": "b",
                "text": "kill 4812",
                "correct": False,
                "rationale": (
                    "Incorrect. 'kill' is a Unix/Linux command. On Windows, the equivalent "
                    "command-line tool is 'taskkill'."
                ),
            },
            {
                "id": "c",
                "text": "taskkill /PID 4812 /F",
                "correct": True,
                "rationale": (
                    "Correct. 'taskkill /PID 4812 /F' sends a forced termination signal to "
                    "the process with PID 4812. The /F flag forces termination of processes "
                    "that do not respond to a graceful shutdown request."
                ),
            },
            {
                "id": "d",
                "text": "sc stop 4812",
                "correct": False,
                "rationale": (
                    "Incorrect. 'sc stop' is for Windows services identified by name, not by "
                    "PID. It would return an error if given a numeric PID."
                ),
            },
        ],
        "explanation": (
            "taskkill is the Windows command-line process termination tool. '/PID <number>' "
            "targets a specific process by its numeric PID. '/F' forces termination for "
            "unresponsive processes. '/IM <name>' can target by image name instead. "
            "Unix 'kill' does not exist natively in Windows cmd; 'sc' and 'net stop' only "
            "target services by name."
        ),
    },
    {
        "id": "c2d1v2-006",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician is remoting into a Windows Server Core installation (no GUI). "
            "They need to verify that the server's hostname is 'FILESRV01' and that it "
            "is a member of the 'CORP' domain, using only the command line. "
            "Which single command displays both the computer name and domain membership?"
        ),
        "options": [
            {
                "id": "a",
                "text": "whoami /all",
                "correct": False,
                "rationale": (
                    "Incorrect. 'whoami /all' shows the current user's security context, "
                    "including group memberships and privileges—but it does not directly "
                    "display the computer name and domain membership in a clear summary."
                ),
            },
            {
                "id": "b",
                "text": "systeminfo | findstr /C:\"Host Name\" /C:\"Domain\"",
                "correct": True,
                "rationale": (
                    "Correct. 'systeminfo' outputs detailed system information including "
                    "'Host Name' and 'Domain' fields. Piping to 'findstr' with those strings "
                    "filters the output to display just the computer name and domain "
                    "membership in a single command."
                ),
            },
            {
                "id": "c",
                "text": "hostname",
                "correct": False,
                "rationale": (
                    "Incorrect. 'hostname' displays only the computer name; it does not "
                    "show domain membership."
                ),
            },
            {
                "id": "d",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /all shows a 'Connection-specific DNS Suffix' that "
                    "may hint at the domain, but it does not explicitly display the AD domain "
                    "membership or the computer's registered NetBIOS name in the same way "
                    "systeminfo does."
                ),
            },
        ],
        "explanation": (
            "systeminfo provides a comprehensive system summary including 'Host Name', "
            "'Domain', OS version, hardware, and more. Filtering with findstr isolates "
            "the two relevant fields. On Server Core, GUI tools are unavailable, so "
            "systeminfo is the definitive CLI method for verifying host identity and domain "
            "membership simultaneously."
        ),
    },
    {
        "id": "c2d1v2-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician suspects a Windows workstation has been compromised and needs to "
            "list all scheduled tasks configured on the system to look for persistence "
            "mechanisms—without opening the Task Scheduler GUI. Which command dumps the "
            "full scheduled task list from the command line?"
        ),
        "options": [
            {
                "id": "a",
                "text": "msconfig /tasks",
                "correct": False,
                "rationale": (
                    "Incorrect. msconfig does not accept a '/tasks' switch and cannot list "
                    "scheduled tasks. It manages boot startup entries and services, not "
                    "the Task Scheduler library."
                ),
            },
            {
                "id": "b",
                "text": "schtasks /query /fo LIST /v",
                "correct": True,
                "rationale": (
                    "Correct. 'schtasks /query /fo LIST /v' queries all scheduled tasks "
                    "on the local machine, formats the output as a detailed LIST, and shows "
                    "verbose information (run-as account, last run time, next run time, "
                    "task actions)—ideal for malware hunting."
                ),
            },
            {
                "id": "c",
                "text": "tasklist /v",
                "correct": False,
                "rationale": (
                    "Incorrect. 'tasklist' lists currently running processes, not scheduled "
                    "tasks. It is the command-line equivalent of the Process tab in Task Manager."
                ),
            },
            {
                "id": "d",
                "text": "services.msc /list",
                "correct": False,
                "rationale": (
                    "Incorrect. services.msc is the Services GUI snap-in; it does not accept "
                    "a '/list' parameter and does not enumerate scheduled tasks."
                ),
            },
        ],
        "explanation": (
            "schtasks is the command-line interface for the Windows Task Scheduler. "
            "'schtasks /query' lists all tasks; '/fo LIST' formats output as a readable list; "
            "'/v' provides verbose detail including the action (executable path), run-as "
            "account, and schedule. Attackers frequently register tasks for persistence, "
            "making schtasks a key forensic tool."
        ),
    },
    # ── Windows administrative tools (MMC snap-ins) ───────────────────────────
    {
        "id": "c2d1v2-008",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "An administrator opens Event Viewer and needs to search across all Windows logs "
            "simultaneously for any error events with Event ID 7045 (a new service was installed) "
            "that occurred in the last 48 hours. The log set is large. "
            "Which Event Viewer feature provides the MOST efficient way to accomplish this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Right-click 'Windows Logs' → Clear Log.",
                "correct": False,
                "rationale": (
                    "Incorrect. Clearing logs destroys evidence. This does not search or filter "
                    "events—it is the opposite of what is needed."
                ),
            },
            {
                "id": "b",
                "text": "Create a Custom View with an XML query filtering on EventID 7045 across all logs for the last 48 hours.",
                "correct": True,
                "rationale": (
                    "Correct. Custom Views in Event Viewer allow XPath/XML queries that can "
                    "search multiple logs simultaneously. The query can filter by Event ID, "
                    "time range, and log source, making cross-log searching efficient for "
                    "incident investigation."
                ),
            },
            {
                "id": "c",
                "text": "Open each log individually (System, Application, Security) and press Ctrl+F to search.",
                "correct": False,
                "rationale": (
                    "Incorrect. Event Viewer does not have a built-in Ctrl+F text search. "
                    "Individual log filtering is possible via 'Filter Current Log', but it "
                    "cannot span multiple logs simultaneously."
                ),
            },
            {
                "id": "d",
                "text": "Run eventvwr.msc /7045 from the command line to filter by Event ID at launch.",
                "correct": False,
                "rationale": (
                    "Incorrect. eventvwr.msc does not accept an Event ID filter as a command-line "
                    "argument. Custom Views or the Filter Current Log dialog are used for ID "
                    "filtering within the GUI."
                ),
            },
        ],
        "explanation": (
            "Event Viewer's Custom Views feature supports XPath-based queries that can target "
            "multiple logs (System, Application, Security, etc.) simultaneously. The XML query "
            "editor allows filtering by EventID, time range, source, and level. This is far "
            "more efficient than manually filtering each log. The 'Filter Current Log' function "
            "only works on one log at a time."
        ),
    },
    {
        "id": "c2d1v2-009",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A Windows 10 workstation is part of a workgroup (not domain-joined). "
            "A technician needs to create a local security policy that forces all "
            "user passwords to be at least 12 characters and expire every 60 days. "
            "Which snap-in is used to configure these local password policies?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Computer Management → Local Users and Groups",
                "correct": False,
                "rationale": (
                    "Incorrect. Local Users and Groups creates and manages accounts and group "
                    "membership but does not configure password complexity or maximum age policies."
                ),
            },
            {
                "id": "b",
                "text": "Local Security Policy (secpol.msc) → Account Policies → Password Policy",
                "correct": True,
                "rationale": (
                    "Correct. secpol.msc (Local Security Policy) contains Account Policies → "
                    "Password Policy, where Minimum Password Length and Maximum Password Age "
                    "are configured directly for the local workstation."
                ),
            },
            {
                "id": "c",
                "text": "Windows Defender Firewall with Advanced Security (wf.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. wf.msc manages network firewall rules; it has no settings "
                    "related to password policies."
                ),
            },
            {
                "id": "d",
                "text": "Disk Management (diskmgmt.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk Management is for partition and volume management; it "
                    "does not configure security or password policies."
                ),
            },
        ],
        "explanation": (
            "secpol.msc (Local Security Policy) provides Account Policies → Password Policy "
            "for standalone workgroup machines. The relevant settings are 'Minimum password "
            "length' (set to 12) and 'Maximum password age' (set to 60 days). On domain-joined "
            "machines, domain GPOs override local policy; on workgroup machines, secpol.msc "
            "is the authoritative source."
        ),
    },
    # ── Control Panel utilities ────────────────────────────────────────────────
    {
        "id": "c2d1v2-010",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A user reports that after installing a new printer driver, their default "
            "printer keeps reverting to a different device after each login. The technician "
            "confirms the correct default is set in Devices and Printers, but the setting "
            "does not persist. Windows 10's 'Let Windows manage my default printer' feature "
            "is suspect. Where is this setting toggled?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → Devices and Printers → right-click printer → Set as default printer",
                "correct": False,
                "rationale": (
                    "Incorrect. Right-clicking and setting the default works temporarily, but "
                    "if 'Let Windows manage my default printer' is enabled, Windows overrides "
                    "this with the most recently used printer. The feature must be disabled "
                    "in Settings, not Control Panel."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Bluetooth & devices → Printers & scanners → uncheck 'Let Windows manage my default printer'",
                "correct": True,
                "rationale": (
                    "Correct. Windows 10/11 Settings → Bluetooth & devices → Printers & "
                    "scanners contains the 'Let Windows manage my default printer' toggle. "
                    "Disabling it preserves the manually set default across logins."
                ),
            },
            {
                "id": "c",
                "text": "regedit → HKCU\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows → set Device to the printer name",
                "correct": False,
                "rationale": (
                    "Incorrect. While the registry stores printer defaults, directly editing "
                    "this value is not the standard or most direct method. The toggle in "
                    "Settings is the purpose-built control and preferred approach."
                ),
            },
            {
                "id": "d",
                "text": "Control Panel → Programs and Features → repair the printer driver",
                "correct": False,
                "rationale": (
                    "Incorrect. Repairing the printer driver via Programs and Features addresses "
                    "driver corruption, not the behavior where Windows auto-switches the default "
                    "printer based on recently used devices."
                ),
            },
        ],
        "explanation": (
            "Windows 10 introduced 'Let Windows manage my default printer', which automatically "
            "changes the default to the most recently used printer on each network location. "
            "This setting lives in Settings → Bluetooth & devices → Printers & scanners "
            "(not in Control Panel). Disabling it prevents Windows from overriding the "
            "user-defined default printer."
        ),
    },
    {
        "id": "c2d1v2-011",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A Windows workstation connected to a corporate domain is displaying the current "
            "date as January 1, 2000. Authentication to Active Directory is failing with "
            "Kerberos errors because of the time skew. The IT policy does not allow the "
            "workstation clock to be set manually. Which Control Panel applet and setting "
            "ensures the PC synchronizes its clock with the domain controller automatically?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → System → Advanced System Settings → adjust the hardware clock",
                "correct": False,
                "rationale": (
                    "Incorrect. Advanced System Settings manages virtual memory, performance, "
                    "and user profiles; it does not control time synchronization or NTP settings."
                ),
            },
            {
                "id": "b",
                "text": "Control Panel → Date and Time → Internet Time → Synchronize with an Internet time server",
                "correct": False,
                "rationale": (
                    "Incorrect. On a domain-joined PC, 'Internet Time' synchronization may be "
                    "disabled by Group Policy, and Kerberos requires syncing with the domain "
                    "controller (the authoritative time source), not a public NTP server."
                ),
            },
            {
                "id": "c",
                "text": "Run 'w32tm /resync' or ensure the Windows Time (W32Time) service is running and configured to sync with the domain hierarchy.",
                "correct": True,
                "rationale": (
                    "Correct. Domain-joined Windows machines use the Windows Time service "
                    "(W32Time) to automatically synchronize with the domain controller. Running "
                    "'w32tm /resync' forces an immediate resync. Ensuring the W32Time service "
                    "is running (and set to Automatic) is the correct fix for persistent time "
                    "skew on domain workstations."
                ),
            },
            {
                "id": "d",
                "text": "Control Panel → Region → change the time zone to UTC to match the domain controller.",
                "correct": False,
                "rationale": (
                    "Incorrect. Kerberos uses UTC internally but the clock must show the correct "
                    "absolute time, not just a different time zone offset. Changing the time "
                    "zone without synchronizing the clock would not fix a year-2000 drift."
                ),
            },
        ],
        "explanation": (
            "Domain-joined Windows PCs use the Windows Time service (W32Time) to synchronize "
            "with the AD domain hierarchy (workstations → domain controllers → PDC Emulator → "
            "external NTP source). Kerberos requires less than 5 minutes of clock skew. "
            "'w32tm /resync' forces an immediate resync. Manually setting the clock violates "
            "policy; public NTP synchronization is overridden by domain GPO."
        ),
    },
    # ── Windows Settings ──────────────────────────────────────────────────────
    {
        "id": "c2d1v2-012",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "A remote worker running Windows 11 reports that after a recent Windows Update "
            "reboot, their second monitor (connected via USB-C DisplayPort Alt Mode) is "
            "no longer detected. The monitor worked before the update. The technician wants "
            "to check whether the display adapter driver was changed by the update and "
            "roll it back if necessary—without using Device Manager. Which Settings path "
            "allows viewing and rolling back driver updates installed by Windows Update?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → System → Display → Advanced display settings",
                "correct": False,
                "rationale": (
                    "Incorrect. Advanced display settings shows refresh rate and display "
                    "adapter information but does not expose driver update history or a "
                    "rollback option."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Windows Update → Update history → Driver updates → Uninstall updates",
                "correct": True,
                "rationale": (
                    "Correct. Settings → Windows Update → Update history shows all installed "
                    "updates categorized by type, including Driver updates. From there, "
                    "'Uninstall updates' allows removing the specific driver update that "
                    "may have caused the regression—without opening Device Manager."
                ),
            },
            {
                "id": "c",
                "text": "Settings → Apps → Installed apps → search for the display driver → Uninstall",
                "correct": False,
                "rationale": (
                    "Incorrect. Display adapter drivers delivered via Windows Update do not "
                    "appear in the Apps list; they are managed through Windows Update history "
                    "or Device Manager."
                ),
            },
            {
                "id": "d",
                "text": "Settings → System → Recovery → Reset this PC → Keep my files",
                "correct": False,
                "rationale": (
                    "Incorrect. Resetting the PC is an extreme measure that reinstalls Windows; "
                    "it is completely disproportionate to rolling back a single driver update."
                ),
            },
        ],
        "explanation": (
            "Windows Update delivers driver updates through the same pipeline as OS updates. "
            "Settings → Windows Update → Update history categorizes updates including Driver "
            "updates. Using 'Uninstall updates' from that view allows targeted removal of a "
            "driver update without the need for Device Manager. This is the Settings-only "
            "path for driver update rollback."
        ),
    },
    {
        "id": "c2d1v2-013",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "A Windows 11 kiosk PC is shared by multiple shift workers. A manager wants "
            "to prevent users from changing the desktop wallpaper, accent color, and lock "
            "screen image so the corporate branding is preserved. The PC is NOT "
            "domain-joined. Which is the MOST appropriate Windows Settings or built-in "
            "method to enforce this on a standalone workstation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → Personalization → uncheck all themes; themes can then not be changed.",
                "correct": False,
                "rationale": (
                    "Incorrect. Unchecking themes in Settings does not prevent users from "
                    "re-enabling them or making individual personalization changes. There is "
                    "no enforcement lock in the Settings Personalization page itself."
                ),
            },
            {
                "id": "b",
                "text": "Use the Local Group Policy Editor (gpedit.msc) → User Configuration → Administrative Templates → Control Panel → Personalization → restrict wallpaper and theme changes.",
                "correct": True,
                "rationale": (
                    "Correct. gpedit.msc (available on Windows 11 Pro) allows enforcing "
                    "personalization restrictions via Local Group Policy. Policies such as "
                    "'Prevent changing desktop background', 'Prevent changing color and "
                    "appearance', and 'Prevent changing lock screen and logon image' lock "
                    "down the UI without requiring domain membership."
                ),
            },
            {
                "id": "c",
                "text": "Settings → Accounts → Family & other users → set all accounts to Standard User.",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard User accounts can still change wallpaper and lock "
                    "screen for their own profile. Standard User status restricts system-level "
                    "changes (installs, driver updates), not personal visual preferences."
                ),
            },
            {
                "id": "d",
                "text": "Rename the C:\\Windows\\Web\\Wallpaper folder so users cannot browse to it.",
                "correct": False,
                "rationale": (
                    "Incorrect. Renaming the wallpaper folder would prevent the default images "
                    "from loading but does not prevent users from setting custom wallpapers "
                    "from other locations."
                ),
            },
        ],
        "explanation": (
            "On a standalone Windows 11 Pro workstation, gpedit.msc (Local Group Policy Editor) "
            "is the correct tool for enforcing UI restrictions. Under User Configuration → "
            "Administrative Templates → Control Panel → Personalization, policies exist to "
            "prevent changing the desktop background, lock screen, and color scheme. These "
            "apply without domain infrastructure and survive user preference changes."
        ),
    },
    # ── Windows networking (workgroup/domain) ─────────────────────────────────
    {
        "id": "c2d1v2-014",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A technician is setting up a Windows 10 workgroup PC to share a folder "
            "called 'Reports' with read-only access for all network users, and full "
            "control for the local 'Managers' group. After creating the share, a network "
            "user can browse the share but cannot open the files. The NTFS permissions "
            "on the folder grant the 'Everyone' group only 'Read' on NTFS. The share "
            "permissions grant 'Everyone' Full Control. Why can't the user open the files?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Share permissions override NTFS permissions; the user should have Full Control.",
                "correct": False,
                "rationale": (
                    "Incorrect. When both share and NTFS permissions apply, Windows uses the "
                    "MORE RESTRICTIVE of the two. Share Full Control + NTFS Read = effective "
                    "Read. Share permissions do not override NTFS."
                ),
            },
            {
                "id": "b",
                "text": "The effective permission is Read (the more restrictive of Share Full Control and NTFS Read), which should allow opening files; the issue is likely that 'Read' on NTFS for files requires Execute on the parent folder.",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS 'Read' permission on a folder allows listing contents and "
                    "reading file contents. Execute is needed to run programs, not to open "
                    "data files."
                ),
            },
            {
                "id": "c",
                "text": "The effective permission is the intersection of both permission sets; with NTFS Read and Share Full Control, the effective access is Read—which should allow opening files. The most likely cause is the NTFS permissions are set on the folder but not inherited by the files inside.",
                "correct": True,
                "rationale": (
                    "Correct. Windows effective permissions over a share = MOST restrictive of "
                    "share and NTFS. NTFS Read + Share Full Control = Read effective, which does "
                    "allow reading/opening files. If users still cannot open files, it is most "
                    "likely that NTFS inheritance is broken—the files themselves may have "
                    "more restrictive explicit permissions that block access, or inheritance "
                    "was disabled so the folder permission did not propagate."
                ),
            },
            {
                "id": "d",
                "text": "The workgroup PC requires a password-protected sharing exemption; unauthenticated guests cannot access NTFS files.",
                "correct": False,
                "rationale": (
                    "Incorrect. While Password Protected Sharing can block anonymous access, "
                    "the question states the user can browse the share, indicating authentication "
                    "succeeded. The access failure on files points to NTFS permission inheritance."
                ),
            },
        ],
        "explanation": (
            "Over a share, Windows applies both share permissions and NTFS permissions; "
            "the effective right is the intersection (most restrictive). NTFS Read on the "
            "folder allows opening files. If files cannot be opened despite Read access on "
            "the folder, inheritance is likely broken—explicit deny entries on files, or "
            "NTFS inheritance was disabled and files have no permissions propagated from "
            "the parent folder."
        ),
    },
    {
        "id": "c2d1v2-015",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A Windows 11 laptop was previously connected to the corporate Wi-Fi (SSID: 'CorpNet') "
            "and set to Private network. The user now works from home on a Wi-Fi network also "
            "named 'CorpNet' (their home router). Windows automatically connects and sets the "
            "profile to Private. The user's home network is untrusted. The technician needs to "
            "change the network profile for the HOME 'CorpNet' SSID to Public WITHOUT "
            "forgetting the corporate saved profile. What is the correct approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → Network & Internet → Wi-Fi → 'CorpNet' → change network profile type to Public.",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 Settings → Network & Internet → Wi-Fi → clicking on "
                    "the connected network name shows the 'Network profile type' option (Public "
                    "or Private). Changing it to Public applies the more restrictive firewall "
                    "profile without forgetting the saved network password or corporate SSID."
                ),
            },
            {
                "id": "b",
                "text": "Forget the 'CorpNet' SSID and manually reconnect each time to force a profile selection dialog.",
                "correct": False,
                "rationale": (
                    "Incorrect. Forgetting the SSID removes the saved credentials, including "
                    "the corporate SSID if they share the same name, and does not provide a "
                    "clean per-BSSID profile separation."
                ),
            },
            {
                "id": "c",
                "text": "Disable Wi-Fi and use Ethernet when at home; the profile change is not possible without domain Group Policy.",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Settings allows changing the network profile type "
                    "from Public to Private (and vice versa) for any connected network without "
                    "Group Policy."
                ),
            },
            {
                "id": "d",
                "text": "Open Windows Defender Firewall → Advanced Settings → change the active profile from Private to Public.",
                "correct": False,
                "rationale": (
                    "Incorrect. The active firewall profile is determined by the Network "
                    "Location/Profile setting, not by a switch inside Windows Defender Firewall "
                    "with Advanced Security. The profile must be changed in the Network & "
                    "Internet Settings."
                ),
            },
        ],
        "explanation": (
            "Windows stores network profiles per SSID. In Settings → Network & Internet → "
            "Wi-Fi → [network name], the 'Network profile type' toggle switches between "
            "Public (restrictive, discovery off) and Private (trusted, discovery on). "
            "Changing it to Public on the home network applies the restrictive firewall "
            "profile while retaining the saved Wi-Fi password and other saved profiles."
        ),
    },
    # ── Application installation requirements ─────────────────────────────────
    {
        "id": "c2d1v2-016",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application installation requirements",
        "stem": (
            "A technician attempts to install a vendor-supplied 32-bit application on a "
            "64-bit Windows 11 workstation. The installer places files in C:\\Program Files (x86) "
            "and adds a registry key. The app runs but cannot read its own registry settings. "
            "The technician discovers the app writes to HKLM\\SOFTWARE\\VendorApp but reads from "
            "the same path and finds nothing. What Windows mechanism MOST likely explains this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows Data Execution Prevention (DEP) is blocking registry reads for 32-bit processes.",
                "correct": False,
                "rationale": (
                    "Incorrect. DEP prevents code execution from data regions in memory; it "
                    "has no effect on registry read/write operations."
                ),
            },
            {
                "id": "b",
                "text": "Registry redirection: 32-bit processes on 64-bit Windows are transparently redirected to HKLM\\SOFTWARE\\WOW6432Node, so the app writes there but reads from the native 64-bit path.",
                "correct": True,
                "rationale": (
                    "Correct. WOW64 (Windows-on-Windows 64-bit) redirects 32-bit process "
                    "registry writes from HKLM\\SOFTWARE to HKLM\\SOFTWARE\\WOW6432Node. If "
                    "any part of the app uses a 64-bit API to read from HKLM\\SOFTWARE directly, "
                    "it will not find the 32-bit values written under WOW6432Node, producing "
                    "empty reads."
                ),
            },
            {
                "id": "c",
                "text": "The application needs to run as Administrator to access HKLM; UAC is blocking the read.",
                "correct": False,
                "rationale": (
                    "Incorrect. HKLM\\SOFTWARE is readable by all users; administrator "
                    "rights are required to write, not read. The symptom (writes succeed, "
                    "reads fail) aligns with registry redirection, not UAC."
                ),
            },
            {
                "id": "d",
                "text": "Windows AppLocker is blocking registry access for unsigned 32-bit processes.",
                "correct": False,
                "rationale": (
                    "Incorrect. AppLocker controls application execution, not registry access. "
                    "If AppLocker were blocking the app entirely, it would not run at all."
                ),
            },
        ],
        "explanation": (
            "WOW64 transparently redirects 32-bit process registry operations targeting "
            "HKLM\\SOFTWARE to HKLM\\SOFTWARE\\WOW6432Node. If the vendor app uses a mix "
            "of 32-bit write paths and 64-bit read paths (or the 32-bit installer writes "
            "via WOW64 redirect while a 64-bit component reads the native path), reads will "
            "return nothing. The fix is to use Reg32 APIs consistently or add the key "
            "to the correct hive."
        ),
    },
    {
        "id": "c2d1v2-017",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application installation requirements",
        "stem": (
            "A user attempts to install an application and the installer terminates with "
            "the message: 'This application requires .NET Framework 3.5.' The workstation "
            "runs Windows 10 and is connected to the internet. What is the FASTEST way "
            "to install the missing .NET Framework 3.5?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Download the .NET Framework 3.5 full offline installer from microsoft.com and run it.",
                "correct": False,
                "rationale": (
                    "Incorrect. This works but is slower than the built-in Windows feature "
                    "installation path, which downloads only what is needed via Windows Update."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Apps → Optional features → Add a feature → search for '.NET Framework 3.5'.",
                "correct": False,
                "rationale": (
                    "Incorrect. .NET Framework 3.5 is a Windows Feature, not an Optional "
                    "Feature in the Apps section. Optional Features covers things like RSAT "
                    "and media codecs."
                ),
            },
            {
                "id": "c",
                "text": "Control Panel → Programs → Turn Windows features on or off → check '.NET Framework 3.5 (includes .NET 2.0 and 3.0)' → click OK.",
                "correct": True,
                "rationale": (
                    "Correct. .NET Framework 3.5 is an optional Windows Feature managed through "
                    "'Turn Windows features on or off'. Enabling it triggers an on-demand download "
                    "from Windows Update, completing in minutes without a separate installer."
                ),
            },
            {
                "id": "d",
                "text": "Run 'DISM /Online /Enable-Feature /FeatureName:NetFx3 /NoRestart' — this is the only supported method.",
                "correct": False,
                "rationale": (
                    "Incorrect. The DISM command is a valid alternative (especially for offline "
                    "scenarios), but the GUI path through 'Turn Windows features on or off' also "
                    "works and is faster for a connected workstation. It is not the ONLY method."
                ),
            },
        ],
        "explanation": (
            ".NET Framework 3.5 (which includes 2.0 and 3.0) is a Windows optional feature, "
            "not a standalone download required on modern Windows. Control Panel → Programs → "
            "'Turn Windows features on or off' is the GUI method; on connected workstations "
            "it fetches the payload from Windows Update automatically. DISM /Enable-Feature "
            ":NetFx3 is the command-line equivalent, useful for scripted or offline deployments."
        ),
    },
    # ── File systems (NTFS/FAT32/exFAT/APFS/ext4) ────────────────────────────
    {
        "id": "c2d1v2-018",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A technician connects a portable SSD formatted as NTFS to a MacBook Pro "
            "running macOS Ventura. The technician needs to copy large video files (each "
            "10–50 GB) FROM the Mac TO the NTFS drive. What behavior should the technician expect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "macOS will read and write NTFS natively with full support; no issues expected.",
                "correct": False,
                "rationale": (
                    "Incorrect. macOS provides native READ support for NTFS but only limited, "
                    "experimental write support (disabled by default). Without third-party drivers, "
                    "the NTFS volume mounts as read-only on macOS."
                ),
            },
            {
                "id": "b",
                "text": "macOS mounts NTFS as read-only by default; writes will fail. A third-party NTFS driver (e.g., Paragon NTFS) is required for write access.",
                "correct": True,
                "rationale": (
                    "Correct. macOS includes an NTFS read driver but the write driver is "
                    "disabled by default. Copying files FROM the Mac TO the NTFS drive "
                    "requires write access, which fails silently or with an error. "
                    "Third-party drivers like Paragon NTFS for Mac or Microsoft NTFS for "
                    "Mac (Seagate) enable full read/write."
                ),
            },
            {
                "id": "c",
                "text": "macOS will reformat the NTFS drive to APFS automatically to enable write access.",
                "correct": False,
                "rationale": (
                    "Incorrect. macOS does not reformat external drives automatically. "
                    "It will mount the NTFS volume as read-only and present a warning if "
                    "write access is attempted."
                ),
            },
            {
                "id": "d",
                "text": "NTFS files larger than 4 GB cannot be transferred on macOS regardless of the driver.",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS supports files far larger than 4 GB. The 4 GB file size "
                    "limit applies to FAT32, not NTFS."
                ),
            },
        ],
        "explanation": (
            "macOS includes an NTFS read driver (built into the kernel) that mounts NTFS "
            "volumes as read-only for safety. Native write support exists but is disabled "
            "because it is not fully stable. To write to an NTFS volume from macOS, users "
            "must install a third-party NTFS driver. Alternatively, reformatting the drive "
            "as exFAT provides native read/write on both platforms."
        ),
    },
    {
        "id": "c2d1v2-019",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A Linux server's /home partition uses ext4. A systems administrator runs "
            "'tune2fs -l /dev/sdb1' and notes the 'Filesystem features' line includes "
            "'has_journal'. The admin plans to mount the partition with the 'noatime' "
            "option. Which statement BEST describes the relationship between these two features?"
        ),
        "options": [
            {
                "id": "a",
                "text": "has_journal and noatime are mutually exclusive; enabling noatime disables the ext4 journal.",
                "correct": False,
                "rationale": (
                    "Incorrect. The ext4 journal (has_journal) tracks metadata changes for "
                    "crash recovery. The 'noatime' mount option suppresses file access-time "
                    "updates. They are independent features and can both be active simultaneously."
                ),
            },
            {
                "id": "b",
                "text": "has_journal provides crash consistency for metadata writes; noatime reduces write I/O by not updating the atime metadata field on each file read.",
                "correct": True,
                "rationale": (
                    "Correct. The ext4 journal (enabled by has_journal) records metadata "
                    "transactions to allow clean recovery after a crash. 'noatime' is a "
                    "mount option that prevents ext4 from updating the access-time (atime) "
                    "attribute whenever a file is read, reducing unnecessary write traffic "
                    "on busy file servers. Both can coexist."
                ),
            },
            {
                "id": "c",
                "text": "noatime bypasses the ext4 journal for all read operations, improving read performance.",
                "correct": False,
                "rationale": (
                    "Incorrect. noatime simply stops writing the access-time metadata to "
                    "disk on file reads. It does not bypass or interact with the journaling "
                    "mechanism for read operations."
                ),
            },
            {
                "id": "d",
                "text": "has_journal is equivalent to NTFS's MFT; noatime disables the MFT mirror.",
                "correct": False,
                "rationale": (
                    "Incorrect. has_journal is ext4's transaction journal, not equivalent to "
                    "the NTFS Master File Table. The MFT is NTFS-specific; noatime is a Linux "
                    "mount option with no NTFS equivalent relationship."
                ),
            },
        ],
        "explanation": (
            "ext4's has_journal feature enables transaction journaling (similar to NTFS's "
            "$LogFile), ensuring metadata consistency after a crash. The 'noatime' mount "
            "option (set in /etc/fstab) prevents updating the file access timestamp on each "
            "read, reducing write overhead—especially important on SSDs and high-throughput "
            "servers. These features are independent and complementary."
        ),
    },
    # ── Partitioning (GPT vs MBR) ─────────────────────────────────────────────
    {
        "id": "c2d1v2-020",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Partitioning (GPT vs MBR)",
        "stem": (
            "A technician uses the diskpart command 'list disk' and sees Disk 0 (500 GB) "
            "with a * in the 'Gpt' column, and Disk 1 (2 TB) with no * in the 'Gpt' column. "
            "The technician needs to add Disk 1 as additional storage and create a single "
            "data volume that uses all 2 TB. Disk 1 currently has no data. What must the "
            "technician do FIRST before creating the partition on Disk 1?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Nothing; an MBR disk supports partitions up to 2 TB, so a single primary partition can span the full disk.",
                "correct": False,
                "rationale": (
                    "Incorrect. MBR supports a maximum partition size of 2 TiB (2,199 GB). "
                    "A 2 TB (2,000 GB decimal / ~1.82 TiB) drive fits within MBR limits, "
                    "but conventional MBR disks are limited to four primary partitions and "
                    "the question specifies a 2 TB drive. However, the key issue is that for "
                    "drives at or approaching the 2 TiB boundary, GPT is strongly recommended, "
                    "and converting is best practice—especially since only 3 primary partitions "
                    "remain usable with an extended partition structure."
                ),
            },
            {
                "id": "b",
                "text": "Run 'select disk 1' then 'convert gpt' to convert Disk 1 to GPT before creating the partition.",
                "correct": True,
                "rationale": (
                    "Correct. Although 2 TB (decimal) is technically within MBR's range, "
                    "best practice—and the CompTIA A+ objective—calls for GPT on any large "
                    "data disk. 'select disk 1' followed by 'convert gpt' converts the empty "
                    "MBR disk to GPT, enabling a single large primary partition across all "
                    "available space without MBR limitations."
                ),
            },
            {
                "id": "c",
                "text": "Format the disk as exFAT first; exFAT does not have the MBR partition size restriction.",
                "correct": False,
                "rationale": (
                    "Incorrect. exFAT is a file system, not a partition table type. Formatting "
                    "a disk as exFAT does not change the underlying MBR partition table or "
                    "its limitations."
                ),
            },
            {
                "id": "d",
                "text": "Reboot into Windows Recovery to convert the partition table; diskpart cannot change partition tables on running systems.",
                "correct": False,
                "rationale": (
                    "Incorrect. diskpart can convert empty disks between MBR and GPT (using "
                    "'convert gpt' or 'convert mbr') on a running system, as long as the disk "
                    "has no partitions (or they have been deleted with 'clean')."
                ),
            },
        ],
        "explanation": (
            "GPT is the modern partition table standard, required for UEFI boot disks and "
            "recommended for all disks larger than ~2 TiB. In diskpart, 'select disk N' "
            "targets the disk; 'convert gpt' rewrites the partition table to GPT (the disk "
            "must have no partitions, or 'clean' must be run first). After conversion, "
            "'create partition primary' spans the entire disk."
        ),
    },
    # ── OS installation & upgrade methods ────────────────────────────────────
    {
        "id": "c2d1v2-021",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician must deploy Windows 11 to a new workstation that has no existing "
            "OS and lacks a USB port but has a network card with PXE support. The environment "
            "has a Windows Deployment Services (WDS) server on the same subnet. "
            "What BIOS/UEFI setting must the technician configure to initiate a PXE boot?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable Legacy Boot (CSM) to allow PXE booting.",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 requires UEFI, not Legacy/CSM mode. Modern WDS "
                    "and PXE boot work in UEFI mode; enabling CSM/Legacy would prevent "
                    "Windows 11 installation."
                ),
            },
            {
                "id": "b",
                "text": "Set the network adapter (PXE) as the first boot device in the UEFI boot order.",
                "correct": True,
                "rationale": (
                    "Correct. To PXE boot, the UEFI firmware must be configured to attempt "
                    "network boot before trying hard drives. Setting the NIC/PXE as the "
                    "first boot device causes the system to broadcast a DHCP/BOOTP request, "
                    "receive a WDS response, and download the WinPE boot image."
                ),
            },
            {
                "id": "c",
                "text": "Disable Secure Boot to allow the unsigned PXE boot image to load.",
                "correct": False,
                "rationale": (
                    "Incorrect. Secure Boot does not need to be disabled for WDS PXE booting; "
                    "WDS supports Secure Boot using signed boot images (bootmgfw.efi). "
                    "Disabling Secure Boot would violate Windows 11's requirements."
                ),
            },
            {
                "id": "d",
                "text": "Connect the WDS server's IP address as a static DNS entry in UEFI to resolve the WDS hostname.",
                "correct": False,
                "rationale": (
                    "Incorrect. PXE boot uses DHCP broadcast (or DHCP option 66/67) to "
                    "locate the boot server; it does not rely on DNS resolution configured "
                    "in UEFI settings."
                ),
            },
        ],
        "explanation": (
            "PXE (Preboot Execution Environment) boot requires the NIC to be the first boot "
            "device in UEFI boot priority. The NIC sends a DHCP discover; the DHCP server "
            "(or WDS proxy DHCP) replies with the WDS server address and boot filename. "
            "UEFI PXE is compatible with Secure Boot when WDS serves a signed boot image. "
            "CSM/Legacy mode is incompatible with Windows 11's UEFI requirement."
        ),
    },
    {
        "id": "c2d1v2-022",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "An enterprise administrator uses sysprep to prepare a Windows 11 reference image "
            "for capture with DISM. After running 'sysprep /generalize /oobe /shutdown', the "
            "image is captured and deployed to 50 workstations. Users report that each "
            "workstation has a different computer name generated automatically. The admin wants "
            "all future deployments to name computers using the format 'WS-' followed by the "
            "last 7 characters of the MAC address. Where is this naming convention configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "In the sysprep GUI under 'System Preparation Tool settings'.",
                "correct": False,
                "rationale": (
                    "Incorrect. The sysprep GUI does not have a computer naming convention "
                    "setting. Naming is handled through an unattend.xml answer file or "
                    "a deployment tool script."
                ),
            },
            {
                "id": "b",
                "text": "In the unattend.xml answer file under the specialize pass, using the ComputerName element with a naming convention variable.",
                "correct": True,
                "rationale": (
                    "Correct. The Windows Setup answer file (unattend.xml) supports the "
                    "ComputerName element in the 'specialize' configuration pass. Deployment "
                    "tools (MDT, SCCM) extend this with variables like %MACADDRESS% or "
                    "custom scripts that generate the WS-<MAC> format at deployment time."
                ),
            },
            {
                "id": "c",
                "text": "In the DISM /capture-image command using the /ComputerName switch.",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM /capture-image captures a disk image to a WIM file; it "
                    "does not have a /ComputerName switch and does not configure the naming "
                    "convention applied during deployment."
                ),
            },
            {
                "id": "d",
                "text": "In the Windows 11 installer boot menu by pressing F8 and entering the computer name manually at each station.",
                "correct": False,
                "rationale": (
                    "Incorrect. Manually entering names at each of 50 workstations during "
                    "setup is not scalable and contradicts the goal of automated deployment. "
                    "Unattend.xml is the correct automation mechanism."
                ),
            },
        ],
        "explanation": (
            "sysprep /generalize removes machine-specific data (SID, computer name, event logs). "
            "The OOBE phase then generates a random new name unless overridden. To enforce a "
            "naming convention, the unattend.xml 'specialize' pass ComputerName element is used; "
            "deployment tools (MDT/SCCM) inject MAC-based or asset-tag-based names using task "
            "sequence variables. This is the standard enterprise PC naming automation pattern."
        ),
    },
    # ── macOS features & tools ────────────────────────────────────────────────
    {
        "id": "c2d1v2-023",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A macOS user notices their MacBook Pro (M2, macOS Ventura) is running slow "
            "and the fan is very loud. They open Activity Monitor and see a process called "
            "'mdworker_shared' consuming 90% CPU. What is this process and what is the "
            "APPROPRIATE action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "mdworker_shared is malware; terminate it and run a full antivirus scan.",
                "correct": False,
                "rationale": (
                    "Incorrect. mdworker_shared is a legitimate macOS process—part of the "
                    "Spotlight indexing subsystem (mds = metadata server). Misidentifying it "
                    "as malware and terminating it is incorrect."
                ),
            },
            {
                "id": "b",
                "text": "mdworker_shared is the Spotlight indexing process; high CPU is normal after a system update, new drive connection, or Spotlight rebuild. Wait for indexing to complete.",
                "correct": True,
                "rationale": (
                    "Correct. mdworker_shared is a Spotlight metadata worker that performs "
                    "file content indexing. High CPU usage is expected (and temporary) after "
                    "macOS updates, connecting new volumes, or forcing a Spotlight index rebuild. "
                    "The correct action is to wait; it will complete and CPU usage will drop."
                ),
            },
            {
                "id": "c",
                "text": "mdworker_shared indicates a failing SSD; replace the drive immediately.",
                "correct": False,
                "rationale": (
                    "Incorrect. mdworker_shared being busy is not a sign of drive failure. "
                    "Drive health should be checked with Disk Utility or SMART monitoring "
                    "tools based on SMART data, not Activity Monitor CPU usage."
                ),
            },
            {
                "id": "d",
                "text": "Disable Spotlight permanently to prevent mdworker_shared from running.",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling Spotlight eliminates search functionality across "
                    "macOS. This is a disproportionate response to a temporary indexing "
                    "condition. If needed, System Settings → Siri & Spotlight can add folders "
                    "to the Privacy tab to exclude specific locations."
                ),
            },
        ],
        "explanation": (
            "Spotlight (mds/mdworker) is macOS's metadata indexing engine. mdworker_shared "
            "processes file metadata for search. Heavy CPU usage is expected after OS updates, "
            "large file additions, or connecting new volumes—the index rebuild is temporary. "
            "To limit Spotlight's scope, add folders to the Privacy exclusion list in System "
            "Settings → Siri & Spotlight. Forced rebuilds can be triggered with "
            "'sudo mdutil -E /' in Terminal."
        ),
    },
    {
        "id": "c2d1v2-024",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A Mac administrator needs to check available disk space, repair disk permissions, "
            "and verify the integrity of an external APFS volume from the macOS command line "
            "(Terminal). Which tool is the macOS command-line equivalent of Disk Utility for "
            "these tasks?"
        ),
        "options": [
            {
                "id": "a",
                "text": "fsck",
                "correct": False,
                "rationale": (
                    "Incorrect. fsck (file system check) checks and repairs file system errors "
                    "but is typically run in single-user mode on unmounted volumes. It does not "
                    "provide disk space reporting or APFS-specific operations like 'repair permissions'."
                ),
            },
            {
                "id": "b",
                "text": "diskutil",
                "correct": True,
                "rationale": (
                    "Correct. 'diskutil' is the command-line interface to Disk Utility on macOS. "
                    "It supports listing disks (diskutil list), verifying/repairing volumes "
                    "(diskutil verifyVolume / repairVolume), checking filesystem info "
                    "(diskutil info /dev/diskX), and APFS-specific commands (diskutil apfs ...)."
                ),
            },
            {
                "id": "c",
                "text": "df -h",
                "correct": False,
                "rationale": (
                    "Incorrect. 'df -h' reports available disk space for mounted volumes but "
                    "cannot repair disk permissions or verify APFS volume integrity."
                ),
            },
            {
                "id": "d",
                "text": "hdiutil",
                "correct": False,
                "rationale": (
                    "Incorrect. hdiutil manages disk image files (DMG)—creating, attaching, "
                    "and verifying disk images. It does not manage physical disks or live "
                    "file system repair."
                ),
            },
        ],
        "explanation": (
            "diskutil is the macOS command-line disk management tool, mirroring the GUI "
            "Disk Utility app. It supports partition listing, volume verification/repair, "
            "formatting, partition resizing, and APFS container management. "
            "'diskutil verifyVolume disk2s1' checks the APFS volume; "
            "'diskutil info /dev/disk2s1' shows capacity and usage. df -h shows space; "
            "fsck is for offline repair; hdiutil handles disk image files."
        ),
    },
    # ── Linux commands ────────────────────────────────────────────────────────
    {
        "id": "c2d1v2-025",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator needs to display the last 50 lines of /var/log/syslog "
            "and then continue watching it in real time as new log entries are written, "
            "to monitor an ongoing service restart. Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "cat /var/log/syslog | grep -c 50",
                "correct": False,
                "rationale": (
                    "Incorrect. 'grep -c' counts matching lines; this does not display the "
                    "last 50 lines or provide real-time monitoring."
                ),
            },
            {
                "id": "b",
                "text": "tail -n 50 -f /var/log/syslog",
                "correct": True,
                "rationale": (
                    "Correct. 'tail -n 50' displays the last 50 lines of the file; the '-f' "
                    "(follow) flag keeps the file open and prints new lines as they are "
                    "appended, providing real-time log monitoring."
                ),
            },
            {
                "id": "c",
                "text": "head -n 50 /var/log/syslog",
                "correct": False,
                "rationale": (
                    "Incorrect. 'head -n 50' displays the FIRST 50 lines of the file, not "
                    "the last, and does not follow the file for new entries."
                ),
            },
            {
                "id": "d",
                "text": "watch -n 1 cat /var/log/syslog",
                "correct": False,
                "rationale": (
                    "Incorrect. 'watch -n 1 cat /var/log/syslog' re-runs 'cat' every second, "
                    "printing the entire file and clearing the screen each time. This is "
                    "inefficient for large logs and does not provide the clean append-following "
                    "behavior of 'tail -f'."
                ),
            },
        ],
        "explanation": (
            "'tail -f' (follow) is the standard Unix/Linux command for real-time log monitoring. "
            "'-n 50' sets the initial output to the last 50 lines. Combined as 'tail -n 50 -f', "
            "it outputs the last 50 lines and then streams each new entry as it is written. "
            "head shows the beginning; cat requires re-running; watch with cat is inefficient."
        ),
    },
    {
        "id": "c2d1v2-026",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux system administrator needs to determine which package owns the file "
            "'/usr/bin/python3' on a Debian/Ubuntu system, because an upgrade changed the "
            "Python binary and broke a script. Which command identifies the owning package?"
        ),
        "options": [
            {
                "id": "a",
                "text": "dpkg -S /usr/bin/python3",
                "correct": True,
                "rationale": (
                    "Correct. On Debian/Ubuntu systems, 'dpkg -S <file_path>' (search) "
                    "queries the package database to find which installed package owns the "
                    "specified file. It returns the package name and version."
                ),
            },
            {
                "id": "b",
                "text": "rpm -qf /usr/bin/python3",
                "correct": False,
                "rationale": (
                    "Incorrect. 'rpm -qf' is the equivalent command on RPM-based distributions "
                    "(Red Hat, CentOS, Fedora). Ubuntu/Debian uses dpkg, not rpm."
                ),
            },
            {
                "id": "c",
                "text": "which python3",
                "correct": False,
                "rationale": (
                    "Incorrect. 'which python3' finds the path of the python3 binary in the "
                    "current PATH. It does not identify which package installed the binary."
                ),
            },
            {
                "id": "d",
                "text": "file /usr/bin/python3",
                "correct": False,
                "rationale": (
                    "Incorrect. 'file' identifies a file's type (ELF executable, script, etc.) "
                    "based on its magic bytes. It does not query the package database."
                ),
            },
        ],
        "explanation": (
            "On Debian/Ubuntu, dpkg is the package manager. 'dpkg -S <path>' queries the "
            "installed package database to identify which package installed a given file. "
            "For example: 'dpkg -S /usr/bin/python3' might return 'python3-minimal: /usr/bin/python3'. "
            "The RPM equivalent is 'rpm -qf'; on systems with apt, 'apt-file search' also works "
            "but requires installing the apt-file package."
        ),
    },
    {
        "id": "c2d1v2-027",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator needs to add a persistent static route so that traffic "
            "destined for the 172.16.50.0/24 network is sent through the gateway 10.0.0.1. "
            "The change must survive a reboot on an Ubuntu 20.04 server using Netplan. "
            "Which approach accomplishes this persistently?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run 'ip route add 172.16.50.0/24 via 10.0.0.1'; this persists across reboots.",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ip route add' adds a route to the running kernel routing "
                    "table only. It is lost on reboot because it is not written to any "
                    "persistent configuration file."
                ),
            },
            {
                "id": "b",
                "text": "Edit the Netplan YAML configuration file (e.g., /etc/netplan/01-netcfg.yaml) to add the route under the interface's 'routes:' section, then run 'netplan apply'.",
                "correct": True,
                "rationale": (
                    "Correct. On Ubuntu 20.04 with Netplan, network configuration (including "
                    "static routes) is defined in YAML files under /etc/netplan/. Adding the "
                    "route under the interface's 'routes:' key and running 'netplan apply' "
                    "makes the route persistent across reboots."
                ),
            },
            {
                "id": "c",
                "text": "Add the route to /etc/network/interfaces using 'up route add -net 172.16.50.0 netmask 255.255.255.0 gw 10.0.0.1'.",
                "correct": False,
                "rationale": (
                    "Incorrect. /etc/network/interfaces is the legacy ifupdown configuration "
                    "file. On Ubuntu 20.04 with Netplan as the default renderer, changes to "
                    "/etc/network/interfaces are ignored by the running network stack unless "
                    "ifupdown is explicitly configured as the renderer."
                ),
            },
            {
                "id": "d",
                "text": "Add the route to /etc/rc.local so it runs at boot.",
                "correct": False,
                "rationale": (
                    "Incorrect. /etc/rc.local is deprecated on modern systemd-based Ubuntu "
                    "and may not be executed. Even if executed, it uses 'ip route add' which "
                    "adds a runtime route but is not the correct Netplan-managed configuration."
                ),
            },
        ],
        "explanation": (
            "Ubuntu 20.04 LTS uses Netplan as its default network configuration abstraction "
            "layer. Persistent routes must be defined in the Netplan YAML files "
            "(/etc/netplan/*.yaml) under the interface's 'routes:' stanza. After editing, "
            "'netplan apply' activates the configuration. 'ip route add' is ephemeral; "
            "/etc/network/interfaces and /etc/rc.local are legacy mechanisms not managed "
            "by Netplan."
        ),
    },
    {
        "id": "c2d1v2-028",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator runs 'ls -la /usr/local/bin/backup.sh' and sees:\n"
            "-rwsr-xr-x 1 root root 8192 Jun 1 10:00 backup.sh\n"
            "A junior admin asks what the 's' in the owner execute position means. "
            "Which answer is CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The 's' means the file is a symbolic link; it points to another script.",
                "correct": False,
                "rationale": (
                    "Incorrect. Symbolic links show 'l' as the file type in the first "
                    "character of the mode string (e.g., lrwxrwxrwx). The 's' in the "
                    "execute position of the owner field indicates the setuid bit."
                ),
            },
            {
                "id": "b",
                "text": "The 's' in the owner execute position is the setuid bit; when executed, the process runs with the file owner's (root's) privileges regardless of who invokes it.",
                "correct": True,
                "rationale": (
                    "Correct. The setuid (Set User ID) bit on an executable causes it to run "
                    "with the privileges of the file's owner—in this case root—when executed "
                    "by any user. This is how commands like 'sudo' and 'passwd' gain elevated "
                    "privileges temporarily."
                ),
            },
            {
                "id": "c",
                "text": "The 's' means the file is locked (sticky) so only root can delete it.",
                "correct": False,
                "rationale": (
                    "Incorrect. The sticky bit appears as 't' in the others execute position "
                    "(e.g., on /tmp: drwxrwxrwt). It restricts file deletion to the owner. "
                    "The 's' in the owner execute position is the setuid bit, not sticky."
                ),
            },
            {
                "id": "d",
                "text": "The 's' means the script requires a secure shell (SSH) connection to run.",
                "correct": False,
                "rationale": (
                    "Incorrect. File mode bits have no relationship to network protocols. "
                    "The 's' in the permission field is a setuid or setgid bit, not an "
                    "SSH requirement."
                ),
            },
        ],
        "explanation": (
            "The setuid bit ('s' in owner execute position) causes an executable to run with "
            "the UID of the file owner rather than the calling user. For root-owned setuid "
            "binaries (rwsr-xr-x), any user who executes the file gains root-level privileges "
            "for the duration of that process. This is used legitimately by passwd, ping, sudo, "
            "etc. Setuid scripts are a significant security risk and are often disabled by "
            "modern kernels."
        ),
    },
    # ── Linux file permissions ─────────────────────────────────────────────────
    {
        "id": "c2d1v2-029",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux file permissions",
        "stem": (
            "A Linux administrator runs 'umask' on a new user account and sees the value '0022'. "
            "The admin creates a new file with 'touch newfile.txt'. "
            "What will the resulting permissions on newfile.txt be?"
        ),
        "options": [
            {
                "id": "a",
                "text": "-rwxrwxrwx (777)",
                "correct": False,
                "rationale": (
                    "Incorrect. 777 is the base permission for directories; files start with "
                    "a base of 666 (rw-rw-rw-). Also, umask subtracts permissions—0022 umask "
                    "applied to a file base of 666 yields 644, not 777."
                ),
            },
            {
                "id": "b",
                "text": "-rw-r--r-- (644)",
                "correct": True,
                "rationale": (
                    "Correct. Files are created with a base permission of 0666 "
                    "(rw-rw-rw-). The umask of 0022 is subtracted: 666 - 022 = 644 (rw-r--r--). "
                    "The owner gets read/write; group and others get read only."
                ),
            },
            {
                "id": "c",
                "text": "-rw------- (600)",
                "correct": False,
                "rationale": (
                    "Incorrect. 600 would result from a umask of 0066 "
                    "(666 - 066 = 600). A umask of 0022 removes write from group and "
                    "others, resulting in 644."
                ),
            },
            {
                "id": "d",
                "text": "-rwxr-xr-x (755)",
                "correct": False,
                "rationale": (
                    "Incorrect. 755 results from applying umask 022 to the directory base "
                    "of 777 (777 - 022 = 755). Files use a base of 666, not 777, because "
                    "the kernel never grants execute bits on newly created regular files."
                ),
            },
        ],
        "explanation": (
            "The umask value is subtracted from the default permission base. For regular files, "
            "the base is 0666 (rw-rw-rw-); for directories it is 0777 (rwxrwxrwx). "
            "With umask 0022: 0666 - 0022 = 0644 (rw-r--r--). The umask 0022 removes write "
            "permission for group and others. Execute is never granted to files by default "
            "via touch regardless of umask."
        ),
    },
    # ── Multiple Response ─────────────────────────────────────────────────────
    {
        "id": "c2d1v2-030",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician is investigating intermittent network connectivity on a Windows "
            "workstation. Which TWO command-line tools can help identify packet loss and "
            "latency between the workstation and a remote host, providing both hop-by-hop "
            "path information AND per-hop loss statistics? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "pathping",
                "correct": True,
                "rationale": (
                    "Correct. pathping combines the functionality of ping and tracert: it "
                    "first traces the path (hop-by-hop), then sends multiple pings to each "
                    "hop to calculate per-hop packet loss percentages and latency statistics."
                ),
            },
            {
                "id": "b",
                "text": "tracert",
                "correct": True,
                "rationale": (
                    "Correct. tracert (traceroute) maps the hop-by-hop path to a destination "
                    "using TTL-expiry ICMP messages and shows per-hop round-trip times, "
                    "helping identify where latency or packet drops begin."
                ),
            },
            {
                "id": "c",
                "text": "nslookup",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup performs DNS name resolution queries; it does not "
                    "measure network path latency or packet loss."
                ),
            },
            {
                "id": "d",
                "text": "ipconfig /flushdns",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /flushdns clears the local DNS resolver cache; "
                    "it does not diagnose network path issues or measure packet loss."
                ),
            },
        ],
        "explanation": (
            "pathping sends a defined number of packets to each hop and calculates per-hop "
            "loss percentages—ideal for pinpointing where loss occurs. tracert maps the "
            "path and shows per-hop RTT, quickly identifying latency spikes. Together they "
            "provide complete path diagnostics. nslookup tests DNS; ipconfig /flushdns "
            "clears DNS cache—neither helps with packet loss analysis."
        ),
    },
    {
        "id": "c2d1v2-031",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A company stores archived video files on a NAS. They need a file system for a "
            "new 8 TB internal archive volume on a Windows Server 2019 system that supports "
            "BOTH file-level NTFS compression to save space AND disk quotas per department "
            "user account. Which TWO file systems available on Windows Server 2019 support "
            "BOTH of these features? (Choose TWO — select only valid options.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "NTFS",
                "correct": True,
                "rationale": (
                    "Correct. NTFS supports both native file/folder compression (transparent "
                    "to applications) and per-user disk quota enforcement, making it the "
                    "primary candidate."
                ),
            },
            {
                "id": "b",
                "text": "ReFS",
                "correct": False,
                "rationale": (
                    "Incorrect. ReFS does not support NTFS-style file compression or per-user "
                    "disk quotas. These are deliberate design omissions in ReFS, which focuses "
                    "on data integrity rather than space efficiency features."
                ),
            },
            {
                "id": "c",
                "text": "FAT32",
                "correct": False,
                "rationale": (
                    "Incorrect. FAT32 does not support file-level compression, disk quotas, "
                    "or files larger than 4 GB. It is not appropriate for an 8 TB volume "
                    "(FAT32 volume limit is 32 GB formatted by Windows)."
                ),
            },
            {
                "id": "d",
                "text": "NTFS on a second volume configured identically",
                "correct": True,
                "rationale": (
                    "Correct. A second NTFS volume on the same or different disk inherits "
                    "all NTFS capabilities including compression and quotas. Both NTFS volumes "
                    "satisfy the requirements—this option confirms NTFS is the only Windows "
                    "Server file system meeting both criteria."
                ),
            },
        ],
        "explanation": (
            "NTFS is the only Windows Server file system that natively supports both "
            "transparent file-level compression (set via file/folder Properties → Advanced) "
            "and per-user disk quotas (configured in volume Properties → Quota tab). "
            "ReFS prioritizes integrity scrubbing over compression/quotas. FAT32 is "
            "unsuitable for multi-TB volumes and lacks both features. exFAT is not "
            "supported as a Windows Server volume file system."
        ),
    },
    {
        "id": "c2d1v2-032",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator needs to check the current disk space usage of all mounted "
            "file systems AND see the inode usage, because a file system reported 'No space "
            "left on device' despite showing available blocks. Which TWO commands provide "
            "this information? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "df -h",
                "correct": True,
                "rationale": (
                    "Correct. 'df -h' (disk free, human-readable) shows used and available "
                    "blocks for all mounted file systems, helping identify which volume is "
                    "full in terms of disk blocks."
                ),
            },
            {
                "id": "b",
                "text": "df -i",
                "correct": True,
                "rationale": (
                    "Correct. 'df -i' displays inode usage (total, used, free inodes) for "
                    "each mounted file system. A 'No space left' error with available blocks "
                    "typically means inodes are exhausted—df -i confirms this."
                ),
            },
            {
                "id": "c",
                "text": "du /",
                "correct": False,
                "rationale": (
                    "Incorrect. 'du' (disk usage) reports how much space individual files and "
                    "directories consume but does not report file system-level free space or "
                    "inode availability."
                ),
            },
            {
                "id": "d",
                "text": "lsblk",
                "correct": False,
                "rationale": (
                    "Incorrect. 'lsblk' lists block devices and their partition structure but "
                    "does not show file system free space or inode utilization."
                ),
            },
        ],
        "explanation": (
            "'df -h' shows human-readable block usage per mount point. 'df -i' shows inode "
            "usage. When a file system reports 'No space left on device' but df -h shows free "
            "blocks, inode exhaustion is the cause—check df -i. Inode exhaustion occurs when "
            "a directory contains a massive number of small files consuming all inodes while "
            "block space remains. The fix is deleting files to free inodes."
        ),
    },
    {
        "id": "c2d1v2-033",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician is preparing a reference Windows 11 image using sysprep. "
            "Which TWO actions does 'sysprep /generalize' perform to prepare the image "
            "for deployment to multiple computers? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Removes the unique machine Security Identifier (SID) so each deployed copy can generate its own unique SID.",
                "correct": True,
                "rationale": (
                    "Correct. /generalize removes the machine SID, computer name, and other "
                    "unique machine identifiers so that when the image is deployed, Windows "
                    "Setup generates a new unique SID for each instance. Duplicate SIDs cause "
                    "domain and authentication problems."
                ),
            },
            {
                "id": "b",
                "text": "Clears the event logs so that only events generated after deployment appear on each target machine.",
                "correct": True,
                "rationale": (
                    "Correct. sysprep /generalize clears the Windows event logs as part of the "
                    "generalization process, ensuring that target systems start with clean logs "
                    "and do not inherit events from the reference build machine."
                ),
            },
            {
                "id": "c",
                "text": "Encrypts the image with BitLocker to secure it during transport on the network.",
                "correct": False,
                "rationale": (
                    "Incorrect. sysprep does not encrypt the image. BitLocker encryption is "
                    "a separate feature managed independently; sysprep /generalize actually "
                    "requires BitLocker to be suspended or disabled before running."
                ),
            },
            {
                "id": "d",
                "text": "Installs the latest Windows Updates on the reference machine before capturing.",
                "correct": False,
                "rationale": (
                    "Incorrect. sysprep does not install Windows Updates. Updates should be "
                    "applied to the reference machine before running sysprep, but sysprep "
                    "itself does not perform update installation."
                ),
            },
        ],
        "explanation": (
            "sysprep /generalize prepares a Windows image for deployment by removing machine-specific "
            "data: it deletes the SID (ensuring each deployed copy generates a unique SID), "
            "removes the computer name, clears event logs, and resets plug-and-play device "
            "states. This generalization makes the image deployable to any compatible hardware "
            "without identity conflicts. BitLocker must be off; sysprep does not install updates."
        ),
    },
    {
        "id": "c2d1v2-034",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "A security auditor reviews a Windows 11 environment and asks which editions "
            "support Windows Sandbox—an isolated, disposable desktop environment for "
            "safely running untrusted applications. Which TWO Windows 11 editions support "
            "Windows Sandbox? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows 11 Pro",
                "correct": True,
                "rationale": (
                    "Correct. Windows Sandbox is available on Windows 11 Pro (and higher). "
                    "It requires virtualization enabled in BIOS and the Windows Sandbox "
                    "optional feature to be turned on."
                ),
            },
            {
                "id": "b",
                "text": "Windows 11 Enterprise",
                "correct": True,
                "rationale": (
                    "Correct. Windows Sandbox is available on Windows 11 Enterprise, providing "
                    "the same isolated virtualized environment. Enterprise also adds more "
                    "advanced security features like Application Guard."
                ),
            },
            {
                "id": "c",
                "text": "Windows 11 Home",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Sandbox is NOT available on Windows 11 Home. Home "
                    "lacks the Hyper-V hypervisor required to run Sandbox, and the feature "
                    "is not listed as an optional feature in the Home edition."
                ),
            },
            {
                "id": "d",
                "text": "Windows 11 SE",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 SE is a restricted education SKU with a limited "
                    "feature set; it does not include Windows Sandbox."
                ),
            },
        ],
        "explanation": (
            "Windows Sandbox (introduced in Windows 10 1903) requires Hyper-V virtualization "
            "and is available on Windows 10/11 Pro, Pro for Workstations, and Enterprise. "
            "It is NOT available on Home edition because Home does not include the Hyper-V "
            "hypervisor. Windows Sandbox is enabled via 'Turn Windows features on or off' "
            "and requires hardware virtualization (VT-x/AMD-V) enabled in UEFI/BIOS."
        ),
    },
    {
        "id": "c2d1v2-035",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A technician is preparing a Windows 11 workstation for a new employee. "
            "Which TWO Control Panel or Settings locations allow the technician to "
            "add a new local user account to the workstation? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → User Accounts → Manage another account → Add a new user in PC settings",
                "correct": True,
                "rationale": (
                    "Correct. Control Panel → User Accounts links to account management; "
                    "the 'Add a new user in PC settings' button redirects to the Settings "
                    "app for adding local or Microsoft accounts, providing a valid path to "
                    "create accounts."
                ),
            },
            {
                "id": "b",
                "text": "Computer Management (compmgmt.msc) → Local Users and Groups → Users → right-click → New User",
                "correct": True,
                "rationale": (
                    "Correct. Computer Management → Local Users and Groups → Users provides "
                    "a right-click 'New User' option that creates a local user account with "
                    "full control over username, password, and account properties."
                ),
            },
            {
                "id": "c",
                "text": "Device Manager → Human Interface Devices → Add new user",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Manager manages hardware devices and drivers; it has "
                    "no functionality for creating user accounts."
                ),
            },
            {
                "id": "d",
                "text": "Disk Management (diskmgmt.msc) → right-click disk → Add User",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk Management manages partitions and volumes; there is no "
                    "'Add User' option and no user account functionality within it."
                ),
            },
        ],
        "explanation": (
            "Local user accounts on a Windows 11 workstation can be created through: "
            "(1) Settings → Accounts → Family & other users → Add someone else; "
            "(2) Computer Management (compmgmt.msc) → Local Users and Groups → Users → "
            "New User (which provides more direct control over account properties); and "
            "(3) the 'net user /add' command. Device Manager and Disk Management have "
            "no user account management capabilities."
        ),
    },
    # ── Remaining hard MC questions to reach 38 ───────────────────────────────
    {
        "id": "c2d1v2-036",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A Windows 10 workstation is configured to use a proxy server for all internet "
            "traffic. A new application bypasses the system proxy and connects directly, "
            "which violates corporate policy. The technician confirms the proxy is set in "
            "Internet Options, but the app uses Windows networking APIs without reading IE "
            "settings. Which additional proxy configuration must the technician set so that "
            "WinHTTP-based applications also use the corporate proxy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → Internet Options → Connections → LAN Settings → set proxy address",
                "correct": False,
                "rationale": (
                    "Incorrect. Internet Options configures the WinINet proxy used by Internet "
                    "Explorer and apps that use the WinINet API. WinHTTP is a separate stack "
                    "with its own proxy settings, not inherited from WinINet/Internet Options."
                ),
            },
            {
                "id": "b",
                "text": "Run 'netsh winhttp set proxy <proxy>:<port>' to configure the WinHTTP proxy separately.",
                "correct": True,
                "rationale": (
                    "Correct. WinHTTP and WinINet are separate Windows HTTP stacks. WinHTTP "
                    "has its own proxy configuration set via 'netsh winhttp set proxy'. "
                    "Alternatively, 'netsh winhttp import proxy source=ie' copies the current "
                    "WinINet (IE) proxy settings to WinHTTP, ensuring both stacks use the same proxy."
                ),
            },
            {
                "id": "c",
                "text": "Configure the proxy as a static route using 'route add' so all traffic is redirected.",
                "correct": False,
                "rationale": (
                    "Incorrect. Static routes work at the IP routing layer; they cannot "
                    "enforce application-level HTTP proxy usage for specific apps. The proxy "
                    "must be configured at the WinHTTP layer."
                ),
            },
            {
                "id": "d",
                "text": "Install a browser extension that forces all traffic through the proxy.",
                "correct": False,
                "rationale": (
                    "Incorrect. A browser extension only affects browser traffic. It has no "
                    "effect on the WinHTTP API used by the application in question."
                ),
            },
        ],
        "explanation": (
            "Windows has two distinct HTTP stacks: WinINet (used by Internet Explorer and "
            "WinINet-based apps, configured via Internet Options) and WinHTTP (used by Windows "
            "services and many modern apps, configured via 'netsh winhttp set proxy'). Setting "
            "a proxy in Internet Options does not automatically apply to WinHTTP clients. "
            "'netsh winhttp import proxy source=ie' migrates IE proxy settings to WinHTTP "
            "as a convenient one-time sync."
        ),
    },
    {
        "id": "c2d1v2-037",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A technician needs to verify that a Windows 10 workstation's DNS client "
            "is correctly resolving an internal hostname 'fileserver.corp.local' to "
            "the expected IP address 192.168.10.20. A recent DNS record change was made "
            "on the domain controller. The technician runs 'ping fileserver.corp.local' "
            "but it still resolves to the OLD IP 192.168.10.10. The technician already "
            "ran 'ipconfig /flushdns'. Which is the NEXT step to force resolution of "
            "the new record?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Restart the DNS Client service using 'net stop dnscache && net start dnscache'.",
                "correct": False,
                "rationale": (
                    "Incorrect. The DNS Client service (dnscache) manages the local resolver "
                    "cache. Restarting it clears the cache similarly to ipconfig /flushdns, "
                    "but the root cause may be NetBIOS name cache, not just the DNS cache."
                ),
            },
            {
                "id": "b",
                "text": "Run 'nbtstat -R' to purge and reload the remote NetBIOS name cache, then retry.",
                "correct": True,
                "rationale": (
                    "Correct. After ipconfig /flushdns clears the DNS resolver cache, stale "
                    "entries in the NetBIOS name cache (nbcache) can still override DNS "
                    "resolution. 'nbtstat -R' (uppercase R) purges and reloads the remote "
                    "NetBIOS name table cache, clearing the stale mapping."
                ),
            },
            {
                "id": "c",
                "text": "Delete the HOSTS file entry for fileserver.corp.local.",
                "correct": False,
                "rationale": (
                    "Incorrect. The HOSTS file can override DNS, but it is only relevant if "
                    "an entry for 'fileserver.corp.local' exists there. Checking the HOSTS "
                    "file is a good step, but ipconfig /flushdns would not have been needed "
                    "if HOSTS were the sole issue (HOSTS is read directly, not cached by ipconfig)."
                ),
            },
            {
                "id": "d",
                "text": "Change the workstation's preferred DNS server to 8.8.8.8 to bypass the corporate DNS.",
                "correct": False,
                "rationale": (
                    "Incorrect. The internal hostname 'fileserver.corp.local' exists only on "
                    "the corporate DNS server. Switching to a public DNS (8.8.8.8) would "
                    "make the hostname unresolvable entirely."
                ),
            },
        ],
        "explanation": (
            "Windows name resolution uses multiple caches: the DNS resolver cache (flushed "
            "by ipconfig /flushdns) and the NetBIOS name cache (cleared by nbtstat -R). "
            "If DNS cache is cleared but the old IP persists, the NetBIOS cache is the next "
            "candidate. 'nbtstat -R' purges remote name entries. Additionally, the HOSTS "
            "file (checked before DNS) should be verified. On modern networks, 'nbtstat -R' "
            "combined with ipconfig /flushdns covers both caches."
        ),
    },
    {
        "id": "c2d1v2-038",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "A Windows 11 user reports that their PC takes over 3 minutes to reach the "
            "desktop after login. A technician suspects multiple startup applications are "
            "causing the delay. The technician wants to identify and disable specific "
            "startup programs WITHOUT using Task Manager or msconfig. "
            "Which Settings location provides this capability?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → System → Storage → Cleanup recommendations",
                "correct": False,
                "rationale": (
                    "Incorrect. Cleanup recommendations identifies files that can be deleted "
                    "to free disk space; it does not manage startup applications."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Apps → Startup",
                "correct": True,
                "rationale": (
                    "Correct. Settings → Apps → Startup lists all registered startup "
                    "applications with their startup impact (Low/Medium/High) and allows "
                    "enabling or disabling each with a toggle, without needing Task Manager "
                    "or msconfig."
                ),
            },
            {
                "id": "c",
                "text": "Settings → Privacy & Security → Background apps",
                "correct": False,
                "rationale": (
                    "Incorrect. Background apps (in Windows 10; removed in Windows 11) "
                    "controlled whether UWP/Store apps could run in the background. It is "
                    "not the same as managing traditional startup programs."
                ),
            },
            {
                "id": "d",
                "text": "Settings → Windows Update → Advanced options → Active hours",
                "correct": False,
                "rationale": (
                    "Incorrect. Active hours in Windows Update defines the time window when "
                    "Windows avoids automatic reboots for updates; it has no relationship "
                    "to startup application management."
                ),
            },
        ],
        "explanation": (
            "Windows 11 Settings → Apps → Startup provides a dedicated startup manager "
            "that shows all registered startup entries, their publisher, and their measured "
            "impact on boot time (Low/Medium/High). This is the Settings-only path, equivalent "
            "to Task Manager's Startup tab but accessible without opening Task Manager. "
            "Each entry can be toggled on or off directly."
        ),
    },
]
