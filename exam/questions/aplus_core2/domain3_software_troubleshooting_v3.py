"""
CompTIA A+ Core 2 (220-1202) — Domain 3: Software Troubleshooting
47 NEW practice questions (v3) covering objectives 3.1 – 3.5.
IDs: c2d3v3-001 through c2d3v3-047
"""

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 3.3 — Malware removal best-practice process
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-001",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician has identified ransomware on a networked Windows "
            "workstation. The machine is still running and connected to the "
            "corporate LAN. Applying CompTIA's malware removal best practices, "
            "what is the correct FIRST action after verifying and identifying "
            "the symptoms?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disable System Restore to prevent the ransomware from hiding in shadow copies",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling System Restore is step 3. Before "
                    "touching the local machine's configuration, the system "
                    "must be quarantined (step 2) to prevent the ransomware "
                    "from encrypting network shares."
                ),
            },
            {
                "id": "b",
                "text": "Quarantine the infected system by disconnecting it from the network",
                "correct": True,
                "rationale": (
                    "Correct. Step 2 of the CompTIA process is to quarantine "
                    "the infected system immediately after verifying symptoms. "
                    "Disconnecting from the LAN stops lateral spread to shared "
                    "drives and other endpoints before any local remediation "
                    "begins."
                ),
            },
            {
                "id": "c",
                "text": "Update anti-malware definitions and run a full scan in normal mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Updating and scanning is part of step 4 "
                    "(Remediate). Running a scan before quarantine and before "
                    "disabling System Restore allows the malware to spread and "
                    "persist in shadow copies."
                ),
            },
            {
                "id": "d",
                "text": "Educate the user about phishing emails that deliver ransomware",
                "correct": False,
                "rationale": (
                    "Incorrect. User education is step 7 — the final step — "
                    "performed only after the system has been fully remediated "
                    "and hardened."
                ),
            },
        ],
        "explanation": (
            "CompTIA malware removal: 1) investigate/verify, 2) quarantine, "
            "3) disable System Restore, 4) remediate, 5) schedule scans/updates, "
            "6) re-enable System Restore and create restore point, 7) educate "
            "end user. Network isolation at step 2 is critical for ransomware "
            "to prevent file-share encryption."
        ),
    },
    {
        "id": "c2d3v3-002",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "After quarantining an infected Windows PC and disabling System "
            "Restore, a technician boots the machine from a USB-based "
            "preinstallation environment and runs an anti-malware scanner. "
            "Several threats are removed. The technician then reboots into "
            "normal Windows and runs another full scan — which reports clean. "
            "According to CompTIA best practices, what should the technician "
            "do NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reconnect to the network and re-enable System Restore, then create a restore point",
                "correct": False,
                "rationale": (
                    "Incorrect. Before re-enabling System Restore (step 6), "
                    "the technician must complete step 5: schedule recurring "
                    "scans and ensure software/OS updates are applied."
                ),
            },
            {
                "id": "b",
                "text": "Schedule recurring anti-malware scans and apply all pending OS and software updates",
                "correct": True,
                "rationale": (
                    "Correct. With remediation confirmed (step 4 complete), "
                    "the next action is step 5: schedule scans and run updates "
                    "to close the vulnerability that allowed infection and "
                    "ensure ongoing protection."
                ),
            },
            {
                "id": "c",
                "text": "Educate the end user about the infection source",
                "correct": False,
                "rationale": (
                    "Incorrect. Education is step 7, the last step. Steps 5 "
                    "(schedule/update) and 6 (re-enable System Restore) must "
                    "be completed first."
                ),
            },
            {
                "id": "d",
                "text": "Reimage the workstation because malware was found during the PE-environment scan",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging is warranted only when malware "
                    "cannot be reliably removed. A clean follow-up scan in "
                    "normal Windows mode indicates remediation was successful; "
                    "reimaging is disproportionate."
                ),
            },
        ],
        "explanation": (
            "After remediation scans confirm clean (step 4), the process "
            "continues with step 5 (schedule scans, apply updates), then "
            "step 6 (re-enable System Restore and create a clean restore "
            "point), and finally step 7 (educate end user). Skipping step 5 "
            "leaves the machine vulnerable to reinfection through the same "
            "unpatched vector."
        ),
    },
    {
        "id": "c2d3v3-003",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician is at step 4 of CompTIA's malware removal process "
            "on a Windows 11 workstation. The machine is quarantined and "
            "System Restore is disabled. The technician updates anti-malware "
            "definitions while offline using a downloaded definition package. "
            "Anti-malware scans in normal mode still detect and immediately "
            "re-detect the same rootkit after removal. What is the BEST "
            "next action within step 4?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run the scan from safe mode or a bootable preinstallation environment to scan the system files without the rootkit loaded",
                "correct": True,
                "rationale": (
                    "Correct. A rootkit that re-appears after removal in "
                    "normal mode is actively hiding in memory and interfering "
                    "with the scanner. Step 4 explicitly includes scanning "
                    "from safe mode or a preinstallation environment (WinPE) "
                    "where the rootkit cannot load and interfere."
                ),
            },
            {
                "id": "b",
                "text": "Proceed to step 5 and schedule scans; the rootkit will be removed on the next scheduled run",
                "correct": False,
                "rationale": (
                    "Incorrect. Moving to step 5 with an active rootkit "
                    "means remediation is incomplete. Step 4 must be fully "
                    "completed — including offline or safe-mode scanning — "
                    "before proceeding."
                ),
            },
            {
                "id": "c",
                "text": "Re-enable System Restore and roll back to a clean snapshot",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore was disabled in step 3 "
                    "precisely because shadow copies may contain the "
                    "infection. Re-enabling it mid-process reintroduces "
                    "that risk and deviates from the process order."
                ),
            },
            {
                "id": "d",
                "text": "Skip to step 7 and educate the user; rootkits require OS reinstall not further scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. While persistent rootkits may ultimately "
                    "require reimaging, the correct approach within the "
                    "seven-step process is to first attempt offline scanning "
                    "before escalating to full OS reinstall."
                ),
            },
        ],
        "explanation": (
            "Rootkits load before the OS security layer and intercept "
            "file-system calls to hide their presence and re-hook after "
            "removal in a live OS. CompTIA step 4 mandates scanning from "
            "a preinstallation environment (bootable WinPE/Linux scanner) "
            "where the rootkit cannot execute, allowing its files to be "
            "detected and removed cleanly."
        ),
    },
    {
        "id": "c2d3v3-004",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician has just completed step 5 of CompTIA's malware "
            "removal process (scheduled scans and applied updates). Which "
            "TWO actions make up step 6 before the technician can move to "
            "the final step? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Re-enable System Restore in Windows System Protection settings",
                "correct": True,
                "rationale": (
                    "Correct. Step 6 begins with re-enabling System Restore, "
                    "which was disabled in step 3. This allows the OS to "
                    "begin capturing new, clean restore points."
                ),
            },
            {
                "id": "b",
                "text": "Create a new System Restore point to capture the clean, remediated state",
                "correct": True,
                "rationale": (
                    "Correct. After re-enabling System Restore, immediately "
                    "creating a restore point captures a known-clean system "
                    "state that can be used for future recovery without "
                    "re-introducing malware."
                ),
            },
            {
                "id": "c",
                "text": "Reconnect the workstation to the network and test internet connectivity",
                "correct": False,
                "rationale": (
                    "Incorrect. Reconnecting to the network is implied as "
                    "part of returning the machine to service, but it is not "
                    "one of the two specific actions CompTIA defines for "
                    "step 6. The step is specifically about System Restore."
                ),
            },
            {
                "id": "d",
                "text": "Disable auto-run on all removable media to prevent reinfection",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardening tasks such as disabling AutoRun "
                    "may be good practice but are not the defined content of "
                    "step 6. This would fall under organizational security "
                    "policy, not the specific seven-step malware removal step."
                ),
            },
        ],
        "explanation": (
            "Step 6 of CompTIA's malware removal process consists of exactly "
            "two sub-actions: (a) re-enable System Restore and (b) create "
            "a new restore point. This ensures a clean recovery baseline "
            "exists. Step 7 (educate end user) follows immediately after."
        ),
    },
    {
        "id": "c2d3v3-005",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician successfully removes a banking Trojan from a "
            "workstation following all seven CompTIA malware removal steps. "
            "During step 7 (educate end user), the user argues they already "
            "know not to click suspicious links and just wants their computer "
            "back. Which statement BEST represents why step 7 is mandatory "
            "even for security-aware users?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Step 7 is only a formality to satisfy helpdesk ticket-closure requirements",
                "correct": False,
                "rationale": (
                    "Incorrect. User education is a substantive security "
                    "control, not a paperwork formality. Banking Trojans "
                    "often arrive through social engineering despite users "
                    "believing they are careful."
                ),
            },
            {
                "id": "b",
                "text": "The user's existing knowledge failed to prevent this infection, so targeted education about the specific attack vector addresses the real gap",
                "correct": True,
                "rationale": (
                    "Correct. The infection occurred despite the user's "
                    "self-reported awareness. Step 7 is specifically about "
                    "explaining how this particular infection happened and "
                    "closing that specific behavioral gap to prevent "
                    "recurrence."
                ),
            },
            {
                "id": "c",
                "text": "CompTIA requires the technician to obtain a signed liability waiver as part of step 7",
                "correct": False,
                "rationale": (
                    "Incorrect. CompTIA's step 7 is about substantive user "
                    "education, not legal waivers. No such signature "
                    "requirement is part of the seven-step process."
                ),
            },
            {
                "id": "d",
                "text": "Step 7 verifies the anti-malware software is properly installed before returning the device",
                "correct": False,
                "rationale": (
                    "Incorrect. Anti-malware verification occurs during "
                    "steps 4 and 5. Step 7 is exclusively about educating "
                    "the human user, not verifying software state."
                ),
            },
        ],
        "explanation": (
            "CompTIA's step 7 is justified even for self-reportedly aware "
            "users because the infection itself proved a gap existed. "
            "Effective education covers the specific vector used (e.g., "
            "malicious PDF attachment, fake update prompt) and tailored "
            "guidance on recognizing that exact technique in future — "
            "turning the incident into a learning moment."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.1 — Windows OS troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 workstation displays the error 'The application "
            "was unable to start correctly (0xc0000142)' for a critical "
            "line-of-business application. The application was working "
            "yesterday; no changes were made by the user. Other applications "
            "work normally. Which action should the technician try FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run SFC /scannow to check for and repair corrupted Windows system DLLs that the application may depend on",
                "correct": True,
                "rationale": (
                    "Correct. Error 0xc0000142 (DLL initialization failure) "
                    "often indicates that a system DLL the application depends "
                    "on has become corrupted. SFC /scannow checks and restores "
                    "protected Windows files including system DLLs and is the "
                    "correct first targeted step."
                ),
            },
            {
                "id": "b",
                "text": "Reinstall the line-of-business application",
                "correct": False,
                "rationale": (
                    "Incorrect. Reinstalling the application does not replace "
                    "Windows system DLLs. If the error stems from a corrupted "
                    "system file (not an app-bundled DLL), reinstalling "
                    "the app will not fix it."
                ),
            },
            {
                "id": "c",
                "text": "Upgrade the workstation to Windows 11 to resolve the DLL compatibility issue",
                "correct": False,
                "rationale": (
                    "Incorrect. Upgrading the OS is disruptive and not "
                    "warranted for a single application error. The error "
                    "appeared on a previously stable system and points to "
                    "local file corruption, not OS version incompatibility."
                ),
            },
            {
                "id": "d",
                "text": "Add the application to Windows Defender's exclusion list",
                "correct": False,
                "rationale": (
                    "Incorrect. 0xc0000142 is an initialization error, not "
                    "a security block. Windows Defender exclusions do not "
                    "resolve DLL load failures caused by file corruption."
                ),
            },
        ],
        "explanation": (
            "Error 0xc0000142 indicates a DLL failed to initialize, often "
            "because a shared Windows system DLL is missing or corrupted. "
            "SFC /scannow scans all protected system files and replaces "
            "corrupted ones from a cached copy. If SFC cannot repair, "
            "follow with DISM /Online /Cleanup-Image /RestoreHealth."
        ),
    },
    {
        "id": "c2d3v3-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 11 workstation frequently shows a BSOD with stop "
            "code PAGE_FAULT_IN_NONPAGED_AREA referencing ntfs.sys after "
            "the user connected a new external USB hard drive. No BSOD "
            "occurs when the USB drive is disconnected. Which is the MOST "
            "appropriate first action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Update the USB host controller driver and the external drive firmware",
                "correct": False,
                "rationale": (
                    "Incorrect. While driver updates may help, the direct "
                    "reference to ntfs.sys with a specific USB device suggests "
                    "the external drive's file system has errors that cause "
                    "the NTFS driver to fault. chkdsk addresses this directly."
                ),
            },
            {
                "id": "b",
                "text": "Run chkdsk /f /r on the external USB drive to repair file system errors",
                "correct": True,
                "rationale": (
                    "Correct. PAGE_FAULT_IN_NONPAGED_AREA referencing ntfs.sys "
                    "that only appears with one external drive indicates the "
                    "NTFS driver is encountering unreadable or corrupt sectors "
                    "on that drive. chkdsk /f /r repairs file system errors "
                    "and recovers bad sectors."
                ),
            },
            {
                "id": "c",
                "text": "Roll back the most recent Windows Update",
                "correct": False,
                "rationale": (
                    "Incorrect. The BSOD is directly correlated with a "
                    "specific USB drive, not a Windows Update. Rolling back "
                    "an update would not address file system corruption on "
                    "the external drive."
                ),
            },
            {
                "id": "d",
                "text": "Replace the internal NVMe SSD as ntfs.sys indicates system drive failure",
                "correct": False,
                "rationale": (
                    "Incorrect. ntfs.sys is the Windows NTFS file system "
                    "driver that services ALL NTFS volumes, including external "
                    "ones. The correlation with the external drive (not the "
                    "internal SSD) is the key diagnostic clue."
                ),
            },
        ],
        "explanation": (
            "PAGE_FAULT_IN_NONPAGED_AREA with ntfs.sys specifically when "
            "one drive is connected indicates a corrupt NTFS structure on "
            "that volume causing the NTFS kernel driver to fault. chkdsk /f "
            "/r on the external drive finds and repairs logical errors and "
            "bad sectors. If chkdsk cannot repair, back up the data and "
            "reformat the drive."
        ),
    },
    {
        "id": "c2d3v3-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 user reports that their desktop icons, taskbar, "
            "and Start menu do not appear after login. Only a blank desktop "
            "background is visible and the cursor moves normally. Task Manager "
            "can be opened via Ctrl+Alt+Del. Which is the MOST targeted "
            "first action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "In Task Manager, end the 'explorer.exe' process if running, then use File > Run new task to start 'explorer.exe'",
                "correct": True,
                "rationale": (
                    "Correct. The Windows Shell (explorer.exe) provides the "
                    "desktop, taskbar, and Start menu. If it failed to start "
                    "or crashed, launching it from Task Manager > File > Run "
                    "new task immediately restores the shell without rebooting."
                ),
            },
            {
                "id": "b",
                "text": "Perform a System Restore from the Windows Recovery Environment",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore is a high-impact action. "
                    "Relaunching explorer.exe is a targeted, immediate fix "
                    "that takes seconds and causes no data loss. System "
                    "Restore is not warranted as a first step."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow from an elevated command prompt in Task Manager",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC may be appropriate if explorer.exe is "
                    "corrupted, but launching explorer.exe first establishes "
                    "whether it is a crash/startup failure rather than "
                    "corruption. Relaunch first, diagnose deeper only if it "
                    "fails again."
                ),
            },
            {
                "id": "d",
                "text": "Reboot the workstation and observe if explorer.exe starts on next login",
                "correct": False,
                "rationale": (
                    "Incorrect. Rebooting is disruptive and may not reveal "
                    "the cause. Relaunching explorer.exe directly from Task "
                    "Manager is faster, less disruptive, and directly tests "
                    "whether the shell simply failed to start."
                ),
            },
        ],
        "explanation": (
            "A blank desktop with a working cursor and accessible Task "
            "Manager is the classic sign that explorer.exe (the Windows "
            "Shell) did not start or crashed. Task Manager > File > Run "
            "new task > explorer.exe immediately restores the shell. If "
            "it crashes again, SFC /scannow or checking the Application "
            "event log for explorer.exe errors is the next step."
        ),
    },
    {
        "id": "c2d3v3-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 workstation generates a BSOD with stop code "
            "KERNEL_DATA_INPAGE_ERROR approximately once per week. The "
            "system event log shows Event ID 7 (disk errors) on the "
            "system drive prior to each crash. Memory tests pass. Which "
            "is the MOST appropriate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run DISM /RestoreHealth to repair the Windows component store",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM repairs OS image corruption in the "
                    "component store. KERNEL_DATA_INPAGE_ERROR combined with "
                    "disk Event ID 7 (bad block / read error) points to a "
                    "hardware-level storage problem, which DISM cannot fix."
                ),
            },
            {
                "id": "b",
                "text": "Run chkdsk /f /r on the system drive and review S.M.A.R.T. data; plan drive replacement if errors are confirmed",
                "correct": True,
                "rationale": (
                    "Correct. KERNEL_DATA_INPAGE_ERROR means the OS could "
                    "not read a required page from the pagefile or OS "
                    "volume. Event ID 7 confirms physical read errors. "
                    "chkdsk /f /r attempts repair; S.M.A.R.T. data reveals "
                    "reallocated sector count and pending sectors, "
                    "confirming whether the drive is failing."
                ),
            },
            {
                "id": "c",
                "text": "Increase the virtual memory pagefile size to prevent page read failures",
                "correct": False,
                "rationale": (
                    "Incorrect. The pagefile size is irrelevant when the "
                    "physical drive itself cannot read data. Increasing the "
                    "pagefile on a failing drive would only extend more "
                    "data onto bad sectors."
                ),
            },
            {
                "id": "d",
                "text": "Update the storage controller driver and reboot to fix the read errors",
                "correct": False,
                "rationale": (
                    "Incorrect. Event ID 7 disk errors with KERNEL_DATA_"
                    "INPAGE_ERROR indicate physical media problems, not a "
                    "driver bug. A driver update would not repair bad sectors."
                ),
            },
        ],
        "explanation": (
            "KERNEL_DATA_INPAGE_ERROR + Event ID 7 (disk errors) = failing "
            "storage device. The OS cannot page data from the disk, causing "
            "the kernel to crash. chkdsk /f /r remaps bad sectors where "
            "possible; S.M.A.R.T. attributes (especially Current Pending "
            "Sectors and Reallocated Sectors Count) determine whether "
            "replacement is necessary. Back up data immediately."
        ),
    },
    {
        "id": "c2d3v3-010",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 11 workstation runs extremely slowly after login. "
            "Task Manager shows CPU at 8%, RAM at 35%, and disk at 100%. "
            "The system is 6 months old with a SATA SSD. Which TWO actions "
            "are MOST likely to identify or resolve the 100% disk usage? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open Resource Monitor > Disk tab to identify which process is generating the highest I/O",
                "correct": True,
                "rationale": (
                    "Correct. Resource Monitor's Disk tab shows per-process "
                    "read/write bytes per second in real time, directly "
                    "identifying the offending process (e.g., Windows Search "
                    "indexing, SysMain, Windows Update) causing 100% disk "
                    "saturation."
                ),
            },
            {
                "id": "b",
                "text": "Disable the SysMain (Superfetch) service if it appears as the top disk consumer",
                "correct": True,
                "rationale": (
                    "Correct. SysMain (formerly Superfetch) pre-loads "
                    "frequently used apps into RAM but can cause sustained "
                    "100% disk I/O on SATA SSDs and HDDs, especially on "
                    "newer Windows 11 installs. Disabling it is a common "
                    "and effective fix when it is the top consumer in "
                    "Resource Monitor."
                ),
            },
            {
                "id": "c",
                "text": "Run DISM /RestoreHealth to repair any corruption causing excessive disk access",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM repairs the component store; it does "
                    "not address a service or process causing high I/O. "
                    "Running DISM would itself add more disk I/O during "
                    "its operation without diagnosing the root cause."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall Windows to eliminate all background processes",
                "correct": False,
                "rationale": (
                    "Incorrect. Reinstalling Windows is the last resort. "
                    "The cause (a specific high-I/O service) can be "
                    "identified and resolved without reinstallation."
                ),
            },
        ],
        "explanation": (
            "100% disk usage with low CPU/RAM on an SSD commonly results "
            "from SysMain, Windows Search indexing, or Windows Update. "
            "Resource Monitor identifies the culprit process precisely. "
            "SysMain is the most common cause on Windows 10/11 with "
            "SATA SSDs and is safely disableable without OS impact."
        ),
    },
    {
        "id": "c2d3v3-011",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A user receives the error 'Your Windows license will expire "
            "soon' and the taskbar has turned black. IT confirms the volume "
            "license activation server is reachable. The machine was recently "
            "cloned from a master image. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The cloned machine has the same machine SID and hardware GUID as the source, causing KMS activation conflicts",
                "correct": False,
                "rationale": (
                    "Incorrect. Duplicate SIDs cause domain authentication "
                    "issues, but KMS activation is based on a client machine "
                    "ID (CMID) derived from different factors. SID duplication "
                    "alone does not typically cause this specific licensing "
                    "error."
                ),
            },
            {
                "id": "b",
                "text": "The cloned machine's KMS client has not yet activated against the KMS server and the 30-day grace period is expiring",
                "correct": True,
                "rationale": (
                    "Correct. Cloned Windows images using volume licensing "
                    "must activate against a KMS server. If Sysprep was not "
                    "run (or /generalize was skipped), the activation clock "
                    "from the source image carries over and the clone may "
                    "exhaust the grace period without activating. Running "
                    "'slmgr /ato' forces immediate KMS activation."
                ),
            },
            {
                "id": "c",
                "text": "The Windows license key is not a volume license key and does not support KMS activation",
                "correct": False,
                "rationale": (
                    "Incorrect. If the key were wrong, the machine would have "
                    "failed to activate from the start — not after working "
                    "initially. A clone from a valid volume-licensed image "
                    "retains a valid GVLK (Generic Volume License Key)."
                ),
            },
            {
                "id": "d",
                "text": "The KMS server has reached its activation client limit and is refusing new activations",
                "correct": False,
                "rationale": (
                    "Incorrect. KMS servers have a minimum threshold of "
                    "activated clients required (25 for Windows clients) but "
                    "no upper client limit. This is not a standard KMS "
                    "failure mode."
                ),
            },
        ],
        "explanation": (
            "Cloned images may carry over the activation grace period "
            "countdown. Running 'slmgr /ato' forces an immediate KMS "
            "activation attempt. If it fails, 'slmgr /dlv' shows the "
            "activation state and remaining grace days. Proper imaging "
            "practice includes running Sysprep /generalize to reset the "
            "activation clock before deployment."
        ),
    },
    {
        "id": "c2d3v3-012",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A technician troubleshoots a Windows workstation where a "
            "non-critical application consistently crashes with an "
            "application error in Event Viewer every morning at 7:02 AM. "
            "No manual interaction triggers it — it simply dies at that "
            "time. Which built-in Windows tool most likely reveals the "
            "cause without additional software?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Task Scheduler (taskschd.msc) — to check for a scheduled task configured to run and conflict with the application",
                "correct": True,
                "rationale": (
                    "Correct. A crash occurring at a precise time daily "
                    "strongly suggests a scheduled task (backup agent, "
                    "update, script) that conflicts with or terminates the "
                    "application. Task Scheduler shows all configured tasks "
                    "and their exact trigger times."
                ),
            },
            {
                "id": "b",
                "text": "Resource Monitor — to watch CPU usage spikes at 7:02 AM",
                "correct": False,
                "rationale": (
                    "Incorrect. Resource Monitor would require the technician "
                    "to be present at 7:02 AM watching in real time and still "
                    "would not reveal WHY the crash happens — only that "
                    "resources were used. Task Scheduler directly shows what "
                    "is executing at that moment."
                ),
            },
            {
                "id": "c",
                "text": "Performance Monitor — to create a data collector set for the crash time window",
                "correct": False,
                "rationale": (
                    "Incorrect. Performance Monitor captures metrics but "
                    "cannot identify a scheduled task as the cause. While "
                    "useful for capacity analysis, Task Scheduler directly "
                    "addresses the time-correlated crash pattern."
                ),
            },
            {
                "id": "d",
                "text": "Windows Memory Diagnostic — to check for RAM errors occurring at peak load",
                "correct": False,
                "rationale": (
                    "Incorrect. Memory diagnostic tests physical RAM for "
                    "faults and is not relevant to a precisely timed "
                    "application crash that correlates with clock time "
                    "rather than memory pressure."
                ),
            },
        ],
        "explanation": (
            "Time-correlated application crashes are a hallmark of Task "
            "Scheduler conflicts — a backup agent terminating the app, "
            "an antivirus scan pegging CPU, or a script killing a process. "
            "Task Scheduler (taskschd.msc) shows all tasks and their trigger "
            "times. Checking tasks scheduled at or just before 7:02 AM "
            "is the fastest diagnostic path."
        ),
    },
    {
        "id": "c2d3v3-013",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 PC boots normally but users report that mapped "
            "network drives show as disconnected (red X) immediately after "
            "login. Running 'net use' from Command Prompt reconnects them "
            "successfully. The issue recurs on every login. Which is the "
            "MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The mapped drives are configured to reconnect at login but Windows connects them before the network is fully available",
                "correct": True,
                "rationale": (
                    "Correct. A well-known Windows behavior: drive mappings "
                    "via Group Policy or the 'reconnect at sign-in' option "
                    "attempt connection during login before the network "
                    "stack and authentication are fully initialized, "
                    "resulting in a red X that clears when the network "
                    "is ready. Enabling 'Always wait for the network at "
                    "computer startup and logon' via GPO resolves this."
                ),
            },
            {
                "id": "b",
                "text": "The file server's SMB service is stopping and restarting every morning",
                "correct": False,
                "rationale": (
                    "Incorrect. If the SMB service on the server were cycling, "
                    "multiple users would report failures and 'net use' from "
                    "the client would also fail. The fact that 'net use' "
                    "reconnects successfully indicates the server is fine "
                    "and the issue is client-side timing."
                ),
            },
            {
                "id": "c",
                "text": "The user's account lacks NTFS read permissions on the mapped drive path",
                "correct": False,
                "rationale": (
                    "Incorrect. A permissions problem would cause persistent "
                    "access failure, not a temporary red X that resolves "
                    "automatically or via 'net use'. Permissions do not "
                    "change between login and running 'net use'."
                ),
            },
            {
                "id": "d",
                "text": "The network adapter duplex is mismatched, causing early login packet loss",
                "correct": False,
                "rationale": (
                    "Incorrect. A duplex mismatch causes performance "
                    "degradation and collisions for all traffic, not a "
                    "timing-specific failure at login that self-resolves "
                    "with a manual reconnect command."
                ),
            },
        ],
        "explanation": (
            "Mapped drives showing red X at login that resolve manually "
            "is a classic Windows race condition: the shell loads before "
            "the network authenticates. Fix via GPO: Computer Configuration "
            "> Administrative Templates > System > Logon > 'Always wait "
            "for the network at computer startup and logon' = Enabled."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.1 — Windows boot troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-014",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A dual-boot PC running Windows 11 and Ubuntu fails to display "
            "the GRUB boot menu after a Windows Update. The system boots "
            "directly into Windows. The Ubuntu partition and files are "
            "intact. Which action BEST restores the dual-boot menu without "
            "reinstalling Ubuntu?"
        ),
        "options": [
            {
                "id": "a",
                "text": "From Ubuntu live USB, run 'grub-install' and 'update-grub' to restore the GRUB bootloader",
                "correct": True,
                "rationale": (
                    "Correct. Windows Updates sometimes overwrite the "
                    "bootloader with the Windows Boot Manager, removing "
                    "GRUB. Booting from Ubuntu live media and reinstalling "
                    "GRUB to the disk's MBR/ESP restores the dual-boot "
                    "menu without touching Ubuntu's data partition."
                ),
            },
            {
                "id": "b",
                "text": "Run 'bootrec /rebuildbcd' from WinRE to add Ubuntu to the Windows Boot Manager",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec /rebuildbcd only scans for and adds "
                    "Windows installations. It does not detect or add Linux "
                    "entries to the BCD. GRUB must be restored from the "
                    "Linux side to manage the dual-boot menu."
                ),
            },
            {
                "id": "c",
                "text": "Use msconfig to add Ubuntu as a boot entry in the Boot tab",
                "correct": False,
                "rationale": (
                    "Incorrect. msconfig's Boot tab only manages Windows "
                    "BCD entries. Linux boot entries are not compatible "
                    "with Windows Boot Manager configuration via msconfig."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall Ubuntu to restore the GRUB bootloader",
                "correct": False,
                "rationale": (
                    "Incorrect. Full reinstallation is unnecessary when "
                    "the Ubuntu partition is intact. GRUB can be reinstalled "
                    "from a live USB without touching the existing Ubuntu "
                    "installation or data."
                ),
            },
        ],
        "explanation": (
            "Windows Updates frequently overwrite the MBR/ESP bootloader "
            "with Windows Boot Manager, silently removing GRUB. The standard "
            "fix is: boot Ubuntu live USB > open terminal > identify the "
            "Ubuntu partition > mount it > run grub-install and update-grub. "
            "GRUB is restored and will once again manage the dual-boot menu."
        ),
    },
    {
        "id": "c2d3v3-015",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A Windows 10 workstation displays 'Inaccessible Boot Device' "
            "BSOD after a storage controller driver was updated via Windows "
            "Update. The system cannot complete boot. WinRE is accessible. "
            "Which is the MOST targeted corrective action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "From WinRE Command Prompt, use DISM to remove the problematic driver package",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM in WinRE can service an offline Windows "
                    "image but removing a driver package offline with DISM "
                    "is a multi-step advanced operation. Using System Restore "
                    "or startup repair is more direct and less risky."
                ),
            },
            {
                "id": "b",
                "text": "From WinRE, use System Restore to roll back to a restore point created before the driver update",
                "correct": True,
                "rationale": (
                    "Correct. INACCESSIBLE_BOOT_DEVICE after a driver update "
                    "means the new storage controller driver cannot enumerate "
                    "the boot device. System Restore from WinRE rolls back "
                    "the driver (and other recent changes) to a pre-update "
                    "state where the driver was working."
                ),
            },
            {
                "id": "c",
                "text": "Reformat the system drive and reinstall Windows 10",
                "correct": False,
                "rationale": (
                    "Incorrect. Reinstalling is a last resort. The cause "
                    "(a bad driver update) is directly addressable via "
                    "System Restore without data loss."
                ),
            },
            {
                "id": "d",
                "text": "Change the SATA mode in BIOS from AHCI to IDE compatibility mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Switching SATA mode would cause Windows to "
                    "use a different driver path but could corrupt the "
                    "current installation and cause further issues. The "
                    "driver update is the confirmed cause; System Restore "
                    "directly reverts it."
                ),
            },
        ],
        "explanation": (
            "INACCESSIBLE_BOOT_DEVICE immediately following a storage "
            "controller driver update is a direct causal relationship — "
            "the new driver cannot initialize the drive. WinRE > System "
            "Restore undoes the driver change. If no restore point exists, "
            "use WinRE > Command Prompt > 'dism /image:C:\\ /get-drivers' "
            "to identify and remove the offending driver offline."
        ),
    },
    {
        "id": "c2d3v3-016",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A GPT-partitioned Windows 11 PC fails to boot after the EFI "
            "System Partition (ESP) was accidentally deleted during a "
            "disk management operation. The BIOS is UEFI-only (no CSM). "
            "The Windows data partition is intact. Which recovery approach "
            "is correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Boot from Windows installation media, enter WinRE Command Prompt, and use diskpart to recreate the ESP, then bcdboot to populate it",
                "correct": True,
                "rationale": (
                    "Correct. With the ESP deleted, the UEFI firmware has "
                    "no boot files to load. The fix is: diskpart > create "
                    "a FAT32 partition with the EFI type attribute > assign "
                    "a drive letter > then run 'bcdboot C:\\Windows /s <ESP "
                    "letter>: /f UEFI' to copy the UEFI boot files and "
                    "rebuild the BCD."
                ),
            },
            {
                "id": "b",
                "text": "Run bootrec /fixmbr and bootrec /fixboot from WinRE",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec /fixmbr and /fixboot operate on "
                    "MBR/BIOS boot records, not the UEFI/GPT ESP. On a "
                    "UEFI-only system with GPT, these commands are "
                    "ineffective for ESP recovery."
                ),
            },
            {
                "id": "c",
                "text": "Enable CSM in BIOS to switch to legacy MBR boot and repair with bootrec",
                "correct": False,
                "rationale": (
                    "Incorrect. The system is UEFI-only with no CSM option. "
                    "Even if CSM were available, switching to legacy mode "
                    "on a GPT disk would require conversion and would likely "
                    "destroy the partition layout."
                ),
            },
            {
                "id": "d",
                "text": "Use Startup Repair from WinRE — it automatically detects and recreates a missing ESP",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Startup Repair can repair corrupted "
                    "boot files but does not recreate a completely deleted "
                    "ESP partition. The partition must first be manually "
                    "recreated with diskpart before boot files can be "
                    "populated."
                ),
            },
        ],
        "explanation": (
            "A deleted ESP on a GPT/UEFI system requires manual recreation: "
            "1) diskpart > select disk > create partition efi size=100 "
            "> format fs=fat32 quick > assign letter=S 2) bcdboot "
            "C:\\Windows /s S: /f UEFI. This rebuilds the EFI partition "
            "with correct boot files and UEFI BCD without touching the "
            "Windows data partition."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.2 — PC security issue troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-017",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A Windows workstation's anti-malware software is turned off and "
            "cannot be re-enabled — the toggle is grayed out in Windows "
            "Security. No GPO disables it. Attempts to enable it via "
            "PowerShell (Set-MpPreference) also fail silently. Which "
            "security condition MOST likely explains this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A third-party antivirus product registered as the active security provider, taking over from Windows Defender",
                "correct": False,
                "rationale": (
                    "Incorrect. A third-party AV product legitimately "
                    "disabling Defender through the Security Center API "
                    "would allow Defender to be re-enabled or the third-"
                    "party product to be visible. Silent PowerShell failure "
                    "with no visible third-party AV points to malware "
                    "interference."
                ),
            },
            {
                "id": "b",
                "text": "Malware has modified registry keys or loaded a policy that disables Windows Defender to prevent detection",
                "correct": True,
                "rationale": (
                    "Correct. A CompTIA-listed security symptom is that "
                    "malware actively disables AV/security tools to prevent "
                    "removal. This is commonly done via registry modifications "
                    "(HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender "
                    "\\DisableAntiSpyware = 1) that override UI controls "
                    "and PowerShell cmdlets."
                ),
            },
            {
                "id": "c",
                "text": "The Windows Security service (SecurityHealthService) needs to be restarted",
                "correct": False,
                "rationale": (
                    "Incorrect. Restarting the health service would restore "
                    "UI responsiveness but would not overcome a registry-"
                    "level policy disabling Defender. If malware set the "
                    "registry key, restarting the service would not "
                    "re-enable protection."
                ),
            },
            {
                "id": "d",
                "text": "The Windows license has expired, removing access to Windows Defender",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Defender functionality is not tied "
                    "to license activation status. An expired license "
                    "affects the ability to receive updates but does not "
                    "gray out the Defender toggle or cause PowerShell "
                    "cmdlets to fail."
                ),
            },
        ],
        "explanation": (
            "Malware frequently disables Windows Defender via the registry "
            "key HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\"
            "DisableAntiSpyware. This key takes policy-level precedence "
            "over both the UI and PowerShell. Remediation: boot from "
            "WinPE or a second OS, delete the key offline, then proceed "
            "with the 7-step malware removal process."
        ),
    },
    {
        "id": "c2d3v3-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user reports their Windows PC is running an unusual process "
            "named 'svch0st.exe' (with a zero instead of the letter O) that "
            "is consuming 40% CPU. Task Manager shows the process is running "
            "from C:\\Users\\Public\\. Legitimate Windows processes are "
            "unaffected. Which BEST describes this threat and the correct "
            "immediate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is a typosquatted malware process masquerading as svchost.exe; terminate it and quarantine the file before running full malware removal steps",
                "correct": True,
                "rationale": (
                    "Correct. Legitimate svchost.exe always runs from "
                    "C:\\Windows\\System32\\, never from user-writable "
                    "directories like C:\\Users\\Public\\. A process with "
                    "a look-alike name from a non-system path is masquerading "
                    "malware. Terminating it and quarantining the binary "
                    "is the correct immediate response before following "
                    "the full 7-step removal process."
                ),
            },
            {
                "id": "b",
                "text": "It is a legitimate Windows service host running from an alternate location due to a Windows Update relocation",
                "correct": False,
                "rationale": (
                    "Incorrect. Microsoft never relocates core Windows "
                    "processes to user-writable directories. Any process "
                    "claiming to be a system process but running from "
                    "C:\\Users\\ is definitively malicious."
                ),
            },
            {
                "id": "c",
                "text": "It is a third-party application's service host; check the vendor's documentation",
                "correct": False,
                "rationale": (
                    "Incorrect. The name 'svch0st.exe' (with zero) is not "
                    "a legitimate vendor naming convention — it is a "
                    "deliberate homoglyph impersonation of 'svchost.exe'. "
                    "Combined with the C:\\Users\\Public\\ path, this is "
                    "unambiguously malware."
                ),
            },
            {
                "id": "d",
                "text": "Add the process to Windows Defender's exclusion list to stop interference with normal operations",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding malware to the exclusion list would "
                    "actively protect the malicious process from detection "
                    "and removal — the opposite of the required action."
                ),
            },
        ],
        "explanation": (
            "Masquerading malware uses near-identical names (typosquatting) "
            "to evade casual inspection. The combination of a look-alike "
            "process name AND a non-system file path (C:\\Users\\Public\\) "
            "is definitive. Legitimate svchost.exe lives only in "
            "C:\\Windows\\System32\\. Quarantine the file and perform full "
            "malware removal."
        ),
    },
    {
        "id": "c2d3v3-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user reports pop-up advertisements appearing on the desktop "
            "and inside applications that normally never display ads, "
            "including Notepad. No browser is open at the time. The "
            "advertisements persist after rebooting. What type of malware "
            "is MOST consistent with these symptoms, and what is the "
            "BEST first action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Adware injecting ads at the OS level; run a dedicated adware/PUP removal tool in addition to standard anti-malware",
                "correct": True,
                "rationale": (
                    "Correct. Ads appearing outside a browser — inside "
                    "non-browser applications — indicate adware operating "
                    "at the OS or driver level, not a browser extension. "
                    "Dedicated PUP/adware removal tools (e.g., Malwarebytes "
                    "with PUP detection enabled) target adware that standard "
                    "AV may classify as low-risk and skip."
                ),
            },
            {
                "id": "b",
                "text": "Browser hijacker; reset all installed browsers to default settings",
                "correct": False,
                "rationale": (
                    "Incorrect. Browser hijackers affect only browser "
                    "behavior (search redirects, homepage changes). Ads "
                    "appearing in Notepad and other non-browser apps confirm "
                    "the adware is OS-level, not browser-confined."
                ),
            },
            {
                "id": "c",
                "text": "Ransomware using pop-ups to demand payment; disconnect from the network immediately",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware displays ransom demands with "
                    "cryptocurrency payment instructions, not product "
                    "advertisements. The ads-in-all-apps pattern is "
                    "characteristic of adware."
                ),
            },
            {
                "id": "d",
                "text": "A compromised Windows Update server pushing malicious display components",
                "correct": False,
                "rationale": (
                    "Incorrect. Compromised update infrastructure would "
                    "affect all machines on the network. A single user "
                    "experiencing system-wide ads points to locally "
                    "installed adware, not a network-side compromise."
                ),
            },
        ],
        "explanation": (
            "System-wide ads appearing in non-browser applications are a "
            "CompTIA-listed security symptom of adware operating at the "
            "OS or display driver level. Standard Windows Defender may not "
            "remove PUPs/adware by default. Use dedicated adware removal "
            "tools with PUP detection enabled, then audit installed "
            "programs in Control Panel for suspicious software."
        ),
    },
    {
        "id": "c2d3v3-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "An executive's Windows laptop frequently experiences sluggish "
            "performance and high network utilization at night when it is "
            "supposed to be idle. Event Viewer shows scheduled task "
            "'WindowsUpdateCheck' running between 2–4 AM from an unusual "
            "path: C:\\ProgramData\\MicrosoftUpdate\\svc.exe. IT has "
            "not configured this task. What is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows Update is legitimately downloading patches during off-hours via the Windows Update Delivery Optimization service",
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate Windows Update tasks run from "
                    "C:\\Windows\\System32\\ or C:\\Windows\\SysWOW64\\. "
                    "A task named 'WindowsUpdateCheck' running from "
                    "C:\\ProgramData\\MicrosoftUpdate\\ is not a Microsoft "
                    "path and is a classic malware masquerade."
                ),
            },
            {
                "id": "b",
                "text": "Malware has established persistence via a scheduled task and is exfiltrating data during off-hours",
                "correct": True,
                "rationale": (
                    "Correct. Malware establishes persistence via Task "
                    "Scheduler using names that mimic legitimate Windows "
                    "tasks. Execution from a non-system path "
                    "(C:\\ProgramData\\) combined with high night-time "
                    "network traffic is a strong indicator of data "
                    "exfiltration malware. This is a CompTIA-listed security "
                    "symptom: high CPU/network usage and altered system tasks."
                ),
            },
            {
                "id": "c",
                "text": "A third-party backup software registered a task using the Windows Update service name to avoid conflicts",
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate third-party software does not "
                    "impersonate Windows Update task names. Naming a task "
                    "'WindowsUpdateCheck' from C:\\ProgramData\\ is a "
                    "deliberate deception pattern associated with malware."
                ),
            },
            {
                "id": "d",
                "text": "The executive's corporate VPN client performs nightly re-authentication, causing the high network usage",
                "correct": False,
                "rationale": (
                    "Incorrect. VPN re-authentication generates minimal "
                    "traffic. The combination of a suspicious non-system "
                    "binary, a masquerade task name, and sustained high "
                    "network utilization for two hours points to malware "
                    "exfiltration, not a VPN event."
                ),
            },
        ],
        "explanation": (
            "Malware commonly achieves persistence via Task Scheduler using "
            "Windows-mimicking names. Key red flags: binary path outside "
            "C:\\Windows\\System32\\; task not visible in IT-managed GPO; "
            "high sustained network traffic during idle periods. Remediation: "
            "delete the malicious task, quarantine the binary, and perform "
            "the full 7-step malware removal process."
        ),
    },
    {
        "id": "c2d3v3-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user's Windows PC exhibits the following: new toolbars in "
            "the browser, slow performance, and an unknown program in the "
            "system tray. The user recently installed free software from "
            "a file-sharing site. Which TWO actions should the technician "
            "take to remediate this? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Uninstall the recently installed free software and any co-installed PUPs via Programs and Features",
                "correct": True,
                "rationale": (
                    "Correct. Bundled software from file-sharing sites "
                    "commonly installs PUPs (Potentially Unwanted Programs) "
                    "alongside the main application. Uninstalling through "
                    "Programs and Features removes the visible components."
                ),
            },
            {
                "id": "b",
                "text": "Run a full scan with anti-malware software that has PUP detection enabled to remove residual components",
                "correct": True,
                "rationale": (
                    "Correct. Manual uninstall often leaves behind registry "
                    "entries, browser extensions, and service components. "
                    "A PUP-aware anti-malware scan removes residual "
                    "components that Programs and Features leaves behind."
                ),
            },
            {
                "id": "c",
                "text": "Reinstall the browser over the existing installation to clear toolbars",
                "correct": False,
                "rationale": (
                    "Incorrect. Reinstalling the browser on top of the "
                    "existing install often preserves extensions and settings, "
                    "including malicious toolbars. The PUP source (the "
                    "installed software) must be removed first."
                ),
            },
            {
                "id": "d",
                "text": "Disable Windows Firewall to reduce system overhead from PUP network monitoring",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabling Windows Firewall increases security "
                    "risk and does not remove PUPs. The firewall should "
                    "remain enabled during and after remediation."
                ),
            },
        ],
        "explanation": (
            "Bundleware/PUP infections from free software installs require "
            "both manual uninstall (to remove the registered software) and "
            "a PUP-specific anti-malware scan (to remove residual browser "
            "hijack components, services, and registry modifications that "
            "the uninstaller leaves behind)."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.2 — Browser security symptoms
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security symptoms",
        "stem": (
            "A user reports that their browser displays a padlock icon with "
            "a warning for a site that previously showed a clean padlock. "
            "The IT team has not changed the site's certificate. Other users "
            "on the same network do not see the warning. Checking the "
            "certificate details on the affected workstation reveals an "
            "unexpected intermediate CA. What is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A man-in-the-middle proxy or SSL inspection appliance is intercepting traffic on this specific workstation, presenting its own certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. An SSL inspection appliance would affect all "
                    "machines routed through it, not one workstation. The "
                    "isolated nature rules out a network-level SSL proxy as "
                    "the cause."
                ),
            },
            {
                "id": "b",
                "text": "Malware has installed a rogue CA certificate in the local machine's Trusted Root store and is intercepting HTTPS traffic on this workstation",
                "correct": True,
                "rationale": (
                    "Correct. Malware that performs local TLS interception "
                    "installs its own CA certificate into the Windows Trusted "
                    "Root store, then generates per-site certificates signed "
                    "by that rogue CA. The certificate chain shows an "
                    "unexpected intermediate CA visible only on the infected "
                    "machine."
                ),
            },
            {
                "id": "c",
                "text": "The website's certificate was reissued with a different CA and the browser has not cached the new root",
                "correct": False,
                "rationale": (
                    "Incorrect. If the site reissued its certificate, ALL "
                    "users would see a change. The isolation to one "
                    "workstation with an unexpected CA in the chain confirms "
                    "a local certificate store modification."
                ),
            },
            {
                "id": "d",
                "text": "The browser's certificate revocation check is failing, causing it to display a warning",
                "correct": False,
                "rationale": (
                    "Incorrect. A revocation check failure produces a "
                    "different warning (certificate revocation server "
                    "unreachable) and does not insert a new intermediate CA "
                    "into the chain visible in the certificate details."
                ),
            },
        ],
        "explanation": (
            "Rogue CA certificate injection is a sophisticated malware "
            "technique allowing full HTTPS inspection on one machine. "
            "Inspect the Windows Certificate Store (certmgr.msc) for "
            "unauthorized CA certificates in Trusted Root and Intermediate "
            "CAs. Remove unauthorized CAs and follow the full malware "
            "removal process."
        ),
    },
    {
        "id": "c2d3v3-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security symptoms",
        "stem": (
            "After clicking a link in an email, a user notices new browser "
            "extensions installed without consent in all installed browsers "
            "(Chrome, Firefox, Edge). The user did not approve any "
            "extension installations. What is the BEST description of "
            "what occurred, and what should be done?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The user's browser sync account pushed extensions from another device; sign out of browser sync to prevent further changes",
                "correct": False,
                "rationale": (
                    "Incorrect. Browser sync would only affect the same "
                    "browser, not multiple different browsers (Chrome, "
                    "Firefox, AND Edge) simultaneously. Cross-browser "
                    "extension installation requires OS-level write access."
                ),
            },
            {
                "id": "b",
                "text": "A drive-by download or malicious link executed code that installed extensions across all browsers; run a full malware scan and remove the extensions",
                "correct": True,
                "rationale": (
                    "Correct. Extensions installed across multiple different "
                    "browsers simultaneously require OS-level execution — "
                    "a browser exploit or drive-by download that ran code "
                    "with user privileges. This is a browser security symptom "
                    "(unauthorized extension installation). Anti-malware "
                    "scan plus manual extension removal from each browser "
                    "is required."
                ),
            },
            {
                "id": "c",
                "text": "Windows Update installed browser extensions as part of a cumulative update",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Update does not install browser "
                    "extensions, especially not across multiple different "
                    "browsers simultaneously. Extensions are browser-specific "
                    "and not distributed through Windows Update."
                ),
            },
            {
                "id": "d",
                "text": "The corporate IT Group Policy deployed the extensions for productivity monitoring",
                "correct": False,
                "rationale": (
                    "Incorrect. GPO-deployed extensions would be applied to "
                    "all managed machines, not just this one, and would "
                    "be visible in the extension management pages as "
                    "admin-installed. A GPO deployment would also not be "
                    "triggered by clicking an email link."
                ),
            },
        ],
        "explanation": (
            "Cross-browser unauthorized extension installation after clicking "
            "a link is a drive-by download executing at the OS level. "
            "Remediation: 1) run anti-malware scan, 2) remove extensions "
            "from each browser's extension manager, 3) check Task Scheduler "
            "and startup entries for persistence mechanisms, 4) follow the "
            "7-step malware removal process."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.4 — Mobile OS troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-024",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone displays 'No SIM card detected' after "
            "the device was dropped. Wi-Fi still works. A replacement SIM "
            "from the carrier also shows 'no SIM' in the same device. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The carrier account is suspended and the SIM is remotely deactivated",
                "correct": False,
                "rationale": (
                    "Incorrect. A suspended carrier account deactivates the "
                    "SIM electronically; a brand-new replacement SIM from "
                    "the carrier would also have a new ICCID and would work "
                    "if the hardware were functional. Both SIMs failing "
                    "in the same device after a drop confirms hardware damage."
                ),
            },
            {
                "id": "b",
                "text": "The SIM card tray or SIM reader hardware was damaged by the drop",
                "correct": True,
                "rationale": (
                    "Correct. A dropped device combined with 'No SIM' on "
                    "both the original and a known-good replacement SIM "
                    "confirms physical damage to the SIM reader or the "
                    "motherboard connector. Wi-Fi working confirms the "
                    "device is otherwise functional, isolating the fault "
                    "to the SIM hardware."
                ),
            },
            {
                "id": "c",
                "text": "The Android OS needs to be updated to re-detect the SIM hardware",
                "correct": False,
                "rationale": (
                    "Incorrect. OS updates add features and fix software "
                    "bugs but cannot repair physical hardware damage. A "
                    "known-good SIM failing after a physical drop confirms "
                    "hardware failure, not a software issue."
                ),
            },
            {
                "id": "d",
                "text": "The device needs a factory reset to clear the SIM detection cache",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM detection is a hardware-level function "
                    "with no persistent software cache that a factory reset "
                    "would clear. Two SIMs failing in the same device after "
                    "a drop points to physical hardware damage."
                ),
            },
        ],
        "explanation": (
            "The diagnostic logic here is hardware substitution: if a "
            "known-good replacement SIM also fails in the same device, "
            "the SIM itself is ruled out and the device SIM reader is "
            "implicated. Physical drop + SIM reader failure is the logical "
            "conclusion. Repair requires physical inspection and likely "
            "SIM tray / motherboard component replacement."
        ),
    },
    {
        "id": "c2d3v3-025",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's iOS device is stuck in a boot loop — the Apple logo "
            "appears, the device restarts, and the cycle repeats. The "
            "loop began during an OS update that lost power midway. "
            "Which is the BEST recovery method?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Force the device into Recovery Mode (DFU mode) and restore via a computer using Finder (macOS) or iTunes (Windows)",
                "correct": True,
                "rationale": (
                    "Correct. A failed mid-update iOS installation causing "
                    "a boot loop requires a full firmware restore from a "
                    "computer. DFU (Device Firmware Update) mode bypasses "
                    "the corrupted iOS and allows Finder/iTunes to flash "
                    "a clean iOS image, resolving the boot loop."
                ),
            },
            {
                "id": "b",
                "text": "Remove the SIM card and reboot to allow the device to boot without carrier authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. A boot loop from a corrupted OS update has "
                    "no dependency on carrier authentication. Removing the "
                    "SIM does not affect the OS boot process."
                ),
            },
            {
                "id": "c",
                "text": "Discharge the battery completely and recharge to reset firmware",
                "correct": False,
                "rationale": (
                    "Incorrect. Fully discharging an iOS device does not "
                    "reset firmware or repair a corrupted OS installation. "
                    "The device will continue to boot loop when recharged."
                ),
            },
            {
                "id": "d",
                "text": "Use iCloud.com to remotely erase the device and restore from iCloud backup",
                "correct": False,
                "rationale": (
                    "Incorrect. Find My iPhone's remote erase requires the "
                    "device to be able to connect to Apple's servers — which "
                    "it cannot do while stuck in a boot loop. A wired DFU "
                    "restore is required."
                ),
            },
        ],
        "explanation": (
            "A mid-update power failure corrupts the iOS image, causing "
            "a boot loop. DFU mode places the device in a state where the "
            "bootrom can communicate with Finder/iTunes without the OS "
            "loading, allowing a complete firmware flash. DFU entry on "
            "iPhone: specific button combination held for exactly 8 + 3 "
            "seconds while connected to a computer."
        ),
    },
    {
        "id": "c2d3v3-026",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A corporate Android device enrolled in MDM is unable to receive "
            "or send calls or texts, but mobile data works. The carrier "
            "confirms the SIM is active and the account is in good standing. "
            "Other employees with identical devices on the same carrier "
            "have no issues. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The MDM profile has applied a restriction that disables voice and SMS services on this device",
                "correct": True,
                "rationale": (
                    "Correct. MDM profiles can selectively disable voice "
                    "calls and SMS while permitting data. An MDM restriction "
                    "applied only to this device — while others on the same "
                    "carrier are unaffected — is the most targeted explanation "
                    "that fits all the facts."
                ),
            },
            {
                "id": "b",
                "text": "The carrier tower nearest the user is having a voice/SMS outage but data is routed through a different tower",
                "correct": False,
                "rationale": (
                    "Incorrect. A single tower outage would affect all "
                    "users in that cell, not one specific device. Other "
                    "employees on the same carrier having no issues rules "
                    "out a carrier-side tower problem."
                ),
            },
            {
                "id": "c",
                "text": "The device's IMEI has been blacklisted by the carrier",
                "correct": False,
                "rationale": (
                    "Incorrect. A blacklisted IMEI blocks all cellular "
                    "services — including data. The fact that mobile data "
                    "works rules out an IMEI blacklist."
                ),
            },
            {
                "id": "d",
                "text": "The device needs a SIM card replacement to restore voice functionality",
                "correct": False,
                "rationale": (
                    "Incorrect. The carrier confirmed the SIM is active. "
                    "Data working on the same SIM confirms it is functional. "
                    "A hardware SIM replacement is not indicated."
                ),
            },
        ],
        "explanation": (
            "MDM profiles can enforce granular restrictions, including "
            "disabling voice calls and/or SMS independently of data. When "
            "one device out of many on the same carrier loses only voice/SMS "
            "while data works, an MDM policy change is the most targeted "
            "explanation. Review the MDM console for recently applied "
            "restrictions on this device's profile."
        ),
    },
    {
        "id": "c2d3v3-027",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone GPS navigation app reports location "
            "accuracy of 'approximately 500 meters' and frequently loses "
            "the GPS fix entirely indoors and in urban canyons. The phone "
            "is 2 years old and has never had this issue until a recent "
            "OS update. Which is the BEST first action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Toggle Location Services off and on, and switch the location mode to 'High Accuracy' (GPS + Wi-Fi + cellular)",
                "correct": True,
                "rationale": (
                    "Correct. An OS update may have reset the location mode "
                    "to 'Battery Saving' (Wi-Fi/cellular only) or 'Device "
                    "Only' (GPS only). High Accuracy mode uses all three "
                    "sources together for best precision. Toggling location "
                    "off/on resets the location stack — a targeted, "
                    "non-destructive first step."
                ),
            },
            {
                "id": "b",
                "text": "Replace the device as the GPS antenna has degraded after 2 years",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware degradation is gradual, not sudden "
                    "following an OS update. The correlation with the update "
                    "strongly suggests a settings or software-level change, "
                    "not hardware failure."
                ),
            },
            {
                "id": "c",
                "text": "Uninstall the navigation app and reinstall it from the Play Store",
                "correct": False,
                "rationale": (
                    "Incorrect. The issue affects GPS accuracy system-wide "
                    "(500m accuracy), not just one app. Reinstalling the "
                    "navigation app does not change the OS location mode "
                    "that governs GPS behavior across all apps."
                ),
            },
            {
                "id": "d",
                "text": "Perform a factory reset to restore the GPS calibration from before the update",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset causes total data loss and "
                    "is not warranted before trying a simple location mode "
                    "settings change. GPS does not store calibration data "
                    "that would be reset by a factory reset."
                ),
            },
        ],
        "explanation": (
            "Post-update GPS degradation commonly results from the OS "
            "resetting location mode to a less accurate setting. High "
            "Accuracy mode (Settings > Location > Mode) combines GPS, "
            "Wi-Fi, and cellular triangulation for best results. If "
            "toggling and mode change don't help, clear the GPS cache "
            "via Settings > Apps > GPS status app, or use a GPS testing "
            "app to verify satellite acquisition."
        ),
    },
    {
        "id": "c2d3v3-028",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone shows the touchscreen is unresponsive "
            "in certain areas but works fine elsewhere. The dead zone "
            "appeared after the phone fell face-down on a desk. Which TWO "
            "findings would confirm this is a hardware problem requiring "
            "screen replacement rather than a software issue? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The dead zone remains in exactly the same screen coordinates after a factory reset",
                "correct": True,
                "rationale": (
                    "Correct. A persistent dead zone in the same physical "
                    "location after a factory reset (which eliminates all "
                    "software state) confirms the digitizer hardware is "
                    "damaged, not a software or app-level issue."
                ),
            },
            {
                "id": "b",
                "text": "A touch diagnostic app (e.g., MultiTouch Tester) shows missing or erratic touch points in the same region regardless of app used",
                "correct": True,
                "rationale": (
                    "Correct. A touch diagnostic app tests raw digitizer "
                    "input directly. If the dead zone appears at the hardware "
                    "input layer across all apps and after reset, the "
                    "digitizer (touch sensor layer) is physically damaged."
                ),
            },
            {
                "id": "c",
                "text": "The issue only occurs in one specific application",
                "correct": False,
                "rationale": (
                    "Incorrect. A hardware digitizer failure affects all "
                    "apps equally. If the dead zone only appears in one app, "
                    "it is a software/app-level overlay issue, not physical "
                    "digitizer damage."
                ),
            },
            {
                "id": "d",
                "text": "Clearing the app cache resolves the unresponsive area temporarily",
                "correct": False,
                "rationale": (
                    "Incorrect. If clearing the app cache temporarily "
                    "resolves the issue, the cause is software/cache-related, "
                    "not physical hardware damage. Hardware failures are not "
                    "affected by app cache operations."
                ),
            },
        ],
        "explanation": (
            "Confirming hardware vs. software for a touch dead zone: "
            "1) Test with a raw touch diagnostic app that bypasses all "
            "application logic — if it shows the same dead zone, the "
            "digitizer layer is damaged. 2) Perform a factory reset — "
            "if the dead zone persists unchanged in the same coordinates, "
            "software is ruled out. Both confirm screen replacement is "
            "needed."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.5 — Mobile app security troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-029",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user receives an SMS message from their bank's short code "
            "asking them to click a link and confirm their credentials. "
            "The user clicks the link and enters their banking password. "
            "Later, they discover unauthorized transactions. Which attack "
            "type BEST describes what occurred, and what should the user "
            "do immediately?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smishing (SMS phishing); immediately change the compromised banking password from a clean device and notify the bank",
                "correct": True,
                "rationale": (
                    "Correct. Smishing is phishing delivered via SMS. The "
                    "attacker spoofed a legitimate bank short code to "
                    "harvest credentials. Immediate password change from "
                    "a known-clean device limits further unauthorized "
                    "access, and notifying the bank triggers fraud controls."
                ),
            },
            {
                "id": "b",
                "text": "Vishing (voice phishing); report the call to the FTC",
                "correct": False,
                "rationale": (
                    "Incorrect. Vishing uses voice calls, not SMS messages. "
                    "This attack used a text message link — the defining "
                    "characteristic of smishing."
                ),
            },
            {
                "id": "c",
                "text": "A man-in-the-middle attack on the bank's servers; the bank is responsible for remediation",
                "correct": False,
                "rationale": (
                    "Incorrect. The attack targeted the user's credentials "
                    "through a fake link — a social engineering attack. "
                    "The bank's servers were not compromised; the user's "
                    "credentials were harvested via a fake site."
                ),
            },
            {
                "id": "d",
                "text": "Spyware installed via the link is monitoring all device activity; perform a factory reset",
                "correct": False,
                "rationale": (
                    "Incorrect. While a malicious link could install spyware, "
                    "the immediate confirmed damage is credential compromise "
                    "leading to unauthorized transactions. The priority is "
                    "credential revocation and bank notification, not "
                    "immediately assuming device compromise without evidence."
                ),
            },
        ],
        "explanation": (
            "Smishing (SMS phishing) is a CompTIA A+ listed attack type. "
            "Attackers spoof legitimate short codes or numbers and direct "
            "victims to credential-harvesting sites. Immediate response: "
            "1) change the compromised password from a verified clean device, "
            "2) notify the bank's fraud department, 3) enable MFA on the "
            "account, 4) review the linked site on the mobile device for "
            "any installed malware."
        ),
    },
    {
        "id": "c2d3v3-030",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A company issues iPhones to employees. An employee's device "
            "is reported lost. Before the device was lost, it was enrolled "
            "in the company's MDM solution. The device has a PIN set. "
            "Which action should the IT department take FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Issue a remote wipe command through the MDM console to erase all corporate data from the device",
                "correct": True,
                "rationale": (
                    "Correct. A lost corporate device with MDM enrollment "
                    "should be remotely wiped immediately to prevent "
                    "unauthorized access to corporate data. MDM remote "
                    "wipe is the primary and most effective first response "
                    "for a lost managed device."
                ),
            },
            {
                "id": "b",
                "text": "Wait 48 hours before acting in case the employee finds the device",
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting creates a window for data exposure. "
                    "Corporate policy and data protection standards require "
                    "immediate response to a lost device, not a wait period. "
                    "The remote wipe can be set up while searching for the "
                    "device."
                ),
            },
            {
                "id": "c",
                "text": "Change the employee's Active Directory password to prevent email access from the device",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing the AD password prevents new email "
                    "authentication but does not protect data already cached "
                    "on the device (contacts, emails, documents, corporate "
                    "apps). Remote wipe removes all data regardless of "
                    "cached credentials."
                ),
            },
            {
                "id": "d",
                "text": "Contact the carrier to suspend the SIM to prevent cellular usage",
                "correct": False,
                "rationale": (
                    "Incorrect. Suspending the SIM prevents cellular calls "
                    "and data but does not protect corporate data stored on "
                    "the device, which can still be accessed locally over "
                    "Wi-Fi or without any connectivity."
                ),
            },
        ],
        "explanation": (
            "Remote wipe via MDM is the CompTIA-recommended and industry-"
            "standard first response to a lost corporate mobile device. "
            "It removes all data (corporate and personal in a corporate "
            "wipe, or all data in a full wipe) and de-enrolls the device. "
            "MDM enrollment is specifically designed for this scenario."
        ),
    },
    {
        "id": "c2d3v3-031",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user's Android device shows unexpected outgoing calls to "
            "premium-rate international numbers that the user did not make. "
            "The calls occur at 3 AM when the user is asleep. The device "
            "is not rooted. No third-party app stores were used. Which "
            "explanation is MOST consistent with these symptoms?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A malicious app from the Play Store with excessive permissions is making calls autonomously to commit toll fraud",
                "correct": True,
                "rationale": (
                    "Correct. Toll fraud malware (dialers) can be embedded "
                    "in legitimate-appearing Play Store apps. Despite Play "
                    "Protect, such apps occasionally pass review. The "
                    "CALL_PHONE permission allows the app to place calls "
                    "without user interaction. Calls at consistent off-"
                    "hours are a pattern indicating automation, not user "
                    "action."
                ),
            },
            {
                "id": "b",
                "text": "The carrier's network is mis-routing calls from another subscriber through this SIM",
                "correct": False,
                "rationale": (
                    "Incorrect. Carrier routing errors would not result in "
                    "charges appearing on this account for calls made to "
                    "premium numbers. The charges on the account confirm "
                    "the calls originated from this SIM/device."
                ),
            },
            {
                "id": "c",
                "text": "SIM cloning is causing a duplicate SIM to make calls billed to this account",
                "correct": False,
                "rationale": (
                    "Incorrect. SIM cloning is rare with modern SIMs using "
                    "cryptographic authentication. Additionally, SIM cloning "
                    "would not explain app-permission patterns. The device "
                    "context (non-rooted, store-only apps) is more consistent "
                    "with a malicious app than SIM hardware compromise."
                ),
            },
            {
                "id": "d",
                "text": "The user is sleepwalking and making calls unconsciously",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not a valid technical explanation "
                    "for a repeating pattern of calls to specific premium "
                    "numbers at the same time nightly. Autonomous app "
                    "behavior is the technically consistent explanation."
                ),
            },
        ],
        "explanation": (
            "Toll fraud / dialer malware is a real Android threat. Apps "
            "with the CALL_PHONE permission can place calls without user "
            "interaction. Even Play Store apps have occasionally slipped "
            "through review with this behavior. Resolution: review app "
            "permissions in Settings > Apps, revoke CALL_PHONE from all "
            "non-dialer apps, uninstall suspicious apps, and scan with "
            "a mobile security tool."
        ),
    },
    {
        "id": "c2d3v3-032",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "An IT administrator discovers that several corporate Android "
            "phones have had their MDM profile silently removed. The devices "
            "are no longer in the MDM console. Investigation shows the "
            "devices were recently updated to a new Android version. "
            "Which TWO actions should IT take? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Re-enroll the devices in MDM and verify that the MDM device administrator privilege is granted and cannot be removed by users",
                "correct": True,
                "rationale": (
                    "Correct. After re-enrollment, IT should ensure the "
                    "MDM app is granted Device Administrator rights (or "
                    "the device is enrolled as a Device Owner) so users "
                    "cannot remove the MDM profile without a factory reset. "
                    "This prevents recurrence."
                ),
            },
            {
                "id": "b",
                "text": "Review the MDM console logs and the OS update release notes to determine if the update introduced a known MDM un-enrollment behavior",
                "correct": True,
                "rationale": (
                    "Correct. Some Android OS major version updates can "
                    "reset device administrator settings or alter MDM "
                    "profile behavior. Reviewing MDM logs and OS release "
                    "notes identifies whether this is a known issue with "
                    "a vendor-provided workaround."
                ),
            },
            {
                "id": "c",
                "text": "Block all future OS updates via MDM to prevent enrollment disruption",
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking all OS updates eliminates security "
                    "patches and creates greater long-term risk than the "
                    "enrollment disruption. Updates should be tested in "
                    "a pilot group before broad deployment, not blocked "
                    "entirely."
                ),
            },
            {
                "id": "d",
                "text": "Perform a factory reset on all affected devices and reissue them without MDM to avoid future enrollment issues",
                "correct": False,
                "rationale": (
                    "Incorrect. Issuing corporate devices without MDM "
                    "removes the primary security management layer. The "
                    "correct response is to fix the enrollment issue, "
                    "not abandon MDM."
                ),
            },
        ],
        "explanation": (
            "Android major version updates can disrupt MDM enrollment, "
            "especially if the MDM enrollment mode changed (e.g., legacy "
            "Device Administrator vs. Android Enterprise). IT should "
            "re-enroll with a robust enrollment mode (Device Owner / "
            "Work Profile), verify unenrollable protection, and check "
            "the MDM vendor's OS compatibility matrix for the new version."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.1 — Windows OS troubleshooting (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-033",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A technician runs 'gpupdate /force' on a Windows domain "
            "workstation but a required Group Policy setting still does "
            "not apply. Other machines on the same OU receive the policy "
            "correctly. Which command BEST diagnoses the problem on this "
            "specific workstation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "gpresult /r",
                "correct": True,
                "rationale": (
                    "Correct. gpresult /r (Resultant Set of Policy) shows "
                    "which GPOs were applied, which were filtered out, and "
                    "which encountered errors. On the affected machine it "
                    "will reveal if the specific policy is being applied, "
                    "filtered by security group, or blocked by WMI filter "
                    "— the most targeted diagnostic for a per-machine GPO "
                    "application failure."
                ),
            },
            {
                "id": "b",
                "text": "sfc /scannow",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC repairs OS file corruption; it does "
                    "not diagnose Group Policy application failures. A "
                    "GPO that applies on other machines but not this one "
                    "is a policy filtering or connectivity issue, not "
                    "a file corruption problem."
                ),
            },
            {
                "id": "c",
                "text": "netstat -an",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat shows network connections and open "
                    "ports. It does not diagnose Group Policy processing "
                    "or reveal which GPOs are or aren't being applied."
                ),
            },
            {
                "id": "d",
                "text": "eventvwr.msc — Application log",
                "correct": False,
                "rationale": (
                    "Incorrect. The Application log contains general app "
                    "events. GPO errors are recorded in the System log "
                    "and specifically in Applications and Services Logs > "
                    "Microsoft > Windows > Group Policy > Operational. "
                    "gpresult /r is still the more direct diagnostic tool."
                ),
            },
        ],
        "explanation": (
            "gpresult /r on the affected machine shows the Resultant Set "
            "of Policy — what applied, what was filtered (by security "
            "group membership, WMI filter, or loopback processing), and "
            "what errored. This pinpoints why a GPO that works for others "
            "is not applying to this specific workstation."
        ),
    },
    {
        "id": "c2d3v3-034",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows workstation shows a notification: 'Windows cannot "
            "access the specified device, path, or file. You may not have "
            "the appropriate permissions to access the item.' This error "
            "occurs for only one specific executable (.exe) that the user "
            "needs to run. The user is a standard user. IT has not "
            "restricted this file via GPO. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows Defender Application Control (WDAC) or AppLocker policy is blocking the executable",
                "correct": False,
                "rationale": (
                    "Incorrect. AppLocker/WDAC would produce a specific "
                    "'This app has been blocked by your system administrator' "
                    "message, not the generic access denied error. IT has "
                    "also confirmed no GPO restriction."
                ),
            },
            {
                "id": "b",
                "text": "The NTFS permissions on the executable file deny read or execute access to the user's account or group",
                "correct": True,
                "rationale": (
                    "Correct. 'Cannot access the specified device, path, "
                    "or file / may not have appropriate permissions' is "
                    "the Windows error message for NTFS permission denial. "
                    "A single file inaccessible to one (standard) user "
                    "while not GPO-restricted indicates specific NTFS "
                    "ACL settings on the file or its parent folder."
                ),
            },
            {
                "id": "c",
                "text": "The file requires elevation (Run as Administrator) to execute",
                "correct": False,
                "rationale": (
                    "Incorrect. A file requiring elevation produces a UAC "
                    "prompt, not an access denied error. UAC prompts standard "
                    "users for administrator credentials rather than refusing "
                    "access with a permissions error."
                ),
            },
            {
                "id": "d",
                "text": "The executable is corrupted and needs to be reinstalled",
                "correct": False,
                "rationale": (
                    "Incorrect. A corrupted executable would produce a "
                    "different error (application failed to initialize, "
                    "bad image, etc.). A permissions message specifically "
                    "indicates an access control issue, not file corruption."
                ),
            },
        ],
        "explanation": (
            "The Windows 'cannot access / may not have appropriate "
            "permissions' error directly indicates NTFS permission denial. "
            "Use icacls <filepath> to view the ACL, or right-click > "
            "Properties > Security tab to review effective permissions "
            "for the user's account. Adjust the ACL to grant Read & "
            "Execute to the appropriate user or group."
        ),
    },
    {
        "id": "c2d3v3-035",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 PC fails to print to a network printer that other "
            "workstations use successfully. The print spooler service is "
            "running. The printer shows as 'offline' on this PC only. "
            "pinging the printer's IP succeeds. Which is the MOST "
            "appropriate next diagnostic step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Delete and re-add the printer, then reinstall the print driver",
                "correct": True,
                "rationale": (
                    "Correct. A printer showing as 'offline' on one PC "
                    "when others can print — despite the print spooler "
                    "running and the device being pingable — indicates "
                    "a corrupt printer object or driver in the Windows "
                    "print subsystem on this machine. Removing and re-adding "
                    "the printer with a fresh driver installation resolves "
                    "this class of problem."
                ),
            },
            {
                "id": "b",
                "text": "Restart the print spooler service on the print server",
                "correct": False,
                "rationale": (
                    "Incorrect. Restarting the spooler on the print server "
                    "would affect all clients. Since other PCs print "
                    "successfully, the server-side spooler is functional. "
                    "The issue is isolated to this workstation's client-"
                    "side printer configuration."
                ),
            },
            {
                "id": "c",
                "text": "Replace the network cable on this workstation to fix packet loss causing the offline status",
                "correct": False,
                "rationale": (
                    "Incorrect. The ping test confirms network connectivity "
                    "to the printer is intact. A cable problem causing "
                    "packet loss sufficient to show the printer as offline "
                    "would also cause the ping to fail or show high latency."
                ),
            },
            {
                "id": "d",
                "text": "Check Windows Firewall rules to ensure port 9100 (RAW printing) is not blocked",
                "correct": False,
                "rationale": (
                    "Incorrect. Outbound port 9100 blocking by Windows "
                    "Firewall would produce a connection timeout error, not "
                    "an 'offline' printer status. The offline status in the "
                    "Windows print subsystem when the device is pingable "
                    "points to a driver or printer object issue, not a "
                    "firewall rule."
                ),
            },
        ],
        "explanation": (
            "Network printer 'offline' on one PC when others print "
            "successfully, with the printer pingable, is a client-side "
            "print driver or printer object corruption issue. Fix: Devices "
            "and Printers > right-click printer > Remove > re-add with "
            "fresh driver from the print server or manufacturer. If the "
            "spooler crashes during reinstall, clear the spooler queue "
            "files from %SystemRoot%\\System32\\spool\\PRINTERS\\ first."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.3 — Malware removal best-practice process (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-036",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician discovers that a Windows PC on a segmented VLAN "
            "is infected with malware that propagates over the network. "
            "The VLAN is shared by 10 other workstations and a file server. "
            "Applying CompTIA's malware removal best practices, which TWO "
            "quarantine actions should be taken before ANY local remediation? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disconnect the infected workstation from the network switch port",
                "correct": True,
                "rationale": (
                    "Correct. Physical or logical disconnection of the "
                    "infected machine from the network (quarantine — step 2) "
                    "is mandatory before any local remediation. The VLAN "
                    "segmentation reduces blast radius but does not substitute "
                    "for isolating the infected machine."
                ),
            },
            {
                "id": "b",
                "text": "Notify affected stakeholders and document the incident before beginning quarantine",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation and notification are important "
                    "but do not precede quarantine. Active network-spreading "
                    "malware can infect additional machines in seconds; "
                    "isolation must happen immediately."
                ),
            },
            {
                "id": "c",
                "text": "Scan the other 10 workstations and the file server for signs of infection",
                "correct": True,
                "rationale": (
                    "Correct. With a network-propagating threat, the scope "
                    "of infection must be assessed immediately. Scanning "
                    "other VLAN members identifies any additional infected "
                    "systems requiring quarantine before they spread further."
                ),
            },
            {
                "id": "d",
                "text": "Run anti-malware definitions update and scan on the infected PC immediately",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning before quarantine (while the machine "
                    "is still networked) allows continued propagation during "
                    "the scan. Quarantine and scope assessment must precede "
                    "local remediation on the infected machine."
                ),
            },
        ],
        "explanation": (
            "For network-spreading malware, quarantine has two dimensions: "
            "1) isolate the confirmed infected machine (physical disconnect "
            "or VLAN isolation), and 2) assess scope by scanning other "
            "machines on the same segment. Both happen before local "
            "remediation begins. Only after all infected machines are "
            "identified and isolated does the per-machine 7-step process "
            "begin."
        ),
    },
    {
        "id": "c2d3v3-037",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician is at step 4 of the malware removal process "
            "and needs to scan a Windows PC with anti-malware software. "
            "The machine has no network access (quarantined). The installed "
            "anti-malware definitions are 45 days old. The technician has "
            "a USB drive. Which is the BEST approach to update definitions "
            "before scanning?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Temporarily reconnect the machine to the network for the 2 minutes needed to download updates",
                "correct": False,
                "rationale": (
                    "Incorrect. Reconnecting a quarantined machine to the "
                    "network — even briefly — violates the quarantine and "
                    "risks spreading the malware further. Definitions must "
                    "be obtained without breaking isolation."
                ),
            },
            {
                "id": "b",
                "text": "Download the offline definition update package on a clean machine, transfer it to the USB drive, and install on the quarantined machine",
                "correct": True,
                "rationale": (
                    "Correct. CompTIA's step 4 specifies updating definitions "
                    "before scanning. Offline update packages (available from "
                    "all major AV vendors) allow definition updates without "
                    "network connectivity, maintaining quarantine while "
                    "ensuring the scanner can detect current malware."
                ),
            },
            {
                "id": "c",
                "text": "Scan with the 45-day-old definitions; modern anti-malware heuristics compensate for outdated signatures",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning with 45-day-old definitions risks "
                    "missing newer malware variants. CompTIA explicitly "
                    "requires updating definitions before scanning as part "
                    "of step 4. Heuristics are supplementary, not a "
                    "replacement for current signatures."
                ),
            },
            {
                "id": "d",
                "text": "Skip definition updates; boot from a bootable AV USB that has its own built-in current signatures",
                "correct": False,
                "rationale": (
                    "Incorrect. A bootable AV environment is a valid scanning "
                    "technique, but the question specifically addresses "
                    "updating definitions before scanning. If the bootable "
                    "AV has outdated definitions, the same gap exists. The "
                    "correct practice is to ensure definitions are current "
                    "via offline update."
                ),
            },
        ],
        "explanation": (
            "Maintaining quarantine while updating definitions requires "
            "offline update packages. All major vendors (Microsoft, "
            "Malwarebytes, etc.) provide standalone definition installers "
            "that can be downloaded on a clean machine and transferred "
            "via USB. This maintains isolation while satisfying the "
            "step 4 requirement to update before scanning."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.2 — PC security issue troubleshooting (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-038",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user reports that their Windows PC's CPU runs at 90–100% "
            "constantly even when no user applications are open. Task Manager "
            "shows a process called 'XMRig.exe' consuming all CPU cycles. "
            "The process is not found in the application list — only in the "
            "Details tab. What type of malware is this, and what is the "
            "BEST first response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Cryptominer malware (cryptocurrency mining); quarantine the machine and begin the 7-step malware removal process",
                "correct": True,
                "rationale": (
                    "Correct. XMRig is a well-known open-source "
                    "cryptocurrency mining application commonly deployed "
                    "by malware as a cryptominer (cryptojacking). High CPU "
                    "usage from a non-user-initiated background process is "
                    "a CompTIA-listed PC security symptom. Quarantine and "
                    "the 7-step removal process are the correct response."
                ),
            },
            {
                "id": "b",
                "text": "Windows Update service running an intensive optimization task; wait for it to complete",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Update processes run under "
                    "TiWorker.exe, wuauclt.exe, or svchost.exe — not "
                    "XMRig.exe. XMRig is a publicly known mining tool "
                    "with no legitimate Windows Update association."
                ),
            },
            {
                "id": "c",
                "text": "A legitimate background optimization tool installed by the OEM; check the manufacturer's website",
                "correct": False,
                "rationale": (
                    "Incorrect. No OEM ships XMRig.exe as a legitimate "
                    "optimization tool. XMRig is open-source mining software "
                    "used exclusively for cryptocurrency mining — its "
                    "presence on a corporate or personal PC without user "
                    "installation is definitive malware evidence."
                ),
            },
            {
                "id": "d",
                "text": "A virus scanning its own process files; end the task and restart Windows Defender",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Defender processes are named "
                    "MsMpEng.exe, not XMRig.exe. Ending XMRig without "
                    "following the full malware removal process will only "
                    "provide temporary relief — the malware will restart "
                    "via its persistence mechanism."
                ),
            },
        ],
        "explanation": (
            "Cryptomining malware (cryptojackers) hijack the victim's CPU "
            "to mine cryptocurrency for the attacker. XMRig is one of the "
            "most common tools deployed. High unexplained CPU usage is a "
            "CompTIA PC security symptom. Remediation: quarantine, follow "
            "7-step removal, check startup entries and scheduled tasks "
            "for persistence, and patch the vulnerability that allowed "
            "the installation."
        ),
    },
    {
        "id": "c2d3v3-039",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A Windows workstation that was recently reimaged suddenly "
            "exhibits signs of reinfection — the same malware indicators "
            "reappear within hours of the clean image deployment. No "
            "software has been installed by the user. The machine rejoined "
            "the domain after reimaging. Which is the MOST likely "
            "explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The master image used for reimaging was infected before deployment",
                "correct": False,
                "rationale": (
                    "Incorrect. If the master image were infected, all "
                    "machines reimaged from it would show the same symptoms. "
                    "The question implies only this machine is affected."
                ),
            },
            {
                "id": "b",
                "text": "A Group Policy or login script on the domain is re-deploying the malware from a compromised network share",
                "correct": True,
                "rationale": (
                    "Correct. Rapid reinfection after reimaging when domain "
                    "is rejoined suggests the infection vector is domain-"
                    "based — a compromised Group Policy startup script, "
                    "login script, or mapped drive with autorun that "
                    "re-executes malware on domain join or login. The "
                    "domain infrastructure must be investigated."
                ),
            },
            {
                "id": "c",
                "text": "The BIOS/UEFI firmware is infected and persists through OS reinstalls",
                "correct": False,
                "rationale": (
                    "Incorrect. UEFI-resident malware exists but is extremely "
                    "rare and would not depend on domain rejoin. The "
                    "correlation between domain rejoin and rapid reinfection "
                    "strongly implicates a domain-based delivery mechanism."
                ),
            },
            {
                "id": "d",
                "text": "The hard drive's HPA (Host Protected Area) contains malware that survives reimaging",
                "correct": False,
                "rationale": (
                    "Incorrect. HPA-based malware is theoretically possible "
                    "but extremely rare. More importantly, it would not "
                    "explain why reinfection correlates with domain rejoin "
                    "rather than occurring immediately at first boot."
                ),
            },
        ],
        "explanation": (
            "Reinfection after reimaging that occurs upon domain rejoin is "
            "the classic indicator of a domain-side infection vector: "
            "compromised login scripts, GPO startup scripts, or infected "
            "SYSVOL/NETLOGON shares. Investigate the domain controller's "
            "SYSVOL, Group Policy startup scripts, and any login scripts "
            "that run on this OU before reimaging additional machines."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.4 — Mobile OS troubleshooting (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-040",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone shows 'Unfortunately, Settings has "
            "stopped' whenever they open the Settings app. Other apps "
            "work normally. The error began after sideloading an app. "
            "A force stop and clear cache of the Settings app does not "
            "resolve it. Which is the BEST next step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clear the data (not just cache) of the Settings app and reboot",
                "correct": False,
                "rationale": (
                    "Incorrect. The Settings app on Android is a system "
                    "app that does not store user data in the traditional "
                    "sense — clearing its data would reset some preferences "
                    "but would not resolve malware interference from the "
                    "sideloaded app."
                ),
            },
            {
                "id": "b",
                "text": "Uninstall the sideloaded app and check if the Settings crash resolves",
                "correct": True,
                "rationale": (
                    "Correct. The Settings crash began after sideloading "
                    "an app. The sideloaded app may have requested or "
                    "abused system-level permissions that interfere with "
                    "the Settings process. Uninstalling the correlation "
                    "trigger is the correct targeted first action."
                ),
            },
            {
                "id": "c",
                "text": "Update Android OS to the latest version to patch the Settings app bug",
                "correct": False,
                "rationale": (
                    "Incorrect. The crash is correlated with a specific "
                    "sideloaded app install, not an OS bug. An OS update "
                    "does not address interference from a third-party app "
                    "with system-level permissions."
                ),
            },
            {
                "id": "d",
                "text": "Use Safe Mode to verify the issue, then perform a factory reset",
                "correct": False,
                "rationale": (
                    "Incorrect. Booting into Safe Mode (which disables "
                    "third-party apps) to confirm whether Settings works "
                    "is a valid diagnostic step, but factory reset should "
                    "not be the direct next step. Uninstalling the "
                    "sideloaded app first is less destructive."
                ),
            },
        ],
        "explanation": (
            "When a system app crash (Settings) appears immediately after "
            "installing a specific third-party app, the installed app is "
            "the suspect. Uninstalling it first is the least destructive "
            "targeted action. If the crash persists after uninstall, "
            "boot into Android Safe Mode — if Settings works in Safe Mode, "
            "another third-party app is the cause. Factory reset is the "
            "last resort."
        ),
    },
    {
        "id": "c2d3v3-041",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's iPhone shows 'iPhone is disabled, connect to iTunes' "
            "after entering the wrong passcode too many times. The user "
            "has never set up Face ID and does not remember their Apple ID "
            "password. iCloud Find My is enabled on the device. Which "
            "recovery method is available?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use the iCloud website's Erase iPhone feature via a browser on another device to erase and restore the phone",
                "correct": True,
                "rationale": (
                    "Correct. When Find My is enabled, iCloud.com > Find "
                    "My > Erase iPhone performs a remote erase that removes "
                    "the lock. After erasure, the device can be set up as "
                    "new or restored from backup. This works even without "
                    "knowing the Apple ID password if the user can reset "
                    "it via recovery email/phone."
                ),
            },
            {
                "id": "b",
                "text": "Enter Recovery Mode (hold Volume Down + Side button) and restore via Finder without an Apple ID",
                "correct": False,
                "rationale": (
                    "Incorrect. When Find My is enabled on an iPhone, "
                    "Activation Lock requires the Apple ID credentials "
                    "to complete a restore — even in Recovery Mode via "
                    "Finder/iTunes. Without the Apple ID, the device will "
                    "prompt for credentials after restore and remain locked."
                ),
            },
            {
                "id": "c",
                "text": "Contact Apple Support to bypass Activation Lock without the Apple ID",
                "correct": False,
                "rationale": (
                    "Incorrect. Apple Support requires proof of purchase "
                    "and the Apple ID credentials or account recovery to "
                    "address Activation Lock. They do not bypass it without "
                    "ownership verification. The iCloud erase path is "
                    "the self-service option."
                ),
            },
            {
                "id": "d",
                "text": "Remove the SIM card and restore the phone via iTunes without activating Find My",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing the SIM does not disable Find My "
                    "or Activation Lock. Activation Lock is tied to the "
                    "Apple ID account, not the SIM, and persists regardless "
                    "of cellular connectivity."
                ),
            },
        ],
        "explanation": (
            "An iPhone disabled by wrong passcode attempts with Find My "
            "enabled can be recovered via iCloud.com > Find My > Erase "
            "iPhone (requires signing into the Apple ID on a browser). "
            "After erasing, setup restarts clean. If the Apple ID password "
            "is forgotten, it must be reset via the account recovery process "
            "before the iCloud erase path is available."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.5 — Mobile app security troubleshooting (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-042",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "An employee reports that after connecting their personal Android "
            "phone to a public USB charging kiosk at an airport, the phone "
            "displayed a prompt asking 'Allow USB debugging?' which they "
            "dismissed. Later, they noticed unfamiliar apps installed. "
            "Which attack technique does this BEST describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Juice jacking — a malicious USB charging station that attempted to establish ADB access to install apps",
                "correct": True,
                "rationale": (
                    "Correct. Juice jacking uses malicious USB charging "
                    "stations that carry data lines, not just power. The "
                    "USB debugging prompt is the ADB authorization request "
                    "— the attacker's station attempted to use ADB to "
                    "install apps. Despite the dismissal, if the device "
                    "was previously in developer mode or if the dismissal "
                    "was accidentally confirmed, app installation is possible."
                ),
            },
            {
                "id": "b",
                "text": "Bluebugging — a Bluetooth attack that installed apps via the Bluetooth interface",
                "correct": False,
                "rationale": (
                    "Incorrect. Bluebugging exploits Bluetooth and does not "
                    "involve USB connections or USB debugging prompts. The "
                    "attack vector here is explicitly a USB charging kiosk."
                ),
            },
            {
                "id": "c",
                "text": "Evil twin Wi-Fi — a rogue access point pushed app updates via OTA",
                "correct": False,
                "rationale": (
                    "Incorrect. An evil twin attack targets Wi-Fi traffic, "
                    "not USB connections. The airport kiosk USB connection "
                    "and the ADB debugging prompt are the defining indicators "
                    "of a USB-based attack."
                ),
            },
            {
                "id": "d",
                "text": "Shoulder surfing — someone observed the unlock pattern and installed apps manually",
                "correct": False,
                "rationale": (
                    "Incorrect. Shoulder surfing is a physical observation "
                    "technique. The automated ADB debugging prompt appearing "
                    "upon connection to the kiosk is a technical indicator "
                    "of an automated attack, not a human manually observing "
                    "and entering the device."
                ),
            },
        ],
        "explanation": (
            "Juice jacking uses modified USB charging stations with active "
            "data lines to attempt ADB connections to connected Android "
            "devices. Best practice: use only power-only USB cables (no "
            "data pins) or carry a portable battery pack when in public. "
            "Disable USB debugging when not needed. The 'Allow USB "
            "debugging?' prompt is the ADB authorization handshake — "
            "always deny it at untrusted connections."
        ),
    },
    {
        "id": "c2d3v3-043",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A security-conscious employee notices their corporate iPhone "
            "can install apps from outside the App Store without any "
            "jailbreak. The IT department is unaware of this capability. "
            "Apps installed this way bypass App Store review. Which "
            "feature or configuration MOST likely explains this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "TestFlight is installed and the device is enrolled in a test program distributing unapproved apps",
                "correct": False,
                "rationale": (
                    "Incorrect. TestFlight requires explicit developer/tester "
                    "enrollment and app-specific invitations. It does not "
                    "allow arbitrary app installation from any source and "
                    "Apple still reviews TestFlight builds."
                ),
            },
            {
                "id": "b",
                "text": "An MDM configuration profile has been installed that trusts an enterprise certificate, enabling side-loading of enterprise-signed apps",
                "correct": True,
                "rationale": (
                    "Correct. iOS allows enterprises to distribute apps "
                    "outside the App Store using Apple's Enterprise Developer "
                    "Program and a provisioning profile installed via MDM "
                    "or manual profile install. A malicious actor or "
                    "unauthorized party installing such a profile allows "
                    "arbitrary enterprise-signed IPAs to be installed, "
                    "bypassing App Store review entirely."
                ),
            },
            {
                "id": "c",
                "text": "The device is running a beta version of iOS that has App Store restrictions disabled",
                "correct": False,
                "rationale": (
                    "Incorrect. iOS beta versions do not disable App Store "
                    "restrictions or enable arbitrary app sideloading. "
                    "Beta iOS requires a developer profile but does not "
                    "allow unsigned or enterprise-signed apps without an "
                    "enterprise certificate."
                ),
            },
            {
                "id": "d",
                "text": "Screen Time restrictions have been misconfigured to allow all app installations",
                "correct": False,
                "rationale": (
                    "Incorrect. Screen Time controls app purchases and age "
                    "ratings within the App Store ecosystem. It does not "
                    "control iOS's code-signing enforcement or enable "
                    "sideloading of unsigned or enterprise-signed apps."
                ),
            },
        ],
        "explanation": (
            "Apple's Enterprise Developer Program allows organizations to "
            "distribute in-house apps via provisioning profiles without "
            "App Store review. However, if an attacker or unauthorized "
            "party installs an enterprise certificate profile on a device, "
            "it enables sideloading of any IPA signed by that certificate. "
            "IT should audit all installed configuration profiles "
            "(Settings > General > VPN & Device Management) and remove "
            "unauthorized profiles."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.1 — Windows boot troubleshooting (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-044",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A Windows 10 workstation displays the message 'We couldn't "
            "complete the updates. Undoing changes. Don't turn off your "
            "computer' and then reboots back into the same message in a "
            "loop. Normal boot fails. Which is the BEST resolution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Boot into WinRE and use Startup Repair to detect and resolve the failed update loop",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Startup Repair addresses boot record "
                    "and driver issues, not failed Windows Update rollback "
                    "loops. It would not specifically resolve a stuck update "
                    "rollback cycle."
                ),
            },
            {
                "id": "b",
                "text": "Boot into WinRE > Command Prompt, then use DISM to uninstall the pending update package that is causing the rollback loop",
                "correct": True,
                "rationale": (
                    "Correct. The update rollback loop occurs when Windows "
                    "cannot complete or roll back a pending update. From "
                    "WinRE Command Prompt, 'dism /image:C:\\ /get-packages' "
                    "lists packages and 'dism /image:C:\\ /remove-package' "
                    "removes the stuck package offline, breaking the loop."
                ),
            },
            {
                "id": "c",
                "text": "Run bootrec /fixboot and bootrec /rebuildbcd from WinRE",
                "correct": False,
                "rationale": (
                    "Incorrect. bootrec commands address missing or corrupt "
                    "boot records and BCD entries, not a Windows Update "
                    "package stuck in a rollback state. The boot record "
                    "is functional — the OS loads far enough to attempt "
                    "the update rollback."
                ),
            },
            {
                "id": "d",
                "text": "Restore the workstation from a backup image taken before the update",
                "correct": False,
                "rationale": (
                    "Incorrect. Image restore is a valid last resort but "
                    "is more disruptive than using DISM to remove the "
                    "specific failing update package. The package removal "
                    "approach preserves all other OS state and data."
                ),
            },
        ],
        "explanation": (
            "A Windows Update rollback loop is resolved offline via DISM: "
            "1) WinRE > Command Prompt 2) dism /image:C:\\ /get-packages "
            "| find 'Pending' to identify the stuck package 3) dism "
            "/image:C:\\ /remove-package /packagename:<name> 4) Reboot. "
            "This removes the problematic update without requiring an "
            "image restore."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.2 — Browser security symptoms (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-045",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security symptoms",
        "stem": (
            "A user's browser shows their banking site with a valid padlock, "
            "but when they log in, their credentials are stolen. The user's "
            "PC hosts file has been modified to map the banking domain to "
            "a malicious IP that serves a certificate issued by a CA that "
            "was secretly installed in the machine's Trusted Root store. "
            "Which attack technique BEST describes this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Pharming — DNS/hosts file poisoning combined with a rogue certificate to present a convincing fake site",
                "correct": True,
                "rationale": (
                    "Correct. Pharming redirects users to fraudulent sites "
                    "by poisoning the hosts file or DNS, while a rogue CA "
                    "certificate in the Trusted Root store allows the fake "
                    "site to present a valid-appearing padlock. The user "
                    "sees no browser warning and believes the site is "
                    "legitimate — a sophisticated phishing variant."
                ),
            },
            {
                "id": "b",
                "text": "SQL injection — the attacker modified the banking database to insert a redirect",
                "correct": False,
                "rationale": (
                    "Incorrect. SQL injection targets server-side databases "
                    "to extract or manipulate data. It does not involve "
                    "hosts file modification or rogue certificate installation "
                    "on the client machine."
                ),
            },
            {
                "id": "c",
                "text": "Session hijacking — the attacker stole an active session cookie",
                "correct": False,
                "rationale": (
                    "Incorrect. Session hijacking steals an existing "
                    "authenticated session token. The scenario describes "
                    "credential harvesting via a fake site before login "
                    "— there is no existing session to hijack."
                ),
            },
            {
                "id": "d",
                "text": "Typosquatting — the user mistyped the banking URL and landed on a similar domain",
                "correct": False,
                "rationale": (
                    "Incorrect. Typosquatting requires the user to type "
                    "an incorrect URL. The scenario specifies the hosts "
                    "file was modified, meaning the user typed the correct "
                    "URL but was silently redirected — this is hosts-based "
                    "pharming."
                ),
            },
        ],
        "explanation": (
            "Pharming via hosts file poisoning + rogue CA is a sophisticated "
            "attack that defeats URL inspection and certificate verification. "
            "Detection: check the hosts file for non-localhost entries, "
            "inspect the Trusted Root CA store for unauthorized CAs, and "
            "verify the IP the browser connected to matches the legitimate "
            "bank's IP. Remediation: restore the hosts file, remove rogue "
            "CAs, and follow the full malware removal process."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.1 — Windows OS troubleshooting (continued)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v3-046",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 11 workstation fails to connect to domain shares "
            "after a password change. The user receives 'The credentials "
            "supplied are not sufficient to access this resource.' Local "
            "applications work. Other domain users on the same PC can "
            "connect to shares without issues. Which is the MOST targeted "
            "resolution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clear the Windows Credential Manager entries for the file server and re-authenticate with the new password",
                "correct": True,
                "rationale": (
                    "Correct. Windows Credential Manager caches network "
                    "credentials. After a password change, the cached old "
                    "credentials for the file server cause authentication "
                    "failures. Clearing the cached entry for the server in "
                    "Credential Manager (Control Panel > Credential Manager "
                    "> Windows Credentials) forces re-authentication with "
                    "the new password."
                ),
            },
            {
                "id": "b",
                "text": "Disjoin and rejoin the workstation to the domain",
                "correct": False,
                "rationale": (
                    "Incorrect. Domain (re)join is a drastic action not "
                    "warranted for a cached credential issue. Other users "
                    "on the same machine connecting fine confirms the domain "
                    "trust is healthy — the issue is user-specific cached "
                    "credentials."
                ),
            },
            {
                "id": "c",
                "text": "Reset the user's Active Directory password again to force a new Kerberos ticket",
                "correct": False,
                "rationale": (
                    "Incorrect. The user's new password is correct — the "
                    "problem is that the old password is cached locally. "
                    "Resetting the AD password again does not clear the "
                    "local Credential Manager cache."
                ),
            },
            {
                "id": "d",
                "text": "Add the user account to the local Administrators group to bypass share permissions",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding to the local Admins group does not "
                    "fix stale Kerberos/NTLM credentials cached in "
                    "Credential Manager and is an inappropriate privilege "
                    "escalation solution for a credential caching problem."
                ),
            },
        ],
        "explanation": (
            "After a domain password change, Windows Credential Manager "
            "retains old cached credentials for network resources. These "
            "cached credentials cause authentication failures (error 1326 / "
            "'credentials not sufficient') until cleared. Control Panel > "
            "Credential Manager > Windows Credentials > find the server "
            "entry > Remove > then re-access the share to prompt for the "
            "new password."
        ),
    },
    {
        "id": "c2d3v3-047",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 workstation has been running continuously for "
            "45 days without a reboot. Users report increasing memory "
            "usage over time, applications become unresponsive after "
            "several days, but performance recovers after a reboot. "
            "Which TWO actions BEST address this systematic problem? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use Resource Monitor or a memory leak detection tool to identify the process with a steadily increasing private bytes count",
                "correct": True,
                "rationale": (
                    "Correct. Progressively increasing memory usage over "
                    "days that resolves on reboot is a classic memory leak. "
                    "Resource Monitor (private bytes column in the Memory "
                    "tab) or tools like RAMMap identify which process is "
                    "consuming memory without releasing it, enabling targeted "
                    "remediation (vendor patch, service restart schedule)."
                ),
            },
            {
                "id": "b",
                "text": "Add more physical RAM to increase the memory available to the leaking process",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding RAM delays the problem but does not "
                    "fix a memory leak. The root cause (a process not "
                    "releasing memory) must be identified and addressed "
                    "at the software level."
                ),
            },
            {
                "id": "c",
                "text": "Schedule a weekly maintenance reboot via Task Scheduler to prevent the memory exhaustion from impacting users",
                "correct": True,
                "rationale": (
                    "Correct. While identifying and patching the leaking "
                    "application is the permanent fix, scheduling a "
                    "maintenance reboot is an accepted interim workaround "
                    "that prevents the leak from reaching a user-impacting "
                    "level while the root-cause investigation and vendor "
                    "patch are pursued."
                ),
            },
            {
                "id": "d",
                "text": "Increase the Windows virtual memory (pagefile) size to accommodate the growing memory demand",
                "correct": False,
                "rationale": (
                    "Incorrect. Expanding the pagefile delays symptom onset "
                    "but does not fix the leak — it just moves the point "
                    "of failure to disk thrashing (100% disk on the pagefile "
                    "drive) rather than RAM exhaustion. Root-cause analysis "
                    "and a maintenance reboot schedule are the correct "
                    "actions."
                ),
            },
        ],
        "explanation": (
            "Progressive memory consumption over days with post-reboot "
            "recovery is a memory leak pattern. Two appropriate actions: "
            "1) Diagnose with Resource Monitor / RAMMap to identify the "
            "offending process (private bytes growing without plateau), "
            "enabling a vendor bug report and patch. 2) Interim mitigation "
            "via scheduled weekly reboot to maintain system stability while "
            "awaiting the fix."
        ),
    },
]

