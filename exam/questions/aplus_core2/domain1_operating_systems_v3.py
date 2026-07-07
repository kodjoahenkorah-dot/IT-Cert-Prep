"""
CompTIA A+ Core 2 (220-1202) — Domain 1: Operating Systems
48 hard/expert scenario-based questions — v3 bank extension.
"""

QUESTIONS = [
    # ── 1.1 Windows Editions ──────────────────────────────────────────────
    {
        "id": "c2d1v3-001",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "A healthcare organization needs workstations that support Windows Sandbox "
            "(an isolated desktop environment for testing suspicious files), BitLocker "
            "encryption, and domain join. The IT manager wants the LOWEST-cost edition "
            "that satisfies all three requirements. Which Windows 11 edition qualifies?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows 11 Home",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Home does not support Windows Sandbox, "
                    "Active Directory domain join, or the full BitLocker management suite."
                ),
            },
            {
                "id": "b",
                "text": "Windows 11 Pro",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 Pro includes Windows Sandbox, full BitLocker "
                    "drive encryption, and Active Directory domain join—all at the lowest "
                    "cost among editions that satisfy all three requirements."
                ),
            },
            {
                "id": "c",
                "text": "Windows 11 Enterprise",
                "correct": False,
                "rationale": (
                    "Incorrect. Enterprise satisfies the requirements but requires volume "
                    "licensing and costs more than Pro, so it is not the minimum edition."
                ),
            },
            {
                "id": "d",
                "text": "Windows 11 SE",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 SE is a restricted edition for education devices; "
                    "it does not support Windows Sandbox or standard enterprise domain join "
                    "in the conventional sense."
                ),
            },
        ],
        "explanation": (
            "Windows 11 Pro is the lowest-cost edition that includes Windows Sandbox "
            "(requires virtualization), full BitLocker management, and Active Directory "
            "domain join. Home lacks all three; Enterprise and Pro for Workstations both "
            "qualify but cost more; SE is an education-only restricted SKU."
        ),
    },
    {
        "id": "c2d1v3-002",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "A financial institution purchases 50 new workstations and wants the OS edition "
            "that supports DirectAccess for always-on VPN, AppLocker for application "
            "whitelisting, and BranchCache for WAN optimization. Which Windows 11 edition "
            "is the MINIMUM that provides all three features?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows 11 Pro",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Pro does not include DirectAccess or AppLocker "
                    "policy enforcement; those are Enterprise-only features."
                ),
            },
            {
                "id": "b",
                "text": "Windows 11 Pro for Workstations",
                "correct": False,
                "rationale": (
                    "Incorrect. Pro for Workstations adds hardware scalability features "
                    "(ReFS, NVDIMM, dual-socket) but still does not include DirectAccess "
                    "or AppLocker enforcement."
                ),
            },
            {
                "id": "c",
                "text": "Windows 11 Enterprise",
                "correct": True,
                "rationale": (
                    "Correct. DirectAccess, AppLocker enforcement, and BranchCache in "
                    "hosted-cache mode are Enterprise (and Education) features. Enterprise "
                    "is the minimum edition that includes all three."
                ),
            },
            {
                "id": "d",
                "text": "Windows 11 Home",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 11 Home is missing the majority of enterprise "
                    "management features, including all three listed."
                ),
            },
        ],
        "explanation": (
            "DirectAccess (always-on VPN successor), AppLocker (application control policies), "
            "and BranchCache hosted-cache mode require Windows 11 Enterprise or Education. "
            "Pro and Pro for Workstations do not include these enterprise management features. "
            "Home lacks virtually all enterprise capabilities."
        ),
    },
    {
        "id": "c2d1v3-003",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows editions",
        "stem": (
            "A technician installs Windows 11 Pro on a workstation. The user later reports "
            "they cannot find the Local Group Policy Editor (gpedit.msc). When the technician "
            "tries to run gpedit.msc, the system says it cannot find the file. "
            "What is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The workstation is domain-joined; gpedit.msc is replaced by rsop.msc on domain machines.",
                "correct": False,
                "rationale": (
                    "Incorrect. Domain-joined machines still have gpedit.msc available. "
                    "rsop.msc shows the Resultant Set of Policy but does not replace gpedit.msc."
                ),
            },
            {
                "id": "b",
                "text": "The Windows 11 Pro installation was performed with a Home edition license key, causing a channel mismatch that removed gpedit.msc.",
                "correct": False,
                "rationale": (
                    "Incorrect. A license key mismatch would cause activation failure, "
                    "not selective feature removal. gpedit.msc absence is tied to the "
                    "installed edition, not the key used to activate it."
                ),
            },
            {
                "id": "c",
                "text": "The machine was actually installed with Windows 11 Home, not Pro; gpedit.msc is absent from the Home edition.",
                "correct": True,
                "rationale": (
                    "Correct. gpedit.msc (Local Group Policy Editor) is available in "
                    "Windows 11 Pro, Enterprise, and Education—but NOT in Home. If the "
                    "feature is missing, the most likely cause is a Home edition install "
                    "despite the intended Pro license."
                ),
            },
            {
                "id": "d",
                "text": "gpedit.msc was removed by Windows Defender as a potentially unwanted application.",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Defender does not quarantine or remove built-in "
                    "OS tools like gpedit.msc. This is a misconception about antivirus scope."
                ),
            },
        ],
        "explanation": (
            "The Local Group Policy Editor (gpedit.msc) is a Pro/Enterprise/Education "
            "feature absent from Windows 11 Home. If a machine purportedly running Pro "
            "cannot find gpedit.msc, the most common cause is that Home was actually "
            "installed. Confirm the edition in Settings → System → About or 'winver'."
        ),
    },
    # ── 1.2 Windows Command-Line Tools ───────────────────────────────────
    {
        "id": "c2d1v3-004",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician suspects a Windows workstation's system files have been corrupted "
            "by malware. Running 'sfc /scannow' completes but reports it could not repair "
            "some files. The technician needs to repair the component store that SFC draws "
            "from. Which command should be run NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "chkdsk C: /f",
                "correct": False,
                "rationale": (
                    "Incorrect. chkdsk /f fixes file system errors on the volume but does "
                    "not repair the Windows component store (WinSxS) that SFC uses as its "
                    "source for replacement files."
                ),
            },
            {
                "id": "b",
                "text": "DISM /Online /Cleanup-Image /RestoreHealth",
                "correct": True,
                "rationale": (
                    "Correct. When SFC cannot repair files, the Windows component store "
                    "itself is likely corrupt. DISM /Online /Cleanup-Image /RestoreHealth "
                    "downloads and replaces damaged component store files from Windows Update, "
                    "after which SFC can successfully use the repaired store."
                ),
            },
            {
                "id": "c",
                "text": "bootrec /rebuildbcd",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec /rebuildbcd repairs the Boot Configuration Data "
                    "store for boot failures. It does not address system file or component "
                    "store corruption."
                ),
            },
            {
                "id": "d",
                "text": "sfc /scannow /offbootdir=C:\\ /offwindir=C:\\Windows",
                "correct": False,
                "rationale": (
                    "Incorrect. The /offbootdir and /offwindir switches are used to scan "
                    "an offline Windows installation from WinPE—not to repair the component "
                    "store on a running system. This does not fix the underlying store corruption."
                ),
            },
        ],
        "explanation": (
            "The standard SFC → DISM repair sequence: if 'sfc /scannow' reports it cannot "
            "fix files, run 'DISM /Online /Cleanup-Image /RestoreHealth' to repair the "
            "component store (WinSxS) using Windows Update as the source, then re-run "
            "'sfc /scannow'. DISM can also use a local WIM with /Source if internet "
            "access is unavailable."
        ),
    },
    {
        "id": "c2d1v3-005",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician needs to display all currently established TCP connections on a "
            "Windows 10 machine, refreshing the output every 5 seconds to watch for "
            "suspicious connections appearing and disappearing. Which command achieves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "netstat -an 5",
                "correct": True,
                "rationale": (
                    "Correct. netstat -an displays all connections and listening ports in "
                    "numerical form. Adding the interval '5' as a trailing argument causes "
                    "netstat to redisplay the output every 5 seconds continuously."
                ),
            },
            {
                "id": "b",
                "text": "netstat -b -r",
                "correct": False,
                "rationale": (
                    "Incorrect. -b shows the executable for each connection and -r shows "
                    "the routing table. Neither -r nor the combination creates a repeating "
                    "refresh interval."
                ),
            },
            {
                "id": "c",
                "text": "netstat -e 5",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat -e displays Ethernet statistics (bytes sent/received "
                    "totals), not individual TCP connections. The 5-second interval works "
                    "with -e but shows the wrong data."
                ),
            },
            {
                "id": "d",
                "text": "netstat /continuous",
                "correct": False,
                "rationale": (
                    "Incorrect. /continuous is not a valid netstat switch on Windows. "
                    "The numeric interval argument (e.g., netstat -an 5) is the correct "
                    "syntax for repeated output."
                ),
            },
        ],
        "explanation": (
            "netstat accepts an optional numeric interval argument that causes it to "
            "repeat output at that interval in seconds. 'netstat -an 5' shows all connections "
            "in numeric format, refreshing every 5 seconds. This is useful for spotting "
            "short-lived suspicious connections. Press Ctrl+C to stop."
        ),
    },
    {
        "id": "c2d1v3-006",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician needs to schedule a script named C:\\scripts\\cleanup.bat to run "
            "every day at 2:00 AM on a Windows Server, using only command-line tools. "
            "Which command creates this scheduled task?"
        ),
        "options": [
            {
                "id": "a",
                "text": "at 02:00 /every:M,T,W,Th,F,S,Su C:\\scripts\\cleanup.bat",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'at' command is deprecated in modern Windows versions "
                    "and has limited scheduling options. schtasks is the current supported "
                    "command-line scheduler."
                ),
            },
            {
                "id": "b",
                "text": "schtasks /create /tn \"DailyCleanup\" /tr C:\\scripts\\cleanup.bat /sc daily /st 02:00",
                "correct": True,
                "rationale": (
                    "Correct. schtasks /create creates a new scheduled task. /tn sets the "
                    "task name, /tr sets the executable/script to run, /sc daily sets the "
                    "daily schedule, and /st 02:00 sets the start time."
                ),
            },
            {
                "id": "c",
                "text": "taskschd.msc /create /daily /time:02:00 /script:C:\\scripts\\cleanup.bat",
                "correct": False,
                "rationale": (
                    "Incorrect. taskschd.msc is the Task Scheduler GUI application and "
                    "does not accept command-line creation parameters in this syntax."
                ),
            },
            {
                "id": "d",
                "text": "cron 0 2 * * * C:\\scripts\\cleanup.bat",
                "correct": False,
                "rationale": (
                    "Incorrect. cron is a Unix/Linux scheduling daemon. It is not natively "
                    "available on Windows (outside of WSL). Windows uses schtasks or the "
                    "Task Scheduler service."
                ),
            },
        ],
        "explanation": (
            "schtasks.exe is the Windows command-line task scheduler. Key switches: "
            "/create (new task), /tn (task name), /tr (task run—the executable), "
            "/sc (schedule type: daily, weekly, monthly, once, etc.), /st (start time "
            "in HH:MM format). The deprecated 'at' command still exists but is not "
            "recommended. cron is Linux-only."
        ),
    },
    {
        "id": "c2d1v3-007",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A remote Windows server is not responding to RDP. A technician with console "
            "access runs 'netstat -an' and sees port 3389 is NOT listed in the LISTENING "
            "state. The Remote Desktop service appears running in services.msc. "
            "Which command would MOST directly enable RDP through Windows Firewall "
            "from the command line without opening the GUI?"
        ),
        "options": [
            {
                "id": "a",
                "text": "net start TermService",
                "correct": False,
                "rationale": (
                    "Incorrect. The Remote Desktop service (TermService) is already shown "
                    "as running. The issue is the firewall, not the service state."
                ),
            },
            {
                "id": "b",
                "text": "netsh advfirewall firewall add rule name=\"RDP\" protocol=TCP dir=in localport=3389 action=allow",
                "correct": True,
                "rationale": (
                    "Correct. This netsh command adds an inbound firewall rule allowing "
                    "TCP port 3389 (RDP), which would be missing if Windows Firewall is "
                    "blocking the port despite the service running."
                ),
            },
            {
                "id": "c",
                "text": "reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 0 /f",
                "correct": False,
                "rationale": (
                    "Incorrect. This registry key enables or disables RDP at the service "
                    "level (0 = enabled). Since the service is already running and port "
                    "3389 is not listening, the issue is the firewall, not this registry "
                    "value—though both might need to be correct for RDP to function."
                ),
            },
            {
                "id": "d",
                "text": "ipconfig /flushdns",
                "correct": False,
                "rationale": (
                    "Incorrect. Flushing the DNS cache resolves name resolution issues, "
                    "not firewall blocking of inbound port 3389."
                ),
            },
        ],
        "explanation": (
            "When RDP service is running but port 3389 is not listening, the Windows "
            "Firewall is blocking the inbound connection before the service can bind. "
            "The netsh advfirewall command adds the required inbound allow rule. "
            "The registry fDenyTSConnections=0 value enables RDP at the OS level; "
            "both the registry setting and firewall rule must allow RDP for it to work."
        ),
    },
    {
        "id": "c2d1v3-008",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician needs to change the IP address of a Windows Server 2022 NIC "
            "named 'Ethernet0' to 10.0.0.50 with subnet mask 255.255.255.0 and default "
            "gateway 10.0.0.1, using only the command line. Which command is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ipconfig /set Ethernet0 10.0.0.50 255.255.255.0 10.0.0.1",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig does not have a /set switch. ipconfig is a "
                    "read-only diagnostic tool for displaying IP configuration; it cannot "
                    "assign IP addresses."
                ),
            },
            {
                "id": "b",
                "text": "netsh interface ip set address \"Ethernet0\" static 10.0.0.50 255.255.255.0 10.0.0.1",
                "correct": True,
                "rationale": (
                    "Correct. The netsh interface ip set address command assigns a static "
                    "IP. 'static' specifies a manual assignment (vs. dhcp), followed by "
                    "the IP, subnet mask, and gateway."
                ),
            },
            {
                "id": "c",
                "text": "net config server /address:10.0.0.50 /mask:255.255.255.0",
                "correct": False,
                "rationale": (
                    "Incorrect. 'net config server' manages the Server service settings "
                    "(like server description) and cannot assign IP addresses to network interfaces."
                ),
            },
            {
                "id": "d",
                "text": "route add 10.0.0.50 mask 255.255.255.0 10.0.0.1",
                "correct": False,
                "rationale": (
                    "Incorrect. The route command manages the IP routing table entries. "
                    "It adds routes, not IP address assignments to interfaces."
                ),
            },
        ],
        "explanation": (
            "netsh interface ip set address is the command-line method for setting a static "
            "IP on Windows. PowerShell equivalents include New-NetIPAddress and "
            "Set-NetIPAddress. ipconfig is display-only; route manages routing tables; "
            "net config server manages Server service properties—none can set interface IPs."
        ),
    },
    {
        "id": "c2d1v3-009",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician runs 'diskpart' and types 'list disk'. Disk 0 shows 931 GB with "
            "an asterisk (*) in the GPT column, and Disk 1 shows 465 GB with no asterisk. "
            "What does the asterisk in the GPT column indicate about Disk 0?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disk 0 is the active boot disk containing the system partition.",
                "correct": False,
                "rationale": (
                    "Incorrect. The active boot disk status is shown separately in the "
                    "partition listing. The GPT column asterisk specifically indicates "
                    "the partition table type."
                ),
            },
            {
                "id": "b",
                "text": "Disk 0 uses a GUID Partition Table (GPT) partition scheme.",
                "correct": True,
                "rationale": (
                    "Correct. In diskpart's 'list disk' output, an asterisk in the GPT "
                    "column means the disk uses GPT partitioning. No asterisk (Disk 1) "
                    "means the disk uses MBR partitioning."
                ),
            },
            {
                "id": "c",
                "text": "Disk 0 is currently selected for subsequent diskpart operations.",
                "correct": False,
                "rationale": (
                    "Incorrect. The currently selected disk is indicated by an asterisk "
                    "in the far left column of 'list disk', not in the GPT column."
                ),
            },
            {
                "id": "d",
                "text": "Disk 0 has errors and should be checked with chkdsk.",
                "correct": False,
                "rationale": (
                    "Incorrect. An asterisk in the GPT column is a normal indicator of "
                    "the partition table type—it does not signal errors."
                ),
            },
        ],
        "explanation": (
            "diskpart's 'list disk' output has several columns: Disk number, Status, Size, "
            "Free, Dyn (dynamic disk), and GPT. An asterisk in the GPT column means the "
            "disk uses GPT; blank means MBR. A separate asterisk in the leftmost position "
            "indicates the currently selected disk. GPT supports disks >2 TB and is required "
            "for UEFI boot."
        ),
    },
    {
        "id": "c2d1v3-010",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A Windows administrator needs to terminate a process named 'malware.exe' (PID 4892) "
            "immediately from the command line, including all child processes. "
            "Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "taskkill /PID 4892 /F",
                "correct": False,
                "rationale": (
                    "Incorrect. taskkill /PID 4892 /F forcefully terminates the specified "
                    "process but does NOT kill child processes spawned by that process. "
                    "The /T switch is required to include the tree."
                ),
            },
            {
                "id": "b",
                "text": "taskkill /PID 4892 /F /T",
                "correct": True,
                "rationale": (
                    "Correct. /F forces termination (doesn't wait for graceful close), "
                    "/T terminates the process tree (the specified process plus all its "
                    "child processes), and /PID 4892 targets the specific PID."
                ),
            },
            {
                "id": "c",
                "text": "net stop malware.exe",
                "correct": False,
                "rationale": (
                    "Incorrect. 'net stop' stops Windows services by service name, not "
                    "arbitrary processes. malware.exe is unlikely to be a registered service, "
                    "and net stop would not kill child processes."
                ),
            },
            {
                "id": "d",
                "text": "tasklist /kill /PID 4892",
                "correct": False,
                "rationale": (
                    "Incorrect. tasklist only lists processes—it has no /kill switch. "
                    "Process termination requires taskkill, not tasklist."
                ),
            },
        ],
        "explanation": (
            "taskkill switches: /PID specifies the process ID, /IM specifies the image "
            "(executable) name, /F forces termination without waiting for graceful shutdown, "
            "/T terminates the entire process tree including children. Use 'tasklist' to "
            "find PIDs before running taskkill. 'net stop' is for Windows services only."
        ),
    },
    # ── 1.3 Windows Administrative Tools ─────────────────────────────────
    {
        "id": "c2d1v3-011",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A technician wants to view all errors and warnings recorded in the past "
            "24 hours across the System, Application, and Security event logs on a "
            "remote Windows Server. Which tool provides this capability with the "
            "ability to connect to a remote computer?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Task Manager",
                "correct": False,
                "rationale": (
                    "Incorrect. Task Manager shows running processes and performance data "
                    "for the local machine only; it cannot connect to remote computers "
                    "or browse event logs."
                ),
            },
            {
                "id": "b",
                "text": "Event Viewer (eventvwr.msc)",
                "correct": True,
                "rationale": (
                    "Correct. Event Viewer can connect to remote computers via Action → "
                    "Connect to Another Computer, and its Custom Views and filter tools "
                    "allow filtering by event level (Error, Warning) and time range across "
                    "multiple log sources."
                ),
            },
            {
                "id": "c",
                "text": "Resource Monitor",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource Monitor shows real-time CPU, disk, network, and "
                    "memory usage for the local machine; it does not browse event logs "
                    "or connect to remote computers."
                ),
            },
            {
                "id": "d",
                "text": "Reliability Monitor",
                "correct": False,
                "rationale": (
                    "Incorrect. Reliability Monitor shows a historical stability index and "
                    "critical events for the local machine only; it does not support remote "
                    "connections or cross-log custom views."
                ),
            },
        ],
        "explanation": (
            "Event Viewer (eventvwr.msc) is the MMC snap-in for browsing Windows event logs. "
            "It supports remote computer connections and Custom Views that aggregate events "
            "across multiple logs with filters for level, time range, and event IDs. "
            "Resource Monitor and Task Manager are local-only real-time tools; Reliability "
            "Monitor provides a visual stability timeline but no remote capability."
        ),
    },
    {
        "id": "c2d1v3-012",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A server administrator needs to see which local user accounts have passwords "
            "set to never expire, and also reset one account's password—all without "
            "domain tools, on a standalone Windows Server. Which tool is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "net user (command line)",
                "correct": False,
                "rationale": (
                    "Incorrect. 'net user <username>' shows account details including "
                    "password expiry, and 'net user <username> <password>' resets passwords. "
                    "However, it cannot show all accounts with the 'never expire' property "
                    "in a visual, filterable list without scripting."
                ),
            },
            {
                "id": "b",
                "text": "Local Users and Groups snap-in (lusrmgr.msc)",
                "correct": True,
                "rationale": (
                    "Correct. lusrmgr.msc provides a GUI listing of all local users with "
                    "the ability to view and edit each account's properties, including the "
                    "'Password never expires' checkbox, and supports direct password resets "
                    "via right-click → Set Password."
                ),
            },
            {
                "id": "c",
                "text": "Active Directory Users and Computers (dsa.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. dsa.msc manages domain accounts in Active Directory. On "
                    "a standalone server (not a domain controller), dsa.msc is not available "
                    "or relevant for local accounts."
                ),
            },
            {
                "id": "d",
                "text": "Computer Management → Shared Folders",
                "correct": False,
                "rationale": (
                    "Incorrect. The Shared Folders section of Computer Management manages "
                    "file shares and sessions, not local user account properties."
                ),
            },
        ],
        "explanation": (
            "lusrmgr.msc (Local Users and Groups) is the MMC snap-in for managing local "
            "accounts on non-domain-controller Windows machines. It lists all local users "
            "and groups, shows account properties (including 'Password never expires'), "
            "and supports password resets. dsa.msc is for domain accounts; Shared Folders "
            "manages SMB shares."
        ),
    },
    {
        "id": "c2d1v3-013",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A Windows 10 workstation boots slowly. Task Manager's Startup tab shows "
            "a program with 'High' startup impact, but the technician cannot determine "
            "the publisher or file path from Task Manager alone. Which tool provides "
            "the full file path, publisher signature, and the registry key or folder "
            "where the startup entry is registered?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MSConfig (System Configuration) → Startup tab",
                "correct": False,
                "rationale": (
                    "Incorrect. In Windows 8+, MSConfig's Startup tab redirects to Task "
                    "Manager's Startup tab and provides the same limited information "
                    "(name, publisher, status, impact)—not the full registry key or path."
                ),
            },
            {
                "id": "b",
                "text": "Autoruns (Sysinternals)",
                "correct": True,
                "rationale": (
                    "Correct. Autoruns is a Sysinternals tool that shows every auto-start "
                    "entry across all Windows startup locations (registry Run keys, Startup "
                    "folders, scheduled tasks, services, drivers, browser extensions, etc.) "
                    "with full file paths, publisher signatures, and the exact registry key "
                    "or folder where each entry is registered."
                ),
            },
            {
                "id": "c",
                "text": "Performance Monitor → Data Collector Sets",
                "correct": False,
                "rationale": (
                    "Incorrect. Performance Monitor captures performance counter data over "
                    "time. It does not enumerate startup programs or show their registry "
                    "locations."
                ),
            },
            {
                "id": "d",
                "text": "Device Manager → View → Show hidden devices",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Manager shows hardware devices and their drivers, "
                    "including hidden/ghost devices. It does not show software startup entries "
                    "or their registry keys."
                ),
            },
        ],
        "explanation": (
            "Autoruns (Sysinternals/Microsoft) is the comprehensive startup manager, showing "
            "all auto-start extensibility points (ASEPs): registry Run/RunOnce keys, Startup "
            "folders, scheduled tasks, services, browser add-ons, Winlogon notifications, etc. "
            "It highlights unsigned entries in red and shows digital signatures—far more "
            "detail than Task Manager or MSConfig."
        ),
    },
    # ── 1.4 Control Panel ─────────────────────────────────────────────────
    {
        "id": "c2d1v3-014",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A user's keyboard types the wrong characters when certain keys are pressed "
            "(e.g., pressing '2' outputs '@', and pressing '@' outputs '\"'). The keyboard "
            "is physically working correctly. Which Control Panel setting is the MOST "
            "likely cause and fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → Ease of Access → Filter Keys is enabled.",
                "correct": False,
                "rationale": (
                    "Incorrect. Filter Keys adjusts how Windows responds to rapid or held "
                    "keystrokes (for users with tremors). It does not change character mapping "
                    "or swap key output."
                ),
            },
            {
                "id": "b",
                "text": "Control Panel → Clock and Region → Region → Change keyboard layout; the wrong input language is active.",
                "correct": True,
                "rationale": (
                    "Correct. The symptom (2 outputs @, @ outputs \") is characteristic of "
                    "a UK keyboard layout active on a US keyboard (or vice versa). The "
                    "keyboard layout (input language) remaps physical keys to different "
                    "characters. Changing to the correct layout resolves the mismatch."
                ),
            },
            {
                "id": "c",
                "text": "Control Panel → Ease of Access → Sticky Keys is enabled.",
                "correct": False,
                "rationale": (
                    "Incorrect. Sticky Keys allows modifier keys (Shift, Ctrl, Alt) to "
                    "remain active after release for one-handed typing. It does not remap "
                    "character output."
                ),
            },
            {
                "id": "d",
                "text": "Control Panel → System → Advanced → Environment Variables; the LANG variable is wrong.",
                "correct": False,
                "rationale": (
                    "Incorrect. The LANG environment variable affects locale settings for "
                    "command-line tools but does not control the Windows keyboard input "
                    "layout that maps physical keys to characters in the GUI."
                ),
            },
        ],
        "explanation": (
            "Wrong character output from physically correct keys is the classic symptom of "
            "a keyboard layout (input language) mismatch. The 2/@/@ quote swap is the "
            "standard US vs. UK layout difference. Fix via Control Panel → Region → "
            "Change keyboard or Settings → Time & Language → Language → Preferred languages "
            "→ keyboard options."
        ),
    },
    {
        "id": "c2d1v3-015",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A Windows workstation is connected to both a wired Ethernet adapter (metric 10) "
            "and a Wi-Fi adapter (metric 25). The user complains that internet traffic is "
            "unexpectedly using Wi-Fi instead of the faster wired connection. "
            "Which Control Panel location allows the administrator to manually control "
            "which adapter is preferred for internet traffic?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → Network and Sharing Center → Change adapter settings → right-click adapter → Properties → Internet Protocol Version 4 → Advanced → Interface Metric",
                "correct": True,
                "rationale": (
                    "Correct. The Interface Metric in the IPv4 advanced settings controls "
                    "the cost Windows assigns to routes learned through that adapter. A lower "
                    "metric is preferred; setting a lower metric on the wired adapter ensures "
                    "it is chosen over Wi-Fi for internet traffic."
                ),
            },
            {
                "id": "b",
                "text": "Control Panel → Network and Sharing Center → Set up a new connection → Prioritize adapters",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Set up a new connection' creates new network connections; "
                    "there is no 'Prioritize adapters' option in this wizard."
                ),
            },
            {
                "id": "c",
                "text": "Control Panel → Device Manager → Network Adapters → right-click → Set Priority",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Manager manages hardware drivers and does not expose "
                    "routing metrics or adapter priority for traffic selection."
                ),
            },
            {
                "id": "d",
                "text": "Control Panel → System → Advanced → Performance → Adapter Priority",
                "correct": False,
                "rationale": (
                    "Incorrect. Advanced System Properties → Performance controls visual "
                    "effects and virtual memory; there is no adapter priority setting here."
                ),
            },
        ],
        "explanation": (
            "Windows uses interface metrics to determine which network adapter's routes "
            "are preferred. A lower metric wins. The metric is configured per-adapter in "
            "IPv4/IPv6 Advanced Settings. Windows can also auto-configure metrics based on "
            "link speed, but manual override via the Interface Metric field gives explicit "
            "control. A wired adapter with metric 10 should be preferred over Wi-Fi at 25."
        ),
    },
    {
        "id": "c2d1v3-016",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A Windows 10 workstation is joined to a domain. A user reports that after "
            "a password change at the domain level, they can no longer access a mapped "
            "network drive to \\\\fileserver\\data that was previously working. "
            "Other domain resources work fine. Which Control Panel tool manages the "
            "stored credentials that may have cached the old password?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Control Panel → User Accounts → Manage your credentials (Credential Manager)",
                "correct": True,
                "rationale": (
                    "Correct. Credential Manager stores saved usernames and passwords for "
                    "network resources and websites. If the old domain password was cached "
                    "for \\\\fileserver, removing or updating that Windows Credential entry "
                    "will allow the system to prompt for (or use) the new credentials."
                ),
            },
            {
                "id": "b",
                "text": "Control Panel → Network and Sharing Center → Manage wireless networks",
                "correct": False,
                "rationale": (
                    "Incorrect. Manage wireless networks handles saved Wi-Fi profiles and "
                    "passwords, not Windows authentication credentials for file server access."
                ),
            },
            {
                "id": "c",
                "text": "Control Panel → System → Remote settings → Remote Desktop credentials",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote Settings manages Remote Desktop access; it does not "
                    "control cached credentials for network file shares."
                ),
            },
            {
                "id": "d",
                "text": "Control Panel → BitLocker Drive Encryption → Manage BitLocker keys",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker manages full-disk encryption keys; it has no "
                    "role in network credential caching or file share authentication."
                ),
            },
        ],
        "explanation": (
            "Credential Manager (Control Panel → User Accounts → Manage your credentials) "
            "stores Windows Credentials (NTLM/Kerberos for network resources), Certificate-Based "
            "Credentials, and Generic Credentials (web passwords). Stale cached credentials "
            "for a file server will cause authentication failures after a password change. "
            "Remove the entry under Windows Credentials to clear the cache."
        ),
    },
    # ── 1.5 Windows Settings ──────────────────────────────────────────────
    {
        "id": "c2d1v3-017",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "A Windows 11 user wants to configure Dynamic Lock so the workstation "
            "automatically locks when they walk away with their paired Bluetooth phone. "
            "Where in Windows Settings is Dynamic Lock configured?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → System → Power & Sleep → Dynamic Lock",
                "correct": False,
                "rationale": (
                    "Incorrect. Power & Sleep settings control display and sleep timeouts; "
                    "Dynamic Lock is not located under this category."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Accounts → Sign-in options → Dynamic Lock",
                "correct": True,
                "rationale": (
                    "Correct. Dynamic Lock is found in Settings → Accounts → Sign-in "
                    "options. After pairing a Bluetooth device to the PC, enabling "
                    "'Allow Windows to automatically lock your device when you're away' "
                    "activates Dynamic Lock."
                ),
            },
            {
                "id": "c",
                "text": "Settings → Bluetooth & devices → Dynamic Lock",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluetooth & devices manages device pairing but does not "
                    "contain the Dynamic Lock configuration. The Bluetooth device must be "
                    "paired first, but the Dynamic Lock toggle is under Sign-in options."
                ),
            },
            {
                "id": "d",
                "text": "Settings → Privacy & Security → Device Security → Dynamic Lock",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Security under Privacy & Security shows hardware "
                    "security features (Secure Boot, TPM); Dynamic Lock is not configured "
                    "there."
                ),
            },
        ],
        "explanation": (
            "Dynamic Lock uses a paired Bluetooth device's signal strength to detect when "
            "the user leaves. It is configured in Settings → Accounts → Sign-in options → "
            "Dynamic Lock. The Bluetooth device must be paired before enabling the feature. "
            "When the device goes out of range, Windows locks automatically after ~30 seconds."
        ),
    },
    {
        "id": "c2d1v3-018",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "A Windows 11 Pro workstation needs to use a proxy server at 192.168.1.100 "
            "port 8080 for all HTTP/HTTPS traffic. The user should not need to configure "
            "this in every application individually. Where in Windows Settings should the "
            "technician configure the system-wide proxy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Settings → Network & Internet → VPN → Add a VPN connection",
                "correct": False,
                "rationale": (
                    "Incorrect. VPN settings configure encrypted tunnel connections to "
                    "VPN endpoints. A proxy server is not a VPN and is configured separately."
                ),
            },
            {
                "id": "b",
                "text": "Settings → Network & Internet → Proxy → Manual proxy setup",
                "correct": True,
                "rationale": (
                    "Correct. Settings → Network & Internet → Proxy provides a Manual "
                    "proxy setup section where the address (192.168.1.100) and port (8080) "
                    "can be entered. Applications that honor the WinINET/WinHTTP system "
                    "proxy (Edge, IE, Chrome, many Windows apps) will route traffic through it."
                ),
            },
            {
                "id": "c",
                "text": "Settings → Privacy & Security → Windows Security → Firewall → Proxy settings",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Security/Firewall manages inbound/outbound traffic "
                    "rules; it does not have proxy configuration settings."
                ),
            },
            {
                "id": "d",
                "text": "Settings → Apps → Default apps → Proxy server",
                "correct": False,
                "rationale": (
                    "Incorrect. Default apps settings control which applications open "
                    "specific file types or protocols; there is no proxy server section here."
                ),
            },
        ],
        "explanation": (
            "Windows system-wide proxy settings are in Settings → Network & Internet → Proxy. "
            "Manual proxy setup allows specifying the proxy address, port, and exceptions. "
            "Applications using WinINET or WinHTTP (Edge, Chrome, many Windows utilities) "
            "inherit these settings. Firefox uses its own proxy settings and ignores the "
            "system proxy by default."
        ),
    },
    # ── 1.6 Windows Networking ────────────────────────────────────────────
    {
        "id": "c2d1v3-019",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A Windows 10 workstation in a workgroup environment needs to share a printer "
            "with other computers. After enabling printer sharing, remote users receive an "
            "error when connecting: 'Windows cannot connect to the printer. Access is denied.' "
            "The technician confirms the firewall is not blocking SMB. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Password Protected Sharing is enabled; remote users must authenticate with a local account.",
                "correct": True,
                "rationale": (
                    "Correct. In Windows workgroups, Password Protected Sharing requires "
                    "remote users to authenticate with a valid local account and password "
                    "on the host machine. Without matching credentials, access is denied. "
                    "Disabling it allows guest access, or the remote users need a local account."
                ),
            },
            {
                "id": "b",
                "text": "The printer driver is 64-bit only; 32-bit client machines cannot connect.",
                "correct": False,
                "rationale": (
                    "Incorrect. Driver architecture mismatches cause different errors "
                    "(driver not found, install fails) and typically do not produce an "
                    "'Access is denied' message. Access denied is an authentication/permission error."
                ),
            },
            {
                "id": "c",
                "text": "The workstation's IPv6 is disabled; printer sharing requires IPv6.",
                "correct": False,
                "rationale": (
                    "Incorrect. Printer sharing works over IPv4. IPv6 is not required for "
                    "SMB-based printer sharing on a LAN."
                ),
            },
            {
                "id": "d",
                "text": "The Print Spooler service is not running on the client machines.",
                "correct": False,
                "rationale": (
                    "Incorrect. A stopped Print Spooler on the client prevents local printing "
                    "and would produce a different error. 'Access is denied' specifically "
                    "indicates an authentication or permission failure on the host."
                ),
            },
        ],
        "explanation": (
            "In Windows workgroup environments, Password Protected Sharing (Network and "
            "Sharing Center → Advanced sharing settings) requires remote users to supply "
            "credentials matching a local account on the host PC. This is a security feature "
            "preventing anonymous access. Options: disable Password Protected Sharing (allows "
            "guest access), create matching local accounts, or use a domain environment."
        ),
    },
    {
        "id": "c2d1v3-020",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A domain-joined Windows workstation shows IP address 169.254.x.x after booting. "
            "The DHCP server is operational and serving other machines on the same subnet. "
            "After running 'ipconfig /release' followed by 'ipconfig /renew', the workstation "
            "still gets a 169.254.x.x address. What does this address indicate and "
            "what should the technician check NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The 169.254.x.x range is a valid APIPA address assigned by a secondary DHCP server for failover.",
                "correct": False,
                "rationale": (
                    "Incorrect. 169.254.0.0/16 is the Automatic Private IP Addressing (APIPA) "
                    "range, self-assigned by Windows when it cannot reach a DHCP server. "
                    "It is not assigned by a DHCP server—it means DHCP failed."
                ),
            },
            {
                "id": "b",
                "text": "APIPA indicates the workstation failed to contact the DHCP server; the technician should check the physical network connection and switch port for the workstation.",
                "correct": True,
                "rationale": (
                    "Correct. A 169.254.x.x address means DHCP discovery failed entirely. "
                    "Since other machines on the same subnet receive DHCP addresses, the issue "
                    "is likely local to this workstation: faulty cable, wrong VLAN/switch port, "
                    "bad NIC, or a blocked port. Checking physical connectivity is the "
                    "correct next step."
                ),
            },
            {
                "id": "c",
                "text": "169.254.x.x is a loopback address indicating the NIC has failed completely.",
                "correct": False,
                "rationale": (
                    "Incorrect. 127.0.0.0/8 is the loopback range. 169.254.0.0/16 is APIPA. "
                    "A completely failed NIC would show no IP address at all (media disconnected), "
                    "not an APIPA address."
                ),
            },
            {
                "id": "d",
                "text": "The workstation's DNS suffix search list is misconfigured, preventing DHCP responses from being accepted.",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS suffix search lists affect name resolution, not DHCP "
                    "lease acquisition. APIPA is a DHCP communication failure, unrelated "
                    "to DNS configuration."
                ),
            },
        ],
        "explanation": (
            "APIPA (Automatic Private IP Addressing) assigns a 169.254.0.0/16 address when "
            "Windows cannot contact a DHCP server after multiple broadcast attempts. Since the "
            "DHCP server works for other clients, the problem is local. Check: cable connection, "
            "switch port state/VLAN assignment, NIC driver/hardware, and whether the workstation "
            "is on the correct network segment. 'ipconfig /renew' failing confirms DHCP "
            "unreachability."
        ),
    },
    # ── 1.7 Application Installation ─────────────────────────────────────
    {
        "id": "c2d1v3-021",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application installation requirements",
        "stem": (
            "A user installs a new application on Windows 10 and is immediately prompted "
            "by UAC. The application requires writing to HKEY_LOCAL_MACHINE in the registry "
            "and C:\\Program Files. The user is a standard (non-admin) user. "
            "What will happen if the user clicks 'No' on the UAC prompt?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The application installs into the user's profile (C:\\Users\\%username%\\AppData) automatically as a per-user install.",
                "correct": False,
                "rationale": (
                    "Incorrect. Only applications specifically written to support per-user "
                    "installation (using HKCU and user-profile paths) will redirect this way. "
                    "An application requiring HKLM and C:\\Program Files will simply fail, "
                    "not automatically redirect."
                ),
            },
            {
                "id": "b",
                "text": "The installation will fail because writing to HKLM and C:\\Program Files requires administrator privileges that the UAC elevation would have granted.",
                "correct": True,
                "rationale": (
                    "Correct. HKEY_LOCAL_MACHINE and C:\\Program Files are protected locations "
                    "requiring administrator rights. Denying the UAC elevation means the "
                    "installer process runs as a standard user and will receive 'Access Denied' "
                    "errors when attempting to write to those locations."
                ),
            },
            {
                "id": "c",
                "text": "UAC will prompt a second time with an administrator credential dialog; clicking No on the first prompt only dismisses the consent screen.",
                "correct": False,
                "rationale": (
                    "Incorrect. On a standard user account, UAC typically shows a credential "
                    "prompt (enter admin credentials). If the user dismisses or cancels, "
                    "the elevation is denied and the operation fails—it does not re-prompt "
                    "automatically."
                ),
            },
            {
                "id": "d",
                "text": "Windows Installer automatically retries the operation using the SYSTEM account.",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Installer (msiexec) does not automatically retry "
                    "with SYSTEM credentials when a user declines UAC elevation. The "
                    "installation simply fails."
                ),
            },
        ],
        "explanation": (
            "HKEY_LOCAL_MACHINE and C:\\Program Files are protected by Windows access controls "
            "and require administrator privileges to write. When a standard user declines UAC "
            "elevation (or cannot provide admin credentials), the installer process lacks "
            "the required rights and fails with Access Denied. Well-designed applications "
            "support per-user installation using HKCU and AppData paths to avoid this."
        ),
    },
    {
        "id": "c2d1v3-022",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Application installation requirements",
        "stem": (
            "A technician needs to install a vendor-provided .msi package silently with "
            "no user interaction and no reboot prompt, logging the installation output "
            "to C:\\install.log. Which msiexec command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "msiexec /i vendor.msi /quiet /norestart /log C:\\install.log",
                "correct": False,
                "rationale": (
                    "Incorrect. /log is not a valid msiexec switch. The logging switch "
                    "is /L (with optional modifiers like *v for verbose). This command "
                    "would fail to create the log file."
                ),
            },
            {
                "id": "b",
                "text": "msiexec /i vendor.msi /qn /norestart /L*v C:\\install.log",
                "correct": True,
                "rationale": (
                    "Correct. /i installs the package, /qn sets the UI level to 'No UI' "
                    "(completely silent), /norestart suppresses any reboot, and /L*v enables "
                    "verbose logging to the specified file (* logs all info, v adds verbose)."
                ),
            },
            {
                "id": "c",
                "text": "msiexec /install vendor.msi --silent --no-restart --log-file C:\\install.log",
                "correct": False,
                "rationale": (
                    "Incorrect. msiexec uses Windows-style switches with forward slashes, "
                    "not Linux-style double-dash arguments. /install, --silent, and "
                    "--log-file are not valid msiexec syntax."
                ),
            },
            {
                "id": "d",
                "text": "msiexec /a vendor.msi /qb /norestart /L*v C:\\install.log",
                "correct": False,
                "rationale": (
                    "Incorrect. /a performs an administrative installation (creates a network "
                    "install point), not a standard silent end-user installation. /i is "
                    "the correct switch for installing to the local machine."
                ),
            },
        ],
        "explanation": (
            "msiexec key switches: /i (install), /x or /uninstall (remove), /qn (no UI, "
            "fully silent), /qb (basic UI—progress bar only), /norestart (suppress reboot), "
            "/L*v <file> (verbose log). /a creates an administrative install point for "
            "network deployment. /quiet is valid for some newer syntaxes but /qn is the "
            "canonical silent install flag."
        ),
    },
    # ── 1.8 File Systems ─────────────────────────────────────────────────
    {
        "id": "c2d1v3-023",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A technician formats a Windows NTFS volume and enables EFS (Encrypting File "
            "System) on a folder. The user encrypts several files. Later, the OS drive "
            "fails and is replaced with a clean Windows install. The user copies the "
            "encrypted files from backup to the new OS. They cannot open them. "
            "What is the MOST accurate explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "EFS uses the computer's hardware TPM key; since the motherboard is the same, the files should open.",
                "correct": False,
                "rationale": (
                    "Incorrect. EFS is not tied to the TPM. EFS encryption is protected "
                    "by the user's RSA certificate/private key stored in their profile. "
                    "A new OS install generates a new certificate unless the old one is "
                    "imported."
                ),
            },
            {
                "id": "b",
                "text": "EFS files are encrypted with the user's EFS certificate private key; after a fresh OS install, the old certificate is gone and the files cannot be decrypted without importing the backup certificate.",
                "correct": True,
                "rationale": (
                    "Correct. EFS uses asymmetric encryption with the user's personal "
                    "certificate. The private key resides in the user's profile. A new OS "
                    "install creates a new user profile with a new EFS certificate. Without "
                    "importing the original certificate (exported before the failure), the "
                    "files are permanently inaccessible."
                ),
            },
            {
                "id": "c",
                "text": "EFS encryption is tied to the NTFS volume serial number; copying to a different volume breaks the encryption binding.",
                "correct": False,
                "rationale": (
                    "Incorrect. EFS is not tied to volume serial numbers. The encryption "
                    "is tied to the user's certificate/private key, which travels with "
                    "the user profile or exported certificate—not the volume."
                ),
            },
            {
                "id": "d",
                "text": "The files must be decrypted on the NTFS volume before backup; EFS files cannot be moved to another machine.",
                "correct": False,
                "rationale": (
                    "Incorrect. EFS files can be moved between machines, but the recipient "
                    "must have the matching private key (via certificate import) to decrypt "
                    "them. The files are not bound to a specific physical disk."
                ),
            },
        ],
        "explanation": (
            "EFS (Encrypting File System) encrypts files using the user's RSA public key; "
            "decryption requires the matching private key stored in the user's certificate "
            "store. After a fresh OS install, a new EFS certificate is generated—the old "
            "private key is gone unless it was exported. Best practice: always export and "
            "back up the EFS certificate (certmgr.msc → Personal → Certificates → EFS "
            "certificate → Export with private key)."
        ),
    },
    {
        "id": "c2d1v3-024",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A Linux administrator runs 'df -h' on a server and sees the root filesystem "
            "is 98% full. Investigation shows /var/log is consuming most of the space. "
            "The administrator wants to find the ten largest files under /var/log "
            "to decide what to archive. Which command lists the ten largest files "
            "in /var/log sorted by size, largest first?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ls -lhS /var/log | head -10",
                "correct": True,
                "rationale": (
                    "Correct. ls -l lists files in long format, -h shows human-readable "
                    "sizes, -S sorts by file size (largest first). Piping to head -10 "
                    "returns only the ten largest files. This works for the immediate "
                    "directory (not recursive)."
                ),
            },
            {
                "id": "b",
                "text": "du -sh /var/log/* | sort -rh | head -10",
                "correct": False,
                "rationale": (
                    "Incorrect. This command (du -sh for each item piped to sort -rh) "
                    "shows directory/file sizes sorted largest-first, which is valid for "
                    "identifying large directories—but du shows disk usage including "
                    "subdirectory totals, not strictly individual files. ls -lhS is more "
                    "precise for files specifically."
                ),
            },
            {
                "id": "c",
                "text": "find /var/log -type f -size +100M",
                "correct": False,
                "rationale": (
                    "Incorrect. This finds files larger than 100 MB but does not sort "
                    "them by size or limit to ten results. The size threshold (+100M) is "
                    "also arbitrary and may miss files smaller than that."
                ),
            },
            {
                "id": "d",
                "text": "df -i /var/log | sort -rn | head -10",
                "correct": False,
                "rationale": (
                    "Incorrect. df -i shows inode usage per filesystem, not individual "
                    "file sizes. It cannot list the ten largest files in a directory."
                ),
            },
        ],
        "explanation": (
            "ls -lhS sorts files by size (largest first) in human-readable format within "
            "the specified directory. head -10 limits output to the top ten. For a recursive "
            "search across subdirectories, 'find /var/log -type f -printf \"%s %p\\n\" | "
            "sort -rn | head -10' is more appropriate. du -sh is better for directory-level "
            "size analysis, not individual file listing."
        ),
    },
    # ── 1.9 OS Installation & Upgrade ─────────────────────────────────────
    {
        "id": "c2d1v3-025",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician performs a clean install of Windows 11 on a laptop. After "
            "installation, Windows Update downloads and installs all available updates "
            "successfully, but the laptop's touchpad gestures (three-finger swipe, "
            "pinch-to-zoom) no longer work. The generic Microsoft driver is installed. "
            "What is the MOST likely fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Roll back Windows to Windows 10, which has native touchpad gesture support.",
                "correct": False,
                "rationale": (
                    "Incorrect. Rolling back the OS is unnecessary and disproportionate. "
                    "Windows 11 supports precision touchpad gestures; the issue is the "
                    "absence of the OEM driver, not the OS version."
                ),
            },
            {
                "id": "b",
                "text": "Download and install the OEM precision touchpad driver from the laptop manufacturer's support site.",
                "correct": True,
                "rationale": (
                    "Correct. Advanced touchpad gestures require the OEM precision touchpad "
                    "driver (e.g., Synaptics, ELAN, Alps). A clean install installs the "
                    "generic HID driver from Windows Update, which lacks gesture support. "
                    "The manufacturer's driver enables full gesture functionality."
                ),
            },
            {
                "id": "c",
                "text": "Enable the Human Interface Device Access service; it is disabled after clean installs.",
                "correct": False,
                "rationale": (
                    "Incorrect. The HID Access service is not disabled by default after "
                    "a clean install. Missing advanced gestures are a driver issue, not a "
                    "service state issue."
                ),
            },
            {
                "id": "d",
                "text": "Re-run Windows Update with optional driver updates; touchpad gestures require a separate optional update package.",
                "correct": False,
                "rationale": (
                    "Incorrect. While optional updates can include drivers, OEM-specific "
                    "precision touchpad drivers with full gesture support are typically "
                    "only available from the manufacturer's site, not Windows Update."
                ),
            },
        ],
        "explanation": (
            "After a clean OS install, Windows installs generic class drivers that provide "
            "basic device functionality but lack OEM-specific features. For touchpads, the "
            "generic HID pointer driver provides movement and clicking but not the advanced "
            "gestures (swipe, pinch, tap zones) provided by OEM precision touchpad drivers "
            "from manufacturers like Synaptics, ELAN, or Alps. Always install OEM drivers "
            "after a clean install."
        ),
    },
    {
        "id": "c2d1v3-026",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Partitioning (GPT vs MBR)",
        "stem": (
            "A technician uses diskpart to inspect a Windows Server disk. The output of "
            "'list partition' on Disk 0 shows: Partition 1 (System, 100 MB), "
            "Partition 2 (Reserved, 16 MB), Partition 3 (Primary, 920 GB), and "
            "Partition 4 (Recovery, 523 MB). What is the purpose of Partition 2 "
            "(the 16 MB Reserved partition)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is the EFI System Partition (ESP) that stores the UEFI boot files.",
                "correct": False,
                "rationale": (
                    "Incorrect. Partition 1 (System, 100 MB) is the EFI System Partition "
                    "on a UEFI/GPT disk. The 16 MB Reserved partition serves a different purpose."
                ),
            },
            {
                "id": "b",
                "text": "It is the Microsoft Reserved Partition (MSR), reserved by Windows for internal use and not visible to users.",
                "correct": True,
                "rationale": (
                    "Correct. The 16 MB Microsoft Reserved Partition (MSR) is created "
                    "automatically on GPT disks. Windows uses it internally for disk "
                    "management operations. It has no drive letter and is not directly "
                    "accessible to users or applications."
                ),
            },
            {
                "id": "c",
                "text": "It stores the Windows hibernation file (hiberfil.sys) for fast startup.",
                "correct": False,
                "rationale": (
                    "Incorrect. hiberfil.sys is stored on the Windows OS partition (C:), "
                    "not in a separate reserved partition."
                ),
            },
            {
                "id": "d",
                "text": "It is the swap/page file partition used when physical RAM is exhausted.",
                "correct": False,
                "rationale": (
                    "Incorrect. The Windows page file (pagefile.sys) resides on the OS "
                    "volume (or a designated data volume)—not in a dedicated reserved partition."
                ),
            },
        ],
        "explanation": (
            "On GPT disks, Windows creates a Microsoft Reserved Partition (MSR) of 16 MB "
            "(128 MB on older Windows versions). It is not user-accessible and has no drive "
            "letter. The MSR provides space for Windows disk management operations. "
            "The layout: ESP (EFI boot files, ~100 MB) → MSR (16 MB) → Primary OS partition "
            "→ Recovery partition. On MBR disks, there is no MSR."
        ),
    },
    {
        "id": "c2d1v3-027",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "An organization is deploying Windows 11 using Windows Autopilot with Intune. "
            "A new laptop is shipped directly to a remote employee. The employee powers it "
            "on and completes the OOBE enrollment. Which pre-requisite must have been "
            "completed by IT before the device was shipped for Autopilot to work?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The technician must have performed a clean Windows 11 install with a custom unattend.xml before shipping.",
                "correct": False,
                "rationale": (
                    "Incorrect. Autopilot is designed to work with OEM-pre-installed Windows; "
                    "a custom unattend.xml clean install is the traditional MDT/WDS method, "
                    "not Autopilot."
                ),
            },
            {
                "id": "b",
                "text": "The device's hardware hash must have been registered in the organization's Autopilot deployment profile in Intune/Microsoft 365.",
                "correct": True,
                "rationale": (
                    "Correct. Windows Autopilot identifies devices by their hardware hash "
                    "(a fingerprint of hardware IDs). IT must register the hash in the "
                    "Intune/Microsoft 365 Autopilot device list and assign a deployment "
                    "profile before the device can self-configure during OOBE."
                ),
            },
            {
                "id": "c",
                "text": "The device must have been domain-joined by a technician at the office before shipping.",
                "correct": False,
                "rationale": (
                    "Incorrect. Autopilot supports Azure AD join (cloud-only) and Hybrid "
                    "Azure AD join without requiring pre-shipment domain join. The cloud "
                    "enrollment happens during OOBE at the employee's location."
                ),
            },
            {
                "id": "d",
                "text": "The OEM must have pre-installed a custom image with line-of-business applications before shipping.",
                "correct": False,
                "rationale": (
                    "Incorrect. Autopilot works with the standard OEM Windows image. "
                    "Applications are deployed automatically via Intune after enrollment—"
                    "no pre-installed custom image is required."
                ),
            },
        ],
        "explanation": (
            "Windows Autopilot is a zero-touch deployment method for cloud-managed organizations. "
            "The device ships with the standard OEM Windows image. IT registers the device's "
            "hardware hash (collected by the OEM, reseller, or a Get-WindowsAutoPilotInfo "
            "script) in the Microsoft Endpoint Manager (Intune) Autopilot portal. During "
            "OOBE, Windows contacts Microsoft servers, identifies the device, and applies "
            "the assigned deployment profile automatically."
        ),
    },
    # ── 1.10 macOS Features & Tools ───────────────────────────────────────
    {
        "id": "c2d1v3-028",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A macOS Ventura user reports that their Mac is running slowly and suspects "
            "a process is consuming excessive CPU. They want to see real-time CPU usage "
            "per process, similar to Windows Task Manager. Which macOS tool should they use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disk Utility",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk Utility manages storage volumes, partitions, and disk "
                    "images on macOS. It does not show process CPU or memory usage."
                ),
            },
            {
                "id": "b",
                "text": "Activity Monitor",
                "correct": True,
                "rationale": (
                    "Correct. Activity Monitor (found in /Applications/Utilities/) is the "
                    "macOS equivalent of Windows Task Manager. It shows real-time CPU, "
                    "memory, energy, disk, and network usage per process, with the ability "
                    "to force-quit unresponsive processes."
                ),
            },
            {
                "id": "c",
                "text": "Console",
                "correct": False,
                "rationale": (
                    "Incorrect. Console displays system logs (crash reports, diagnostic "
                    "logs, unified log stream) but does not show real-time per-process "
                    "resource utilization."
                ),
            },
            {
                "id": "d",
                "text": "System Information (About This Mac → System Report)",
                "correct": False,
                "rationale": (
                    "Incorrect. System Information provides a static hardware and software "
                    "inventory report; it does not show real-time process activity or CPU usage."
                ),
            },
        ],
        "explanation": (
            "Activity Monitor (/Applications/Utilities/Activity Monitor.app) is the macOS "
            "process monitor. Its tabs show CPU (% per process, number of threads), Memory "
            "(RAM usage, swap), Energy (power impact), Disk (I/O per process), and Network "
            "(bytes sent/received). Processes can be sorted by any column and force-quit "
            "from within the tool. The equivalent of Windows Task Manager."
        ),
    },
    {
        "id": "c2d1v3-029",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A macOS administrator needs to view the IP address, subnet mask, default "
            "gateway, and DNS servers configured on a MacBook, using only the command line "
            "in Terminal. Which command displays detailed network configuration similar "
            "to 'ipconfig /all' on Windows?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ifconfig -a",
                "correct": False,
                "rationale": (
                    "Incorrect. ifconfig -a shows IP/MAC addresses and interface status "
                    "but does not display the default gateway or DNS server assignments."
                ),
            },
            {
                "id": "b",
                "text": "networksetup -getinfo \"Wi-Fi\" (for each service) combined with scutil --dns",
                "correct": True,
                "rationale": (
                    "Correct. 'networksetup -getinfo <service>' displays IP, subnet, "
                    "router (gateway), and other settings for a specific network service. "
                    "'scutil --dns' shows the DNS resolver configuration. Together they "
                    "provide the full picture equivalent to ipconfig /all."
                ),
            },
            {
                "id": "c",
                "text": "ipconfig getifaddr en0",
                "correct": False,
                "rationale": (
                    "Incorrect. On macOS, 'ipconfig getifaddr en0' retrieves only the IP "
                    "address of a single interface—it does not show subnet mask, gateway, "
                    "or DNS servers."
                ),
            },
            {
                "id": "d",
                "text": "arp -a",
                "correct": False,
                "rationale": (
                    "Incorrect. arp -a shows the ARP cache (IP-to-MAC mappings for "
                    "recently contacted hosts) but does not display the local machine's "
                    "IP configuration, gateway, or DNS settings."
                ),
            },
        ],
        "explanation": (
            "macOS lacks a direct single-command equivalent to 'ipconfig /all'. "
            "'networksetup -getinfo <service name>' shows IP, subnet, router, and DHCP info "
            "for a named network service (list services with 'networksetup -listallnetworkservices'). "
            "'scutil --dns' shows DNS resolver configuration. 'ifconfig' shows interface "
            "addresses. For a GUI equivalent, System Settings → Network provides all information."
        ),
    },
    {
        "id": "c2d1v3-030",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A macOS user needs to install an application that came as a .pkg file. "
            "After double-clicking the .pkg, macOS displays 'The package could not be "
            "opened because it is from an unidentified developer'. The user has verified "
            "the file's SHA-256 hash matches the vendor's published checksum. "
            "Where should the technician look to allow this specific package to install?"
        ),
        "options": [
            {
                "id": "a",
                "text": "System Settings → General → Software Update → Allow unsigned packages",
                "correct": False,
                "rationale": (
                    "Incorrect. Software Update manages OS and App Store updates; there is "
                    "no 'Allow unsigned packages' toggle there."
                ),
            },
            {
                "id": "b",
                "text": "System Settings → Privacy & Security → scroll to the security section where a prompt appears to allow the blocked package",
                "correct": True,
                "rationale": (
                    "Correct. After Gatekeeper blocks a .pkg or .app, macOS records the "
                    "block and shows a temporary 'Open Anyway' button at the bottom of "
                    "System Settings → Privacy & Security within about an hour of the block. "
                    "Clicking it allows that specific package to proceed."
                ),
            },
            {
                "id": "c",
                "text": "Terminal → sudo spctl --master-disable (permanently disables Gatekeeper)",
                "correct": False,
                "rationale": (
                    "Incorrect. 'sudo spctl --master-disable' disables Gatekeeper entirely, "
                    "removing protection for all future downloads. This is more dangerous "
                    "than granting an exception for a single vetted package."
                ),
            },
            {
                "id": "d",
                "text": "Keychain Access → add the developer's certificate to the trusted list",
                "correct": False,
                "rationale": (
                    "Incorrect. Keychain Access manages certificates and credentials, but "
                    "adding a certificate there does not override Gatekeeper's block for "
                    "an unidentified developer—the 'Open Anyway' flow in Privacy & Security "
                    "is the correct per-app override mechanism."
                ),
            },
        ],
        "explanation": (
            "Gatekeeper blocks .pkg and .app files from unidentified developers. The targeted "
            "bypass: open System Settings → Privacy & Security; within ~60 minutes of the "
            "block, an 'Open Anyway' button appears next to the blocked item. This grants "
            "a one-time exception for that specific file. Disabling Gatekeeper system-wide "
            "('spctl --master-disable') is the nuclear option and should be avoided."
        ),
    },
    # ── 1.11 Linux Commands ───────────────────────────────────────────────
    {
        "id": "c2d1v3-031",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux technician needs to display the last 50 lines of /var/log/syslog "
            "and then continue watching the file in real time as new entries are appended, "
            "without restarting the command. Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "cat /var/log/syslog | tail -50",
                "correct": False,
                "rationale": (
                    "Incorrect. This displays the last 50 lines once and exits. It does "
                    "not continue watching the file for new entries."
                ),
            },
            {
                "id": "b",
                "text": "tail -n 50 -f /var/log/syslog",
                "correct": True,
                "rationale": (
                    "Correct. tail -n 50 shows the last 50 lines; -f (follow) keeps the "
                    "file open and prints new lines as they are appended in real time. "
                    "Press Ctrl+C to stop."
                ),
            },
            {
                "id": "c",
                "text": "less +F /var/log/syslog",
                "correct": False,
                "rationale": (
                    "Incorrect. 'less +F' does follow a file like tail -f, but it starts "
                    "from the beginning of the file, not the last 50 lines. Also, it is "
                    "less commonly used for this purpose than tail -f."
                ),
            },
            {
                "id": "d",
                "text": "watch tail /var/log/syslog",
                "correct": False,
                "rationale": (
                    "Incorrect. 'watch tail' re-runs tail periodically (default every 2 "
                    "seconds), refreshing the screen—but it shows a snapshot and does not "
                    "continuously stream new lines the way tail -f does. It also only shows "
                    "the default last 10 lines, not 50."
                ),
            },
        ],
        "explanation": (
            "tail -f (follow) is the standard way to monitor a log file in real time on "
            "Linux. The -n 50 option sets the initial number of lines displayed. "
            "Combined: 'tail -n 50 -f /var/log/syslog' starts with the last 50 lines and "
            "continuously appends new lines. 'less +F' is an alternative but starts from "
            "the top of the file. 'watch' polls at intervals rather than streaming."
        ),
    },
    {
        "id": "c2d1v3-032",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux file permissions",
        "stem": (
            "A Linux directory /opt/shared is used by multiple users in the group 'team'. "
            "The administrator wants any new files created inside this directory to "
            "automatically inherit the group ownership 'team' regardless of which user "
            "creates them. Which permission should be set on /opt/shared?"
        ),
        "options": [
            {
                "id": "a",
                "text": "chmod +t /opt/shared (sticky bit)",
                "correct": False,
                "rationale": (
                    "Incorrect. The sticky bit (+t) on a directory prevents users from "
                    "deleting files owned by other users (used on /tmp). It does not affect "
                    "group inheritance for newly created files."
                ),
            },
            {
                "id": "b",
                "text": "chmod g+s /opt/shared (setgid bit)",
                "correct": True,
                "rationale": (
                    "Correct. The setgid bit on a directory causes new files and "
                    "subdirectories created within it to inherit the directory's group "
                    "ownership ('team') rather than the creating user's primary group. "
                    "This is the standard mechanism for shared project directories."
                ),
            },
            {
                "id": "c",
                "text": "chmod u+s /opt/shared (setuid bit)",
                "correct": False,
                "rationale": (
                    "Incorrect. The setuid bit on a directory is ignored by Linux (it has "
                    "effect only on executable files, causing them to run as the file owner). "
                    "It does not control group inheritance in directories."
                ),
            },
            {
                "id": "d",
                "text": "chown :team /opt/shared (change group ownership of the directory only)",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the directory's group to 'team' sets the group on "
                    "the directory itself but does not cause new files created inside to "
                    "inherit that group. The setgid bit is required for that behavior."
                ),
            },
        ],
        "explanation": (
            "The setgid bit (chmod g+s) on a Linux directory enables group inheritance: "
            "newly created files and subdirectories inside the directory inherit the "
            "directory's group (here: 'team') rather than the creating user's primary group. "
            "This is the standard pattern for shared team directories. The sticky bit "
            "protects files from deletion by non-owners. setuid on directories is ignored "
            "in Linux (but meaningful in some BSDs)."
        ),
    },
    {
        "id": "c2d1v3-033",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux system administrator needs to display all currently listening TCP and "
            "UDP ports along with the process name and PID that owns each socket, without "
            "installing additional tools. Which command works on a modern Linux system "
            "that may not have netstat installed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "netstat -tulnp",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat -tulnp is the classic command for this purpose, "
                    "but the question specifies systems where netstat may NOT be installed "
                    "(it is part of the deprecated net-tools package not included by default "
                    "in many modern distributions like CentOS 8+, RHEL 8+, Ubuntu 20.04+)."
                ),
            },
            {
                "id": "b",
                "text": "ss -tulnp",
                "correct": True,
                "rationale": (
                    "Correct. ss (socket statistics) is the modern replacement for netstat "
                    "and is installed by default on all modern Linux distributions. "
                    "-t (TCP), -u (UDP), -l (listening), -n (numeric ports), -p (show "
                    "process/PID) produces the same view as netstat -tulnp."
                ),
            },
            {
                "id": "c",
                "text": "lsof -i",
                "correct": False,
                "rationale": (
                    "Incorrect. lsof -i lists open internet connections and is powerful, "
                    "but lsof is not always installed by default and the output format "
                    "differs significantly. ss is the preferred modern replacement for netstat."
                ),
            },
            {
                "id": "d",
                "text": "cat /proc/net/tcp",
                "correct": False,
                "rationale": (
                    "Incorrect. /proc/net/tcp contains raw socket data in hexadecimal "
                    "format (IP addresses and ports are hex-encoded). While it technically "
                    "contains the information, it requires manual decoding and is not "
                    "practical for routine use."
                ),
            },
        ],
        "explanation": (
            "ss (iproute2 package) is the modern replacement for netstat (net-tools). "
            "On RHEL/CentOS 8+, Ubuntu 20.04+, and other modern distros, net-tools is "
            "not installed by default. ss is always available. Key flags match netstat: "
            "-t (TCP), -u (UDP), -l (listening sockets only), -n (no name resolution), "
            "-p (process info). 'ss -tulnp' is the direct modern equivalent of 'netstat -tulnp'."
        ),
    },
    {
        "id": "c2d1v3-034",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator needs to add a new user named 'webadmin' with a home "
            "directory of /home/webadmin, a default shell of /bin/bash, and add the user "
            "to the existing group 'www-data'. Which single command creates the user with "
            "all these parameters?"
        ),
        "options": [
            {
                "id": "a",
                "text": "adduser webadmin --home /home/webadmin --shell /bin/bash --ingroup www-data",
                "correct": False,
                "rationale": (
                    "Incorrect. adduser (the interactive/friendlier Debian wrapper) uses "
                    "different flag syntax. The correct flags for adduser are --home, "
                    "--shell, and --ingroup, but 'useradd' is the more universal and "
                    "scriptable command specified in most exam contexts."
                ),
            },
            {
                "id": "b",
                "text": "useradd -m -d /home/webadmin -s /bin/bash -G www-data webadmin",
                "correct": True,
                "rationale": (
                    "Correct. useradd -m creates the home directory, -d specifies its path, "
                    "-s sets the login shell, and -G adds the user to a supplementary group "
                    "(www-data). The username is the last argument."
                ),
            },
            {
                "id": "c",
                "text": "useradd webadmin -home /home/webadmin -shell /bin/bash -group www-data",
                "correct": False,
                "rationale": (
                    "Incorrect. useradd uses single-dash short options (-d, -s, -G) or "
                    "double-dash long options (--home-dir, --shell, --groups). The flags "
                    "-home, -shell, and -group shown here are invalid."
                ),
            },
            {
                "id": "d",
                "text": "groupadd www-data && useradd webadmin && usermod -aG www-data webadmin",
                "correct": False,
                "rationale": (
                    "Incorrect. This sequence has errors: groupadd www-data would fail if "
                    "www-data already exists, useradd webadmin without -m won't create the "
                    "home directory, and multiple commands are required rather than one. "
                    "The single useradd command with proper flags is more efficient and correct."
                ),
            },
        ],
        "explanation": (
            "useradd key options: -m (create home directory), -d <path> (specify home "
            "directory path), -s <shell> (login shell), -G <group> (supplementary group), "
            "-g <group> (primary group). Without -m, no home directory is created. "
            "After creation, set the password with 'passwd webadmin'. 'adduser' is a "
            "Debian/Ubuntu interactive wrapper around useradd with slightly different syntax."
        ),
    },
    # ── Multiple Response Questions (14 more: total 6 from original plan + 8 extra) ─
    {
        "id": "c2d1v3-035",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician is troubleshooting a Windows 10 workstation that cannot reach "
            "network resources. Which TWO commands would help determine whether the "
            "problem is a misconfigured default gateway versus a DNS resolution failure? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ping 8.8.8.8",
                "correct": True,
                "rationale": (
                    "Correct. Pinging a public IP address (8.8.8.8) bypasses DNS entirely. "
                    "If this succeeds but a hostname ping fails, DNS is the problem. "
                    "If it fails, the issue is routing or the gateway."
                ),
            },
            {
                "id": "b",
                "text": "nslookup google.com",
                "correct": True,
                "rationale": (
                    "Correct. nslookup queries the DNS server to resolve a hostname. "
                    "If ping to 8.8.8.8 succeeds but nslookup fails or returns wrong "
                    "results, DNS misconfiguration is confirmed as the problem."
                ),
            },
            {
                "id": "c",
                "text": "chkdsk C: /f",
                "correct": False,
                "rationale": (
                    "Incorrect. chkdsk checks and repairs file system errors. It has no "
                    "relevance to network connectivity, gateway configuration, or DNS."
                ),
            },
            {
                "id": "d",
                "text": "sfc /scannow",
                "correct": False,
                "rationale": (
                    "Incorrect. sfc (System File Checker) scans and repairs protected "
                    "Windows system files. It does not diagnose network configuration issues."
                ),
            },
        ],
        "explanation": (
            "The IP-vs-DNS diagnostic technique: ping by IP (8.8.8.8) tests routing and "
            "gateway connectivity without DNS. nslookup tests DNS resolution. If IP ping "
            "works but hostnames fail, DNS is the issue. If IP ping fails, the problem is "
            "routing, gateway, or firewall. These two commands together quickly isolate the "
            "network problem layer."
        ),
    },
    {
        "id": "c2d1v3-036",
        "domain": 1,
        "objective": "1.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows editions",
        "stem": (
            "An IT administrator is reviewing Windows 11 editions for deployment. "
            "Which TWO features are available in Windows 11 Pro but NOT in Windows 11 Home? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "BitLocker Drive Encryption (full management)",
                "correct": True,
                "rationale": (
                    "Correct. Full BitLocker management (including BitLocker To Go for "
                    "removable drives) is available in Windows 11 Pro. Home includes only "
                    "Device Encryption (a simplified subset) on qualifying hardware."
                ),
            },
            {
                "id": "b",
                "text": "Windows Hello facial recognition",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Hello (facial recognition, fingerprint, PIN) is "
                    "available in both Windows 11 Home and Pro—it is not a Pro-exclusive feature."
                ),
            },
            {
                "id": "c",
                "text": "Active Directory domain join",
                "correct": True,
                "rationale": (
                    "Correct. Joining an Active Directory domain requires Windows 11 Pro "
                    "or higher. Windows 11 Home can only join Microsoft 365 cloud/Azure AD "
                    "environments, not traditional on-premises AD domains."
                ),
            },
            {
                "id": "d",
                "text": "Microsoft Store access",
                "correct": False,
                "rationale": (
                    "Incorrect. The Microsoft Store is available in all Windows 11 editions "
                    "including Home. It is not a Pro-exclusive feature."
                ),
            },
        ],
        "explanation": (
            "Windows 11 Pro adds over Home: Active Directory domain join, full BitLocker "
            "management, Local Group Policy Editor (gpedit.msc), Windows Sandbox, Remote "
            "Desktop host (RDP server), Hyper-V, Assigned Access (kiosk mode), and "
            "Azure AD join with mobile device management. Home retains Windows Hello, "
            "the Microsoft Store, and Device Encryption."
        ),
    },
    {
        "id": "c2d1v3-037",
        "domain": 1,
        "objective": "1.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "File systems (NTFS/FAT32/exFAT/APFS/ext4)",
        "stem": (
            "A technician is selecting a file system for different use cases. "
            "Which TWO statements about NTFS are correct? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "NTFS supports per-file and per-folder access control lists (ACLs) for granular permissions.",
                "correct": True,
                "rationale": (
                    "Correct. NTFS uses Access Control Lists (ACLs) tied to each file and "
                    "folder, allowing fine-grained permissions (Full Control, Modify, Read & "
                    "Execute, Read, Write) per user or group."
                ),
            },
            {
                "id": "b",
                "text": "NTFS has a maximum individual file size of 4 GB minus 1 byte.",
                "correct": False,
                "rationale": (
                    "Incorrect. The 4 GB minus 1 byte limit applies to FAT32, not NTFS. "
                    "NTFS theoretical maximum file size is 16 EB (exabytes), limited in "
                    "practice by the volume size."
                ),
            },
            {
                "id": "c",
                "text": "NTFS supports disk quotas, allowing administrators to limit disk space usage per user.",
                "correct": True,
                "rationale": (
                    "Correct. NTFS includes built-in disk quota management. Administrators "
                    "can set disk usage limits per user on NTFS volumes via Disk Management "
                    "or the fsutil quota command."
                ),
            },
            {
                "id": "d",
                "text": "NTFS volumes are natively writable on macOS without additional software.",
                "correct": False,
                "rationale": (
                    "Incorrect. macOS can read NTFS volumes natively but cannot write to "
                    "them without third-party drivers (e.g., Paragon NTFS, Tuxera NTFS). "
                    "Native macOS NTFS write support is disabled by default."
                ),
            },
        ],
        "explanation": (
            "NTFS key features: ACLs (per-file/folder permissions), journaling ($LogFile), "
            "disk quotas, EFS encryption, file/folder compression, sparse files, hard and "
            "symbolic links, volume shadow copies, and large file/volume support (16 EB "
            "theoretical max). FAT32 has the 4 GB file limit. NTFS write on macOS requires "
            "third-party tools."
        ),
    },
    {
        "id": "c2d1v3-038",
        "domain": 1,
        "objective": "1.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "OS installation & upgrade methods",
        "stem": (
            "A technician is performing an in-place upgrade from Windows 10 to Windows 11. "
            "The PC Check Tool (PC Health Check) reports the machine does NOT meet Windows 11 "
            "requirements. Which TWO hardware requirements are unique to Windows 11 "
            "and were NOT required by Windows 10? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "TPM 2.0 (Trusted Platform Module version 2.0)",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 requires TPM 2.0, whereas Windows 10 only "
                    "recommended TPM 1.2 and did not enforce it as a hard requirement "
                    "for installation."
                ),
            },
            {
                "id": "b",
                "text": "At least 4 GB of RAM",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows 10 (64-bit) also requires at least 2 GB RAM "
                    "(4 GB recommended). Windows 11 requires 4 GB RAM, which is an "
                    "increase but both versions have a RAM floor. This is not a completely "
                    "new requirement unique to Windows 11."
                ),
            },
            {
                "id": "c",
                "text": "UEFI firmware with Secure Boot capability",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 requires UEFI firmware with Secure Boot enabled "
                    "and capable. Windows 10 could install on legacy BIOS/MBR systems. "
                    "This is a new hard requirement for Windows 11."
                ),
            },
            {
                "id": "d",
                "text": "A dedicated GPU with DirectX 9 support",
                "correct": False,
                "rationale": (
                    "Incorrect. Both Windows 10 and Windows 11 require DirectX 9 compatible "
                    "graphics. Windows 11 requires DirectX 12 compatible graphics for the "
                    "new desktop, but DirectX 9 was also required by Windows 10—it is not "
                    "a new unique requirement."
                ),
            },
        ],
        "explanation": (
            "Windows 11 new/upgraded hardware requirements vs. Windows 10: TPM 2.0 (hard "
            "requirement, not just recommended), UEFI Secure Boot (legacy BIOS blocked), "
            "64-bit CPU with at least 1 GHz with 2+ cores from the approved CPU list, "
            "4 GB RAM (up from 2 GB for 64-bit Win 10), 64 GB storage (up from 32 GB), "
            "and DirectX 12 compatible graphics with WDDM 2.0 driver."
        ),
    },
    {
        "id": "c2d1v3-039",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Linux commands",
        "stem": (
            "A Linux administrator needs to investigate disk space usage on a server. "
            "Which TWO commands provide disk space information? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "df -h",
                "correct": True,
                "rationale": (
                    "Correct. df (disk free) reports the disk space usage of file systems, "
                    "showing total, used, available space, and mount points in human-readable "
                    "format with -h."
                ),
            },
            {
                "id": "b",
                "text": "du -sh /home/*",
                "correct": True,
                "rationale": (
                    "Correct. du (disk usage) reports the disk space consumed by files and "
                    "directories. '-s' summarizes (one total per argument), '-h' is "
                    "human-readable, and '/home/*' reports each user's home directory size."
                ),
            },
            {
                "id": "c",
                "text": "free -h",
                "correct": False,
                "rationale": (
                    "Incorrect. free -h reports RAM and swap memory usage—it shows physical "
                    "memory availability, not disk/filesystem space."
                ),
            },
            {
                "id": "d",
                "text": "uptime",
                "correct": False,
                "rationale": (
                    "Incorrect. uptime displays how long the system has been running and "
                    "the load averages. It provides no disk space information."
                ),
            },
        ],
        "explanation": (
            "df (disk free) reports filesystem-level disk usage (total, used, available per "
            "mounted filesystem). du (disk usage) reports the space consumed by specific "
            "files and directories. Together they are the primary Linux tools for disk space "
            "investigation. free reports memory; uptime reports system load. Both df and du "
            "are part of the GNU coreutils package."
        ),
    },
    {
        "id": "c2d1v3-040",
        "domain": 1,
        "objective": "1.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows networking (workgroup/domain)",
        "stem": (
            "A technician needs to map a network drive persistently so it reconnects at "
            "every login. Which TWO methods correctly create a persistent mapped drive "
            "to \\\\server\\share as drive Z: for the current user? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "net use Z: \\\\server\\share /persistent:yes",
                "correct": True,
                "rationale": (
                    "Correct. The /persistent:yes flag saves the drive mapping so it "
                    "reconnects at every login for the current user. Without this flag, "
                    "the mapping is session-only."
                ),
            },
            {
                "id": "b",
                "text": "File Explorer → This PC → Map Network Drive → specify \\\\server\\share → check 'Reconnect at sign-in'",
                "correct": True,
                "rationale": (
                    "Correct. The Map Network Drive wizard in File Explorer provides a "
                    "'Reconnect at sign-in' checkbox that saves the mapping persistently "
                    "in the user's profile, equivalent to /persistent:yes."
                ),
            },
            {
                "id": "c",
                "text": "net use Z: \\\\server\\share (without /persistent flag)",
                "correct": False,
                "rationale": (
                    "Incorrect. Without /persistent:yes, net use creates a session-only "
                    "mapping that is lost after logoff. The default persistence depends "
                    "on the current /persistent setting, which defaults to no."
                ),
            },
            {
                "id": "d",
                "text": "Adding a shortcut to \\\\server\\share on the Desktop",
                "correct": False,
                "rationale": (
                    "Incorrect. A desktop shortcut to a UNC path creates a folder shortcut, "
                    "not a mapped drive letter. It does not appear as Z: in File Explorer "
                    "or command-line tools."
                ),
            },
        ],
        "explanation": (
            "Persistent mapped drives survive logoff and are re-established at login. "
            "net use with /persistent:yes and the File Explorer Map Network Drive wizard "
            "with 'Reconnect at sign-in' both achieve this. Persistent mappings are stored "
            "in the user's registry (HKCU\\Network). Group Policy Drive Maps can also "
            "create persistent mappings in domain environments."
        ),
    },
    {
        "id": "c2d1v3-041",
        "domain": 1,
        "objective": "1.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Control Panel utilities",
        "stem": (
            "A technician is configuring a Windows 10 workstation's power settings for "
            "maximum performance in a desktop environment (always plugged in, no battery). "
            "Which TWO actions should be taken from Control Panel Power Options? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Select the 'High performance' power plan.",
                "correct": True,
                "rationale": (
                    "Correct. The High performance plan disables CPU throttling, keeps "
                    "the processor at maximum speed, and sets display/sleep timeouts to "
                    "longer values—optimizing for speed rather than power savings."
                ),
            },
            {
                "id": "b",
                "text": "Set 'Turn off the display' and 'Put the computer to sleep' to 'Never' under the plugged-in column.",
                "correct": True,
                "rationale": (
                    "Correct. For a desktop that must remain available at all times "
                    "(e.g., a server or kiosk), disabling the display timeout and sleep "
                    "prevents interruptions. This is configured in 'Change plan settings' "
                    "for the selected power plan."
                ),
            },
            {
                "id": "c",
                "text": "Enable 'Balanced' power plan and set the processor minimum state to 100%.",
                "correct": False,
                "rationale": (
                    "Incorrect. The Balanced plan dynamically scales processor speed. "
                    "Setting minimum state to 100% within Balanced partially mimics High "
                    "performance but is an indirect approach; selecting High performance "
                    "directly is cleaner and also sets other optimized parameters."
                ),
            },
            {
                "id": "d",
                "text": "Enable Hibernate to allow the system to quickly resume from a powered-off state.",
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling hibernate allows the system to save its state and "
                    "power off, which is counterproductive for maximum performance where "
                    "the machine should remain fully on and available."
                ),
            },
        ],
        "explanation": (
            "For maximum performance on a plugged-in desktop: select 'High performance' "
            "plan (prevents CPU frequency scaling down) and set display/sleep timeouts to "
            "'Never'. The High performance plan keeps processor speed at maximum and "
            "disables aggressive power-saving features. Balanced dynamically throttles the "
            "CPU to save power. Power Saver further reduces performance for battery conservation."
        ),
    },
    {
        "id": "c2d1v3-042",
        "domain": 1,
        "objective": "1.10",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "macOS features & tools",
        "stem": (
            "A technician is comparing macOS backup and recovery options. "
            "Which TWO statements about macOS recovery are correct? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pressing Command+R during startup boots a Mac into macOS Recovery, which includes Disk Utility and the ability to reinstall macOS.",
                "correct": True,
                "rationale": (
                    "Correct. Command+R (Intel Macs) or holding the power button (Apple "
                    "Silicon Macs) boots into macOS Recovery. Recovery includes Disk "
                    "Utility (for disk repair/erase), Reinstall macOS, Terminal, and "
                    "Restore from Time Machine Backup."
                ),
            },
            {
                "id": "b",
                "text": "Time Machine can perform full system restores in addition to individual file recovery.",
                "correct": True,
                "rationale": (
                    "Correct. Time Machine supports both granular file recovery (browsing "
                    "backups to restore individual files) and full system restoration "
                    "(from macOS Recovery → Restore from Time Machine Backup)."
                ),
            },
            {
                "id": "c",
                "text": "macOS Recovery requires an active internet connection on all Mac models.",
                "correct": False,
                "rationale": (
                    "Incorrect. macOS Recovery has a local partition with recovery tools. "
                    "Internet Recovery (Option+Command+R or Shift+Option+Command+R) requires "
                    "internet connectivity to download macOS, but the standard local Recovery "
                    "partition does not."
                ),
            },
            {
                "id": "d",
                "text": "FileVault encryption and Time Machine backups are incompatible; FileVault must be disabled before backing up.",
                "correct": False,
                "rationale": (
                    "Incorrect. FileVault and Time Machine are fully compatible. Time Machine "
                    "backs up the encrypted volume contents; the backup itself can also be "
                    "encrypted. FileVault does not need to be disabled for backups."
                ),
            },
        ],
        "explanation": (
            "macOS Recovery (accessed via Command+R on Intel, or holding power on Apple "
            "Silicon) provides: Disk Utility, Reinstall macOS, Restore from Time Machine, "
            "Terminal, and Startup Security Utility. Time Machine backs up the full system "
            "and supports both file-level and system-level restores. Internet Recovery "
            "(downloads macOS from Apple servers) is a separate mode requiring internet access."
        ),
    },
    {
        "id": "c2d1v3-043",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A Windows system is experiencing intermittent application crashes. "
            "Which TWO tools should a technician use to gather crash details and "
            "identify the failing component? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Event Viewer → Windows Logs → Application log",
                "correct": True,
                "rationale": (
                    "Correct. Application crashes generate Error events in the Application "
                    "log in Event Viewer, including the faulting application name, faulting "
                    "module, exception code, and offset—critical for identifying the root cause."
                ),
            },
            {
                "id": "b",
                "text": "Reliability Monitor (View reliability history)",
                "correct": True,
                "rationale": (
                    "Correct. Reliability Monitor (search 'reliability' in Start or "
                    "Control Panel → Security and Maintenance → Reliability Monitor) shows "
                    "a timeline of application failures, Windows failures, and miscellaneous "
                    "failures, with drill-down details for each event."
                ),
            },
            {
                "id": "c",
                "text": "Disk Management (diskmgmt.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk Management handles storage volumes and partitions. "
                    "It does not contain application crash information or diagnostic logs."
                ),
            },
            {
                "id": "d",
                "text": "Services (services.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. services.msc manages service startup types and states. "
                    "While a failing service can cause application issues, services.msc "
                    "itself does not show crash details or application error logs."
                ),
            },
        ],
        "explanation": (
            "For application crash diagnosis: Event Viewer → Application log shows detailed "
            "crash records with exception codes (e.g., 0xc0000005 = Access Violation) and "
            "the faulting module (often a third-party DLL). Reliability Monitor provides a "
            "visual timeline of all failures, making it easy to correlate crashes with "
            "changes (updates, installs). Together they provide the complete crash picture."
        ),
    },
    {
        "id": "c2d1v3-044",
        "domain": 1,
        "objective": "1.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Application installation requirements",
        "stem": (
            "A technician is assessing whether a legacy 32-bit application can run on a "
            "modern 64-bit Windows 11 workstation. Which TWO statements about running "
            "32-bit applications on 64-bit Windows are correct? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "WOW64 (Windows-on-Windows 64-bit) enables 32-bit applications to run on 64-bit Windows.",
                "correct": True,
                "rationale": (
                    "Correct. WOW64 is the compatibility subsystem that translates 32-bit "
                    "Windows API calls to their 64-bit equivalents, allowing 32-bit "
                    "applications to execute on 64-bit Windows without modification."
                ),
            },
            {
                "id": "b",
                "text": "32-bit applications on 64-bit Windows use the C:\\Windows\\SysWOW64 directory for 32-bit system DLLs.",
                "correct": True,
                "rationale": (
                    "Correct. On 64-bit Windows, C:\\Windows\\System32 contains 64-bit "
                    "system files, while C:\\Windows\\SysWOW64 contains the 32-bit versions. "
                    "The naming is counterintuitive—WOW64 hosts the 32-bit DLLs."
                ),
            },
            {
                "id": "c",
                "text": "A 32-bit application can load 64-bit DLLs for improved performance.",
                "correct": False,
                "rationale": (
                    "Incorrect. Processes cannot mix 32-bit and 64-bit code in the same "
                    "process space. A 32-bit process can only load 32-bit DLLs; it cannot "
                    "load 64-bit DLLs."
                ),
            },
            {
                "id": "d",
                "text": "16-bit DOS applications run natively through WOW64 on 64-bit Windows.",
                "correct": False,
                "rationale": (
                    "Incorrect. 64-bit Windows does NOT support 16-bit applications. "
                    "WOW64 handles 32-bit compatibility only. 16-bit apps require a "
                    "virtual machine (e.g., DOSBox) on 64-bit Windows."
                ),
            },
        ],
        "explanation": (
            "WOW64 is the 32-bit compatibility layer in 64-bit Windows. It intercepts "
            "32-bit API calls and redirects them appropriately. SysWOW64 (counterintuitively) "
            "holds 32-bit system DLLs; System32 holds 64-bit DLLs. 32-bit app registry "
            "calls are also redirected to HKLM\\SOFTWARE\\WOW6432Node. 16-bit applications "
            "are NOT supported on 64-bit Windows—the NTVDM (NT Virtual DOS Machine) is "
            "only available on 32-bit Windows."
        ),
    },
    {
        "id": "c2d1v3-045",
        "domain": 1,
        "objective": "1.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows Settings",
        "stem": (
            "A Windows 11 workstation is shared by multiple employees who each log in with "
            "their own domain accounts. The IT department wants to ensure each user's "
            "files remain private and cannot be accessed by other users on the same machine. "
            "Which Windows feature provides this separation by default on NTFS volumes?"
        ),
        "options": [
            {
                "id": "a",
                "text": "BitLocker whole-disk encryption",
                "correct": False,
                "rationale": (
                    "Incorrect. BitLocker encrypts the entire volume, protecting data if "
                    "the drive is removed—but it does not provide per-user file separation "
                    "while the OS is running and unlocked. All logged-in users can still "
                    "access each other's files unless NTFS permissions restrict them."
                ),
            },
            {
                "id": "b",
                "text": "NTFS user profile permissions—each user's profile folder (C:\\Users\\username) is protected by ACLs granting access only to that user and Administrators.",
                "correct": True,
                "rationale": (
                    "Correct. When Windows creates a user profile folder under C:\\Users, "
                    "it sets NTFS ACLs granting full control to the owner and Administrators "
                    "only. Standard users cannot browse or read other users' profile folders "
                    "by default."
                ),
            },
            {
                "id": "c",
                "text": "Windows Sandbox isolates each user's session in a separate container.",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Sandbox is a lightweight disposable desktop for "
                    "safely running untrusted applications—it is not a mechanism for "
                    "per-user file access separation in shared workstation scenarios."
                ),
            },
            {
                "id": "d",
                "text": "User Account Control (UAC) blocks cross-user file access by prompting for elevation.",
                "correct": False,
                "rationale": (
                    "Incorrect. UAC prompts for administrative elevation when system-level "
                    "changes are attempted. It does not enforce file-level separation "
                    "between standard user accounts—that is the role of NTFS ACLs."
                ),
            },
        ],
        "explanation": (
            "NTFS ACLs are the enforcement mechanism for user file privacy on Windows. "
            "C:\\Users\\<username> receives ACLs granting Full Control to the user and "
            "Administrators, and denying access to other standard users. This is set "
            "automatically when a new user profile is created. BitLocker protects against "
            "offline access (stolen drive); UAC governs system changes—neither enforces "
            "between-user file separation at runtime."
        ),
    },
    {
        "id": "c2d1v3-046",
        "domain": 1,
        "objective": "1.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows administrative tools (MMC snap-ins)",
        "stem": (
            "A Windows Server 2019 administrator uses Performance Monitor to capture a "
            "data collector set over 24 hours. After reviewing the report, they notice "
            "memory Pages/sec consistently exceeds 20 with a high 'Page Faults/sec' counter. "
            "What does this indicate, and what is the MOST appropriate remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "High Pages/sec indicates network packet fragmentation; upgrade the NIC.",
                "correct": False,
                "rationale": (
                    "Incorrect. Pages/sec is a memory performance counter measuring hard "
                    "page faults (disk reads/writes for paging). It has no relation to "
                    "network packet fragmentation or NIC performance."
                ),
            },
            {
                "id": "b",
                "text": "The server is experiencing excessive paging (thrashing), indicating insufficient physical RAM; adding RAM is the appropriate fix.",
                "correct": True,
                "rationale": (
                    "Correct. Pages/sec measures the rate of hard page faults—pages read "
                    "from or written to the pagefile. Sustained values above 20 indicate "
                    "the server is frequently swapping memory to disk (thrashing), which "
                    "causes severe performance degradation. Adding physical RAM reduces "
                    "the need to page."
                ),
            },
            {
                "id": "c",
                "text": "Pages/sec above 20 indicates CPU cache misses; upgrading to a faster processor resolves the issue.",
                "correct": False,
                "rationale": (
                    "Incorrect. CPU cache misses are measured by processor cache counters, "
                    "not Pages/sec. Pages/sec is specifically a memory paging metric "
                    "reflecting disk I/O due to insufficient RAM."
                ),
            },
            {
                "id": "d",
                "text": "This is normal behavior; Pages/sec above 20 is the Windows optimal operating range.",
                "correct": False,
                "rationale": (
                    "Incorrect. Sustained Pages/sec above 20 is a well-documented warning "
                    "threshold indicating a memory bottleneck. Values near 0 are normal "
                    "when adequate RAM is installed."
                ),
            },
        ],
        "explanation": (
            "Pages/sec (Memory object in Performance Monitor) measures hard page faults: "
            "accesses to memory pages not in physical RAM that require disk I/O to the "
            "pagefile. Sustained values > 20 indicate thrashing (excessive paging). "
            "Combined with high Page Faults/sec, this confirms RAM insufficiency. "
            "Remediation: add physical RAM. Secondary checks: identify the process "
            "consuming the most Working Set memory (Process\\Working Set counter)."
        ),
    },
    {
        "id": "c2d1v3-047",
        "domain": 1,
        "objective": "1.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows command-line tools",
        "stem": (
            "A technician needs to view the current IP routing table on a Windows workstation "
            "to understand how traffic destined for 192.168.50.0/24 will be routed. "
            "Which command displays the IPv4 routing table?"
        ),
        "options": [
            {
                "id": "a",
                "text": "arp -a",
                "correct": False,
                "rationale": (
                    "Incorrect. arp -a displays the ARP cache mapping IP addresses to "
                    "MAC addresses for recently contacted hosts. It does not show the "
                    "routing table."
                ),
            },
            {
                "id": "b",
                "text": "route print",
                "correct": True,
                "rationale": (
                    "Correct. 'route print' displays the full IPv4 and IPv6 routing tables, "
                    "showing network destination, netmask, gateway, interface, and metric "
                    "for each route. This reveals how traffic to 192.168.50.0/24 will "
                    "be forwarded."
                ),
            },
            {
                "id": "c",
                "text": "netstat -r",
                "correct": False,
                "rationale": (
                    "Incorrect. While netstat -r does display the routing table (equivalent "
                    "to route print), the question asks for the BEST or most direct command. "
                    "However, netstat -r is technically correct—but in practice 'route print' "
                    "is the canonical tool for routing table inspection on Windows."
                ),
            },
            {
                "id": "d",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /all shows interface-level IP configuration "
                    "(IP, mask, gateway, DNS, DHCP lease info) but does not display the "
                    "complete routing table with all route entries."
                ),
            },
        ],
        "explanation": (
            "'route print' is the Windows command for displaying the IPv4 and IPv6 routing "
            "tables. The output shows: Interface list (adapters), IPv4 Route Table (network "
            "destination, netmask, gateway, interface, metric), and Persistent Routes. "
            "To add a route: 'route add'; to delete: 'route delete'. The PowerShell "
            "equivalent is 'Get-NetRoute'."
        ),
    },
    {
        "id": "c2d1v3-048",
        "domain": 1,
        "objective": "1.11",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Linux file permissions",
        "stem": (
            "A Linux administrator runs 'ls -la /usr/bin/passwd' and sees:\n"
            "-rwsr-xr-x 1 root root 68208 Jan 10 2023 /usr/bin/passwd\n"
            "A junior admin asks what the 's' in the owner's execute position means "
            "and why it is there. What is the correct explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The 's' means the file is a symbolic link to /etc/shadow; it is not directly executable.",
                "correct": False,
                "rationale": (
                    "Incorrect. A symbolic link is indicated by 'l' as the first character "
                    "of the permission string. The 's' in the execute position of the owner "
                    "field indicates the setuid bit, not a symlink."
                ),
            },
            {
                "id": "b",
                "text": "The 's' is the setuid bit; when any user runs passwd, it temporarily executes as root, allowing it to write to /etc/shadow which is owned by root.",
                "correct": True,
                "rationale": (
                    "Correct. The setuid bit on an executable causes it to run with the "
                    "privileges of the file's owner (root) rather than the user who invokes "
                    "it. passwd needs root privileges to update /etc/shadow, so setuid "
                    "allows any user to change their own password without full root access."
                ),
            },
            {
                "id": "c",
                "text": "The 's' means the file is immutable (system-locked) and cannot be modified or deleted by any user including root.",
                "correct": False,
                "rationale": (
                    "Incorrect. Immutable files on Linux are set with 'chattr +i' and "
                    "shown via 'lsattr'. The 's' in the execute bit position is specifically "
                    "the setuid flag, not an immutability indicator."
                ),
            },
            {
                "id": "d",
                "text": "The 's' replaces 'x' to indicate the file requires a special security certificate to execute.",
                "correct": False,
                "rationale": (
                    "Incorrect. Linux file permissions do not use certificate-based execution "
                    "controls. The 's' replaces 'x' to visually indicate the setuid bit is "
                    "set AND execute permission is granted; 'S' (capital) would mean setuid "
                    "is set but execute is NOT set."
                ),
            },
        ],
        "explanation": (
            "The setuid bit ('s' replacing 'x' in the owner execute position) on an "
            "executable file causes it to run with the file owner's privileges (here: root), "
            "regardless of which user executes it. passwd must write to /etc/shadow "
            "(root-owned, mode 640), so it carries setuid. Capital 'S' means setuid is set "
            "but execute is not set (unusual and potentially misconfigured). The setgid "
            "'s' appears in the group execute position and runs the file as the file's group."
        ),
    },
]

