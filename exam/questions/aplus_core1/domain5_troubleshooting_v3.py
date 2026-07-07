"""
CompTIA A+ Core 1 (220-1201) — Domain 5: Hardware and Network Troubleshooting
41 NEW practice questions at hard/expert difficulty (v3 bank).
"""

QUESTIONS = [
    # ── 5.1 Troubleshooting Methodology ──────────────────────────────────────
    {
        "id": "a1d5v3-001",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A help desk technician receives a ticket stating 'my computer is broken.' "
            "The user is unavailable by phone. According to the CompTIA troubleshooting "
            "methodology, which action represents the BEST use of Step 1 given that "
            "the user cannot be reached?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Visit the workstation, attempt to reproduce the reported symptom, and document observations",
                "correct": True,
                "rationale": (
                    "Correct. Step 1 (Identify the problem) includes gathering information "
                    "and duplicating the problem when possible. When the user is unavailable, "
                    "the technician should go to the workstation, attempt to reproduce the "
                    "issue, and record what is observed — gathering first-hand evidence."
                ),
            },
            {
                "id": "b",
                "text": "Immediately reimage the workstation to eliminate any software cause",
                "correct": False,
                "rationale": (
                    "Incorrect. Reimaging is a drastic corrective action. Implementing a "
                    "fix before identifying the problem violates the methodology and may "
                    "result in permanent data loss."
                ),
            },
            {
                "id": "c",
                "text": "Escalate the ticket immediately because identifying the problem requires user input",
                "correct": False,
                "rationale": (
                    "Incorrect. Escalation is appropriate when the technician cannot "
                    "resolve the issue after attempting it. The technician has not yet "
                    "attempted to gather information first-hand."
                ),
            },
            {
                "id": "d",
                "text": "Close the ticket and ask the user to resubmit it with more details",
                "correct": False,
                "rationale": (
                    "Incorrect. Closing the ticket without attempting to investigate does "
                    "not align with the troubleshooting methodology and fails the user. "
                    "The technician should investigate independently."
                ),
            },
        ],
        "explanation": (
            "Step 1 of the CompTIA methodology (Identify the Problem) includes gathering "
            "information, duplicating the problem if possible, and questioning users about "
            "symptoms. When the user is unavailable, the technician should visit the "
            "workstation and attempt to observe/reproduce the issue directly. Good "
            "documentation of first-hand observations substitutes for user questioning."
        ),
    },
    {
        "id": "a1d5v3-002",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician confirms that rolling back a Windows driver update resolves "
            "a display issue on a user's laptop. The display now works correctly. "
            "According to the CompTIA troubleshooting methodology, what should the "
            "technician do BEFORE documenting findings and closing the ticket?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify full system functionality and implement preventive measures",
                "correct": True,
                "rationale": (
                    "Correct. After implementing the fix (rolling back the driver — Step 4), "
                    "the next step is Step 5: verify full system functionality (test all "
                    "display functions, ask the user to confirm) and implement preventive "
                    "measures (e.g., block the problematic driver update from reinstalling). "
                    "Documentation is Step 6 and comes last."
                ),
            },
            {
                "id": "b",
                "text": "Establish a new theory of probable cause in case the issue recurs",
                "correct": False,
                "rationale": (
                    "Incorrect. A new theory is only needed when the original theory is "
                    "disproved. The driver rollback resolved the issue, so no new theory "
                    "is required."
                ),
            },
            {
                "id": "c",
                "text": "Re-examine the problem identification step to ensure the root cause is correct",
                "correct": False,
                "rationale": (
                    "Incorrect. The fix has been confirmed to work. Revisiting Step 1 is "
                    "only appropriate if the fix did not resolve the issue. The methodology "
                    "moves forward to verification."
                ),
            },
            {
                "id": "d",
                "text": "Document findings immediately after the fix is applied",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation (Step 6) comes after verifying full "
                    "functionality (Step 5). Documenting before verification skips a "
                    "required confirmation step."
                ),
            },
        ],
        "explanation": (
            "The CompTIA 6-step methodology in order: 1) Identify problem, 2) Theory of "
            "probable cause, 3) Test theory, 4) Plan of action and implement, 5) Verify "
            "full functionality + preventive measures, 6) Document. After a fix is "
            "implemented, always verify before documenting. Preventive measures (e.g., "
            "hiding the bad driver update in Windows Update) are part of Step 5."
        ),
    },
    {
        "id": "a1d5v3-003",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "During the troubleshooting process, a technician has two equally plausible "
            "theories for why a workstation is experiencing random BSODs: faulty RAM "
            "or a driver conflict. The CompTIA methodology calls for testing the theory "
            "to determine the cause. Which approach BEST reflects the methodology when "
            "testing two competing theories?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Test the easiest or least invasive theory first (reseat/swap RAM), then move to driver testing if RAM passes",
                "correct": True,
                "rationale": (
                    "Correct. When multiple theories exist, start with the least invasive "
                    "and most probable test. Reseating or swapping RAM is non-destructive "
                    "and quick. If RAM tests clean, proceed to the next theory. This "
                    "structured approach avoids wasted effort."
                ),
            },
            {
                "id": "b",
                "text": "Implement both fixes simultaneously (replace RAM and reinstall drivers) to save time",
                "correct": False,
                "rationale": (
                    "Incorrect. Changing multiple variables simultaneously violates the "
                    "scientific methodology embedded in Step 3. If both changes are made "
                    "at once and the issue resolves, the root cause remains unknown."
                ),
            },
            {
                "id": "c",
                "text": "Escalate immediately because two theories indicate the problem is too complex for a field technician",
                "correct": False,
                "rationale": (
                    "Incorrect. Having two theories is normal and does not by itself "
                    "justify escalation. The technician should test each theory "
                    "systematically before escalating."
                ),
            },
            {
                "id": "d",
                "text": "Skip testing and proceed directly to implementing the most expensive fix to ensure it is covered",
                "correct": False,
                "rationale": (
                    "Incorrect. Implementing a fix without testing the theory is the "
                    "classic anti-pattern the methodology is designed to prevent. Expensive "
                    "components may be replaced unnecessarily."
                ),
            },
        ],
        "explanation": (
            "When multiple theories exist, the CompTIA methodology recommends testing "
            "them one at a time, starting with the most probable and least invasive. "
            "Changing one variable at a time (the scientific method) ensures that when "
            "the problem is resolved, you know exactly which variable was the cause. "
            "This avoids wasted parts, time, and misidentification of root cause."
        ),
    },
    # ── 5.2 Motherboards, RAM, CPUs, Power ───────────────────────────────────
    {
        "id": "a1d5v3-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "After installing a second RAM kit in a dual-channel desktop, a technician "
            "powers the system on and finds it boots but runs at a much lower clock "
            "speed than expected. CPU-Z shows the RAM operating in single-channel mode "
            "at 2133 MHz instead of the configured 3200 MHz XMP. What is the MOST "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The DIMMs are installed in adjacent slots rather than the correct paired (A2/B2) slots for dual-channel",
                "correct": True,
                "rationale": (
                    "Correct. Most motherboards require DIMMs to occupy specific paired "
                    "slots (e.g., A1+B1 or A2+B2) to enable dual-channel mode. Installing "
                    "both sticks in adjacent slots (A1+A2) forces single-channel operation "
                    "and often defaults the memory to JEDEC speeds (2133 MHz) rather than "
                    "the XMP profile."
                ),
            },
            {
                "id": "b",
                "text": "The new RAM kit has a different CAS latency and is incompatible with the motherboard",
                "correct": False,
                "rationale": (
                    "Incorrect. CAS latency differences cause the BIOS to negotiate the "
                    "slowest common latency, but would not alone cause single-channel "
                    "operation or such a dramatic speed reduction to JEDEC baseline. "
                    "Slot placement is the stronger determinant here."
                ),
            },
            {
                "id": "c",
                "text": "XMP profiles are not supported on dual-channel configurations",
                "correct": False,
                "rationale": (
                    "Incorrect. XMP (eXtreme Memory Profile) is specifically designed "
                    "for multi-channel configurations and is fully supported in "
                    "dual-channel setups. XMP must simply be enabled in BIOS."
                ),
            },
            {
                "id": "d",
                "text": "The CPU's integrated memory controller does not support 3200 MHz",
                "correct": False,
                "rationale": (
                    "Incorrect. While some CPUs have IMC limits, the symptom specifically "
                    "shows single-channel operation. If the IMC were the bottleneck, the "
                    "system would still operate in dual-channel at the supported speed, "
                    "not drop to single-channel."
                ),
            },
        ],
        "explanation": (
            "Dual-channel memory requires DIMMs to be installed in matched paired "
            "slots — typically the same color or specifically labeled A1+B1 or A2+B2. "
            "Placing both sticks in A1+A2 (same channel) results in single-channel "
            "operation. Additionally, XMP/DOCP must be manually enabled in BIOS to "
            "run above JEDEC defaults. Check the motherboard manual for the correct "
            "slot pairing diagram."
        ),
    },
    {
        "id": "a1d5v3-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A desktop PC emits one long beep followed by two short beeps on an Award "
            "BIOS system and refuses to POST. The technician has already confirmed RAM "
            "is properly seated. What does this beep code indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Video card or GPU failure",
                "correct": True,
                "rationale": (
                    "Correct. On Award BIOS, 1 long beep + 2 short beeps is the standard "
                    "code for a video card failure or no video detected. The system cannot "
                    "initialize the display subsystem and halts POST."
                ),
            },
            {
                "id": "b",
                "text": "RAM failure — a DIMM has failed its memory test",
                "correct": False,
                "rationale": (
                    "Incorrect. Award BIOS RAM failure typically produces 1 long + 3 short "
                    "beeps (memory error) or continuous short beeps. 1 long + 2 short "
                    "specifically maps to a video error on Award BIOS."
                ),
            },
            {
                "id": "c",
                "text": "CPU is overheating and thermal protection is halting POST",
                "correct": False,
                "rationale": (
                    "Incorrect. CPU thermal protection typically triggers during or after "
                    "POST, not as a beep code sequence at the very start. Overheating at "
                    "POST level is typically represented differently or as a continuous "
                    "tone."
                ),
            },
            {
                "id": "d",
                "text": "Keyboard controller error preventing the system from continuing POST",
                "correct": False,
                "rationale": (
                    "Incorrect. Award BIOS keyboard controller errors produce different "
                    "beep patterns. 1 long + 2 short is specifically the video failure "
                    "code for Award BIOS."
                ),
            },
        ],
        "explanation": (
            "Beep codes are BIOS-vendor specific. Key facts for the A+ exam: "
            "Award BIOS: 1 long + 2 short = video error; AMI BIOS: 1 long + 3 short = "
            "video error. RAM errors on AMI are indicated by 2 or 3 short beeps. "
            "Always consult the motherboard manual for exact codes, but video errors "
            "are high-frequency A+ exam topics."
        ),
    },
    {
        "id": "a1d5v3-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A workstation powers on for about two seconds, then immediately powers "
            "off without any POST beep or display output. This cycle repeats if the "
            "power button is pressed again. Which component is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The power supply is failing to sustain output past the Power Good signal timeout",
                "correct": True,
                "rationale": (
                    "Correct. A PSU that cannot hold stable voltages will trigger the "
                    "ATX 'Power Good' (PG) signal to drop shortly after startup. When "
                    "PG drops, the motherboard immediately halts and cuts power — "
                    "creating the 2-second boot-then-shutdown cycle. This is a PSU "
                    "failure signature."
                ),
            },
            {
                "id": "b",
                "text": "A failing hard drive causing the BIOS to stall waiting for a storage device",
                "correct": False,
                "rationale": (
                    "Incorrect. A hard drive failure causes the system to POST, reach "
                    "the storage detection phase, and then produce an error message. "
                    "A 2-second power cycle before any POST output is a PSU-level event."
                ),
            },
            {
                "id": "c",
                "text": "A corrupt BIOS causing the system to reset before POST completes",
                "correct": False,
                "rationale": (
                    "Incorrect. A corrupt BIOS can prevent POST from completing but "
                    "typically does not cause a physical power cut within 2 seconds. "
                    "The immediate power-off pattern is characteristic of PSU instability."
                ),
            },
            {
                "id": "d",
                "text": "An incompatible CPU that the motherboard cannot initialize",
                "correct": False,
                "rationale": (
                    "Incorrect. An incompatible or unsupported CPU typically causes a "
                    "no-POST condition (no display, no beeps) but does not cause the "
                    "dramatic 2-second power cycle that indicates a Power Good failure."
                ),
            },
        ],
        "explanation": (
            "The ATX Power Good (PG) signal is a logic signal the PSU sends to the "
            "motherboard once all voltage rails stabilize. If the PSU cannot sustain "
            "stable voltages, PG drops, and the motherboard resets within milliseconds. "
            "This manifests as a brief 2-5 second power-on followed by shutdown. "
            "Test or replace the PSU. Verify with a PSU tester or known-good PSU."
        ),
    },
    {
        "id": "a1d5v3-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A technician installs a new CPU in a motherboard and the system posts "
            "but immediately shows a warning that the CPU is running at 800 MHz "
            "instead of 3.6 GHz. BIOS settings appear correct. What is the MOST "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The CPU cooler is not properly seated, causing immediate thermal throttling",
                "correct": True,
                "rationale": (
                    "Correct. If the CPU cooler is not making full thermal contact "
                    "(loose mount, no thermal paste, or improperly seated), the CPU "
                    "reaches its thermal limit within seconds of startup and throttles "
                    "aggressively — sometimes to as low as 800 MHz — as a protective "
                    "measure. This is a common post-installation mistake."
                ),
            },
            {
                "id": "b",
                "text": "The BIOS needs to be updated to support the new CPU's full speed",
                "correct": False,
                "rationale": (
                    "Incorrect. An unsupported CPU BIOS version would typically cause a "
                    "no-boot or instability, not an extreme clock reduction to 800 MHz "
                    "within the first POST. Thermal throttling is a more immediate and "
                    "specific explanation."
                ),
            },
            {
                "id": "c",
                "text": "The power supply is too weak to power the new CPU at full speed",
                "correct": False,
                "rationale": (
                    "Incorrect. Underpowering a CPU tends to cause system instability "
                    "or shutdowns, not a controlled reduction to 800 MHz immediately "
                    "at POST. The controlled throttle signature points to thermal "
                    "protection."
                ),
            },
            {
                "id": "d",
                "text": "The CPU multiplier is locked in BIOS at the minimum setting",
                "correct": False,
                "rationale": (
                    "Incorrect. The question states BIOS settings appear correct. "
                    "Additionally, consumer CPUs boot at full speed unless there is a "
                    "thermal or power event — a locked multiplier at 800 MHz would be "
                    "an unusual deliberate setting."
                ),
            },
        ],
        "explanation": (
            "After installing a new CPU, the most common cause of immediate aggressive "
            "throttling is a poorly seated cooler. Without proper thermal contact, the "
            "CPU temperature spikes within seconds of startup, triggering thermal "
            "throttle protection (TDP control). Always apply thermal paste and verify "
            "all mounting screws/clips are fully engaged before first boot. Monitor "
            "CPU temperature in BIOS immediately after a new CPU install."
        ),
    },
    # ── 5.3 Storage Drives and RAID ───────────────────────────────────────────
    {
        "id": "a1d5v3-008",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A server with a RAID 1 array of two 4 TB drives reports that one drive "
            "has failed. The RAID controller is in degraded mode and the remaining "
            "drive is functioning. An administrator replaces the failed drive with a "
            "new 4 TB drive. What will happen next?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The RAID controller will automatically rebuild the mirror from the surviving drive to the new drive",
                "correct": True,
                "rationale": (
                    "Correct. RAID 1 (mirroring) stores identical data on both drives. "
                    "When a failed drive is replaced with a compatible drive, most RAID "
                    "controllers automatically begin a rebuild — copying all data from "
                    "the surviving drive to the new drive — restoring full redundancy."
                ),
            },
            {
                "id": "b",
                "text": "The array cannot be rebuilt; all data must be restored from backup",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 1 can survive a single drive failure because the "
                    "surviving mirror drive contains all data. Rebuilding to a new drive "
                    "is the designed recovery procedure."
                ),
            },
            {
                "id": "c",
                "text": "The new drive will be formatted and added as a third mirror in a RAID 1E configuration",
                "correct": False,
                "rationale": (
                    "Incorrect. Simply replacing a failed drive in a RAID 1 pair does "
                    "not automatically upgrade to RAID 1E. The controller will treat the "
                    "replacement as the second mirror drive and rebuild the standard "
                    "RAID 1 pair."
                ),
            },
            {
                "id": "d",
                "text": "The system must be rebooted into recovery mode before the RAID can rebuild",
                "correct": False,
                "rationale": (
                    "Incorrect. Many RAID controllers and software RAID implementations "
                    "support hot-swap rebuilding — the rebuild begins automatically when "
                    "the replacement drive is detected, without requiring a reboot."
                ),
            },
        ],
        "explanation": (
            "RAID 1 fault tolerance: it tolerates one drive failure. The surviving mirror "
            "contains 100% of the data. Replacing the failed drive triggers an automatic "
            "rebuild. During the rebuild, the array is in degraded mode (no redundancy). "
            "The rebuild time depends on drive capacity and controller speed. The server "
            "remains operational throughout."
        ),
    },
    {
        "id": "a1d5v3-009",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A Windows workstation was running fine, but after a sudden power outage "
            "it boots to the message: 'Operating system not found.' The BIOS correctly "
            "identifies the SSD and lists it first in the boot order. What should the "
            "technician do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Boot from Windows installation media and run Startup Repair to fix the boot record",
                "correct": True,
                "rationale": (
                    "Correct. 'Operating system not found' with the drive detected in "
                    "BIOS indicates the boot record (MBR or GPT/BCD) was corrupted, "
                    "not the drive itself. Windows Startup Repair (accessed from "
                    "installation media) can automatically detect and repair a "
                    "corrupted boot record without data loss."
                ),
            },
            {
                "id": "b",
                "text": "Replace the SSD immediately because the power outage has caused physical damage",
                "correct": False,
                "rationale": (
                    "Incorrect. The BIOS can see and identify the SSD, which means "
                    "the hardware is functional. A boot record corruption (logical "
                    "issue) is the more likely cause — physical replacement is "
                    "premature."
                ),
            },
            {
                "id": "c",
                "text": "Boot into BIOS and change the SATA mode from AHCI to IDE",
                "correct": False,
                "rationale": (
                    "Incorrect. Switching SATA modes while a Windows OS is installed "
                    "will typically make the system unbootable or produce a BSOD. "
                    "The current issue is a corrupted boot record, not a mode "
                    "mismatch."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall Windows from scratch to create a new boot record",
                "correct": False,
                "rationale": (
                    "Incorrect. A full reinstall would erase user data. Startup Repair "
                    "is the non-destructive first option and is specifically designed "
                    "for this scenario."
                ),
            },
        ],
        "explanation": (
            "'Operating system not found' with the drive visible in BIOS means the "
            "boot loader (MBR/GPT or BCD) was corrupted — a common result of an "
            "abrupt power loss mid-write. Boot from Windows installation media, "
            "choose Repair > Troubleshoot > Startup Repair. Alternatively, use "
            "'bootrec /fixmbr', '/fixboot', '/rebuildbcd' from the Command Prompt in "
            "the recovery environment. Data is generally intact."
        ),
    },
    {
        "id": "a1d5v3-010",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A user reports that a folder of critical work documents on their PC has "
            "completely disappeared after a scheduled disk cleanup ran overnight. "
            "The folder is not in the Recycle Bin. Which tool should the technician "
            "use FIRST to attempt recovery?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check Windows File History or Previous Versions (Shadow Copies) for a recoverable snapshot",
                "correct": True,
                "rationale": (
                    "Correct. Windows File History and Previous Versions (Volume Shadow "
                    "Copy) create periodic snapshots of files and folders. Right-clicking "
                    "the parent folder and selecting 'Restore previous versions' is the "
                    "least invasive first recovery option and often restores deleted "
                    "files without third-party tools."
                ),
            },
            {
                "id": "b",
                "text": "Run chkdsk /f to find and repair the deleted files",
                "correct": False,
                "rationale": (
                    "Incorrect. chkdsk /f repairs file-system metadata errors (lost "
                    "clusters, cross-linked files). It does not recover intentionally "
                    "deleted files — the file records have been removed from the "
                    "directory, not corrupted."
                ),
            },
            {
                "id": "c",
                "text": "Defragment the drive to consolidate deleted file fragments into recoverable sectors",
                "correct": False,
                "rationale": (
                    "Incorrect. Defragmentation moves data on the disk and can "
                    "overwrite the space formerly occupied by deleted files, making "
                    "recovery LESS likely. Defragging after a deletion is harmful "
                    "to recovery efforts."
                ),
            },
            {
                "id": "d",
                "text": "Run a full antivirus scan to check whether malware deleted the files",
                "correct": False,
                "rationale": (
                    "Incorrect. The scheduled disk cleanup, not malware, is the probable "
                    "cause. Running an AV scan is secondary; attempting file recovery "
                    "from a snapshot is the immediate priority."
                ),
            },
        ],
        "explanation": (
            "When files are deleted and not in the Recycle Bin, Windows Previous Versions "
            "(backed by VSS/Shadow Copy) is the fastest non-destructive recovery method. "
            "If File History/VSS is not enabled, use a file recovery tool (e.g., "
            "Recuva) on an unmounted or read-only drive to prevent overwriting deleted "
            "data. Never defragment or run intensive disk operations before attempting "
            "recovery."
        ),
    },
    # ── 5.4 Video / Projector / Display ───────────────────────────────────────
    {
        "id": "a1d5v3-011",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A desktop monitor displays a stable image but has a persistent green "
            "horizontal line running across one-third of the screen. The line is "
            "visible regardless of input source and even appears during POST. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A row of stuck or dead pixels in the LCD panel itself",
                "correct": True,
                "rationale": (
                    "Correct. A persistent, unchanging horizontal line visible across "
                    "all input sources and during POST (before the GPU/OS is involved) "
                    "indicates a hardware defect in the LCD panel — a row of stuck or "
                    "dead pixels permanently displaying green. Since it is present even "
                    "at POST, the display itself is defective, not the GPU or OS."
                ),
            },
            {
                "id": "b",
                "text": "A failing GPU producing a damaged video signal on the green channel",
                "correct": False,
                "rationale": (
                    "Incorrect. If the GPU were generating the line, it would change "
                    "when switching to a different input source (such as a second "
                    "computer). A line present on all sources including at POST points "
                    "to the monitor's panel, not the signal source."
                ),
            },
            {
                "id": "c",
                "text": "A loose display cable causing signal interference on the green sub-pixel row",
                "correct": False,
                "rationale": (
                    "Incorrect. A loose cable causes flickering, noise, or intermittent "
                    "signal loss — not a stable, persistent single-color horizontal line "
                    "that is constant across all inputs and power states."
                ),
            },
            {
                "id": "d",
                "text": "The monitor's color calibration profile is corrupted, rendering one row incorrectly",
                "correct": False,
                "rationale": (
                    "Incorrect. Color profiles affect the entire image uniformly, not "
                    "a single pixel row. A stuck pixel row is a hardware-level defect "
                    "independent of color calibration software."
                ),
            },
        ],
        "explanation": (
            "A persistent colored line on an LCD that appears regardless of input "
            "source and during POST is a panel defect (stuck pixel row). Since POST "
            "runs before any OS or driver involvement, the GPU/driver/OS are eliminated "
            "as causes. The monitor panel needs replacement. Verify by connecting a "
            "known-good monitor — if the line disappears, the original panel is "
            "confirmed defective."
        ),
    },
    {
        "id": "a1d5v3-012",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A user notices that their widescreen monitor is displaying a 16:9 video "
            "in a 4:3 aspect ratio with black bars on both sides, even though the "
            "video file is encoded at 1920x1080. The monitor's native resolution is "
            "2560x1440. What should the technician check FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify that the display resolution and scaling settings in the OS are set to the monitor's native resolution",
                "correct": True,
                "rationale": (
                    "Correct. Black bars on the sides with incorrect aspect ratio most "
                    "often indicate the OS is outputting a lower resolution (e.g., "
                    "1280x960 or 1024x768) rather than the native 2560x1440. The display "
                    "then letterboxes/pillarboxes the signal. Setting the correct native "
                    "resolution resolves the issue."
                ),
            },
            {
                "id": "b",
                "text": "Replace the video cable because DisplayPort does not support 16:9 aspect ratios",
                "correct": False,
                "rationale": (
                    "Incorrect. DisplayPort (and HDMI) fully support any aspect ratio "
                    "the GPU outputs. The cable is not the cause of incorrect aspect ratio "
                    "rendering."
                ),
            },
            {
                "id": "c",
                "text": "Update the media player software to correct aspect ratio rendering",
                "correct": False,
                "rationale": (
                    "Incorrect. The description states black bars appear as part of the "
                    "display output — a display/resolution issue — not a media player "
                    "rendering issue. The OS resolution setting should be checked first."
                ),
            },
            {
                "id": "d",
                "text": "Check the monitor's OSD menu and adjust the horizontal size",
                "correct": False,
                "rationale": (
                    "Incorrect. While OSD aspect ratio settings can affect display, "
                    "the primary cause of pillarboxing is an incorrect OS resolution. "
                    "The OS settings should be checked before adjusting hardware OSD controls."
                ),
            },
        ],
        "explanation": (
            "Pillarboxing (black bars on sides) on a widescreen monitor occurs when "
            "the video output resolution uses a 4:3 aspect ratio. Ensure the OS display "
            "settings output the monitor's native resolution (2560x1440 at 16:9). Also "
            "check the GPU control panel's scaling options (maintain aspect ratio vs. "
            "full panel) and the monitor's OSD aspect ratio setting."
        ),
    },
    {
        "id": "a1d5v3-013",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A laptop's built-in display works perfectly, but when the technician "
            "connects an external monitor via HDMI the external monitor shows 'No "
            "Signal.' The HDMI cable has been tested and works on another laptop. "
            "Pressing the Fn+Display toggle key appears to have no effect. What should "
            "the technician try NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Use the OS display settings (right-click desktop → Display Settings) to detect and configure the external display",
                "correct": True,
                "rationale": (
                    "Correct. The Fn key display toggle may not work if the GPU driver "
                    "does not register the event. Using Windows Display Settings → "
                    "Detect (or pressing Win+P) forces the OS and GPU driver to "
                    "enumerate connected displays, which often activates the external "
                    "monitor."
                ),
            },
            {
                "id": "b",
                "text": "Replace the laptop's HDMI port on the motherboard",
                "correct": False,
                "rationale": (
                    "Incorrect. Hardware replacement is a last resort. The Fn key "
                    "not working is more likely a driver or OS issue. Attempting "
                    "OS-level detection first is the correct step."
                ),
            },
            {
                "id": "c",
                "text": "Update the external monitor's firmware to add HDMI input support",
                "correct": False,
                "rationale": (
                    "Incorrect. The monitor is confirmed to work on another laptop — "
                    "firmware is not the issue. The problem is with the laptop's "
                    "output configuration."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall the operating system to reset display driver associations",
                "correct": False,
                "rationale": (
                    "Incorrect. OS reinstallation is an extreme measure. Display settings "
                    "configuration or a GPU driver update are the appropriate next steps."
                ),
            },
        ],
        "explanation": (
            "When the Fn+display toggle is unresponsive, the GPU driver may not be "
            "processing the hotkey event. Win+P (Windows) opens the projection mode "
            "picker (PC screen only / Duplicate / Extend / Second screen only). "
            "Display Settings → Detect forces enumeration of connected displays. "
            "If neither works, update or reinstall the GPU driver — the driver is "
            "responsible for external display detection."
        ),
    },
    # ── 5.5 Mobile Device Issues ──────────────────────────────────────────────
    {
        "id": "a1d5v3-014",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user reports that their smartphone's GPS is inaccurate indoors, showing "
            "their location as several blocks away, but works correctly when they step "
            "outside. The device has full cellular signal throughout. What is the MOST "
            "likely cause of the indoor GPS inaccuracy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "GPS satellite signals are blocked by the building structure, so the device falls back to less accurate cell tower or Wi-Fi triangulation",
                "correct": True,
                "rationale": (
                    "Correct. GPS requires line-of-sight to at least four satellites. "
                    "Buildings attenuate and reflect satellite signals. Indoors, the "
                    "device falls back to cell tower or Wi-Fi-based positioning, which "
                    "has accuracy measured in tens to hundreds of meters — explaining "
                    "the off-by-blocks inaccuracy."
                ),
            },
            {
                "id": "b",
                "text": "The GPS antenna on the smartphone is physically damaged and needs replacement",
                "correct": False,
                "rationale": (
                    "Incorrect. A damaged GPS antenna would produce inaccuracy both "
                    "indoors and outdoors. The fact that it works correctly outside "
                    "rules out hardware damage."
                ),
            },
            {
                "id": "c",
                "text": "Location permissions for the app have been revoked and it is using a cached location",
                "correct": False,
                "rationale": (
                    "Incorrect. Revoked permissions would affect location accuracy "
                    "consistently in all environments, not specifically indoors versus "
                    "outdoors."
                ),
            },
            {
                "id": "d",
                "text": "The cellular carrier is throttling GPS data in high-density areas",
                "correct": False,
                "rationale": (
                    "Incorrect. GPS is a receive-only system using satellite signals — "
                    "carriers cannot throttle GPS. The indoor/outdoor difference is "
                    "purely due to signal attenuation."
                ),
            },
        ],
        "explanation": (
            "GPS (GNSS) requires direct line-of-sight to multiple satellites. Building "
            "materials (concrete, steel, glass with metallic coatings) block or "
            "significantly attenuate satellite signals. Modern smartphones use "
            "A-GPS (Assisted GPS) combined with cell tower triangulation and Wi-Fi "
            "positioning (Google/Apple location databases) as fallback. Indoors, "
            "fallback positioning is inherently less accurate."
        ),
    },
    {
        "id": "a1d5v3-015",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user's smartphone battery drains from 100% to 20% within 4 hours of "
            "normal use, whereas it previously lasted 14+ hours. The battery is "
            "2 years old. No new apps have been recently installed. What is the "
            "MOST likely cause and the correct solution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The lithium-ion battery has degraded due to age and charge cycles; replace the battery",
                "correct": True,
                "rationale": (
                    "Correct. Lithium-ion batteries degrade with each charge cycle, "
                    "losing capacity over time. At 2 years with regular daily use, "
                    "a battery may have undergone 300-500+ cycles, reducing usable "
                    "capacity significantly. Replacement is the correct solution when "
                    "battery health is below ~80%."
                ),
            },
            {
                "id": "b",
                "text": "Screen brightness is set too high; reduce brightness to extend battery life",
                "correct": False,
                "rationale": (
                    "Incorrect. While screen brightness affects battery life, a reduction "
                    "from 14+ hours to 4 hours is too dramatic to be explained by brightness "
                    "alone. Battery age and degradation is the primary cause."
                ),
            },
            {
                "id": "c",
                "text": "The operating system has a memory leak consuming excessive CPU cycles and draining the battery",
                "correct": False,
                "rationale": (
                    "Incorrect. A memory leak might cause accelerated drain, but gradual "
                    "battery degradation over 2 years is the most fitting explanation for "
                    "this symptom pattern, especially without new app installations."
                ),
            },
            {
                "id": "d",
                "text": "The charging cable is delivering insufficient current, under-charging the battery",
                "correct": False,
                "rationale": (
                    "Incorrect. An inadequate charging cable would mean the battery "
                    "never reaches 100% charge, but the user reports a full 100% starting "
                    "charge. Under-charging at start is ruled out; degradation is the "
                    "more logical diagnosis."
                ),
            },
        ],
        "explanation": (
            "Lithium-ion battery chemistry degrades with each charge-discharge cycle. "
            "After 300-500 cycles (approximately 1-2 years of daily charging), capacity "
            "typically drops to 80% or below, noticeably reducing runtime. Most "
            "smartphones show battery health in Settings. If health is below 80%, "
            "battery replacement restores normal runtime. Enable battery optimization "
            "settings as a temporary measure."
        ),
    },
    {
        "id": "a1d5v3-016",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A tablet's Wi-Fi connectivity is intermittent. It connects to the network "
            "and shows full signal strength, but browsing frequently stalls and "
            "reconnects. Bluetooth also drops connections at the same times. Other "
            "Wi-Fi devices nearby work fine. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The tablet's Wi-Fi/Bluetooth combo antenna or antenna cable is loose or damaged",
                "correct": True,
                "rationale": (
                    "Correct. Wi-Fi (2.4/5 GHz) and Bluetooth (2.4 GHz) in tablets "
                    "typically share a combo antenna or at minimum share the same "
                    "antenna cable path. Simultaneous intermittent failures of both "
                    "wireless technologies on one device while other devices work "
                    "normally points to a hardware antenna fault on the tablet."
                ),
            },
            {
                "id": "b",
                "text": "The Wi-Fi router is experiencing channel congestion",
                "correct": False,
                "rationale": (
                    "Incorrect. If router congestion were the cause, all devices would "
                    "be affected equally. Other devices working fine isolates the problem "
                    "to this tablet."
                ),
            },
            {
                "id": "c",
                "text": "The tablet has too many cached DNS entries causing resolution failures",
                "correct": False,
                "rationale": (
                    "Incorrect. Stale DNS cache can cause name resolution failures but "
                    "does not explain simultaneous Bluetooth drops or the physical "
                    "connection-level intermittency described."
                ),
            },
            {
                "id": "d",
                "text": "The 2.4 GHz band is being jammed by a nearby microwave oven",
                "correct": False,
                "rationale": (
                    "Incorrect. Microwave interference would affect all 2.4 GHz devices "
                    "in the area, not just this one tablet. Other devices functioning "
                    "normally rules out environmental RF interference."
                ),
            },
        ],
        "explanation": (
            "In tablets and laptops, Wi-Fi and Bluetooth share a combo radio chip and "
            "often share antenna cables routed through the device chassis. A loose "
            "antenna connector (commonly disturbed during screen repairs or drops) "
            "causes poor signal reception and intermittent dropouts on both radio "
            "technologies simultaneously. Inspect the antenna cable connections to the "
            "wireless module."
        ),
    },
    # ── 5.6 Printer Issues ────────────────────────────────────────────────────
    {
        "id": "a1d5v3-017",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "An inkjet printer produces output where all colors appear correct but "
            "the black text is faded and streaky, even after printing a cleaning page. "
            "Running the head alignment utility makes no difference. What is the MOST "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The black ink cartridge nozzles are clogged or the black ink is nearly depleted",
                "correct": True,
                "rationale": (
                    "Correct. Inkjet print heads can have individual color nozzles "
                    "clog independently. Faded and streaky black output with other "
                    "colors intact isolates the problem to the black (K) ink channel — "
                    "either clogged nozzles or near-empty ink. A deep nozzle cleaning "
                    "cycle or cartridge replacement addresses this."
                ),
            },
            {
                "id": "b",
                "text": "The print head carriage belt has stretched, causing misalignment of the black pass",
                "correct": False,
                "rationale": (
                    "Incorrect. A stretched carriage belt causes misalignment (blurred "
                    "or offset print) affecting all colors in the scan direction, not "
                    "isolated black streaking that persists after alignment."
                ),
            },
            {
                "id": "c",
                "text": "The paper feed rollers are worn, causing the paper to move unevenly through the ink zone",
                "correct": False,
                "rationale": (
                    "Incorrect. Worn paper rollers cause skewing, horizontal banding, "
                    "or multi-page feeds, not selective faded black output while "
                    "colors print correctly."
                ),
            },
            {
                "id": "d",
                "text": "The print driver is configured to use composite black (CMY mix) instead of the black cartridge",
                "correct": False,
                "rationale": (
                    "Incorrect. While composite black mode uses CMY inks instead of "
                    "the K cartridge, this would produce dull brownish-black text but "
                    "not streaking. The streaky symptom specifically indicates nozzle "
                    "clogging or depleted ink."
                ),
            },
        ],
        "explanation": (
            "Inkjet printers use separate CMYK ink channels. Faded and streaky black "
            "output with other colors printing correctly isolates the issue to the "
            "black ink channel. Perform a deep nozzle cleaning cycle, then print a "
            "nozzle check pattern. If cleaning doesn't resolve it, the black cartridge "
            "needs replacement. Note: repeated aggressive cleaning wastes ink — if two "
            "cleanings don't help, replace the cartridge."
        ),
    },
    {
        "id": "a1d5v3-018",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A laser printer consistently jams at the same point in the paper path — "
            "approximately 6 inches from the front of the printer, every time. Paper "
            "from a brand-new ream is being used. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A worn or damaged paper feed roller at that location in the paper path",
                "correct": True,
                "rationale": (
                    "Correct. Consistent jams at the same location in the paper path "
                    "indicate a mechanical component at that point is faulty — most "
                    "likely a feed roller that is worn, glazed, or has debris on it. "
                    "Using fresh paper rules out paper quality as a cause."
                ),
            },
            {
                "id": "b",
                "text": "The paper is loaded against the wrong side of the tray guide, causing skewing",
                "correct": False,
                "rationale": (
                    "Incorrect. Improperly loaded paper would cause skewing and jams "
                    "at entry to the paper path (near the tray), not consistently at "
                    "a specific point 6 inches in."
                ),
            },
            {
                "id": "c",
                "text": "The fuser temperature is too low, causing the paper to stick to the fuser roller",
                "correct": False,
                "rationale": (
                    "Incorrect. A cool fuser can cause paper to wrap around the fuser "
                    "roller (typically near the output end, not 6 inches from the "
                    "front/input). Additionally, a fuser issue would typically also "
                    "affect toner adhesion."
                ),
            },
            {
                "id": "d",
                "text": "A static electricity buildup is attracting the paper to the metal tray walls",
                "correct": False,
                "rationale": (
                    "Incorrect. Static buildup in printers usually causes sheets to "
                    "stick together at the output tray or affects print quality — not "
                    "a repeatable jam at a fixed point inside the paper path."
                ),
            },
        ],
        "explanation": (
            "Repeatable jams at the same location in the paper path are the hallmark "
            "of a mechanical fault at that specific point — worn rollers, debris, "
            "or a damaged guide. Clean the rollers in the jam zone with isopropyl "
            "alcohol. If cleaning doesn't resolve it, replace the roller assembly "
            "at that stage. Many laser printers have service kits that include the "
            "commonly worn rollers."
        ),
    },
    {
        "id": "a1d5v3-019",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "After a toner cartridge replacement, a laser printer produces pages with "
            "a faint ghost image of the previous page appearing below the current page "
            "content — like a shadow or second impression. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The new toner cartridge contains a drum that is not fully erasing the previous image, causing ghosting",
                "correct": True,
                "rationale": (
                    "Correct. Ghosting (or page ghosting) in laser printing occurs when "
                    "residual charge or toner from a previous image is not fully cleaned "
                    "from the drum before the next page. This is often caused by a failing "
                    "drum cleaning blade or a defective drum in the new cartridge. The "
                    "ghost appears at intervals corresponding to the drum circumference."
                ),
            },
            {
                "id": "b",
                "text": "The fuser is overheating and re-transferring already-fused toner from the paper back to the drum",
                "correct": False,
                "rationale": (
                    "Incorrect. Fuser overheating causes paper warping, burning smell, "
                    "or charring — not a ghost image of the previous page content. "
                    "Ghosting is a drum/charge issue."
                ),
            },
            {
                "id": "c",
                "text": "The transfer corona wire is coated with toner and transferring an extra layer to each page",
                "correct": False,
                "rationale": (
                    "Incorrect. A contaminated transfer corona would cause poor toner "
                    "transfer (faded or uneven output), not a recognizable ghost of a "
                    "previous page's specific content."
                ),
            },
            {
                "id": "d",
                "text": "The print buffer in the printer's RAM is retaining the previous print job",
                "correct": False,
                "rationale": (
                    "Incorrect. A buffer retention issue would cause actual full-page "
                    "reprints of previous jobs, not a faint ghost shadow at a fixed "
                    "interval. This is a physical drum residue issue, not a data issue."
                ),
            },
        ],
        "explanation": (
            "Page ghosting in laser printers is caused by residual electrostatic charge "
            "or leftover toner on the photosensitive drum that is not fully removed by "
            "the drum cleaning blade. The ghost appears at intervals matching the drum "
            "circumference. If the issue started with a new cartridge, the cartridge "
            "drum or cleaning blade may be defective — try a different cartridge. "
            "Also check primary charge roller condition."
        ),
    },
    {
        "id": "a1d5v3-020",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A thermal receipt printer in a retail store is producing blank receipts "
            "even though the paper roll has been replaced with a new roll and the "
            "print head appears clean. What should the technician check NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify the thermal paper is loaded with the correct (coated) side facing the print head",
                "correct": True,
                "rationale": (
                    "Correct. Thermal printers apply heat to thermally-sensitive paper "
                    "to create an image. Thermal paper has only one coated side. If the "
                    "paper is loaded backward (uncoated side toward the print head), the "
                    "result is a blank receipt because the heat activates nothing. "
                    "This is the most common cause after a paper roll change."
                ),
            },
            {
                "id": "b",
                "text": "Replace the thermal print head, which has burned out from overuse",
                "correct": False,
                "rationale": (
                    "Incorrect. A burned-out print head would have shown a gradual "
                    "decline in print quality before producing blanks. A fresh roll "
                    "immediately producing blanks strongly suggests backward paper "
                    "loading, not head failure."
                ),
            },
            {
                "id": "c",
                "text": "Reconnect the USB cable; a loose connection is causing the printer to receive empty data",
                "correct": False,
                "rationale": (
                    "Incorrect. A disconnected USB cable would cause the receipt to not "
                    "print at all (no movement, no output). A blank receipt being "
                    "physically ejected indicates the printer is receiving data and "
                    "feeding paper — just not activating the coating."
                ),
            },
            {
                "id": "d",
                "text": "Update the printer firmware to re-enable the thermal control circuit",
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware does not control whether the thermal coating "
                    "is activated — that is determined by the paper orientation and head "
                    "temperature. Firmware updates are not the appropriate first step "
                    "for blank thermal output."
                ),
            },
        ],
        "explanation": (
            "Thermal printers create images by applying localized heat to paper coated "
            "with a thermochromic layer. The coating is only on one side. If the paper "
            "is loaded with the uncoated side facing the print head, heat produces "
            "no visible mark — blank receipts result. To identify the coated side, "
            "scratch with a fingernail or apply a brief heat source: the coated side "
            "will darken. Load with the coated side facing inward toward the head."
        ),
    },
    # ── 5.7 Wired/Wireless Network Troubleshooting ────────────────────────────
    {
        "id": "a1d5v3-021",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A network technician is investigating slow throughput on a Gigabit "
            "Ethernet link between a workstation and a switch. The cable is CAT6 "
            "and 8 meters long. The switch port and NIC both show 100 Mbps / "
            "half-duplex in their respective status pages, even though both support "
            "1000BASE-T. What is the MOST likely cause of the speed downgrade?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A duplex mismatch — one side is set to auto-negotiate while the other is hard-coded to 100/full, preventing proper 1000BASE-T negotiation",
                "correct": True,
                "rationale": (
                    "Correct. A duplex/speed mismatch between the NIC and the switch "
                    "port (one hard-coded, one set to auto-negotiate) causes the "
                    "auto-negotiating side to fall back to its lowest common speed "
                    "and potentially half-duplex. Both should be set to 'Auto' or "
                    "both hard-coded to the same values for 1 Gbps to negotiate."
                ),
            },
            {
                "id": "b",
                "text": "CAT6 cable cannot support 1000BASE-T — CAT6A is required for Gigabit speeds",
                "correct": False,
                "rationale": (
                    "Incorrect. CAT5e and above support 1000BASE-T (Gigabit Ethernet). "
                    "CAT6 exceeds the requirement. The cable is not the limiting factor "
                    "at 8 meters."
                ),
            },
            {
                "id": "c",
                "text": "The workstation's NIC is defective and must be replaced with a certified 1 GbE NIC",
                "correct": False,
                "rationale": (
                    "Incorrect. A defective NIC would typically cause connection failure "
                    "or errors, not a clean negotiation to 100/half. The duplex mismatch "
                    "scenario explains the fallback behavior."
                ),
            },
            {
                "id": "d",
                "text": "The switch VLAN configuration is throttling the workstation's port to 100 Mbps",
                "correct": False,
                "rationale": (
                    "Incorrect. VLAN configuration does not control physical link speed. "
                    "The duplex mismatch is the standard explanation for this symptom "
                    "on hardware that is physically capable of Gigabit."
                ),
            },
        ],
        "explanation": (
            "Duplex mismatch (one side auto, one side hard-coded) is a common cause of "
            "unexpected speed/duplex negotiation failures. When one side is forced to "
            "100 Mbps full-duplex and the other is auto-negotiating, the auto side "
            "may fall back to half-duplex at 100 Mbps, causing late collisions and "
            "poor throughput. Best practice: set both NIC and switch port to Auto "
            "negotiation, or hard-code both sides to matching values."
        ),
    },
    {
        "id": "a1d5v3-022",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician suspects that port 443 on a remote web server at 10.1.1.100 "
            "is blocked by an intermediate firewall. Which Windows command provides "
            "the MOST direct test of TCP connectivity on that specific port?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Test-NetConnection -ComputerName 10.1.1.100 -Port 443",
                "correct": True,
                "rationale": (
                    "Correct. Test-NetConnection (PowerShell) performs a TCP connection "
                    "test to a specific host and port, reporting TcpTestSucceeded as "
                    "True or False. This directly tests port-level TCP reachability, "
                    "far more informative than a simple ICMP ping."
                ),
            },
            {
                "id": "b",
                "text": "ping 10.1.1.100",
                "correct": False,
                "rationale": (
                    "Incorrect. ICMP ping tests host reachability (layer 3) only — it "
                    "does not test whether a specific TCP port is open or blocked by "
                    "a firewall."
                ),
            },
            {
                "id": "c",
                "text": "tracert 10.1.1.100",
                "correct": False,
                "rationale": (
                    "Incorrect. tracert traces the routing path using ICMP and does "
                    "not test TCP port status. A firewall blocking port 443 would not "
                    "be visible in a tracert output."
                ),
            },
            {
                "id": "d",
                "text": "nslookup 10.1.1.100",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup performs a reverse DNS lookup on an IP address. "
                    "It does not test TCP connectivity to any port."
                ),
            },
        ],
        "explanation": (
            "Test-NetConnection (PowerShell) is the built-in Windows tool for testing "
            "TCP port connectivity. It outputs TcpTestSucceeded (True/False), ping "
            "RTT, and trace route hops. On older systems without PowerShell 4.0+, "
            "'telnet 10.1.1.100 443' can test TCP port connectivity (if the Telnet "
            "client is installed). For Linux, 'nc -zv 10.1.1.100 443' or "
            "'curl -I https://10.1.1.100' are equivalent."
        ),
    },
    {
        "id": "a1d5v3-023",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician wants to flush the local DNS resolver cache on a Windows "
            "workstation because the user is receiving a stale IP address for an "
            "internal server that was recently migrated. Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ipconfig /flushdns",
                "correct": True,
                "rationale": (
                    "Correct. 'ipconfig /flushdns' purges the local DNS resolver cache "
                    "on a Windows workstation, forcing subsequent name lookups to query "
                    "the DNS server for fresh records rather than serving stale cached "
                    "IP addresses."
                ),
            },
            {
                "id": "b",
                "text": "ipconfig /release",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ipconfig /release' releases the current DHCP IP address "
                    "lease — it does not affect the DNS cache."
                ),
            },
            {
                "id": "c",
                "text": "netstat -f",
                "correct": False,
                "rationale": (
                    "Incorrect. 'netstat -f' displays fully qualified domain names in "
                    "the connections list; it does not flush DNS cache."
                ),
            },
            {
                "id": "d",
                "text": "nslookup /reset",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup does not have a '/reset' switch that flushes "
                    "the OS DNS cache. nslookup queries DNS servers but does not manage "
                    "the local cache."
                ),
            },
        ],
        "explanation": (
            "'ipconfig /flushdns' clears the Windows DNS resolver cache (stored in "
            "the DNS Client service). This forces fresh DNS lookups for all subsequent "
            "requests. Use 'ipconfig /displaydns' first to confirm a stale entry exists "
            "before flushing. On Linux: 'sudo systemd-resolve --flush-caches' or "
            "restart nscd/dnsmasq depending on the distribution."
        ),
    },
    {
        "id": "a1d5v3-024",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician at the command prompt types 'arp -a' on a Windows workstation "
            "that cannot reach the default gateway (192.168.1.1). The ARP table shows "
            "192.168.1.1 mapped to ff-ff-ff-ff-ff-ff. What does this indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The ARP resolution for the gateway has failed; the broadcast MAC address indicates the gateway is unreachable or ARP is not being answered",
                "correct": True,
                "rationale": (
                    "Correct. A MAC address of ff-ff-ff-ff-ff-ff is the Ethernet "
                    "broadcast address. Its presence in the ARP table for the gateway IP "
                    "means ARP requests were sent but no ARP reply was received — the "
                    "gateway is not responding to ARP, indicating it is offline, on a "
                    "different VLAN, or the workstation's NIC is misconfigured."
                ),
            },
            {
                "id": "b",
                "text": "The gateway's MAC address has been successfully resolved and all traffic is being forwarded",
                "correct": False,
                "rationale": (
                    "Incorrect. A legitimate resolved MAC address would be a unicast "
                    "address (e.g., 00-1A-2B-3C-4D-5E). The broadcast address "
                    "ff-ff-ff-ff-ff-ff is not a valid resolved unicast MAC and indicates "
                    "resolution failure."
                ),
            },
            {
                "id": "c",
                "text": "The gateway is a broadcast device (hub) and intentionally uses the broadcast MAC",
                "correct": False,
                "rationale": (
                    "Incorrect. Gateways/routers never legitimately use ff-ff-ff-ff-ff-ff "
                    "as their unicast MAC address. The all-ones MAC is strictly a "
                    "layer 2 broadcast destination, not a device MAC."
                ),
            },
            {
                "id": "d",
                "text": "An ARP poisoning attack has replaced the gateway's real MAC with the broadcast address",
                "correct": False,
                "rationale": (
                    "Incorrect. ARP poisoning typically replaces the gateway MAC with "
                    "the attacker's MAC (a valid unicast address), not the broadcast "
                    "address. The broadcast MAC in ARP cache indicates failed resolution, "
                    "not an attack."
                ),
            },
        ],
        "explanation": (
            "The ARP cache stores IP-to-MAC mappings learned from ARP replies. "
            "ff-ff-ff-ff-ff-ff (all ones) is the Ethernet broadcast address, not "
            "a valid host MAC. Seeing it in the ARP cache for the gateway means the "
            "workstation sent an ARP request (broadcast) but never received a unicast "
            "reply. This indicates the gateway is unreachable at layer 2 — possible "
            "causes: wrong subnet, VLAN mismatch, gateway offline, or wrong gateway IP "
            "configured."
        ),
    },
    {
        "id": "a1d5v3-025",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "Multiple workstations on the same switch experience network connectivity "
            "loss simultaneously every evening around 6 PM, and connectivity restores "
            "automatically within 30 seconds. Network logs show a Spanning Tree "
            "topology change notification at 6 PM each time. What is the MOST likely "
            "cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A device on the network is powering off at 6 PM, triggering an STP topology change that temporarily clears the MAC address table",
                "correct": True,
                "rationale": (
                    "Correct. When a switch port goes down (device powers off), STP "
                    "generates a Topology Change Notification (TCN). This causes all "
                    "switches to age out their MAC address tables, temporarily flooding "
                    "traffic until tables are repopulated — causing brief connectivity "
                    "loss. The 6 PM pattern suggests a scheduled shutdown (e.g., a "
                    "server or device on a power schedule)."
                ),
            },
            {
                "id": "b",
                "text": "The ISP is performing maintenance at 6 PM and temporarily dropping the internet uplink",
                "correct": False,
                "rationale": (
                    "Incorrect. ISP maintenance would affect internet access but not "
                    "internal LAN connectivity between workstations on the same switch. "
                    "The STP topology change notification specifically points to a local "
                    "layer 2 event."
                ),
            },
            {
                "id": "c",
                "text": "A DHCP lease renewal storm at 6 PM is consuming all available bandwidth",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP lease renewals do not trigger STP topology changes. "
                    "The STP TCN is the key evidence pointing to a port state change, "
                    "not a bandwidth or DHCP event."
                ),
            },
            {
                "id": "d",
                "text": "The switch is running a scheduled firmware update at 6 PM and rebooting",
                "correct": False,
                "rationale": (
                    "Incorrect. A switch reboot would cause longer downtime (minutes, "
                    "not 30 seconds) and affect all ports simultaneously in a different "
                    "pattern than a topology change notification on a specific port."
                ),
            },
        ],
        "explanation": (
            "Spanning Tree Protocol (STP) topology changes occur when a switch port "
            "changes state (up or down). A TCN causes switches to reduce their MAC "
            "address table aging timer, flushing learned addresses and temporarily "
            "flooding traffic as the table is rebuilt. The 30-second disruption at a "
            "consistent time pattern indicates a device powering on or off. Identify "
            "which port the TCN originates from using switch logs, then investigate "
            "what device is on that port."
        ),
    },
    {
        "id": "a1d5v3-026",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A user connects a laptop directly to the cable modem with an Ethernet "
            "cable (bypassing the router) and gets internet access with a public IP. "
            "When reconnected through the router, there is no internet access. Other "
            "devices connected to the router also cannot reach the internet. What "
            "is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router's WAN interface has not obtained a DHCP lease from the ISP, or the WAN connection is misconfigured",
                "correct": True,
                "rationale": (
                    "Correct. If a direct modem connection works but all devices through "
                    "the router fail, the problem is between the modem and the router's "
                    "WAN port — the router is not obtaining a valid WAN IP from the ISP "
                    "via DHCP, PPPoE, or static configuration. Check the router's WAN "
                    "status page."
                ),
            },
            {
                "id": "b",
                "text": "The laptop's NIC is defective and requires replacement",
                "correct": False,
                "rationale": (
                    "Incorrect. The laptop works when connected directly to the modem, "
                    "so the NIC is functional. The issue affects all devices through "
                    "the router, pointing to the router's WAN configuration."
                ),
            },
            {
                "id": "c",
                "text": "The DNS server addresses in the router's LAN DHCP configuration are incorrect",
                "correct": False,
                "rationale": (
                    "Incorrect. Incorrect DNS would allow IP connectivity but prevent "
                    "name resolution. The symptom is 'no internet access' at all, "
                    "suggesting no WAN IP — not just a DNS issue."
                ),
            },
            {
                "id": "d",
                "text": "The cable modem needs to be replaced because it cannot handle routing",
                "correct": False,
                "rationale": (
                    "Incorrect. The modem works correctly when connected directly. The "
                    "modem is not the problem. The router's WAN interface configuration "
                    "is the fault point."
                ),
            },
        ],
        "explanation": (
            "When a direct modem connection works but all router-connected devices fail, "
            "the fault is the router's WAN interface. Common causes: the router's WAN "
            "type is set to Static but should be DHCP; the MAC address the ISP recognizes "
            "changed (clone the laptop MAC); PPPoE credentials are wrong; or the router "
            "needs a restart after the modem was released from a direct connection. "
            "Check the router admin panel's WAN/Internet Status page."
        ),
    },
    {
        "id": "a1d5v3-027",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A 5 GHz Wi-Fi network shows excellent signal strength on a laptop but "
            "delivers only 20 Mbps throughput, far below the expected 300+ Mbps. "
            "The router is 5 meters away, line-of-sight. A speed test from a wired "
            "connection on the same router delivers 450 Mbps. What should the "
            "technician investigate FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check whether the laptop's wireless adapter supports only 802.11n (single-stream) rather than 802.11ac/Wi-Fi 5",
                "correct": True,
                "rationale": (
                    "Correct. A client device that only supports 802.11n (150 Mbps "
                    "single-stream maximum) will never achieve 300+ Mbps regardless of "
                    "signal strength or router capability. Throughput is limited by the "
                    "slower of the two devices. Checking the adapter spec (Device Manager "
                    "→ Network Adapters → Properties) is the first diagnostic step."
                ),
            },
            {
                "id": "b",
                "text": "Replace the Wi-Fi router because its 5 GHz radio is degraded",
                "correct": False,
                "rationale": (
                    "Incorrect. The router delivers 450 Mbps on wired connections, "
                    "indicating the internet and routing subsystem are fine. The bottleneck "
                    "is the wireless link, which is client-capability dependent."
                ),
            },
            {
                "id": "c",
                "text": "Move the router closer to eliminate any remaining signal attenuation",
                "correct": False,
                "rationale": (
                    "Incorrect. The laptop already shows excellent signal at 5 meters "
                    "line-of-sight. Signal attenuation is not the limiting factor. "
                    "The throughput cap is a capability issue, not a signal issue."
                ),
            },
            {
                "id": "d",
                "text": "Enable 160 MHz channel width on the router to increase throughput",
                "correct": False,
                "rationale": (
                    "Incorrect. Wider channels benefit clients that support them. If "
                    "the laptop adapter is 802.11n single-stream, it cannot benefit "
                    "from 160 MHz channels. The adapter capability must be verified "
                    "first."
                ),
            },
        ],
        "explanation": (
            "Wireless throughput is limited by the capabilities of the weakest link — "
            "either the router or the client adapter. 802.11n single-stream (SISO): "
            "~150 Mbps theoretical / ~70 Mbps practical. 802.11ac (Wi-Fi 5): up to "
            "867 Mbps per stream. 802.11ax (Wi-Fi 6): even higher. Always check the "
            "client adapter specification (Device Manager or system info) before "
            "investigating other causes of poor wireless throughput."
        ),
    },
    # ── Multiple Response Questions ───────────────────────────────────────────
    {
        "id": "a1d5v3-028",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "According to the CompTIA troubleshooting methodology, which TWO activities "
            "are explicitly part of Step 5 (Verify full system functionality and "
            "implement preventive measures)? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Confirm with the user that the original problem is resolved and that no new issues have been introduced",
                "correct": True,
                "rationale": (
                    "Correct. User confirmation that the problem is resolved is an "
                    "explicit component of Step 5. The technician must verify the fix "
                    "worked from the user's perspective, not just from technical testing."
                ),
            },
            {
                "id": "b",
                "text": "Implement measures to prevent the same problem from recurring (e.g., configure automatic updates, backups)",
                "correct": True,
                "rationale": (
                    "Correct. Preventive measures are the second sub-activity of Step 5. "
                    "After verifying the fix, take steps to prevent recurrence — examples: "
                    "enabling automatic driver updates, creating a backup, applying a "
                    "security patch, or documenting a configuration change."
                ),
            },
            {
                "id": "c",
                "text": "Establish a new theory of probable cause for any secondary issues noticed",
                "correct": False,
                "rationale": (
                    "Incorrect. Establishing a new theory is Step 2. If a secondary issue "
                    "is discovered during Step 5, the technician would open a new ticket "
                    "and restart the methodology from Step 1 for that separate issue."
                ),
            },
            {
                "id": "d",
                "text": "Document the problem, all actions taken, and the outcome in the ticketing system",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation is Step 6, which occurs after Step 5 is "
                    "complete. Step 5 focuses on verification and prevention; Step 6 "
                    "focuses on recording."
                ),
            },
        ],
        "explanation": (
            "Step 5 has two components: (a) Verify full system functionality — test "
            "that the fix worked, confirm with the user; and (b) Implement preventive "
            "measures — take action to prevent recurrence (patches, backups, config "
            "changes, user education). Only after both parts of Step 5 are complete "
            "should the technician move to Step 6 (Documentation)."
        ),
    },
    {
        "id": "a1d5v3-029",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A workstation displays a 'No bootable device' error after what appeared "
            "to be a successful Windows 11 installation on a new NVMe SSD. Which TWO "
            "BIOS/UEFI settings should the technician verify? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Confirm that Secure Boot settings are compatible with the Windows installation (UEFI + GPT)",
                "correct": True,
                "rationale": (
                    "Correct. Windows 11 requires UEFI with Secure Boot and a GPT "
                    "partition scheme. If the OS was installed in Legacy/BIOS mode "
                    "with MBR, or if Secure Boot was toggled incorrectly after "
                    "installation, the system will fail to boot. UEFI mode and "
                    "Secure Boot settings must match the installation."
                ),
            },
            {
                "id": "b",
                "text": "Verify the NVMe SSD is listed in the UEFI boot order and is the selected primary boot device",
                "correct": True,
                "rationale": (
                    "Correct. Even if the installation was successful, if the SSD is "
                    "not listed first in the UEFI boot priority order, the system will "
                    "attempt to boot from another device and fail with 'no bootable "
                    "device.' Confirming boot order is a fundamental check."
                ),
            },
            {
                "id": "c",
                "text": "Increase the RAM voltage to ensure the NVMe SSD receives adequate power during boot",
                "correct": False,
                "rationale": (
                    "Incorrect. NVMe SSDs are powered by the PCIe slot, not RAM voltage "
                    "rails. RAM voltage has no effect on NVMe SSD power or boot "
                    "initialization."
                ),
            },
            {
                "id": "d",
                "text": "Disable hyperthreading to reduce boot initialization time",
                "correct": False,
                "rationale": (
                    "Incorrect. Hyperthreading is a CPU execution feature that has no "
                    "bearing on UEFI boot device detection or boot record loading. "
                    "Disabling it would not resolve a 'no bootable device' error."
                ),
            },
        ],
        "explanation": (
            "A 'No bootable device' error after OS installation has two common UEFI "
            "causes: (1) Boot order — the NVMe SSD must be first; (2) Boot mode "
            "mismatch — Windows 11 requires UEFI mode with GPT. If installed in CSM/"
            "Legacy mode with MBR, or if Secure Boot is misconfigured, the UEFI "
            "firmware will not recognize the boot loader. Verify both in BIOS setup."
        ),
    },
    {
        "id": "a1d5v3-030",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A technician is configuring a new RAID array for a file server and "
            "needs both fault tolerance AND improved read performance. Which TWO "
            "RAID levels provide fault tolerance AND offer read performance benefits "
            "over a single disk? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "RAID 1 (mirroring) — reads can be distributed between mirrors",
                "correct": True,
                "rationale": (
                    "Correct. RAID 1 provides fault tolerance (one drive can fail). "
                    "Many RAID controllers can split read requests across both mirror "
                    "members, providing read performance that approaches 2x that of "
                    "a single drive."
                ),
            },
            {
                "id": "b",
                "text": "RAID 5 (distributed parity) — read performance scales with the number of drives",
                "correct": True,
                "rationale": (
                    "Correct. RAID 5 with N drives provides fault tolerance (one drive "
                    "failure tolerated) and read performance roughly equal to (N-1) "
                    "drives, since data is striped across all drives and reads can be "
                    "parallelized."
                ),
            },
            {
                "id": "c",
                "text": "RAID 0 (striping) — maximum read and write performance with data spread across all drives",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 0 provides excellent performance but zero fault "
                    "tolerance — losing any single drive loses all data. The question "
                    "requires fault tolerance."
                ),
            },
            {
                "id": "d",
                "text": "JBOD (Just a Bunch of Disks) — volumes span multiple drives for maximum capacity",
                "correct": False,
                "rationale": (
                    "Incorrect. JBOD concatenates drives into a single volume but "
                    "provides no fault tolerance and no performance improvement over "
                    "a single disk. Losing any drive in a JBOD set loses data on that "
                    "segment."
                ),
            },
        ],
        "explanation": (
            "RAID levels with both fault tolerance and read performance improvement: "
            "RAID 1 tolerates one drive failure and can split reads (if controller "
            "supports it). RAID 5 tolerates one drive failure and stripes data for "
            "parallel reads. RAID 6 tolerates two failures with read benefits. RAID 10 "
            "(mirror + stripe) offers the best of both. RAID 0 is performance-only "
            "(no fault tolerance). JBOD offers neither."
        ),
    },
    {
        "id": "a1d5v3-031",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A technician is diagnosing a smartphone that runs hot and has excessive "
            "battery drain even when idle. Which TWO diagnostic steps should be "
            "performed FIRST? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check the device's battery usage statistics to identify which app is consuming the most CPU/power while in background",
                "correct": True,
                "rationale": (
                    "Correct. Battery usage statistics (Settings → Battery on iOS/Android) "
                    "show which applications are consuming power. A rogue or misbehaving "
                    "background app is the most common cause of unexpected heat and "
                    "battery drain when idle."
                ),
            },
            {
                "id": "b",
                "text": "Force-stop recently installed or suspicious applications and monitor temperature",
                "correct": True,
                "rationale": (
                    "Correct. Force-stopping suspicious background apps eliminates them "
                    "as a cause and is a non-destructive diagnostic step. If the "
                    "temperature normalizes after force-stopping a specific app, that "
                    "app is the culprit."
                ),
            },
            {
                "id": "c",
                "text": "Immediately perform a factory reset to eliminate all possible software causes",
                "correct": False,
                "rationale": (
                    "Incorrect. A factory reset is a drastic, last-resort step that "
                    "erases all user data. It should only be performed after less "
                    "destructive diagnostic steps have failed to isolate the cause."
                ),
            },
            {
                "id": "d",
                "text": "Replace the battery as heat always indicates battery failure",
                "correct": False,
                "rationale": (
                    "Incorrect. Heat and battery drain are symptoms of many causes — "
                    "software (runaway app, malware), hardware (failing battery), or "
                    "configuration (background sync). Battery replacement without "
                    "diagnosing the root cause may not resolve the issue."
                ),
            },
        ],
        "explanation": (
            "Excessive heat and battery drain on a smartphone are most commonly caused "
            "by runaway background processes or applications. Battery usage statistics "
            "provide a ranked list of power consumers. Force-stopping the top consumer "
            "or uninstalling recently added apps is the least destructive first step. "
            "If the issue persists after all app-level investigation, consider a factory "
            "reset, and if still present, hardware diagnostics for the battery."
        ),
    },
    {
        "id": "a1d5v3-032",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A network printer appears online in the print queue, but jobs sent to "
            "it remain stuck with 'Error - Printing.' Deleting and resubmitting the "
            "jobs has no effect. Which TWO steps are MOST likely to resolve the issue? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Clear the print spooler by stopping the Print Spooler service, deleting files from the spool folder, then restarting the service",
                "correct": True,
                "rationale": (
                    "Correct. A corrupted print job in the Windows spooler can block "
                    "all subsequent jobs. Stopping the Print Spooler (services.msc or "
                    "'net stop spooler'), deleting files from "
                    "C:\\Windows\\System32\\spool\\PRINTERS\\, and restarting the service "
                    "clears the blockage."
                ),
            },
            {
                "id": "b",
                "text": "Verify the printer's IP address has not changed and update the printer port if necessary",
                "correct": True,
                "rationale": (
                    "Correct. If the network printer's IP address changed (e.g., after "
                    "a DHCP lease renewal or router reboot), the Windows printer port "
                    "still points to the old IP. The printer appears 'online' in the "
                    "queue UI but jobs fail because the connection goes to an incorrect "
                    "address. Updating the port IP resolves this."
                ),
            },
            {
                "id": "c",
                "text": "Reinstall Windows on the workstation to refresh all printer-related system files",
                "correct": False,
                "rationale": (
                    "Incorrect. A full OS reinstall is massively disproportionate to "
                    "a printer spooler or IP address issue. The two targeted fixes above "
                    "address the most common causes without data loss."
                ),
            },
            {
                "id": "d",
                "text": "Replace the printer's network card because 'Error - Printing' always indicates hardware failure",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Error - Printing' is a Windows print queue status "
                    "that most commonly indicates a software/configuration problem "
                    "(corrupted spooler or wrong port IP), not printer hardware failure."
                ),
            },
        ],
        "explanation": (
            "Stuck print jobs with 'Error - Printing' have two common root causes: "
            "(1) Corrupted spooler files — stop Print Spooler service, clear "
            "C:\\Windows\\System32\\spool\\PRINTERS\\, restart service; "
            "(2) Changed printer IP — verify the printer port IP in Printer Properties "
            "→ Ports matches the printer's current IP. Use a reserved DHCP address "
            "or static IP on the printer to prevent future IP changes."
        ),
    },
    {
        "id": "a1d5v3-033",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A new employee's workstation has an IP address of 169.254.22.5, cannot "
            "reach any network resources, and the network cable light on the switch "
            "port is off. Which TWO steps should the technician perform? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check that the Ethernet cable is fully plugged in at both the workstation NIC and the switch port",
                "correct": True,
                "rationale": (
                    "Correct. The switch port activity light being off is a strong "
                    "indicator of no physical link. The cable may not be fully inserted, "
                    "may be the wrong type, or may be damaged. Physical layer (Layer 1) "
                    "must be confirmed before investigating IP configuration."
                ),
            },
            {
                "id": "b",
                "text": "Test the cable with a cable tester or swap it for a known-good cable to verify Layer 1 connectivity",
                "correct": True,
                "rationale": (
                    "Correct. An APIPA address combined with no switch port link light "
                    "strongly suggests a physical layer failure. Testing or replacing "
                    "the cable verifies whether the cable is the cause. A cable tester "
                    "checks for continuity, shorts, and proper pin-out."
                ),
            },
            {
                "id": "c",
                "text": "Configure a static IP address to bypass the DHCP failure",
                "correct": False,
                "rationale": (
                    "Incorrect. Assigning a static IP will not help if there is no "
                    "physical link (Layer 1 failure). IP configuration issues are "
                    "irrelevant until the physical connection is established."
                ),
            },
            {
                "id": "d",
                "text": "Replace the network switch because the missing link light indicates switch failure",
                "correct": False,
                "rationale": (
                    "Incorrect. A single port with no link light on a switch most "
                    "likely indicates a cable or NIC issue, not the switch. A switch "
                    "failure would affect multiple ports. Cable/NIC diagnosis comes "
                    "before switch replacement."
                ),
            },
        ],
        "explanation": (
            "OSI Layer 1 (Physical) must be confirmed before investigating higher layers. "
            "No switch port link light + APIPA address = no physical layer connectivity. "
            "Check cable insertion, try a known-good cable, and verify the NIC is "
            "enabled in Device Manager. Only after the link light is confirmed active "
            "should you investigate DHCP or IP configuration."
        ),
    },
    {
        "id": "a1d5v3-034",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician is troubleshooting intermittent packet loss between a "
            "Windows workstation and a server at 10.10.5.50. Which TWO commands "
            "provide the MOST useful data about packet loss and per-hop latency? "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ping 10.10.5.50 -n 100",
                "correct": True,
                "rationale": (
                    "Correct. Running ping with a large packet count (-n 100 on Windows) "
                    "sends 100 ICMP echo requests and reports the number of packets lost "
                    "as a percentage, along with min/max/average RTT. This quantifies "
                    "end-to-end packet loss."
                ),
            },
            {
                "id": "b",
                "text": "tracert 10.10.5.50",
                "correct": True,
                "rationale": (
                    "Correct. tracert shows each hop along the path and the RTT to each "
                    "router. Hops with asterisks (*) indicate dropped ICMP TTL-exceeded "
                    "replies. A hop where latency suddenly spikes or drops begin "
                    "localizes the packet loss to that segment."
                ),
            },
            {
                "id": "c",
                "text": "arp -a",
                "correct": False,
                "rationale": (
                    "Incorrect. arp -a displays the local ARP cache (IP to MAC mappings). "
                    "It provides no information about packet loss or per-hop latency "
                    "along the path to a remote host."
                ),
            },
            {
                "id": "d",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /all displays the local adapter IP configuration. "
                    "It does not measure packet loss or test connectivity to any remote "
                    "host."
                ),
            },
        ],
        "explanation": (
            "For packet loss investigation: ping -n 100 sends multiple packets and "
            "reports a loss percentage — essential for quantifying intermittent loss. "
            "tracert identifies which hop introduces latency or drops packets — asterisks "
            "at intermediate hops may indicate that router blocks ICMP TTL-exceeded, "
            "but asterisks at the final hop with packet loss in ping confirms the "
            "problem location. Use pathping (Windows) for combined path + loss statistics."
        ),
    },
    {
        "id": "a1d5v3-035",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A corporate wireless network uses WPA2-Enterprise with 802.1X authentication. "
            "A new employee's laptop cannot connect to the SSID; it prompts for "
            "credentials but fails with 'Authentication failed' after entering valid "
            "domain credentials. Other employees connect without issue. Which TWO "
            "causes should the technician investigate FIRST? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The laptop's wireless profile is missing or has an incorrect EAP type configured (e.g., PEAP vs. EAP-TLS)",
                "correct": True,
                "rationale": (
                    "Correct. WPA2-Enterprise uses EAP (Extensible Authentication "
                    "Protocol) methods such as PEAP, EAP-TLS, or EAP-TTLS. If the "
                    "client profile specifies the wrong EAP method, authentication will "
                    "fail even with correct credentials. A new employee's laptop likely "
                    "needs the correct wireless profile pushed via GPO or manually "
                    "configured."
                ),
            },
            {
                "id": "b",
                "text": "The RADIUS server does not have the user account in its allowed authentication policy or the user has not been added to the correct security group",
                "correct": True,
                "rationale": (
                    "Correct. WPA2-Enterprise authenticates through a RADIUS server "
                    "(e.g., Microsoft NPS). If the new employee's account is not in the "
                    "security group that the RADIUS network policy authorizes for wireless "
                    "access, authentication will be rejected even with correct credentials."
                ),
            },
            {
                "id": "c",
                "text": "The access point is broadcasting on a channel not supported by the laptop's wireless adapter",
                "correct": False,
                "rationale": (
                    "Incorrect. An unsupported channel would prevent the laptop from "
                    "associating with the SSID at all — it would not reach the credential "
                    "prompt stage. The credential prompt confirms layer 2 association "
                    "succeeded; the failure is at the authentication layer."
                ),
            },
            {
                "id": "d",
                "text": "The WPA2 pre-shared key needs to be updated on the laptop",
                "correct": False,
                "rationale": (
                    "Incorrect. WPA2-Enterprise uses 802.1X authentication (no PSK). "
                    "Pre-shared keys are a WPA2-Personal feature. The credential prompt "
                    "confirms this is an Enterprise network; PSK is not relevant."
                ),
            },
        ],
        "explanation": (
            "WPA2-Enterprise (802.1X) authentication failures despite correct "
            "credentials have two primary causes: (1) Incorrect EAP method in the "
            "client wireless profile — the profile must specify the same EAP type "
            "(PEAP, EAP-TLS, etc.) as the RADIUS server requires; (2) RADIUS policy "
            "exclusion — the user must be in the authorized group in the Network Policy "
            "Server (NPS) or FreeRADIUS policy. Check NPS event logs for the specific "
            "rejection reason."
        ),
    },
    # ── Additional Hard / Expert Questions ────────────────────────────────────
    {
        "id": "a1d5v3-036",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A technician uses a multimeter to test a desktop PSU's +5 V rail and "
            "measures 4.6 V under load. The ATX specification allows ±5% tolerance. "
            "What should the technician conclude?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The PSU is out of specification; 4.75 V is the minimum acceptable +5 V rail value and 4.6 V indicates PSU failure",
                "correct": True,
                "rationale": (
                    "Correct. ATX +5 V rail tolerance is ±5%: acceptable range is "
                    "4.75 V – 5.25 V. A reading of 4.6 V is below the 4.75 V minimum, "
                    "meaning the PSU is outside specification and should be replaced. "
                    "Components powered by the +5 V rail (storage controllers, USB, "
                    "logic chips) may behave erratically or fail."
                ),
            },
            {
                "id": "b",
                "text": "The PSU is within specification; ±5% of 5 V allows down to 4.5 V",
                "correct": False,
                "rationale": (
                    "Incorrect. 5% of 5 V = 0.25 V, so the minimum is 4.75 V, not 4.5 V. "
                    "4.6 V is below the 4.75 V floor and is out of ATX specification."
                ),
            },
            {
                "id": "c",
                "text": "The reading is normal; voltage sag under load is expected and 4.6 V is acceptable",
                "correct": False,
                "rationale": (
                    "Incorrect. The ATX specification already accounts for load conditions. "
                    "A reading below 4.75 V at any tested load point means the PSU "
                    "is failing to maintain spec."
                ),
            },
            {
                "id": "d",
                "text": "The multimeter is the likely fault; replace the measurement tool before condemning the PSU",
                "correct": False,
                "rationale": (
                    "Incorrect. While meter calibration can be questioned, a reading "
                    "0.4 V below the expected value (8% low) is far beyond typical meter "
                    "inaccuracy on a digital multimeter. The PSU reading is the valid "
                    "finding."
                ),
            },
        ],
        "explanation": (
            "ATX PSU voltage tolerances (±5%): +12 V: 11.4–12.6 V; +5 V: 4.75–5.25 V; "
            "+3.3 V: 3.135–3.465 V. These tolerances are measured under load. A +5 V "
            "reading of 4.6 V is 8% below nominal — well outside the 5% tolerance. "
            "The PSU must be replaced. Components powered by the +5 V rail include "
            "drive logic, USB ports, and low-voltage motherboard components."
        ),
    },
    {
        "id": "a1d5v3-037",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A storage administrator is told that the company's RAID 10 array of eight "
            "drives has lost two drives. After reviewing the controller logs, they find "
            "the two failed drives are from the same mirrored pair (e.g., Disk 1 "
            "and its mirror Disk 2). What is the result?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data loss — both copies of that mirror pair are gone and the entire RAID 10 array is offline",
                "correct": True,
                "rationale": (
                    "Correct. RAID 10 (mirrored stripes) can survive multiple drive "
                    "failures as long as no mirrored pair loses both of its drives. "
                    "If both drives in any single mirror pair fail simultaneously, "
                    "the data on that stripe is unrecoverable, and the entire array "
                    "goes offline."
                ),
            },
            {
                "id": "b",
                "text": "The array continues in degraded mode because RAID 10 always tolerates two drive failures",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 10 can tolerate two failures only if they are from "
                    "different mirror pairs. Losing both drives of the same pair "
                    "eliminates that stripe's data entirely — no parity exists to "
                    "reconstruct it."
                ),
            },
            {
                "id": "c",
                "text": "RAID 10 uses parity to reconstruct the lost mirror pair from the remaining six drives",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 10 uses no parity — it uses mirroring (RAID 1) "
                    "and striping (RAID 0). Without parity, lost data from a fully "
                    "failed mirror pair cannot be mathematically reconstructed."
                ),
            },
            {
                "id": "d",
                "text": "The remaining three mirror pairs can vote on the missing data through a consensus algorithm",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID does not use voting or consensus algorithms. "
                    "Only distributed parity systems (RAID 5/6) have a mathematical "
                    "reconstruction mechanism. RAID 10 has no such fallback for a "
                    "fully lost mirror pair."
                ),
            },
        ],
        "explanation": (
            "RAID 10 fault tolerance: it can sustain multiple drive failures across "
            "different mirror pairs (e.g., in an 8-drive RAID 10, it could survive "
            "up to 4 failures — one from each pair). However, if both drives in any "
            "single mirror pair fail, that stripe is gone and the array fails. "
            "This is why RAID 10 risk analysis considers 'which pair fails' not just "
            "'how many drives fail.' Restore from backup."
        ),
    },
    {
        "id": "a1d5v3-038",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A user running dual monitors notices that the second monitor flickers "
            "randomly every few minutes, while the primary monitor is always stable. "
            "Swapping cables between the two monitors causes the flickering to follow "
            "the cable, not the monitor. What should the technician do NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace the display cable connected to the second monitor port",
                "correct": True,
                "rationale": (
                    "Correct. When a symptom follows the cable rather than the monitor, "
                    "the cable is definitively identified as the faulty component. "
                    "Replacing the cable is the correct and immediate next action."
                ),
            },
            {
                "id": "b",
                "text": "Replace the second monitor because the flicker indicates its internal electronics are failing",
                "correct": False,
                "rationale": (
                    "Incorrect. The swap test proved the monitor is not the fault — "
                    "when the cable was moved to the other monitor, it flickered, but "
                    "the original monitor on the good cable became stable. The monitor "
                    "is functioning correctly."
                ),
            },
            {
                "id": "c",
                "text": "Update the GPU driver to resolve timing conflicts between the two display outputs",
                "correct": False,
                "rationale": (
                    "Incorrect. A GPU driver issue would typically affect both outputs "
                    "or change behavior when drivers are updated. The cable swap test "
                    "has isolated the cause to the physical cable — no driver update is "
                    "needed."
                ),
            },
            {
                "id": "d",
                "text": "Replace the GPU because it cannot maintain a stable signal on the second port",
                "correct": False,
                "rationale": (
                    "Incorrect. If the GPU port were the fault, swapping cables would "
                    "make the same port always flicker regardless of which cable was "
                    "used. The symptom followed the cable, not the port, confirming "
                    "the cable is defective."
                ),
            },
        ],
        "explanation": (
            "When troubleshooting intermittent display issues with multiple monitors, "
            "the swap test is the definitive isolation technique. If swapping cables "
            "causes the symptom to move with the cable — the cable is the cause. If "
            "the symptom stays on the same display — the display is the cause. If the "
            "symptom stays on the same GPU port — the GPU/port is the cause. This "
            "systematic approach eliminates variables one at a time."
        ),
    },
    {
        "id": "a1d5v3-039",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "An inkjet printer produces output that looks correct on screen but when "
            "printed, all colors are shifted — what should be cyan appears in the "
            "wrong location relative to magenta and yellow content, creating a "
            "rainbow fringe around every colored object. What is this defect called "
            "and what is the correct fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Color registration misalignment; run the printer's print head alignment utility",
                "correct": True,
                "rationale": (
                    "Correct. Color registration misalignment occurs when the individual "
                    "color channels (CMYK) print at slightly offset positions. The result "
                    "is color fringing or halo effects around objects. The print head "
                    "alignment utility adjusts the relative firing positions of each "
                    "color nozzle row to bring them into registration."
                ),
            },
            {
                "id": "b",
                "text": "Ink bleeding caused by incompatible paper; switch to inkjet-rated paper",
                "correct": False,
                "rationale": (
                    "Incorrect. Ink bleeding (ink spreading into paper fibers) produces "
                    "fuzzy edges uniformly across the print — not a specific directional "
                    "offset between color channels. The described rainbow fringe is "
                    "characteristic of registration misalignment."
                ),
            },
            {
                "id": "c",
                "text": "A failed magenta cartridge printing at double intensity; replace the magenta cartridge",
                "correct": False,
                "rationale": (
                    "Incorrect. A failed cartridge would produce absence or excessive "
                    "quantity of one color uniformly — not a spatial offset between "
                    "channels. The fringe description indicates a positional, not "
                    "quantitative, issue."
                ),
            },
            {
                "id": "d",
                "text": "ICC color profile mismatch between the OS and the printer; recalibrate the color profile",
                "correct": False,
                "rationale": (
                    "Incorrect. An ICC profile mismatch produces overall color "
                    "inaccuracy (wrong hues, saturation) but not a physical spatial "
                    "offset between CMYK channels that creates fringing."
                ),
            },
        ],
        "explanation": (
            "Print head alignment (also called print head registration) corrects the "
            "spatial offset between color ink channels in an inkjet printer. Over time "
            "or after cartridge replacement, the nozzle rows for C, M, Y, and K can "
            "drift slightly relative to each other. The alignment utility prints a "
            "test pattern and either automatically or manually adjusts the bi-directional "
            "and inter-channel firing offsets to bring all colors into precise alignment."
        ),
    },
    {
        "id": "a1d5v3-040",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician types 'netstat -r' on a Windows workstation and observes "
            "that the default gateway entry (0.0.0.0 with network mask 0.0.0.0) is "
            "completely absent from the routing table. The workstation has a valid "
            "IP address and subnet mask. What will be the effect on this workstation's "
            "connectivity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The workstation can communicate with devices on its local subnet but cannot reach any remote networks or the internet",
                "correct": True,
                "rationale": (
                    "Correct. The default gateway entry (0.0.0.0/0.0.0.0) is the route "
                    "of last resort used for all traffic destined for non-local networks. "
                    "Without it, the workstation has no route for packets to any network "
                    "outside its own subnet, so internet and cross-subnet access fail. "
                    "Local subnet communication still works because the directly-connected "
                    "route is present."
                ),
            },
            {
                "id": "b",
                "text": "The workstation cannot communicate with any device, including those on the local subnet",
                "correct": False,
                "rationale": (
                    "Incorrect. A missing default route only prevents routing beyond "
                    "the local subnet. Directly connected hosts on the same subnet can "
                    "still be reached via the directly-connected route entry, which "
                    "is derived from the IP address and subnet mask."
                ),
            },
            {
                "id": "c",
                "text": "The workstation will automatically use the subnet broadcast address as a fallback gateway",
                "correct": False,
                "rationale": (
                    "Incorrect. There is no automatic fallback gateway mechanism. Without "
                    "a default route, non-local traffic is simply dropped (ICMP "
                    "'Destination Host Unreachable' is returned)."
                ),
            },
            {
                "id": "d",
                "text": "The workstation will use its DNS server address as an alternate path for internet traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS resolves names to IP addresses — it has no routing "
                    "function. Without a default gateway route, traffic cannot be forwarded "
                    "beyond the local subnet regardless of DNS configuration."
                ),
            },
        ],
        "explanation": (
            "The routing table entry 0.0.0.0 / 0.0.0.0 (default route) tells the "
            "workstation where to send packets that do not match any more specific "
            "route. It is normally set to the default gateway IP. Without this entry, "
            "the workstation can only reach hosts on its directly connected subnet. "
            "Fix: 'route add 0.0.0.0 mask 0.0.0.0 <gateway_IP>' or reconfigure the "
            "network adapter settings to include the correct default gateway."
        ),
    },
    {
        "id": "a1d5v3-041",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network troubleshooting",
        "stem": (
            "Two workstations on the same subnet intermittently lose connectivity to "
            "each other and to the default gateway. Network logs reveal duplicate IP "
            "address warnings for 192.168.1.50. One workstation has a static IP of "
            "192.168.1.50; a new network printer was recently added. What is the MOST "
            "likely cause and solution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The DHCP server assigned 192.168.1.50 to the new printer, creating an IP address conflict; exclude 192.168.1.50 from the DHCP scope or assign the printer a static IP outside the DHCP range",
                "correct": True,
                "rationale": (
                    "Correct. An IP address conflict occurs when two devices are "
                    "configured with the same IP. The DHCP server included 192.168.1.50 "
                    "in its pool, and it was assigned to the new printer. The solution "
                    "is to either exclude 192.168.1.50 from the DHCP scope, or assign "
                    "the printer a static IP address in a range that is excluded from "
                    "DHCP allocation."
                ),
            },
            {
                "id": "b",
                "text": "The printer is generating a broadcast storm that is overwhelming the switch's MAC table",
                "correct": False,
                "rationale": (
                    "Incorrect. A broadcast storm would cause network-wide saturation "
                    "affecting all devices on the segment — not selective, intermittent "
                    "connectivity loss specifically correlated with duplicate IP warnings "
                    "for a single address."
                ),
            },
            {
                "id": "c",
                "text": "The switch port for the workstation has a spanning tree loop causing ARP thrashing",
                "correct": False,
                "rationale": (
                    "Incorrect. An STP loop would cause widespread connectivity issues "
                    "and would appear in switch logs as topology changes or high CPU "
                    "utilization — not duplicate IP address events."
                ),
            },
            {
                "id": "d",
                "text": "The workstation's static IP is incorrect for the subnet and must be reconfigured",
                "correct": False,
                "rationale": (
                    "Incorrect. The workstation was working before the printer was added. "
                    "The correlation between adding the printer and the conflict appearing "
                    "identifies the printer (and its DHCP-assigned address) as the new "
                    "variable. The static IP on the workstation is not the problem."
                ),
            },
        ],
        "explanation": (
            "IP address conflicts arise when two devices share the same IP. Static IPs "
            "that fall within the DHCP scope are a common source of conflicts — the "
            "DHCP server does not know a device has claimed that address statically. "
            "Best practices: reserve a static IP block outside the DHCP pool (e.g., "
            "DHCP scope 192.168.1.100–200; static IPs use 192.168.1.1–99), or use DHCP "
            "reservations (fixed MAC-to-IP assignments within the DHCP server) for "
            "devices that need consistent addresses."
        ),
    },
]
