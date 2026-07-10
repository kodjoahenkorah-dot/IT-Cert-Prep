"""CompTIA Security+ SY0-701 practice questions — Domain 5 (Security Program
Management and Oversight), file G.

46 scenario-driven questions (42 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 5 in
``_topic_labels.json``.
"""

QUESTIONS = [
    {
        "id": "nd5g-001",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A risk analyst is quantifying exposure for a supply-chain-injection scenario against a "
            "pharmaceutical distributor's order-management platform, valued at $720,000 (asset value, AV). "
            "Vendor incident reports for comparable platforms indicate that a successful compromise typically "
            "destroys or renders unusable 25% of the platform's value (exposure factor, EF). What is the single "
            "loss expectancy (SLE) for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$180,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $720,000 x 0.25 = $180,000, the expected loss from one occurrence "
                    "of the event."
                ),
            },
            {
                "id": "b",
                "text": "$540,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the complement of the exposure factor (75%) instead of the stated "
                    "25% EF ($720,000 x 0.75), which is not what the scenario describes."
                ),
            },
            {
                "id": "c",
                "text": "$720,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the asset value with the exposure factor ignored entirely. SLE must "
                    "scale AV by the proportion of value actually expected to be lost."
                ),
            },
            {
                "id": "d",
                "text": "$2,880,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from dividing AV by EF ($720,000 / 0.25) rather than multiplying. "
                    "Dividing produces a figure larger than the asset itself, which cannot be a valid SLE."
                ),
            },
        ],
        "explanation": (
            "SLE = Asset Value (AV) x Exposure Factor (EF). Here, $720,000 x 0.25 = $180,000. EF must be "
            "multiplied, not subtracted from 1 and applied, divided into AV, or ignored."
        ),
    },
    {
        "id": "nd5g-002",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A single loss expectancy (SLE) of $96,000 has been calculated for a rogue-firmware-update scenario "
            "against a fleet of smart parking meters. Municipal maintenance logs indicate this type of incident "
            "occurs, on average, once every 8 years. What is the annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$12,000",
                "correct": True,
                "rationale": (
                    "Correct. ARO = 1 event / 8 years = 0.125. ALE = SLE x ARO = $96,000 x 0.125 = $12,000."
                ),
            },
            {
                "id": "b",
                "text": "$96,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats ALE as identical to SLE, ignoring the annualized rate of occurrence "
                    "entirely. ALE must account for how often the event is expected per year."
                ),
            },
            {
                "id": "c",
                "text": "$1,200",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading 'once every 8 years' as an ARO of 0.0125 (as if it "
                    "were once every 80 years) instead of the correct 0.125 (1/8)."
                ),
            },
            {
                "id": "d",
                "text": "$768,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing SLE by ARO ($96,000 / 0.125) instead of multiplying, "
                    "which inflates the figure well beyond the single-loss amount."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO. 'Once every 8 years' converts to ARO = 1/8 = 0.125. $96,000 x 0.125 = $12,000."
        ),
    },
    {
        "id": "nd5g-003",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "Before mitigation, the ALE for a regional airline's baggage-routing control system is $130,000/year. "
            "A proposed safeguard (annual cost of safeguard, ACS, of $60,000) would reduce the ALE to $55,000/year. "
            "Using cost-benefit analysis of the control, what should the airline conclude?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The safeguard produces a net benefit of $15,000/year ($75,000 ALE reduction minus the "
                    "$60,000 ACS), so it is cost-justified."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Value of the control = (ALE_before - ALE_after) - ACS = ($130,000 - $55,000) - "
                    "$60,000 = $75,000 - $60,000 = $15,000. A positive figure means the safeguard is worth its cost."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The safeguard produces a net benefit of $75,000/year, because the ALE reduction alone "
                    "determines value regardless of the safeguard's cost."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the ALE reduction ($130,000 - $55,000) before subtracting the $60,000 "
                    "ACS. The safeguard's own cost must be netted out to determine whether it is truly worthwhile."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The safeguard costs $5,000 more than the residual $55,000 ALE it leaves behind, producing "
                    "a net loss, so it should not be implemented."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This compares the safeguard's cost to the post-control ALE rather than to the "
                    "reduction in ALE it produces, which is the wrong comparison for a cost-benefit calculation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The airline saves $70,000/year ($130,000 original ALE minus the $60,000 safeguard cost), "
                    "so the safeguard is justified."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This subtracts ACS from the original ALE but omits the residual $55,000 ALE that "
                    "still remains after the control is applied, understating the true comparison."
                ),
            },
        ],
        "explanation": (
            "Cost-benefit analysis of a safeguard: Value = (ALE before control - ALE after control) - ACS. "
            "($130,000 - $55,000) - $60,000 = $15,000 net benefit, so the control is worth implementing."
        ),
    },
    {
        "id": "nd5g-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A national logistics hub's automated sorting-robot fleet is valued at $1,800,000 (AV). Security "
            "engineers estimate that a successful attack against the fleet's control software would destroy 8% "
            "of its value (EF). Incident records show this type of attack has occurred 3 times over the past 12 "
            "years. What is the ALE?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$36,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $1,800,000 x 0.08 = $144,000. ARO = 3 events / 12 years = 0.25. "
                    "ALE = SLE x ARO = $144,000 x 0.25 = $36,000."
                ),
            },
            {
                "id": "b",
                "text": "$144,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the SLE, not the ALE — it stops after AV x EF and never applies the ARO "
                    "of 0.25 to annualize the figure."
                ),
            },
            {
                "id": "c",
                "text": "$450,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from AV x ARO ($1,800,000 x 0.25), skipping the exposure factor "
                    "entirely rather than first computing SLE from AV and EF."
                ),
            },
            {
                "id": "d",
                "text": "$12,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading '3 times in 12 years' as a rate of 1 occurrence per "
                    "12 years (ARO = 1/12 = 0.0833) instead of the correct 3/12 = 0.25."
                ),
            },
        ],
        "explanation": (
            "SLE = AV x EF = $1,800,000 x 0.08 = $144,000. ARO = 3/12 = 0.25 (three times in 12 years). ALE = "
            "SLE x ARO = $144,000 x 0.25 = $36,000."
        ),
    },
    {
        "id": "nd5g-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A securities clearinghouse's trade-settlement platform BIA specifies that after a declared outage, "
            "the platform must be back online within 90 minutes, and no more than 2 minutes of in-flight trade "
            "data may be lost. Which metric describes the 2-minute figure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Recovery point objective (RPO)",
                "correct": True,
                "rationale": (
                    "Correct. RPO defines the maximum acceptable amount of data loss, measured backward in time "
                    "from the point of failure — exactly the 2-minute figure described."
                ),
            },
            {
                "id": "b",
                "text": "Recovery time objective (RTO)",
                "correct": False,
                "rationale": (
                    "Incorrect. RTO is the 90-minute figure — the maximum acceptable time to restore the "
                    "platform after an outage — not the amount of data loss tolerated."
                ),
            },
            {
                "id": "c",
                "text": "Mean time to repair (MTTR)",
                "correct": False,
                "rationale": (
                    "Incorrect. MTTR is the average time it actually takes to repair a failed component, an "
                    "operational metric derived from history, not a data-loss tolerance target set by the plan."
                ),
            },
            {
                "id": "d",
                "text": "Mean time between failures (MTBF)",
                "correct": False,
                "rationale": (
                    "Incorrect. MTBF measures the average time between failures of a component (a reliability "
                    "metric), and has nothing to do with how much data may be lost during a single outage."
                ),
            },
        ],
        "explanation": (
            "RTO = how long the platform can be down. RPO = how much data can be lost, measured backward in "
            "time from the failure. MTTR/MTBF are historical reliability metrics, not recovery targets."
        ),
    },
    {
        "id": "nd5g-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A fleet of 24 identical ATMs logged a combined total of 210,240 operating hours over one year, "
            "experiencing 8 failures across the fleet. What metric is being calculated when an analyst divides "
            "210,240 hours by 8 failures, and what is the resulting value?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MTBF of 26,280 hours",
                "correct": True,
                "rationale": (
                    "Correct. MTBF = total operating time / number of failures = 210,240 / 8 = 26,280 hours, the "
                    "average time the fleet operates between failures."
                ),
            },
            {
                "id": "b",
                "text": "MTTR of 26,280 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. The arithmetic (total time / failures) is correct for MTBF, but MTTR measures "
                    "average time to repair a failure, not average time between failures — the wrong metric name "
                    "for this calculation."
                ),
            },
            {
                "id": "c",
                "text": "MTBF of 210,240 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This uses the total operating time without dividing by the 8 recorded failures, "
                    "which overstates the true average time between failures."
                ),
            },
            {
                "id": "d",
                "text": "MTTR of 8 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This mistakes the failure count itself for a repair-time duration; MTTR requires "
                    "actual repair-time data, none of which was given in the scenario."
                ),
            },
        ],
        "explanation": (
            "MTBF = total operational time / number of failures = 210,240 / 8 = 26,280 hours. MTTR is a distinct "
            "metric measuring average repair duration, not derivable from this data."
        ),
    },
    {
        "id": "nd5g-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA sets an RPO of 5 minutes for a legal e-signature platform's document-execution ledger. Which "
            "backup or replication strategy BEST satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Continuous data protection (CDP) or synchronous, near-real-time transaction replication",
                "correct": True,
                "rationale": (
                    "Correct. Only continuous or synchronous near-real-time replication can bound data loss to "
                    "roughly 5 minutes or less in the event of a failure."
                ),
            },
            {
                "id": "b",
                "text": "A storage snapshot taken once per hour",
                "correct": False,
                "rationale": (
                    "Incorrect. An hourly snapshot could still lose up to an hour of executed-document data, "
                    "far exceeding the 5-minute RPO."
                ),
            },
            {
                "id": "c",
                "text": "A full backup taken every night at midnight",
                "correct": False,
                "rationale": (
                    "Incorrect. A nightly full backup could expose the platform to up to 24 hours of data loss, "
                    "nowhere close to a 5-minute RPO."
                ),
            },
            {
                "id": "d",
                "text": "A weekly full backup supplemented by daily differential backups",
                "correct": False,
                "rationale": (
                    "Incorrect. Even with daily differentials, up to a full day of executed documents could be "
                    "lost between backup windows — far beyond the 5-minute tolerance the RPO establishes."
                ),
            },
        ],
        "explanation": (
            "RPO drives backup/replication frequency. A tight 5-minute RPO requires continuous or synchronous "
            "replication; periodic backups or snapshots, however frequent within reason, cannot meet it."
        ),
    },
    {
        "id": "nd5g-008",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA for an online tax-filing portal states that the maximum tolerable downtime (MTD) is 5 hours. "
            "The technical recovery team confirms that systems can be fully restored (RTO) within 3.5 hours. "
            "What does the remaining 1.5 hours represent, and what is it called?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Work recovery time (WRT) — the additional time needed after systems are technically "
                    "restored to validate data integrity, reconcile filings, and resume full business operations"
                ),
                "correct": True,
                "rationale": (
                    "Correct. MTD = RTO + WRT. WRT covers the post-restoration work (data validation, "
                    "reconciliation, catch-up processing) required before the business is truly back to normal, "
                    "which is exactly the gap between the 3.5-hour RTO and the 5-hour MTD."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Additional recovery point objective (RPO) — extra tolerance for data loss beyond the "
                    "original RPO figure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RPO measures acceptable data loss going backward in time from a failure; it has "
                    "no relationship to the time remaining after systems are restored."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Evidence of a planning error, since the MTD should never be allowed to exceed the RTO"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MTD is expected to exceed RTO by definition (MTD = RTO + WRT); an MTD greater "
                    "than the RTO is normal and correct, not an error."
                ),
            },
            {
                "id": "d",
                "text": "Mean time to repair (MTTR) — the historical average time needed to repair failures",
                "correct": False,
                "rationale": (
                    "Incorrect. MTTR is a historical reliability average calculated from past repair data, not "
                    "a planning figure derived by subtracting RTO from MTD."
                ),
            },
        ],
        "explanation": (
            "Maximum tolerable downtime (MTD) is composed of RTO (time to technically restore systems) plus WRT "
            "(work recovery time — the follow-on effort to validate and fully resume business operations)."
        ),
    },
    {
        "id": "nd5g-009",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Before demonstrating its proprietary fraud-detection algorithm to a prospective client, a fintech "
            "startup requires the visiting company to sign a document that prohibits the visiting company from "
            "disclosing anything it learns about the algorithm during the demo. The startup does not disclose any "
            "confidential information belonging to the visiting company, so no reciprocal obligation is needed. "
            "Which document BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A unilateral (one-way) non-disclosure agreement (NDA)",
                "correct": True,
                "rationale": (
                    "Correct. A unilateral NDA binds only the receiving party (the visiting company) to protect "
                    "confidential information disclosed by the other party — exactly this one-directional demo "
                    "scenario."
                ),
            },
            {
                "id": "b",
                "text": "A mutual (bilateral) non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A mutual NDA obligates both parties to protect each other's confidential "
                    "information, but only the startup is disclosing anything here — the visiting company has no "
                    "information to protect."
                ),
            },
            {
                "id": "c",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents non-binding mutual intent to cooperate; it does not create the "
                    "enforceable confidentiality obligation the startup needs before revealing its algorithm."
                ),
            },
            {
                "id": "d",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes a joint business partnership with shared profit, loss, and "
                    "authority; a one-time product demo does not create a partnership requiring this."
                ),
            },
        ],
        "explanation": (
            "When only one party is disclosing confidential information, a unilateral NDA is the correct "
            "instrument; a mutual NDA is unnecessary since no reciprocal disclosure is occurring."
        ),
    },
    {
        "id": "nd5g-010",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "An engineering firm already has a master service agreement (MSA) in place with an IT contractor "
            "covering payment terms, liability, and dispute resolution for all future work. The firm now needs a "
            "document that defines the specific deliverables, timeline, and price for an upcoming network "
            "redesign project. Which document should be created?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A statement of work (SOW)",
                "correct": True,
                "rationale": (
                    "Correct. An SOW defines the specific deliverables, milestones, timeline, and pricing for an "
                    "individual project, operating under the standing legal framework already established by the "
                    "MSA."
                ),
            },
            {
                "id": "b",
                "text": "A new master service agreement (MSA) specific to this project",
                "correct": False,
                "rationale": (
                    "Incorrect. The MSA already establishes the overarching legal and commercial terms; creating "
                    "a second MSA is redundant and not how the framework is designed to be used for individual "
                    "projects."
                ),
            },
            {
                "id": "c",
                "text": "A service level agreement (SLA) covering only project deliverables and price",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines measurable performance metrics such as uptime or response time; it "
                    "does not itself specify deliverables, timeline, and price for a discrete project."
                ),
            },
            {
                "id": "d",
                "text": "An amendment to the existing non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA governs confidentiality of shared information; it has no mechanism for "
                    "specifying project deliverables, timelines, or pricing."
                ),
            },
        ],
        "explanation": (
            "Under an MSA umbrella, individual engagements are scoped with a statement of work (SOW), which "
            "defines deliverables, timeline, and price without renegotiating the overarching legal terms."
        ),
    },
    {
        "id": "nd5g-011",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A parcel-delivery company negotiating a contract with a cloud-based logistics-routing platform wants "
            "enforceable, measurable uptime and API-response-time commitments, along with service credits owed "
            "if those targets are missed. Which document BEST provides this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A service level agreement (SLA)",
                "correct": True,
                "rationale": (
                    "Correct. An SLA defines quantifiable performance metrics (uptime, response time) paired "
                    "with enforceable remedies, such as service credits, for missed targets — exactly what the "
                    "delivery company needs."
                ),
            },
            {
                "id": "b",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding statement of intent; it cannot enforce measurable "
                    "uptime commitments or trigger service credits for missed performance."
                ),
            },
            {
                "id": "c",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes a joint business partnership with shared profit/loss and "
                    "authority; it is not designed to define vendor performance metrics or remedies."
                ),
            },
            {
                "id": "d",
                "text": "A master service agreement (MSA) with no attached performance schedule",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA establishes overarching legal terms but, without an attached SLA, does "
                    "not itself define measurable performance metrics or service credits."
                ),
            },
        ],
        "explanation": (
            "SLAs are distinguished by measurable performance metrics paired with enforceable remedies for "
            "missed targets — the correct instrument whenever uptime and service-credit commitments are required."
        ),
    },
    {
        "id": "nd5g-012",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two independent nonprofit organizations want to document their mutual intention to give each other's "
            "staff limited read access to a shared volunteer-scheduling database. No money will change hands, and "
            "neither organization wants a legally binding performance obligation — only a documented statement of "
            "cooperative intent. Which document BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A memorandum of understanding (MOU)",
                "correct": True,
                "rationale": (
                    "Correct. An MOU documents a mutual intention to cooperate without creating a legally "
                    "enforceable, financially binding obligation — exactly the arrangement described."
                ),
            },
            {
                "id": "b",
                "text": "A service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines enforceable, measurable performance metrics, implying a binding "
                    "obligation the nonprofits explicitly want to avoid here."
                ),
            },
            {
                "id": "c",
                "text": "A master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA is a binding contract governing the legal terms for recurring paid "
                    "engagements, not a non-binding statement of cooperative intent between nonprofits."
                ),
            },
            {
                "id": "d",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes a binding business partnership with shared liability and "
                    "financial terms — far more formal than the intent-only relationship described."
                ),
            },
        ],
        "explanation": (
            "MOUs capture mutual intent to cooperate without the binding, measurable obligations found in SLAs, "
            "MSAs, or BPAs."
        ),
    },
    {
        "id": "nd5g-013",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "An EV-charging network operator is onboarding a new payment-gateway vendor. Which factor should "
            "PRIMARILY determine the vendor's initial inherent risk tier during onboarding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The sensitivity of the data the vendor will process (cardholder data) and the criticality "
                    "of the payment service to charging-station operations"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Inherent risk tiering is driven by what data the vendor touches and how critical "
                    "the vendor's service is to the business — here, sensitive payment data and a service that "
                    "directly enables revenue-generating transactions."
                ),
            },
            {
                "id": "b",
                "text": "How many years the vendor has been in business and its brand recognition",
                "correct": False,
                "rationale": (
                    "Incorrect. Longevity and brand reputation are not reliable indicators of security risk; a "
                    "long-established vendor can still pose significant risk depending on the data and criticality "
                    "involved."
                ),
            },
            {
                "id": "c",
                "text": "The geographic location of the vendor's corporate headquarters alone",
                "correct": False,
                "rationale": (
                    "Incorrect. Headquarters location alone does not capture the actual risk of data sensitivity "
                    "or service criticality, though jurisdiction may be one input among many, not the primary "
                    "driver."
                ),
            },
            {
                "id": "d",
                "text": "Which vendor submitted the lowest-cost bid during procurement",
                "correct": False,
                "rationale": (
                    "Incorrect. Cost is a procurement consideration, not a security risk-tiering factor, and "
                    "selecting on cost alone can actually increase risk if it overrides security due diligence."
                ),
            },
        ],
        "explanation": (
            "Initial vendor risk tiering should be based on data sensitivity and business criticality — the "
            "factors that determine how much harm a vendor compromise could actually cause."
        ),
    },
    {
        "id": "nd5g-014",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A cold-chain pharmaceutical logistics company's contract with its temperature-monitoring SaaS "
            "vendor includes a right-to-audit clause. Three years into the relationship, the company has never "
            "exercised that clause or requested updated security documentation. Which vendor risk management "
            "practice is currently missing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ongoing/continuous monitoring of the vendor's security posture throughout the relationship "
                    "lifecycle, including actually exercising the audit rights already secured"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Having a right-to-audit clause is only useful if it is actually exercised over "
                    "time; the company has the contractual capability but is not performing the ongoing "
                    "monitoring the relationship requires."
                ),
            },
            {
                "id": "b",
                "text": "A newly negotiated non-disclosure agreement (NDA) to formalize confidentiality expectations",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA addresses confidentiality of shared information, not the need to actually "
                    "exercise existing oversight mechanisms over the vendor's evolving security posture."
                ),
            },
            {
                "id": "c",
                "text": "A right-to-audit clause added to the contract",
                "correct": False,
                "rationale": (
                    "Incorrect. The right-to-audit clause already exists in the contract; the gap is that it has "
                    "never actually been exercised, not that it is missing."
                ),
            },
            {
                "id": "d",
                "text": "A one-time penetration test performed by the vendor's own internal team",
                "correct": False,
                "rationale": (
                    "Incorrect. A vendor-run internal test is not independent, and a one-time test does not "
                    "address the underlying gap, which is the lack of ongoing, exercised oversight."
                ),
            },
        ],
        "explanation": (
            "Effective vendor risk management requires periodically exercising contractual oversight tools like "
            "right-to-audit clauses, not merely holding them unused for years."
        ),
    },
    {
        "id": "nd5g-015",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A digital bank routes 100% of its customer identity-verification checks through a single "
            "third-party identity-proofing vendor. During a regional outage at that vendor, no new customers can "
            "register and no existing customers can complete step-up authentication. Which vendor risk does this "
            "scenario BEST illustrate, and what is the MOST appropriate mitigation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Vendor concentration risk (a single point of failure from sole-sourcing a critical "
                    "function); mitigate by qualifying and maintaining a secondary identity-proofing provider"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Relying entirely on one vendor for a business-critical function creates "
                    "concentration risk — any disruption to that vendor cascades directly into an outage. "
                    "Diversifying to a qualified secondary provider reduces this single point of failure."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Fourth-party risk (an undisclosed subcontractor of the vendor); mitigate by requiring the "
                    "vendor to disclose its subcontractors"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario does not involve an undisclosed subcontractor — it describes total "
                    "dependence on one primary, known vendor, which is concentration risk rather than fourth-party "
                    "risk."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Contractual risk from a missing SLA; mitigate by adding financial penalties for downtime "
                    "to the existing contract"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Penalties might compensate the bank financially, but they do nothing to restore "
                    "service during an outage; the underlying architectural single point of failure remains "
                    "unaddressed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Data residency risk from cross-border processing; mitigate by requiring the vendor to "
                    "process data only within the bank's home country"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario relates to where data is processed or stored; the "
                    "problem is total operational dependence on a single vendor, not data residency."
                ),
            },
        ],
        "explanation": (
            "Sole-sourcing a critical function to one vendor creates concentration risk (a single point of "
            "failure). The correct mitigation is architectural diversification — qualifying an alternate "
            "provider — not merely financial remedies or unrelated controls."
        ),
    },
    {
        "id": "nd5g-016",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A company discontinues a legacy public-facing API integration after learning it contains a critical, "
            "unpatchable vulnerability with no vendor fix available and no feasible compensating control that "
            "would adequately reduce the risk. The integration is fully removed from production. Which risk "
            "management strategy is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk avoidance",
                "correct": True,
                "rationale": (
                    "Correct. Eliminating the risk-bearing activity entirely — removing the vulnerable API "
                    "integration from production because it cannot be adequately secured — is the definition of "
                    "risk avoidance."
                ),
            },
            {
                "id": "b",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation means reducing risk through controls while continuing the activity; "
                    "the company explicitly determined no feasible compensating control existed and removed the "
                    "integration entirely instead."
                ),
            },
            {
                "id": "c",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance means continuing to operate while formally tolerating the risk; the "
                    "company did not continue running the vulnerable integration — it eliminated it."
                ),
            },
            {
                "id": "d",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference shifts the risk to a third party (e.g., via insurance or "
                    "outsourcing); nothing here shifts the risk elsewhere — the activity itself was discontinued."
                ),
            },
        ],
        "explanation": (
            "Risk avoidance eliminates the risk-bearing activity entirely, which is exactly what occurs when an "
            "unpatchable, uncompensatable integration is removed from production rather than mitigated, "
            "accepted, or transferred."
        ),
    },
    {
        "id": "nd5g-017",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A water-treatment facility cannot patch a critical vulnerability in a legacy industrial controller "
            "without voiding the manufacturer's safety certification. Instead, the security team deploys a "
            "dedicated firewall rule set restricting the controller to communicate only with one authorized "
            "engineering workstation, and adds continuous anomaly monitoring on that network segment. Which risk "
            "management strategy is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk mitigation",
                "correct": True,
                "rationale": (
                    "Correct. Deploying compensating controls (network segmentation, restricted communication, "
                    "monitoring) to reduce the likelihood and impact of exploitation — without eliminating the "
                    "controller or the underlying vulnerability — is risk mitigation."
                ),
            },
            {
                "id": "b",
                "text": "Risk avoidance",
                "correct": False,
                "rationale": (
                    "Incorrect. Avoidance would mean removing the controller from service entirely; the facility "
                    "instead continues operating it with added compensating controls."
                ),
            },
            {
                "id": "c",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance implies taking no further action; the team actively implemented "
                    "compensating technical controls rather than simply tolerating the exposure."
                ),
            },
            {
                "id": "d",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference shifts the risk to a third party (such as an insurer or vendor); the "
                    "facility retains the risk and manages it internally with its own controls."
                ),
            },
        ],
        "explanation": (
            "Risk mitigation involves implementing compensating controls to reduce risk when a direct fix "
            "(patching) is not possible, distinct from avoidance (eliminating the activity), acceptance (no "
            "action), or transference (shifting risk to a third party)."
        ),
    },
    {
        "id": "nd5g-018",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "Select the TWO scenarios below that represent risk ACCEPTANCE, as opposed to avoidance, mitigation, "
            "or transference."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A CFO signs a formal, documented risk exception memo tolerating a low-severity finding on a "
                    "billing system scheduled for decommissioning in 90 days"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A formally documented decision to knowingly tolerate a risk, with executive "
                    "sign-off and no further planned action, is a textbook example of risk acceptance."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Executive leadership documents a decision to take no further action on a risk because the "
                    "cost of additional mitigation exceeds the risk's potential loss"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A formal decision to retain a risk as-is, after concluding that further "
                    "mitigation is not cost-justified, is the defining characteristic of risk acceptance."
                ),
            },
            {
                "id": "c",
                "text": "A company purchases a cyber liability insurance policy to cover breach-related costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Purchasing insurance shifts the financial impact of the risk to a third-party "
                    "insurer, which is risk transference, not acceptance."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A network team segments a legacy system onto an isolated VLAN with restricted access to "
                    "reduce the likelihood of exploitation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a technical control (segmentation) to reduce the likelihood or impact of "
                    "an event is risk mitigation, not acceptance."
                ),
            },
        ],
        "explanation": (
            "Risk acceptance is a formal, documented decision to retain a risk without further action — distinct "
            "from transference (shifting the risk via insurance) or mitigation (adding controls to reduce it)."
        ),
    },
    {
        "id": "nd5g-019",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A risk register entry for 'unauthenticated smart-building HVAC control interface' lists an inherent "
            "risk score of 18 (severe) before controls. After the team implemented network isolation and "
            "continuous anomaly monitoring, the entry was updated to show a score of 7 (low). What does the value "
            "'7' represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Residual risk — the risk remaining after controls have been applied",
                "correct": True,
                "rationale": (
                    "Correct. Residual risk is what remains after mitigating controls are put in place, which is "
                    "exactly the post-control score of 7 in this register entry."
                ),
            },
            {
                "id": "b",
                "text": "Inherent risk — the risk level before any controls are considered",
                "correct": False,
                "rationale": (
                    "Incorrect. The inherent (pre-control) risk is the score of 18 given earlier in the scenario, "
                    "not the updated value of 7."
                ),
            },
            {
                "id": "c",
                "text": "Risk appetite — the amount of risk leadership has agreed to accept organization-wide",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk appetite is a leadership-defined threshold set independently of any single "
                    "register entry, not a calculated risk score derived from applying specific controls."
                ),
            },
            {
                "id": "d",
                "text": "Risk velocity — how quickly the risk could materialize and impact the organization",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk velocity describes the speed of onset of a risk event, a separate concept "
                    "from a post-control severity score on the register."
                ),
            },
        ],
        "explanation": (
            "A risk register commonly tracks both inherent risk (before controls) and residual risk (after "
            "controls). Here, 18 is inherent and 7 is residual — distinct from appetite (a leadership threshold) "
            "or velocity (speed of onset)."
        ),
    },
    {
        "id": "nd5g-020",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A board-approved risk appetite statement reads: 'No individual risk with a residual score above 15 "
            "(on a 25-point scale) may proceed without documented executive exception.' A new data-sharing "
            "initiative is assessed with a residual risk score of 19. What must happen next?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The initiative must be formally escalated for a documented exception, reviewed and signed "
                    "off by the designated risk-acceptance authority, before it may proceed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The appetite statement explicitly requires a documented executive exception for "
                    "any risk exceeding the threshold; a score of 19 exceeds 15, triggering that requirement "
                    "before the initiative can move forward."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The initiative is automatically and permanently cancelled, since it exceeds the appetite "
                    "threshold"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Exceeding the appetite threshold triggers a documented exception process, not an "
                    "automatic, permanent cancellation — the initiative may still proceed if formally approved."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The initiative may proceed immediately without further review, since business need "
                    "outweighs the stated appetite"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Business need does not override a documented governance requirement; the "
                    "appetite statement explicitly mandates a formal exception before proceeding above the "
                    "threshold."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The initiative must be reported directly to an external regulator for independent approval"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risk appetite exceptions are an internal governance matter handled by the "
                    "organization's designated risk-acceptance authority, not an external regulatory approval "
                    "process."
                ),
            },
        ],
        "explanation": (
            "A quantified risk appetite statement establishes a threshold; risks exceeding it require a "
            "documented exception from the designated internal authority, not automatic cancellation or silent "
            "approval."
        ),
    },
    {
        "id": "nd5g-021",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A risk register entry for 'expanding SaaS shadow-IT footprint' has an assigned owner, a documented "
            "inherent score, and a documented residual score, and is scheduled for its next formal review in six "
            "months. However, the entry defines no threshold or indicator that would trigger an earlier, "
            "out-of-cycle reassessment if the situation worsens rapidly. Which practice is missing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A defined key risk indicator (KRI) or trigger threshold that prompts escalation and "
                    "reassessment before the next scheduled review"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Without a defined KRI or trigger threshold, a rapidly worsening risk could go "
                    "unnoticed for months until the next scheduled review, even though it may need immediate "
                    "attention."
                ),
            },
            {
                "id": "b",
                "text": "A risk owner assigned to be accountable for tracking and treating the risk",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the entry already has an assigned owner; that requirement is "
                    "already satisfied."
                ),
            },
            {
                "id": "c",
                "text": "A documented residual risk score reflecting current controls",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the entry already has a documented residual score; that "
                    "requirement is already satisfied."
                ),
            },
            {
                "id": "d",
                "text": "A scheduled date for the next periodic review of the risk",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states a six-month review is already scheduled; the gap is the "
                    "absence of an early-warning trigger for reassessment before that scheduled date, not the "
                    "absence of a scheduled review itself."
                ),
            },
        ],
        "explanation": (
            "A mature risk register entry needs not only an owner, scores, and a periodic review date, but also "
            "defined key risk indicators or triggers that can prompt reassessment ahead of schedule when "
            "conditions change rapidly."
        ),
    },
    {
        "id": "nd5g-022",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "Select the TWO purposes a risk register serves within an organization's governance program."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Provides a centralized, prioritized inventory of identified risks to inform leadership "
                    "decision-making and resource allocation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A risk register's core purpose is to consolidate and prioritize known risks so "
                    "leadership can make informed decisions about where to focus resources and attention."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Establishes accountability by documenting an assigned owner responsible for tracking and "
                    "treating each risk"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Recording an owner for each entry creates clear accountability, ensuring someone "
                    "is responsible for driving each risk through assessment, treatment, and reporting."
                ),
            },
            {
                "id": "c",
                "text": "Serves as a substitute for conducting a formal business impact analysis (BIA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A risk register tracks identified risks; it does not replace the distinct "
                    "process of a BIA, which determines criticality, RTOs, and RPOs for business functions."
                ),
            },
            {
                "id": "d",
                "text": "Automatically enforces technical controls on the systems associated with each risk",
                "correct": False,
                "rationale": (
                    "Incorrect. A risk register is a documentation and tracking artifact; it has no mechanism to "
                    "automatically deploy or enforce technical controls."
                ),
            },
        ],
        "explanation": (
            "Risk registers exist to centralize and prioritize risk information for leadership and to assign "
            "clear ownership — they are documentation tools, not substitutes for BIAs and not automated "
            "enforcement mechanisms."
        ),
    },
    {
        "id": "nd5g-023",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "One governance document mandates that 'all customer records must be retained for no longer than 7 "
            "years from the date of account closure.' A separate document provides the exact database purge "
            "scripts, schedule, and validation steps used to enforce that retention limit. What are these two "
            "documents called, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard (the 7-year retention mandate) and procedure (the purge scripts and schedule)",
                "correct": True,
                "rationale": (
                    "Correct. A standard specifies a mandatory, measurable requirement (7 years). A procedure "
                    "gives the mandatory step-by-step instructions for how to implement and enforce it."
                ),
            },
            {
                "id": "b",
                "text": "Policy (the 7-year retention mandate) and guideline (the purge scripts and schedule)",
                "correct": False,
                "rationale": (
                    "Incorrect. A policy is a broad, high-level statement of intent, not a specific measurable "
                    "mandate; a guideline is optional/recommended, but the purge steps here are mandatory, "
                    "matching a procedure instead."
                ),
            },
            {
                "id": "c",
                "text": "Procedure (the 7-year retention mandate) and standard (the purge scripts and schedule)",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the correct pairing — the specific measurable requirement is the "
                    "standard, and the step-by-step instructions are the procedure."
                ),
            },
            {
                "id": "d",
                "text": "Guideline (the 7-year retention mandate) and policy (the purge scripts and schedule)",
                "correct": False,
                "rationale": (
                    "Incorrect. A guideline implies an optional, recommended practice, but the 7-year limit is "
                    "mandatory; a policy is a broad statement of intent, not detailed instructions."
                ),
            },
        ],
        "explanation": (
            "Governance hierarchy: policy (broad intent) -> standard (mandatory, measurable requirement) -> "
            "procedure (mandatory step-by-step instructions) -> guideline (optional recommendation)."
        ),
    },
    {
        "id": "nd5g-024",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "Company guidance recommends, but does not require, that employees enable an additional biometric "
            "lock screen on company-issued phones for faster, more convenient unlocking. The mandatory security "
            "policy already requires a 6-digit PIN, which one employee uses without enabling the recommended "
            "biometric option. Has the employee violated a governance document?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "No — the biometric lock screen is described in a guideline, which is optional and "
                    "recommended rather than mandatory, so not following it is not a violation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Guidelines represent recommended best practices, not mandatory requirements. Since "
                    "the employee already satisfies the mandatory PIN requirement in the policy, declining the "
                    "optional biometric recommendation is not a violation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Yes — any documented security recommendation, whether labeled mandatory or optional, "
                    "carries the same enforceable weight as a policy"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Governance documents are intentionally tiered; guidelines are explicitly "
                    "non-mandatory and do not carry the same enforceable weight as a policy or standard."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Yes — declining an available security enhancement always constitutes negligence regardless "
                    "of whether it was required"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Declining a recommended, non-mandatory enhancement while still meeting the "
                    "mandatory control (the PIN) is not negligence; the governance framework distinguishes "
                    "required controls from optional recommendations for exactly this reason."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No — because guidelines are only ever issued for physical security, not for mobile device "
                    "configuration"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The conclusion (no violation) is right, but the reasoning is wrong — guidelines "
                    "can cover any security topic, including mobile device configuration; the determining factor "
                    "is that guidelines are optional, not their subject matter."
                ),
            },
        ],
        "explanation": (
            "Guidelines are recommended, non-mandatory practices. Not following a guideline is not a governance "
            "violation as long as the applicable mandatory policy or standard is still satisfied."
        ),
    },
    {
        "id": "nd5g-025",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A business unit operates a legacy manufacturing execution system that cannot be upgraded to meet the "
            "organization's mandatory multifactor authentication standard without breaking certified production "
            "line integrations. The business unit wants to keep the system running past the standard's compliance "
            "deadline. What is the CORRECT governance process to follow?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Submit a formal, risk-based policy exception request to the designated risk-acceptance "
                    "authority, documenting compensating controls and a defined expiration or re-review date"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Deviations from a mandatory standard must go through a formal, documented exception "
                    "process — assessed by the appropriate authority, paired with compensating controls, and "
                    "time-bound — rather than being decided unilaterally by the business unit."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The business unit documents its own justification internally and continues operating the "
                    "system without notifying security governance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Bypassing the governance function entirely removes independent risk oversight "
                    "and accountability, undermining the purpose of having a mandatory standard in the first "
                    "place."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The mandatory standard is automatically waived for any system where compliance would break "
                    "existing integrations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Standards do not include automatic waivers based on technical inconvenience; "
                    "every deviation requires an explicit, documented, and approved exception."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The system must be immediately decommissioned, since no exception process exists for "
                    "mandatory standards"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Formal exception processes do exist precisely for situations like this; "
                    "immediate decommissioning is not required if a documented, approved, compensating-control "
                    "exception can be obtained instead."
                ),
            },
        ],
        "explanation": (
            "Legitimate deviations from mandatory standards require a formal, documented exception process — "
            "reviewed by the appropriate authority, backed by compensating controls, and time-bound — not "
            "unilateral action, automatic waivers, or forced decommissioning."
        ),
    },
    {
        "id": "nd5g-026",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A CISO is briefing new hires on the different drivers behind the organization's security "
            "requirements. Which of the following is the BEST example of a contractual/industry-mandated security "
            "requirement, as opposed to a legal/regulatory requirement imposed by government law?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "PCI DSS compliance, required by the payment card brands as a condition of accepting "
                    "card payments, rather than imposed directly by government statute"
                ),
                "correct": True,
                "rationale": (
                    "Correct. PCI DSS is established and enforced by the payment card industry itself (via "
                    "card brand contracts and merchant agreements), not by government legislation — a classic "
                    "example of a contractual/industry-driven requirement."
                ),
            },
            {
                "id": "b",
                "text": "HIPAA compliance, required by U.S. federal law for covered entities handling health data",
                "correct": False,
                "rationale": (
                    "Incorrect. HIPAA is a U.S. federal statute; compliance is a legal/regulatory requirement, "
                    "not a contractual or industry-imposed one."
                ),
            },
            {
                "id": "c",
                "text": "GDPR compliance, required by European Union regulation for processing EU residents' data",
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR is an EU regulation with the force of law; it is a legal/regulatory "
                    "requirement, not a contractual/industry standard."
                ),
            },
            {
                "id": "d",
                "text": "Sarbanes-Oxley (SOX) compliance, required by U.S. federal securities law for public companies",
                "correct": False,
                "rationale": (
                    "Incorrect. SOX is U.S. federal legislation; compliance is a legal/regulatory obligation, "
                    "not one imposed through industry contracts."
                ),
            },
        ],
        "explanation": (
            "Governance requirements can be driven by law/regulation (HIPAA, GDPR, SOX) or by contractual/"
            "industry mandates (PCI DSS, imposed by the payment card brands rather than a government body). "
            "Recognizing the distinction helps determine enforcement mechanisms and applicability."
        ),
    },
    {
        "id": "nd5g-027",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A U.S.-based online retailer has no physical offices, employees, or servers in the European Union, "
            "but its website is available in French and German, prices are displayed in euros, and it ships "
            "directly to EU addresses with targeted EU marketing campaigns. Does GDPR apply to this retailer's "
            "processing of EU customers' personal data?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Yes — GDPR has extraterritorial scope and applies to any organization, regardless of "
                    "physical location, that offers goods or services to individuals in the EU"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Under GDPR's extraterritorial scope (Article 3), the regulation applies to "
                    "processing of EU residents' data whenever an organization offers goods or services to them, "
                    "regardless of where the organization itself is based."
                ),
            },
            {
                "id": "b",
                "text": (
                    "No — GDPR only applies to organizations with a physical office, subsidiary, or server "
                    "located within the European Union"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR explicitly extends beyond organizations physically located in the EU; "
                    "physical presence is not a prerequisite for applicability."
                ),
            },
            {
                "id": "c",
                "text": (
                    "No — GDPR only applies to companies that are legally incorporated within an EU member state"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Incorporation location is irrelevant to GDPR applicability; the determining "
                    "factor is whether the organization targets or offers goods/services to individuals in the "
                    "EU."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Yes, but only if the retailer also maintains an EU-based bank account for processing "
                    "payments"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR applicability does not depend on banking arrangements; it turns on whether "
                    "the organization is offering goods or services to, or monitoring the behavior of, individuals "
                    "in the EU."
                ),
            },
        ],
        "explanation": (
            "GDPR's extraterritorial scope means that offering goods or services to EU residents — evidenced "
            "here by localized language, euro pricing, and targeted marketing — triggers applicability "
            "regardless of the organization's physical location."
        ),
    },
    {
        "id": "nd5g-028",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A company operating in the EU confirms that attackers exfiltrated a database containing EU "
            "residents' personal data, and the incident is assessed as likely to result in a high risk to the "
            "affected individuals' rights and freedoms (e.g., identity theft exposure). Beyond notifying the "
            "supervisory authority within 72 hours, what ADDITIONAL obligation does GDPR impose in a high-risk "
            "scenario like this?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The company must also communicate the breach to the affected data subjects themselves, "
                    "without undue delay"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When a breach is likely to result in a high risk to individuals' rights and "
                    "freedoms, GDPR requires direct communication to the affected data subjects, in addition to "
                    "the 72-hour supervisory authority notification."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The company must extend its 72-hour supervisory authority notification window to 30 days "
                    "for high-risk breaches"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. High risk does not extend the notification timeline — if anything, the urgency "
                    "increases; the 72-hour supervisory authority window remains, and subject notification is "
                    "an additional, not extended, obligation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The company is relieved of the supervisory authority notification requirement if the risk "
                    "is classified as high rather than low"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is backwards — supervisory authority notification remains required "
                    "regardless, and a high-risk classification adds the subject-notification obligation rather "
                    "than removing any existing one."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The company must pay each affected data subject a fixed statutory compensation amount set "
                    "by GDPR"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR does not establish a fixed, automatic per-person compensation amount for "
                    "breaches; individuals may separately pursue damages, but this is not a defined breach-"
                    "notification obligation."
                ),
            },
        ],
        "explanation": (
            "GDPR distinguishes between the 72-hour supervisory authority notification (required for most "
            "breaches) and direct notification to affected data subjects without undue delay, which is an "
            "additional obligation triggered specifically when the breach poses a high risk to their rights and "
            "freedoms."
        ),
    },
    {
        "id": "nd5g-029",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "An online retailer analyzes transaction patterns to detect and block fraudulent purchases, without "
            "obtaining separate opt-in consent from each customer for this specific analysis. The retailer has "
            "documented a formal assessment weighing its interest in preventing fraud against the impact on "
            "customers' privacy, and concluded the processing is necessary and proportionate. Which GDPR lawful "
            "basis for processing is the retailer relying on?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Legitimate interest, supported by a documented balancing test weighing the retailer's "
                    "interest against the impact on data subjects"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Legitimate interest allows processing without separate consent when the "
                    "controller's interest (here, fraud prevention) is documented and shown, through a balancing "
                    "test, not to be overridden by the individual's privacy rights."
                ),
            },
            {
                "id": "b",
                "text": "Consent, since the customer implicitly agreed by making a purchase on the website",
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR consent must be a freely given, specific, informed, and unambiguous "
                    "affirmative action — it cannot be inferred implicitly from making a purchase, and the "
                    "scenario states no separate opt-in consent was obtained."
                ),
            },
            {
                "id": "c",
                "text": "Contractual necessity, since fraud analysis is required to fulfill the purchase contract",
                "correct": False,
                "rationale": (
                    "Incorrect. Fraud-detection analytics go beyond what is strictly necessary to fulfill the "
                    "immediate purchase contract itself; the scenario specifically describes a legitimate-"
                    "interest balancing test, not a contract-performance justification."
                ),
            },
            {
                "id": "d",
                "text": "Vital interest, since fraud prevention protects the customer's life or physical safety",
                "correct": False,
                "rationale": (
                    "Incorrect. Vital interest applies to processing necessary to protect someone's life (e.g., "
                    "medical emergencies), not financial fraud prevention."
                ),
            },
        ],
        "explanation": (
            "Legitimate interest is a lawful basis that permits processing without separate consent when the "
            "controller documents a balancing test showing its interest is not overridden by the individual's "
            "rights — a common basis for fraud prevention."
        ),
    },
    {
        "id": "nd5g-030",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "Select the TWO statements that correctly describe core data-processing PRINCIPLES defined under "
            "GDPR Article 5, as opposed to data-subject rights or breach-notification obligations."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data minimization — personal data collected must be adequate, relevant, and limited to "
                    "what is necessary for the stated purpose"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Data minimization is one of the six core processing principles in GDPR Article 5, "
                    "requiring that only necessary data be collected."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Storage limitation — personal data must not be retained in identifiable form for longer "
                    "than necessary for the purposes for which it was collected"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Storage limitation is another of the six Article 5 principles, requiring "
                    "retention periods to be tied to the stated purpose rather than indefinite."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Right to erasure — data subjects may request deletion of their personal data under "
                    "certain conditions"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The right to erasure is a data-subject right (Article 17), not one of the six "
                    "Article 5 processing principles."
                ),
            },
            {
                "id": "d",
                "text": (
                    "72-hour notification — controllers must notify the supervisory authority within 72 hours "
                    "of becoming aware of a qualifying breach"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The 72-hour notification rule is a breach-notification obligation (Article 33), "
                    "not one of the six Article 5 processing principles."
                ),
            },
        ],
        "explanation": (
            "GDPR Article 5 defines processing principles (lawfulness/fairness/transparency, purpose limitation, "
            "data minimization, accuracy, storage limitation, integrity/confidentiality) — distinct from "
            "data-subject rights (like erasure) and separate breach-notification obligations (like the 72-hour "
            "rule)."
        ),
    },
    {
        "id": "nd5g-031",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A beverage company's secret flavor formula is stored in a locked vault-style repository accessible "
            "to only two employees, who have each signed additional confidentiality agreements beyond the "
            "standard NDA. Which data classification level is MOST appropriate for this formula?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The organization's highest internal classification tier (e.g., 'Restricted' or 'Top "
                    "Secret'), reserved for information whose disclosure would cause catastrophic, "
                    "existential harm to the business"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A core trade secret that constitutes the company's primary competitive "
                    "differentiator — protected with vault-level access and extra confidentiality obligations — "
                    "warrants the organization's highest classification tier, well above ordinary confidential "
                    "data."
                ),
            },
            {
                "id": "b",
                "text": "'Confidential,' the same tier used for routine internal financial reports",
                "correct": False,
                "rationale": (
                    "Incorrect. Treating an existential trade secret the same as routine internal financial "
                    "reports understates its sensitivity; the extreme access restrictions described (vault "
                    "storage, two named employees, extra agreements) reflect a tier above ordinary confidential "
                    "data."
                ),
            },
            {
                "id": "c",
                "text": "'Internal,' since the formula is only used within company operations and never shared publicly",
                "correct": False,
                "rationale": (
                    "Incorrect. 'Internal' typically covers general business information with low-to-moderate "
                    "sensitivity; the extraordinary protections applied here go far beyond what an 'Internal' "
                    "classification would justify."
                ),
            },
            {
                "id": "d",
                "text": "'Public,' since the finished product itself is sold openly to consumers",
                "correct": False,
                "rationale": (
                    "Incorrect. The finished product being sold publicly does not mean its underlying "
                    "manufacturing formula is public; the formula itself remains one of the company's most "
                    "closely guarded secrets."
                ),
            },
        ],
        "explanation": (
            "Classification levels scale with the harm disclosure would cause. A trade secret whose exposure "
            "could be existential to the business — protected accordingly — belongs at the organization's "
            "highest internal tier, not merely 'Confidential' or lower."
        ),
    },
    {
        "id": "nd5g-032",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "Marketing materials describing a new product were classified 'Confidential' during development to "
            "prevent premature disclosure ahead of a scheduled embargo. The embargo has now lifted, and the "
            "product was officially launched with a public press release covering the same details. What should "
            "happen to the classification of the original marketing materials?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The materials should be formally reclassified to 'Public' now that the embargo has "
                    "lifted and the same information has been officially released"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification is tied to the sensitivity of the information at a given time; "
                    "once the embargo-driven reason for restriction no longer applies and the same content has "
                    "been officially released, the materials should be downgraded to reflect their current, "
                    "public status."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The materials must remain 'Confidential' permanently, since classification levels are "
                    "never changed once assigned"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification is not permanent — data classification policies typically "
                    "include a process for periodic review and reclassification (upgrade or downgrade) as "
                    "circumstances change."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The materials should be upgraded to 'Restricted,' since public launches increase overall "
                    "organizational risk"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Upgrading classification after information has already been made public is "
                    "backwards; the driver for restriction (the embargo) has ended, warranting a downgrade, not "
                    "an upgrade."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The classification should be left unchanged until the next scheduled annual data "
                    "classification audit, regardless of the embargo lifting"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting for a distant scheduled audit is unnecessary and creates needless "
                    "handling friction; reclassification should occur promptly once the triggering event (the "
                    "embargo lifting and public release) has clearly occurred."
                ),
            },
        ],
        "explanation": (
            "Data classification is dynamic and event-driven, not permanent. Once the reason for restriction "
            "(an embargo) no longer applies and the same content is publicly released, the classification "
            "should be promptly downgraded to match its current sensitivity."
        ),
    },
    {
        "id": "nd5g-033",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "A single email thread contains an opening paragraph of publicly released marketing copy and, "
            "further down, an unreleased summary of confidential merger-and-acquisition negotiation terms. At "
            "what classification level must the entire email be handled?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The highest classification level present anywhere in the email — in this case, "
                    "'Confidential' (or higher) — governs handling of the entire message"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When a single document or message mixes content of differing sensitivity, "
                    "standard practice is to handle the entire item at its highest classification level, since "
                    "the whole message cannot be selectively protected."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The email may be handled as 'Public' overall, since the publicly released marketing copy "
                    "appears first in the message"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The order in which content appears does not lower the required protection level; "
                    "the confidential M&A content anywhere in the message drives the classification of the whole "
                    "email."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The email should be classified based on the average sensitivity of its sections, "
                    "resulting in an 'Internal' rating"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification is not averaged across a document's sections; the presence of any "
                    "highly sensitive content requires the whole item to be protected at that higher level."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Each recipient may independently decide which classification level applies based on "
                    "their own judgment of the content"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification is determined by the data owner and organizational policy, not "
                    "left to each individual recipient's discretion, which would produce inconsistent and "
                    "insecure handling."
                ),
            },
        ],
        "explanation": (
            "When content of mixed sensitivity is combined into a single document or message, the entire item "
            "must be classified and handled at the highest sensitivity level present within it."
        ),
    },
    {
        "id": "nd5g-034",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A ride-sharing app decides which trip data to collect (pickup/drop-off locations, route, fare) and "
            "determines it will be used for both billing and internal safety analytics. The app stores this data "
            "with a cloud storage vendor that processes and retains it strictly according to the app's written "
            "instructions and retention schedule. Which roles do the ride-sharing app and the cloud storage "
            "vendor hold, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The ride-sharing app is the data controller; the cloud storage vendor is the data processor",
                "correct": True,
                "rationale": (
                    "Correct. The app determines the purposes and means of processing (what data to collect and "
                    "why), making it the controller. The vendor acts strictly on the app's instructions, making "
                    "it the processor."
                ),
            },
            {
                "id": "b",
                "text": "The ride-sharing app is the data processor; the cloud storage vendor is the data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the roles — the vendor does not decide why or how the data is "
                    "used; it merely follows the app's instructions, which is the definition of a processor, not "
                    "a controller."
                ),
            },
            {
                "id": "c",
                "text": "Both the ride-sharing app and the cloud storage vendor are joint data controllers",
                "correct": False,
                "rationale": (
                    "Incorrect. Joint controllers both determine the purposes and means of processing together; "
                    "here, only the app makes those determinations, and the vendor merely executes them per "
                    "instruction."
                ),
            },
            {
                "id": "d",
                "text": "The ride-sharing app is the data custodian; the cloud storage vendor is the data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. A custodian applies technical safeguards under a data owner's direction; the app "
                    "is not merely implementing someone else's decisions — it is the entity that decided what "
                    "data to collect and why, which makes it the controller."
                ),
            },
        ],
        "explanation": (
            "The entity that determines the purposes and means of processing is the controller; an entity that "
            "processes data strictly per the controller's instructions is the processor."
        ),
    },
    {
        "id": "nd5g-035",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "An insurance carrier's business data owner sets the classification level and access requirements "
            "for its claims-processing dataset. A cloud operations team then implements the day-to-day technical "
            "safeguards — configuring encryption keys, access-control lists, and backup schedules — required to "
            "meet those requirements, without making any decisions about who should ultimately be allowed access. "
            "Which role does the cloud operations team hold?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data custodian",
                "correct": True,
                "rationale": (
                    "Correct. A custodian implements the technical safeguards (encryption, access controls, "
                    "backups) required to protect data according to classification and requirements set by the "
                    "data owner, without making the underlying access-policy decisions."
                ),
            },
            {
                "id": "b",
                "text": "Data owner",
                "correct": False,
                "rationale": (
                    "Incorrect. The data owner is explicitly identified as the business role that sets "
                    "classification and access requirements; the cloud operations team only implements those "
                    "requirements technically."
                ),
            },
            {
                "id": "c",
                "text": "Data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. The controller (in a GDPR sense) determines the purposes and means of "
                    "processing; the cloud operations team does not decide why the data is processed, only how "
                    "it is technically protected per instructions."
                ),
            },
            {
                "id": "d",
                "text": "Data subject",
                "correct": False,
                "rationale": (
                    "Incorrect. A data subject is the individual whom the personal data is about, not an "
                    "organizational role responsible for implementing technical safeguards."
                ),
            },
        ],
        "explanation": (
            "The data custodian role handles the technical implementation of security controls (encryption, "
            "ACLs, backups) as directed by the data owner, distinct from the owner (who sets requirements) or "
            "the controller (who determines processing purposes)."
        ),
    },
    {
        "id": "nd5g-036",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "Two independent airlines in a codeshare alliance jointly design a shared loyalty-rewards program. "
            "Together, they jointly decide which passenger flight and spending data will be collected and how it "
            "will be used to calculate combined loyalty points across both carriers. Neither airline unilaterally "
            "controls these decisions. Which data role do the two airlines share?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Joint controllers",
                "correct": True,
                "rationale": (
                    "Correct. When two or more entities jointly determine the purposes and means of processing "
                    "the same personal data, they are joint controllers, sharing responsibility for that "
                    "processing."
                ),
            },
            {
                "id": "b",
                "text": "Data processors",
                "correct": False,
                "rationale": (
                    "Incorrect. Processors act on the instructions of a separate controller; here, both "
                    "airlines are jointly making the underlying decisions about purposes and means themselves, "
                    "not following another party's instructions."
                ),
            },
            {
                "id": "c",
                "text": "Data custodians",
                "correct": False,
                "rationale": (
                    "Incorrect. Custodians implement technical safeguards under someone else's direction; the "
                    "airlines are making the strategic decisions about data collection and use, which is a "
                    "controller function, not a custodial one."
                ),
            },
            {
                "id": "d",
                "text": "Data subjects",
                "correct": False,
                "rationale": (
                    "Incorrect. Data subjects are the individuals whom the personal data describes (the "
                    "passengers), not the organizations making decisions about how that data is processed."
                ),
            },
        ],
        "explanation": (
            "Joint controllers arise when two or more parties together determine the purposes and means of "
            "processing shared data — distinct from processors (who follow instructions) and custodians (who "
            "implement technical safeguards)."
        ),
    },
    {
        "id": "nd5g-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "An IT asset disposition team is decommissioning a batch of solid-state drives (SSDs) that stored "
            "sensitive engineering data, and will not reuse or resell them. A junior technician proposes running "
            "the drives through the same industrial degausser used for the organization's magnetic tape backups. "
            "Why is this approach inappropriate for the SSDs?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "SSDs store data electronically via NAND flash cells rather than magnetically, so "
                    "degaussing has no reliable effect on them; cryptographic erase or physical destruction "
                    "should be used instead"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Degaussing works by disrupting the magnetic domains on magnetic media (like hard "
                    "disk platters or tape); SSDs have no magnetic storage medium, so degaussing does not "
                    "reliably sanitize them. NIST SP 800-88 recommends cryptographic erase or physical "
                    "destruction for flash-based media."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Degaussing is effective on SSDs but is prohibited by regulation for any device that "
                    "previously stored engineering data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no such blanket regulatory prohibition tied to engineering data; the "
                    "actual issue is a technical one — degaussing simply does not work on non-magnetic flash "
                    "media."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Degaussing is effective on SSDs, but only if performed twice consecutively to fully erase "
                    "all sectors"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Repeating an ineffective process does not make it effective; degaussing has no "
                    "meaningful effect on flash memory regardless of how many times it is applied."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Degaussing works equally well on SSDs and magnetic tape, so this approach is actually "
                    "appropriate and should proceed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is factually wrong — degaussing relies on disrupting magnetic domains, "
                    "which SSDs do not have, making the technique ineffective for sanitizing flash-based storage."
                ),
            },
        ],
        "explanation": (
            "Sanitization method must match media type. Degaussing is effective only on magnetic media; SSDs "
            "require cryptographic erase or physical destruction (shredding/pulverizing) per NIST SP 800-88 "
            "guidance."
        ),
    },
    {
        "id": "nd5g-038",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "An aerospace manufacturer contracts a third-party e-waste vendor to physically shred a batch of hard "
            "drives that stored export-controlled technical data. Which artifact should the manufacturer obtain "
            "from the vendor to provide auditable proof that the drives were properly destroyed?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A certificate of destruction, ideally including serial numbers, destruction method, "
                    "date, and (for export-controlled data) witnessed or on-site verification"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A certificate of destruction provides the formal, auditable record that specific "
                    "media were destroyed, by whom, when, and how — critical evidence for compliance, especially "
                    "with export-controlled data where witnessed destruction may also be warranted."
                ),
            },
            {
                "id": "b",
                "text": "A signed non-disclosure agreement (NDA) with the e-waste vendor",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects confidentiality of information the vendor might encounter, but "
                    "it does not document that the specific drives were actually destroyed."
                ),
            },
            {
                "id": "c",
                "text": "A service level agreement (SLA) defining the vendor's pickup and turnaround times",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA addresses operational performance metrics like turnaround time, not "
                    "auditable proof that destruction of specific media actually occurred."
                ),
            },
            {
                "id": "d",
                "text": "A memorandum of understanding (MOU) outlining the general disposal relationship",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding statement of general intent to cooperate; it provides no "
                    "specific, auditable evidence that any particular batch of drives was destroyed."
                ),
            },
        ],
        "explanation": (
            "A certificate of destruction is the auditable evidence needed to confirm that specific media were "
            "properly sanitized or destroyed by a third-party vendor, distinct from general contractual "
            "documents like NDAs, SLAs, or MOUs."
        ),
    },
    {
        "id": "nd5g-039",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company returns a batch of leased core routers and switches to the leasing company at the end of "
            "the contract term. IT staff remove the devices from the network monitoring system but do not reset "
            "the devices to factory defaults or clear their saved (NVRAM) startup configuration before shipping "
            "them back. What is the PRIMARY security risk this creates?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The saved configurations may expose internal network topology, VLAN design, ACLs, and "
                    "potentially stored credentials or shared keys to whoever handles the devices next"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Router and switch startup configurations often contain sensitive details — "
                    "network topology, VLAN assignments, access control lists, SNMP community strings, and "
                    "sometimes locally stored credentials or pre-shared keys — that would be exposed to the next "
                    "handler if not cleared before the devices leave company control."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The leasing company will be unable to bill the organization correctly without the saved "
                    "configuration data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Billing is unrelated to device configuration data; the actual concern is "
                    "confidentiality exposure of sensitive network information, not a billing dependency."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Leaving the configuration intact violates hardware warranty terms and voids future "
                    "support eligibility"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Warranty and support eligibility are not affected by leaving configuration data "
                    "on returned devices; the real issue is that sensitive network design information remains "
                    "exposed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Removing devices from the network monitoring system is sufficient on its own to prevent "
                    "any data exposure risk"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Removing a device from monitoring only stops the organization from watching it; "
                    "it does nothing to clear the sensitive configuration data still stored on the device itself."
                ),
            },
        ],
        "explanation": (
            "Decommissioning network hardware requires clearing saved configurations (NVRAM/startup-config), not "
            "just removing devices from monitoring, to prevent exposure of network topology, ACLs, and stored "
            "credentials to the next party who handles the equipment."
        ),
    },
    {
        "id": "nd5g-040",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "An organization's standard annual security awareness training covers phishing, password hygiene, "
            "and physical security for all employees. Database administrators and cloud infrastructure engineers "
            "receive no additional training beyond this general course, despite having standing privileged access "
            "capable of exfiltrating or destroying entire production datasets. Which improvement would MOST "
            "directly address this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Supplementing the general training with role-based awareness training tailored to "
                    "privileged users, covering topics like insider-threat indicators, privileged-session "
                    "monitoring, and social engineering targeting admin credentials"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Users with elevated access represent disproportionate risk and face threats "
                    "(targeted social engineering, insider-threat scenarios) that general awareness training does "
                    "not cover; role-based training closes that gap for the population that needs it most."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increasing the frequency of the same general-audience training from annual to "
                    "semi-annual for all employees, including privileged users"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Repeating identical, non-tailored content more often does not address the "
                    "specific risks unique to privileged access; the content itself, not just its frequency, "
                    "needs to be tailored to that population."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Removing privileged users from the general awareness training entirely, since they are "
                    "assumed to already understand security topics"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Privileged users should receive the baseline general training in addition to "
                    "supplemental role-based content, not be exempted from foundational awareness topics."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Requiring privileged users to sign an acknowledgment of the acceptable use policy (AUP) "
                    "in lieu of any training"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Signing an acknowledgment confirms awareness of a policy's existence but does "
                    "not provide the substantive training needed to recognize and respond to threats specifically "
                    "targeting privileged access."
                ),
            },
        ],
        "explanation": (
            "A mature security awareness program layers role-based training on top of general organization-wide "
            "training for populations — like privileged users — who face elevated or distinct risks that generic "
            "content does not adequately cover."
        ),
    },
    {
        "id": "nd5g-041",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "A call-center company previously responded to failed phishing simulations by having a manager "
            "publicly name every employee who clicked, in a company-wide email. After switching to a leaderboard "
            "that publicly recognizes and rewards the employees who report the most simulated phishing emails, "
            "the organization observes both a lower click-through rate and a higher self-reporting rate over the "
            "following two quarters. What does this trend BEST demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Positive reinforcement (recognizing and rewarding good reporting behavior) is more "
                    "effective at driving both reduced clicks and increased self-reporting than punitive, "
                    "public-shaming approaches"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Publicly shaming employees who click tends to discourage honest self-reporting "
                    "out of fear of embarrassment, while positive reinforcement encourages the desired behavior "
                    "(reporting) without that chilling effect — exactly the improvement observed after the "
                    "switch."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The improvement is coincidental and unrelated to the change in approach, since click "
                    "rates naturally decline over time regardless of program design"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While some natural variation can occur, attributing a sustained two-quarter "
                    "improvement in both metrics purely to coincidence ignores the clear behavioral mechanism "
                    "(reduced fear of public shaming, increased incentive to report) introduced by the program "
                    "change."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Public recognition of any kind, positive or negative, produces identical behavioral "
                    "outcomes, so the specific approach used does not matter"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario shows a clear behavioral difference between the punitive and "
                    "positive approaches — negative public exposure suppressed reporting, while positive "
                    "recognition increased it, demonstrating the approach does matter."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The leaderboard approach is effective only because it eliminated the phishing simulation "
                    "program entirely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario describes a continued phishing simulation program with a different "
                    "reward structure, not the elimination of simulations altogether."
                ),
            },
        ],
        "explanation": (
            "Punitive, shame-based responses to phishing-simulation failures tend to suppress honest self-"
            "reporting due to fear of embarrassment. Positive reinforcement that rewards good reporting behavior "
            "is generally more effective at improving both click rates and reporting rates."
        ),
    },
    {
        "id": "nd5g-042",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "A finance department employee nearly wired funds after receiving a phone call that used AI-"
            "generated audio closely mimicking the CFO's voice, urgently instructing an out-of-cycle payment. The "
            "organization's annual awareness training content has not been updated in three years and does not "
            "mention voice-based social engineering or synthetic media. What should the security awareness team "
            "do in response?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Update the training content to specifically address emerging threats such as AI-generated "
                    "voice deepfakes used in vishing and business email compromise attempts, alongside "
                    "verification procedures for unusual payment requests"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Awareness training must evolve as attacker techniques evolve; content that has "
                    "not been updated in three years is unlikely to prepare staff for newer threats like "
                    "AI-generated voice impersonation, which this near-miss demonstrates is now a real, relevant "
                    "risk."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Continue delivering the same annual training unchanged, since the employee ultimately did "
                    "not complete the fraudulent transfer"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A near-miss is a clear signal that the training content is outdated and gapped; "
                    "the fact that this particular attempt failed does not mean future attempts using the same "
                    "technique will also fail without updated preparation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Discontinue phone-based verification for all payment requests going forward, replacing "
                    "it entirely with training on physical security topics"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical security topics are unrelated to this incident; the gap is specifically "
                    "around voice-based social engineering and payment-verification procedures, not physical "
                    "security."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Wait until the next scheduled three-year content refresh cycle to incorporate the new "
                    "threat information"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting years to address a demonstrated, active gap leaves the organization "
                    "exposed to repeat attempts using the same technique in the interim; emerging threats "
                    "identified through incidents should prompt prompt content updates."
                ),
            },
        ],
        "explanation": (
            "Security awareness content must be periodically refreshed to address emerging attack techniques "
            "(such as AI-generated voice deepfakes), especially after a near-miss incident demonstrates the "
            "current material no longer reflects the threats employees actually face."
        ),
    },
    {
        "id": "nd5g-043",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A credit union's own compliance department reviews lending controls quarterly as a self-assessment. "
            "Separately, an independent CPA firm with no ties to the credit union audits its financial statements "
            "annually, and a federal regulator periodically examines the credit union's compliance with lending "
            "regulations. Which pair of terms correctly describes the CPA firm's engagement and the regulator's "
            "engagement, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "External audit (the CPA firm) and regulatory examination (the federal regulator)",
                "correct": True,
                "rationale": (
                    "Correct. An independent third party with no organizational ties performing the audit "
                    "makes it an external audit. A government supervisory body reviewing compliance with "
                    "regulations is a regulatory examination — a distinct process from a standard external audit."
                ),
            },
            {
                "id": "b",
                "text": "Internal audit (the CPA firm) and external audit (the federal regulator)",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal audit refers to an organization's own staff (like the compliance "
                    "department's quarterly self-assessment); the CPA firm is independent and external, not "
                    "internal, and the regulator's review is a regulatory examination, not a standard external "
                    "audit."
                ),
            },
            {
                "id": "c",
                "text": "Regulatory examination (the CPA firm) and internal audit (the federal regulator)",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses both terms — the CPA firm's independent financial audit is an "
                    "external audit, and the regulator's supervisory review is a regulatory examination, not an "
                    "internal audit."
                ),
            },
            {
                "id": "d",
                "text": "External audit (the CPA firm) and internal audit (the federal regulator)",
                "correct": False,
                "rationale": (
                    "Incorrect. The regulator is not part of the credit union's own organization, so its review "
                    "cannot be an internal audit; a government body's compliance review is specifically termed a "
                    "regulatory examination."
                ),
            },
        ],
        "explanation": (
            "Internal audits are performed by an organization's own staff. External audits are performed by "
            "independent third parties with no organizational ties. Regulatory examinations are performed "
            "specifically by government supervisory bodies verifying compliance with applicable regulations."
        ),
    },
    {
        "id": "nd5g-044",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A client engages a penetration testing firm for a short, fixed-duration engagement and, to maximize "
            "coverage within the limited time, provides the testers with full network diagrams, source code "
            "repository access, and credentials for multiple user roles before testing begins. Which type of "
            "penetration test is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A white-box (full-knowledge) test",
                "correct": True,
                "rationale": (
                    "Correct. Providing testers with complete internal knowledge — network diagrams, source "
                    "code access, and credentials — before testing begins is the defining characteristic of a "
                    "white-box test, chosen here specifically to maximize efficiency and coverage within a short "
                    "engagement window."
                ),
            },
            {
                "id": "b",
                "text": "A black-box (zero-knowledge) test",
                "correct": False,
                "rationale": (
                    "Incorrect. A black-box test simulates an external attacker with no prior knowledge of the "
                    "target; the client here deliberately provided extensive internal information, which is the "
                    "opposite approach."
                ),
            },
            {
                "id": "c",
                "text": "A gray-box (partial-knowledge) test",
                "correct": False,
                "rationale": (
                    "Incorrect. Gray-box testing involves limited, partial knowledge (such as only user-level "
                    "credentials); the client provided full diagrams, source code access, and multiple "
                    "role credentials, which goes well beyond a gray-box level of disclosure."
                ),
            },
            {
                "id": "d",
                "text": "A purple team exercise",
                "correct": False,
                "rationale": (
                    "Incorrect. A purple team exercise involves active, real-time collaboration between "
                    "attacking (red) and defending (blue) teams during the engagement; the scenario describes a "
                    "standard penetration test with pre-shared knowledge, not a collaborative red/blue exercise."
                ),
            },
        ],
        "explanation": (
            "White-box (full-knowledge) testing provides testers complete internal information up front, "
            "maximizing thoroughness and efficiency within a limited testing window — distinct from black-box "
            "(no knowledge), gray-box (partial knowledge), and purple team (collaborative) approaches."
        ),
    },
    {
        "id": "nd5g-045",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "Before a penetration test begins against a client's internet-facing infrastructure, the testing firm "
            "insists on obtaining a signed document from an authorized client executive explicitly granting "
            "permission to perform the specific attacks in scope, on the specific dates agreed. What is the "
            "PRIMARY purpose of this document?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It serves as a letter of authorization ('get out of jail free' letter) protecting the "
                    "testers from legal or criminal liability if the authorized testing activity is discovered "
                    "or reported by a third party, such as the client's ISP or law enforcement"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A letter of authorization, signed by someone with the actual authority to grant "
                    "it, is the tester's legal protection — proof that the intrusive activity being performed was "
                    "explicitly sanctioned by the system owner, shielding testers from liability if the activity "
                    "is flagged by outside parties."
                ),
            },
            {
                "id": "b",
                "text": "It defines the specific dollar amount the client will pay for the engagement",
                "correct": False,
                "rationale": (
                    "Incorrect. Pricing terms belong in a statement of work or contract, not in an authorization "
                    "letter, whose purpose is legal protection for the scope and timing of the test itself."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It guarantees the testing firm a minimum uptime commitment for the client's systems during "
                    "the engagement"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Uptime guarantees are unrelated; an authorization letter concerns legal "
                    "permission to test, not the client's own infrastructure availability commitments."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It transfers legal ownership of any vulnerabilities discovered from the client to the "
                    "testing firm"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ownership of discovered vulnerabilities is not a legal concept transferred via "
                    "this document; the letter's function is authorizing the testing activity itself, not "
                    "assigning ownership of findings."
                ),
            },
        ],
        "explanation": (
            "A letter of authorization ('get out of jail free' letter), signed by someone with genuine authority "
            "over the systems in scope, is the critical legal artifact protecting penetration testers from "
            "liability for activity that would otherwise appear malicious if discovered by third parties."
        ),
    },
    {
        "id": "nd5g-046",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "During an authorized, scoped penetration test, the testing team discovers clear evidence of an "
            "active, in-progress compromise by an unrelated, unauthorized threat actor already present on a "
            "system outside the agreed testing scope. Select the TWO actions the testing team should take "
            "IMMEDIATELY."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Immediately halt further interaction with the affected out-of-scope system and avoid any "
                    "additional exploitation or investigation of the unrelated compromise"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The system and the unrelated compromise fall outside the signed rules of "
                    "engagement and authorization; continuing to interact with it exceeds the tester's legal "
                    "authorization and could interfere with evidence or an active incident response."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Notify the client's designated emergency contact, as specified in the rules of engagement, "
                    "without delay"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Rules of engagement typically designate an emergency contact and escalation path "
                    "for exactly this situation; the client must be alerted immediately so its incident response "
                    "process can begin addressing the real, active threat."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Continue investigating and documenting the unauthorized actor's full extent of access to "
                    "gather as much detail as possible before reporting"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Continuing to investigate an out-of-scope, unauthorized compromise exceeds the "
                    "tester's legal authorization under the signed rules of engagement and could interfere with "
                    "evidence needed for the client's own incident response and potential law enforcement "
                    "involvement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Directly notify any third parties or customers who might be affected by the compromise, "
                    "without going through the client"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Notifying outside parties directly is not the tester's role and would likely "
                    "violate the engagement's confidentiality and reporting terms; findings must be reported to "
                    "the client, who is responsible for any required external notifications."
                ),
            },
        ],
        "explanation": (
            "Upon discovering an unrelated, active compromise outside the authorized scope, testers must stop "
            "interacting with that system and immediately escalate to the client's designated emergency contact "
            "per the rules of engagement — not continue investigating beyond scope or notify outside parties "
            "directly."
        ),
    },
]
