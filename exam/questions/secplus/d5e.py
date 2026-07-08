"""CompTIA Security+ SY0-701 practice questions -- Domain 5 (Security Program
Management and Oversight), file E.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 5 in
``_topic_labels.json``.
"""

QUESTIONS = [
    {
        "id": "nd5e-001",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A regional airline's flight-reservation platform is valued at $780,000 (asset value, AV). "
            "Security engineers estimate that a successful ransomware attack against the platform would "
            "encrypt or corrupt approximately 25% of its value (exposure factor, EF) before recovery. "
            "What is the single loss expectancy (SLE) for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$195,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $780,000 x 0.25 = $195,000, the expected loss from a single "
                    "occurrence of the event."
                ),
            },
            {
                "id": "b",
                "text": "$585,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the complement of the exposure factor (75%) instead of the stated "
                    "25% EF ($780,000 x 0.75), which represents the retained value, not the loss."
                ),
            },
            {
                "id": "c",
                "text": "$780,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is simply the asset value with the exposure factor ignored entirely, as if "
                    "the full asset were destroyed."
                ),
            },
            {
                "id": "d",
                "text": "$3,120,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from dividing AV by EF ($780,000 / 0.25) rather than multiplying, "
                    "producing a figure larger than the asset itself, which cannot be a valid SLE."
                ),
            },
        ],
        "explanation": (
            "SLE = Asset Value (AV) x Exposure Factor (EF). Here, $780,000 x 0.25 = $195,000. EF must be "
            "multiplied, not subtracted from 1 and applied, ignored, or divided into AV."
        ),
    },
    {
        "id": "nd5e-002",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A single loss expectancy (SLE) of $64,000 has been calculated for a credential-stuffing "
            "attack against a subscription streaming service's customer accounts. Security telemetry "
            "indicates this type of attack succeeds, on average, once every 8 years. What is the "
            "annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$8,000",
                "correct": True,
                "rationale": (
                    "Correct. ARO = 1 event / 8 years = 0.125. ALE = SLE x ARO = $64,000 x 0.125 = $8,000."
                ),
            },
            {
                "id": "b",
                "text": "$512,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing SLE by ARO ($64,000 / 0.125) instead of multiplying, "
                    "which inflates the figure far beyond the single-loss amount."
                ),
            },
            {
                "id": "c",
                "text": "$64,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats ALE as identical to SLE, ignoring the annualized rate of occurrence "
                    "entirely."
                ),
            },
            {
                "id": "d",
                "text": "$800",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading 'once every 8 years' as an ARO of 0.0125 (as if it "
                    "were once every 80 years) instead of the correct 0.125 (1/8)."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO. 'Once every 8 years' converts to ARO = 1/8 = 0.125. $64,000 x 0.125 = "
            "$8,000."
        ),
    },
    {
        "id": "nd5e-003",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "Before mitigation, the ALE for an unencrypted legacy file-transfer service at a logistics "
            "firm is $95,000/year. A proposed control (annual cost of safeguard, ACS, of $40,000) would "
            "reduce the ALE to $35,000/year. Using cost-benefit analysis of the control, what should the "
            "organization conclude?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The control produces a net benefit of $20,000/year ($60,000 ALE reduction minus the $40,000 "
                    "ACS), so it is cost-justified."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Value of the control = (ALE_before - ALE_after) - ACS = ($95,000 - $35,000) - "
                    "$40,000 = $60,000 - $40,000 = $20,000. A positive figure means the control is worth its "
                    "cost."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The control produces a net benefit of $60,000/year, because the ALE reduction alone "
                    "determines value regardless of the control's cost."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores the $40,000 ACS entirely. The cost of the safeguard must be "
                    "subtracted from the ALE reduction to determine net value, not disregarded."
                ),
            },
            {
                "id": "c",
                "text": "The control produces a net benefit of $55,000/year ($95,000 ALE before minus the $40,000 ACS).",
                "correct": False,
                "rationale": (
                    "Incorrect. This subtracts ACS from ALE_before while skipping ALE_after entirely, rather than "
                    "subtracting ACS from the actual ALE reduction ($60,000)."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The control produces a net loss of $5,000/year ($35,000 ALE after minus the $40,000 ACS), so "
                    "it is not cost-justified."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This subtracts ACS from ALE_after instead of from the ALE reduction, understating "
                    "the safeguard's benefit and reaching the wrong conclusion."
                ),
            },
        ],
        "explanation": (
            "Value of a control = (ALE_before - ALE_after) - ACS. ($95,000 - $35,000) - $40,000 = "
            "$20,000, a positive net benefit, so the control is cost-justified."
        ),
    },
    {
        "id": "nd5e-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A chemical manufacturing plant's process-control network has an asset value of $3,500,000. "
            "Security engineers estimate that a successful sabotage event against the network would "
            "destroy approximately 8% of the asset's value (EF), and historical incident data shows this "
            "type of event occurs, on average, 3 times per year (ARO = 3). What is the annualized loss "
            "expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$840,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $3,500,000 x 0.08 = $280,000. ALE = SLE x ARO = $280,000 x 3 = "
                    "$840,000."
                ),
            },
            {
                "id": "b",
                "text": "$280,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the SLE (AV x EF), but it stops there and never multiplies by the ARO of "
                    "3, understating the annualized exposure."
                ),
            },
            {
                "id": "c",
                "text": "$93,333",
                "correct": False,
                "rationale": (
                    "Incorrect. This divides the SLE by the ARO ($280,000 / 3) instead of multiplying by it, "
                    "which reduces rather than annualizes the loss figure."
                ),
            },
            {
                "id": "d",
                "text": "$10,500,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This multiplies AV directly by ARO ($3,500,000 x 3), skipping the exposure factor "
                    "entirely and drastically overstating the loss."
                ),
            },
        ],
        "explanation": (
            "ALE = AV x EF x ARO = $3,500,000 x 0.08 x 3 = $840,000. Unlike most scenarios where ARO is a "
            "fraction below 1, here ARO = 3 (three occurrences per year) still must be multiplied, not "
            "divided or ignored."
        ),
    },
    {
        "id": "nd5e-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A business impact analysis determines that the maximum tolerable downtime (MTD) for a "
            "hospital's electronic prescribing system is 90 minutes, beyond which patient safety is "
            "materially compromised. The current disaster recovery plan specifies a recovery time "
            "objective (RTO) of 3 hours for this system. What should this finding prompt the organization "
            "to do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Treat the RTO as a gap against the MTD and invest in faster recovery capability (such as a "
                    "hot site or automated failover) until the RTO falls within the 90-minute MTD."
                ),
                "correct": True,
                "rationale": (
                    "Correct. MTD is the hard, business-driven ceiling on downtime. When the planned RTO exceeds "
                    "the MTD, the current recovery capability is inadequate and must be improved to close the "
                    "gap."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Redefine the MTD to 3 hours so that it matches the current RTO, since the existing DR plan "
                    "already reflects what is operationally achievable."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards logic. MTD reflects patient-safety and business tolerance for "
                    "downtime, not whatever IT currently happens to be able to support."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Shorten the recovery point objective (RPO) for the system, since RPO and RTO measure the "
                    "same recovery constraint."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RPO addresses acceptable data loss measured backward in time, not recovery "
                    "duration; adjusting RPO does nothing to close a downtime gap against MTD."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Accept the gap as within normal tolerance, since 3 hours is a common industry-standard RTO "
                    "for clinical systems."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A generic industry benchmark does not override this organization's own "
                    "BIA-derived MTD, which was specifically tied to patient safety for this system."
                ),
            },
        ],
        "explanation": (
            "MTD is the outer limit of tolerable downtime a business process can sustain. When the "
            "planned RTO exceeds the BIA-derived MTD, the recovery capability -- not the MTD -- must "
            "change."
        ),
    },
    {
        "id": "nd5e-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A fleet of 15 identical warehouse barcode scanners logged a combined total of 65,700 "
            "operating hours over one year, experiencing 18 failures across the fleet. What metric is "
            "being calculated when an analyst divides 65,700 hours by 18 failures, and what is the "
            "resulting value?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MTBF of 3,650 hours",
                "correct": True,
                "rationale": (
                    "Correct. MTBF = total operating time / number of failures = 65,700 / 18 = 3,650 hours, the "
                    "average time the fleet operates between failures."
                ),
            },
            {
                "id": "b",
                "text": "MTTR of 3,650 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. The arithmetic (total time / failures) is correct for MTBF, but MTTR measures "
                    "average time to repair a failure, not average time between failures -- the wrong metric name "
                    "for this calculation."
                ),
            },
            {
                "id": "c",
                "text": "MTBF of 65,700 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This uses the total operating time without dividing by the 18 recorded failures, "
                    "which overstates the true average time between failures."
                ),
            },
            {
                "id": "d",
                "text": "MTBF of 4,380 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing total hours by the fleet size of 15 instead of the 18 "
                    "failure count (65,700 / 15 = 4,380), giving average hours per device rather than the mean "
                    "time between failures."
                ),
            },
        ],
        "explanation": (
            "MTBF = total operational time / number of failures = 65,700 / 18 = 3,650 hours. MTTR is a "
            "distinct metric measuring average repair duration, not derivable from this data."
        ),
    },
    {
        "id": "nd5e-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA for a mid-size bank identifies that the core ledger system has an RTO of 1 hour, while "
            "the customer-facing mobile banking app -- which depends entirely on the ledger system for "
            "balance and transaction data -- has an RTO of 30 minutes. During DR plan development, what "
            "does this finding indicate the organization MUST do?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Recognize that the mobile app's effective recovery time is constrained by the ledger "
                    "system's 1-hour RTO, and either shorten the ledger's RTO to 30 minutes or revise the app's "
                    "RTO to be realistic."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Because the mobile app depends on the ledger system, its true recovery cannot be "
                    "faster than its dependency's recovery. The BIA must reconcile the mismatch between the "
                    "dependent and upstream RTOs."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Restore the mobile banking app first, since it has the shorter RTO and therefore the higher "
                    "business priority."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Restoring the dependent app first is pointless if the ledger system it depends on "
                    "isn't yet available; recovery order must follow dependency chains, not RTO value alone."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Treat the two RTOs as independent targets, since RTO applies separately to each system "
                    "regardless of dependencies."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ignoring dependency chains during DR planning results in under-restored "
                    "functionality even after each system's individual RTO is technically met."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Lengthen the ledger system's RTO to match its lower business criticality relative to the "
                    "customer-facing app."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The ledger is the upstream dependency for the higher-priority app; lengthening "
                    "its RTO makes the mismatch worse rather than resolving it."
                ),
            },
        ],
        "explanation": (
            "When a dependent system's RTO is shorter than an upstream dependency's RTO, the dependent "
            "system's recovery is effectively bottlenecked by the dependency. BIA and DR planning must "
            "reconcile such dependency-chain mismatches rather than treating each RTO in isolation."
        ),
    },
    {
        "id": "nd5e-008",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "An oil-field services company signs a framework agreement with a specialized "
            "industrial-controls consultancy. The agreement fixes payment terms, insurance requirements, "
            "and intellectual-property ownership rules that will apply to dozens of individual statements "
            "of work (SOWs) over a multi-year relationship, but it does not itself specify the scope or "
            "deliverables of any particular engagement. Which type of agreement is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A master service agreement (MSA)",
                "correct": True,
                "rationale": (
                    "Correct. An MSA establishes the recurring legal and commercial terms (payment, insurance, IP "
                    "ownership) that govern a long-term vendor relationship, leaving specific scope and "
                    "deliverables to be defined in individual SOWs."
                ),
            },
            {
                "id": "b",
                "text": "A service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. No measurable performance metrics (uptime, response time) or penalties are "
                    "described; the scenario centers on recurring legal/commercial terms, not performance "
                    "commitments."
                ),
            },
            {
                "id": "c",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA documents a formal partnership with shared ownership, profit-sharing, or "
                    "joint governance. This scenario describes a standard vendor-services framework, not a joint "
                    "partnership."
                ),
            },
            {
                "id": "d",
                "text": "A non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA governs confidentiality of shared information only. It does not establish "
                    "payment terms, insurance requirements, or IP ownership rules across many engagements."
                ),
            },
        ],
        "explanation": (
            "An MSA is the recurring legal/commercial framework covering payment, liability, and IP terms "
            "for repeat engagements, with scope-specific details left to individual SOWs -- distinct from "
            "the performance metrics of an SLA or the joint-ownership structure of a BPA."
        ),
    },
    {
        "id": "nd5e-009",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A company's contracted DNS-hosting provider guarantees 99.99% monthly uptime, with "
            "escalating service credits owed to the customer for each defined tier of missed "
            "availability. Which agreement type defines this arrangement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A service level agreement (SLA)",
                "correct": True,
                "rationale": (
                    "Correct. Quantifiable performance metrics (uptime percentage) paired with enforceable "
                    "remedies (escalating service credits) for missed targets are the defining features of an "
                    "SLA."
                ),
            },
            {
                "id": "b",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA establishes joint ownership, profit-sharing, or governance between "
                    "partners. This scenario describes a single vendor's measurable performance commitment, not a "
                    "partnership."
                ),
            },
            {
                "id": "c",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding statement of mutual intent with no enforceable penalties. "
                    "This scenario explicitly describes binding service credits tied to missed metrics."
                ),
            },
            {
                "id": "d",
                "text": "A master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA sets overarching legal/commercial terms for repeat engagements without "
                    "itself defining specific performance metrics -- the opposite of this scenario's focus on "
                    "measurable uptime."
                ),
            },
        ],
        "explanation": (
            "SLAs are distinguished by measurable performance metrics (here, 99.99% uptime) paired with "
            "enforceable remedies (service credits) for missed targets."
        ),
    },
    {
        "id": "nd5e-010",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two public universities in different states want to formally document their mutual "
            "understanding to collaborate on a joint cybersecurity research grant, sharing high-level "
            "research goals and points of contact, but explicitly note that the document creates no "
            "binding financial or legal obligations on either party. Which type of agreement is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A memorandum of understanding (MOU)",
                "correct": True,
                "rationale": (
                    "Correct. An MOU documents a good-faith, non-binding statement of mutual intent to cooperate, "
                    "which matches the explicitly non-binding, no-financial-obligation nature described here."
                ),
            },
            {
                "id": "b",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA implies a binding partnership with shared liability, ownership, or "
                    "financial obligations, which directly contradicts the scenario's explicit statement that no "
                    "binding obligations are created."
                ),
            },
            {
                "id": "c",
                "text": "A service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. No measurable performance metrics or penalties for missed targets are described; "
                    "the scenario is a non-binding statement of cooperative intent, not a performance contract."
                ),
            },
            {
                "id": "d",
                "text": "A master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA is a binding legal framework governing repeat commercial engagements. This "
                    "scenario explicitly describes a non-binding document with no legal obligations, the defining "
                    "opposite of an MSA."
                ),
            },
        ],
        "explanation": (
            "An MOU documents mutual intent to cooperate without creating binding legal or financial "
            "obligations -- distinct from the enforceable commitments of an SLA, MSA, or BPA."
        ),
    },
    {
        "id": "nd5e-011",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "During an annual vendor review, a company's security team wants to formally exercise a "
            "contractual right to review a critical vendor's security controls, but the vendor refuses to "
            "schedule an on-site assessment, citing an unusually busy quarter. What should the security "
            "team do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Reference the specific right-to-audit clause in the signed contract and formally invoke it, "
                    "escalating through the vendor relationship owner if the vendor continues to refuse."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The contract should already grant the audit right; formally invoking it per its "
                    "terms, and escalating if refused, is the appropriate first step to enforce contractual "
                    "oversight."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Immediately terminate the vendor contract for breach, since refusing an audit request is "
                    "grounds for termination."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Termination is premature as a first action; it should follow formal escalation "
                    "and documented non-compliance with the contractual audit clause, not precede any attempt to "
                    "enforce it."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Accept the vendor's self-attested security questionnaire completed during onboarding as a "
                    "substitute for the scheduled audit."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A stale, self-attested questionnaire from onboarding does not satisfy a "
                    "contractual audit right or verify the vendor's current control state."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Quietly drop the audit request to preserve the business relationship, since the vendor is "
                    "described as critical to operations."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Abandoning contractual oversight of a critical vendor increases, rather than "
                    "manages, the organization's risk exposure."
                ),
            },
        ],
        "explanation": (
            "When a vendor resists a contractually granted audit right, the correct first step is to "
            "formally invoke the specific clause and escalate through the relationship owner -- not to "
            "accept a substitute, terminate immediately, or drop the request."
        ),
    },
    {
        "id": "nd5e-012",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "While reviewing a critical SaaS vendor's due-diligence package, a vendor risk analyst "
            "discovers that the vendor relies on an undisclosed fourth-party subcontractor to process a "
            "subset of customer data, a relationship not mentioned anywhere in the signed contract. What "
            "is the BEST next step?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Require the vendor to formally disclose all subcontractors and update the contract to extend "
                    "equivalent security and data-protection obligations to the subcontractor before continuing "
                    "the relationship."
                ),
                "correct": True,
                "rationale": (
                    "Correct. This directly addresses fourth-party risk by restoring visibility and contractually "
                    "flowing down equivalent obligations to the subcontractor, the standard vendor risk "
                    "management response."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Take no action, since the organization's contract is with the vendor directly and the vendor "
                    "is solely responsible for managing its own subcontractors."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Fourth-party processing still exposes the organization's data; the lack of "
                    "visibility and contractual flow-down is itself the risk that must be remediated, not "
                    "ignored."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Terminate the vendor relationship immediately, since using an undisclosed subcontractor is "
                    "an automatic disqualifying event."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Immediate termination is overly drastic as a first response, before assessing the "
                    "actual risk and attempting remediation through disclosure and contract updates."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ignore the finding as long as the subcontractor is located in the same country as the "
                    "primary vendor."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Subcontractor location does not address the core issue -- undisclosed data "
                    "processing and missing contractual obligations -- which exists regardless of jurisdiction."
                ),
            },
        ],
        "explanation": (
            "Undisclosed fourth-party subcontractors are addressed by requiring disclosure and extending "
            "equivalent contractual obligations down the supply chain, not by ignoring the finding, "
            "overreacting with immediate termination, or assuming location alone resolves the risk."
        ),
    },
    {
        "id": "nd5e-013",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Vendor risk management",
        "stem": (
            "During initial onboarding of a new vendor, select the TWO factors that should weigh MOST "
            "heavily in determining the vendor's inherent risk tier."
        ),
        "options": [
            {
                "id": "a",
                "text": "The sensitivity and volume of the organization's data the vendor will access, store, or process",
                "correct": True,
                "rationale": (
                    "Correct. The nature and amount of data exposed to the vendor is a primary driver of inherent "
                    "risk -- greater sensitivity and volume mean greater potential impact if the vendor is "
                    "compromised."
                ),
            },
            {
                "id": "b",
                "text": "How critical the vendor's product or service is to the organization's core business operations",
                "correct": True,
                "rationale": (
                    "Correct. Criticality to business operations directly drives inherent risk, since a "
                    "disruption or compromise at a highly critical vendor has outsized operational impact."
                ),
            },
            {
                "id": "c",
                "text": "The size of the vendor's marketing budget and its brand recognition in the industry",
                "correct": False,
                "rationale": (
                    "Incorrect. Brand recognition and marketing spend say nothing about the vendor's actual data "
                    "access, criticality, or security posture, and should not drive risk tiering."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The total dollar amount of the contract, independent of what data or systems the vendor will "
                    "touch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Contract value alone, divorced from data sensitivity and criticality, is not a "
                    "reliable inherent-risk indicator -- a low-cost vendor with broad sensitive-data access can "
                    "pose far greater risk than an expensive vendor with minimal access."
                ),
            },
        ],
        "explanation": (
            "Inherent vendor risk tiering should be driven primarily by the sensitivity/volume of data "
            "accessed and the vendor's criticality to business operations -- not by brand reputation or "
            "contract size in isolation."
        ),
    },
    {
        "id": "nd5e-014",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A company discovers that a marketing microsite built on an unsupported CMS has a critical "
            "unpatched RCE vulnerability with no available vendor patch. The business unit agrees the "
            "microsite generates negligible revenue. Leadership decides to decommission the microsite "
            "entirely rather than invest in compensating controls. Which risk management strategy does "
            "this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk avoidance",
                "correct": True,
                "rationale": (
                    "Correct. Eliminating the asset and the activity that creates the risk entirely -- "
                    "decommissioning the microsite rather than continuing to operate it in some reduced-risk form "
                    "-- is risk avoidance."
                ),
            },
            {
                "id": "b",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation reduces likelihood or impact while the activity continues (for "
                    "example, a WAF or network segmentation), whereas this scenario eliminates the asset "
                    "entirely."
                ),
            },
            {
                "id": "c",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference shifts the financial impact of a risk to a third party, such as "
                    "through insurance or a contract. Decommissioning the asset does not shift risk to anyone "
                    "else."
                ),
            },
            {
                "id": "d",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance means continuing to operate with the risk unaddressed. Shutting the "
                    "microsite down is the opposite of continuing to operate with the risk in place."
                ),
            },
        ],
        "explanation": (
            "Decommissioning an asset to eliminate the risk-bearing activity entirely -- rather than "
            "reducing, transferring, or tolerating the risk -- is the definition of risk avoidance."
        ),
    },
    {
        "id": "nd5e-015",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "After purchasing a $10 million cyber-insurance policy, a company's CFO tells the board that "
            "the organization has 'transferred' all ransomware risk and no further investment in "
            "ransomware controls is needed. A risk analyst points out that the policy has a $2 million "
            "sublimit specifically for ransomware extortion payments and a 30% coinsurance clause. What "
            "is the BEST characterization of the organization's actual risk posture?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The organization has only partially transferred the risk; it retains substantial residual "
                    "financial exposure above the sublimit and through coinsurance, so mitigation controls are "
                    "still warranted."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Sublimits and coinsurance clauses cap and share the insurer's payout, leaving the "
                    "organization holding significant residual (accepted) exposure that insurance alone does not "
                    "eliminate -- active mitigation remains necessary."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The organization has fully transferred the risk, since any cyber-insurance policy by "
                    "definition eliminates the need for additional security controls."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance never eliminates the underlying risk of disruption or reputational "
                    "harm, and this specific policy explicitly caps ransomware payouts well below the full loss "
                    "potential."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The organization has mitigated the risk, since purchasing insurance is a form of risk "
                    "mitigation rather than transference."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance is the textbook example of risk transference, not mitigation; "
                    "mitigation would involve technical or procedural controls that reduce the likelihood or "
                    "impact of ransomware itself."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The organization has avoided the risk, since the insurance policy removes the possibility of "
                    "a ransomware attack occurring."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance addresses financial consequences after an event occurs; it has no "
                    "effect on the likelihood of an attack and therefore cannot constitute avoidance."
                ),
            },
        ],
        "explanation": (
            "Cyber insurance transfers financial risk, but sublimits and coinsurance clauses mean "
            "transference is rarely complete -- the uncovered residual exposure is effectively retained "
            "(accepted), and active mitigation controls remain warranted alongside the policy."
        ),
    },
    {
        "id": "nd5e-016",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A business unit wants to continue running a legacy application that cannot be patched "
            "against a critical vulnerability. Rather than decommissioning it, the business unit "
            "implements network isolation, enhanced logging, and restricts access to a small number of "
            "authorized users, then documents the residual risk and obtains written sign-off from the "
            "designated risk owner authorizing continued operation. Which combination of concepts does "
            "this scenario BEST illustrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Risk mitigation through compensating controls, followed by formal risk acceptance of the "
                    "documented residual risk"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Isolation, logging, and access restriction are compensating controls that reduce "
                    "(mitigate) risk while the application continues running; the documented sign-off on what "
                    "remains is formal acceptance of the residual risk."
                ),
            },
            {
                "id": "b",
                "text": "Risk avoidance, since isolating the application removes it from the production network entirely",
                "correct": False,
                "rationale": (
                    "Incorrect. Isolation and access restriction are compensating controls that reduce risk while "
                    "keeping the application running, not elimination of the risk-bearing activity, which would "
                    "be avoidance."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Risk transference, since the risk owner's sign-off shifts liability for the vulnerability to "
                    "that individual"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A risk owner's sign-off documents internal accountability for accepting residual "
                    "risk; it does not shift the risk to an external third party, which is what transference "
                    "requires."
                ),
            },
            {
                "id": "d",
                "text": (
                    "An unmanaged risk exception, since no compensating controls or formal approval process were "
                    "actually applied"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This directly contradicts the scenario, which explicitly describes compensating "
                    "controls (isolation, logging, access restriction) and a documented, authorized sign-off."
                ),
            },
        ],
        "explanation": (
            "This scenario illustrates two sequential concepts: mitigation via compensating controls that "
            "reduce risk while the application keeps running, followed by formal, documented acceptance "
            "of whatever risk remains."
        ),
    },
    {
        "id": "nd5e-017",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A company's board-approved risk appetite statement caps acceptable individual risk exposure "
            "at a residual risk score of 12 (on a 25-point scale). A newly identified risk -- "
            "'unencrypted backup tapes stored at an offsite vendor facility' -- is scored at 16 after "
            "considering existing controls. What should happen NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The risk should be escalated for additional treatment (mitigation, transfer, or avoidance) "
                    "or, if the business insists on proceeding, for formal risk acceptance by an executive "
                    "authorized to approve exceptions above the board's stated appetite."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A residual score exceeding the stated appetite requires either treatment that "
                    "brings the risk within tolerance or a documented, appropriately senior exception -- it "
                    "cannot simply be left as-is."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The risk should be removed from the risk register, since risks exceeding the organization's "
                    "stated appetite do not need to be tracked."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risks that exceed appetite are precisely the ones that most need active tracking "
                    "and treatment, not removal from the register."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The risk register entry should be edited to lower the residual score to 12 so it aligns with "
                    "the stated risk appetite."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adjusting the recorded score to artificially match the appetite misrepresents the "
                    "actual risk and does nothing to reduce real exposure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No action is required, since a score of 16 still falls within the 25-point maximum scale and "
                    "is therefore acceptable."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scale's maximum value is irrelevant; the organization's own stated appetite "
                    "threshold of 12 is the operative benchmark, and a score of 16 exceeds it."
                ),
            },
        ],
        "explanation": (
            "When a residual risk score exceeds the board's stated risk appetite, the risk must be "
            "escalated for further treatment or for a documented, senior-level exception -- not deleted, "
            "silently re-scored, or ignored because it fits within a scale's numeric maximum."
        ),
    },
    {
        "id": "nd5e-018",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A CFO grants formal risk acceptance for a moderate-severity vulnerability in a "
            "soon-to-be-retired billing system, citing the system's planned decommissioning in 4 months. "
            "Six months later, the system is still in production and the vulnerability remains "
            "unaddressed, with no updated documentation. What does this scenario BEST illustrate the risk "
            "register is missing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A review/expiration date on the risk acceptance, so that the accepted risk is automatically "
                    "revisited when the underlying assumption (imminent decommissioning) no longer holds"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Time-bound risk acceptances need a built-in review or expiration trigger; without "
                    "one, a stale acceptance persists long after the justification that supported it has expired."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A quantitative ALE calculation, since only monetary figures can justify a risk acceptance "
                    "decision"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario's failure isn't a missing dollar figure -- it's that the "
                    "acceptance's rationale went stale with no mechanism to trigger re-review."
                ),
            },
            {
                "id": "c",
                "text": "A designated risk owner, since risk acceptance decisions cannot be made without one",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario already shows a designated approver (the CFO); the gap illustrated "
                    "is the absence of a review trigger, not missing ownership."
                ),
            },
            {
                "id": "d",
                "text": "A CVSS score for the vulnerability, since risk register entries are invalid without one",
                "correct": False,
                "rationale": (
                    "Incorrect. A CVSS score supports severity rating but does not address the gap actually "
                    "illustrated here -- an acceptance that outlived its stated justification with no re-review "
                    "mechanism."
                ),
            },
        ],
        "explanation": (
            "Time-bound risk acceptances must include a review or expiration date tied to the assumption "
            "that justified them; otherwise the acceptance silently persists after its rationale has "
            "expired, as happened here once the decommissioning was delayed."
        ),
    },
    {
        "id": "nd5e-019",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Risk register & appetite",
        "stem": (
            "Select the TWO statements that correctly distinguish risk appetite from risk tolerance."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Risk appetite is a broad, board-level statement of the overall amount and type of risk the "
                    "organization is willing to pursue or retain in pursuit of its objectives"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk appetite operates at a strategic level, setting the overall willingness to "
                    "take on risk across the organization."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Risk tolerance defines the acceptable variation around a specific risk or objective -- the "
                    "narrower operational boundaries within which the organization can function while still "
                    "remaining within its overall appetite"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk tolerance operates at a more granular, operational level, bounding acceptable "
                    "deviation for individual risks or objectives within the broader appetite."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Risk appetite is always expressed as a single dollar figure representing the maximum ALE the "
                    "organization will accept across all risks combined"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risk appetite is typically a qualitative or strategic statement of overall risk "
                    "willingness, not necessarily one aggregate dollar cap applied uniformly across every risk."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Risk tolerance and risk appetite are interchangeable terms with no meaningful distinction in "
                    "a risk management program"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. They operate at different levels -- appetite is the broad, strategic boundary, "
                    "while tolerance is the narrower, operational boundary for specific risks -- and conflating "
                    "them loses important governance nuance."
                ),
            },
        ],
        "explanation": (
            "Risk appetite is the board-level, strategic statement of overall risk willingness; risk "
            "tolerance is the narrower, operational boundary for acceptable variation on specific risks, "
            "nested within the broader appetite."
        ),
    },
    {
        "id": "nd5e-020",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "A document states, 'Passwords must be a minimum of 14 characters and rotated every 90 days,' "
            "while a separate document states, 'The organization is committed to protecting the "
            "confidentiality, integrity, and availability of information assets through appropriate "
            "authentication controls.' Which pairing correctly identifies these two governance documents?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The first is a standard (a specific, measurable technical requirement); the second is a "
                    "policy (a high-level statement of intent)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Standards specify measurable, mandatory technical requirements derived from policy; "
                    "policies state the organization's high-level intent and commitment without prescribing "
                    "specific numbers."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The first is a procedure (step-by-step instructions); the second is a guideline (an optional "
                    "recommendation)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The first document states a measurable requirement, not sequential how-to steps "
                    "-- a procedure would describe how to configure or change a password, not the numeric "
                    "requirement itself."
                ),
            },
            {
                "id": "c",
                "text": "The first is a policy; the second is a standard",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the pairing: the specific, measurable numeric requirement is the "
                    "standard, and the broad statement of intent is the policy."
                ),
            },
            {
                "id": "d",
                "text": "Both documents are standards, since both define required security controls",
                "correct": False,
                "rationale": (
                    "Incorrect. The second document contains no measurable requirement, only a general commitment "
                    "to authentication controls -- characteristic of a policy, not a standard."
                ),
            },
        ],
        "explanation": (
            "Policies state high-level intent; standards translate that intent into specific, measurable, "
            "mandatory requirements. The 14-character/90-day rule is a standard; the "
            "confidentiality/integrity/availability commitment is a policy."
        ),
    },
    {
        "id": "nd5e-021",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A security policy requires that all firewall rule changes be peer-reviewed and approved by "
            "someone other than the requester before deployment. A network engineer, working alone on an "
            "urgent outage, requests and approves his own emergency firewall change to restore service. "
            "What governance concept does this situation illustrate a violation of, and what should "
            "happen NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "This violates segregation of duties; the change should be logged as an emergency exception, "
                    "and a peer review should occur retroactively as soon as possible per the organization's "
                    "emergency change procedure."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Even emergency changes must be tracked through a defined emergency-change process, "
                    "with after-the-fact peer review to restore the segregation of duties that urgency "
                    "temporarily bypassed."
                ),
            },
            {
                "id": "b",
                "text": "This violates least privilege, and the engineer's firewall access should be permanently revoked.",
                "correct": False,
                "rationale": (
                    "Incorrect. The issue described is the engineer approving his own change, a "
                    "segregation-of-duties problem, not that he holds more access than his job requires."
                ),
            },
            {
                "id": "c",
                "text": (
                    "No governance concept was violated, since restoring service during an outage always "
                    "overrides standard change-approval requirements."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Even emergency changes must follow a defined emergency-change process with "
                    "after-the-fact review; urgency does not eliminate governance obligations entirely."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This violates non-repudiation, and the change should be reversed immediately regardless of "
                    "whether service is restored."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation concerns proving who performed an action, not the separation of "
                    "requester and approver roles, and reflexively reversing a restorative change is not the "
                    "appropriate next step."
                ),
            },
        ],
        "explanation": (
            "Self-approval of one's own change violates segregation of duties. Emergency changes should "
            "still be logged as exceptions and subjected to retroactive peer review under the emergency "
            "change procedure, rather than being treated as exempt from governance entirely."
        ),
    },
    {
        "id": "nd5e-022",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "During an audit, an auditor finds that a company's acceptable use policy (AUP) has not been "
            "reviewed or updated in 6 years, despite significant changes in the organization's cloud "
            "usage and remote-work practices during that time. Which governance control gap does this "
            "finding MOST directly point to?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A lack of a defined periodic policy review cycle to ensure governance documents remain "
                    "current with the organization's evolving risk environment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A stale policy that hasn't kept pace with major operational changes points directly "
                    "to a missing or unenforced periodic review cycle for governance documents."
                ),
            },
            {
                "id": "b",
                "text": "A lack of employee acknowledgment tracking for the AUP",
                "correct": False,
                "rationale": (
                    "Incorrect. The finding is about the policy's content going stale over six years, not about "
                    "whether employees signed acknowledgment forms for whatever version currently exists."
                ),
            },
            {
                "id": "c",
                "text": "A lack of technical enforcement of the AUP through DLP tooling",
                "correct": False,
                "rationale": (
                    "Incorrect. The audit finding concerns the governance review process itself, not whether "
                    "technical controls enforce the (outdated) policy's existing provisions."
                ),
            },
            {
                "id": "d",
                "text": "A lack of a data classification scheme referenced within the AUP",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the finding relates to data classification; the gap identified is "
                    "purely the absence of a review/update cadence over a six-year span."
                ),
            },
        ],
        "explanation": (
            "Governance documents must be reviewed on a defined periodic cycle so they stay current with "
            "operational and risk-environment changes; a six-year-stale AUP despite major "
            "cloud/remote-work shifts is a textbook symptom of a missing review cycle."
        ),
    },
    {
        "id": "nd5e-023",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A retailer plans to deploy a new in-store facial-recognition system that will systematically "
            "scan and profile shoppers to detect suspected repeat shoplifters, using biometric data as "
            "its primary identifier. Under GDPR, what must the retailer do BEFORE deploying this system?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Conduct a Data Protection Impact Assessment (DPIA), since large-scale, systematic processing "
                    "of biometric special-category data for profiling is a canonical high-risk scenario requiring "
                    "one."
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR requires a DPIA before processing likely to result in high risk to "
                    "individuals' rights, and systematic large-scale biometric profiling is one of the explicit "
                    "textbook examples."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Appoint a Data Protection Officer (DPO) for the first time, since DPIAs may only be authored "
                    "by a DPO and none is otherwise required by this processing."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A DPO may assist with a DPIA but authoring one is not conditioned on first "
                    "appointing a DPO; DPO appointment triggers (such as large-scale monitoring as a core "
                    "activity) are evaluated separately."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Obtain unambiguous, freely given consent from every individual whose face is scanned before "
                    "any processing occurs, since consent is the only lawful basis available for biometric data."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Consent is one possible lawful basis for special-category data, but it is not the "
                    "only one, and indiscriminate scanning of the public makes 'freely given' consent difficult "
                    "to establish; the more immediate obligation triggered here is completing a DPIA."
                ),
            },
            {
                "id": "d",
                "text": (
                    "File a prior notification with the relevant supervisory authority describing the processing, "
                    "since GDPR requires advance notice for all new data-processing activities."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR generally removed blanket prior-notification requirements in favor of "
                    "accountability and DPIA obligations; a universal advance-notice filing is not the correct "
                    "requirement here."
                ),
            },
        ],
        "explanation": (
            "Systematic, large-scale processing of biometric special-category data for profiling purposes "
            "is a canonical GDPR high-risk scenario that requires a Data Protection Impact Assessment "
            "before processing begins."
        ),
    },
    {
        "id": "nd5e-024",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "An EU resident submits a valid erasure request for personal data a bank holds about them. "
            "The bank identifies that a portion of the requested data consists of transaction records it "
            "is legally required to retain for 7 years under anti-money-laundering regulations. What "
            "should the bank do?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Erase the data not subject to the retention obligation, but retain the transaction records "
                    "required under anti-money-laundering law, and inform the requester of this partial exception "
                    "with the legal basis cited."
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR's erasure right includes a recognized exception for data subject to a legal "
                    "retention obligation; the bank must honor the request to the extent legally possible and "
                    "document the exception for the remainder."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Deny the erasure request in its entirety, since any legal retention obligation for a portion "
                    "of the data voids the erasure right for all of the requester's data."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The legal-obligation exception applies specifically to the data covered by that "
                    "obligation, not to the requester's entire data holdings."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Erase all requested data immediately, since GDPR's right to erasure always overrides "
                    "conflicting national retention laws."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR explicitly recognizes legal-obligation exceptions to the erasure right; it "
                    "does not categorically override other statutory retention requirements such as "
                    "anti-money-laundering rules."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ignore the request until the 7-year retention period expires, since no response is required "
                    "while any portion of the data is under legal hold."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The bank must still respond to the requester within GDPR's required timeframe, "
                    "addressing what can and cannot be erased now rather than deferring the response entirely."
                ),
            },
        ],
        "explanation": (
            "The right to erasure is not absolute -- GDPR recognizes an exception where retention is "
            "required for compliance with a legal obligation. The correct response is partial erasure "
            "with documented justification for what is retained."
        ),
    },
    {
        "id": "nd5e-025",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A research team pseudonymizes a patient dataset by replacing names with reversible tokens, "
            "retaining a separate secured key/lookup table that allows re-identification. The team argues "
            "the dataset is now anonymized and therefore falls entirely outside GDPR's scope. Is this "
            "argument correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "No. Because re-identification remains possible via the retained key, the dataset is "
                    "pseudonymized, not anonymized, and pseudonymized data is still considered personal data "
                    "subject to GDPR."
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR distinguishes pseudonymization (reversible, still personal data) from true "
                    "anonymization (irreversible, out of scope). Retaining a re-identification key keeps the "
                    "dataset within GDPR's scope."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Yes. Any dataset with names replaced by tokens is anonymized by definition and therefore "
                    "exempt from GDPR, regardless of whether a re-identification key exists."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This contradicts GDPR's definitions; retaining any means of re-identification is "
                    "exactly what distinguishes pseudonymization (still regulated) from anonymization (out of "
                    "scope)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Yes, but only if the key/lookup table is stored in a different EU member state than the "
                    "dataset itself."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Jurisdictional separation within the EU has no bearing on whether data is "
                    "anonymized; what matters is whether re-identification is possible at all, not where the key "
                    "is physically stored."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No, but only because the data concerns patients specifically; pseudonymized data about "
                    "non-health subjects would be considered anonymized."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The subject matter of the data does not determine pseudonymization versus "
                    "anonymization status; the presence of a re-identification mechanism does, regardless of the "
                    "data's subject matter."
                ),
            },
        ],
        "explanation": (
            "Pseudonymized data -- data that could be re-identified using a retained key -- remains "
            "personal data under GDPR. Only irreversible anonymization, where re-identification is no "
            "longer possible by any party, falls outside GDPR's scope."
        ),
    },
    {
        "id": "nd5e-026",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A regulator requires a company to have its security controls evaluated by an assessor with "
            "no financial or organizational ties to the company, whose findings will be submitted "
            "directly to the regulator as part of a compliance filing. Which type of audit does this "
            "describe?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A third-party (external, independent) audit",
                "correct": True,
                "rationale": (
                    "Correct. An assessor unaffiliated with either the company or a specific customer, reporting "
                    "findings to a regulator, is the defining characteristic of an independent third-party audit."
                ),
            },
            {
                "id": "b",
                "text": "A first-party (internal) audit",
                "correct": False,
                "rationale": (
                    "Incorrect. First-party audits are performed by the organization's own internal audit or "
                    "compliance function, not by an unaffiliated outside assessor."
                ),
            },
            {
                "id": "c",
                "text": "A second-party audit",
                "correct": False,
                "rationale": (
                    "Incorrect. Second-party audits are typically performed by, or on behalf of, a customer or "
                    "business partner assessing a supplier -- not an independent party reporting directly to a "
                    "regulator."
                ),
            },
            {
                "id": "d",
                "text": "A self-assessment questionnaire",
                "correct": False,
                "rationale": (
                    "Incorrect. A self-assessment is completed by the organization itself, the opposite of an "
                    "independent, unaffiliated assessor's evaluation described here."
                ),
            },
        ],
        "explanation": (
            "An audit performed by an assessor with no financial or organizational ties to the company, "
            "whose results feed directly into a regulatory filing, is a third-party (independent, "
            "external) audit -- distinct from first-party internal audits or second-party customer-driven "
            "assessments."
        ),
    },
    {
        "id": "nd5e-027",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "During an authorized penetration test, the testing team pivots from an in-scope web "
            "application server to a database server that hosts unrelated production financial data, "
            "which was explicitly listed as out of scope in the signed rules of engagement. The team is "
            "confident they could demonstrate a critical finding by continuing. What should the team do?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Stop before further interacting with the out-of-scope system, document the pivot path as a "
                    "finding, and immediately notify the client contact per the rules of engagement."
                ),
                "correct": True,
                "rationale": (
                    "Correct. The rules of engagement define the legal boundaries of authorization. Exceeding "
                    "scope, even to demonstrate impact, breaches that authorization and must be halted and "
                    "reported immediately, not pursued further."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Continue exploiting the out-of-scope database server, since demonstrating maximum impact is "
                    "the primary goal of any penetration test."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Authorization under the ROE does not extend to explicitly out-of-scope systems; "
                    "continuing exceeds legal authorization regardless of the demonstrative value of doing so."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Continue but only export non-sensitive metadata from the database server, since avoiding "
                    "sensitive data access makes the access permissible."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Any interaction with an explicitly out-of-scope system exceeds the signed "
                    "authorization, regardless of what data is or isn't ultimately touched."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Wait until the final report is delivered to mention the pivot path, since ROE violations "
                    "only need to be disclosed in formal deliverables."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Unauthorized access to an out-of-scope system should be reported immediately, not "
                    "held until the final report, given the legal and operational risk of leaving the client "
                    "unaware."
                ),
            },
        ],
        "explanation": (
            "Rules of engagement define the legal limits of an authorized penetration test. A pivot "
            "toward an explicitly out-of-scope system must be stopped and reported immediately, "
            "regardless of the finding's demonstrative value."
        ),
    },
    {
        "id": "nd5e-028",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "Select the TWO statements that correctly distinguish a SOC 2 Type II report from a SOC 2 "
            "Type I report."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Type II evaluates the operating effectiveness of controls over a review period (commonly "
                    "6-12 months), not just their design."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Type II reports test whether controls actually operated effectively over an "
                    "extended period, providing stronger assurance than a design-only assessment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Type I is a point-in-time assessment of whether controls are suitably designed, without "
                    "testing their effectiveness over time."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Type I evaluates control design as of a specific date but does not test whether "
                    "those controls operated effectively over any period."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Type I always covers a longer review period than Type II, since it requires more extensive "
                    "testing."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the relationship: Type I is a point-in-time design assessment, "
                    "while Type II covers an extended review period to test operating effectiveness."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both types are public, unrestricted reports that vendors may freely publish on their "
                    "marketing websites."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SOC 2 reports (both Type I and Type II) are restricted-use documents typically "
                    "shared under NDA with customers and auditors, unlike a SOC 3 report, which is designed for "
                    "general public distribution."
                ),
            },
        ],
        "explanation": (
            "Type I assesses control design at a single point in time; Type II tests operating "
            "effectiveness over an extended review period, providing stronger assurance. Neither is a "
            "freely publishable, unrestricted report."
        ),
    },
    {
        "id": "nd5e-029",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A software company's proprietary matching algorithm -- its core competitive differentiator "
            "-- is stored in a private repository accessible only to a small engineering team. Disclosure "
            "to a competitor would eliminate the company's primary market advantage, though it carries no "
            "direct regulatory or legal reporting obligation. Which classification level is MOST "
            "appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restricted (or an equivalent highest-sensitivity tier reserved for trade secrets and "
                    "material competitive assets)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification is driven by the business impact of disclosure, not solely by the "
                    "existence of a regulatory mandate; losing the company's core competitive advantage warrants "
                    "the highest protective tier."
                ),
            },
            {
                "id": "b",
                "text": "Public, since no law or regulation requires the algorithm to be protected",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification is driven by the business/competitive impact of disclosure, not "
                    "solely by a legal mandate; this algorithm is clearly not intended for open release."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Internal, since the data is only accessed by employees and doesn't involve customer personal "
                    "information"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'Internal' typically denotes routine, low-impact business data; a core trade "
                    "secret whose loss would eliminate the company's market advantage warrants stronger "
                    "protection than the general internal-use tier."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Confidential, but only until the algorithm is patented, after which it can automatically be "
                    "reclassified as Public"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario ties classification to patent status, and even after any "
                    "patent filing the company would likely still protect specific implementation details; an "
                    "automatic downgrade is not a sound classification practice here."
                ),
            },
        ],
        "explanation": (
            "Classification level reflects the business impact of disclosure, not just legal/regulatory "
            "obligation. A trade secret whose loss would eliminate a company's competitive advantage "
            "warrants the highest-sensitivity tier even without a compliance trigger."
        ),
    },
    {
        "id": "nd5e-030",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "A dataset of customer transaction records was originally classified 'Confidential' because "
            "it contained names, account numbers, and purchase histories. A data engineering team "
            "subsequently removes all directly and indirectly identifying fields, replacing them with "
            "irreversible aggregate statistics, and destroys the original identifiable dataset. What "
            "should happen to the classification of the resulting aggregate dataset?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It may be reclassified to a lower sensitivity level (such as Internal or Public, per "
                    "policy), because true anonymization that removes re-identification risk changes the data's "
                    "actual risk profile."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification should reflect current sensitivity. Irreversible anonymization that "
                    "removes re-identification risk materially lowers the data's risk profile and justifies a "
                    "downgrade under policy."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It must remain classified 'Confidential' indefinitely, since data classification, once "
                    "assigned, can never be downgraded under any circumstance."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification frameworks explicitly allow labels to change, including "
                    "downgrades, when the data's actual sensitivity changes, as it did here through irreversible "
                    "anonymization."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It must be reclassified as 'Restricted,' since removing identifying fields always increases "
                    "the operational sensitivity of a dataset."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Removing identifiers and irreversibly aggregating data reduces, rather than "
                    "increases, its sensitivity and re-identification risk."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Classification does not apply to aggregate statistical data, so no classification label is "
                    "required going forward."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Data classification schemes require every dataset to carry a label -- even a low "
                    "one such as Public or Internal -- rather than leaving datasets unlabeled entirely."
                ),
            },
        ],
        "explanation": (
            "Data classification should be reassessed when a dataset's actual risk profile changes. "
            "Irreversible anonymization that removes re-identification risk justifies downgrading the "
            "classification, but the dataset must still carry a defined label."
        ),
    },
    {
        "id": "nd5e-031",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A sales executive verbally discusses next quarter's unreleased pricing strategy -- "
            "classified 'Confidential' per policy -- during a public webinar Q&A session, believing that "
            "because the information was spoken rather than written or emailed, no data-classification "
            "handling rules applied. Is this reasoning correct?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "No. Classification handling requirements apply to the sensitivity of the information itself, "
                    "regardless of the medium -- verbal, written, or electronic -- through which it is disclosed."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Data classification governs the information's sensitivity and requires appropriate "
                    "handling in whatever form it takes, including spoken disclosure, not just written or "
                    "electronic formats."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Yes, because data classification policies and their associated handling controls "
                    "(encryption, DLP, access restriction) are technical controls that can only govern electronic "
                    "data formats."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Technical controls like DLP are just one enforcement mechanism for classification "
                    "policy; the underlying handling requirements still apply to the information regardless of "
                    "how it is disclosed."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Yes, because verbal statements are inherently non-repudiable and therefore fall outside "
                    "classification scope."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Non-repudiation is an unrelated concept concerning proof of authorship or action, "
                    "and has no bearing on whether classification handling rules apply to spoken information."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No, but only because the disclosure occurred during a company-sponsored webinar; the same "
                    "statement made in an unofficial setting would not violate policy."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The violation is the unauthorized disclosure of Confidential information to an "
                    "external/public audience, which is neither excused nor worsened by whether the venue is "
                    "company-sponsored."
                ),
            },
        ],
        "explanation": (
            "Classification handling obligations attach to the sensitivity of information itself, not the "
            "medium used to disclose it -- verbally revealing Confidential information to a public "
            "audience is a policy violation just as much as emailing or writing it would be."
        ),
    },
    {
        "id": "nd5e-032",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "An online education platform (Company A) decides which student engagement metrics to collect "
            "and how they will be used to personalize course recommendations. Company A contracts a "
            "third-party analytics firm (Company B) to run the machine-learning models strictly according "
            "to Company A's written specifications, with no independent decision-making authority over "
            "the data's purpose. Which roles do Company A and Company B respectively hold?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Company A is the data controller; Company B is the data processor.",
                "correct": True,
                "rationale": (
                    "Correct. Company A determines the purposes and means of processing (the defining "
                    "characteristic of a controller), while Company B acts strictly on Company A's instructions "
                    "with no independent decision-making authority (the defining characteristic of a processor)."
                ),
            },
            {
                "id": "b",
                "text": "Company A is the data processor; Company B is the data controller.",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the roles: the party deciding the purposes and means of processing "
                    "is the controller (Company A), not the party merely executing instructions."
                ),
            },
            {
                "id": "c",
                "text": "Company A is the data custodian; Company B is the data controller.",
                "correct": False,
                "rationale": (
                    "Incorrect. Company A determines purpose and means, the defining characteristic of a "
                    "controller, not merely the technical custody role of a custodian."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both Company A and Company B are joint controllers, since both are actively involved in "
                    "processing the data."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Company B has no independent decision-making authority over the data's purposes "
                    "or means and acts solely on Company A's instructions, which is the defining characteristic "
                    "of a processor, not a joint controller."
                ),
            },
        ],
        "explanation": (
            "The party that determines the purposes and means of processing is the controller; a party "
            "that processes data strictly on the controller's documented instructions, with no "
            "independent decision-making authority, is the processor."
        ),
    },
    {
        "id": "nd5e-033",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A cloud operations team is responsible for configuring backup schedules, encryption keys, "
            "and access-control lists for a dataset whose business purpose and retention requirements are "
            "defined by the compliance department. Which data role does the cloud operations team hold "
            "with respect to this dataset?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data custodian",
                "correct": True,
                "rationale": (
                    "Correct. The custodian performs the day-to-day technical safeguarding of data -- backups, "
                    "encryption, access controls -- as directed by the party that defines its purpose and "
                    "requirements."
                ),
            },
            {
                "id": "b",
                "text": "Data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. The compliance department, not the operations team, determines the dataset's "
                    "purpose and retention requirements, the defining role of the controller."
                ),
            },
            {
                "id": "c",
                "text": "Data processor",
                "correct": False,
                "rationale": (
                    "Incorrect. Processor typically refers to an external third-party organization processing "
                    "data on a controller's behalf, whereas this is an internal technical team performing "
                    "custodial safeguarding duties."
                ),
            },
            {
                "id": "d",
                "text": "Data owner",
                "correct": False,
                "rationale": (
                    "Incorrect. The data owner is typically the accountable business role that defines "
                    "requirements, closer to the compliance department here; the operations team performs the "
                    "technical implementation characteristic of a custodian, not ownership."
                ),
            },
        ],
        "explanation": (
            "A custodian performs technical safeguarding tasks (backups, encryption, access-control "
            "implementation) under the direction of the party -- often the data owner or controller -- "
            "that defines the data's purpose and requirements."
        ),
    },
    {
        "id": "nd5e-034",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "Select the TWO statements that correctly describe a data CUSTODIAN's responsibilities, as "
            "distinguished from a data controller's responsibilities, within a data governance program."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The custodian performs the day-to-day technical safeguarding of data -- such as backups, "
                    "encryption, and access-control implementation -- as directed by the controller or data "
                    "owner."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Custodians carry out the hands-on technical protection of data according to "
                    "requirements set by the controller or owner, not their own independent purposes."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The custodian does not decide the purposes or lawful basis for processing data; that "
                    "decision belongs to the controller."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Deciding why and how data is processed is the defining authority of the controller; "
                    "the custodian's role is limited to technical implementation of safeguards."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The custodian determines the business purpose and lawful basis for collecting the data in "
                    "the first place."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Determining the business purpose and lawful basis for processing is the defining "
                    "responsibility of the controller, not the custodian."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The custodian is, by definition, an external third-party organization engaged strictly to "
                    "process data solely on the controller's documented instructions."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes a processor. Custodians are commonly an internal technical role "
                    "(such as IT operations or a DBA team) performing safeguarding duties, and conflating the two "
                    "roles is a common exam trap."
                ),
            },
        ],
        "explanation": (
            "A custodian handles the technical, day-to-day safeguarding of data under direction from the "
            "controller or owner and has no authority over why or how data is processed -- and should not "
            "be conflated with a processor, which is specifically an external party bound to a "
            "controller's instructions."
        ),
    },
    {
        "id": "nd5e-035",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company is decommissioning a batch of self-encrypting drives (SEDs) that stored moderately "
            "sensitive internal project files, and the drives will be redeployed to a different internal "
            "department rather than leaving organizational control. Which sanitization method is MOST "
            "efficient while still meeting the requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Cryptographic erase -- destroying or replacing the drive's internal encryption key, "
                    "rendering all previously stored data unrecoverable"
                ),
                "correct": True,
                "rationale": (
                    "Correct. For SEDs being redeployed internally rather than leaving organizational custody, "
                    "cryptographic erase is fast, verifiable, and appropriately leverages the drive's built-in "
                    "encryption capability."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Physical destruction (shredding), since it is the only method that guarantees data cannot be "
                    "recovered from a self-encrypting drive"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical destruction is unnecessarily costly and destructive for drives being "
                    "redeployed internally; it also prevents the planned reuse, which contradicts the scenario's "
                    "requirement."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A single-pass logical overwrite of the entire drive, since overwriting is required for any "
                    "drive before reissue"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A full logical overwrite on an SED is slower and less efficient than "
                    "cryptographic erase, and it doesn't take advantage of the drive's built-in encryption the "
                    "way crypto-erase does."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No sanitization is required, since the drives are only moving to another department within "
                    "the same company"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Moderately sensitive project data still requires sanitization before reassignment "
                    "to a different department or user population, even within the same organization."
                ),
            },
        ],
        "explanation": (
            "Cryptographic erase is the efficient, appropriate sanitization method for self-encrypting "
            "drives that remain within organizational control and will be redeployed, avoiding the cost "
            "and reuse-prevention of physical destruction while still rendering prior data unrecoverable."
        ),
    },
    {
        "id": "nd5e-036",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company returns a leased multifunction printer/copier to the leasing company at the end of "
            "the contract term. The device has an internal hard drive that cached digital copies of "
            "scanned invoices and contracts over several years. What is the MOST significant risk if the "
            "device is returned without any sanitization step?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The printer's internal hard drive may still contain recoverable scanned documents, and "
                    "returning the device without wiping it constitutes a data-loss/media-sanitization gap, since "
                    "decommissioning obligations extend to embedded storage on leased hardware."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Multifunction devices commonly cache or store scanned images on internal drives; "
                    "this overlooked embedded storage is a frequently exploited gap in decommissioning practice."
                ),
            },
            {
                "id": "b",
                "text": (
                    "There is no meaningful risk, since printers do not retain data after a print or scan job "
                    "completes."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is factually wrong; many multifunction devices cache or store scanned images "
                    "on internal drives, sometimes indefinitely, until explicitly cleared."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The only risk is a contractual penalty for returning the device in non-original condition, "
                    "unrelated to data exposure."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This understates the actual risk, which is exposure of confidential scanned "
                    "business documents to the leasing company or a subsequent lessee of the device."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The risk is eliminated automatically because the device will be factory-reset by the leasing "
                    "company before it is redeployed to another customer."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The organization cannot rely on a downstream party's future actions to fulfill "
                    "its own data-sanitization obligation before relinquishing control of the device."
                ),
            },
        ],
        "explanation": (
            "Embedded storage on devices like multifunction printers/copiers is a commonly overlooked "
            "decommissioning risk. The organization relinquishing control of leased hardware is "
            "responsible for sanitizing any internal storage before return, not assuming a downstream "
            "party will do so."
        ),
    },
    {
        "id": "nd5e-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company contracts an e-waste recycling vendor to physically destroy decommissioned hard "
            "drives containing regulated financial records. Beyond obtaining a certificate of destruction "
            "after the fact, what should the company do BEFOREHAND to strengthen assurance that the "
            "vendor's destruction practices meet regulatory requirements?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Verify the vendor holds a recognized third-party media-destruction certification (such as "
                    "NAID AAA) and review its documented chain-of-custody process for handling drives between "
                    "pickup and destruction."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Proactive vendor due diligence -- confirming recognized certification and a sound "
                    "chain-of-custody process -- provides much stronger assurance than relying solely on a "
                    "reactive after-the-fact certificate."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Nothing further is needed, since a certificate of destruction issued after the fact is "
                    "legally sufficient documentation regardless of the vendor's actual practices."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A certificate alone does not verify that the vendor's underlying process was "
                    "sound; upfront due diligence strengthens assurance that the certificate will actually "
                    "reflect proper handling."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require the vendor to email photographs of the destroyed drives instead of performing any "
                    "vendor due diligence."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Photographs alone do not establish chain of custody or verify the vendor's "
                    "overall process or certification status, and do not substitute for proper due diligence."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Require the vendor to sign a standard non-disclosure agreement (NDA), since an NDA alone is "
                    "sufficient assurance of proper media destruction practices."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA addresses confidentiality of information the vendor might learn, not "
                    "whether the vendor's physical destruction process and chain of custody actually meet "
                    "regulatory standards."
                ),
            },
        ],
        "explanation": (
            "Strong assurance for outsourced media destruction comes from upfront vendor due diligence -- "
            "verifying recognized certifications and a documented chain-of-custody process -- not solely "
            "from a certificate received after destruction has already occurred."
        ),
    },
    {
        "id": "nd5e-038",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "An organization's standard annual security awareness training satisfies compliance "
            "requirements for all employees, but the finance department continues to fall victim to "
            "targeted business-email-compromise attempts impersonating executives requesting urgent wire "
            "transfers, despite everyone having completed the training. What is the BEST way to address "
            "this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Supplement the general training with role-based training specific to finance staff, covering "
                    "wire-transfer verification procedures and BEC red flags relevant to their specific job "
                    "function."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Generic training doesn't address role-specific attack patterns; targeted role-based "
                    "training that covers finance-specific verification procedures directly closes this gap."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the frequency of the same general annual training to twice per year, since more "
                    "repetition of identical content will address the gap."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Repeating the same generic, non-role-specific content more often does not address "
                    "the finance department's specific exposure to BEC and wire-fraud tactics."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Discontinue the annual training entirely, since it has proven ineffective at stopping the "
                    "finance department's incidents."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The general training still serves a baseline compliance and awareness purpose; "
                    "the correct fix is to supplement it with targeted content, not eliminate it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Restrict finance staff's email access to internal senders only, since technical controls are "
                    "always more effective than training."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking external email would break the finance department's actual business "
                    "function (communicating with external banks and vendors) and is not a proportionate, "
                    "targeted response to the stated problem."
                ),
            },
        ],
        "explanation": (
            "Role-based training that addresses the specific attack patterns a given department faces "
            "closes gaps that generic, one-size-fits-all annual training leaves open."
        ),
    },
    {
        "id": "nd5e-039",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "A security team wants to reduce reliance on annual computer-based training modules and "
            "instead build sustained day-to-day security engagement across departments. It recruits "
            "informal volunteer 'security champions' within each business unit who receive extra training "
            "and serve as a first point of contact for security questions and early reporting of "
            "suspicious activity in their teams. What BEST describes the primary benefit of this "
            "approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It embeds security awareness into daily team culture through peer-level advocates, extending "
                    "the reach and immediacy of the security program beyond what centralized annual training "
                    "alone can achieve."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Security champion programs are a recognized best practice for sustaining engagement "
                    "and enabling faster, more local reporting than a once-a-year training module alone can "
                    "provide."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It eliminates the organization's need for formal, centralized security awareness training "
                    "going forward."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Champions supplement, rather than replace, formal baseline training and any "
                    "associated compliance obligations."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It transfers legal liability for security incidents from the organization to the individual "
                    "security champions."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Informal champion roles do not shift the organization's legal liability for "
                    "incidents onto volunteer employees."
                ),
            },
            {
                "id": "d",
                "text": "It guarantees a measurable phishing click-rate reduction within the first reporting quarter.",
                "correct": False,
                "rationale": (
                    "Incorrect. While champion programs typically improve engagement over time, simply "
                    "establishing the role does not guarantee any specific, immediate metric outcome."
                ),
            },
        ],
        "explanation": (
            "Security champion programs extend a security team's day-to-day reach and cultural "
            "embeddedness beyond what centralized, periodic training alone achieves, without replacing "
            "formal training or shifting legal liability."
        ),
    },
    {
        "id": "nd5e-040",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "A security team notices that its phishing-simulation click rate has stayed flat at 10% for "
            "two years, but the median time between an employee receiving a real phishing email and "
            "reporting it to the security team has dropped from 3 days to 20 minutes. How should the "
            "security team interpret this combined trend?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The awareness program is showing meaningful behavioral improvement in reporting speed and "
                    "vigilance, even though the click rate itself hasn't changed; both metrics should be "
                    "considered together rather than relying on click rate alone."
                ),
                "correct": True,
                "rationale": (
                    "Correct. A mature evaluation looks beyond click rate to behaviors like reporting speed, "
                    "which reflects genuine improvement in vigilance and materially reduces attacker dwell time "
                    "even without a lower click rate."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The awareness program has failed, since click rate is the single authoritative metric of "
                    "program success and it has not improved."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Relying on a single metric (click rate) ignores the meaningful behavioral "
                    "improvement reflected in dramatically faster reporting, which reduces real-world incident "
                    "impact."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The two metrics contradict each other, so neither can be trusted and the program should be "
                    "scrapped and rebuilt from scratch."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The metrics do not contradict each other; a flat click rate alongside much faster "
                    "reporting is a coherent, plausible outcome reflecting improved vigilance without full "
                    "elimination of susceptibility."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The drop in reporting time is a statistical artifact of simulations and should be "
                    "disregarded, since only simulated phishing results are meaningful for evaluating training."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly measures reporting speed against real phishing emails, "
                    "which is actually a more meaningful real-world behavioral indicator than simulation-only "
                    "click-rate metrics."
                ),
            },
        ],
        "explanation": (
            "Mature security awareness evaluation considers multiple behavioral metrics together. A flat "
            "click rate alongside a dramatically faster real-world reporting time reflects genuine "
            "improvement in vigilance, not program failure or contradictory, untrustworthy data."
        ),
    },
]
