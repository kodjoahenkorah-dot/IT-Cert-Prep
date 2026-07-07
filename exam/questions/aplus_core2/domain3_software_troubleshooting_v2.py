"""
CompTIA A+ Core 2 (220-1202) — Domain 3: Software Troubleshooting
37 NEW practice questions covering objectives 3.1 – 3.5. (v2)
"""

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 3.3 — Malware removal best-practice process  (7 questions)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v2-001",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician is working through CompTIA's seven-step malware "
            "removal process. The system has been quarantined and System "
            "Restore has been disabled. The technician is about to scan "
            "with anti-malware software. According to the process, which "
            "sub-task must be completed BEFORE launching the scan?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Update anti-malware definitions to the latest version",
                "correct": True,
                "rationale": (
                    "Correct. Step 4 begins with updating anti-malware "
                    "definitions so the scanner can detect the most current "
                    "malware variants. Running a scan with stale definitions "
                    "risks missing recently released malware that may be "
                    "responsible for the infection."
                ),
            },
            {
                "id": "b",
                "text": "Re-enable System Restore and create a clean restore point",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore is re-enabled in step 6, "
                    "after scanning and remediation are complete. Re-enabling "
                    "it before scanning would allow malware to persist inside "
                    "shadow copies, potentially reinfecting the system."
                ),
            },
            {
                "id": "c",
                "text": "Educate the end user about the infection vector",
                "correct": False,
                "rationale": (
                    "Incorrect. User education is step 7, the final step "
                    "of the process, performed only after the system has "
                    "been fully cleaned, hardened, and restore points have "
                    "been re-established."
                ),
            },
            {
                "id": "d",
                "text": "Schedule recurring anti-malware scans before the on-demand scan",
                "correct": False,
                "rationale": (
                    "Incorrect. Scheduling recurring scans is part of step 5. "
                    "The first on-demand remediation scan (step 4) must be "
                    "completed before scheduling ongoing scans."
                ),
            },
        ],
        "explanation": (
            "Step 4 of the CompTIA malware removal process (Remediate) "
            "requires updating anti-malware definitions first, then scanning "
            "— preferably in safe mode or a preinstallation environment. "
            "Up-to-date definitions are critical; outdated definitions will "
            "miss newer variants that may be exactly what infected the system."
        ),
    },
    {
        "id": "c2d3v2-002",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician notices that a workstation infected with a rootkit "
            "consistently passes anti-malware scans run from within the "
            "running Windows OS but symptoms persist. Which change to the "
            "scanning approach, prescribed in step 4 of the CompTIA malware "
            "removal process, would MOST likely detect the rootkit?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Boot into a preinstallation environment (Windows PE) and scan from there",
                "correct": True,
                "rationale": (
                    "Correct. Rootkits hook into the running OS kernel to "
                    "hide their files and processes from scanners. Step 4 "
                    "explicitly recommends scanning from safe mode or a "
                    "preinstallation environment (WinPE) because these "
                    "environments load a different kernel where the rootkit "
                    "hooks are not active, allowing the scanner to see "
                    "the malicious files directly."
                ),
            },
            {
                "id": "b",
                "text": "Run the scan with administrator privileges in the normal Windows desktop",
                "correct": False,
                "rationale": (
                    "Incorrect. Rootkits operate at ring-0 (kernel level), "
                    "above administrator privilege. Running the scanner "
                    "as admin within the infected OS still allows the rootkit "
                    "to intercept file-system calls and hide from the scanner."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow first to expose the hidden rootkit files",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC /scannow checks Windows-protected system "
                    "files against known-good hashes but uses the running "
                    "OS APIs, which a rootkit can intercept. SFC would not "
                    "reliably expose kernel-level rootkit components."
                ),
            },
            {
                "id": "d",
                "text": "Install a second anti-malware product and run concurrent scans",
                "correct": False,
                "rationale": (
                    "Incorrect. Multiple scanners running within the same "
                    "infected OS are all subject to the same rootkit hooks. "
                    "Two compromised scanners do not equal one clean one. "
                    "The OS isolation approach is what matters."
                ),
            },
        ],
        "explanation": (
            "Rootkits intercept OS-level calls to hide from scanners running "
            "within the infected OS. The CompTIA step-4 guidance to scan from "
            "safe mode or a preinstallation environment (WinPE boot disk) "
            "bypasses the rootkit's hooks because a different, uninfected "
            "kernel is used, giving the scanner unobstructed file-system access."
        ),
    },
    {
        "id": "c2d3v2-003",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician completes an anti-malware scan in step 4 and "
            "confirms no threats remain. The machine is reconnected to the "
            "network. According to CompTIA's seven-step malware removal "
            "process, what is the correct NEXT step (step 5)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Schedule future scans and apply all pending OS and application updates",
                "correct": True,
                "rationale": (
                    "Correct. Step 5 is to schedule scans and run updates. "
                    "This includes setting up recurring anti-malware scans "
                    "and ensuring the OS and applications are fully patched "
                    "to close vulnerabilities that were exploited during "
                    "the infection."
                ),
            },
            {
                "id": "b",
                "text": "Re-enable System Restore and create a restore point immediately",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-enabling System Restore is step 6, which "
                    "comes after scheduling scans and running updates (step 5). "
                    "Reversing these steps skips important hardening before "
                    "capturing a 'clean' restore point."
                ),
            },
            {
                "id": "c",
                "text": "Educate the end user about how to avoid future infections",
                "correct": False,
                "rationale": (
                    "Incorrect. End-user education is step 7 — the final step. "
                    "At this point in the process, the system still needs "
                    "updates and a new restore point before the interaction "
                    "with the user concludes."
                ),
            },
            {
                "id": "d",
                "text": "Quarantine the system again to verify no reinfection occurred",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine (step 2) is performed at the "
                    "beginning of the process. After confirmed clean "
                    "remediation, the machine is reconnected; re-quarantining "
                    "at step 5 contradicts the process flow."
                ),
            },
        ],
        "explanation": (
            "CompTIA's seven steps: 1) Investigate and verify symptoms, "
            "2) Quarantine, 3) Disable System Restore, 4) Remediate "
            "(update definitions, scan), 5) Schedule scans and run updates, "
            "6) Re-enable System Restore and create a restore point, "
            "7) Educate end user. Step 5 closes the vulnerability window "
            "by patching the system before creating a new baseline."
        ),
    },
    {
        "id": "c2d3v2-004",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A user reports popup ads appearing in the browser and a new "
            "toolbar the user did not install. Anti-malware reports the "
            "system is clean. The technician investigates further and "
            "confirms an adware-bundled freeware installation three days "
            "ago. Which step of the malware removal process is the "
            "technician currently performing?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Step 1 — Investigate and verify malware symptoms",
                "correct": True,
                "rationale": (
                    "Correct. Step 1 involves identifying and verifying that "
                    "the observed symptoms (popups, unwanted toolbar) are "
                    "indeed caused by malware or a PUP. Correlating the "
                    "symptoms with the recent freeware install confirms the "
                    "infection before proceeding to quarantine."
                ),
            },
            {
                "id": "b",
                "text": "Step 4 — Remediate the infected system",
                "correct": False,
                "rationale": (
                    "Incorrect. Remediation (step 4) involves running scans "
                    "to remove the threat. The technician is still in the "
                    "investigation phase, correlating symptoms with a likely "
                    "cause — that is step 1."
                ),
            },
            {
                "id": "c",
                "text": "Step 7 — Educate the end user",
                "correct": False,
                "rationale": (
                    "Incorrect. User education is the final step after "
                    "remediation is complete. The technician has not yet "
                    "quarantined or cleaned the system."
                ),
            },
            {
                "id": "d",
                "text": "Step 3 — Disable System Restore",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore is disabled in step 3 after "
                    "quarantine (step 2). The technician is still investigating "
                    "the cause of symptoms, which is step 1."
                ),
            },
        ],
        "explanation": (
            "Step 1 of the CompTIA malware removal process is to 'Identify "
            "and verify malware symptoms.' The technician is linking popup "
            "ads and an unauthorized toolbar to a recent freeware install — "
            "this is the investigation and verification work of step 1 before "
            "quarantine and remediation begin."
        ),
    },
    {
        "id": "c2d3v2-005",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician is at step 2 (Quarantine) of the malware removal "
            "process. Which TWO actions correctly implement this step? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Disconnect the workstation's network cable and disable Wi-Fi",
                "correct": True,
                "rationale": (
                    "Correct. Network disconnection — physical and wireless — "
                    "isolates the infected system, preventing lateral movement "
                    "to other machines and stopping command-and-control "
                    "communications. This is the core action of step 2."
                ),
            },
            {
                "id": "b",
                "text": "Notify IT management or document the infection per the incident response plan",
                "correct": True,
                "rationale": (
                    "Correct. CompTIA's quarantine step also includes notifying "
                    "appropriate personnel and documenting the incident. This "
                    "ensures organizational awareness and preserves evidence "
                    "for forensic or compliance purposes."
                ),
            },
            {
                "id": "c",
                "text": "Run a full anti-malware scan immediately to measure how much is infected",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning before disabling System Restore "
                    "(step 3) risks the malware surviving in shadow copies. "
                    "Scanning is part of step 4; quarantine (step 2) comes "
                    "first to stop spread before any remediation begins."
                ),
            },
            {
                "id": "d",
                "text": "Re-enable System Restore to create a snapshot of the infected state for analysis",
                "correct": False,
                "rationale": (
                    "Incorrect. Creating a restore point of an infected state "
                    "would preserve the malware in shadow copies. System "
                    "Restore is disabled in step 3 specifically to prevent "
                    "this scenario."
                ),
            },
        ],
        "explanation": (
            "Step 2 (Quarantine) has two components: (a) physically isolate "
            "the machine from the network to stop malware spread and C2 traffic, "
            "and (b) notify management/document the incident per the "
            "organizational incident response policy. These actions occur "
            "before disabling System Restore (step 3) or scanning (step 4)."
        ),
    },
    {
        "id": "c2d3v2-006",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "After completing the CompTIA seven-step malware removal process, "
            "the technician tells the user: 'Your computer is clean now — "
            "all done.' The user is released without any additional "
            "interaction. Which step has been omitted, and why does it matter?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Step 7 (Educate the end user) was skipped; without education the user's behavior that caused the infection is unchanged, making reinfection likely",
                "correct": True,
                "rationale": (
                    "Correct. Step 7 is end-user education. Most infections "
                    "result from user actions such as clicking phishing links "
                    "or downloading bundled software. Skipping this step "
                    "leaves the human attack vector unaddressed, and the same "
                    "behavior will almost certainly lead to another infection."
                ),
            },
            {
                "id": "b",
                "text": "Step 5 (Schedule scans) was skipped; without recurring scans the machine will be reinfected immediately",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes releasing the user after "
                    "saying the machine is clean — implying all technical steps "
                    "were done — but no conversation occurred with the user. "
                    "Step 7 (education) is the missing human-facing final step."
                ),
            },
            {
                "id": "c",
                "text": "Step 6 (Re-enable System Restore) was skipped; the machine now has no recovery points",
                "correct": False,
                "rationale": (
                    "Incorrect. The technician declared the machine clean, "
                    "which implies technical remediation steps were completed. "
                    "The omission described is the lack of any interaction "
                    "to educate the user — step 7."
                ),
            },
            {
                "id": "d",
                "text": "Step 2 (Quarantine) was skipped; the machine should have been reconnected to the network last",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine is step 2 — it is performed at the "
                    "start. The machine is reconnected during or after step 5. "
                    "The missing action here is post-remediation user education."
                ),
            },
        ],
        "explanation": (
            "The CompTIA malware removal process ends with step 7: Educate "
            "the end user. This step closes the human vulnerability loop. "
            "Topics should include the infection vector (phishing, unsafe "
            "downloads, social engineering), organizational security policies, "
            "and how to recognize future threats. Without it, the user is "
            "likely to repeat the behavior that caused the infection."
        ),
    },
    {
        "id": "c2d3v2-007",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician is performing step 4 (Remediate) of the CompTIA "
            "malware removal process on a machine confirmed to have a "
            "persistent Trojan. Which TWO scanning environment choices "
            "are explicitly recommended in this step to maximize "
            "effectiveness? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Boot the machine into safe mode before scanning",
                "correct": True,
                "rationale": (
                    "Correct. Safe mode loads minimal drivers and services, "
                    "preventing most malware from launching at startup. This "
                    "allows the anti-malware scanner to detect and remove "
                    "files that would be locked or hidden in a normal boot."
                ),
            },
            {
                "id": "b",
                "text": "Scan from a bootable preinstallation environment (WinPE) using an offline scanner",
                "correct": True,
                "rationale": (
                    "Correct. A WinPE (preinstallation environment) boot disk "
                    "loads a separate, clean OS. Since the infected OS is "
                    "never started, malware cannot hook into the kernel or "
                    "lock files, allowing the scanner full access to all "
                    "malicious files on the target drive."
                ),
            },
            {
                "id": "c",
                "text": "Scan from within the normal Windows session logged in as the infected user",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning from inside the running infected OS "
                    "allows active malware to hide from or interfere with "
                    "the scanner. CompTIA step 4 specifically recommends "
                    "environments that bypass the active infected OS."
                ),
            },
            {
                "id": "d",
                "text": "Run the scan over the network from a remote IT workstation via UNC path",
                "correct": False,
                "rationale": (
                    "Incorrect. Scanning via network share does not load "
                    "the scanner on the infected machine's processor in a "
                    "clean context. The infected OS still mediates file "
                    "access, allowing rootkit or Trojan evasion. This is "
                    "not a CompTIA-recommended approach for step 4."
                ),
            },
        ],
        "explanation": (
            "CompTIA step 4 explicitly calls for two scanning techniques to "
            "overcome evasion: (1) safe mode — minimal OS footprint, most "
            "malware cannot auto-start; and (2) preinstallation environment "
            "— fully offline kernel, zero reliance on the infected OS. "
            "Both approaches prevent the malware from hiding from or "
            "interfering with the scanner."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.1 — Windows OS troubleshooting  (10 questions)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v2-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 workstation shows the error 'The application was "
            "unable to start correctly (0xc000007b)' when launching any "
            "64-bit application. The same applications run fine on other "
            "identical machines. Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A required 64-bit runtime DLL (such as a Visual C++ redistributable) is corrupt or a 32-bit version has replaced the 64-bit version",
                "correct": True,
                "rationale": (
                    "Correct. Error 0xc000007b indicates an application "
                    "tried to load an incompatible DLL — most commonly "
                    "a 32-bit DLL was placed in the System32 folder where "
                    "64-bit DLLs are expected, or a runtime redistributable "
                    "(VC++, .NET) is corrupted. Reinstalling the appropriate "
                    "64-bit redistributable fixes this."
                ),
            },
            {
                "id": "b",
                "text": "The hard drive is failing and corrupting application executables on the fly",
                "correct": False,
                "rationale": (
                    "Incorrect. Drive failure would produce different errors "
                    "(read errors, BSOD, CHKDSK findings) and would not "
                    "present as a consistent DLL initialization failure "
                    "across ALL 64-bit apps while 32-bit apps work."
                ),
            },
            {
                "id": "c",
                "text": "Windows Update has disabled 64-bit application support",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Update does not disable application "
                    "architecture support. This is not a valid Windows "
                    "behavior; 64-bit support is a core OS feature that "
                    "cannot be toggled by updates."
                ),
            },
            {
                "id": "d",
                "text": "The user account lacks the 'Run as 64-bit' privilege required by these applications",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no Windows privilege called 'Run "
                    "as 64-bit.' Architecture compatibility is determined "
                    "by the OS and DLL bitness, not by user rights."
                ),
            },
        ],
        "explanation": (
            "Error 0xc000007b (STATUS_INVALID_IMAGE_FORMAT) occurs when an "
            "application loads a DLL of the wrong bitness or a corrupted "
            "runtime DLL. The most common fix: reinstall Microsoft Visual "
            "C++ Redistributable (both x64 and x86 versions), and/or "
            "run SFC /scannow followed by DISM /RestoreHealth to repair "
            "corrupted system binaries."
        ),
    },
    {
        "id": "c2d3v2-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A user complains that their Windows 11 PC takes 4–5 minutes to "
            "reach the desktop after the welcome screen appears. Login times "
            "are fine on other machines. Task Manager shows low CPU and RAM "
            "at login. Event Viewer has no errors but shows many Group Policy "
            "events. Which diagnostic action is MOST targeted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run 'gpresult /h gpreport.html' to generate a Group Policy results report and review applied policies and timings",
                "correct": True,
                "rationale": (
                    "Correct. When GPO events are present during an abnormally "
                    "slow login, gpresult /h produces an HTML report that "
                    "lists all applied policies and their processing times. "
                    "A slow logon script, large software deployment GPO, or "
                    "misconfigured folder redirection will show as a high-"
                    "duration event in the report."
                ),
            },
            {
                "id": "b",
                "text": "Run DISM /RestoreHealth to fix Windows components that may delay login",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM repairs the Windows component store. "
                    "Multiple GPO events during slow login point to Group "
                    "Policy processing — a policy configuration issue, not "
                    "an OS component corruption issue."
                ),
            },
            {
                "id": "c",
                "text": "Replace the SSD because slow boot correlates with drive latency",
                "correct": False,
                "rationale": (
                    "Incorrect. Disk replacement is a hardware solution. "
                    "The task manager shows low CPU/RAM and the delay begins "
                    "after the welcome screen, suggesting policy processing "
                    "— a software/configuration problem. Hardware is not "
                    "implicated."
                ),
            },
            {
                "id": "d",
                "text": "Disable all startup programs via Task Manager > Startup",
                "correct": False,
                "rationale": (
                    "Incorrect. Startup programs load after the desktop "
                    "appears, not during the 'reaching desktop' phase. "
                    "Disabling them would not address a delay caused by "
                    "Group Policy processing during logon."
                ),
            },
        ],
        "explanation": (
            "Slow Windows logon with Group Policy events in Event Viewer "
            "is best diagnosed with gpresult /h, which shows which policies "
            "were applied and how long each took. Common culprits: logon "
            "scripts on slow shares, large software distribution packages, "
            "or folder redirection to a slow UNC path. Disabling or optimizing "
            "the offending GPO resolves the delay."
        ),
    },
    {
        "id": "c2d3v2-010",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows workstation prints to a local USB printer successfully "
            "but cannot print to any network printer. Other workstations "
            "print to the same network printers without issue. The Print "
            "Spooler service is running. Which action should the technician "
            "try FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check Windows Firewall settings to ensure File and Printer Sharing is allowed for the private network profile",
                "correct": True,
                "rationale": (
                    "Correct. A Windows Firewall rule that blocks outbound "
                    "SMB or the 'File and Printer Sharing' exception being "
                    "disabled for the active network profile (Private/Domain) "
                    "would prevent access to network printers while local USB "
                    "printing continues to work. This is the most targeted "
                    "first check for a single-machine network printing failure."
                ),
            },
            {
                "id": "b",
                "text": "Restart the Print Spooler service to clear a stuck print queue",
                "correct": False,
                "rationale": (
                    "Incorrect. Restarting the spooler clears stuck jobs "
                    "but does not address a connectivity issue. The spooler "
                    "is already running and local printing works, ruling out "
                    "a spooler problem."
                ),
            },
            {
                "id": "c",
                "text": "Reinstall the network printer drivers to resolve a driver conflict",
                "correct": False,
                "rationale": (
                    "Incorrect. Driver reinstallation applies when printing "
                    "fails to one specific printer. The symptom is ALL network "
                    "printers failing while local printing works — a network/"
                    "firewall issue, not a driver issue."
                ),
            },
            {
                "id": "d",
                "text": "Rejoin the workstation to the domain to repair broken SMB authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Rejoining the domain is a significant action "
                    "used when domain trust is broken. The symptom could exist "
                    "on a workgroup machine too, and the firewall setting is "
                    "a simpler, more likely cause to check first."
                ),
            },
        ],
        "explanation": (
            "Network printer access from a single machine uses SMB/IPP "
            "protocols. A misconfigured Windows Firewall profile (especially "
            "if the network was re-classified as Public instead of Private/"
            "Domain) blocks these protocols, explaining why local USB printing "
            "works while all network printers fail. Check: Control Panel > "
            "Windows Defender Firewall > Allow an app > File and Printer "
            "Sharing — enable for the active profile."
        ),
    },
    {
        "id": "c2d3v2-011",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 laptop's screen stays black after waking from "
            "hibernation. The power LED is on, keyboard inputs show the "
            "Caps Lock LED responding, and a brief flicker suggests Windows "
            "has resumed. An external monitor shows the desktop normally. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The laptop's GPU driver is failing to re-initialize the internal display after hibernation resume",
                "correct": True,
                "rationale": (
                    "Correct. GPU driver resume failures after hibernation are "
                    "a known Windows issue. The Caps Lock LED confirms the OS "
                    "is running; the external display working confirms the GPU "
                    "is functional. The internal display's failure to re-"
                    "initialize points to a driver-level handshake problem "
                    "with the integrated display. Updating or rolling back "
                    "the display driver typically resolves this."
                ),
            },
            {
                "id": "b",
                "text": "The laptop's LCD backlight has burned out permanently",
                "correct": False,
                "rationale": (
                    "Incorrect. If the backlight had burned out, it would "
                    "fail consistently — not only after hibernation. The "
                    "flicker on resume and normal operation otherwise rules "
                    "out permanent hardware failure."
                ),
            },
            {
                "id": "c",
                "text": "Hibernate is corrupting the user profile, causing the desktop to fail to load",
                "correct": False,
                "rationale": (
                    "Incorrect. Profile corruption would affect all displays "
                    "equally; the external monitor showing the desktop "
                    "correctly contradicts a profile issue. The problem is "
                    "specific to the internal display, not the session."
                ),
            },
            {
                "id": "d",
                "text": "The BIOS is configured to disable the internal display during OS runtime",
                "correct": False,
                "rationale": (
                    "Incorrect. A BIOS setting disabling the internal display "
                    "would be persistent, not triggered specifically by "
                    "hibernation resume. The symptom is inconsistent "
                    "with a static BIOS configuration."
                ),
            },
        ],
        "explanation": (
            "Black internal screen after hibernation with a working external "
            "monitor is a classic display driver resume bug. The GPU resumes "
            "but fails to re-establish the internal panel's display pipeline. "
            "Workarounds: update the GPU driver, press Win+P to cycle display "
            "modes, or disable Fast Startup. Long-term fix: install the "
            "latest OEM or WHQL display driver."
        ),
    },
    {
        "id": "c2d3v2-012",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A technician needs to identify which process opened a specific "
            "network connection to an external IP address on a Windows "
            "workstation. Which command-line tool provides both the process "
            "name/PID and the remote IP:port mapping simultaneously?"
        ),
        "options": [
            {
                "id": "a",
                "text": "netstat -b (or netstat -ano and cross-reference with tasklist)",
                "correct": True,
                "rationale": (
                    "Correct. 'netstat -b' displays active connections with "
                    "the executable name that created each connection. "
                    "'netstat -ano' shows PID numbers which can then be "
                    "matched to process names using 'tasklist /FI \"PID eq "
                    "<PID>\"'. Both approaches map open connections to "
                    "their originating process."
                ),
            },
            {
                "id": "b",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /all shows network adapter "
                    "configuration (IP addresses, MAC addresses, DNS servers) "
                    "but does not display active connections or the processes "
                    "that created them."
                ),
            },
            {
                "id": "c",
                "text": "ping -t <remote IP>",
                "correct": False,
                "rationale": (
                    "Incorrect. Ping tests ICMP reachability. It does not "
                    "enumerate active TCP/UDP connections, show open ports, "
                    "or identify which process owns a connection."
                ),
            },
            {
                "id": "d",
                "text": "tracert <remote IP>",
                "correct": False,
                "rationale": (
                    "Incorrect. Tracert shows the hop-by-hop path to a "
                    "destination but does not display currently established "
                    "connections or their owning processes."
                ),
            },
        ],
        "explanation": (
            "netstat is the Windows tool for mapping active TCP/UDP connections. "
            "'netstat -b' shows the owning executable per connection. "
            "'netstat -ano' shows numeric PIDs, which are cross-referenced "
            "with tasklist to get process names. Resource Monitor's Network "
            "tab also shows per-process connections in a GUI format."
        ),
    },
    {
        "id": "c2d3v2-013",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows 10 PC displays a BSOD with stop code "
            "CRITICAL_PROCESS_DIED immediately at login. The error started "
            "after a forced power-off during a Windows Update. Which TWO "
            "recovery actions should the technician attempt from WinRE? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run 'sfc /scannow' from the WinRE Command Prompt to repair corrupted system files",
                "correct": True,
                "rationale": (
                    "Correct. A forced shutdown during a Windows Update can "
                    "leave OS files partially written and corrupted. Running "
                    "SFC from WinRE (offline: 'sfc /scannow /offbootdir=C:\\ "
                    "/offwindir=C:\\Windows') repairs protected system files "
                    "that critical processes depend on."
                ),
            },
            {
                "id": "b",
                "text": "Use System Restore from WinRE to roll back to a state before the failed update",
                "correct": True,
                "rationale": (
                    "Correct. If a restore point exists from before the update, "
                    "System Restore from WinRE reverses the partial update "
                    "damage, restoring the OS to a known-good state. This is "
                    "appropriate when SFC alone cannot repair the damage."
                ),
            },
            {
                "id": "c",
                "text": "Replace the RAM, as CRITICAL_PROCESS_DIED always indicates a hardware failure",
                "correct": False,
                "rationale": (
                    "Incorrect. CRITICAL_PROCESS_DIED can be caused by "
                    "software issues — a corrupted OS update is a classic "
                    "cause. Hardware replacement should only be considered "
                    "after software repair options are exhausted."
                ),
            },
            {
                "id": "d",
                "text": "Disable all third-party services via msconfig from WinRE",
                "correct": False,
                "rationale": (
                    "Incorrect. CRITICAL_PROCESS_DIED after a failed update "
                    "is a system-file corruption issue, not a third-party "
                    "service conflict. msconfig's clean-boot approach targets "
                    "service conflicts, not OS file damage."
                ),
            },
        ],
        "explanation": (
            "CRITICAL_PROCESS_DIED after a power-cut during Windows Update "
            "indicates OS binary corruption. The two CompTIA-aligned first "
            "responses from WinRE are: SFC (repairs corrupted protected "
            "files from the component store) and System Restore (rolls back "
            "to a pre-corruption state). DISM /RestoreHealth is a third "
            "option if SFC cannot repair the component store."
        ),
    },
    {
        "id": "c2d3v2-014",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A technician receives a complaint that a Windows workstation "
            "application takes 8 minutes to open a 50 MB Excel file from "
            "a network share, while a local copy opens in 5 seconds. Other "
            "users open the same share file in 30 seconds. Which Windows "
            "tool should the technician use to check if the workstation's "
            "network adapter is experiencing performance degradation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Performance Monitor (perfmon.exe) with the Network Interface counters",
                "correct": True,
                "rationale": (
                    "Correct. Performance Monitor with 'Network Interface' "
                    "counters (Bytes Received/sec, Output Queue Length, "
                    "Packets Received Errors) provides granular, loggable "
                    "metrics to identify whether the adapter is throttling, "
                    "dropping packets, or experiencing high queue lengths — "
                    "pointing to an adapter or driver performance problem."
                ),
            },
            {
                "id": "b",
                "text": "Device Manager — check the network adapter for yellow warning indicators",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Manager shows driver/hardware errors "
                    "with visible warnings, but a functioning-yet-degraded "
                    "adapter often shows no warning flag. Device Manager "
                    "cannot measure real-time throughput or queue lengths."
                ),
            },
            {
                "id": "c",
                "text": "Event Viewer — search the System log for network-related errors",
                "correct": False,
                "rationale": (
                    "Incorrect. Event Viewer logs discrete events (driver "
                    "errors, disconnections) but does not provide the "
                    "continuous throughput metrics needed to diagnose a "
                    "slow adapter. Performance Monitor is better suited "
                    "for quantitative adapter performance analysis."
                ),
            },
            {
                "id": "d",
                "text": "Task Manager — view the Network column on the Performance tab",
                "correct": False,
                "rationale": (
                    "Incorrect. Task Manager's Network tab shows current "
                    "utilization as a percentage but lacks the detail of "
                    "Performance Monitor counters (queue length, error rate, "
                    "packet counts) needed to diagnose adapter-level "
                    "degradation versus network path issues."
                ),
            },
        ],
        "explanation": (
            "Performance Monitor with Network Interface object counters "
            "provides granular metrics: Bytes Total/sec (throughput), "
            "Output Queue Length (congestion), Packets Received Errors "
            "(hardware errors), and Current Bandwidth. These counters "
            "distinguish an adapter problem (errors, throttled throughput) "
            "from a network path problem (high ping, router issue)."
        ),
    },
    {
        "id": "c2d3v2-015",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows user reports that Cortana / Windows Search returns "
            "no results for local files. The Windows Search service is "
            "running. Other system functions are normal. Which action "
            "should the technician perform FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rebuild the Windows Search index via Indexing Options in Control Panel",
                "correct": True,
                "rationale": (
                    "Correct. Windows Search depends on a pre-built index "
                    "of local files. A corrupted or incomplete index causes "
                    "search to return no results even though the service is "
                    "running. Rebuilding the index (Control Panel > Indexing "
                    "Options > Advanced > Rebuild) forces re-indexing of "
                    "all indexed locations and restores search functionality."
                ),
            },
            {
                "id": "b",
                "text": "Reinstall Windows to replace the Windows Search component",
                "correct": False,
                "rationale": (
                    "Incorrect. Reinstalling Windows for a broken search "
                    "index is grossly disproportionate. Index corruption is "
                    "a common, easily resolved issue using Indexing Options."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow to repair corrupted Search DLLs",
                "correct": False,
                "rationale": (
                    "Incorrect. While SFC could help if Search binaries are "
                    "corrupted, the described symptom (service running but "
                    "no results) is typical of index corruption, not DLL "
                    "corruption. Index rebuild is the more targeted first step."
                ),
            },
            {
                "id": "d",
                "text": "Grant the user administrator rights so Windows Search can access all files",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Search indexes accessible content "
                    "within the user's profile and configured locations "
                    "regardless of admin rights. Privilege escalation does "
                    "not repair a corrupt index and introduces unnecessary "
                    "security risk."
                ),
            },
        ],
        "explanation": (
            "The Windows Search index is a database of file metadata and "
            "content. Index corruption — from abrupt shutdowns, disk errors, "
            "or update failures — causes searches to return no results. "
            "Rebuilding via Control Panel > Indexing Options > Advanced > "
            "Rebuild triggers a full re-index. Large indexes may take hours "
            "to rebuild but full search functionality returns once complete."
        ),
    },
    {
        "id": "c2d3v2-016",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A Windows 10 workstation boots successfully but takes 3 minutes "
            "to reach the desktop. Event Viewer shows ID 7000 (Service "
            "failed to start) for a third-party VPN service. That service "
            "is set to Automatic. No BSOD occurs. What change will MOST "
            "likely reduce the boot time without disabling the VPN service?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Change the VPN service startup type to 'Automatic (Delayed Start)'",
                "correct": True,
                "rationale": (
                    "Correct. A service failing to start at normal Automatic "
                    "startup adds its full timeout (typically 30 seconds) "
                    "to the boot process while Windows waits for it to respond. "
                    "Delayed Start starts the service after critical services "
                    "are up, often resolving the dependency timing issue and "
                    "eliminating the startup delay."
                ),
            },
            {
                "id": "b",
                "text": "Delete the failing VPN service registry key to prevent it from loading",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting the service registry key removes "
                    "the VPN software's service entirely, which may break "
                    "VPN functionality. The requirement is to keep the service "
                    "but reduce boot delay."
                ),
            },
            {
                "id": "c",
                "text": "Set the VPN service to Manual and start it via a logon script",
                "correct": False,
                "rationale": (
                    "Incorrect. A logon script workaround is less elegant "
                    "and adds administrative overhead. Delayed Start "
                    "is the built-in Windows mechanism designed precisely "
                    "for this scenario."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall the VPN client so its service executable is repaired",
                "correct": False,
                "rationale": (
                    "Incorrect. A timeout error (7000) at boot with manual "
                    "start succeeding indicates a dependency timing problem, "
                    "not a corrupted executable. Reinstallation would not "
                    "change the service's startup behavior."
                ),
            },
        ],
        "explanation": (
            "Service startup type 'Automatic (Delayed Start)' was introduced "
            "specifically to improve boot performance by deferring non-critical "
            "services until core Windows services are stable. This eliminates "
            "the 30-second wait for a service that times out because its "
            "dependencies (network, RPC, etc.) aren't ready when it tries "
            "to start. Change via services.msc > service properties > "
            "Startup type."
        ),
    },
    {
        "id": "c2d3v2-017",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A dual-boot system running Windows 10 and Windows 11 no longer "
            "shows the boot menu after the user accidentally ran "
            "'bcdedit /bootsequence' with incorrect parameters. Both OSes "
            "are on separate partitions and the drives are healthy. Which "
            "command will BEST restore the dual-boot menu?"
        ),
        "options": [
            {
                "id": "a",
                "text": "bootrec /rebuildbcd from the Windows Recovery Environment",
                "correct": True,
                "rationale": (
                    "Correct. 'bootrec /rebuildbcd' scans all drives for "
                    "Windows installations and offers to add them to the "
                    "BCD (Boot Configuration Data) store. This rebuilds "
                    "the boot menu with all detected installations, "
                    "restoring the dual-boot selection screen."
                ),
            },
            {
                "id": "b",
                "text": "bcdedit /default {current} to reset the default boot entry",
                "correct": False,
                "rationale": (
                    "Incorrect. Setting a default entry does not restore "
                    "a missing or corrupted BCD menu. If entries for both "
                    "OSes are missing from the BCD, bcdedit /default cannot "
                    "reference entries that do not exist."
                ),
            },
            {
                "id": "c",
                "text": "Format the EFI System Partition and reinstall the bootloader",
                "correct": False,
                "rationale": (
                    "Incorrect. Formatting the ESP is destructive and "
                    "unnecessary. 'bootrec /rebuildbcd' reconstructs the BCD "
                    "without destroying the partition or requiring reinstallation."
                ),
            },
            {
                "id": "d",
                "text": "Use msconfig to add a boot entry for the missing OS",
                "correct": False,
                "rationale": (
                    "Incorrect. msconfig's Boot tab can modify existing BCD "
                    "entries but cannot discover and add missing OS installations "
                    "from scratch. That requires bootrec /rebuildbcd."
                ),
            },
        ],
        "explanation": (
            "'bootrec /rebuildbcd' scans connected drives for compatible "
            "Windows installations and adds them to the BCD store, restoring "
            "the boot selection menu. If /rebuildbcd finds the installations "
            "but the BCD file itself is corrupted, precede it with "
            "'bootrec /fixmbr' and 'bootrec /fixboot' to ensure the "
            "boot sector is intact before rebuilding the BCD."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.2 — PC security issue troubleshooting  (6 questions)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v2-018",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A technician is investigating a Windows workstation where "
            "CPU usage spikes to 100% at night. Review of Task Manager "
            "history and scheduled tasks reveals a process named "
            "'svch0st.exe' (zero, not letter O) running under a standard "
            "user account at 2:00 AM every day. The legitimate svchost.exe "
            "is located in C:\\Windows\\System32. Where is this suspicious "
            "process running from, and what security symptom does this "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "It is likely malware masquerading as a system process (process name spoofing) running from a non-standard path, a classic PC security symptom",
                "correct": True,
                "rationale": (
                    "Correct. Malware commonly uses process names that "
                    "visually resemble legitimate processes (svch0st vs "
                    "svchost) to avoid detection. The legitimate svchost.exe "
                    "always runs from C:\\Windows\\System32 under SYSTEM, "
                    "NETWORK SERVICE, or LOCAL SERVICE — never under a "
                    "user account. A differently-named process under a user "
                    "account is a classic PC security symptom of a Trojan "
                    "or cryptominer."
                ),
            },
            {
                "id": "b",
                "text": "It is Windows Update running under a scheduled task and the name discrepancy is a display bug",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Update runs under SYSTEM or "
                    "TrustedInstaller, not standard user accounts, and "
                    "uses processes named TiWorker.exe, wuauclt.exe, or "
                    "WaasMedicAgent.exe — not a misspelled svchost. "
                    "A display bug would not alter the executable name."
                ),
            },
            {
                "id": "c",
                "text": "It is a legitimate background indexing task that runs under the user's account context",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Search indexing uses SearchIndexer.exe "
                    "and SearchHost.exe, not svchost variants. Indexing would "
                    "also scale with disk activity, not pin CPU at 100%."
                ),
            },
            {
                "id": "d",
                "text": "It is an antivirus scheduled scan disguised as a system process to avoid being killed",
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate antivirus products run under their "
                    "own named processes (MsMpEng.exe, avgnt.exe, etc.) "
                    "and are not scheduled under standard user accounts "
                    "with misleading names."
                ),
            },
        ],
        "explanation": (
            "Process name spoofing (using characters like '0' for 'o') is "
            "a textbook malware evasion technique. Legitimate svchost.exe: "
            "lives only in C:\\Windows\\System32, runs under SYSTEM/NETWORK "
            "SERVICE/LOCAL SERVICE, and never under a regular user account. "
            "Verify via Process Explorer (show verified signatures) or "
            "Task Manager > right-click > Open file location. Treat any "
            "deviation as malware and follow the 7-step removal process."
        ),
    },
    {
        "id": "c2d3v2-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user contacts the help desk saying their Windows desktop "
            "wallpaper has been replaced by a black screen with white text "
            "reading: 'YOUR FILES ARE ENCRYPTED. Send 0.5 BTC to restore "
            "access.' The user's Documents and Pictures folders contain "
            "files with the extension '.enc'. What is the PRIMARY "
            "recommended action according to CompTIA best practices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Immediately isolate the workstation from the network to prevent encryption from spreading to shared drives",
                "correct": True,
                "rationale": (
                    "Correct. This is active ransomware. Isolation (step 2 "
                    "of the malware removal process — quarantine) is the "
                    "immediate priority. Modern ransomware actively scans "
                    "for and encrypts mapped network drives and accessible "
                    "SMB shares; disconnecting from the network stops "
                    "lateral spread while incident response begins."
                ),
            },
            {
                "id": "b",
                "text": "Use System Restore to recover the encrypted files before they are permanently lost",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore recovers system settings and "
                    "registry state, not user data files. Additionally, acting "
                    "on the infected machine before isolating it allows the "
                    "ransomware to continue encrypting network shares."
                ),
            },
            {
                "id": "c",
                "text": "Contact the Bitcoin address provided to negotiate a lower ransom",
                "correct": False,
                "rationale": (
                    "Incorrect. Paying or negotiating the ransom is against "
                    "CompTIA guidance and most organizational security "
                    "policies. Payment does not guarantee decryption keys "
                    "and funds criminal activity."
                ),
            },
            {
                "id": "d",
                "text": "Change the file extension of all .enc files back to their original extensions",
                "correct": False,
                "rationale": (
                    "Incorrect. Renaming the extensions does not decrypt "
                    "the underlying data. The content is cryptographically "
                    "encrypted; only a valid decryption key will restore "
                    "the files."
                ),
            },
        ],
        "explanation": (
            "Ransomware is identified by altered/encrypted files and a "
            "ransom demand — both CompTIA-listed PC security symptoms. "
            "The correct first response is network quarantine to stop "
            "spread. Recovery then relies on clean offline backups; "
            "if no backups exist, check nomoreransom.org for any available "
            "decryptors before considering whether to engage with attackers."
        ),
    },
    {
        "id": "c2d3v2-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user reports that their Windows PC automatically opens a "
            "website selling security software each time they log in. "
            "The website URL appears in the Run registry key "
            "(HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run). "
            "Anti-malware scans show no threats. What is the MOST likely "
            "explanation and best fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A PUP or adware added a Run key entry; remove the registry entry and uninstall the associated software",
                "correct": True,
                "rationale": (
                    "Correct. Potentially Unwanted Programs (PUPs) and adware "
                    "commonly add Run key entries to the registry to launch "
                    "at login and display ads or push products. Many AV tools "
                    "do not flag PUPs by default. The fix is to delete the "
                    "registry entry and uninstall the software via Programs "
                    "and Features."
                ),
            },
            {
                "id": "b",
                "text": "The system is infected with a rootkit that the scanner cannot detect",
                "correct": False,
                "rationale": (
                    "Incorrect. A rootkit would hide itself and its registry "
                    "entries; the technician would not see the Run key entry "
                    "clearly. A visible Run key entry pointing to a URL is "
                    "characteristic of PUP/adware, not a rootkit."
                ),
            },
            {
                "id": "c",
                "text": "A Group Policy logon script is directing the browser to open that URL",
                "correct": False,
                "rationale": (
                    "Incorrect. GPO logon scripts would appear in the Group "
                    "Policy settings, not in HKCU Run keys. Also, a corporate "
                    "GPO would not direct users to a third-party security "
                    "software purchase page."
                ),
            },
            {
                "id": "d",
                "text": "Windows Startup Repair is redirecting the browser as part of an automated repair routine",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Startup Repair is a recovery tool "
                    "that repairs boot issues; it does not interact with "
                    "browser sessions or add registry Run key entries."
                ),
            },
        ],
        "explanation": (
            "Registry Run keys are a common persistence mechanism for PUPs "
            "and adware. HKCU Run entries are per-user; HKLM Run entries "
            "affect all users. To remediate: delete the key in regedit, "
            "uninstall the associated software via Control Panel, and run "
            "a scan with a tool that specifically detects PUPs (Malwarebytes "
            "free edition is commonly recommended). Also check the Startup "
            "folder: %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup."
        ),
    },
    {
        "id": "c2d3v2-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "Users across an entire department report that their antivirus "
            "software was automatically uninstalled overnight. Windows "
            "Security Center shows no active protection on all affected "
            "machines. Machines in other departments are unaffected. The "
            "department's machines all share the same OU in Active "
            "Directory. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A malicious or misconfigured Group Policy Object linked to the department's OU executed a software removal policy",
                "correct": True,
                "rationale": (
                    "Correct. GPOs linked to a specific OU apply only to "
                    "computers in that OU. A GPO configured with a software "
                    "removal policy (or a script) could uninstall the AV "
                    "across all machines in the OU simultaneously. A malicious "
                    "or misconfigured GPO is the most likely cause when the "
                    "scope exactly matches an OU boundary."
                ),
            },
            {
                "id": "b",
                "text": "The antivirus vendor pushed an automatic uninstall update to all enterprise licenses",
                "correct": False,
                "rationale": (
                    "Incorrect. AV vendors do not push silent uninstall updates. "
                    "An update might upgrade or patch the product but would "
                    "not remove it without administrative action."
                ),
            },
            {
                "id": "c",
                "text": "A network worm propagated only within the department's network segment and removed the AV",
                "correct": False,
                "rationale": (
                    "Incorrect. A worm would not limit itself to a single OU — "
                    "it propagates by network connectivity, not by AD structure. "
                    "The OU-level exactness of the affected scope points to "
                    "a GPO, not a network-spreading worm."
                ),
            },
            {
                "id": "d",
                "text": "Windows Update removed the AV as an incompatible application on those machines",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Update may flag incompatible software "
                    "during major version upgrades, but it does not silently "
                    "remove AV software on a standard monthly update cycle, "
                    "and it would not be scoped to one OU."
                ),
            },
        ],
        "explanation": (
            "GPO software policy (Computer Configuration > Software Settings "
            "> Software Installation) can deploy or remove applications. "
            "When the scope of an incident matches an AD OU boundary exactly, "
            "a GPO is the most logical cause. Investigate with gpresult or "
            "the GPMC to identify recently modified GPOs linked to the "
            "affected OU. If malicious, follow incident response procedures."
        ),
    },
    {
        "id": "c2d3v2-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security symptoms",
        "stem": (
            "A user's browser has a new extension installed that was not "
            "added by the user. The extension intercepts HTTPS traffic "
            "by installing its own root certificate in the system's "
            "Trusted Root CA store. The user noticed online banking "
            "sessions no longer show the expected padlock indicator. "
            "What type of attack is this and what is the correct response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSL/TLS interception by a malicious browser extension performing a local MITM attack; remove the extension and delete its root certificate from the Trusted Root CA store",
                "correct": True,
                "rationale": (
                    "Correct. A malicious extension that installs a custom "
                    "CA root certificate can intercept and decrypt HTTPS "
                    "traffic on the local machine (local MITM). It acts as "
                    "a proxy, re-signing sessions with its own cert. Removal "
                    "requires uninstalling the extension AND deleting the "
                    "rogue CA certificate from the Trusted Root CA store via "
                    "certmgr.msc or the browser's certificate manager."
                ),
            },
            {
                "id": "b",
                "text": "The website's SSL certificate expired and the bank needs to be notified",
                "correct": False,
                "rationale": (
                    "Incorrect. An expired server certificate would affect "
                    "all users, not just this one. The browser extension and "
                    "rogue CA certificate are local to this machine, explaining "
                    "why only this user is affected."
                ),
            },
            {
                "id": "c",
                "text": "Windows Update revoked the bank website's certificate as untrusted",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Update does not revoke specific "
                    "website certificates. Certificate revocation is handled "
                    "by CAs and browsers via CRL/OCSP, not Windows Update."
                ),
            },
            {
                "id": "d",
                "text": "The network's corporate proxy is performing authorized SSL inspection",
                "correct": False,
                "rationale": (
                    "Incorrect. Authorized corporate SSL inspection certificates "
                    "are deployed via GPO and would affect all machines on the "
                    "network. An unknown extension that installed without the "
                    "user's knowledge is not an authorized corporate control."
                ),
            },
        ],
        "explanation": (
            "Rogue browser extensions that install custom CA root certificates "
            "are used for local SSL/TLS MITM attacks. This is a CompTIA-listed "
            "browser security concern. Full remediation: (1) remove the "
            "extension from the browser, (2) open certmgr.msc and remove "
            "the rogue certificate from Trusted Root CAs, (3) scan with "
            "anti-malware, (4) change banking passwords from a clean device."
        ),
    },
    {
        "id": "c2d3v2-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A technician discovers a Windows workstation is participating "
            "in a botnet: it sends large volumes of outbound SMTP traffic "
            "at night and the hosts file contains entries redirecting "
            "security update domains to 127.0.0.1. Which TWO immediate "
            "actions should the technician take? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Quarantine the workstation by disconnecting it from the network",
                "correct": True,
                "rationale": (
                    "Correct. Isolation stops the botnet spam campaign and "
                    "removes the machine from the attacker's C2 infrastructure. "
                    "This is step 2 of the malware removal process and "
                    "the immediate priority for an active threat."
                ),
            },
            {
                "id": "b",
                "text": "Restore the hosts file to its default state to re-enable security update access",
                "correct": True,
                "rationale": (
                    "Correct. Clearing the malicious hosts file entries is "
                    "a critical remediation step. The redirected update domains "
                    "block anti-malware definition updates, which is why they "
                    "were tampered with. Restoring the file (delete all non-"
                    "comment entries) allows updates to flow once the machine "
                    "is reconnected."
                ),
            },
            {
                "id": "c",
                "text": "Immediately pay the ransom to stop the botnet activity",
                "correct": False,
                "rationale": (
                    "Incorrect. A botnet infection is not ransomware. There "
                    "is no ransom demand, and botnet operators do not offer "
                    "disinfection services. Payment is not applicable here."
                ),
            },
            {
                "id": "d",
                "text": "Enable the Windows SMTP relay service to monitor outbound mail content",
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling SMTP relay on an infected machine "
                    "would facilitate, not stop, the spam campaign. Monitoring "
                    "malware traffic is a secondary forensic activity, not an "
                    "immediate remediation step."
                ),
            },
        ],
        "explanation": (
            "A botnet-infected machine performing spam and blocking security "
            "updates requires: (1) immediate network quarantine to stop the "
            "active attack, and (2) restoration of the hosts file to restore "
            "update connectivity. Both are critical first steps before "
            "proceeding through the full seven-step malware removal process, "
            "including scanning in safe mode or WinPE."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.4 — Mobile OS troubleshooting  (7 questions)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v2-024",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone shows 'Mobile network not available' "
            "even though the SIM card is inserted and other users' phones "
            "work fine on the same carrier nearby. Wi-Fi and Bluetooth work. "
            "Reseating the SIM made no difference. Which should the "
            "technician try NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reset network settings (Settings > General Management > Reset > Reset Network Settings)",
                "correct": True,
                "rationale": (
                    "Correct. Resetting network settings clears the APN "
                    "configuration, mobile network settings, and all "
                    "wireless credentials. A corrupted APN entry or mobile "
                    "network configuration is a common cause of 'no mobile "
                    "network' when Wi-Fi and Bluetooth (separate subsystem) "
                    "still function. This is non-destructive to user data."
                ),
            },
            {
                "id": "b",
                "text": "Replace the SIM card because it must be faulty despite appearing physically intact",
                "correct": False,
                "rationale": (
                    "Incorrect. Wi-Fi and Bluetooth functioning rules out "
                    "a complete radio failure. SIM replacement is a valid "
                    "later step, but resetting network settings addresses "
                    "software-level APN/modem configuration issues first."
                ),
            },
            {
                "id": "c",
                "text": "Perform a factory reset as the operating system has been corrupted",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset is a last resort and causes "
                    "data loss. A software-level network settings reset "
                    "is far less disruptive and should be tried before "
                    "considering a full reset."
                ),
            },
            {
                "id": "d",
                "text": "Contact the carrier to provision a new SIM profile remotely",
                "correct": False,
                "rationale": (
                    "Incorrect. Remote SIM provisioning addresses "
                    "carrier-side account issues. The symptom (working after "
                    "seating, same carrier available to others nearby) "
                    "points to a device-side configuration issue, not a "
                    "carrier account problem."
                ),
            },
        ],
        "explanation": (
            "Mobile network unavailability with Wi-Fi/BT working often "
            "points to a corrupted APN (Access Point Name) configuration or "
            "modem firmware state. Resetting network settings restores APN "
            "defaults and clears modem state. If this fails, try manually "
            "entering the carrier's APN settings, then consider SIM "
            "replacement or a factory reset as escalation steps."
        ),
    },
    {
        "id": "c2d3v2-025",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user reports that their iPhone touchscreen registers taps "
            "in the wrong location — tapping the top-left of the screen "
            "activates icons in the lower-right. The issue persists after "
            "a reboot. The device was recently dropped. Which is the MOST "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The digitizer sustained physical damage from the drop, causing touch coordinate mapping to be inaccurate",
                "correct": True,
                "rationale": (
                    "Correct. Touch coordinate offset (tapping one area "
                    "registers elsewhere) is a classic symptom of digitizer "
                    "damage — either from physical impact or the digitizer "
                    "partially separating from the display assembly. "
                    "A reboot rules out a temporary software glitch. "
                    "Digitizer replacement is required."
                ),
            },
            {
                "id": "b",
                "text": "The display's color profile has shifted and is misrepresenting icon positions",
                "correct": False,
                "rationale": (
                    "Incorrect. Color profile changes affect visual rendering "
                    "but have no effect on touch input coordinates. Touch "
                    "input is handled by a separate digitizer layer, not the "
                    "display panel."
                ),
            },
            {
                "id": "c",
                "text": "iOS accessibility zoom is enabled and is offsetting touch targets",
                "correct": False,
                "rationale": (
                    "Incorrect. Accessibility zoom would produce a zoomed-in "
                    "view and you could verify it visually. A post-drop "
                    "offset on a normal-looking screen points to physical "
                    "digitizer damage, not an accessibility setting."
                ),
            },
            {
                "id": "d",
                "text": "The Touch ID sensor was damaged and is intercepting touch events",
                "correct": False,
                "rationale": (
                    "Incorrect. Touch ID handles biometric authentication "
                    "for the home button area only; it does not process "
                    "general display touch coordinates. Damage to Touch ID "
                    "would affect fingerprint unlock, not full-screen touch "
                    "accuracy."
                ),
            },
        ],
        "explanation": (
            "Touch coordinate offset after physical impact is diagnostic "
            "of digitizer damage. The digitizer is a thin glass/film layer "
            "overlaying the display that converts touch pressure/position "
            "into coordinates. Physical impact can crack it internally or "
            "cause it to shift. Resolution: digitizer or full display "
            "assembly replacement depending on the device model."
        ),
    },
    {
        "id": "c2d3v2-026",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A corporate Android device enrolled in MDM consistently shows "
            "a 'Storage is running low' notification. The device has "
            "128 GB storage with 96 GB used. MDM policy prevents users "
            "from deleting corporate apps. The device has no SD card slot. "
            "Which action is MOST appropriate for the technician?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clear the cache of large applications and enable cloud backup to offload photos and documents",
                "correct": True,
                "rationale": (
                    "Correct. Since corporate apps cannot be deleted by "
                    "policy and there is no SD slot, clearing app caches "
                    "(recovers non-essential temp data) and offloading "
                    "personal files (photos, documents) to cloud storage "
                    "(Google Drive, OneDrive) is the appropriate non-"
                    "destructive approach to reclaim space within MDM "
                    "constraints."
                ),
            },
            {
                "id": "b",
                "text": "Root the device to access the system partition and remove pre-installed apps",
                "correct": False,
                "rationale": (
                    "Incorrect. Rooting a corporate MDM-enrolled device is "
                    "a serious security policy violation. MDM solutions "
                    "detect rooted devices and will remotely wipe them. "
                    "This action is prohibited regardless of storage needs."
                ),
            },
            {
                "id": "c",
                "text": "Perform a factory reset to return the device to 128 GB free",
                "correct": False,
                "rationale": (
                    "Incorrect. A factory reset would wipe corporate data "
                    "and require re-enrollment in MDM. It is disproportionate "
                    "when the storage issue can be addressed by clearing "
                    "caches and moving personal files to the cloud."
                ),
            },
            {
                "id": "d",
                "text": "Disable MDM enrollment so the user can delete corporate apps manually",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing MDM enrollment violates corporate "
                    "security policy, exposes the device to unmanaged status, "
                    "and may trigger a remote wipe. The technician should "
                    "work within MDM constraints."
                ),
            },
        ],
        "explanation": (
            "Storage management on MDM-enrolled corporate devices requires "
            "working within policy constraints. Clearing app caches "
            "(Settings > Apps > select app > Storage > Clear Cache) "
            "reclaims space used by temporary files without deleting apps "
            "or data. Cloud backup of personal media (photos, documents) "
            "is the appropriate way to reclaim significant storage while "
            "respecting MDM policy."
        ),
    },
    {
        "id": "c2d3v2-027",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "An Android phone's GPS navigation app reports locations that "
            "are consistently 200–300 meters off from the user's actual "
            "position. The issue occurs outdoors in open areas. Wi-Fi "
            "location and cellular location appear to work roughly correctly. "
            "Which is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The GPS chip is receiving signals but has a poor satellite fix due to a hardware or antenna issue",
                "correct": True,
                "rationale": (
                    "Correct. A consistent 200–300 m GPS offset in open "
                    "areas (where Wi-Fi and cell triangulation, which have "
                    "lower accuracy, are approximately correct) suggests the "
                    "GPS chip is functioning but unable to obtain a precise "
                    "satellite fix — indicative of a weak GPS antenna or "
                    "partial chip failure. A correctly functioning GPS in "
                    "open air provides < 5 m accuracy."
                ),
            },
            {
                "id": "b",
                "text": "The navigation app's map data is outdated and shows old road positions",
                "correct": False,
                "rationale": (
                    "Incorrect. Map data inaccuracies would appear as wrong "
                    "street names or missing roads, not as a consistent "
                    "positional offset. The GPS coordinate reported by the "
                    "device itself is what is off by 200–300 m."
                ),
            },
            {
                "id": "c",
                "text": "Location Services is disabled for the navigation app specifically",
                "correct": False,
                "rationale": (
                    "Incorrect. If Location Services were disabled for the "
                    "app, it would receive no location data at all, not an "
                    "inaccurate position. A wrong-but-present position "
                    "indicates GPS is delivering data, just inaccurately."
                ),
            },
            {
                "id": "d",
                "text": "The time zone setting is wrong, causing GPS timestamp errors that offset position calculations",
                "correct": False,
                "rationale": (
                    "Incorrect. GPS position calculation relies on satellite "
                    "signal timing, not the device's local time zone setting. "
                    "Android's GPS uses UTC from the GPS satellites, not "
                    "the local clock for position calculation."
                ),
            },
        ],
        "explanation": (
            "GPS accuracy in open areas should be < 5 m with a good satellite "
            "fix. A consistent offset of 200–300 m suggests the device is "
            "falling back to assisted GPS (A-GPS) from cell towers or Wi-Fi "
            "due to a weak GPS antenna or chip issue. Test with a GPS "
            "diagnostic app (GPS Status, GPS Test) to confirm the number "
            "of locked satellites. Low satellite count or poor SNR "
            "confirms antenna or hardware degradation."
        ),
    },
    {
        "id": "c2d3v2-028",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's iPhone cannot send or receive iMessages, though "
            "SMS/MMS works fine. The Apple ID is signed in. Other iPhone "
            "users on the same Wi-Fi can use iMessage normally. Which TWO "
            "steps should the technician try FIRST? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Toggle iMessage off and back on in Settings > Messages",
                "correct": True,
                "rationale": (
                    "Correct. Toggling iMessage off and on forces the device "
                    "to re-register the Apple ID with Apple's iMessage "
                    "activation servers. This resolves the most common cause "
                    "of iMessage failure on a single device — a stale or "
                    "corrupted activation token."
                ),
            },
            {
                "id": "b",
                "text": "Sign out of Apple ID and sign back in to refresh the iMessage registration",
                "correct": True,
                "rationale": (
                    "Correct. Signing out of the Apple ID logs the device "
                    "out of all Apple services including iMessage. Signing "
                    "back in triggers a fresh activation, resolving issues "
                    "caused by expired or corrupted Apple ID session tokens "
                    "associated with iMessage."
                ),
            },
            {
                "id": "c",
                "text": "Replace the SIM card to re-register the phone number with Apple",
                "correct": False,
                "rationale": (
                    "Incorrect. iMessage uses Apple ID and the device's "
                    "Apple servers registration, not the SIM card directly. "
                    "SMS/MMS working confirms the SIM is functional. SIM "
                    "replacement would not affect iMessage activation."
                ),
            },
            {
                "id": "d",
                "text": "Reset the device to factory settings to clear the iMessage database",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset is a last resort that causes "
                    "significant data loss. The two toggle-based steps "
                    "resolve the vast majority of single-device iMessage "
                    "failures without data loss."
                ),
            },
        ],
        "explanation": (
            "iMessage failure on a single device while SMS/MMS works and "
            "other devices on the same network are fine indicates a device-"
            "level iMessage activation issue, not a network problem. "
            "Standard fixes: (1) toggle iMessage off/on (re-activates), "
            "(2) sign out/in to Apple ID (refreshes all service tokens). "
            "If both fail, check date/time accuracy (must be automatic) "
            "then contact Apple Support."
        ),
    },
    {
        "id": "c2d3v2-029",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone Wi-Fi disconnects every 5–10 minutes "
            "when the screen turns off. Wi-Fi works normally while the "
            "screen is on. Other devices stay connected on the same network. "
            "Which setting is MOST likely causing this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wi-Fi is set to disconnect during sleep/battery optimization to save power",
                "correct": True,
                "rationale": (
                    "Correct. Android power-saving features can configure "
                    "Wi-Fi to disconnect when the device sleeps to conserve "
                    "battery. The setting is typically under Settings > Wi-Fi "
                    "> Advanced > Keep Wi-Fi on during sleep (older Android) "
                    "or under battery optimization settings. Setting it to "
                    "'Always' or disabling Wi-Fi battery optimization keeps "
                    "the connection active with the screen off."
                ),
            },
            {
                "id": "b",
                "text": "The Wi-Fi router is using MAC address filtering that expires sessions every 10 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. MAC filter sessions do not have a time-based "
                    "expiry — they either allow or deny a MAC address "
                    "persistently. Other devices remaining connected on the "
                    "same network also rules out a router-side session "
                    "expiry affecting only this device."
                ),
            },
            {
                "id": "c",
                "text": "The phone's DHCP lease is expiring every 10 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard DHCP lease times are hours to days. "
                    "A 10-minute lease would be an extremely unusual router "
                    "configuration and would affect all clients, not just "
                    "this device."
                ),
            },
            {
                "id": "d",
                "text": "Airplane mode is being activated automatically by a scheduled task app",
                "correct": False,
                "rationale": (
                    "Incorrect. Most Android phones do not have built-in "
                    "scheduled Airplane mode. An app doing this would also "
                    "disable Bluetooth and cellular, and the symptom would "
                    "show as full connectivity loss, not just Wi-Fi."
                ),
            },
        ],
        "explanation": (
            "Android's aggressive battery optimization can disconnect Wi-Fi "
            "when the screen sleeps. The fix is in Settings > Battery > "
            "Battery Optimization > find the Wi-Fi/connectivity system app "
            "and set to 'Don't optimize,' or in Wi-Fi Advanced settings set "
            "'Keep Wi-Fi on during sleep' to Always. This is a common issue "
            "on power-optimized Android OEM builds (Samsung, Huawei, Xiaomi)."
        ),
    },
    {
        "id": "c2d3v2-030",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "After updating to a new Android OS version, a user's "
            "fingerprint sensor no longer works. The sensor hardware "
            "is physically undamaged. The user is prompted to set up "
            "fingerprints again but enrollment fails with an error. "
            "Which action should the technician recommend FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Delete all stored fingerprints and re-enroll after the OS update clears biometric data for security",
                "correct": True,
                "rationale": (
                    "Correct. A major Android OS update invalidates stored "
                    "biometric templates for security reasons. The OS clears "
                    "fingerprint data to prevent use of templates registered "
                    "under an older security model. The user must re-enroll "
                    "fingerprints after the update. Settings > Biometrics and "
                    "Security > Fingerprints > delete existing > re-enroll."
                ),
            },
            {
                "id": "b",
                "text": "Replace the fingerprint sensor hardware as it is incompatible with the new OS version",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware incompatibility after a software "
                    "update is unlikely for a built-in sensor. The OS clearing "
                    "biometric templates post-update is standard Android "
                    "security behavior — it is a software issue, not hardware."
                ),
            },
            {
                "id": "c",
                "text": "Downgrade the OS to restore fingerprint functionality",
                "correct": False,
                "rationale": (
                    "Incorrect. OS downgrading is rarely supported on Android "
                    "devices (locked bootloaders), causes data loss, and is "
                    "unnecessary. Re-enrollment after an update is the "
                    "expected and correct resolution."
                ),
            },
            {
                "id": "d",
                "text": "Disable Android Keystore and re-enable it to restore biometric enrollment capability",
                "correct": False,
                "rationale": (
                    "Incorrect. The Android Keystore cannot be user-disabled, "
                    "and this action would not address the biometric template "
                    "invalidation caused by the OS update. Re-enrollment "
                    "is the correct fix."
                ),
            },
        ],
        "explanation": (
            "Android OS major version updates commonly invalidate stored "
            "biometric (fingerprint/face) data as part of the security "
            "model — templates enrolled under an older security patch level "
            "are considered untrusted. This is expected behavior, not a bug "
            "or hardware failure. Simply re-enrolling fingerprints "
            "restores functionality."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.5 — Mobile app security troubleshooting  (7 questions)
    # -------------------------------------------------------------------------
    {
        "id": "c2d3v2-031",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "An iOS device being used for corporate email suddenly requests "
            "an unusual number of permissions: microphone, camera, contacts, "
            "and location, after a minor app update was installed. MDM "
            "shows the app passed the original App Store review. What is "
            "the GREATEST security concern?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The app update introduced malicious code after bypassing App Store review (a supply chain attack), requesting permissions to exfiltrate data",
                "correct": True,
                "rationale": (
                    "Correct. Even legitimate App Store apps can become "
                    "malicious after an update — a supply chain attack. "
                    "Sudden permission escalation after an update on a "
                    "corporate device is a major mobile security concern. "
                    "The app should be quarantined, the update reported to "
                    "Apple, and the device reviewed via MDM for data "
                    "exfiltration indicators."
                ),
            },
            {
                "id": "b",
                "text": "The app requires these permissions to enable multifactor authentication for corporate email",
                "correct": False,
                "rationale": (
                    "Incorrect. MFA email apps may legitimately request "
                    "camera (for QR scanning) and microphone (for voice "
                    "MFA), but requesting all four permissions in a minor "
                    "update is disproportionate and warrants investigation "
                    "before granting."
                ),
            },
            {
                "id": "c",
                "text": "iOS is prompting for permissions it already had; this is a display bug after the update",
                "correct": False,
                "rationale": (
                    "Incorrect. iOS does not re-prompt for previously granted "
                    "permissions after updates unless new permissions are "
                    "being requested. A prompt for new permissions post-update "
                    "means the app code changed to request them — a "
                    "meaningful security signal."
                ),
            },
            {
                "id": "d",
                "text": "MDM is requiring the app to re-declare permissions as part of compliance scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. MDM does not trigger iOS permission dialogs. "
                    "Permission prompts are generated by the app requesting "
                    "access via the iOS API. MDM can block or manage apps "
                    "but does not cause them to request new permissions."
                ),
            },
        ],
        "explanation": (
            "Post-update permission escalation is a red flag for supply "
            "chain attacks, where a legitimate app is compromised in its "
            "development pipeline or account takeover occurs for the developer. "
            "CompTIA lists bootleg apps and unexpected app behavior as "
            "key mobile security concerns. Response: deny the permissions, "
            "uninstall the updated version, report to Apple, and investigate "
            "via MDM logs for any data transmission activity."
        ),
    },
    {
        "id": "c2d3v2-032",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user's Android phone is showing ads in the notification bar "
            "from an app they installed three months ago that seemed "
            "legitimate. The app has no visible ad integration in its "
            "interface. Removing notification permission for the app in "
            "Settings stops the ads. What type of threat is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Adware using Android notification channels to deliver ads outside the app UI",
                "correct": True,
                "rationale": (
                    "Correct. Adware that abuses Android's notification "
                    "system channels is a known mobile security threat. "
                    "Apps can post notifications to the system tray "
                    "independently of their UI. Revoking notification "
                    "permission stops the ads but the app may still "
                    "exfiltrate data — full removal is recommended."
                ),
            },
            {
                "id": "b",
                "text": "The Android OS is delivering system notifications that mimic ads",
                "correct": False,
                "rationale": (
                    "Incorrect. Android system notifications do not contain "
                    "third-party ads. The fact that revoking one app's "
                    "notification permission stopped the ads confirms "
                    "the app is responsible."
                ),
            },
            {
                "id": "c",
                "text": "The mobile carrier is inserting ads into notification data packets",
                "correct": False,
                "rationale": (
                    "Incorrect. Carriers can inject ads into unencrypted "
                    "web traffic in some regions but cannot insert content "
                    "into Android's notification system, which is controlled "
                    "by the device's OS and apps."
                ),
            },
            {
                "id": "d",
                "text": "A browser push notification subscription is delivering ads from a website the user visited",
                "correct": False,
                "rationale": (
                    "Incorrect. Browser push notifications are sent through "
                    "the browser app's notification channel, not an "
                    "unrelated app's channel. The scenario specifies a "
                    "standalone app, not a browser subscription."
                ),
            },
        ],
        "explanation": (
            "Adware apps that abuse Android notification channels post ads "
            "through the system notification tray, making them hard to "
            "attribute to the source app. To identify the source app, "
            "long-press the notification to see which app sent it. "
            "Fix: revoke notification permission (stops ads) then uninstall "
            "the app completely. Run a scan to ensure no additional adware "
            "components were installed."
        ),
    },
    {
        "id": "c2d3v2-033",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "An employee reports their iPhone is slower than usual and the "
            "battery drains within 3 hours. Investigation reveals the "
            "device has an MDM profile installed by an unknown organization "
            "alongside the corporate MDM profile. The employee downloaded "
            "a 'free VPN' app from the App Store last week. What is the "
            "MOST likely explanation and best action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The free VPN app installed a rogue MDM profile to monitor or intercept traffic; remove the unauthorized profile via Settings > General > VPN & Device Management",
                "correct": True,
                "rationale": (
                    "Correct. Malicious or privacy-violating VPN apps "
                    "sometimes instruct users to install configuration "
                    "profiles (MDM or VPN profiles) that allow traffic "
                    "interception, content filtering, or app management. "
                    "An MDM profile from an unknown organization is a "
                    "critical security concern. It should be removed "
                    "immediately via Settings > General > VPN & Device "
                    "Management, and the app uninstalled."
                ),
            },
            {
                "id": "b",
                "text": "The corporate IT department installed a second MDM profile for additional policy enforcement",
                "correct": False,
                "rationale": (
                    "Incorrect. Corporate IT would communicate profile "
                    "deployments. An unknown organization's MDM profile "
                    "arriving the same week as a third-party app install "
                    "is a strong indicator of the app as the delivery "
                    "mechanism, not IT."
                ),
            },
            {
                "id": "c",
                "text": "Apple installed an additional profile as part of an iOS beta test program",
                "correct": False,
                "rationale": (
                    "Incorrect. Apple does not silently install MDM profiles "
                    "from unknown organizations. Beta programs require explicit "
                    "user enrollment with clearly labeled Apple profiles."
                ),
            },
            {
                "id": "d",
                "text": "The second MDM profile is a VPN configuration profile and poses no security risk",
                "correct": False,
                "rationale": (
                    "Incorrect. An MDM profile grants significant control "
                    "over the device — far beyond a simple VPN configuration "
                    "profile. An MDM from an unknown organization always "
                    "represents a security concern and should be removed."
                ),
            },
        ],
        "explanation": (
            "Some VPN and free utility apps for iOS instruct users to install "
            "configuration or MDM profiles that give the app operator "
            "device management capabilities. iOS > Settings > General > "
            "VPN & Device Management shows all installed profiles. An "
            "unrecognized MDM profile should be removed immediately. "
            "This represents a CompTIA-listed mobile security concern: "
            "unauthorized MDM/profile installation allowing traffic "
            "interception."
        ),
    },
    {
        "id": "c2d3v2-034",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "An Android user receives an SMS from their bank with a link to "
            "install a 'security update' APK. After installation, the user's "
            "bank account shows unauthorized transactions. The Google Play "
            "Store shows no recent banking app updates. What attack was "
            "used and what should the technician do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Smishing (SMS phishing) delivered a banking Trojan APK; immediately uninstall the APK, change banking credentials from a clean device, and follow the 7-step malware removal process",
                "correct": True,
                "rationale": (
                    "Correct. This is a smishing attack — an SMS-delivered "
                    "banking Trojan that impersonates a legitimate banking "
                    "update. The APK is malware. Immediate actions: "
                    "(1) uninstall the APK, (2) change banking passwords "
                    "and notify the bank from a clean device, (3) follow "
                    "the CompTIA malware removal steps including scanning "
                    "in safe mode or WinPE equivalent (Android safe mode)."
                ),
            },
            {
                "id": "b",
                "text": "The bank's legitimate SMS update mechanism has a bug causing unauthorized transactions; contact the bank's IT department",
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate banks never distribute app updates "
                    "via SMS-linked APKs outside the Play Store. This is "
                    "a textbook smishing / social engineering attack. Treating "
                    "it as a bank bug would delay critical remediation."
                ),
            },
            {
                "id": "c",
                "text": "The Play Store update mechanism is flawed; sideloading is an acceptable workaround",
                "correct": False,
                "rationale": (
                    "Incorrect. The Play Store is the secure distribution "
                    "channel for Android apps. Advising users to sideload "
                    "APKs from SMS links is dangerous guidance that directly "
                    "caused this incident."
                ),
            },
            {
                "id": "d",
                "text": "The banking app has a legitimate self-update mechanism that triggered the transactions inadvertently",
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate banking apps do not execute "
                    "financial transactions as part of a self-update. "
                    "The correlation between the smishing APK install "
                    "and unauthorized transactions is the clear causal link."
                ),
            },
        ],
        "explanation": (
            "Smishing (SMS phishing) delivering banking Trojans is a common "
            "mobile attack vector. The attacker impersonates a trusted entity "
            "(bank) to trick the user into installing a malicious APK. "
            "CompTIA-listed response: treat as malware, quarantine (step 2), "
            "scan in Android safe mode (step 4), change all account passwords "
            "from a clean device, and educate the user never to install apps "
            "from links in text messages."
        ),
    },
    {
        "id": "c2d3v2-035",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A company's MDM console shows that a corporate iPhone has been "
            "jailbroken. Which TWO security risks does a jailbroken corporate "
            "device introduce that are specifically listed as CompTIA mobile "
            "security concerns? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "MDM profiles and corporate security policies can be bypassed or removed by the device owner",
                "correct": True,
                "rationale": (
                    "Correct. Jailbreaking gives the user root access to iOS, "
                    "allowing MDM enrollment profiles and device management "
                    "policies to be removed without organizational authorization. "
                    "This is a CompTIA-listed concern: jailbreaking undermines "
                    "device management controls."
                ),
            },
            {
                "id": "b",
                "text": "Bootleg/third-party apps installed via Cydia can access corporate data stored in other apps",
                "correct": True,
                "rationale": (
                    "Correct. iOS's app sandbox normally prevents apps from "
                    "accessing each other's data. Jailbreaking removes the "
                    "sandbox boundary, allowing bootleg apps to read data "
                    "from corporate email, files, or credential stores. "
                    "CompTIA explicitly lists bootleg apps on jailbroken "
                    "devices as a mobile security concern."
                ),
            },
            {
                "id": "c",
                "text": "The device's cellular radio is permanently damaged by the jailbreak",
                "correct": False,
                "rationale": (
                    "Incorrect. Jailbreaking is a software modification and "
                    "does not cause hardware damage to the cellular radio. "
                    "This is a factually incorrect statement unrelated to "
                    "CompTIA security concerns."
                ),
            },
            {
                "id": "d",
                "text": "The battery life is reduced by 50% due to jailbreak processes running in the background",
                "correct": False,
                "rationale": (
                    "Incorrect. While jailbreak tweaks may somewhat affect "
                    "battery life, a fixed 50% reduction is not a cited "
                    "security concern. The security concerns are about data "
                    "integrity and policy enforcement, not battery efficiency."
                ),
            },
        ],
        "explanation": (
            "CompTIA A+ lists two key jailbreak/rooting security concerns: "
            "(1) MDM and corporate policies can be bypassed or removed, "
            "losing organizational control of the device; and (2) bootleg "
            "apps (installed via Cydia/alternative stores) bypass Apple's "
            "vetting process and can access the full file system, including "
            "data from corporate apps. The corporate response is remote "
            "wipe via MDM and device replacement with a non-jailbroken unit."
        ),
    },
    {
        "id": "c2d3v2-036",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user's Android phone is generating unexpected premium-rate "
            "SMS charges. The user has not sent any texts to short codes. "
            "Data usage logs show a background app sending periodic SMS "
            "messages via the Android SMS API. The app was downloaded from "
            "the Play Store six months ago and recently updated. Which type "
            "of threat BEST describes this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SMS Trojan that sends premium-rate texts without user knowledge to generate revenue for the attacker",
                "correct": True,
                "rationale": (
                    "Correct. An SMS Trojan silently sends texts to premium "
                    "numbers using the device's SMS API. The user is billed "
                    "by their carrier for the premium charges. This is a "
                    "CompTIA-listed mobile security concern. The trigger "
                    "is an app update that introduced the malicious SMS code "
                    "after passing an initial Play Store review."
                ),
            },
            {
                "id": "b",
                "text": "The carrier is incorrectly billing the user for subscription texts they signed up for",
                "correct": False,
                "rationale": (
                    "Incorrect. The Android SMS log confirms an app is "
                    "programmatically sending messages. This is not a billing "
                    "error — the device is actively generating the texts "
                    "without user input."
                ),
            },
            {
                "id": "c",
                "text": "A legitimate app feature is using SMS as a backup authentication channel",
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate authentication flows send SMS "
                    "to the user's own number and would be disclosed in "
                    "the app's permissions and usage description. Silent "
                    "background SMS to external premium numbers is not "
                    "a legitimate authentication behavior."
                ),
            },
            {
                "id": "d",
                "text": "The Android OS is automatically enrolling the device in a carrier premium service",
                "correct": False,
                "rationale": (
                    "Incorrect. The Android OS does not autonomously enroll "
                    "devices in premium carrier services. The SMS API requires "
                    "an app to initiate messages. The app is the source, "
                    "not the OS."
                ),
            },
        ],
        "explanation": (
            "SMS Trojans are a monetization malware type that silently sends "
            "texts to attacker-controlled premium short codes, generating "
            "per-message revenue. CompTIA identifies unexpected charges and "
            "unauthorized outgoing messages as mobile security symptoms. "
            "Fix: revoke SMS permission for the app, uninstall it, report "
            "to Google Play Protect, and contact the carrier for a "
            "refund on fraudulent charges."
        ),
    },
    {
        "id": "c2d3v2-037",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "An IT technician reviews MDM logs and finds that a corporate "
            "Android phone has USB debugging enabled and recently connected "
            "to an unknown computer via USB. The employee denies connecting "
            "to any personal computer. Corporate policy prohibits USB "
            "debugging on managed devices. What is the GREATEST risk this "
            "configuration creates, and what is the correct response?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ADB over USB allows an attacker with physical USB access to extract corporate data, install apps, or execute shell commands; disable USB debugging via MDM policy and investigate the unauthorized connection",
                "correct": True,
                "rationale": (
                    "Correct. ADB (Android Debug Bridge) enabled with USB "
                    "debugging allows anyone who connects via USB and whose "
                    "RSA key the device trusts to extract files, install "
                    "APKs, capture the screen, and run shell commands — all "
                    "without user confirmation. CompTIA lists USB debugging/"
                    "developer mode as a key mobile security concern. "
                    "The MDM should enforce a policy to disable it."
                ),
            },
            {
                "id": "b",
                "text": "USB debugging only allows device charging; the real risk is the unknown computer installing malware via Bluetooth",
                "correct": False,
                "rationale": (
                    "Incorrect. USB debugging is far more than charging — "
                    "it enables the full ADB interface (shell, file transfer, "
                    "app installation). The risk described is specifically "
                    "from the ADB-enabled USB connection, not Bluetooth."
                ),
            },
            {
                "id": "c",
                "text": "USB debugging is a standard corporate MDM feature and does not represent a security concern",
                "correct": False,
                "rationale": (
                    "Incorrect. USB debugging is explicitly a developer/debug "
                    "feature that bypasses many Android security controls. "
                    "CompTIA and most security frameworks classify it as a "
                    "significant risk on corporate devices and recommend "
                    "disabling it via MDM policy."
                ),
            },
            {
                "id": "d",
                "text": "The risk is negligible because ADB requires the device to be unlocked and the user to approve the connection",
                "correct": False,
                "rationale": (
                    "Incorrect. While ADB does require USB debugging to be "
                    "enabled and an initial 'Allow USB debugging?' approval, "
                    "once an RSA key is trusted, subsequent connections from "
                    "that computer proceed without additional prompts. An "
                    "attacker who previously got approval — or who connected "
                    "when the device was unlocked — can reconnect silently. "
                    "The risk is real and significant."
                ),
            },
        ],
        "explanation": (
            "ADB over USB on an enabled-debugging Android device is a "
            "CompTIA-listed mobile security concern (developer mode / USB "
            "debugging). An attacker with USB access and a trusted ADB key "
            "can: 'adb pull' to steal files, 'adb install' to sideload "
            "malware, 'adb shell' to run commands. Corporate MDM policy "
            "should set a restriction disabling developer options. "
            "The unauthorized USB connection requires forensic investigation "
            "to determine what data may have been accessed or exfiltrated."
        ),
    },
]
