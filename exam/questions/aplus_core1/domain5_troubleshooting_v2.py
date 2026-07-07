"""
CompTIA A+ Core 1 (220-1201) — Domain 5: Hardware and Network Troubleshooting
38 NEW practice questions at hard/expert difficulty (v2 bank).
"""

QUESTIONS = [
    # ── 5.1 Troubleshooting Methodology ──────────────────────────────────────
    {
        "id": "a1d5v2-001",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician is called because a user's workstation displays a BSOD on "
            "startup. The technician reboots, observes the stop code, and notices that "
            "a RAM module was recently upgraded. Without attempting any fix, the "
            "technician forms the hypothesis that the new RAM module is incompatible. "
            "Which step of the CompTIA troubleshooting methodology has just been "
            "completed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Step 2 — Establish a theory of probable cause",
                "correct": True,
                "rationale": (
                    "Correct. Forming a hypothesis about what is causing the problem — "
                    "in this case suspecting incompatible RAM based on gathered facts — "
                    "is Step 2: Establish a theory of probable cause. The technician "
                    "has not yet tested or acted on the hypothesis."
                ),
            },
            {
                "id": "b",
                "text": "Step 1 — Identify the problem",
                "correct": False,
                "rationale": (
                    "Incorrect. Step 1 covers gathering information (observing symptoms, "
                    "questioning the user, noting recent changes). Forming a hypothesis "
                    "about the root cause moves beyond identification into Step 2."
                ),
            },
            {
                "id": "c",
                "text": "Step 3 — Test the theory to determine the cause",
                "correct": False,
                "rationale": (
                    "Incorrect. Testing the theory requires taking an action to confirm "
                    "or refute the hypothesis (e.g., reseating or swapping the RAM). "
                    "That has not been done yet."
                ),
            },
            {
                "id": "d",
                "text": "Step 4 — Establish a plan of action and implement the solution",
                "correct": False,
                "rationale": (
                    "Incorrect. A plan of action is created only after the theory has "
                    "been tested and confirmed. The technician is still at the hypothesis "
                    "stage."
                ),
            },
        ],
        "explanation": (
            "The six CompTIA steps: 1) Identify the problem, 2) Establish a theory "
            "of probable cause, 3) Test the theory, 4) Establish a plan and implement, "
            "5) Verify full functionality, 6) Document. Forming a hypothesis without "
            "yet acting on it is precisely Step 2."
        ),
    },
    {
        "id": "a1d5v2-002",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician confirms their theory by rolling back a Windows driver update, "
            "which resolves a user's print failure. Before closing the ticket the "
            "technician plans to prevent recurrence. According to the CompTIA methodology, "
            "which step covers adding preventive measures?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Step 5 — Verify full system functionality and implement preventive measures",
                "correct": True,
                "rationale": (
                    "Correct. After implementing the fix, Step 5 requires the technician "
                    "to verify the system works fully and to take preventive measures "
                    "(e.g., configuring automatic driver approval policies) so the "
                    "problem does not recur."
                ),
            },
            {
                "id": "b",
                "text": "Step 4 — Establish a plan of action and implement the solution",
                "correct": False,
                "rationale": (
                    "Incorrect. Step 4 is about executing the fix (rolling back the "
                    "driver), which has already been done. Preventive measures and "
                    "functionality verification are explicitly Step 5."
                ),
            },
            {
                "id": "c",
                "text": "Step 6 — Document findings, actions, and outcomes",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation is the final step and occurs after "
                    "verification and prevention are complete, not before."
                ),
            },
            {
                "id": "d",
                "text": "Step 3 — Test the theory to determine the cause",
                "correct": False,
                "rationale": (
                    "Incorrect. Testing the theory confirmed the driver was the cause; "
                    "that step is already complete. Preventive measures belong to Step 5."
                ),
            },
        ],
        "explanation": (
            "Step 5 has two components: (a) verify the fix restored full functionality "
            "(ask the user, test the system) and (b) implement preventive measures to "
            "avoid recurrence. Only then does the technician proceed to Step 6 "
            "(documentation)."
        ),
    },
    {
        "id": "a1d5v2-003",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A help-desk technician receives a ticket saying 'the internet is down.' "
            "Before touching any hardware or configuration, what is the FIRST action the "
            "technician should take according to the CompTIA troubleshooting methodology?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Gather information: question the user to clarify exact symptoms, affected systems, and any recent changes",
                "correct": True,
                "rationale": (
                    "Correct. The very first activity in Step 1 (Identify the problem) "
                    "is to gather information by questioning the user. 'The internet is "
                    "down' is vague — the technician must determine whether one PC, all "
                    "PCs, or the whole site is affected, and what changed recently."
                ),
            },
            {
                "id": "b",
                "text": "Reboot the router and access point to restore connectivity quickly",
                "correct": False,
                "rationale": (
                    "Incorrect. Rebooting hardware before identifying the problem is "
                    "acting without information. A reboot may clear a transient fault "
                    "but can also lose log data needed to diagnose the root cause."
                ),
            },
            {
                "id": "c",
                "text": "Run ipconfig /release and /renew on the affected workstation",
                "correct": False,
                "rationale": (
                    "Incorrect. This is a theoretical fix applied before the problem has "
                    "been properly identified. Step 1 requires gathering information first."
                ),
            },
            {
                "id": "d",
                "text": "Call the ISP to report an outage and wait for their response",
                "correct": False,
                "rationale": (
                    "Incorrect. Escalating to the ISP before even identifying whether "
                    "the issue is internal or external skips several required steps. "
                    "The technician must gather information first."
                ),
            },
        ],
        "explanation": (
            "Step 1 begins with gathering information: talking to the user, clarifying "
            "symptoms, identifying affected devices, and asking about recent changes. "
            "Only after gathering sufficient information can a theory be formed. Acting "
            "before identifying the problem may worsen the situation or obscure clues."
        ),
    },
    {
        "id": "a1d5v2-004",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician replaces a faulty network switch and connectivity is restored. "
            "The user confirms everything works. The technician then notices the server "
            "room temperature is unusually warm and adjusts the HVAC setting before "
            "writing the ticket. Which step of the methodology does the HVAC adjustment "
            "represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Step 5 — Implementing a preventive measure to avoid recurrence",
                "correct": True,
                "rationale": (
                    "Correct. Correcting the temperature is a preventive measure taken "
                    "after resolving the primary problem and verifying functionality. "
                    "Preventive measures are explicitly part of Step 5."
                ),
            },
            {
                "id": "b",
                "text": "Step 6 — Documenting the environmental condition",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation (Step 6) records what happened; it does "
                    "not involve taking corrective environmental actions."
                ),
            },
            {
                "id": "c",
                "text": "Step 1 — Gathering environmental data as part of problem identification",
                "correct": False,
                "rationale": (
                    "Incorrect. The technician has already resolved the problem and "
                    "verified functionality. Step 1 occurs at the beginning of the "
                    "process, not after resolution."
                ),
            },
            {
                "id": "d",
                "text": "Step 4 — Implementing the solution",
                "correct": False,
                "rationale": (
                    "Incorrect. The solution (replacing the switch) was the Step 4 "
                    "action. The HVAC adjustment is a secondary preventive action, "
                    "which falls under Step 5."
                ),
            },
        ],
        "explanation": (
            "Step 5 explicitly includes 'implement preventive measures' in addition to "
            "verifying full functionality. Addressing environmental factors (temperature, "
            "dust, power) that may have contributed to or could cause future failures "
            "is a textbook example of a preventive measure within Step 5."
        ),
    },
    # ── 5.2 Motherboard, RAM, CPU, Power ─────────────────────────────────────
    {
        "id": "a1d5v2-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A technician presses the power button on a desktop PC and absolutely nothing "
            "happens — no fans spin, no LEDs light, no beeps. The power outlet tests "
            "good. What is the MOST logical first component to check?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The power supply — verify the rear rocker switch is ON and test it with a PSU tester",
                "correct": True,
                "rationale": (
                    "Correct. A completely dead system (no fans, no lights, no response) "
                    "when the outlet is good points directly at the power supply as the "
                    "first suspect. The rear rocker switch may be OFF, or the PSU may "
                    "have failed. A PSU tester provides immediate confirmation without "
                    "disassembling the entire system."
                ),
            },
            {
                "id": "b",
                "text": "The RAM — remove and reseat the DIMMs",
                "correct": False,
                "rationale": (
                    "Incorrect. Failed RAM typically allows the power supply to spin up "
                    "fans and LEDs before halting at POST. With zero sign of power, the "
                    "PSU is a more direct first suspect."
                ),
            },
            {
                "id": "c",
                "text": "The CPU — reseat the processor in its socket",
                "correct": False,
                "rationale": (
                    "Incorrect. A dislodged CPU may prevent POST but typically does not "
                    "prevent the PSU from powering up fans and LEDs at all. Total silence "
                    "is a power supply or power path issue."
                ),
            },
            {
                "id": "d",
                "text": "The front-panel power switch — bypass it with a screwdriver",
                "correct": False,
                "rationale": (
                    "Incorrect. While a faulty front-panel switch is possible, it is "
                    "much less common than a failed PSU and should be checked after "
                    "confirming the PSU is delivering power."
                ),
            },
        ],
        "explanation": (
            "A 'dead' system with no power-on response at all (no fans, no lights) "
            "almost always means the PSU is not outputting voltage. Start with the "
            "obvious: check the rear rocker switch, the cable, and then use a PSU tester "
            "to verify the 24-pin and CPU power connector rails. Only after confirming "
            "the PSU is good should you investigate the motherboard's power path."
        ),
    },
    {
        "id": "a1d5v2-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "After installing a second identical 16 GB DDR5 DIMM to double system RAM, "
            "a workstation now only recognizes 16 GB instead of 32 GB, and only one "
            "DIMM slot's LED is lit on the motherboard. The motherboard manual shows "
            "a four-slot configuration. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The new DIMM is in a non-paired slot; DDR5 requires DIMMs to be installed in the correct channel-pairing slots for dual-channel operation",
                "correct": True,
                "rationale": (
                    "Correct. Modern motherboards require DIMMs to be installed in "
                    "specific paired slots for dual-channel operation and often for "
                    "simple recognition. Installing the second DIMM in an adjacent "
                    "(non-paired) slot rather than the matching channel slot (e.g., A1 "
                    "and B1 instead of A1 and A2) commonly results in only one module "
                    "being recognized."
                ),
            },
            {
                "id": "b",
                "text": "The new DIMM has a different latency (CL) rating and the XMP profile must be enabled",
                "correct": False,
                "rationale": (
                    "Incorrect. Latency differences cause the slower-rated profile to "
                    "be used but do not cause a DIMM to go completely unrecognized. "
                    "The module would still appear in the BIOS even at base speed."
                ),
            },
            {
                "id": "c",
                "text": "The BIOS needs to be updated to support 32 GB total RAM",
                "correct": False,
                "rationale": (
                    "Incorrect. While BIOS updates can expand memory support, if the "
                    "BIOS already recognized 16 GB (one DIMM), it almost certainly "
                    "supports the same DIMM in a second slot. Slot placement is more "
                    "likely the issue."
                ),
            },
            {
                "id": "d",
                "text": "The new DIMM is defective and must be replaced",
                "correct": False,
                "rationale": (
                    "Incorrect. Before concluding a DIMM is defective, verify it is "
                    "seated in the correct slot. A DIMM in the wrong slot is a very "
                    "common installation error that mimics a defective module."
                ),
            },
        ],
        "explanation": (
            "DDR4 and DDR5 motherboards pair slots for dual-channel operation using a "
            "color-coded scheme (e.g., A1+B1 or slots 2+4 in many four-DIMM boards). "
            "Installing the second DIMM in the wrong slot (e.g., A1+A2 instead of A1+B1) "
            "can result in the module going undetected or the system reverting to "
            "single-channel mode. Always consult the motherboard manual for the correct "
            "installation order."
        ),
    },
    {
        "id": "a1d5v2-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A user reports their PC produces a single short beep at startup (normal "
            "POST) but then freezes at the Windows loading screen every morning for the "
            "first minute, after which it resumes normally. No BSOD occurs. Temperatures "
            "are within normal range. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A failing hard drive with bad sectors that slow the disk read during early boot",
                "correct": True,
                "rationale": (
                    "Correct. A hard drive with developing bad sectors can cause the "
                    "OS loader or early boot files to take an abnormally long time to "
                    "read as the drive retries sectors. This produces a temporary freeze "
                    "that clears once the file is finally read. The S.M.A.R.T. data "
                    "would likely show pending or reallocated sectors."
                ),
            },
            {
                "id": "b",
                "text": "The CMOS battery is dead, causing the BIOS to re-initialize settings each boot",
                "correct": False,
                "rationale": (
                    "Incorrect. A dead CMOS battery causes date/time resets and may add "
                    "a BIOS setup prompt, but does not cause a freeze at the Windows "
                    "loading screen that resolves on its own."
                ),
            },
            {
                "id": "c",
                "text": "A Windows startup application is consuming CPU time, delaying the boot",
                "correct": False,
                "rationale": (
                    "Incorrect. A misbehaving startup application would freeze after "
                    "the Windows desktop loads, not at the Windows loading screen before "
                    "login. The freeze at the loading screen is pre-logon and points to "
                    "storage I/O issues."
                ),
            },
            {
                "id": "d",
                "text": "RAM is overheating during the cold-boot initialization phase",
                "correct": False,
                "rationale": (
                    "Incorrect. RAM overheating causes failures after the system has "
                    "been running for a sustained period, not during a cold boot. "
                    "Also, temperatures are reported as normal."
                ),
            },
        ],
        "explanation": (
            "A transient freeze at the Windows loading screen (before login) that "
            "resolves after a delay is a classic early sign of hard drive deterioration. "
            "Sectors containing boot-critical files are retried multiple times before "
            "being read successfully. Run chkdsk /r and review S.M.A.R.T. attributes "
            "(pending sectors, reallocated sectors). Back up data and replace the drive."
        ),
    },
    {
        "id": "a1d5v2-008",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "An ATX desktop spontaneously powers on a few seconds after being shut down "
            "by the operating system. No scheduled wake events are configured. What "
            "setting is MOST likely responsible?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wake-on-LAN (WoL) is enabled in the BIOS and a magic packet is being received",
                "correct": True,
                "rationale": (
                    "Correct. Wake-on-LAN keeps the network interface powered when the "
                    "system is off (on standby power). If a magic packet (broadcast to "
                    "the NIC's MAC) is received — from a network scanner, management "
                    "tool, or misconfigured device — the system powers on. Disabling WoL "
                    "in BIOS or network adapter settings prevents this."
                ),
            },
            {
                "id": "b",
                "text": "The CMOS battery has failed, causing the RTC alarm to trigger a spurious wake event",
                "correct": False,
                "rationale": (
                    "Incorrect. A dead CMOS battery causes loss of date/time and BIOS "
                    "settings but does not typically cause spontaneous power-on events. "
                    "RTC alarms are a configured BIOS setting, not a side effect of a "
                    "dead battery."
                ),
            },
            {
                "id": "c",
                "text": "The front-panel power button is stuck and sending a continuous power signal",
                "correct": False,
                "rationale": (
                    "Incorrect. A stuck power button would prevent clean shutdown in the "
                    "first place. The system shuts down normally before spontaneously "
                    "powering on, which rules out a mechanical button fault."
                ),
            },
            {
                "id": "d",
                "text": "The PSU is providing excess 5 V standby power, triggering the ATX power-on signal",
                "correct": False,
                "rationale": (
                    "Incorrect. Excess standby voltage would cause hardware damage and "
                    "is not a normal failure mode. Wake-on-LAN is a far more common and "
                    "expected cause of spontaneous power-on after a clean shutdown."
                ),
            },
        ],
        "explanation": (
            "ATX motherboards remain on 5 V standby (VSB) power when the system is "
            "shut down. Wake-on-LAN uses this standby power to keep the NIC active. "
            "A magic packet received by the NIC asserts the PS_ON signal, powering "
            "the system on. Other wake events (USB wake, PCIe wake, RTC alarm) can "
            "also trigger spurious power-on. Check BIOS Power Management settings "
            "and the Windows Device Manager NIC power management tab."
        ),
    },
    {
        "id": "a1d5v2-009",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A technician is troubleshooting a server that intermittently produces "
            "ECC memory error log entries but no crashes. A single DIMM in slot B2 "
            "shows a steadily increasing correctable error count. The other seven "
            "DIMMs show zero errors. What is the BEST action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Replace the DIMM in slot B2; a rising correctable error count indicates degrading cells that will eventually become uncorrectable",
                "correct": True,
                "rationale": (
                    "Correct. ECC (Error-Correcting Code) RAM can correct single-bit "
                    "errors in real time, preventing crashes. However, a steadily rising "
                    "correctable error count on one specific DIMM signals that its cells "
                    "are degrading. Before errors become uncorrectable (causing data "
                    "corruption), the DIMM should be replaced proactively."
                ),
            },
            {
                "id": "b",
                "text": "Ignore the errors — ECC is designed to handle them indefinitely",
                "correct": False,
                "rationale": (
                    "Incorrect. ECC corrects errors in the short term, but a rising "
                    "error count means the DIMM is failing. Eventually errors will "
                    "become multi-bit (uncorrectable), causing data corruption or "
                    "crashes. Proactive replacement is required."
                ),
            },
            {
                "id": "c",
                "text": "Reseat all eight DIMMs to re-establish contact and reset the error counters",
                "correct": False,
                "rationale": (
                    "Incorrect. While poor contact can cause errors, a rising error "
                    "count localized to a single DIMM is more consistent with cell "
                    "degradation than seating issues. Reseating may temporarily reduce "
                    "errors but does not address a degrading module."
                ),
            },
            {
                "id": "d",
                "text": "Update the BIOS firmware to improve ECC error tolerance thresholds",
                "correct": False,
                "rationale": (
                    "Incorrect. BIOS/firmware updates cannot repair degrading DRAM "
                    "cells. Adjusting thresholds would simply delay the alert without "
                    "fixing the underlying hardware problem."
                ),
            },
        ],
        "explanation": (
            "ECC RAM adds extra bits per data word to detect and correct single-bit "
            "errors in flight. A single DIMM with a monotonically increasing correctable "
            "error count — while all others show zero — clearly identifies a degrading "
            "module, not an environmental or systemic issue. Replace the module before "
            "the error rate escalates to multi-bit (UECC) events, which ECC cannot "
            "correct and which cause crashes or silent data corruption."
        ),
    },
    # ── 5.3 Storage & RAID ────────────────────────────────────────────────────
    {
        "id": "a1d5v2-010",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A RAID 1 mirror array with two drives loses one drive. The administrator "
            "replaces the failed drive with an identical model. What happens next and "
            "what must the administrator do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The array initiates a rebuild, copying all data from the surviving drive to the new drive; monitor the rebuild to completion",
                "correct": True,
                "rationale": (
                    "Correct. RAID 1 (mirroring) can tolerate a single drive failure. "
                    "When a replacement drive is installed, the RAID controller begins "
                    "a rebuild by copying the complete dataset from the surviving drive "
                    "to the new drive. The administrator should monitor the process and "
                    "avoid another failure during the rebuild, when the array is "
                    "vulnerable."
                ),
            },
            {
                "id": "b",
                "text": "The array cannot recover; restore all data from backup to the two new drives",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 1 is specifically designed to survive one drive "
                    "failure. The surviving drive holds a complete copy of the data and "
                    "can be used as the source for a rebuild."
                ),
            },
            {
                "id": "c",
                "text": "The new drive is automatically formatted and RAID 1 parity is rebuilt from scratch",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 1 does not use parity — it uses mirroring. The "
                    "rebuild copies the full disk contents from the healthy drive to the "
                    "new drive; no parity calculation is involved."
                ),
            },
            {
                "id": "d",
                "text": "The system boots from the new drive and rebuilds the old surviving drive in the background",
                "correct": False,
                "rationale": (
                    "Incorrect. The new (blank) drive receives data from the surviving "
                    "drive, not the other way around. The surviving drive is the source; "
                    "the replacement drive is the destination."
                ),
            },
        ],
        "explanation": (
            "RAID 1 tolerates one drive failure because both drives contain identical "
            "data. On replacement drive insertion, the controller begins a 'resync' or "
            "'rebuild,' writing every block from the healthy drive to the new drive. "
            "During the rebuild, the array is degraded (no fault tolerance). If the "
            "healthy drive fails during the rebuild, data is lost — so backup before "
            "and careful monitoring are essential."
        ),
    },
    {
        "id": "a1d5v2-011",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A storage administrator notices that sequential write performance on a "
            "RAID 5 array with five 7,200-RPM drives has dropped by 40% after adding "
            "a large number of small random write I/Os from a new database application. "
            "No drives have failed. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RAID 5 write penalty — each small random write requires four I/O operations (read-modify-write parity), saturating the drives",
                "correct": True,
                "rationale": (
                    "Correct. RAID 5 has a write penalty: every write requires two reads "
                    "(old data + old parity) and two writes (new data + new parity). For "
                    "small random writes this four-I/O penalty greatly amplifies the "
                    "workload, reducing effective throughput for all I/O on the array, "
                    "including sequential writes."
                ),
            },
            {
                "id": "b",
                "text": "The RAID controller battery-backed cache has failed, disabling write caching",
                "correct": False,
                "rationale": (
                    "Incorrect. A failed BBU (battery-backed unit) would force write-"
                    "through mode instead of write-back, which reduces performance. "
                    "However, the question specifies no hardware failures, and the write "
                    "penalty is the more fundamental explanation for the pattern described."
                ),
            },
            {
                "id": "c",
                "text": "Drive fragmentation has increased seek times on all five spindles",
                "correct": False,
                "rationale": (
                    "Incorrect. Fragmentation affects HDDs over time but would cause "
                    "gradual degradation, not a sudden 40% drop correlated with the "
                    "introduction of a specific random-write workload."
                ),
            },
            {
                "id": "d",
                "text": "The new database application is using NTFS compression, increasing I/O overhead",
                "correct": False,
                "rationale": (
                    "Incorrect. NTFS compression adds CPU and I/O overhead but would "
                    "not explain a 40% drop in sequential writes correlated with "
                    "random-write workload from RAID's own write-amplification mechanics."
                ),
            },
        ],
        "explanation": (
            "RAID 5 write penalty: for each logical write, the controller reads the "
            "old data block and old parity block, computes new parity, and writes both "
            "the new data and new parity — four physical I/Os per logical write. Under "
            "heavy random-write workloads this amplification consumes drive bandwidth "
            "and hurts sequential throughput. Solutions include RAID 6 with a write-"
            "back cache, RAID 10, or an all-flash array that mitigates the penalty."
        ),
    },
    {
        "id": "a1d5v2-012",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A Windows PC cannot boot after a power outage. The BIOS correctly detects "
            "the NVMe SSD. The boot error reads: 'Reboot and Select proper Boot device.' "
            "chkdsk run from the Windows recovery environment shows no file system "
            "errors. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The Master Boot Record (MBR) or UEFI boot partition data was corrupted by the unclean shutdown",
                "correct": True,
                "rationale": (
                    "Correct. A clean file system (no errors from chkdsk) but a 'no boot "
                    "device' error indicates the boot-sector or partition metadata is "
                    "corrupt. On MBR disks the MBR itself or the boot sector may be "
                    "damaged; on GPT/UEFI systems the EFI System Partition (ESP) or BCD "
                    "store may be corrupt. The OS recovery tools (bootrec /fixmbr, "
                    "bootrec /rebuildbcd, bcdboot) can repair this."
                ),
            },
            {
                "id": "b",
                "text": "The NVMe drive's firmware crashed and must be reflashed",
                "correct": False,
                "rationale": (
                    "Incorrect. The BIOS detects the drive and the file system passes "
                    "chkdsk, which means the drive is functional. A firmware crash would "
                    "prevent detection entirely."
                ),
            },
            {
                "id": "c",
                "text": "The SATA controller was set to IDE mode during the outage and must be switched to AHCI",
                "correct": False,
                "rationale": (
                    "Incorrect. NVMe drives do not use SATA or AHCI; they connect over "
                    "PCIe. The IDE/AHCI setting is irrelevant for an NVMe device."
                ),
            },
            {
                "id": "d",
                "text": "Windows Update installed a bad driver during shutdown that is preventing boot",
                "correct": False,
                "rationale": (
                    "Incorrect. A bad driver would produce a BSOD during Windows "
                    "startup, not a 'no boot device' error before the OS loader runs. "
                    "The boot error occurs below the OS level."
                ),
            },
        ],
        "explanation": (
            "A 'no boot device' error with a healthy, detected disk and a clean file "
            "system points to corrupt boot metadata. On UEFI/GPT systems, use the "
            "Windows Recovery Environment: 'bootrec /rebuildbcd' and 'bcdboot c:\\windows'. "
            "On legacy MBR systems: 'bootrec /fixmbr' and 'bootrec /fixboot'. Power "
            "outages during a write cycle can corrupt the boot sector even when the "
            "file system survives intact."
        ),
    },
    {
        "id": "a1d5v2-013",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "An administrator configures four identical 4 TB drives into a RAID 10 "
            "array. What is the usable storage capacity and the maximum number of "
            "simultaneous drive failures the array can survive without data loss?"
        ),
        "options": [
            {
                "id": "a",
                "text": "8 TB usable; can survive up to two drive failures as long as they are not both from the same mirrored pair",
                "correct": True,
                "rationale": (
                    "Correct. RAID 10 (1+0) stripes across mirrored pairs. With four "
                    "4 TB drives, two mirrors of 4 TB each are created, then striped — "
                    "yielding 8 TB usable (50% overhead). The array survives two drive "
                    "failures provided each failure is in a different mirror pair. If "
                    "both drives in the same pair fail, the array is lost."
                ),
            },
            {
                "id": "b",
                "text": "12 TB usable; can survive any single drive failure",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 10 uses 50% of raw capacity for mirroring, yielding "
                    "8 TB (not 12 TB) from four 4 TB drives. 12 TB would be RAID 5 "
                    "with one parity drive equivalent."
                ),
            },
            {
                "id": "c",
                "text": "16 TB usable; RAID 10 uses all capacity and has no redundancy",
                "correct": False,
                "rationale": (
                    "Incorrect. 16 TB with no redundancy describes RAID 0 (striping "
                    "only). RAID 10 sacrifices 50% of capacity for redundancy."
                ),
            },
            {
                "id": "d",
                "text": "8 TB usable; can survive only one drive failure regardless of which drive fails",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 10 can survive two drive failures when they are "
                    "from different mirror pairs. It only fails when both drives in "
                    "the same mirror set fail simultaneously."
                ),
            },
        ],
        "explanation": (
            "RAID 10 = mirroring (RAID 1) + striping (RAID 0). With four drives: two "
            "mirrors of 4 TB each, striped together = 8 TB usable (50% overhead). "
            "Fault tolerance: one drive per mirror pair can fail without data loss. "
            "With two mirror pairs, two total drives can fail — but losing both drives "
            "in the same pair destroys the array. RAID 10 combines good performance "
            "with moderate fault tolerance."
        ),
    },
    # ── 5.4 Display & Projector ───────────────────────────────────────────────
    {
        "id": "a1d5v2-014",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A desktop monitor displays a correct image for about 10 seconds after "
            "power-on, then gradually fades to black. Changing the display cable and "
            "connecting to a different PC produces the same result. What is the MOST "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The monitor's backlight is failing — it works briefly while cold but cannot sustain luminance as it warms up",
                "correct": True,
                "rationale": (
                    "Correct. The problem is consistent across two different source "
                    "PCs and cables, isolating the fault to the monitor itself. A "
                    "backlight that starts correctly and then fails as the unit warms "
                    "is a classic sign of a failing CCFL lamp or a failing driver "
                    "circuit for LED backlights."
                ),
            },
            {
                "id": "b",
                "text": "The GPU is overheating and disabling its video output after 10 seconds",
                "correct": False,
                "rationale": (
                    "Incorrect. The same behavior occurs when connected to a different "
                    "PC, ruling out a GPU-specific fault. The monitor is the common "
                    "denominator."
                ),
            },
            {
                "id": "c",
                "text": "The HDMI cable is defective and attenuates the signal after thermal expansion",
                "correct": False,
                "rationale": (
                    "Incorrect. The cable was already replaced and the symptom persists. "
                    "Cable failure is not the cause."
                ),
            },
            {
                "id": "d",
                "text": "The monitor's power management (DPMS) is set to blank the display after 10 seconds of inactivity",
                "correct": False,
                "rationale": (
                    "Incorrect. DPMS blanking occurs when no input signal is detected "
                    "or after an idle timeout, not 10 seconds after power-on while "
                    "content is actively displayed. The gradual fade is also inconsistent "
                    "with an abrupt DPMS sleep transition."
                ),
            },
        ],
        "explanation": (
            "When a monitor shows a correct image and then progressively fades to "
            "black after a fixed warm-up time, the backlight (or its driver/inverter) "
            "is failing. CCFL lamps can exhibit cold-start behavior — they produce "
            "light briefly when cool but fail once a certain temperature is reached. "
            "LED backlights can behave similarly if a driver IC is failing. Since the "
            "fault is reproducible across multiple sources, the monitor needs repair "
            "or replacement."
        ),
    },
    {
        "id": "a1d5v2-015",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A user complains their monitor shows flickering lines and the image "
            "occasionally tears or scrolls horizontally. The problem occurs with two "
            "different video cables. Connecting the monitor to a different PC produces "
            "the same symptoms. What is the MOST likely faulty component?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The monitor's internal electronics (e.g., failing capacitors on the control board)",
                "correct": True,
                "rationale": (
                    "Correct. The fault is reproduced on two different PCs and with "
                    "two different cables, which conclusively rules out the source "
                    "computer and cables. The common element is the monitor. Failing "
                    "capacitors on the monitor's main board are a very common cause "
                    "of flickering, image tearing, and distortion."
                ),
            },
            {
                "id": "b",
                "text": "The GPU's video memory is failing, corrupting the display signal",
                "correct": False,
                "rationale": (
                    "Incorrect. The symptom occurs with two different PCs, ruling out "
                    "a single GPU. A GPU VRAM fault would only affect one machine."
                ),
            },
            {
                "id": "c",
                "text": "The operating system's display driver is corrupt",
                "correct": False,
                "rationale": (
                    "Incorrect. Testing on a second PC (presumably with a different OS "
                    "installation or driver) still produces the fault. The OS driver is "
                    "not the cause."
                ),
            },
            {
                "id": "d",
                "text": "Electromagnetic interference from nearby equipment is disrupting the video signal",
                "correct": False,
                "rationale": (
                    "Incorrect. EMI severe enough to produce the described symptoms "
                    "would affect both PCs equally and would typically be correlated "
                    "with a specific environmental source that is identifiable. The "
                    "fault follows the monitor, not the environment."
                ),
            },
        ],
        "explanation": (
            "Systematic diagnosis: swap components one at a time. The monitor produces "
            "the same fault with different PCs and cables, making it the definitive "
            "faulty component. Failing electrolytic capacitors on the monitor's power "
            "or logic board are a frequent cause of these symptoms — the capacitors "
            "can bulge or leak, disrupting power supply rails and causing flickering, "
            "tearing, or color distortion."
        ),
    },
    {
        "id": "a1d5v2-016",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Display & projector issues",
        "stem": (
            "A projector displays an image with a large dark circular shadow in the "
            "center of the projected image. The projector is functioning and lamp hours "
            "are within specification. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Dust or debris has accumulated on the projector's optical lens, casting a shadow",
                "correct": True,
                "rationale": (
                    "Correct. Debris (dust, fingerprints, dead insects) on the projection "
                    "lens or optical path creates a visible shadow on the projected image, "
                    "typically darker in the center or in a specific zone corresponding "
                    "to the obstruction's position. Cleaning the lens resolves this."
                ),
            },
            {
                "id": "b",
                "text": "The projector lamp is nearing end of life and producing uneven light distribution",
                "correct": False,
                "rationale": (
                    "Incorrect. A dying lamp causes overall dimness or flickering, not "
                    "a distinct localized dark shadow. The question also states lamp hours "
                    "are within specification."
                ),
            },
            {
                "id": "c",
                "text": "The projection screen has a dark spot where the surface has delaminated",
                "correct": False,
                "rationale": (
                    "Incorrect. A screen defect would cause a localized dark area when "
                    "any projector is aimed at that spot, and could be confirmed by "
                    "projecting onto a different surface. However, a shadow in the image "
                    "that moves with the projector — not with the screen — indicates a "
                    "projector-internal obstruction."
                ),
            },
            {
                "id": "d",
                "text": "The projector's color wheel is cracked, blocking the light path",
                "correct": False,
                "rationale": (
                    "Incorrect. A cracked color wheel (on DLP projectors) typically "
                    "causes color artifacts, complete image loss, or a loud noise — "
                    "not a clean circular shadow in the center of the image."
                ),
            },
        ],
        "explanation": (
            "A localized dark area in a projected image — especially a circular shadow "
            "centered on the image — is the hallmark of a dirty or obstructed lens. "
            "Projector lenses attract dust and may get fingerprints during handling. "
            "Clean the lens using appropriate lens-cleaning tools (blower, lens cloth). "
            "Never touch the lens with bare hands. If the shadow remains after cleaning, "
            "inspect the internal optical path for debris near the light engine."
        ),
    },
    # ── 5.5 Mobile Device Issues ──────────────────────────────────────────────
    {
        "id": "a1d5v2-017",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user reports their iPhone shows a message that the accessory connected "
            "to the Lightning port is not supported. The OEM Lightning cable charges "
            "correctly, but a third-party cable does not charge or sync. What is "
            "the MOST likely explanation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The third-party cable lacks Apple MFi certification; iOS rejects unauthenticated accessories",
                "correct": True,
                "rationale": (
                    "Correct. Apple's Lightning standard requires accessories to include "
                    "an MFi (Made for iPhone/iPad) authentication chip. iOS queries the "
                    "chip; if absent or if authentication fails, the OS displays an "
                    "'accessory not supported' message and blocks charging/data transfer."
                ),
            },
            {
                "id": "b",
                "text": "The Lightning port is dirty; clean it with compressed air",
                "correct": False,
                "rationale": (
                    "Incorrect. A dirty port would affect all cables equally, including "
                    "the OEM cable. Since the OEM cable works, port contamination is "
                    "not the cause."
                ),
            },
            {
                "id": "c",
                "text": "The iOS version is incompatible with the cable's USB specification",
                "correct": False,
                "rationale": (
                    "Incorrect. iOS compatibility issues would affect all cables of that "
                    "USB spec, not just third-party ones. The OEM cable would also fail "
                    "if this were an iOS version issue."
                ),
            },
            {
                "id": "d",
                "text": "The third-party cable uses USB-C internally and requires a USB-C to Lightning adapter",
                "correct": False,
                "rationale": (
                    "Incorrect. The physical connector is Lightning (since the OEM "
                    "Lightning cable works). The issue is authentication, not a connector "
                    "type mismatch."
                ),
            },
        ],
        "explanation": (
            "Apple's MFi (Made for iPhone/iPad/iPod) program requires third-party cable "
            "manufacturers to embed an authentication IC in Lightning accessories. iOS "
            "communicates with this chip; if the chip is absent, counterfeit, or "
            "damaged, the OS rejects the accessory. Only MFi-certified cables pass "
            "this check. USB-C devices use a different (PD/USB-C) standard without "
            "MFi authentication."
        ),
    },
    {
        "id": "a1d5v2-018",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user's Android smartphone has been getting increasingly hot during "
            "normal use even when no demanding applications are running. Battery life "
            "has decreased noticeably over the past week. There are no new app "
            "installations. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A rogue background process or malware is consuming CPU/GPU resources continuously",
                "correct": True,
                "rationale": (
                    "Correct. Abnormal heat during idle use combined with rapid battery "
                    "drain and no recent app installs is the classic presentation of a "
                    "background process (or malware) running constantly. High CPU/GPU "
                    "utilization generates heat and drains the battery quickly. Check "
                    "running processes in Settings > Battery or a system monitor app."
                ),
            },
            {
                "id": "b",
                "text": "The wireless radio is set to maximum transmit power, generating excess heat",
                "correct": False,
                "rationale": (
                    "Incorrect. Wireless radio power contributes modestly to heat but "
                    "would not account for significant temperature increase and battery "
                    "drain in the pattern described, which points to sustained high "
                    "CPU/GPU workload."
                ),
            },
            {
                "id": "c",
                "text": "The battery is swelling internally and the chemical reaction produces heat",
                "correct": False,
                "rationale": (
                    "Incorrect. While a failing battery can generate heat, battery "
                    "swelling typically causes the device to visibly bulge. The combined "
                    "symptoms of both high heat and high battery drain during idle "
                    "activity are more characteristic of a software/malware issue."
                ),
            },
            {
                "id": "d",
                "text": "The phone's thermal throttling has failed, allowing the CPU to run at full speed indefinitely",
                "correct": False,
                "rationale": (
                    "Incorrect. Thermal throttling is a CPU governor feature; its "
                    "failure would cause performance to remain high when hot but would "
                    "not explain why the CPU is running flat-out during normal idle use "
                    "in the first place."
                ),
            },
        ],
        "explanation": (
            "Unexpected heat and rapid battery drain during light use — without new "
            "app installs — is a red flag for malware or a rogue background service. "
            "Check Settings > Battery > Battery Usage to identify the top consumers. "
            "On Android, a system monitor app or ADB shell 'top' command can list CPU "
            "usage by process. If malware is suspected, run a mobile security scan "
            "and consider a factory reset."
        ),
    },
    {
        "id": "a1d5v2-019",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A technician receives a tablet that will not charge and shows no response "
            "when the power button is pressed. The charging cable and adapter test "
            "correctly with another device. After leaving the tablet on the charger for "
            "30 minutes, it still shows no response. What should the technician try NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Perform a hard reset by holding the power button (and volume button if needed) for 10–15 seconds to force the device out of a locked state",
                "correct": True,
                "rationale": (
                    "Correct. A completely unresponsive device with a known-good charger "
                    "may be in a locked or frozen low-power state, not necessarily "
                    "completely dead. A hard reset (forced restart) clears this state "
                    "without affecting user data and is the appropriate next step after "
                    "confirming the charger is functional."
                ),
            },
            {
                "id": "b",
                "text": "Replace the battery immediately, as it is clearly dead and must be swapped",
                "correct": False,
                "rationale": (
                    "Incorrect. Replacing the battery before attempting a hard reset "
                    "is premature. The device may be in a locked state that a hard reset "
                    "can resolve without any hardware replacement."
                ),
            },
            {
                "id": "c",
                "text": "Connect the tablet to a PC via USB and attempt to flash the firmware",
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware flashing is a drastic step and requires the "
                    "device to be partially responsive or in a specific bootloader mode. "
                    "A hard reset is the correct intermediate step before any firmware "
                    "intervention."
                ),
            },
            {
                "id": "d",
                "text": "Declare the device unrepairable, as 30 minutes on a good charger with no response means total hardware failure",
                "correct": False,
                "rationale": (
                    "Incorrect. A device that has deeply discharged may take longer than "
                    "30 minutes to accumulate enough charge to power on. A forced restart "
                    "attempt and extended charge time are both warranted before declaring "
                    "the device a total failure."
                ),
            },
        ],
        "explanation": (
            "Tablets and phones that are completely unresponsive but have a good charger "
            "may be in a hard-locked or deep-discharge state. The correct sequence: "
            "1) Attempt a hard reset (hold power ± volume for 10–15 s); 2) Allow "
            "extended charge time (1+ hour) before power-on attempt; 3) Try a different "
            "wall outlet. Only after these steps fail is hardware replacement warranted."
        ),
    },
    {
        "id": "a1d5v2-020",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Mobile device issues",
        "stem": (
            "A user reports that their smartphone's GPS location is wildly inaccurate "
            "when outdoors but works reasonably well indoors using Wi-Fi location. "
            "The device has a clear view of the sky and location permissions are granted "
            "to the app. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The device's GPS antenna or receiver hardware is defective",
                "correct": True,
                "rationale": (
                    "Correct. GPS accuracy depends on receiving satellite signals via "
                    "the device's GPS antenna. Wi-Fi-based location (using nearby AP "
                    "positions) works because it doesn't use the GPS hardware. If GPS "
                    "is wildly inaccurate outdoors despite a clear sky and correct "
                    "permissions, the GPS antenna or receiver chip is the most likely "
                    "hardware fault."
                ),
            },
            {
                "id": "b",
                "text": "High Accuracy mode is disabled; enabling it will fix GPS accuracy",
                "correct": False,
                "rationale": (
                    "Incorrect. High Accuracy mode uses GPS + Wi-Fi + cellular together. "
                    "If GPS is defective, enabling High Accuracy mode will still fail "
                    "to improve GPS-derived accuracy — only the non-GPS components will "
                    "help, which matches the symptom of working indoors but not outdoors."
                ),
            },
            {
                "id": "c",
                "text": "The app has a software bug causing coordinate parsing errors",
                "correct": False,
                "rationale": (
                    "Incorrect. A software bug in one app would be an app-specific "
                    "issue. The question implies the GPS system itself is inaccurate, "
                    "which would affect all GPS-using apps."
                ),
            },
            {
                "id": "d",
                "text": "The cellular carrier is providing incorrect Assisted GPS (A-GPS) data",
                "correct": False,
                "rationale": (
                    "Incorrect. A-GPS data from the carrier provides almanac and "
                    "ephemeris data to speed up satellite acquisition; errors in this "
                    "data would cause slow first-fix times, not consistently inaccurate "
                    "positions once acquired."
                ),
            },
        ],
        "explanation": (
            "GPS location relies on the device's dedicated GPS receiver picking up "
            "satellite signals. Wi-Fi location uses a database of AP MAC addresses and "
            "their known positions — no GPS hardware required. A device that works with "
            "Wi-Fi location but fails GPS outdoors (with permissions granted and a clear "
            "sky) has a GPS hardware failure. Diagnosis: test with a pure GPS app, "
            "compare with another device at the same location."
        ),
    },
    # ── 5.6 Printer Troubleshooting ───────────────────────────────────────────
    {
        "id": "a1d5v2-021",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "An inkjet printer is producing output with horizontal white bands (gaps) "
            "across every printed page, and the gaps correspond to missing nozzle rows. "
            "A nozzle check print confirms several nozzle segments are not firing. "
            "What is the BEST first corrective action?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run the printer's built-in print head cleaning cycle to clear clogged nozzles",
                "correct": True,
                "rationale": (
                    "Correct. Inkjet print head clogs are the leading cause of missing "
                    "lines or banding. The manufacturer's cleaning cycle forces ink "
                    "through the nozzles to dissolve dried ink. Multiple cycles may be "
                    "needed. If cleaning fails, a manual soak (print head removed and "
                    "soaked in warm distilled water) or replacement is the next step."
                ),
            },
            {
                "id": "b",
                "text": "Replace the ink cartridges with new ones, as the clogging is caused by low ink",
                "correct": False,
                "rationale": (
                    "Incorrect. Low ink can cause lighter output but typically affects "
                    "all nozzles proportionally, not specific segments. Clogged nozzles "
                    "require cleaning, not a new cartridge (though a fresh cartridge "
                    "can help after cleaning if ink is also low)."
                ),
            },
            {
                "id": "c",
                "text": "Adjust the print resolution to a lower DPI setting to avoid stressing the nozzles",
                "correct": False,
                "rationale": (
                    "Incorrect. Lowering DPI will not unclog blocked nozzles; it will "
                    "simply reduce print quality across all remaining functional nozzles."
                ),
            },
            {
                "id": "d",
                "text": "Update the printer firmware to reassign the image to non-clogged nozzle rows",
                "correct": False,
                "rationale": (
                    "Incorrect. Firmware does not dynamically remap image data around "
                    "physically blocked nozzles. The nozzles must be physically cleaned "
                    "or the print head replaced."
                ),
            },
        ],
        "explanation": (
            "Inkjet banding with missing horizontal rows is caused by clogged nozzles, "
            "usually from dried ink when the printer is idle for extended periods. The "
            "standard fix is the built-in head cleaning utility (accessible from the "
            "printer software or front panel). Run 2–3 cycles and print a nozzle test "
            "pattern after each. If nozzles remain blocked, try a print head soak. "
            "Persistent clogs require print head replacement."
        ),
    },
    {
        "id": "a1d5v2-022",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A thermal receipt printer in a retail environment is producing blank receipts "
            "even though the printer shows 'Ready' and the paper feeds correctly. "
            "A technician scratches the surface of the paper with a fingernail and "
            "notices no mark appears. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The paper roll is loaded thermal-coating side out (facing away from the print head)",
                "correct": True,
                "rationale": (
                    "Correct. Thermal paper has a heat-sensitive coating on only one "
                    "side. If the roll is loaded backward (coating facing inward, away "
                    "from the thermal print head), the print head heats the uncoated "
                    "side and no marks appear. Scratching the coated side with a "
                    "fingernail leaves a dark mark; scratching the plain side does not."
                ),
            },
            {
                "id": "b",
                "text": "The thermal print head is burned out and no longer generating heat",
                "correct": False,
                "rationale": (
                    "Incorrect. If the print head were burned out, scratching the "
                    "thermal paper (the correct coated side) with a fingernail would "
                    "still produce a mark from the physical pressure/friction. The "
                    "scratch test on the paper itself showed no mark, indicating the "
                    "wrong side of the paper is facing the head."
                ),
            },
            {
                "id": "c",
                "text": "The printer driver is sending blank data due to a print queue corruption",
                "correct": False,
                "rationale": (
                    "Incorrect. A software issue would show as garbled or missing "
                    "content in otherwise printed output. The thermal paper scratch "
                    "test indicating no reactive surface is a definitive hardware/media "
                    "clue that points to paper orientation."
                ),
            },
            {
                "id": "d",
                "text": "The paper is incompatible thermal stock with a different activation temperature",
                "correct": False,
                "rationale": (
                    "Incorrect. While incompatible thermal paper can cause light printing, "
                    "the scratch test producing no mark at all confirms the surface being "
                    "presented to the head is not the thermal coating — i.e., the paper "
                    "is loaded backward."
                ),
            },
        ],
        "explanation": (
            "Thermal printers print by applying heat to heat-sensitive paper. The "
            "coating is only on one side. A quick diagnostic: scratch the paper surface "
            "firmly with a fingernail — the coated side will show a dark gray mark from "
            "friction-generated heat; the plain side will not. If the loaded surface "
            "shows no mark, reload the paper with the coated side facing the print head. "
            "Most rolls feed with the coated side facing outward (away from the roll)."
        ),
    },
    {
        "id": "a1d5v2-023",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "Users report that the network laser printer shows 'Paper Jam' but there is "
            "no visible paper in the paper path. The technician opens all access panels, "
            "confirms the path is clear, closes the covers, and the error persists. "
            "What should the technician check NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Check all paper sensors and rollers for a small torn piece of paper that may not be visible at a glance",
                "correct": True,
                "rationale": (
                    "Correct. A small torn fragment (often a corner) can lodge against "
                    "a paper sensor or between rollers and remain invisible unless "
                    "specifically searched for with a flashlight. The sensor remains "
                    "triggered, causing a persistent jam error even though no full "
                    "sheet is visible."
                ),
            },
            {
                "id": "b",
                "text": "Reinstall the printer driver on the print server to clear the jam error code",
                "correct": False,
                "rationale": (
                    "Incorrect. The jam error is generated by a hardware paper sensor "
                    "on the printer itself, not by the driver. A driver reinstall cannot "
                    "clear a sensor-triggered fault."
                ),
            },
            {
                "id": "c",
                "text": "Replace the fuser assembly, which is detecting paper that has melted onto the roller",
                "correct": False,
                "rationale": (
                    "Incorrect. While a jammed piece of paper on the fuser roller is "
                    "possible, the technician should first fully inspect for paper "
                    "fragments before replacing the fuser, which is an expensive "
                    "component."
                ),
            },
            {
                "id": "d",
                "text": "Upgrade the printer firmware to fix a false jam detection bug",
                "correct": False,
                "rationale": (
                    "Incorrect. A firmware bug causing false jam errors is possible but "
                    "highly unlikely compared to a physical paper fragment. Physical "
                    "inspection must be exhausted before considering firmware."
                ),
            },
        ],
        "explanation": (
            "Persistent 'paper jam' errors with no visible paper are almost always "
            "caused by a small torn fragment lodged at a paper sensor or in the paper "
            "path. Use a flashlight to carefully inspect every inch of the paper path, "
            "including the fuser input and output rollers, the transfer roller area, "
            "and the exit assembly. Remove any fragments with tweezers. Never pull "
            "a fragment toward you against the paper path direction."
        ),
    },
    {
        "id": "a1d5v2-024",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A laser printer that was recently relocated to a new office is printing "
            "with an overall gray background on every page instead of clean white "
            "areas. The drum has been recently replaced. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The primary charge roller (PCR) or charging corona wire is contaminated, preventing the drum from being uniformly charged",
                "correct": True,
                "rationale": (
                    "Correct. The primary charge roller uniformly charges the drum "
                    "surface to a high negative voltage before the laser writes the "
                    "image. If the PCR is dirty or failing, the drum is not uniformly "
                    "charged; the developer deposits toner in areas that should be clean, "
                    "producing a gray background (also called 'fogging')."
                ),
            },
            {
                "id": "b",
                "text": "The toner cartridge is overfilled and toner is spilling into the paper path",
                "correct": False,
                "rationale": (
                    "Incorrect. Toner overfill would cause thick smears or blotches, "
                    "not a uniform gray background across the entire white area. The "
                    "fogging pattern specifically indicates a charging problem."
                ),
            },
            {
                "id": "c",
                "text": "The fuser temperature is too low, causing unfused toner to spread across the page",
                "correct": False,
                "rationale": (
                    "Incorrect. Low fuser temperature causes smearing (toner that wipes "
                    "off), not a gray background on white areas. The toner must reach "
                    "the drum incorrectly for fogging to occur."
                ),
            },
            {
                "id": "d",
                "text": "The paper tray is loaded with recycled paper that has residual toner from a previous use",
                "correct": False,
                "rationale": (
                    "Incorrect. While recycled paper can cause quality issues, the "
                    "systematic gray background on all pages is more consistent with "
                    "a printing process component failure than a paper media issue, "
                    "especially given the recent relocation."
                ),
            },
        ],
        "explanation": (
            "Foggy or gray background on laser printer output (toner in non-image areas) "
            "is caused by insufficient drum charging. The PCR (or corona wire) must "
            "charge the drum to ~-600 V; if contaminated, the voltage is too low, "
            "developer toner (which is attracted to areas of lower voltage) adheres "
            "to the background. Clean the PCR (if user-accessible) or replace the "
            "toner cartridge which often includes the PCR. Also check that the drum "
            "was not exposed to light during the relocation."
        ),
    },
    # ── 5.7 Network Troubleshooting ───────────────────────────────────────────
    {
        "id": "a1d5v2-025",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician suspects a workstation's ARP cache has a stale entry mapping "
            "the default gateway IP to an incorrect MAC address, causing intermittent "
            "connectivity loss. Which Windows command displays the current ARP cache "
            "so the technician can verify the gateway's MAC?"
        ),
        "options": [
            {
                "id": "a",
                "text": "arp -a",
                "correct": True,
                "rationale": (
                    "Correct. 'arp -a' (or 'arp -g') displays the current ARP (Address "
                    "Resolution Protocol) cache, which maps IP addresses to MAC "
                    "(hardware) addresses. The technician can compare the gateway's "
                    "listed MAC against the known gateway MAC to identify stale or "
                    "poisoned entries."
                ),
            },
            {
                "id": "b",
                "text": "ipconfig /all",
                "correct": False,
                "rationale": (
                    "Incorrect. ipconfig /all shows the local adapter's IP configuration "
                    "(IP, mask, gateway IP, DNS), but does not display the ARP cache or "
                    "the MAC addresses of other devices on the network."
                ),
            },
            {
                "id": "c",
                "text": "netstat -r",
                "correct": False,
                "rationale": (
                    "Incorrect. 'netstat -r' displays the IP routing table (network "
                    "destinations, gateway IPs, and metrics), not the ARP cache "
                    "containing IP-to-MAC mappings."
                ),
            },
            {
                "id": "d",
                "text": "nslookup <gateway_IP>",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup performs DNS lookups, resolving names to IPs "
                    "or IPs to names. It does not query or display ARP cache contents."
                ),
            },
        ],
        "explanation": (
            "The ARP cache holds recent IP-to-MAC address mappings. 'arp -a' lists all "
            "entries. A stale entry (wrong MAC for the gateway IP) can cause outbound "
            "frames to go to the wrong host. To delete a stale entry: 'arp -d <IP>'. "
            "ARP cache poisoning (a security attack) also presents as incorrect MAC "
            "mappings and is diagnosed the same way."
        ),
    },
    {
        "id": "a1d5v2-026",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician needs to release the current DHCP lease on a Windows "
            "workstation and obtain a completely new IP address assignment. Which "
            "sequence of commands should be used?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ipconfig /release followed by ipconfig /renew",
                "correct": True,
                "rationale": (
                    "Correct. 'ipconfig /release' sends a DHCP Release message, "
                    "relinquishing the current lease and removing the IP address. "
                    "'ipconfig /renew' then sends a DHCP Discover, going through the "
                    "full DORA process (Discover, Offer, Request, Acknowledge) to obtain "
                    "a new lease."
                ),
            },
            {
                "id": "b",
                "text": "ipconfig /flushdns followed by ipconfig /registerdns",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ipconfig /flushdns' clears the DNS resolver cache; "
                    "'ipconfig /registerdns' re-registers the workstation's DNS records "
                    "with the DNS server. Neither command affects the DHCP lease or "
                    "the IP address assignment."
                ),
            },
            {
                "id": "c",
                "text": "netsh interface ip set address dhcp",
                "correct": False,
                "rationale": (
                    "Incorrect. While this netsh command can set an adapter to use DHCP, "
                    "it does not initiate a release of the current lease before requesting "
                    "a new one, making it less reliable for forcing a lease renewal. "
                    "The ipconfig /release + /renew sequence is the standard procedure."
                ),
            },
            {
                "id": "d",
                "text": "ipconfig /all followed by ping 0.0.0.0",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ipconfig /all' displays configuration; 'ping 0.0.0.0' "
                    "tests the loopback but neither command releases or renews a DHCP "
                    "lease."
                ),
            },
        ],
        "explanation": (
            "DHCP lease management from the Windows command line: "
            "'ipconfig /release' – sends DHCPRELEASE to the server and clears the IP. "
            "'ipconfig /renew' – initiates DORA to get a new lease. Use '/release6' "
            "and '/renew6' for IPv6 (DHCPv6) addresses. These commands are fundamental "
            "for troubleshooting DHCP conflicts, APIPA addresses, and stale lease issues."
        ),
    },
    {
        "id": "a1d5v2-027",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network command-line tools",
        "stem": (
            "A Linux administrator needs to display all listening TCP and UDP ports "
            "along with the owning process name on a Linux server. Which command "
            "is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "ss -tulnp",
                "correct": True,
                "rationale": (
                    "Correct. 'ss' (socket statistics) is the modern Linux replacement "
                    "for netstat. The flags: -t (TCP), -u (UDP), -l (listening only), "
                    "-n (numeric ports), -p (show process name/PID). This gives a "
                    "complete view of all listening services and their owning processes."
                ),
            },
            {
                "id": "b",
                "text": "traceroute localhost",
                "correct": False,
                "rationale": (
                    "Incorrect. traceroute tests the network path to a destination "
                    "(loopback in this case). It does not display listening ports or "
                    "process information."
                ),
            },
            {
                "id": "c",
                "text": "ping -c 4 127.0.0.1",
                "correct": False,
                "rationale": (
                    "Incorrect. ping tests connectivity to the loopback interface but "
                    "does not enumerate listening ports or running processes."
                ),
            },
            {
                "id": "d",
                "text": "ifconfig -a",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ifconfig -a' displays network interface configuration "
                    "(IP addresses, MAC addresses, statistics) but does not list "
                    "listening ports or process information."
                ),
            },
        ],
        "explanation": (
            "'ss -tulnp' is the preferred modern command for listing listening sockets "
            "on Linux: -t = TCP, -u = UDP, -l = listening, -n = don't resolve service "
            "names (show port numbers), -p = show process. The legacy equivalent is "
            "'netstat -tulnp'. On systems where netstat is unavailable (deprecated "
            "on modern distributions), ss is the replacement."
        ),
    },
    {
        "id": "a1d5v2-028",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A newly installed network switch has two ports connected to the same "
            "upstream switch, creating an unintentional loop. The network becomes "
            "saturated with broadcast traffic within seconds and all devices lose "
            "connectivity. What protocol should have been enabled on the switches to "
            "prevent this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Spanning Tree Protocol (STP) or Rapid Spanning Tree Protocol (RSTP)",
                "correct": True,
                "rationale": (
                    "Correct. STP/RSTP prevents Layer 2 broadcast storms by detecting "
                    "loops and logically blocking redundant ports, ensuring only one "
                    "active path exists between any two network segments. Without STP, "
                    "a loop causes a broadcast storm where broadcast frames circulate "
                    "endlessly, saturating all bandwidth."
                ),
            },
            {
                "id": "b",
                "text": "Dynamic Host Configuration Protocol (DHCP) snooping",
                "correct": False,
                "rationale": (
                    "Incorrect. DHCP snooping filters unauthorized DHCP server responses "
                    "but has no mechanism to prevent Layer 2 loops or broadcast storms."
                ),
            },
            {
                "id": "c",
                "text": "Quality of Service (QoS) traffic shaping",
                "correct": False,
                "rationale": (
                    "Incorrect. QoS prioritizes traffic types but cannot prevent or "
                    "break a physical Layer 2 loop that is flooding the network with "
                    "broadcast frames."
                ),
            },
            {
                "id": "d",
                "text": "Network Address Translation (NAT)",
                "correct": False,
                "rationale": (
                    "Incorrect. NAT translates private IP addresses to public IPs for "
                    "routing; it operates at Layer 3 and cannot prevent or detect a "
                    "Layer 2 switching loop."
                ),
            },
        ],
        "explanation": (
            "A broadcast storm caused by a Layer 2 loop occurs when switches flood "
            "broadcast frames endlessly because there is no TTL at Layer 2. "
            "STP (IEEE 802.1D) and RSTP (IEEE 802.1W) prevent this by electing a "
            "root bridge, computing shortest paths, and blocking redundant links. "
            "RSTP converges much faster than classic STP (sub-second vs. 30-50 seconds). "
            "Most managed switches enable STP by default; always verify it is active."
        ),
    },
    {
        "id": "a1d5v2-029",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A workstation receives an IP address in the 169.254.x.x range after "
            "connecting to the network. The DHCP server is confirmed to be running "
            "and has available leases. Other workstations on the same subnet receive "
            "correct addresses. Which Windows service must be verified and restarted "
            "on the affected workstation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "DHCP Client service (Dhcp)",
                "correct": True,
                "rationale": (
                    "Correct. The 169.254.x.x APIPA address indicates the workstation "
                    "sent a DHCP Discover but received no response — or the DHCP Client "
                    "Windows service is stopped/disabled. Since the DHCP server is "
                    "working for other clients, the local DHCP Client service on this "
                    "workstation must be verified and restarted (services.msc)."
                ),
            },
            {
                "id": "b",
                "text": "DNS Client service (Dnscache)",
                "correct": False,
                "rationale": (
                    "Incorrect. The DNS Client service handles DNS name resolution "
                    "caching. It is not involved in obtaining a DHCP lease or an IP "
                    "address. An APIPA address indicates a DHCP failure, not a DNS "
                    "failure."
                ),
            },
            {
                "id": "c",
                "text": "Windows Firewall service (MpsSvc)",
                "correct": False,
                "rationale": (
                    "Incorrect. The Windows Firewall does not block DHCP transactions "
                    "by default. It is not the cause of APIPA address assignment and "
                    "restarting it will not obtain a DHCP lease."
                ),
            },
            {
                "id": "d",
                "text": "Network Location Awareness service (NlaSvc)",
                "correct": False,
                "rationale": (
                    "Incorrect. NlaSvc identifies network type (domain, private, public) "
                    "but is not the service responsible for DHCP lease acquisition. "
                    "A stopped NlaSvc may cause incorrect network profile assignment "
                    "but not an APIPA address."
                ),
            },
        ],
        "explanation": (
            "When a Windows PC self-assigns an APIPA address while the DHCP server "
            "is operational and serving other clients, the DHCP Client service (Dhcp) "
            "on the affected machine is the most likely culprit. Open services.msc "
            "(or 'sc query dhcp' from CMD), verify the service is running, set it to "
            "Automatic, and restart it, then run 'ipconfig /renew' to trigger a fresh "
            "lease acquisition."
        ),
    },
    {
        "id": "a1d5v2-030",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A technician pings a remote host at 10.0.2.1 from a workstation and "
            "receives: 'Reply from 10.0.0.1: Destination host unreachable.' The "
            "technician's workstation has IP 10.0.1.50/24 with gateway 10.0.0.1. "
            "What does this response indicate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The router (10.0.0.1) received the packet but has no route to the 10.0.2.0/24 network",
                "correct": True,
                "rationale": (
                    "Correct. 'Destination host unreachable' returned from an intermediate "
                    "router (not the target host) indicates the router received the packet "
                    "but could not find a route to forward it. The gateway (10.0.0.1) "
                    "has no routing entry for 10.0.2.0/24 and is responding with an ICMP "
                    "Type 3 (Destination Unreachable) message."
                ),
            },
            {
                "id": "b",
                "text": "The workstation's NIC is disabled and the packet never left the local machine",
                "correct": False,
                "rationale": (
                    "Incorrect. If the NIC were disabled, the ping would fail with "
                    "'General failure' or 'Transmit failed.' The reply coming from "
                    "10.0.0.1 proves the packet was transmitted from the workstation "
                    "and reached the router."
                ),
            },
            {
                "id": "c",
                "text": "The target host 10.0.2.1 is powered off and refusing ICMP packets",
                "correct": False,
                "rationale": (
                    "Incorrect. If the host were powered off, the router nearest the "
                    "target network would generate the 'Destination host unreachable' "
                    "reply — but in this scenario the reply comes from the workstation's "
                    "own gateway (10.0.0.1), which means the gateway itself cannot "
                    "route to the destination network at all."
                ),
            },
            {
                "id": "d",
                "text": "The workstation and 10.0.2.1 are on the same subnet and ARP has failed",
                "correct": False,
                "rationale": (
                    "Incorrect. 10.0.1.50/24 and 10.0.2.1 are on different subnets "
                    "(10.0.1.0/24 vs. 10.0.2.0/24). ARP is used for same-subnet "
                    "communication; this packet is correctly sent to the gateway for "
                    "inter-subnet routing."
                ),
            },
        ],
        "explanation": (
            "ICMP Destination Unreachable (Type 3) returned from an intermediate "
            "router — not the target host — means the router has no route to the "
            "destination network. The packet left the workstation, reached the gateway, "
            "and the gateway returned the error. Check the routing table on the "
            "gateway with 'route print' (Windows) or 'ip route show' (Linux). Adding "
            "a static route or ensuring OSPF/RIP propagates the 10.0.2.0/24 route "
            "will resolve the issue."
        ),
    },
    {
        "id": "a1d5v2-031",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A user can access websites and email but cannot connect to the corporate "
            "file server by hostname (\\\\fileserver). Pinging the server by IP "
            "(10.1.1.20) succeeds. Pinging 'fileserver' by name fails with 'Ping "
            "request could not find host fileserver.' What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The workstation's DNS server is not resolving internal hostnames, or the 'fileserver' A record is missing from internal DNS",
                "correct": True,
                "rationale": (
                    "Correct. Internet access and external DNS resolution work (websites "
                    "and email), but internal hostname resolution fails. This indicates "
                    "either the internal DNS server does not have an A record for "
                    "'fileserver,' the workstation is using an external DNS server "
                    "instead of the internal one, or the DNS zone for the internal domain "
                    "is misconfigured."
                ),
            },
            {
                "id": "b",
                "text": "The file server's SMB port (445) is blocked by the firewall",
                "correct": False,
                "rationale": (
                    "Incorrect. A blocked SMB port would prevent connection to the share "
                    "but would not prevent the hostname from resolving via ping. The ping "
                    "failure by name (but success by IP) is a DNS problem, not a port "
                    "problem."
                ),
            },
            {
                "id": "c",
                "text": "The default gateway is incorrectly configured and is blocking internal traffic",
                "correct": False,
                "rationale": (
                    "Incorrect. If the gateway were misconfiguring internal routing, "
                    "pinging 10.1.1.20 by IP would also fail. The IP ping succeeds, "
                    "proving the routing path is intact. Only name resolution is broken."
                ),
            },
            {
                "id": "d",
                "text": "The user's Windows hosts file has an incorrect entry for 'fileserver'",
                "correct": False,
                "rationale": (
                    "Incorrect. An incorrect hosts file entry would cause the hostname "
                    "to resolve to the wrong IP, not fail to resolve entirely. The "
                    "error 'could not find host' indicates a complete resolution failure."
                ),
            },
        ],
        "explanation": (
            "Successful IP ping + successful internet browsing + failed internal name "
            "resolution = internal DNS issue. Check the workstation's configured DNS "
            "servers (ipconfig /all); if they point to an external DNS (e.g., 8.8.8.8), "
            "the internal 'fileserver' record will not be found. Correct the DNS server "
            "setting to point to the internal DNS server, or add the record to the "
            "appropriate internal DNS zone."
        ),
    },
    {
        "id": "a1d5v2-032",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "A user's wired network connection works at 100 Mbps instead of the "
            "expected 1 Gbps. Both the switch and NIC support gigabit. The link LED "
            "shows amber (100 Mbps) instead of green (1 Gbps). What is the MOST "
            "likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A Category 5 (Cat 5) cable is being used instead of the required Cat 5e or Cat 6 for gigabit operation",
                "correct": True,
                "rationale": (
                    "Correct. Gigabit Ethernet (1000BASE-T) requires all four wire pairs "
                    "and meets stringent crosstalk specifications. Cat 5 cable does not "
                    "reliably support gigabit; both endpoints auto-negotiate down to "
                    "100 Mbps when signal quality is insufficient. Cat 5e or Cat 6 is "
                    "required for sustained gigabit over copper."
                ),
            },
            {
                "id": "b",
                "text": "The NIC duplex is set to half-duplex, limiting throughput to 100 Mbps",
                "correct": False,
                "rationale": (
                    "Incorrect. Half-duplex affects collision avoidance but does not "
                    "change the link speed from gigabit to 100 Mbps. A half-duplex "
                    "gigabit link would still show gigabit link speed; only speed "
                    "auto-negotiation (not duplex) determines the 100/1000 Mbps "
                    "handshake."
                ),
            },
            {
                "id": "c",
                "text": "The switch port has QoS policies limiting the port to 100 Mbps",
                "correct": False,
                "rationale": (
                    "Incorrect. QoS policies operate at Layer 3/4 and shape traffic "
                    "throughput above the physical layer. They do not change the "
                    "physical link negotiation speed shown by the LED."
                ),
            },
            {
                "id": "d",
                "text": "The switch is overloaded and throttling the gigabit port to prevent congestion",
                "correct": False,
                "rationale": (
                    "Incorrect. Switch congestion causes packet drops and increased "
                    "latency at the application level but does not change the physical "
                    "layer negotiated link speed."
                ),
            },
        ],
        "explanation": (
            "1000BASE-T (Gigabit Ethernet over copper) requires all four wire pairs "
            "and Cat 5e or better cabling. Cat 5 (not Cat 5e) lacks the crosstalk "
            "suppression needed for gigabit, causing auto-negotiation to fall back "
            "to 100BASE-TX. Verify cable category by reading the cable jacket printing. "
            "Replace Cat 5 with Cat 5e or Cat 6 to achieve gigabit link speed."
        ),
    },
    # ── Multiple Response Questions ───────────────────────────────────────────
    {
        "id": "a1d5v2-033",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Troubleshooting methodology",
        "stem": (
            "A technician's initial theory about a network issue has been tested and "
            "disproved. According to the CompTIA troubleshooting methodology, which "
            "TWO actions are correct at this point? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Establish a new theory of probable cause based on remaining evidence",
                "correct": True,
                "rationale": (
                    "Correct. When a theory is disproved, Step 2 is revisited: the "
                    "technician must formulate a new theory using available evidence "
                    "and any additional information gathered during the failed test."
                ),
            },
            {
                "id": "b",
                "text": "Escalate to a higher-tier technician if unable to determine the cause independently",
                "correct": True,
                "rationale": (
                    "Correct. If reformulating a theory is beyond the technician's "
                    "knowledge or resources, escalation is explicitly allowed in the "
                    "CompTIA methodology at the point where a theory cannot be "
                    "established."
                ),
            },
            {
                "id": "c",
                "text": "Proceed to establish a plan of action based on the original (disproved) theory",
                "correct": False,
                "rationale": (
                    "Incorrect. A plan of action is only established after a theory has "
                    "been tested and confirmed. Proceeding with a disproved theory wastes "
                    "time and may cause additional harm."
                ),
            },
            {
                "id": "d",
                "text": "Document the findings and close the ticket as unresolved",
                "correct": False,
                "rationale": (
                    "Incorrect. Documentation (Step 6) is the final step after resolution. "
                    "Closing a ticket on a disproved theory without further investigation "
                    "abandons the customer and violates the methodology."
                ),
            },
        ],
        "explanation": (
            "When a theory is disproved, the methodology loops back to Step 2 — not "
            "forward. The technician either forms a new theory or escalates. This loop "
            "continues until a theory is confirmed. Only a confirmed theory leads to "
            "Step 4 (plan and implement). Closing the ticket without resolution is "
            "never the correct action while there is still a problem to solve."
        ),
    },
    {
        "id": "a1d5v2-034",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Motherboard/CPU/RAM/power issues",
        "stem": (
            "A workstation exhibits random application crashes and occasional BSODs with "
            "memory-related stop codes. The system has been running the same software "
            "for two years with no issues. Which TWO actions should the technician "
            "perform to diagnose the cause? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run Windows Memory Diagnostic (mdsched.exe) or Memtest86+ to test RAM",
                "correct": True,
                "rationale": (
                    "Correct. Memory-specific BSODs after stable two-year operation "
                    "suggest physical RAM degradation. Windows Memory Diagnostic or "
                    "Memtest86+ performs thorough hardware-level RAM tests and will "
                    "identify faulty cells or banks."
                ),
            },
            {
                "id": "b",
                "text": "Test each DIMM individually by removing all but one and rotating to identify the faulty module",
                "correct": True,
                "rationale": (
                    "Correct. After a memory test fails, isolating the specific faulty "
                    "DIMM by testing each stick individually is the standard diagnostic "
                    "procedure. This confirms which module must be replaced."
                ),
            },
            {
                "id": "c",
                "text": "Reinstall the operating system to resolve software-caused memory errors",
                "correct": False,
                "rationale": (
                    "Incorrect. Memory-specific BSODs following two years of stable "
                    "operation are hardware in origin. A clean OS reinstall will not "
                    "fix physically degrading RAM cells."
                ),
            },
            {
                "id": "d",
                "text": "Replace the power supply because low voltage causes RAM to produce errors",
                "correct": False,
                "rationale": (
                    "Incorrect. While extreme PSU voltage instability can cause RAM "
                    "errors, this is an uncommon cause and should be investigated after "
                    "RAM itself has been tested and ruled out. RAM testing is more "
                    "targeted and direct."
                ),
            },
        ],
        "explanation": (
            "When RAM-specific BSODs appear in a stable system: 1) Confirm the fault "
            "is RAM with mdsched.exe or Memtest86+ (passes entire RAM); 2) If errors "
            "found, isolate the bad module by testing one DIMM at a time. Then replace "
            "only the faulty DIMM. No need to reinstall OS or replace PSU unless RAM "
            "tests clean and further investigation warrants it."
        ),
    },
    {
        "id": "a1d5v2-035",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Storage & RAID troubleshooting",
        "stem": (
            "A technician is advising a small business on which RAID levels provide "
            "fault tolerance. Which TWO RAID levels offer data redundancy and can "
            "survive at least one drive failure? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "RAID 1 (mirroring)",
                "correct": True,
                "rationale": (
                    "Correct. RAID 1 mirrors all data across two (or more) drives. "
                    "If one drive fails, the mirror drive contains a complete copy "
                    "of all data and the array continues to function in a degraded "
                    "but operational state."
                ),
            },
            {
                "id": "b",
                "text": "RAID 5 (distributed parity)",
                "correct": True,
                "rationale": (
                    "Correct. RAID 5 uses distributed parity across three or more "
                    "drives. The loss of any single drive can be tolerated; the data "
                    "on the failed drive is reconstructed from the parity and data on "
                    "the remaining drives."
                ),
            },
            {
                "id": "c",
                "text": "RAID 0 (striping)",
                "correct": False,
                "rationale": (
                    "Incorrect. RAID 0 stripes data across drives for performance but "
                    "has zero redundancy. The loss of any single drive in a RAID 0 "
                    "array results in complete data loss."
                ),
            },
            {
                "id": "d",
                "text": "JBOD (Just a Bunch of Disks)",
                "correct": False,
                "rationale": (
                    "Incorrect. JBOD (or spanning) concatenates drives into a single "
                    "volume without any redundancy. Failure of any one drive results "
                    "in loss of data stored on that drive."
                ),
            },
        ],
        "explanation": (
            "Fault-tolerant RAID levels include RAID 1 (mirror), RAID 5 (single "
            "distributed parity), RAID 6 (dual parity), and RAID 10 (striped mirrors). "
            "RAID 0 and JBOD/spanning provide no fault tolerance. For the A+ exam, "
            "know that RAID 0 = performance only, RAID 1 = full mirror, RAID 5 = "
            "single parity, RAID 6 = double parity, RAID 10 = mirror + stripe."
        ),
    },
    {
        "id": "a1d5v2-036",
        "domain": 5,
        "objective": "5.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Printer troubleshooting",
        "stem": (
            "A laser printer produces pages where the printed image appears shifted "
            "significantly to one side, cutting off content at the edge. Which TWO "
            "are the MOST likely causes? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The paper guides in the tray are not adjusted to the paper size, allowing paper to feed off-center",
                "correct": True,
                "rationale": (
                    "Correct. Loose or improperly set paper guides allow sheets to "
                    "shift laterally as they feed through the pickup mechanism. This "
                    "causes the printed image to be misregistered horizontally, cutting "
                    "off content on one side."
                ),
            },
            {
                "id": "b",
                "text": "The printer driver is configured with incorrect paper margins for the document size",
                "correct": True,
                "rationale": (
                    "Correct. Incorrect margin or page size settings in the printer "
                    "driver can offset the printed image from the physical paper edge, "
                    "producing output that appears shifted with content cut off."
                ),
            },
            {
                "id": "c",
                "text": "The fuser is not bonding toner to the correct side of the paper",
                "correct": False,
                "rationale": (
                    "Incorrect. The fuser applies heat and pressure uniformly across "
                    "the full width of the paper. It does not cause lateral image "
                    "registration errors; it affects whether toner bonds, not where "
                    "it lands on the page."
                ),
            },
            {
                "id": "d",
                "text": "The toner cartridge has been shaken, distributing toner unevenly toward one side",
                "correct": False,
                "rationale": (
                    "Incorrect. Shaking a toner cartridge redistributes toner uniformly "
                    "within the cartridge to help with low toner; it does not cause a "
                    "lateral shift of the entire printed image."
                ),
            },
        ],
        "explanation": (
            "Image shift (content cut off at one edge) in laser printers is typically "
            "caused by mechanical or software registration issues: 1) Paper guides in "
            "the tray not matching the actual paper size — paper feeds off-center; "
            "2) Driver/application margin settings mismatched with the physical paper. "
            "Adjust the tray guides and verify the paper size setting in the driver. "
            "Hardware registration offset adjustment is available in the printer's "
            "service menu on some models."
        ),
    },
    {
        "id": "a1d5v2-037",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Network troubleshooting",
        "stem": (
            "All workstations on a single floor suddenly lose internet access "
            "simultaneously. Other floors are unaffected. Local network shares on the "
            "same floor are accessible. Which TWO components should the technician "
            "investigate FIRST? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "The floor's distribution switch or its uplink connection to the core switch",
                "correct": True,
                "rationale": (
                    "Correct. Local shares work (same-switch Layer 2 connectivity is "
                    "fine), but internet access fails for the entire floor, implying "
                    "the problem is in the uplink from the floor's switch to the "
                    "rest of the network. A failed uplink port, cable, or SFP between "
                    "the distribution switch and core switch is a prime suspect."
                ),
            },
            {
                "id": "b",
                "text": "The router or firewall interface handling this floor's VLAN",
                "correct": True,
                "rationale": (
                    "Correct. If the floor is on its own VLAN, a router or firewall "
                    "interface serving that VLAN may have failed, lost its IP, or had "
                    "an ACL change that blocks outbound routing — explaining internet "
                    "loss for all floor users while intra-switch (same-VLAN) shares "
                    "still work."
                ),
            },
            {
                "id": "c",
                "text": "Each workstation's NIC driver, which may have been updated simultaneously via group policy",
                "correct": False,
                "rationale": (
                    "Incorrect. A simultaneous NIC driver issue affecting every "
                    "workstation on one floor but no other floor is extremely unlikely. "
                    "The floor-level scope of the outage points to shared infrastructure "
                    "(switch uplink or router interface), not individual device drivers."
                ),
            },
            {
                "id": "d",
                "text": "The ISP connection, which may have gone down",
                "correct": False,
                "rationale": (
                    "Incorrect. The ISP connection is shared by all floors. An ISP "
                    "outage would affect the entire building, not just one floor. "
                    "Since other floors have internet access, the ISP is not at fault."
                ),
            },
        ],
        "explanation": (
            "Floor-specific internet loss with functional local shares isolates the "
            "fault to the boundary between the floor's local switching (working) and "
            "the upward routing infrastructure (failing). Focus on: the floor "
            "distribution switch uplink port/cable, the core switch port receiving "
            "that uplink, and the router/firewall interface for the floor's VLAN. "
            "Check interface status with 'show interfaces' on managed switches."
        ),
    },
    {
        "id": "a1d5v2-038",
        "domain": 5,
        "objective": "5.7",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Network command-line tools",
        "stem": (
            "A technician needs to perform two tasks on a Windows workstation: "
            "(1) flush the local DNS resolver cache to force fresh lookups, and "
            "(2) display the current routing table to verify the default gateway. "
            "Which TWO commands accomplish these tasks? (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "ipconfig /flushdns — flushes the local DNS resolver cache",
                "correct": True,
                "rationale": (
                    "Correct. 'ipconfig /flushdns' clears the Windows DNS resolver "
                    "cache (also called the DNS client cache). After flushing, the "
                    "next name resolution query goes to the configured DNS server "
                    "rather than returning a cached (potentially stale) result."
                ),
            },
            {
                "id": "b",
                "text": "route print — displays the IP routing table including the default gateway",
                "correct": True,
                "rationale": (
                    "Correct. 'route print' (or 'netstat -r') displays the complete "
                    "IP routing table, which includes the default route (0.0.0.0 with "
                    "the gateway IP) and all other static and connected routes. This "
                    "verifies the default gateway entry."
                ),
            },
            {
                "id": "c",
                "text": "ipconfig /release — releases the DNS cache and removes all cached entries",
                "correct": False,
                "rationale": (
                    "Incorrect. 'ipconfig /release' sends a DHCP Release message and "
                    "removes the IP address assignment; it does not flush the DNS "
                    "resolver cache. The correct DNS flush command is '/flushdns'."
                ),
            },
            {
                "id": "d",
                "text": "nslookup — displays the routing table and resolves the default gateway hostname",
                "correct": False,
                "rationale": (
                    "Incorrect. nslookup performs DNS lookups; it does not display the "
                    "routing table. The routing table is displayed by 'route print' or "
                    "'netstat -r'."
                ),
            },
        ],
        "explanation": (
            "Key Windows network commands: "
            "'ipconfig /flushdns' — purges the local DNS cache (useful when stale "
            "records are causing resolution failures). "
            "'route print' — shows the full IPv4/IPv6 routing table, including the "
            "default gateway route (0.0.0.0/0.0.0.0). "
            "Companion commands: 'ipconfig /displaydns' (view cache before flushing), "
            "'netstat -r' (alternative routing table display), 'route add/delete' "
            "(modify routes manually)."
        ),
    },
]
