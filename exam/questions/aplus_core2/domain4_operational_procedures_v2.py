"""
CompTIA A+ Core 2 (220-1202) — Domain 4: Operational Procedures
38 NEW practice questions (v2) aligned to objectives 4.1–4.9.
IDs c2d4v2-001 through c2d4v2-038.
~33 multiple_choice + 5 multiple_response.
"""

QUESTIONS = [
    # ── 4.1 Documentation / ticketing / asset management ──────────────────────
    {
        "id": "c2d4v2-001",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A tier-1 technician resolves a workstation issue and marks the ticket 'resolved' "
            "without entering a description of the fix. Two weeks later, a different technician "
            "encounters the identical symptom on a different machine. Which consequence MOST "
            "directly results from the missing resolution notes?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The second technician cannot open a new ticket because the first ticket was closed without a resolution.",
                "correct": False,
                "rationale": "Incorrect. Ticket systems allow new tickets to be opened regardless of prior closure status. The absence of resolution notes does not block ticket creation.",
            },
            {
                "id": "b",
                "text": "The knowledge base lacks a reusable fix, forcing the second technician to repeat full troubleshooting from scratch.",
                "correct": True,
                "rationale": "Correct. Documenting the resolution transforms a closed ticket into a knowledge-base record. Without it, institutional knowledge is lost and future technicians must rediscover the same solution, increasing mean time to resolution (MTTR).",
            },
            {
                "id": "c",
                "text": "The SLA timer on the original ticket resets, automatically escalating it to tier 2.",
                "correct": False,
                "rationale": "Incorrect. SLA timers are not controlled by resolution note presence. Escalation rules are based on time thresholds and ticket status, not documentation completeness.",
            },
            {
                "id": "d",
                "text": "The asset record is automatically flagged as non-compliant in the CMDB.",
                "correct": False,
                "rationale": "Incorrect. CMDB compliance flags relate to configuration drift or policy violations, not to ticket note completeness.",
            },
        ],
        "explanation": (
            "Ticket documentation serves two purposes: tracking the current incident and building a knowledge base for future incidents. "
            "Required resolution fields include: root cause, steps taken, parts replaced, and time spent. "
            "Incomplete tickets inflate MTTR across the organization and impede trend analysis."
        ),
    },
    {
        "id": "c2d4v2-002",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Asset management",
        "stem": (
            "An organization is preparing for an external compliance audit. The auditor requests "
            "the current software license inventory, including license type, quantity purchased, "
            "and quantity in use. Which asset management record MOST directly satisfies this request?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Hardware procurement invoices from the past three years",
                "correct": False,
                "rationale": "Incorrect. Hardware invoices document physical device purchases but do not track software licenses, quantities, or current deployment counts.",
            },
            {
                "id": "b",
                "text": "Network topology diagram showing all connected devices",
                "correct": False,
                "rationale": "Incorrect. A topology diagram shows logical or physical network connections and device types but does not contain license type, count, or assignment information.",
            },
            {
                "id": "c",
                "text": "Software license tracking record (license type, seat count, users/devices assigned)",
                "correct": True,
                "rationale": "Correct. A software license tracking record is the specific asset management document that records license type (OEM, perpetual, subscription, open-source), seats purchased, and current deployment, providing exactly what a compliance audit requires.",
            },
            {
                "id": "d",
                "text": "End-user acceptable use policy signed by all employees",
                "correct": False,
                "rationale": "Incorrect. An AUP documents permitted use; it contains no information about license quantities, types, or deployment status.",
            },
        ],
        "explanation": (
            "Asset management includes both hardware (tagged devices, serial numbers, assigned users, warranty status) and "
            "software (license type, seat counts, expiration dates, version deployed). "
            "Separate license tracking prevents under-licensing (legal risk) and over-licensing (wasted spend). "
            "Audit readiness requires both record types to be current."
        ),
    },
    {
        "id": "c2d4v2-003",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Asset management",
        "stem": (
            "A technician replaces the motherboard in a company laptop under warranty. After the "
            "repair, the asset tag on the chassis still matches the original database record, "
            "but the new motherboard has a different serial number. Which asset management action "
            "is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Retire the original asset record and create a new one with the motherboard serial number as the primary identifier.",
                "correct": False,
                "rationale": "Incorrect. The asset is still the same device (same chassis, same tag, same assigned user). Retiring and recreating breaks historical service records tied to the original asset ID unnecessarily.",
            },
            {
                "id": "b",
                "text": "Update the existing asset record to reflect the new motherboard serial number as a component detail under the original asset ID.",
                "correct": True,
                "rationale": "Correct. The asset tag (chassis-level ID) remains the primary record key. Component-level changes such as a motherboard swap should be documented as component updates within the existing asset record, preserving continuity of service history and warranty tracking.",
            },
            {
                "id": "c",
                "text": "No update is needed because the asset tag on the chassis has not changed.",
                "correct": False,
                "rationale": "Incorrect. The asset record should reflect the current hardware configuration. An unrecorded component change means the record inaccurately describes what is inside the device, which is a problem during future troubleshooting and warranty claims.",
            },
            {
                "id": "d",
                "text": "Affix a second asset tag to the new motherboard and create a child asset record linked to the laptop.",
                "correct": False,
                "rationale": "Incorrect. Tagging internal components separately is uncommon for user devices (more typical in specialized inventory for expensive FRUs at the enterprise level) and is not a standard practice described in CompTIA A+ asset management.",
            },
        ],
        "explanation": (
            "Asset records track the full lifecycle of a physical asset: procurement, assigned user, location, service history, "
            "and component changes. The chassis/asset-tag is the primary key. "
            "Component swaps (RAM, storage, motherboard) are documented as maintenance events within the existing record, "
            "not as replacements of the asset identity. This preserves audit trails and warranty records."
        ),
    },
    {
        "id": "c2d4v2-004",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "A technician is dispatched to repair a printer but discovers the building requires "
            "a visitor badge for all contractors. After waiting 45 minutes for building access "
            "and losing significant repair time, the technician needs to document this for future "
            "visits. Which document type BEST captures this recurring process requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Incident report documenting the access delay as a security event",
                "correct": False,
                "rationale": "Incorrect. An incident report documents unexpected security or operational events. Requiring visitor badges is standard building security policy, not an incident.",
            },
            {
                "id": "b",
                "text": "Standard operating procedure (SOP) for on-site visits that includes pre-visit badge coordination",
                "correct": True,
                "rationale": "Correct. An SOP captures repeatable process steps. Updating the on-site visit SOP to include pre-visit badge coordination prevents the delay from recurring, ensuring technicians coordinate access before departing the office.",
            },
            {
                "id": "c",
                "text": "Change management request to modify the building's badge policy",
                "correct": False,
                "rationale": "Incorrect. IT change management governs changes to IT systems and configurations, not physical security policies of client buildings.",
            },
            {
                "id": "d",
                "text": "Knowledge base article explaining how to request a visitor badge on arrival",
                "correct": False,
                "rationale": "Incorrect. A KB article would help technicians who encounter this reactively, but an SOP proactively incorporates it into the standard pre-visit checklist, preventing the wait entirely.",
            },
        ],
        "explanation": (
            "SOPs encode process knowledge that prevents recurring failures. When a field experience reveals a gap "
            "(e.g., missed site access requirement), updating the relevant SOP — such as a pre-visit checklist — "
            "operationalizes the lesson. Knowledge-base articles address how to solve known technical problems; "
            "SOPs define the repeatable process workflow."
        ),
    },
    # ── 4.2 Change management ─────────────────────────────────────────────────
    {
        "id": "c2d4v2-005",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "An administrator wants to migrate a file server from Windows Server 2019 to "
            "Windows Server 2022 over a weekend. The change advisory board (CAB) approves the "
            "request but asks the administrator to define 'affected systems.' Which answer "
            "BEST represents the affected systems for this change?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Only the file server being migrated",
                "correct": False,
                "rationale": "Incorrect. 'Affected systems' must include all systems that depend on the file server — workstations, backup agents, monitoring tools, login scripts, and applications that reference the server by hostname or IP — not just the target server itself.",
            },
            {
                "id": "b",
                "text": "All workstations, applications, and services that currently connect to the file server, plus backup and monitoring systems",
                "correct": True,
                "rationale": "Correct. A thorough affected-systems list identifies every dependency so the CAB can assess true impact. Omitting dependent systems leads to undiscovered outages during the change window.",
            },
            {
                "id": "c",
                "text": "All servers in the same data center rack as the file server",
                "correct": False,
                "rationale": "Incorrect. Physical proximity does not determine logical dependency. Rack neighbors are irrelevant unless they specifically consume services from the file server.",
            },
            {
                "id": "d",
                "text": "Only systems that require downtime during the migration window",
                "correct": False,
                "rationale": "Incorrect. Affected systems include any system with a dependency, even if that system remains online. For example, login scripts may silently fail without the server, even if the workstation itself stays running.",
            },
        ],
        "explanation": (
            "Change management requires documenting affected systems — every service, workstation, application, or user "
            "that could be impacted by the change. This drives the scope of testing, user notification, and rollback requirements. "
            "Narrowly defining affected systems is a common root cause of change-related outages not anticipated in the CAB review."
        ),
    },
    {
        "id": "c2d4v2-006",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Change management",
        "stem": (
            "A network engineer submits a change request to reconfigure a core router's BGP "
            "settings at 2:00 AM on a Sunday. The change is approved with a two-hour maintenance "
            "window. At 2:45 AM, the new BGP configuration is applied but causes intermittent "
            "routing failures. The engineer has 75 minutes left in the window. What is the CORRECT "
            "next action according to change management best practices?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Continue troubleshooting the BGP configuration until the window closes, then request an extension.",
                "correct": False,
                "rationale": "Incorrect. Continuing to troubleshoot an unknown issue under time pressure risks a longer outage. Change management requires executing the rollback plan when the change is not working within the window, not extending troubleshooting indefinitely.",
            },
            {
                "id": "b",
                "text": "Execute the rollback plan immediately to restore the original BGP configuration before the window expires.",
                "correct": True,
                "rationale": "Correct. The change is not working and there is a finite maintenance window. The pre-approved rollback plan exists precisely for this situation. Rollback restores service; a post-incident review will determine root cause and plan a corrective re-attempt.",
            },
            {
                "id": "c",
                "text": "Submit an emergency change request to the CAB to extend the maintenance window.",
                "correct": False,
                "rationale": "Incorrect. Emergency CAB requests take time and do not solve the current routing failure. The rollback plan is pre-authorized and should be executed first to restore service.",
            },
            {
                "id": "d",
                "text": "Leave the partial configuration in place and monitor traffic for 24 hours before deciding.",
                "correct": False,
                "rationale": "Incorrect. A partially applied BGP change with intermittent routing failures is an active production incident. Deferring resolution for 24 hours is inconsistent with incident response and change management obligations.",
            },
        ],
        "explanation": (
            "Maintenance windows exist to limit the blast radius of changes. If a change is not successful and stable "
            "before the window closes, the rollback plan — which is pre-approved — must be executed to restore normal operations. "
            "Post-implementation reviews then identify root cause, update the change plan, and schedule a corrective change request."
        ),
    },
    {
        "id": "c2d4v2-007",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "During a post-implementation review, the team discovers that a successful OS "
            "upgrade removed a legacy .NET 3.5 component that a line-of-business application "
            "depends on. The application failed silently for 18 hours before anyone noticed. "
            "Which change management control MOST likely would have prevented this oversight?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A longer maintenance window to allow more time for the upgrade",
                "correct": False,
                "rationale": "Incorrect. A longer window does not surface unknown dependencies; it only provides more time after the dependency failure is discovered.",
            },
            {
                "id": "b",
                "text": "A more comprehensive sandbox test in a non-production environment that replicates the application stack",
                "correct": True,
                "rationale": "Correct. Sandbox testing that mirrors the production application stack (including the .NET 3.5 dependency) would have revealed the silent failure before the change was applied to production, allowing the team to add .NET 3.5 re-enablement to the change plan.",
            },
            {
                "id": "c",
                "text": "A rollback plan that could revert the OS upgrade",
                "correct": False,
                "rationale": "Incorrect. A rollback plan helps recover after a detected failure, but it does not prevent the dependency from being overlooked during planning. The 18-hour silent failure indicates the issue was not detected promptly, not that rollback was unavailable.",
            },
            {
                "id": "d",
                "text": "End-user notification of the maintenance window",
                "correct": False,
                "rationale": "Incorrect. Notifying users of the window does not reveal application dependencies. Users may not know or report the silent failure until impacted operations are discovered.",
            },
        ],
        "explanation": (
            "Sandbox testing must replicate the full production environment — including all dependent applications and their "
            "runtime requirements — not just the target system. Silent application failures (no error popup, just broken functionality) "
            "are particularly dangerous and often only surface in comprehensive integration tests."
        ),
    },
    # ── 4.3 Backup and recovery ───────────────────────────────────────────────
    {
        "id": "c2d4v2-008",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backup types",
        "stem": (
            "An organization uses full backups every Sunday night and differential backups "
            "Monday through Saturday. A ransomware attack encrypts all data on a Wednesday "
            "afternoon. Which backup sets are needed for restoration, and how much data "
            "is at risk of loss under this scheme?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Sunday full + Monday differential + Tuesday differential; data created Wednesday before the attack is at risk.",
                "correct": False,
                "rationale": "Incorrect. With differentials, Monday's and Tuesday's sets are superseded by Tuesday's differential (which contains all changes since Sunday). Only the full and the most recent differential are required. However, data from Wednesday before the attack is still at risk of loss.",
            },
            {
                "id": "b",
                "text": "Sunday full + Tuesday differential only; data created on Wednesday before the attack is lost.",
                "correct": True,
                "rationale": "Correct. A differential captures all changes since the last full, so Tuesday's set contains everything from Monday and Tuesday. Wednesday's data (between Tuesday's differential completion and the attack) was not yet backed up and is lost.",
            },
            {
                "id": "c",
                "text": "Sunday full only; differentials are supplemental and not required for restore.",
                "correct": False,
                "rationale": "Incorrect. The full alone only restores Sunday's data. Without Tuesday's differential, Monday's and Tuesday's changes are lost.",
            },
            {
                "id": "d",
                "text": "Sunday full + Monday differential; Tuesday's differential is excluded because it may be infected.",
                "correct": False,
                "rationale": "Incorrect. While verifying backup integrity for infection is wise, the correct restore set is full + most recent clean differential. Using an older differential intentionally sacrifices recoverable data unnecessarily.",
            },
        ],
        "explanation": (
            "Differential: captures all changes since last full. Restore = last full + most recent differential. "
            "RPO with daily differentials = up to one business day of data. "
            "Contrast with incremental: each set captures only changes since the last backup of any type, "
            "requiring full + all incrementals but producing smaller individual backup sets."
        ),
    },
    {
        "id": "c2d4v2-009",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backup types",
        "stem": (
            "A backup administrator is comparing incremental vs. differential strategies for a "
            "500 GB data set that changes approximately 5% per day. After two weeks without a "
            "new full backup, which statement BEST describes the key operational trade-off "
            "between the two strategies?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Incremental backups produce faster restores but consume more storage than differentials over time.",
                "correct": False,
                "rationale": "Incorrect. This is backwards. Incremental backups are faster to create (smaller sets) but slower to restore (require full + every incremental). Differentials grow in size daily but restore faster (full + one differential).",
            },
            {
                "id": "b",
                "text": "Incremental backups are faster to create and use less media, but restores require more sets and are slower; differentials use more media over time but restore faster with just two sets.",
                "correct": True,
                "rationale": "Correct. After two weeks, each differential contains up to 70% of the data set (~350 GB), while each incremental contains only one day's changes (~25 GB). Restore of incrementals requires 14 sets; differentials require only 2 — making the restore time trade-off clear.",
            },
            {
                "id": "c",
                "text": "Both strategies produce identical storage consumption and restore times when configured correctly.",
                "correct": False,
                "rationale": "Incorrect. They are fundamentally different in both metrics. The choice is a deliberate trade-off, not an equivalence.",
            },
            {
                "id": "d",
                "text": "Differential backups clear the archive bit after each run, preventing overlap with incremental backups.",
                "correct": False,
                "rationale": "Incorrect. Differential backups do NOT clear the archive bit (that's incremental's job). Differential backups read the archive bit but do not reset it, which is precisely why each differential accumulates all changes since the last full.",
            },
        ],
        "explanation": (
            "Archive bit mechanics: Full backup — clears archive bit on all backed-up files. "
            "Incremental — backs up files with archive bit set, then clears it (each set is small, restore needs all). "
            "Differential — backs up files with archive bit set, does NOT clear it (each set grows, restore needs just two). "
            "Choosing between them depends on acceptable restore time vs. backup window and media costs."
        ),
    },
    {
        "id": "c2d4v2-010",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "A startup follows the 3-2-1 rule: local NAS (copy 1), external USB drive in a locked "
            "desk drawer (copy 2), and a cloud backup service (copy 3). A flood damages the entire "
            "office, destroying the NAS and the USB drive. Which aspect of the 3-2-1 rule did "
            "the company FAIL to implement correctly?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The company only had two media types (NAS and USB are both disk-based).",
                "correct": False,
                "rationale": "Incorrect. NAS (typically spinning or SSD storage) and USB external drives are technically different media form factors. While they share disk-based technology, the more critical failure is geographic co-location.",
            },
            {
                "id": "b",
                "text": "Both on-premises copies (NAS and USB) were stored at the same physical location, violating the 'at least 1 off-site' requirement effectively by having only one off-site copy — but the real failure is that the two on-site copies were co-located and lost together.",
                "correct": True,
                "rationale": "Correct. The '1 off-site' requirement was technically met by the cloud backup. However, the 3-2-1 rule's purpose is met only when the off-site copy is the survivor of a site disaster. In this case the cloud copy does survive, but the lesson is that the USB copy in the desk drawer does not provide geographic separation — it should have been kept off-site to provide a second independent copy outside the flood zone.",
            },
            {
                "id": "c",
                "text": "The company should have had four copies instead of three to survive this event.",
                "correct": False,
                "rationale": "Incorrect. Three copies satisfy the 3-2-1 rule. The cloud copy survived, meaning recovery is possible. The issue is not copy count but the placement of the second on-premises copy.",
            },
            {
                "id": "d",
                "text": "Cloud backups do not qualify as a valid 3-2-1 off-site copy because they are not under the company's direct control.",
                "correct": False,
                "rationale": "Incorrect. Cloud storage is explicitly recognized as a valid off-site copy under the 3-2-1 rule. The cloud copy provides geographic diversity even if it is managed by a third party.",
            },
        ],
        "explanation": (
            "3-2-1 rule requires: 3 copies, 2 media types, 1 off-site. The 'off-site' requirement protects against site-level "
            "disasters. Having two copies on-premises at the same location means both are at risk from the same event. "
            "The USB drive in the desk drawer should have been at a second geographic location (or the cloud counts as the off-site "
            "copy in this scenario — the cloud copy survives). The company can recover from the cloud backup."
        ),
    },
    {
        "id": "c2d4v2-011",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Backup rotation (GFS/3-2-1)",
        "stem": (
            "An IT manager implements a Grandfather-Father-Son (GFS) rotation with daily (son), "
            "weekly (father), and monthly (grandfather) backup sets. The 'son' tapes are reused "
            "after one week, 'father' tapes after one month, and 'grandfather' tapes are retained "
            "for one year. A corruption event on a Tuesday is not discovered until the following "
            "Monday (eight days later). What is the MOST significant recovery challenge in this GFS scheme?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The 'son' daily tapes from before the corruption have already been overwritten, so the most recent clean daily restore point no longer exists.",
                "correct": True,
                "rationale": "Correct. Son tapes are reused weekly. Eight days after the corruption, the pre-corruption daily tapes have been overwritten. The most recent clean restore point is the weekly (father) tape from the previous week — meaning potentially 8-14 days of data loss.",
            },
            {
                "id": "b",
                "text": "GFS rotation cannot recover from corruption events because it only protects against accidental deletion.",
                "correct": False,
                "rationale": "Incorrect. GFS rotation provides historical restore points and can recover from corruption events. The limitation here is not the type of event but the retention window of daily tapes.",
            },
            {
                "id": "c",
                "text": "Monthly grandfather tapes are stored off-site and cannot be retrieved in time for a Monday recovery.",
                "correct": False,
                "rationale": "Incorrect. Off-site retrieval is typically achievable within hours to a day. The fundamental problem is which restore point is available and how old it is, not retrieval time.",
            },
            {
                "id": "d",
                "text": "The weekly father tape from Friday contains the corrupted data, making all tapes unusable.",
                "correct": False,
                "rationale": "Incorrect. The Friday father tape was created after the Tuesday corruption event, so it does contain corrupted data. However, the father tape from the previous Friday (before the corruption) is still intact. The issue is only that the daily tapes pre-dating the corruption are overwritten.",
            },
        ],
        "explanation": (
            "GFS retention windows determine how far back you can restore. With daily (son) tapes reused weekly, "
            "a corruption event discovered after more than 7 days means all daily pre-corruption tapes are overwritten. "
            "Recovery falls back to the most recent weekly (father) tape that predates the event. "
            "Longer daily retention periods or immutable backup copies mitigate this gap."
        ),
    },
    # ── 4.4 Safety procedures ────────────────────────────────────────────────
    {
        "id": "c2d4v2-012",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A technician is asked to replace a CPU in a server in a carpeted room with no "
            "ESD mat available. Which BEST practice should the technician apply to minimize "
            "ESD risk given the available tools?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Work barefoot to improve grounding through direct floor contact.",
                "correct": False,
                "rationale": "Incorrect. Barefoot contact with carpet does not provide a reliable earth-ground path and may actually increase triboelectric charge generation. This is not a recognized ESD mitigation technique.",
            },
            {
                "id": "b",
                "text": "Wear an ESD wrist strap clipped to the server chassis (kept plugged in but powered off), touch the chassis frequently, and avoid shuffling feet on the carpet.",
                "correct": True,
                "rationale": "Correct. The ESD wrist strap connected to a plugged-in (off) chassis provides the best available protection. Minimizing movement on carpet reduces charge buildup. Touching the chassis before handling components is the standard supplementary technique when a mat is unavailable.",
            },
            {
                "id": "c",
                "text": "Spray the carpet with water to increase conductivity and reduce static buildup.",
                "correct": False,
                "rationale": "Incorrect. Introducing moisture near server equipment creates a far greater risk (short circuits, electrocution, corrosion) than ESD. This is never an acceptable ESD mitigation technique.",
            },
            {
                "id": "d",
                "text": "Fully unplug the server and clip the wrist strap to the unplugged chassis for grounding.",
                "correct": False,
                "rationale": "Incorrect. Clipping the wrist strap to an unplugged chassis does not provide a true earth-ground path. The chassis must remain plugged in (powered off) to use the safety-ground wire in the power cord as the ground reference.",
            },
        ],
        "explanation": (
            "ESD best practices in order of effectiveness: ESD mat + wrist strap + plugged-in chassis (optimal). "
            "When a mat is unavailable: wrist strap to plugged-in chassis + minimize foot movement on carpet. "
            "Unplugged chassis = no earth ground reference. Water near electronics = serious hazard. "
            "The 1 MΩ resistor in the strap limits current to safe levels while slowly dissipating charge."
        ),
    },
    {
        "id": "c2d4v2-013",
        "domain": 4,
        "objective": "4.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Safety procedures (ESD)",
        "stem": (
            "A laser printer produces smeared, unfused output and the technician suspects a "
            "fuser failure. Before opening the printer to inspect the fuser, which safety "
            "precaution is MOST critical?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Put on an ESD wrist strap to prevent damaging the printer's formatter board.",
                "correct": False,
                "rationale": "Incorrect. ESD protection is relevant when handling circuit boards, but the primary hazard when servicing a fuser is thermal — the fuser operates at temperatures of 165–220 °C (330–428 °F).",
            },
            {
                "id": "b",
                "text": "Power off the printer and allow the fuser to cool for at least 10–15 minutes before touching it.",
                "correct": True,
                "rationale": "Correct. Fusers retain extreme heat after printing. Touching a hot fuser can cause severe burns. Powering off and allowing sufficient cooling time is the mandatory safety precaution before fuser inspection or removal.",
            },
            {
                "id": "c",
                "text": "Disconnect the drum unit before accessing the fuser to prevent toner exposure.",
                "correct": False,
                "rationale": "Incorrect. While toner handling precautions are important (avoid inhalation), the immediate personal safety risk of a hot fuser is far more critical than toner exposure during a fuser inspection.",
            },
            {
                "id": "d",
                "text": "Use insulated gloves rated for high-voltage electrical work before removing the fuser.",
                "correct": False,
                "rationale": "Incorrect. The fuser hazard is thermal (heat), not high voltage. High-voltage-rated electrical gloves protect against shock, not burns, and are not the appropriate PPE for fuser removal.",
            },
        ],
        "explanation": (
            "Laser printer safety: Fuser — thermal hazard (burns), allow cool-down before handling. "
            "High-voltage power supply — electrical hazard, capacitors retain charge; power off and discharge. "
            "Toner — respiratory hazard, avoid inhalation, use toner-specific vacuum. "
            "Ozone output from corona wires — ventilate the work area. "
            "Never open a laser assembly while laser is active — laser safety class risk."
        ),
    },
    # ── 4.5 Environmental impacts and controls ────────────────────────────────
    {
        "id": "c2d4v2-014",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "An IT manager notices that hard drives in a rack-mounted storage array are failing "
            "at twice the expected rate. Environmental monitoring shows relative humidity in the "
            "server room averages 15% RH. Which environmental factor is MOST likely contributing "
            "to the premature drive failures, and what is the correct remediation?"
        ),
        "options": [
            {
                "id": "a",
                "text": "High humidity is causing condensation on drive platters; install dehumidifiers.",
                "correct": False,
                "rationale": "Incorrect. 15% RH is very low (dry), not high. Condensation occurs with high humidity (above ~60% RH). The problem is the opposite.",
            },
            {
                "id": "b",
                "text": "Low humidity is increasing electrostatic discharge risk and may cause static-related damage; install humidifiers to bring RH to 40–60%.",
                "correct": True,
                "rationale": "Correct. Below 40% RH, static electricity builds up rapidly on surfaces and personnel, dramatically increasing ESD risk to drives and PCBs. The ASHRAE recommended range for data centers is 40–60% RH. Adding humidification brings the environment into spec.",
            },
            {
                "id": "c",
                "text": "Low humidity causes metallic corrosion on drive connectors; coat connectors with anti-corrosion spray.",
                "correct": False,
                "rationale": "Incorrect. Corrosion is associated with high humidity and condensation, not low humidity. Anti-corrosion spray on drive connectors is not a standard environmental control.",
            },
            {
                "id": "d",
                "text": "Humidity has no bearing on drive failure rates; investigate the power delivery to the storage array.",
                "correct": False,
                "rationale": "Incorrect. Humidity has a well-documented effect on ESD risk and component longevity. Power issues are possible but the 15% RH reading is a clear and directly relevant environmental finding.",
            },
        ],
        "explanation": (
            "Data center environmental thresholds: Temperature 18–27 °C (64–81 °F), Humidity 40–60% RH. "
            "Low humidity (<40%) → elevated ESD risk, static damage to drives and ICs. "
            "High humidity (>60%) → condensation risk, corrosion. "
            "Control via precision CRAC units with integrated humidifiers/dehumidifiers. "
            "Environmental monitoring should alert on exceedances in real time."
        ),
    },
    {
        "id": "c2d4v2-015",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Environmental controls",
        "stem": (
            "A company is decommissioning 80 desktop computers that contain HDDs with confidential "
            "HR data. The IT manager wants to ensure data cannot be recovered from the drives "
            "before the systems are sent to a recycler. Which data sanitization method is MOST "
            "appropriate for drives that will be physically recycled (not reused internally)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Perform a single-pass overwrite using DBAN on each drive.",
                "correct": False,
                "rationale": "Incorrect. While a single-pass overwrite is acceptable for many use cases under NIST 800-88, physical destruction is the highest-assurance method for drives headed to external recyclers where the IT team loses custody control.",
            },
            {
                "id": "b",
                "text": "Delete all user profile folders and empty the Recycle Bin on each machine.",
                "correct": False,
                "rationale": "Incorrect. Deleting files only removes directory entries; data remains on disk and is trivially recoverable with free tools. This is the lowest possible assurance level and wholly inadequate for HR confidential data.",
            },
            {
                "id": "c",
                "text": "Degauss or physically shred/destroy the drives, then document destruction with a certificate of destruction.",
                "correct": True,
                "rationale": "Correct. Physical destruction (shredding, crushing, degaussing) provides the highest assurance of unrecoverability. A certificate of destruction documents compliance and chain-of-custody for audit purposes. This is the recommended method when drives will not be reused.",
            },
            {
                "id": "d",
                "text": "Reformat each drive using Windows Disk Management quick format.",
                "correct": False,
                "rationale": "Incorrect. Quick format only removes the partition table and file system structure, leaving all data intact and easily recoverable. Even a full format provides only basic overwrite protection on HDDs.",
            },
        ],
        "explanation": (
            "NIST 800-88 data sanitization levels (low to high): Clear (overwrite, acceptable for reuse), "
            "Purge (cryptographic erase or secure overwrite), Destroy (physical shredding/degaussing — no recovery possible). "
            "For drives leaving organizational custody, Destroy is preferred. "
            "Always document destruction with a certificate for regulatory and audit trails. "
            "SSDs require cryptographic erase (Purge) or physical destruction because overwrite alone may not reach all NAND cells."
        ),
    },
    {
        "id": "c2d4v2-016",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "A UPS in a server room begins emitting a continuous alarm. The technician checks "
            "the display and sees the battery is at 12% and utility power is still active "
            "(no outage). Which condition MOST likely triggered this alarm?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The UPS is overloaded and drawing more power than its rated capacity from the utility feed.",
                "correct": False,
                "rationale": "Incorrect. An overload condition would typically trigger an overload alarm (distinct audible/visual pattern) and may cause the UPS to bypass or shut down, not a low-battery alarm on utility power.",
            },
            {
                "id": "b",
                "text": "The UPS battery has degraded or failed and is not being charged normally despite utility power being present.",
                "correct": True,
                "rationale": "Correct. A UPS battery at 12% with active utility power indicates the battery is either failing to charge (bad battery, failed charger circuit, or a recent deep discharge that exceeded battery capacity) and needs replacement. UPS batteries typically need replacement every 3–5 years.",
            },
            {
                "id": "c",
                "text": "The UPS is in bypass mode and the battery is not connected to the system.",
                "correct": False,
                "rationale": "Incorrect. Bypass mode (static or manual) connects the load directly to utility power and typically triggers a bypass indicator — not a low-battery alarm. In bypass, the battery charge state may not be displayed or relevant.",
            },
            {
                "id": "d",
                "text": "The utility voltage is too high, causing the UPS to run on battery to protect equipment.",
                "correct": False,
                "rationale": "Incorrect. UPS units protect against overvoltage using an AVR or surge suppression circuit — they do not typically switch to battery for an overvoltage condition. A continuous low-battery alarm with utility power present points to battery failure, not input voltage.",
            },
        ],
        "explanation": (
            "UPS maintenance: batteries degrade over time (3–5 year typical lifespan). "
            "Low-battery alarm with utility power present = battery not accepting charge or severely degraded. "
            "Regular UPS tests (monthly self-test, annual discharge test) catch battery degradation before a real outage. "
            "Replace batteries proactively. Document battery replacement dates in the asset record."
        ),
    },
    # ── 4.6 Incident response / licensing / regulated data ───────────────────
    {
        "id": "c2d4v2-017",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A technician images a suspect workstation's drive for forensic analysis and records "
            "the MD5 hash as 'A1B2C3...' at the time of imaging. Three weeks later in court, "
            "the opposing counsel challenges evidence integrity. The technician hashes the "
            "original drive again and gets 'A1B2C3...' — an identical value. What does this "
            "hash verification MOST directly prove?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The drive was not accessed or altered after the original image was taken.",
                "correct": False,
                "rationale": "Incorrect. Hash verification proves bit-for-bit integrity of the drive content at the time of the second hash compared to the time of the first hash. It does not directly prove absence of access — it proves absence of modification.",
            },
            {
                "id": "b",
                "text": "The drive content is bit-for-bit identical to what it was when imaged, establishing that the evidence has not been tampered with.",
                "correct": True,
                "rationale": "Correct. A cryptographic hash (MD5, SHA-256) produces a unique fingerprint of data. An identical hash value before and after means not a single bit has changed, directly establishing evidence integrity for chain-of-custody purposes.",
            },
            {
                "id": "c",
                "text": "The drive was properly handled and stored in the evidence locker the entire time.",
                "correct": False,
                "rationale": "Incorrect. The hash verifies data integrity, not physical handling history. The physical chain of custody log (sign-in/sign-out records, evidence bag seals) documents handling. Both are required for complete chain of custody.",
            },
            {
                "id": "d",
                "text": "The forensic image on which analysis was performed is admissible as the original evidence.",
                "correct": False,
                "rationale": "Incorrect. The forensic image's admissibility depends on hashing the image at creation and verifying it matches the original drive hash — not just re-hashing the original. The image is analyzed; the hashed original is preserved.",
            },
        ],
        "explanation": (
            "Chain-of-custody hash verification: hash the original drive immediately after seizure (establishes baseline), "
            "hash the forensic image after creation (confirms perfect copy), hash the original again if challenged "
            "(confirms it was not modified). "
            "SHA-256 is preferred over MD5 (collision vulnerabilities in MD5) for legal proceedings. "
            "The chain-of-custody log documents who had access and when — the hash proves what the content was."
        ),
    },
    {
        "id": "c2d4v2-018",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A manager asks a technician to inspect a colleague's work laptop for 'suspicious "
            "activity' without the user's knowledge and without submitting a formal incident "
            "request. The manager claims verbal authorization is sufficient. Which action "
            "should the technician take?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Proceed with the inspection since managers have authority over their employees' devices.",
                "correct": False,
                "rationale": "Incorrect. Even when managers have authority, forensic access to an employee's device requires formal authorization through established channels (HR, legal, IT security) to ensure the investigation is lawful, documented, and the evidence is admissible.",
            },
            {
                "id": "b",
                "text": "Refuse to inspect the device and report the manager's request to HR.",
                "correct": False,
                "rationale": "Incorrect. Outright refusal without escalation is not the best response. The request may be legitimate but improperly channeled. The correct action involves proper escalation and documentation, not simple refusal.",
            },
            {
                "id": "c",
                "text": "Decline to proceed without formal written authorization through the proper incident-response or HR/legal process, and document the manager's verbal request.",
                "correct": True,
                "rationale": "Correct. Proper chain-of-custody and incident-response procedures require formal written authorization before accessing a user's device forensically. Documenting the verbal request protects the technician and creates a record. Proceeding without proper authorization could violate privacy laws and taint evidence.",
            },
            {
                "id": "d",
                "text": "Inspect the device and document the findings in a personal notebook rather than the ticketing system to maintain confidentiality.",
                "correct": False,
                "rationale": "Incorrect. Documenting in a personal notebook rather than official channels breaks chain-of-custody requirements and removes the institutional oversight required for a proper investigation.",
            },
        ],
        "explanation": (
            "Incident response chain-of-custody requires: formal written authorization from appropriate authority (HR, legal, CISO), "
            "proper documentation in official systems, and following established procedures before accessing any device forensically. "
            "Unauthorized or informally authorized access may violate employee privacy rights, render evidence inadmissible, "
            "and expose the technician and organization to legal liability."
        ),
    },
    {
        "id": "c2d4v2-019",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "An employee emails a spreadsheet containing the full names, home addresses, "
            "Social Security numbers, and birth dates of 500 customers to a personal Gmail "
            "account 'to work from home.' Which data classification type is MOST at risk, "
            "and which regulation is MOST likely violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "PHI under HIPAA, because names and addresses are health-related",
                "correct": False,
                "rationale": "Incorrect. PHI requires a health or medical component. Names, addresses, SSNs, and birth dates alone are PII — not PHI — unless linked to a medical condition or treatment record.",
            },
            {
                "id": "b",
                "text": "PII potentially subject to state breach-notification laws and/or GDPR (if EU data subjects are included), because SSNs, names, and addresses are directly identifying",
                "correct": True,
                "rationale": "Correct. SSN, full name, home address, and birth date are classic PII identifiers. Emailing PII to a personal, uncontrolled account is a data breach / unauthorized disclosure. Applicable regulations depend on jurisdiction (U.S. state laws mandate breach notification; GDPR applies if any EU residents' data is included).",
            },
            {
                "id": "c",
                "text": "PCI DSS data, because customer financial information is implied",
                "correct": False,
                "rationale": "Incorrect. PCI DSS specifically governs payment card numbers (credit/debit). SSNs and addresses are not PCI data unless credit card numbers are also present.",
            },
            {
                "id": "d",
                "text": "No regulated data is involved because the employee is only accessing their own company's customer data.",
                "correct": False,
                "rationale": "Incorrect. Organizations have legal obligations to protect customer PII regardless of whether the data is accessed by an employee vs. an outsider. Unauthorized transmission to a personal account is a policy violation and likely a regulatory breach.",
            },
        ],
        "explanation": (
            "PII = any data that can identify an individual (name + SSN + DOB + address are textbook PII). "
            "PHI = PII with a health/medical component, governed by HIPAA. PCI = payment card numbers, governed by PCI DSS. "
            "GDPR = personal data of EU residents. U.S. PII is primarily regulated at the state level (e.g., CCPA, state breach-notification laws). "
            "Emailing PII to uncontrolled personal accounts is an unauthorized disclosure — a reportable data breach in most frameworks."
        ),
    },
    {
        "id": "c2d4v2-020",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "A company purchases 50 licenses of an OEM operating system bundled with new PCs. "
            "After a PC fails and is replaced with a spare, the IT team wants to install the "
            "OEM OS license on the spare. Why is this NOT permitted?"
        ),
        "options": [
            {
                "id": "a",
                "text": "OEM licenses are tied to the original hardware they shipped with and are non-transferable to different machines.",
                "correct": True,
                "rationale": "Correct. OEM (Original Equipment Manufacturer) software licenses are permanently bound to the specific hardware they were sold with. They cannot be transferred to a different machine, even within the same organization. This is a key distinguishing feature vs. retail or volume licenses.",
            },
            {
                "id": "b",
                "text": "OEM licenses require annual renewal and have expired after 12 months.",
                "correct": False,
                "rationale": "Incorrect. OEM OS licenses (e.g., Windows OEM) are perpetual (not subscription-based) but are hardware-locked. Renewal is not the issue.",
            },
            {
                "id": "c",
                "text": "OEM software can only be used on servers, not desktop PCs.",
                "correct": False,
                "rationale": "Incorrect. OEM licensing is used for both desktop and server systems. The hardware-lock restriction applies to both.",
            },
            {
                "id": "d",
                "text": "The spare PC does not meet the minimum hardware requirements for the OS.",
                "correct": False,
                "rationale": "Incorrect. Hardware requirements are a separate consideration. The licensing constraint — hardware binding — is the reason the OEM license cannot be moved, regardless of the spare's specifications.",
            },
        ],
        "explanation": (
            "Software license types: OEM — hardware-bound, non-transferable, cheaper, no retail support. "
            "Retail — transferable between machines, user owns the license. "
            "Volume/Enterprise — tied to an organization, managed via KMS/MAK, transferable within the org. "
            "Open-source — governed by open-source license (MIT, GPL, etc.). "
            "Subscription — time-limited, revoked when subscription lapses. "
            "OEM misuse (moving to a different machine) is a license violation."
        ),
    },
    # ── 4.7 Communication and professionalism ─────────────────────────────────
    {
        "id": "c2d4v2-021",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A technician is repairing a computer on-site and overhears a heated argument between "
            "two executives in the adjacent office. One executive mentions a confidential merger "
            "that is not yet public. After the visit, a friend asks the technician if the company "
            "is 'doing anything interesting.' Which response is MOST professional?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Share a vague hint that 'big things are coming' without naming the company.",
                "correct": False,
                "rationale": "Incorrect. Even vague disclosures of confidential information overheard on a client site are a breach of professional confidentiality. The information is not the technician's to share in any form.",
            },
            {
                "id": "b",
                "text": "Decline to share any information about observations made at client sites.",
                "correct": True,
                "rationale": "Correct. Technicians are obligated to maintain client confidentiality. Information observed or overheard while on a client site — including business conversations, documents, or system contents — must not be disclosed to anyone outside the authorized incident context.",
            },
            {
                "id": "c",
                "text": "Post a cryptic comment on social media without naming the company directly.",
                "correct": False,
                "rationale": "Incorrect. Any posting about client site experiences, even anonymized or cryptic, violates confidentiality obligations and CompTIA's explicitly stated prohibition on sharing customer information on social media.",
            },
            {
                "id": "d",
                "text": "Report the conversation to the client's IT manager to ensure it is documented.",
                "correct": False,
                "rationale": "Incorrect. The technician's role is to service equipment, not to monitor or report on executive conversations. Reporting non-IT observations to management is outside the technician's scope and could create legal or professional complications.",
            },
        ],
        "explanation": (
            "CompTIA professionalism: never disclose experiences at customer sites — on social media or in personal conversations. "
            "Client confidentiality extends to everything observed: documents, conversations, business information, personnel situations. "
            "The obligation applies even to information overheard incidentally, not just directly accessed as part of the job."
        ),
    },
    {
        "id": "c2d4v2-022",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A technician schedules a 1-hour on-site appointment for a network troubleshooting "
            "visit. Upon arrival, the issue turns out to be far more complex than anticipated "
            "and will require at least 3 additional hours. The client has a meeting in 90 minutes. "
            "Which communication approach is MOST professional?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Work silently and as fast as possible, hoping to finish before the client's meeting.",
                "correct": False,
                "rationale": "Incorrect. Working without informing the client of the timeline change leaves them with no opportunity to adjust plans. They may be forced to cancel their meeting without warning, damaging the relationship.",
            },
            {
                "id": "b",
                "text": "Immediately inform the client that the issue is more complex than expected, provide an updated time estimate, and ask whether they prefer to continue now or reschedule.",
                "correct": True,
                "rationale": "Correct. Setting clear and updated expectations when circumstances change is a core professionalism principle. Giving the client the information to make an informed decision (continue or reschedule) demonstrates respect for their time and maintains trust.",
            },
            {
                "id": "c",
                "text": "Leave after the original 1-hour window and submit a ticket for a follow-up visit without telling the client.",
                "correct": False,
                "rationale": "Incorrect. Leaving without explaining the situation or offering options abandons the client mid-issue and violates the expectation of transparent communication.",
            },
            {
                "id": "d",
                "text": "Tell the client the issue is simple and will be fixed quickly to avoid causing alarm.",
                "correct": False,
                "rationale": "Incorrect. Providing false assurance violates honesty norms, and the client will quickly discover the misrepresentation when the repair takes far longer, severely damaging trust.",
            },
        ],
        "explanation": (
            "CompTIA professionalism principles include: set and manage clear expectations, communicate timeline changes proactively, "
            "never make promises you cannot keep, and respect the customer's time. "
            "When scope changes, inform the customer immediately with updated estimates and options. "
            "This applies both to on-site visits and remote support calls."
        ),
    },
    {
        "id": "c2d4v2-023",
        "domain": 4,
        "objective": "4.7",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Communication & professionalism",
        "stem": (
            "A technician on a support call uses several technical acronyms (BSOD, RAID, POST) "
            "while explaining a problem to a non-technical user. The user responds with 'OK' "
            "but asks the same questions repeatedly. Which root cause MOST likely explains the "
            "user's behavior, and what should the technician do?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The user has a poor memory; the technician should speak more slowly and repeat acronyms louder.",
                "correct": False,
                "rationale": "Incorrect. Assuming a cognitive issue and speaking louder is condescending and counterproductive. The most likely cause is that the user does not understand the technical jargon, not a memory or hearing problem.",
            },
            {
                "id": "b",
                "text": "The user does not understand the technical terms; the technician should rephrase explanations using plain, jargon-free language and confirm understanding.",
                "correct": True,
                "rationale": "Correct. Polite 'OK' responses and repeated questions are classic indicators that the user does not understand but is reluctant to say so. CompTIA emphasizes avoiding jargon with non-technical users and confirming comprehension, not just delivering information.",
            },
            {
                "id": "c",
                "text": "The user is being difficult and should be transferred to a manager.",
                "correct": False,
                "rationale": "Incorrect. A user who is confused by technical terms is not 'being difficult' — they are lacking information the technician failed to communicate clearly. Escalating avoids the technician's communication responsibility.",
            },
            {
                "id": "d",
                "text": "The user needs a written technical report emailed after the call so they can reference the acronyms.",
                "correct": False,
                "rationale": "Incorrect. Sending a jargon-filled written report does not solve the comprehension problem. The immediate fix is to adjust communication style during the call.",
            },
        ],
        "explanation": (
            "CompTIA professionalism: avoid using technical jargon when speaking with non-technical users. "
            "Use plain language analogies, confirm understanding with open-ended questions ('Does that make sense?', "
            "'Can you describe what you see now?'), and listen actively for signs of confusion. "
            "Repeated questions from a user usually indicate they do not understand, not that they are being obstinate."
        ),
    },
    # ── 4.8 Scripting basics ─────────────────────────────────────────────────
    {
        "id": "c2d4v2-024",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A help desk receives a ticket: 'Users cannot run the nightly_report script on the "
            "Windows 10 workstation; double-clicking the file opens Notepad instead of executing "
            "it.' The file is named 'nightly_report.ps1'. What is the MOST likely cause?"
        ),
        "options": [
            {
                "id": "a",
                "text": ".ps1 files are not associated with PowerShell by default on Windows 10; double-clicking opens them in a text editor rather than executing them.",
                "correct": True,
                "rationale": "Correct. By design, Windows does not associate double-click execution with .ps1 files — they open in Notepad (or the default text editor) for security reasons. PowerShell scripts must be run explicitly via PowerShell.exe, the ISE, or a shortcut that invokes the interpreter.",
            },
            {
                "id": "b",
                "text": "The .ps1 extension is not recognized on Windows 10; the file should be renamed to .bat.",
                "correct": False,
                "rationale": "Incorrect. Windows 10 recognizes .ps1 as a PowerShell script file type. The issue is not recognition but execution association. Renaming to .bat would produce syntax errors since PowerShell syntax is not batch syntax.",
            },
            {
                "id": "c",
                "text": "PowerShell is not installed on Windows 10 by default, so the script cannot run.",
                "correct": False,
                "rationale": "Incorrect. PowerShell 5.1 ships with Windows 10 by default. The problem is the file association for double-click execution, not the absence of PowerShell.",
            },
            {
                "id": "d",
                "text": "The script has a syntax error on line 1, causing the editor to open instead of execution.",
                "correct": False,
                "rationale": "Incorrect. Syntax errors would cause a runtime error after the script starts executing, not prevent it from launching. The symptom (Notepad opens) indicates a file association issue, not a script error.",
            },
        ],
        "explanation": (
            "Windows security feature: .ps1 files open in a text editor when double-clicked because Windows intentionally "
            "does not register PowerShell as the default double-click handler for .ps1 files. "
            "To execute: right-click → 'Run with PowerShell', run from a PowerShell console, or use a .bat wrapper that calls powershell.exe -File script.ps1. "
            "Additionally, the PowerShell execution policy (Get-ExecutionPolicy) must allow the script to run."
        ),
    },
    {
        "id": "c2d4v2-025",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A Linux server administrator writes an automation script and saves it as 'deploy.sh'. "
            "When attempting to execute it with './deploy.sh', the shell returns: "
            "'Permission denied'. The file exists and the path is correct. "
            "Which action MOST directly resolves this error?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rename the file with a .bash extension instead of .sh.",
                "correct": False,
                "rationale": "Incorrect. The file extension does not control execute permissions on Linux. Renaming to .bash does not change the permission bits and will produce the same error.",
            },
            {
                "id": "b",
                "text": "Run 'chmod +x deploy.sh' to add execute permission to the file.",
                "correct": True,
                "rationale": "Correct. On Linux, newly created files do not have execute permission by default. 'chmod +x' sets the execute bit, allowing the file to be run directly. This is the standard fix for a 'Permission denied' error when executing a shell script.",
            },
            {
                "id": "c",
                "text": "Log in as root before running the script, since only root can execute .sh files.",
                "correct": False,
                "rationale": "Incorrect. Root access is not required to execute shell scripts. The execute permission must be set on the file itself, and any user with execute permission can run it. Running everything as root is also a security anti-pattern.",
            },
            {
                "id": "d",
                "text": "Move the script to /usr/bin/ so that the PATH variable can locate it.",
                "correct": False,
                "rationale": "Incorrect. Moving to /usr/bin/ changes the script's location but not its execute permissions. The same 'Permission denied' error would occur in /usr/bin/ if the execute bit is not set.",
            },
        ],
        "explanation": (
            "Linux file permissions: read (r/4), write (w/2), execute (x/1) for owner, group, others. "
            "chmod +x filename adds execute permission for all. chmod 755 is common for scripts (owner: rwx, group/others: r-x). "
            "Newly created files default to 644 (rw-r--r--) — no execute bit. "
            "This is a fundamental Linux scripting task covered in CompTIA A+ objective 4.8."
        ),
    },
    {
        "id": "c2d4v2-026",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Scripting basics",
        "stem": (
            "An administrator writes a Python script to automate user account provisioning. "
            "During testing, the script inadvertently creates 200 duplicate Active Directory "
            "accounts before the error is caught. Which scripting best practice would MOST "
            "effectively have prevented this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Run the script with elevated domain admin privileges to ensure it has permission to create accounts.",
                "correct": False,
                "rationale": "Incorrect. Elevated privileges make the problem worse (more impact from an error), not better. The principle of least privilege should be applied — use only the permissions necessary for the task.",
            },
            {
                "id": "b",
                "text": "Test the script in a non-production (sandbox/dev) AD environment with a small subset of test data before running in production.",
                "correct": True,
                "rationale": "Correct. Sandbox testing with a representative but small test dataset would have revealed the duplicate-creation bug against test accounts, not 200 real ones. This is the primary mitigation for the risk of inadvertently changing system settings.",
            },
            {
                "id": "c",
                "text": "Schedule the script to run at night when fewer users are active to reduce impact.",
                "correct": False,
                "rationale": "Incorrect. Timing does not prevent the logic error from occurring; it only shifts when the damage happens. The duplicate accounts would still be created regardless of the time of day.",
            },
            {
                "id": "d",
                "text": "Add a comment block to the script explaining what it does before deploying it.",
                "correct": False,
                "rationale": "Incorrect. Comments improve code readability but do not affect script behavior or test the logic. Documentation does not substitute for functional testing.",
            },
        ],
        "explanation": (
            "CompTIA scripting risks: (1) unintentionally introducing malware, (2) inadvertently changing system settings. "
            "Mitigation: sandbox testing against non-production systems with controlled test data; "
            "code review before deployment; dry-run mode (print what would be changed without executing); "
            "least-privilege execution; version control and peer review. "
            "Scripts performing write/create operations are especially dangerous without prior testing."
        ),
    },
    {
        "id": "c2d4v2-027",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A Windows technician needs to quickly automate a simple task: rename 30 files in a "
            "folder by appending today's date to each filename. The technician has no PowerShell "
            "experience and needs the simplest possible solution. Which script type is MOST "
            "appropriate for this straightforward Windows task?"
        ),
        "options": [
            {
                "id": "a",
                "text": ".py (Python)",
                "correct": False,
                "rationale": "Incorrect. Python is capable and cross-platform, but requires Python to be installed and has more syntax overhead for a simple file-renaming task on Windows than a batch file.",
            },
            {
                "id": "b",
                "text": ".bat (Windows batch file)",
                "correct": True,
                "rationale": "Correct. A .bat file using the built-in %date% variable and a for loop is the simplest native solution for a one-off file-renaming task on Windows. It requires no additional software, runs natively in cmd.exe, and has minimal syntax for straightforward operations.",
            },
            {
                "id": "c",
                "text": ".sh (Bash shell script)",
                "correct": False,
                "rationale": "Incorrect. .sh scripts require WSL or Git Bash on Windows and are the native solution on Linux/macOS, not Windows. They add unnecessary complexity for a native Windows task.",
            },
            {
                "id": "d",
                "text": ".js (JavaScript)",
                "correct": False,
                "rationale": "Incorrect. JavaScript is primarily a browser or Node.js scripting language. While Windows Script Host can run JScript (.js), it is not the conventional or simplest choice for file system automation on Windows.",
            },
        ],
        "explanation": (
            "Choosing the right script type for the task and platform: "
            ".bat is simple, native, and zero-setup on Windows for straightforward automation. "
            ".ps1 (PowerShell) is better for complex tasks requiring structured data, WMI, or remote management. "
            ".py is best for cross-platform logic or complex processing. "
            ".sh is the native choice on Linux/macOS. "
            "For a quick Windows-only file task, .bat is optimal."
        ),
    },
    # ── 4.9 Remote access technologies ───────────────────────────────────────
    {
        "id": "c2d4v2-028",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A network administrator needs to securely manage configurations on a Linux-based "
            "firewall appliance from a Windows 11 workstation. The firewall has no graphical "
            "interface. Which remote access method should the administrator use?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RDP (Remote Desktop Protocol)",
                "correct": False,
                "rationale": "Incorrect. RDP provides graphical desktop access and is designed for Windows. A Linux firewall with no GUI cannot be meaningfully managed via RDP, and RDP is not native to Linux without additional software (e.g., xrdp).",
            },
            {
                "id": "b",
                "text": "SSH (Secure Shell)",
                "correct": True,
                "rationale": "Correct. SSH provides an encrypted, authenticated command-line interface to remote Linux/Unix systems. It is the industry standard for managing CLI-only Linux appliances from any platform, and Windows 11 includes a built-in OpenSSH client.",
            },
            {
                "id": "c",
                "text": "Telnet",
                "correct": False,
                "rationale": "Incorrect. Telnet provides CLI access but transmits all data — including credentials — in plain text. It is a security risk and should not be used for managing network appliances. SSH replaced Telnet specifically for this reason.",
            },
            {
                "id": "d",
                "text": "VNC (Virtual Network Computing)",
                "correct": False,
                "rationale": "Incorrect. VNC provides graphical desktop sharing. A CLI-only Linux firewall has no desktop to share. VNC also requires software installation on the remote system and provides no advantage over SSH for CLI management.",
            },
        ],
        "explanation": (
            "SSH (port 22) is the standard encrypted protocol for remote CLI management of Linux/Unix/network appliances. "
            "Windows 11 and Windows 10 (1803+) include OpenSSH client natively (ssh command in PowerShell/cmd). "
            "SSH key-based authentication is more secure than password authentication for administrative access. "
            "Telnet (port 23) is the legacy, insecure predecessor — flag and disable it in any security review."
        ),
    },
    {
        "id": "c2d4v2-029",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Remote access technologies",
        "stem": (
            "A help desk technician uses a third-party remote desktop tool to connect to a "
            "user's PC through a cloud relay server, without configuring any firewall rules. "
            "Which feature of this type of tool MOST explains why no inbound firewall ports "
            "need to be opened on the client machine?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The tool uses UDP rather than TCP, which bypasses firewall rule enforcement.",
                "correct": False,
                "rationale": "Incorrect. Firewalls inspect both TCP and UDP traffic. Using UDP does not inherently bypass firewall rules. This is technically incorrect.",
            },
            {
                "id": "b",
                "text": "The client agent initiates an outbound connection to the cloud relay; both parties connect outbound, so no inbound firewall hole is required.",
                "correct": True,
                "rationale": "Correct. Tools like TeamViewer, AnyDesk, and most RMM agents work by having both the client and the technician initiate outbound connections to a cloud relay/broker. Since most firewalls allow outbound traffic by default, no inbound port forwarding is needed on the client's network.",
            },
            {
                "id": "c",
                "text": "The tool runs in the browser and uses HTTPS port 443, which is always allowed inbound.",
                "correct": False,
                "rationale": "Incorrect. HTTPS port 443 is usually allowed outbound, not inbound to client workstations. Browser-based tools still rely on outbound connections from the client, not inbound connections to the client.",
            },
            {
                "id": "d",
                "text": "The firewall automatically detects and whitelists remote support tool traffic as trusted.",
                "correct": False,
                "rationale": "Incorrect. Firewalls do not automatically whitelist remote support tool traffic. Standard enterprise firewalls require explicit rules for inbound connections. The tool avoids this by using outbound-only connections through a relay.",
            },
        ],
        "explanation": (
            "Cloud-relay remote access tools (TeamViewer, AnyDesk, ConnectWise Control, Quick Assist) work by having both "
            "the client and the support technician initiate outbound connections to a shared relay infrastructure. "
            "The relay brokers the session. Since outbound traffic on standard ports (443/TCP) is allowed by default on most "
            "firewalls, no inbound NAT or firewall rules are needed at the client site — a key advantage over raw RDP which "
            "requires inbound port 3389 to be open."
        ),
    },
    {
        "id": "c2d4v2-030",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A company's security policy prohibits Remote Desktop Protocol (RDP) access directly "
            "from the public internet to internal servers. A remote administrator needs to manage "
            "servers using RDP. Which architecture BEST satisfies both the security policy "
            "and the operational requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Enable RDP on all servers and open port 3389 on the perimeter firewall for the administrator's home IP only.",
                "correct": False,
                "rationale": "Incorrect. IP-whitelisting port 3389 on the perimeter firewall still exposes RDP to the internet (for a specific IP), which typically violates a 'no direct RDP from the internet' policy and leaves the server vulnerable to IP spoofing and the administrator's dynamic home IP changing.",
            },
            {
                "id": "b",
                "text": "Require the administrator to connect to the corporate VPN first, then use RDP over the encrypted VPN tunnel to reach internal servers.",
                "correct": True,
                "rationale": "Correct. VPN + RDP is the standard architecture for remote administrator access. The VPN authenticates the user and creates an encrypted tunnel, making the RDP traffic appear as an internal connection. RDP port 3389 is never exposed to the public internet.",
            },
            {
                "id": "c",
                "text": "Replace RDP with Telnet to use a simpler protocol that is easier to secure.",
                "correct": False,
                "rationale": "Incorrect. Telnet is less secure than RDP — it transmits credentials in plaintext. Replacing a functional protocol with a weaker one is never the correct security approach.",
            },
            {
                "id": "d",
                "text": "Use MSRA (Microsoft Remote Assistance) instead of RDP for server management.",
                "correct": False,
                "rationale": "Incorrect. MSRA is designed for desktop support with user interaction, not unattended server management. It requires the remote user to be present and initiate the session, which is impractical for headless server administration.",
            },
        ],
        "explanation": (
            "VPN + RDP is a fundamental layered security architecture: VPN provides authentication, encryption, and network-level access control "
            "(port 3389 closed to internet); RDP provides the graphical session once inside the trusted VPN. "
            "Alternatives include Jump Servers / Bastion Hosts (RDP from internet to bastion only, then RDP internally). "
            "Direct RDP from internet — even with NLA — is considered high risk due to brute-force and vulnerability exposure (e.g., BlueKeep)."
        ),
    },
    # ── Multiple-response questions (5) ───────────────────────────────────────
    {
        "id": "c2d4v2-031",
        "domain": 4,
        "objective": "4.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Backup types",
        "stem": (
            "An IT architect is evaluating backup strategies. Select the TWO statements that are "
            "TRUE regarding incremental vs. differential backup behavior with respect to the "
            "archive bit. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "An incremental backup backs up files with the archive bit set and then clears (resets) the archive bit.",
                "correct": True,
                "rationale": "Correct. Incremental backups copy changed files (archive bit set) then clear the bit, so the next incremental only captures changes since the last backup — keeping individual sets small.",
            },
            {
                "id": "b",
                "text": "A differential backup backs up files with the archive bit set but does NOT clear the archive bit.",
                "correct": True,
                "rationale": "Correct. Differential backups read the archive bit but do not reset it. This means each differential accumulates all changes since the last full, which is why they grow in size daily but only require one set (plus the full) for restore.",
            },
            {
                "id": "c",
                "text": "A full backup does not interact with the archive bit in any way.",
                "correct": False,
                "rationale": "Incorrect. A full backup copies all selected files and clears the archive bit on all backed-up files, resetting the baseline for subsequent incrementals or differentials.",
            },
            {
                "id": "d",
                "text": "Differential backups require more restore sets than incremental backups for the same recovery period.",
                "correct": False,
                "rationale": "Incorrect. This is backwards. Differential backups require fewer restore sets (full + 1 differential). Incrementals require more sets (full + every incremental since the full).",
            },
        ],
        "explanation": (
            "Archive bit / backup type matrix: "
            "Full — reads all files, clears archive bit. "
            "Incremental — reads files with archive bit set, clears archive bit. "
            "Differential — reads files with archive bit set, does NOT clear archive bit. "
            "This explains why incrementals are small but restores are slow (many sets), and differentials grow but restores are fast (two sets)."
        ),
    },
    {
        "id": "c2d4v2-032",
        "domain": 4,
        "objective": "4.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Change management",
        "stem": (
            "A change request form is being reviewed by the CAB. Select the THREE elements that "
            "MUST be present on a complete change request form per CompTIA A+ best practices. "
            "(Choose THREE.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "A documented rollback plan",
                "correct": True,
                "rationale": "Correct. A rollback plan is mandatory — it defines how to revert the change if it fails, and the CAB will not approve a change without one.",
            },
            {
                "id": "b",
                "text": "The end-user's personal home address for after-hours contact",
                "correct": False,
                "rationale": "Incorrect. Personal home addresses of end users are not required on a change request form and would be a privacy violation. The responsible staff member's contact details are required, not end-user personal information.",
            },
            {
                "id": "c",
                "text": "Purpose and scope of the change",
                "correct": True,
                "rationale": "Correct. The CAB needs to understand what the change is, why it is needed, and what systems or services it affects in order to evaluate its risk and necessity.",
            },
            {
                "id": "d",
                "text": "Date, time, and maintenance window for the change",
                "correct": True,
                "rationale": "Correct. The scheduled date/time and maintenance window allow the CAB to assess user impact, plan notifications, and ensure the window does not conflict with other critical operations.",
            },
        ],
        "explanation": (
            "Mandatory change request fields per CompTIA A+: purpose/scope, affected systems, date/time/window, "
            "responsible staff member, risk analysis, rollback plan. "
            "The CAB uses these fields to evaluate whether to approve, defer, or reject the change. "
            "Incomplete change requests are returned to the submitter before CAB review."
        ),
    },
    {
        "id": "c2d4v2-033",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_response",
        "difficulty": "expert",
        "study_topic": "Prohibited content & incident response (chain of custody)",
        "stem": (
            "A technician discovers what appears to be stolen intellectual property on a "
            "contractor's laptop while performing routine maintenance. Select the TWO actions "
            "that BEST preserve chain of custody and comply with incident response procedures. "
            "(Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Stop all work on the device and do not open, copy, move, or delete any files.",
                "correct": True,
                "rationale": "Correct. Halting work preserves the device's current state. Any alteration — even opening a file — can change metadata (access timestamps) and compromise evidence integrity and chain of custody.",
            },
            {
                "id": "b",
                "text": "Immediately report the discovery to management and/or the appropriate security or legal team and document the date, time, and circumstances of discovery.",
                "correct": True,
                "rationale": "Correct. Chain of custody requires timely, documented reporting to authorized personnel. The report establishes the first entry in the custody log: who found what, when, and under what circumstances.",
            },
            {
                "id": "c",
                "text": "Quickly copy the suspected IP files to a company server for analysis before reporting.",
                "correct": False,
                "rationale": "Incorrect. Copying evidence alters file metadata, creates unanswered questions about integrity, and takes action before authorization — all of which damage chain of custody and may constitute unauthorized access.",
            },
            {
                "id": "d",
                "text": "Notify the contractor that their laptop will be held for investigation so they can gather their belongings.",
                "correct": False,
                "rationale": "Incorrect. Notifying the subject of an investigation before the evidence is secured gives them the opportunity to destroy evidence. This is explicitly contrary to incident response best practices.",
            },
        ],
        "explanation": (
            "Chain-of-custody first response: (1) stop — do not alter the device, (2) secure — prevent others from accessing it, "
            "(3) document — record discovery details with timestamp, (4) report — notify management/security/legal per policy. "
            "Never notify the subject before evidence is secured. Never copy evidence without authorization. "
            "Every person who accesses the device must be logged."
        ),
    },
    {
        "id": "c2d4v2-034",
        "domain": 4,
        "objective": "4.8",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Scripting basics",
        "stem": (
            "A security team is auditing scripts used across the enterprise. Select the TWO "
            "PRIMARY risks associated with running unreviewed scripts from external sources, "
            "as identified in CompTIA A+ objectives. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Unintentionally introducing malware embedded in or downloaded by the script",
                "correct": True,
                "rationale": "Correct. Scripts from untrusted sources may contain or fetch malware payloads. Because scripts execute with the permissions of the running user, embedded malware can have significant access to the system.",
            },
            {
                "id": "b",
                "text": "Inadvertently changing system settings or configuration",
                "correct": True,
                "rationale": "Correct. Scripts that perform write operations can modify registry entries, file permissions, user accounts, firewall rules, or application configurations in ways that are difficult to detect and reverse.",
            },
            {
                "id": "c",
                "text": "The script file extension will be rejected by Windows Defender automatically.",
                "correct": False,
                "rationale": "Incorrect. Windows Defender does scan scripts but does not universally reject all external scripts. Script-based attacks regularly bypass AV tools. AV is not the primary risk identified in this context.",
            },
            {
                "id": "d",
                "text": "The script may increase CPU usage, reducing gaming performance on workstations.",
                "correct": False,
                "rationale": "Incorrect. Performance impact is a minor consideration. The CompTIA-identified primary risks are security-focused: malware introduction and unintended system modification.",
            },
        ],
        "explanation": (
            "CompTIA A+ Core 2 objective 4.8 explicitly names two primary scripting risks: "
            "(1) unintentionally introducing malware, (2) inadvertently changing system settings. "
            "A third risk sometimes noted is browser/system crashes from poorly written scripts. "
            "Mitigations: review scripts before execution, test in sandbox environments, apply least-privilege execution, "
            "use code signing to verify script origin and integrity."
        ),
    },
    {
        "id": "c2d4v2-035",
        "domain": 4,
        "objective": "4.9",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Remote access technologies",
        "stem": (
            "A security policy review is examining all remote access methods in use. Select the "
            "TWO remote access technologies that present a significant risk due to transmitting "
            "data without native encryption. (Choose TWO.)"
        ),
        "options": [
            {
                "id": "a",
                "text": "Telnet",
                "correct": True,
                "rationale": "Correct. Telnet transmits all session data — including usernames, passwords, and commands — as unencrypted plain text, making it trivially interceptable with a packet capture tool.",
            },
            {
                "id": "b",
                "text": "VNC (Virtual Network Computing) without a VPN or SSH tunnel",
                "correct": True,
                "rationale": "Correct. Basic VNC implementations (RFB protocol) provide limited or no encryption by default. Authentication may be weak and session data can be captured. VNC should always be tunneled through SSH or VPN in production environments.",
            },
            {
                "id": "c",
                "text": "SSH (Secure Shell)",
                "correct": False,
                "rationale": "Incorrect. SSH was designed specifically to provide encrypted, authenticated remote access. It is the secure replacement for Telnet and rlogin.",
            },
            {
                "id": "d",
                "text": "RDP over TLS with Network Level Authentication (NLA)",
                "correct": False,
                "rationale": "Incorrect. RDP with TLS and NLA encrypts the session and requires authentication before establishing the remote desktop session. It is not an example of unencrypted remote access.",
            },
        ],
        "explanation": (
            "Encryption status of common remote access protocols: "
            "Telnet — no encryption (plain text, port 23). "
            "VNC — no built-in encryption in base RFB protocol (requires SSH tunnel or VPN). "
            "SSH — encrypted (AES, port 22). "
            "RDP with TLS/NLA — encrypted (TLS, port 3389). "
            "MSRA/Quick Assist — encrypted. "
            "VPN (IPsec/SSL) — encrypted. "
            "Flag Telnet and unencrypted VNC in any security audit."
        ),
    },
    # ── Additional hard/expert questions ──────────────────────────────────────
    {
        "id": "c2d4v2-036",
        "domain": 4,
        "objective": "4.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Documentation & ticketing",
        "stem": (
            "An IT manager reviews monthly ticket metrics and finds that 40% of tickets are "
            "escalated to tier 2 without documentation of what tier 1 already attempted. "
            "This results in tier 2 technicians repeating the same diagnostic steps. "
            "Which ticketing field, if consistently completed, would MOST directly eliminate "
            "this redundancy?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Severity/priority rating",
                "correct": False,
                "rationale": "Incorrect. The priority rating controls response time but does not document what troubleshooting steps were already attempted. It would not reduce redundant diagnostics by tier 2.",
            },
            {
                "id": "b",
                "text": "Escalation notes documenting all troubleshooting steps attempted at tier 1 before escalation",
                "correct": True,
                "rationale": "Correct. Escalation notes that detail every step already attempted (with results) allow tier 2 to pick up exactly where tier 1 left off, eliminating redundant steps, reducing time to resolution, and improving the escalation handoff quality.",
            },
            {
                "id": "c",
                "text": "Category field (hardware/software/network)",
                "correct": False,
                "rationale": "Incorrect. Categorization improves routing and reporting but does not communicate what was already tried. Tier 2 receiving a correctly categorized but diagnostically empty ticket still must start over.",
            },
            {
                "id": "d",
                "text": "Resolution field populated with 'escalated to tier 2'",
                "correct": False,
                "rationale": "Incorrect. Noting that a ticket was escalated only states the outcome, not the work performed. Tier 2 still lacks the diagnostic history needed to avoid repeating steps.",
            },
        ],
        "explanation": (
            "Effective escalation in ticketing requires: all actions taken to date, results/findings at each step, "
            "current state of the system, and any relevant diagnostic data collected. "
            "This is sometimes called 'escalation notes' or 'work notes' and is distinct from the final resolution field. "
            "Good escalation documentation is key to reducing MTTR and avoiding duplicate work across support tiers."
        ),
    },
    {
        "id": "c2d4v2-037",
        "domain": 4,
        "objective": "4.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Environmental controls",
        "stem": (
            "A facilities manager asks an IT technician to explain why the server room must "
            "be kept cooler than typical office space. The servers generate 15 kW of heat "
            "continuously. Which explanation is MOST technically accurate regarding the "
            "need for dedicated cooling?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Servers run cooler code when the room temperature is lower, improving software performance.",
                "correct": False,
                "rationale": "Incorrect. Software execution speed is not directly affected by room temperature in normal operating ranges. This conflates ambient temperature with processor clock speed, which is hardware-controlled.",
            },
            {
                "id": "b",
                "text": "Servers generate sustained high heat loads that standard HVAC cannot handle; elevated operating temperatures accelerate component failure and degrade reliability.",
                "correct": True,
                "rationale": "Correct. A 15 kW continuous heat load requires precision cooling (CRAC/CRAH units) that maintains the ASHRAE-recommended 18–27 °C inlet temperature. Sustained high temperatures accelerate electromigration in ICs, reduce capacitor lifespan, and increase the risk of thermal throttling and unplanned shutdowns.",
            },
            {
                "id": "c",
                "text": "Cold air is denser and provides better electrical conduction for server components.",
                "correct": False,
                "rationale": "Incorrect. Air density and electrical conduction are not factors in server cooling design. Servers do not use air as a conductor. This is a nonsensical distractor.",
            },
            {
                "id": "d",
                "text": "Regulatory compliance requires server rooms to be kept at exactly 18 °C regardless of heat load.",
                "correct": False,
                "rationale": "Incorrect. There is no universal regulation mandating exactly 18 °C. ASHRAE recommends a range (18–27 °C for inlet air). The actual setpoint depends on equipment specifications and efficiency targets.",
            },
        ],
        "explanation": (
            "Data center cooling fundamentals: servers convert electrical power to heat (near 100% efficiency). "
            "A 15 kW server load requires approximately 15 kW of cooling capacity. "
            "ASHRAE A1–A4 classes define allowable inlet temperature ranges. Precision CRAC/CRAH units are required because "
            "standard office HVAC lacks the capacity and precision to maintain narrow temperature/humidity ranges "
            "against dense compute loads. High temps cause: throttling, increased failure rates, reduced lifespan."
        ),
    },
    {
        "id": "c2d4v2-038",
        "domain": 4,
        "objective": "4.6",
        "type": "multiple_choice",
        "difficulty": "expert",
        "study_topic": "Licensing & regulated data (PII/PCI/GDPR/PHI)",
        "stem": (
            "An online retailer collects EU customers' names, shipping addresses, and payment "
            "card numbers. A data breach exposes 10,000 records. The CISO asks the IT team "
            "which regulatory notification obligations are triggered. Which answer MOST "
            "completely identifies the applicable obligations?"
        ),
        "options": [
            {
                "id": "a",
                "text": "HIPAA breach notification only, because health data may be inferred from purchase history.",
                "correct": False,
                "rationale": "Incorrect. HIPAA applies to covered health entities and their business associates. A retail company is not a HIPAA-covered entity, and purchase history inference does not constitute PHI. HIPAA notification is not triggered here.",
            },
            {
                "id": "b",
                "text": "GDPR breach notification (within 72 hours to the supervisory authority) for EU personal data, and PCI DSS incident response requirements for payment card data.",
                "correct": True,
                "rationale": "Correct. GDPR Article 33 requires notification to the relevant data protection authority within 72 hours of discovering a personal data breach affecting EU residents. PCI DSS requires notifying card brands and acquiring bank and following the PCI incident response plan when cardholder data is compromised. Both are triggered simultaneously.",
            },
            {
                "id": "c",
                "text": "No regulatory notification is required unless law enforcement determines a crime was committed.",
                "correct": False,
                "rationale": "Incorrect. GDPR and PCI DSS breach notification obligations are triggered by the breach itself, not by a law enforcement determination. Waiting for law enforcement would violate both the 72-hour GDPR window and PCI DSS contractual obligations.",
            },
            {
                "id": "d",
                "text": "PCI DSS notification only; GDPR does not apply to payment data.",
                "correct": False,
                "rationale": "Incorrect. GDPR applies to all personal data of EU residents — including names and addresses — not just payment data. The breach exposed PII (names, addresses) and PCI data (card numbers), triggering both regimes independently.",
            },
        ],
        "explanation": (
            "Breach notification quick reference: "
            "GDPR — 72 hours to supervisory authority, data subjects notified 'without undue delay' if high risk; applies to all EU resident personal data. "
            "PCI DSS — notify card brands and acquiring bank per incident response plan; timeline varies by card brand (typically 24–72 hours). "
            "HIPAA — 60 days from discovery for covered entities in the U.S. "
            "U.S. state laws — vary by state (30–90 days typical). "
            "Multiple frameworks can apply simultaneously; always identify all applicable obligations before crafting a response."
        ),
    },
]
