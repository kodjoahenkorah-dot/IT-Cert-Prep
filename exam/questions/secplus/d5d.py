"""CompTIA Security+ SY0-701 practice questions — Domain 5 (Security Program
Management and Oversight), file D.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 5 in
``_topic_labels.json``. Scenarios are brand-new relative to d5a.py, d5b.py,
and d5c.py.
"""

QUESTIONS = [
    {
        "id": "nd5d-001",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A regional credit union's online banking platform is valued at $920,000 (asset value, AV). Forensic "
            "data from a similar account-takeover campaign at a peer institution indicates that a successful "
            "attack typically compromises and renders unusable 40% of the platform's value (exposure factor, EF) "
            "before the fraud team can contain it. What is the single loss expectancy (SLE) for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$368,000",
                "correct": True,
                "rationale": "Correct. SLE = AV x EF = $920,000 x 0.40 = $368,000.",
            },
            {
                "id": "b",
                "text": "$552,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the complement of the exposure factor (60%) instead of the stated "
                    "40% EF ($920,000 x 0.60), which does not match what the scenario describes."
                ),
            },
            {
                "id": "c",
                "text": "$920,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the asset value with the exposure factor ignored entirely. SLE must "
                    "scale AV by the proportion of value actually expected to be lost."
                ),
            },
            {
                "id": "d",
                "text": "$2,300,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from dividing AV by EF ($920,000 / 0.40) rather than multiplying. "
                    "Dividing produces a figure larger than the asset itself, which cannot be a valid SLE."
                ),
            },
        ],
        "explanation": (
            "SLE = Asset Value (AV) x Exposure Factor (EF). Here, $920,000 x 0.40 = $368,000. EF must be "
            "multiplied against AV, not subtracted from 1 and applied, divided into AV, or ignored."
        ),
    },
    {
        "id": "nd5d-002",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A single loss expectancy (SLE) of $54,000 has been calculated for a supply-chain vendor-portal "
            "compromise scenario at a mid-size manufacturer. Historical incident data shows this specific "
            "scenario has occurred 3 times in the past 4 years. What is the annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$40,500",
                "correct": True,
                "rationale": (
                    "Correct. ARO = 3 events / 4 years = 0.75. ALE = SLE x ARO = $54,000 x 0.75 = $40,500."
                ),
            },
            {
                "id": "b",
                "text": "$72,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing SLE by ARO ($54,000 / 0.75) instead of multiplying, "
                    "which inflates the figure well beyond the single-loss amount."
                ),
            },
            {
                "id": "c",
                "text": "$54,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats ALE as identical to SLE, ignoring the annualized rate of occurrence "
                    "(the fact that this occurs three times, not once, per 4-year window)."
                ),
            },
            {
                "id": "d",
                "text": "$13,500",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading the frequency as once every 4 years (ARO = 1/4 = "
                    "0.25) instead of correctly accounting for all three occurrences (ARO = 3/4 = 0.75)."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO. 'Three times in 4 years' converts to ARO = 3/4 = 0.75. $54,000 x 0.75 = $40,500."
        ),
    },
    {
        "id": "nd5d-003",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A telehealth company's patient-scheduling database is valued at $2,400,000 (AV). Security engineers "
            "estimate that a successful attack would destroy 10% of the database's value (EF), and threat "
            "intelligence indicates this type of attack succeeds 4 times per 10 years against comparable "
            "telehealth providers. What is the annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$96,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $2,400,000 x 0.10 = $240,000. ARO = 4 events / 10 years = 0.4. "
                    "ALE = SLE x ARO = $240,000 x 0.4 = $96,000."
                ),
            },
            {
                "id": "b",
                "text": "$240,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the SLE ($2,400,000 x 0.10) with the ARO ignored entirely (effectively "
                    "treated as if ARO = 1, i.e., the event happens every year)."
                ),
            },
            {
                "id": "c",
                "text": "$960,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies ARO directly to the full asset value ($2,400,000 x 0.4) without "
                    "first applying the exposure factor, skipping the SLE step entirely."
                ),
            },
            {
                "id": "d",
                "text": "$9,600",
                "correct": False,
                "rationale": (
                    "Incorrect. This misreads '4 times per 10 years' as an ARO of 0.04 (4%) rather than the "
                    "correct 0.4 (4/10), understating the true frequency by a factor of 10."
                ),
            },
        ],
        "explanation": (
            "SLE = AV x EF = $2,400,000 x 0.10 = $240,000. ARO = 4/10 = 0.4. ALE = SLE x ARO = $240,000 x 0.4 = "
            "$96,000. Both the exposure factor and the annualized rate of occurrence must be applied, in order."
        ),
    },
    {
        "id": "nd5d-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "Before mitigation, the ALE for business-partner API credential-stuffing exposure at a fintech firm "
            "is $210,000/year. A proposed safeguard (adaptive, risk-based authentication, annual cost of "
            "safeguard, ACS, of $70,000) would reduce the ALE to $50,000/year. Using cost-benefit analysis of "
            "the control, what should the organization conclude?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The safeguard produces a net benefit of $90,000/year ($160,000 ALE reduction minus the "
                    "$70,000 ACS), so it is cost-justified."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Value of the control = (ALE_before - ALE_after) - ACS = ($210,000 - $50,000) - "
                    "$70,000 = $160,000 - $70,000 = $90,000. A positive figure means the safeguard is worth its "
                    "cost."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The safeguard produces a net benefit of $160,000/year, because the full ALE reduction "
                    "determines value regardless of the safeguard's cost."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores the $70,000 ACS entirely. Cost-benefit analysis requires "
                    "subtracting the cost of the safeguard from the ALE reduction it produces."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The safeguard produces a net benefit of $140,000/year, calculated as ALE_before minus ACS "
                    "($210,000 - $70,000)."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This subtracts ACS from ALE_before instead of from the ALE reduction "
                    "(ALE_before - ALE_after), producing an inflated and incorrect figure."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The safeguard produces a net benefit of only $20,000/year, because the $70,000 ACS must be "
                    "subtracted from the ALE reduction twice to account for both the before and after states."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. ACS is subtracted from the ALE reduction only once. Double-subtracting the "
                    "safeguard's cost understates the true value of the control."
                ),
            },
        ],
        "explanation": (
            "Value of a control = (ALE_before - ALE_after) - ACS = ($210,000 - $50,000) - $70,000 = $90,000/year "
            "net benefit, making the safeguard cost-justified."
        ),
    },
    {
        "id": "nd5d-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA for a national retailer's point-of-sale (POS) authorization service specifies that after a "
            "declared disruption, the service must be restored within 2 hours, and no more than 5 minutes of "
            "transaction data may be lost. Which pair of metrics does this describe, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "RTO of 2 hours; RPO of 5 minutes",
                "correct": True,
                "rationale": (
                    "Correct. RTO is the maximum acceptable time to restore the service (2 hours); RPO is the "
                    "maximum acceptable amount of data loss, measured backward in time (5 minutes)."
                ),
            },
            {
                "id": "b",
                "text": "RPO of 2 hours; RTO of 5 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. This swaps the two definitions: the 2-hour figure is a restoration-time target "
                    "(RTO), and the 5-minute figure is a data-loss tolerance (RPO), not the reverse."
                ),
            },
            {
                "id": "c",
                "text": "MTTR of 2 hours; MTBF of 5 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. MTTR and MTBF are historical, actual-performance metrics derived from past "
                    "incident data, not forward-looking BIA-defined recovery targets like the ones described "
                    "here."
                ),
            },
            {
                "id": "d",
                "text": "MTD of 2 hours; WRT of 5 minutes",
                "correct": False,
                "rationale": (
                    "Incorrect. The 2-hour figure is explicitly a restoration deadline (RTO), not the broader "
                    "maximum tolerable downtime (MTD), and the 5-minute figure describes data loss, not "
                    "work-recovery time (WRT)."
                ),
            },
        ],
        "explanation": (
            "RTO governs the acceptable downtime duration before restoration; RPO governs the acceptable amount "
            "of data loss. Neither is a historical reliability statistic (MTTR/MTBF) nor the broader MTD/WRT "
            "pairing."
        ),
    },
    {
        "id": "nd5d-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A fleet of 18 identical cold-storage temperature sensors logged a combined total of 157,680 "
            "operating hours over one year, experiencing 6 failures across the fleet. What metric is being "
            "calculated when an analyst divides 157,680 hours by 6 failures, and what is the resulting value?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MTBF of 26,280 hours",
                "correct": True,
                "rationale": (
                    "Correct. MTBF = total operating time / number of failures = 157,680 / 6 = 26,280 hours, the "
                    "average time the fleet operates between failures."
                ),
            },
            {
                "id": "b",
                "text": "MTTR of 26,280 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. The arithmetic (total time / failures) is correct for MTBF, but MTTR measures "
                    "average time to repair a failure, not average time between failures — the wrong metric "
                    "name for this calculation."
                ),
            },
            {
                "id": "c",
                "text": "MTBF of 157,680 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This uses the total operating time without dividing by the 6 recorded failures, "
                    "which overstates the true average time between failures."
                ),
            },
            {
                "id": "d",
                "text": "MTTR of 6 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This mistakes the failure count itself for a repair-time duration; MTTR requires "
                    "actual repair-time data, none of which was given in the scenario."
                ),
            },
        ],
        "explanation": (
            "MTBF = total operational time / number of failures = 157,680 / 6 = 26,280 hours. MTTR is a "
            "distinct metric measuring average repair duration, not derivable from this data."
        ),
    },
    {
        "id": "nd5d-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "Select the TWO statements that correctly describe maximum tolerable downtime (MTD) and work "
            "recovery time (WRT) in a business impact analysis."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "MTD represents the total time a business process can be unavailable before causing "
                    "unacceptable harm, and it encompasses both the technical recovery time (RTO) and the "
                    "additional time needed to fully resume normal operations (WRT)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. MTD = RTO + WRT. It is the outer boundary of tolerable downtime, which must "
                    "accommodate both getting systems back online and fully reintegrating them into normal "
                    "business operations."
                ),
            },
            {
                "id": "b",
                "text": (
                    "WRT is the time needed, after systems are technically restored, to reintegrate data, "
                    "verify functionality, and resume full business operations"
                ),
                "correct": True,
                "rationale": (
                    "Correct. WRT begins where RTO ends — it covers the post-restoration work (data "
                    "reconciliation, validation, cutover) required before the business process is truly back to "
                    "normal."
                ),
            },
            {
                "id": "c",
                "text": "WRT measures the average time between hardware failures for a given system",
                "correct": False,
                "rationale": (
                    "Incorrect. That describes MTBF, a historical reliability statistic, not WRT, which is a "
                    "forward-looking recovery-planning duration."
                ),
            },
            {
                "id": "d",
                "text": (
                    "MTD is fully satisfied as long as the RTO target is met, regardless of any additional "
                    "recovery activities that follow"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Because MTD = RTO + WRT, meeting RTO alone is insufficient if the subsequent "
                    "WRT activities push the total downtime past the MTD boundary."
                ),
            },
        ],
        "explanation": (
            "MTD is the outer limit of tolerable downtime and equals RTO (technical restoration) plus WRT "
            "(post-restoration work needed to fully resume operations). WRT is not a reliability statistic, and "
            "meeting RTO alone does not guarantee MTD is respected."
        ),
    },
    {
        "id": "nd5d-008",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two hospital systems in different states want to exchange de-identified research datasets for a "
            "joint clinical study. No payment will change hands and neither party wants a legally binding "
            "performance commitment — they simply want to document their mutual intent and the general terms of "
            "cooperation. Which agreement type is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Memorandum of understanding (MOU)",
                "correct": True,
                "rationale": (
                    "Correct. An MOU documents mutual intent and general terms of a cooperative relationship "
                    "without creating binding performance obligations or payment terms, matching this scenario."
                ),
            },
            {
                "id": "b",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines measurable performance metrics (uptime, response time) for a "
                    "service relationship, which does not apply to a non-binding research-data cooperation."
                ),
            },
            {
                "id": "c",
                "text": "Business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formally establishes shared equity, profit/loss, and decision-making "
                    "authority in a joint venture, which is far more binding and commercial than what is "
                    "described."
                ),
            },
            {
                "id": "d",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA establishes overarching commercial terms (payment, liability) for repeat "
                    "paid engagements, but this is a one-time, no-payment cooperative research arrangement."
                ),
            },
        ],
        "explanation": (
            "An MOU fits non-binding, no-payment cooperative arrangements documenting mutual intent — exactly "
            "the scenario described, unlike the measurable-performance SLA, equity-sharing BPA, or "
            "recurring-commercial MSA."
        ),
    },
    {
        "id": "nd5d-009",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A company's contract for a third-party fraud-detection API specifies 99.99% uptime, a maximum "
            "average response latency of 200ms, and a maximum of 4 hours between an anomaly being flagged and a "
            "human analyst engaging with it. Which document specifies these measurable operational performance "
            "commitments?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Service level agreement (SLA)",
                "correct": True,
                "rationale": (
                    "Correct. An SLA defines the specific, measurable performance thresholds (uptime, latency, "
                    "response time) a provider commits to, exactly the content described."
                ),
            },
            {
                "id": "b",
                "text": "Memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents general, non-binding intent to cooperate; it does not specify "
                    "quantified, enforceable performance metrics like uptime or latency."
                ),
            },
            {
                "id": "c",
                "text": "Business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA governs equity, profit-sharing, and joint decision-making in a business "
                    "partnership, not technical performance thresholds for a purchased API service."
                ),
            },
            {
                "id": "d",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA sets the overarching legal and commercial framework (liability, payment "
                    "terms) for the relationship; specific measurable performance thresholds like these are "
                    "defined in an SLA, which may be referenced as an exhibit to the MSA rather than standing in "
                    "for it."
                ),
            },
        ],
        "explanation": (
            "Quantified, enforceable performance commitments (uptime, latency, response time) are the defining "
            "content of a service level agreement, distinct from an MOU's non-binding intent, a BPA's equity "
            "terms, or an MSA's overarching commercial framework."
        ),
    },
    {
        "id": "nd5d-010",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two independent renewable-energy companies formally establish a jointly owned entity to build and "
            "operate a shared solar farm, splitting capital investment, profits, losses, and management decision "
            "rights on a 50/50 basis. Which agreement type governs this arrangement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Business partnership agreement (BPA)",
                "correct": True,
                "rationale": (
                    "Correct. A BPA formally defines the terms of a joint venture, including equity split, "
                    "profit/loss sharing, and joint management authority, matching this scenario precisely."
                ),
            },
            {
                "id": "b",
                "text": "Memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding statement of intent; it lacks the enforceable equity, "
                    "profit-sharing, and decision-rights terms a jointly owned operating entity requires."
                ),
            },
            {
                "id": "c",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA governs standalone commercial services engagements between a customer and "
                    "a vendor, not a jointly owned equity venture with shared profits and losses."
                ),
            },
            {
                "id": "d",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines measurable service performance metrics, not equity ownership, "
                    "profit/loss sharing, or joint management authority."
                ),
            },
        ],
        "explanation": (
            "A business partnership agreement formalizes joint ownership, shared profit/loss, and joint "
            "decision-making — the defining features of this joint venture, unlike an MOU, MSA, or SLA."
        ),
    },
    {
        "id": "nd5d-011",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A regional bank's procurement team has selected a new fraud-analytics SaaS vendor to process "
            "transaction data containing customer PII. Before a data processing agreement is finalized and the "
            "vendor is provisioned any access, which action should the security team perform FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Score the vendor through a standardized security risk assessment (e.g., a completed "
                    "security questionnaire and review of an independent audit report such as SOC 2)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Understanding the vendor's actual risk posture through a structured assessment "
                    "must precede both contract negotiation and any provisioning of access to PII."
                ),
            },
            {
                "id": "b",
                "text": "Require the vendor to sign a data processing agreement (DPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A DPA is necessary before processing begins, but its specific control and "
                    "safeguard requirements should be informed by the risk assessment; signing it as the very "
                    "first step commits the relationship before the vendor's actual risk posture is understood."
                ),
            },
            {
                "id": "c",
                "text": "Conduct an unannounced penetration test against the vendor's production environment",
                "correct": False,
                "rationale": (
                    "Incorrect. Testing a vendor's environment without prior authorization and scoping is "
                    "inappropriate and not a valid first step in vendor risk management."
                ),
            },
            {
                "id": "d",
                "text": "Provision API access and monitor the vendor's data handling behavior in production",
                "correct": False,
                "rationale": (
                    "Incorrect. This grants access to live customer PII before any risk evaluation has "
                    "occurred, exposing sensitive data with no assurance of the vendor's controls."
                ),
            },
        ],
        "explanation": (
            "Vendor risk management requires assessing a vendor's security posture before granting access or "
            "finalizing contractual terms — assessment informs the DPA and access decisions, not the reverse."
        ),
    },
    {
        "id": "nd5d-012",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A pharmaceutical company wants contractual assurance that its clinical-trial data-management vendor "
            "will notify it within 24 hours of discovering a security incident affecting the company's data, and "
            "will cooperate with the company's forensic investigation. Which contractual mechanism should be "
            "negotiated into the vendor agreement to obtain this assurance?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A breach/incident notification and cooperation clause with a defined timeframe",
                "correct": True,
                "rationale": (
                    "Correct. This is exactly the obligation described — a specific, enforceable clause "
                    "requiring prompt notification and investigative cooperation upon discovery of an incident."
                ),
            },
            {
                "id": "b",
                "text": "A non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects the confidentiality of shared information but does not obligate "
                    "the vendor to notify the company of incidents or cooperate with an investigation."
                ),
            },
            {
                "id": "c",
                "text": "A right-to-audit clause",
                "correct": False,
                "rationale": (
                    "Incorrect. A right-to-audit clause allows the company to inspect and verify the vendor's "
                    "controls; it does not itself create a proactive breach-notification obligation on the "
                    "vendor's part."
                ),
            },
            {
                "id": "d",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding statement of general intent, too informal to reliably "
                    "enforce a specific, time-bound notification and cooperation obligation for a critical data "
                    "processor."
                ),
            },
        ],
        "explanation": (
            "A dedicated breach-notification-and-cooperation clause, with an explicit timeframe, is the "
            "contractual mechanism that obligates a vendor to promptly disclose and assist with incidents — "
            "distinct from confidentiality (NDA), verification rights (right-to-audit), or non-binding intent "
            "(MOU)."
        ),
    },
    {
        "id": "nd5d-013",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Vendor risk management",
        "stem": (
            "A company's third-party risk program tiers all critical vendors as 'low,' 'medium,' or 'high' risk "
            "based on annual reassessments. A vendor last formally reassessed two years ago still carries a "
            "'low risk' tier, even though the vendor disclosed a breach of its own network six months ago and "
            "has since added a new offshore subcontractor with access to the company's data. Which vendor risk "
            "management deficiency does this MOST reflect?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Failure to trigger an event-driven reassessment when material changes occur, relying "
                    "solely on a fixed calendar-based review cycle"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A mature program re-tiers vendors when a material event occurs (a breach, a new "
                    "subprocessor) rather than waiting for the next scheduled annual review, which this program "
                    "failed to do."
                ),
            },
            {
                "id": "b",
                "text": "Lack of an initial due diligence assessment when the vendor was first onboarded",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario indicates a formal assessment did occur (two years ago); the gap is "
                    "the failure to update the tiering after material changes, not an absent initial assessment."
                ),
            },
            {
                "id": "c",
                "text": "Absence of a right-to-audit clause in the vendor contract",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario indicates an audit-rights gap; the described failure is "
                    "specifically about not updating the risk tier in response to new information."
                ),
            },
            {
                "id": "d",
                "text": "Missing non-disclosure agreement (NDA) with the vendor",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidentiality documentation is unrelated to the described failure to "
                    "re-evaluate risk tiering after a breach disclosure and a new subprocessor were introduced."
                ),
            },
        ],
        "explanation": (
            "Vendor risk tiering must be dynamic, triggered by material events such as a vendor breach or a new "
            "subprocessor, not left static between calendar-based annual reviews."
        ),
    },
    {
        "id": "nd5d-014",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A company identifies a risk in which a legacy fax-to-email gateway could be exploited to expose a "
            "small volume of non-regulated internal memos. The calculated ALE is $1,200/year, while the cheapest "
            "available control would cost $40,000/year to implement. Leadership formally documents a decision to "
            "take no further action on this specific risk and continue routine monitoring. Which risk management "
            "strategy is being applied?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk acceptance",
                "correct": True,
                "rationale": (
                    "Correct. Leadership is knowingly and formally choosing to take no additional action because "
                    "the cost of mitigation ($40,000) far exceeds the potential loss ($1,200), documenting the "
                    "decision — the definition of risk acceptance."
                ),
            },
            {
                "id": "b",
                "text": "Risk avoidance",
                "correct": False,
                "rationale": (
                    "Incorrect. Avoidance means eliminating the activity or exposure entirely (e.g., "
                    "decommissioning the gateway); here, the gateway remains in service with no change."
                ),
            },
            {
                "id": "c",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference shifts financial responsibility to a third party (e.g., via cyber "
                    "insurance); nothing in the scenario indicates the risk is being shifted anywhere."
                ),
            },
            {
                "id": "d",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation involves implementing a control to reduce likelihood or impact; "
                    "leadership explicitly declined to implement the available control."
                ),
            },
        ],
        "explanation": (
            "Formally documenting a decision to take no further action, after weighing cost against loss "
            "exposure, is risk acceptance — distinct from avoidance, transference, or mitigation, none of which "
            "occurred here."
        ),
    },
    {
        "id": "nd5d-015",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Risk management strategies",
        "stem": (
            "After a competitor suffered a $3 million ransomware extortion payout, a company purchases a "
            "$5 million cyber-insurance policy specifically covering ransomware extortion payments and incident "
            "response costs, choosing this over further investment in detection tooling. Which risk management "
            "strategy does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk transference",
                "correct": True,
                "rationale": (
                    "Correct. Purchasing insurance shifts the financial burden of a ransomware event to a third "
                    "party (the insurer), which is the defining characteristic of risk transference."
                ),
            },
            {
                "id": "b",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation reduces the likelihood or impact of an event through controls; "
                    "insurance does not make a ransomware event less likely or less damaging operationally, it "
                    "just shifts who bears the cost."
                ),
            },
            {
                "id": "c",
                "text": "Risk avoidance",
                "correct": False,
                "rationale": (
                    "Incorrect. Avoidance means eliminating the exposure by discontinuing the risky "
                    "activity entirely; the company remains just as exposed to a ransomware attack operationally."
                ),
            },
            {
                "id": "d",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance means taking no action and absorbing any loss directly; here the "
                    "company is actively paying a premium to shift the financial impact elsewhere, not simply "
                    "absorbing it."
                ),
            },
        ],
        "explanation": (
            "Purchasing insurance to shift financial responsibility for a risk to a third party is risk "
            "transference — it does not reduce likelihood/impact (mitigation), eliminate the exposure "
            "(avoidance), or leave the organization to absorb losses unaided (acceptance)."
        ),
    },
    {
        "id": "nd5d-016",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A fintech startup discovers that a planned instant peer-to-peer payment feature would require "
            "real-time anti-money-laundering transaction monitoring whose ongoing cost exceeds the feature's "
            "projected revenue. Leadership cancels the feature entirely rather than launching it in any form. "
            "Which risk management strategy does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk avoidance",
                "correct": True,
                "rationale": (
                    "Correct. Canceling the feature entirely eliminates the associated risk-generating activity "
                    "altogether, rather than reducing, shifting, or absorbing it — the defining trait of "
                    "avoidance."
                ),
            },
            {
                "id": "b",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation would mean launching a scaled-down or partially monitored version of "
                    "the feature with reduced risk; instead, the feature was canceled entirely."
                ),
            },
            {
                "id": "c",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario shifts the financial burden of this risk to a third "
                    "party such as an insurer or partner; the feature and its associated risk simply do not "
                    "launch."
                ),
            },
            {
                "id": "d",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance means proceeding while knowingly absorbing the risk; here leadership "
                    "actively eliminated the exposure by not launching the feature at all."
                ),
            },
        ],
        "explanation": (
            "Eliminating an activity entirely, rather than launching it in a reduced-risk form, transferring the "
            "cost, or knowingly proceeding, is risk avoidance."
        ),
    },
    {
        "id": "nd5d-017",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "The CFO determines that, based on current cash reserves and insurance coverage, the organization "
            "could financially absorb losses of up to $8,000,000 annually without becoming insolvent. Separately, "
            "the board states it prefers to keep total annual risk exposure below $3,000,000, even though more "
            "could technically be absorbed, in order to preserve capital for growth investments. What does the "
            "$8,000,000 figure represent, and how does it differ from the board's $3,000,000 position?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "$8,000,000 is risk capacity, the objective financial ceiling the organization could "
                    "survive; $3,000,000 is risk appetite, the board's chosen, more conservative preference set "
                    "below that ceiling"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk capacity is the objective maximum an organization could financially bear. "
                    "Risk appetite is a deliberately chosen, often more conservative, strategic preference that "
                    "can sit below capacity."
                ),
            },
            {
                "id": "b",
                "text": "$8,000,000 is risk appetite; $3,000,000 is risk capacity",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the definitions: the objective financial survivability ceiling is "
                    "capacity, and the board's chosen preference is appetite, not the other way around."
                ),
            },
            {
                "id": "c",
                "text": "$8,000,000 is risk tolerance; $3,000,000 is risk appetite",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk tolerance is the acceptable variance permitted around a specific stated "
                    "appetite for a given objective, not an absolute, organization-wide financial survivability "
                    "ceiling like the $8,000,000 figure."
                ),
            },
            {
                "id": "d",
                "text": "Both figures represent risk appetite, expressed in two different ways",
                "correct": False,
                "rationale": (
                    "Incorrect. This collapses two distinct concepts; capacity is an objective, calculated "
                    "ceiling, while appetite is a deliberately chosen preference, and the two are not "
                    "interchangeable even when both are expressed in dollars."
                ),
            },
        ],
        "explanation": (
            "Risk capacity is the objective maximum loss an organization could financially bear. Risk appetite "
            "is the strategic, chosen level of risk the organization is willing to pursue, which can — and here "
            "does — sit below capacity."
        ),
    },
    {
        "id": "nd5d-018",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A risk register entry for 'growing SaaS shadow-IT footprint' has an assigned risk owner, a residual "
            "risk score, and a scheduled annual review date, but has no defined key risk indicator (KRI) or "
            "threshold that would trigger re-escalation between scheduled reviews. Which deficiency does this "
            "MOST directly create?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The risk could silently worsen well past acceptable levels without being detected until the "
                    "next scheduled review, delaying response to a materially increased exposure"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Without a KRI and threshold, there is no mechanism to detect and escalate "
                    "worsening conditions between review cycles, so a rapidly growing risk could go unaddressed "
                    "for months."
                ),
            },
            {
                "id": "b",
                "text": "The risk cannot be assigned an inherent risk score without a defined KRI",
                "correct": False,
                "rationale": (
                    "Incorrect. Inherent risk scoring is independent of KRIs; it reflects risk before controls "
                    "are applied and does not require a monitoring indicator to be calculated."
                ),
            },
            {
                "id": "c",
                "text": "The organization cannot document an overall risk appetite without a KRI at the entry level",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk appetite is an organization-wide strategic statement, not something derived "
                    "from an individual register entry's monitoring indicators."
                ),
            },
            {
                "id": "d",
                "text": "The assigned risk owner cannot be held accountable for the risk without a defined KRI",
                "correct": False,
                "rationale": (
                    "Incorrect. Accountability flows from the ownership assignment itself, not from the "
                    "presence of a specific monitoring metric; the owner is still accountable, just without an "
                    "early-warning trigger."
                ),
            },
        ],
        "explanation": (
            "A mature risk register entry should include a KRI and threshold so that material worsening of a "
            "risk triggers escalation immediately, rather than only being caught at the next scheduled review."
        ),
    },
    {
        "id": "nd5d-019",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Risk register & appetite",
        "stem": (
            "Select the TWO statements that correctly distinguish inherent risk from residual risk in a risk "
            "register."
        ),
        "options": [
            {
                "id": "a",
                "text": "Inherent risk reflects the risk level before any controls or mitigations are applied",
                "correct": True,
                "rationale": (
                    "Correct. Inherent risk is the baseline exposure that exists absent any compensating "
                    "controls, mitigations, or safeguards."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Residual risk reflects the risk that remains after existing controls are factored in, and "
                    "is what should be compared against the organization's risk appetite when deciding whether "
                    "further action is needed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Residual risk represents the actual current exposure after controls, making it "
                    "the appropriate figure to evaluate against a stated risk appetite or tolerance threshold."
                ),
            },
            {
                "id": "c",
                "text": "Residual risk is always reduced to zero once any control has been implemented",
                "correct": False,
                "rationale": (
                    "Incorrect. Controls reduce but virtually never eliminate risk entirely; some residual "
                    "exposure almost always remains after mitigation."
                ),
            },
            {
                "id": "d",
                "text": "Inherent risk changes every time a new control is added to the environment",
                "correct": False,
                "rationale": (
                    "Incorrect. Inherent risk is a static baseline representing risk without controls; it is "
                    "residual risk, not inherent risk, that changes as controls are added or removed."
                ),
            },
        ],
        "explanation": (
            "Inherent risk is the pre-control baseline exposure and does not change as controls are added. "
            "Residual risk is what remains after controls and is the figure compared against risk appetite; it "
            "is rarely reduced to zero."
        ),
    },
    {
        "id": "nd5d-020",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "One governance document states, 'All remote employees must use company-issued, MDM-enrolled devices "
            "to access internal systems' — a mandatory, board-ratified rule. A separate document recommends, but "
            "does not require, that remote employees position their home workstation away from windows to "
            "reduce shoulder-surfing risk of sensitive information. What BEST describes the second document?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A guideline",
                "correct": True,
                "rationale": (
                    "Correct. A guideline offers recommended, non-mandatory best practices, exactly matching a "
                    "suggested (not required) workstation-placement recommendation."
                ),
            },
            {
                "id": "b",
                "text": "A standard",
                "correct": False,
                "rationale": (
                    "Incorrect. Standards impose mandatory, specific technical or procedural requirements; this "
                    "document explicitly does not require compliance."
                ),
            },
            {
                "id": "c",
                "text": "A policy",
                "correct": False,
                "rationale": (
                    "Incorrect. Policies are high-level, mandatory management directives (like the first "
                    "document requiring MDM-enrolled devices); this second document is explicitly optional."
                ),
            },
            {
                "id": "d",
                "text": "A procedure",
                "correct": False,
                "rationale": (
                    "Incorrect. Procedures are mandatory, step-by-step instructions for accomplishing a "
                    "required task, not an optional recommendation like this one."
                ),
            },
        ],
        "explanation": (
            "Guidelines are non-mandatory recommended practices, distinct from mandatory policies (high-level "
            "directives), standards (specific mandatory requirements), and procedures (mandatory step-by-step "
            "instructions)."
        ),
    },
    {
        "id": "nd5d-021",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A company's board of directors delegates day-to-day execution of the security program to the CISO "
            "but retains ultimate fiduciary accountability for the organization's overall risk posture. A major "
            "breach occurs due to a known, unpatched vulnerability that the CISO had flagged as needing dedicated "
            "budget for remediation eighteen months earlier — funding the board declined at the time. Who bears "
            "ultimate accountability for the resulting incident?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The board of directors",
                "correct": True,
                "rationale": (
                    "Correct. Ultimate accountability for organizational risk, including the consequences of "
                    "funding decisions that left a known risk unaddressed, cannot be delegated away from the "
                    "board even though the CISO executed operationally and properly escalated the issue."
                ),
            },
            {
                "id": "b",
                "text": "The CISO, because they hold operational responsibility for the security program",
                "correct": False,
                "rationale": (
                    "Incorrect. Operational responsibility is distinct from ultimate accountability, and here "
                    "the CISO fulfilled their duty by identifying the risk and escalating the funding need."
                ),
            },
            {
                "id": "c",
                "text": "The IT department that failed to apply the patch",
                "correct": False,
                "rationale": (
                    "Incorrect. IT's inability to patch was a downstream consequence of the funding decision; "
                    "ultimate accountability for that risk decision sits above the operational IT function."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No single party, since the vulnerability was previously disclosed to the board and became "
                    "a shared decision with no clear accountability"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Accountability does not dissolve simply because a risk decision was made "
                    "collectively; the board, as the accountable governing body, retains it."
                ),
            },
        ],
        "explanation": (
            "Governance accountability cannot be delegated downward: the board retains ultimate accountability "
            "for organizational risk outcomes, even when operational staff performed their duties correctly and "
            "the board itself declined the funding that would have prevented the incident."
        ),
    },
    {
        "id": "nd5d-022",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "During an internal audit, an auditor discovers that the organization's information security policy "
            "was last formally reviewed and re-approved by executive leadership six years ago, despite "
            "significant changes in the regulatory environment, technology stack, and threat landscape since "
            "then. Subordinate procedures beneath the policy have been updated more frequently. Which governance "
            "deficiency does this MOST reflect?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Failure to conduct a periodic policy review and revision cycle",
                "correct": True,
                "rationale": (
                    "Correct. Governance requires that top-level policies themselves be periodically reviewed "
                    "and re-approved on a defined cadence to ensure they remain aligned with the current "
                    "regulatory, technical, and threat environment — not just the procedures beneath them."
                ),
            },
            {
                "id": "b",
                "text": "Failure to obtain original executive sign-off on the policy",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the policy was formally approved; the issue is staleness "
                    "from lack of review, not an absent original approval."
                ),
            },
            {
                "id": "c",
                "text": "The policy is now legally unenforceable against employees",
                "correct": False,
                "rationale": (
                    "Incorrect. An outdated policy generally remains internally enforceable; the concern is "
                    "that it may no longer adequately address current risks, not that it has lost enforceability."
                ),
            },
            {
                "id": "d",
                "text": (
                    "This is acceptable governance practice, since updating subordinate procedures more "
                    "frequently is sufficient on its own"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Updating procedures alone leaves a governance gap; the overarching policy must "
                    "also be periodically reviewed to ensure it still reflects current mandatory direction, "
                    "since procedures derive their authority from the policy."
                ),
            },
        ],
        "explanation": (
            "Mature governance requires periodic review and re-approval of top-level policies on a defined "
            "cadence, independent of how frequently subordinate procedures are updated, so that policy stays "
            "current with the evolving regulatory, technical, and threat landscape."
        ),
    },
    {
        "id": "nd5d-023",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A retailer wants to process EU customers' browsing behavior data to build internal fraud-detection "
            "models, without obtaining separate opt-in consent, arguing the processing is necessary for its "
            "legitimate interests and does not override the data subjects' fundamental rights. Under GDPR, which "
            "lawful basis is the retailer relying on, and what additional step MUST accompany reliance on it?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Legitimate interests; the retailer must conduct and document a legitimate interests "
                    "assessment (LIA) balancing its business need against the impact on individuals' rights and "
                    "freedoms"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Legitimate interests is a valid GDPR lawful basis, but it requires a documented "
                    "balancing test weighing the organization's interest against the impact on data subjects — "
                    "exactly what the retailer must additionally perform."
                ),
            },
            {
                "id": "b",
                "text": "Consent; a simple checkbox at account signup satisfies the requirement",
                "correct": False,
                "rationale": (
                    "Incorrect. The retailer explicitly is not relying on consent; it is invoking legitimate "
                    "interests instead, which has a different requirement (a documented balancing assessment, "
                    "not a consent checkbox)."
                ),
            },
            {
                "id": "c",
                "text": "Contractual necessity; no additional documentation is required",
                "correct": False,
                "rationale": (
                    "Incorrect. This is not framed as processing necessary to perform a contract, and legitimate "
                    "interests reliance specifically requires a documented balancing assessment, not zero "
                    "documentation."
                ),
            },
            {
                "id": "d",
                "text": "Vital interests; the retailer must notify a supervisory authority within 72 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. Vital interests applies to life-threatening situations, not fraud analytics, and "
                    "the 72-hour supervisory notification requirement is a breach-notification obligation, "
                    "unrelated to selecting a lawful basis for routine processing."
                ),
            },
        ],
        "explanation": (
            "Legitimate interests is a valid lawful basis under GDPR but requires a documented balancing "
            "assessment weighing the organization's need against individuals' rights — distinct from consent, "
            "contractual necessity, or vital interests, and unrelated to breach-notification timelines."
        ),
    },
    {
        "id": "nd5d-024",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "An EU resident disputes the accuracy of a credit-risk score a company calculated about them and "
            "formally requests that the company limit further use of the disputed data to storage only — without "
            "deleting it — while the accuracy dispute is investigated. Which GDPR right is being exercised?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Right to restriction of processing",
                "correct": True,
                "rationale": (
                    "Correct. This right allows a data subject to limit an organization to merely storing "
                    "(rather than actively using) their data during a dispute over accuracy, exactly as "
                    "described."
                ),
            },
            {
                "id": "b",
                "text": "Right to erasure",
                "correct": False,
                "rationale": (
                    "Incorrect. The individual explicitly does not want the data deleted; they want its active "
                    "use paused while the dispute is resolved, which is restriction, not erasure."
                ),
            },
            {
                "id": "c",
                "text": "Right to data portability",
                "correct": False,
                "rationale": (
                    "Incorrect. Data portability lets a subject obtain and transfer their data to another "
                    "provider; nothing in the scenario involves transferring data elsewhere."
                ),
            },
            {
                "id": "d",
                "text": "Right to object",
                "correct": False,
                "rationale": (
                    "Incorrect. The right to object is used to stop processing based on legitimate interests or "
                    "direct marketing going forward; it is distinct from the specific, temporary pause during an "
                    "accuracy dispute described here, which is restriction of processing."
                ),
            },
        ],
        "explanation": (
            "The right to restriction of processing lets a data subject require an organization to stop "
            "actively using (but not delete) their data, commonly invoked while contesting its accuracy — "
            "distinct from erasure, portability, or the right to object."
        ),
    },
    {
        "id": "nd5d-025",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "Select the TWO obligations that GDPR places specifically on data CONTROLLERS, as distinguished from "
            "data processors."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Determining the purposes and means of processing and ensuring a valid lawful basis exists "
                    "before processing begins"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Deciding why and how personal data is processed, and establishing the lawful basis "
                    "for it, is the defining obligation of a controller."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Responding to and fulfilling data subjects' rights requests (e.g., access, erasure, "
                    "rectification) as the primary point of accountability"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Controllers are the primary accountable party for honoring data subject rights "
                    "requests, even where a processor handles the underlying data."
                ),
            },
            {
                "id": "c",
                "text": "Processing personal data strictly and only according to the controller's documented instructions",
                "correct": False,
                "rationale": (
                    "Incorrect. That is a processor's obligation toward the controller, not something a "
                    "controller does — the controller issues the instructions, it does not follow someone "
                    "else's."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Notifying the controller without undue delay upon becoming aware of a personal data breach"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the processor's obligation toward the controller; the controller instead "
                    "notifies the relevant supervisory authority and, where required, affected data subjects."
                ),
            },
        ],
        "explanation": (
            "Controllers determine purposes/means of processing and are accountable for data subject rights; "
            "processors follow the controller's instructions and must notify the controller of breaches — these "
            "roles are not interchangeable."
        ),
    },
    {
        "id": "nd5d-026",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A publicly traded company's external financial auditor, as part of the annual SOX compliance "
            "engagement, also tests IT general controls (ITGCs) such as change management and logical access, "
            "issuing an independent opinion used by the company's shareholders and regulators. Which type of "
            "audit is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "External (independent third-party) audit",
                "correct": True,
                "rationale": (
                    "Correct. It is performed by an independent auditor outside the company, for the benefit of "
                    "external stakeholders (shareholders and regulators), the defining trait of an external "
                    "audit."
                ),
            },
            {
                "id": "b",
                "text": "Internal audit",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal audits are performed by the organization's own internal audit function "
                    "for internal management use, not by an independent outside auditor for external "
                    "stakeholders."
                ),
            },
            {
                "id": "c",
                "text": "Self-assessment",
                "correct": False,
                "rationale": (
                    "Incorrect. A self-assessment lacks independence by definition; this engagement is "
                    "explicitly performed by an independent, external auditor."
                ),
            },
            {
                "id": "d",
                "text": "Penetration test",
                "correct": False,
                "rationale": (
                    "Incorrect. Testing ITGCs like change management and logical access through control "
                    "walkthroughs and evidence sampling is an audit activity, not adversarial exploitation of "
                    "vulnerabilities."
                ),
            },
        ],
        "explanation": (
            "An independent auditor testing controls for the benefit of external stakeholders (shareholders, "
            "regulators) is an external audit, distinct from an internal audit, an unindependent self-assessment, "
            "or a penetration test's adversarial exploitation activity."
        ),
    },
    {
        "id": "nd5d-027",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "During a scoped external penetration test, the testing team discovers evidence suggesting a live, "
            "in-progress compromise by an unrelated, unknown third-party threat actor already present on the "
            "target network. Which pre-agreed rules of engagement (ROE) provision should dictate the tester's "
            "next action?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The ROE's emergency-contact and incident-disclosure/escalation provision, defining how and "
                    "to whom the tester must immediately report evidence of unrelated active compromise"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A well-formed ROE includes a defined escalation path (deconfliction) for exactly "
                    "this situation, so the tester reports promptly through the pre-agreed channel rather than "
                    "improvising."
                ),
            },
            {
                "id": "b",
                "text": "The scope-of-work clause defining in-scope IP address ranges",
                "correct": False,
                "rationale": (
                    "Incorrect. Scope defines what may be tested, not the procedure for handling a discovery of "
                    "unrelated active compromise by a third party."
                ),
            },
            {
                "id": "c",
                "text": "The non-disclosure agreement (NDA) governing the engagement",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA governs confidentiality of findings between the tester and client; it "
                    "does not define the obligation or procedure to urgently report a discovered unrelated "
                    "compromise."
                ),
            },
            {
                "id": "d",
                "text": "The authorization letter ('get out of jail free' card) permitting the test",
                "correct": False,
                "rationale": (
                    "Incorrect. This document provides legal protection for the tester while conducting "
                    "authorized testing; it does not define the procedure for reporting an unrelated, "
                    "third-party compromise discovered mid-engagement."
                ),
            },
        ],
        "explanation": (
            "ROE should include a defined escalation/deconfliction procedure for exactly this scenario — "
            "discovering evidence of an unrelated active compromise — separate from scope definitions, "
            "confidentiality terms, or the tester's legal authorization document."
        ),
    },
    {
        "id": "nd5d-028",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A vendor provides a customer with an ISO/IEC 27001 certificate as evidence of its security posture. "
            "The customer's security team wants to know specifically which controls were tested, how they were "
            "tested, and the auditor's detailed findings, rather than just confirmation that a certification "
            "body issued the certificate. Which type of assurance artifact should the customer additionally "
            "request?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A detailed third-party audit report (e.g., the full ISO 27001 audit/surveillance report or "
                    "a SOC 2 Type II report) providing granular control-testing detail and findings"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A certificate alone confirms conformance to a standard but does not itself contain "
                    "the underlying detailed test evidence and findings; a full audit report supplies that "
                    "granularity."
                ),
            },
            {
                "id": "b",
                "text": "A self-attestation questionnaire completed by the vendor",
                "correct": False,
                "rationale": (
                    "Incorrect. A self-attestation lacks any independent verification and provides weaker, not "
                    "stronger, evidence than the certificate the customer already has."
                ),
            },
            {
                "id": "c",
                "text": "A penetration test executive summary only",
                "correct": False,
                "rationale": (
                    "Incorrect. A pentest summary is narrower in scope than a full controls audit and tests "
                    "exploitability of specific systems, not the comprehensive, evidence-based ISMS control "
                    "testing the customer is asking about."
                ),
            },
            {
                "id": "d",
                "text": "A renewed certificate with a later expiration date",
                "correct": False,
                "rationale": (
                    "Incorrect. A newer certificate still does not provide granular control-testing detail; it "
                    "only re-confirms conformance without the underlying evidence the customer wants."
                ),
            },
        ],
        "explanation": (
            "A certification/certificate confirms conformance to a standard but omits detailed testing evidence; "
            "the full audit report (not a self-attestation, pentest summary, or a mere renewed certificate) "
            "provides the granular control-by-control detail requested."
        ),
    },
    {
        "id": "nd5d-029",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "A pharmaceutical company's unpublished Phase III clinical trial results reveal a serious, previously "
            "unknown safety signal. Premature or unauthorized disclosure could trigger a stock trading halt, "
            "regulatory action, and a patient safety recall. Which classification level is MOST appropriate for "
            "this data prior to its scheduled public disclosure?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Restricted",
                "correct": True,
                "rationale": (
                    "Correct. Restricted is reserved for an organization's most sensitive data, where disclosure "
                    "would cause severe financial, legal, regulatory, and safety harm — exactly what this "
                    "unpublished safety signal represents."
                ),
            },
            {
                "id": "b",
                "text": "Confidential",
                "correct": False,
                "rationale": (
                    "Incorrect. Confidential applies to sensitive data causing meaningful but more limited harm "
                    "if disclosed; the severity here (trading halt, regulatory action, patient recall) rises to "
                    "the organization's highest tier, Restricted."
                ),
            },
            {
                "id": "c",
                "text": "Internal",
                "correct": False,
                "rationale": (
                    "Incorrect. Internal classification is for routine, non-sensitive information restricted "
                    "only to employees generally; it grossly understates the severe harm this data's disclosure "
                    "would cause."
                ),
            },
            {
                "id": "d",
                "text": "Public",
                "correct": False,
                "rationale": (
                    "Incorrect. Public is for information with no confidentiality concern; this is precisely the "
                    "opposite of the unpublished, market- and safety-sensitive data described."
                ),
            },
        ],
        "explanation": (
            "Data whose disclosure would cause severe financial, legal, regulatory, and safety harm belongs at "
            "the organization's highest classification tier, Restricted, above Confidential, Internal, or "
            "Public."
        ),
    },
    {
        "id": "nd5d-030",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A network architecture diagram was classified 'Confidential' during an active penetration test "
            "engagement, out of concern that competitors might exploit an unpatched design flaw if the diagram "
            "leaked while remediation was pending. Six months later, every vulnerability depicted has been "
            "remediated and the architecture itself is materially different following a subsequent redesign. A "
            "records-management analyst is deciding whether to reclassify the now-outdated diagram. What should "
            "MOST influence this decision?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Whether the specific risk that justified the original classification still exists; since "
                    "the vulnerabilities are remediated and the diagram is materially outdated, it should be "
                    "reassessed and likely downgraded, because classification reflects current sensitivity, not "
                    "a permanent label"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification is not fixed for the life of a document; it should be periodically "
                    "reassessed against the current risk the content poses, and downgraded when the original "
                    "justification no longer applies."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The diagram must remain Confidential permanently, since classification levels, once "
                    "assigned, can never be lowered"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification levels can and should be reviewed and downgraded when the "
                    "underlying sensitivity or risk that justified the original level no longer applies."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The diagram should be reclassified as Public immediately, since any information more than "
                    "six months old is presumed no longer sensitive"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Age alone does not dictate Public classification; the diagram could still "
                    "warrant Internal or Confidential handling for reasons unrelated to the now-remediated "
                    "vulnerabilities, such as general competitive sensitivity of internal architecture."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Reclassification should be based solely on which department originally created the "
                    "document, regardless of the content's current sensitivity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Authorship or origin does not determine sensitivity; the decision should be "
                    "based on the content's current risk and relevance, not who created it."
                ),
            },
        ],
        "explanation": (
            "Classification should be reassessed against whether the original justifying risk still exists; a "
            "document is not permanently locked at its initial classification, nor should reclassification be "
            "decided by age alone or by document ownership."
        ),
    },
    {
        "id": "nd5d-031",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A newly hired data analyst is building a dataset that merges anonymized website analytics with "
            "third-party purchased marketing segments and is unsure which classification label to apply. Per a "
            "mature data classification program, who SHOULD make the final classification determination for this "
            "dataset?"
        ),
        "options": [
            {
                "id": "a",
                "text": "The designated data owner accountable for this business data domain",
                "correct": True,
                "rationale": (
                    "Correct. Classification decisions require business context and accountability over the "
                    "specific data domain, which is the data owner's role, not the analyst who merely builds the "
                    "dataset."
                ),
            },
            {
                "id": "b",
                "text": "The data custodian/IT team, since they physically store and secure the data",
                "correct": False,
                "rationale": (
                    "Incorrect. Custodians implement technical controls based on a classification that has "
                    "already been assigned; they do not decide the classification level themselves."
                ),
            },
            {
                "id": "c",
                "text": "The analyst herself, since she has the most hands-on familiarity with the dataset's structure",
                "correct": False,
                "rationale": (
                    "Incorrect. Familiarity with a dataset's technical structure is not the same as having the "
                    "business accountability and authority to set its classification level."
                ),
            },
            {
                "id": "d",
                "text": "The compliance department exclusively, without any business input, for regulatory consistency",
                "correct": False,
                "rationale": (
                    "Incorrect. Compliance may set policy floors and provide guidance, but the accountable data "
                    "owner — not compliance acting alone — applies classification for a specific dataset."
                ),
            },
        ],
        "explanation": (
            "Data classification determinations belong to the accountable data owner, who has the business "
            "context and authority — distinct from custodians (who implement controls), the analyst building "
            "the dataset, or compliance acting alone."
        ),
    },
    {
        "id": "nd5d-032",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A university (Institution A) determines that it will collect and analyze student engagement data to "
            "improve course design, and contracts a third-party learning-analytics platform (Vendor B) that "
            "processes this data strictly according to the university's documented specifications and for no "
            "other purpose. Which role does Institution A hold, and which role does Vendor B hold?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Institution A is the controller; Vendor B is the processor",
                "correct": True,
                "rationale": (
                    "Correct. Institution A determines the purposes and means of processing (controller), while "
                    "Vendor B processes data strictly on Institution A's instructions and for no independent "
                    "purpose (processor)."
                ),
            },
            {
                "id": "b",
                "text": "Institution A is the processor; Vendor B is the controller",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the roles: Institution A decides what data to collect and why "
                    "(controller), while Vendor B merely executes processing per those instructions (processor)."
                ),
            },
            {
                "id": "c",
                "text": "Institution A is the data custodian; Vendor B is the data owner",
                "correct": False,
                "rationale": (
                    "Incorrect. Custodian and owner are internal data-governance roles concerned with technical "
                    "implementation and business accountability within a single organization, not the "
                    "controller/processor relationship between two separate organizations described here."
                ),
            },
            {
                "id": "d",
                "text": "Both Institution A and Vendor B are joint controllers",
                "correct": False,
                "rationale": (
                    "Incorrect. Joint controllers jointly determine purposes and means together; here, Vendor B "
                    "has no independent decision-making authority and processes strictly per Institution A's "
                    "instructions, making it a processor, not a joint controller."
                ),
            },
        ],
        "explanation": (
            "The party that determines the purposes and means of processing is the controller (Institution A); "
            "the party processing strictly on that entity's instructions is the processor (Vendor B) — distinct "
            "from the custodian/owner pairing or joint-controller arrangements."
        ),
    },
    {
        "id": "nd5d-033",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A cloud infrastructure team configures encryption, applies patches, and enforces access control "
            "lists on a data warehouse, strictly per security standards and classification requirements set by "
            "the data governance committee and the business's data owners. Which data role does the cloud "
            "infrastructure team hold?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data custodian",
                "correct": True,
                "rationale": (
                    "Correct. The custodian implements the technical security controls (encryption, patching, "
                    "access enforcement) required by classification and policy set by others — exactly the "
                    "team's role here."
                ),
            },
            {
                "id": "b",
                "text": "Data owner",
                "correct": False,
                "rationale": (
                    "Incorrect. The data owner sets policy and classification requirements; this team executes "
                    "technical controls per requirements set by others, which is custodianship, not ownership."
                ),
            },
            {
                "id": "c",
                "text": "Data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. Controller is the GDPR term for the entity that determines the purposes and "
                    "means of processing; this team is executing technical implementation per someone else's "
                    "specifications, not determining why or how data is processed."
                ),
            },
            {
                "id": "d",
                "text": "Data steward",
                "correct": False,
                "rationale": (
                    "Incorrect. A data steward typically manages day-to-day data quality, consistency, and "
                    "business definitions/metadata — a related but distinct role from the technical security "
                    "implementation (encryption, patching, ACLs) described, which belongs to the custodian."
                ),
            },
        ],
        "explanation": (
            "Implementing technical security controls per requirements set by the data owner and governance "
            "committee is the defining function of a data custodian, distinct from the owner (sets policy), the "
            "controller (GDPR purposes/means role), or the steward (data quality/metadata role)."
        ),
    },
    {
        "id": "nd5d-034",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A data processor engaged to handle a controller's customer-support ticket data quietly begins "
            "routing a subset of that data through a new AI summarization sub-vendor, without notifying the "
            "controller or obtaining prior authorization. Which principle of the controller-processor "
            "relationship has been violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Processors must obtain prior authorization from the controller before engaging a "
                    "subprocessor, and must flow down equivalent data-protection obligations to it"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A processor cannot unilaterally introduce a new subprocessor; the controller must "
                    "grant prior (specific or general) authorization, and the subprocessor must be bound to "
                    "equivalent protections."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Processors are free to engage any subprocessor without controller involvement, as long as "
                    "the original contract's terms are otherwise met"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is the opposite of the actual obligation — engaging a subprocessor without "
                    "the controller's prior authorization is itself the violation, regardless of whether other "
                    "contract terms are met."
                ),
            },
            {
                "id": "c",
                "text": "This only matters if the new subprocessor is located outside the country",
                "correct": False,
                "rationale": (
                    "Incorrect. The authorization requirement applies regardless of the subprocessor's location; "
                    "cross-border transfers add additional requirements on top of, not instead of, the "
                    "authorization obligation."
                ),
            },
            {
                "id": "d",
                "text": "Only the data custodian, not the processor, has any obligation regarding subprocessors",
                "correct": False,
                "rationale": (
                    "Incorrect. Data custodian is a distinct, non-regulatory operational role not implicated "
                    "here; the processor itself bears the specific subprocessor-authorization obligation to the "
                    "controller."
                ),
            },
        ],
        "explanation": (
            "Processors must obtain the controller's prior authorization before engaging any subprocessor and "
            "must flow down equivalent data-protection obligations — an obligation that exists regardless of "
            "subprocessor location and is not a custodian's responsibility."
        ),
    },
    {
        "id": "nd5d-035",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A hospital is decommissioning a batch of MRI imaging workstation hard drives that stored PHI. The "
            "drives will be donated to a local community college's IT training program for non-sensitive "
            "coursework use, so they must remain fully functional. Per NIST SP 800-88 guidance, which "
            "sanitization method is MOST appropriate?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Purge",
                "correct": True,
                "rationale": (
                    "Correct. Purge provides higher assurance than Clear, appropriate because the drives are "
                    "leaving organizational control (external donation), while leaving the drives fully "
                    "functional and reusable, unlike Destroy."
                ),
            },
            {
                "id": "b",
                "text": "Clear",
                "correct": False,
                "rationale": (
                    "Incorrect. Clear provides only enough assurance for media that stays within the "
                    "organization's own control for reuse; since the drives are leaving the organization "
                    "entirely via donation, a higher-assurance Purge is required."
                ),
            },
            {
                "id": "c",
                "text": "Destroy",
                "correct": False,
                "rationale": (
                    "Incorrect. Destroy renders drives permanently non-functional, defeating the requirement "
                    "that the donated drives remain usable for the college's coursework."
                ),
            },
            {
                "id": "d",
                "text": "Degauss the drives with a Type I/II degausser",
                "correct": False,
                "rationale": (
                    "Incorrect. Degaussing a hard drive typically also destroys the drive's usability (it "
                    "disrupts the servo tracks needed for the drive to operate), which conflicts with the "
                    "requirement that the drives remain fully functional after sanitization."
                ),
            },
        ],
        "explanation": (
            "Purge is the appropriate NIST SP 800-88 category when media is leaving organizational control but "
            "must remain functional for reuse — insufficient assurance from Clear, but without the "
            "functionality loss of Destroy or degaussing."
        ),
    },
    {
        "id": "nd5d-036",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "An organization ships a locked, tamper-evident container of end-of-life backup tapes containing "
            "financial records to a third-party destruction vendor for shredding. Which practice provides the "
            "STRONGEST assurance that the tapes were not accessed or substituted between pickup and destruction?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A documented, unbroken chain-of-custody record tracking every custody transfer, with "
                    "tamper-evident seal verification at each handoff and witnessed destruction"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Chain of custody specifically tracks and verifies control of the physical media "
                    "throughout transport and destruction, directly addressing the risk of undetected access or "
                    "substitution in transit."
                ),
            },
            {
                "id": "b",
                "text": "A certificate of destruction issued by the vendor after shredding is complete",
                "correct": False,
                "rationale": (
                    "Incorrect. A certificate confirms that destruction occurred, but on its own does not prove "
                    "custody was unbroken or that the tapes weren't accessed or swapped before that destruction "
                    "took place."
                ),
            },
            {
                "id": "c",
                "text": "A vendor's general industry certification (e.g., NAID AAA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A vendor-level certification reflects the vendor's overall program and "
                    "qualifications, not shipment-specific evidence of unbroken custody for this particular "
                    "batch of tapes."
                ),
            },
            {
                "id": "d",
                "text": "A signed non-disclosure agreement (NDA) with the destruction vendor",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA provides confidentiality obligations and legal recourse if data is "
                    "misused, but it does not itself provide physical tracking evidence of custody during "
                    "transport."
                ),
            },
        ],
        "explanation": (
            "Only a documented, verified chain-of-custody record provides in-transit assurance against access "
            "or substitution; a certificate of destruction, a vendor certification, and an NDA each address a "
            "different concern and do not by themselves prove custody was unbroken."
        ),
    },
    {
        "id": "nd5d-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company deletes a cloud virtual machine instance and its attached block-storage volume after a "
            "project concludes, but does not revoke the IAM role and API credentials scoped to that instance, nor "
            "remove the DNS records pointing to its now-released IP address. Three months later, the cloud "
            "provider reassigns the IP address to a different customer's compromised instance, which then "
            "receives authenticated API calls intended for the decommissioned company using the still-valid, "
            "unrevoked credentials. What decommissioning failure MOST directly enabled this exposure?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Failure to revoke or rotate credentials and remove stale DNS records as part of the "
                    "decommissioning process"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Decommissioning must include deprovisioning identity/access artifacts and network "
                    "references, not just deleting the compute and storage resources; the leftover credentials "
                    "and DNS record are exactly what enabled the exposure."
                ),
            },
            {
                "id": "b",
                "text": "Failure to physically destroy the underlying storage media",
                "correct": False,
                "rationale": (
                    "Incorrect. In a shared cloud environment, the customer does not control physical media "
                    "destruction; the exposure mechanism described is at the identity/DNS layer, which is the "
                    "customer's own responsibility."
                ),
            },
            {
                "id": "c",
                "text": "Failure to obtain a certificate of destruction from the cloud provider",
                "correct": False,
                "rationale": (
                    "Incorrect. This is unrelated to the described exposure, which resulted from lingering "
                    "credentials and a stale DNS record, not from a lack of a media-destruction certificate."
                ),
            },
            {
                "id": "d",
                "text": "Failure to classify the VM's data prior to deletion",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification of the data wasn't the missing step here; the gap was leaving "
                    "access artifacts (credentials, DNS) active after the resource itself was deleted."
                ),
            },
        ],
        "explanation": (
            "Cloud asset decommissioning must deprovision identity and network artifacts (credentials, IAM "
            "roles, DNS records) alongside the compute/storage resources themselves; leaving them active creates "
            "exposure when the underlying IP or resource is later reused by someone else."
        ),
    },
    {
        "id": "nd5d-038",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "An organization's standard annual security awareness training is completed by 100% of staff, "
            "including the executive team. A recent red-team engagement, however, successfully compromised two "
            "C-suite executives via a highly personalized vishing (voice phishing) call impersonating the IT help "
            "desk and requesting approval of an unexpected MFA push notification. Which training gap MOST likely "
            "contributed to this outcome?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Lack of role-based, targeted training for high-value targets covering vishing tactics and "
                    "MFA fatigue/push-bombing, beyond the generic annual baseline"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The generic annual training was completed but did not address the specific "
                    "tactic (vishing combined with MFA push-bombing) or the specific high-value audience "
                    "(executives) that was actually targeted and exploited."
                ),
            },
            {
                "id": "b",
                "text": "The organization failed to require executives to complete annual training at all",
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states 100% of staff, including executives, completed the "
                    "training; completion is not the gap here."
                ),
            },
            {
                "id": "c",
                "text": "The organization should eliminate MFA for executives to reduce phishing risk",
                "correct": False,
                "rationale": (
                    "Incorrect. Removing MFA would increase, not decrease, risk; it does not address the "
                    "underlying training gap and is a dangerous overcorrection."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The organization needs to increase the frequency of the same generic training from annual "
                    "to monthly"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. More frequent repetitions of the same generic, non-targeted content would not "
                    "address the specific tactic or specific high-value audience that was actually exploited."
                ),
            },
        ],
        "explanation": (
            "Generic, one-size-fits-all annual training does not adequately prepare high-value targets like "
            "executives against tailored social-engineering tactics such as vishing and MFA push-bombing; "
            "role-based, threat-specific training is needed for that audience."
        ),
    },
    {
        "id": "nd5d-039",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "A security team wants to redesign its phishing-simulation program to increase the reporting rate "
            "without relying on punitive measures against employees who click. Which approach BEST supports this "
            "goal?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Publicly and positively recognizing employees who correctly report simulated (and real) "
                    "phishing emails, such as through a leaderboard or small rewards"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Positive reinforcement for the desired behavior (reporting) builds a supportive "
                    "reporting culture and directly increases reporting rates without relying on punishment."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Requiring employees who click a simulated phishing email to attend a mandatory disciplinary "
                    "meeting with HR"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This is a punitive approach that discourages honest reporting out of fear, "
                    "directly contradicting the stated goal of avoiding punitive measures."
                ),
            },
            {
                "id": "c",
                "text": "Reducing the frequency of phishing simulations so employees encounter them less often",
                "correct": False,
                "rationale": (
                    "Incorrect. Fewer simulations give employees fewer opportunities to practice and build the "
                    "reporting habit, working against the goal of increasing reporting rate."
                ),
            },
            {
                "id": "d",
                "text": "Removing the 'report phishing' button from the email client to simplify the interface",
                "correct": False,
                "rationale": (
                    "Incorrect. This would eliminate the very mechanism needed to measure and increase reporting "
                    "rate, directly undermining the stated goal."
                ),
            },
        ],
        "explanation": (
            "Positive reinforcement for reporting behavior — rather than punishment for clicking, reduced "
            "simulation frequency, or removing the reporting mechanism — builds a supportive culture that "
            "increases genuine reporting rates."
        ),
    },
    {
        "id": "nd5d-040",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "Select the TWO practices that reflect a MATURE security awareness program's use of simulated "
            "phishing data, as opposed to treating click rate alone as a punitive scorecard."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Using simulation results to identify specific departments or roles needing additional "
                    "targeted training, rather than solely to rank or punish individuals"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Aggregating results to target training investment where it is most needed is a "
                    "constructive, program-improvement use of simulation data."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Tracking the trend in reporting rate alongside click rate, since a rising reporting rate "
                    "reflects improved vigilance even if click rate has plateaued"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Reporting rate captures active, positive behavior change and provides a fuller "
                    "picture of program effectiveness than click rate alone."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Publicly ranking individual employees from most to least clicks and tying the ranking to "
                    "compensation or performance reviews"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Punitive, individually identifying use of simulation data undermines "
                    "psychological safety and discourages honest reporting, the opposite of a mature program's "
                    "goal."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Using click-through rate as the sole KPI reported to the board, since it is the simplest "
                    "metric to explain"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Relying on a single, overly simplistic metric fails to capture the fuller "
                    "behavioral picture; mature programs report blended metrics, including reporting rate and "
                    "targeted-training outcomes."
                ),
            },
        ],
        "explanation": (
            "Mature awareness programs use simulation data constructively — targeting training and tracking "
            "reporting-rate trends — rather than punitively ranking individuals or relying on click rate as the "
            "sole board-level KPI."
        ),
    },
]
