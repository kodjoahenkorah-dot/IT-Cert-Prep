"""CompTIA Security+ SY0-701 practice questions -- Domain 5 (Security Program
Management and Oversight), file F.

45 scenario-driven questions (41 multiple_choice + 4 multiple_response)
covering every study_topic label listed under domain 5 in
``_topic_labels.json``.
"""

QUESTIONS = [
    {
        "id": "nd5f-001",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A regional grocery chain's loyalty-rewards database is valued at $540,000 (asset value, AV). "
            "Security engineers estimate that a successful SQL injection attack against the database would "
            "corrupt or expose approximately 40% of its value (exposure factor, EF) before containment. "
            "What is the single loss expectancy (SLE) for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$216,000",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $540,000 x 0.40 = $216,000, the expected loss from one "
                    "occurrence of the event."
                ),
            },
            {
                "id": "b",
                "text": "$324,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the complement of the exposure factor (60%) instead of the "
                    "stated 40% EF ($540,000 x 0.60), which represents the retained value, not the loss."
                ),
            },
            {
                "id": "c",
                "text": "$540,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the full asset value with the exposure factor ignored entirely, as "
                    "if the entire database were destroyed."
                ),
            },
            {
                "id": "d",
                "text": "$1,350,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This comes from dividing AV by EF ($540,000 / 0.40) rather than multiplying, "
                    "producing a figure larger than the asset itself, which cannot be a valid SLE."
                ),
            },
        ],
        "explanation": (
            "SLE = Asset Value (AV) x Exposure Factor (EF). Here, $540,000 x 0.40 = $216,000. EF must be "
            "multiplied directly against AV, not subtracted from 1, ignored, or divided into AV."
        ),
    },
    {
        "id": "nd5f-002",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A single loss expectancy (SLE) of $72,000 has been calculated for a warehouse robotics "
            "control-system tampering incident at an e-commerce fulfillment company. Historical telemetry "
            "shows this type of incident occurs, on average, once every 6 years. What is the annualized "
            "loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$12,000",
                "correct": True,
                "rationale": (
                    "Correct. ARO = 1 event / 6 years = 0.1667. ALE = SLE x ARO = $72,000 x 0.1667 = "
                    "$12,000."
                ),
            },
            {
                "id": "b",
                "text": "$432,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from dividing SLE by ARO ($72,000 / 0.1667) instead of "
                    "multiplying, inflating the figure far beyond the single-loss amount."
                ),
            },
            {
                "id": "c",
                "text": "$72,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This treats ALE as identical to SLE, ignoring the annualized rate of "
                    "occurrence entirely."
                ),
            },
            {
                "id": "d",
                "text": "$1,200",
                "correct": False,
                "rationale": (
                    "Incorrect. This results from misreading 'once every 6 years' as an ARO of 0.0167 (as "
                    "if it were once every 60 years) instead of the correct 0.1667 (1/6)."
                ),
            },
        ],
        "explanation": (
            "ALE = SLE x ARO. 'Once every 6 years' converts to ARO = 1/6 = 0.1667. $72,000 x 0.1667 = "
            "$12,000."
        ),
    },
    {
        "id": "nd5f-003",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "Before mitigation, the ALE for an unpatched contamination-monitoring sensor network at a "
            "semiconductor fabrication plant is $150,000/year. A proposed control (annual cost of "
            "safeguard, ACS, of $55,000) would reduce the post-mitigation ALE to $60,000/year. Using the "
            "cost-benefit formula (ALE before - ALE after - ACS), what is the value of this control, and "
            "is it financially justified?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$35,000; yes, the control is justified because it saves more than it costs",
                "correct": True,
                "rationale": (
                    "Correct. $150,000 - $60,000 - $55,000 = $35,000. Since the result is positive, the "
                    "control's risk reduction exceeds its annual cost, so it is financially justified."
                ),
            },
            {
                "id": "b",
                "text": "$90,000; yes, the control is justified",
                "correct": False,
                "rationale": (
                    "Incorrect. This is only ALE-before minus ALE-after ($150,000 - $60,000) with the ACS "
                    "never subtracted, overstating the true value of the control."
                ),
            },
            {
                "id": "c",
                "text": "$95,000; yes, the control is justified",
                "correct": False,
                "rationale": (
                    "Incorrect. This subtracts only the ACS from the pre-mitigation ALE ($150,000 - "
                    "$55,000) while ignoring the post-mitigation ALE entirely, overstating the benefit."
                ),
            },
            {
                "id": "d",
                "text": "-$35,000; no, the control is not justified",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the sign of the correctly computed $35,000 result, which "
                    "flips a cost-justified control into an apparently unjustified one."
                ),
            },
        ],
        "explanation": (
            "Value of control = ALE(before) - ALE(after) - ACS = $150,000 - $60,000 - $55,000 = $35,000. "
            "A positive value means the control is cost-justified."
        ),
    },
    {
        "id": "nd5f-004",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Quantitative risk analysis (SLE/ALE/ARO)",
        "stem": (
            "A satellite communications operator's ground-station control asset is valued at $2,600,000 "
            "(AV). Analysts estimate a signal-jamming attack would require replacing or recalibrating "
            "approximately 15% of the asset's value (EF), and such attacks are projected to occur once "
            "every 4 years on average. What is the annualized loss expectancy (ALE)?"
        ),
        "options": [
            {
                "id": "a",
                "text": "$97,500",
                "correct": True,
                "rationale": (
                    "Correct. SLE = AV x EF = $2,600,000 x 0.15 = $390,000. ARO = 1/4 = 0.25. ALE = SLE x "
                    "ARO = $390,000 x 0.25 = $97,500."
                ),
            },
            {
                "id": "b",
                "text": "$390,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This is the SLE ($2,600,000 x 0.15) with the annualized rate of occurrence "
                    "never applied, effectively assuming the attack happens every year."
                ),
            },
            {
                "id": "c",
                "text": "$1,560,000",
                "correct": False,
                "rationale": (
                    "Incorrect. This misreads 'once every 4 years' as an ARO of 4 (as if the attack occurs "
                    "4 times per year) instead of the correct ARO of 0.25 ($390,000 x 4)."
                ),
            },
            {
                "id": "d",
                "text": "$552,500",
                "correct": False,
                "rationale": (
                    "Incorrect. This applies the complement of the exposure factor (85%) to compute SLE "
                    "($2,600,000 x 0.85 x 0.25) instead of the stated 15% EF."
                ),
            },
        ],
        "explanation": (
            "ALE = AV x EF x ARO. Here, $2,600,000 x 0.15 x 0.25 = $97,500. Each factor must be applied "
            "exactly as stated, not inverted, ignored, or substituted."
        ),
    },
    {
        "id": "nd5f-005",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A fleet of 25 identical rooftop solar-farm inverters logged a combined total of 219,000 "
            "operating hours over one year, during which 6 inverters failed and were replaced. Based on "
            "this data, what is the mean time between failures (MTBF) for this inverter model?"
        ),
        "options": [
            {
                "id": "a",
                "text": "36,500 hours",
                "correct": True,
                "rationale": (
                    "Correct. MTBF = total operating hours / number of failures = 219,000 / 6 = 36,500 "
                    "hours."
                ),
            },
            {
                "id": "b",
                "text": "8,760 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This is simply the number of hours in one year (24 x 365), ignoring both "
                    "the fleet size and the failure count entirely."
                ),
            },
            {
                "id": "c",
                "text": "1,314,000 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This multiplies total operating hours by the failure count (219,000 x 6) "
                    "instead of dividing, producing a nonsensical result larger than the total hours logged."
                ),
            },
            {
                "id": "d",
                "text": "43,800 hours",
                "correct": False,
                "rationale": (
                    "Incorrect. This divides total operating hours by the fleet size (219,000 / 5, using "
                    "an incorrect count of 5) rather than by the actual number of failures (6)."
                ),
            },
        ],
        "explanation": (
            "MTBF = total operating hours across the fleet / number of failures during the period. "
            "219,000 / 6 = 36,500 hours."
        ),
    },
    {
        "id": "nd5f-006",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A genomics sequencing lab's BIA sets a recovery point objective (RPO) of 30 minutes for its "
            "sample-tracking database, which links physical specimens to sequencing results. Which backup "
            "strategy BEST satisfies this RPO?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Continuous transaction log shipping (or near-synchronous replication) to a standby "
                    "database"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Continuous log shipping/near-synchronous replication keeps data loss on the "
                    "order of seconds to a few minutes, comfortably meeting a 30-minute RPO."
                ),
            },
            {
                "id": "b",
                "text": "Full backups taken once every 24 hours during a nightly maintenance window",
                "correct": False,
                "rationale": (
                    "Incorrect. A nightly-only backup could lose up to 24 hours of specimen-tracking data, "
                    "far exceeding the 30-minute RPO."
                ),
            },
            {
                "id": "c",
                "text": "Weekly full backups supplemented by daily differential backups",
                "correct": False,
                "rationale": (
                    "Incorrect. This still leaves up to a full day of potential data loss between "
                    "differential backups, which does not meet a 30-minute RPO."
                ),
            },
            {
                "id": "d",
                "text": "A quarterly offsite tape backup rotation",
                "correct": False,
                "rationale": (
                    "Incorrect. Quarterly tape backups could lose months of sample-tracking linkage data, "
                    "which is unacceptable and unrelated to the stated RPO."
                ),
            },
        ],
        "explanation": (
            "RPO defines the maximum tolerable data loss measured in time. A 30-minute RPO requires very "
            "frequent, near-continuous data protection such as log shipping or near-synchronous "
            "replication -- not periodic full/differential backups."
        ),
    },
    {
        "id": "nd5f-007",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "A drone-delivery company's BIA determines that the maximum tolerable downtime (MTD) for its "
            "flight-authorization platform is 6 hours before the business suffers unacceptable regulatory "
            "and safety consequences. The current disaster recovery plan, however, is only capable of "
            "restoring the platform within 8 hours (RTO). What should the security team recommend?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Invest in recovery capabilities (e.g., a warmer standby site or faster failover) so "
                    "the actual RTO is brought below the 6-hour MTD"
                ),
                "correct": True,
                "rationale": (
                    "Correct. RTO must always be less than or equal to MTD; an 8-hour RTO against a 6-hour "
                    "MTD means the current recovery capability cannot prevent unacceptable harm, so "
                    "recovery capability must be improved."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Formally revise the MTD upward to 8 hours so it matches the current RTO and close the "
                    "gap on paper"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. MTD reflects the business/safety threshold beyond which harm becomes "
                    "unacceptable; it is derived from operational and regulatory reality, not adjusted "
                    "simply to make an inadequate RTO look compliant."
                ),
            },
            {
                "id": "c",
                "text": "Accept the gap, since RTO and MTD are unrelated planning metrics",
                "correct": False,
                "rationale": (
                    "Incorrect. RTO and MTD are directly related -- RTO is the recovery target that must "
                    "fit within the MTD ceiling -- so an RTO that exceeds MTD is a critical planning gap, "
                    "not something to ignore."
                ),
            },
            {
                "id": "d",
                "text": "Shorten the RPO to compensate for the longer RTO",
                "correct": False,
                "rationale": (
                    "Incorrect. RPO governs acceptable data loss, not downtime duration; tightening RPO "
                    "does nothing to close the gap between an 8-hour RTO and a 6-hour MTD."
                ),
            },
        ],
        "explanation": (
            "MTD is the outer boundary of tolerable downtime; RTO is the planned/actual recovery target "
            "and must be less than or equal to MTD. When RTO exceeds MTD, the organization must improve "
            "recovery capability, not redefine the business tolerance to fit current performance."
        ),
    },
    {
        "id": "nd5f-008",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Business impact analysis (RTO/RPO/MTTR/MTBF)",
        "stem": (
            "During an airport's BIA, the baggage-handling control system is assigned an RTO of 2 hours, "
            "while the terminal's public guest Wi-Fi network is assigned an RTO of 24 hours. What is the "
            "PRIMARY justification for assigning these two systems such different RTOs?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Criticality to safety and operations: baggage handling directly affects flight "
                    "operations and passenger safety, while guest Wi-Fi is a convenience service with "
                    "minimal operational impact if unavailable"
                ),
                "correct": True,
                "rationale": (
                    "Correct. BIA-derived RTOs are set according to each system's criticality to core "
                    "business operations and safety; baggage handling is mission-critical, while guest "
                    "Wi-Fi is a low-impact amenity that can tolerate a much longer outage."
                ),
            },
            {
                "id": "b",
                "text": "Guest Wi-Fi uses newer hardware, so it inherently requires a longer RTO",
                "correct": False,
                "rationale": (
                    "Incorrect. RTO assignment is driven by business impact and criticality, not by the "
                    "relative age or technical modernity of the underlying hardware."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The two systems must always share an identical RTO because they are both hosted at "
                    "the same physical airport facility"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical co-location does not require identical RTOs; each system's RTO is "
                    "set independently based on its own business impact, which is why differentiated "
                    "(tiered) RTOs are standard practice in a BIA."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Regulatory bodies mandate a fixed 2-hour RTO for every airport IT system regardless of "
                    "function"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no blanket regulatory RTO applied uniformly to every airport "
                    "system; RTOs are tailored per system based on its individual business impact."
                ),
            },
        ],
        "explanation": (
            "A BIA tiers RTOs according to each system's criticality: mission-critical, safety-affecting "
            "systems receive aggressive (short) RTOs, while low-impact convenience services can tolerate "
            "much longer recovery windows."
        ),
    },
    {
        "id": "nd5f-009",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two agritech companies agree to jointly develop a soil-moisture sensor product, formally "
            "documenting how profits and losses will be split, which company contributes which resources, "
            "and how disputes between the partners will be resolved. Which type of agreement is BEST "
            "suited to this arrangement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Business partnership agreement (BPA)",
                "correct": True,
                "rationale": (
                    "Correct. A BPA is specifically designed to formalize a business partnership, "
                    "including how partners share profits, losses, responsibilities, and dispute-resolution "
                    "procedures -- exactly the terms described here."
                ),
            },
            {
                "id": "b",
                "text": "Service level agreement (SLA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An SLA defines measurable service performance commitments (e.g., uptime, "
                    "response time) between a provider and customer, not profit/loss sharing or "
                    "partnership governance."
                ),
            },
            {
                "id": "c",
                "text": "Memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU documents a general, typically non-binding intent to cooperate; it "
                    "is not designed to formalize binding profit/loss splits or partnership dispute "
                    "resolution the way a BPA is."
                ),
            },
            {
                "id": "d",
                "text": "Master service agreement (MSA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MSA establishes recurring baseline terms (payment, liability, "
                    "confidentiality) for a customer-vendor relationship across future work orders, not a "
                    "profit-sharing partnership between co-developers."
                ),
            },
        ],
        "explanation": (
            "A business partnership agreement (BPA) formalizes the terms of a business partnership, "
            "including profit/loss sharing, resource contributions, and dispute resolution between the "
            "partnering organizations."
        ),
    },
    {
        "id": "nd5f-010",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "A theme park operator has a signed master service agreement (MSA) with a physical security "
            "consulting firm that establishes standard payment terms, confidentiality obligations, and "
            "liability limits applicable to all future engagements. The operator now wants the firm to "
            "perform a specific penetration test of the park's ticketing kiosks next month. Which "
            "additional document should define the scope, deliverables, timeline, and cost of THIS "
            "specific engagement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A statement of work (SOW)",
                "correct": True,
                "rationale": (
                    "Correct. An SOW defines the specific scope, deliverables, timeline, and cost for an "
                    "individual engagement performed under the umbrella terms already established by the "
                    "MSA."
                ),
            },
            {
                "id": "b",
                "text": "A new MSA replacing the existing one",
                "correct": False,
                "rationale": (
                    "Incorrect. The existing MSA already governs the ongoing relationship's baseline terms; "
                    "there is no need to replace it just to scope a single engagement -- that is precisely "
                    "the purpose of an SOW."
                ),
            },
            {
                "id": "c",
                "text": "A memorandum of understanding (MOU)",
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU expresses non-binding mutual intent between parties; it does not "
                    "define billable scope, deliverables, or cost for a specific paid engagement under an "
                    "existing contract."
                ),
            },
            {
                "id": "d",
                "text": "A business partnership agreement (BPA)",
                "correct": False,
                "rationale": (
                    "Incorrect. A BPA formalizes a joint business partnership with shared profit/loss, "
                    "which does not describe a vendor performing a discrete, billed penetration test under "
                    "an existing MSA."
                ),
            },
        ],
        "explanation": (
            "Under an MSA-based vendor relationship, each individual project's scope, deliverables, "
            "timeline, and cost are defined in a statement of work (SOW), while the MSA continues to "
            "govern the overarching legal and commercial terms."
        ),
    },
    {
        "id": "nd5f-011",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Third-party agreements (SLA/MOU/MSA/BPA)",
        "stem": (
            "Two state university library systems want to formally document their mutual intent to share "
            "digitized archive access with each other, without creating a legally binding, penalty-bearing "
            "contract. Select the TWO characteristics that are typically true of the memorandum of "
            "understanding (MOU) they should use."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It expresses a mutual intent to cooperate and generally carries lower legal "
                    "enforceability than a fully binding contract"
                ),
                "correct": True,
                "rationale": (
                    "Correct. An MOU is typically used to document good-faith intent to cooperate and "
                    "carries less legal weight than a fully binding, penalty-enforced contract."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It is commonly used between two organizations, including public/government entities, "
                    "to formalize a cooperative relationship without the financial penalty clauses found in "
                    "commercial contracts"
                ),
                "correct": True,
                "rationale": (
                    "Correct. MOUs are frequently used between public institutions (such as universities) "
                    "to document cooperative arrangements without imposing binding financial penalties for "
                    "non-performance."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It legally guarantees specific, measurable performance metrics enforceable through "
                    "financial penalties, identical to an SLA"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU does not typically include enforceable, penalty-backed performance "
                    "metrics; that level of enforceability is characteristic of an SLA, not an MOU."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It permanently supersedes and replaces the need for any future formal contract between "
                    "the two organizations"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An MOU does not preclude or replace future formal, binding contracts; "
                    "organizations often follow an MOU with a more detailed contract if the relationship "
                    "expands."
                ),
            },
        ],
        "explanation": (
            "An MOU documents mutual intent to cooperate, is common between public/government entities, "
            "and generally carries lower legal enforceability than a binding contract -- it does not "
            "guarantee penalty-backed performance metrics or replace the need for future formal contracts."
        ),
    },
    {
        "id": "nd5f-012",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Vendor risk management",
        "stem": (
            "A title insurance and escrow company hears an unconfirmed rumor that its property-appraisal "
            "software vendor suffered a breach. The existing contract includes a right-to-audit clause. "
            "What should the escrow company do FIRST?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Formally invoke the right-to-audit clause to independently verify the vendor's current "
                    "security posture and confirm or rule out a breach"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The right-to-audit clause exists precisely for situations like this: it lets "
                    "the customer independently verify the vendor's security posture rather than relying on "
                    "unconfirmed rumor or the vendor's self-reporting alone."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Immediately terminate the contract without contacting the vendor, since any breach "
                    "rumor justifies unilateral termination"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Terminating an unconfirmed relationship without verification is premature "
                    "and could breach the contract itself; the right-to-audit clause is the appropriate "
                    "mechanism to confirm facts first."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Wait for the vendor's next scheduled annual security assessment, since rumors do not "
                    "warrant an out-of-cycle review"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A credible breach rumor involving a vendor with access to sensitive escrow "
                    "data warrants prompt investigation, not deferral to a routine annual cycle that may be "
                    "months away."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Disregard the rumor entirely unless the vendor proactively discloses an incident, since "
                    "unverified rumors do not warrant action"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Relying solely on the vendor to self-report ignores the customer's own "
                    "contractual right and due-diligence responsibility to verify vendor security when "
                    "credible concerns arise."
                ),
            },
        ],
        "explanation": (
            "A right-to-audit clause gives a customer the contractual ability to independently verify a "
            "vendor's security controls. Credible concerns -- even unconfirmed rumors involving sensitive "
            "data -- warrant prompt exercise of that clause rather than premature termination, passive "
            "waiting, or disregard."
        ),
    },
    {
        "id": "nd5f-013",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Vendor risk management",
        "stem": (
            "An amusement park's payment-processing vendor was last formally security-assessed three years "
            "ago, and the contract includes no requirement for continuous monitoring or periodic "
            "reassessment. What should the security team recommend?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Conduct an updated vendor risk assessment now and amend the contract to require "
                    "periodic reassessment or continuous monitoring going forward"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Vendor risk is not static; a three-year-old assessment with no ongoing "
                    "monitoring leaves the organization blind to changes in the vendor's security posture, "
                    "so both a refreshed assessment and an ongoing monitoring requirement are needed."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Rely on the original assessment, since a vendor that passed once can be assumed secure "
                    "indefinitely"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Security postures change over time (new systems, staff turnover, emerging "
                    "threats); a point-in-time assessment does not remain valid indefinitely, especially for "
                    "a payment-processing vendor handling sensitive financial data."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require the vendor to obtain cyber-insurance coverage instead of undergoing "
                    "reassessment"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance transfers financial impact after a loss occurs; it does not "
                    "provide visibility into or reduce the likelihood of the vendor's current security "
                    "weaknesses, which is what an updated assessment addresses."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Terminate the vendor relationship immediately, since any assessment older than one year "
                    "automatically disqualifies a vendor"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An outdated assessment is a gap to remediate through reassessment, not "
                    "automatic grounds for termination; termination is disproportionate without evidence of "
                    "an actual security failure."
                ),
            },
        ],
        "explanation": (
            "Vendor risk management is an ongoing lifecycle, not a one-time gate. Stale assessments should "
            "be refreshed and contracts should require periodic reassessment or continuous monitoring so "
            "risk visibility does not degrade over time."
        ),
    },
    {
        "id": "nd5f-014",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Vendor risk management",
        "stem": (
            "A hospital system is selecting a telehealth video-visit vendor. Select the TWO factors that "
            "should weigh MOST heavily during the vendor's initial risk tiering."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The sensitivity and volume of protected health information (PHI) the vendor will "
                    "access, store, or transmit during video visits"
                ),
                "correct": True,
                "rationale": (
                    "Correct. The type and amount of sensitive data a vendor touches is a primary driver of "
                    "vendor risk tier -- a telehealth vendor handling PHI warrants a higher tier than one "
                    "handling only non-sensitive data."
                ),
            },
            {
                "id": "b",
                "text": (
                    "How deeply the vendor's service is integrated into critical clinical workflows and "
                    "systems, and the impact if that integration fails or is compromised"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Criticality of the vendor's role in essential business/clinical processes is "
                    "a core risk-tiering factor; a vendor embedded in patient-care workflows poses higher "
                    "risk than a peripheral, non-critical tool."
                ),
            },
            {
                "id": "c",
                "text": "The color scheme and visual branding of the vendor's user interface",
                "correct": False,
                "rationale": (
                    "Incorrect. Interface aesthetics have no bearing on security or privacy risk and play "
                    "no role in vendor risk tiering."
                ),
            },
            {
                "id": "d",
                "text": (
                    "How many years the vendor's marketing department has existed as a registered business "
                    "entity"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Corporate age of a marketing department is not a meaningful indicator of "
                    "security risk and is not a standard vendor risk-tiering criterion."
                ),
            },
        ],
        "explanation": (
            "Vendor risk tiering is PRIMARILY driven by the sensitivity/volume of data the vendor touches "
            "and the criticality of the vendor's integration into essential business processes -- not by "
            "cosmetic or unrelated factors."
        ),
    },
    {
        "id": "nd5f-015",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Risk management strategies",
        "stem": (
            "After repeated fraudulent chargebacks tied to cryptocurrency donations, a museum's leadership "
            "decides to stop accepting cryptocurrency donations altogether rather than invest in additional "
            "fraud-detection controls. Which risk management strategy does this decision represent?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Risk avoidance",
                "correct": True,
                "rationale": (
                    "Correct. Eliminating the activity that creates the risk entirely -- discontinuing "
                    "cryptocurrency donations -- is risk avoidance, not simply reducing or transferring the "
                    "exposure."
                ),
            },
            {
                "id": "b",
                "text": "Risk mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mitigation would mean implementing controls (e.g., stronger fraud "
                    "detection) to reduce the risk of the activity while continuing it, which is the "
                    "opposite of what the museum chose to do."
                ),
            },
            {
                "id": "c",
                "text": "Risk transference",
                "correct": False,
                "rationale": (
                    "Incorrect. Transference shifts financial impact to a third party (e.g., insurance or a "
                    "payment processor assuming liability) while the activity continues; the museum instead "
                    "stopped the activity entirely."
                ),
            },
            {
                "id": "d",
                "text": "Risk acceptance",
                "correct": False,
                "rationale": (
                    "Incorrect. Acceptance means knowingly continuing to bear a risk without further action; "
                    "the museum took affirmative action to eliminate the risk-bearing activity instead."
                ),
            },
        ],
        "explanation": (
            "Risk avoidance eliminates the risk by discontinuing the activity or process that creates it -- "
            "here, ceasing cryptocurrency donations entirely, rather than reducing (mitigation), shifting "
            "(transference), or tolerating (acceptance) the risk."
        ),
    },
    {
        "id": "nd5f-016",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk management strategies",
        "stem": (
            "A craft brewery chain purchases a $2 million cyber-insurance policy after a competitor "
            "suffered a costly ransomware incident. The CFO tells the board that the brewery's cyber risk "
            "is now fully addressed. Which statement BEST evaluates this claim?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The claim is inaccurate; insurance transfers financial impact but does not reduce the "
                    "likelihood of an incident or cover uninsurable harms such as reputational damage, "
                    "regulatory penalties, or losses beyond policy limits and exclusions"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Insurance is a risk-transference tool for financial impact within policy "
                    "limits; it does nothing to reduce the probability of an attack and typically excludes "
                    "or caps coverage for reputational harm, certain regulatory fines, and losses above the "
                    "policy limit, so residual risk remains."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The claim is accurate, since purchasing any cyber-insurance policy eliminates all forms "
                    "of cyber risk by definition"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Insurance never eliminates risk; it transfers a portion of the financial "
                    "consequences, subject to exclusions, deductibles, and coverage limits, while the "
                    "underlying vulnerability and non-financial harms remain."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The claim is accurate, because $2 million exceeds the brewery's total annual revenue "
                    "and therefore covers any conceivable loss"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Policy dollar amount alone does not guarantee coverage of every loss type; "
                    "exclusions (e.g., for certain attack vectors, war/nation-state carve-outs, or "
                    "regulatory fines) can leave significant losses uncovered regardless of the policy "
                    "limit."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The claim is inaccurate, but only because the brewery should have chosen risk "
                    "avoidance instead of any form of insurance"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The problem is not that insurance was chosen instead of avoidance; it is "
                    "that insurance alone does not address likelihood reduction or every category of harm -- "
                    "it should complement, not replace, mitigating controls."
                ),
            },
        ],
        "explanation": (
            "Cyber insurance transfers financial impact within its terms; it does not reduce the likelihood "
            "of an incident and typically leaves reputational damage, certain regulatory penalties, and "
            "losses beyond policy limits/exclusions as residual, uninsured risk."
        ),
    },
    {
        "id": "nd5f-017",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Risk management strategies",
        "stem": (
            "A regional airport's legacy baggage-scanner controller cannot be patched against a known "
            "vulnerability without voiding the manufacturer's safety certification. The security team "
            "isolates the controller on a segmented VLAN with strict firewall rules and enhanced monitoring, "
            "and the airport's director of operations formally signs off on the remaining residual risk in "
            "writing. Which two risk management strategies are BOTH represented in this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Mitigation (the compensating controls) followed by acceptance (the formal sign-off)",
                "correct": True,
                "rationale": (
                    "Correct. Segmenting and monitoring the controller are compensating controls that "
                    "reduce risk (mitigation), and the director's documented sign-off on the remaining "
                    "exposure is a formal risk acceptance of what mitigation could not eliminate."
                ),
            },
            {
                "id": "b",
                "text": "Avoidance followed by transference",
                "correct": False,
                "rationale": (
                    "Incorrect. The airport did not eliminate the activity (avoidance) or shift financial "
                    "impact to a third party such as an insurer (transference); it reduced risk with "
                    "controls and then formally accepted the remainder."
                ),
            },
            {
                "id": "c",
                "text": "Transference followed by avoidance",
                "correct": False,
                "rationale": (
                    "Incorrect. No third party assumed financial responsibility, and the baggage-scanning "
                    "function was not discontinued, so neither transference nor avoidance describes this "
                    "scenario."
                ),
            },
            {
                "id": "d",
                "text": "Acceptance followed by mitigation",
                "correct": False,
                "rationale": (
                    "Incorrect. The order is reversed: the compensating controls (mitigation) were applied "
                    "first, and formal risk acceptance of the residual exposure came afterward, not before."
                ),
            },
        ],
        "explanation": (
            "Compensating controls (VLAN segmentation, firewall rules, monitoring) reduce risk (mitigation) "
            "when the vulnerability itself cannot be patched; a documented executive sign-off on the "
            "remaining exposure is a separate step -- formal risk acceptance."
        ),
    },
    {
        "id": "nd5f-018",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Risk management strategies",
        "stem": (
            "Select the TWO scenarios below that represent risk TRANSFERENCE, as opposed to avoidance, "
            "mitigation, or acceptance."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "A retailer outsources credit-card payment processing to a PCI DSS-compliant third "
                    "party, which contractually assumes liability for payment-data breaches"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Shifting both the processing function and the associated financial/legal "
                    "liability to a third party is a textbook example of risk transference."
                ),
            },
            {
                "id": "b",
                "text": "A company purchases a cyber-insurance policy to cover potential ransomware losses",
                "correct": True,
                "rationale": (
                    "Correct. Purchasing insurance shifts the financial impact of a potential loss to the "
                    "insurer, which is the defining characteristic of risk transference."
                ),
            },
            {
                "id": "c",
                "text": (
                    "A company deploys endpoint detection and response (EDR) software to reduce the "
                    "likelihood of successful ransomware execution"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Deploying a technical control to reduce likelihood or impact is risk "
                    "mitigation, not transference; no financial responsibility is shifted to a third party."
                ),
            },
            {
                "id": "d",
                "text": (
                    "A board formally documents its decision to continue operating a low-risk legacy "
                    "reporting tool without further investment, given its minimal exposure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Knowingly continuing to bear a risk without further action is risk "
                    "acceptance, not transference; nothing is shifted to another party."
                ),
            },
        ],
        "explanation": (
            "Risk transference shifts financial or legal responsibility for a risk to a third party -- "
            "through insurance or a contract that assigns liability -- unlike mitigation (reducing risk "
            "with controls) or acceptance (tolerating risk as-is)."
        ),
    },
    {
        "id": "nd5f-019",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "An underwater data-center operator's risk register entry for 'seawater cooling-loop sensor "
            "tampering' originally listed an inherent risk score of 20 (severe). After deploying tamper-"
            "evident sensor enclosures and redundant monitoring, the risk owner recalculates and records a "
            "residual risk score of 6 (low). What does this recalculation demonstrate?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The implemented controls measurably reduced risk from the pre-control (inherent) level "
                    "to the post-control (residual) level, and the register should be updated to reflect "
                    "the new residual score going forward"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Inherent risk reflects exposure before controls; residual risk reflects "
                    "exposure after controls are applied. A drop from 20 to 6 shows the tamper-evident "
                    "enclosures and redundant monitoring meaningfully reduced risk, and the register should "
                    "now track the residual score."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The inherent risk score of 20 should be deleted from the register entirely, since only "
                    "the current residual score matters going forward"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A well-formed risk register retains the inherent score alongside the "
                    "residual score to show the effect of controls over time; deleting historical inherent "
                    "risk data removes valuable context for future reviews and audits."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The risk has been fully eliminated and can be removed from the register, since a "
                    "residual score of 6 indicates zero remaining risk"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A residual score of 6 (low) still represents nonzero remaining risk; only a "
                    "score of zero (which is exceedingly rare) would justify removal from active tracking, "
                    "and even low risks are typically still monitored."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The controls were ineffective, since any register entry that still carries a nonzero "
                    "residual score after remediation indicates failed mitigation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A large reduction from 20 to 6 demonstrates the controls were highly "
                    "effective; expecting mitigation to always drive residual risk to exactly zero "
                    "misunderstands how risk treatment works in practice."
                ),
            },
        ],
        "explanation": (
            "Risk registers track both inherent risk (before controls) and residual risk (after controls). "
            "A significant reduction between the two demonstrates control effectiveness; it does not mean "
            "the risk is eliminated or that historical inherent-risk data should be discarded."
        ),
    },
    {
        "id": "nd5f-020",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Risk register & appetite",
        "stem": (
            "An online sports-betting platform's board has published a formal risk appetite statement "
            "capping acceptable individual risk exposure at a residual score of 8 (on a 1-25 scale). The "
            "CFO wants to launch a new instant-payout feature carrying a calculated residual risk score of "
            "14, arguing the revenue opportunity justifies the exception. What is the BEST way to handle "
            "this situation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Log the risk in the risk register and route it through a formal governance exception "
                    "process requiring explicit, documented approval from a level of authority empowered to "
                    "exceed the board's stated appetite"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A risk that exceeds the board-defined appetite threshold cannot simply be "
                    "approved by an individual executive informally; it must go through a documented "
                    "exception/escalation process to a governance body with the authority to knowingly "
                    "exceed the stated appetite."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Allow the CFO to approve the exception unilaterally, since revenue-generating features "
                    "are automatically exempt from the board's risk appetite statement"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Revenue potential does not create an automatic exemption from board-approved "
                    "risk appetite; exceeding the threshold requires formal, documented governance approval, "
                    "not unilateral executive override."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Quietly launch the feature without recording it in the risk register, since a score of "
                    "14 would embarrass the CFO if formally documented"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Omitting a known, above-appetite risk from the register undermines the "
                    "entire purpose of risk governance and leaves the organization unable to track or "
                    "manage a risk it knows about."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Automatically cancel the feature, since any risk above the stated appetite threshold "
                    "must always be rejected outright with no possibility of exception"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Risk appetite statements typically allow for documented, governed "
                    "exceptions when justified; an automatic, no-exception rejection ignores the legitimate "
                    "exception process most governance frameworks provide."
                ),
            },
        ],
        "explanation": (
            "When a proposed risk exceeds the board's stated risk appetite, the correct response is a "
            "formal, documented exception process with approval from an authority empowered to accept "
            "above-appetite risk -- not silent omission, unilateral approval, or automatic rejection."
        ),
    },
    {
        "id": "nd5f-021",
        "domain": 5,
        "objective": "5.2",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Risk register & appetite",
        "stem": (
            "During a risk register review at a pharmaceutical clinical-supply logistics firm, an internal "
            "auditor finds several high-severity entries -- including 'temperature-excursion sensor "
            "failure on cold-chain shipments' -- that list a risk description, a likelihood, and an impact "
            "score, but no assigned individual accountable for tracking and driving remediation. What is "
            "the MOST significant consequence of this gap?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Without a named risk owner, there is no clear accountability for ensuring the risk is "
                    "actively monitored, treated, and reported on, so it can stall indefinitely without "
                    "anyone being responsible"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A risk owner is the individual accountable for tracking a risk's status and "
                    "driving treatment to closure; without one, high-severity risks like cold-chain sensor "
                    "failures can remain unaddressed indefinitely because no single person is responsible."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The risk score calculation itself becomes mathematically invalid whenever an owner "
                    "field is blank"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The likelihood and impact scoring used to calculate risk score is "
                    "independent of whether an owner has been assigned; a missing owner is an accountability "
                    "gap, not a mathematical one."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Regulators automatically consider any risk register missing an owner field to be legally "
                    "void and unusable for compliance purposes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no blanket rule voiding a risk register for a missing owner field; "
                    "the practical problem is the lack of accountability for remediation, not automatic "
                    "legal invalidation."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The risk is automatically reclassified as accepted by default once 90 days pass without "
                    "an assigned owner"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. There is no standard rule that a risk becomes 'accepted' by default after a "
                    "time period simply because no owner is assigned; that would require a documented, "
                    "deliberate acceptance decision, not an automatic default."
                ),
            },
        ],
        "explanation": (
            "A mature risk register assigns a specific owner accountable for tracking and driving each risk "
            "to resolution. Missing an owner creates an accountability gap that allows even severe risks to "
            "languish without anyone actively managing them."
        ),
    },
    {
        "id": "nd5f-022",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "A regional telecom ISP publishes a document requiring 'all customer authentication data must "
            "be encrypted using AES-256 at rest' and a separate document titled 'Encryption Implementation "
            "Procedure' that specifies the exact key-management tool, algorithm library, and key-rotation "
            "steps engineers must follow to comply. How should these two documents be correctly classified "
            "within the governance hierarchy?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The first is a standard (a mandatory, specific requirement), and the second is a "
                    "procedure (the detailed, step-by-step instructions for meeting that requirement)"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A standard specifies a mandatory, measurable requirement (AES-256 at rest); a "
                    "procedure provides the detailed, step-by-step instructions engineers follow to "
                    "implement that requirement -- exactly as described."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Both documents are policies, since any document that references encryption is "
                    "automatically classified as a policy"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A policy is a high-level statement of management intent and objectives; "
                    "neither document here is a broad policy statement -- one is a specific mandatory "
                    "requirement (standard) and the other is step-by-step instructions (procedure)."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The first is a guideline (an optional recommendation), and the second is a policy (a "
                    "high-level statement of intent)"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. 'Must be encrypted using AES-256' is mandatory language, not an optional "
                    "recommendation (guideline); and step-by-step implementation instructions are a "
                    "procedure, not a high-level policy statement."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The first is a procedure, and the second is a standard, since procedures are always "
                    "published before their corresponding standards"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the roles: the mandatory algorithm/requirement statement is "
                    "the standard, and the detailed implementation steps are the procedure; there is no rule "
                    "that procedures precede standards in publication order."
                ),
            },
        ],
        "explanation": (
            "In the governance hierarchy, a policy states high-level intent, a standard defines mandatory, "
            "specific requirements (e.g., AES-256), a procedure gives step-by-step implementation "
            "instructions, and a guideline offers optional recommendations."
        ),
    },
    {
        "id": "nd5f-023",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security governance & policies",
        "stem": (
            "A national park service's IT policy requires that all VPN gateway configuration changes be "
            "peer-reviewed and approved by someone other than the engineer who made the change before "
            "deployment. An auditor discovers that a single network engineer has, on multiple occasions, "
            "made a change and then approved their own change request using a secondary administrative "
            "account. Which governance principle has been violated?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Separation of duties",
                "correct": True,
                "rationale": (
                    "Correct. Separation of duties requires that no single individual can both make and "
                    "approve a sensitive change; using a secondary account to self-approve defeats the "
                    "control's purpose even though it technically involves 'two accounts.'"
                ),
            },
            {
                "id": "b",
                "text": "Least privilege",
                "correct": False,
                "rationale": (
                    "Incorrect. Least privilege concerns limiting each account's access to only what is "
                    "needed for its role; the issue here is that one person controls both ends of an "
                    "approval workflow, which is a separation-of-duties failure, not an over-privileging "
                    "issue."
                ),
            },
            {
                "id": "c",
                "text": "Job rotation",
                "correct": False,
                "rationale": (
                    "Incorrect. Job rotation involves periodically moving personnel between roles to surface "
                    "hidden fraud or errors; the scenario describes a single person circumventing an "
                    "approval control, not a rotation-related gap."
                ),
            },
            {
                "id": "d",
                "text": "Mandatory vacation",
                "correct": False,
                "rationale": (
                    "Incorrect. Mandatory vacation forces absence periods so that another person's review "
                    "can surface irregularities; it does not directly address one person using a second "
                    "account to approve their own change."
                ),
            },
        ],
        "explanation": (
            "Separation of duties requires that critical actions (making and approving a change) be split "
            "between different individuals. An engineer using a secondary account to approve their own "
            "change defeats the intent of that control, regardless of the technical account boundary."
        ),
    },
    {
        "id": "nd5f-024",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "During an audit, a professional esports league discovers its incident response policy has not "
            "been formally reviewed or updated in five years, despite the league having since expanded into "
            "cloud-hosted tournament infrastructure and third-party streaming integrations not covered by "
            "the original document. What is the BEST recommendation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Establish (or enforce) a periodic policy review cycle, and update the incident response "
                    "policy now to reflect the current cloud and third-party streaming environment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Governance documents must be reviewed and updated on a periodic cycle to "
                    "remain relevant; a five-year-old policy that predates major infrastructure changes no "
                    "longer reflects the environment it is meant to govern and must be revised, with a "
                    "recurring review cadence established going forward."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Leave the policy unchanged, since incident response policies do not need to reflect "
                    "changes in underlying infrastructure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An incident response policy must reflect the actual environment it governs; "
                    "leaving it unrevised after major infrastructure changes (cloud hosting, third-party "
                    "streaming) leaves significant gaps in incident handling coverage."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Delete the policy entirely, since an outdated policy is worse than having no policy at "
                    "all"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Removing the policy entirely eliminates any governance baseline, including "
                    "the parts that remain valid; the correct action is to update and maintain it, not "
                    "discard it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Wait for the next major security incident to occur before revising the policy, so the "
                    "update can be based on real-world lessons learned"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Waiting for an actual incident before closing a known governance gap is "
                    "reactive and unnecessarily risky; the gap should be proactively remediated once "
                    "identified during the audit."
                ),
            },
        ],
        "explanation": (
            "Governance documents require periodic review and update cycles so they stay aligned with the "
            "current environment. A stale policy that predates significant infrastructure changes should be "
            "proactively revised, not deleted or left for a future incident to expose."
        ),
    },
    {
        "id": "nd5f-025",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_response",
        "difficulty": "medium",
        "study_topic": "Security governance & policies",
        "stem": (
            "A newly hired CISO is briefing the board on the organization's security governance structure. "
            "Select the TWO statements that correctly describe sound security governance practice."
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The board (or an equivalent governance committee) retains ultimate accountability for "
                    "the security program's risk posture, even though it delegates day-to-day execution to "
                    "the CISO and security team"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Ultimate accountability for organizational risk rests with the board/senior "
                    "governance body; delegation of operational execution to the CISO does not transfer "
                    "that ultimate accountability away from the board."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Security governance should establish clear roles, responsibilities, and reporting lines "
                    "so that policy exceptions and significant risk decisions are escalated to an "
                    "appropriate level of authority"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Effective governance defines who is responsible for what and ensures "
                    "significant decisions and exceptions are escalated to individuals or bodies with the "
                    "authority to make them, rather than being decided ad hoc."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Once the CISO is hired, the board has no further oversight role and can delegate all "
                    "accountability for security outcomes to that single individual"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Hiring a CISO delegates operational execution, not ultimate accountability; "
                    "the board retains an ongoing oversight responsibility for the organization's risk "
                    "posture."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Governance documents should remain static once approved, since revising them implies "
                    "the original version was flawed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Governance documents must be periodically reviewed and updated as the "
                    "business, threat landscape, and regulatory environment evolve; treating them as static "
                    "undermines the entire purpose of governance."
                ),
            },
        ],
        "explanation": (
            "Sound governance keeps ultimate accountability with the board while delegating execution, "
            "defines clear roles and escalation paths, and treats governance documents as living artifacts "
            "requiring periodic review -- not a one-time, unchangeable deliverable."
        ),
    },
    {
        "id": "nd5f-026",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A Canadian marketing analytics firm regularly receives personal data about EU residents from "
            "a European retail client so it can perform campaign analytics. Canada does not have an EU "
            "adequacy decision covering this type of transfer. Which mechanism should the two companies use "
            "to lawfully authorize this ongoing cross-border data transfer under GDPR?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Standard contractual clauses (SCCs) incorporated into the data transfer agreement",
                "correct": True,
                "rationale": (
                    "Correct. In the absence of an adequacy decision, GDPR permits cross-border transfers "
                    "when the parties adopt European Commission-approved standard contractual clauses that "
                    "impose GDPR-equivalent obligations on the data recipient."
                ),
            },
            {
                "id": "b",
                "text": (
                    "A simple verbal agreement between the two companies' marketing teams, since GDPR does "
                    "not require documentation for cross-border transfers"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR requires a documented, legally recognized transfer mechanism (such as "
                    "SCCs, binding corporate rules, or an adequacy decision) for transfers outside the "
                    "EU/EEA; an undocumented verbal agreement provides no such safeguard."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Reclassifying the personal data as anonymized data, which exempts it from GDPR transfer "
                    "restrictions regardless of its actual content"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Simply relabeling identifiable personal data as 'anonymized' without "
                    "actually irreversibly removing identifying elements does not exempt it from GDPR; "
                    "GDPR's transfer rules apply based on the data's actual identifiability, not its label."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Relying on the retailer's EU establishment alone, since a transfer mechanism is only "
                    "required when the RECEIVING company is located inside the EU"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR's cross-border transfer restrictions apply specifically when personal "
                    "data leaves the EU/EEA to a recipient in a country without an adequacy decision -- "
                    "exactly this scenario -- regardless of where the sending company is based."
                ),
            },
        ],
        "explanation": (
            "Without an adequacy decision for the destination country, GDPR requires an approved transfer "
            "mechanism such as standard contractual clauses (or binding corporate rules) to lawfully move "
            "personal data outside the EU/EEA."
        ),
    },
    {
        "id": "nd5f-027",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "An ad-tech company builds behavioral advertising profiles of EU website visitors and uses them "
            "to serve targeted marketing emails. An EU data subject formally notifies the company that they "
            "object to their data being used for direct marketing purposes. Under GDPR, what must the "
            "company do?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Immediately stop processing that individual's personal data for direct marketing "
                    "purposes, since the right to object to processing for direct marketing is absolute "
                    "under GDPR"
                ),
                "correct": True,
                "rationale": (
                    "Correct. GDPR grants an unconditional right to object to processing for direct "
                    "marketing purposes; unlike objections based on legitimate interest grounds, this right "
                    "cannot be overridden by the controller's own interests and must be honored immediately."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Continue processing the data for direct marketing as long as the company can "
                    "demonstrate a compelling legitimate business interest that outweighs the individual's "
                    "objection"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A 'compelling legitimate interest' override only applies to objections raised "
                    "under Article 21(1) for legitimate-interest-based processing; the right to object to "
                    "direct marketing specifically (Article 21(2)) is absolute and has no such override."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Require the individual to submit a formal erasure request instead, since an objection "
                    "alone is not a valid GDPR right"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The right to object is a distinct, explicitly enumerated GDPR right on its "
                    "own; the company must act on the objection directly and cannot demand the individual "
                    "file a different type of request instead."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Ignore the request unless the individual also revokes consent for all other forms of "
                    "processing, not just direct marketing"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. An objection to direct marketing is scoped specifically to that purpose; the "
                    "company must honor it for marketing use without requiring the individual to also "
                    "withdraw from unrelated processing activities."
                ),
            },
        ],
        "explanation": (
            "Under GDPR Article 21(2), a data subject's objection to processing for direct marketing "
            "purposes is absolute -- the controller must stop that processing immediately, with no "
            "legitimate-interest override available (unlike general Article 21(1) objections)."
        ),
    },
    {
        "id": "nd5f-028",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A mobile game publisher headquartered outside the EU discovers on a Wednesday morning that an "
            "attacker exfiltrated a database containing EU players' email addresses and in-game purchase "
            "histories. Under GDPR, by when must the publisher notify the relevant supervisory authority, "
            "absent an applicable exemption?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Within 72 hours of becoming aware of the breach",
                "correct": True,
                "rationale": (
                    "Correct. GDPR requires controllers to notify the relevant supervisory authority without "
                    "undue delay and, where feasible, within 72 hours of becoming aware of a personal data "
                    "breach, unless the breach is unlikely to result in risk to individuals."
                ),
            },
            {
                "id": "b",
                "text": "Within 30 calendar days, matching most U.S. state breach notification laws",
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR's own notification deadline is 72 hours from awareness, which is "
                    "considerably shorter than many U.S. state breach-notification timelines; the publisher "
                    "must follow GDPR's stricter standard for EU data subjects."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Only at the end of the current fiscal quarter, as part of routine regulatory reporting"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR breach notification is time-critical and tied to awareness of the "
                    "incident, not aligned to a company's internal fiscal reporting calendar."
                ),
            },
            {
                "id": "d",
                "text": (
                    "There is no notification deadline as long as the publisher is headquartered outside the "
                    "EU"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. GDPR applies extraterritorially to any organization processing EU residents' "
                    "personal data, regardless of where the organization is headquartered; the 72-hour "
                    "notification obligation still applies."
                ),
            },
        ],
        "explanation": (
            "GDPR requires notifying the relevant supervisory authority within 72 hours of becoming aware "
            "of a personal data breach (unless unlikely to result in risk to individuals), and this "
            "obligation applies extraterritorially to non-EU organizations processing EU residents' data."
        ),
    },
    {
        "id": "nd5f-029",
        "domain": 5,
        "objective": "5.3",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Compliance & privacy (GDPR)",
        "stem": (
            "A fitness wearable manufacturer wants to process users' continuous heart-rate and "
            "sleep-pattern data (special category health data under GDPR) to generate personalized coaching "
            "recommendations. Which lawful basis is MOST appropriate for this specific processing activity?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Explicit consent obtained specifically for this processing purpose",
                "correct": True,
                "rationale": (
                    "Correct. Special category data such as health data generally requires an additional, "
                    "heightened lawful basis under GDPR Article 9, and explicit consent specific to the "
                    "processing purpose is the most commonly applicable basis for optional, "
                    "consumer-facing health-related features like personalized coaching."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Legitimate interest, since the manufacturer's business goal of improving user engagement "
                    "is sufficient justification on its own for processing special category data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Legitimate interest is generally not sufficient on its own to justify "
                    "processing special category data such as health data; Article 9 requires one of its own "
                    "specific conditions (most commonly explicit consent) rather than the general Article 6 "
                    "legitimate interest basis."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Performance of a contract, since any data collected by a fitness product is automatically "
                    "necessary to fulfill the sales contract"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Contract necessity only covers data genuinely required to deliver the "
                    "core product/service; optional personalized coaching built on continuous health "
                    "metrics goes beyond what is strictly necessary for the sales contract and, as special "
                    "category data, still requires an Article 9 basis such as explicit consent."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Public task, since fitness and wellness are generally beneficial to public health "
                    "outcomes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The 'public task' basis applies to processing carried out by public "
                    "authorities or bodies performing an official function, not to a private wearable "
                    "manufacturer's commercial coaching feature."
                ),
            },
        ],
        "explanation": (
            "Processing special category data (such as health metrics) under GDPR requires an Article 9 "
            "condition, most commonly the data subject's explicit consent for that specific processing "
            "purpose -- general Article 6 bases like legitimate interest or contract necessity are not "
            "sufficient on their own."
        ),
    },
    {
        "id": "nd5f-030",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A prospective enterprise customer wants documented evidence that a cloud backup vendor's "
            "security controls were not only well-designed but ALSO operated effectively over the past nine "
            "months. Which assurance artifact should the vendor provide?"
        ),
        "options": [
            {
                "id": "a",
                "text": "A SOC 2 Type II report",
                "correct": True,
                "rationale": (
                    "Correct. A SOC 2 Type II report evaluates the operating effectiveness of controls over "
                    "an extended review period (here, nine months), which is exactly the evidence the "
                    "customer is requesting."
                ),
            },
            {
                "id": "b",
                "text": "A SOC 2 Type I report",
                "correct": False,
                "rationale": (
                    "Incorrect. A Type I report only assesses whether controls are suitably designed as of "
                    "a single point in time; it does not test whether those controls operated effectively "
                    "over any period, which is what the customer specifically asked for."
                ),
            },
            {
                "id": "c",
                "text": "A signed non-disclosure agreement (NDA)",
                "correct": False,
                "rationale": (
                    "Incorrect. An NDA only restricts disclosure of confidential information between "
                    "parties; it provides no independent evidence about the design or operating "
                    "effectiveness of the vendor's security controls."
                ),
            },
            {
                "id": "d",
                "text": "The vendor's internal, unaudited self-assessment checklist",
                "correct": False,
                "rationale": (
                    "Incorrect. A self-assessment lacks independent third-party verification; the customer "
                    "is asking for objective assurance, which requires an independent auditor's opinion "
                    "such as a SOC 2 Type II report."
                ),
            },
        ],
        "explanation": (
            "A SOC 2 Type II report is the assurance artifact that verifies controls operated effectively "
            "over an extended period, distinguishing it from a Type I report (design only, point in time) "
            "or unaudited self-attestations."
        ),
    },
    {
        "id": "nd5f-031",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A hospital contracts a penetration testing firm to assess its clinical network. Before testing "
            "begins, hospital leadership insists that certain networked infusion pumps and life-support "
            "equipment be explicitly listed as off-limits due to patient-safety concerns, even though those "
            "devices are technically reachable from the tested network segment. Which element of the rules "
            "of engagement (ROE) captures this requirement?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Exclusions (systems and assets explicitly out of scope for testing)",
                "correct": True,
                "rationale": (
                    "Correct. Exclusions in the ROE explicitly identify systems -- such as life-support "
                    "medical devices -- that testers must not touch, even if they are technically reachable "
                    "from in-scope network segments, precisely to prevent patient-safety incidents."
                ),
            },
            {
                "id": "b",
                "text": "The testing methodology (black box, gray box, or white box)",
                "correct": False,
                "rationale": (
                    "Incorrect. Testing methodology describes how much internal knowledge the testers are "
                    "given about the environment; it does not define which specific systems are forbidden "
                    "from being touched during the engagement."
                ),
            },
            {
                "id": "c",
                "text": "The engagement's disclosure/reporting timeline",
                "correct": False,
                "rationale": (
                    "Incorrect. The disclosure timeline governs when and how findings are reported after "
                    "testing concludes; it has no bearing on which live systems are excluded from testing "
                    "activity."
                ),
            },
            {
                "id": "d",
                "text": "The emergency contact and communication escalation plan",
                "correct": False,
                "rationale": (
                    "Incorrect. The emergency contact plan defines who to notify if something goes wrong "
                    "during testing; it is a separate ROE element from explicitly excluding specific "
                    "off-limits systems from the test scope entirely."
                ),
            },
        ],
        "explanation": (
            "Rules of engagement define exclusions -- systems explicitly placed off-limits, even if "
            "technically reachable -- separately from testing methodology, reporting timelines, and "
            "emergency contact procedures. Life-critical medical devices are a classic exclusion scenario."
        ),
    },
    {
        "id": "nd5f-032",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "A bank's compliance team engages an external regulatory examiner to verify the bank's adherence "
            "to specific PCI DSS control requirements, while separately its internal red team conducts an "
            "authorized simulated attack to determine whether those same systems can actually be "
            "compromised. Which statement BEST distinguishes these two activities?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The examiner's engagement is a compliance audit, verifying adherence to a defined "
                    "control framework; the red team's engagement is a penetration test, verifying whether "
                    "systems can actually be exploited despite those controls"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A compliance audit checks whether required controls from a specific framework "
                    "(here, PCI DSS) are documented and in place; a penetration test goes further by "
                    "actively attempting exploitation to determine real-world exploitability, regardless of "
                    "documented compliance."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Both activities are functionally identical, since both ultimately produce a written "
                    "report of findings"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Producing a written report does not make the two activities identical; their "
                    "purpose and methodology differ fundamentally -- one verifies framework adherence, the "
                    "other actively attempts exploitation."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The examiner's engagement is a penetration test, and the red team's engagement is a "
                    "compliance audit, since only external parties can legally perform penetration testing"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the roles, and there is no rule limiting penetration testing to "
                    "external parties only; internal red teams routinely perform authorized penetration "
                    "testing."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Compliance audits and penetration tests are mutually exclusive activities and can never "
                    "both apply to the same set of systems"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario itself shows both activities applying to the same systems "
                    "concurrently; organizations commonly undergo both compliance audits and penetration "
                    "tests against the same environment for different assurance purposes."
                ),
            },
        ],
        "explanation": (
            "A compliance audit verifies adherence to a specific framework's documented control "
            "requirements, while a penetration test actively attempts to exploit systems to determine "
            "real-world security effectiveness -- the two serve complementary but distinct purposes."
        ),
    },
    {
        "id": "nd5f-033",
        "domain": 5,
        "objective": "5.4",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Audits & penetration testing",
        "stem": (
            "An internal audit at a semiconductor fabrication plant samples 60 recent privileged-access "
            "reviews and finds that 15 of them (25%) were not completed on the schedule mandated by policy. "
            "What is the BEST immediate action for the audit team to recommend?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Document the finding as a control deficiency, determine the root cause of the missed "
                    "reviews, and require remediation with a defined corrective action plan and follow-up "
                    "verification"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A 25% non-compliance rate on a mandated control is a material finding; the "
                    "proper audit response is to formally document the deficiency, investigate the root "
                    "cause, and require a tracked corrective action plan with follow-up verification -- not "
                    "to dismiss it or take unilateral technical action."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Disregard the finding, since a 25% miss rate is within an acceptable margin of error for "
                    "any audit sample"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A 25% failure rate on a mandated privileged-access review control is a "
                    "significant compliance gap, not an acceptable margin of error; it warrants formal "
                    "documentation and remediation, not dismissal."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Have the audit team immediately revoke all privileged access across the organization "
                    "until every review is re-performed"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Auditors identify and report findings; they do not unilaterally take "
                    "disruptive operational action like mass access revocation, which is a decision for "
                    "system/process owners and could cause significant business disruption disproportionate "
                    "to the finding."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Lower the mandated review frequency in policy so future audits no longer flag missed "
                    "reviews as a finding"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Weakening the control's requirement to avoid future findings does not address "
                    "the underlying process failure and undermines the purpose of the control; the correct "
                    "response is remediation, not lowering the bar."
                ),
            },
        ],
        "explanation": (
            "Audit findings of material non-compliance should be documented, root-caused, and remediated "
            "through a tracked corrective action plan with follow-up verification -- not dismissed, acted "
            "on unilaterally by auditors, or resolved by weakening the underlying control requirement."
        ),
    },
    {
        "id": "nd5f-034",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "A maritime shipping company's quarterly operations report contains a 'Public' section "
            "summarizing industry-wide shipping volume trends and a 'Confidential' section listing the "
            "real-time GPS coordinates and cargo manifests of the company's active vessels. If the report "
            "is distributed as a single combined document, at what classification level should the ENTIRE "
            "document be labeled and handled?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Confidential, matching the highest sensitivity level of any section contained within "
                    "the combined document"
                ),
                "correct": True,
                "rationale": (
                    "Correct. When sections of differing sensitivity are combined into a single document, "
                    "standard classification practice is to label and handle the entire document at the "
                    "highest classification level present, since the most sensitive content dictates the "
                    "required protection."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Public, since the majority of readers will only be interested in the industry-wide "
                    "trend data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classifying the whole document at the lowest level ignores the presence of "
                    "real-time vessel GPS coordinates and cargo manifests, exposing genuinely sensitive "
                    "operational data to unauthorized recipients."
                ),
            },
            {
                "id": "c",
                "text": (
                    "An average of the two classification levels, since the document is only partially "
                    "sensitive"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification levels are not numeric values that can be averaged; the "
                    "correct approach is to apply the highest applicable level to the combined document, not "
                    "some blended intermediate label."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Whatever level the document's original author personally prefers, since classification "
                    "is discretionary once a document is drafted"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification follows organizational policy criteria based on content "
                    "sensitivity and impact of disclosure, not an individual author's personal preference."
                ),
            },
        ],
        "explanation": (
            "When content of mixed sensitivity is combined into one document, the entire document must be "
            "classified and handled at the highest sensitivity level present -- here, Confidential, due to "
            "the real-time vessel location and cargo data."
        ),
    },
    {
        "id": "nd5f-035",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data classification levels",
        "stem": (
            "An aerospace manufacturer classified a set of engineering documents 'Restricted' two years ago "
            "because they were subject to an active FAA investigation. The investigation formally closed "
            "one year ago with no further findings, and the company's data classification policy specifies "
            "that documents should be reviewed for declassification once the triggering condition no longer "
            "applies. What should happen to these documents?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The documents should be formally reviewed against current classification criteria now "
                    "that the triggering FAA investigation has closed, and reclassified to a lower level if "
                    "no other justification for 'Restricted' status remains"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification policy ties periodic review to the status of the triggering "
                    "condition; once the investigation that justified 'Restricted' status has closed, the "
                    "documents should be reassessed and declassified if no other sensitivity factor still "
                    "applies."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The documents must remain 'Restricted' permanently, since classification levels can "
                    "never be downgraded once assigned"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification levels are not permanent; documents are commonly reviewed and "
                    "declassified or downgraded once the condition that justified the elevated sensitivity "
                    "no longer applies."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The documents should be immediately destroyed, since 'Restricted' documents cannot be "
                    "retained after their triggering condition ends"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Ending the classification trigger calls for a review and possible "
                    "declassification, not automatic destruction; retention requirements are governed "
                    "separately by records-retention policy, and premature destruction could violate other "
                    "regulatory obligations."
                ),
            },
            {
                "id": "d",
                "text": (
                    "No action is required, since classification reviews are optional and left entirely to "
                    "individual employee discretion"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The scenario states the company's policy specifically requires review once "
                    "the triggering condition no longer applies; this is a defined policy obligation, not an "
                    "optional, individually discretionary action."
                ),
            },
        ],
        "explanation": (
            "Data classification is not static -- documents should be periodically reviewed against current "
            "criteria, and when the original justification for an elevated classification (such as an "
            "active investigation) no longer applies, the document should be reassessed for declassification."
        ),
    },
    {
        "id": "nd5f-036",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data classification levels",
        "stem": (
            "An insurance underwriter emails a proprietary risk-scoring model, labeled 'Restricted' per "
            "company policy, to an external actuarial consultant using unencrypted personal email, bypassing "
            "the corporate DLP gateway that would have blocked or encrypted the transfer. Which statement "
            "BEST characterizes this event?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "It is a policy violation: 'Restricted' data carries the organization's strictest "
                    "handling requirements (e.g., mandatory encryption and approved channels only), and "
                    "sending it via unencrypted personal email bypasses those controls"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Classification levels carry specific mandatory handling requirements; "
                    "'Restricted' data requires the strongest protections (such as encryption and approved "
                    "transfer channels), and using unencrypted personal email to send it outside the "
                    "organization directly violates those requirements."
                ),
            },
            {
                "id": "b",
                "text": (
                    "It is acceptable, since classification labels only apply to data stored at rest and "
                    "impose no requirements once data is being transmitted"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification-driven handling requirements apply across all data states -- "
                    "at rest, in transit, and in use -- not only to data at rest; transmission of "
                    "'Restricted' data still requires the mandated protections."
                ),
            },
            {
                "id": "c",
                "text": (
                    "It is acceptable, since the recipient is a trusted external consultant and trust "
                    "relationships override classification-based handling rules"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Classification handling requirements are based on the sensitivity of the "
                    "data itself, not on subjective trust in the recipient; even a trusted external party "
                    "must receive 'Restricted' data through approved, protected channels."
                ),
            },
            {
                "id": "d",
                "text": (
                    "It is acceptable, since bypassing DLP is only a policy violation if the data is "
                    "subsequently proven to have been intercepted by an attacker"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The violation occurs at the point the mandated handling controls (encryption, "
                    "approved channel) are bypassed, regardless of whether the data is later proven to have "
                    "been intercepted; the policy is preventive, not dependent on proof of actual harm."
                ),
            },
        ],
        "explanation": (
            "Classification levels dictate specific, mandatory handling requirements across all data "
            "states. Sending 'Restricted' data via unencrypted personal email and bypassing DLP controls is "
            "a policy violation regardless of recipient trust or whether interception is later proven."
        ),
    },
    {
        "id": "nd5f-037",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A nonprofit fundraising platform (Company A) decides which donor data fields to collect (name, "
            "donation history, contact preferences) and why (targeted campaign outreach). It integrates a "
            "third-party payment gateway (Company B) that processes donation transactions strictly according "
            "to Company A's written instructions and does not use the donor data for any purpose of its own. "
            "Under standard data-role terminology, what are Company A and Company B, respectively?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Company A is the data controller; Company B is the data processor",
                "correct": True,
                "rationale": (
                    "Correct. Company A determines the purposes and means of processing (what data to "
                    "collect and why), making it the controller; Company B processes data strictly on "
                    "Company A's instructions without its own independent purpose, making it the processor."
                ),
            },
            {
                "id": "b",
                "text": "Company A is the data processor; Company B is the data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. This reverses the roles: the entity that determines the purposes and means "
                    "of processing (Company A) is the controller, while the entity acting strictly on "
                    "another party's instructions (Company B) is the processor."
                ),
            },
            {
                "id": "c",
                "text": "Both companies are joint controllers, since both handle the same donor data",
                "correct": False,
                "rationale": (
                    "Incorrect. Joint controllership requires both parties to jointly determine the purposes "
                    "and means of processing; here, only Company A sets the purposes, while Company B "
                    "merely executes Company A's instructions, which is the defining characteristic of a "
                    "processor, not a joint controller."
                ),
            },
            {
                "id": "d",
                "text": "Company A is the data custodian; Company B is the data owner",
                "correct": False,
                "rationale": (
                    "Incorrect. Custodian and owner describe internal operational/accountability roles for "
                    "implementing safeguards and being accountable for an asset within one organization; the "
                    "relationship described here (deciding purposes vs. processing on instruction) maps to "
                    "controller and processor, not custodian and owner."
                ),
            },
        ],
        "explanation": (
            "The entity that determines the purposes and means of processing personal data is the "
            "controller; an entity that processes data solely on the controller's documented instructions, "
            "without its own independent purpose, is the processor."
        ),
    },
    {
        "id": "nd5f-038",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "For the 'student records' data domain at a university, one team defines field-naming "
            "conventions, data-quality rules, and business definitions (e.g., what qualifies as an "
            "'enrolled' student), and resolves disputes about how the data should be interpreted across "
            "departments. A separate IT team implements the actual access controls, encryption, and backup "
            "schedules for the underlying database. Which role does the FIRST team perform?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data steward",
                "correct": True,
                "rationale": (
                    "Correct. A data steward is responsible for the day-to-day business-level management of "
                    "a data domain -- defining naming conventions, quality rules, and business definitions, "
                    "and resolving interpretation disputes -- as distinct from implementing technical "
                    "safeguards."
                ),
            },
            {
                "id": "b",
                "text": "Data custodian",
                "correct": False,
                "rationale": (
                    "Incorrect. The data custodian is the role responsible for implementing technical "
                    "safeguards such as access controls, encryption, and backups -- that describes the "
                    "SECOND (IT) team in this scenario, not the first."
                ),
            },
            {
                "id": "c",
                "text": "Data processor",
                "correct": False,
                "rationale": (
                    "Incorrect. A data processor handles data on behalf of and per the instructions of a "
                    "controller, typically in a third-party or vendor relationship; this scenario describes "
                    "internal business-level data-quality governance, not third-party processing."
                ),
            },
            {
                "id": "d",
                "text": "Data controller",
                "correct": False,
                "rationale": (
                    "Incorrect. The controller determines the overall purposes and means of processing "
                    "personal data at an organizational level; defining field-level naming conventions and "
                    "quality rules for one data domain is the narrower, operational role of a data steward."
                ),
            },
        ],
        "explanation": (
            "A data steward manages the day-to-day business-level quality, definitions, and usage rules for "
            "a specific data domain, while a data custodian implements the technical safeguards (access "
            "control, encryption, backups) that protect that data."
        ),
    },
    {
        "id": "nd5f-039",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Data roles (controller/processor/custodian)",
        "stem": (
            "A hospital formally designates its Chief Medical Officer (CMO) as accountable for the "
            "electronic health record (EHR) system, including deciding which clinical roles may access "
            "which record fields, while the IT department implements the actual technical access controls "
            "and encryption the CMO approves. Which role does the CMO hold with respect to the EHR system?"
        ),
        "options": [
            {
                "id": "a",
                "text": "Data owner",
                "correct": True,
                "rationale": (
                    "Correct. The data owner is the accountable individual (typically a senior role) who "
                    "makes access-authorization decisions and bears ultimate accountability for an "
                    "information asset -- exactly the CMO's role here with respect to the EHR system."
                ),
            },
            {
                "id": "b",
                "text": "Data custodian",
                "correct": False,
                "rationale": (
                    "Incorrect. The data custodian implements the technical safeguards approved by the "
                    "owner (as the IT department does here); the CMO, who decides access policy, is the "
                    "owner, not the custodian."
                ),
            },
            {
                "id": "c",
                "text": "Data processor",
                "correct": False,
                "rationale": (
                    "Incorrect. A data processor acts on behalf of a controller under contract, typically as "
                    "an external party; the CMO is an internal, accountable decision-maker for the hospital's "
                    "own system, not a third-party processor."
                ),
            },
            {
                "id": "d",
                "text": "Data subject",
                "correct": False,
                "rationale": (
                    "Incorrect. A data subject is the individual to whom personal data relates (i.e., the "
                    "patient); the CMO is exercising an accountability/authorization role over the system, "
                    "not the individual the data is about."
                ),
            },
        ],
        "explanation": (
            "The data owner is accountable for an information asset and makes access-authorization "
            "decisions, while the data custodian implements the technical controls the owner approves. The "
            "CMO's role here -- deciding who may access which fields -- is that of the data owner."
        ),
    },
    {
        "id": "nd5f-040",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A veterinary clinic chain is reassigning a batch of self-encrypting drives (SEDs) that stored "
            "moderately sensitive appointment and billing records from a closing clinic location to a "
            "different clinic within the same organization. Which sanitization approach BEST balances "
            "security and drive reusability for this scenario?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Perform a cryptographic erase (destroying/regenerating the drive's internal encryption "
                    "key) so the previously encrypted data becomes permanently unrecoverable, then reuse the "
                    "drive"
                ),
                "correct": True,
                "rationale": (
                    "Correct. For self-encrypting drives storing moderately sensitive data being reassigned "
                    "internally, cryptographic erase renders the old data unrecoverable almost instantly "
                    "while leaving the physical drive intact and reusable -- an efficient, appropriate "
                    "control for this sensitivity level and internal-reuse purpose."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Physically shred the drives, since any drive that ever stored patient or billing "
                    "records must always be destroyed rather than reused"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Physical destruction is appropriate when a drive is being retired or the "
                    "data is highly sensitive with no reuse need; here, the drives are being reassigned for "
                    "continued internal use, so cryptographic erase is more proportionate and avoids "
                    "unnecessary asset loss."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Perform a quick format of the drive, since a quick format is functionally equivalent to "
                    "a full sanitization for compliance purposes"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A quick format only removes the file system's pointers to data, not the "
                    "underlying data itself, which remains recoverable with common forensic tools; it does "
                    "not meet sanitization requirements for even moderately sensitive records."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Take no sanitization action, since the drives are staying within the same organization "
                    "and therefore never leave the custody of a trusted party"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Reassignment to different staff/locations within the same organization still "
                    "requires sanitization so employees at the new location cannot access the prior "
                    "location's records they are not authorized to see."
                ),
            },
        ],
        "explanation": (
            "For self-encrypting drives being reassigned for continued internal use, cryptographic erase "
            "(key destruction) is an efficient and appropriate sanitization method -- it renders prior data "
            "unrecoverable while preserving the drive for reuse, unlike quick formatting (insufficient) or "
            "physical destruction (unnecessarily wasteful here)."
        ),
    },
    {
        "id": "nd5f-041",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A law firm is returning a leased multifunction scanner/copier to the leasing company at the "
            "end of its contract term. The device's internal hard drive cached digitally scanned copies of "
            "privileged client documents. The leasing company's return instructions do not mention data "
            "sanitization. What should the law firm do BEFORE returning the device?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Sanitize (or remove and separately destroy) the internal hard drive regardless of "
                    "whether the leasing company's instructions mention it, since the firm remains "
                    "responsible for protecting privileged client data residing on its equipment"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Data-owning organizations remain responsible for sanitizing sensitive data on "
                    "any device before it leaves their custody, including leased equipment being returned; "
                    "the absence of a sanitization step in the lessor's return instructions does not remove "
                    "that obligation, especially for privileged legal data."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Return the device as-is, since the leasing company's silence on sanitization means it "
                    "assumes full responsibility for any data remaining on the drive"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Responsibility for protecting an organization's sensitive data does not "
                    "automatically transfer to a lessor simply because the return instructions omit "
                    "sanitization steps; the data owner remains accountable for ensuring sensitive data does "
                    "not leave its custody unprotected."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Physically destroy the entire multifunction device, since leased equipment can never be "
                    "sanitized and returned intact"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Destroying the entire leased device would breach the lease agreement and is "
                    "unnecessary; the internal hard drive can be sanitized (or removed and destroyed "
                    "separately, with an equivalent replacement provided if required) while the rest of the "
                    "device is returned intact."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Do nothing, since copier/scanner internal storage is a marketing myth and these devices "
                    "do not actually retain scanned document data"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Modern multifunction copiers/scanners commonly include internal hard drives "
                    "that cache scanned and printed document images; this is a well-documented, real data "
                    "exposure risk, not a myth, and must be addressed before return."
                ),
            },
        ],
        "explanation": (
            "Organizations remain responsible for sanitizing sensitive data on any device -- including "
            "leased equipment with internal storage such as copier/scanner hard drives -- before it leaves "
            "their custody, regardless of what the lessor's return instructions state."
        ),
    },
    {
        "id": "nd5f-042",
        "domain": 5,
        "objective": "5.1",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Secure asset decommissioning and media sanitization",
        "stem": (
            "A genomics research lab contracts a certified e-waste vendor to physically shred a batch of "
            "decommissioned drives that stored raw sequencing data. The shredding occurs as scheduled, but "
            "the lab's asset inventory is never updated to reflect the drives' disposal, and no certificate "
            "of destruction is requested or retained. What is the BEST corrective action?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Obtain and retain a certificate of destruction from the vendor covering the drives "
                    "already shredded, and update the asset inventory to reflect their disposed status, then "
                    "implement a process requiring both steps for all future decommissioning"
                ),
                "correct": True,
                "rationale": (
                    "Correct. A certificate of destruction provides documented, auditable proof that "
                    "specific assets were properly sanitized, and an updated asset inventory prevents "
                    "decommissioned drives from being mistaken for active, in-use assets; both should be "
                    "obtained retroactively where possible and required going forward."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Take no further action, since the drives were physically shredded and the data is "
                    "already irrecoverable regardless of documentation"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. While the physical destruction may have achieved the sanitization goal, the "
                    "missing documentation and stale asset inventory create an audit and accountability gap "
                    "that must still be remediated, not dismissed as unimportant."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Re-shred a new, different batch of drives so the vendor can issue a fresh certificate of "
                    "destruction covering the incident"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Destroying unrelated drives does nothing to document the disposal of the "
                    "original batch; the correct step is to obtain documentation specifically tied to the "
                    "drives that were already shredded, if the vendor's records can still confirm it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Report the incident as a data breach to regulators, since any missing certificate of "
                    "destruction automatically constitutes unauthorized data disclosure"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. A missing certificate of destruction and stale inventory is a documentation "
                    "and process control gap, not evidence that data was actually disclosed to an "
                    "unauthorized party; treating it as an automatic reportable breach mischaracterizes the "
                    "issue."
                ),
            },
        ],
        "explanation": (
            "Proper decommissioning requires both the sanitization/destruction action itself AND supporting "
            "documentation -- a certificate of destruction and an updated asset inventory -- to provide "
            "auditable proof and prevent tracking gaps, even when physical destruction has already occurred."
        ),
    },
    {
        "id": "nd5f-043",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "A hospital's accounts-payable department has been targeted three times in the past year by "
            "business email compromise (BEC) attempts impersonating vendors and requesting changes to "
            "payment banking details. Staff in that department currently complete the same generic annual "
            "security awareness training as every other employee, covering broad topics like phishing "
            "recognition and password hygiene. What is the BEST recommendation to reduce this department's "
            "risk?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Supplement the generic annual training with role-specific training focused on BEC "
                    "indicators and a mandatory out-of-band verification procedure for any request to change "
                    "vendor payment details"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Generic, one-size-fits-all training does not address the specific, "
                    "high-frequency threat this department actually faces; targeted, role-specific training "
                    "combined with a concrete verification procedure directly reduces the risk of successful "
                    "BEC-driven fraudulent payments."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Conclude that no additional action is needed, since the department already completes "
                    "the same mandatory annual training as the rest of the organization"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Three real BEC attempts against the same department demonstrate that the "
                    "generic training is not adequately addressing this department's specific, elevated "
                    "risk; more action is clearly warranted."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Remove accounts-payable staff from all future security awareness training, since they "
                    "have already completed the mandatory annual module"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Completing baseline annual training does not mean additional, targeted "
                    "training is unnecessary; removing this high-risk department from further training "
                    "moves in exactly the wrong direction."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Block all external email to the accounts-payable department entirely, eliminating the "
                    "need for any additional training"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Blocking all external email would prevent the department from communicating "
                    "with legitimate vendors and is operationally impractical; targeted awareness training "
                    "and a verification procedure address the risk without breaking legitimate business "
                    "processes."
                ),
            },
        ],
        "explanation": (
            "Security awareness training should be tailored to the specific, demonstrated risks a role or "
            "department faces. A department repeatedly targeted by BEC needs role-specific training and "
            "concrete verification procedures, not just generic annual modules."
        ),
    },
    {
        "id": "nd5f-044",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "medium",
        "study_topic": "Security awareness training",
        "stem": (
            "After each simulated phishing test, a call-center company's operations manager sends a "
            "company-wide email publicly naming every employee who clicked the simulated link, along with "
            "sarcastic commentary. Reported click-through rates have not improved, and the security team "
            "later learns that real phishing reports to the security mailbox have also declined. What is "
            "the BEST corrective action?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "Replace the public shaming approach with private, constructive coaching for employees "
                    "who click, paired with positive recognition for employees who report suspicious emails, "
                    "to rebuild a psychologically safe reporting culture"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Public shaming discourages employees from reporting mistakes (including real "
                    "phishing emails they may have clicked), which explains the drop in real-phishing "
                    "reports; replacing it with private coaching and positive reinforcement for reporting "
                    "rebuilds the psychological safety needed for an effective awareness culture."
                ),
            },
            {
                "id": "b",
                "text": (
                    "Increase the frequency of public shaming emails, since employees clearly are not "
                    "sufficiently motivated by the current approach"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Increasing punitive public shaming is likely to further suppress honest "
                    "reporting of real incidents (as already observed), making the security posture worse, "
                    "not better."
                ),
            },
            {
                "id": "c",
                "text": (
                    "Discontinue phishing simulations entirely, since click rates have not improved and the "
                    "exercise is therefore proven ineffective"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The simulations are not inherently ineffective; the punitive delivery method "
                    "(public shaming) is the problem. Ending simulations entirely would remove a valuable "
                    "training and measurement tool rather than fixing the flawed approach to using it."
                ),
            },
            {
                "id": "d",
                "text": (
                    "Terminate the employment of any staff member who clicks a simulated phishing link three "
                    "or more times"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Punitive termination policies for simulation clicks are disproportionate and "
                    "would further erode trust and honest reporting, worsening the exact problem (declining "
                    "real-phishing reports) already observed."
                ),
            },
        ],
        "explanation": (
            "Punitive, public shaming after phishing simulations discourages honest reporting of real "
            "incidents. The best fix replaces shaming with private coaching and positive reinforcement for "
            "reporting, preserving both the training value of simulations and a healthy reporting culture."
        ),
    },
    {
        "id": "nd5f-045",
        "domain": 5,
        "objective": "5.5",
        "type": "multiple_choice",
        "difficulty": "hard",
        "study_topic": "Security awareness training",
        "stem": (
            "A security team wants to determine whether its security awareness program is producing genuine "
            "behavior change rather than just compliance with a training requirement. Which metric BEST "
            "supports this evaluation?"
        ),
        "options": [
            {
                "id": "a",
                "text": (
                    "The rate at which employees proactively report real, unsimulated suspicious emails to "
                    "the security team, and the median time it takes them to do so"
                ),
                "correct": True,
                "rationale": (
                    "Correct. Proactive reporting of real suspicious emails, and how quickly it happens, "
                    "reflects employees actually applying what they learned in real situations -- a genuine "
                    "behavior-change indicator, unlike passive completion metrics."
                ),
            },
            {
                "id": "b",
                "text": (
                    "The percentage of employees who completed the mandatory annual training module by its "
                    "deadline"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Training completion only shows that employees clicked through required "
                    "content; it says nothing about whether they retained the material or changed their "
                    "actual behavior when facing a real threat."
                ),
            },
            {
                "id": "c",
                "text": (
                    "The total number of security awareness training modules published by the security team "
                    "during the year"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. The volume of training content produced is an output metric describing "
                    "program activity, not an outcome metric measuring whether employee behavior actually "
                    "changed."
                ),
            },
            {
                "id": "d",
                "text": (
                    "The average quiz score employees achieved immediately after finishing each training "
                    "module"
                ),
                "correct": False,
                "rationale": (
                    "Incorrect. Immediate post-training quiz scores primarily measure short-term recall of "
                    "material just presented, not sustained, real-world behavior change demonstrated over "
                    "time in genuine situations."
                ),
            },
        ],
        "explanation": (
            "Genuine behavior change is best measured through real-world outcome metrics -- such as the rate "
            "and speed of employees reporting actual suspicious emails -- rather than output or completion "
            "metrics like training completion rates, content volume, or immediate quiz scores."
        ),
    },
]
