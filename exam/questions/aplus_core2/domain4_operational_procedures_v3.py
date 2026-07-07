"""
CompTIA A+ Core 2 (220-1202) — Domain 4: Operational Procedures
47 new practice questions (v3) aligned to objectives 4.1–4.9.
IDs: c2d4v3-001 through c2d4v3-047
"""

QUESTIONS = [
    # ── 4.1 Documentation / ticketing / asset management ──────────────────────
    {
        "id": "c2d4v3-001",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A technician resolves a recurring blue-screen issue by updating a NIC driver. "
            "Before closing the ticket, the technician wants to maximize its value as a "
            "future knowledge-base reference. Which action is MOST important to complete "
            "before marking the ticket resolved?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Document the root cause (outdated NIC driver), the exact steps taken to resolve it, and the driver version installed, then obtain end-user sign-off.",
                "correct": True,
                "rationale": "Correct. A ticket doubles as a KB article when it contains root cause, resolution steps with specifics (driver version), and user acceptance. This allows future technicians to reproduce the fix quickly.",
            },
            {
                "id": "b",
                "text": "Close the ticket immediately; any technician can determine what was done from system logs.",
                "correct": False,
                "rationale": "Incorrect. System logs are not part of the ticket record and require separate access. Closing without documentation prevents KB reuse and misses end-user acceptance verification.",
            },
            {
                "id": "c",
                "text": "Escalate the ticket to Tier 2 to verify the fix holds for 30 days before closing.",
                "correct": False,
                "rationale": "Incorrect. Escalation is for issues beyond the current tier's capability, not for routine monitoring after a successful fix. Thirty-day holds are not standard ticketing practice.",
            },
            {
                "id": "d",
                "text": "Update only the category field to 'Network — Driver' and close the ticket.",
                "correct": False,
                "rationale": "Incorrect. Updating the category without documenting root cause, fix steps, and user sign-off leaves the ticket incomplete as a knowledge record.",
            },
        ],
        "explanation": (
            "Complete ticket closure requires: accurate problem description, documented root cause, step-by-step resolution, "
            "any parts or software versions used, escalation history, and end-user acceptance. "
            "This transforms the ticket into a searchable KB article for future incidents."
        ),
    },
    {
        "id": "c2d4v3-002",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "A company deploys 50 new laptops. The IT manager wants to ensure the organization "
            "can track warranty expiration, assigned user, and device location throughout each "
            "laptop's life cycle. Which procurement-phase action creates the foundation for "
            "ongoing asset tracking?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Record the serial number, assign an asset tag, and enter the warranty end date and assigned user in the asset management database at the time of deployment.",
                "correct": True,
                "rationale": "Correct. Entering serial number, asset tag, warranty data, and user assignment at deployment creates the authoritative record that links the physical device to all subsequent tracking (moves, repairs, decommissioning).",
            },
            {
                "id": "b",
                "text": "Wait for the first repair ticket to create the asset record so only active devices are tracked.",
                "correct": False,
                "rationale": "Incorrect. Waiting for a repair ticket means the device is untracked from deployment until a problem occurs, creating an audit gap and potential for unaccounted assets.",
            },
            {
                "id": "c",
                "text": "Photograph each laptop and store the photos in a shared drive folder named by purchase date.",
                "correct": False,
                "rationale": "Incorrect. Photos without structured database entries do not support searchable warranty lookups, user assignment queries, or automated expiration alerts.",
            },
            {
                "id": "d",
                "text": "Ask department managers to self-report any device issues so IT can build an ad-hoc inventory.",
                "correct": False,
                "rationale": "Incorrect. Ad-hoc, user-reported inventory is unreliable and incomplete. Asset tracking must be driven by IT at the point of deployment, not reactively.",
            },
        ],
        "explanation": (
            "Asset management life cycle: procurement → tagging → database entry (serial, asset tag, warranty, assigned user) "
            "→ moves/adds/changes tracked → decommissioning (data sanitization, disposal). "
            "The deployment-time entry is the anchor for all downstream tracking activities."
        ),
    },
    {
        "id": "c2d4v3-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A technician updates a workstation's BIOS firmware without submitting a change "
            "request, reasoning that the task was 'minor.' The update corrupts the firmware "
            "and bricks the workstation. Which documentation failure MOST directly caused "
            "this outcome to be unrecoverable in a timely manner?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Absence of a rollback plan documented in a change request",
                "correct": True,
                "rationale": "Correct. A proper change request requires a rollback plan — in this case, the prior BIOS version download or flash procedure. Without it, recovery steps were undefined and had to be improvised, increasing downtime.",
            },
            {
                "id": "b",
                "text": "Absence of an asset tag on the workstation",
                "correct": False,
                "rationale": "Incorrect. While asset tags are important, missing one does not affect the ability to recover from a failed firmware update. The critical failure was missing a rollback plan.",
            },
            {
                "id": "c",
                "text": "Absence of a network topology diagram",
                "correct": False,
                "rationale": "Incorrect. Network topology diagrams document network layout; they have no bearing on BIOS firmware recovery procedures.",
            },
            {
                "id": "d",
                "text": "Absence of an SOP for new-user setup",
                "correct": False,
                "rationale": "Incorrect. New-user setup SOPs govern onboarding tasks, not firmware update procedures. The missing document type was a change request with a rollback plan.",
            },
        ],
        "explanation": (
            "Every change — including 'minor' ones like BIOS updates — should follow change management. "
            "The rollback plan is the document that enables rapid recovery when a change fails. "
            "Bypassing the change request process removes both the approval gate and the safety net."
        ),
    },
    {
        "id": "c2d4v3-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "During a quarterly audit, an auditor discovers that 8 monitors appear in the "
            "asset database but cannot be physically located. The devices lack asset tags. "
            "Which asset management practice, if enforced at decommissioning, would have "
            "MOST directly prevented this discrepancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Updating the asset record to 'decommissioned' status and removing the asset tag upon disposal",
                "correct": True,
                "rationale": "Correct. Updating the asset record at decommissioning closes the life cycle in the database. Devices still listed as 'active' but physically disposed of create exactly the phantom-asset discrepancy found in the audit.",
            },
            {
                "id": "b",
                "text": "Performing a full backup of monitor firmware before disposal",
                "correct": False,
                "rationale": "Incorrect. Monitors typically do not have user-configurable firmware requiring backup. This action would not update the asset database to reflect disposal.",
            },
            {
                "id": "c",
                "text": "Publishing an AUP requiring employees to report lost equipment",
                "correct": False,
                "rationale": "Incorrect. An AUP sets usage rules; it cannot substitute for IT-driven asset lifecycle processes. User self-reporting is unreliable for managing decommissioned assets.",
            },
            {
                "id": "d",
                "text": "Encrypting the asset database to prevent unauthorized changes",
                "correct": False,
                "rationale": "Incorrect. Encryption protects the database from unauthorized access but does not ensure records are updated when assets are disposed of. The process failure is procedural, not a security issue.",
            },
        ],
        "explanation": (
            "Full asset life cycle management requires database updates at every phase: acquisition, assignment, move, repair, "
            "and decommissioning. Devices not marked decommissioned remain 'active' in the database indefinitely, "
            "creating phantom records that fail audits and waste investigation time."
        ),
    },
    # ── 4.2 Change management ─────────────────────────────────────────────────
    {
        "id": "c2d4v3-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "A technician needs to migrate a file server to new hardware during a Saturday "
            "maintenance window. The change advisory board (CAB) has approved the change. "
            "Which element of the approved change request is MOST important for minimizing "
            "risk during the actual execution?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The documented rollback plan with specific steps to revert to the original server if migration fails",
                "correct": True,
                "rationale": "Correct. The rollback plan is the pre-approved safety net activated when execution fails. During execution, having a tested and documented rollback procedure is the single most risk-reducing element because it defines the recovery path without improvisation.",
            },
            {
                "id": "b",
                "text": "The list of all users who will be affected by the migration",
                "correct": False,
                "rationale": "Incorrect. The affected-user list is important for communication but does not mitigate technical risk during execution. If the migration fails, the rollback plan—not the user list—guides recovery.",
            },
            {
                "id": "c",
                "text": "The CAB approval signature confirming authorization",
                "correct": False,
                "rationale": "Incorrect. CAB approval authorizes the change but does not provide execution guidance. During the maintenance window, the rollback plan is the operative risk-mitigation document.",
            },
            {
                "id": "d",
                "text": "The purpose and scope section explaining why the migration is needed",
                "correct": False,
                "rationale": "Incorrect. Purpose and scope are required for CAB evaluation but are informational, not operational. They do not reduce risk during execution.",
            },
        ],
        "explanation": (
            "Change request components: purpose/scope, affected systems/users, risk analysis, responsible staff, "
            "scheduled date/time window, sandbox test results, end-user notification plan, and rollback plan. "
            "The rollback plan is the most operationally critical component during execution because it provides "
            "pre-approved steps to restore service quickly when a change does not go as planned."
        ),
    },
    {
        "id": "c2d4v3-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "A developer proposes deploying a critical security patch to all production web "
            "servers immediately without going through the change advisory board (CAB), "
            "arguing the patch fixes an actively exploited zero-day. Which response BEST "
            "balances security urgency with change management discipline?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Invoke the emergency change process: obtain verbal/emergency CAB approval, document the change simultaneously, and complete full documentation within 24 hours.",
                "correct": True,
                "rationale": "Correct. Most change management frameworks include an emergency change path for active threats. Emergency approval (condensed CAB, verbal approval from designated authority) allows rapid deployment while maintaining accountability and documentation obligations.",
            },
            {
                "id": "b",
                "text": "Deploy immediately with no documentation since security emergencies override all change processes.",
                "correct": False,
                "rationale": "Incorrect. Security emergencies accelerate the process but do not eliminate it. Undocumented emergency changes create audit failures, unknown rollback procedures, and post-incident review gaps.",
            },
            {
                "id": "c",
                "text": "Wait for the next scheduled CAB meeting next Tuesday since all changes must follow the standard weekly cycle.",
                "correct": False,
                "rationale": "Incorrect. Waiting a week with an actively exploited vulnerability on production web servers is operationally and legally indefensible. Emergency change procedures exist precisely for this situation.",
            },
            {
                "id": "d",
                "text": "Apply the patch to production and submit a change request afterward as a 'retroactive' approval.",
                "correct": False,
                "rationale": "Incorrect. Retroactive approval defeats the purpose of change management—the CAB cannot evaluate risk or modify an already-executed change. This practice is generally prohibited and creates audit issues.",
            },
        ],
        "explanation": (
            "Change management frameworks (ITIL, CompTIA) recognize emergency change processes for active security threats. "
            "Key elements: condensed approval (emergency CAB or designated authority), simultaneous or same-day documentation, "
            "rollback plan still required. The emergency path preserves accountability without sacrificing speed when genuinely needed."
        ),
    },
    {
        "id": "c2d4v3-007",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "After a successful database migration, the responsible technician closes the "
            "change request and submits a post-implementation review. Which information is "
            "MOST valuable to include in the post-implementation review?"
        ),
        "options": [
            {
                "id": "a",
                "text": "What went as planned, what deviated from the plan, lessons learned, and whether the rollback plan needs updating",
                "correct": True,
                "rationale": "Correct. Post-implementation reviews capture actual vs. planned outcomes, deviations, and lessons learned. Updating the rollback plan based on real experience improves future change readiness.",
            },
            {
                "id": "b",
                "text": "The names of all employees who were notified about the change window",
                "correct": False,
                "rationale": "Incorrect. User notification records belong in the change request itself, not the post-implementation review. The review focuses on execution quality and process improvement.",
            },
            {
                "id": "c",
                "text": "A statement that the change succeeded with no further action required",
                "correct": False,
                "rationale": "Incorrect. A simple success declaration provides no actionable intelligence for future changes. Even successful changes often have execution variations worth capturing.",
            },
            {
                "id": "d",
                "text": "The CAB members who approved the change and their approval timestamps",
                "correct": False,
                "rationale": "Incorrect. Approval records are part of the change request, not the post-implementation review. The review is forward-looking — how to improve the next change.",
            },
        ],
        "explanation": (
            "Post-implementation reviews close the change management feedback loop: compare actual outcomes to the plan, "
            "document deviations (even minor ones), capture lessons learned, and update runbooks and rollback procedures. "
            "This continuous improvement cycle reduces risk in future changes."
        ),
    },
    # ── 4.3 Backup and recovery ───────────────────────────────────────────────
    {
        "id": "c2d4v3-008",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backup types",
        "stem": (
            "A company runs a full backup every Sunday. On Wednesday morning a ransomware "
            "attack encrypts all data. Recovery must be as fast as possible and minimize "
            "the number of backup sets to restore. Which backup strategy, if used Monday "
            "through Tuesday, would result in the FEWEST restore operations?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Incremental backups — requires Sunday full + Monday incremental + Tuesday incremental (3 sets)",
                "correct": False,
                "rationale": "Incorrect. Incremental backups require the full plus every incremental since the last full, resulting in 3 restore operations in this scenario — not the minimum possible.",
            },
            {
                "id": "b",
                "text": "Differential backups — requires Sunday full + Tuesday differential only (2 sets)",
                "correct": True,
                "rationale": "Correct. Each differential contains all changes since the last full, so only the most recent differential is needed alongside the full. This always results in exactly 2 restore sets regardless of how many days have elapsed since the last full.",
            },
            {
                "id": "c",
                "text": "Copy backup — requires restoring each copy individually, more sets than incremental",
                "correct": False,
                "rationale": "Incorrect. Copy backups capture a full point-in-time copy without affecting archive bits. They are not typically used in rotation strategies to minimize restore sets.",
            },
            {
                "id": "d",
                "text": "Both strategies require the same number of restore operations.",
                "correct": False,
                "rationale": "Incorrect. Incremental requires full + N incrementals; differential requires full + 1 differential. After multiple days, differential consistently requires fewer restore operations.",
            },
        ],
        "explanation": (
            "Restore set counts: Differential = always 2 (last full + most recent differential). "
            "Incremental = 1 + N (last full + all N incrementals since). "
            "Differential trades larger daily backup size for faster, simpler restore. "
            "Incremental trades smaller daily backups for more complex restore requiring every set in order."
        ),
    },
    {
        "id": "c2d4v3-009",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backup types",
        "stem": (
            "A backup administrator wants to combine the fast backup speed of incrementals "
            "with the single-set restore speed of a full backup, without re-reading all "
            "source data daily. Which backup method achieves this goal?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Differential backup",
                "correct": False,
                "rationale": "Incorrect. Differential backups still require restoring two sets (full + differential) and do not produce a single consolidated restore set without re-reading all source data.",
            },
            {
                "id": "b",
                "text": "Synthetic full backup",
                "correct": True,
                "rationale": "Correct. A synthetic full backup is assembled on the backup server by merging the last full with subsequent incrementals — without reading source data again. The result is a current full-backup set that can be restored from a single operation.",
            },
            {
                "id": "c",
                "text": "GFS (Grandfather-Father-Son) rotation",
                "correct": False,
                "rationale": "Incorrect. GFS is a tape-rotation schedule that organizes retention of daily/weekly/monthly sets. It is not a backup type and does not produce synthetic consolidated backups.",
            },
            {
                "id": "d",
                "text": "Incremental backup with deduplication",
                "correct": False,
                "rationale": "Incorrect. Deduplication reduces storage by eliminating redundant data blocks but does not merge the sets into a single restorable full backup. Restore still requires all incremental sets.",
            },
        ],
        "explanation": (
            "Synthetic full: backup software reads the previous full + all incrementals from the backup repository, "
            "merges them server-side, and writes a new full backup without touching the source systems. "
            "Benefits: source I/O preserved, full-backup restore speed, incremental backup windows. "
            "Common in enterprise backup products (Veeam, Commvault, Veritas)."
        ),
    },
    {
        "id": "c2d4v3-010",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "A small law firm follows the 3-2-1 backup rule. They have: (1) a local NAS, "
            "(2) a USB external drive stored in the office, and (3) a cloud backup service. "
            "A flood damages the office over a holiday weekend, destroying both on-site "
            "storage devices. Which copy survives and satisfies the 3-2-1 rule's intent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The cloud backup copy survives, demonstrating the off-site requirement of the 3-2-1 rule.",
                "correct": True,
                "rationale": "Correct. The '1' in 3-2-1 requires at least one copy stored off-site. The cloud backup is geographically separate and survives the site-level disaster, enabling full data recovery.",
            },
            {
                "id": "b",
                "text": "Both the NAS and USB drive survive because they used different media types.",
                "correct": False,
                "rationale": "Incorrect. Different media types satisfy the '2' requirement but both devices are in the same physical location, so a site-level disaster like a flood destroys both regardless of media type.",
            },
            {
                "id": "c",
                "text": "None of the copies survive because the 3-2-1 rule requires all three copies to be off-site.",
                "correct": False,
                "rationale": "Incorrect. The 3-2-1 rule requires only ONE copy off-site, not all three. The rule explicitly allows two on-site copies on different media.",
            },
            {
                "id": "d",
                "text": "The USB drive survives because external drives are classified as off-site storage.",
                "correct": False,
                "rationale": "Incorrect. An external USB drive stored in the same office is on-site storage, not off-site. Off-site means a physically separate geographic location.",
            },
        ],
        "explanation": (
            "3-2-1 rule breakdown: '3' = three copies total; '2' = stored on two different media types (protects against single-media failure); "
            "'1' = at least one copy off-site (protects against site-level disaster). "
            "Cloud storage is the most common modern off-site solution. "
            "An external drive in the same building does not satisfy the off-site requirement."
        ),
    },
    {
        "id": "c2d4v3-011",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "In a Grandfather-Father-Son (GFS) tape rotation, a technician is labeling "
            "tapes for a week. Monday through Thursday tapes will be reused after one week; "
            "Friday tapes will be kept for one month; the last Friday tape of the month "
            "will be archived for one year. Which tier label correctly maps to 'Father'?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Monday through Thursday daily tapes (reused weekly)",
                "correct": False,
                "rationale": "Incorrect. Daily tapes reused weekly are 'Son' tapes — the most granular tier in the GFS hierarchy.",
            },
            {
                "id": "b",
                "text": "Friday weekly tapes retained for one month",
                "correct": True,
                "rationale": "Correct. 'Father' tapes in GFS are the weekly tapes, typically taken on the last business day of the week and retained for one month before being recycled.",
            },
            {
                "id": "c",
                "text": "Last Friday of the month tape archived for one year",
                "correct": False,
                "rationale": "Incorrect. Monthly tapes retained long-term (typically one year) are 'Grandfather' tapes — the top tier of the GFS hierarchy.",
            },
            {
                "id": "d",
                "text": "All tapes, because GFS does not differentiate between retention tiers.",
                "correct": False,
                "rationale": "Incorrect. GFS is defined by exactly three differentiated retention tiers: daily (Son), weekly (Father), and monthly (Grandfather), each with progressively longer retention periods.",
            },
        ],
        "explanation": (
            "GFS tape tiers: Son = daily backups, retained ~1 week, highest rotation frequency; "
            "Father = weekly backups (end-of-week), retained ~1 month; "
            "Grandfather = monthly backups (end-of-month), retained ~1 year or longer. "
            "GFS manages media reuse to balance retention coverage against tape/storage cost."
        ),
    },
    # ── 4.4 Safety procedures ────────────────────────────────────────────────
    {
        "id": "c2d4v3-012",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A technician is called to replace a laptop keyboard in a customer's home office. "
            "No ESD mat or wrist strap is available on site. Which improvised technique BEST "
            "reduces ESD risk during the repair?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Periodically touch an unpainted metal surface of the powered-off, plugged-in laptop chassis before and during handling components.",
                "correct": True,
                "rationale": "Correct. Touching unpainted metal on a plugged-in (but off) chassis repeatedly equalizes the technician's electrostatic potential with ground. While not as effective as a wrist strap, it is the best available improvised method.",
            },
            {
                "id": "b",
                "text": "Work faster to minimize the time components are exposed to static.",
                "correct": False,
                "rationale": "Incorrect. Working quickly does not reduce static charge; it increases the chance of error. ESD damage occurs instantly upon contact — speed provides no protection.",
            },
            {
                "id": "c",
                "text": "Use a standard rubber mat as an ESD substitute work surface.",
                "correct": False,
                "rationale": "Incorrect. Standard rubber mats are insulators, not ESD-dissipative materials. They can hold static charge and are not a substitute for a grounded anti-static mat.",
            },
            {
                "id": "d",
                "text": "Hold components by the edge connectors to avoid touching circuit traces.",
                "correct": False,
                "rationale": "Incorrect. Handling by edge connectors prevents fingerprint contamination but does not prevent ESD. Static discharge happens from the technician's body to the component regardless of where it is held.",
            },
        ],
        "explanation": (
            "Best ESD practice: wrist strap + mat + grounded chassis. When equipment is unavailable, periodically touching "
            "an unpainted grounded metal surface (plugged-in chassis) is the best improvised technique. "
            "Always hold boards by edges, never flex them, and store removed parts in antistatic bags."
        ),
    },
    {
        "id": "c2d4v3-013",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A technician needs to lift a server rack enclosure (approximately 45 kg / 100 lb) "
            "with the help of a colleague. Which lifting technique BEST prevents personal injury?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Bend at the knees, keep the back straight, grip the object firmly, and lift using leg muscles while keeping the load close to the body.",
                "correct": True,
                "rationale": "Correct. Safe manual-handling technique uses leg muscles (stronger and less injury-prone than back muscles), maintains a straight back, keeps the load close to reduce lever-arm torque on the spine, and uses a firm grip.",
            },
            {
                "id": "b",
                "text": "Bend at the waist to get close to the object, then straighten the back while lifting.",
                "correct": False,
                "rationale": "Incorrect. Bending at the waist concentrates load stress on the lumbar spine and is the most common cause of back injuries during lifting.",
            },
            {
                "id": "c",
                "text": "Lift quickly in one smooth motion to reduce the total time the load stresses the back.",
                "correct": False,
                "rationale": "Incorrect. Rapid lifting increases peak force on the spine and reduces control. Controlled, deliberate movement is safer than speed.",
            },
            {
                "id": "d",
                "text": "Have one person lift the front while the other steadies from the rear, regardless of height difference.",
                "correct": False,
                "rationale": "Incorrect. A significant height difference between co-lifters creates uneven load distribution and risks the object tipping or one person over-extending. Both lifters should be at comparable heights or use a mechanical aid.",
            },
        ],
        "explanation": (
            "CompTIA A+ safe lifting rules: use proper lifting technique (legs, not back), get assistance for heavy items, "
            "use equipment (dollies, lift tables) when available, keep load close to body, and never twist the waist while lifting. "
            "For rack equipment, use rack-mounted slide rails and cable management rather than repeated manual lifting."
        ),
    },
    # ── 4.5 Environmental impacts and controls ────────────────────────────────
    {
        "id": "c2d4v3-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "A server room's humidity sensor reads 15% RH. The IT manager is concerned "
            "about equipment reliability. Which risk is MOST directly associated with "
            "this low-humidity environment?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Condensation forming on circuit boards causing short circuits",
                "correct": False,
                "rationale": "Incorrect. Condensation results from high humidity (above ~60% RH), not low humidity. Low humidity does not cause liquid condensation on electronics.",
            },
            {
                "id": "b",
                "text": "Increased electrostatic discharge (ESD) events damaging components",
                "correct": True,
                "rationale": "Correct. Very low humidity (below ~30–35% RH) significantly increases ESD risk because dry air does not dissipate static charge efficiently, allowing large static potentials to build up on surfaces and personnel.",
            },
            {
                "id": "c",
                "text": "Accelerated corrosion of metallic connectors and traces",
                "correct": False,
                "rationale": "Incorrect. Corrosion is primarily driven by high humidity and contaminants, not low humidity. Dry environments actually reduce moisture-driven corrosion.",
            },
            {
                "id": "d",
                "text": "Reduced cooling efficiency leading to thermal throttling",
                "correct": False,
                "rationale": "Incorrect. Cooling efficiency in air-cooled data centers relates to airflow, temperature, and heat load — not relative humidity. Humidity outside normal range does not directly reduce cooling capacity.",
            },
        ],
        "explanation": (
            "Optimal data center humidity: 40–60% RH per ASHRAE guidelines. "
            "Too low (<30%): high ESD risk (static builds up in dry air). "
            "Too high (>60%): condensation, corrosion, mold risk. "
            "Both extremes damage electronics; humidity monitoring and control are essential environmental controls."
        ),
    },
    {
        "id": "c2d4v3-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "A technician is asked to properly dispose of an old CRT monitor containing "
            "lead and a depleted toner cartridge from a laser printer. Which disposal "
            "approach is MOST compliant with environmental regulations for BOTH items?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Place both in office recycling bins since the monitor screen is glass and the cartridge is plastic.",
                "correct": False,
                "rationale": "Incorrect. CRT monitors contain lead (in the cathode ray tube), a regulated hazardous material. Toner cartridges may contain fine particulate toner and chemical components — neither belongs in standard recycling.",
            },
            {
                "id": "b",
                "text": "Return the toner cartridge to the manufacturer's take-back program and send the CRT to a certified e-waste recycler.",
                "correct": True,
                "rationale": "Correct. Manufacturer take-back programs handle toner cartridges in compliance with environmental standards. Certified e-waste recyclers handle CRTs under regulations governing lead and other hazardous materials in electronics.",
            },
            {
                "id": "c",
                "text": "Landfill both items after removing all visible wiring to reduce hazard.",
                "correct": False,
                "rationale": "Incorrect. Removing wiring does not eliminate hazardous materials (lead, toner chemicals). Landfill disposal of CRTs and toner is regulated and typically illegal without proper processing.",
            },
            {
                "id": "d",
                "text": "Incinerate both items to minimize volume before disposal.",
                "correct": False,
                "rationale": "Incorrect. Incineration of CRTs and toner can release toxic compounds (lead oxides, VOCs). Regulated disposal channels must be used — not incineration.",
            },
        ],
        "explanation": (
            "Hazardous IT disposal categories: CRTs (lead), batteries (Li-ion, NiMH, lead-acid), toner cartridges, "
            "fluorescent backlights (mercury). All require certified e-waste recyclers or manufacturer take-back programs. "
            "SDS (Safety Data Sheet) provides handling and disposal guidance for specific materials. "
            "Improper disposal creates regulatory liability under EPA and state laws."
        ),
    },
    {
        "id": "c2d4v3-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Environmental controls",
        "stem": (
            "During a site survey, a technician notices servers near a window that receives "
            "direct sunlight for four hours each day, causing inlet temperatures to spike to "
            "35 °C. The CRAC unit is working correctly. Which environmental control change "
            "MOST directly addresses the root cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Increase CRAC output to compensate for the solar heat gain.",
                "correct": False,
                "rationale": "Incorrect. Increasing CRAC output treats the symptom (high temperature) but not the root cause (solar heat entering through the window). It also increases energy cost unnecessarily.",
            },
            {
                "id": "b",
                "text": "Block or eliminate the direct sunlight reaching the servers via window coverings, relocating servers, or applying UV-blocking film.",
                "correct": True,
                "rationale": "Correct. The root cause is radiant solar heat gain. Blocking the source (window covering, film, or relocation) eliminates the heat input rather than overworking the cooling system to compensate.",
            },
            {
                "id": "c",
                "text": "Add a second UPS to handle the increased power draw from higher server fan speeds.",
                "correct": False,
                "rationale": "Incorrect. A UPS provides power conditioning and battery backup; it has no effect on thermal management. Adding capacity for fans treats a secondary symptom, not the root cause.",
            },
            {
                "id": "d",
                "text": "Install additional RAM in the servers to reduce CPU utilization and heat output.",
                "correct": False,
                "rationale": "Incorrect. The heat spike is caused by external solar radiation, not by server workload. Additional RAM will not reduce radiant heat gain from sunlight.",
            },
        ],
        "explanation": (
            "Environmental controls include temperature management (ASHRAE target 18–27 °C inlet), airflow containment, "
            "and source-elimination for heat. Direct sunlight is a heat source that must be physically blocked. "
            "Treating root causes (heat elimination) is more effective and energy-efficient than compensating "
            "with increased cooling output."
        ),
    },
    # ── 4.6 Incident response / licensing / regulated data ───────────────────
    {
        "id": "c2d4v3-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A technician is imaging a hard drive for forensic analysis. After creating the "
            "image with dd, the technician computes an MD5 hash of the source drive and the "
            "image file and finds the hashes match. Later, opposing counsel challenges the "
            "image's integrity. Which chain-of-custody record MOST directly refutes the "
            "integrity challenge?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The forensic imaging tool's vendor documentation",
                "correct": False,
                "rationale": "Incorrect. Vendor documentation describes how the tool works generally; it does not prove this specific image was not tampered with after creation.",
            },
            {
                "id": "b",
                "text": "The original matching MD5 hash values documented at the time of imaging, signed and timestamped in the chain-of-custody log",
                "correct": True,
                "rationale": "Correct. A documented, timestamped hash comparison at the time of imaging proves the image was an exact copy of the source at that moment. If the current image hash still matches, integrity is demonstrated. The chain-of-custody log with signatures and timestamps provides legal admissibility.",
            },
            {
                "id": "c",
                "text": "The technician's personal notes stating the image was not modified",
                "correct": False,
                "rationale": "Incorrect. Personal notes without a documented cryptographic hash are testimonial and subject to credibility challenges. They do not provide mathematical proof of integrity.",
            },
            {
                "id": "d",
                "text": "A screenshot of the imaging software showing 'copy complete'",
                "correct": False,
                "rationale": "Incorrect. A completion screenshot confirms the tool ran but provides no cryptographic proof that the image matches the source or that it was not altered afterward.",
            },
        ],
        "explanation": (
            "Forensic chain of custody requires: hash verification (MD5 or SHA-256) computed immediately after imaging, "
            "documented alongside the source hash, with technician signature and timestamp. "
            "The hash is the cryptographic integrity anchor — if the image hash matches the original documented hash, "
            "bit-for-bit fidelity is mathematically proven. All access to evidence must also be logged."
        ),
    },
    {
        "id": "c2d4v3-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A manager discovers an employee has stored a large volume of confidential "
            "competitor pricing data on a company workstation — data that appears to have "
            "been exfiltrated from a competitor. The manager asks the help desk technician "
            "to delete the files immediately to avoid liability. What should the technician do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Delete the files as instructed, then document the deletion in the ticket.",
                "correct": False,
                "rationale": "Incorrect. Deleting the files destroys evidence of a potential crime or civil violation. Even when instructed by a manager, destroying evidence may constitute obstruction of justice.",
            },
            {
                "id": "b",
                "text": "Refuse to delete the files; escalate to legal/HR/information security and preserve the workstation as-is, documenting the refusal and reasoning.",
                "correct": True,
                "rationale": "Correct. Suspected illegal content (including exfiltrated competitor data) must be preserved as potential evidence. The technician should escalate to the appropriate authority (legal, HR, CISO) and document the incident with timestamps. Deleting evidence at a manager's request could expose both the manager and the company to obstruction charges.",
            },
            {
                "id": "c",
                "text": "Copy the files to a personal drive for safekeeping before deleting them from the workstation.",
                "correct": False,
                "rationale": "Incorrect. Copying the files to a personal device violates chain of custody and could create additional legal exposure. Evidence must remain in controlled custody.",
            },
            {
                "id": "d",
                "text": "Quarantine the workstation from the network but proceed with deleting the files.",
                "correct": False,
                "rationale": "Incorrect. Network quarantine is the correct containment step but should not be paired with file deletion. Evidence must be preserved; the quarantine isolates the device without destroying data.",
            },
        ],
        "explanation": (
            "When encountering suspected illegal or sensitive content, technicians must: stop working on the device, "
            "do not alter or delete files, escalate to management/legal/law enforcement as appropriate, "
            "document all actions with timestamps, and maintain chain of custody. "
            "A manager's instruction to destroy evidence does not override legal or ethical obligations."
        ),
    },
    {
        "id": "c2d4v3-019",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "A retail company collects customer names, email addresses, and credit card "
            "numbers for online transactions. A data breach exposes all three data types. "
            "Which regulatory framework is PRIMARILY triggered by the exposure of the "
            "credit card numbers?"
        ),
        "options": [
            {
                "id": "a",
                "text": "HIPAA",
                "correct": False,
                "rationale": "Incorrect. HIPAA governs protected health information (PHI), not payment card data. Credit card numbers are not PHI.",
            },
            {
                "id": "b",
                "text": "GDPR",
                "correct": False,
                "rationale": "Incorrect. GDPR applies to the personal data (names, emails) of EU residents broadly, but the specific framework governing payment card number security is PCI DSS, which applies regardless of geography.",
            },
            {
                "id": "c",
                "text": "PCI DSS",
                "correct": True,
                "rationale": "Correct. PCI DSS (Payment Card Industry Data Security Standard) is the specific mandatory framework for any entity that stores, processes, or transmits payment card data. Exposure of card numbers triggers PCI DSS breach notification and assessment obligations.",
            },
            {
                "id": "d",
                "text": "FERPA",
                "correct": False,
                "rationale": "Incorrect. FERPA (Family Educational Rights and Privacy Act) governs student education records in the U.S. It has no applicability to retail payment card data.",
            },
        ],
        "explanation": (
            "Regulatory mapping by data type: credit/debit card numbers → PCI DSS (global, any entity accepting cards); "
            "health information + identity → PHI → HIPAA (U.S. healthcare); personal data of EU residents → GDPR; "
            "student education records → FERPA (U.S. education). "
            "A single breach can trigger multiple frameworks simultaneously (e.g., GDPR + PCI DSS for an EU cardholder breach)."
        ),
    },
    {
        "id": "c2d4v3-020",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "A software company purchases perpetual licenses for 25 seats of a design "
            "application. Six months later, the company hires 10 more designers and installs "
            "the software on their machines without purchasing additional licenses. "
            "Which term BEST describes this situation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "License compliance — the company is within its rights under the perpetual license.",
                "correct": False,
                "rationale": "Incorrect. A perpetual license for 25 seats permits installation on 25 machines. Installing on 35 machines without additional purchase exceeds the licensed seat count.",
            },
            {
                "id": "b",
                "text": "License violation / software piracy — the company has exceeded the purchased seat count.",
                "correct": True,
                "rationale": "Correct. Exceeding the purchased seat count of a software license constitutes a license violation, also called unlicensed use or software piracy. It exposes the company to audits, fines, and civil liability from the software vendor.",
            },
            {
                "id": "c",
                "text": "Open-source license compliance — perpetual licenses are equivalent to open-source licenses.",
                "correct": False,
                "rationale": "Incorrect. Perpetual licenses are commercial licenses granting permanent use rights for a specific seat count and version — they are fundamentally different from open-source licenses.",
            },
            {
                "id": "d",
                "text": "EULA expansion — the perpetual license EULA automatically scales with the company's growth.",
                "correct": False,
                "rationale": "Incorrect. Commercial EULAs do not automatically expand seat counts as a company grows. Additional licenses must be purchased or a volume agreement must be in place.",
            },
        ],
        "explanation": (
            "License types: perpetual (permanent use, specific version/seat count), subscription (time-limited, often per seat), "
            "concurrent/floating (limits simultaneous users), site license (unlimited installs at a location), "
            "open-source (free use, with varying copyleft/permissive obligations), EULA (defines legal terms). "
            "Exceeding seat counts in any model is a license violation subject to audits and penalties."
        ),
    },
    # ── 4.7 Communication and professionalism ─────────────────────────────────
    {
        "id": "c2d4v3-021",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A technician arrives at a user's workstation and discovers the user is on a "
            "critical conference call and cannot be interrupted. The technician needs to "
            "replace a faulty keyboard that is actively preventing work. Which action BEST "
            "reflects professionalism and respect for the user?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Wait quietly until the call ends, briefly explain the repair needed, obtain verbal consent, perform the replacement quickly, confirm functionality, and leave without disruption.",
                "correct": True,
                "rationale": "Correct. Waiting for an appropriate pause respects the user's critical task. Obtaining consent before beginning work, completing it efficiently, and confirming resolution reflect professionalism, minimal disruption, and thorough service.",
            },
            {
                "id": "b",
                "text": "Begin the keyboard replacement immediately since it is a quick repair that will not significantly disrupt the call.",
                "correct": False,
                "rationale": "Incorrect. Beginning work without the user's knowledge or consent violates professionalism standards — even for quick repairs. The user should be informed and agree before work begins.",
            },
            {
                "id": "c",
                "text": "Leave and return at the end of the business day since the user is unavailable.",
                "correct": False,
                "rationale": "Incorrect. The keyboard is causing active work disruption. Leaving without attempting to resolve the issue prioritizes the technician's convenience over the user's needs.",
            },
            {
                "id": "d",
                "text": "Send an email informing the user the repair will be rescheduled and close the ticket.",
                "correct": False,
                "rationale": "Incorrect. Unilaterally rescheduling without attempting to assist the user on the current visit and closing the ticket prematurely fails both the user and the ticket management process.",
            },
        ],
        "explanation": (
            "CompTIA A+ professionalism: avoid interrupting without necessity, respect the customer's time and priorities, "
            "obtain consent before beginning work, set clear expectations, complete work efficiently, "
            "and verify resolution before leaving. A brief, considerate pause for a critical call demonstrates both empathy and good judgment."
        ),
    },
    {
        "id": "c2d4v3-022",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A user asks the technician when their laptop will be repaired. The technician "
            "is unsure because the replacement part is on backorder. Which response BEST "
            "demonstrates proper expectation setting?"
        ),
        "options": [
            {
                "id": "a",
                "text": "'I'll have it done by Friday' — giving a definite deadline to satisfy the user, even if uncertain.",
                "correct": False,
                "rationale": "Incorrect. Providing a deadline you cannot keep destroys trust when it is missed. Setting false expectations is worse than honest uncertainty.",
            },
            {
                "id": "b",
                "text": "'I'm not sure — it could be days or weeks.' — being honest but providing no actionable information.",
                "correct": False,
                "rationale": "Incorrect. While honest, a vague response with no follow-up plan fails to set proper expectations or demonstrate a commitment to resolution.",
            },
            {
                "id": "c",
                "text": "'The part is on backorder. I'll check the estimated delivery date today and contact you by 3 PM with a specific timeline. If the date changes, I will update you immediately.'",
                "correct": True,
                "rationale": "Correct. This response is honest about uncertainty, commits to a specific follow-up action with a time, and promises proactive communication if the situation changes — the hallmarks of setting proper expectations.",
            },
            {
                "id": "d",
                "text": "'You should contact the vendor directly about the part delivery since this is outside my control.'",
                "correct": False,
                "rationale": "Incorrect. Redirecting the user to the vendor deflects responsibility inappropriately. The technician owns the repair workflow and communication with the user, even when factors are outside direct control.",
            },
        ],
        "explanation": (
            "Expectation setting best practices: be honest about uncertainty, provide specific follow-up commitments with timelines, "
            "proactively communicate changes, and take ownership of the resolution process. "
            "A specific promise (call by 3 PM) is far more trust-building than a vague estimate or a redirected responsibility."
        ),
    },
    {
        "id": "c2d4v3-023",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Communication & professionalism",
        "stem": (
            "While repairing a workstation, a technician notices unlocked drawers containing "
            "what appear to be financial spreadsheets with salary data. Later, the technician "
            "mentions this to a colleague in the break room. Which professionalism principle "
            "did the technician violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Proper lifting technique",
                "correct": False,
                "rationale": "Incorrect. Lifting technique is a safety procedure, not relevant to information handling. The violation is about how sensitive information was treated.",
            },
            {
                "id": "b",
                "text": "Confidentiality of customer and organizational data",
                "correct": True,
                "rationale": "Correct. Technicians encounter sensitive information during site visits (financial data, personnel records, intellectual property). Discussing this information with colleagues — even casually — violates the confidentiality principle and could violate the organization's data policies.",
            },
            {
                "id": "c",
                "text": "Proper ESD handling procedures",
                "correct": False,
                "rationale": "Incorrect. ESD procedures govern hardware handling. The issue here is information security and professional ethics, not static electricity.",
            },
            {
                "id": "d",
                "text": "Change management documentation requirements",
                "correct": False,
                "rationale": "Incorrect. Change management applies to technical modifications to systems. The violation is about confidentiality of incidentally observed sensitive information.",
            },
        ],
        "explanation": (
            "CompTIA professionalism principles include: respect for customer privacy, confidentiality of all information "
            "encountered during site visits (financial, personnel, technical), and prohibition on sharing customer experiences "
            "with colleagues or on social media. Incidentally observed sensitive data must be treated with the same discretion "
            "as deliberately provided confidential information."
        ),
    },
    {
        "id": "c2d4v3-024",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A user is explaining a complex problem and keeps going off-topic with unrelated "
            "complaints. The technician needs the specific symptom details to proceed. "
            "Which technique BEST refocuses the conversation without seeming dismissive?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Interrupt immediately and say, 'I only need to hear about the specific error message.'",
                "correct": False,
                "rationale": "Incorrect. Abruptly interrupting the user and narrowing focus aggressively dismisses their concerns and violates the active-listening principle of not interrupting.",
            },
            {
                "id": "b",
                "text": "Wait for a natural pause, then use a closed-ended question to redirect: 'To make sure I capture this correctly — what is the exact error message that appears?'",
                "correct": True,
                "rationale": "Correct. Waiting for a pause respects the user, and a specific closed-ended question redirects focus to actionable data without dismissing the user's broader concerns. This technique is efficient and professional.",
            },
            {
                "id": "c",
                "text": "Let the user talk indefinitely to ensure all complaints are captured before beginning diagnosis.",
                "correct": False,
                "rationale": "Incorrect. Allowing unlimited off-topic conversation is inefficient and does not serve the user's technical need. Redirecting focus after adequate listening is appropriate and professional.",
            },
            {
                "id": "d",
                "text": "Transfer the call to a different technician to reset the conversation.",
                "correct": False,
                "rationale": "Incorrect. Transferring to avoid a challenging conversation abandons the user and creates frustration. Managing difficult conversations is a core professional skill.",
            },
        ],
        "explanation": (
            "Open-ended questions gather broad information; closed-ended questions narrow to specific facts. "
            "When redirecting a user, wait for a natural pause (active listening), then use a closed-ended question "
            "to focus on the actionable symptom. This demonstrates control of the conversation while respecting the user."
        ),
    },
    # ── 4.8 Scripting basics ─────────────────────────────────────────────────
    {
        "id": "c2d4v3-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A technician needs to automate user account creation on a Linux server. "
            "The script must read a CSV file of usernames, create each account with "
            "useradd, and set a temporary password. Which script file extension and "
            "interpreter are MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": ".ps1 / PowerShell Core — because PowerShell supports CSV import natively",
                "correct": False,
                "rationale": "Incorrect. While PowerShell Core runs on Linux, using a .sh Bash script is the idiomatic and expected approach for Linux system administration tasks such as account creation.",
            },
            {
                "id": "b",
                "text": ".bat / Windows Command Interpreter — because batch files are the universal automation standard",
                "correct": False,
                "rationale": "Incorrect. .bat files run under the Windows Command Interpreter and have no native execution capability on Linux. They cannot issue Linux commands.",
            },
            {
                "id": "c",
                "text": ".sh / Bash — because Bash is the native automation shell for Linux environments",
                "correct": True,
                "rationale": "Correct. Bash (.sh) is the native scripting environment for Linux. It can read CSV files (read/awk), call useradd and passwd directly, and is available by default on all major Linux distributions.",
            },
            {
                "id": "d",
                "text": ".vbs / Windows Script Host — because VBScript can connect to Linux systems via COM objects",
                "correct": False,
                "rationale": "Incorrect. VBScript runs under Windows Script Host (wscript/cscript) and has no native Linux presence. It cannot issue native Linux commands.",
            },
        ],
        "explanation": (
            "Platform-to-extension mapping: Linux admin tasks → .sh (Bash); Windows admin tasks → .ps1 (PowerShell) or .bat (legacy); "
            "cross-platform → .py (Python). "
            "Always choose the idiomatic scripting language for the target platform to maximize tool support, readability, "
            "and maintainability."
        ),
    },
    {
        "id": "c2d4v3-026",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A PowerShell script that automated patch deployment worked in the test lab "
            "but on production it throws: 'File .ps1 cannot be loaded because running "
            "scripts is disabled on this system.' What is the MOST likely cause and fix?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The script file is corrupted; re-download it from the source.",
                "correct": False,
                "rationale": "Incorrect. The error message explicitly states scripts are disabled, not that the file is corrupt. File corruption produces different errors.",
            },
            {
                "id": "b",
                "text": "PowerShell execution policy is set to Restricted on the production system; set it to RemoteSigned or AllSigned via Set-ExecutionPolicy.",
                "correct": True,
                "rationale": "Correct. This is the standard PowerShell execution policy error. The Restricted policy (Windows default in some configurations) blocks all scripts. Setting to RemoteSigned (run local scripts freely, require signatures for downloaded scripts) or AllSigned resolves this while maintaining a security posture.",
            },
            {
                "id": "c",
                "text": "The .ps1 extension is not registered in Windows; rename the file to .bat.",
                "correct": False,
                "rationale": "Incorrect. The error is about execution policy, not file extension registration. Renaming to .bat would not work — the code is PowerShell syntax, not batch syntax.",
            },
            {
                "id": "d",
                "text": "PowerShell is not installed on the production server; install it from the Microsoft Store.",
                "correct": False,
                "rationale": "Incorrect. If PowerShell were absent, the error would state that the command was not found or the application did not exist, not that running scripts is disabled. The error confirms PowerShell is present but policy-restricted.",
            },
        ],
        "explanation": (
            "PowerShell execution policies: Restricted (no scripts), AllSigned (all scripts must be signed), "
            "RemoteSigned (local scripts run freely; downloaded scripts need a signature), Unrestricted (all scripts run with warning). "
            "Set via: Set-ExecutionPolicy RemoteSigned -Scope LocalMachine. "
            "This is a common deployment gotcha when moving scripts from test to production environments."
        ),
    },
    {
        "id": "c2d4v3-027",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Scripting basics",
        "stem": (
            "A technician wants to write a single script that will run on both Windows and "
            "Linux systems to collect system uptime and IP address information. Which script "
            "type is MOST suitable and WHY?"
        ),
        "options": [
            {
                "id": "a",
                "text": ".bat — because batch files execute on all platforms via the Windows Subsystem for Linux",
                "correct": False,
                "rationale": "Incorrect. Batch files (.bat) run under Windows Command Interpreter. WSL allows Linux binaries on Windows, not the reverse — .bat does not run natively on Linux.",
            },
            {
                "id": "b",
                "text": ".py — because Python has a cross-platform runtime available for Windows, Linux, and macOS and supports subprocess/os modules for system calls",
                "correct": True,
                "rationale": "Correct. Python (.py) is the leading cross-platform scripting language with interpreters available for all major OSes. The subprocess and platform modules allow OS-appropriate command execution from a single script file.",
            },
            {
                "id": "c",
                "text": ".vbs — because VBScript is the only language with native Windows and Linux interpreters",
                "correct": False,
                "rationale": "Incorrect. VBScript runs only under Windows Script Host on Windows. It has no native Linux interpreter and has been deprecated by Microsoft.",
            },
            {
                "id": "d",
                "text": ".sh — because Bash is installed by default on both Windows and Linux",
                "correct": False,
                "rationale": "Incorrect. Bash is native to Linux/macOS. On Windows it requires WSL or Git Bash, making it unsuitable as a natively cross-platform script without additional configuration.",
            },
        ],
        "explanation": (
            "Cross-platform scripting options: Python (.py) — best choice, native runtime for all OS; "
            "PowerShell Core (.ps1) — second option, available on all platforms but less ubiquitous by default; "
            ".bat — Windows only; .sh — Linux/macOS only (WSL required for Windows); .vbs — Windows only, deprecated. "
            "Python is the strongest answer for true cross-platform automation."
        ),
    },
    {
        "id": "c2d4v3-028",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A sysadmin runs a .bat script that deletes temporary files across all user "
            "profiles. During testing, the script accidentally deletes a directory path it "
            "was not intended to process because a variable contained a space without "
            "quotes. Which scripting risk category does this BEST exemplify?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Malware introduction via embedded commands",
                "correct": False,
                "rationale": "Incorrect. This was a logic bug in the script itself — not malware. The harmful action came from an unintended path due to a quoting error, not from malicious embedded code.",
            },
            {
                "id": "b",
                "text": "Inadvertently changing system settings or deleting data due to untested script logic",
                "correct": True,
                "rationale": "Correct. CompTIA identifies 'inadvertently changing system settings' as a key scripting risk. An unquoted variable causing unintended directory deletion is a classic example of this risk — the script works as coded, but the logic produces harmful unintended results.",
            },
            {
                "id": "c",
                "text": "Browser crash caused by excessive DOM manipulation",
                "correct": False,
                "rationale": "Incorrect. Browser DOM manipulation is a risk for JavaScript in web contexts, not .bat scripts on a local system.",
            },
            {
                "id": "d",
                "text": "Credential exposure via plain-text password storage in the script",
                "correct": False,
                "rationale": "Incorrect. Credential exposure is a separate scripting risk (hard-coded passwords) unrelated to the unintended directory deletion from a quoting error.",
            },
        ],
        "explanation": (
            "CompTIA scripting risks: (1) unintentionally introducing malware, (2) inadvertently changing system settings, "
            "(3) browser/system crashes. The directory-deletion scenario from a quoting error is textbook risk #2. "
            "Mitigation: thorough sandbox testing, code review, restricted permissions (least privilege), and version control."
        ),
    },
    # ── 4.9 Remote access technologies ───────────────────────────────────────
    {
        "id": "c2d4v3-029",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A help desk technician needs to remotely assist a user running Windows 11 Home "
            "who cannot connect to the company VPN. The user needs to share their screen so "
            "the technician can guide troubleshooting in real time. The user has no additional "
            "software installed. Which built-in Windows tool should the technician use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Remote Desktop Connection (mstsc.exe)",
                "correct": False,
                "rationale": "Incorrect. Remote Desktop is not available as a host (incoming connection) on Windows 11 Home — only Windows 11 Pro/Enterprise support inbound RDP connections. mstsc only allows the user to connect out.",
            },
            {
                "id": "b",
                "text": "Quick Assist (built into Windows 10/11)",
                "correct": True,
                "rationale": "Correct. Quick Assist ships with Windows 10 and 11 including Home edition. The user opens Quick Assist, shares a code with the helper, and the technician can view or control the screen — no additional software required.",
            },
            {
                "id": "c",
                "text": "Windows Subsystem for Linux (WSL) with SSH server",
                "correct": False,
                "rationale": "Incorrect. WSL provides a Linux environment and SSH access to a command-line interface — it cannot share the Windows graphical desktop with a helper.",
            },
            {
                "id": "d",
                "text": "Windows Sandbox",
                "correct": False,
                "rationale": "Incorrect. Windows Sandbox is an isolated VM environment for testing untrusted software. It has no remote assistance or screen-sharing capability.",
            },
        ],
        "explanation": (
            "Windows built-in remote assistance: Quick Assist (Win 10/11 all editions, code-based screen share/control); "
            "MSRA/Windows Remote Assistance (older, invitation-based, still available but superseded by Quick Assist); "
            "RDP host (Win 10/11 Pro and Enterprise only, port 3389, full session takeover). "
            "For Home users who need tech support, Quick Assist is the correct built-in tool."
        ),
    },
    {
        "id": "c2d4v3-030",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Remote access technologies",
        "stem": (
            "A security auditor finds that IT staff are connecting to Linux servers using SSH "
            "with password authentication over the public internet. The auditor recommends "
            "replacing password authentication with a more secure method. Which SSH "
            "authentication method should be implemented?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Telnet with strong passwords",
                "correct": False,
                "rationale": "Incorrect. Telnet transmits all data in plain text. Using Telnet with any password type over the public internet is a critical security failure.",
            },
            {
                "id": "b",
                "text": "SSH with public key authentication (key pair)",
                "correct": True,
                "rationale": "Correct. SSH public key authentication uses a cryptographic key pair — private key stored securely on the client, public key on the server. It is immune to password-spray and brute-force attacks and is the recommended method for internet-facing SSH access.",
            },
            {
                "id": "c",
                "text": "RDP with NLA (Network Level Authentication)",
                "correct": False,
                "rationale": "Incorrect. RDP is a Windows-specific protocol primarily; the servers are Linux. More importantly, the question asks for a more secure SSH authentication method, not a protocol replacement.",
            },
            {
                "id": "d",
                "text": "VNC with encrypted tunnel",
                "correct": False,
                "rationale": "Incorrect. VNC provides graphical remote access, not CLI access to Linux servers. It requires additional software installation and, while a VPN/SSH tunnel improves security, it does not address the SSH authentication method question.",
            },
        ],
        "explanation": (
            "SSH authentication methods by security level: public key (strongest, recommended for internet-facing servers), "
            "certificate-based (enterprise PKI), keyboard-interactive/password (weakest, vulnerable to brute-force). "
            "For internet-facing SSH: disable password auth (PasswordAuthentication no in sshd_config), require key auth, "
            "restrict source IPs where possible, and consider port knocking or VPN as additional layers."
        ),
    },
    {
        "id": "c2d4v3-031",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A technician needs to securely manage a network switch's CLI over the internet "
            "without exposing the switch's management port directly. Which combination of "
            "remote access technologies provides the MOST secure approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Telnet through a jump server with no VPN",
                "correct": False,
                "rationale": "Incorrect. Telnet transmits credentials and commands in plain text. Even through a jump server, Telnet over the internet is unacceptably insecure.",
            },
            {
                "id": "b",
                "text": "VPN to the corporate network, then SSH to the switch management interface",
                "correct": True,
                "rationale": "Correct. VPN encrypts the internet-facing tunnel, removing the switch management port from direct internet exposure. SSH then provides an encrypted, authenticated CLI session to the switch — a defense-in-depth approach.",
            },
            {
                "id": "c",
                "text": "Direct RDP connection to the switch's management IP",
                "correct": False,
                "rationale": "Incorrect. Most network switches do not support RDP. Network device CLI management uses SSH or Telnet — RDP is for Windows desktop sessions.",
            },
            {
                "id": "d",
                "text": "VNC with username/password to the switch's graphical interface",
                "correct": False,
                "rationale": "Incorrect. Network switches typically do not have graphical interfaces accessible via VNC. CLI access via SSH is the appropriate method for switch management.",
            },
        ],
        "explanation": (
            "Defense-in-depth for remote network device management: VPN provides encrypted transport and removes direct internet "
            "exposure of management interfaces; SSH provides encrypted, authenticated CLI access. "
            "Never expose management interfaces directly to the internet using Telnet or unencrypted protocols. "
            "Jump servers (bastion hosts) + SSH are also acceptable alternatives to VPN in enterprise environments."
        ),
    },
    # ── Multiple-response questions (~6 total) ────────────────────────────────
    {
        "id": "c2d4v3-032",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Backup types",
        "stem": (
            "A backup administrator is evaluating backup strategies. Select the TWO statements "
            "that are TRUE about incremental backups compared to differential backups. "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Incremental backups are typically faster to create each day than differential backups.",
                "correct": True,
                "rationale": "Correct. Each incremental captures only data changed since the LAST backup (any type), so each daily backup set is small and quick. Differentials grow each day as they accumulate all changes since the last full.",
            },
            {
                "id": "b",
                "text": "Incremental restores require fewer backup sets than differential restores.",
                "correct": False,
                "rationale": "Incorrect. Incremental restore requires the last full plus every incremental since. Differential restore always requires just two sets: last full + most recent differential. Differential restores are simpler.",
            },
            {
                "id": "c",
                "text": "Restoring from incrementals requires applying each incremental in chronological order after the full.",
                "correct": True,
                "rationale": "Correct. Because each incremental contains only changes since the prior backup, they must be applied in sequence to reconstruct the full data set. Skipping any incremental results in missing data.",
            },
            {
                "id": "d",
                "text": "Incremental backups clear the archive bit after each backup, while differentials do not.",
                "correct": False,
                "rationale": "Incorrect. This is actually reversed. Incremental backups reset the archive bit (mark files as backed up), which is why the next incremental only picks up new changes. Differentials do NOT reset the archive bit, which is why they keep accumulating all changes since the last full.",
            },
        ],
        "explanation": (
            "Archive bit behavior: Full and Incremental backups reset the archive bit after backing up a file. "
            "Differential and Copy backups do NOT reset the archive bit. "
            "This is why incrementals are small and fast (only unchanged-since-last-backup files) "
            "while differentials grow each day (all unchanged-since-last-full files). "
            "Incremental = fast backup, slow restore. Differential = slower backup, fast restore."
        ),
    },
    {
        "id": "c2d4v3-033",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "An organization wants to protect against ransomware that can also encrypt "
            "network-connected backup drives. Select the TWO backup strategy elements that "
            "MOST effectively defend against this specific threat. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Keep at least one backup copy on media that is offline or air-gapped (disconnected from the network).",
                "correct": True,
                "rationale": "Correct. Ransomware can only encrypt drives/shares it can reach. An offline or air-gapped backup copy is inaccessible to the ransomware at the time of attack, preserving a clean recovery point.",
            },
            {
                "id": "b",
                "text": "Increase backup frequency from weekly to daily.",
                "correct": False,
                "rationale": "Incorrect. More frequent backups improve RPO but if all copies are network-connected, ransomware will encrypt all of them. Frequency alone does not address the threat.",
            },
            {
                "id": "c",
                "text": "Store at least one backup copy off-site or in immutable cloud storage (write-once, cannot be overwritten or deleted).",
                "correct": True,
                "rationale": "Correct. Immutable cloud storage (object lock / WORM) prevents ransomware from overwriting or encrypting backup data even if the cloud credentials are compromised. Off-site/immutable copies are the ransomware-resilience extension of the 3-2-1 rule (sometimes called 3-2-1-1-0).",
            },
            {
                "id": "d",
                "text": "Compress all backups to reduce storage footprint.",
                "correct": False,
                "rationale": "Incorrect. Compression reduces storage usage but has no effect on whether ransomware can reach and encrypt the backup files. It does not address ransomware resiliency.",
            },
        ],
        "explanation": (
            "Ransomware-resilient backup strategy: offline/air-gapped copies (disconnected from network during attack), "
            "immutable storage (write-once — cannot be encrypted by ransomware even if reached), "
            "and off-site copies (geographic separation). "
            "The 3-2-1-1-0 extension adds 1 offline/immutable copy and 0 backup errors (regular restore testing)."
        ),
    },
    {
        "id": "c2d4v3-034",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A technician discovers malware on a workstation that appears to be beaconing "
            "to an external command-and-control server. Select the TWO FIRST actions "
            "the technician should take according to incident response best practices. "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Isolate the workstation from the network immediately to stop ongoing exfiltration.",
                "correct": True,
                "rationale": "Correct. Network isolation (disconnect from network) is the first containment action — it stops the active C2 communication and potential data exfiltration while preserving the system state for forensic analysis.",
            },
            {
                "id": "b",
                "text": "Report the incident to the appropriate personnel (manager, security team, or incident response team).",
                "correct": True,
                "rationale": "Correct. Notifying the security/incident response team simultaneously with containment activates the broader response. Technicians should not investigate independently; proper escalation ensures legal, compliance, and forensic requirements are met.",
            },
            {
                "id": "c",
                "text": "Run the organization's antivirus scanner to remove the malware immediately.",
                "correct": False,
                "rationale": "Incorrect. Running AV before forensic imaging alters the system state and may destroy evidence of the attack vector, persistence mechanisms, and exfiltrated data. Containment and preservation come before remediation.",
            },
            {
                "id": "d",
                "text": "Reimage the workstation to ensure the malware is completely removed.",
                "correct": False,
                "rationale": "Incorrect. Reimaging destroys all forensic evidence and must only occur after the investigation and evidence-preservation phases are complete. Immediate reimaging violates incident response and chain-of-custody procedures.",
            },
        ],
        "explanation": (
            "Incident response sequence (simplified): Identify → Contain (isolate) → Report/Escalate → Preserve evidence "
            "→ Investigate → Remediate → Recover → Post-incident review. "
            "Containment (network isolation) and reporting are immediate first steps. "
            "Remediation (AV, reimaging) occurs after evidence is preserved — never before."
        ),
    },
    {
        "id": "c2d4v3-035",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A security manager is reviewing scripting policies after an incident where a "
            "malicious .js file was emailed to employees. Select the TWO controls that MOST "
            "directly reduce the risk of malicious script execution. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Configure email gateway filters to strip or quarantine script file attachments (.js, .vbs, .ps1, .bat).",
                "correct": True,
                "rationale": "Correct. Blocking common script file extensions at the email gateway prevents delivery of script-based malware to endpoints, addressing the primary delivery vector in this scenario.",
            },
            {
                "id": "b",
                "text": "Require code signing for all scripts executed in the environment and configure execution policies accordingly.",
                "correct": True,
                "rationale": "Correct. Code signing ensures scripts are authenticated from a trusted source. Execution policies (e.g., PowerShell AllSigned) block unsigned or tampered scripts from running, directly mitigating execution of malicious scripts.",
            },
            {
                "id": "c",
                "text": "Increase the maximum email attachment size limit to allow scripts to be scanned more thoroughly.",
                "correct": False,
                "rationale": "Incorrect. Increasing attachment size does not improve script security scanning. This control addresses a different concern (large file handling) and would not reduce script execution risk.",
            },
            {
                "id": "d",
                "text": "Deploy additional NAS storage to hold backup copies of scripts.",
                "correct": False,
                "rationale": "Incorrect. Additional storage is irrelevant to preventing malicious script execution. Script backups serve availability purposes, not security execution controls.",
            },
        ],
        "explanation": (
            "Script execution risk mitigations: (1) gateway/endpoint filtering of script attachments; "
            "(2) code signing + execution policy enforcement; (3) application allowlisting (only approved scripts run); "
            "(4) least-privilege execution (limit which accounts can run scripts); "
            "(5) endpoint protection that scans script content. "
            "Defense-in-depth applies multiple layers simultaneously."
        ),
    },
    {
        "id": "c2d4v3-036",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A help desk manager is auditing ticket quality. Select the TWO elements that "
            "are REQUIRED in every properly closed ticket per CompTIA A+ best practices. "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Documented resolution steps and root cause",
                "correct": True,
                "rationale": "Correct. A closed ticket must document how the issue was resolved and what caused it. This is the basis for knowledge-base reuse and trend analysis.",
            },
            {
                "id": "b",
                "text": "End-user acceptance or sign-off confirming the issue is resolved",
                "correct": True,
                "rationale": "Correct. End-user acceptance (verbal or written sign-off) confirms the issue is resolved from the user's perspective and prevents premature ticket closure that requires reopening.",
            },
            {
                "id": "c",
                "text": "A list of all other tickets opened by the same user in the past year",
                "correct": False,
                "rationale": "Incorrect. Historical ticket lists may be useful for trend analysis but are not a required element of a properly closed ticket. This is reporting-level data, not a ticket-closure requirement.",
            },
            {
                "id": "d",
                "text": "The technician's hourly billing rate for the work performed",
                "correct": False,
                "rationale": "Incorrect. Billing rates may appear on invoices in managed service contexts but are not a CompTIA-defined required ticket field. Ticket fields focus on technical documentation, not financial data.",
            },
        ],
        "explanation": (
            "Required ticket-closure elements per CompTIA: accurate problem description, root cause, resolution steps, "
            "parts/software used, any escalation paths, and end-user acceptance/sign-off. "
            "These make the ticket a complete incident record and potential KB article. "
            "Missing end-user sign-off is one of the most common reasons tickets need to be reopened."
        ),
    },
    {
        "id": "c2d4v3-037",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Remote access technologies",
        "stem": (
            "A security team is hardening remote access. Select the TWO controls that MOST "
            "effectively reduce the attack surface of an RDP (Remote Desktop Protocol) "
            "deployment. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Require Network Level Authentication (NLA) for all RDP connections.",
                "correct": True,
                "rationale": "Correct. NLA requires users to authenticate before a full RDP session is established, preventing unauthenticated users from reaching the Windows login screen and reducing exposure to credential-stuffing attacks on the session layer.",
            },
            {
                "id": "b",
                "text": "Change the default RDP listening port from 3389 to a non-standard port.",
                "correct": False,
                "rationale": "Incorrect. Port obfuscation (security through obscurity) marginally reduces automated port-scan attacks but does not prevent determined attackers who perform full port scans. It is not a primary hardening control.",
            },
            {
                "id": "c",
                "text": "Restrict RDP access to specific source IP ranges using a firewall or VPN, preventing direct internet exposure.",
                "correct": True,
                "rationale": "Correct. Placing RDP behind a VPN or restricting it to known IP ranges via firewall prevents internet-wide brute-force attempts — the most common attack vector against exposed RDP. This is the single most impactful hardening control.",
            },
            {
                "id": "d",
                "text": "Enable the built-in Guest account as the RDP login to avoid exposing admin credentials.",
                "correct": False,
                "rationale": "Incorrect. The Guest account should be disabled (not used as a workaround). Using Guest for RDP exposes the system to unauthenticated or low-privilege access and violates least-privilege principles.",
            },
        ],
        "explanation": (
            "RDP hardening priorities: (1) restrict source IPs via firewall/VPN — eliminates internet-wide attack surface; "
            "(2) enable NLA — requires authentication before session establishment; "
            "(3) enforce MFA for RDP sessions; (4) disable RDP on systems that don't require it; "
            "(5) monitor for failed login attempts. Port-changing is low-value security theater compared to these controls."
        ),
    },
    # ── Additional hard/expert questions to complete 47 ──────────────────────
    {
        "id": "c2d4v3-038",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A technician is writing a KB article based on a resolved ticket about a "
            "recurring print-spooler crash. Which element makes the KB article MOST useful "
            "for the next technician who encounters the same issue?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A list of the user's previous unrelated help desk requests",
                "correct": False,
                "rationale": "Incorrect. Prior unrelated tickets provide no troubleshooting value for the print-spooler issue. KB articles should be issue-specific and actionable.",
            },
            {
                "id": "b",
                "text": "Step-by-step reproduction steps, the root cause identified, the exact fix applied (commands, settings, versions), and verification procedure",
                "correct": True,
                "rationale": "Correct. A high-quality KB article includes: how to recognize the issue, root cause, exact resolution steps (including commands and version numbers), and how to verify the fix — enabling any technician to resolve the same issue independently.",
            },
            {
                "id": "c",
                "text": "The ticket number and creation date only, with a reference to the original ticket for details",
                "correct": False,
                "rationale": "Incorrect. Referencing the ticket without extracting the resolution details requires two lookups and is not usable as a standalone KB article. KB articles should be self-contained.",
            },
            {
                "id": "d",
                "text": "The user's contact information for follow-up",
                "correct": False,
                "rationale": "Incorrect. User contact information belongs in the ticket, not the KB article. KB articles are issue-focused, not user-focused.",
            },
        ],
        "explanation": (
            "Effective KB articles are: searchable (clear title and keywords), self-contained (full context without "
            "needing to cross-reference tickets), actionable (exact steps, commands, versions), and verified "
            "(include a test to confirm resolution). They reduce mean time to resolve (MTTR) for recurring issues."
        ),
    },
    {
        "id": "c2d4v3-039",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "A junior technician pushes an OS update to production workstations at 2 PM on "
            "a Monday without a change request, causing 30 workstations to reboot mid-day "
            "and disrupting a company-wide financial close process. Which change management "
            "requirement did the technician MOST directly violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The requirement to test changes in a sandbox before production deployment",
                "correct": False,
                "rationale": "Incorrect. Sandbox testing is important, but the most direct violation is bypassing CAB approval entirely and deploying without a change request during business hours — not specifically the absence of sandbox testing.",
            },
            {
                "id": "b",
                "text": "The requirement to obtain CAB approval with an appropriate maintenance window before deploying changes to production",
                "correct": True,
                "rationale": "Correct. CAB approval defines what, when, and how a change is deployed. Deploying without approval and outside a maintenance window (2 PM Monday during financial close) directly caused the disruption. This is the most fundamental change management violation.",
            },
            {
                "id": "c",
                "text": "The requirement to create a rollback plan after the change is deployed",
                "correct": False,
                "rationale": "Incorrect. The rollback plan must be prepared before deployment, not after. But the more fundamental violation is the absence of any change request or CAB approval.",
            },
            {
                "id": "d",
                "text": "The requirement to notify the vendor before deploying OS updates",
                "correct": False,
                "rationale": "Incorrect. Vendor notification is not a standard change management requirement. CAB approval, appropriate timing, and documentation are the core requirements that were violated.",
            },
        ],
        "explanation": (
            "Change management prevents exactly this scenario: unplanned changes during business hours disrupting critical processes. "
            "The CAB evaluates risk, approves timing (maintenance windows are typically nights/weekends), and ensures rollback plans exist. "
            "Any change to production systems — including 'routine' OS updates — requires a change request."
        ),
    },
    {
        "id": "c2d4v3-040",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A technician finishes replacing a motherboard and places the old board on the "
            "workbench in a standard clear plastic bag while documenting the repair. "
            "Which problem does this create?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The plastic bag may trap heat and warp the motherboard.",
                "correct": False,
                "rationale": "Incorrect. Heat warping is not a concern from a room-temperature plastic bag over a short documentation period. The critical risk is static electricity.",
            },
            {
                "id": "b",
                "text": "Standard plastic bags are not antistatic and can generate electrostatic charge that damages the board's components.",
                "correct": True,
                "rationale": "Correct. Standard plastic bags are non-dissipative insulators that can build up and hold static charge. Even a decommissioned board stored in a regular plastic bag could be damaged if it were to be tested or reused. All circuit boards must be stored in antistatic (pink/silver) bags.",
            },
            {
                "id": "c",
                "text": "The bag prevents the technician from reading the board's serial number for documentation.",
                "correct": False,
                "rationale": "Incorrect. Reading through a plastic bag is not the concern here. The ESD damage risk from an inappropriate storage container is the critical issue.",
            },
            {
                "id": "d",
                "text": "No problem exists since the board is already removed from the system and no longer powered.",
                "correct": False,
                "rationale": "Incorrect. ESD damage occurs from static discharge, not from a powered system. A static charge can damage sensitive components on an unpowered board when the board is later handled.",
            },
        ],
        "explanation": (
            "ESD storage rule: all circuit boards, RAM, CPUs, GPUs, and other sensitive components must be stored in "
            "antistatic bags (distinguishable by their metallic silver or pink color). "
            "Standard plastic bags are ESD hazards. Antistatic mats should be used as the work surface when components are out of bags."
        ),
    },
    {
        "id": "c2d4v3-041",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "An organization is building a small server room in an existing office building. "
            "The facilities manager asks the IT team which combination of environmental "
            "controls is MOST critical for protecting server hardware from the two most "
            "damaging environmental risks."
        ),
        "options": [
            {
                "id": "a",
                "text": "Surge suppressors for power spikes and motion-sensor lighting for safety",
                "correct": False,
                "rationale": "Incorrect. Motion-sensor lighting is a convenience feature unrelated to server hardware protection. The two most damaging environmental threats to servers are heat and electrostatic discharge.",
            },
            {
                "id": "b",
                "text": "HVAC/cooling system maintaining 18–27 °C and humidity control maintaining 40–60% RH",
                "correct": True,
                "rationale": "Correct. Excessive heat causes thermal throttling, hardware failure, and fires. Humidity outside the 40–60% RH range causes either ESD (too dry) or condensation/corrosion (too humid). These are the two most damaging continuous environmental threats to server hardware.",
            },
            {
                "id": "c",
                "text": "Fluorescent lighting with UV filters and anti-reflective floor coating",
                "correct": False,
                "rationale": "Incorrect. Lighting type and floor coating are unrelated to the primary environmental threats to server hardware.",
            },
            {
                "id": "d",
                "text": "Fire suppression system only — since fire is the most catastrophic risk",
                "correct": False,
                "rationale": "Incorrect. Fire suppression is important but addresses an extreme, infrequent event. Continuous temperature and humidity management protect against day-to-day hardware degradation that is far more common than fires.",
            },
        ],
        "explanation": (
            "Data center environmental controls priority: (1) temperature (CRAC/HVAC, 18–27 °C) — heat is the #1 cause of "
            "premature hardware failure; (2) humidity (40–60% RH) — too low increases ESD, too high causes condensation; "
            "(3) fire suppression (clean agent or pre-action sprinkler); (4) airborne particulate filtration; "
            "(5) physical access controls. Temperature and humidity together form the foundation of environmental protection."
        ),
    },
    {
        "id": "c2d4v3-042",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "A technician is decommissioning a hard drive that held patient medical records "
            "for a U.S. healthcare clinic. The organization requires the sanitization method "
            "to meet both HIPAA data protection standards and NIST 800-88 guidelines for "
            "high-sensitivity data on a spinning hard disk. Which sanitization method is "
            "MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Quick format — erases the file allocation table, making data inaccessible.",
                "correct": False,
                "rationale": "Incorrect. Quick format only removes the directory entries; data remains on disk and is trivially recoverable with forensic tools. This does not meet HIPAA or NIST 800-88 standards for high-sensitivity PHI.",
            },
            {
                "id": "b",
                "text": "Physical destruction (shredding) or degaussing, with a Certificate of Destruction documented for the chain-of-custody record.",
                "correct": True,
                "rationale": "Correct. NIST 800-88 identifies physical destruction (shredding, disintegration) and degaussing as 'destroy' methods appropriate for high-sensitivity media. A Certificate of Destruction documents the event for HIPAA compliance and chain of custody.",
            },
            {
                "id": "c",
                "text": "Delete all patient files and empty the recycle bin.",
                "correct": False,
                "rationale": "Incorrect. Deleting files and emptying the recycle bin only removes file-system pointers; the actual data remains on disk until overwritten. This is completely inadequate for PHI under HIPAA.",
            },
            {
                "id": "d",
                "text": "Encrypt the entire drive with BitLocker, then format — this makes old data cryptographically irretrievable.",
                "correct": False,
                "rationale": "Incorrect. While cryptographic erasure is a valid NIST 800-88 'purge' method when done correctly (encrypting first, then discarding the key), the question specifies high-sensitivity PHI requiring the 'destroy' level of sanitization — physical destruction or degaussing.",
            },
        ],
        "explanation": (
            "NIST 800-88 sanitization levels for HDDs: Clear (overwrite — acceptable for moderate sensitivity), "
            "Purge (cryptographic erase, degauss — acceptable for most regulated data), Destroy (shred, disintegrate — "
            "required for high-sensitivity or classified data). For PHI under HIPAA, a Certificate of Destruction "
            "must be retained as part of the chain-of-custody record. Quick format and file deletion are never adequate."
        ),
    },
    {
        "id": "c2d4v3-043",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Scripting basics",
        "stem": (
            "A technician examines a file named 'inventory_report.js' found on a Windows "
            "workstation. When double-clicked, the file opens and runs automatically. "
            "Which Windows component executes .js files by default, and why is this a "
            "security concern?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PowerShell executes .js files; the concern is that PowerShell has broad system access.",
                "correct": False,
                "rationale": "Incorrect. PowerShell does not execute .js files by default. .js files on Windows are associated with Windows Script Host (wscript.exe or cscript.exe) by default.",
            },
            {
                "id": "b",
                "text": "Windows Script Host (wscript.exe) executes .js files by default; this is a concern because malicious .js files can execute system commands, download malware, and modify registry entries without user prompting.",
                "correct": True,
                "rationale": "Correct. Windows Script Host (wscript.exe) is the default handler for .js and .vbs files on Windows. WSH has significant system access, making it a popular malware delivery vector. A malicious .js attachment or download executes silently when opened.",
            },
            {
                "id": "c",
                "text": "A web browser executes .js files; the concern is JavaScript running in an insecure browser context.",
                "correct": False,
                "rationale": "Incorrect. When a .js file is double-clicked in Windows Explorer (not opened in a browser), Windows associates it with wscript.exe by default, not a browser. Browser JavaScript and WSH JavaScript are entirely separate execution contexts.",
            },
            {
                "id": "d",
                "text": ".js files are plain text and cannot be executed without a compiler; there is no security concern.",
                "correct": False,
                "rationale": "Incorrect. .js files are interpreted (not compiled) scripts. Windows Script Host interprets and executes them directly. They are a significant malware vector, not inert text files.",
            },
        ],
        "explanation": (
            "Windows Script Host (wscript.exe/cscript.exe) handles .js and .vbs files on Windows by default. "
            "WSH-based malware (ransomware, downloaders) exploits this to execute malicious code when a user opens an email attachment. "
            "Mitigation: re-associate .js/.vbs with Notepad (not WSH), disable WSH via Group Policy, and block script attachments at the email gateway."
        ),
    },
    {
        "id": "c2d4v3-044",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A company allows employees to work from home using personal computers. The "
            "security team is evaluating remote access options. Which remote access approach "
            "BEST protects corporate resources while allowing access from unmanaged personal devices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Allow direct RDP connections from personal devices to internal servers over the internet.",
                "correct": False,
                "rationale": "Incorrect. Direct internet-facing RDP exposes corporate servers to brute-force attacks, credential stuffing, and exploit attempts from unmanaged (potentially compromised) personal devices.",
            },
            {
                "id": "b",
                "text": "Require VPN with MFA before any remote access is granted, so that all traffic is tunneled and encrypted.",
                "correct": True,
                "rationale": "Correct. VPN + MFA ensures: (1) encrypted tunnel protects data in transit, (2) MFA prevents credential-only attacks, (3) the VPN gateway acts as an access control point. This approach does not expose internal resources directly to the internet.",
            },
            {
                "id": "c",
                "text": "Share internal server credentials directly with employees for direct server login.",
                "correct": False,
                "rationale": "Incorrect. Sharing server credentials violates least-privilege principles and creates uncontrolled access. Credential compromise on a personal device would give full server access.",
            },
            {
                "id": "d",
                "text": "Use Telnet over port 23 for remote terminal access since it is firewall-friendly.",
                "correct": False,
                "rationale": "Incorrect. Telnet transmits all data including credentials in plain text. It is never acceptable for remote access, particularly from untrusted personal devices over the internet.",
            },
        ],
        "explanation": (
            "Remote access from unmanaged devices: VPN + MFA is the baseline security requirement. "
            "Additional controls: VDI/virtual desktop (keeps data off the personal device), conditional access policies "
            "(check device posture before granting VPN/app access), and split tunneling vs. full tunnel analysis. "
            "Direct internet-exposed RDP or Telnet is never acceptable from security-conscious organizations."
        ),
    },
    {
        "id": "c2d4v3-045",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A user insists that a specific third-party application must be installed on "
            "their work laptop to do their job. The application is not on the approved "
            "software list and requires administrator privileges to install. The technician "
            "is not authorized to approve exceptions. Which action is MOST professional?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Install the software since the user's productivity need outweighs the policy.",
                "correct": False,
                "rationale": "Incorrect. Installing unapproved software without authorization violates IT policy and potentially security and compliance requirements. Convenience does not override policy.",
            },
            {
                "id": "b",
                "text": "Refuse the request without explanation to avoid a policy discussion.",
                "correct": False,
                "rationale": "Incorrect. Refusing without explanation is dismissive and unhelpful. The technician should explain the policy, empathize with the need, and provide a path forward.",
            },
            {
                "id": "c",
                "text": "Explain the software approval policy, acknowledge the user's need, and guide them through the exception request process to get proper authorization.",
                "correct": True,
                "rationale": "Correct. Professional communication means explaining policies clearly and respectfully, acknowledging the user's legitimate need, and empowering them with the process to get an approved exception — rather than simply refusing or capitulating.",
            },
            {
                "id": "d",
                "text": "Install the software temporarily until the manager responds.",
                "correct": False,
                "rationale": "Incorrect. Installing software 'temporarily' without authorization still violates policy and creates security/compliance risk. There is no safe 'temporary' violation of software approval policies.",
            },
        ],
        "explanation": (
            "When facing policy conflicts in customer interactions: empathize with the user's need, explain the policy reason, "
            "and provide the path to a legitimate resolution (exception process, approved alternatives). "
            "This maintains professional integrity, policy compliance, and user trust simultaneously. "
            "Policy enforcement is part of the technician role, but it should be done respectfully."
        ),
    },
    {
        "id": "c2d4v3-046",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backup types",
        "stem": (
            "A backup administrator runs full backups every Sunday and incremental backups "
            "Monday through Saturday. On Saturday at 5 PM, a cryptographic ransomware "
            "attack begins and is not detected until Monday morning. The attack started "
            "Saturday and encrypted incrementals taken Saturday evening. Which recovery "
            "point is available that is MOST current and unaffected by encryption?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Saturday's incremental backup",
                "correct": False,
                "rationale": "Incorrect. The ransomware started Saturday and the Saturday evening incremental was encrypted during or after the attack. This backup set is compromised.",
            },
            {
                "id": "b",
                "text": "Friday's incremental backup, combined with Sunday's full",
                "correct": True,
                "rationale": "Correct. The attack began Saturday, so Saturday's incremental is compromised. Friday's incremental (taken Friday evening, before the attack) is clean. Restoring Sunday's full + Monday through Friday incrementals provides the most current unaffected restore point.",
            },
            {
                "id": "c",
                "text": "Sunday's full backup only",
                "correct": False,
                "rationale": "Incorrect. Sunday's full alone is the oldest available point. Monday through Friday incrementals are also unaffected (the attack was Saturday) and should be applied to minimize data loss.",
            },
            {
                "id": "d",
                "text": "No restore is possible because all incremental backups since Sunday are corrupted.",
                "correct": False,
                "rationale": "Incorrect. Only Saturday's incremental is compromised. Monday through Friday incrementals predate the attack and are unaffected, enabling restore to end of Friday.",
            },
        ],
        "explanation": (
            "Ransomware recovery planning requires knowing when the attack started. "
            "The most recent clean restore point is the last backup created BEFORE the attack. "
            "With incrementals: apply the last full + all incrementals up to (but not including) the first compromised set. "
            "This reinforces why off-site/immutable copies and frequent backups are both needed — "
            "and why backup integrity should be monitored for signs of sudden large-scale changes."
        ),
    },
    {
        "id": "c2d4v3-047",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A forensic technician seals a hard drive into an evidence bag, writes the date, "
            "time, and her initials on the bag's tamper-evident seal, and logs the item in "
            "an evidence log. Three days later, a second analyst retrieves the drive to "
            "perform analysis. Which chain-of-custody action MUST the second analyst take "
            "when receiving the drive?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Open the bag, create a forensic image, and return the drive without updating the evidence log.",
                "correct": False,
                "rationale": "Incorrect. Opening the bag and returning the drive without logging the access breaks the chain of custody. Every access to evidence must be documented, including who received it, when, and for what purpose.",
            },
            {
                "id": "b",
                "text": "Inspect the tamper-evident seal for integrity, then document the receipt in the evidence log with date, time, signature, and purpose of access before opening the bag.",
                "correct": True,
                "rationale": "Correct. Chain of custody requires verifying seal integrity (tamper evidence) and recording every transfer/access in the evidence log before proceeding. This creates an unbroken, court-admissible record of who handled the evidence and when.",
            },
            {
                "id": "c",
                "text": "Discard the original evidence bag and re-seal the drive in a new bag after analysis.",
                "correct": False,
                "rationale": "Incorrect. Discarding the original bag destroys tamper evidence and breaks the documented chain. Original packaging should be retained alongside the new seal if re-bagging is necessary.",
            },
            {
                "id": "d",
                "text": "Begin analysis immediately to preserve the freshness of volatile data on the drive.",
                "correct": False,
                "rationale": "Incorrect. A sealed hard drive contains non-volatile persistent storage — there is no 'freshness' concern. Chain-of-custody documentation always precedes analysis, regardless of perceived urgency.",
            },
        ],
        "explanation": (
            "Every evidence transfer requires: verify tamper seal integrity, log the transfer (date, time, recipient, "
            "purpose), obtain signature of both parties (transferor and recipient), and only then proceed. "
            "The evidence log creates a documented chain of accountability from seizure to courtroom. "
            "Any break in this chain — undocumented access, discarded packaging, unwitnessed transfers — "
            "can render evidence inadmissible."
        ),
    },
]
