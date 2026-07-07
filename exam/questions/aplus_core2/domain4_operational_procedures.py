"""
CompTIA A+ Core 2 (220-1202) — Domain 4: Operational Procedures
34 practice questions aligned to objectives 4.1–4.9.
"""

QUESTIONS = [
    # ── 4.1 Documentation / ticketing / asset management ──────────────────────
    {
        "id": "c2d4-001",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A technician receives a ticket for a laptop that 'keeps freezing.' "
            "After arriving on site, the technician discovers the symptom only occurs "
            "during a specific video-conferencing application. Which action BEST demonstrates "
            "proper ticketing practices before closing the ticket?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Update the ticket description to reflect the actual symptom (freezes only during video-conferencing), document root cause and fix, then obtain user sign-off and mark resolved.",
                "correct": True,
                "rationale": "Correct. Proper ticketing requires an accurate problem description, documented resolution steps, and end-user acceptance before closure — ensuring the knowledge base is useful for future incidents.",
            },
            {
                "id": "b",
                "text": "Close the ticket as 'user error' because the original description was vague.",
                "correct": False,
                "rationale": "Incorrect. Closing without an accurate description, root cause, or resolution discards valuable troubleshooting data and fails the end user.",
            },
            {
                "id": "c",
                "text": "Open a second ticket for the video-conferencing issue and leave the original open.",
                "correct": False,
                "rationale": "Incorrect. The original ticket should be updated rather than duplicated; duplicate tickets skew metrics and waste resources.",
            },
            {
                "id": "d",
                "text": "Escalate immediately to Tier 2 without updating the ticket description.",
                "correct": False,
                "rationale": "Incorrect. Escalation without updating the ticket leaves Tier 2 without critical diagnostic context, reducing resolution efficiency.",
            },
        ],
        "explanation": (
            "Ticketing best practices require: accurate user/device info, a precise problem description updated as new facts emerge, "
            "clear documentation of root cause and resolution steps, escalation levels used, and end-user acceptance. "
            "A well-maintained ticket doubles as a KB article for future incidents."
        ),
    },
    {
        "id": "c2d4-002",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A company is audited and cannot account for 12 laptops listed in its IT asset "
            "database. The auditor notes the laptops lack physical markings linking them to "
            "the database records. Which asset management control would MOST directly have "
            "prevented this discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Assigning assigned-user records in the ticketing system",
                "correct": False,
                "rationale": "Incorrect. User assignment records help with accountability but do not physically identify hardware, so assets can still be misidentified or lost without physical tags.",
            },
            {
                "id": "b",
                "text": "Affixing unique asset tags or barcodes to each device and linking them to the asset database",
                "correct": True,
                "rationale": "Correct. Physical asset tags create a one-to-one link between a device and its database record, enabling accurate physical inventory counts and audit reconciliation.",
            },
            {
                "id": "c",
                "text": "Implementing a change management request form for all hardware moves",
                "correct": False,
                "rationale": "Incorrect. Change management forms track planned changes but do not retroactively identify untagged hardware or reconcile physical inventory.",
            },
            {
                "id": "d",
                "text": "Publishing an acceptable use policy (AUP) for all employees",
                "correct": False,
                "rationale": "Incorrect. An AUP defines permitted use of IT resources but provides no mechanism to physically identify or track hardware assets.",
            },
        ],
        "explanation": (
            "Asset management relies on the full procurement life cycle: purchase, tagging (asset tag/ID), database entry with assigned user, "
            "warranty/licensing records, and eventual decommissioning. Physical tags are the critical link between a database record and the physical device."
        ),
    },
    {
        "id": "c2d4-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A new employee starts Monday. The IT team must provision an account, laptop, "
            "email, VPN credentials, and building badge. Which document type BEST ensures "
            "every step is completed consistently for every new hire?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Network topology diagram",
                "correct": False,
                "rationale": "Incorrect. A network topology diagram shows physical/logical network layout — it does not guide HR or IT through onboarding tasks.",
            },
            {
                "id": "b",
                "text": "Standard operating procedure (SOP) new-user setup checklist",
                "correct": True,
                "rationale": "Correct. An SOP new-user setup checklist enumerates every provisioning step in the required order, ensuring repeatability and compliance regardless of which technician performs the work.",
            },
            {
                "id": "c",
                "text": "Acceptable use policy (AUP)",
                "correct": False,
                "rationale": "Incorrect. An AUP defines rules for acceptable use of IT systems; it is a policy document, not a procedural checklist for IT provisioning tasks.",
            },
            {
                "id": "d",
                "text": "Incident report",
                "correct": False,
                "rationale": "Incorrect. Incident reports document security or operational events after they occur — not routine, repeatable provisioning workflows.",
            },
        ],
        "explanation": (
            "SOPs are step-by-step procedural documents. CompTIA identifies two key SOP subtypes for Domain 4: "
            "new-user setup checklist (onboarding) and end-user termination checklist (offboarding). "
            "Both enforce consistency and reduce errors compared to ad-hoc procedures."
        ),
    },
    {
        "id": "c2d4-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "An employee is terminated. The IT department must disable accounts, collect "
            "hardware, revoke VPN and badge access, and preserve email for litigation hold. "
            "Which document should drive this process to ensure nothing is missed?"
        ),
        "options": [
            {
                "id": "a",
                "text": "End-user termination SOP checklist",
                "correct": True,
                "rationale": "Correct. An end-user termination SOP checklist enumerates every offboarding step — account disablement, hardware return, access revocation, and data preservation — ensuring legal and security obligations are met consistently.",
            },
            {
                "id": "b",
                "text": "Acceptable use policy",
                "correct": False,
                "rationale": "Incorrect. The AUP is signed by employees to acknowledge usage rules; it does not direct IT staff through offboarding tasks.",
            },
            {
                "id": "c",
                "text": "KB article on password resets",
                "correct": False,
                "rationale": "Incorrect. A knowledge-base article addresses a specific technical task and is not a comprehensive process document for termination.",
            },
            {
                "id": "d",
                "text": "Regulatory compliance document",
                "correct": False,
                "rationale": "Incorrect. Regulatory compliance documents describe legal obligations; they do not provide the step-by-step IT workflow for an individual termination event.",
            },
        ],
        "explanation": (
            "The end-user termination SOP checklist is the offboarding counterpart to the new-user setup checklist. "
            "It ensures access revocation, hardware recovery, and data-preservation steps are completed in the correct order "
            "to satisfy both security policy and legal requirements."
        ),
    },
    # ── 4.2 Change management ─────────────────────────────────────────────────
    {
        "id": "c2d4-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "A sysadmin wants to push a new Group Policy Object (GPO) to all workstations "
            "to enforce USB port blocking. The change has not been tested in production. "
            "Which change-management step is MOST critical to perform BEFORE submitting the "
            "change request form to the change advisory board (CAB)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Perform sandbox testing in a non-production environment",
                "correct": True,
                "rationale": "Correct. Sandbox testing validates the change in an isolated environment before it touches production systems, reduces risk, and gives the CAB concrete test evidence to evaluate in the change request.",
            },
            {
                "id": "b",
                "text": "Notify all end users of the upcoming change",
                "correct": False,
                "rationale": "Incorrect. User communication is important but occurs after CAB approval, not before the change is even submitted for review.",
            },
            {
                "id": "c",
                "text": "Execute the rollback plan",
                "correct": False,
                "rationale": "Incorrect. A rollback plan must be documented and ready, but it is executed only if the change fails — not before sandbox testing or CAB submission.",
            },
            {
                "id": "d",
                "text": "Identify the responsible staff member for the change",
                "correct": False,
                "rationale": "Incorrect. Identifying a responsible staff member is required on the change form but is an administrative step, not the most critical risk-mitigation step before CAB review.",
            },
        ],
        "explanation": (
            "Change management requires: documented purpose/scope, risk analysis, affected systems, date/time window, responsible staff, "
            "rollback plan, and CAB approval. Sandbox testing is performed before submission so the CAB receives empirical evidence rather "
            "than just intent. Without it, the risk level assessment is speculative."
        ),
    },
    {
        "id": "c2d4-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "A firmware update is applied to 40 network switches during a maintenance window. "
            "Thirty minutes after the update, half the switches begin dropping packets. "
            "According to change management best practices, what should the responsible "
            "staff member do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open a new change request to apply a corrective patch",
                "correct": False,
                "rationale": "Incorrect. Opening a new change request for an emergency that is actively impacting production delays recovery. The pre-approved rollback plan should be invoked immediately.",
            },
            {
                "id": "b",
                "text": "Execute the pre-documented rollback plan to revert the firmware",
                "correct": True,
                "rationale": "Correct. The rollback plan is specifically created so that a failed change can be reversed quickly without a new CAB cycle. Executing it first restores service, then a post-incident review addresses root cause.",
            },
            {
                "id": "c",
                "text": "Escalate to the CAB chair for emergency approval before taking any action",
                "correct": False,
                "rationale": "Incorrect. While escalation to management is appropriate, the rollback plan is pre-approved precisely for this scenario. Waiting for emergency CAB approval delays restoration.",
            },
            {
                "id": "d",
                "text": "Continue monitoring for another hour to determine if the issue self-resolves",
                "correct": False,
                "rationale": "Incorrect. Continued monitoring while 20 switches drop packets prolongs the outage and is not consistent with change management's goal of minimizing business impact.",
            },
        ],
        "explanation": (
            "A rollback plan is a mandatory component of any change request. It is pre-approved by the CAB so that "
            "the responsible staff member can execute it immediately upon detecting a failed change, without delay. "
            "After rollback, a post-implementation review documents lessons learned."
        ),
    },
    # ── 4.3 Backup and recovery ───────────────────────────────────────────────
    {
        "id": "c2d4-007",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backup types",
        "stem": (
            "An organization runs a full backup every Sunday and incremental backups "
            "Monday–Saturday. A storage failure occurs Thursday afternoon. "
            "Which backups must be restored, and in what order?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sunday's full, then Monday, Tuesday, and Wednesday incrementals in chronological order",
                "correct": True,
                "rationale": "Correct. Incremental backups capture only changes since the LAST backup of any type. Recovery requires the last full plus every incremental since, applied in chronological order.",
            },
            {
                "id": "b",
                "text": "Only Sunday's full backup",
                "correct": False,
                "rationale": "Incorrect. The full alone contains no data written Monday–Wednesday; all subsequent incrementals are required to bring data current.",
            },
            {
                "id": "c",
                "text": "Sunday's full and only Wednesday's incremental",
                "correct": False,
                "rationale": "Incorrect. That describes a differential scheme. With incrementals, Wednesday's backup contains only Wednesday's changes — Monday's and Tuesday's changes are in their respective incrementals and would be missing.",
            },
            {
                "id": "d",
                "text": "Only Wednesday's incremental backup",
                "correct": False,
                "rationale": "Incorrect. An incremental is not self-contained; without the full and prior incrementals the data set cannot be rebuilt.",
            },
        ],
        "explanation": (
            "Incremental = changes since the last backup of any type (fast backups, slow restore: full + all incrementals in order). "
            "Differential = changes since the last full (full + one differential). "
            "Synthetic full merges existing backups server-side to create a current full without re-reading source data."
        ),
    },
    {
        "id": "c2d4-008",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backup types",
        "stem": (
            "A company runs a full backup every Sunday and differential backups Monday–Saturday. "
            "A failure occurs Friday morning. Which backups are required to restore, and "
            "why are fewer sets needed compared to an incremental strategy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sunday's full and Thursday's differential only, because each differential captures all changes since Sunday",
                "correct": True,
                "rationale": "Correct. A differential backup captures ALL changes since the last full, so Thursday's differential contains everything from Monday through Thursday. Only two sets are ever needed: the last full plus the most recent differential.",
            },
            {
                "id": "b",
                "text": "Sunday's full plus Monday, Tuesday, Wednesday, and Thursday differentials",
                "correct": False,
                "rationale": "Incorrect. Each subsequent differential already subsumes all prior differentials since the last full. Only the most recent differential is needed alongside the full.",
            },
            {
                "id": "c",
                "text": "Only Thursday's differential, because differentials are self-contained",
                "correct": False,
                "rationale": "Incorrect. A differential is not self-contained; it contains changes relative to the last full backup. The full backup must be restored first.",
            },
            {
                "id": "d",
                "text": "Sunday's full and Wednesday's differential, because the most recent complete day is used",
                "correct": False,
                "rationale": "Incorrect. Thursday's differential is newer and subsumes Wednesday's. Using Wednesday's would miss Thursday's data, leaving the restore one day behind.",
            },
        ],
        "explanation": (
            "Differential backups grow in size each day (capturing more cumulative changes) but simplify restore: "
            "last full + most recent differential only, vs. full + every incremental. "
            "The trade-off is larger backup windows and media consumption with differentials."
        ),
    },
    {
        "id": "c2d4-009",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "A small business stores all backups on a single NAS in the server room. "
            "A fire destroys the server room over the weekend. Which principle, if "
            "implemented, would MOST effectively ensure data survived this event?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Grandfather-Father-Son (GFS) rotation",
                "correct": False,
                "rationale": "Incorrect. GFS is a tape-rotation schedule managing daily, weekly, and monthly sets. It does not inherently require off-site copies, so all GFS sets stored on the on-site NAS would be lost in a fire.",
            },
            {
                "id": "b",
                "text": "The 3-2-1 backup rule",
                "correct": True,
                "rationale": "Correct. The 3-2-1 rule requires 3 copies of data on 2 different media types with 1 copy stored off-site. The off-site copy would have survived the fire, ensuring recovery.",
            },
            {
                "id": "c",
                "text": "Synthetic full backups",
                "correct": False,
                "rationale": "Incorrect. Synthetic full backups reduce backup window time by assembling a full from existing backups server-side. They address efficiency, not geographic redundancy or disaster survivability.",
            },
            {
                "id": "d",
                "text": "Incremental backup every four hours",
                "correct": False,
                "rationale": "Incorrect. More frequent incrementals reduce RPO but if all copies remain on-site, every copy is destroyed along with the server room.",
            },
        ],
        "explanation": (
            "The 3-2-1 rule: keep 3 copies of data, on 2 different storage media types, with at least 1 copy off-site "
            "(or in the cloud). This protects against site-level disasters (fire, flood, theft). "
            "GFS complements 3-2-1 by organizing how long to retain daily/weekly/monthly sets, but location strategy is separate."
        ),
    },
    {
        "id": "c2d4-010",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "An organization uses a Grandfather-Father-Son (GFS) tape rotation. "
            "A ransomware attack encrypts all on-site data on a Tuesday. "
            "The 'grandfather' (monthly) tapes are stored in a bank vault. "
            "What is the PRIMARY recovery limitation of this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "GFS does not support incremental backups, so restore will be incomplete.",
                "correct": False,
                "rationale": "Incorrect. GFS is a rotation scheme, not a backup type. It can be used with full, incremental, or differential backups.",
            },
            {
                "id": "b",
                "text": "The recovery point will be the end of the prior month, resulting in up to 30+ days of data loss.",
                "correct": True,
                "rationale": "Correct. If only monthly grandfather tapes are off-site, the most recent clean restore point is the last monthly tape — potentially 30+ days old. Daily son and weekly father tapes stored on-site are also encrypted.",
            },
            {
                "id": "c",
                "text": "The vault tapes cannot be decrypted without the on-site key server.",
                "correct": False,
                "rationale": "Incorrect. The question does not state that tapes are encrypted with an on-site key. This is a speculative distractor; the core limitation is data age (RPO), not encryption dependency.",
            },
            {
                "id": "d",
                "text": "GFS rotation requires that monthly tapes be returned to site before restoration can begin.",
                "correct": False,
                "rationale": "Incorrect. GFS does not mandate on-site tape presence before restoration — tapes can be brought from the vault. The limitation is the staleness of the monthly snapshot.",
            },
        ],
        "explanation": (
            "In GFS, 'son' tapes (daily) and 'father' tapes (weekly) are typically cycled on-site; 'grandfather' (monthly) tapes "
            "are rotated off-site. If on-site tapes are compromised, recovery is limited to the most recent off-site (monthly) tape, "
            "creating a large recovery point objective (RPO). The 3-2-1 rule recommends off-site copies of more recent backups to shrink RPO."
        ),
    },
    # ── 4.4 Safety procedures ────────────────────────────────────────────────
    {
        "id": "c2d4-011",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A technician is replacing a RAM module in a desktop while wearing an ESD wrist strap. "
            "The strap is clipped to the metal chassis of the powered-off (but still plugged-in) PC. "
            "Which statement BEST describes this setup?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Optimal: the plug maintains ground continuity through the power supply, safely dissipating ESD.",
                "correct": True,
                "rationale": "Correct. With the PC plugged in (but powered off), the three-prong outlet keeps the chassis at earth ground through the power supply's safety-ground wire, giving the ESD strap a true earth-ground reference — the recommended setup.",
            },
            {
                "id": "b",
                "text": "Dangerous: the technician could be electrocuted because the power supply is still energized.",
                "correct": False,
                "rationale": "Incorrect. The system is powered off. The ESD strap connects through a 1 MΩ resistor, limiting current to a safe level. The risk of electrocution from a powered-off, plugged-in system is negligible.",
            },
            {
                "id": "c",
                "text": "Suboptimal: the strap should be clipped to an unpainted metal surface on the wall, not the chassis.",
                "correct": False,
                "rationale": "Incorrect. Clipping to the chassis (itself at earth ground via the outlet) is correct. Attaching to a random wall surface is not a standardized ESD grounding method.",
            },
            {
                "id": "d",
                "text": "Incorrect: the system must be fully unplugged before ESD work can begin.",
                "correct": False,
                "rationale": "Incorrect. Unplugging removes the earth-ground path, defeating the ESD strap. The correct practice is to keep the system plugged in (powered off) so the chassis is at earth ground.",
            },
        ],
        "explanation": (
            "ESD wrist straps work by providing a high-resistance (≈1 MΩ) path from technician to earth ground, slowly dissipating "
            "static charge. Clipping to a plugged-in (off) chassis uses the outlet's safety ground. An antistatic mat should also be "
            "used on the work surface. Components removed from systems should be stored in antistatic bags."
        ),
    },
    {
        "id": "c2d4-012",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A technician notices a small electrical fire has started inside a laser printer. "
            "Which fire-suppression method should the technician use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "CO2 or dry-chemical Class C fire extinguisher",
                "correct": True,
                "rationale": "Correct. Class C extinguishers are rated for energized electrical equipment fires. CO2 and dry chemical do not conduct electricity and leave no corrosive residue (CO2) or manageable residue (dry chemical).",
            },
            {
                "id": "b",
                "text": "Water extinguisher aimed directly at the flame",
                "correct": False,
                "rationale": "Incorrect. Water conducts electricity. Using a water extinguisher on an energized electrical fire creates an electrocution hazard and may spread the fire.",
            },
            {
                "id": "c",
                "text": "Class A foam extinguisher",
                "correct": False,
                "rationale": "Incorrect. Class A extinguishers are designed for ordinary combustibles (wood, paper). Foam is conductive and unsuitable for live electrical equipment.",
            },
            {
                "id": "d",
                "text": "Unplug the printer first, then use any extinguisher type",
                "correct": False,
                "rationale": "Incorrect. While de-energizing is ideal, it may not be safely possible. The correct action is to use a Class C-rated extinguisher and evacuate if necessary, not to delay suppression.",
            },
        ],
        "explanation": (
            "Electrical fires are Class C in the US classification system. Approved agents: CO2, dry chemical (ABC or BC rated), "
            "and clean-agent (halon alternatives). Water and foam conduct electricity and are prohibited on energized equipment. "
            "Always evacuate and call emergency services for any significant fire."
        ),
    },
    # ── 4.5 Environmental impacts and controls ────────────────────────────────
    {
        "id": "c2d4-013",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "A business experiences brief voltage drops (brownouts) three to four times a week, "
            "causing servers to reboot unexpectedly. Which power-conditioning device BEST "
            "addresses this problem while also providing a few minutes of runtime during a "
            "complete power failure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Surge suppressor",
                "correct": False,
                "rationale": "Incorrect. A surge suppressor protects against voltage spikes, not sustained voltage drops (brownouts). It provides no battery backup.",
            },
            {
                "id": "b",
                "text": "Uninterruptible power supply (UPS)",
                "correct": True,
                "rationale": "Correct. A UPS contains a battery that continuously or automatically conditions power, compensates for brownouts via voltage regulation (AVR), and provides battery runtime during complete outages for orderly shutdown.",
            },
            {
                "id": "c",
                "text": "Power distribution unit (PDU)",
                "correct": False,
                "rationale": "Incorrect. A PDU distributes power and may include surge protection and monitoring but does not provide battery backup or automatic voltage regulation for brownouts.",
            },
            {
                "id": "d",
                "text": "Line conditioner without battery backup",
                "correct": False,
                "rationale": "Incorrect. A line conditioner regulates voltage and filters noise but provides no battery, so a complete blackout still causes an abrupt shutdown.",
            },
        ],
        "explanation": (
            "UPS units solve brownouts (via automatic voltage regulation), blackouts (battery backup), and surges (built-in filtering). "
            "Surge suppressors only handle spikes. The UPS battery provides runtime for a graceful shutdown or failover. "
            "For servers, an online/double-conversion UPS is preferred because output is always from the inverter."
        ),
    },
    {
        "id": "c2d4-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "An IT manager must dispose of a large quantity of expired lithium-ion laptop batteries. "
            "Which disposal method is MOST compliant with environmental regulations?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Place them in standard office recycling bins since they contain recyclable materials.",
                "correct": False,
                "rationale": "Incorrect. Li-ion batteries cannot go in standard recycling or trash; they are regulated hazardous waste due to flammable electrolytes and heavy metal content.",
            },
            {
                "id": "b",
                "text": "Dispose via a certified e-waste or battery recycling facility that complies with local hazardous-waste regulations.",
                "correct": True,
                "rationale": "Correct. Li-ion batteries are classified as hazardous materials. Disposal must follow SDS/MSDS guidance and applicable regulations (EPA, local law), typically through a certified recycler or manufacturer take-back program.",
            },
            {
                "id": "c",
                "text": "Discharge fully and dispose in landfill, since depleted batteries are inert.",
                "correct": False,
                "rationale": "Incorrect. Even depleted Li-ion batteries contain regulated heavy metals and electrolytes. Landfill disposal violates most environmental regulations and is not made safe by discharging.",
            },
            {
                "id": "d",
                "text": "Store indefinitely in an on-site hazmat cabinet as long as the batteries are not leaking.",
                "correct": False,
                "rationale": "Incorrect. Indefinite storage is not compliant disposal. Regulations require timely disposal through approved channels regardless of battery condition.",
            },
        ],
        "explanation": (
            "SDS (Safety Data Sheet) governs handling and disposal of hazardous materials including batteries (Li-ion, NiMH, lead-acid) "
            "and toner cartridges. All must be disposed of through certified facilities or manufacturer take-back programs. "
            "Improper disposal can result in fines and environmental liability."
        ),
    },
    # ── 4.6 Incident response / licensing / regulated data ───────────────────
    {
        "id": "c2d4-015",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A help desk technician discovers what appears to be child sexual abuse material (CSAM) "
            "while troubleshooting a user's workstation. Which sequence of actions BEST follows "
            "incident response and chain-of-custody best practices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Immediately delete the files, inform the user, and document the deletion in the ticket.",
                "correct": False,
                "rationale": "Incorrect. Deleting evidence destroys the chain of custody and may constitute evidence tampering — a criminal offense. The user must not be informed, as that could constitute tipping off a suspect.",
            },
            {
                "id": "b",
                "text": "Do not touch the files; preserve the system state; immediately report to management and potentially law enforcement; document all actions with timestamps.",
                "correct": True,
                "rationale": "Correct. Chain-of-custody procedures require: stop working on the device, preserve evidence (do not alter files), report to management and law enforcement if required, document every action with date/time, and maintain a log of who accessed the evidence.",
            },
            {
                "id": "c",
                "text": "Copy the files to a personal USB drive for safekeeping, then report to management.",
                "correct": False,
                "rationale": "Incorrect. Copying evidence to a personal device breaks chain of custody, may violate laws related to possession of illegal material, and introduces integrity questions about the evidence.",
            },
            {
                "id": "d",
                "text": "Reimage the workstation immediately to prevent further spread, then notify management.",
                "correct": False,
                "rationale": "Incorrect. Reimaging destroys forensic evidence. Evidence preservation always takes priority over rapid remediation in an incident involving potential criminal activity.",
            },
        ],
        "explanation": (
            "Chain of custody requires: identify and preserve evidence without alteration, document who accesses it and when, "
            "report to management (and law enforcement for criminal matters), and create a forensic image for analysis rather than "
            "working on original media. The original system should be secured as evidence."
        ),
    },
    {
        "id": "c2d4-016",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "After a suspected data breach, a forensic analyst needs to examine a workstation's "
            "hard drive while preserving evidence integrity. Which action is the FIRST step "
            "to maintain chain of custody?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Create a bit-for-bit forensic image of the drive before any analysis",
                "correct": True,
                "rationale": "Correct. Creating a forensic image (bit-level copy) preserves original evidence. Analysis is performed on the image, not the source drive, maintaining the integrity and chain of custody of the original.",
            },
            {
                "id": "b",
                "text": "Boot the workstation into Windows to browse files and capture screenshots",
                "correct": False,
                "rationale": "Incorrect. Booting the OS modifies timestamps, swap files, and registry entries, altering evidence and potentially invalidating forensic findings in court.",
            },
            {
                "id": "c",
                "text": "Run antivirus on the live system to remove any malware before imaging",
                "correct": False,
                "rationale": "Incorrect. Running antivirus on the original drive modifies files and destroys evidence. The drive must be imaged in its current state before any remediation.",
            },
            {
                "id": "d",
                "text": "Attach the drive to a second PC and delete suspicious files to halt the breach",
                "correct": False,
                "rationale": "Incorrect. Deleting files alters evidence and destroys the chain of custody. Containment should be achieved by network isolation, not by modifying the evidence.",
            },
        ],
        "explanation": (
            "Forensic imaging creates a hash-verified copy (MD5/SHA-256) of the original drive. Every subsequent step — analysis, "
            "keyword search, file recovery — is performed on the copy. The original, sealed with its hash documented, constitutes "
            "the evidence preserved for legal proceedings."
        ),
    },
    {
        "id": "c2d4-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "A U.S. medical practice stores patient diagnoses, insurance numbers, and treatment "
            "histories on a cloud server. A technician asks which data classification applies. "
            "Which regulation and classification are CORRECT?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PCI DSS — payment card industry data, because insurance billing is involved",
                "correct": False,
                "rationale": "Incorrect. PCI DSS governs payment card numbers (credit/debit). Insurance numbers and medical records are not PCI data.",
            },
            {
                "id": "b",
                "text": "HIPAA — Protected Health Information (PHI), because health records and identifiers are regulated",
                "correct": True,
                "rationale": "Correct. HIPAA defines PHI as individually identifiable health information. Diagnoses, treatment histories, and insurance numbers tied to a patient all qualify, and HIPAA mandates specific security and privacy controls.",
            },
            {
                "id": "c",
                "text": "GDPR — General Data Protection Regulation, because it covers all personal data globally",
                "correct": False,
                "rationale": "Incorrect. GDPR applies to EU residents' personal data. A U.S.-only medical practice is primarily governed by HIPAA, not GDPR, unless it processes data of EU data subjects.",
            },
            {
                "id": "d",
                "text": "PII only — since patient names and insurance numbers are personally identifiable information",
                "correct": False,
                "rationale": "Incorrect. While PHI is a subset of PII, the specific regulation covering health records in the U.S. is HIPAA. Simply labeling this as 'PII only' understates the regulatory requirements and appropriate controls.",
            },
        ],
        "explanation": (
            "Regulated data types: PII (any data identifying an individual), PHI (health-related PII, governed by HIPAA), "
            "PCI (payment card numbers, governed by PCI DSS), GDPR (personal data of EU residents). "
            "Data retention requirements also differ: HIPAA typically requires 6 years for medical records."
        ),
    },
    {
        "id": "c2d4-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "A software developer uses an open-source library licensed under the GNU GPL v3 "
            "in a commercial product. The company wants to keep the product's source code "
            "proprietary. Which statement BEST describes the licensing conflict?"
        ),
        "options": [
            {
                "id": "a",
                "text": "There is no conflict; open-source software can always be incorporated into commercial products.",
                "correct": False,
                "rationale": "Incorrect. Open-source licenses vary widely. The GPL v3 is 'copyleft' — it requires derivative works to also be licensed under GPL v3 and distributed with source code.",
            },
            {
                "id": "b",
                "text": "The GPL v3 copyleft requirement forces the company to release the entire product's source code under GPL v3 if distributed.",
                "correct": True,
                "rationale": "Correct. GPL v3 is a strong copyleft license. Incorporating GPL v3 code into a distributed product requires the entire work to be licensed under GPL v3 and source code made available, conflicting with keeping the product proprietary.",
            },
            {
                "id": "c",
                "text": "The company can keep source proprietary as long as it credits the open-source author in documentation.",
                "correct": False,
                "rationale": "Incorrect. Attribution satisfies some licenses (e.g., MIT, BSD) but not GPL v3. GPL v3 requires source distribution regardless of attribution.",
            },
            {
                "id": "d",
                "text": "EULA restrictions override open-source licenses, so the company's EULA controls.",
                "correct": False,
                "rationale": "Incorrect. An EULA is between the company and its customers. It cannot override the obligations imposed on the company by the upstream open-source license under which it received the library.",
            },
        ],
        "explanation": (
            "Open-source licenses range from permissive (MIT, BSD, Apache 2.0 — allow proprietary use) to copyleft "
            "(GPL v2/v3, LGPL — require derivative works to carry same license). "
            "EULA governs the company-to-end-user relationship. DRM restricts usage after distribution. "
            "Companies must audit license obligations before incorporating OSS into commercial products."
        ),
    },
    # ── 4.7 Communication and professionalism ─────────────────────────────────
    {
        "id": "c2d4-019",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A user calls the help desk, extremely frustrated, claiming the technician who "
            "visited yesterday 'broke' the printer. The technician believes the printer was "
            "already malfunctioning before the visit. Which response BEST demonstrates "
            "professional communication?"
        ),
        "options": [
            {
                "id": "a",
                "text": "'I understand why you're frustrated. Let me review the ticket notes from yesterday and then schedule a time to come look at this with you. Can you describe exactly what's happening now?'",
                "correct": True,
                "rationale": "Correct. This response acknowledges the user's frustration (empathy), avoids arguing or being defensive, asks open-ended questions to clarify the problem, and commits to an action — all hallmarks of professional communication.",
            },
            {
                "id": "b",
                "text": "'That's impossible. The printer was working fine when we left. You must have changed something.'",
                "correct": False,
                "rationale": "Incorrect. This response is defensive and accusatory. It dismisses the user's concern and damages the support relationship without gathering facts.",
            },
            {
                "id": "c",
                "text": "'I'll note your complaint in the ticket and have a manager call you back eventually.'",
                "correct": False,
                "rationale": "Incorrect. Vague timelines ('eventually') and passive escalation without empathy fail to meet the user's expectations and demonstrate poor professionalism.",
            },
            {
                "id": "d",
                "text": "'Printers break all the time for various reasons — this sort of thing happens.'",
                "correct": False,
                "rationale": "Incorrect. Dismissing the problem trivializes the user's experience, violates the principle of not being judgmental, and does nothing to resolve the issue.",
            },
        ],
        "explanation": (
            "CompTIA A+ professionalism principles include: do not argue or become defensive, avoid dismissing problems, "
            "ask open-ended questions, actively listen, set clear expectations/timelines, maintain a positive attitude, "
            "and follow up. Never disclose experiences with customers on social media."
        ),
    },
    {
        "id": "c2d4-020",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Communication & professionalism",
        "stem": (
            "During a support call, the user repeatedly interrupts the technician and uses "
            "culturally specific idioms the technician does not fully understand. "
            "Which approach BEST reflects cultural sensitivity and active listening?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Allow the user to finish speaking, then politely ask for clarification on the unclear phrases using neutral, plain language.",
                "correct": True,
                "rationale": "Correct. Active listening means not interrupting. Cultural sensitivity means asking for clarification without mocking or expressing confusion dismissively, and using clear, culture-neutral language.",
            },
            {
                "id": "b",
                "text": "Interrupt the user to keep the call efficient and ask for a definition of each idiom immediately.",
                "correct": False,
                "rationale": "Incorrect. Interrupting violates active-listening principles and may come across as dismissive or rude, especially if the interruption implies the technician does not value what the user is saying.",
            },
            {
                "id": "c",
                "text": "Assume you understand the idioms and proceed without clarifying, to avoid making the user feel culturally judged.",
                "correct": False,
                "rationale": "Incorrect. Proceeding on incorrect assumptions risks miscommunication and an unresolved issue. Polite clarification is more respectful than silent misunderstanding.",
            },
            {
                "id": "d",
                "text": "Transfer the call to a technician who shares the user's cultural background.",
                "correct": False,
                "rationale": "Incorrect. Transferring based solely on cultural background is not a CompTIA-endorsed practice and may not be feasible. It also avoids the technician's responsibility to develop cultural competence.",
            },
        ],
        "explanation": (
            "CompTIA emphasizes: actively listen (do not interrupt), be culturally sensitive, use appropriate titles, "
            "avoid jargon that may not translate across cultures, and use plain language. "
            "Asking for clarification after the user finishes is the correct approach."
        ),
    },
    {
        "id": "c2d4-021",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A technician is on a client site repairing a workstation when a personal text message "
            "arrives. The client is watching. Which action is MOST professional?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Silence the phone without reading the message and continue working on the client's issue.",
                "correct": True,
                "rationale": "Correct. CompTIA stresses avoiding personal distractions during customer interactions. Silencing the device and remaining focused demonstrates respect for the client's time.",
            },
            {
                "id": "b",
                "text": "Excuse yourself briefly, read the message in the hallway, and return within one minute.",
                "correct": False,
                "rationale": "Incorrect. Leaving to check a personal message still signals that personal communications take priority over the client's needs — even if brief, it is unprofessional.",
            },
            {
                "id": "c",
                "text": "Read and respond to the message quickly while explaining it will only take a second.",
                "correct": False,
                "rationale": "Incorrect. Reading and responding in front of the client demonstrates divided attention and disrespect, violating the principle of avoiding distractions during customer interactions.",
            },
            {
                "id": "d",
                "text": "Post a quick update on social media about the client's interesting technical problem, then resume work.",
                "correct": False,
                "rationale": "Incorrect. Posting about client experiences on social media violates confidentiality and is explicitly prohibited by CompTIA professionalism guidelines.",
            },
        ],
        "explanation": (
            "Key professionalism rules: avoid personal distractions (phone, social media) during customer interactions; "
            "never disclose customer information or experiences on social media; be on time and give the customer your full attention. "
            "Personal calls/texts should wait unless a genuine emergency."
        ),
    },
    # ── 4.8 Scripting basics ─────────────────────────────────────────────────
    {
        "id": "c2d4-022",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A Windows administrator needs to automate monthly software inventory collection "
            "across 200 workstations, output results to a CSV file, and email the report. "
            "Which script file type is MOST appropriate and WHY?"
        ),
        "options": [
            {
                "id": "a",
                "text": ".bat — because batch files run natively on all Windows versions without additional tools",
                "correct": False,
                "rationale": "Incorrect. Batch (.bat) files can run on Windows natively but have very limited capabilities for structured output, CSV formatting, WMI queries, and sending email — making them inappropriate for this complex task.",
            },
            {
                "id": "b",
                "text": ".ps1 — because PowerShell provides rich object-oriented cmdlets for WMI queries, CSV export, and email via Send-MailMessage",
                "correct": True,
                "rationale": "Correct. PowerShell (.ps1) is the premier Windows automation language, with native cmdlets (Get-WmiObject/Get-CimInstance, Export-Csv, Send-MailMessage) that make inventory, reporting, and email automation straightforward.",
            },
            {
                "id": "c",
                "text": ".sh — because shell scripts are the industry standard for cross-platform automation",
                "correct": False,
                "rationale": "Incorrect. .sh (Bash/shell) scripts run on Unix/Linux/macOS. On Windows, they require WSL or Git Bash and are not the native tool for Windows administration tasks.",
            },
            {
                "id": "d",
                "text": ".vbs — because VBScript integrates best with Windows COM objects for inventory",
                "correct": False,
                "rationale": "Incorrect. VBScript (.vbs) can access WMI, but Microsoft deprecated it in Windows 11 23H2 and later. PowerShell is the recommended modern replacement with far greater capability.",
            },
        ],
        "explanation": (
            "Script types and primary platforms: .bat (Windows batch, legacy), .ps1 (PowerShell, Windows/cross-platform), "
            ".vbs (VBScript, Windows, deprecated), .sh (Bash/shell, Linux/macOS), .js (JavaScript, browser/Node.js), "
            ".py (Python, cross-platform). PowerShell is the current standard for Windows enterprise automation."
        ),
    },
    {
        "id": "c2d4-023",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A sysadmin downloads a PowerShell script from an online forum to automate "
            "drive mapping across the organization. Which risk is MOST significant when "
            "running an untested, third-party script in a production environment?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The script may inadvertently change system settings or introduce malware if not reviewed.",
                "correct": True,
                "rationale": "Correct. CompTIA identifies the primary scripting risks as unintentionally introducing malware and inadvertently changing system settings. Untested third-party scripts must be reviewed and sandbox-tested before production use.",
            },
            {
                "id": "b",
                "text": "The script file extension (.ps1) may not be recognized by older Windows versions.",
                "correct": False,
                "rationale": "Incorrect. PowerShell has shipped with Windows since Vista/Server 2008. Extension recognition is not a significant risk for .ps1 files in modern environments.",
            },
            {
                "id": "c",
                "text": "The script will be blocked by default User Account Control (UAC) prompts, preventing any damage.",
                "correct": False,
                "rationale": "Incorrect. UAC prompts can be suppressed or bypassed by scripts that request elevation. UAC is not a reliable safety net against malicious or poorly written scripts run by an admin.",
            },
            {
                "id": "d",
                "text": "PowerShell scripts cannot map network drives, so the script will simply fail without causing harm.",
                "correct": False,
                "rationale": "Incorrect. PowerShell can absolutely map network drives (New-PSDrive, net use). More importantly, a script can perform other unintended actions even if its primary stated purpose fails.",
            },
        ],
        "explanation": (
            "CompTIA scripting risks: (1) unintentionally introducing malware embedded in scripts, "
            "(2) inadvertently changing system settings, (3) browser/system crashes due to resource mishandling. "
            "Mitigation: review scripts before execution, sandbox-test, use code signing, apply least privilege."
        ),
    },
    {
        "id": "c2d4-024",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Scripting basics",
        "stem": (
            "Match each script file extension to its PRIMARY platform and use case. "
            "A technician must automate nightly log rotation on a Linux web server. "
            "Which file extension and interpreter are CORRECT for this task?"
        ),
        "options": [
            {
                "id": "a",
                "text": ".bat / Windows Command Interpreter",
                "correct": False,
                "rationale": "Incorrect. .bat files are Windows batch scripts and do not run on Linux without emulation. They cannot natively manipulate Linux file paths or use Linux commands.",
            },
            {
                "id": "b",
                "text": ".sh / Bash (or POSIX shell)",
                "correct": True,
                "rationale": "Correct. .sh files are shell scripts executed by Bash or another POSIX-compliant shell on Linux/macOS. They are the standard tool for Linux automation tasks such as log rotation, cron jobs, and file management.",
            },
            {
                "id": "c",
                "text": ".ps1 / PowerShell Core",
                "correct": False,
                "rationale": "Incorrect. While PowerShell Core (.ps1) does run on Linux, it is not the native or conventional choice for Linux log rotation. .sh scripts are the expected and idiomatic solution.",
            },
            {
                "id": "d",
                "text": ".vbs / Windows Script Host",
                "correct": False,
                "rationale": "Incorrect. VBScript (.vbs) runs under Windows Script Host (wscript/cscript) and has no native support on Linux.",
            },
        ],
        "explanation": (
            "Script extension / primary runtime quick reference: "
            ".bat → Windows Command Interpreter; "
            ".ps1 → PowerShell (Windows/Linux/macOS); "
            ".vbs → Windows Script Host (wscript/cscript); "
            ".sh → Bash/POSIX shell (Linux/macOS); "
            ".js → Browser or Node.js; "
            ".py → Python interpreter (cross-platform). "
            "Linux cron + .sh is the conventional pattern for scheduled system tasks."
        ),
    },
    # ── 4.9 Remote access technologies ───────────────────────────────────────
    {
        "id": "c2d4-025",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A remote worker reports that their company laptop cannot reach internal resources "
            "via the corporate VPN. The technician needs to take full control of the desktop "
            "to troubleshoot without requiring the user to install additional software (the "
            "user is on Windows 10 Pro). Which built-in remote-assistance tool should the "
            "technician use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Microsoft Remote Assistance (MSRA / Quick Assist)",
                "correct": True,
                "rationale": "Correct. Microsoft Remote Assistance (msra.exe) and its successor Quick Assist are built into Windows 10 and require no additional software. They allow a helper to view or control the user's session with the user's consent.",
            },
            {
                "id": "b",
                "text": "Remote Desktop Protocol (RDP)",
                "correct": False,
                "rationale": "Incorrect. RDP (mstsc.exe) creates a new session, typically locking the physical console. It is not designed for shared-view troubleshooting and requires the helper to know the user's credentials.",
            },
            {
                "id": "c",
                "text": "SSH with X11 forwarding",
                "correct": False,
                "rationale": "Incorrect. SSH with X11 forwarding is a Linux/macOS tool for forwarding graphical applications — it is not built into Windows 10 by default and is not relevant for Windows desktop sharing.",
            },
            {
                "id": "d",
                "text": "VNC server installed on the user's machine",
                "correct": False,
                "rationale": "Incorrect. VNC requires installing server software on the remote machine — the question specifies no additional software. MSRA/Quick Assist is already present.",
            },
        ],
        "explanation": (
            "Remote access tools: RDP — full session takeover, requires credentials; MSRA/Quick Assist — shared/view-only or control session with user consent, built-in; "
            "VNC — cross-platform screen sharing, requires software install; SSH — encrypted CLI, Linux/macOS primary use; "
            "RMM tools — enterprise agent-based management; third-party (TeamViewer, Zoom) — cross-platform but require install."
        ),
    },
    {
        "id": "c2d4-026",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A security team is reviewing remote access methods used by IT staff. They flag "
            "one method for transmitting credentials in plain text, creating a significant "
            "eavesdropping risk on untrusted networks. Which remote access protocol is "
            "MOST likely being flagged?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SSH (Secure Shell)",
                "correct": False,
                "rationale": "Incorrect. SSH encrypts all traffic including credentials. It was specifically designed to replace Telnet precisely because Telnet transmitted credentials in plaintext.",
            },
            {
                "id": "b",
                "text": "RDP over TLS",
                "correct": False,
                "rationale": "Incorrect. Modern RDP uses TLS encryption for both authentication and session data, protecting credentials in transit.",
            },
            {
                "id": "c",
                "text": "Telnet",
                "correct": True,
                "rationale": "Correct. Telnet transmits all data — including usernames and passwords — as plain text. Any network device or attacker performing a packet capture can read credentials directly. It is flagged in any security review of remote access.",
            },
            {
                "id": "d",
                "text": "VPN with IPsec",
                "correct": False,
                "rationale": "Incorrect. IPsec VPN encrypts all traffic between endpoints. It is a security control, not a source of credential exposure.",
            },
        ],
        "explanation": (
            "Security considerations by method: Telnet — no encryption (plain text); FTP — credentials plain text; "
            "SSH — encrypted (replaces Telnet/rlogin); RDP — TLS encrypted (port 3389, restrict with NLA); "
            "VPN — encrypts tunnel (IPsec or TLS); VNC — encryption varies by implementation (often needs VPN wrapper); "
            "RMM tools — agent-based, encrypted, but broad attack surface if compromised."
        ),
    },
    {
        "id": "c2d4-027",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Remote access technologies",
        "stem": (
            "A managed service provider (MSP) uses a Remote Monitoring and Management (RMM) "
            "platform to silently deploy patches and run scripts on client systems. "
            "Which security consideration is MOST unique to RMM compared to RDP or VNC?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RMM sessions are unencrypted, unlike RDP and VNC.",
                "correct": False,
                "rationale": "Incorrect. Enterprise RMM platforms (Kaseya, ConnectWise Automate, NinjaRMM) use encrypted communications. Lack of encryption is not a distinctive RMM risk.",
            },
            {
                "id": "b",
                "text": "RMM agents run silently with elevated privileges on all managed endpoints, making a compromised RMM server a single point of control over every client.",
                "correct": True,
                "rationale": "Correct. RMM agents typically run as SYSTEM or root on managed endpoints. A compromised RMM platform (like the 2021 Kaseya VSA attack) gives an attacker the ability to execute code on thousands of endpoints simultaneously — far beyond the blast radius of a single RDP compromise.",
            },
            {
                "id": "c",
                "text": "RMM requires the end user to approve each connection, increasing friction compared to RDP.",
                "correct": False,
                "rationale": "Incorrect. RMM agents operate silently and do not require per-session end-user approval — that is actually a security concern, not a mitigation. It is RMM's silent/unattended access that creates risk, not user-approval friction.",
            },
            {
                "id": "d",
                "text": "RMM tools use port 3389, creating the same firewall exposure as RDP.",
                "correct": False,
                "rationale": "Incorrect. RMM platforms use their own cloud relay infrastructure and agents, not port 3389 (which is RDP's port). Their attack surface is different from direct RDP exposure.",
            },
        ],
        "explanation": (
            "RMM platforms provide powerful unattended management at scale but concentrate risk: a single compromised RMM server "
            "gives attackers privileged code execution on all managed endpoints. MSPs must protect RMM with MFA, IP whitelisting, "
            "and least-privilege agent accounts. The 2021 Kaseya VSA attack demonstrated this supply-chain/RMM risk vector."
        ),
    },
    # ── Multiple-response questions (5) ───────────────────────────────────────
    {
        "id": "c2d4-028",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A help desk manager wants to ensure tickets contain all required fields per "
            "CompTIA A+ best practices. Select the THREE items that MUST be recorded "
            "in every support ticket. (Choose THREE.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "User information (name, contact details, department)",
                "correct": True,
                "rationale": "Correct. User information is a mandatory ticket field — needed to contact the user, track recurrence, and assign accountability.",
            },
            {
                "id": "b",
                "text": "Description of the problem (clear and concise)",
                "correct": True,
                "rationale": "Correct. An accurate problem description is foundational to diagnosis, escalation, and future knowledge-base reuse.",
            },
            {
                "id": "c",
                "text": "Technician's home phone number",
                "correct": False,
                "rationale": "Incorrect. Personal contact information for the technician is not a required ticket field and would violate privacy best practices.",
            },
            {
                "id": "d",
                "text": "Device information (make/model, serial/asset number, OS)",
                "correct": True,
                "rationale": "Correct. Device information allows technicians to research known issues, match warranty records, and apply device-specific solutions.",
            },
        ],
        "explanation": (
            "CompTIA A+ ticketing required fields include: user info, device info, problem description, category, severity/priority, "
            "escalation level (if applicable), and resolution. Clear, concise communication in each field improves both current resolution "
            "and future knowledge-base quality."
        ),
    },
    {
        "id": "c2d4-029",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "An organization is designing a backup strategy. Select the TWO statements that "
            "are TRUE about the 3-2-1 backup rule. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "It requires at least three copies of data stored on at least two different media types.",
                "correct": True,
                "rationale": "Correct. The '3-2' portion of 3-2-1 specifies 3 copies on 2 different media (e.g., internal disk + external tape/cloud) to protect against single-media failure.",
            },
            {
                "id": "b",
                "text": "All three copies must be stored in the same physical location for rapid recovery.",
                "correct": False,
                "rationale": "Incorrect. The '1' in 3-2-1 explicitly requires that at least one copy be stored off-site. Co-locating all copies defeats the disaster-recovery purpose of the rule.",
            },
            {
                "id": "c",
                "text": "At least one copy must be stored off-site or in the cloud.",
                "correct": True,
                "rationale": "Correct. The '1' in 3-2-1 mandates an off-site copy to survive site-level disasters such as fire, flood, or theft.",
            },
            {
                "id": "d",
                "text": "The rule requires daily full backups to be valid.",
                "correct": False,
                "rationale": "Incorrect. The 3-2-1 rule specifies copy count and location strategy, not backup frequency or type. Any backup type (full, incremental, differential) can satisfy it.",
            },
        ],
        "explanation": (
            "3-2-1: 3 copies, 2 different media, 1 off-site. It is agnostic to backup type or frequency. "
            "An extended variant, 3-2-1-1-0, adds 1 immutable/air-gapped copy and 0 backup errors (verified backups). "
            "The rule is the foundation of modern ransomware and disaster-recovery resilience."
        ),
    },
    {
        "id": "c2d4-030",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A technician is preparing to replace a GPU inside a tower PC. Select the TWO "
            "personal safety and component-protection measures that are MOST important "
            "BEFORE opening the case. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Power off the system and leave it plugged in to maintain chassis earth ground.",
                "correct": True,
                "rationale": "Correct. Powering off prevents electrical injury while leaving the plug in maintains the earth-ground reference for the ESD wrist strap through the power supply's safety ground.",
            },
            {
                "id": "b",
                "text": "Put on an ESD wrist strap connected to the chassis.",
                "correct": True,
                "rationale": "Correct. The ESD wrist strap provides a high-resistance path to ground, dissipating static charges that could damage sensitive components like the GPU.",
            },
            {
                "id": "c",
                "text": "Wear latex gloves to prevent fingerprints on the GPU PCB.",
                "correct": False,
                "rationale": "Incorrect. Latex gloves are not ESD-safe. Standard latex can generate and hold static charge. ESD-safe gloves are available but are not a CompTIA-specified requirement; an ESD strap and mat are the standard measures.",
            },
            {
                "id": "d",
                "text": "Place the GPU in a standard plastic bag for transport after removal.",
                "correct": False,
                "rationale": "Incorrect. Standard plastic bags are not antistatic and can generate static charge. Removed components must be stored in antistatic bags.",
            },
        ],
        "explanation": (
            "ESD protection toolkit: ESD wrist strap (technician ground), ESD mat (work surface ground), antistatic bags (component storage), "
            "proper grounding (chassis at earth ground via plugged-in, powered-off system). "
            "Standard plastic and latex are ESD hazards, not protections."
        ),
    },
    {
        "id": "c2d4-031",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "An e-commerce company in Germany processes EU customer credit card payments and "
            "stores customer health data from a wellness app. Select the TWO regulations that "
            "DIRECTLY govern data the company must comply with. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "GDPR (General Data Protection Regulation)",
                "correct": True,
                "rationale": "Correct. GDPR applies to any organization processing personal data of EU residents. The German company processing EU customer data is squarely within GDPR scope for all personal data categories including health data.",
            },
            {
                "id": "b",
                "text": "PCI DSS (Payment Card Industry Data Security Standard)",
                "correct": True,
                "rationale": "Correct. PCI DSS applies to any entity that stores, processes, or transmits payment card data. Processing EU customer credit card payments mandates PCI DSS compliance.",
            },
            {
                "id": "c",
                "text": "HIPAA (Health Insurance Portability and Accountability Act)",
                "correct": False,
                "rationale": "Incorrect. HIPAA is a U.S. federal law that applies to covered entities and business associates in the U.S. healthcare system. A German e-commerce company not operating in the U.S. healthcare space is not subject to HIPAA; GDPR covers health data in this EU context.",
            },
            {
                "id": "d",
                "text": "FISMA (Federal Information Security Modernization Act)",
                "correct": False,
                "rationale": "Incorrect. FISMA applies to U.S. federal agencies and their contractors. A private German e-commerce company is not subject to FISMA.",
            },
        ],
        "explanation": (
            "Data regulation applicability: GDPR — EU personal data (any company processing EU resident data); "
            "PCI DSS — payment card data (any entity, global); HIPAA — U.S. healthcare covered entities/BAs; "
            "FISMA — U.S. federal agencies. Regulated data types: PII (identity), PHI (health+identity), PCI (payment cards). "
            "Data retention requirements vary by regulation."
        ),
    },
    {
        "id": "c2d4-032",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A junior technician asks which script file types are natively supported on "
            "Windows without installing additional runtimes (beyond what ships with a "
            "default Windows 10 installation). Select the TWO correct answers. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": ".bat (batch files executed by cmd.exe)",
                "correct": True,
                "rationale": "Correct. cmd.exe and the Windows batch interpreter have shipped with every version of Windows. .bat files require no additional runtime.",
            },
            {
                "id": "b",
                "text": ".ps1 (PowerShell scripts executed by PowerShell)",
                "correct": True,
                "rationale": "Correct. Windows PowerShell (5.1) ships with Windows 10 by default. .ps1 scripts run natively without additional installs (execution policy may need adjustment).",
            },
            {
                "id": "c",
                "text": ".py (Python scripts)",
                "correct": False,
                "rationale": "Incorrect. Python is not installed by default on Windows 10. It must be separately downloaded and installed from python.org or the Microsoft Store.",
            },
            {
                "id": "d",
                "text": ".sh (Bash shell scripts)",
                "correct": False,
                "rationale": "Incorrect. Bash is not natively available on Windows 10 without enabling WSL or installing Git Bash. It is native to Linux/macOS.",
            },
        ],
        "explanation": (
            "Windows 10 native script support (no additional install): .bat/.cmd (cmd.exe), .ps1 (PowerShell 5.1), "
            ".vbs (Windows Script Host — deprecated in Windows 11 24H2). "
            "Python (.py), Ruby (.rb), and Bash (.sh) all require separate installation or WSL."
        ),
    },
    # ── Additional hard/expert questions to reach 34 total ───────────────────
    {
        "id": "c2d4-033",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "A data center manager observes that server inlet temperatures are consistently "
            "3–5 °C above recommended levels. Airflow measurements show hot exhaust air is "
            "recirculating back to server intakes. Which containment strategy BEST resolves "
            "this problem?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Increase computer room air conditioner (CRAC) setpoint temperature to adapt to the higher ambient.",
                "correct": False,
                "rationale": "Incorrect. Raising the CRAC setpoint addresses the symptom but not the root cause (hot-aisle/cold-aisle recirculation). Server inlet temperatures will remain elevated relative to supply air.",
            },
            {
                "id": "b",
                "text": "Implement hot-aisle/cold-aisle containment with blanking panels to prevent hot-exhaust recirculation.",
                "correct": True,
                "rationale": "Correct. Hot-aisle/cold-aisle containment directs cool supply air to server intakes (cold aisle) and captures hot exhaust in a separate hot aisle routed back to CRAC units. Blanking panels fill empty rack slots to prevent bypass airflow.",
            },
            {
                "id": "c",
                "text": "Add portable fans to increase general airflow in the room.",
                "correct": False,
                "rationale": "Incorrect. Portable fans increase turbulence and may worsen recirculation by mixing hot and cold air zones rather than separating them.",
            },
            {
                "id": "d",
                "text": "Reduce server utilization to lower heat output.",
                "correct": False,
                "rationale": "Incorrect. Reducing utilization is operationally impractical and treats the symptom rather than the infrastructure design problem causing recirculation.",
            },
        ],
        "explanation": (
            "Environmental controls for data centers: hot-aisle/cold-aisle containment (separate intake and exhaust airflow), "
            "blanking panels (prevent bypass airflow), proper temperature (ASHRAE recommends 18–27 °C inlet), "
            "humidity control (40–60% RH to prevent ESD and condensation), and ventilation. "
            "Airborne particulate protection uses enclosures and air filters."
        ),
    },
    {
        "id": "c2d4-034",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "An IT director asks why a change request form requires a 'risk analysis' section "
            "even for low-impact changes like installing an approved printer driver. "
            "Which response BEST explains the purpose of risk analysis in the change "
            "management process?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk analysis is only required for high-impact changes; low-impact changes can skip it to save time.",
                "correct": False,
                "rationale": "Incorrect. Risk analysis is required for all change requests regardless of perceived impact. What appears low-impact may have unforeseen dependencies (driver conflicts, certificate requirements) that analysis would surface.",
            },
            {
                "id": "b",
                "text": "Risk analysis documents potential negative outcomes, assigns a risk level, and justifies the rollback plan — enabling the CAB to make an informed approval decision for any change.",
                "correct": True,
                "rationale": "Correct. Risk analysis evaluates potential failure modes, their likelihood and impact, and assigns a risk level. Even for a printer driver, it might reveal a conflict with an existing security agent. This evidence is what the CAB uses to approve, reject, or modify the change.",
            },
            {
                "id": "c",
                "text": "Risk analysis is a legal requirement under HIPAA and must be included for regulatory compliance.",
                "correct": False,
                "rationale": "Incorrect. While HIPAA requires a security risk analysis for covered entities, the change-management risk analysis described in CompTIA A+ is an IT governance best practice, not specifically a HIPAA mandate applied to every IT change.",
            },
            {
                "id": "d",
                "text": "Risk analysis is used to determine the budget required for the change, not to assess technical risk.",
                "correct": False,
                "rationale": "Incorrect. Budget estimation may be part of a change request but is distinct from risk analysis. Risk analysis specifically evaluates the probability and impact of the change causing unintended harm.",
            },
        ],
        "explanation": (
            "Change management risk analysis: identifies what could go wrong, assesses probability and impact, "
            "assigns a risk level (low/medium/high/critical), and informs the rollback plan. "
            "The CAB uses this to make informed approval decisions. All changes — even seemingly trivial ones — "
            "require risk analysis because unknown dependencies can cause significant outages."
        ),
    },
]
