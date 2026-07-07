"""
CompTIA A+ Core 1 (220-1201) — Domain 5: Hardware and Network Troubleshooting
46 practice questions at hard/expert difficulty.
"""

QUESTIONS = [
    # ── 5.1 Troubleshooting Methodology ──────────────────────────────────────
    {
        "id": "a1d5-001",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician has gathered information, questioned the user, and confirmed "
            "that a recent driver update preceded the issue. They now suspect the new "
            "driver is the cause. According to the CompTIA best-practice troubleshooting "
            "methodology, what is the correct NEXT step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Test the theory to determine the cause (e.g., roll back the driver)",
                "correct": True,
                "rationale": (
                    "Correct. After establishing a theory of probable cause, the next step "
                    "is to test the theory to confirm or refute it before committing to a "
                    "full repair plan."
                ),
            },
            {
                "id": "b",
                "text": "Document the findings, actions, and outcomes",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation is the final step, performed only after the "
                    "problem is resolved and full functionality has been verified."
                ),
            },
            {
                "id": "c",
                "text": "Establish a plan of action to resolve the problem",
                "correct": False,
                "rationale": (
                    "Incorrect. A plan of action is created only after the theory has been "
                    "tested and confirmed; forming a plan before testing the theory skips "
                    "a required verification step."
                ),
            },
            {
                "id": "d",
                "text": "Verify full system functionality",
                "correct": False,
                "rationale": (
                    "Incorrect. Verifying full functionality comes after a fix has been "
                    "implemented, not immediately after forming a theory."
                ),
            },
        ],
        "explanation": (
            "The six-step CompTIA methodology: 1) Identify the problem, 2) Establish a "
            "theory of probable cause, 3) Test the theory, 4) Establish a plan of action "
            "and implement, 5) Verify full functionality and add preventive measures, "
            "6) Document findings, actions, and outcomes. After forming a theory you MUST "
            "test it before planning a fix."
        ),
    },
    {
        "id": "a1d5-002",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician fixes a failed network card, confirms the user can reach the "
            "internet, and then asks whether any other issues exist. The user says "
            "everything is fine. What should the technician do NEXT before closing the "
            "ticket?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Document findings, actions taken, and outcomes",
                "correct": True,
                "rationale": (
                    "Correct. After verifying full system functionality (which includes "
                    "asking the user if everything is fine), the final step is to document "
                    "the problem, steps taken, and resolution for future reference."
                ),
            },
            {
                "id": "b",
                "text": "Establish a new theory of probable cause",
                "correct": False,
                "rationale": (
                    "Incorrect. A new theory is only warranted if the initial theory was "
                    "wrong and testing disproved it. The user has confirmed the issue is "
                    "resolved."
                ),
            },
            {
                "id": "c",
                "text": "Implement preventive measures before documenting",
                "correct": False,
                "rationale": (
                    "Incorrect. Preventive measures are part of step 5 (verify full "
                    "functionality), which has already been completed. Documentation "
                    "remains the last action before closing the ticket."
                ),
            },
            {
                "id": "d",
                "text": "Escalate the ticket to a higher-tier technician",
                "correct": False,
                "rationale": (
                    "Incorrect. Escalation is only appropriate when the technician cannot "
                    "resolve the issue. The problem is already resolved."
                ),
            },
        ],
        "explanation": (
            "Step 6 of the CompTIA methodology is to document findings, actions, and "
            "outcomes. This happens after step 5 (verify full system functionality and "
            "implement preventive measures). Documentation ensures the knowledge is "
            "available for future reference and auditing."
        ),
    },
    {
        "id": "a1d5-003",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician tests a theory that a bad patch cable is causing intermittent "
            "connectivity by swapping it with a known-good cable — the problem persists. "
            "According to the CompTIA troubleshooting methodology, what should the "
            "technician do NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Re-establish a new theory or escalate if unable to determine the cause",
                "correct": True,
                "rationale": (
                    "Correct. When a tested theory is disproved, the methodology directs "
                    "the technician to establish a new theory of probable cause or escalate "
                    "if they cannot determine the cause on their own."
                ),
            },
            {
                "id": "b",
                "text": "Establish a plan of action based on the original theory and implement it",
                "correct": False,
                "rationale": (
                    "Incorrect. Since testing disproved the original theory, proceeding "
                    "with a plan based on that theory would be incorrect and waste time "
                    "without fixing the real issue."
                ),
            },
            {
                "id": "c",
                "text": "Document the findings and close the ticket",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation is the final step after a problem is fully "
                    "resolved. The problem has not been resolved."
                ),
            },
            {
                "id": "d",
                "text": "Verify full system functionality to confirm the repair",
                "correct": False,
                "rationale": (
                    "Incorrect. There is nothing to verify — the fix has not been applied "
                    "because the theory was disproved. A new theory must be formed first."
                ),
            },
        ],
        "explanation": (
            "When testing disproves a theory, the CompTIA methodology loops back to "
            "step 2: establish a new theory of probable cause (or escalate if unable). "
            "You do not move forward to planning or verification until a theory is "
            "confirmed."
        ),
    },
    {
        "id": "a1d5-004",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "During step 1 of the CompTIA troubleshooting methodology (identify the "
            "problem), which action is MOST important before attempting a fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Question the user about recent changes to the environment",
                "correct": True,
                "rationale": (
                    "Correct. Inquiring about recent changes (software installs, hardware "
                    "moves, configuration updates) is a critical part of identifying the "
                    "problem because changes immediately preceding the symptom are the "
                    "most likely cause."
                ),
            },
            {
                "id": "b",
                "text": "Replace components one at a time starting with the least expensive",
                "correct": False,
                "rationale": (
                    "Incorrect. Component replacement is part of establishing and testing "
                    "a theory, not the identification step. Replacing parts without "
                    "identifying the problem first is wasteful."
                ),
            },
            {
                "id": "c",
                "text": "Implement an immediate fix to restore productivity",
                "correct": False,
                "rationale": (
                    "Incorrect. Implementing a fix before identifying the problem violates "
                    "the methodology and may mask the root cause or cause additional damage."
                ),
            },
            {
                "id": "d",
                "text": "Verify full system functionality before gathering data",
                "correct": False,
                "rationale": (
                    "Incorrect. Verifying functionality is step 5, performed after the "
                    "fix is implemented. Gathering information comes first."
                ),
            },
        ],
        "explanation": (
            "Step 1 (Identify the problem) includes gathering information, duplicating "
            "the problem if possible, questioning users about symptoms, and — critically "
            "— inquiring about recent changes to hardware, software, or the environment. "
            "Changes immediately preceding the symptom are frequently the root cause."
        ),
    },
    # ── 5.2 Motherboards, RAM, CPUs, Power ───────────────────────────────────
    {
        "id": "a1d5-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A desktop PC powers on (fans spin, LEDs light), but the display remains "
            "completely black and there is no POST. You have already verified the monitor "
            "works on another computer. Which component is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A faulty or improperly seated RAM module",
                "correct": True,
                "rationale": (
                    "Correct. RAM issues (failed, removed, or improperly seated DIMMs) "
                    "are a leading cause of no-POST/black-screen. The CPU cannot proceed "
                    "past the memory check, so nothing appears on-screen."
                ),
            },
            {
                "id": "b",
                "text": "A failed hard drive",
                "correct": False,
                "rationale": (
                    "Incorrect. A failed hard drive will typically allow POST to complete "
                    "and the system will reach a 'bootable device not found' error rather "
                    "than a completely black screen before POST."
                ),
            },
            {
                "id": "c",
                "text": "An expired CMOS battery",
                "correct": False,
                "rationale": (
                    "Incorrect. A dead CMOS battery causes incorrect date/time settings "
                    "and may produce a CMOS checksum error, but the system usually still "
                    "POSTs and displays a message."
                ),
            },
            {
                "id": "d",
                "text": "A failed optical drive",
                "correct": False,
                "rationale": (
                    "Incorrect. A failed optical drive has no effect on POST and would "
                    "not cause a black screen before the OS loads."
                ),
            },
        ],
        "explanation": (
            "No POST with a blank screen (fans and LEDs active) points to a failure "
            "early in the boot sequence. RAM is tested very early; a missing or bad "
            "DIMM prevents POST from completing. Swap or reseat RAM first. A bad GPU "
            "could also cause this, but RAM is statistically more common."
        ),
    },
    {
        "id": "a1d5-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A workstation randomly shuts down after 30–45 minutes of use. The shutdowns "
            "never occur during the first few minutes of operation. Which is the MOST "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CPU overheating due to a clogged or failed heat sink/fan",
                "correct": True,
                "rationale": (
                    "Correct. Thermal-shutdown is the hallmark of overheating: the system "
                    "runs fine when cool, then shuts off abruptly once it reaches a "
                    "thermal protection threshold, typically after tens of minutes of "
                    "sustained load."
                ),
            },
            {
                "id": "b",
                "text": "Faulty RAM causing data corruption",
                "correct": False,
                "rationale": (
                    "Incorrect. Bad RAM typically produces BSODs, application crashes, or "
                    "file corruption rather than the clean, time-delayed abrupt shutdowns "
                    "characteristic of overheating."
                ),
            },
            {
                "id": "c",
                "text": "A failing power supply with inadequate wattage",
                "correct": False,
                "rationale": (
                    "Incorrect. While a failing PSU can cause shutdowns, it usually does "
                    "so under sudden heavy load (not after a consistent warm-up period) "
                    "or produces other symptoms like instability at POST. Overheating is "
                    "more precisely time-delayed."
                ),
            },
            {
                "id": "d",
                "text": "A corrupt operating system file",
                "correct": False,
                "rationale": (
                    "Incorrect. OS corruption causes boot failures, BSODs, or application "
                    "errors — not clean, heat-correlated abrupt power-offs."
                ),
            },
        ],
        "explanation": (
            "When a system shuts down cleanly only after a warm-up period (30–45 min), "
            "overheating is the classic culprit. CPUs and GPUs include thermal protection "
            "that triggers an immediate shutdown when a threshold is exceeded. Check and "
            "clean the heat sink, verify fan operation, and re-apply thermal paste if "
            "needed."
        ),
    },
    {
        "id": "a1d5-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A user reports that every morning their PC shows the wrong date and time and "
            "they must re-enter them manually. The OS and BIOS settings appear correct "
            "otherwise. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The CMOS battery on the motherboard needs to be replaced",
                "correct": True,
                "rationale": (
                    "Correct. The CMOS battery (typically a CR2032 lithium coin cell) "
                    "maintains the real-time clock and BIOS settings when AC power is "
                    "removed. When it fails, date/time resets to the default (usually "
                    "Jan 1, 2000 or a similar epoch) every time the system is "
                    "unplugged or power is lost."
                ),
            },
            {
                "id": "b",
                "text": "The Windows Time service is disabled",
                "correct": False,
                "rationale": (
                    "Incorrect. A disabled Windows Time service would prevent NTP "
                    "synchronization but would not cause the clock to reset to an "
                    "entirely incorrect date every time the machine is powered on."
                ),
            },
            {
                "id": "c",
                "text": "The hard drive firmware is corrupted",
                "correct": False,
                "rationale": (
                    "Incorrect. Hard drive firmware does not control the real-time clock "
                    "or CMOS settings; it would cause storage errors, not clock resets."
                ),
            },
            {
                "id": "d",
                "text": "The CPU is overclocked and causing RTC drift",
                "correct": False,
                "rationale": (
                    "Incorrect. Overclocking can cause instability or BSODs but does not "
                    "cause the date/time to reset entirely to an epoch value every morning."
                ),
            },
        ],
        "explanation": (
            "The CMOS battery powers the real-time clock (RTC) and non-volatile BIOS "
            "settings while the machine is unplugged. When this CR2032-type cell dies "
            "(typically after 3–7 years), the clock loses its value whenever AC power "
            "is removed, presenting as a reset date/time each morning. Replace the coin "
            "cell battery on the motherboard."
        ),
    },
    {
        "id": "a1d5-008",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A PC emits a series of beep codes on startup and does not POST. The "
            "technician counts one long beep followed by three short beeps. On an AMI "
            "BIOS system, this pattern typically indicates a failure of which component?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Video (GPU/display adapter)",
                "correct": True,
                "rationale": (
                    "Correct. On AMI BIOS, 1 long + 3 short beeps is the standard code "
                    "for a video card/GPU failure or no video memory detected. The system "
                    "cannot initialize the display subsystem."
                ),
            },
            {
                "id": "b",
                "text": "RAM failure",
                "correct": False,
                "rationale": (
                    "Incorrect. AMI BIOS RAM errors are typically indicated by 2 short "
                    "beeps (parity error) or 3 short beeps (base memory read/write "
                    "failure), not 1 long + 3 short."
                ),
            },
            {
                "id": "c",
                "text": "CPU failure",
                "correct": False,
                "rationale": (
                    "Incorrect. A CPU failure usually produces a continuous beep or no "
                    "beep at all (no POST whatsoever). One long + three short is the "
                    "video error code on AMI systems."
                ),
            },
            {
                "id": "d",
                "text": "Keyboard controller failure",
                "correct": False,
                "rationale": (
                    "Incorrect. Keyboard controller failure produces a different beep "
                    "sequence on AMI BIOS (commonly 1 long + 2 short or other patterns "
                    "depending on BIOS version)."
                ),
            },
        ],
        "explanation": (
            "POST beep codes vary by BIOS manufacturer. On AMI BIOS, 1 long + 3 short "
            "beeps signals a video adapter or GPU problem. On Award BIOS, 1 long + 2 "
            "short is the video error. Always consult the motherboard manual for the "
            "specific code table, but for the A+ exam, AMI 1-long-3-short = video "
            "failure is a tested fact."
        ),
    },
    {
        "id": "a1d5-009",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A technician notices a strong burning smell coming from a desktop computer "
            "and observes that several capacitors on the motherboard are bulging at the "
            "top. What is the BEST course of action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Power down immediately and replace the motherboard",
                "correct": True,
                "rationale": (
                    "Correct. Bulging capacitors indicate electrolytic capacitor failure "
                    "and are a fire and explosion hazard. The system must be powered "
                    "off immediately and the motherboard replaced — capacitors cannot "
                    "be safely ignored."
                ),
            },
            {
                "id": "b",
                "text": "Replace the power supply and continue using the motherboard",
                "correct": False,
                "rationale": (
                    "Incorrect. The bulging capacitors are on the motherboard itself. "
                    "Replacing the PSU does not address the failed components on the "
                    "board; continued use risks fire or further damage."
                ),
            },
            {
                "id": "c",
                "text": "Increase case airflow to cool the capacitors and monitor the system",
                "correct": False,
                "rationale": (
                    "Incorrect. Bulging capacitors have already failed internally; "
                    "cooling will not repair them. Continued operation is unsafe."
                ),
            },
            {
                "id": "d",
                "text": "Re-flash the BIOS firmware to restore capacitor function",
                "correct": False,
                "rationale": (
                    "Incorrect. Capacitor swelling is a physical hardware failure. BIOS "
                    "firmware has no influence over physical capacitor condition."
                ),
            },
        ],
        "explanation": (
            "Bulging or leaking electrolytic capacitors are a serious physical failure "
            "symptom indicating the capacitor's electrolyte has vaporized or leaked. "
            "The top of the capacitor should be flat; any dome-shape means failure. "
            "These can rupture, leak corrosive electrolyte, or cause fire. The "
            "motherboard must be replaced."
        ),
    },
    {
        "id": "a1d5-010",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A Windows workstation frequently produces a Blue Screen of Death (BSOD) "
            "with memory-related stop codes (e.g., MEMORY_MANAGEMENT, PAGE_FAULT_IN_"
            "NONPAGED_AREA). The errors occur randomly across multiple applications. "
            "Which diagnostic tool should the technician run FIRST to confirm the cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Windows Memory Diagnostic (mdsched.exe) to test the RAM",
                "correct": True,
                "rationale": (
                    "Correct. Memory-related BSODs across multiple applications are a "
                    "classic sign of faulty RAM. Windows Memory Diagnostic (mdsched.exe) "
                    "performs a thorough RAM test during the next reboot and is the "
                    "appropriate first tool."
                ),
            },
            {
                "id": "b",
                "text": "chkdsk /r to scan the hard drive for file system errors",
                "correct": False,
                "rationale": (
                    "Incorrect. chkdsk /r tests the disk for bad sectors. While disk "
                    "errors can cause BSODs, the specific stop codes listed "
                    "(MEMORY_MANAGEMENT, PAGE_FAULT_IN_NONPAGED_AREA) point to RAM, "
                    "not disk."
                ),
            },
            {
                "id": "c",
                "text": "Device Manager to check for driver conflicts",
                "correct": False,
                "rationale": (
                    "Incorrect. Driver conflicts can cause BSODs, but would typically "
                    "show a specific driver-related stop code. Generic memory stop codes "
                    "are more consistent with physical RAM errors."
                ),
            },
            {
                "id": "d",
                "text": "CPU-Z to review overclocking settings",
                "correct": False,
                "rationale": (
                    "Incorrect. While overclocking can cause instability, reviewing CPU-Z "
                    "is a secondary step. The immediate diagnostic for memory-specific "
                    "BSODs is a RAM test."
                ),
            },
        ],
        "explanation": (
            "When BSODs consistently reference memory stop codes, the first step is to "
            "test the physical RAM. Windows Memory Diagnostic (mdsched.exe) is built-in "
            "and tests RAM at the next reboot. Memtest86+ is an alternative that runs "
            "from bootable media. If RAM passes, investigate drivers and OS integrity."
        ),
    },
    # ── 5.3 Storage Drives and RAID ───────────────────────────────────────────
    {
        "id": "a1d5-011",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A hard drive begins making a repetitive clicking sound during operation "
            "and the OS reports read errors. What is the MOST likely cause and the "
            "BEST immediate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The drive's read/write heads are failing; back up data immediately and replace the drive",
                "correct": True,
                "rationale": (
                    "Correct. A repetitive clicking or clunking from a hard drive — "
                    "often called the 'click of death' — indicates that the read/write "
                    "heads are repeatedly resetting or failing to find the track. This "
                    "is a sign of imminent drive failure; data must be backed up at once "
                    "and the drive replaced."
                ),
            },
            {
                "id": "b",
                "text": "The drive cable is loose; reseat the SATA cable and the noise will stop",
                "correct": False,
                "rationale": (
                    "Incorrect. A loose cable causes connectivity errors or the drive not "
                    "being detected, not a rhythmic clicking sound from inside the drive "
                    "mechanism itself."
                ),
            },
            {
                "id": "c",
                "text": "The drive needs to be defragmented to resolve head thrashing",
                "correct": False,
                "rationale": (
                    "Incorrect. Defragmentation addresses file fragmentation to reduce "
                    "seek times; it does not fix physical head failures and could "
                    "actually cause further damage by subjecting a failing drive to "
                    "heavy workload."
                ),
            },
            {
                "id": "d",
                "text": "The drive's firmware needs to be updated to correct head positioning",
                "correct": False,
                "rationale": (
                    "Incorrect. A firmware update cannot repair physically failing heads. "
                    "The clicking indicates a mechanical failure that firmware cannot "
                    "address."
                ),
            },
        ],
        "explanation": (
            "The 'click of death' is one of the most serious drive symptoms: the "
            "read/write heads are mechanically failing and repeatedly recalibrating. "
            "Immediate data backup is critical; further use of the drive risks total "
            "data loss. Replace the drive after recovering data. S.M.A.R.T. "
            "monitoring may also show reallocated sector count and pending sector "
            "count attributes spiking."
        ),
    },
    {
        "id": "a1d5-012",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "During routine maintenance, a monitoring tool reports a S.M.A.R.T. failure "
            "warning on a server's secondary hard drive. The drive is still operational "
            "and the server is running normally. What should the technician do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Back up all data on the drive immediately and plan for drive replacement",
                "correct": True,
                "rationale": (
                    "Correct. A S.M.A.R.T. (Self-Monitoring, Analysis, and Reporting "
                    "Technology) failure warning means the drive's internal sensors have "
                    "detected parameters that predict imminent failure. The drive may "
                    "still function briefly, so data backup must happen at once before "
                    "the drive fails completely."
                ),
            },
            {
                "id": "b",
                "text": "Ignore the warning — S.M.A.R.T. alerts are often false positives",
                "correct": False,
                "rationale": (
                    "Incorrect. S.M.A.R.T. warnings are a reliable early indicator of "
                    "drive problems. While not every warning ends in immediate failure, "
                    "ignoring them risks data loss and violates best practice."
                ),
            },
            {
                "id": "c",
                "text": "Run chkdsk /r to repair the drive and clear the S.M.A.R.T. flag",
                "correct": False,
                "rationale": (
                    "Incorrect. chkdsk /r can repair file-system errors but cannot clear "
                    "S.M.A.R.T. failure counters or fix the underlying hardware "
                    "deterioration causing the warning."
                ),
            },
            {
                "id": "d",
                "text": "Replace the drive immediately without backing up data first",
                "correct": False,
                "rationale": (
                    "Incorrect. Replacing the drive without first backing up data risks "
                    "losing all data on the drive. The warning provides a window to "
                    "recover data — take advantage of it."
                ),
            },
        ],
        "explanation": (
            "S.M.A.R.T. monitors attributes like reallocated sectors, uncorrectable "
            "errors, spin-up time, and head flying height. A failure warning means "
            "one or more thresholds have been breached. The drive may continue to "
            "function for hours or days — use that window to back up all data, then "
            "replace the drive."
        ),
    },
    {
        "id": "a1d5-013",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A server running RAID 5 with four drives loses two drives simultaneously "
            "due to a power surge. The array goes offline. What is the result, and what "
            "is the correct action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RAID 5 cannot survive the loss of two drives; data is lost — restore from backup",
                "correct": True,
                "rationale": (
                    "Correct. RAID 5 can tolerate only one drive failure. Losing two "
                    "drives simultaneously exceeds its fault tolerance, making the array "
                    "unrecoverable through RAID mechanisms alone. Data must be restored "
                    "from a backup."
                ),
            },
            {
                "id": "b",
                "text": "Replace both drives and the RAID 5 array will rebuild automatically",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 5 uses single-drive parity. With two drives missing, "
                    "there is insufficient parity information to reconstruct the data. "
                    "Replacing the drives will not restore data — the array is failed."
                ),
            },
            {
                "id": "c",
                "text": "Replace one drive; RAID 5 can survive a double failure and rebuild from two-drive parity",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 5 uses single distributed parity and tolerates only "
                    "one drive failure. Double-drive parity is the feature of RAID 6, "
                    "not RAID 5."
                ),
            },
            {
                "id": "d",
                "text": "The array will enter degraded mode and continue operating on the remaining two drives",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 5 can enter degraded mode only when exactly one "
                    "drive fails. Two simultaneous failures take the array completely "
                    "offline with no read capability."
                ),
            },
        ],
        "explanation": (
            "RAID 5 tolerates one drive failure using distributed parity. RAID 6 "
            "tolerates two simultaneous drive failures using dual parity. When two "
            "RAID 5 drives fail, parity data alone is insufficient to reconstruct "
            "both missing drives; the array is lost. This is why RAID is not a "
            "backup — an off-site backup is essential."
        ),
    },
    {
        "id": "a1d5-014",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A user complains that their computer is extremely slow to boot and that "
            "file operations take much longer than normal. The storage device is an "
            "NVMe SSD. S.M.A.R.T. shows a high percentage of the drive's write "
            "endurance consumed. Which condition BEST explains the sluggish performance?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The SSD is near its write endurance limit, causing the controller to slow writes to protect remaining cells",
                "correct": True,
                "rationale": (
                    "Correct. SSDs throttle write speed as NAND flash cells approach "
                    "their rated program/erase (P/E) cycle limit. The controller "
                    "intentionally slows I/O to protect remaining cell life — a behavior "
                    "sometimes called 'drive slowdown near EOL.'"
                ),
            },
            {
                "id": "b",
                "text": "The NVMe slot is operating in PCIe 2.0 x1 mode instead of the expected x4 bandwidth",
                "correct": False,
                "rationale": (
                    "Incorrect. While a bandwidth downgrade would reduce throughput, it "
                    "would not correlate with S.M.A.R.T. endurance data. The S.M.A.R.T "
                    "reading directly points to endurance as the cause."
                ),
            },
            {
                "id": "c",
                "text": "The TRIM command is disabled, causing write amplification",
                "correct": False,
                "rationale": (
                    "Incorrect. Disabled TRIM can degrade performance over time but "
                    "would not cause the specific S.M.A.R.T. endurance threshold "
                    "reading described. The endurance exhaustion is the direct indicator."
                ),
            },
            {
                "id": "d",
                "text": "Defragmentation is required to reduce SSD read latency",
                "correct": False,
                "rationale": (
                    "Incorrect. SSDs are random-access devices and do not benefit from "
                    "defragmentation; in fact, defragmenting an SSD wastes P/E cycles "
                    "and further degrades endurance."
                ),
            },
        ],
        "explanation": (
            "S.M.A.R.T. attributes on SSDs include 'Media Wearout Indicator' or "
            "'Percentage Used.' As NAND flash cells reach their rated P/E cycle limit, "
            "many controllers enter a 'read-only' or 'slowed write' state to prevent "
            "data corruption. High endurance consumption + slow performance = drive "
            "nearing end-of-life; plan replacement."
        ),
    },
    {
        "id": "a1d5-015",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "After installing a new SATA SSD as a secondary drive, a technician finds "
            "the drive is not visible in Windows Explorer but does appear in Device "
            "Manager. What is the MOST likely reason and the correct fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The drive has not been initialized or partitioned; use Disk Management to initialize and create a volume",
                "correct": True,
                "rationale": (
                    "Correct. A new drive that appears in Device Manager (OS detects it) "
                    "but not in Explorer (no drive letter) is almost always uninitialized "
                    "or unformatted. Disk Management (diskmgmt.msc) is used to initialize "
                    "the disk (MBR or GPT), create a partition, format it, and assign "
                    "a drive letter."
                ),
            },
            {
                "id": "b",
                "text": "The SATA port is set to IDE mode; switch it to AHCI in BIOS",
                "correct": False,
                "rationale": (
                    "Incorrect. If the SATA mode were the issue, the drive would likely "
                    "not appear in Device Manager at all. An uninitialized disk showing "
                    "in Device Manager but not Explorer is a partition/format issue."
                ),
            },
            {
                "id": "c",
                "text": "The drive letter conflicts with a network share; reassign the letter in Device Manager",
                "correct": False,
                "rationale": (
                    "Incorrect. Drive letter conflicts can prevent Explorer from showing "
                    "a drive, but the first step for a brand-new drive is initialization "
                    "and partitioning, which is the most common reason for this symptom."
                ),
            },
            {
                "id": "d",
                "text": "The drive's firmware is incompatible; update the SSD firmware",
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware incompatibility would typically prevent the drive "
                    "from being detected at all or cause errors. The specific symptom of "
                    "'in Device Manager but not Explorer' points to an uninitialized disk."
                ),
            },
        ],
        "explanation": (
            "A new drive appears in Device Manager (recognized by the OS) but is absent "
            "from File Explorer because it has no partition table, partition, or "
            "assigned drive letter. Open Disk Management (diskmgmt.msc), initialize "
            "the disk (GPT recommended for modern systems), create a new simple volume, "
            "format it (NTFS typical for Windows), and assign a drive letter."
        ),
    },
    # ── 5.4 Video / Projector / Display ───────────────────────────────────────
    {
        "id": "a1d5-016",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A laptop display shows a very dim image that is only visible when a "
            "flashlight is shone at an angle. An external monitor connected to the "
            "laptop displays normally. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The LCD backlight or its inverter has failed",
                "correct": True,
                "rationale": (
                    "Correct. A dim image visible only with a flashlight is the classic "
                    "symptom of a failed CCFL backlight or its inverter. The LCD panel "
                    "and GPU are working (image is present), but there is no backlight "
                    "to illuminate it. The external monitor working confirms the GPU "
                    "is fine."
                ),
            },
            {
                "id": "b",
                "text": "The display cable connecting the motherboard to the LCD is broken",
                "correct": False,
                "rationale": (
                    "Incorrect. A broken display cable typically causes no image, "
                    "flickering, or lines — not a dim image where content is still "
                    "visible with a flashlight."
                ),
            },
            {
                "id": "c",
                "text": "The GPU is failing and cannot drive the internal display",
                "correct": False,
                "rationale": (
                    "Incorrect. If the GPU were failing, the external monitor would also "
                    "be affected. Since the external display works normally, the GPU is "
                    "operational."
                ),
            },
            {
                "id": "d",
                "text": "The display brightness setting in the OS is set to the minimum level",
                "correct": False,
                "rationale": (
                    "Incorrect. Software brightness settings reduce backlight intensity "
                    "but do not cause complete backlight failure resulting in an image "
                    "only visible by flashlight. This extreme dimness indicates hardware "
                    "failure."
                ),
            },
        ],
        "explanation": (
            "Laptop LCD panels require a backlight (CCFL or LED) to be visible. When "
            "the backlight or its inverter fails, the image exists but is invisible "
            "in normal lighting. A flashlight at the right angle reveals the image. "
            "CCFL lamps require an inverter board to convert DC to high-voltage AC; "
            "either the lamp or the inverter may have failed. LED backlights are driven "
            "directly and failure is usually the driver circuit or the LEDs themselves."
        ),
    },
    {
        "id": "a1d5-017",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A user complains that their LCD monitor shows a permanent ghost image of "
            "the taskbar and open application windows even when the screen content "
            "changes. What is this condition called, and what is the recommended "
            "long-term solution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Burn-in (image retention); use a screen saver or power management to blank the display when idle",
                "correct": True,
                "rationale": (
                    "Correct. Burn-in (or image persistence/retention) occurs when a "
                    "static image is displayed for extended periods, causing uneven pixel "
                    "degradation. Using a screen saver or configuring the monitor to "
                    "sleep/blank after inactivity prevents further burn-in."
                ),
            },
            {
                "id": "b",
                "text": "Dead pixels; replace the LCD panel",
                "correct": False,
                "rationale": (
                    "Incorrect. Dead pixels are individual pixels that do not respond at "
                    "all (stuck on black or a fixed color), not persistent ghost images "
                    "of former content."
                ),
            },
            {
                "id": "c",
                "text": "A loose display cable causing signal ghosting; reseat the cable",
                "correct": False,
                "rationale": (
                    "Incorrect. A loose cable causes flickering, noise, or complete "
                    "signal loss — not a faint permanent image of previous screen content."
                ),
            },
            {
                "id": "d",
                "text": "Incorrect refresh rate causing phosphor afterglow; change the refresh rate in display settings",
                "correct": False,
                "rationale": (
                    "Incorrect. Phosphor afterglow relates to CRT (cathode-ray tube) "
                    "monitors, not LCDs. LCDs do not use phosphor; burn-in in LCDs "
                    "results from liquid crystal and backlight degradation."
                ),
            },
        ],
        "explanation": (
            "LCD burn-in (also called image retention or image persistence) is caused "
            "by long-term display of static content degrading the pixels unevenly. "
            "Prevention is better than cure: configure a screensaver or auto-sleep "
            "policy. OLED panels are more susceptible to burn-in than IPS or TN LCD."
        ),
    },
    {
        "id": "a1d5-018",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A classroom projector suddenly shuts off during a presentation and will "
            "not restart immediately. After 20 minutes it powers on normally. This "
            "behavior repeats whenever it is used for more than an hour. What is the "
            "MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The projector is overheating; clean the air filter and ensure adequate ventilation",
                "correct": True,
                "rationale": (
                    "Correct. Projector lamps generate intense heat. Most projectors have "
                    "thermal protection that shuts the unit off when internal temperature "
                    "exceeds a threshold. After cooling (about 20 min), it operates "
                    "again. A clogged air filter or obstructed vents are the most common "
                    "causes."
                ),
            },
            {
                "id": "b",
                "text": "The projector lamp has burned out and needs replacement",
                "correct": False,
                "rationale": (
                    "Incorrect. A burned-out lamp causes permanent loss of image; the "
                    "projector would not recover after 20 minutes. Overheating allows "
                    "normal operation once cooled."
                ),
            },
            {
                "id": "c",
                "text": "The HDMI cable is overheating and causing signal loss",
                "correct": False,
                "rationale": (
                    "Incorrect. Cables do not overheat in normal conditions and would not "
                    "cause a complete projector shutdown. The projector's internal thermal "
                    "protection is the culprit."
                ),
            },
            {
                "id": "d",
                "text": "The projector's power supply is failing under sustained load",
                "correct": False,
                "rationale": (
                    "Incorrect. A failing power supply would cause random shutdowns at "
                    "any time, not a pattern tied to a consistent runtime plus a recovery "
                    "after a specific cool-down period."
                ),
            },
        ],
        "explanation": (
            "Projectors generate enormous heat from their UHP lamps. Thermal shutdown "
            "after extended use that resolves after ~20 minutes of cooling is the "
            "hallmark of overheating. Check and clean the dust filter, ensure the "
            "exhaust and intake vents are unobstructed, and verify the fan is working. "
            "Operating in a high-ambient-temperature room can also contribute."
        ),
    },
    {
        "id": "a1d5-019",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A user connects a second monitor via HDMI and can see video, but there is "
            "no audio from the monitor's built-in speakers. The laptop's own speakers "
            "work fine. What should the technician check FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify that the HDMI audio output device is selected as the default playback device in OS sound settings",
                "correct": True,
                "rationale": (
                    "Correct. HDMI carries both video and audio. When a new HDMI display "
                    "is connected, the OS may not automatically switch the default audio "
                    "output. In Windows Sound settings (or macOS Sound Preferences), the "
                    "technician must select the HDMI output as the default playback device."
                ),
            },
            {
                "id": "b",
                "text": "Replace the HDMI cable with a DisplayPort cable for audio support",
                "correct": False,
                "rationale": (
                    "Incorrect. HDMI natively supports audio transmission. The cable is "
                    "not the issue — the audio output device selection in the OS is the "
                    "more likely cause."
                ),
            },
            {
                "id": "c",
                "text": "Connect a separate 3.5 mm audio cable from the laptop headphone jack to the monitor",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a workaround, not the best first step. The HDMI "
                    "connection should carry audio; the correct fix is to set the HDMI "
                    "device as the audio output in the OS."
                ),
            },
            {
                "id": "d",
                "text": "Update the monitor firmware to enable audio over HDMI",
                "correct": False,
                "rationale": (
                    "Incorrect. Monitor firmware updates rarely affect audio routing. "
                    "The OS audio device selection is the standard first check."
                ),
            },
        ],
        "explanation": (
            "HDMI supports audio alongside video. When a monitor with built-in speakers "
            "is connected via HDMI but produces no sound, the OS has typically not "
            "switched the default audio output. In Windows: right-click the speaker "
            "icon → Sounds → Playback tab, select the HDMI output device, and set it "
            "as default. macOS: System Preferences → Sound → Output."
        ),
    },
    # ── 5.5 Mobile Device Issues ──────────────────────────────────────────────
    {
        "id": "a1d5-020",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A technician inspects a smartphone and notices the back of the device is "
            "visibly bulging and the screen has begun to separate from the frame. The "
            "device still powers on. What is the BEST immediate action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Stop using the device immediately; do not charge it, and safely dispose of or recycle the battery",
                "correct": True,
                "rationale": (
                    "Correct. A bulging smartphone battery indicates lithium-ion cell "
                    "swelling from gas produced by internal chemical breakdown. This is "
                    "a thermal runaway and fire risk. The device must not be used or "
                    "charged; it should be handled carefully, kept away from flammable "
                    "materials, and taken to proper e-waste/battery recycling."
                ),
            },
            {
                "id": "b",
                "text": "Charge the device to 100% to recalibrate the battery cells",
                "correct": False,
                "rationale": (
                    "Incorrect. Charging a swollen lithium-ion battery is extremely "
                    "dangerous and may trigger thermal runaway, fire, or explosion."
                ),
            },
            {
                "id": "c",
                "text": "Press the back panel down firmly to re-seat it and continue using the device",
                "correct": False,
                "rationale": (
                    "Incorrect. Applying pressure to a swollen battery can cause it to "
                    "rupture, leak toxic/flammable electrolyte, or ignite. This is "
                    "extremely dangerous."
                ),
            },
            {
                "id": "d",
                "text": "Place the device in the freezer to cool the battery and reduce swelling",
                "correct": False,
                "rationale": (
                    "Incorrect. Extreme cold causes condensation inside the device and "
                    "can damage electronics. It does not repair a swollen battery and "
                    "is not a safe or recommended practice."
                ),
            },
        ],
        "explanation": (
            "Lithium-ion battery swelling (caused by electrolyte decomposition "
            "producing gas) is a serious safety hazard. The 'pouch' or cell inside is "
            "under pressure and can vent toxic fumes, catch fire, or explode if "
            "punctured, compressed, or subjected to further charging. CompTIA expects "
            "technicians to know: stop use immediately, do not charge, handle "
            "carefully, dispose of at a proper e-waste facility."
        ),
    },
    {
        "id": "a1d5-021",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user reports that after dropping their smartphone in a sink, the device "
            "powers on but the touch screen responds erratically — registering touches "
            "in the wrong location or triggering actions without being touched. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Liquid damage to the digitizer causing erratic capacitive sensor readings",
                "correct": True,
                "rationale": (
                    "Correct. The digitizer is the capacitive layer that detects touch "
                    "location. Water or residual moisture disrupts the capacitive field, "
                    "causing ghost touches, incorrect touch registration, and phantom "
                    "inputs. This is a direct result of liquid damage."
                ),
            },
            {
                "id": "b",
                "text": "A corrupted touch-screen driver that needs to be reinstalled",
                "correct": False,
                "rationale": (
                    "Incorrect. Driver corruption does not typically cause erratic "
                    "positional errors after a specific water-contact event. The "
                    "correlation with the drop in water points to physical/liquid "
                    "damage."
                ),
            },
            {
                "id": "c",
                "text": "A cracked LCD panel redirecting touch input signals",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario does not mention visible screen cracks, "
                    "and a cracked LCD typically causes display issues (lines, dark spots) "
                    "rather than erratic touch registration."
                ),
            },
            {
                "id": "d",
                "text": "Malware using the accessibility service to simulate ghost touches",
                "correct": False,
                "rationale": (
                    "Incorrect. Malware is a possible cause of ghost touches in general "
                    "but does not explain the direct causal link to water immersion. "
                    "Liquid damage is the most logical diagnosis given the scenario."
                ),
            },
        ],
        "explanation": (
            "Capacitive touchscreens work by detecting changes in an electrical field "
            "caused by a finger. Water bridges capacitive sensors, creating false "
            "readings and phantom touches. The correct action is to power off the "
            "device, allow it to dry completely (using silica gel, not heat), and "
            "inspect the digitizer. If erratic behavior persists after drying, the "
            "digitizer assembly likely needs replacement."
        ),
    },
    {
        "id": "a1d5-022",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user's tablet charges very slowly and only when using the original "
            "manufacturer cable, but not with third-party USB-C cables. The charging "
            "port looks slightly bent. What is the BEST explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The USB-C port has physical damage that allows only the tighter fit of the OEM cable to make proper contact",
                "correct": True,
                "rationale": (
                    "Correct. A bent or damaged USB-C port may not make consistent "
                    "electrical contact with cables of varying plug tolerances. The OEM "
                    "cable may have a slightly different plug geometry that still engages "
                    "the bent contacts. The proper fix is port repair or replacement."
                ),
            },
            {
                "id": "b",
                "text": "Third-party cables are incompatible because the tablet uses USB Power Delivery (PD) exclusively",
                "correct": False,
                "rationale": (
                    "Incorrect. USB PD is a standard and most USB-C cables support it. "
                    "The visible damage to the port is the more direct explanation for "
                    "the selective compatibility."
                ),
            },
            {
                "id": "c",
                "text": "The tablet's charging IC is failing and will only accept current from OEM chargers",
                "correct": False,
                "rationale": (
                    "Incorrect. While charging ICs can fail, the visible physical damage "
                    "to the port is the most direct and probable cause of selective "
                    "contact — especially when other cables physically don't connect well."
                ),
            },
            {
                "id": "d",
                "text": "A software update has blocked third-party charging accessory authentication",
                "correct": False,
                "rationale": (
                    "Incorrect. Some Apple devices do use MFi authentication, but for "
                    "USB-C devices a software block on cables is unusual, and the visible "
                    "physical damage to the port makes physical contact failure the "
                    "obvious first diagnosis."
                ),
            },
        ],
        "explanation": (
            "Damaged USB-C or Lightning ports (bent pins, debris, or deformed housing) "
            "cause poor or intermittent electrical contact. A physically damaged port "
            "may work with one cable but not another depending on plug tolerances. "
            "Inspect the port for bent pins or debris, attempt cleaning with compressed "
            "air, then arrange port replacement if contact remains poor."
        ),
    },
    # ── 5.6 Printer Issues ────────────────────────────────────────────────────
    {
        "id": "a1d5-023",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A laser printer produces pages where the toner smears when rubbed with a "
            "finger, even though the image appears complete. What is the MOST likely "
            "cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The fuser assembly is faulty and not reaching the correct temperature to bond the toner",
                "correct": True,
                "rationale": (
                    "Correct. In laser printing, the fuser uses heat and pressure to "
                    "permanently bond toner to paper. If the fuser is not reaching "
                    "adequate temperature (or the fuser roller is damaged), toner sits "
                    "on the paper without fusing and smears when touched."
                ),
            },
            {
                "id": "b",
                "text": "The toner cartridge is low and producing weak electrostatic attraction",
                "correct": False,
                "rationale": (
                    "Incorrect. A low toner cartridge causes faded or light print, not "
                    "unfused toner that smears. Toner quantity does not affect fusing."
                ),
            },
            {
                "id": "c",
                "text": "The drum unit is worn and leaving excess toner on the page",
                "correct": False,
                "rationale": (
                    "Incorrect. A worn drum can cause streaks, spots, or ghost images "
                    "but does not prevent fusing. The smearing symptom specifically "
                    "implicates the fuser."
                ),
            },
            {
                "id": "d",
                "text": "The paper type is incompatible, causing the toner to repel",
                "correct": False,
                "rationale": (
                    "Incorrect. While incorrect paper (e.g., inkjet-only stock) can "
                    "affect fusing to some degree, the most direct and testable cause "
                    "of unfused toner is a faulty fuser assembly."
                ),
            },
        ],
        "explanation": (
            "Laser printing has four stages: charging, exposing, developing, and fusing. "
            "The fuser (a heated roller pair) permanently bonds toner by melting it into "
            "the paper fibers. Toner that smears indicates it was never fused — the "
            "fuser temperature is too low or the assembly has failed. Replace the fuser "
            "unit. Be careful: fusers operate at high temperatures and may retain heat "
            "after shutdown."
        ),
    },
    {
        "id": "a1d5-024",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A laser printer is printing vertical black lines down every page regardless "
            "of the document content. The lines are consistently in the same position "
            "on every page. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A scratch or gouge on the photosensitive drum",
                "correct": True,
                "rationale": (
                    "Correct. A damaged drum (scratch, gouge, or toner build-up in a "
                    "fixed location) produces a consistent vertical line at the same "
                    "position on every page because the drum rotates at the same speed "
                    "as the page advances, creating the same defect repeatedly."
                ),
            },
            {
                "id": "b",
                "text": "A clogged print head nozzle",
                "correct": False,
                "rationale": (
                    "Incorrect. Clogged print head nozzles are an inkjet issue, not a "
                    "laser printer issue. Laser printers do not have print heads."
                ),
            },
            {
                "id": "c",
                "text": "Low toner causing uneven distribution",
                "correct": False,
                "rationale": (
                    "Incorrect. Low toner causes faded or inconsistent overall coverage, "
                    "not consistent vertical lines in the same fixed position on every page."
                ),
            },
            {
                "id": "d",
                "text": "A faulty fuser roller leaving toner streaks",
                "correct": False,
                "rationale": (
                    "Incorrect. A fuser roller defect can leave marks but tends to "
                    "produce smearing or horizontal artifacts. Consistent vertical lines "
                    "at the same horizontal position on every page are characteristic "
                    "of a drum defect."
                ),
            },
        ],
        "explanation": (
            "In a laser printer, the photosensitive drum is charged, then selectively "
            "discharged by the laser to form the image. A physical defect (scratch, "
            "chip, or toner contamination) on the drum surface causes toner to adhere "
            "or fail to adhere at that point on every rotation, producing a repeating "
            "vertical line at the same position on every page. Replacing the drum/toner "
            "cartridge (which includes the drum in most consumer printers) resolves it."
        ),
    },
    {
        "id": "a1d5-025",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "Users report that the network laser printer randomly pulls multiple sheets "
            "of paper at once, resulting in jams and misprinted pages. The printer uses "
            "standard 20 lb bond paper from a new ream. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The paper pickup/separation rollers are worn and no longer separating sheets properly",
                "correct": True,
                "rationale": (
                    "Correct. The separation pad or roller prevents multi-sheet feeds by "
                    "gripping and holding back excess sheets. When these components wear "
                    "out, multiple sheets are fed simultaneously (multipage misfeed). "
                    "Replacement of the pickup and separation rollers resolves this."
                ),
            },
            {
                "id": "b",
                "text": "The paper weight is too heavy for the printer's paper path",
                "correct": False,
                "rationale": (
                    "Incorrect. Standard 20 lb bond paper is the most common paper "
                    "weight used in office laser printers and is well within spec. "
                    "Paper weight is not the issue."
                ),
            },
            {
                "id": "c",
                "text": "The fuser temperature is too high, causing the paper to stick to itself",
                "correct": False,
                "rationale": (
                    "Incorrect. The fuser acts on paper after it has already been fed "
                    "through the pickup mechanism. Fuser temperature does not cause "
                    "multi-sheet feed at the input tray."
                ),
            },
            {
                "id": "d",
                "text": "A corrupt print job in the queue is sending multiple copies simultaneously",
                "correct": False,
                "rationale": (
                    "Incorrect. A corrupt print job could cause garbled output but would "
                    "not cause the physical mechanism to grab multiple sheets at once. "
                    "This is a mechanical (roller wear) issue."
                ),
            },
        ],
        "explanation": (
            "Multipage misfeed (multiple sheets feeding at once) is caused by worn "
            "pickup rollers and/or a worn or glazed separation pad. The separation "
            "pad/roller uses friction to hold back sheets while the pickup roller feeds "
            "one at a time. With worn components this friction is insufficient. "
            "Cleaning or replacing the rollers and separation pad resolves the issue. "
            "Fanning paper before loading can temporarily help."
        ),
    },
    {
        "id": "a1d5-026",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A color laser printer is producing prints where all colors appear correct "
            "except cyan, which is missing entirely, leaving the print looking "
            "orange-red. What is the BEST first step?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check and replace the cyan toner cartridge",
                "correct": True,
                "rationale": (
                    "Correct. Color laser printers use CMYK (Cyan, Magenta, Yellow, "
                    "Black) cartridges. If cyan is completely absent from the output, "
                    "the cyan cartridge is likely empty, improperly seated, or failed. "
                    "Check the cartridge first."
                ),
            },
            {
                "id": "b",
                "text": "Recalibrate the color profile in the printer driver",
                "correct": False,
                "rationale": (
                    "Incorrect. A color profile calibration issue would shift or distort "
                    "colors across the board; a completely missing color channel indicates "
                    "a hardware (cartridge or transfer belt) issue, not a calibration issue."
                ),
            },
            {
                "id": "c",
                "text": "Replace the entire imaging drum unit",
                "correct": False,
                "rationale": (
                    "Incorrect. While a failed drum segment could theoretically affect "
                    "one color, the most common and most likely first check for a "
                    "completely missing color is the corresponding toner cartridge."
                ),
            },
            {
                "id": "d",
                "text": "Reinstall the printer driver to restore color channel mapping",
                "correct": False,
                "rationale": (
                    "Incorrect. A driver reinstall would not fix a physical absence of "
                    "color caused by an empty or failed toner cartridge."
                ),
            },
        ],
        "explanation": (
            "Color laser printers use four separate toner cartridges (CMYK). The absence "
            "of a single color across all output is almost always a cartridge-level "
            "problem: empty, improperly seated, or shutter not opening. Removing and "
            "reseating the cyan cartridge is the first step; if that fails, replace it. "
            "If the new cartridge also fails to produce cyan, the cyan print drum or "
            "developer unit may be defective."
        ),
    },
    {
        "id": "a1d5-027",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A user sends a print job for a document that should print in portrait "
            "orientation, but it consistently prints in landscape, cutting off the right "
            "side of the content. All other users on the same network printer print "
            "correctly. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The page orientation setting in the application or printer preferences on the user's PC is set to landscape",
                "correct": True,
                "rationale": (
                    "Correct. Because other users print correctly, the printer itself is "
                    "not misconfigured. The issue is specific to this user's workstation — "
                    "the print orientation is set to landscape in the application or the "
                    "local printer preferences/driver settings."
                ),
            },
            {
                "id": "b",
                "text": "The printer's paper tray is loaded with paper in landscape orientation",
                "correct": False,
                "rationale": (
                    "Incorrect. Paper loaded in the wrong orientation would affect all "
                    "users, not just one. Since other users print correctly, the tray "
                    "is fine."
                ),
            },
            {
                "id": "c",
                "text": "The printer firmware is set to landscape mode and needs to be reset",
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware-level orientation settings would affect all "
                    "jobs, not just one user's. The problem is isolated to one workstation."
                ),
            },
            {
                "id": "d",
                "text": "The document has an embedded PostScript page orientation command forcing landscape",
                "correct": False,
                "rationale": (
                    "Incorrect. While possible, this is a less likely cause than a simple "
                    "misconfigured printer setting on the user's PC, and would be "
                    "investigated only after checking the driver/application settings."
                ),
            },
        ],
        "explanation": (
            "Orientation issues that are user-specific (not affecting other users on "
            "the same printer) almost always stem from the local workstation's printer "
            "driver properties or application print settings. Check File → Print → "
            "Properties in the application, or open the printer's preferences in "
            "Settings → Printers and verify the orientation is set to Portrait."
        ),
    },
    # ── 5.7 Wired/Wireless Network Troubleshooting ────────────────────────────
    {
        "id": "a1d5-028",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A user can access resources on the local network but cannot reach any "
            "internet sites by domain name. Pinging the IP address 8.8.8.8 succeeds. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The DNS server address configured on the workstation is incorrect or the DNS server is down",
                "correct": True,
                "rationale": (
                    "Correct. Successful ping by IP (8.8.8.8) proves IP connectivity "
                    "and default gateway routing are working. Failure to reach sites by "
                    "domain name (while IP works) isolates the problem to DNS resolution. "
                    "The DNS server is unreachable, down, or misconfigured."
                ),
            },
            {
                "id": "b",
                "text": "The default gateway is misconfigured, blocking internet traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. If the default gateway were misconfigured, the ping to "
                    "8.8.8.8 (an external IP) would also fail, since that requires "
                    "routing through the gateway."
                ),
            },
            {
                "id": "c",
                "text": "The workstation has an APIPA address and cannot route beyond the local subnet",
                "correct": False,
                "rationale": (
                    "Incorrect. An APIPA (169.254.x.x) address would prevent reaching "
                    "8.8.8.8 by IP, which the user can do. The IP configuration is "
                    "valid."
                ),
            },
            {
                "id": "d",
                "text": "The network cable is damaged, causing intermittent packet loss",
                "correct": False,
                "rationale": (
                    "Incorrect. A damaged cable causing packet loss would also disrupt "
                    "the ping to 8.8.8.8, not just name resolution."
                ),
            },
        ],
        "explanation": (
            "The classic diagnostic: if you can ping an external IP but not reach sites "
            "by name, DNS is the problem. Use 'nslookup google.com' to test resolution. "
            "Common fixes: correct the DNS server IP in network adapter settings, "
            "use a public DNS like 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare) temporarily, "
            "or restart/fix the DNS service on the local DNS server."
        ),
    },
    {
        "id": "a1d5-029",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician needs to determine the exact path (each router hop) that "
            "packets take from a Windows workstation to a remote server at 203.0.113.50 "
            "to identify where along the route latency spikes occur. Which command "
            "should the technician use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "tracert 203.0.113.50",
                "correct": True,
                "rationale": (
                    "Correct. tracert (Trace Route) sends ICMP packets with incrementing "
                    "TTL values to discover each hop between the workstation and the "
                    "destination, displaying the round-trip time (RTT) for each hop. "
                    "This directly identifies where latency increases along the path."
                ),
            },
            {
                "id": "b",
                "text": "ping 203.0.113.50",
                "correct": False,
                "rationale": (
                    "Incorrect. ping measures round-trip time to the final destination "
                    "only; it does not show individual hop latency or the route taken."
                ),
            },
            {
                "id": "c",
                "text": "netstat -an",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat displays active network connections, listening "
                    "ports, and statistics for the local machine — it does not trace "
                    "the route to a remote host."
                ),
            },
            {
                "id": "d",
                "text": "nslookup 203.0.113.50",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup performs DNS lookups (resolving names to IPs "
                    "or reverse lookups). It does not trace network paths or measure "
                    "per-hop latency."
                ),
            },
        ],
        "explanation": (
            "tracert (Windows) / traceroute (Linux/macOS) uses ICMP Echo Requests with "
            "incrementing IP TTL values. Each router decrements the TTL; when it reaches "
            "0, the router sends back an ICMP 'Time Exceeded' message, revealing its "
            "address and RTT. This maps the route and pinpoints high-latency hops or "
            "routing anomalies."
        ),
    },
    {
        "id": "a1d5-030",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician suspects a workstation's IP configuration is incorrect after "
            "a DHCP server change. Which Windows command displays the full IP "
            "configuration (IP address, subnet mask, default gateway, and DNS servers) "
            "for all network adapters?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ipconfig /all",
                "correct": True,
                "rationale": (
                    "Correct. 'ipconfig /all' displays full IP configuration details "
                    "for all adapters including IP address, subnet mask, default gateway, "
                    "DNS server addresses, DHCP server, lease times, and MAC address."
                ),
            },
            {
                "id": "b",
                "text": "netstat -r",
                "correct": False,
                "rationale": (
                    "Incorrect. 'netstat -r' displays the routing table, not individual "
                    "adapter IP configuration details like DNS servers or DHCP lease info."
                ),
            },
            {
                "id": "c",
                "text": "ping /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ping does not have an '/all' switch that displays network "
                    "configuration. ping tests connectivity to a target host."
                ),
            },
            {
                "id": "d",
                "text": "nslookup /all",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup performs DNS queries; it does not display the "
                    "workstation's IP configuration, subnet mask, or gateway settings."
                ),
            },
        ],
        "explanation": (
            "ipconfig /all is the go-to Windows command for viewing complete IP "
            "configuration. Key fields: IP Address, Subnet Mask, Default Gateway, "
            "DNS Servers, DHCP Enabled/Server, Lease Obtained/Expires, and Physical "
            "(MAC) Address. On Linux/macOS use 'ip addr' or 'ifconfig -a'."
        ),
    },
    {
        "id": "a1d5-031",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician wants to verify whether a domain name resolves to the correct "
            "IP address and which DNS server is answering the query. Which command "
            "should be used on a Windows workstation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "nslookup <domain_name>",
                "correct": True,
                "rationale": (
                    "Correct. nslookup queries the configured DNS server and returns the "
                    "resolved IP address along with the name and address of the DNS server "
                    "that answered the query — exactly the information the technician needs."
                ),
            },
            {
                "id": "b",
                "text": "ping <domain_name>",
                "correct": False,
                "rationale": (
                    "Incorrect. ping does resolve the name to an IP but does not show "
                    "which DNS server answered the query, making it less useful for DNS "
                    "server verification."
                ),
            },
            {
                "id": "c",
                "text": "tracert <domain_name>",
                "correct": False,
                "rationale": (
                    "Incorrect. tracert traces the network path to the destination; it "
                    "performs name resolution incidentally but is not designed to verify "
                    "DNS server answers."
                ),
            },
            {
                "id": "d",
                "text": "netstat -n <domain_name>",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat displays active connections and statistics; it "
                    "does not perform or display DNS resolution results."
                ),
            },
        ],
        "explanation": (
            "nslookup (Name Server Lookup) queries the configured DNS server for a "
            "specific name or IP. The output shows: the DNS server name and IP, and "
            "the resolved name/IP for the query. It can also query specific DNS servers "
            "by typing 'server <ip>' within the interactive mode, useful for "
            "comparing authoritative vs. recursive resolver results."
        ),
    },
    {
        "id": "a1d5-032",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician needs to see all currently established TCP connections on a "
            "Windows workstation and the process ID (PID) associated with each "
            "connection, to identify a suspicious process communicating with an "
            "external IP. Which command is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "netstat -ano",
                "correct": True,
                "rationale": (
                    "Correct. 'netstat -ano' displays all active connections and "
                    "listening ports (-a), in numeric format without name resolution "
                    "(-n), and includes the owning process ID (-o). The PID can then "
                    "be cross-referenced in Task Manager."
                ),
            },
            {
                "id": "b",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /all shows the adapter configuration "
                    "(IP, gateway, DNS). It does not show active connections or "
                    "associated processes."
                ),
            },
            {
                "id": "c",
                "text": "tracert <suspicious_IP>",
                "correct": False,
                "rationale": (
                    "Incorrect. tracert traces the network path to a destination. It "
                    "does not display local process connections or listening ports."
                ),
            },
            {
                "id": "d",
                "text": "ping -t <suspicious_IP>",
                "correct": False,
                "rationale": (
                    "Incorrect. ping -t continuously pings a target to test reachability; "
                    "it does not enumerate local connections or reveal which process "
                    "owns a connection."
                ),
            },
        ],
        "explanation": (
            "'netstat -ano' is the standard command for connection forensics: -a shows "
            "all connections/ports, -n suppresses DNS lookups for speed, -o adds the "
            "owning PID. Cross-reference PID with Task Manager (Details tab) to "
            "identify the process. 'netstat -b' also shows executable names but "
            "requires elevation."
        ),
    },
    {
        "id": "a1d5-033",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician needs to map a network share (\\\\fileserver\\data) to drive "
            "letter Z: from a Windows command prompt so that it persists across reboots "
            "for all users. Which command accomplishes this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "net use Z: \\\\fileserver\\data /persistent:yes",
                "correct": True,
                "rationale": (
                    "Correct. 'net use' maps a network drive. 'Z:' assigns the drive "
                    "letter, '\\\\fileserver\\data' specifies the UNC path, and "
                    "'/persistent:yes' ensures the mapping is restored at each logon."
                ),
            },
            {
                "id": "b",
                "text": "netstat -r \\\\fileserver\\data Z:",
                "correct": False,
                "rationale": (
                    "Incorrect. netstat displays routing and connection statistics; "
                    "it cannot map network drives."
                ),
            },
            {
                "id": "c",
                "text": "ipconfig /map Z: \\\\fileserver\\data",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig manages IP configuration; it has no "
                    "functionality for mapping network drives."
                ),
            },
            {
                "id": "d",
                "text": "ping \\\\fileserver\\data /drive:Z",
                "correct": False,
                "rationale": (
                    "Incorrect. ping tests connectivity; it has no facility for mapping "
                    "drives or UNC paths."
                ),
            },
        ],
        "explanation": (
            "'net use' is the Windows command-line tool for mapping and managing "
            "network drives and shared resources. Syntax: net use <drive>: <UNC_path> "
            "[/persistent:yes|no] [/user:<domain\\user>] [<password>]. "
            "'/persistent:yes' ensures the mapping is saved and restored at each "
            "logon. Group Policy is the enterprise alternative."
        ),
    },
    {
        "id": "a1d5-034",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "Users in one wing of a building report that their wired network connection "
            "drops for 2–5 seconds every few minutes throughout the day. Other parts of "
            "the building are unaffected. Network logs show frequent link-state changes "
            "on the switch port for that wing. What is this symptom called and what is "
            "the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Port flapping; most likely caused by a bad patch cable or a failing NIC in one device causing the switch port to oscillate",
                "correct": True,
                "rationale": (
                    "Correct. Port flapping refers to a switch port repeatedly cycling "
                    "between up and down states. It disrupts all devices connected through "
                    "that port. Common causes include a faulty cable, damaged connector, "
                    "failing NIC, or duplex mismatch. Because it is localized to one wing, "
                    "the cabling or a device in that segment is the likely culprit."
                ),
            },
            {
                "id": "b",
                "text": "High latency caused by network congestion at the router",
                "correct": False,
                "rationale": (
                    "Incorrect. Congestion causes slow speeds and high latency, not "
                    "sudden complete link-state drops that appear in switch logs as "
                    "repeated up/down transitions."
                ),
            },
            {
                "id": "c",
                "text": "DNS server unavailability causing periodic name resolution timeouts",
                "correct": False,
                "rationale": (
                    "Incorrect. DNS failures cause name resolution errors, not physical "
                    "link-state changes logged by the switch."
                ),
            },
            {
                "id": "d",
                "text": "IP address conflicts causing ARP table corruption on the switch",
                "correct": False,
                "rationale": (
                    "Incorrect. IP conflicts cause connectivity issues between specific "
                    "hosts but do not cause physical link-state oscillations visible in "
                    "switch port logs."
                ),
            },
        ],
        "explanation": (
            "Port flapping (link-state oscillation) is documented in switch logs as "
            "repeated 'link up / link down' events. Causes include: damaged cables, "
            "loose connectors, failing NIC, duplex/speed auto-negotiation problems, "
            "or a device with a faulty network stack. Identify the port, isolate each "
            "device and cable in the affected segment, and replace faulty components."
        ),
    },
    {
        "id": "a1d5-035",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A user's laptop connects to the corporate Wi-Fi SSID but shows 'Limited "
            "connectivity' with an IP address of 169.254.45.12. Other devices on the "
            "same SSID receive correct IP addresses. What is the MOST likely cause and "
            "fix for this specific laptop?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The laptop failed to obtain a DHCP lease; run 'ipconfig /release' followed by 'ipconfig /renew'",
                "correct": True,
                "rationale": (
                    "Correct. 169.254.x.x is an APIPA (Automatic Private IP Addressing) "
                    "address assigned by Windows when a DHCP lease cannot be obtained. "
                    "Since other devices on the same SSID work, the DHCP server is fine; "
                    "this laptop's DHCP client process failed. Releasing and renewing "
                    "forces a fresh DHCP request."
                ),
            },
            {
                "id": "b",
                "text": "The DHCP server has run out of addresses in its pool",
                "correct": False,
                "rationale": (
                    "Incorrect. If the DHCP pool were exhausted, all devices attempting "
                    "to connect would fail, not just this one laptop."
                ),
            },
            {
                "id": "c",
                "text": "The wireless access point has reached its maximum client association limit",
                "correct": False,
                "rationale": (
                    "Incorrect. If the AP client limit were reached, the laptop would "
                    "not associate with the SSID at all and would not even receive an "
                    "APIPA address (which requires an association)."
                ),
            },
            {
                "id": "d",
                "text": "The laptop's wireless adapter driver is outdated and must be updated before DHCP will work",
                "correct": False,
                "rationale": (
                    "Incorrect. An outdated driver may cause connectivity issues, but "
                    "the APIPA address indicates the adapter is associated and the DHCP "
                    "transaction simply failed; a release/renew is the immediate fix."
                ),
            },
        ],
        "explanation": (
            "APIPA (169.254.0.0/16) is a self-assigned address used by Windows when "
            "DHCP discovery fails after the standard timeout period. 'ipconfig /release' "
            "clears the (non-existent) lease, and 'ipconfig /renew' sends a new DHCP "
            "DISCOVER broadcast. If renew fails repeatedly, check if the wireless "
            "association is stable and whether the DHCP client Windows service is running."
        ),
    },
    {
        "id": "a1d5-036",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "Several users on the same floor report that their wireless connection is "
            "very slow during peak hours (10 AM – 2 PM) but fast early morning. "
            "All users are associated with the same access point on the 2.4 GHz band. "
            "A Wi-Fi analyzer shows several neighboring networks on overlapping channels. "
            "What is the MOST likely cause of the slow speeds?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Co-channel and adjacent-channel interference on the 2.4 GHz band from neighboring networks",
                "correct": True,
                "rationale": (
                    "Correct. The 2.4 GHz band has only three non-overlapping channels "
                    "(1, 6, 11 in North America). During peak hours more neighboring "
                    "networks are active, causing co-channel interference that forces "
                    "devices to wait longer for a clear channel, degrading throughput."
                ),
            },
            {
                "id": "b",
                "text": "The access point's DHCP pool is exhausted during peak hours",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP exhaustion causes 'limited connectivity' (APIPA "
                    "addresses), not merely slow speeds. Users are connected and just "
                    "experiencing reduced throughput."
                ),
            },
            {
                "id": "c",
                "text": "The internet service provider throttles bandwidth during business hours",
                "correct": False,
                "rationale": (
                    "Incorrect. ISP throttling would affect all floors and all wireless "
                    "bands equally. The symptom is specific to a floor/AP and correlates "
                    "with neighboring networks on the 2.4 GHz band."
                ),
            },
            {
                "id": "d",
                "text": "The access point firmware needs updating to support newer Wi-Fi standards",
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware does not explain a time-of-day pattern correlated "
                    "with peak business hours. The Wi-Fi analyzer data directly implicates "
                    "interference from neighboring networks."
                ),
            },
        ],
        "explanation": (
            "The 2.4 GHz band is highly congested in office environments with only "
            "three non-overlapping channels. As neighboring networks become active "
            "during peak hours, CSMA/CA contention increases and throughput drops. "
            "Solutions: change the AP to a non-overlapping channel (1, 6, or 11), "
            "migrate clients to the 5 GHz band (more available channels, less "
            "interference), or deploy additional APs with proper channel planning."
        ),
    },
    {
        "id": "a1d5-037",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A VoIP user reports that their calls are breaking up and voices sound "
            "robotic or choppy, even though network speed tests show adequate bandwidth. "
            "What network quality metric is MOST likely responsible for this symptom?"
        ),
        "options": [
            {
                "id": "a",
                "text": "High jitter (variable packet delay)",
                "correct": True,
                "rationale": (
                    "Correct. Jitter is the variation in latency between successive "
                    "packets. VoIP requires low and consistent latency to reconstruct "
                    "audio smoothly. High jitter causes audio packets to arrive "
                    "irregularly, making speech choppy or robotic even when overall "
                    "bandwidth is sufficient."
                ),
            },
            {
                "id": "b",
                "text": "Low download bandwidth",
                "correct": False,
                "rationale": (
                    "Incorrect. VoIP uses very little bandwidth (~64 Kbps per call for "
                    "G.711). The scenario states bandwidth tests are adequate, ruling "
                    "this out."
                ),
            },
            {
                "id": "c",
                "text": "MTU mismatch causing fragmentation",
                "correct": False,
                "rationale": (
                    "Incorrect. MTU mismatch can cause packet fragmentation and some "
                    "latency, but the symptom of choppy/robotic audio during a speed-"
                    "test-passing connection is most characteristic of jitter."
                ),
            },
            {
                "id": "d",
                "text": "Incorrect VLAN assignment for the VoIP phone",
                "correct": False,
                "rationale": (
                    "Incorrect. A completely wrong VLAN would likely prevent the call "
                    "from connecting at all, not cause choppy audio during an established "
                    "call."
                ),
            },
        ],
        "explanation": (
            "Jitter is the enemy of real-time protocols like VoIP and video conferencing. "
            "A jitter buffer can compensate for small variations, but when jitter is "
            "large, the buffer overflows or underflows, causing gaps, robotic voice, "
            "or dropped audio. QoS (Quality of Service) policies that prioritize "
            "real-time traffic (DSCP marking, traffic shaping) are used to control "
            "jitter on enterprise networks."
        ),
    },
    # ── Multiple Response Questions ───────────────────────────────────────────
    {
        "id": "a1d5-038",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "According to the CompTIA best-practice troubleshooting methodology, which "
            "TWO actions are part of Step 1 (Identify the problem)? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Question users about symptoms and inquire about recent changes",
                "correct": True,
                "rationale": (
                    "Correct. Questioning users and asking about recent changes (software "
                    "installs, hardware changes, environment changes) is explicitly part "
                    "of Step 1 — Identify the problem."
                ),
            },
            {
                "id": "b",
                "text": "Duplicate the problem if possible to confirm the symptom",
                "correct": True,
                "rationale": (
                    "Correct. Attempting to duplicate/reproduce the problem is a key "
                    "activity in Step 1 — it confirms the issue is real and helps "
                    "identify triggers."
                ),
            },
            {
                "id": "c",
                "text": "Establish a plan of action and implement the solution",
                "correct": False,
                "rationale": (
                    "Incorrect. Planning and implementing is Step 4, not Step 1. "
                    "Jumping to implementation before identifying the problem violates "
                    "the methodology."
                ),
            },
            {
                "id": "d",
                "text": "Document findings and outcomes in the ticketing system",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation is Step 6, the final step after the "
                    "problem has been resolved and verified."
                ),
            },
        ],
        "explanation": (
            "Step 1 (Identify the problem) includes: gathering information from the "
            "user, duplicating the problem, questioning users about symptoms, inquiring "
            "about recent changes, and approaching the problem systematically "
            "(top-to-bottom/bottom-to-top of OSI, or divide-and-conquer). Steps 4 and "
            "6 refer to later stages of the methodology."
        ),
    },
    {
        "id": "a1d5-039",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A PC fails to POST and emits a continuous beep tone. Which TWO components "
            "should the technician check FIRST as the most likely causes? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "RAM — remove and reseat all DIMM modules",
                "correct": True,
                "rationale": (
                    "Correct. A continuous beep or repeated beep sequences at POST "
                    "frequently indicate a RAM failure. Reseating all DIMMs is a quick "
                    "first action before replacing modules."
                ),
            },
            {
                "id": "b",
                "text": "Power supply — verify it is delivering correct voltages with a PSU tester",
                "correct": True,
                "rationale": (
                    "Correct. An inadequate or failing power supply can cause no-POST "
                    "symptoms and erratic beep codes by starving the motherboard of "
                    "proper voltage rails. Testing the PSU is an essential early step."
                ),
            },
            {
                "id": "c",
                "text": "Hard drive — run S.M.A.R.T. diagnostic on the boot drive",
                "correct": False,
                "rationale": (
                    "Incorrect. POST failure occurs before any storage device is "
                    "accessed. A hard drive S.M.A.R.T. test is irrelevant when the "
                    "system cannot even initialize hardware."
                ),
            },
            {
                "id": "d",
                "text": "Network adapter — remove and test without the NIC installed",
                "correct": False,
                "rationale": (
                    "Incorrect. While a faulty expansion card can cause POST issues, "
                    "the NIC is far less likely than RAM or PSU to cause a continuous "
                    "beep at startup."
                ),
            },
        ],
        "explanation": (
            "When a system produces beep codes or a continuous beep at POST and does "
            "not boot, the most common culprits are RAM and the PSU. Start by reseating "
            "RAM modules (one at a time, testing each), then verify PSU voltages. If "
            "both pass, check the CPU, motherboard, and any expansion cards by "
            "progressively removing components."
        ),
    },
    {
        "id": "a1d5-040",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A server administrator is reviewing S.M.A.R.T. data for a hard drive that "
            "has begun to show errors. Which TWO S.M.A.R.T. attributes are the STRONGEST "
            "predictors of imminent drive failure? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Reallocated Sectors Count (attribute 5) — indicates how many bad sectors have been remapped",
                "correct": True,
                "rationale": (
                    "Correct. Reallocated Sectors Count tracks how many bad sectors the "
                    "drive has remapped to spare areas. A rising count indicates active "
                    "surface degradation and is one of the strongest predictors of "
                    "impending failure."
                ),
            },
            {
                "id": "b",
                "text": "Uncorrectable Sector Count (attribute 198) — sectors that could not be read or remapped",
                "correct": True,
                "rationale": (
                    "Correct. Uncorrectable Sector Count tracks sectors that could not "
                    "be read and could not be remapped. Any non-zero value is critical "
                    "and means data has already been lost; the drive is failing."
                ),
            },
            {
                "id": "c",
                "text": "Power-On Hours Count (attribute 9) — total operational hours",
                "correct": False,
                "rationale": (
                    "Incorrect. Power-On Hours indicates drive age but is not a direct "
                    "predictor of imminent failure by itself. Many drives exceed expected "
                    "MTBF without failing."
                ),
            },
            {
                "id": "d",
                "text": "Drive Temperature (attribute 194) — current operating temperature",
                "correct": False,
                "rationale": (
                    "Incorrect. Elevated temperature is a risk factor but is not by "
                    "itself a direct failure predictor; it correlates with environmental "
                    "conditions rather than mechanical wear. Reallocated and uncorrectable "
                    "sector counts are more immediate predictors."
                ),
            },
        ],
        "explanation": (
            "Research (Google Disk Failure Study, Backblaze reports) identifies "
            "reallocated sector count, uncorrectable sector count, and current pending "
            "sector count as the top S.M.A.R.T. attributes predictive of near-term "
            "failure. A non-zero and rising reallocated sector count means the drive "
            "is actively remapping bad areas; an uncorrectable sector count means data "
            "is already being lost."
        ),
    },
    {
        "id": "a1d5-041",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A wireless laptop shows 'Connected, No Internet.' A wired workstation on "
            "the same subnet has no issues. Which TWO troubleshooting steps should the "
            "technician perform FIRST on the laptop? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run 'ipconfig /all' to verify the laptop has a valid IP address, gateway, and DNS",
                "correct": True,
                "rationale": (
                    "Correct. Verifying IP configuration is the essential first step. "
                    "An APIPA address (169.254.x.x) indicates a DHCP failure; an "
                    "incorrect gateway or DNS would explain 'no internet' with a valid "
                    "local IP."
                ),
            },
            {
                "id": "b",
                "text": "Ping the default gateway to test layer 3 connectivity to the router",
                "correct": True,
                "rationale": (
                    "Correct. If the IP config appears correct, pinging the default "
                    "gateway tests whether layer 3 connectivity to the router exists. "
                    "If the gateway ping fails, the wireless connection or routing is "
                    "the problem."
                ),
            },
            {
                "id": "c",
                "text": "Replace the wireless access point with a wired switch",
                "correct": False,
                "rationale": (
                    "Incorrect. Replacing hardware is a drastic action and inappropriate "
                    "as a first step. The wired workstation works, suggesting the AP and "
                    "switch are functioning; the issue is likely configuration on the "
                    "laptop."
                ),
            },
            {
                "id": "d",
                "text": "Call the ISP to report an outage",
                "correct": False,
                "rationale": (
                    "Incorrect. The wired workstation has no issues, which means the "
                    "internet connection itself is fine. The problem is specific to the "
                    "wireless laptop."
                ),
            },
        ],
        "explanation": (
            "When a wireless device shows 'Connected, No Internet' while wired devices "
            "work: 1) Check IP config (ipconfig /all) — APIPA means DHCP failure; "
            "2) Ping the gateway — if it fails, layer 3 path is broken on the wireless "
            "interface; 3) Ping an external IP (e.g., 8.8.8.8) — if that succeeds but "
            "DNS fails, check DNS settings. Isolating each layer confirms where the "
            "fault lies."
        ),
    },
    {
        "id": "a1d5-042",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A laser printer is producing pages with faded, light print that is "
            "uneven across the page. Which TWO are the MOST likely causes? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The toner cartridge is low or near the end of its rated page yield",
                "correct": True,
                "rationale": (
                    "Correct. Low toner is the most common cause of faded, light, or "
                    "uneven output. When toner levels drop, the developer cannot "
                    "adequately coat the drum, producing a lighter image."
                ),
            },
            {
                "id": "b",
                "text": "The toner density or economy mode setting is configured for reduced toner use",
                "correct": True,
                "rationale": (
                    "Correct. Many laser printers have an 'EconoMode,' 'Draft,' or "
                    "'Toner Save' setting that deliberately reduces toner density for "
                    "lighter, faster output. If enabled, output will be faded."
                ),
            },
            {
                "id": "c",
                "text": "The fuser temperature is too high, over-baking the toner and making it disappear",
                "correct": False,
                "rationale": (
                    "Incorrect. Excessive fuser temperature tends to cause paper "
                    "warping, melting, or jams, not faded print. Faded print is a "
                    "toner delivery or density issue, not a fusing temperature issue."
                ),
            },
            {
                "id": "d",
                "text": "The paper is too thick, preventing adequate toner adhesion",
                "correct": False,
                "rationale": (
                    "Incorrect. While heavy cardstock can affect fusing, it does not "
                    "typically cause uniformly faded output on standard paper. Low toner "
                    "or economy mode settings are far more likely."
                ),
            },
        ],
        "explanation": (
            "Faded or light laser print typically results from: 1) Low/empty toner — "
            "shaking the cartridge gently can temporarily redistribute toner; or "
            "2) Economy/toner-save mode enabled in driver or printer settings. "
            "Check the toner level first, then review the print quality settings "
            "in the printer driver properties."
        ),
    },
    # ── Additional Hard / Expert Questions ────────────────────────────────────
    {
        "id": "a1d5-043",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A workstation randomly reboots without any error message or BSOD, "
            "particularly under high CPU and GPU load (e.g., video rendering). "
            "The technician measures 11.4 V on the +12 V rail using a PSU tester. "
            "What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The power supply is failing and cannot deliver stable +12 V under load",
                "correct": True,
                "rationale": (
                    "Correct. The ATX specification allows ±5% tolerance on the +12 V "
                    "rail, meaning acceptable range is 11.4 V – 12.6 V. At exactly 11.4 V "
                    "the reading is at the very edge of spec and will likely drop further "
                    "under peak load, causing the system to reset. A failing PSU is the "
                    "direct cause."
                ),
            },
            {
                "id": "b",
                "text": "The CPU is overheating and triggering emergency shutdown",
                "correct": False,
                "rationale": (
                    "Incorrect. Thermal shutdown typically produces a clean power-off "
                    "after a warm-up period. The PSU voltage measurement at the limit of "
                    "spec is a more specific finding that directly explains random "
                    "reboots under load."
                ),
            },
            {
                "id": "c",
                "text": "The RAM is failing under the additional memory pressure of the rendering workload",
                "correct": False,
                "rationale": (
                    "Incorrect. RAM failures under load typically produce BSODs with "
                    "memory stop codes, not clean unexpected reboots. The voltage "
                    "measurement is the key diagnostic finding here."
                ),
            },
            {
                "id": "d",
                "text": "The motherboard voltage regulator module (VRM) is throttling the CPU",
                "correct": False,
                "rationale": (
                    "Incorrect. VRM throttling reduces CPU speed to lower power draw; "
                    "it does not cause sudden reboots. A failing PSU that cannot maintain "
                    "the +12 V rail is the more direct explanation."
                ),
            },
        ],
        "explanation": (
            "ATX +12 V rail tolerance is ±5% (11.4 V min to 12.6 V max). A measurement "
            "at exactly 11.4 V indicates the PSU is at its absolute limit under the "
            "tester's load — under actual rendering load (GPU and CPU both pulling "
            "from the +12 V rail) the voltage will sag below spec, causing the system "
            "to power off and on. Replace the PSU with one that has adequate wattage "
            "headroom."
        ),
    },
    {
        "id": "a1d5-044",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A user connects a laptop to a conference room projector via VGA and the "
            "laptop screen displays normally, but the projector screen is black. "
            "Pressing Fn + display toggle shows no change. What should the technician "
            "check FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Verify the projector's input source is set to VGA",
                "correct": True,
                "rationale": (
                    "Correct. Most projectors have multiple input sources (HDMI, VGA, "
                    "DisplayPort, composite). If the projector is set to the wrong "
                    "input, it will display a black or blank screen even when a valid "
                    "signal is connected to the VGA port. This is the simplest and most "
                    "likely first cause."
                ),
            },
            {
                "id": "b",
                "text": "Replace the VGA cable with an HDMI cable",
                "correct": False,
                "rationale": (
                    "Incorrect. Replacing the cable without first verifying the source "
                    "selection skips the simplest diagnostic step. The cable may be "
                    "fine, and the projector may simply be on the wrong input."
                ),
            },
            {
                "id": "c",
                "text": "Reinstall the laptop's graphics driver",
                "correct": False,
                "rationale": (
                    "Incorrect. The laptop screen works normally, indicating the GPU "
                    "and driver are functional. Reinstalling the driver is premature "
                    "and unlikely to resolve an input-selection issue on the projector."
                ),
            },
            {
                "id": "d",
                "text": "Replace the projector lamp, which has burned out",
                "correct": False,
                "rationale": (
                    "Incorrect. A burned-out lamp would affect all inputs equally; the "
                    "projector would show no image regardless of input source. The "
                    "simplest explanation — wrong input selected — should be ruled out "
                    "first."
                ),
            },
        ],
        "explanation": (
            "When a projector displays a black screen despite being connected, the first "
            "and most common cause is incorrect data source (input) selection. Modern "
            "projectors have multiple input ports; if the active source isn't set to "
            "the port being used, no image appears. Use the projector's remote or panel "
            "buttons to cycle through sources (VGA/PC, HDMI, etc.)."
        ),
    },
    {
        "id": "a1d5-045",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user notices that their smartphone's stylus pointer drifts across the "
            "screen on its own without any user input, and the cursor appears in the "
            "wrong location relative to where they tap. The device has not been "
            "dropped or exposed to moisture. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Digitizer calibration failure or a digitizer hardware defect causing cursor drift",
                "correct": True,
                "rationale": (
                    "Correct. Cursor/stylus drift — where the on-screen pointer does not "
                    "correspond to the physical input location or moves without input — "
                    "is caused by a miscalibrated or failing digitizer. The digitizer is "
                    "the input-sensing layer that translates physical touch/stylus "
                    "position to screen coordinates."
                ),
            },
            {
                "id": "b",
                "text": "A low battery causing the CPU to throttle and input events to be misprocessed",
                "correct": False,
                "rationale": (
                    "Incorrect. CPU throttling from a low battery affects processing "
                    "speed, not the physical accuracy of the digitizer's coordinate "
                    "mapping."
                ),
            },
            {
                "id": "c",
                "text": "Malware intercepting touch input and redirecting it to a different screen coordinate",
                "correct": False,
                "rationale": (
                    "Incorrect. Malware can generate phantom input but is far less "
                    "likely than a hardware digitizer failure for this symptom pattern, "
                    "especially in the absence of other indicators of malware."
                ),
            },
            {
                "id": "d",
                "text": "A screen protector that is too thick, adding parallax to touch input",
                "correct": False,
                "rationale": (
                    "Incorrect. A thick screen protector can create minor parallax error "
                    "at extreme angles, but would not cause autonomous cursor drift or "
                    "significant coordinate mismatch."
                ),
            },
        ],
        "explanation": (
            "Digitizer drift or cursor drift occurs when the digitizer hardware or its "
            "calibration is faulty, causing the device to misinterpret or self-generate "
            "input coordinates. For stylus-enabled devices (EMR or AES), the digitizer "
            "layer beneath the display must accurately track position. A recalibration "
            "utility may resolve software calibration drift; persistent hardware drift "
            "requires digitizer replacement."
        ),
    },
    {
        "id": "a1d5-046",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A laser printer produces output with repeating spots and smudges at "
            "regular intervals down every page. A technician measures the circumference "
            "of the photosensitive drum and finds the defect repeats exactly every "
            "94 mm — matching the drum circumference. Which component needs to be "
            "replaced?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The photosensitive drum (or the toner cartridge that contains it)",
                "correct": True,
                "rationale": (
                    "Correct. Repeating print defects that occur at intervals matching "
                    "the circumference of the photosensitive drum indicate a drum "
                    "surface defect (scratch, contamination, or coating damage). "
                    "Because the drum rotates once per drum-circumference of paper "
                    "travel, the defect repeats at that exact interval."
                ),
            },
            {
                "id": "b",
                "text": "The fuser roller, which has a damaged surface causing repeated marks",
                "correct": False,
                "rationale": (
                    "Incorrect. Fuser roller defects also produce repeating marks, but "
                    "the interval would match the fuser roller circumference (typically "
                    "smaller or larger than the drum circumference, depending on the "
                    "printer). The technician has confirmed the interval matches the drum."
                ),
            },
            {
                "id": "c",
                "text": "The transfer roller, which is leaving toner behind on the drum",
                "correct": False,
                "rationale": (
                    "Incorrect. The transfer roller transfers toner from drum to paper. "
                    "A defective transfer roller would cause inconsistent transfer, not "
                    "precisely repeating marks at the drum circumference interval."
                ),
            },
            {
                "id": "d",
                "text": "The primary charge roller (PCR), which is failing to evenly charge the drum",
                "correct": False,
                "rationale": (
                    "Incorrect. A failing PCR would cause uneven charging and result "
                    "in light or inconsistent areas of the page, not repeating discrete "
                    "spots or smudges at a fixed interval."
                ),
            },
        ],
        "explanation": (
            "In laser printer diagnostics, the interval between repeating defects "
            "identifies which rotating component is responsible. Measure the "
            "circumference of the drum, fuser roller, and transfer roller; match the "
            "interval to the component. Drum circumference defects = drum problem. "
            "Fuser roller circumference defects = fuser problem. This 'page ruler' "
            "technique is standard for laser printer diagnosis."
        ),
    },
]
