"""CompTIA Security+ SY0-701 practice questions — Domain 5 (Security Program
Management and Oversight), file B.

40 scenario-driven questions (36 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 5 in
``_topic_labels.json``. All scenarios are distinct from d5a.py.
"""

QUESTIONS = [
    {
        "id": "nd5b-001",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A hospital risk analyst is quantifying exposure for a ransomware scenario against the patient "
            "records database, valued at $800,000 (asset value, AV). Loss data from comparable healthcare "
            "breaches indicates that a successful ransomware event against this class of system typically "
            "renders 25% of the database's value unusable due to corruption and forensic quarantine (exposure "
            "factor, EF). What is the single loss expectancy (SLE) for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$200,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $800,000 x 0.25 = $200,000, the expected loss from one occurrence "
                    "of the event."
                ),
            },
            {
                "id": "b",
                "text": "$600,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the complement of the exposure factor (75%) instead of the stated "
                    "25% EF ($800,000 x 0.75), which is not what the scenario describes."
                ),
            },
            {
                "id": "c",
                "text": "$800,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the asset value with the exposure factor ignored entirely. SLE must "
                    "scale AV by the proportion of value actually expected to be lost."
                ),
            },
            {
                "id": "d",
                "text": "$3,200,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from dividing AV by EF ($800,000 / 0.25) rather than multiplying, "
                    "producing a figure far larger than the asset itself, which cannot be a valid SLE."
                ),
            },
        ],
        "explanation": (
            "SLE = Asset Value (AV) x Exposure Factor (EF). Here, $800,000 x 0.25 = $200,000. EF must be "
            "multiplied against AV directly, not complemented, ignored, or divided into AV."
        ),
    },
    {
        "id": "nd5b-002",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A single loss expectancy (SLE) of $18,000 has been calculated for a point-of-sale card-skimming "
            "incident at a regional retail chain. Fraud analytics show this specific type of incident occurs, "
            "on average, 3 times per year across the chain's locations. What is the annualized loss expectancy "
            "(ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$54,000",
                "correct": True,
                "rationale": (
                    "Correct. ARO = 3 (three occurrences per year). ALE = SLE x ARO = $18,000 x 3 = $54,000."
                ),
            },
            {
                "id": "b",
                "text": "$6,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing SLE by ARO ($18,000 / 3) instead of multiplying, "
                    "which understates the annualized figure well below the single-loss amount."
                ),
            },
            {
                "id": "c",
                "text": "$18,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats ALE as identical to SLE, ignoring the annualized rate of occurrence "
                    "entirely. ALE must account for how often the event is expected per year."
                ),
            },
            {
                "id": "d",
                "text": "$36,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from counting only 2 of the 3 annual occurrences ($18,000 x 2) "
                    "instead of the full ARO of 3 the scenario states."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO. With an SLE of $18,000 and an ARO of 3 (3 occurrences/year), ALE = $18,000 x 3 = "
            "$54,000. Unlike an ARO below 1, an ARO greater than 1 must still simply be multiplied against SLE."
        ),
    },
    {
        "id": "nd5b-003",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "Before mitigation, the ALE for a phishing-driven business email compromise (BEC) exposure is "
            "$120,000/year. A proposed initiative combining security awareness training with DMARC enforcement "
            "(annual cost of safeguard, ACS, of $30,000) is projected to reduce the ALE to $45,000/year. Using "
            "cost-benefit analysis of the control, what should the organization conclude?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The safeguard produces a net benefit of $45,000/year ($75,000 ALE reduction minus the "
                    "$30,000 ACS), so it is cost-justified."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Value of the control = (ALE_before - ALE_after) - ACS = ($120,000 - $45,000) - "
                    "$30,000 = $75,000 - $30,000 = $45,000. A positive figure means the safeguard is worth its "
                    "cost."
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
                    "Incorrect. This is the ALE reduction ($120,000 - $45,000) before subtracting the $30,000 "
                    "ACS. The safeguard's own cost must be netted out to determine whether it is actually "
                    "worthwhile."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The safeguard's $30,000 cost is less than the residual $45,000 ALE it leaves behind, "
                    "producing net savings of $15,000/year."
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
                    "The organization saves $90,000/year ($120,000 original ALE minus the $30,000 safeguard "
                    "cost), so the safeguard is justified."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This subtracts ACS from the original ALE but omits the residual $45,000 ALE that "
                    "still remains after the control is applied, understating the true comparison."
                ),
            },
        ],
        "explanation": (
            "Cost-benefit analysis of a safeguard: Value = (ALE before control - ALE after control) - ACS. "
            "($120,000 - $45,000) - $30,000 = $45,000 net benefit, so the control is worth implementing."
        ),
    },
    {
        "id": "nd5b-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A university's ALE for compromised student financial-aid records is $70,000/year prior to any new "
            "control. Two competing safeguards are proposed. Safeguard A (a multifactor authentication rollout) "
            "has an ACS of $15,000 and would reduce the ALE to $25,000/year. Safeguard B (a managed detection "
            "and response contract) has an ACS of $40,000 and would reduce the ALE to $5,000/year. Based on "
            "cost-benefit analysis, which safeguard should the university select?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Safeguard A, because it produces a higher net benefit ($30,000/year) than Safeguard B "
                    "($25,000/year), even though Safeguard B leaves a lower residual ALE."
                ),
                "correct": True,
                "rationale": (
                    "Correct. Value_A = ($70,000 - $25,000) - $15,000 = $45,000 - $15,000 = $30,000. Value_B = "
                    "($70,000 - $5,000) - $40,000 = $65,000 - $40,000 = $25,000. Safeguard A wins on net "
                    "cost-benefit despite Safeguard B's lower residual risk."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Safeguard B, because it reduces the ALE further, to $5,000, versus Safeguard A's $25,000."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Focusing only on the lowest residual ALE ignores each safeguard's cost; once ACS "
                    "is netted out, Safeguard B's net benefit ($25,000) is actually lower than Safeguard A's "
                    "($30,000)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Safeguard B, because its higher ACS of $40,000 signals a more robust, enterprise-grade "
                    "control."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A control's cost is not a proxy for its value; cost-benefit analysis requires "
                    "comparing the net benefit each option produces, and Safeguard B's net benefit is lower."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Both are equally justified, since each safeguard reduces the ALE by more than its own ACS."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While both reduce ALE by more than their cost, their net benefits differ "
                    "($30,000 for A versus $25,000 for B), so they are not equally justified — A is the better "
                    "choice."
                ),
            },
        ],
        "explanation": (
            "When comparing competing safeguards, net benefit — (ALE reduction) - ACS — determines the best "
            "choice, not the lowest residual ALE or the highest safeguard cost alone. Here, Safeguard A's "
            "$30,000 net benefit exceeds Safeguard B's $25,000."
        ),
    },
    {
        "id": "nd5b-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA determines that if the claims-processing system for an insurance carrier is unavailable for "
            "more than 10 hours, regulatory penalties and irrecoverable customer attrition make the outage "
            "catastrophic to the business — the maximum tolerable downtime (MTD) is 10 hours. When setting the "
            "recovery time objective (RTO) for this system, which approach is BEST?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Set the RTO below the MTD (e.g., 6-7 hours) to leave a safety margin for detection, "
                    "decision-making, and recovery execution before the catastrophic threshold is reached."
                ),
                "correct": True,
                "rationale": (
                    "Correct. MTD is the absolute outer limit; RTO is the operational recovery target and should "
                    "always be set with margin below the MTD so recovery completes before the catastrophic "
                    "threshold is reached."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Set the RTO exactly equal to the MTD (10 hours), since that maximizes the allowable "
                    "recovery window."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Setting RTO equal to MTD leaves zero margin for delays in detection or "
                    "decision-making, risking breach of the MTD if anything in the recovery process slips."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Set the RTO higher than the MTD (e.g., 12 hours), since a longer target gives the recovery "
                    "team more realistic time to work."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An RTO exceeding the MTD directly violates the purpose of the MTD as the "
                    "business's absolute outer boundary for tolerable downtime."
                ),
            },
            {
                "id": "d",
                "text": (
                    "MTD and RTO are unrelated figures, so the RTO should be derived solely from the RPO."
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. RTO and MTD are directly related recovery-time concepts; RPO instead governs "
                    "acceptable data loss and has no bearing on how RTO relates to MTD."
                ),
            },
        ],
        "explanation": (
            "MTD is the outer limit beyond which an outage becomes catastrophic. RTO is the planned recovery "
            "target and must always be set with a safety margin below MTD, never equal to or beyond it."
        ),
    },
    {
        "id": "nd5b-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A fleet of 12 identical industrial sensors logged a combined total of 52,560 operating hours over "
            "one year, experiencing 6 failures across the fleet. What metric is being calculated when an analyst "
            "divides 52,560 hours by 6 failures, and what is the resulting value?"
        ),
        "options": [
            {
                "id": "a",
                "text": "MTBF of 8,760 hours",
                "correct": True,
                "rationale": (
                    "Correct. MTBF = total operating time / number of failures = 52,560 / 6 = 8,760 hours, the "
                    "average time the fleet operates between failures."
                ),
            },
            {
                "id": "b",
                "text": "MTBF of 52,560 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This uses the total operating time without dividing by the 6 recorded failures, "
                    "which overstates the true average time between failures."
                ),
            },
            {
                "id": "c",
                "text": "MTTR of 8,760 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. The arithmetic (total time / failures) is correct for MTBF, but MTTR measures "
                    "average time to repair a failure, not average time between failures — the wrong metric name "
                    "for this calculation."
                ),
            },
            {
                "id": "d",
                "text": "MTBF of 6 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This mistakes the failure count itself for the answer, rather than actually "
                    "dividing the total operating hours by that count."
                ),
            },
        ],
        "explanation": (
            "MTBF = total operational time / number of failures = 52,560 / 6 = 8,760 hours. MTTR is a distinct "
            "metric measuring average repair duration, not derivable from this data."
        ),
    },
    {
        "id": "nd5b-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A BIA sets an RTO of 15 minutes for a stock exchange's order-matching engine. Which disaster "
            "recovery approach BEST satisfies this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "An active-active hot site architecture with automated failover and real-time state "
                    "replication between sites"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Only an automated, active-active hot site with real-time replication can restore "
                    "service within roughly 15 minutes; anything requiring manual intervention cannot reliably "
                    "meet such a tight RTO."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A warm site with pre-configured but powered-down servers that must be manually started and "
                    "configured during a disaster"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Manually starting and configuring servers, even if pre-configured, typically "
                    "takes well beyond 15 minutes, failing to meet the RTO."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A cold site with contracted space and no pre-installed equipment, activated only after a "
                    "disaster is declared"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Procuring and installing equipment at a cold site can take days, far exceeding a "
                    "15-minute RTO."
                ),
            },
            {
                "id": "d",
                "text": "Nightly replication to a secondary data center with a 4-hour manual cutover runbook",
                "correct": False,
                "rationale": (
                    "Incorrect. A 4-hour manual cutover process far exceeds the 15-minute RTO, regardless of how "
                    "current the replicated data is."
                ),
            },
        ],
        "explanation": (
            "RTO drives site-tier and failover architecture selection. An extremely tight 15-minute RTO requires "
            "an automated active-active hot site; warm sites, cold sites, and manual cutover runbooks cannot "
            "meet it."
        ),
    },
    {
        "id": "nd5b-008",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two competing manufacturing firms are exploring a potential merger and need to exchange proprietary "
            "product roadmaps, financials, and trade secrets during due diligence. Neither firm is yet committing "
            "to any ongoing service relationship or joint operations — they only need a binding commitment that "
            "shared information will not be disclosed to third parties. Which document BEST fits this need?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Non-disclosure agreement (NDA)",
                "correct": True,
                "rationale": (
                    "Correct. An NDA is specifically designed to create a binding confidentiality obligation "
                    "over shared sensitive information, exactly what this due-diligence exchange requires."
                ),
            },
            {
                "id": "b",
                "text": "Memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents mutual intent to cooperate and is typically non-binding; it is "
                    "not primarily a confidentiality-protection mechanism for sensitive due-diligence data."
                ),
            },
            {
                "id": "c",
                "text": "Business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes an actual joint business partnership with shared profit and "
                    "loss, which is premature at the due-diligence stage described here."
                ),
            },
            {
                "id": "d",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA governs recurring paid vendor engagements, not confidential information "
                    "sharing between two independent firms exploring a merger."
                ),
            },
        ],
        "explanation": (
            "An NDA is the correct instrument for protecting confidentiality of exchanged sensitive information, "
            "distinct from the non-binding intent of an MOU, the equity-sharing structure of a BPA, or the "
            "vendor-services framework of an MSA."
        ),
    },
    {
        "id": "nd5b-009",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A company's contracted colocation provider guarantees 99.95% monthly uptime under a signed SLA, "
            "with financial service credits owed for shortfalls. This month, the provider's actual uptime "
            "measured 99.6%. What should the company do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Formally document the SLA breach with supporting monitoring data and invoke the contract's "
                    "defined remedy (e.g., service credit) process with the provider"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The SLA already defines a documented remedy process for missed metrics; the "
                    "correct first step is to formally invoke it with supporting evidence, not to bypass it."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Immediately terminate the contract for cause without first documenting or invoking the "
                    "defined remedy process"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Skipping the contractually defined remedy process and jumping straight to "
                    "termination is premature and may itself violate the contract's dispute procedures."
                ),
            },
            {
                "id": "c",
                "text": "Renegotiate a new MOU with the provider to replace the existing SLA",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is a non-binding intent document; it is not the mechanism for enforcing "
                    "a breach of an existing binding SLA."
                ),
            },
            {
                "id": "d",
                "text": "Absorb the shortfall as a routine risk-acceptance decision and take no further action",
                "correct": False,
                "rationale": (
                    "Incorrect. This ignores a specific, already-contracted remedy the company is entitled to "
                    "invoke; failing to pursue it forfeits value the company is owed."
                ),
            },
        ],
        "explanation": (
            "When a measurable SLA metric is missed, the correct first step is to document the breach and "
            "invoke the contract's defined remedy process, not to terminate prematurely, substitute a "
            "non-binding MOU, or silently accept the loss."
        ),
    },
    {
        "id": "nd5b-010",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A company has an existing MSA with a penetration-testing firm establishing standard payment terms, "
            "liability caps, and confidentiality obligations for all future engagements. The company now wants "
            "to commission one specific web-application penetration test with a defined scope, timeline, and "
            "deliverables. Which document should be created for this specific engagement?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A statement of work (SOW) that references the existing MSA and defines the scope, "
                    "timeline, and deliverables for this specific test"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An SOW defines the specifics of one engagement (scope, timeline, deliverables) "
                    "while relying on the already-established MSA for the overarching legal and payment terms."
                ),
            },
            {
                "id": "b",
                "text": "A brand-new MSA negotiated solely for this one engagement",
                "correct": False,
                "rationale": (
                    "Incorrect. Negotiating a new MSA is redundant and inefficient, duplicating the overarching "
                    "legal framework the parties already established."
                ),
            },
            {
                "id": "c",
                "text": "A memorandum of understanding (MOU) describing the parties' general intent to work together",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU is non-binding and does not define the specific scope, timeline, or "
                    "deliverables the company needs for this engagement."
                ),
            },
            {
                "id": "d",
                "text": "A service level agreement (SLA) specifying only uptime and response-time metrics for the engagement",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA covers performance metrics like uptime, which are not applicable to "
                    "defining the scope and deliverables of a one-time penetration test project."
                ),
            },
        ],
        "explanation": (
            "Under an established MSA, individual engagements are defined through SOWs, which reference the "
            "MSA's standing terms rather than requiring a new overarching contract, a non-binding MOU, or an "
            "SLA meant for ongoing performance metrics."
        ),
    },
    {
        "id": "nd5b-011",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A global enterprise has over 600 active third-party vendors and cannot perform the same in-depth "
            "security assessment on every one within a reasonable budget. Which approach BEST allows the vendor "
            "risk management program to allocate its limited assessment resources effectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Tier vendors by criticality and data sensitivity (e.g., based on data accessed, system "
                    "dependency, and financial impact), and apply proportionally deeper due diligence to "
                    "higher-tier vendors"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk-based vendor tiering directs the deepest scrutiny to the vendors that pose "
                    "the greatest actual risk, allowing limited assessment resources to scale across a large "
                    "vendor population."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Apply the exact same standardized questionnaire and assessment depth to every vendor "
                    "regardless of the data or systems they touch"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A one-size-fits-all approach wastes resources on low-risk vendors and may "
                    "under-scrutinize high-risk ones; it does not scale efficiently to a large vendor population."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Assess only the vendors with the largest annual contract value, since higher-cost vendors "
                    "necessarily pose the greatest security risk"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Contract cost does not reliably correlate with security risk exposure; a "
                    "low-cost vendor with access to highly sensitive data can pose far greater risk than an "
                    "expensive but low-access vendor."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Rely exclusively on each vendor's self-reported security rating without any independent "
                    "verification, since this scales to any vendor count"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Unverified self-attestation, even if it scales easily, does not provide reliable "
                    "assurance for higher-risk vendors and undermines the purpose of due diligence."
                ),
            },
        ],
        "explanation": (
            "Risk-based vendor tiering — assessing depth proportional to criticality and data sensitivity — is "
            "the standard way to scale vendor risk management across a large portfolio, unlike uniform "
            "assessment, cost-based prioritization, or unverified self-attestation."
        ),
    },
    {
        "id": "nd5b-012",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "During due diligence, a company discovers that its critical cloud-storage vendor relies on an "
            "offshore subcontractor to perform backup operations, and that subcontractor was never disclosed in "
            "the original vendor questionnaire. What risk management gap does this MOST directly represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Inadequate fourth-party (subcontractor/supply-chain) risk visibility — the primary vendor's "
                    "own downstream relationships were not disclosed or assessed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. This is a classic fourth-party risk gap: the organization's direct vendor has its "
                    "own undisclosed downstream relationships that were never surfaced or evaluated."
                ),
            },
            {
                "id": "b",
                "text": "A right-to-audit clause violation, since the subcontractor has not yet been audited",
                "correct": False,
                "rationale": (
                    "Incorrect. A right-to-audit clause is a separate contractual provision issue; the core "
                    "problem described is the undisclosed subcontracting relationship itself, not an audit that "
                    "hasn't yet occurred."
                ),
            },
            {
                "id": "c",
                "text": "A data classification failure, since the backup data was mislabeled",
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing in the scenario indicates a labeling or classification error; the issue "
                    "is an undisclosed subcontracting relationship, not mislabeled data."
                ),
            },
            {
                "id": "d",
                "text": "A risk transference failure, because insurance was never purchased for the subcontractor relationship",
                "correct": False,
                "rationale": (
                    "Incorrect. The gap described is a due-diligence and visibility issue, not a failure to "
                    "transfer risk via insurance."
                ),
            },
        ],
        "explanation": (
            "Fourth-party (subcontractor) risk arises when a primary vendor's own supply chain is not disclosed "
            "or assessed. This is distinct from audit-clause enforcement, data classification, or risk "
            "transference concerns."
        ),
    },
    {
        "id": "nd5b-013",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Vendor risk management",
        "stem": (
            "A company is terminating its relationship with a marketing analytics vendor that had API access to "
            "customer purchase history. Which action is MOST important to complete as part of vendor offboarding?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Revoke the vendor's API credentials/access and obtain contractual confirmation that all "
                    "shared customer data has been returned or securely destroyed"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Proper offboarding requires both cutting off active access and confirming the "
                    "disposition of any data the vendor previously received — leaving either step out creates "
                    "lingering exposure."
                ),
            },
            {
                "id": "b",
                "text": "Simply allow the vendor's API credentials to expire naturally at the end of the current contract term",
                "correct": False,
                "rationale": (
                    "Incorrect. Passive expiration leaves an unnecessary window of continued access and does "
                    "not address what happens to data already shared with the vendor."
                ),
            },
            {
                "id": "c",
                "text": "Request that the vendor sign a new SLA covering post-termination uptime guarantees",
                "correct": False,
                "rationale": (
                    "Incorrect. Uptime guarantees are irrelevant once the relationship has ended; an SLA is the "
                    "wrong instrument for closing out access and data-handling obligations."
                ),
            },
            {
                "id": "d",
                "text": "Add the vendor to a permanent internal deny list without further action, since blocking is sufficient by itself",
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking future access alone does not confirm that existing credentials were "
                    "actually revoked or that already-shared data was returned or destroyed."
                ),
            },
        ],
        "explanation": (
            "Vendor offboarding requires both active credential revocation and documented confirmation of data "
            "return/destruction — passive expiration, irrelevant new agreements, or blocking alone are all "
            "insufficient."
        ),
    },
    {
        "id": "nd5b-014",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Risk management strategies",
        "stem": (
            "After repeated chargeback fraud losses linked to cryptocurrency payments, a retailer's leadership "
            "decides to stop accepting cryptocurrency as a payment method entirely, rather than invest in "
            "fraud-detection tooling for that channel. Which risk management strategy does this represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk avoidance",
                "correct": True,
                "rationale": (
                    "Correct. Eliminating the risk-bearing activity (accepting cryptocurrency payments) entirely, "
                    "rather than continuing it with added controls, is the definition of risk avoidance."
                ),
            },
            {
                "id": "b",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation means reducing risk through added controls while continuing the "
                    "activity; here, the activity itself is discontinued entirely."
                ),
            },
            {
                "id": "c",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance means continuing to bear the risk with no change in activity; here, "
                    "the risk-bearing activity is eliminated rather than tolerated."
                ),
            },
            {
                "id": "d",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference shifts the risk to a third party (e.g., an insurer); no third "
                    "party assumes this risk — the exposure is simply eliminated by discontinuing the activity."
                ),
            },
        ],
        "explanation": (
            "Discontinuing a risk-bearing activity entirely, rather than reducing, tolerating, or shifting the "
            "risk elsewhere, is the defining characteristic of risk avoidance."
        ),
    },
    {
        "id": "nd5b-015",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "After implementing a planned mitigation, the risk owner recalculates the residual risk score for a "
            "legacy file-transfer protocol still in use and finds it remains above the organization's documented "
            "risk appetite threshold. What should the risk owner do NEXT?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Escalate the risk for a formal decision, by the appropriate management level, to accept the "
                    "excess residual risk, apply additional treatment, transfer it, or avoid it — with the "
                    "decision documented in the risk register"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When residual risk still exceeds appetite after treatment, the risk owner must "
                    "escalate for a deliberate, documented decision on further handling rather than leaving the "
                    "gap unresolved."
                ),
            },
            {
                "id": "b",
                "text": "Close the risk register entry, since a mitigating control has already been implemented",
                "correct": False,
                "rationale": (
                    "Incorrect. Closing the entry ignores that residual risk still exceeds the organization's "
                    "stated appetite; the underlying issue isn't resolved just because some control exists."
                ),
            },
            {
                "id": "c",
                "text": "Automatically purchase a cyber-insurance policy to cover the excess residual risk without further review",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference should be a deliberate, evaluated decision weighed against other "
                    "options, not an automatic default action taken without review."
                ),
            },
            {
                "id": "d",
                "text": "Take no further action, since risk appetite is only a guideline and has no bearing on individual risk register entries",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk appetite is meant to actively bound decisions about individual risks; "
                    "treating it as a non-binding suggestion contradicts its governance purpose."
                ),
            },
        ],
        "explanation": (
            "When residual risk still exceeds the organization's risk appetite after treatment, it must be "
            "escalated for a formal, documented decision — not closed, defaulted to insurance, or ignored."
        ),
    },
    {
        "id": "nd5b-016",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "Select the TWO actions below that represent risk MITIGATION, as opposed to avoidance, acceptance, "
            "or transference."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Segmenting a legacy OT/ICS network from the corporate IT network to reduce the potential "
                    "blast radius of a compromise"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Adding a technical control (segmentation) to reduce the likelihood or impact of a "
                    "compromise, while continuing to operate the network, is textbook risk mitigation."
                ),
            },
            {
                "id": "b",
                "text": "Requiring multifactor authentication for all privileged administrative accounts",
                "correct": True,
                "rationale": (
                    "Correct. MFA is a control added to reduce the likelihood of credential-based compromise "
                    "while the underlying activity (privileged account use) continues — mitigation, not avoidance "
                    "or transference."
                ),
            },
            {
                "id": "c",
                "text": "Purchasing a cyber liability insurance policy to cover breach-related legal costs",
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance shifts the financial impact of a risk to a third-party insurer, which "
                    "is risk transference, not mitigation."
                ),
            },
            {
                "id": "d",
                "text": "Decommissioning a legacy web application that cannot be patched, rather than continuing to operate it",
                "correct": False,
                "rationale": (
                    "Incorrect. Eliminating the risk-bearing activity entirely is risk avoidance, not mitigation "
                    "— no control is being added to an activity that continues."
                ),
            },
        ],
        "explanation": (
            "Mitigation adds controls (segmentation, MFA) to reduce risk while the activity continues — distinct "
            "from transference (insurance) and avoidance (discontinuing the activity)."
        ),
    },
    {
        "id": "nd5b-017",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Risk register & appetite",
        "stem": (
            "During a risk register audit, a reviewer notes that several open, high-severity risk entries have "
            "an assigned risk owner but no target remediation date or scheduled review date. Which issue does "
            "this MOST likely create?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "There is no way to hold the risk owner accountable to a timeline, and treatment activities "
                    "may drift indefinitely without triggering follow-up or escalation"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Without a target date, there is no benchmark against which to measure progress or "
                    "trigger escalation, so treatment can stall indefinitely even with an owner assigned."
                ),
            },
            {
                "id": "b",
                "text": "The risk's inherent risk score can no longer be calculated",
                "correct": False,
                "rationale": (
                    "Incorrect. The inherent risk score depends on likelihood and impact data, not on whether a "
                    "target remediation date has been set."
                ),
            },
            {
                "id": "c",
                "text": "The risk automatically converts from residual to inherent status",
                "correct": False,
                "rationale": (
                    "Incorrect. Whether a risk is inherent or residual reflects whether controls have been "
                    "applied, which has nothing to do with a missing target date."
                ),
            },
            {
                "id": "d",
                "text": "The risk owner assignment becomes invalid and must be reassigned",
                "correct": False,
                "rationale": (
                    "Incorrect. A missing target date does not invalidate an already properly assigned risk "
                    "owner; the owner remains accountable, just without a tracked deadline."
                ),
            },
        ],
        "explanation": (
            "Risk register entries need both an assigned owner and a target remediation/review date. Missing "
            "the date removes the mechanism for holding treatment to a timeline, even when ownership is clear."
        ),
    },
    {
        "id": "nd5b-018",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "The board has defined a quantifiable risk appetite statement: 'No individual risk with a calculated "
            "ALE exceeding $250,000 may proceed without documented CFO sign-off.' A newly identified risk "
            "involving an unencrypted legacy file share has an SLE of $500,000 and an ARO of 0.6, and has not yet "
            "been escalated to the CFO. What should happen?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The risk must be escalated for CFO sign-off, because its ALE of $300,000 ($500,000 x 0.6) "
                    "exceeds the board's $250,000 appetite threshold"
                ),
                "correct": True,
                "rationale": (
                    "Correct. ALE = SLE x ARO = $500,000 x 0.6 = $300,000, which exceeds the $250,000 threshold "
                    "the appetite statement defines, triggering mandatory CFO escalation."
                ),
            },
            {
                "id": "b",
                "text": (
                    "No escalation is required, because the SLE of $500,000, not the ALE, is what the appetite "
                    "statement measures"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The board's appetite statement explicitly references ALE, not SLE; using the "
                    "wrong figure misapplies the threshold."
                ),
            },
            {
                "id": "c",
                "text": (
                    "No escalation is required, because the ALE of $300,000 is still below the $500,000 SLE, "
                    "and the appetite statement compares ALE to SLE, not to a fixed dollar threshold"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The appetite statement compares ALE to the fixed $250,000 threshold, not to the "
                    "SLE; comparing ALE to SLE is not the mechanism the board defined."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The risk must be escalated, but only because the ARO exceeds 0.5, not because of any "
                    "dollar threshold"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This misreads the appetite statement's actual mechanism, which is a dollar-based "
                    "ALE threshold, not a standalone ARO threshold."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO = $500,000 x 0.6 = $300,000. Since the board's documented risk appetite caps "
            "unescalated risk at an ALE of $250,000, this risk exceeds the threshold and requires CFO sign-off."
        ),
    },
    {
        "id": "nd5b-019",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "A risk register entry for 'outdated TLS configuration on customer portal' shows a residual risk "
            "score that has crept from 6 (low) to 9 (moderate) to 14 (high) over three consecutive quarterly "
            "reviews, even though the originally implemented controls have not been modified or removed. What "
            "is the MOST likely explanation, and the appropriate response?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Control effectiveness may be degrading relative to an evolving threat landscape (e.g., "
                    "newly disclosed TLS vulnerabilities or deprecated cipher suites); the risk should be "
                    "reassessed and controls updated rather than assumed to still be adequate"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Risk scores can legitimately rise over time as the external threat landscape "
                    "evolves, even without changes to the controls themselves — the register should trigger "
                    "reassessment, not be dismissed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The risk register contains a data-entry error, since a risk score cannot change unless the "
                    "underlying controls are physically altered"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risk scores legitimately change as threats, asset value, or context evolve, "
                    "even without any changes to the controls themselves."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The organization's risk appetite must have been lowered each quarter, artificially "
                    "inflating the score"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Nothing indicates the appetite threshold changed; the risk's own likelihood or "
                    "impact assessment is what increased, independent of appetite."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The entry should be closed and removed from the register, since the same controls remain "
                    "in place from the original assessment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Closing an increasingly severe risk contradicts sound risk management; it should "
                    "be reassessed and treated further, not dismissed simply because the controls are unchanged."
                ),
            },
        ],
        "explanation": (
            "A rising residual risk score with unchanged controls typically signals control effectiveness "
            "eroding against an evolving threat landscape, and should trigger reassessment rather than being "
            "dismissed as an error, an appetite change, or grounds for closure."
        ),
    },
    {
        "id": "nd5b-020",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "A company's internal security handbook states that employees 'should consider using a password "
            "manager to generate and store unique credentials,' but does not require it or make it a condition "
            "of system access. What type of governance document provision is this?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A guideline — a recommended, non-mandatory best practice",
                "correct": True,
                "rationale": (
                    "Correct. 'Should consider' language, with no enforcement or condition attached, is the "
                    "hallmark of a guideline: an optional recommendation rather than a mandatory requirement."
                ),
            },
            {
                "id": "b",
                "text": "A standard",
                "correct": False,
                "rationale": (
                    "Incorrect. Standards are mandatory, measurable technical requirements; 'should consider' "
                    "language is explicitly non-mandatory, the opposite of a standard."
                ),
            },
            {
                "id": "c",
                "text": "A procedure",
                "correct": False,
                "rationale": (
                    "Incorrect. Procedures are mandatory, step-by-step instructions for performing a task, not "
                    "an optional recommendation like this one."
                ),
            },
            {
                "id": "d",
                "text": "A policy",
                "correct": False,
                "rationale": (
                    "Incorrect. Policies are broad, typically mandatory statements of management intent, not an "
                    "optional individual suggestion phrased as 'should consider.'"
                ),
            },
        ],
        "explanation": (
            "Governance hierarchy: policy (broad, mandatory intent) -> standard (mandatory, measurable "
            "requirement) -> procedure (mandatory step-by-step instructions) -> guideline (optional "
            "recommendation), which is what 'should consider' language describes."
        ),
    },
    {
        "id": "nd5b-021",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A newly hired CISO is briefing the board on the organization's security governance structure. "
            "Which statement BEST describes who holds ultimate accountability, to the board, for the overall "
            "effectiveness of the security program?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The CISO (or equivalent executive) is accountable to the board for the security program's "
                    "overall effectiveness, even though day-to-day control execution is delegated to data "
                    "owners, custodians, and operational teams"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The CISO holds executive-level accountability to the board for the security "
                    "program as a whole, while delegating operational execution to other roles."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The security operations center (SOC) analysts are accountable, since they directly monitor "
                    "and respond to incidents daily"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. SOC analysts perform operational monitoring and response tasks; they are not "
                    "the executive held accountable to the board for the overall program."
                ),
            },
            {
                "id": "c",
                "text": "Each individual data owner is independently accountable to the board for the entire security program",
                "correct": False,
                "rationale": (
                    "Incorrect. Data owners are accountable for their own specific data domains, not the "
                    "organization-wide program in its entirety."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The organization's cyber-insurance carrier is accountable, since it financially backs the "
                    "risk of a security failure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An insurer bears financial risk transference, not organizational governance "
                    "accountability to the board."
                ),
            },
        ],
        "explanation": (
            "Executive-level accountability for the overall security program rests with the CISO (or equivalent "
            "executive) reporting to the board, distinct from operational roles like SOC analysts, individual "
            "data owners, or third parties like insurers."
        ),
    },
    {
        "id": "nd5b-022",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A legacy manufacturing execution system cannot support the organization's mandatory AES-256 "
            "encryption-at-rest standard due to hardware limitations, and replacing it is not feasible for "
            "another 18 months. What is the appropriate governance action?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Submit a formal, time-bound policy exception request documenting compensating controls, a "
                    "review/expiration date, and sign-off from an appropriate risk-accepting authority"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A documented, time-bound exception with compensating controls and formal sign-off "
                    "is the standard governance mechanism for a legitimate, temporary inability to meet a "
                    "mandatory standard."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Quietly continue operating the system without encryption and without documenting the "
                    "deviation, since replacement is already planned"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An undocumented deviation from a mandatory standard bypasses governance "
                    "oversight and leaves the risk untracked and unowned."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Immediately decommission the system, since any deviation from a mandatory standard is "
                    "automatically prohibited"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This response is disproportionate; a documented, time-bound exception with "
                    "compensating controls is the standard governance mechanism, not automatic decommissioning."
                ),
            },
            {
                "id": "d",
                "text": "Rewrite the encryption standard itself to permanently exempt this specific system",
                "correct": False,
                "rationale": (
                    "Incorrect. Permanently weakening an organization-wide standard for one system's convenience "
                    "undermines governance, rather than using the proper time-bound exception process."
                ),
            },
        ],
        "explanation": (
            "When a system legitimately cannot meet a mandatory standard, the correct governance response is a "
            "formal, time-bound, documented exception with compensating controls and appropriate sign-off — not "
            "silent noncompliance, disproportionate decommissioning, or permanently rewriting the standard."
        ),
    },
    {
        "id": "nd5b-023",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A company operating in the EU detects that an attacker exfiltrated a database containing EU "
            "residents' personal data. Under GDPR, within what timeframe must the company generally notify the "
            "relevant supervisory authority after becoming aware of the breach, absent an applicable exception?"
        ),
        "options": [
            {
                "id": "a",
                "text": "72 hours",
                "correct": True,
                "rationale": (
                    "Correct. GDPR requires notification to the supervisory authority without undue delay and, "
                    "where feasible, no later than 72 hours after becoming aware of the breach."
                ),
            },
            {
                "id": "b",
                "text": "24 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This is too short; GDPR's standard notification window to the supervisory "
                    "authority is 72 hours, not 24."
                ),
            },
            {
                "id": "c",
                "text": "30 days",
                "correct": False,
                "rationale": (
                    "Incorrect. This far exceeds GDPR's required notification window of 72 hours to the "
                    "supervisory authority."
                ),
            },
            {
                "id": "d",
                "text": "There is no fixed deadline as long as notification eventually occurs",
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR specifically imposes the 72-hour standard for supervisory authority "
                    "notification, not an open-ended timeline."
                ),
            },
        ],
        "explanation": (
            "GDPR requires breach notification to the relevant supervisory authority within 72 hours of "
            "becoming aware of the breach, absent an applicable exception."
        ),
    },
    {
        "id": "nd5b-024",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A company found in serious violation of GDPR's core data-processing principles (e.g., lacking a "
            "lawful basis for processing) is subject to the regulation's highest administrative fine tier. Which "
            "figure correctly reflects that maximum tier?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Up to €20 million, or 4% of the company's total global annual turnover from the preceding "
                    "financial year — whichever is HIGHER"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR's highest fine tier is up to €20 million or 4% of global annual turnover, "
                    "whichever amount is greater, ensuring the penalty scales meaningfully for large "
                    "multinational firms."
                ),
            },
            {
                "id": "b",
                "text": "Up to €20 million, or 4% of global annual turnover — whichever is LOWER",
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR's highest tier uses whichever amount is greater, not lesser, so the fine "
                    "can scale up with the size of the violating organization."
                ),
            },
            {
                "id": "c",
                "text": "Up to €10 million, or 2% of global annual turnover — whichever is higher",
                "correct": False,
                "rationale": (
                    "Incorrect. This figure represents GDPR's LOWER fine tier (for less severe violations), not "
                    "the highest tier described in this scenario."
                ),
            },
            {
                "id": "d",
                "text": "A fixed penalty of €1 million regardless of company size or revenue",
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR fines scale with revenue and violation severity; there is no fixed flat "
                    "penalty at any tier."
                ),
            },
        ],
        "explanation": (
            "GDPR's highest administrative fine tier, reserved for serious violations of core processing "
            "principles, is up to €20 million or 4% of global annual turnover, whichever is greater — distinct "
            "from the lower €10 million/2% tier."
        ),
    },
    {
        "id": "nd5b-025",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "An e-commerce company processes a customer's shipping address and payment details solely to fulfill "
            "the customer's purchase order, without requesting separate opt-in consent for that specific "
            "processing. Under GDPR, which lawful basis MOST directly justifies this processing?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Performance of a contract — processing that is necessary to fulfill the contractual "
                    "obligation (the purchase) the data subject entered into"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Processing strictly necessary to fulfill an order the customer initiated falls "
                    "under the 'performance of a contract' lawful basis, which does not require separate consent."
                ),
            },
            {
                "id": "b",
                "text": "Consent",
                "correct": False,
                "rationale": (
                    "Incorrect. Consent is a distinct lawful basis requiring an affirmative opt-in; it is not "
                    "what justifies processing that is merely necessary to fulfill an already-placed order."
                ),
            },
            {
                "id": "c",
                "text": "Legitimate interest",
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate interest is a balancing-test basis typically used for purposes like "
                    "fraud prevention or direct marketing, not the primary basis for data strictly necessary to "
                    "perform the contracted transaction itself."
                ),
            },
            {
                "id": "d",
                "text": "Public task",
                "correct": False,
                "rationale": (
                    "Incorrect. Public task applies to processing carried out by a public authority or in the "
                    "exercise of official governmental functions, not a private e-commerce order fulfillment."
                ),
            },
        ],
        "explanation": (
            "GDPR recognizes several lawful bases for processing. Data strictly necessary to fulfill a contract "
            "the data subject entered into (such as order fulfillment) relies on the 'performance of a contract' "
            "basis, not consent, legitimate interest, or public task."
        ),
    },
    {
        "id": "nd5b-026",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "Before a penetration test begins, the testing team and the client must formally agree on the "
            "systems in scope, permitted testing windows, prohibited techniques (e.g., no denial-of-service "
            "testing against production), and emergency stop procedures. Which document captures these terms?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Rules of engagement (ROE)",
                "correct": True,
                "rationale": (
                    "Correct. The rules of engagement is the pre-engagement document that formally defines "
                    "scope, timing, permitted/prohibited techniques, and emergency procedures for a penetration "
                    "test."
                ),
            },
            {
                "id": "b",
                "text": "A non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA protects the confidentiality of information exchanged; it does not "
                    "define testing scope, timing, or permitted techniques."
                ),
            },
            {
                "id": "c",
                "text": "A SOC 2 Type II report",
                "correct": False,
                "rationale": (
                    "Incorrect. A SOC 2 report attests to control effectiveness after an audit; it is not the "
                    "pre-engagement scoping document for a penetration test."
                ),
            },
            {
                "id": "d",
                "text": "A vulnerability scan report",
                "correct": False,
                "rationale": (
                    "Incorrect. A scan report is an output/deliverable of testing activity, not the "
                    "pre-engagement authorization document that defines scope and rules before testing starts."
                ),
            },
        ],
        "explanation": (
            "Rules of engagement formally define a penetration test's scope, timing, permitted/prohibited "
            "techniques, and emergency procedures before testing begins — distinct from confidentiality (NDA), "
            "attestation (SOC 2), or test output (scan report) documents."
        ),
    },
    {
        "id": "nd5b-027",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "An internal auditor samples 40 recent production change tickets and finds that 12 of them (30%) "
            "were deployed without the change advisory board (CAB) approval required by the documented "
            "change-management policy. What should this be recorded as, and what is the appropriate next step?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A control deficiency (audit finding); the finding should be documented with a corrective "
                    "action plan, an assigned owner, a remediation timeline, and a follow-up review to validate "
                    "the fix"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A mandatory control being bypassed 30% of the time is a legitimate control "
                    "deficiency that should follow the standard audit finding lifecycle: documentation, "
                    "corrective action, ownership, and follow-up validation."
                ),
            },
            {
                "id": "b",
                "text": "A false positive, since 70% of the sampled tickets did comply with the policy",
                "correct": False,
                "rationale": (
                    "Incorrect. A 30% noncompliance rate on a mandatory control is a legitimate finding, not a "
                    "false positive to be dismissed simply because the majority of samples passed."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Sufficient grounds to immediately suspend the entire change-management program pending a "
                    "full external audit"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This response is disproportionate; a documented finding with a corrective action "
                    "plan is the standard response, not suspending the entire program."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No action is needed, since the underlying policy itself, not the CAB approval step, was "
                    "not violated"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The CAB approval requirement is part of the documented policy; skipping it is "
                    "itself the compliance gap the audit correctly identified."
                ),
            },
        ],
        "explanation": (
            "A sampled control failure rate like this represents a documented control deficiency requiring a "
            "corrective action plan, ownership, and follow-up — not dismissal, disproportionate program "
            "suspension, or the claim that no policy was violated."
        ),
    },
    {
        "id": "nd5b-028",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_response",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "Select the TWO elements that MUST be explicitly defined in a penetration test's rules of "
            "engagement (ROE) before testing begins."
        ),
        "options": [
            {
                "id": "a",
                "text": "The authorized scope of systems/networks to be tested and the testing time window",
                "correct": True,
                "rationale": (
                    "Correct. Defining exactly what is in scope and when testing may occur is a core, essential "
                    "component of any pre-engagement rules of engagement."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Emergency stop/escalation procedures and points of contact if testing causes unintended "
                    "impact"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Defined emergency procedures and contacts are essential so that testing can be "
                    "safely halted and escalated if something goes wrong."
                ),
            },
            {
                "id": "c",
                "text": "The final remediation budget the client will allocate after the report is delivered",
                "correct": False,
                "rationale": (
                    "Incorrect. Remediation budgeting is decided after the test, based on the findings; it is "
                    "not something defined in the pre-engagement rules of engagement."
                ),
            },
            {
                "id": "d",
                "text": "The specific CVE identifiers the testers are guaranteed to find during the engagement",
                "correct": False,
                "rationale": (
                    "Incorrect. Test outcomes cannot be guaranteed in advance; specific vulnerabilities are "
                    "unknown until testing actually occurs, so this cannot be predefined in the ROE."
                ),
            },
        ],
        "explanation": (
            "Rules of engagement must define scope, timing, and emergency procedures before testing begins — "
            "unlike post-engagement budgeting decisions or guaranteed findings, which cannot be known in advance."
        ),
    },
    {
        "id": "nd5b-029",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "An internal HR compensation-banding report is accessible only to HR and finance staff. Its "
            "disclosure would cause moderate embarrassment and some internal morale friction, but it involves no "
            "regulatory obligation, no legal exposure, and no material financial harm to the company. Which "
            "classification level BEST fits this data?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Internal/Confidential (a mid-tier level) — sensitive enough to restrict beyond general "
                    "staff, but not warranting the strictest controls reserved for regulated or legally/"
                    "financially critical data"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The stated impact (moderate embarrassment, morale friction, no legal/regulatory/"
                    "financial harm) matches a mid-tier classification, not the least sensitive or most "
                    "sensitive extreme."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Restricted (the highest tier), with the same strict need-to-know and encryption controls "
                    "used for regulated financial or legal data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Over-classifying moderate-sensitivity HR data at the highest tier wastes control "
                    "resources meant for genuinely severe-impact data, such as regulated or legally critical "
                    "information."
                ),
            },
            {
                "id": "c",
                "text": "Public, since compensation bands are common industry knowledge in general terms",
                "correct": False,
                "rationale": (
                    "Incorrect. This specific, company-internal report is not intended for public release, and "
                    "disclosure would still cause internal harm, ruling out a public classification."
                ),
            },
            {
                "id": "d",
                "text": "There is no need to classify this data at all, since no regulation explicitly covers internal compensation bands",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification is driven by the business impact of disclosure, not solely by "
                    "whether a specific regulation applies; sensitive internal data still requires classification."
                ),
            },
        ],
        "explanation": (
            "Classification level should match the potential harm from disclosure. Moderate-impact, non-"
            "regulated internal data fits a mid-tier level — not the highest tier reserved for severe harm, "
            "public, or unclassified."
        ),
    },
    {
        "id": "nd5b-030",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "A customer email marketing list is subject to both an internal data-handling policy (which would "
            "classify it as 'Internal') and a stricter regulatory consent/opt-out requirement under applicable "
            "privacy law (which would treat this data as requiring more restrictive handling). Marketing wants "
            "to label the list 'Public' because it is only used for newsletters. What is the correct "
            "classification approach?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Classify the data at the level required by the MOST restrictive applicable obligation (the "
                    "stricter regulatory requirement), regardless of the internal team's preferred convenience "
                    "label"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When multiple obligations apply to the same data, the classification must reflect "
                    "the strictest applicable requirement, not the label most convenient for the team using the "
                    "data."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Classify it as 'Public,' per marketing's request, since that reflects its intended "
                    "day-to-day business use"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification must reflect actual sensitivity and regulatory exposure, not the "
                    "convenience of the team using the data for a particular purpose."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Classify it as 'Internal' only, since that is the organization's own internal policy "
                    "default and regulatory requirements are advisory"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Applicable legal and regulatory requirements are not merely advisory; they can "
                    "mandate a stricter classification than internal policy alone would assign."
                ),
            },
            {
                "id": "d",
                "text": "Allow each department that uses the list to assign its own classification level independently",
                "correct": False,
                "rationale": (
                    "Incorrect. Classification must be consistent and centrally governed based on sensitivity "
                    "and regulatory exposure, not assigned ad hoc by whichever department happens to be using "
                    "the data."
                ),
            },
        ],
        "explanation": (
            "When multiple classification obligations apply to the same dataset, the strictest applicable "
            "requirement governs — not a convenient business label, an internal-only default, or department-by-"
            "department discretion."
        ),
    },
    {
        "id": "nd5b-031",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "Select the TWO factors that should PRIMARILY drive the classification level assigned to a given "
            "dataset."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The potential business, legal, regulatory, or reputational impact if the data is "
                    "disclosed, altered, or lost"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification is fundamentally driven by the potential impact of a confidentiality, "
                    "integrity, or availability failure affecting the data."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Applicable legal and regulatory requirements governing the specific type of data (e.g., "
                    "health, financial, or personal data)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Legal and regulatory obligations tied to specific data types directly inform the "
                    "minimum classification and handling requirements that must be applied."
                ),
            },
            {
                "id": "c",
                "text": "The number of years the employee who created the data has been with the company",
                "correct": False,
                "rationale": (
                    "Incorrect. An employee's tenure has no bearing on the sensitivity or classification of the "
                    "data they created."
                ),
            },
            {
                "id": "d",
                "text": "The department's available budget for storage infrastructure",
                "correct": False,
                "rationale": (
                    "Incorrect. Storage budget is an operational/cost consideration, not a driver of a dataset's "
                    "classification level."
                ),
            },
        ],
        "explanation": (
            "Data classification should be driven by potential impact of disclosure/loss and applicable legal/"
            "regulatory requirements — not by unrelated factors like an employee's tenure or a department's "
            "infrastructure budget."
        ),
    },
    {
        "id": "nd5b-032",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A VP of Sales is formally accountable for the CRM database, including deciding which roles may "
            "access specific fields (e.g., deal values, contact details) and approving its classification "
            "level. Which role does the VP fulfill?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data owner — holds ultimate business accountability for the data, including classification "
                    "and access-approval decisions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ultimate accountability for a dataset's classification and access decisions is "
                    "the defining responsibility of the data owner role."
                ),
            },
            {
                "id": "b",
                "text": "Data custodian",
                "correct": False,
                "rationale": (
                    "Incorrect. The custodian implements the technical and operational controls (backups, "
                    "access provisioning) directed by the owner, rather than making the accountable "
                    "classification/access decisions described here."
                ),
            },
            {
                "id": "c",
                "text": "Data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. Controller is a GDPR-specific term for the entity determining the purposes and "
                    "means of processing; the VP's described role here is the internal data-owner accountability "
                    "role."
                ),
            },
            {
                "id": "d",
                "text": "Data processor",
                "correct": False,
                "rationale": (
                    "Incorrect. A processor handles data solely on another party's instructions, typically an "
                    "external party — not an internally accountable business owner making access decisions."
                ),
            },
        ],
        "explanation": (
            "The data owner holds ultimate business accountability for a dataset, including classification and "
            "access approval — distinct from the custodian (technical implementation), controller (GDPR "
            "purpose-setter), or processor (external party acting on instructions)."
        ),
    },
    {
        "id": "nd5b-033",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A payroll outsourcing firm processes employee salary data strictly according to each client "
            "company's instructions. However, the firm also independently decides to retain a de-identified "
            "subset of that data for its own internal fraud-analytics research, determining the purpose and "
            "retention period itself without client instruction. For THIS SPECIFIC fraud-analytics activity, "
            "what is the payroll firm's role?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Data controller for that specific activity — because it independently determines the "
                    "purpose and means of that particular processing, an organization can be a controller for "
                    "one activity and a processor for another"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR roles are assessed per processing activity, not organization-wide. Where the "
                    "firm independently decides the purpose and means of processing, it acts as a controller for "
                    "that specific activity, even while remaining a processor for its main payroll work."
                ),
            },
            {
                "id": "b",
                "text": "Still solely a data processor, since it is a processor for its main payroll business",
                "correct": False,
                "rationale": (
                    "Incorrect. A role is determined per processing activity, not fixed globally for an entire "
                    "organization; for the activity where it decides purpose and means independently, it acts "
                    "as a controller."
                ),
            },
            {
                "id": "c",
                "text": "A data custodian, since it is handling data belonging to its clients",
                "correct": False,
                "rationale": (
                    "Incorrect. Custodian describes an internal technical-safeguarding role, not the GDPR "
                    "controller/processor distinction relevant to determining who decides the purpose of "
                    "processing."
                ),
            },
            {
                "id": "d",
                "text": "A data subject, since the fraud-analytics activity relates to the employees whose data was originally collected",
                "correct": False,
                "rationale": (
                    "Incorrect. The payroll firm is the entity processing and analyzing the data, not the "
                    "individual to whom the data pertains; the employees themselves are the data subjects."
                ),
            },
        ],
        "explanation": (
            "GDPR controller/processor status is assessed per processing activity. An organization that "
            "independently determines the purpose and means of a specific activity is a controller for that "
            "activity, even if it acts strictly as a processor for other activities involving the same data."
        ),
    },
    {
        "id": "nd5b-034",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "Two independent hospital systems jointly design and jointly determine the purposes and means of a "
            "shared, de-identified research database, with both organizations making shared decisions about how "
            "the data will be used. Under GDPR terminology, what are the two hospital systems considered?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Joint controllers — both organizations jointly determine the purposes and means of the "
                    "processing and share responsibility for GDPR compliance regarding that database"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR explicitly recognizes joint controllership when two or more parties jointly "
                    "determine the purposes and means of processing, as described here."
                ),
            },
            {
                "id": "b",
                "text": (
                    "One is the controller and the other is automatically the processor, since GDPR always "
                    "assigns exactly one controller per dataset"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR does not force a single-controller structure; it explicitly recognizes "
                    "joint controllership when parties jointly determine purposes and means, as is the case here."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Both are data processors, since the research database serves a secondary purpose beyond "
                    "direct patient care"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Processors act on another party's instructions; here, both hospitals "
                    "independently and jointly decide the purposes and means themselves, which is the defining "
                    "trait of controllers, not processors."
                ),
            },
            {
                "id": "d",
                "text": "Both are data custodians, since they jointly safeguard the shared research database",
                "correct": False,
                "rationale": (
                    "Incorrect. Custodian describes an internal technical-safeguarding role, not the GDPR-"
                    "specific joint decision-making relationship described in this scenario."
                ),
            },
        ],
        "explanation": (
            "When two or more parties jointly determine the purposes and means of processing, GDPR recognizes "
            "them as joint controllers with shared compliance responsibility — distinct from a single-controller "
            "structure, a processor relationship, or a custodian role."
        ),
    },
    {
        "id": "nd5b-035",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "An IT department is redeploying a batch of internal loaner laptops, previously used to access "
            "moderately sensitive internal documents, to a different department within the same company for "
            "continued internal use at a similar sensitivity level. Following NIST SP 800-88 sanitization "
            "guidance, which sanitization category is MOST appropriate before reissuing these devices?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Clear — a single logical sanitization (e.g., overwrite via standard OS/vendor tools) is "
                    "sufficient for media that will remain within the organization's control at a similar or "
                    "lower sensitivity level"
                ),
                "correct": True,
                "rationale": (
                    "Correct. NIST SP 800-88 identifies Clear as the proportionate sanitization tier for media "
                    "staying within organizational control at a comparable sensitivity level, as described here."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Purge — techniques such as cryptographic erase or degaussing, reserved for media leaving "
                    "organizational control or moving to a significantly lower trust environment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Purge is reserved for media leaving the organization's control or moving to a "
                    "meaningfully lower-trust environment; it is disproportionate for internal reuse at a "
                    "comparable sensitivity level."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Destroy — physical destruction such as shredding, reserved for end-of-life media that will "
                    "never be reused"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Destruction is disproportionate and wasteful for functional laptops being "
                    "redeployed for continued internal use, rather than reaching end-of-life."
                ),
            },
            {
                "id": "d",
                "text": "No sanitization is needed, since the laptops are remaining within the same company",
                "correct": False,
                "rationale": (
                    "Incorrect. Even internal redeployment across departments requires sanitization to prevent "
                    "unauthorized access to the previous department's data by the new custodians."
                ),
            },
        ],
        "explanation": (
            "NIST SP 800-88 scales sanitization to context: Clear suffices for media staying within "
            "organizational control at similar sensitivity, while Purge and Destroy are reserved for media "
            "leaving control or reaching true end-of-life."
        ),
    },
    {
        "id": "nd5b-036",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company is returning a batch of leased end-user laptops to the leasing company at the end of the "
            "lease term. These laptops previously stored trade secrets and cannot be physically destroyed, "
            "since they must be returned intact and functional per the lease agreement. What should the company "
            "do before returning them?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Perform a verified purge (e.g., cryptographic erase for self-encrypting drives, or a "
                    "vendor-approved secure-erase utility) and retain internal documentation confirming "
                    "sanitization before shipment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A verified purge renders the data unrecoverable while leaving the hardware intact "
                    "and functional, satisfying both the security requirement and the lease's return condition."
                ),
            },
            {
                "id": "b",
                "text": "Physically destroy the drives inside the laptops before returning them, since destruction is always the most secure option",
                "correct": False,
                "rationale": (
                    "Incorrect. This would breach the lease agreement's requirement that devices be returned "
                    "intact and functional; destruction is not compatible with a return-and-reuse lease "
                    "obligation."
                ),
            },
            {
                "id": "c",
                "text": "Perform a quick reformat of each laptop's drive, since that is sufficient once the lease has legally ended",
                "correct": False,
                "rationale": (
                    "Incorrect. A quick reformat does not reliably remove data and leaves trade secrets "
                    "recoverable using common forensic tools."
                ),
            },
            {
                "id": "d",
                "text": "Return the laptops as-is and rely on the leasing company's own data-wiping process after receipt",
                "correct": False,
                "rationale": (
                    "Incorrect. The organization that held the sensitive data is responsible for sanitizing it "
                    "before relinquishing physical control, not for trusting the next custodian to do so."
                ),
            },
        ],
        "explanation": (
            "When leased media must be returned intact, a verified purge (rather than physical destruction, "
            "quick format, or reliance on the lessor) is the correct way to render the prior data unrecoverable "
            "while meeting the lease's return condition."
        ),
    },
    {
        "id": "nd5b-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A company physically destroys a batch of decommissioned database servers but does not update its "
            "configuration management database (CMDB) or vulnerability-scanning scope to reflect their "
            "retirement. Three months later, the vulnerability management team is still generating alerts "
            "referencing these nonexistent hosts, and an auditor flags the discrepancy. What step was MISSING "
            "from the decommissioning process?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Updating the CMDB/asset inventory (and dependent tooling, such as the vulnerability "
                    "scanner's scope) to reflect the assets' retired status at the time of destruction"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Decommissioning must include updating the asset inventory and any dependent "
                    "tooling so records stay accurate — this step was skipped, causing the stale alerts."
                ),
            },
            {
                "id": "b",
                "text": "Obtaining a certificate of destruction from the vendor who performed the shredding",
                "correct": False,
                "rationale": (
                    "Incorrect. A certificate documents that destruction occurred but does not, by itself, "
                    "update internal inventory or scanning systems to reflect that fact."
                ),
            },
            {
                "id": "c",
                "text": "Conducting a fresh risk assessment of the destroyed servers before disposal",
                "correct": False,
                "rationale": (
                    "Incorrect. Risk assessment is a pre-decommissioning consideration; it does not resolve the "
                    "stale post-decommissioning inventory records causing the false alerts."
                ),
            },
            {
                "id": "d",
                "text": "Notifying the data protection officer (DPO) of the destruction event",
                "correct": False,
                "rationale": (
                    "Incorrect. DPO notification concerns regulatory/privacy obligations for personal data, not "
                    "the operational gap of stale asset records generating false vulnerability alerts."
                ),
            },
        ],
        "explanation": (
            "Proper decommissioning includes updating the CMDB and dependent tooling (like vulnerability "
            "scanner scope) at the time of destruction — a certificate of destruction, a pre-disposal risk "
            "assessment, or DPO notification do not, by themselves, close that gap."
        ),
    },
    {
        "id": "nd5b-038",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "A company's mandatory annual security awareness training covers phishing, password hygiene, and "
            "physical security for all staff. Post-incident review shows that the majority of the past year's "
            "actual security incidents involved developers committing API keys and credentials directly into "
            "public code repositories. What should the awareness program prioritize next?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Supplement the general training with role-specific training for developers on secure "
                    "coding practices and secrets management (e.g., using vaults, pre-commit secret-scanning "
                    "hooks)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Since the actual incident data points to a developer-specific workflow gap, "
                    "targeted role-based training on secure coding and secrets management directly addresses "
                    "the root cause."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the frequency of the existing general-audience training from annual to quarterly, "
                    "without changing its content"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Repeating the same generic, non-technical content more often does not address "
                    "the specific developer-workflow gap that caused these incidents."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Discontinue general security awareness training entirely and rely solely on automated "
                    "secret-scanning tools"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Eliminating human training removes a complementary layer of defense; automated "
                    "tooling alone doesn't build developer understanding of secure practices."
                ),
            },
            {
                "id": "d",
                "text": "Require developers to sign an updated acceptable use policy acknowledgment",
                "correct": False,
                "rationale": (
                    "Incorrect. A policy signature attesting the policy was read does not teach the specific "
                    "secure-coding and secrets-management skills needed to prevent this incident type."
                ),
            },
        ],
        "explanation": (
            "Awareness programs should be tailored to actual incident data. When incidents cluster around a "
            "specific role's workflow (here, developers and secrets management), targeted role-based training "
            "is the correct next investment, not generic frequency increases, eliminating training, or a policy "
            "sign-off."
        ),
    },
    {
        "id": "nd5b-039",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "After each phishing simulation, a manager publicly reads out, by name, the list of employees who "
            "clicked the simulated link during the all-hands meeting. Click-through rates have not improved, "
            "and the security team has noticed a further decline in employees voluntarily reporting suspicious "
            "emails. What change to the awareness program is MOST likely to help?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace the public callout with private, immediate, non-punitive coaching/feedback for "
                    "individuals who click, paired with recognition for those who correctly report phishing "
                    "attempts"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Removing the punitive public shaming and replacing it with private coaching plus "
                    "positive reinforcement for reporting directly addresses the behavior decline the security "
                    "team observed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the difficulty and frequency of the phishing simulations without changing the "
                    "feedback approach"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Harder or more frequent tests, without fixing the punitive feedback loop, are "
                    "likely to further discourage reporting rather than improve it."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Continue the public callout but also publish a company-wide leaderboard ranking each "
                    "employee individually by number of clicks"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This intensifies the public-shaming dynamic already shown to be counterproductive, "
                    "rather than correcting it."
                ),
            },
            {
                "id": "d",
                "text": "Eliminate phishing simulations entirely, since they have not produced measurable improvement",
                "correct": False,
                "rationale": (
                    "Incorrect. The simulations themselves are not the core problem; the punitive public-"
                    "shaming feedback approach is what is suppressing reporting behavior."
                ),
            },
        ],
        "explanation": (
            "Punitive, public feedback tends to suppress reporting behavior and does not improve outcomes. "
            "Replacing it with private, non-punitive coaching and positive reinforcement for reporting is the "
            "corrective approach, not harsher tests, intensified shaming, or eliminating simulations altogether."
        ),
    },
    {
        "id": "nd5b-040",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "Select the TWO metrics that BEST measure genuine behavior change from a security awareness "
            "program, beyond simply tracking the phishing simulation click-through rate."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The rate and speed at which employees report suspicious emails (including simulated "
                    "phishing) to the security team"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Reporting rate and speed directly measure whether employees are actively applying "
                    "training to detect and escalate threats, not just avoiding a single test link."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Trends in real-world incidents caused by user behavior (e.g., credential compromise, "
                    "policy violations) over time"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Tracking actual behavior-driven incidents over time shows whether training is "
                    "translating into fewer real-world security failures, a direct measure of program impact."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The total number of training hours logged in the learning management system, regardless "
                    "of assessment results"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hours logged measures completion or attendance, not whether employees' actual "
                    "behavior or judgment changed as a result."
                ),
            },
            {
                "id": "d",
                "text": "The total number of security policies published by the organization during the year",
                "correct": False,
                "rationale": (
                    "Incorrect. This is an output of the governance program itself, not a measure of employee "
                    "behavior change resulting from awareness training."
                ),
            },
        ],
        "explanation": (
            "Meaningful awareness metrics track behavior — reporting rate/speed and real-world incident trends "
            "— rather than pure activity/output measures like training hours logged or policies published."
        ),
    },
]
