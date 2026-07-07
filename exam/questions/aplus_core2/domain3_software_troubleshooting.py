"""
CompTIA A+ Core 2 (220-1202) — Domain 3: Software Troubleshooting
36 practice questions covering objectives 3.1 – 3.5.
"""

QUESTIONS = [
    # -------------------------------------------------------------------------
    # 3.3 — Malware Removal Best-Practice Process (7 steps) — 3 questions min
    # -------------------------------------------------------------------------
    {
        "id": "c2d3-001",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician has verified malware symptoms on a Windows PC. "
            "According to CompTIA's malware removal best practices, what "
            "should be done IMMEDIATELY NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Quarantine the infected system",
                "correct": True,
                "rationale": (
                    "Correct. After (1) investigating and verifying symptoms, "
                    "step (2) is to quarantine the infected system — disconnect "
                    "it from the network to stop spread before remediation."
                ),
            },
            {
                "id": "b",
                "text": "Remediate the system with anti-malware scans",
                "correct": False,
                "rationale": (
                    "Incorrect. Remediation is step 4; you must quarantine and "
                    "disable System Restore first to prevent spread and "
                    "reinfection via a shadow copy."
                ),
            },
            {
                "id": "c",
                "text": "Educate the end user",
                "correct": False,
                "rationale": (
                    "Incorrect. End-user education is the FINAL step (7), "
                    "performed only after the system has been cleaned and "
                    "hardened."
                ),
            },
            {
                "id": "d",
                "text": "Enable System Restore and create a restore point",
                "correct": False,
                "rationale": (
                    "Incorrect. You DISABLE System Restore early (step 3); "
                    "re-enabling it and creating a clean restore point is "
                    "step 6, near the end of the process."
                ),
            },
        ],
        "explanation": (
            "CompTIA malware removal order: 1) investigate and verify "
            "symptoms, 2) quarantine infected systems, 3) disable System "
            "Restore (Windows), 4) remediate (update anti-malware, scan in "
            "safe mode / preinstallation environment), 5) schedule scans and "
            "run updates, 6) re-enable System Restore and create a restore "
            "point, 7) educate the end user."
        ),
    },
    {
        "id": "c2d3-002",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "During malware remediation a technician notices that System "
            "Restore is still enabled. The technician has already quarantined "
            "the machine. What is the correct NEXT action before running "
            "anti-malware scans?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Create a new restore point so a clean baseline exists",
                "correct": False,
                "rationale": (
                    "Incorrect. Creating a restore point while malware is "
                    "present would capture an infected state, potentially "
                    "reinfecting the system if that point is later used."
                ),
            },
            {
                "id": "b",
                "text": "Disable System Restore to prevent malware hiding in shadow copies",
                "correct": True,
                "rationale": (
                    "Correct. Step 3 of the CompTIA process requires disabling "
                    "System Restore before scanning so malware cannot persist "
                    "inside Volume Shadow Copy snapshots and reinfect the "
                    "system after removal."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow to repair corrupted OS files first",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC is a repair tool used after malware has "
                    "been removed. Running it while malware is active may "
                    "produce unreliable results and could cause SFC to "
                    "overwrite clean files with infected ones cached by "
                    "the malware."
                ),
            },
            {
                "id": "d",
                "text": "Educate the user about safe browsing before scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. User education is the last step (7). The "
                    "immediate priority is to prevent the malware from "
                    "surviving remediation via a shadow copy."
                ),
            },
        ],
        "explanation": (
            "Step 3 — disabling System Restore — is critical because Volume "
            "Shadow Copies can harbor malware. After disabling it, the "
            "technician proceeds to step 4: update anti-malware definitions "
            "and scan in safe mode or a preinstallation environment."
        ),
    },
    {
        "id": "c2d3-003",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "After successfully removing malware from a Windows workstation, "
            "a technician has run full anti-malware scans, confirmed the "
            "system is clean, and scheduled recurring scans. According to "
            "CompTIA best practices, what are the correct NEXT TWO actions, "
            "in order?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Re-enable System Restore and create a restore point, then educate the end user",
                "correct": True,
                "rationale": (
                    "Correct. Step 6 is to re-enable System Restore and create "
                    "a known-good restore point. Step 7 — the final step — is "
                    "to educate the end user on how to avoid future infections."
                ),
            },
            {
                "id": "b",
                "text": "Quarantine the system again, then re-enable System Restore",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarantine (step 2) is performed at the "
                    "beginning of the process, not after remediation. The "
                    "system should be reconnected to the network at this stage, "
                    "not isolated again."
                ),
            },
            {
                "id": "c",
                "text": "Educate the end user, then create a restore point",
                "correct": False,
                "rationale": (
                    "Incorrect. The order matters: restore point creation "
                    "(step 6) comes before user education (step 7). Reversing "
                    "these steps does not follow CompTIA's documented sequence."
                ),
            },
            {
                "id": "d",
                "text": "Disable System Restore again, then schedule additional scans",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore should be RE-ENABLED at this "
                    "point — not disabled. Scheduling scans is step 5, which "
                    "has already been completed."
                ),
            },
        ],
        "explanation": (
            "Once remediation and scheduled scans are confirmed (steps 4–5), "
            "the technician re-enables System Restore and captures a "
            "known-clean restore point (step 6), then closes the interaction "
            "by educating the user (step 7) on avoiding phishing, suspicious "
            "downloads, and other infection vectors."
        ),
    },
    {
        "id": "c2d3-004",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "Which TWO actions are part of step 4 (Remediate infected systems) "
            "in CompTIA's seven-step malware removal process? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Update anti-malware definitions before scanning",
                "correct": True,
                "rationale": (
                    "Correct. Updating definitions is explicitly listed under "
                    "step 4 so the scanner recognizes current malware variants "
                    "before attempting removal."
                ),
            },
            {
                "id": "b",
                "text": "Run scans from safe mode or a preinstallation environment",
                "correct": True,
                "rationale": (
                    "Correct. Scanning from safe mode or a preinstallation "
                    "environment (e.g., Windows PE) prevents active malware "
                    "from interfering with the scanner or hiding in memory."
                ),
            },
            {
                "id": "c",
                "text": "Create a System Restore point immediately after scanning",
                "correct": False,
                "rationale": (
                    "Incorrect. Creating a restore point is step 6, after "
                    "scanning is complete, updates are scheduled (step 5), and "
                    "System Restore is re-enabled."
                ),
            },
            {
                "id": "d",
                "text": "Notify the end user about safe-browsing habits",
                "correct": False,
                "rationale": (
                    "Incorrect. End-user education is step 7, the last step of "
                    "the process, not part of the technical remediation phase."
                ),
            },
        ],
        "explanation": (
            "Step 4 remediation has two key sub-tasks: (a) update anti-malware "
            "software/definitions, and (b) use scanning techniques that bypass "
            "the running OS — safe mode or a preinstallation environment — so "
            "the malware cannot evade detection."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.1 — Windows OS Troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3-005",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A user reports a Blue Screen of Death (BSOD) with the stop code "
            "MEMORY_MANAGEMENT. The system has been stable for two years. No "
            "new software was installed, but a RAM module was recently reseated "
            "after a cleaning session. Which action should the technician "
            "perform FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run Windows Memory Diagnostic (mdsched.exe) to test RAM",
                "correct": True,
                "rationale": (
                    "Correct. The MEMORY_MANAGEMENT stop code points directly "
                    "to RAM issues. Since RAM was recently reseated, testing it "
                    "with mdsched.exe is the most targeted first step to confirm "
                    "hardware fault."
                ),
            },
            {
                "id": "b",
                "text": "Run SFC /scannow to repair corrupted system files",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC repairs OS file corruption but does not "
                    "diagnose RAM hardware problems. MEMORY_MANAGEMENT BSODs "
                    "after reseating RAM strongly indicate a hardware cause."
                ),
            },
            {
                "id": "c",
                "text": "Use DISM /RestoreHealth to repair the Windows image",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM repairs the Windows component store and is "
                    "used when SFC finds unfixable corruption. It does not "
                    "address RAM hardware faults."
                ),
            },
            {
                "id": "d",
                "text": "Boot into safe mode and uninstall recently updated drivers",
                "correct": False,
                "rationale": (
                    "Incorrect. No new drivers were mentioned; the trigger was "
                    "physical RAM reseating. Driver removal would not address "
                    "a possible bad RAM seating or failing module."
                ),
            },
        ],
        "explanation": (
            "MEMORY_MANAGEMENT BSODs combined with recent RAM physical "
            "manipulation warrant immediate RAM testing. mdsched.exe runs at "
            "next boot and performs extended memory tests. If RAM passes, "
            "follow up with SFC / DISM to rule out OS corruption."
        ),
    },
    {
        "id": "c2d3-006",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A Windows 11 workstation displays 'An operating system wasn't "
            "found' after a power outage. The BIOS detects the SSD. The drive "
            "appears healthy in another machine. Which tool should the "
            "technician use to repair the boot configuration?"
        ),
        "options": [
            {
                "id": "a",
                "text": "bootrec /fixmbr and bootrec /fixboot from the Windows Recovery Environment",
                "correct": True,
                "rationale": (
                    "Correct. 'No OS found' with a visible, healthy drive "
                    "typically indicates a corrupt Master Boot Record or "
                    "Boot Configuration Data. bootrec /fixmbr rewrites the MBR "
                    "and bootrec /fixboot writes a new boot sector; "
                    "bootrec /rebuildbcd can then re-add the OS entry."
                ),
            },
            {
                "id": "b",
                "text": "Run DISM /Online /RestoreHealth from the Windows Recovery Environment",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM /Online requires a running Windows "
                    "instance. In WinRE without a bootable OS, this flag will "
                    "fail; and DISM targets the component store, not boot "
                    "sector data."
                ),
            },
            {
                "id": "c",
                "text": "Use msconfig to change the default boot entry",
                "correct": False,
                "rationale": (
                    "Incorrect. msconfig requires Windows to be running; it "
                    "cannot operate when the system cannot boot to the OS "
                    "selection screen."
                ),
            },
            {
                "id": "d",
                "text": "Perform a System Restore from the Windows Recovery Environment",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore can fix software-level problems "
                    "but cannot repair a missing or corrupt boot sector, which "
                    "is the most likely cause of 'No OS found' with a healthy "
                    "drive."
                ),
            },
        ],
        "explanation": (
            "'An operating system wasn't found' with an otherwise healthy, "
            "BIOS-detected drive points to a corrupted boot sector or BCD "
            "store — a common power-outage result. Booting from Windows "
            "installation media into WinRE and running bootrec commands "
            "(fixmbr, fixboot, rebuildbcd) is the standard resolution."
        ),
    },
    {
        "id": "c2d3-007",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "After a Windows Update, users report that a critical business "
            "application crashes immediately on launch. The application ran "
            "perfectly before the update. Other applications are unaffected. "
            "Which solution is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Roll back the Windows Update through Settings > Update & Security > View Update History",
                "correct": True,
                "rationale": (
                    "Correct. Rolling back the specific update that caused the "
                    "regression is the fastest, least-disruptive fix when a "
                    "single application breaks immediately after a known update."
                ),
            },
            {
                "id": "b",
                "text": "Repair the application using its installer with the 'Repair' option",
                "correct": False,
                "rationale": (
                    "Incorrect. Repairing the application does not address a "
                    "change in the OS environment (the update). The root cause "
                    "is the update, not the application's own files."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow to restore system files modified by the update",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC repairs corrupted/missing protected OS "
                    "files but does not revert intentional changes made by "
                    "Windows Updates. It would not restore the pre-update state."
                ),
            },
            {
                "id": "d",
                "text": "Reimage the workstation with the latest corporate image",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging is the last resort for software "
                    "issues. Rolling back the update is far less disruptive "
                    "and directly addresses the root cause."
                ),
            },
        ],
        "explanation": (
            "When a Windows Update directly causes application regression, "
            "rolling back that specific update (Settings > Windows Update > "
            "Update History > Uninstall updates) restores the prior working "
            "state without full reimaging. If the update is mandatory, "
            "contacting the application vendor for a compatible version is "
            "the next step."
        ),
    },
    {
        "id": "c2d3-008",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A technician runs SFC /scannow and receives the message: "
            "'Windows Resource Protection found corrupt files but was unable "
            "to fix some of them.' Which command should be run NEXT to attempt "
            "deeper repair?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DISM /Online /Cleanup-Image /RestoreHealth",
                "correct": True,
                "rationale": (
                    "Correct. When SFC cannot repair files, the Windows "
                    "component store itself may be corrupted. DISM "
                    "/RestoreHealth repairs the component store from Windows "
                    "Update or a mounted image, after which SFC can often "
                    "complete successfully on a second run."
                ),
            },
            {
                "id": "b",
                "text": "chkdsk /f /r on the system drive",
                "correct": False,
                "rationale": (
                    "Incorrect. chkdsk repairs file-system-level disk errors "
                    "and bad sectors. While useful for drive health, it does "
                    "not repair the Windows component store that SFC relies on."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow a second time immediately",
                "correct": False,
                "rationale": (
                    "Incorrect. Re-running SFC without first repairing the "
                    "component store with DISM will likely produce the same "
                    "'unable to fix' result, as the source files SFC uses "
                    "are still corrupted."
                ),
            },
            {
                "id": "d",
                "text": "Roll back the most recent Windows Update",
                "correct": False,
                "rationale": (
                    "Incorrect. Rolling back updates addresses regression "
                    "issues but does not repair a corrupted component store. "
                    "DISM must be used to restore a healthy component store "
                    "before SFC can succeed."
                ),
            },
        ],
        "explanation": (
            "SFC /scannow depends on the Windows component store (WinSxS). "
            "When SFC cannot fix files, DISM /Online /Cleanup-Image "
            "/RestoreHealth pulls correct files from Windows Update to repair "
            "the component store. After DISM succeeds, running SFC again "
            "typically resolves the remaining corruption."
        ),
    },
    {
        "id": "c2d3-009",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows user logs in and receives a message that their profile "
            "could not be loaded; they are signed in with a temporary profile. "
            "Files saved to the desktop disappear after logout. What is the "
            "BEST remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rebuild the Windows user profile by creating a new profile and migrating data",
                "correct": True,
                "rationale": (
                    "Correct. A corrupted user profile requires rebuilding: "
                    "create a new local or domain profile, copy personal data "
                    "(Desktop, Documents, AppData) from the old profile folder, "
                    "and re-link or log in with the new profile."
                ),
            },
            {
                "id": "b",
                "text": "Run DISM /RestoreHealth to fix the corrupted profile",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM repairs the Windows component store, not "
                    "user profile hives (NTUSER.DAT). A corrupt profile "
                    "requires profile-level intervention."
                ),
            },
            {
                "id": "c",
                "text": "Perform a System Restore to a point before the profile corruption",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore targets OS configuration and "
                    "registry settings; it does not restore user profile "
                    "data (documents, AppData) and may overwrite unrelated "
                    "recent changes."
                ),
            },
            {
                "id": "d",
                "text": "Delete the temporary profile registry key and reboot",
                "correct": False,
                "rationale": (
                    "Incorrect. Deleting only the temp profile key may "
                    "regenerate a fresh empty profile but does not recover "
                    "the user's existing data or fix the underlying corruption "
                    "in the original profile hive."
                ),
            },
        ],
        "explanation": (
            "Temporary profile sign-in indicates the original NTUSER.DAT "
            "hive is corrupted or locked. The correct fix is to rebuild the "
            "profile: rename or delete the corrupted profile folder "
            "(%SystemDrive%\\Users\\<user>), allow Windows to recreate it on "
            "next login, then migrate personal data from the backup copy."
        ),
    },
    {
        "id": "c2d3-010",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A PC running Windows 10 spontaneously reboots during startup "
            "and enters a reboot loop. The technician needs to access "
            "advanced startup options. Which key or method allows the "
            "technician to access the Windows Recovery Environment (WinRE) "
            "without installation media?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Allow Windows to fail to boot three consecutive times to trigger Automatic Repair",
                "correct": True,
                "rationale": (
                    "Correct. After three consecutive failed boot attempts, "
                    "Windows 10/11 automatically launches the WinRE / "
                    "Automatic Repair screen, providing access to Startup "
                    "Repair, Command Prompt, System Restore, and other tools "
                    "without installation media."
                ),
            },
            {
                "id": "b",
                "text": "Press F8 during startup to access the legacy Advanced Boot Options menu",
                "correct": False,
                "rationale": (
                    "Incorrect. F8 was used in Windows 7 and earlier. On "
                    "Windows 10 with fast SSD boot times, F8 is effectively "
                    "disabled by default and will not reliably open the "
                    "Advanced Boot Options menu."
                ),
            },
            {
                "id": "c",
                "text": "Hold Shift and press F10 at the login screen",
                "correct": False,
                "rationale": (
                    "Incorrect. Shift+F10 opens a Command Prompt during "
                    "Windows Setup from installation media, not from the "
                    "normal boot cycle. It cannot be used during a boot loop."
                ),
            },
            {
                "id": "d",
                "text": "Boot from a USB Linux live environment and run Windows repair tools",
                "correct": False,
                "rationale": (
                    "Incorrect. A Linux live environment cannot run native "
                    "Windows recovery tools such as Startup Repair, bootrec, "
                    "or System Restore."
                ),
            },
        ],
        "explanation": (
            "Windows 10/11 monitors boot health and after three consecutive "
            "failed boots enters Automatic Repair mode, launching WinRE. "
            "From there, Startup Repair, System Restore, Command Prompt "
            "(bootrec, SFC, DISM), and boot settings are all accessible "
            "without installation media."
        ),
    },
    {
        "id": "c2d3-011",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A workstation exhibits sluggish performance. Task Manager shows "
            "CPU at 15%, RAM at 40%, and disk at 100%. Which Windows tool "
            "provides the BEST detailed view of which process is causing "
            "excessive disk I/O?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Resource Monitor (resmon.exe)",
                "correct": True,
                "rationale": (
                    "Correct. Resource Monitor's Disk tab shows per-process "
                    "read/write bytes per second and response times, making "
                    "it the best built-in tool to pinpoint the process "
                    "responsible for 100% disk utilization."
                ),
            },
            {
                "id": "b",
                "text": "Performance Monitor (perfmon.exe)",
                "correct": False,
                "rationale": (
                    "Incorrect. Performance Monitor is excellent for logging "
                    "counters over time but requires manual counter setup and "
                    "does not show real-time per-process disk I/O as quickly "
                    "or intuitively as Resource Monitor."
                ),
            },
            {
                "id": "c",
                "text": "Event Viewer (eventvwr.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. Event Viewer records system and application "
                    "log events; it does not display real-time disk I/O "
                    "statistics or identify which process is stressing "
                    "the disk."
                ),
            },
            {
                "id": "d",
                "text": "Device Manager (devmgmt.msc)",
                "correct": False,
                "rationale": (
                    "Incorrect. Device Manager manages hardware drivers and "
                    "devices. It does not provide process-level disk "
                    "utilization data."
                ),
            },
        ],
        "explanation": (
            "A 100% disk utilization with low CPU/RAM suggests a process is "
            "performing excessive I/O (e.g., Windows Search indexing, "
            "Superfetch/SysMain, Windows Update). Resource Monitor "
            "(resmon.exe) > Disk tab pinpoints the offending process with "
            "real-time read/write rates."
        ),
    },
    {
        "id": "c2d3-012",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows PC clock consistently drifts behind by 10–15 minutes "
            "per day despite being on a domain. Other domain computers "
            "maintain accurate time. What is the MOST likely cause specific "
            "to this workstation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The CMOS battery is failing and cannot maintain RTC time",
                "correct": True,
                "rationale": (
                    "Correct. A failing CMOS (real-time clock) battery causes "
                    "the hardware clock to lose time consistently. Domain "
                    "machines sync via W32tm, but if the hardware clock drifts "
                    "too far between syncs, time skew accumulates — especially "
                    "after power loss."
                ),
            },
            {
                "id": "b",
                "text": "The Windows Time Service (W32tm) is misconfigured on the domain controller",
                "correct": False,
                "rationale": (
                    "Incorrect. If the domain controller's W32tm were "
                    "misconfigured, all domain members would show the same "
                    "time drift, not just this one workstation."
                ),
            },
            {
                "id": "c",
                "text": "The network adapter is blocking NTP packets on UDP 123",
                "correct": False,
                "rationale": (
                    "Incorrect. A firewall blocking NTP would prevent time "
                    "sync entirely (large jump errors), not cause a gradual "
                    "consistent drift, and other symptoms such as "
                    "authentication failures would likely be present."
                ),
            },
            {
                "id": "d",
                "text": "The operating system is set to a wrong time zone",
                "correct": False,
                "rationale": (
                    "Incorrect. A wrong time zone causes a constant offset "
                    "(e.g., always 5 hours off) not a gradual daily drift "
                    "of 10–15 minutes."
                ),
            },
        ],
        "explanation": (
            "Consistent daily time drift on a single domain workstation, "
            "while all others are accurate, is a classic sign of a failing "
            "CMOS battery. The RTC loses charge and cannot maintain accurate "
            "time between boots or during sleep states. Replacing the CMOS "
            "battery and re-syncing time resolves the issue."
        ),
    },
    {
        "id": "c2d3-013",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A user reports that their USB hub shows a yellow warning in "
            "Device Manager reading 'USB Controller — Not enough USB "
            "controller resources.' All USB ports stop functioning after "
            "connecting a high-speed USB 3.0 device. Which action BEST "
            "resolves this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Connect the USB 3.0 device directly to a rear motherboard USB 3.0 port instead of the hub",
                "correct": True,
                "rationale": (
                    "Correct. USB hubs share bandwidth and interrupt resources "
                    "of the controller. High-speed USB 3.0 devices consume "
                    "more controller resources. Plugging directly into the "
                    "native controller port bypasses the hub's resource "
                    "contention and resolves the warning."
                ),
            },
            {
                "id": "b",
                "text": "Disable and re-enable the USB controller in Device Manager",
                "correct": False,
                "rationale": (
                    "Incorrect. Toggling the controller will temporarily reset "
                    "ports but does not address the root cause — too many "
                    "devices sharing limited controller resources through "
                    "the hub."
                ),
            },
            {
                "id": "c",
                "text": "Update the USB controller driver from the manufacturer's website",
                "correct": False,
                "rationale": (
                    "Incorrect. The issue is a hardware resource allocation "
                    "problem (endpoints/bandwidth), not a driver bug. A driver "
                    "update would not increase the physical resource capacity "
                    "of the USB controller."
                ),
            },
            {
                "id": "d",
                "text": "Run SFC /scannow to repair USB-related system files",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC repairs Windows protected system files. "
                    "A USB resource exhaustion warning is a hardware/resource "
                    "allocation issue unrelated to OS file corruption."
                ),
            },
        ],
        "explanation": (
            "USB controllers have a finite number of endpoints. Each USB "
            "device claims endpoints; high-speed USB 3.0 devices claim more. "
            "A hub compounds the problem by multiplexing many devices through "
            "one controller port. Connecting bandwidth-hungry devices directly "
            "to native controller ports reduces hub resource contention."
        ),
    },
    {
        "id": "c2d3-014",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A technician needs to configure a Windows PC to boot only "
            "essential services and Microsoft services to isolate whether "
            "a third-party service is causing system instability. Which "
            "tool and configuration accomplish this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "msconfig > Services tab: hide Microsoft services, disable all remaining; Startup tab: open Task Manager to disable startup items",
                "correct": True,
                "rationale": (
                    "Correct. msconfig's Services tab with 'Hide all Microsoft "
                    "services' checked and then 'Disable all' performs a clean "
                    "boot that loads only Microsoft services, isolating "
                    "third-party service conflicts. Startup items are managed "
                    "via Task Manager in Windows 10/11."
                ),
            },
            {
                "id": "b",
                "text": "Boot into Safe Mode with Networking from the Windows Recovery Environment",
                "correct": False,
                "rationale": (
                    "Incorrect. Safe mode disables most drivers and services "
                    "but does not allow selective enabling of specific services "
                    "for isolation testing. Clean boot via msconfig is the "
                    "correct method for systematic third-party service "
                    "isolation."
                ),
            },
            {
                "id": "c",
                "text": "Use services.msc to set all services to Manual startup and reboot",
                "correct": False,
                "rationale": (
                    "Incorrect. Manually setting all services to Manual "
                    "including Microsoft services would break Windows "
                    "functionality. msconfig's 'Hide Microsoft services' "
                    "option is the safe, targeted approach."
                ),
            },
            {
                "id": "d",
                "text": "Use the System Configuration Diagnostic startup mode",
                "correct": False,
                "rationale": (
                    "Incorrect. Diagnostic startup loads basic devices and "
                    "services only — similar to safe mode — and does not "
                    "support selective enabling/disabling for systematic "
                    "isolation. Selective startup is the correct mode."
                ),
            },
        ],
        "explanation": (
            "A clean boot in Windows uses msconfig (Selective startup) with "
            "Microsoft services hidden and all third-party services disabled. "
            "If stability improves, services are re-enabled in batches to "
            "identify the culprit. This is the CompTIA-recommended method "
            "for isolating service-caused system instability."
        ),
    },
    {
        "id": "c2d3-015",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A Windows service that a business-critical application depends "
            "on fails to start after every reboot. The Event Log shows "
            "error 1053: 'The service did not respond to the start or "
            "control request in a timely fashion.' The service starts "
            "successfully when started manually. What is the MOST likely "
            "cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A dependent service or driver that the application service relies on is not yet started when Windows initializes this service",
                "correct": True,
                "rationale": (
                    "Correct. Error 1053 at boot often occurs when a service "
                    "starts before its dependency (network, database, another "
                    "service) is ready. Setting the service to Automatic "
                    "(Delayed Start) or correcting the dependency order in "
                    "services.msc resolves this."
                ),
            },
            {
                "id": "b",
                "text": "The service executable is corrupted and needs reinstallation",
                "correct": False,
                "rationale": (
                    "Incorrect. If the executable were corrupted, the service "
                    "would also fail to start manually. Since manual start "
                    "succeeds, the executable is intact; the issue is a "
                    "timing/dependency problem."
                ),
            },
            {
                "id": "c",
                "text": "The service account password has expired, blocking automatic authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. A password expiry would produce a logon "
                    "failure error (1069), not a timeout error (1053). Also, "
                    "a password issue would affect manual starts as well."
                ),
            },
            {
                "id": "d",
                "text": "Windows Defender is quarantining the service executable on boot",
                "correct": False,
                "rationale": (
                    "Incorrect. A quarantined executable would show a security "
                    "alert, the file would be inaccessible, and the service "
                    "would also fail to start manually."
                ),
            },
        ],
        "explanation": (
            "Error 1053 at boot with successful manual start is a classic "
            "service dependency timing issue. Setting the service to "
            "'Automatic (Delayed Start)' gives Windows and dependent "
            "services time to initialize. Alternatively, add the required "
            "dependency in the service's properties under 'Dependencies'."
        ),
    },
    {
        "id": "c2d3-016",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A technician is troubleshooting a Windows PC with extremely "
            "slow login times (profile load takes 3–5 minutes). The issue "
            "affects only domain users on this one workstation. Which TWO "
            "actions should the technician take to diagnose or resolve "
            "this? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check for a corrupt or oversized roaming profile and rebuild the local profile",
                "correct": True,
                "rationale": (
                    "Correct. Slow profile loads on a single machine with "
                    "domain accounts often indicate a large or corrupted "
                    "roaming profile. Rebuilding the local profile copy "
                    "and/or cleaning up the profile size resolves the "
                    "load delay."
                ),
            },
            {
                "id": "b",
                "text": "Run gpresult /r to check for Group Policy processing delays or misconfigured logon scripts",
                "correct": True,
                "rationale": (
                    "Correct. Group Policy logon scripts or poorly scoped "
                    "GPOs can dramatically slow logins. gpresult /r shows "
                    "applied policies and can reveal a slow-processing GPO "
                    "or logon script causing the delay."
                ),
            },
            {
                "id": "c",
                "text": "Run DISM /RestoreHealth to repair Windows OS files",
                "correct": False,
                "rationale": (
                    "Incorrect. DISM /RestoreHealth repairs the Windows "
                    "component store and is not relevant to profile load "
                    "timing caused by roaming profile size or GPO delays."
                ),
            },
            {
                "id": "d",
                "text": "Replace the user's password with a shorter one to speed up Kerberos authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Password length has negligible impact on "
                    "Kerberos ticket acquisition time. This action does not "
                    "address profile load or GPO processing delays."
                ),
            },
        ],
        "explanation": (
            "Slow domain profile loads on a single workstation point to "
            "roaming profile issues (size, corruption, network path latency) "
            "or GPO/logon script problems. Checking profile size/corruption "
            "and reviewing gpresult output are the two most targeted "
            "diagnostic actions."
        ),
    },
    {
        "id": "c2d3-017",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows OS troubleshooting",
        "stem": (
            "A user experiences frequent unexpected shutdowns on a Windows "
            "laptop. The shutdowns occur during CPU-intensive tasks. The "
            "system logs show no BSOD, and the OS appears healthy. What is "
            "the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Overheating causing the system's thermal protection to force shutdown",
                "correct": True,
                "rationale": (
                    "Correct. Shutdowns during CPU-intensive tasks without "
                    "BSOD or OS errors are classic thermal protection "
                    "shutdowns. The CPU or GPU exceeds safe temperature "
                    "thresholds and the firmware shuts down the system to "
                    "prevent damage."
                ),
            },
            {
                "id": "b",
                "text": "Corrupted Windows system files causing the OS to crash",
                "correct": False,
                "rationale": (
                    "Incorrect. OS file corruption typically causes BSODs or "
                    "application errors, not clean thermal-style shutdowns "
                    "with no stop code. The logs would reflect OS-level "
                    "errors."
                ),
            },
            {
                "id": "c",
                "text": "Malware scheduling shutdowns via the Windows Task Scheduler",
                "correct": False,
                "rationale": (
                    "Incorrect. Task Scheduler-triggered shutdowns would "
                    "occur at scheduled times, not specifically during "
                    "high CPU load. Load correlation strongly suggests "
                    "thermal throttling or protection."
                ),
            },
            {
                "id": "d",
                "text": "The power plan is set to power saver, restricting CPU performance",
                "correct": False,
                "rationale": (
                    "Incorrect. Power Saver throttles CPU speed to reduce heat "
                    "and consumption but does not force system shutdowns. "
                    "Throttling would manifest as slowness, not abrupt "
                    "poweroffs."
                ),
            },
        ],
        "explanation": (
            "Thermal protection shutdowns occur when the processor or GPU "
            "temperature exceeds safe limits — common on laptops with clogged "
            "vents or dried thermal paste. Check HWMonitor or similar tools "
            "for temperatures, clean the cooling system, and replace thermal "
            "compound as needed."
        ),
    },
    {
        "id": "c2d3-018",
        "domain": 3,
        "objective": "3.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Windows boot troubleshooting",
        "stem": (
            "A technician is troubleshooting a Windows workstation that "
            "frequently shows a BSOD with stop code IRQL_NOT_LESS_OR_EQUAL "
            "after installing a new third-party graphics card driver. "
            "Which action should be taken FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Boot into safe mode and roll back the graphics driver",
                "correct": True,
                "rationale": (
                    "Correct. IRQL_NOT_LESS_OR_EQUAL is typically caused by "
                    "a driver accessing memory at an incorrect interrupt "
                    "request level. Since the BSOD started after a driver "
                    "install, rolling back the driver in safe mode (where "
                    "the problematic driver won't load) is the correct "
                    "first action."
                ),
            },
            {
                "id": "b",
                "text": "Replace the graphics card with a known-good unit",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware replacement is premature. The BSOD "
                    "appeared after a driver change, not a hardware change, "
                    "so rolling back the driver is the logical first step "
                    "before considering hardware."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow in safe mode to repair system files",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC repairs OS file corruption. "
                    "IRQL_NOT_LESS_OR_EQUAL after a driver install is a "
                    "driver problem, not an OS file problem. SFC would not "
                    "address a misbehaving driver."
                ),
            },
            {
                "id": "d",
                "text": "Perform a System Restore to before the driver installation",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore would work, but rolling back "
                    "only the driver in safe mode is less disruptive and more "
                    "surgical — System Restore affects all changes since the "
                    "restore point, not just the driver."
                ),
            },
        ],
        "explanation": (
            "IRQL_NOT_LESS_OR_EQUAL BSODs after driver installs indicate the "
            "driver is making illegal memory accesses at the wrong interrupt "
            "level. Safe mode loads only essential drivers, allowing the new "
            "driver to be rolled back via Device Manager > Driver > Roll Back "
            "Driver without triggering the BSOD."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.2 — PC Security Issue Troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3-019",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A Windows workstation can access local network shares but cannot "
            "browse the internet or reach any external IP address. A ping to "
            "8.8.8.8 fails. Other workstations on the same subnet have no "
            "issues. The user has never reported this problem before. "
            "Anti-malware scans are clean. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malware has modified the Windows hosts file or added a malicious static route to block internet traffic",
                "correct": True,
                "rationale": (
                    "Correct. Malware commonly modifies %SystemRoot%\\System32\\"
                    "drivers\\etc\\hosts or adds static routes (route add) to "
                    "block security update sites or all internet traffic while "
                    "leaving LAN access intact. This is a known PC security "
                    "symptom: 'unable to access network' (specifically internet)."
                ),
            },
            {
                "id": "b",
                "text": "The network adapter's duplex setting is mismatched with the switch port",
                "correct": False,
                "rationale": (
                    "Incorrect. A duplex mismatch causes poor performance and "
                    "packet loss for ALL network traffic, not selective blocking "
                    "of internet while local shares work fine."
                ),
            },
            {
                "id": "c",
                "text": "The ISP has blocked this workstation's MAC address",
                "correct": False,
                "rationale": (
                    "Incorrect. ISPs operate at the WAN level and see the "
                    "router's MAC address, not individual workstation MACs. "
                    "An ISP block would affect the entire site."
                ),
            },
            {
                "id": "d",
                "text": "Windows Firewall is blocking outbound ICMP traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. Windows Firewall blocking outbound ICMP would "
                    "prevent ping to 8.8.8.8 but would not block all internet "
                    "TCP/UDP traffic. The symptom of complete internet failure "
                    "with working LAN is broader than ICMP filtering."
                ),
            },
        ],
        "explanation": (
            "Unable to reach the internet while LAN works is a CompTIA-listed "
            "PC security symptom. Common malware techniques include hosts file "
            "poisoning (redirecting domains to 127.0.0.1) and injecting static "
            "routes to null the default gateway for external traffic. Check "
            "the hosts file and run 'route print' to detect malicious entries."
        ),
    },
    {
        "id": "c2d3-020",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user reports that their web browser is displaying a persistent "
            "security certificate warning for their company's internal website, "
            "which previously worked fine. The certificate is issued by the "
            "company's internal CA. Other users on the same network have no "
            "issue. Which is the MOST likely cause on this specific workstation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The company's internal CA root certificate has been removed from the workstation's Trusted Root CA store",
                "correct": True,
                "rationale": (
                    "Correct. If the internal CA root certificate is missing "
                    "from the local machine's Trusted Root Certification "
                    "Authorities store, the browser cannot build a trust chain "
                    "to the internal site's certificate, producing a warning. "
                    "Other users whose stores are intact would not be affected."
                ),
            },
            {
                "id": "b",
                "text": "The internal website's SSL certificate has expired",
                "correct": False,
                "rationale": (
                    "Incorrect. An expired server certificate would affect ALL "
                    "users hitting that site, not just one workstation. The "
                    "issue is isolated to one machine, pointing to a local "
                    "trust store problem."
                ),
            },
            {
                "id": "c",
                "text": "The browser's cache contains a stale copy of the old certificate",
                "correct": False,
                "rationale": (
                    "Incorrect. Certificate cache issues are rare and would "
                    "typically resolve after clearing the browser cache. More "
                    "importantly, they would not produce a persistent trust "
                    "warning; the browser validates the live certificate from "
                    "the server each session."
                ),
            },
            {
                "id": "d",
                "text": "The web server is sending an incomplete certificate chain",
                "correct": False,
                "rationale": (
                    "Incorrect. An incomplete chain on the server side would "
                    "affect all clients. The fact that only this workstation "
                    "is affected means the server configuration is fine and "
                    "the problem is local."
                ),
            },
        ],
        "explanation": (
            "Browser certificate warnings for internal sites on a single "
            "machine — while others work — indicate the local Trusted Root "
            "CA store is missing the internal CA certificate. This can happen "
            "due to Group Policy not applying, manual deletion, or malware. "
            "Fix: redeploy the CA root certificate via GPO or manually "
            "import it into the machine's certificate store."
        ),
    },
    {
        "id": "c2d3-021",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Browser security symptoms",
        "stem": (
            "A user reports that every time they search Google, they are "
            "redirected to an unfamiliar search engine. The browser homepage "
            "has also changed without the user's action. No other users on "
            "the network are affected. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A browser hijacker has modified the browser's search engine and homepage settings",
                "correct": True,
                "rationale": (
                    "Correct. Browser hijackers are a class of potentially "
                    "unwanted program (PUP) or malware that modify default "
                    "search engine, homepage, and new-tab page settings — "
                    "often installed via bundled software. Redirection and "
                    "homepage changes are the hallmark symptoms."
                ),
            },
            {
                "id": "b",
                "text": "The DNS server has been compromised and is redirecting all traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. A compromised DNS server would affect all "
                    "users on the network, not just one workstation. The "
                    "isolated nature of the symptom indicates a local, "
                    "per-machine browser modification."
                ),
            },
            {
                "id": "c",
                "text": "Google's servers are temporarily redirecting traffic for maintenance",
                "correct": False,
                "rationale": (
                    "Incorrect. Google does not redirect users to competing "
                    "search engines for maintenance. This explanation is "
                    "technically implausible and does not account for the "
                    "homepage change."
                ),
            },
            {
                "id": "d",
                "text": "The browser's proxy settings point to a misconfigured corporate proxy",
                "correct": False,
                "rationale": (
                    "Incorrect. A misconfigured corporate proxy would affect "
                    "all users routed through it, and would more likely cause "
                    "access failures rather than redirecting to a different "
                    "search engine."
                ),
            },
        ],
        "explanation": (
            "Browser redirection and unauthorized homepage changes are "
            "CompTIA-listed browser security symptoms caused by browser "
            "hijackers. Resolution: scan with anti-malware, reset browser "
            "settings to default, uninstall suspect extensions, and check "
            "browser shortcut targets for appended redirect URLs."
        ),
    },
    {
        "id": "c2d3-022",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user's Windows 10 PC repeatedly fails to install Windows "
            "Defender definition updates. The update downloads but fails "
            "with error 0x80070643. The machine has no other update issues. "
            "Anti-malware scans are inconclusive. What is the MOST likely "
            "security-related explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Active malware is blocking or corrupting anti-malware updates to preserve its persistence",
                "correct": True,
                "rationale": (
                    "Correct. OS update failures — particularly targeting "
                    "security/AV definition updates — are a CompTIA-listed "
                    "PC security symptom. Sophisticated malware deliberately "
                    "blocks or corrupts AV updates to prevent detection and "
                    "removal."
                ),
            },
            {
                "id": "b",
                "text": "The Windows Update service is set to Manual and needs to be changed to Automatic",
                "correct": False,
                "rationale": (
                    "Incorrect. If Windows Update were disabled, no updates "
                    "would download at all. The issue describes a download "
                    "that completes but then fails to install — a more "
                    "targeted failure consistent with malware interference."
                ),
            },
            {
                "id": "c",
                "text": "The SSD is nearly full and cannot write the update files",
                "correct": False,
                "rationale": (
                    "Incorrect. Insufficient disk space would produce a "
                    "different error code and would affect all updates, not "
                    "specifically the anti-malware definition update."
                ),
            },
            {
                "id": "d",
                "text": "Group Policy has configured Windows Defender to use WSUS but WSUS does not have the definition package",
                "correct": False,
                "rationale": (
                    "Incorrect. A WSUS package availability issue would affect "
                    "all machines pointed at that WSUS server, not a single "
                    "workstation. The isolated failure on one machine is more "
                    "consistent with local malware interference."
                ),
            },
        ],
        "explanation": (
            "Selective failure of AV/security definition updates on a single "
            "machine is a hallmark PC security symptom. Malware may hook the "
            "update process, corrupt downloaded definition files, or block "
            "the update service. Remediation should follow the CompTIA "
            "7-step malware removal process, including scanning from a "
            "preinstallation environment."
        ),
    },
    {
        "id": "c2d3-023",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user reports seeing a full-screen alert stating their computer "
            "is infected and they must call a phone number immediately to "
            "avoid data loss. The legitimate Windows Security Center shows no "
            "threats. What type of threat is this, and what is the BEST "
            "immediate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rogue/fake antivirus (scareware); close the browser or end the process in Task Manager without calling the number",
                "correct": True,
                "rationale": (
                    "Correct. This describes scareware / fake antivirus — a "
                    "CompTIA-listed security symptom (false antivirus alert). "
                    "The goal is social engineering the user into calling a "
                    "fraudulent 'tech support' number or paying for fake "
                    "software. Close via Task Manager or force-quit the "
                    "browser; never call the number."
                ),
            },
            {
                "id": "b",
                "text": "A legitimate Windows security warning; call the number to get Microsoft support",
                "correct": False,
                "rationale": (
                    "Incorrect. Microsoft and legitimate security software "
                    "never display phone numbers in pop-up alerts or instruct "
                    "users to call for immediate assistance in this manner. "
                    "This is a tech-support scam."
                ),
            },
            {
                "id": "c",
                "text": "Ransomware encrypting files; immediately disconnect from the network and contact IT",
                "correct": False,
                "rationale": (
                    "Incorrect. Ransomware typically displays payment demands "
                    "with cryptocurrency addresses after encrypting files, not "
                    "phone numbers for 'tech support.' A clean Windows Security "
                    "Center also rules out active encryption activity."
                ),
            },
            {
                "id": "d",
                "text": "A Group Policy desktop alert from the IT department; follow the on-screen instructions",
                "correct": False,
                "rationale": (
                    "Incorrect. Corporate IT alerts via GPO use different "
                    "mechanisms (dialog boxes, system notifications) and would "
                    "be consistent across the organization, not targeted at "
                    "one user with a phone number."
                ),
            },
        ],
        "explanation": (
            "Fake antivirus / scareware is a social engineering attack "
            "designed to frighten users into calling fraudulent support lines "
            "or purchasing useless software. It is a CompTIA A+ listed "
            "security symptom. Users should be trained to recognize that "
            "legitimate security tools never demand phone calls via pop-ups."
        ),
    },
    {
        "id": "c2d3-024",
        "domain": 3,
        "objective": "3.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "PC security issue troubleshooting",
        "stem": (
            "A user notices that several personal documents on their "
            "workstation have been renamed with an unfamiliar extension "
            "(.locked) and cannot be opened. A text file on the desktop "
            "contains instructions for payment in cryptocurrency. What "
            "should the technician do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Immediately disconnect the workstation from the network to prevent spread to shared drives",
                "correct": True,
                "rationale": (
                    "Correct. This is active ransomware. Immediate network "
                    "isolation (quarantine — step 2 of the malware removal "
                    "process) is the priority to prevent the ransomware from "
                    "spreading to network shares, backup drives, or other "
                    "systems."
                ),
            },
            {
                "id": "b",
                "text": "Pay the ransom to recover the files quickly",
                "correct": False,
                "rationale": (
                    "Incorrect. Paying the ransom does not guarantee file "
                    "recovery, funds criminal activity, and is against "
                    "virtually all security policy guidance. It is never the "
                    "recommended first action."
                ),
            },
            {
                "id": "c",
                "text": "Run SFC /scannow to restore the renamed files",
                "correct": False,
                "rationale": (
                    "Incorrect. SFC restores protected Windows OS files, not "
                    "user documents renamed by ransomware. It would have no "
                    "effect on encrypted/renamed personal files."
                ),
            },
            {
                "id": "d",
                "text": "Perform a System Restore to recover the encrypted files",
                "correct": False,
                "rationale": (
                    "Incorrect. System Restore may restore some system "
                    "settings but does not recover user data files. Also, "
                    "acting on the local machine before isolating it from "
                    "the network risks spreading the ransomware further."
                ),
            },
        ],
        "explanation": (
            "Ransomware (altered/encrypted personal files with a ransom note) "
            "is an 'altered system/personal files' security symptom. The "
            "immediate priority is network quarantine to stop lateral "
            "movement. Then follow the 7-step malware removal process and "
            "restore from clean backups rather than paying the ransom."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.4 — Mobile OS and Application Troubleshooting
    # -------------------------------------------------------------------------
    {
        "id": "c2d3-025",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone battery drains from 100% to 0% in under "
            "4 hours with minimal usage. The device is 8 months old. Which "
            "diagnostic step should the technician perform FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check the Battery Usage screen in Settings to identify apps with abnormal power consumption",
                "correct": True,
                "rationale": (
                    "Correct. The Battery Usage screen (Settings > Battery > "
                    "Battery Usage) shows per-app power consumption. Identifying "
                    "a runaway app is the most targeted first step before "
                    "hardware replacement or OS-level actions."
                ),
            },
            {
                "id": "b",
                "text": "Immediately replace the battery as it has failed after 8 months",
                "correct": False,
                "rationale": (
                    "Incorrect. Eight months is within normal battery lifespan. "
                    "Hardware replacement without first ruling out software "
                    "causes (rogue app, sync setting, brightness) is premature "
                    "and may be unnecessary."
                ),
            },
            {
                "id": "c",
                "text": "Factory reset the device to eliminate all software causes at once",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset is a last resort. Checking "
                    "battery usage first identifies the cause without data "
                    "loss and allows targeted remediation."
                ),
            },
            {
                "id": "d",
                "text": "Update the OS to the latest version to patch battery management bugs",
                "correct": False,
                "rationale": (
                    "Incorrect. Updating the OS without first diagnosing the "
                    "cause may not resolve the issue and could introduce other "
                    "variables. Diagnosis precedes treatment."
                ),
            },
        ],
        "explanation": (
            "Mobile battery drain troubleshooting starts with the Battery "
            "Usage screen to identify runaway apps (location services, "
            "background sync, push email loops). After identifying the app, "
            "restrict its background activity or uninstall it before "
            "escalating to hardware."
        ),
    },
    {
        "id": "c2d3-026",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "An iOS device fails to install an OS update. The device has "
            "adequate storage (12 GB free) and is connected to Wi-Fi. The "
            "update download completes but installation fails each time. "
            "Which action should the technician try FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Delete the downloaded update profile and re-download; if it fails again, update via iTunes/Finder on a computer",
                "correct": True,
                "rationale": (
                    "Correct. A corrupted downloaded update package is a "
                    "common cause of installation failure despite adequate "
                    "space. Deleting it (Settings > General > iPhone Storage "
                    "> iOS update > Delete) forces a fresh download. If that "
                    "fails, connecting to a Mac/PC via iTunes/Finder for an "
                    "OTA-bypassing wired update is the next step."
                ),
            },
            {
                "id": "b",
                "text": "Restore the device to factory settings and then update",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset before exhausting simpler "
                    "remediation steps causes unnecessary data loss. The "
                    "downloaded package should be deleted and re-fetched first."
                ),
            },
            {
                "id": "c",
                "text": "Disable Wi-Fi and use cellular data to download the update instead",
                "correct": False,
                "rationale": (
                    "Incorrect. iOS requires Wi-Fi for OTA updates larger "
                    "than a few hundred MB (major updates cannot download "
                    "over cellular). This action would not resolve the "
                    "installation failure."
                ),
            },
            {
                "id": "d",
                "text": "Disable iCloud Backup to free additional space for the update",
                "correct": False,
                "rationale": (
                    "Incorrect. iCloud Backup runs in the cloud and does not "
                    "consume local device storage. With 12 GB free, storage "
                    "is not the issue."
                ),
            },
        ],
        "explanation": (
            "iOS update installation failures with adequate space and Wi-Fi "
            "usually indicate a corrupted downloaded update. Deleting the "
            "cached update package and re-downloading is the first fix. "
            "If that fails, a wired update via iTunes/Finder on a computer "
            "bypasses OTA and typically resolves persistent failures."
        ),
    },
    {
        "id": "c2d3-027",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone screen does not rotate when the device "
            "is physically turned to landscape orientation, even in apps "
            "that support it. Which should the technician check FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify that Auto-Rotate is enabled in Quick Settings or Display settings",
                "correct": True,
                "rationale": (
                    "Correct. The most common cause of auto-rotate failure "
                    "is the Auto-Rotate toggle being disabled by the user "
                    "accidentally (often via the Quick Settings panel). "
                    "This is a settings check that takes seconds."
                ),
            },
            {
                "id": "b",
                "text": "Replace the accelerometer as it has failed",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware failure (accelerometer) is possible "
                    "but should only be suspected after ruling out the software "
                    "setting. A disabled Auto-Rotate toggle is far more common."
                ),
            },
            {
                "id": "c",
                "text": "Perform a factory reset to restore default display settings",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset is an extreme measure for "
                    "what is almost certainly a simple settings toggle. It "
                    "causes data loss and is not warranted as a first step."
                ),
            },
            {
                "id": "d",
                "text": "Update the display driver via a system update",
                "correct": False,
                "rationale": (
                    "Incorrect. Android devices don't have user-updatable "
                    "standalone display drivers outside of OS updates. This "
                    "action does not address the likely settings cause."
                ),
            },
        ],
        "explanation": (
            "Auto-rotate issues are almost always caused by the rotation "
            "lock toggle being enabled. Check Quick Settings (swipe down) "
            "for the Auto-Rotate or Portrait Lock toggle first. If enabled "
            "and still not rotating, test with a rotation test app to "
            "determine if the accelerometer hardware has failed."
        ),
    },
    {
        "id": "c2d3-028",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's iPhone randomly reboots several times daily, across "
            "multiple apps and even at the home screen. The device runs the "
            "latest iOS. Battery health shows 74%. Which action is MOST "
            "likely to resolve this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace the battery, as 74% battery health can cause voltage sags that trigger unexpected shutdowns and reboots",
                "correct": True,
                "rationale": (
                    "Correct. Apple considers batteries below 80% health "
                    "as significantly degraded. At 74%, the battery may "
                    "experience voltage drops under load that the device "
                    "interprets as insufficient power, causing random "
                    "reboots. Battery replacement is the primary fix."
                ),
            },
            {
                "id": "b",
                "text": "Uninstall all third-party apps and test, since an app is causing the crash",
                "correct": False,
                "rationale": (
                    "Incorrect. Random reboots at the home screen (no apps "
                    "running) rule out a single app as the root cause. "
                    "Battery health of 74% is a well-known hardware trigger "
                    "for this symptom."
                ),
            },
            {
                "id": "c",
                "text": "Restore the iPhone via iTunes/Finder to eliminate a software glitch",
                "correct": False,
                "rationale": (
                    "Incorrect. While a restore might temporarily help if "
                    "there's a software cause, the degraded battery health "
                    "(74%) is the most clinically significant finding and "
                    "the most likely root cause of voltage-sag-induced "
                    "reboots."
                ),
            },
            {
                "id": "d",
                "text": "Enable Low Power Mode permanently to reduce reboot frequency",
                "correct": False,
                "rationale": (
                    "Incorrect. Low Power Mode reduces background activity "
                    "and may lessen voltage demands temporarily, but it is "
                    "a workaround, not a fix. The degraded battery is the "
                    "root cause and should be replaced."
                ),
            },
        ],
        "explanation": (
            "Random reboots across all contexts on an iPhone with 74% "
            "battery health are strongly indicative of battery failure. "
            "Degraded lithium batteries cannot maintain stable voltage "
            "under load, causing the device to reboot as a protection "
            "mechanism. Apple recommends battery replacement below 80% "
            "health for optimal performance."
        ),
    },
    {
        "id": "c2d3-029",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user's Android phone cannot connect to any Bluetooth devices. "
            "The device was connecting successfully yesterday. Wi-Fi works "
            "fine. The Bluetooth toggle is on. Which is the BEST next step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Toggle Airplane Mode on then off, or perform a soft reset to reset the Bluetooth stack",
                "correct": True,
                "rationale": (
                    "Correct. Toggling Airplane Mode (which disables and "
                    "re-enables all radios) or a soft reset clears the "
                    "Bluetooth stack state, resolving transient software "
                    "faults that prevent connection while the hardware is "
                    "intact."
                ),
            },
            {
                "id": "b",
                "text": "Replace the device as the Bluetooth hardware has failed",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware failure should only be concluded "
                    "after software troubleshooting (radio reset, clearing "
                    "paired devices, factory reset) fails. An overnight "
                    "failure with Wi-Fi intact suggests a software/stack "
                    "issue rather than hardware."
                ),
            },
            {
                "id": "c",
                "text": "Update to the latest OS version to patch Bluetooth connectivity",
                "correct": False,
                "rationale": (
                    "Incorrect. An OS update is not the first diagnostic "
                    "step for a Bluetooth issue that appeared suddenly. "
                    "Stack reset is faster and more targeted."
                ),
            },
            {
                "id": "d",
                "text": "Forget all paired Bluetooth devices and re-pair them",
                "correct": False,
                "rationale": (
                    "Incorrect. Forgetting paired devices is a valid step "
                    "but is more applicable when one specific device fails "
                    "to pair. When ALL Bluetooth is non-functional, resetting "
                    "the radio/stack first is more appropriate."
                ),
            },
        ],
        "explanation": (
            "Sudden Bluetooth failure with Wi-Fi working indicates a "
            "software/stack issue rather than radio hardware failure "
            "(which would likely affect Wi-Fi too, as they share the "
            "2.4 GHz radio). Airplane Mode toggle or soft reset is the "
            "fastest initial step; if that fails, clear Bluetooth cache "
            "(Android: Settings > Apps > Bluetooth), then consider "
            "factory reset before hardware conclusion."
        ),
    },
    {
        "id": "c2d3-030",
        "domain": 3,
        "objective": "3.4",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mobile OS troubleshooting",
        "stem": (
            "A user reports their Android phone is running extremely slowly "
            "and apps frequently crash. The device has been in use for "
            "2 years without a reset. Which TWO actions should the technician "
            "recommend FIRST before escalating to a factory reset? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clear the cache partition via recovery mode to remove accumulated system cache",
                "correct": True,
                "rationale": (
                    "Correct. Clearing the cache partition removes temporary "
                    "system files that can accumulate over time and degrade "
                    "performance without erasing user data. This is a safe "
                    "first escalation step."
                ),
            },
            {
                "id": "b",
                "text": "Uninstall unused apps and check storage to ensure at least 10–15% free space",
                "correct": True,
                "rationale": (
                    "Correct. Insufficient free storage causes Android "
                    "performance degradation and app crashes, as the OS needs "
                    "free space for virtual memory swapping and temp file "
                    "creation. Uninstalling apps and freeing storage is a "
                    "non-destructive first step."
                ),
            },
            {
                "id": "c",
                "text": "Immediately perform a factory reset to restore peak performance",
                "correct": False,
                "rationale": (
                    "Incorrect. Factory reset causes complete data loss and "
                    "should only be performed after less destructive steps "
                    "(cache clear, storage management, app audit) have failed "
                    "to resolve the issue."
                ),
            },
            {
                "id": "d",
                "text": "Replace the battery to eliminate power-related performance throttling",
                "correct": False,
                "rationale": (
                    "Incorrect. While a degraded battery can cause throttling, "
                    "software causes (cache, storage, runaway apps) are far "
                    "more likely after 2 years. Software steps should precede "
                    "hardware intervention."
                ),
            },
        ],
        "explanation": (
            "Sluggish Android performance after extended use is commonly "
            "caused by accumulated cache data and near-full storage. "
            "Clearing the system cache partition and freeing storage are "
            "the safest, most targeted first steps. Factory reset is "
            "reserved for when software remediation fails."
        ),
    },
    # -------------------------------------------------------------------------
    # 3.5 — Mobile OS and Application Security Issues
    # -------------------------------------------------------------------------
    {
        "id": "c2d3-031",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user installs an Android app downloaded from a third-party "
            "website (not the Google Play Store). After installation, the "
            "phone's data usage triples and the battery drains unusually "
            "fast. Which security concern BEST explains this behavior?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The APK from the unofficial source contained malware that is sending data in the background",
                "correct": True,
                "rationale": (
                    "Correct. Side-loaded APKs from unvetted sources bypass "
                    "Google Play Protect scanning and frequently contain "
                    "spyware or adware. Excessive data usage and battery "
                    "drain after a side-loaded install are classic indicators "
                    "of malicious background activity."
                ),
            },
            {
                "id": "b",
                "text": "Google Play Protect blocked the app and is scanning the device continuously",
                "correct": False,
                "rationale": (
                    "Incorrect. Google Play Protect scans are not resource-"
                    "intensive enough to triple data usage. Also, Play Protect "
                    "may warn about the side-loaded app but does not perform "
                    "continuous scanning that would cause such dramatic "
                    "resource consumption."
                ),
            },
            {
                "id": "c",
                "text": "The app requires developer mode to be enabled and is consuming resources during setup",
                "correct": False,
                "rationale": (
                    "Incorrect. Developer mode does not consume significant "
                    "data or battery by itself, and an app's one-time setup "
                    "would not persistently triple ongoing data usage."
                ),
            },
            {
                "id": "d",
                "text": "The user's carrier is throttling data, causing the phone to retry and use more power",
                "correct": False,
                "rationale": (
                    "Incorrect. Carrier throttling reduces data speed but "
                    "does not increase data usage or cause significant "
                    "battery drain. The timing correlation with the "
                    "third-party APK install is the critical diagnostic clue."
                ),
            },
        ],
        "explanation": (
            "Sideloading APKs (installing from sources other than official "
            "app stores) is a major Android security risk. APKs from "
            "unofficial sources are not vetted and frequently bundle "
            "malware. High network traffic and battery drain post-install "
            "are CompTIA-listed mobile security symptoms. The app should "
            "be uninstalled and the device scanned."
        ),
    },
    {
        "id": "c2d3-032",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A corporate mobile device enrolled in MDM suddenly shows "
            "unexpected app behavior — apps the user did not install are "
            "appearing, and personal contacts are being uploaded to an "
            "unknown server. Investigation reveals the device has been "
            "rooted. What is the PRIMARY security concern, and what is "
            "the BEST action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rooting bypassed MDM controls and security policies; remotely wipe the device via MDM and re-enroll it",
                "correct": True,
                "rationale": (
                    "Correct. Rooting removes Android's security sandbox, "
                    "allowing apps to bypass MDM profiles, install silently, "
                    "and access protected data. A rooted corporate device "
                    "is a critical security violation. Remote wipe via MDM "
                    "and re-enrollment (on an unrooted device) is the correct "
                    "response."
                ),
            },
            {
                "id": "b",
                "text": "Uninstall the unauthorized apps manually and run an anti-malware scan",
                "correct": False,
                "rationale": (
                    "Incorrect. On a rooted device, apps can reinstall "
                    "themselves at the system level and resist removal. "
                    "Manual uninstall does not address the root (pun intended) "
                    "cause — the compromised OS security model. Remote wipe "
                    "is required."
                ),
            },
            {
                "id": "c",
                "text": "Reset the device's root access by running an unroot tool and re-apply MDM policies",
                "correct": False,
                "rationale": (
                    "Incorrect. Unroot tools vary in reliability and may "
                    "not fully restore the OS security posture. Corporate "
                    "policy typically requires a full wipe and clean OS "
                    "flash on any rooted corporate device."
                ),
            },
            {
                "id": "d",
                "text": "Change the MDM enrollment password to prevent further unauthorized configuration changes",
                "correct": False,
                "rationale": (
                    "Incorrect. A password change does not address the "
                    "compromised device itself. On a rooted Android, system-"
                    "level access means MDM certificates and profiles can "
                    "be manipulated directly."
                ),
            },
        ],
        "explanation": (
            "Rooting an Android device removes the OS security boundary, "
            "rendering MDM profiles and app sandboxing ineffective. "
            "CompTIA identifies root/jailbreak as a key mobile security "
            "concern. Corporate policy mandates remote wipe via MDM for "
            "compromised devices, followed by re-enrollment on a verified "
            "clean device."
        ),
    },
    {
        "id": "c2d3-033",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user's iPhone displays a message saying 'This accessory may "
            "not be supported' and they notice unexpected charges to their "
            "Apple ID for in-app purchases they did not make. The device "
            "was recently jailbroken by the user to install apps from "
            "outside the App Store. What is the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Jailbreaking removed iOS security protections, allowing bootleg apps to steal Apple ID credentials and make unauthorized purchases",
                "correct": True,
                "rationale": (
                    "Correct. Jailbreaking iOS removes kernel-level security "
                    "protections. Bootleg apps installed via Cydia or "
                    "similar can access stored credentials, including Apple "
                    "ID tokens, and make unauthorized purchases. This is a "
                    "CompTIA-listed mobile security concern."
                ),
            },
            {
                "id": "b",
                "text": "Apple's payment servers are experiencing fraud; report to Apple directly",
                "correct": False,
                "rationale": (
                    "Incorrect. Apple's servers are not the failure point. "
                    "The jailbreak is the direct cause of the compromised "
                    "security model that allowed credential theft on the "
                    "device itself."
                ),
            },
            {
                "id": "c",
                "text": "The unsupported accessory warning is causing payment processing errors",
                "correct": False,
                "rationale": (
                    "Incorrect. The 'unsupported accessory' message relates "
                    "to MFi (Made for iPhone) certification of physical "
                    "accessories and is unrelated to App Store purchase "
                    "fraud. The two symptoms have separate causes."
                ),
            },
            {
                "id": "d",
                "text": "The user's Wi-Fi is compromised and a man-in-the-middle attack is intercepting transactions",
                "correct": False,
                "rationale": (
                    "Incorrect. iOS uses certificate pinning for App Store "
                    "transactions, making MITM attacks extremely difficult "
                    "on unmodified devices. The jailbreak is the far more "
                    "likely attack vector."
                ),
            },
        ],
        "explanation": (
            "Jailbreaking iOS undermines the App Store's vetting process "
            "and the OS security sandbox. Bootleg apps (installed outside "
            "the official App Store) can access keychain data, OAuth tokens, "
            "and Apple ID credentials. CompTIA lists jailbreaking and "
            "bootleg apps as primary mobile security concerns. The solution "
            "is to restore the device to factory iOS via iTunes/Finder."
        ),
    },
    {
        "id": "c2d3-034",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user reports receiving a data-usage limit notification and "
            "observes sluggish response on their company Android phone. "
            "The IT department confirms no policy changes were made. "
            "Developer options are enabled on the device. Which of the "
            "following is the GREATEST security concern that could explain "
            "both symptoms simultaneously?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Developer mode is enabled, allowing ADB over Wi-Fi access that a threat actor is using to exfiltrate data",
                "correct": True,
                "rationale": (
                    "Correct. Developer mode with ADB over Wi-Fi enabled "
                    "allows remote command-line access to the device without "
                    "physical connection. A threat actor on the same network "
                    "could use ADB to exfiltrate data continuously, causing "
                    "both the high network usage and sluggish performance "
                    "simultaneously — a CompTIA-listed security concern."
                ),
            },
            {
                "id": "b",
                "text": "The cellular carrier has reduced the data cap without notice",
                "correct": False,
                "rationale": (
                    "Incorrect. A carrier data cap reduction would not cause "
                    "sluggish device response; it would simply throttle "
                    "data speed after the cap. The performance degradation "
                    "combined with high traffic suggests active processing "
                    "on the device."
                ),
            },
            {
                "id": "c",
                "text": "A background app update is consuming bandwidth and CPU during download",
                "correct": False,
                "rationale": (
                    "Incorrect. App updates are temporary and would not "
                    "persistently consume data to the limit or cause ongoing "
                    "sluggishness. The combination of sustained high traffic "
                    "and developer mode enabled suggests a more serious "
                    "compromise."
                ),
            },
            {
                "id": "d",
                "text": "The GPS is running continuously, using cellular data to upload location data",
                "correct": False,
                "rationale": (
                    "Incorrect. GPS location data uploads are small in size "
                    "and would not consume enough data to trigger a plan-"
                    "level data limit notification. Developer mode with "
                    "ADB is the more concerning and data-intensive scenario."
                ),
            },
        ],
        "explanation": (
            "Developer mode (and specifically ADB over Wi-Fi or USB debugging) "
            "on a corporate device is a CompTIA-listed security concern. "
            "It opens the device to remote shell access and data exfiltration. "
            "IT should disable developer options via MDM policy, revoke ADB "
            "access, and investigate the device for unauthorized connections."
        ),
    },
    {
        "id": "c2d3-035",
        "domain": 3,
        "objective": "3.5",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Mobile app security troubleshooting",
        "stem": (
            "A user's Android phone shows fake security warnings claiming "
            "the device is infected and personal files have been leaked "
            "to unknown parties. The user recently installed an app from "
            "a link in a text message. Which TWO actions should the "
            "technician take? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Uninstall the suspicious app and run a reputable mobile anti-malware scan",
                "correct": True,
                "rationale": (
                    "Correct. The suspicious app installed via an SMS link "
                    "is the most likely source of the fake warnings and "
                    "data leakage. Uninstalling it and scanning with a "
                    "trusted mobile security app removes the threat and "
                    "confirms whether other malware is present."
                ),
            },
            {
                "id": "b",
                "text": "Change the user's account passwords from a different, trusted device immediately",
                "correct": True,
                "rationale": (
                    "Correct. If personal files and credentials may have been "
                    "leaked (a stated symptom), changing passwords from a "
                    "clean device is critical to limit credential-based "
                    "damage while the phone is being remediated."
                ),
            },
            {
                "id": "c",
                "text": "Pay the fee shown in the security warning to restore device functionality",
                "correct": False,
                "rationale": (
                    "Incorrect. The warnings are fake security alerts — a "
                    "CompTIA-listed mobile security symptom. Paying would "
                    "not remove the malware and would fund the attacker."
                ),
            },
            {
                "id": "d",
                "text": "Enable developer mode to use ADB to forcefully remove the app",
                "correct": False,
                "rationale": (
                    "Incorrect. Enabling developer mode on a potentially "
                    "compromised device introduces additional security risk. "
                    "Standard app uninstall via Settings is sufficient for "
                    "most malware; factory reset if needed."
                ),
            },
        ],
        "explanation": (
            "An app installed via SMS link (smishing) is a classic malware "
            "delivery vector on Android. Fake security warnings and data "
            "leakage are CompTIA-listed mobile security symptoms. The "
            "correct response is to remove the threat app, scan the device, "
            "and change credentials from a trusted device — not to engage "
            "with the fraudulent warnings."
        ),
    },
    {
        "id": "c2d3-036",
        "domain": 3,
        "objective": "3.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Malware removal best-practice process",
        "stem": (
            "A technician has completed all seven steps of CompTIA's malware "
            "removal process on a workstation. The end user asks why they "
            "need to sit through a security briefing when the computer is "
            "already clean. Which response BEST justifies step 7 of the "
            "malware removal process?"
        ),
        "options": [
            {
                "id": "a",
                "text": "User education prevents reinfection by teaching the user to recognize phishing, avoid unsafe downloads, and understand security policies",
                "correct": True,
                "rationale": (
                    "Correct. Step 7 — educating the end user — addresses "
                    "the human attack vector. Most malware infections result "
                    "from user actions (clicking phishing links, downloading "
                    "untrusted software). Without education, the same behavior "
                    "will lead to reinfection regardless of how thorough "
                    "technical remediation was."
                ),
            },
            {
                "id": "b",
                "text": "It is a regulatory requirement and must be completed to close the helpdesk ticket",
                "correct": False,
                "rationale": (
                    "Incorrect. While documentation may be required for "
                    "compliance, the purpose of CompTIA's step 7 is not "
                    "ticket closure — it is genuine user education to prevent "
                    "recurrence. Framing it as paperwork misses the security "
                    "intent."
                ),
            },
            {
                "id": "c",
                "text": "The anti-malware software requires user acknowledgment before it can be re-enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. Anti-malware software does not require end-"
                    "user acknowledgment to operate. This answer fabricates "
                    "a technical dependency that does not exist."
                ),
            },
            {
                "id": "d",
                "text": "The technician needs the user's signature to confirm the repair, which is step 7",
                "correct": False,
                "rationale": (
                    "Incorrect. Step 7 is about substantive education — "
                    "explaining how malware arrives and how to avoid it — "
                    "not merely obtaining a signature for documentation "
                    "purposes."
                ),
            },
        ],
        "explanation": (
            "The CompTIA malware removal process ends with user education "
            "because technology alone cannot prevent reinfection when human "
            "behavior is the root cause. Effective education covers: "
            "recognizing phishing emails, avoiding unofficial software "
            "sources, understanding social engineering, and following "
            "organizational security policies."
        ),
    },
]
