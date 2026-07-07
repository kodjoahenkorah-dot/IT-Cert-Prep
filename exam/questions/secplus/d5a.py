"""CompTIA Security+ SY0-701 practice questions — Domain 5 (Security Program
Management and Oversight), file A.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 5 in
``_topic_labels.json``.
"""

QUESTIONS = [
    {
        "id": "nd5a-001",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A risk analyst is quantifying the impact of a ransomware scenario against an e-commerce platform "
            "valued at $500,000 (asset value, AV). Historical incident data and vendor loss reports indicate that "
            "a successful ransomware event typically destroys or renders unusable 40% of the platform's value "
            "(exposure factor, EF). What is the single loss expectancy (SLE) for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$200,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $500,000 x 0.40 = $200,000, the expected loss from a single "
                    "occurrence of the event."
                ),
            },
            {
                "id": "b",
                "text": "$300,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from applying the complement of the exposure factor (60%) instead "
                    "of the stated 40% EF ($500,000 x 0.60), which is not what the scenario describes."
                ),
            },
            {
                "id": "c",
                "text": "$500,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is simply the asset value with the exposure factor ignored entirely. SLE "
                    "must scale AV by the proportion of value actually expected to be lost."
                ),
            },
            {
                "id": "d",
                "text": "$1,250,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from dividing AV by EF ($500,000 / 0.40) rather than multiplying. "
                    "Dividing produces a figure larger than the asset itself, which cannot be a valid SLE."
                ),
            },
        ],
        "explanation": (
            "SLE = Asset Value (AV) x Exposure Factor (EF). Here, $500,000 x 0.40 = $200,000. EF must be "
            "multiplied, not subtracted from 1 and applied, divided into AV, or ignored."
        ),
    },
    {
        "id": "nd5a-002",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A single loss expectancy (SLE) of $150,000 has been calculated for a data center flooding scenario. "
            "Insurance actuarial data indicates this type of flood occurs, on average, once every 5 years at this "
            "location. What is the annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$30,000",
                "correct": True,
                "rationale": (
                    "Correct. ARO = 1 event / 5 years = 0.2. ALE = SLE x ARO = $150,000 x 0.2 = $30,000."
                ),
            },
            {
                "id": "b",
                "text": "$750,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing SLE by ARO ($150,000 / 0.2) instead of multiplying, "
                    "which inflates the figure well beyond the single-loss amount."
                ),
            },
            {
                "id": "c",
                "text": "$150,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats ALE as identical to SLE, ignoring the annualized rate of occurrence "
                    "entirely. ALE must account for how often the event is expected per year."
                ),
            },
            {
                "id": "d",
                "text": "$3,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading 'once every 5 years' as an ARO of 0.02 (as if it "
                    "were once every 50 years) instead of the correct 0.2 (1/5)."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO. 'Once every 5 years' converts to ARO = 1/5 = 0.2. $150,000 x 0.2 = $30,000."
        ),
    },
    {
        "id": "nd5a-003",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "Before mitigation, the ALE for an unpatched VPN concentrator vulnerability is $80,000/year. A "
            "proposed safeguard (annual cost of safeguard, ACS, of $45,000) would reduce the ALE to $20,000/year. "
            "Using cost-benefit analysis of the control, what should the organization conclude?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The safeguard produces a net benefit of $15,000/year ($60,000 ALE reduction minus the "
                    "$45,000 ACS), so it is cost-justified."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Value of the control = (ALE_before - ALE_after) - ACS = ($80,000 - $20,000) - "
                    "$45,000 = $60,000 - $45,000 = $15,000. A positive figure means the safeguard is worth its cost."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The safeguard produces a net benefit of $60,000/year, because the ALE reduction alone "
                    "determines value regardless of the safeguard's cost."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the ALE reduction ($80,000 - $20,000) before subtracting the $45,000 ACS. "
                    "The safeguard's own cost must be netted out to determine whether it is actually worthwhile."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The safeguard costs $25,000 more than the residual $20,000 ALE it leaves behind, producing "
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
                    "The organization saves $35,000/year ($80,000 original ALE minus the $45,000 safeguard "
                    "cost), so the safeguard is justified."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This subtracts ACS from the original ALE but omits the residual $20,000 ALE that "
                    "still remains after the control is applied, understating the true comparison."
                ),
            },
        ],
        "explanation": (
            "Cost-benefit analysis of a safeguard: Value = (ALE before control - ALE after control) - ACS. "
            "($80,000 - $20,000) - $45,000 = $15,000 net benefit, so the control is worth implementing."
        ),
    },
    {
        "id": "nd5a-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A logistics company values a fleet-tracking database at $250,000 (AV). A successful attack against "
            "this database is expected to destroy 60% of its value (EF). Loss history shows this type of attack "
            "occurs once every two years (ARO = 0.5). What is the ALE?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$75,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $250,000 x 0.60 = $150,000. ALE = SLE x ARO = $150,000 x 0.5 = "
                    "$75,000."
                ),
            },
            {
                "id": "b",
                "text": "$150,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the SLE, not the ALE — it stops after AV x EF and never applies the ARO "
                    "of 0.5 to annualize the figure."
                ),
            },
            {
                "id": "c",
                "text": "$125,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from AV x ARO ($250,000 x 0.5), skipping the exposure factor entirely "
                    "rather than first computing SLE from AV and EF."
                ),
            },
            {
                "id": "d",
                "text": "$37,500",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading 'once every two years' as an ARO of 0.25 (as if it "
                    "were once every four years) instead of the correct 0.5."
                ),
            },
        ],
        "explanation": (
            "SLE = AV x EF = $250,000 x 0.60 = $150,000. ALE = SLE x ARO = $150,000 x 0.5 = $75,000. Every "
            "factor (AV, EF, ARO) must be applied, in the correct order, to reach the ALE."
        ),
    },
    {
        "id": "nd5a-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A manufacturing plant's SCADA system has an asset value of $4,000,000. Security engineers estimate "
            "that a successful attack would destroy 5% of the system's value. Records show this type of attack "
            "has occurred twice in the last 8 years. What is the ALE?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$50,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = $4,000,000 x 0.05 = $200,000. ARO = 2 events / 8 years = 0.25. ALE = "
                    "$200,000 x 0.25 = $50,000."
                ),
            },
            {
                "id": "b",
                "text": "$200,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the SLE ($4,000,000 x 0.05), with the annualized rate of occurrence "
                    "never applied to convert it into an ALE."
                ),
            },
            {
                "id": "c",
                "text": "$25,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from counting only one occurrence over 8 years (ARO = 1/8 = 0.125) "
                    "instead of the two occurrences the scenario states, understating the true ARO."
                ),
            },
            {
                "id": "d",
                "text": "$1,000,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from multiplying AV directly by ARO ($4,000,000 x 0.25), skipping the "
                    "exposure factor and the SLE calculation altogether."
                ),
            },
        ],
        "explanation": (
            "SLE = AV x EF = $4,000,000 x 0.05 = $200,000. ARO = 2/8 = 0.25 (twice in 8 years). ALE = SLE x ARO "
            "= $200,000 x 0.25 = $50,000."
        ),
    },
    {
        "id": "nd5a-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A disaster recovery plan states that after a declared disaster, the ERP system must be restored "
            "within 4 hours, and no more than 30 minutes of transaction data may be lost. Which metric describes "
            "the 30-minute figure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Recovery point objective (RPO)",
                "correct": True,
                "rationale": (
                    "Correct. RPO defines the maximum acceptable amount of data loss, measured in time, between "
                    "the last good backup/replication point and the point of failure — exactly the 30-minute "
                    "figure described."
                ),
            },
            {
                "id": "b",
                "text": "Recovery time objective (RTO)",
                "correct": False,
                "rationale": (
                    "Incorrect. RTO is the 4-hour figure — the maximum acceptable time to restore the system "
                    "after an outage — not the amount of data loss tolerated."
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
            "RTO = how long you can be down. RPO = how much data you can afford to lose (measured backward in "
            "time from the failure). MTTR/MTBF are historical reliability metrics, not recovery targets."
        ),
    },
    {
        "id": "nd5a-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A fleet of 20 identical edge servers logged a combined total of 87,600 operating hours over one "
            "year, experiencing 4 failures across the fleet. What metric is being calculated when an analyst "
            "divides 87,600 hours by 4 failures, and what is the resulting value?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MTBF of 21,900 hours",
                "correct": True,
                "rationale": (
                    "Correct. MTBF = total operating time / number of failures = 87,600 / 4 = 21,900 hours, the "
                    "average time the fleet operates between failures."
                ),
            },
            {
                "id": "b",
                "text": "MTTR of 21,900 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. The arithmetic (total time / failures) is correct for MTBF, but MTTR measures "
                    "average time to repair a failure, not average time between failures — the wrong metric name "
                    "for this calculation."
                ),
            },
            {
                "id": "c",
                "text": "MTBF of 87,600 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This uses the total operating time without dividing by the 4 recorded failures, "
                    "which overstates the true average time between failures."
                ),
            },
            {
                "id": "d",
                "text": "MTTR of 4 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This mistakes the failure count itself for a repair-time duration; MTTR requires "
                    "actual repair-time data, none of which was given in the scenario."
                ),
            },
        ],
        "explanation": (
            "MTBF = total operational time / number of failures = 87,600 / 4 = 21,900 hours. MTTR is a distinct "
            "metric measuring average repair duration, not derivable from this data."
        ),
    },
    {
        "id": "nd5a-008",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA sets an RPO of 15 minutes for a financial transaction database. Which backup strategy BEST "
            "satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Continuous data protection (CDP) or near-real-time transaction log replication",
                "correct": True,
                "rationale": (
                    "Correct. Only continuous or near-real-time replication of transaction logs can guarantee "
                    "data loss is bounded to roughly 15 minutes or less in the event of a failure."
                ),
            },
            {
                "id": "b",
                "text": "A full backup taken every night at midnight",
                "correct": False,
                "rationale": (
                    "Incorrect. A nightly full backup could expose the organization to up to 24 hours of data "
                    "loss, far exceeding the 15-minute RPO."
                ),
            },
            {
                "id": "c",
                "text": "A weekly full backup supplemented by daily differential backups",
                "correct": False,
                "rationale": (
                    "Incorrect. Even with daily differentials, up to a full day of transactions could be lost "
                    "between backup windows — nowhere close to a 15-minute RPO."
                ),
            },
            {
                "id": "d",
                "text": "A storage snapshot taken every 4 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. A 4-hour snapshot interval could still lose up to 4 hours of data, well beyond "
                    "the 15-minute tolerance the RPO establishes."
                ),
            },
        ],
        "explanation": (
            "RPO drives backup/replication frequency. A tight 15-minute RPO requires continuous or near-real-time "
            "replication; periodic backups (nightly, weekly+differential, or multi-hour snapshots) cannot meet it."
        ),
    },
    {
        "id": "nd5a-009",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A post-incident metrics review shows that MTTR for critical outages grew from 2 hours to 9 hours "
            "over the past year, while MTBF for the same systems remained essentially constant. Which conclusion "
            "is BEST supported by this data?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The team's ability to detect and restore service after a failure has degraded, even though "
                    "failures are not occurring more often."
                ),
                "correct": True,
                "rationale": (
                    "Correct. MTTR reflects how long it takes to fix a failure once it happens; a rising MTTR "
                    "with unchanged MTBF points squarely at slower detection/response/repair, not a change in "
                    "failure frequency."
                ),
            },
            {
                "id": "b",
                "text": "The system's overall reliability has decreased because failures are happening more often.",
                "correct": False,
                "rationale": (
                    "Incorrect. A stable MTBF specifically indicates failure frequency has not changed; this "
                    "conclusion misinterprets what MTBF measures."
                ),
            },
            {
                "id": "c",
                "text": "The RTO for this system should be lowered to compensate for the change.",
                "correct": False,
                "rationale": (
                    "Incorrect. RTO is a business-defined recovery target, not a lever that fixes a slower repair "
                    "process; lowering a target does not make the team restore service any faster."
                ),
            },
            {
                "id": "d",
                "text": "The RPO must have increased because more data is being lost during each outage.",
                "correct": False,
                "rationale": (
                    "Incorrect. No data-loss information was provided, and RPO is a data-loss tolerance target, "
                    "not something inferred from repair-time trends."
                ),
            },
        ],
        "explanation": (
            "MTTR measures repair speed; MTBF measures failure frequency. A rising MTTR alongside a flat MTBF "
            "isolates the problem to detection/restoration efficiency, not failure rate, RTO, or RPO."
        ),
    },
    {
        "id": "nd5a-010",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two government agencies want to formalize a cooperative arrangement to share threat intelligence. "
            "There is no budget exchange and neither agency wants a legally binding performance obligation — "
            "only a documented statement of mutual intent. Which document BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memorandum of understanding (MOU)",
                "correct": True,
                "rationale": (
                    "Correct. An MOU documents a mutual intention to cooperate without creating a legally "
                    "enforceable, financially binding obligation — exactly the arrangement described."
                ),
            },
            {
                "id": "b",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines enforceable, measurable performance metrics (uptime, response "
                    "time), implying a binding obligation the agencies explicitly want to avoid here."
                ),
            },
            {
                "id": "c",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA is an overarching binding contract that governs the legal terms for future "
                    "paid engagements, not a non-binding statement of cooperative intent between agencies."
                ),
            },
            {
                "id": "d",
                "text": "Business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes a binding business partnership, typically including shared "
                    "liability, roles, and financial terms — far more formal than the intent-only relationship "
                    "described."
                ),
            },
        ],
        "explanation": (
            "MOUs (sometimes MOAs) capture mutual intent to cooperate without the binding, measurable obligations "
            "found in SLAs, MSAs, or BPAs."
        ),
    },
    {
        "id": "nd5a-011",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A firm plans to engage a managed security service provider (MSSP) across multiple projects over "
            "several years. It wants one overarching contract establishing payment terms, liability, and dispute "
            "resolution that individual future statements of work (SOWs) can each reference. Which document "
            "should be established?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Master service agreement (MSA)",
                "correct": True,
                "rationale": (
                    "Correct. An MSA establishes the recurring legal and commercial framework (payment terms, "
                    "liability, dispute resolution) that subsequent SOWs for individual projects can reference "
                    "without renegotiating from scratch."
                ),
            },
            {
                "id": "b",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines specific, measurable performance metrics such as uptime or "
                    "response time — a component that might be attached to individual SOWs, but it is not the "
                    "overarching legal framework itself."
                ),
            },
            {
                "id": "c",
                "text": "Business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes a joint business partnership with shared profit, loss, or "
                    "decision-making authority, not a vendor-services framework for recurring paid engagements."
                ),
            },
            {
                "id": "d",
                "text": "A one-time statement of work (SOW) covering all future projects",
                "correct": False,
                "rationale": (
                    "Incorrect. An SOW defines deliverables and terms for one specific engagement; it is not "
                    "designed to serve as the reusable overarching legal framework the firm wants."
                ),
            },
        ],
        "explanation": (
            "The MSA is the umbrella contract for an ongoing vendor relationship; individual SOWs (which may "
            "incorporate their own SLAs) reference the MSA's standing legal terms."
        ),
    },
    {
        "id": "nd5a-012",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two companies are forming a joint venture to co-develop and jointly sell a new SaaS product, "
            "sharing profits, losses, and decision-making authority for the venture. Which agreement type BEST "
            "formalizes this relationship?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Business partnership agreement (BPA)",
                "correct": True,
                "rationale": (
                    "Correct. A BPA defines the terms of a formal business partnership, including ownership, "
                    "profit/loss sharing, and decision-making authority — precisely what this joint venture needs."
                ),
            },
            {
                "id": "b",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA governs recurring vendor/customer purchasing terms, not an equity-style "
                    "partnership with shared profit and loss."
                ),
            },
            {
                "id": "c",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA only defines measurable performance metrics for a service; it does not "
                    "address partnership structure, profit sharing, or joint decision-making authority."
                ),
            },
            {
                "id": "d",
                "text": "Non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects confidentiality of shared information; it does not establish the "
                    "business terms of a joint venture partnership."
                ),
            },
        ],
        "explanation": (
            "A BPA is the appropriate vehicle for formalizing a joint business relationship with shared equity, "
            "profit/loss, and authority — distinct from purely commercial (MSA) or performance-only (SLA) terms."
        ),
    },
    {
        "id": "nd5a-013",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Select the TWO characteristics that are typically defining features of a service level agreement "
            "(SLA) between a cloud provider and a customer."
        ),
        "options": [
            {
                "id": "a",
                "text": "Defines measurable performance metrics such as uptime percentage and support response times",
                "correct": True,
                "rationale": (
                    "Correct. Quantifiable, enforceable performance commitments (uptime, response time, "
                    "resolution time) are the core content of an SLA."
                ),
            },
            {
                "id": "b",
                "text": "Establishes financial penalties or service credits when performance metrics are not met",
                "correct": True,
                "rationale": (
                    "Correct. SLAs commonly tie missed metrics to remedies such as service credits or penalties, "
                    "giving the performance commitments teeth."
                ),
            },
            {
                "id": "c",
                "text": "Creates a non-binding statement of mutual intent between two government agencies",
                "correct": False,
                "rationale": (
                    "Incorrect. This describes an MOU, not an SLA. SLAs are binding performance contracts, not "
                    "non-binding intent statements."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Establishes an overarching legal framework governing multiple future work orders without "
                    "defining specific performance metrics"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This describes an MSA. An SLA is defined specifically by its measurable "
                    "performance metrics, the opposite of omitting them."
                ),
            },
        ],
        "explanation": (
            "SLAs are distinguished by measurable performance metrics paired with enforceable remedies for "
            "missed targets — unlike the non-binding intent of an MOU or the metric-free legal framework of an MSA."
        ),
    },
    {
        "id": "nd5a-014",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "Before allowing a new SaaS vendor to begin processing customer PII, which action should the security "
            "team perform FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Conduct a vendor risk assessment, including review of the vendor's security certifications "
                    "(e.g., SOC 2) and completed security questionnaire"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Due diligence — assessing the vendor's security posture and certifications before "
                    "any data sharing begins — is the foundational first step in vendor risk management."
                ),
            },
            {
                "id": "b",
                "text": "Require the vendor to sign an SLA guaranteeing 99.99% uptime",
                "correct": False,
                "rationale": (
                    "Incorrect. Uptime commitments do not address the security risk of processing PII, and "
                    "negotiating agreement terms is premature before the underlying risk has even been assessed."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Add the vendor to the approved vendor list and begin data sharing while the risk assessment "
                    "is conducted in parallel"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Sharing sensitive data before due diligence is complete reverses the correct "
                    "order of operations and exposes the organization to unassessed risk."
                ),
            },
            {
                "id": "d",
                "text": "Purchase cyber liability insurance to cover potential losses from the vendor relationship",
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance is a risk-transference option that may follow a risk assessment; it "
                    "does not itself evaluate or reduce the vendor's security risk, and it is not the first step."
                ),
            },
        ],
        "explanation": (
            "Vendor onboarding due diligence — assessing security controls, certifications, and questionnaire "
            "responses — must occur before granting access to sensitive data, not after or in parallel."
        ),
    },
    {
        "id": "nd5a-015",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Vendor risk management",
        "stem": (
            "A security manager wants contractual assurance that the organization can verify a critical vendor's "
            "security controls at any time during the contract term, including on-site inspection. Which "
            "contractual provision provides this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A right-to-audit clause",
                "correct": True,
                "rationale": (
                    "Correct. A right-to-audit clause contractually guarantees the customer's ability to verify "
                    "or inspect the vendor's controls throughout the relationship."
                ),
            },
            {
                "id": "b",
                "text": "A non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects the confidentiality of information exchanged; it grants no right "
                    "to inspect or audit the vendor's controls."
                ),
            },
            {
                "id": "c",
                "text": "A service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines performance metrics like uptime and response time; it does not, "
                    "by itself, grant audit or inspection rights."
                ),
            },
            {
                "id": "d",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding statement of intent and provides no enforceable audit "
                    "rights."
                ),
            },
        ],
        "explanation": (
            "Ongoing verification of a vendor's security posture requires an explicit right-to-audit clause in "
            "the contract, distinct from confidentiality (NDA), performance (SLA), or intent (MOU) provisions."
        ),
    },
    {
        "id": "nd5a-016",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A company completed a thorough security assessment of a critical supplier two years ago and has not "
            "reevaluated the relationship since. Which vendor risk management practice is currently missing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Ongoing/continuous monitoring of the vendor's security posture throughout the relationship "
                    "lifecycle"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Vendor risk changes over time; a one-time assessment must be followed by periodic "
                    "or continuous reassessment for the life of the relationship, which is missing here."
                ),
            },
            {
                "id": "b",
                "text": "A one-time penetration test conducted by the vendor's own internal team",
                "correct": False,
                "rationale": (
                    "Incorrect. A vendor-run internal test is not independent, and being one-time does not "
                    "address the underlying gap, which is the lack of ongoing oversight."
                ),
            },
            {
                "id": "c",
                "text": "A signed non-disclosure agreement (NDA) to formalize confidentiality expectations",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA addresses confidentiality of shared information, not the need to "
                    "reassess a vendor's evolving security posture over time."
                ),
            },
            {
                "id": "d",
                "text": "A right-to-audit clause added retroactively to the existing contract",
                "correct": False,
                "rationale": (
                    "Incorrect. Having the contractual capability to audit is not the same as actually performing "
                    "continuous monitoring; the clause alone does not fill the practice gap described."
                ),
            },
        ],
        "explanation": (
            "Effective vendor risk management is a lifecycle process: initial due diligence must be followed by "
            "continuous or periodic monitoring, not a single point-in-time assessment."
        ),
    },
    {
        "id": "nd5a-017",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "After a risk assessment, leadership determines that the cost of implementing additional encryption "
            "controls for a low-value, low-likelihood risk exceeds the potential loss. They formally document a "
            "decision to take no further action and simply monitor the risk going forward. Which risk management "
            "strategy is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk acceptance",
                "correct": True,
                "rationale": (
                    "Correct. A formally documented decision to take no further action, because the cost of "
                    "additional controls outweighs the benefit, is the definition of risk acceptance."
                ),
            },
            {
                "id": "b",
                "text": "Risk avoidance",
                "correct": False,
                "rationale": (
                    "Incorrect. Avoidance means eliminating the risk by discontinuing the activity or exposure "
                    "entirely; the organization here continues operating and simply monitors the risk."
                ),
            },
            {
                "id": "c",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation means implementing controls to reduce risk; leadership explicitly "
                    "decided not to implement the proposed encryption control."
                ),
            },
            {
                "id": "d",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference shifts the risk to a third party (e.g., via insurance or "
                    "outsourcing); nothing in the scenario shifts the risk elsewhere — it is retained internally."
                ),
            },
        ],
        "explanation": (
            "Risk acceptance is a formal, documented decision to retain a risk as-is, typically when the cost of "
            "further mitigation exceeds the expected benefit."
        ),
    },
    {
        "id": "nd5a-018",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A company migrates workloads to a public cloud IaaS provider under a shared responsibility model, "
            "where the provider secures the physical infrastructure and hypervisor while the company remains "
            "responsible for securing the OS, applications, and data. Which risk management strategy BEST "
            "describes this arrangement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Risk sharing — responsibility for managing the risk is divided between the organization and "
                    "the cloud provider"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Under a shared responsibility model, neither party fully assumes the risk; each "
                    "manages the portion within its control, which is the definition of risk sharing."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Risk transference — the cloud provider assumes full financial and legal liability for any "
                    "security incident"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Transference implies moving essentially the entire risk/liability elsewhere "
                    "(e.g., insurance); the company still retains liability and duties for its layer of the stack."
                ),
            },
            {
                "id": "c",
                "text": "Risk avoidance — the organization eliminates its exposure to infrastructure-layer threats",
                "correct": False,
                "rationale": (
                    "Incorrect. Avoidance means not engaging in the risk-bearing activity at all. Migrating to "
                    "cloud redistributes risk; it does not eliminate the organization's exposure entirely."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Risk acceptance — the organization tolerates residual infrastructure risk without further "
                    "action"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance implies no further action is taken. Here, responsibilities are "
                    "actively divided and actively managed by both parties, not merely tolerated passively."
                ),
            },
        ],
        "explanation": (
            "Cloud shared responsibility models are a textbook example of risk sharing: the risk is divided "
            "between provider and customer rather than fully transferred, avoided, or passively accepted."
        ),
    },
    {
        "id": "nd5a-019",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "Select the TWO scenarios below that represent risk transference (as opposed to acceptance, "
            "avoidance, or mitigation)."
        ),
        "options": [
            {
                "id": "a",
                "text": "Purchasing a cyber liability insurance policy to cover breach-related costs",
                "correct": True,
                "rationale": (
                    "Correct. Insurance is the classic example of transference: the financial impact of the risk "
                    "is shifted to a third-party insurer."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Outsourcing payment card processing to a PCI DSS-compliant third-party processor so card "
                    "data never touches internal systems"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Outsourcing the processing (and much of the associated compliance/security burden) "
                    "to a specialized third party transfers that risk away from the organization."
                ),
            },
            {
                "id": "c",
                "text": "Discontinuing an unprofitable product line because of its associated data-handling risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Eliminating the risk-bearing activity entirely is risk avoidance, not "
                    "transference — no third party assumes the risk."
                ),
            },
            {
                "id": "d",
                "text": "Deploying additional EDR agents to reduce malware dwell time",
                "correct": False,
                "rationale": (
                    "Incorrect. Adding a technical control to reduce the likelihood/impact of an event is risk "
                    "mitigation, not transference."
                ),
            },
        ],
        "explanation": (
            "Transference shifts the financial or operational burden of a risk to a third party — via insurance "
            "or outsourcing — unlike avoidance (eliminating the activity) or mitigation (adding controls)."
        ),
    },
    {
        "id": "nd5a-020",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "The board states that, overall, the organization is generally unwilling to accept any risk that "
            "could cause reputational damage exceeding a 'moderate' rating. For a specific new product launch, "
            "however, the board agrees to accept up to a 'high' rated risk for the first six months post-launch. "
            "What BEST describes the board's general default position and its temporary exception, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Risk appetite (the general 'moderate' position) and risk tolerance (the temporary 'high' "
                    "allowance for the launch)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk appetite is the organization's broad, strategic willingness to accept risk in "
                    "pursuit of objectives. Risk tolerance is the acceptable variation permitted around a "
                    "specific objective or initiative — exactly the temporary launch exception."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Risk tolerance (the general 'moderate' position) and risk appetite (the temporary 'high' "
                    "allowance for the launch)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the terms: the broad organization-wide position is appetite, and "
                    "the narrow, initiative-specific variance is tolerance, not the other way around."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Risk capacity (the general 'moderate' position) and risk appetite (the temporary 'high' "
                    "allowance for the launch)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risk capacity is the objective maximum risk the organization can financially "
                    "bear, not a stated preference; the 'unwilling to accept' language describes a preference "
                    "(appetite), not a hard capacity limit."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Risk tolerance (the general 'moderate' position) and risk capacity (the temporary 'high' "
                    "allowance for the launch)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This mixes both terms incorrectly; neither the broad default nor the launch "
                    "exception describes an objective financial ceiling (capacity)."
                ),
            },
        ],
        "explanation": (
            "Risk appetite is the broad, strategic risk level an organization is generally willing to accept. "
            "Risk tolerance is the narrower, acceptable variation permitted for a specific objective or "
            "initiative. Risk capacity is the objective maximum the organization could financially absorb."
        ),
    },
    {
        "id": "nd5a-021",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A risk register entry for 'unpatched legacy ERP server' lists an inherent risk score of 20 (severe) "
            "before controls. After network segmentation and compensating monitoring controls were implemented, "
            "the entry was updated to show a score of 8 (moderate). What does the value '8' represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Residual risk — the risk remaining after controls have been applied",
                "correct": True,
                "rationale": (
                    "Correct. Residual risk is what remains after mitigating controls are put in place, which is "
                    "exactly the post-control score of 8 in this register entry."
                ),
            },
            {
                "id": "b",
                "text": "Inherent risk — the risk level before any controls are considered",
                "correct": False,
                "rationale": (
                    "Incorrect. The inherent (pre-control) risk is the score of 20 given earlier in the scenario, "
                    "not the updated value of 8."
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
                "text": "Risk exposure — the total possible financial loss from the risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Exposure typically refers to a monetary loss figure (such as ALE), not a "
                    "qualitative risk score like the 8/20 scale used in this register."
                ),
            },
        ],
        "explanation": (
            "A risk register commonly tracks both inherent risk (before controls) and residual risk (after "
            "controls). Here, 20 is inherent and 8 is residual — distinct from appetite (a leadership threshold) "
            "or exposure (a monetary loss figure)."
        ),
    },
    {
        "id": "nd5a-022",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "During a risk register review, an auditor notes that several high-severity risks have no assigned "
            "risk owner. Which issue does this MOST likely create?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Accountability for tracking, treating, and reporting on the risk is unclear, and treatment "
                    "may stall indefinitely"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A risk owner is the person accountable for driving a risk through assessment, "
                    "treatment, and reporting; without one, no one is responsible for ensuring progress."
                ),
            },
            {
                "id": "b",
                "text": "The risk's annualized loss expectancy (ALE) cannot be mathematically calculated",
                "correct": False,
                "rationale": (
                    "Incorrect. ALE calculation depends on AV, EF, and ARO data, not on whether an owner has been "
                    "assigned to the register entry."
                ),
            },
            {
                "id": "c",
                "text": "The risk automatically defaults to a formally 'accepted' status",
                "correct": False,
                "rationale": (
                    "Incorrect. Formal risk acceptance requires a deliberate, documented sign-off decision; "
                    "simply lacking an assigned owner does not equal an intentional acceptance decision."
                ),
            },
            {
                "id": "d",
                "text": "The risk is automatically removed from the register during the next audit cycle",
                "correct": False,
                "rationale": (
                    "Incorrect. Missing ownership is not grounds for removing a risk from the register; risks "
                    "remain tracked until they are resolved, mitigated, or formally accepted."
                ),
            },
        ],
        "explanation": (
            "Every risk register entry needs an assigned owner to maintain accountability; without one, "
            "treatment activities have no clear driver and can stall indefinitely."
        ),
    },
    {
        "id": "nd5a-023",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "One governance document mandates that 'all production databases must be encrypted using AES-256 at "
            "rest.' A separate document provides the exact step-by-step commands and configuration settings for "
            "enabling that encryption on the organization's specific database platform. What are these two "
            "documents called, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard (the AES-256 mandate) and procedure (the step-by-step instructions)",
                "correct": True,
                "rationale": (
                    "Correct. A standard specifies a mandatory, measurable technical requirement (AES-256). A "
                    "procedure gives the mandatory step-by-step instructions for how to implement it."
                ),
            },
            {
                "id": "b",
                "text": "Policy (the AES-256 mandate) and guideline (the step-by-step instructions)",
                "correct": False,
                "rationale": (
                    "Incorrect. A policy is a broad, high-level statement of intent, not a specific technical "
                    "mandate; a guideline is optional/recommended, but the step-by-step instructions here are "
                    "mandatory, matching a procedure instead."
                ),
            },
            {
                "id": "c",
                "text": "Procedure (the AES-256 mandate) and standard (the step-by-step instructions)",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the correct pairing — the specific technical requirement is the "
                    "standard, and the step-by-step instructions are the procedure."
                ),
            },
            {
                "id": "d",
                "text": "Guideline (the AES-256 mandate) and policy (the step-by-step instructions)",
                "correct": False,
                "rationale": (
                    "Incorrect. A guideline implies an optional, recommended practice, but the AES-256 "
                    "requirement is mandatory; a policy is a broad statement of intent, not detailed instructions."
                ),
            },
        ],
        "explanation": (
            "Governance hierarchy: policy (broad intent) -> standard (mandatory, measurable requirement) -> "
            "procedure (mandatory step-by-step instructions) -> guideline (optional recommendation)."
        ),
    },
    {
        "id": "nd5a-024",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "To ensure security investment decisions align with business objectives and regulatory obligations, "
            "and to provide executive-level oversight and accountability for the security program, which "
            "governance body should be established?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A security steering committee composed of senior leadership and department stakeholders",
                "correct": True,
                "rationale": (
                    "Correct. A steering committee provides the cross-functional, executive-level governance "
                    "needed to align security investment with business strategy and regulatory obligations."
                ),
            },
            {
                "id": "b",
                "text": "The security operations center (SOC) analyst team",
                "correct": False,
                "rationale": (
                    "Incorrect. The SOC performs day-to-day operational monitoring and detection; it does not "
                    "provide strategic, executive-level governance oversight."
                ),
            },
            {
                "id": "c",
                "text": "The internal audit function alone",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal audit provides independent assurance and testing of controls, but it "
                    "does not itself make ongoing governance and investment decisions."
                ),
            },
            {
                "id": "d",
                "text": "The change advisory board (CAB)",
                "correct": False,
                "rationale": (
                    "Incorrect. The CAB reviews and approves individual change requests within change management, "
                    "not overall security strategy and investment alignment."
                ),
            },
        ],
        "explanation": (
            "A security steering committee (drawing senior leadership across departments) is the governance "
            "structure responsible for aligning security strategy, investment, and accountability with the "
            "business — distinct from operational (SOC), assurance (audit), or change-specific (CAB) bodies."
        ),
    },
    {
        "id": "nd5a-025",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "An employee is disciplined after using a company laptop to run a personal cryptocurrency mining "
            "operation after hours. Which governance document did the employee MOST likely violate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Acceptable use policy (AUP)",
                "correct": True,
                "rationale": (
                    "Correct. The AUP defines permitted and prohibited uses of company systems; running a "
                    "personal side business on a company laptop is a textbook AUP violation."
                ),
            },
            {
                "id": "b",
                "text": "Data classification policy",
                "correct": False,
                "rationale": (
                    "Incorrect. This policy governs how data is labeled and handled based on sensitivity; it is "
                    "unrelated to unauthorized personal use of company hardware."
                ),
            },
            {
                "id": "c",
                "text": "Change management policy",
                "correct": False,
                "rationale": (
                    "Incorrect. This policy governs how changes to production systems are requested, reviewed, "
                    "and approved, which has no bearing on personal misuse of an issued laptop."
                ),
            },
            {
                "id": "d",
                "text": "Business continuity policy",
                "correct": False,
                "rationale": (
                    "Incorrect. This policy addresses maintaining operations during disruptions, an unrelated "
                    "concern to an individual employee's misuse of a company asset."
                ),
            },
        ],
        "explanation": (
            "The acceptable use policy defines what employees may and may not do with company-provided systems; "
            "unauthorized personal use (like crypto mining) is a classic AUP violation."
        ),
    },
    {
        "id": "nd5a-026",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "An EU resident emails a company demanding that it delete all personal data it holds about them, "
            "since they no longer use the service. Under GDPR, which right is the individual exercising?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Right to erasure ('right to be forgotten')",
                "correct": True,
                "rationale": (
                    "Correct. The right to erasure allows a data subject to request deletion of their personal "
                    "data under certain conditions, matching this request exactly."
                ),
            },
            {
                "id": "b",
                "text": "Right to data portability",
                "correct": False,
                "rationale": (
                    "Incorrect. Portability allows a subject to receive their data in a usable format and "
                    "transfer it elsewhere — it does not involve requesting deletion."
                ),
            },
            {
                "id": "c",
                "text": "Right to rectification",
                "correct": False,
                "rationale": (
                    "Incorrect. Rectification allows correcting inaccurate personal data; the individual here is "
                    "requesting deletion, not correction."
                ),
            },
            {
                "id": "d",
                "text": "Right of access",
                "correct": False,
                "rationale": (
                    "Incorrect. The right of access allows a subject to obtain a copy of the data held about "
                    "them; it does not itself compel deletion."
                ),
            },
        ],
        "explanation": (
            "GDPR's right to erasure ('right to be forgotten') specifically covers requests to delete personal "
            "data, distinct from access, rectification, or portability rights."
        ),
    },
    {
        "id": "nd5a-027",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A multinational healthcare company processes large-scale special category (health) data of EU "
            "citizens. Under GDPR, which role is the organization required to designate to oversee data "
            "protection compliance and serve as a contact point for supervisory authorities?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data Protection Officer (DPO)",
                "correct": True,
                "rationale": (
                    "Correct. GDPR requires designation of a DPO for organizations engaged in large-scale "
                    "processing of special category data, to oversee compliance and liaise with supervisory "
                    "authorities."
                ),
            },
            {
                "id": "b",
                "text": "Data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. The controller is the entity that determines the purposes and means of "
                    "processing — typically the company itself — not the specific statutory compliance-oversight "
                    "role GDPR requires here."
                ),
            },
            {
                "id": "c",
                "text": "Data custodian",
                "correct": False,
                "rationale": (
                    "Incorrect. A custodian handles the day-to-day technical storage and security of data; it is "
                    "not the GDPR-mandated compliance-oversight and regulator-liaison role described."
                ),
            },
            {
                "id": "d",
                "text": "Data processor",
                "correct": False,
                "rationale": (
                    "Incorrect. A processor is a third party that processes data on the controller's behalf, not "
                    "an internally designated compliance-oversight role."
                ),
            },
        ],
        "explanation": (
            "GDPR mandates a Data Protection Officer for organizations conducting large-scale processing of "
            "special category data, distinct from the controller/processor/custodian data-handling roles."
        ),
    },
    {
        "id": "nd5a-028",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "Select the TWO rights that are explicitly granted to data subjects under the GDPR."
        ),
        "options": [
            {
                "id": "a",
                "text": "Right to erasure — the ability to request deletion of personal data under certain conditions",
                "correct": True,
                "rationale": (
                    "Correct. GDPR explicitly grants data subjects a conditional right to have their personal "
                    "data erased."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Right to data portability — the ability to receive personal data in a structured, commonly "
                    "used format and transmit it to another controller"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR explicitly grants data subjects the right to obtain their data in a portable "
                    "format and move it to another provider."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Right to indemnification — guaranteed financial compensation from the controller regardless "
                    "of fault"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR is not a guaranteed no-fault compensation scheme; this is not a right the "
                    "regulation defines."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Right to perpetual storage — guarantees that a controller must retain data indefinitely "
                    "upon request"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR emphasizes data minimization and storage limitation principles — the "
                    "opposite of a right compelling indefinite retention, which does not exist under the "
                    "regulation."
                ),
            },
        ],
        "explanation": (
            "GDPR's core data subject rights include erasure, access, rectification, restriction of processing, "
            "and portability. Fabricated rights like guaranteed no-fault compensation or perpetual storage are "
            "not part of the regulation."
        ),
    },
    {
        "id": "nd5a-029",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A company's own compliance department performs a review of security controls to prepare for an "
            "upcoming regulatory examination. Which type of audit is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Internal audit",
                "correct": True,
                "rationale": (
                    "Correct. An internal audit is conducted by an organization's own staff (here, the internal "
                    "compliance department) to assess controls, often in preparation for external scrutiny."
                ),
            },
            {
                "id": "b",
                "text": "External audit",
                "correct": False,
                "rationale": (
                    "Incorrect. External audits are performed by an independent third-party firm, not the "
                    "company's own internal staff."
                ),
            },
            {
                "id": "c",
                "text": "Regulatory audit",
                "correct": False,
                "rationale": (
                    "Incorrect. A regulatory audit is conducted directly by the regulator or government body "
                    "itself, not by the company's internal compliance department."
                ),
            },
            {
                "id": "d",
                "text": "Penetration test",
                "correct": False,
                "rationale": (
                    "Incorrect. A penetration test is an authorized, simulated attack to find exploitable "
                    "vulnerabilities, not a review of compliance controls."
                ),
            },
        ],
        "explanation": (
            "Internal audits are performed by an organization's own personnel; external audits and regulatory "
            "audits involve independent third parties or the regulator itself, and a pentest is a distinct "
            "activity entirely."
        ),
    },
    {
        "id": "nd5a-030",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A customer needs assurance not just that a SaaS vendor's controls are appropriately designed, but "
            "that they operated effectively over a continuous 6-month period. Which report should the vendor "
            "provide?"
        ),
        "options": [
            {
                "id": "a",
                "text": "SOC 2 Type II report",
                "correct": True,
                "rationale": (
                    "Correct. A SOC 2 Type II report attests to the operating effectiveness of controls over an "
                    "extended period, exactly the assurance the customer requires."
                ),
            },
            {
                "id": "b",
                "text": "SOC 2 Type I report",
                "correct": False,
                "rationale": (
                    "Incorrect. A Type I report only attests to the suitability of control design at a single "
                    "point in time, not their effectiveness over a period of operation."
                ),
            },
            {
                "id": "c",
                "text": "SOC 1 report",
                "correct": False,
                "rationale": (
                    "Incorrect. SOC 1 addresses controls relevant to financial reporting, not the security, "
                    "availability, and confidentiality trust services criteria the customer cares about."
                ),
            },
            {
                "id": "d",
                "text": "A self-assessment questionnaire completed by the vendor",
                "correct": False,
                "rationale": (
                    "Incorrect. A self-attestation lacks the independent third-party verification the customer "
                    "is explicitly seeking."
                ),
            },
        ],
        "explanation": (
            "SOC 2 Type II reports test operating effectiveness of controls over a period (commonly 6-12 "
            "months), unlike Type I (design only, point-in-time), SOC 1 (financial reporting controls), or an "
            "unverified vendor self-assessment."
        ),
    },
    {
        "id": "nd5a-031",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A spreadsheet contains unreleased quarterly earnings figures. Premature disclosure would violate "
            "securities regulations and cause severe financial and legal harm to the company. Which "
            "classification level and access control BEST fit this data?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Restricted/Confidential (the highest sensitivity level), with strict need-to-know access "
                    "and encryption"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Data whose premature disclosure would cause severe financial, legal, and "
                    "regulatory harm warrants the highest classification level and the tightest, need-to-know "
                    "access controls."
                ),
            },
            {
                "id": "b",
                "text": "Internal, with access available to all employees company-wide",
                "correct": False,
                "rationale": (
                    "Incorrect. Company-wide access is far too broad for data whose leak would cause severe "
                    "regulatory and financial harm; the sensitivity here far exceeds a general 'internal' label."
                ),
            },
            {
                "id": "c",
                "text": "Public, since it will eventually be released to shareholders",
                "correct": False,
                "rationale": (
                    "Incorrect. Eventual future publication does not justify treating currently unreleased data "
                    "as public; premature disclosure now is exactly what causes the harm described."
                ),
            },
            {
                "id": "d",
                "text": "Private, with access granted to both the finance and marketing departments",
                "correct": False,
                "rationale": (
                    "Incorrect. Marketing has no legitimate need-to-know for unreleased earnings data; granting "
                    "it access is overly broad despite the otherwise plausible-sounding classification label."
                ),
            },
        ],
        "explanation": (
            "Classification level should match the potential harm from disclosure. Data whose leak would cause "
            "severe regulatory/financial/legal consequences requires the highest classification tier and strict, "
            "need-to-know access — not broad internal, public, or overly inclusive private access."
        ),
    },
    {
        "id": "nd5a-032",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A document originally classified 'Confidential' due to pending litigation is now three years past "
            "the litigation's resolution, and the underlying information has since been referenced in public "
            "court records. What should happen to this document under a well-run data classification program?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It should be reviewed and reclassified (e.g., downgraded to Public/Internal), since the "
                    "original sensitivity rationale no longer applies"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification is a lifecycle process; when the reason for a higher classification "
                    "no longer holds, the data should be reviewed and reclassified appropriately."
                ),
            },
            {
                "id": "b",
                "text": "It must remain Confidential permanently, since classification levels are never changed once assigned",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification schemes require periodic review; treating labels as permanent "
                    "and unchangeable contradicts standard data governance practice."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It should be immediately destroyed per media sanitization procedures, since Confidential "
                    "documents cannot be reclassified"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario calls for reclassification, not destruction, and the underlying "
                    "claim that Confidential documents cannot be reclassified is false."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It should be escalated to Restricted, since litigation-related documents always increase in "
                    "sensitivity over time"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The information's sensitivity has decreased, not increased, since it is now part "
                    "of the public record; this option's underlying premise is backwards for this scenario."
                ),
            },
        ],
        "explanation": (
            "Data classification requires periodic review and reclassification as circumstances change; a "
            "static, permanent label (or automatic escalation/destruction) contradicts sound governance practice."
        ),
    },
    {
        "id": "nd5a-033",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A retail company (Company A) decides what customer data to collect and why (e.g., for marketing "
            "analytics), and hires a cloud analytics vendor (Company B) to process that data strictly according "
            "to Company A's instructions. Under GDPR terminology, what is Company B's role?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data processor — it processes personal data on behalf of, and per the instructions of, the "
                    "controller"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Company B only processes the data according to Company A's instructions, which is "
                    "the defining role of a data processor under GDPR."
                ),
            },
            {
                "id": "b",
                "text": "Data controller — it determines the purposes and means of processing",
                "correct": False,
                "rationale": (
                    "Incorrect. Company A, not Company B, determines the purposes and means of processing; "
                    "Company B simply follows instructions."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Data custodian — it is responsible for the day-to-day physical/technical safeguarding "
                    "within the controller's own environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A custodian is typically an internal role within the controller's own "
                    "organization managing storage systems, not an external, separately contracted vendor "
                    "governed by GDPR's controller/processor framework."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Data owner — it holds ultimate accountability for the classification and business value of "
                    "the data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Company A holds that accountability as the controller; the vendor has no "
                    "ownership stake in or ultimate accountability for the data."
                ),
            },
        ],
        "explanation": (
            "Under GDPR, the entity determining the purposes/means of processing is the controller (Company A); "
            "an entity processing data solely on the controller's instructions is the processor (Company B)."
        ),
    },
    {
        "id": "nd5a-034",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A DBA team is responsible for implementing backups, applying access controls, and maintaining the "
            "technical security of a customer database, per policies set by the business unit that formally "
            "'owns' the data. Which role does the DBA team fulfill?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data custodian — implements and maintains technical/operational controls per the owner's direction",
                "correct": True,
                "rationale": (
                    "Correct. The custodian carries out the technical, day-to-day handling and protection of "
                    "data according to policies set by the data owner — exactly the DBA team's role here."
                ),
            },
            {
                "id": "b",
                "text": "Data owner — has ultimate accountability for the data's classification and business use",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario explicitly states the business unit, not the DBA team, holds that "
                    "ownership and accountability."
                ),
            },
            {
                "id": "c",
                "text": "Data controller — determines the purposes and legal basis for processing",
                "correct": False,
                "rationale": (
                    "Incorrect. Controller is a GDPR-specific role for the party determining processing purposes; "
                    "the DBA team executes technical controls but does not decide why the data is processed."
                ),
            },
            {
                "id": "d",
                "text": "Data processor — a separate external organization processing data on the controller's behalf",
                "correct": False,
                "rationale": (
                    "Incorrect. The DBA team is internal staff acting under the business unit's direction, not a "
                    "separate external processing entity."
                ),
            },
        ],
        "explanation": (
            "The custodian is the internal role implementing technical safeguards (backups, access controls) on "
            "behalf of the data owner, distinct from the owner (accountability), controller (GDPR purpose-setter), "
            "or processor (external third party)."
        ),
    },
    {
        "id": "nd5a-035",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "An organization is decommissioning a batch of failed SSDs that contained highly sensitive data and "
            "will not be resold or reused. Which sanitization method is MOST appropriate and effective for SSDs "
            "specifically, as opposed to traditional magnetic HDDs?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Physical destruction (shredding/disintegration) of the SSD media",
                "correct": True,
                "rationale": (
                    "Correct. Because SSDs use flash memory (not magnetic platters) and wear-leveling can "
                    "prevent software overwrites from reaching every physical cell, physical destruction is the "
                    "most reliable method to guarantee data cannot be recovered."
                ),
            },
            {
                "id": "b",
                "text": "Degaussing using a strong magnetic field",
                "correct": False,
                "rationale": (
                    "Incorrect. Degaussing only erases magnetic storage media (HDDs, tapes); SSD flash memory is "
                    "not magnetic and is unaffected by degaussing."
                ),
            },
            {
                "id": "c",
                "text": "A single-pass software overwrite (wipe) of all addressable sectors",
                "correct": False,
                "rationale": (
                    "Incorrect. SSD wear-leveling and over-provisioning mean a software overwrite of addressable "
                    "sectors may not reach every physical flash cell, potentially leaving recoverable data "
                    "remnants."
                ),
            },
            {
                "id": "d",
                "text": "Reformatting the drive using the quick format option",
                "correct": False,
                "rationale": (
                    "Incorrect. A quick format only clears file system tables/directory structures; the "
                    "underlying data remains largely intact and recoverable with common forensic tools."
                ),
            },
        ],
        "explanation": (
            "SSDs require physical destruction (or verified cryptographic erasure) for reliable sanitization, "
            "since degaussing does not affect flash memory and software wipes may miss cells due to "
            "wear-leveling and over-provisioning."
        ),
    },
    {
        "id": "nd5a-036",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company outsources hard drive shredding to a third-party e-waste vendor. Which artifact should "
            "the company obtain to provide auditable proof that the specific assets were properly sanitized, and "
            "to support future compliance evidence requests?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A certificate of destruction listing asset serial numbers, method used, and date",
                "correct": True,
                "rationale": (
                    "Correct. A certificate of destruction documents exactly which assets were destroyed, how, "
                    "and when, providing the independently verifiable evidence needed for audits and compliance."
                ),
            },
            {
                "id": "b",
                "text": "A signed non-disclosure agreement (NDA) with the vendor",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects the confidentiality of information shared with the vendor, but "
                    "provides no proof that destruction of specific assets actually occurred."
                ),
            },
            {
                "id": "c",
                "text": "A service level agreement (SLA) specifying turnaround time for destruction services",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA sets performance expectations (like turnaround time) for the service; it "
                    "does not itself document that specific assets were destroyed."
                ),
            },
            {
                "id": "d",
                "text": "An entry in the vendor's internal asset inventory system",
                "correct": False,
                "rationale": (
                    "Incorrect. The vendor's own internal records are not an independently provided, auditable "
                    "artifact for the customer; the customer needs its own certificate as compliance evidence."
                ),
            },
        ],
        "explanation": (
            "A certificate of destruction is the standard auditable proof of proper media sanitization, distinct "
            "from confidentiality (NDA), performance (SLA), or the vendor's own internal recordkeeping."
        ),
    },
    {
        "id": "nd5a-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company is terminating its contract with an IaaS provider and wants assurance that data on the "
            "shared physical storage backing its now-deleted virtual disks cannot be recovered by other tenants. "
            "Since the company has no physical access to the underlying drives, what should it rely on?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Contractual/documented assurance (e.g., via a SOC 2 report or contract terms) that the "
                    "provider cryptographically erases or logically sanitizes underlying storage blocks per its "
                    "data destruction procedures"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since the customer cannot physically access shared cloud infrastructure, it must "
                    "rely on the provider's documented, independently attested sanitization procedures and "
                    "contractual commitments."
                ),
            },
            {
                "id": "b",
                "text": "Physically degaussing the drives itself before contract termination",
                "correct": False,
                "rationale": (
                    "Incorrect. A cloud tenant has no physical access to the provider's shared infrastructure, "
                    "making self-performed degaussing impossible."
                ),
            },
            {
                "id": "c",
                "text": "Instructing the provider to perform a quick format of the customer's virtual disks",
                "correct": False,
                "rationale": (
                    "Incorrect. A quick format does not sanitize the underlying physical storage blocks and does "
                    "not address data remanence concerns on shared media."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Relying on the provider's standard data retention policy, since retention and sanitization "
                    "are the same control"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A retention policy governs how long data is kept before deletion; it is a "
                    "distinct control from sanitization/destruction of the underlying media at end-of-life."
                ),
            },
        ],
        "explanation": (
            "In shared cloud infrastructure, a tenant cannot physically sanitize media itself and must instead "
            "rely on the provider's documented and independently attested destruction/sanitization procedures."
        ),
    },
    {
        "id": "nd5a-038",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "Over four quarterly phishing simulations, an organization's click-through rate dropped from 22% to "
            "6%, but the rate at which employees reported the simulated phishing emails to security only rose "
            "from 3% to 5%. What should the security awareness team prioritize next?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Reinforcing training on how and where to report suspicious emails, since reporting behavior "
                    "still lags well behind the improved click-through rate"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A persistently low reporting rate means most employees who avoid clicking still "
                    "aren't actively reporting threats, leaving the organization slow to detect real attacks; "
                    "this gap should be the next focus."
                ),
            },
            {
                "id": "b",
                "text": "Declaring the program complete, since the click-through rate has improved significantly",
                "correct": False,
                "rationale": (
                    "Incorrect. An improved click rate alone does not mean employees can identify and report "
                    "real threats; the stagnant reporting rate is still a significant gap for real incidents."
                ),
            },
            {
                "id": "c",
                "text": "Increasing the frequency of simulated phishing emails without changing training content",
                "correct": False,
                "rationale": (
                    "Incorrect. Simply running more simulations without addressing why employees aren't "
                    "reporting is unlikely to move the specific metric that matters most here."
                ),
            },
            {
                "id": "d",
                "text": "Suspending phishing simulations since the click-through rate is now within acceptable limits",
                "correct": False,
                "rationale": (
                    "Incorrect. Stopping simulations removes both the reinforcement mechanism and the ability to "
                    "measure the still-low reporting rate that needs improvement."
                ),
            },
        ],
        "explanation": (
            "Click-through rate and reporting rate measure different behaviors. A low, stagnant reporting rate "
            "despite an improved click rate indicates the training program should now focus on reinforcing how "
            "and where to report suspicious messages."
        ),
    },
    {
        "id": "nd5a-039",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "An employee notices a coworker copying large volumes of proprietary files to a personal USB drive "
            "shortly after announcing their resignation, but hesitates to report it for fear of damaging the "
            "relationship. Which element of a security awareness program MOST directly addresses this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A well-publicized, non-punitive reporting mechanism (e.g., an anonymous hotline) paired "
                    "with training that normalizes reporting anomalous behavior"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A visible, non-punitive channel combined with training that reduces social "
                    "hesitancy directly targets the employee's fear of reporting a coworker."
                ),
            },
            {
                "id": "b",
                "text": "Mandatory annual security policy acknowledgment (sign-off) forms",
                "correct": False,
                "rationale": (
                    "Incorrect. A signature attesting that a policy was read does not build the confidence or "
                    "provide the mechanism needed to actually report a peer's suspicious behavior."
                ),
            },
            {
                "id": "c",
                "text": "Role-based access control (RBAC) training focused on least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. RBAC/least-privilege training addresses how access is provisioned, not the "
                    "reporting hesitancy and insider-threat awareness gap described in the scenario."
                ),
            },
            {
                "id": "d",
                "text": "A gamified phishing simulation leaderboard",
                "correct": False,
                "rationale": (
                    "Incorrect. Phishing simulations target email-based social engineering awareness, not the "
                    "broader insider-threat reporting culture and hesitancy issue at play here."
                ),
            },
        ],
        "explanation": (
            "Insider-threat awareness requires a clear, non-punitive reporting mechanism and training that "
            "normalizes reporting concerning peer behavior — distinct from policy sign-offs, access-control "
            "training, or phishing-specific exercises."
        ),
    },
    {
        "id": "nd5a-040",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "Select the TWO practices that are MOST effective for building a sustainable security awareness "
            "culture, as opposed to a one-time compliance checkbox activity."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Delivering brief, role-specific microlearning modules on a recurring (e.g., monthly) basis "
                    "rather than a single annual session"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Frequent, targeted reinforcement tailored to job role builds lasting behavior "
                    "change far better than a single yearly training event."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Using real-world, anonymized examples of incidents (including near-misses) from within the "
                    "organization to make training relatable"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Relevant, organization-specific examples increase engagement and retention "
                    "compared to generic, abstract training content."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Requiring all employees to complete the exact same generic training module once per year "
                    "regardless of role"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is precisely the one-size-fits-all, once-a-year checkbox approach the "
                    "question contrasts against a sustainable awareness culture."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Limiting awareness communications to email newsletters sent only during Cybersecurity "
                    "Awareness Month each October"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A once-a-year seasonal push, rather than sustained, recurring reinforcement "
                    "throughout the year, does not build a lasting awareness culture."
                ),
            },
        ],
        "explanation": (
            "Sustainable security awareness relies on frequent, role-specific, relatable reinforcement — not "
            "annual, generic, one-time training events."
        ),
    },
]
